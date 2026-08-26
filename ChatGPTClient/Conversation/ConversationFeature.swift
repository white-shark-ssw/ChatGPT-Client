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
        }
    }
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
    private var accountContextObserver: NSObjectProtocol?
    private var memoryWarningObserver: NSObjectProtocol?

    private(set) var conversations: [ConversationSummary] = []
    private(set) var selectedConversationID: String?
    var onAccountScopeReset: (() -> Void)?

    var selectedConversation: ConversationDetail? {
        guard let id = selectedConversationID, let key = residentKey(for: id), let state = residentStates[key] else { return nil }
        if case .loaded(let detail) = state { return detail }
        return nil
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
        selectedConversationID = id
        guard let key = residentKey(for: id), let state = residentStates[key] else {
            diagnostics.info(category: "conversation", name: "resident.miss", fields: diagnosticsFields(for: id))
            return
        }
        var fields = diagnosticsFields(for: id)
        fields["residentCount"] = String(residentStates.count)
        fields["state"] = Self.residentStateName(state)
        diagnostics.info(category: "conversation", name: "resident.hit", fields: fields)
    }

    func diagnosticsFields(for id: String) -> [String: String] {
        var fields = ["conversationHash": Self.shortHash(id)]
        if let index = conversations.firstIndex(where: { $0.id == id }) { fields["listPosition"] = String(index + 1) }
        return fields
    }

    func loadConversations(completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        let span = diagnostics.startSpan(category: "conversation", name: "listLoad")
        withTransientSession { [weak self] result in
            guard let self else { return }
            switch result {
            case .failure(let error):
                span.end(status: "failed", fields: ["stage": "auth"])
                self.finishOnMain(.failure(error), completion: completion)
            case .success(let context):
                self.requestConversationList(using: context, span: span, completion: completion)
            }
        }
    }

    func loadSelectedConversation(completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        guard let id = selectedConversationID else {
            finishOnMain(.failure(ConversationRepositoryError.invalidPayload), completion: completion)
            return
        }
        loadConversation(id: id, completion: completion)
    }

    func syncLatestMessages(completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        guard let id = selectedConversationID else {
            finishOnMain(.failure(ConversationRepositoryError.invalidPayload), completion: completion)
            return
        }
        let previous = selectedConversation
        var fields = diagnosticsFields(for: id)
        fields["previousVisibleMessageCount"] = String(previous?.messages.count ?? 0)
        fields["localStateBefore"] = previous == nil ? "empty" : "loaded"
        let span = diagnostics.startSpan(category: "conversation", name: "latestSync", fields: fields)
        loadConversation(id: id, replacingCurrentRequest: true, preserveLoadedResidentOnFailure: true) { [weak self] result in
            guard let self else { return }
            switch result {
            case .success(let detail):
                var fields = self.recoveryDiffFields(previous: previous, current: detail)
                fields["localStateAfter"] = "server_backed"
                span.end(status: "ok", fields: fields)
                completion(.success(detail))
            case .failure(let error):
                span.end(status: "failed", fields: ["stage": "detailLoad", "localStateAfter": previous == nil ? "failed" : "preserved"])
                completion(.failure(error))
            }
        }
    }

    func reloadSelectedConversation(completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        guard let id = selectedConversationID else {
            finishOnMain(.failure(ConversationRepositoryError.invalidPayload), completion: completion)
            return
        }
        let previous = selectedConversation
        var fields = diagnosticsFields(for: id)
        fields["previousVisibleMessageCount"] = String(previous?.messages.count ?? 0)
        fields["localStateBefore"] = previous == nil ? "empty_or_failed" : "loaded"
        let span = diagnostics.startSpan(category: "conversation", name: "conversationReload", fields: fields)
        removeResidentState(id: id)
        diagnostics.info(category: "conversation", name: "conversationReload.stateCleared", traceID: span.traceID, fields: diagnosticsFields(for: id))
        loadConversation(id: id, replacingCurrentRequest: true) { [weak self] result in
            guard let self else { return }
            switch result {
            case .success(let detail):
                var fields = self.recoveryDiffFields(previous: previous, current: detail)
                fields["localStateAfter"] = "server_backed"
                span.end(status: "ok", fields: fields)
                completion(.success(detail))
            case .failure(let error):
                span.end(status: "failed", fields: ["stage": "detailLoad", "localStateAfter": "failed"])
                completion(.failure(error))
            }
        }
    }

    func loadConversation(id: String, replacingCurrentRequest: Bool = false, preserveLoadedResidentOnFailure: Bool = false, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        if !replacingCurrentRequest, let key = residentKey(for: id) {
            if let state = residentStates[key] {
                finishResidentHit(id: id, state: state, completion: completion)
                return
            }
            if appendCompletionIfOperationExists(key: key, id: id, completion: completion) { return }
        }

        withTransientSession { [weak self] result in
            guard let self else { return }
            switch result {
            case .failure(let error):
                self.finishOnMain(.failure(error), completion: completion)
            case .success(let context):
                DispatchQueue.main.async {
                    self.beginDetailOperation(id: id, context: context, replacingCurrentRequest: replacingCurrentRequest, preserveLoadedResidentOnFailure: preserveLoadedResidentOnFailure, completion: completion)
                }
            }
        }
    }

    private func beginDetailOperation(id: String, context: ConversationTransportContext, replacingCurrentRequest: Bool, preserveLoadedResidentOnFailure: Bool, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        adoptAccountScope(context.scope)
        guard activeAccountScope == context.scope else {
            completion(.failure(ConversationRepositoryError.accountContextChanged))
            return
        }
        let key = ConversationResidentKey(scope: context.scope, conversationID: id)
        if !replacingCurrentRequest {
            if let state = residentStates[key] {
                finishResidentHit(id: id, state: state, completion: completion)
                return
            }
            if appendCompletionIfOperationExists(key: key, id: id, completion: completion) { return }
        }

        let operationGeneration = (detailOperationGenerations[key] ?? 0) + 1
        detailOperationGenerations[key] = operationGeneration
        if replacingCurrentRequest { cancelDetailOperation(key: key, replacementOperationGeneration: operationGeneration) }
        detailOperations[key] = ConversationDetailOperation(generation: operationGeneration, preserveLoadedResidentOnFailure: preserveLoadedResidentOnFailure, task: nil, completions: [completion])
        var fields = diagnosticsFields(for: id)
        fields["operationGeneration"] = String(operationGeneration)
        let span = diagnostics.startSpan(category: "conversation", name: "detailLoad", fields: fields)
        requestConversationDetail(key: key, operationGeneration: operationGeneration, using: context, span: span)
    }

    private func finishResidentHit(id: String, state: ConversationResidentState, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        var fields = diagnosticsFields(for: id)
        fields["residentCount"] = String(residentStates.count)
        fields["state"] = Self.residentStateName(state)
        diagnostics.info(category: "conversation", name: "resident.hit", fields: fields)
        switch state {
        case .loaded(let detail): finishOnMain(.success(detail), completion: completion)
        case .failed(let error): finishOnMain(.failure(error), completion: completion)
        }
    }

    private func appendCompletionIfOperationExists(key: ConversationResidentKey, id: String, completion: @escaping (Result<ConversationDetail, Error>) -> Void) -> Bool {
        guard var operation = detailOperations[key] else { return false }
        operation.completions.append(completion)
        detailOperations[key] = operation
        var fields = diagnosticsFields(for: id)
        fields["operationGeneration"] = String(operation.generation)
        fields["completionCount"] = String(operation.completions.count)
        diagnostics.info(category: "conversation", name: "detail.coalesced", fields: fields)
        return true
    }

    private func withTransientSession(completion: @escaping (Result<ConversationTransportContext, Error>) -> Void) {
        if let transientSession, let transientSessionScope {
            if let verifiedContext = authSessionStore.verifiedAccountContext() {
                let verifiedScope = ConversationAccountScope(verifiedContext)
                if verifiedScope != transientSessionScope {
                    resetAccountScope(to: verifiedScope)
                } else {
                    completion(.success(ConversationTransportContext(session: transientSession, scope: transientSessionScope)))
                    return
                }
            } else {
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
            guard state == .verified, let session, let accountContext = self.authSessionStore.verifiedAccountContext() else {
                session?.finishTasksAndInvalidate()
                DispatchQueue.main.async { self.finishTransientSessionProbe(.failure(ConversationRepositoryError.authenticationNotAvailable)) }
                return
            }
            let scope = ConversationAccountScope(accountContext)
            DispatchQueue.main.async {
                self.adoptAccountScope(scope)
                guard self.activeAccountScope == scope else {
                    session.invalidateAndCancel()
                    self.finishTransientSessionProbe(.failure(ConversationRepositoryError.accountContextChanged))
                    return
                }
                self.transientSession = session
                self.transientSessionScope = scope
                self.finishTransientSessionProbe(.success(ConversationTransportContext(session: session, scope: scope)))
            }
        }
    }

    private func finishTransientSessionProbe(_ result: Result<ConversationTransportContext, Error>) {
        let completions = transientSessionProbeCompletions ?? []
        transientSessionProbeCompletions = nil
        for completion in completions { completion(result) }
    }

    private func requestConversationList(using context: ConversationTransportContext, span: DiagnosticsSpan, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        diagnostics.info(category: "conversation", name: "list.request", traceID: span.traceID, fields: ["method": "GET", "route": "conversation_list", "offset": "0", "limit": "28", "order": "updated"])
        var request = URLRequest(url: Self.listURL)
        request.httpMethod = "GET"
        context.session.dataTask(with: request) { [weak self] data, response, error in
            guard let self else { return }
            if let error {
                self.diagnostics.error(category: "conversation", name: "list.failed", traceID: span.traceID, error: error)
                span.end(status: "failed", fields: ["stage": "network"])
                self.finishScopedListResult(context: context, result: .failure(error), completion: completion)
                return
            }
            guard let response = response as? HTTPURLResponse, let data else {
                span.end(status: "failed", fields: ["stage": "response", "reason": "non_http_response"])
                self.finishScopedListResult(context: context, result: .failure(ConversationRepositoryError.invalidResponse), completion: completion)
                return
            }
            guard (200..<300).contains(response.statusCode) else {
                span.end(status: "failed", fields: ["stage": "response", "httpStatus": String(response.statusCode)])
                self.finishScopedListResult(context: context, result: .failure(ConversationRepositoryError.httpStatus(response.statusCode)), completion: completion)
                return
            }
            guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let rawItems = payload["items"] as? [[String: Any]] else {
                span.end(status: "failed", fields: ["stage": "parse", "reason": "missing_items"])
                self.finishScopedListResult(context: context, result: .failure(ConversationRepositoryError.invalidPayload), completion: completion)
                return
            }

            let items = rawItems.compactMap(Self.parseConversationSummary)
            var fields = ["httpStatus": String(response.statusCode), "byteCount": String(data.count), "itemCount": String(items.count)]
            if let total = payload["total"] as? NSNumber { fields["totalCount"] = total.stringValue }
            DispatchQueue.main.async {
                guard self.activeAccountScope == context.scope else {
                    var discardedFields = fields
                    discardedFields["reason"] = "account_changed"
                    span.end(status: "discarded", fields: discardedFields)
                    completion(.failure(ConversationRepositoryError.accountContextChanged))
                    return
                }
                self.diagnostics.info(category: "conversation", name: "list.response", traceID: span.traceID, fields: fields)
                span.end(status: "ok", fields: fields)
                self.conversations = items
                completion(.success(items))
            }
        }
    }

    private func finishScopedListResult(context: ConversationTransportContext, result: Result<[ConversationSummary], Error>, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        DispatchQueue.main.async {
            guard self.activeAccountScope == context.scope else {
                completion(.failure(ConversationRepositoryError.accountContextChanged))
                return
            }
            completion(result)
        }
    }

    private func requestConversationDetail(key: ConversationResidentKey, operationGeneration: Int, using context: ConversationTransportContext, span: DiagnosticsSpan) {
        let id = key.conversationID
        let detailURL = URL(string: "https://chatgpt.com/backend-api/conversation")!.appendingPathComponent(id)
        var requestFields = diagnosticsFields(for: id)
        requestFields["method"] = "GET"
        requestFields["route"] = "conversation_detail"
        requestFields["operationGeneration"] = String(operationGeneration)
        diagnostics.info(category: "conversation", name: "detail.request", traceID: span.traceID, fields: requestFields)
        var request = URLRequest(url: detailURL)
        request.httpMethod = "GET"
        let task = context.session.dataTask(with: request) { [weak self] data, response, error in
            guard let self else { return }
            if let error {
                let nsError = error as NSError
                if nsError.domain == NSURLErrorDomain && nsError.code == NSURLErrorCancelled {
                    var fields = self.diagnosticsFields(for: id)
                    fields["operationGeneration"] = String(operationGeneration)
                    self.diagnostics.info(category: "conversation", name: "detail.cancelled", traceID: span.traceID, fields: fields)
                    span.end(status: "cancelled", fields: fields)
                    return
                }
                self.diagnostics.error(category: "conversation", name: "detail.failed", traceID: span.traceID, error: error, fields: self.diagnosticsFields(for: id))
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
            var fields = self.diagnosticsFields(for: id)
            fields["httpStatus"] = String(response.statusCode)
            fields["byteCount"] = String(data.count)
            fields["mappingCount"] = String(mapping.count)
            fields["visibleMessageCount"] = String(messages.count)
            fields["operationGeneration"] = String(operationGeneration)
            self.diagnostics.info(category: "conversation", name: "detail.response", traceID: span.traceID, fields: fields)
            span.end(status: "ok", fields: fields)
            self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .success(detail))
        }
        DispatchQueue.main.async {
            guard var operation = self.detailOperations[key], operation.generation == operationGeneration else {
                task.cancel()
                return
            }
            operation.task = task
            self.detailOperations[key] = operation
        }
    }

    private func cancelDetailOperation(key: ConversationResidentKey, replacementOperationGeneration: Int) {
        guard let operation = detailOperations.removeValue(forKey: key) else { return }
        var fields = diagnosticsFields(for: key.conversationID)
        fields["cancelledOperationGeneration"] = String(operation.generation)
        fields["replacementOperationGeneration"] = String(replacementOperationGeneration)
        fields["taskPresent"] = operation.task == nil ? "false" : "true"
        diagnostics.info(category: "conversation", name: "detail.cancel.requested", fields: fields)
        operation.task?.cancel()
    }

    private func finishDetailOperation(key: ConversationResidentKey, operationGeneration: Int, result: Result<ConversationDetail, Error>) {
        DispatchQueue.main.async {
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
                var fields = self.diagnosticsFields(for: key.conversationID)
                fields["residentCount"] = String(self.residentStates.count)
                fields["residentApproximateTextBytes"] = String(Self.approximateTextBytes(detail))
                fields["residentTotalApproximateTextBytes"] = String(self.residentStates.values.reduce(0) { $0 + Self.approximateTextBytes($1) })
                fields["visibility"] = self.selectedConversationID == key.conversationID ? "foreground" : "hidden"
                fields["state"] = "loaded"
                self.diagnostics.info(category: "conversation", name: "resident.stored", fields: fields)
            case .failure(let error):
                let hasLoadedResident: Bool
                if let existingState = self.residentStates[key], case .loaded = existingState { hasLoadedResident = true } else { hasLoadedResident = false }
                if !operation.preserveLoadedResidentOnFailure || !hasLoadedResident { self.residentStates[key] = .failed(error) }
                var fields = self.diagnosticsFields(for: key.conversationID)
                fields["residentCount"] = String(self.residentStates.count)
                fields["state"] = operation.preserveLoadedResidentOnFailure && hasLoadedResident ? "loaded_preserved" : "failed"
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

    private func handleAccountContextChange() {
        guard let context = authSessionStore.verifiedAccountContext() else {
            if activeAccountScope != nil { resetAccountScope(to: nil) }
            return
        }
        let scope = ConversationAccountScope(context)
        if let activeAccountScope {
            if activeAccountScope != scope { resetAccountScope(to: scope) }
        } else {
            activeAccountScope = scope
        }
    }

    private func adoptAccountScope(_ scope: ConversationAccountScope) {
        if let activeAccountScope {
            if activeAccountScope != scope { resetAccountScope(to: scope) }
        } else {
            activeAccountScope = scope
        }
    }

    private func resetAccountScope(to newScope: ConversationAccountScope?) {
        let removedResidentCount = residentStates.count
        let cancelledOperationCount = detailOperations.count
        for operation in detailOperations.values { operation.task?.cancel() }
        detailOperations.removeAll()
        detailOperationGenerations.removeAll()
        residentStates.removeAll()
        conversations = []
        selectedConversationID = nil
        transientSession?.invalidateAndCancel()
        transientSession = nil
        transientSessionScope = nil
        activeAccountScope = newScope
        diagnostics.info(category: "conversation", name: "accountScope.reset", fields: ["residentRemovedCount": String(removedResidentCount), "operationCancelledCount": String(cancelledOperationCount), "nextScopeVerified": newScope == nil ? "false" : "true"])
        onAccountScopeReset?()
    }

    private func handleMemoryWarning() {
        let selectedKey = selectedConversationID.flatMap { residentKey(for: $0) }
        let evictedKeys = residentStates.keys.filter { $0 != selectedKey }
        guard !evictedKeys.isEmpty else { return }
        for key in evictedKeys { residentStates.removeValue(forKey: key) }
        diagnostics.warning(category: "conversation", name: "resident.evicted", fields: ["reason": "memory_warning", "evictedCount": String(evictedKeys.count), "residentCount": String(residentStates.count)])
    }

    private func residentKey(for id: String) -> ConversationResidentKey? {
        guard let activeAccountScope else { return nil }
        return ConversationResidentKey(scope: activeAccountScope, conversationID: id)
    }

    private func removeResidentState(id: String) {
        guard let key = residentKey(for: id) else { return }
        residentStates.removeValue(forKey: key)
    }

    private func recoveryDiffFields(previous: ConversationDetail?, current: ConversationDetail) -> [String: String] {
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

    private func finishOnMain<T>(_ result: Result<T, Error>, completion: @escaping (Result<T, Error>) -> Void) {
        if Thread.isMainThread { completion(result) } else { DispatchQueue.main.async { completion(result) } }
    }

    private static func parseConversationSummary(_ item: [String: Any]) -> ConversationSummary? {
        guard let id = item["id"] as? String, !id.isEmpty else { return nil }
        return ConversationSummary(id: id, title: normalizedTitle(item["title"] as? String), updateTime: (item["update_time"] as? NSNumber)?.doubleValue)
    }

    private static func normalizedTitle(_ title: String?) -> String {
        let trimmed = title?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
        return trimmed.isEmpty ? "未命名会话" : trimmed
    }

    private static func shortHash(_ value: String) -> String {
        "sha256:" + SHA256.hash(data: Data(value.utf8)).prefix(6).map { String(format: "%02x", $0) }.joined()
    }

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
        let item = repository.conversations[indexPath.row]
        diagnostics.info(category: "navigation", name: "conversation.selected", fields: repository.diagnosticsFields(for: item.id))
        onSelectConversation?(item.id)
        tableView.reloadData()
    }

    func resetForAccountScopeChange() {
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
        errorView?.removeFromSuperview()
        errorView = nil
        navigationItem.rightBarButtonItem?.isEnabled = false
        repository.loadConversations { [weak self] result in
            guard let self else { return }
            self.loading = false
            self.refreshControl?.endRefreshing()
            self.navigationItem.rightBarButtonItem?.isEnabled = true
            switch result {
            case .success: self.tableView.reloadData()
            case .failure(let error):
                guard !Self.isAccountContextChanged(error) else { return }
                self.showError(error)
            }
        }
    }

    private static func isAccountContextChanged(_ error: Error) -> Bool {
        guard let repositoryError = error as? ConversationRepositoryError else { return false }
        if case .accountContextChanged = repositoryError { return true }
        return false
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
    private var recoveryActionInProgress = false
    private var recoveryPresentationGeneration = 0

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
        guard loadingConversationID != id || repository.selectedConversation?.id != id else { return }
        recoveryPresentationGeneration += 1
        hideSyncToast()
        recoveryActionInProgress = false
        if let detail = repository.selectedConversation {
            loadingConversationID = nil
            activityIndicator.stopAnimating()
            apply(detail)
            updateConversationMenu()
            return
        }
        loadingConversationID = id
        messages = []
        tableView.reloadData()
        stateLabel.text = "正在读取会话…"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        activityIndicator.startAnimating()
        updateConversationMenu()
        repository.loadConversation(id: id) { [weak self] result in
            guard let self, self.repository.selectedConversationID == id else { return }
            self.loadingConversationID = nil
            self.activityIndicator.stopAnimating()
            switch result {
            case .success(let detail): self.apply(detail)
            case .failure(let error):
                self.stateLabel.text = "读取失败\n\(error.localizedDescription)"
                self.stateLabel.isHidden = false
                self.retryButton.isHidden = false
            }
            self.updateConversationMenu()
        }
    }

    func resetForAccountScopeChange() {
        recoveryPresentationGeneration += 1
        hideSyncToast()
        recoveryActionInProgress = false
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
        let canRecover = repository.selectedConversationID != nil && !recoveryActionInProgress
        let recoveryAttributes: UIMenuElement.Attributes = canRecover ? [] : [.disabled]
        let syncAction = UIAction(title: "同步最新消息", image: UIImage(systemName: "arrow.triangle.2.circlepath"), attributes: recoveryAttributes) { [weak self] _ in self?.syncLatestMessages() }
        let reloadAction = UIAction(title: "重载当前会话", image: UIImage(systemName: "arrow.clockwise"), attributes: recoveryAttributes) { [weak self] _ in self?.reloadCurrentConversation() }
        navigationItem.rightBarButtonItem = UIBarButtonItem(title: nil, image: UIImage(systemName: "ellipsis.circle"), primaryAction: nil, menu: UIMenu(children: [syncAction, reloadAction]))
    }

    private func syncLatestMessages() {
        guard let id = repository.selectedConversationID, !recoveryActionInProgress else { return }
        let previousMessages = messages
        let hadLoadedDetail = repository.selectedConversation?.id == id
        recoveryActionInProgress = true
        recoveryPresentationGeneration += 1
        let presentationGeneration = recoveryPresentationGeneration
        diagnostics.info(category: "navigation", name: "conversation.latestSync.requested", fields: repository.diagnosticsFields(for: id))
        updateConversationMenu()
        showSyncToast("正在同步最新消息…")
        repository.syncLatestMessages { [weak self] result in
            guard let self, self.repository.selectedConversationID == id, self.recoveryPresentationGeneration == presentationGeneration else { return }
            self.recoveryActionInProgress = false
            self.loadingConversationID = nil
            self.activityIndicator.stopAnimating()
            switch result {
            case .success(let detail):
                let changed = self.hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
                self.apply(detail)
                self.showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0)
            case .failure(let error):
                self.hideSyncToast()
                if !hadLoadedDetail {
                    self.stateLabel.text = "读取失败\n\(error.localizedDescription)"
                    self.stateLabel.isHidden = false
                    self.retryButton.isHidden = false
                }
                let alert = UIAlertController(title: "同步失败", message: error.localizedDescription, preferredStyle: .alert)
                alert.addAction(UIAlertAction(title: "好", style: .default))
                self.present(alert, animated: true)
            }
            self.updateConversationMenu()
        }
    }

    private func hasVisibleMessageChanges(from previous: [ConversationMessage], to current: [ConversationMessage]) -> Bool {
        guard previous.count == current.count else { return true }
        return zip(previous, current).contains { old, new in old.id != new.id || old.role != new.role || old.text != new.text || old.createTime != new.createTime }
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

    @objc private func reloadCurrentConversation() {
        guard let id = repository.selectedConversationID, !recoveryActionInProgress else { return }
        recoveryActionInProgress = true
        recoveryPresentationGeneration += 1
        let presentationGeneration = recoveryPresentationGeneration
        hideSyncToast()
        diagnostics.info(category: "navigation", name: "conversation.detailReload.requested", fields: repository.diagnosticsFields(for: id))
        loadingConversationID = id
        messages = []
        tableView.reloadData()
        stateLabel.text = "正在重新加载会话…"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        activityIndicator.startAnimating()
        updateConversationMenu()
        repository.reloadSelectedConversation { [weak self] result in
            guard let self, self.repository.selectedConversationID == id, self.recoveryPresentationGeneration == presentationGeneration else { return }
            self.recoveryActionInProgress = false
            self.loadingConversationID = nil
            self.activityIndicator.stopAnimating()
            switch result {
            case .success(let detail): self.apply(detail)
            case .failure(let error):
                self.stateLabel.text = "读取失败\n\(error.localizedDescription)"
                self.stateLabel.isHidden = false
                self.retryButton.isHidden = false
            }
            self.updateConversationMenu()
        }
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
