import CryptoKit
import UIKit
import WebKit

struct ConversationSummary {
    let id: String
    let title: String
    let updateTime: TimeInterval?
}

struct ConversationMessage {
    enum Role: String {
        case user
        case assistant
    }

    let id: String
    let role: Role
    let text: String
    let createTime: TimeInterval?
}

struct ConversationDetail {
    let id: String
    let title: String
    let currentNodeID: String
    let messages: [ConversationMessage]
}

enum ConversationRepositoryError: LocalizedError {
    case authenticationNotAvailable
    case missingTransientSession
    case invalidResponse
    case httpStatus(Int)
    case invalidPayload
    case missingCurrentNode
    case conversationIdentityMismatch
    case accountContextChanged
    case operationSuperseded

    var errorDescription: String? {
        switch self {
        case .authenticationNotAvailable: return "当前登录会话不可用，请先完成登录或账户验证。"
        case .missingTransientSession: return "未建立可用的原生读取会话。"
        case .invalidResponse: return "服务器返回了无法识别的响应。"
        case .httpStatus(let status): return "服务器请求失败（HTTP \(status)）。"
        case .invalidPayload: return "会话数据格式不完整。"
        case .missingCurrentNode: return "会话缺少当前消息分支。"
        case .conversationIdentityMismatch: return "返回的会话身份与请求目标不一致。"
        case .accountContextChanged: return "账户上下文已变化，请重新选择会话。"
        case .operationSuperseded: return "请求已由较新的操作替换。"
        }
    }
}

enum ConversationDetailOperationKind: String {
    case load
    case sync
    case reload
}

struct ConversationDetailOperationSnapshot {
    let generation: Int
    let kind: ConversationDetailOperationKind
}

private struct ConversationAccountScope: Hashable {
    let userID: String
    let accountID: String

    init(_ context: AuthAccountContext) {
        userID = context.userID
        accountID = context.accountID
    }
}

private struct ConversationResidentKey: Hashable {
    let scope: ConversationAccountScope
    let conversationID: String
}

private enum ConversationResidentState {
    case loaded(ConversationDetail)
    case failed(Error)
}

private struct ConversationTransportContext {
    let session: AuthTransientSession
    let scope: ConversationAccountScope
}

private struct ConversationDetailOperation {
    let generation: Int
    let kind: ConversationDetailOperationKind
    let preserveLoadedResidentOnFailure: Bool
    var task: URLSessionDataTask?
    var completions: [(Result<ConversationDetail, Error>) -> Void]
}

final class ConversationRepository {
    private static let listURL: URL = {
        var components = URLComponents(string: "https://chatgpt.com/backend-api/conversations")!
        components.queryItems = [
            URLQueryItem(name: "offset", value: "0"),
            URLQueryItem(name: "limit", value: "28"),
            URLQueryItem(name: "order", value: "updated")
        ]
        return components.url!
    }()

    private let diagnostics = DiagnosticsLogger.shared
    private let authSessionStore = AuthSessionStore.shared
    private var transientSession: AuthTransientSession?
    private var transientSessionScope: ConversationAccountScope?
    private var transientSessionProbeCompletions: [(Result<ConversationTransportContext, Error>) -> Void]?
    private var activeAccountScope: ConversationAccountScope?
    private var residentStates: [ConversationResidentKey: ConversationResidentState] = [:]
    private var detailOperationGenerations: [ConversationResidentKey: Int] = [:]
    private var detailOperations: [ConversationResidentKey: ConversationDetailOperation] = [:]
    private var listOperationGeneration = 0
    private var accountContextObserver: NSObjectProtocol?
    private var memoryWarningObserver: NSObjectProtocol?

    private(set) var conversations: [ConversationSummary] = []
    private(set) var selectedConversationID: String?
    var onAccountScopeReset: (() -> Void)?

    var selectedConversation: ConversationDetail? {
        requireMainThread()
        guard let id = selectedConversationID else { return nil }
        return residentDetail(id: id)
    }

    init() {
        accountContextObserver = NotificationCenter.default.addObserver(forName: AuthSessionStore.accountContextDidChangeNotification, object: authSessionStore, queue: .main) { [weak self] _ in self?.handleAccountContextChange() }
        memoryWarningObserver = NotificationCenter.default.addObserver(forName: UIApplication.didReceiveMemoryWarningNotification, object: nil, queue: .main) { [weak self] _ in self?.handleMemoryWarning() }
    }

    deinit {
        if let accountContextObserver { NotificationCenter.default.removeObserver(accountContextObserver) }
        if let memoryWarningObserver { NotificationCenter.default.removeObserver(memoryWarningObserver) }
        for operation in detailOperations.values { operation.task?.cancel() }
        transientSession?.finishTasksAndInvalidate()
    }

    func selectConversation(id: String) {
        requireMainThread()
        let previousID = selectedConversationID
        selectedConversationID = id
        if previousID != id {
            var fields = diagnosticsFields(for: id)
            fields["previousConversationHash"] = previousID.map(Self.shortHash) ?? "none"
            fields["activeOperationCount"] = String(detailOperations.count)
            diagnostics.info(category: "navigation", name: "conversation.selectionChanged", fields: fields)
        }
        guard let key = residentKey(for: id), let state = residentStates[key] else {
            diagnostics.info(category: "conversation", name: "resident.miss", fields: residentDiagnosticsFields(for: id))
            return
        }
        var fields = residentDiagnosticsFields(for: id)
        fields["state"] = Self.residentStateName(state)
        diagnostics.info(category: "conversation", name: "resident.hit", fields: fields)
    }

    func diagnosticsFields(for id: String) -> [String: String] {
        requireMainThread()
        var fields = ["conversationHash": Self.shortHash(id)]
        if let index = conversations.firstIndex(where: { $0.id == id }) { fields["listPosition"] = String(index + 1) }
        return fields
    }

    func residentDiagnosticsFields(for id: String) -> [String: String] {
        requireMainThread()
        var fields = diagnosticsFields(for: id)
        fields["residentCount"] = String(residentStates.count)
        fields["activeOperationCount"] = String(detailOperations.count)
        fields["protectedResidentCount"] = String(protectedResidentKeys().count)
        return fields
    }

    func detailOperationSnapshot(for id: String) -> ConversationDetailOperationSnapshot? {
        requireMainThread()
        guard let key = residentKey(for: id), let operation = detailOperations[key] else { return nil }
        return ConversationDetailOperationSnapshot(generation: operation.generation, kind: operation.kind)
    }

    func loadConversations(completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        requireMainThread()
        listOperationGeneration += 1
        let generation = listOperationGeneration
        let span = diagnostics.startSpan(category: "conversation", name: "listLoad", fields: ["operationGeneration": String(generation)])
        withTransientSession { [weak self] result in
            guard let self else { return }
            self.requireMainThread()
            guard generation == self.listOperationGeneration else {
                span.end(status: "discarded", fields: ["reason": "operation_superseded", "operationGeneration": String(generation)])
                completion(.failure(ConversationRepositoryError.operationSuperseded))
                return
            }
            switch result {
            case .failure(let error):
                span.end(status: "failed", fields: ["stage": "auth", "operationGeneration": String(generation)])
                completion(.failure(error))
            case .success(let context):
                self.requestConversationList(using: context, operationGeneration: generation, span: span, completion: completion)
            }
        }
    }

    func loadSelectedConversation(completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        requireMainThread()
        guard let id = selectedConversationID else {
            completion(.failure(ConversationRepositoryError.invalidPayload))
            return
        }
        loadConversation(id: id, completion: completion)
    }

    func syncLatestMessages(id: String, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        requireMainThread()
        let previous = residentDetail(id: id)
        var fields = diagnosticsFields(for: id)
        fields["previousVisibleMessageCount"] = String(previous?.messages.count ?? 0)
        fields["localStateBefore"] = previous == nil ? "empty" : "loaded"
        let span = diagnostics.startSpan(category: "conversation", name: "latestSync", fields: fields)
        loadConversation(id: id, replacingCurrentRequest: true, operationKind: .sync, preserveLoadedResidentOnFailure: true) { [weak self] result in
            guard let self else { return }
            switch result {
            case .success(let detail):
                var fields = self.recoveryDiffFields(previous: previous, current: detail)
                fields["localStateAfter"] = "server_backed"
                span.end(status: "ok", fields: fields)
                completion(.success(detail))
            case .failure(let error):
                let status = Self.isLifecycleTermination(error) ? "superseded" : "failed"
                span.end(status: status, fields: ["stage": "detailLoad", "localStateAfter": previous == nil ? "failed" : "preserved"])
                completion(.failure(error))
            }
        }
    }

    func reloadConversation(id: String, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        requireMainThread()
        let previous = residentDetail(id: id)
        var fields = diagnosticsFields(for: id)
        fields["previousVisibleMessageCount"] = String(previous?.messages.count ?? 0)
        fields["localStateBefore"] = previous == nil ? "empty_or_failed" : "loaded"
        let span = diagnostics.startSpan(category: "conversation", name: "conversationReload", fields: fields)
        removeResidentState(id: id)
        diagnostics.info(category: "conversation", name: "conversationReload.stateCleared", traceID: span.traceID, fields: diagnosticsFields(for: id))
        loadConversation(id: id, replacingCurrentRequest: true, operationKind: .reload) { [weak self] result in
            guard let self else { return }
            switch result {
            case .success(let detail):
                var fields = self.recoveryDiffFields(previous: previous, current: detail)
                fields["localStateAfter"] = "server_backed"
                span.end(status: "ok", fields: fields)
                completion(.success(detail))
            case .failure(let error):
                let status = Self.isLifecycleTermination(error) ? "superseded" : "failed"
                span.end(status: status, fields: ["stage": "detailLoad", "localStateAfter": "failed"])
                completion(.failure(error))
            }
        }
    }

    func loadConversation(id: String, replacingCurrentRequest: Bool = false, operationKind: ConversationDetailOperationKind = .load, preserveLoadedResidentOnFailure: Bool = false, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        requireMainThread()
        if !replacingCurrentRequest, let key = residentKey(for: id) {
            if appendCompletionIfOperationExists(key: key, id: id, completion: completion) { return }
            if let state = residentStates[key] {
                finishResidentHit(id: id, state: state, completion: completion)
                return
            }
        }

        withTransientSession { [weak self] result in
            guard let self else { return }
            self.requireMainThread()
            switch result {
            case .failure(let error): completion(.failure(error))
            case .success(let context):
                self.beginDetailOperation(id: id, context: context, replacingCurrentRequest: replacingCurrentRequest, operationKind: operationKind, preserveLoadedResidentOnFailure: preserveLoadedResidentOnFailure, completion: completion)
            }
        }
    }

    private func beginDetailOperation(id: String, context: ConversationTransportContext, replacingCurrentRequest: Bool, operationKind: ConversationDetailOperationKind, preserveLoadedResidentOnFailure: Bool, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        requireMainThread()
        guard validateTransportContext(context) else {
            completion(.failure(ConversationRepositoryError.accountContextChanged))
            return
        }
        let key = ConversationResidentKey(scope: context.scope, conversationID: id)
        if !replacingCurrentRequest {
            if appendCompletionIfOperationExists(key: key, id: id, completion: completion) { return }
            if let state = residentStates[key] {
                finishResidentHit(id: id, state: state, completion: completion)
                return
            }
        }

        let operationGeneration = (detailOperationGenerations[key] ?? 0) + 1
        detailOperationGenerations[key] = operationGeneration
        let replacedOperation = replacingCurrentRequest ? detailOperations.removeValue(forKey: key) : nil
        detailOperations[key] = ConversationDetailOperation(generation: operationGeneration, kind: operationKind, preserveLoadedResidentOnFailure: preserveLoadedResidentOnFailure, task: nil, completions: [completion])
        let replacedCompletions = replacedOperation.map { cancelReplacedOperation($0, key: key, replacementOperationGeneration: operationGeneration) } ?? []

        var fields = residentDiagnosticsFields(for: id)
        fields["operationGeneration"] = String(operationGeneration)
        fields["operationKind"] = operationKind.rawValue
        let span = diagnostics.startSpan(category: "conversation", name: "detailLoad", fields: fields)
        requestConversationDetail(key: key, operationGeneration: operationGeneration, using: context, span: span)
        for replacedCompletion in replacedCompletions { replacedCompletion(.failure(ConversationRepositoryError.operationSuperseded)) }
    }

    private func finishResidentHit(id: String, state: ConversationResidentState, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        var fields = residentDiagnosticsFields(for: id)
        fields["state"] = Self.residentStateName(state)
        diagnostics.info(category: "conversation", name: "resident.hit", fields: fields)
        switch state {
        case .loaded(let detail): completion(.success(detail))
        case .failed(let error): completion(.failure(error))
        }
    }

    private func appendCompletionIfOperationExists(key: ConversationResidentKey, id: String, completion: @escaping (Result<ConversationDetail, Error>) -> Void) -> Bool {
        guard var operation = detailOperations[key] else { return false }
        operation.completions.append(completion)
        detailOperations[key] = operation
        var fields = residentDiagnosticsFields(for: id)
        fields["operationGeneration"] = String(operation.generation)
        fields["operationKind"] = operation.kind.rawValue
        fields["completionCount"] = String(operation.completions.count)
        diagnostics.info(category: "conversation", name: "detail.coalesced", fields: fields)
        return true
    }

    private func withTransientSession(completion: @escaping (Result<ConversationTransportContext, Error>) -> Void) {
        requireMainThread()
        if let transientSession, let transientSessionScope {
            if let verifiedContext = authSessionStore.verifiedAccountContext() {
                let verifiedScope = ConversationAccountScope(verifiedContext)
                bindVerifiedAccountScope(verifiedScope)
                if verifiedScope == transientSessionScope, activeAccountScope == verifiedScope {
                    completion(.success(ConversationTransportContext(session: transientSession, scope: transientSessionScope)))
                    return
                }
                transientSession.invalidateAndCancel()
                self.transientSession = nil
                self.transientSessionScope = nil
            } else if activeAccountScope == transientSessionScope {
                completion(.success(ConversationTransportContext(session: transientSession, scope: transientSessionScope)))
                return
            }
        }
        if transientSessionProbeCompletions != nil {
            transientSessionProbeCompletions?.append(completion)
            diagnostics.info(category: "conversation", name: "authContext.coalesced", fields: ["completionCount": String(transientSessionProbeCompletions?.count ?? 0)])
            return
        }

        transientSessionProbeCompletions = [completion]
        diagnostics.info(category: "conversation", name: "authContext.requested")
        let cookieStore = WKWebsiteDataStore.default().httpCookieStore
        authSessionStore.probeAccountContext(using: cookieStore, createTransientSession: true) { [weak self] state, session in
            guard let self else {
                session?.finishTasksAndInvalidate()
                return
            }
            guard state == .verified, let session, let returnedContext = self.authSessionStore.verifiedAccountContext() else {
                session?.finishTasksAndInvalidate()
                DispatchQueue.main.async { self.finishTransientSessionProbe(.failure(ConversationRepositoryError.authenticationNotAvailable)) }
                return
            }
            let returnedScope = ConversationAccountScope(returnedContext)
            DispatchQueue.main.async {
                self.requireMainThread()
                guard let currentContext = self.authSessionStore.verifiedAccountContext(), ConversationAccountScope(currentContext) == returnedScope else {
                    session.invalidateAndCancel()
                    self.finishTransientSessionProbe(.failure(ConversationRepositoryError.accountContextChanged))
                    return
                }
                self.bindVerifiedAccountScope(returnedScope)
                guard self.activeAccountScope == returnedScope else {
                    session.invalidateAndCancel()
                    self.finishTransientSessionProbe(.failure(ConversationRepositoryError.accountContextChanged))
                    return
                }
                self.transientSession = session
                self.transientSessionScope = returnedScope
                self.finishTransientSessionProbe(.success(ConversationTransportContext(session: session, scope: returnedScope)))
            }
        }
    }

    private func finishTransientSessionProbe(_ result: Result<ConversationTransportContext, Error>) {
        requireMainThread()
        let completions = transientSessionProbeCompletions ?? []
        transientSessionProbeCompletions = nil
        for completion in completions { completion(result) }
    }

    private func requestConversationList(using context: ConversationTransportContext, operationGeneration: Int, span: DiagnosticsSpan, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        requireMainThread()
        let requestFields = ["method": "GET", "route": "conversation_list", "offset": "0", "limit": "28", "order": "updated", "operationGeneration": String(operationGeneration)]
        diagnostics.info(category: "conversation", name: "list.request", traceID: span.traceID, fields: requestFields)
        var request = URLRequest(url: Self.listURL)
        request.httpMethod = "GET"
        context.session.dataTask(with: request) { [weak self] data, response, error in
            guard let self else { return }
            if let error {
                self.diagnostics.error(category: "conversation", name: "list.failed", traceID: span.traceID, error: error)
                self.finishListOperation(context: context, operationGeneration: operationGeneration, span: span, statusFields: ["stage": "network"], result: .failure(error), completion: completion)
                return
            }
            guard let response = response as? HTTPURLResponse, let data else {
                self.finishListOperation(context: context, operationGeneration: operationGeneration, span: span, statusFields: ["stage": "response", "reason": "non_http_response"], result: .failure(ConversationRepositoryError.invalidResponse), completion: completion)
                return
            }
            guard (200..<300).contains(response.statusCode) else {
                self.finishListOperation(context: context, operationGeneration: operationGeneration, span: span, statusFields: ["stage": "response", "httpStatus": String(response.statusCode)], result: .failure(ConversationRepositoryError.httpStatus(response.statusCode)), completion: completion)
                return
            }
            guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let rawItems = payload["items"] as? [[String: Any]] else {
                self.finishListOperation(context: context, operationGeneration: operationGeneration, span: span, statusFields: ["stage": "parse", "reason": "missing_items"], result: .failure(ConversationRepositoryError.invalidPayload), completion: completion)
                return
            }
            let items = rawItems.compactMap(Self.parseConversationSummary)
            var fields = ["httpStatus": String(response.statusCode), "byteCount": String(data.count), "itemCount": String(items.count), "operationGeneration": String(operationGeneration)]
            if let total = payload["total"] as? NSNumber { fields["totalCount"] = total.stringValue }
            self.finishListOperation(context: context, operationGeneration: operationGeneration, span: span, statusFields: fields, result: .success(items), completion: completion)
        }
    }

    private func finishListOperation(context: ConversationTransportContext, operationGeneration: Int, span: DiagnosticsSpan, statusFields: [String: String], result: Result<[ConversationSummary], Error>, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        DispatchQueue.main.async {
            self.requireMainThread()
            guard self.activeAccountScope == context.scope else {
                var fields = statusFields
                fields["reason"] = "account_changed"
                span.end(status: "discarded", fields: fields)
                completion(.failure(ConversationRepositoryError.accountContextChanged))
                return
            }
            guard self.listOperationGeneration == operationGeneration else {
                var fields = statusFields
                fields["reason"] = "operation_superseded"
                span.end(status: "discarded", fields: fields)
                completion(.failure(ConversationRepositoryError.operationSuperseded))
                return
            }
            switch result {
            case .success(let items):
                self.conversations = items
                self.diagnostics.info(category: "conversation", name: "list.response", traceID: span.traceID, fields: statusFields)
                span.end(status: "ok", fields: statusFields)
                completion(.success(items))
            case .failure(let error):
                span.end(status: "failed", fields: statusFields)
                completion(.failure(error))
            }
        }
    }

    private func requestConversationDetail(key: ConversationResidentKey, operationGeneration: Int, using context: ConversationTransportContext, span: DiagnosticsSpan) {
        requireMainThread()
        let id = key.conversationID
        let detailURL = URL(string: "https://chatgpt.com/backend-api/conversation")!.appendingPathComponent(id)
        var requestFields = diagnosticsFields(for: id)
        requestFields["method"] = "GET"
        requestFields["route"] = "conversation_detail"
        requestFields["operationGeneration"] = String(operationGeneration)
        if let operation = detailOperations[key] { requestFields["operationKind"] = operation.kind.rawValue }
        diagnostics.info(category: "conversation", name: "detail.request", traceID: span.traceID, fields: requestFields)
        var request = URLRequest(url: detailURL)
        request.httpMethod = "GET"
        let callbackFields = requestFields
        let task = context.session.dataTask(with: request) { [weak self] data, response, error in
            guard let self else { return }
            if let error {
                let nsError = error as NSError
                if nsError.domain == NSURLErrorDomain && nsError.code == NSURLErrorCancelled {
                    self.diagnostics.info(category: "conversation", name: "detail.cancelled", traceID: span.traceID, fields: callbackFields)
                    span.end(status: "cancelled", fields: callbackFields)
                    return
                }
                self.diagnostics.error(category: "conversation", name: "detail.failed", traceID: span.traceID, error: error, fields: callbackFields)
                span.end(status: "failed", fields: ["stage": "network"])
                self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .failure(error))
                return
            }
            guard let response = response as? HTTPURLResponse, let data else {
                span.end(status: "failed", fields: ["stage": "response", "reason": "non_http_response"])
                self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .failure(ConversationRepositoryError.invalidResponse))
                return
            }
            guard (200..<300).contains(response.statusCode) else {
                span.end(status: "failed", fields: ["stage": "response", "httpStatus": String(response.statusCode)])
                self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .failure(ConversationRepositoryError.httpStatus(response.statusCode)))
                return
            }
            guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let mapping = payload["mapping"] as? [String: Any], let currentNode = payload["current_node"] as? String, !currentNode.isEmpty else {
                span.end(status: "failed", fields: ["stage": "parse", "reason": "missing_mapping_or_current_node"])
                self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .failure(ConversationRepositoryError.missingCurrentNode))
                return
            }
            if let returnedID = payload["conversation_id"] as? String, !returnedID.isEmpty, returnedID != id {
                span.end(status: "failed", fields: ["stage": "identity", "reason": "conversation_identity_mismatch"])
                self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .failure(ConversationRepositoryError.conversationIdentityMismatch))
                return
            }

            let messages = Self.parseCurrentBranch(mapping: mapping, currentNode: currentNode)
            let title = Self.normalizedTitle(payload["title"] as? String)
            let detail = ConversationDetail(id: id, title: title, currentNodeID: currentNode, messages: messages)
            var fields = callbackFields
            fields["httpStatus"] = String(response.statusCode)
            fields["byteCount"] = String(data.count)
            fields["mappingCount"] = String(mapping.count)
            fields["visibleMessageCount"] = String(messages.count)
            self.diagnostics.info(category: "conversation", name: "detail.response", traceID: span.traceID, fields: fields)
            span.end(status: "ok", fields: fields)
            self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .success(detail))
        }
        guard var operation = detailOperations[key], operation.generation == operationGeneration else {
            task.cancel()
            return
        }
        operation.task = task
        detailOperations[key] = operation
    }

    private func cancelReplacedOperation(_ operation: ConversationDetailOperation, key: ConversationResidentKey, replacementOperationGeneration: Int) -> [(Result<ConversationDetail, Error>) -> Void] {
        var fields = diagnosticsFields(for: key.conversationID)
        fields["cancelledOperationGeneration"] = String(operation.generation)
        fields["replacementOperationGeneration"] = String(replacementOperationGeneration)
        fields["cancelledOperationKind"] = operation.kind.rawValue
        fields["taskPresent"] = operation.task == nil ? "false" : "true"
        diagnostics.info(category: "conversation", name: "detail.cancel.requested", fields: fields)
        operation.task?.cancel()
        return operation.completions
    }

    private func finishDetailOperation(key: ConversationResidentKey, operationGeneration: Int, result: Result<ConversationDetail, Error>) {
        DispatchQueue.main.async {
            self.requireMainThread()
            guard self.activeAccountScope == key.scope else {
                self.logDiscardedDetail(key: key, operationGeneration: operationGeneration, reason: "account_changed")
                return
            }
            guard let operation = self.detailOperations[key], operation.generation == operationGeneration else {
                self.logDiscardedDetail(key: key, operationGeneration: operationGeneration, reason: "operation_superseded")
                return
            }
            self.detailOperations.removeValue(forKey: key)
            switch result {
            case .success(let detail):
                self.residentStates[key] = .loaded(detail)
                var fields = self.residentDiagnosticsFields(for: key.conversationID)
                fields["residentApproximateTextBytes"] = String(Self.approximateTextBytes(detail))
                fields["residentTotalApproximateTextBytes"] = String(self.residentStates.values.reduce(0) { $0 + Self.approximateTextBytes($1) })
                fields["visibility"] = self.selectedConversationID == key.conversationID ? "foreground" : "hidden"
                fields["state"] = "loaded"
                fields["operationKind"] = operation.kind.rawValue
                self.diagnostics.info(category: "conversation", name: "resident.stored", fields: fields)
            case .failure(let error):
                let hasLoadedResident: Bool
                if let existingState = self.residentStates[key], case .loaded = existingState { hasLoadedResident = true } else { hasLoadedResident = false }
                if !operation.preserveLoadedResidentOnFailure || !hasLoadedResident { self.residentStates[key] = .failed(error) }
                var fields = self.residentDiagnosticsFields(for: key.conversationID)
                fields["state"] = operation.preserveLoadedResidentOnFailure && hasLoadedResident ? "loaded_preserved" : "failed"
                fields["operationKind"] = operation.kind.rawValue
                self.diagnostics.info(category: "conversation", name: "resident.terminal", fields: fields)
            }
            for completion in operation.completions { completion(result) }
        }
    }

    private func logDiscardedDetail(key: ConversationResidentKey, operationGeneration: Int, reason: String) {
        var fields = diagnosticsFields(for: key.conversationID)
        fields["operationGeneration"] = String(operationGeneration)
        fields["currentOperationGeneration"] = String(detailOperationGenerations[key] ?? 0)
        fields["reason"] = reason
        diagnostics.info(category: "conversation", name: "detail.discarded", fields: fields)
    }

    private func validateTransportContext(_ context: ConversationTransportContext) -> Bool {
        requireMainThread()
        if let verifiedContext = authSessionStore.verifiedAccountContext() {
            let verifiedScope = ConversationAccountScope(verifiedContext)
            bindVerifiedAccountScope(verifiedScope)
            return verifiedScope == context.scope && activeAccountScope == context.scope && transientSessionScope == context.scope
        }
        return activeAccountScope == context.scope && transientSessionScope == context.scope
    }

    private func handleAccountContextChange() {
        requireMainThread()
        guard let context = authSessionStore.verifiedAccountContext() else {
            if activeAccountScope != nil { resetAccountScope(to: nil) }
            return
        }
        bindVerifiedAccountScope(ConversationAccountScope(context))
    }

    private func bindVerifiedAccountScope(_ scope: ConversationAccountScope) {
        requireMainThread()
        if let activeAccountScope {
            if activeAccountScope != scope { resetAccountScope(to: scope) }
        } else {
            activeAccountScope = scope
        }
    }

    private func resetAccountScope(to newScope: ConversationAccountScope?) {
        requireMainThread()
        let removedResidentCount = residentStates.count
        let cancelledOperations = Array(detailOperations.values)
        listOperationGeneration += 1
        for operation in cancelledOperations { operation.task?.cancel() }
        detailOperations.removeAll()
        detailOperationGenerations.removeAll()
        residentStates.removeAll()
        conversations = []
        selectedConversationID = nil
        transientSession?.invalidateAndCancel()
        transientSession = nil
        transientSessionScope = nil
        activeAccountScope = newScope
        diagnostics.info(category: "conversation", name: "accountScope.reset", fields: ["residentRemovedCount": String(removedResidentCount), "operationCancelledCount": String(cancelledOperations.count), "nextScopeVerified": newScope == nil ? "false" : "true"])
        onAccountScopeReset?()
        for operation in cancelledOperations {
            for completion in operation.completions { completion(.failure(ConversationRepositoryError.accountContextChanged)) }
        }
    }

    private func handleMemoryWarning() {
        requireMainThread()
        let protectedKeys = protectedResidentKeys()
        let evictedKeys = residentStates.keys.filter { !protectedKeys.contains($0) }
        guard !evictedKeys.isEmpty else {
            diagnostics.warning(category: "conversation", name: "resident.evictionSkipped", fields: ["reason": "memory_warning", "residentCount": String(residentStates.count), "protectedResidentCount": String(protectedKeys.count), "activeOperationCount": String(detailOperations.count)])
            return
        }
        for key in evictedKeys { residentStates.removeValue(forKey: key) }
        diagnostics.warning(category: "conversation", name: "resident.evicted", fields: ["reason": "memory_warning", "evictedCount": String(evictedKeys.count), "residentCount": String(residentStates.count), "protectedResidentCount": String(protectedKeys.count), "activeOperationCount": String(detailOperations.count)])
    }

    private func protectedResidentKeys() -> Set<ConversationResidentKey> {
        requireMainThread()
        var keys = Set(detailOperations.keys)
        if let selectedConversationID, let selectedKey = residentKey(for: selectedConversationID) { keys.insert(selectedKey) }
        return keys.intersection(Set(residentStates.keys))
    }

    private func residentKey(for id: String) -> ConversationResidentKey? {
        requireMainThread()
        guard let activeAccountScope else { return nil }
        return ConversationResidentKey(scope: activeAccountScope, conversationID: id)
    }

    private func residentDetail(id: String) -> ConversationDetail? {
        requireMainThread()
        guard let key = residentKey(for: id), let state = residentStates[key], case .loaded(let detail) = state else { return nil }
        return detail
    }

    private func removeResidentState(id: String) {
        requireMainThread()
        guard let key = residentKey(for: id) else { return }
        residentStates.removeValue(forKey: key)
    }

    private func recoveryDiffFields(previous: ConversationDetail?, current: ConversationDetail) -> [String: String] {
        requireMainThread()
        let previousMessages = previous?.messages ?? []
        var previousByID: [String: ConversationMessage] = [:]
        var currentByID: [String: ConversationMessage] = [:]
        for message in previousMessages { previousByID[message.id] = message }
        for message in current.messages { currentByID[message.id] = message }
        let addedCount = currentByID.keys.reduce(0) { $0 + (previousByID[$1] == nil ? 1 : 0) }
        let removedCount = previousByID.keys.reduce(0) { $0 + (currentByID[$1] == nil ? 1 : 0) }
        let changedCount = current.messages.reduce(0) { count, message in
            guard let old = previousByID[message.id] else { return count }
            return count + ((old.role != message.role || old.text != message.text || old.createTime != message.createTime) ? 1 : 0)
        }
        return ["previousVisibleMessageCount": String(previousMessages.count), "currentVisibleMessageCount": String(current.messages.count), "addedVisibleMessageCount": String(addedCount), "removedVisibleMessageCount": String(removedCount), "changedVisibleMessageCount": String(changedCount)]
    }

    private func requireMainThread() { precondition(Thread.isMainThread, "ConversationRepository mutable state must stay on main thread") }

    private static func parseConversationSummary(_ item: [String: Any]) -> ConversationSummary? {
        guard let id = item["id"] as? String, !id.isEmpty else { return nil }
        return ConversationSummary(id: id, title: normalizedTitle(item["title"] as? String), updateTime: (item["update_time"] as? NSNumber)?.doubleValue)
    }

    private static func normalizedTitle(_ title: String?) -> String {
        let trimmed = title?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
        return trimmed.isEmpty ? "未命名会话" : trimmed
    }

    private static func shortHash(_ value: String) -> String { "sha256:" + SHA256.hash(data: Data(value.utf8)).prefix(6).map { String(format: "%02x", $0) }.joined() }

    private static func residentStateName(_ state: ConversationResidentState) -> String {
        switch state {
        case .loaded: return "loaded"
        case .failed: return "failed"
        }
    }

    private static func approximateTextBytes(_ detail: ConversationDetail) -> Int { detail.messages.reduce(0) { $0 + $1.text.utf8.count } }

    private static func approximateTextBytes(_ state: ConversationResidentState) -> Int {
        if case .loaded(let detail) = state { return approximateTextBytes(detail) }
        return 0
    }

    static func isLifecycleTermination(_ error: Error) -> Bool {
        guard let repositoryError = error as? ConversationRepositoryError else { return false }
        switch repositoryError {
        case .accountContextChanged, .operationSuperseded: return true
        default: return false
        }
    }

    private static func parseCurrentBranch(mapping: [String: Any], currentNode: String) -> [ConversationMessage] {
        var nodeIDs: [String] = []
        var visited = Set<String>()
        var nodeID: String? = currentNode
        while let currentID = nodeID, !currentID.isEmpty, visited.insert(currentID).inserted {
            nodeIDs.append(currentID)
            guard let node = mapping[currentID] as? [String: Any] else { break }
            nodeID = node["parent"] as? String
        }

        var messages: [ConversationMessage] = []
        for id in nodeIDs.reversed() {
            guard let node = mapping[id] as? [String: Any], let message = node["message"] as? [String: Any], let author = message["author"] as? [String: Any], let rawRole = author["role"] as? String, let role = ConversationMessage.Role(rawValue: rawRole), let content = message["content"] as? [String: Any] else { continue }
            let text = visibleText(from: content)
            guard !text.isEmpty else { continue }
            let messageID = (message["id"] as? String).flatMap { $0.isEmpty ? nil : $0 } ?? id
            messages.append(ConversationMessage(id: messageID, role: role, text: text, createTime: (message["create_time"] as? NSNumber)?.doubleValue))
        }
        return messages
    }

    private static func visibleText(from content: [String: Any]) -> String {
        var textParts: [String] = []
        if let text = content["text"] as? String, !text.isEmpty { textParts.append(text) }
        if let parts = content["parts"] as? [Any] {
            for part in parts {
                if let text = part as? String, !text.isEmpty { textParts.append(text) }
                else if let object = part as? [String: Any], let text = object["text"] as? String, !text.isEmpty { textParts.append(text) }
            }
        }
        return textParts.joined(separator: "\n").trimmingCharacters(in: .whitespacesAndNewlines)
    }
}

final class ConversationSidebarViewController: UITableViewController {
    var onSelectConversation: ((String) -> Void)?

    private let repository: ConversationRepository
    private let diagnostics = DiagnosticsLogger.shared
    private var loading = false
    private var loadPresentationGeneration = 0
    private var errorView: UIView?

    init(repository: ConversationRepository) {
        self.repository = repository
        super.init(style: .plain)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "ChatGPT"
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "ConversationCell")
        tableView.rowHeight = 58
        navigationItem.leftBarButtonItem = UIBarButtonItem(title: "设置", style: .plain, target: self, action: #selector(openSettings))
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadConversations))
        refreshControl = UIRefreshControl()
        refreshControl?.addTarget(self, action: #selector(reloadConversations), for: .valueChanged)
        loadConversations()
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int { repository.conversations.count }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let item = repository.conversations[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "ConversationCell", for: indexPath)
        cell.textLabel?.text = item.title
        cell.textLabel?.font = .preferredFont(forTextStyle: .body)
        cell.textLabel?.numberOfLines = 2
        cell.accessoryType = repository.selectedConversationID == item.id ? .checkmark : .none
        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        onSelectConversation?(repository.conversations[indexPath.row].id)
        tableView.reloadData()
    }

    func resetForAccountScopeChange() {
        loadPresentationGeneration += 1
        loading = false
        refreshControl?.endRefreshing()
        navigationItem.rightBarButtonItem?.isEnabled = true
        errorView?.removeFromSuperview()
        errorView = nil
        tableView.reloadData()
    }

    @objc private func reloadConversations() { loadConversations() }

    private func loadConversations() {
        guard !loading else { return }
        loading = true
        loadPresentationGeneration += 1
        let presentationGeneration = loadPresentationGeneration
        errorView?.removeFromSuperview()
        errorView = nil
        navigationItem.rightBarButtonItem?.isEnabled = false
        repository.loadConversations { [weak self] result in
            guard let self, self.loadPresentationGeneration == presentationGeneration else { return }
            self.loading = false
            self.refreshControl?.endRefreshing()
            self.navigationItem.rightBarButtonItem?.isEnabled = true
            switch result {
            case .success: self.tableView.reloadData()
            case .failure(let error):
                guard !ConversationRepository.isLifecycleTermination(error) else { return }
                self.showError(error)
            }
        }
    }

    private func showError(_ error: Error) {
        let label = UILabel()
        label.font = .preferredFont(forTextStyle: .body)
        label.textColor = .secondaryLabel
        label.textAlignment = .center
        label.numberOfLines = 0
        label.text = error.localizedDescription

        let retryButton = UIButton(type: .system)
        retryButton.setTitle("重新加载", for: .normal)
        retryButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
        retryButton.addTarget(self, action: #selector(reloadConversations), for: .touchUpInside)

        let loginButton = UIButton(type: .system)
        loginButton.setTitle("登录 / 账户验证", for: .normal)
        loginButton.addTarget(self, action: #selector(openLogin), for: .touchUpInside)

        let stack = UIStackView(arrangedSubviews: [label, retryButton, loginButton])
        stack.axis = .vertical
        stack.alignment = .center
        stack.spacing = 12
        stack.translatesAutoresizingMaskIntoConstraints = false
        tableView.addSubview(stack)
        NSLayoutConstraint.activate([
            stack.centerXAnchor.constraint(equalTo: tableView.frameLayoutGuide.centerXAnchor),
            stack.centerYAnchor.constraint(equalTo: tableView.frameLayoutGuide.centerYAnchor),
            stack.widthAnchor.constraint(lessThanOrEqualTo: tableView.frameLayoutGuide.widthAnchor, multiplier: 0.8)
        ])
        errorView = stack
    }

    @objc private func openLogin() {
        diagnostics.info(category: "navigation", name: "nativeRead.login.open")
        navigationController?.pushViewController(AuthWebViewController(mode: .authentication), animated: true)
    }

    @objc private func openSettings() {
        diagnostics.info(category: "navigation", name: "settings.open")
        navigationController?.pushViewController(SettingsViewController(), animated: true)
    }
}

final class ConversationDetailViewController: UIViewController, UITableViewDataSource {
    private let repository: ConversationRepository
    private let diagnostics = DiagnosticsLogger.shared
    private let tableView = UITableView(frame: .zero, style: .plain)
    private let activityIndicator = UIActivityIndicatorView(style: .medium)
    private let stateLabel = UILabel()
    private let retryButton = UIButton(type: .system)
    private let syncToastView = UIView()
    private let syncToastLabel = UILabel()
    private var syncToastHideWorkItem: DispatchWorkItem?
    private var messages: [ConversationMessage] = []
    private var loadingConversationID: String?
    private var presentationGeneration = 0

    init(repository: ConversationRepository) {
        self.repository = repository
        super.init(nibName: nil, bundle: nil)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        title = "新对话"

        tableView.dataSource = self
        tableView.separatorStyle = .none
        tableView.keyboardDismissMode = .interactive
        tableView.rowHeight = UITableView.automaticDimension
        tableView.estimatedRowHeight = 96
        tableView.register(ConversationMessageCell.self, forCellReuseIdentifier: ConversationMessageCell.reuseIdentifier)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(tableView)

        stateLabel.font = .preferredFont(forTextStyle: .body)
        stateLabel.textColor = .secondaryLabel
        stateLabel.textAlignment = .center
        stateLabel.numberOfLines = 0
        stateLabel.text = "从侧边栏选择一个会话"
        stateLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(stateLabel)

        retryButton.setTitle("重新加载", for: .normal)
        retryButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
        retryButton.addTarget(self, action: #selector(reloadCurrentConversation), for: .touchUpInside)
        retryButton.isHidden = true
        retryButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(retryButton)

        activityIndicator.hidesWhenStopped = true
        activityIndicator.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(activityIndicator)

        syncToastView.backgroundColor = UIColor.black.withAlphaComponent(0.78)
        syncToastView.layer.cornerRadius = 12
        syncToastView.isHidden = true
        syncToastView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(syncToastView)
        syncToastLabel.font = .preferredFont(forTextStyle: .headline)
        syncToastLabel.textColor = .white
        syncToastLabel.textAlignment = .center
        syncToastLabel.numberOfLines = 0
        syncToastLabel.translatesAutoresizingMaskIntoConstraints = false
        syncToastView.addSubview(syncToastLabel)

        NSLayoutConstraint.activate([
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            tableView.topAnchor.constraint(equalTo: view.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            stateLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            stateLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            stateLabel.leadingAnchor.constraint(greaterThanOrEqualTo: view.leadingAnchor, constant: 24),
            stateLabel.trailingAnchor.constraint(lessThanOrEqualTo: view.trailingAnchor, constant: -24),
            retryButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            retryButton.topAnchor.constraint(equalTo: stateLabel.bottomAnchor, constant: 14),
            activityIndicator.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicator.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -36),
            syncToastView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            syncToastView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            syncToastView.leadingAnchor.constraint(greaterThanOrEqualTo: view.leadingAnchor, constant: 36),
            syncToastView.trailingAnchor.constraint(lessThanOrEqualTo: view.trailingAnchor, constant: -36),
            syncToastLabel.leadingAnchor.constraint(equalTo: syncToastView.leadingAnchor, constant: 18),
            syncToastLabel.trailingAnchor.constraint(equalTo: syncToastView.trailingAnchor, constant: -18),
            syncToastLabel.topAnchor.constraint(equalTo: syncToastView.topAnchor, constant: 12),
            syncToastLabel.bottomAnchor.constraint(equalTo: syncToastView.bottomAnchor, constant: -12)
        ])
        updateConversationMenu()
    }

    func showConversation(id: String) {
        guard repository.selectedConversationID == id else { return }
        presentationGeneration += 1
        let currentPresentationGeneration = presentationGeneration
        let presentationStart = ProcessInfo.processInfo.systemUptime
        let operationSnapshot = repository.detailOperationSnapshot(for: id)
        let existingDetail = repository.selectedConversation
        let previousMessages = existingDetail?.messages ?? []
        hideSyncToast()

        if let detail = existingDetail {
            loadingConversationID = operationSnapshot == nil ? nil : id
            activityIndicator.stopAnimating()
            apply(detail)
            logResidentFirstVisible(id: id, startedAt: presentationStart, operationKind: operationSnapshot?.kind)
        } else {
            loadingConversationID = id
            messages = []
            tableView.reloadData()
            stateLabel.text = operationSnapshot?.kind == .reload ? "正在重新加载会话…" : "正在读取会话…"
            stateLabel.isHidden = false
            retryButton.isHidden = true
            activityIndicator.startAnimating()
        }

        if operationSnapshot?.kind == .sync { showSyncToast("正在同步最新消息…") }
        updateConversationMenu()
        if operationSnapshot == nil, existingDetail != nil { return }

        let observedKind = operationSnapshot?.kind ?? .load
        repository.loadConversation(id: id) { [weak self] result in
            guard let self, self.repository.selectedConversationID == id, self.presentationGeneration == currentPresentationGeneration else { return }
            self.finishVisibleOperation(id: id, kind: observedKind, previousMessages: previousMessages, result: result)
        }
    }

    func resetForAccountScopeChange() {
        presentationGeneration += 1
        hideSyncToast()
        loadingConversationID = nil
        activityIndicator.stopAnimating()
        title = "新对话"
        messages = []
        tableView.reloadData()
        stateLabel.text = "从侧边栏选择一个会话"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        updateConversationMenu()
    }

    private func apply(_ detail: ConversationDetail) {
        title = detail.title
        messages = detail.messages
        stateLabel.text = detail.messages.isEmpty ? "当前分支没有可显示的用户或助手文本消息" : nil
        stateLabel.isHidden = !detail.messages.isEmpty
        retryButton.isHidden = true
        tableView.reloadData()
    }

    private func updateConversationMenu() {
        let selectedID = repository.selectedConversationID
        let operationKind = selectedID.flatMap { repository.detailOperationSnapshot(for: $0)?.kind }
        let recoveryInProgress = operationKind == .sync || operationKind == .reload
        let canRecover = selectedID != nil && !recoveryInProgress
        let recoveryAttributes: UIMenuElement.Attributes = canRecover ? [] : [.disabled]
        let syncAction = UIAction(title: "同步最新消息", image: UIImage(systemName: "arrow.triangle.2.circlepath"), attributes: recoveryAttributes) { [weak self] _ in self?.syncLatestMessages() }
        let reloadAction = UIAction(title: "重载当前会话", image: UIImage(systemName: "arrow.clockwise"), attributes: recoveryAttributes) { [weak self] _ in self?.reloadCurrentConversation() }
        navigationItem.rightBarButtonItem = UIBarButtonItem(title: nil, image: UIImage(systemName: "ellipsis.circle"), primaryAction: nil, menu: UIMenu(children: [syncAction, reloadAction]))
    }

    private func syncLatestMessages() {
        guard let id = repository.selectedConversationID else { return }
        if let kind = repository.detailOperationSnapshot(for: id)?.kind, kind == .sync || kind == .reload { return }
        let previousMessages = messages
        let hadLoadedDetail = repository.selectedConversation?.id == id
        presentationGeneration += 1
        let currentPresentationGeneration = presentationGeneration
        diagnostics.info(category: "navigation", name: "conversation.latestSync.requested", fields: repository.diagnosticsFields(for: id))
        showSyncToast("正在同步最新消息…")
        repository.syncLatestMessages(id: id) { [weak self] result in
            guard let self, self.repository.selectedConversationID == id, self.presentationGeneration == currentPresentationGeneration else { return }
            self.loadingConversationID = nil
            self.activityIndicator.stopAnimating()
            switch result {
            case .success(let detail):
                let changed = self.hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
                self.apply(detail)
                self.showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0)
            case .failure(let error):
                guard !ConversationRepository.isLifecycleTermination(error) else { return }
                self.hideSyncToast()
                if !hadLoadedDetail {
                    self.stateLabel.text = "读取失败\n\(error.localizedDescription)"
                    self.stateLabel.isHidden = false
                    self.retryButton.isHidden = false
                }
                self.showRecoveryError(title: "同步失败", error: error)
            }
            self.updateConversationMenu()
        }
        updateConversationMenu()
    }

    private func finishVisibleOperation(id: String, kind: ConversationDetailOperationKind, previousMessages: [ConversationMessage], result: Result<ConversationDetail, Error>) {
        loadingConversationID = nil
        activityIndicator.stopAnimating()
        switch result {
        case .success(let detail):
            let changed = hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
            apply(detail)
            if kind == .sync { showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0) }
        case .failure(let error):
            guard !ConversationRepository.isLifecycleTermination(error) else { return }
            if kind == .sync, repository.selectedConversation != nil {
                hideSyncToast()
                showRecoveryError(title: "同步失败", error: error)
            } else {
                hideSyncToast()
                stateLabel.text = "读取失败\n\(error.localizedDescription)"
                stateLabel.isHidden = false
                retryButton.isHidden = false
                if kind == .sync { showRecoveryError(title: "同步失败", error: error) }
            }
        }
        updateConversationMenu()
    }

    private func hasVisibleMessageChanges(from previous: [ConversationMessage], to current: [ConversationMessage]) -> Bool {
        guard previous.count == current.count else { return true }
        return zip(previous, current).contains { old, new in old.id != new.id || old.role != new.role || old.text != new.text || old.createTime != new.createTime }
    }

    private func logResidentFirstVisible(id: String, startedAt: TimeInterval, operationKind: ConversationDetailOperationKind?) {
        var fields = repository.residentDiagnosticsFields(for: id)
        fields["elapsedMs"] = String(format: "%.2f", (ProcessInfo.processInfo.systemUptime - startedAt) * 1000)
        fields["activeOperationKind"] = operationKind?.rawValue ?? "none"
        diagnostics.info(category: "conversation", name: "resident.firstVisible", fields: fields)
    }

    private func showSyncToast(_ text: String, autoHideAfter delay: TimeInterval? = nil) {
        syncToastHideWorkItem?.cancel()
        syncToastHideWorkItem = nil
        syncToastLabel.text = text
        syncToastView.isHidden = false
        guard let delay else { return }
        let workItem = DispatchWorkItem { [weak self] in
            self?.syncToastView.isHidden = true
            self?.syncToastHideWorkItem = nil
        }
        syncToastHideWorkItem = workItem
        DispatchQueue.main.asyncAfter(deadline: .now() + delay, execute: workItem)
    }

    private func hideSyncToast() {
        syncToastHideWorkItem?.cancel()
        syncToastHideWorkItem = nil
        syncToastView.isHidden = true
    }

    private func showRecoveryError(title: String, error: Error) {
        let alert = UIAlertController(title: title, message: error.localizedDescription, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "好", style: .default))
        present(alert, animated: true)
    }

    @objc private func reloadCurrentConversation() {
        guard let id = repository.selectedConversationID else { return }
        if let kind = repository.detailOperationSnapshot(for: id)?.kind, kind == .sync || kind == .reload { return }
        presentationGeneration += 1
        let currentPresentationGeneration = presentationGeneration
        hideSyncToast()
        diagnostics.info(category: "navigation", name: "conversation.detailReload.requested", fields: repository.diagnosticsFields(for: id))
        loadingConversationID = id
        messages = []
        tableView.reloadData()
        stateLabel.text = "正在重新加载会话…"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        activityIndicator.startAnimating()
        repository.reloadConversation(id: id) { [weak self] result in
            guard let self, self.repository.selectedConversationID == id, self.presentationGeneration == currentPresentationGeneration else { return }
            self.loadingConversationID = nil
            self.activityIndicator.stopAnimating()
            switch result {
            case .success(let detail): self.apply(detail)
            case .failure(let error):
                guard !ConversationRepository.isLifecycleTermination(error) else { return }
                self.stateLabel.text = "读取失败\n\(error.localizedDescription)"
                self.stateLabel.isHidden = false
                self.retryButton.isHidden = false
            }
            self.updateConversationMenu()
        }
        updateConversationMenu()
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int { messages.count }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: ConversationMessageCell.reuseIdentifier, for: indexPath) as! ConversationMessageCell
        cell.configure(with: messages[indexPath.row])
        return cell
    }
}

final class ConversationMessageCell: UITableViewCell {
    static let reuseIdentifier = "ConversationMessageCell"

    private let bubbleView = UIView()
    private let messageLabel = UILabel()
    private var userLeadingConstraint: NSLayoutConstraint!
    private var userTrailingConstraint: NSLayoutConstraint!
    private var assistantLeadingConstraint: NSLayoutConstraint!
    private var assistantTrailingConstraint: NSLayoutConstraint!
    private var maxWidthConstraint: NSLayoutConstraint!

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        selectionStyle = .none
        backgroundColor = .systemBackground
        contentView.backgroundColor = .systemBackground

        bubbleView.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(bubbleView)
        messageLabel.font = .preferredFont(forTextStyle: .body)
        messageLabel.numberOfLines = 0
        messageLabel.translatesAutoresizingMaskIntoConstraints = false
        bubbleView.addSubview(messageLabel)

        userLeadingConstraint = bubbleView.leadingAnchor.constraint(greaterThanOrEqualTo: contentView.layoutMarginsGuide.leadingAnchor, constant: 44)
        userTrailingConstraint = bubbleView.trailingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.trailingAnchor)
        assistantLeadingConstraint = bubbleView.leadingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.leadingAnchor)
        assistantTrailingConstraint = bubbleView.trailingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.trailingAnchor)
        maxWidthConstraint = bubbleView.widthAnchor.constraint(lessThanOrEqualTo: contentView.widthAnchor, multiplier: 0.82)

        NSLayoutConstraint.activate([
            bubbleView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 7),
            bubbleView.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -7),
            messageLabel.leadingAnchor.constraint(equalTo: bubbleView.leadingAnchor, constant: 12),
            messageLabel.trailingAnchor.constraint(equalTo: bubbleView.trailingAnchor, constant: -12),
            messageLabel.topAnchor.constraint(equalTo: bubbleView.topAnchor, constant: 9),
            messageLabel.bottomAnchor.constraint(equalTo: bubbleView.bottomAnchor, constant: -9)
        ])
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    func configure(with message: ConversationMessage) {
        messageLabel.text = message.text
        NSLayoutConstraint.deactivate([userLeadingConstraint, userTrailingConstraint, assistantLeadingConstraint, assistantTrailingConstraint, maxWidthConstraint])
        switch message.role {
        case .user:
            bubbleView.backgroundColor = .secondarySystemBackground
            bubbleView.layer.cornerRadius = 18
            NSLayoutConstraint.activate([userLeadingConstraint, userTrailingConstraint, maxWidthConstraint])
        case .assistant:
            bubbleView.backgroundColor = .clear
            bubbleView.layer.cornerRadius = 0
            NSLayoutConstraint.activate([assistantLeadingConstraint, assistantTrailingConstraint])
        }
    }
}
