import CryptoKit
import Foundation
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

struct ConversationRoundProjection {
    struct Round {
        let userMessageID: String
        let answerMessageID: String?
    }

    let rounds: [Round]

    var answerMessageIDs: [String] { rounds.compactMap(\.answerMessageID) }

    static func derive(from messages: [ConversationMessage]) -> ConversationRoundProjection {
        var rounds: [Round] = []
        for message in messages {
            switch message.role {
            case .user:
                rounds.append(Round(userMessageID: message.id, answerMessageID: nil))
            case .assistant:
                guard let last = rounds.last, last.answerMessageID == nil else { continue }
                rounds[rounds.count - 1] = Round(userMessageID: last.userMessageID, answerMessageID: message.id)
            }
        }
        return ConversationRoundProjection(rounds: rounds)
    }
}

struct ConversationDetail {
    let id: String
    let title: String
    let currentNodeID: String
    let messages: [ConversationMessage]
}

enum ConversationRepositoryError: LocalizedError, Equatable {
    case authenticationNotAvailable
    case authenticationTemporarilyUnavailable
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
        case .authenticationTemporarilyUnavailable: return "暂时无法验证账户，请检查网络连接。"
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

private struct ConversationListCacheEntry: Codable {
    let id: String
    let title: String
    let updateTime: TimeInterval?

    init(_ summary: ConversationSummary) {
        id = summary.id
        title = summary.title
        updateTime = summary.updateTime
    }

    var summary: ConversationSummary { ConversationSummary(id: id, title: title, updateTime: updateTime) }
}

private struct ConversationListCacheSnapshot: Codable {
    let schemaVersion: Int
    let lastSuccessfulReconciliationTime: TimeInterval
    let items: [ConversationListCacheEntry]
}

private final class ConversationListCacheStore {
    static let schemaVersion = 1

    enum LoadResult {
        case missing(durationMs: Double)
        case loaded(snapshot: ConversationListCacheSnapshot, byteCount: Int, durationMs: Double)
        case rejected(reason: String, durationMs: Double)
    }

    private let queue = DispatchQueue(label: "com.whitesharkssw.chatgptclient.conversation-list-cache", qos: .utility)
    private let fileManager = FileManager.default

    func load(namespace: String, completion: @escaping (LoadResult) -> Void) {
        queue.async {
            let startedAt = ProcessInfo.processInfo.systemUptime
            completion(self.loadSnapshot(namespace: namespace, startedAt: startedAt))
        }
    }

    func loadLastVerified(completion: @escaping (String?, LoadResult) -> Void) {
        queue.async {
            let startedAt = ProcessInfo.processInfo.systemUptime
            do {
                let hintURL = try self.lastVerifiedNamespaceURL()
                guard self.fileManager.fileExists(atPath: hintURL.path) else {
                    completion(nil, .missing(durationMs: Self.elapsedMs(since: startedAt)))
                    return
                }
                let namespace = try String(contentsOf: hintURL, encoding: .utf8).trimmingCharacters(in: .whitespacesAndNewlines)
                guard Self.isValidNamespace(namespace) else {
                    try? self.fileManager.removeItem(at: hintURL)
                    completion(nil, .rejected(reason: "scope_hint_invalid", durationMs: Self.elapsedMs(since: startedAt)))
                    return
                }
                let result = self.loadSnapshot(namespace: namespace, startedAt: startedAt)
                switch result {
                case .loaded: break
                case .missing, .rejected: try? self.fileManager.removeItem(at: hintURL)
                }
                completion(namespace, result)
            } catch {
                completion(nil, .rejected(reason: "scope_hint_read_failed", durationMs: Self.elapsedMs(since: startedAt)))
            }
        }
    }

    func rememberVerifiedNamespace(_ namespace: String, completion: @escaping (Result<Void, Error>) -> Void) {
        queue.async {
            do {
                try self.writeLastVerifiedNamespace(namespace)
                completion(.success(()))
            } catch {
                completion(.failure(error))
            }
        }
    }

    func write(namespace: String, summaries: [ConversationSummary], reconciliationTime: TimeInterval, completion: @escaping (Result<(byteCount: Int, durationMs: Double), Error>) -> Void) {
        queue.async {
            let startedAt = ProcessInfo.processInfo.systemUptime
            do {
                let snapshot = ConversationListCacheSnapshot(schemaVersion: Self.schemaVersion, lastSuccessfulReconciliationTime: reconciliationTime, items: summaries.map(ConversationListCacheEntry.init))
                let encoder = JSONEncoder()
                encoder.outputFormatting = [.sortedKeys]
                let data = try encoder.encode(snapshot)
                let url = try self.cacheURL(namespace: namespace)
                try data.write(to: url, options: .atomic)
                try self.fileManager.setAttributes([.protectionKey: FileProtectionType.completeUntilFirstUserAuthentication], ofItemAtPath: url.path)
                try self.writeLastVerifiedNamespace(namespace)
                completion(.success((byteCount: data.count, durationMs: Self.elapsedMs(since: startedAt))))
            } catch {
                completion(.failure(error))
            }
        }
    }

    func clearLastVerifiedNamespace() {
        queue.async {
            guard let url = try? self.lastVerifiedNamespaceURL(), self.fileManager.fileExists(atPath: url.path) else { return }
            try? self.fileManager.removeItem(at: url)
        }
    }

    private func loadSnapshot(namespace: String, startedAt: TimeInterval) -> LoadResult {
        do {
            let url = try cacheURL(namespace: namespace)
            guard fileManager.fileExists(atPath: url.path) else { return .missing(durationMs: Self.elapsedMs(since: startedAt)) }
            let data = try Data(contentsOf: url)
            let snapshot: ConversationListCacheSnapshot
            do {
                snapshot = try JSONDecoder().decode(ConversationListCacheSnapshot.self, from: data)
            } catch {
                try? fileManager.removeItem(at: url)
                return .rejected(reason: "decode_failed", durationMs: Self.elapsedMs(since: startedAt))
            }
            guard snapshot.schemaVersion == Self.schemaVersion else {
                try? fileManager.removeItem(at: url)
                return .rejected(reason: "schema_mismatch", durationMs: Self.elapsedMs(since: startedAt))
            }
            return .loaded(snapshot: snapshot, byteCount: data.count, durationMs: Self.elapsedMs(since: startedAt))
        } catch {
            return .rejected(reason: "read_failed", durationMs: Self.elapsedMs(since: startedAt))
        }
    }

    private func cacheDirectoryURL() throws -> URL {
        let applicationSupport = try fileManager.url(for: .applicationSupportDirectory, in: .userDomainMask, appropriateFor: nil, create: true)
        let directory = applicationSupport.appendingPathComponent("ConversationListCache", isDirectory: true)
        if !fileManager.fileExists(atPath: directory.path) {
            try fileManager.createDirectory(at: directory, withIntermediateDirectories: true, attributes: [.protectionKey: FileProtectionType.completeUntilFirstUserAuthentication])
        } else {
            try fileManager.setAttributes([.protectionKey: FileProtectionType.completeUntilFirstUserAuthentication], ofItemAtPath: directory.path)
        }
        return directory
    }

    private func cacheURL(namespace: String) throws -> URL { try cacheDirectoryURL().appendingPathComponent("snapshot-\(namespace).json", isDirectory: false) }

    private func lastVerifiedNamespaceURL() throws -> URL { try cacheDirectoryURL().appendingPathComponent("last-verified-scope.txt", isDirectory: false) }

    private func writeLastVerifiedNamespace(_ namespace: String) throws {
        guard Self.isValidNamespace(namespace) else { throw CocoaError(.fileWriteInvalidFileName) }
        let url = try lastVerifiedNamespaceURL()
        try Data(namespace.utf8).write(to: url, options: .atomic)
        try fileManager.setAttributes([.protectionKey: FileProtectionType.completeUntilFirstUserAuthentication], ofItemAtPath: url.path)
    }

    private static func isValidNamespace(_ namespace: String) -> Bool {
        guard namespace.count == 64 else { return false }
        return namespace.unicodeScalars.allSatisfy { CharacterSet(charactersIn: "0123456789abcdef").contains($0) }
    }

    private static func elapsedMs(since startedAt: TimeInterval) -> Double { (ProcessInfo.processInfo.systemUptime - startedAt) * 1000 }
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
    private static let listCacheFreshnessInterval: TimeInterval = 60

    private let diagnostics = DiagnosticsLogger.shared
    private let authSessionStore = AuthSessionStore.shared
    private let listCacheStore = ConversationListCacheStore()
    private var transientSession: AuthTransientSession?
    private var transientSessionScope: ConversationAccountScope?
    private var transientSessionProbeCompletions: [(Result<ConversationTransportContext, Error>) -> Void]?
    private var activeAccountScope: ConversationAccountScope?
    private var provisionalCacheNamespace: String?
    private var residentStates: [ConversationResidentKey: ConversationResidentState] = [:]
    private var detailOperationGenerations: [ConversationResidentKey: Int] = [:]
    private var detailOperations: [ConversationResidentKey: ConversationDetailOperation] = [:]
    private var listOperationGeneration = 0
    private var accountContextObserver: NSObjectProtocol?
    private var memoryWarningObserver: NSObjectProtocol?

    private(set) var conversations: [ConversationSummary] = []
    private(set) var selectedConversationID: String?
    var onAccountScopeReset: (() -> Void)?
    var onConversationListChanged: (() -> Void)?

    var selectedConversation: ConversationDetail? {
        requireMainThread()
        guard let id = selectedConversationID else { return nil }
        return residentDetail(id: id)
    }

    var canOpenConversationFromList: Bool {
        requireMainThread()
        return activeAccountScope != nil
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

    func loadConversations(forceRefresh: Bool = false, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        requireMainThread()
        listOperationGeneration += 1
        let generation = listOperationGeneration
        let span = diagnostics.startSpan(category: "conversation", name: "listLoad", fields: ["operationGeneration": String(generation), "refreshMode": forceRefresh ? "manual" : "automatic"])
        if forceRefresh {
            beginAuthenticatedConversationListLoad(forceRefresh: true, operationGeneration: generation, span: span, completion: completion)
            return
        }
        prepareProvisionalConversationListCache(operationGeneration: generation, span: span) { [weak self] result in
            guard let self else { return }
            self.requireMainThread()
            switch result {
            case .failure(let error):
                span.end(status: "discarded", fields: ["reason": "operation_superseded", "operationGeneration": String(generation)])
                completion(.failure(error))
            case .success:
                self.beginAuthenticatedConversationListLoad(forceRefresh: false, operationGeneration: generation, span: span, completion: completion)
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
                let error: ConversationRepositoryError = state == .failed ? .authenticationTemporarilyUnavailable : .authenticationNotAvailable
                DispatchQueue.main.async { self.finishTransientSessionProbe(.failure(error)) }
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

    private func prepareProvisionalConversationListCache(operationGeneration: Int, span: DiagnosticsSpan, completion: @escaping (Result<Void, Error>) -> Void) {
        requireMainThread()
        guard activeAccountScope == nil, conversations.isEmpty else {
            completion(.success(()))
            return
        }
        diagnostics.info(category: "conversation", name: "listCache.provisional.started", traceID: span.traceID, fields: ["operationGeneration": String(operationGeneration)])
        listCacheStore.loadLastVerified { [weak self] namespace, loadResult in
            guard let self else { return }
            DispatchQueue.main.async {
                self.requireMainThread()
                guard self.listOperationGeneration == operationGeneration else {
                    completion(.failure(ConversationRepositoryError.operationSuperseded))
                    return
                }
                switch loadResult {
                case .missing(let durationMs):
                    self.diagnostics.info(category: "conversation", name: "listCache.provisional.completed", traceID: span.traceID, fields: ["hit": "false", "durationMs": String(format: "%.2f", durationMs)])
                case .rejected(let reason, let durationMs):
                    self.diagnostics.warning(category: "conversation", name: "listCache.provisional.completed", fields: ["hit": "false", "durationMs": String(format: "%.2f", durationMs), "reason": reason])
                case .loaded(let snapshot, let byteCount, let durationMs):
                    guard let namespace else {
                        self.diagnostics.warning(category: "conversation", name: "listCache.provisional.completed", fields: ["hit": "false", "reason": "missing_namespace"])
                        completion(.success(()))
                        return
                    }
                    self.conversations = snapshot.items.map(\.summary)
                    self.provisionalCacheNamespace = namespace
                    self.onConversationListChanged?()
                    let age = Self.cacheAge(reconciliationTime: snapshot.lastSuccessfulReconciliationTime)
                    self.diagnostics.info(category: "conversation", name: "listCache.provisional.completed", traceID: span.traceID, fields: ["hit": "true", "entryCount": String(self.conversations.count), "byteCount": String(byteCount), "ageSeconds": age.isFinite ? String(format: "%.2f", age) : "invalid", "durationMs": String(format: "%.2f", durationMs), "scopeHash": "sha256:\(namespace.prefix(12))"])
                }
                completion(.success(()))
            }
        }
    }

    private func beginAuthenticatedConversationListLoad(forceRefresh: Bool, operationGeneration: Int, span: DiagnosticsSpan, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        requireMainThread()
        withTransientSession { [weak self] result in
            guard let self else { return }
            self.requireMainThread()
            guard operationGeneration == self.listOperationGeneration else {
                span.end(status: "discarded", fields: ["reason": "operation_superseded", "operationGeneration": String(operationGeneration)])
                completion(.failure(ConversationRepositoryError.operationSuperseded))
                return
            }
            switch result {
            case .failure(let error):
                if !forceRefresh, let provisionalNamespace = self.provisionalCacheNamespace, !self.conversations.isEmpty, let repositoryError = error as? ConversationRepositoryError, repositoryError == .authenticationTemporarilyUnavailable {
                    self.diagnostics.info(category: "conversation", name: "listCache.autoRefreshDecision", traceID: span.traceID, fields: ["decision": "offline_cache", "scopeHash": "sha256:\(provisionalNamespace.prefix(12))", "operationGeneration": String(operationGeneration)])
                    span.end(status: "ok", fields: ["source": "cache", "auth": "temporarily_unavailable", "itemCount": String(self.conversations.count), "operationGeneration": String(operationGeneration)])
                    completion(.success(self.conversations))
                    return
                }
                if let repositoryError = error as? ConversationRepositoryError, repositoryError == .authenticationNotAvailable { self.rejectProvisionalConversationListCache(reason: "auth_not_available") }
                span.end(status: "failed", fields: ["stage": "auth", "operationGeneration": String(operationGeneration)])
                completion(.failure(error))
            case .success(let context):
                let verifiedNamespace = Self.cacheNamespace(for: context.scope)
                if let provisionalNamespace = self.provisionalCacheNamespace {
                    if provisionalNamespace != verifiedNamespace {
                        self.diagnostics.info(category: "conversation", name: "listCache.scopeRejected", traceID: span.traceID, fields: ["scopeHash": "sha256:\(provisionalNamespace.prefix(12))", "reason": "verified_scope_mismatch"])
                        self.conversations = []
                        self.selectedConversationID = nil
                        self.onConversationListChanged?()
                        self.listCacheStore.clearLastVerifiedNamespace()
                    }
                    self.provisionalCacheNamespace = nil
                }
                self.loadConversationListCache(using: context, operationGeneration: operationGeneration, forceRefresh: forceRefresh, span: span, completion: completion)
            }
        }
    }

    private func rejectProvisionalConversationListCache(reason: String) {
        requireMainThread()
        if let namespace = provisionalCacheNamespace {
            diagnostics.info(category: "conversation", name: "listCache.scopeRejected", fields: ["scopeHash": "sha256:\(namespace.prefix(12))", "reason": reason])
            provisionalCacheNamespace = nil
            conversations = []
            selectedConversationID = nil
            onConversationListChanged?()
        }
        listCacheStore.clearLastVerifiedNamespace()
    }

    private func loadConversationListCache(using context: ConversationTransportContext, operationGeneration: Int, forceRefresh: Bool, span: DiagnosticsSpan, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        requireMainThread()
        let namespace = Self.cacheNamespace(for: context.scope)
        listCacheStore.rememberVerifiedNamespace(namespace) { [weak self] result in
            guard let self, case .failure(let error) = result else { return }
            self.diagnostics.warning(category: "conversation", name: "listCache.scopeHint", fields: ["result": "failed", "errorType": String(describing: type(of: error))])
        }
        diagnostics.info(category: "conversation", name: "listCache.load.started", traceID: span.traceID, fields: ["schema": String(ConversationListCacheStore.schemaVersion), "operationGeneration": String(operationGeneration)])
        listCacheStore.load(namespace: namespace) { [weak self] loadResult in
            guard let self else { return }
            DispatchQueue.main.async {
                self.requireMainThread()
                guard self.activeAccountScope == context.scope else {
                    self.diagnostics.info(category: "conversation", name: "listCache.scopeRejected", traceID: span.traceID, fields: ["scopeHash": "sha256:\(namespace.prefix(12))", "reason": "account_changed"])
                    span.end(status: "discarded", fields: ["reason": "account_changed", "operationGeneration": String(operationGeneration)])
                    completion(.failure(ConversationRepositoryError.accountContextChanged))
                    return
                }
                guard self.listOperationGeneration == operationGeneration else {
                    self.diagnostics.info(category: "conversation", name: "listCache.scopeRejected", traceID: span.traceID, fields: ["scopeHash": "sha256:\(namespace.prefix(12))", "reason": "operation_superseded"])
                    span.end(status: "discarded", fields: ["reason": "operation_superseded", "operationGeneration": String(operationGeneration)])
                    completion(.failure(ConversationRepositoryError.operationSuperseded))
                    return
                }

                var snapshot: ConversationListCacheSnapshot?
                switch loadResult {
                case .missing(let durationMs):
                    self.diagnostics.info(category: "conversation", name: "listCache.load.completed", traceID: span.traceID, fields: ["hit": "false", "schema": String(ConversationListCacheStore.schemaVersion), "entryCount": "0", "durationMs": String(format: "%.2f", durationMs)])
                case .rejected(let reason, let durationMs):
                    self.diagnostics.warning(category: "conversation", name: "listCache.load.completed", fields: ["hit": "false", "schema": String(ConversationListCacheStore.schemaVersion), "entryCount": "0", "durationMs": String(format: "%.2f", durationMs), "reason": reason])
                case .loaded(let loadedSnapshot, let byteCount, let durationMs):
                    snapshot = loadedSnapshot
                    let cachedItems = loadedSnapshot.items.map(\.summary)
                    let shouldPublish = self.conversations.isEmpty
                    if shouldPublish {
                        self.conversations = cachedItems
                        self.onConversationListChanged?()
                    }
                    let age = Self.cacheAge(reconciliationTime: loadedSnapshot.lastSuccessfulReconciliationTime)
                    self.diagnostics.info(category: "conversation", name: "listCache.load.completed", traceID: span.traceID, fields: ["hit": "true", "schema": String(loadedSnapshot.schemaVersion), "entryCount": String(cachedItems.count), "byteCount": String(byteCount), "ageSeconds": age.isFinite ? String(format: "%.2f", age) : "invalid", "published": shouldPublish ? "true" : "false", "durationMs": String(format: "%.2f", durationMs)])
                }

                if forceRefresh {
                    self.diagnostics.info(category: "conversation", name: "listCache.autoRefreshDecision", traceID: span.traceID, fields: ["decision": "manual_bypass", "operationGeneration": String(operationGeneration)])
                    self.requestConversationList(using: context, operationGeneration: operationGeneration, span: span, completion: completion)
                    return
                }
                if let snapshot {
                    let age = Self.cacheAge(reconciliationTime: snapshot.lastSuccessfulReconciliationTime)
                    if age < Self.listCacheFreshnessInterval {
                        self.diagnostics.info(category: "conversation", name: "listCache.autoRefreshDecision", traceID: span.traceID, fields: ["decision": "recent_skip", "freshnessSeconds": String(Int(Self.listCacheFreshnessInterval)), "ageSeconds": String(format: "%.2f", age), "operationGeneration": String(operationGeneration)])
                        span.end(status: "ok", fields: ["source": "cache", "networkRequest": "skipped", "itemCount": String(self.conversations.count), "operationGeneration": String(operationGeneration)])
                        completion(.success(self.conversations))
                        return
                    }
                    self.diagnostics.info(category: "conversation", name: "listCache.autoRefreshDecision", traceID: span.traceID, fields: ["decision": "stale", "freshnessSeconds": String(Int(Self.listCacheFreshnessInterval)), "ageSeconds": age.isFinite ? String(format: "%.2f", age) : "invalid", "operationGeneration": String(operationGeneration)])
                } else {
                    self.diagnostics.info(category: "conversation", name: "listCache.autoRefreshDecision", traceID: span.traceID, fields: ["decision": "missing", "operationGeneration": String(operationGeneration)])
                }
                self.requestConversationList(using: context, operationGeneration: operationGeneration, span: span, completion: completion)
            }
        }
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
            let totalCount = (payload["total"] as? NSNumber)?.intValue
            var fields = ["httpStatus": String(response.statusCode), "byteCount": String(data.count), "itemCount": String(items.count), "operationGeneration": String(operationGeneration)]
            if let totalCount { fields["totalCount"] = String(totalCount) }
            self.finishListOperation(context: context, operationGeneration: operationGeneration, span: span, statusFields: fields, result: .success(items), totalCount: totalCount, completion: completion)
        }
    }

    private func finishListOperation(context: ConversationTransportContext, operationGeneration: Int, span: DiagnosticsSpan, statusFields: [String: String], result: Result<[ConversationSummary], Error>, totalCount: Int? = nil, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
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
                let reconciliation = self.reconcileConversationPage(items, totalCount: totalCount)
                self.conversations = reconciliation.items
                self.onConversationListChanged?()
                var reconcileFields = reconciliation.fields
                reconcileFields["pageCount"] = String(items.count)
                reconcileFields["resultCount"] = String(reconciliation.items.count)
                self.diagnostics.info(category: "conversation", name: "listCache.reconcile", traceID: span.traceID, fields: reconcileFields)
                self.diagnostics.info(category: "conversation", name: "list.response", traceID: span.traceID, fields: statusFields)
                self.persistConversationListCache(scope: context.scope, operationGeneration: operationGeneration, span: span, statusFields: statusFields, completion: completion)
            case .failure(let error):
                span.end(status: "failed", fields: statusFields)
                completion(.failure(error))
            }
        }
    }

    private func persistConversationListCache(scope: ConversationAccountScope, operationGeneration: Int, span: DiagnosticsSpan, statusFields: [String: String], completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        requireMainThread()
        let summaries = conversations
        let reconciliationTime = Date().timeIntervalSince1970
        let namespace = Self.cacheNamespace(for: scope)
        listCacheStore.write(namespace: namespace, summaries: summaries, reconciliationTime: reconciliationTime) { [weak self] writeResult in
            guard let self else { return }
            DispatchQueue.main.async {
                self.requireMainThread()
                guard self.activeAccountScope == scope else {
                    self.diagnostics.info(category: "conversation", name: "listCache.scopeRejected", traceID: span.traceID, fields: ["scopeHash": "sha256:\(namespace.prefix(12))", "reason": "account_changed_after_write"])
                    span.end(status: "discarded", fields: ["reason": "account_changed", "operationGeneration": String(operationGeneration)])
                    completion(.failure(ConversationRepositoryError.accountContextChanged))
                    return
                }
                guard self.listOperationGeneration == operationGeneration else {
                    self.diagnostics.info(category: "conversation", name: "listCache.scopeRejected", traceID: span.traceID, fields: ["scopeHash": "sha256:\(namespace.prefix(12))", "reason": "operation_superseded_after_write"])
                    span.end(status: "discarded", fields: ["reason": "operation_superseded", "operationGeneration": String(operationGeneration)])
                    completion(.failure(ConversationRepositoryError.operationSuperseded))
                    return
                }
                var finalFields = statusFields
                finalFields["resultCount"] = String(self.conversations.count)
                switch writeResult {
                case .success(let result):
                    self.diagnostics.info(category: "conversation", name: "listCache.write", traceID: span.traceID, fields: ["entryCount": String(summaries.count), "byteCount": String(result.byteCount), "durationMs": String(format: "%.2f", result.durationMs), "schema": String(ConversationListCacheStore.schemaVersion)])
                    finalFields["cacheWrite"] = "ok"
                case .failure(let error):
                    self.diagnostics.warning(category: "conversation", name: "listCache.write", fields: ["entryCount": String(summaries.count), "schema": String(ConversationListCacheStore.schemaVersion), "result": "failed", "errorType": String(describing: type(of: error))])
                    finalFields["cacheWrite"] = "failed"
                }
                span.end(status: "ok", fields: finalFields)
                completion(.success(self.conversations))
            }
        }
    }

    private func reconcileConversationPage(_ page: [ConversationSummary], totalCount: Int?) -> (items: [ConversationSummary], fields: [String: String]) {
        requireMainThread()
        let previous = conversations
        var previousByID: [String: ConversationSummary] = [:]
        var previousIndexByID: [String: Int] = [:]
        for (index, item) in previous.enumerated() {
            previousByID[item.id] = item
            previousIndexByID[item.id] = index
        }

        var seen = Set<String>()
        var authoritativePage: [ConversationSummary] = []
        var insertedCount = 0
        var updatedCount = 0
        var unchangedCount = 0
        for item in page where seen.insert(item.id).inserted {
            authoritativePage.append(item)
            if let old = previousByID[item.id] {
                if old.title != item.title || old.updateTime != item.updateTime { updatedCount += 1 } else { unchangedCount += 1 }
            } else {
                insertedCount += 1
            }
        }

        let offPageCandidates = previous.filter { !seen.contains($0.id) }
        let preservedOffPage: [ConversationSummary]
        if let totalCount {
            preservedOffPage = Array(offPageCandidates.prefix(max(0, totalCount - authoritativePage.count)))
        } else {
            preservedOffPage = offPageCandidates
        }
        let reconciled = authoritativePage + preservedOffPage
        let movedCount = reconciled.enumerated().reduce(0) { count, pair in
            let (index, item) = pair
            guard let previousIndex = previousIndexByID[item.id] else { return count }
            return count + (previousIndex == index ? 0 : 1)
        }
        var fields = ["insertedCount": String(insertedCount), "updatedCount": String(updatedCount), "movedCount": String(movedCount), "unchangedCount": String(unchangedCount), "preservedOffPageCount": String(preservedOffPage.count), "discardedExcessOffPageCount": String(max(0, offPageCandidates.count - preservedOffPage.count))]
        if let totalCount { fields["authoritativeTotalCount"] = String(totalCount) }
        return (reconciled, fields)
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
        provisionalCacheNamespace = nil
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

    private static func cacheNamespace(for scope: ConversationAccountScope) -> String {
        let value = scope.userID + "\u{0}" + scope.accountID
        return SHA256.hash(data: Data(value.utf8)).map { String(format: "%02x", $0) }.joined()
    }

    private static func cacheAge(reconciliationTime: TimeInterval) -> TimeInterval {
        let now = Date().timeIntervalSince1970
        guard reconciliationTime > 0, reconciliationTime <= now else { return .infinity }
        return now - reconciliationTime
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
        repository.onConversationListChanged = { [weak self] in self?.tableView.reloadData() }
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "ChatGPT"
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "ConversationCell")
        tableView.rowHeight = 58
        navigationItem.leftBarButtonItem = UIBarButtonItem(title: "设置", style: .plain, target: self, action: #selector(openSettings))
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadConversationsFromButton))
        refreshControl = UIRefreshControl()
        refreshControl?.tintColor = .secondaryLabel
        refreshControl?.addTarget(self, action: #selector(refreshControlChanged), for: .valueChanged)
        loadConversations(forceRefresh: false)
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
        guard repository.canOpenConversationFromList else {
            setListNavigationStatus("当前仅显示缓存")
            return
        }
        setListNavigationStatus()
        onSelectConversation?(repository.conversations[indexPath.row].id)
        tableView.reloadData()
    }

    func resetForAccountScopeChange() {
        loadPresentationGeneration += 1
        loading = false
        finishRefreshPresentation(reason: "account_scope_reset")
        setListNavigationStatus()
        navigationItem.rightBarButtonItem?.isEnabled = true
        errorView?.removeFromSuperview()
        errorView = nil
        tableView.reloadData()
    }

    @objc private func reloadConversationsFromButton() {
        diagnostics.info(category: "ui", name: "conversationList.manualRefreshRequested", fields: ["source": "button"])
        loadConversations(forceRefresh: true)
    }

    @objc private func refreshControlChanged() {
        diagnostics.info(category: "ui", name: "conversationList.manualRefreshRequested", fields: ["source": "pull"])
        loadConversations(forceRefresh: true)
    }

    private func loadConversations(forceRefresh: Bool) {
        guard !loading else {
            if forceRefresh { finishRefreshPresentation(reason: "ignored_existing_load") }
            return
        }
        loading = true
        loadPresentationGeneration += 1
        let presentationGeneration = loadPresentationGeneration
        errorView?.removeFromSuperview()
        errorView = nil
        setListNavigationStatus(forceRefresh ? "正在刷新…" : nil)
        navigationItem.rightBarButtonItem?.isEnabled = false
        repository.loadConversations(forceRefresh: forceRefresh) { [weak self] result in
            guard let self, self.loadPresentationGeneration == presentationGeneration else { return }
            self.loading = false
            self.finishRefreshPresentation(reason: "load_completed")
            self.navigationItem.rightBarButtonItem?.isEnabled = true
            switch result {
            case .success:
                self.tableView.reloadData()
                self.setListNavigationStatus(forceRefresh ? "已刷新 · \(self.repository.conversations.count) 条" : nil)
            case .failure(let error):
                guard !ConversationRepository.isLifecycleTermination(error) else { return }
                if !self.repository.conversations.isEmpty {
                    self.setListNavigationStatus(forceRefresh ? "刷新失败 · 当前显示缓存" : "网络不可用 · 当前显示缓存")
                    self.tableView.reloadData()
                    return
                }
                self.setListNavigationStatus()
                self.showError(error)
            }
        }
    }

    private func setListNavigationStatus(_ text: String? = nil) {
        navigationItem.prompt = nil
        title = text ?? "ChatGPT"
    }

    private func finishRefreshPresentation(reason: String) {
        let wasRefreshing = refreshControl?.isRefreshing ?? false
        let offsetBefore = tableView.contentOffset.y
        let insetBefore = tableView.adjustedContentInset.top
        if wasRefreshing { refreshControl?.endRefreshing() }
        diagnostics.info(category: "ui", name: "conversationList.refreshPresentation", fields: ["reason": reason, "wasRefreshing": wasRefreshing ? "true" : "false", "contentOffsetY": String(format: "%.2f", offsetBefore), "adjustedInsetTop": String(format: "%.2f", insetBefore)])
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
        retryButton.addTarget(self, action: #selector(reloadConversationsFromButton), for: .touchUpInside)

        var arrangedSubviews: [UIView] = [label, retryButton]
        if let repositoryError = error as? ConversationRepositoryError, repositoryError == .authenticationNotAvailable {
            let loginButton = UIButton(type: .system)
            loginButton.setTitle("登录 / 账户验证", for: .normal)
            loginButton.addTarget(self, action: #selector(openLogin), for: .touchUpInside)
            arrangedSubviews.append(loginButton)
        }

        let stack = UIStackView(arrangedSubviews: arrangedSubviews)
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

final class ConversationDetailViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    private struct ScrollAnchor {
        let messageID: String
        let relativeOffset: CGFloat
    }

    private enum AnswerJumpDirection: String {
        case previous
        case next
    }

    private let repository: ConversationRepository
    private let diagnostics = DiagnosticsLogger.shared
    private let preferences = AppPreferences.shared
    private let tableView = UITableView(frame: .zero, style: .plain)
    private let activityIndicator = UIActivityIndicatorView(style: .medium)
    private let stateLabel = UILabel()
    private let retryButton = UIButton(type: .system)
    private let syncToastView = UIView()
    private let syncToastLabel = UILabel()
    private let answerJumpButton = UIButton(type: .system)
    private let headerTitleLabel = UILabel()
    private let headerMetadataLabel = UILabel()
    private let headerStack = UIStackView()
    private var syncToastHideWorkItem: DispatchWorkItem?
    private var preferenceObserver: NSObjectProtocol?
    private var messages: [ConversationMessage] = []
    private var roundProjection = ConversationRoundProjection(rounds: [])
    private var answerRows: [Int] = []
    private var programmaticAnswerTargetRow: Int?
    private var answerJumpAnimationInFlight = false
    private var currentAnswerJumpDirection: AnswerJumpDirection?
    private var lastUserDragDirection: AnswerJumpDirection = .previous
    private var previousContentOffsetY: CGFloat = 0
    private var loadingConversationID: String?
    private var presentationGeneration = 0
    private var displayedConversationID: String?
    private var scrollAnchorsByConversationID: [String: ScrollAnchor] = [:]

    init(repository: ConversationRepository) {
        self.repository = repository
        super.init(nibName: nil, bundle: nil)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    deinit {
        if let preferenceObserver { NotificationCenter.default.removeObserver(preferenceObserver) }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        title = "新对话"

        headerTitleLabel.font = .systemFont(ofSize: 17, weight: .semibold)
        headerTitleLabel.textColor = .label
        headerTitleLabel.textAlignment = .center
        headerTitleLabel.lineBreakMode = .byTruncatingTail
        headerTitleLabel.setContentCompressionResistancePriority(.defaultLow, for: .horizontal)
        headerMetadataLabel.font = .systemFont(ofSize: 12, weight: .regular)
        headerMetadataLabel.textColor = .secondaryLabel
        headerMetadataLabel.textAlignment = .center
        headerMetadataLabel.lineBreakMode = .byTruncatingTail
        headerMetadataLabel.setContentCompressionResistancePriority(.defaultLow, for: .horizontal)
        headerStack.axis = .vertical
        headerStack.alignment = .center
        headerStack.spacing = 0
        headerStack.addArrangedSubview(headerTitleLabel)
        headerStack.addArrangedSubview(headerMetadataLabel)
        navigationItem.titleView = headerStack

        tableView.dataSource = self
        tableView.delegate = self
        tableView.separatorStyle = .none
        tableView.keyboardDismissMode = .interactive
        tableView.rowHeight = UITableView.automaticDimension
        tableView.estimatedRowHeight = UITableView.automaticDimension
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

        answerJumpButton.backgroundColor = .secondarySystemBackground
        answerJumpButton.tintColor = .label
        answerJumpButton.layer.cornerRadius = 22
        answerJumpButton.layer.shadowColor = UIColor.black.cgColor
        answerJumpButton.layer.shadowOpacity = 0.12
        answerJumpButton.layer.shadowRadius = 3
        answerJumpButton.layer.shadowOffset = CGSize(width: 0, height: 1)
        answerJumpButton.addTarget(self, action: #selector(jumpToAdjacentAnswer), for: .touchUpInside)
        answerJumpButton.isHidden = true
        answerJumpButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(answerJumpButton)

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
            answerJumpButton.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -14),
            answerJumpButton.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor, constant: -14),
            answerJumpButton.widthAnchor.constraint(equalToConstant: 44),
            answerJumpButton.heightAnchor.constraint(equalToConstant: 44),
            syncToastView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            syncToastView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            syncToastView.leadingAnchor.constraint(greaterThanOrEqualTo: view.leadingAnchor, constant: 36),
            syncToastView.trailingAnchor.constraint(lessThanOrEqualTo: view.trailingAnchor, constant: -36),
            syncToastLabel.leadingAnchor.constraint(equalTo: syncToastView.leadingAnchor, constant: 18),
            syncToastLabel.trailingAnchor.constraint(equalTo: syncToastView.trailingAnchor, constant: -18),
            syncToastLabel.topAnchor.constraint(equalTo: syncToastView.topAnchor, constant: 12),
            syncToastLabel.bottomAnchor.constraint(equalTo: syncToastView.bottomAnchor, constant: -12)
        ])

        preferenceObserver = NotificationCenter.default.addObserver(forName: AppPreferences.didChangeNotification, object: preferences, queue: .main) { [weak self] _ in self?.preferencesDidChange() }
        updateHeaderMetadata()
        updateConversationMenu()
    }

    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        updateAnswerJumpButton()
    }

    func showConversation(id: String) {
        guard repository.selectedConversationID == id else { return }
        captureScrollAnchorForDisplayedConversation()
        displayedConversationID = id
        programmaticAnswerTargetRow = nil
        answerJumpAnimationInFlight = false
        lastUserDragDirection = .previous
        previousContentOffsetY = tableView.contentOffset.y
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
            apply(detail, captureCurrentAnchor: false)
            logResidentFirstVisible(id: id, startedAt: presentationStart, operationKind: operationSnapshot?.kind)
        } else {
            loadingConversationID = id
            clearVisibleMessagePresentation()
            resetScrollPositionToTop()
            stateLabel.text = operationSnapshot?.kind == .reload ? "正在重新加载会话…" : "正在读取会话…"
            stateLabel.isHidden = false
            retryButton.isHidden = true
            activityIndicator.startAnimating()
        }

        updateHeaderMetadata()
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
        displayedConversationID = nil
        programmaticAnswerTargetRow = nil
        answerJumpAnimationInFlight = false
        scrollAnchorsByConversationID.removeAll()
        activityIndicator.stopAnimating()
        title = "新对话"
        clearVisibleMessagePresentation()
        resetScrollPositionToTop()
        stateLabel.text = "从侧边栏选择一个会话"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        updateHeaderMetadata()
        updateConversationMenu()
    }

    private func apply(_ detail: ConversationDetail, captureCurrentAnchor: Bool = true) {
        if captureCurrentAnchor, displayedConversationID == detail.id, !messages.isEmpty { captureScrollAnchor(for: detail.id) }
        displayedConversationID = detail.id
        title = detail.title
        messages = detail.messages
        rebuildRoundProjection()
        stateLabel.text = detail.messages.isEmpty ? "当前分支没有可显示的用户或助手文本消息" : nil
        stateLabel.isHidden = !detail.messages.isEmpty
        retryButton.isHidden = true
        tableView.reloadData()
        restoreScrollAnchor(for: detail.id)
        updateHeaderMetadata()
        updateAnswerJumpButton()
    }

    private func clearVisibleMessagePresentation() {
        messages = []
        roundProjection = ConversationRoundProjection(rounds: [])
        answerRows = []
        programmaticAnswerTargetRow = nil
        answerJumpAnimationInFlight = false
        currentAnswerJumpDirection = nil
        navigationItem.prompt = nil
        answerJumpButton.isHidden = true
        tableView.reloadData()
        updateHeaderMetadata()
    }

    private func rebuildRoundProjection() {
        roundProjection = ConversationRoundProjection.derive(from: messages)
        var rowsByMessageID: [String: Int] = [:]
        for (row, message) in messages.enumerated() where rowsByMessageID[message.id] == nil { rowsByMessageID[message.id] = row }
        answerRows = roundProjection.rounds.compactMap { rowsByMessageID[$0.userMessageID] }
        programmaticAnswerTargetRow = nil
        answerJumpAnimationInFlight = false
    }

    private func updateHeaderMetadata() {
        navigationItem.prompt = nil
        headerTitleLabel.text = title ?? "新对话"
        guard let id = displayedConversationID else {
            headerMetadataLabel.text = nil
            headerMetadataLabel.isHidden = true
            return
        }
        let hasAuthoritativeDetail = repository.selectedConversation?.id == id
        headerMetadataLabel.text = preferences.showsConversationRoundCount && hasAuthoritativeDetail ? "聊天 · \(roundProjection.rounds.count)轮" : "聊天"
        headerMetadataLabel.isHidden = false
    }

    private func preferencesDidChange() {
        updateHeaderMetadata()
        tableView.reloadData()
        updateAnswerJumpButton()
    }

    private func captureScrollAnchorForDisplayedConversation() {
        guard let id = displayedConversationID else { return }
        captureScrollAnchor(for: id)
    }

    private func captureScrollAnchor(for id: String) {
        guard !messages.isEmpty, let indexPath = tableView.indexPathsForVisibleRows?.min(by: { $0.row < $1.row }), messages.indices.contains(indexPath.row) else { return }
        let rowRect = tableView.rectForRow(at: indexPath)
        let relativeOffset = tableView.contentOffset.y - rowRect.minY
        scrollAnchorsByConversationID[id] = ScrollAnchor(messageID: messages[indexPath.row].id, relativeOffset: relativeOffset)
        var fields = repository.diagnosticsFields(for: id)
        fields["anchorRowIndex"] = String(indexPath.row)
        fields["relativeOffsetPoints"] = String(format: "%.2f", relativeOffset)
        diagnostics.info(category: "conversation", name: "scrollAnchor.saved", fields: fields)
    }

    private func restoreScrollAnchor(for id: String) {
        guard !messages.isEmpty else {
            resetScrollPositionToTop()
            return
        }
        guard let anchor = scrollAnchorsByConversationID[id] else {
            scrollToLatestMessage(for: id)
            return
        }
        guard let row = messages.firstIndex(where: { $0.id == anchor.messageID }) else {
            scrollAnchorsByConversationID.removeValue(forKey: id)
            resetScrollPositionToTop()
            var fields = repository.diagnosticsFields(for: id)
            fields["reason"] = "message_not_found"
            diagnostics.info(category: "conversation", name: "scrollAnchor.discarded", fields: fields)
            return
        }
        let indexPath = IndexPath(row: row, section: 0)
        view.layoutIfNeeded()
        tableView.layoutIfNeeded()
        tableView.scrollToRow(at: indexPath, at: .top, animated: false)
        tableView.layoutIfNeeded()
        setScrollOffsetY(tableView.rectForRow(at: indexPath).minY + anchor.relativeOffset)
        var fields = repository.diagnosticsFields(for: id)
        fields["anchorRowIndex"] = String(row)
        fields["relativeOffsetPoints"] = String(format: "%.2f", anchor.relativeOffset)
        diagnostics.info(category: "conversation", name: "scrollAnchor.restored", fields: fields)
    }

    private func scrollToLatestMessage(for id: String) {
        guard let lastRow = messages.indices.last else {
            resetScrollPositionToTop()
            return
        }
        view.layoutIfNeeded()
        tableView.layoutIfNeeded()
        tableView.scrollToRow(at: IndexPath(row: lastRow, section: 0), at: .bottom, animated: false)
        tableView.layoutIfNeeded()
        previousContentOffsetY = tableView.contentOffset.y
        var fields = repository.diagnosticsFields(for: id)
        fields["targetRowIndex"] = String(lastRow)
        fields["contentOffsetY"] = String(format: "%.2f", tableView.contentOffset.y)
        diagnostics.info(category: "conversation", name: "scrollAnchor.defaultLatest", fields: fields)
    }

    private func resetScrollPositionToTop() {
        view.layoutIfNeeded()
        tableView.layoutIfNeeded()
        setScrollOffsetY(-tableView.adjustedContentInset.top)
    }

    private func setScrollOffsetY(_ value: CGFloat) {
        let minimumY = -tableView.adjustedContentInset.top
        let maximumY = max(minimumY, tableView.contentSize.height - tableView.bounds.height + tableView.adjustedContentInset.bottom)
        tableView.setContentOffset(CGPoint(x: tableView.contentOffset.x, y: min(max(value, minimumY), maximumY)), animated: false)
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
        updateHeaderMetadata()
        updateAnswerJumpButton()
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

    private func copyVisibleMessage(_ message: ConversationMessage) {
        UIPasteboard.general.string = message.text
        diagnostics.info(category: "interaction", name: "message.copy", fields: ["role": message.role.rawValue])
        showSyncToast("已复制", autoHideAfter: 1.2)
    }

    private func lowerBoundAnswerIndex(for row: Int) -> Int {
        var lower = 0
        var upper = answerRows.count
        while lower < upper {
            let middle = lower + (upper - lower) / 2
            if answerRows[middle] < row { lower = middle + 1 } else { upper = middle }
        }
        return lower
    }

    private func adjacentAnswerRows() -> (previous: Int?, next: Int?) {
        guard answerRows.count >= 2, let visibleRows = tableView.indexPathsForVisibleRows?.map(\.row), let firstVisible = visibleRows.min(), let lastVisible = visibleRows.max() else { return (nil, nil) }
        let firstVisibleAnswerIndex = lowerBoundAnswerIndex(for: firstVisible)
        if firstVisibleAnswerIndex < answerRows.count, answerRows[firstVisibleAnswerIndex] <= lastVisible {
            let visibleMiddle = firstVisible + (lastVisible - firstVisible) / 2
            var currentIndex = firstVisibleAnswerIndex
            var index = firstVisibleAnswerIndex + 1
            while index < answerRows.count, answerRows[index] <= lastVisible {
                if abs(answerRows[index] - visibleMiddle) < abs(answerRows[currentIndex] - visibleMiddle) { currentIndex = index }
                index += 1
            }
            return (currentIndex > 0 ? answerRows[currentIndex - 1] : nil, currentIndex + 1 < answerRows.count ? answerRows[currentIndex + 1] : nil)
        }

        let referenceRow = firstVisible + (lastVisible - firstVisible) / 2
        let insertionIndex = lowerBoundAnswerIndex(for: referenceRow)
        let previous = insertionIndex > 0 ? answerRows[insertionIndex - 1] : nil
        let next = insertionIndex < answerRows.count ? answerRows[insertionIndex] : nil
        return (previous, next)
    }

    private func adjacentAnswerRows(relativeToAnswerRow row: Int) -> (previous: Int?, next: Int?) {
        let index = lowerBoundAnswerIndex(for: row)
        guard index < answerRows.count, answerRows[index] == row else { return adjacentAnswerRows() }
        return (index > 0 ? answerRows[index - 1] : nil, index + 1 < answerRows.count ? answerRows[index + 1] : nil)
    }

    private func effectiveAdjacentAnswerRows() -> (previous: Int?, next: Int?) {
        guard let targetRow = programmaticAnswerTargetRow else { return adjacentAnswerRows() }
        return adjacentAnswerRows(relativeToAnswerRow: targetRow)
    }

    private func answerTargetOffsetY(for row: Int) -> CGFloat {
        tableView.layoutIfNeeded()
        let rowRect = tableView.rectForRow(at: IndexPath(row: row, section: 0))
        let minimumY = -tableView.adjustedContentInset.top
        let maximumY = max(minimumY, tableView.contentSize.height - tableView.bounds.height + tableView.adjustedContentInset.bottom)
        return min(max(rowRect.minY - tableView.adjustedContentInset.top, minimumY), maximumY)
    }

    private func updateAnswerJumpButton() {
        guard preferences.showsAnswerQuickNavigation else {
            currentAnswerJumpDirection = nil
            answerJumpButton.isHidden = true
            return
        }
        let targets = effectiveAdjacentAnswerRows()
        let direction: AnswerJumpDirection?
        if targets.previous == nil { direction = targets.next == nil ? nil : .next }
        else if targets.next == nil { direction = .previous }
        else if programmaticAnswerTargetRow != nil, let currentAnswerJumpDirection { direction = currentAnswerJumpDirection }
        else { direction = lastUserDragDirection }
        guard let direction else {
            currentAnswerJumpDirection = nil
            answerJumpButton.isHidden = true
            return
        }
        if currentAnswerJumpDirection != direction {
            currentAnswerJumpDirection = direction
            answerJumpButton.setImage(UIImage(systemName: direction == .previous ? "chevron.up" : "chevron.down"), for: .normal)
            answerJumpButton.accessibilityLabel = direction == .previous ? "上一轮" : "下一轮"
        }
        if answerJumpButton.isHidden { answerJumpButton.isHidden = false }
    }

    @objc private func jumpToAdjacentAnswer() {
        let targets = effectiveAdjacentAnswerRows()
        guard let direction = currentAnswerJumpDirection else { return }
        let targetRow = direction == .previous ? targets.previous : targets.next
        guard let targetRow, messages.indices.contains(targetRow) else {
            updateAnswerJumpButton()
            return
        }
        let retargeting = answerJumpAnimationInFlight
        if retargeting { tableView.setContentOffset(tableView.contentOffset, animated: false) }
        let currentOffsetY = tableView.contentOffset.y
        programmaticAnswerTargetRow = targetRow
        answerJumpAnimationInFlight = true
        diagnostics.info(category: "interaction", name: "answerJump.requested", fields: ["direction": direction.rawValue, "targetRow": String(targetRow), "targetRole": "user", "retargeting": retargeting ? "true" : "false", "currentOffsetY": String(format: "%.2f", currentOffsetY)])
        tableView.scrollToRow(at: IndexPath(row: targetRow, section: 0), at: .top, animated: true)
        updateAnswerJumpButton()
    }

    @objc private func reloadCurrentConversation() {
        guard let id = repository.selectedConversationID else { return }
        if let kind = repository.detailOperationSnapshot(for: id)?.kind, kind == .sync || kind == .reload { return }
        captureScrollAnchor(for: id)
        presentationGeneration += 1
        let currentPresentationGeneration = presentationGeneration
        hideSyncToast()
        diagnostics.info(category: "navigation", name: "conversation.detailReload.requested", fields: repository.diagnosticsFields(for: id))
        loadingConversationID = id
        clearVisibleMessagePresentation()
        resetScrollPositionToTop()
        stateLabel.text = "正在重新加载会话…"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        activityIndicator.startAnimating()
        repository.reloadConversation(id: id) { [weak self] result in
            guard let self, self.repository.selectedConversationID == id, self.presentationGeneration == currentPresentationGeneration else { return }
            self.loadingConversationID = nil
            self.activityIndicator.stopAnimating()
            switch result {
            case .success(let detail): self.apply(detail, captureCurrentAnchor: false)
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

    func scrollViewWillBeginDragging(_ scrollView: UIScrollView) {
        answerJumpAnimationInFlight = false
        programmaticAnswerTargetRow = nil
        previousContentOffsetY = scrollView.contentOffset.y
        updateAnswerJumpButton()
    }

    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        let currentY = scrollView.contentOffset.y
        if scrollView.isDragging {
            let delta = currentY - previousContentOffsetY
            let newDirection: AnswerJumpDirection?
            if delta > 0.5 { newDirection = .next }
            else if delta < -0.5 { newDirection = .previous }
            else { newDirection = nil }
            if let newDirection, newDirection != lastUserDragDirection {
                lastUserDragDirection = newDirection
                updateAnswerJumpButton()
            }
        }
        previousContentOffsetY = currentY
    }

    func scrollViewDidEndDragging(_ scrollView: UIScrollView, willDecelerate decelerate: Bool) {
        if !decelerate { updateAnswerJumpButton() }
    }

    func scrollViewDidEndDecelerating(_ scrollView: UIScrollView) { updateAnswerJumpButton() }

    func scrollViewDidEndScrollingAnimation(_ scrollView: UIScrollView) {
        answerJumpAnimationInFlight = false
        if let targetRow = programmaticAnswerTargetRow, messages.indices.contains(targetRow) {
            let indexPath = IndexPath(row: targetRow, section: 0)
            tableView.scrollToRow(at: indexPath, at: .top, animated: false)
            tableView.layoutIfNeeded()
            let targetOffsetY = answerTargetOffsetY(for: targetRow)
            let landingError = tableView.contentOffset.y - targetOffsetY
            diagnostics.info(category: "interaction", name: "answerJump.completed", fields: ["targetRow": String(targetRow), "targetRole": "user", "landingErrorPoints": String(format: "%.2f", landingError)])
        }
        updateAnswerJumpButton()
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int { messages.count }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: ConversationMessageCell.reuseIdentifier, for: indexPath) as! ConversationMessageCell
        let message = messages[indexPath.row]
        cell.configure(with: message, showTimestamp: preferences.showsMessageTimestamps, onCopy: message.role == .assistant ? { [weak self] in self?.copyVisibleMessage(message) } : nil)
        return cell
    }

    func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration? {
        guard messages.indices.contains(indexPath.row) else { return nil }
        let message = messages[indexPath.row]
        guard message.role == .user else { return nil }
        return UIContextMenuConfiguration(identifier: message.id as NSString, previewProvider: nil) { [weak self] _ in
            let copy = UIAction(title: "复制", image: UIImage(systemName: "doc.on.doc")) { [weak self] _ in self?.copyVisibleMessage(message) }
            return UIMenu(children: [copy])
        }
    }
}

final class ConversationMessageCell: UITableViewCell {
    static let reuseIdentifier = "ConversationMessageCell"

    private let bubbleView = UIView()
    private let messageLabel = UILabel()
    private let timestampLabel = UILabel()
    private let actionStack = UIStackView()
    private let copyButton = UIButton(type: .system)
    private var onCopy: (() -> Void)?
    private var userLeadingConstraint: NSLayoutConstraint!
    private var userTrailingConstraint: NSLayoutConstraint!
    private var assistantLeadingConstraint: NSLayoutConstraint!
    private var assistantTrailingConstraint: NSLayoutConstraint!
    private var maxWidthConstraint: NSLayoutConstraint!
    private var timestampLeadingConstraint: NSLayoutConstraint!
    private var timestampTrailingConstraint: NSLayoutConstraint!
    private var actionLeadingConstraint: NSLayoutConstraint!
    private var timestampToBubbleConstraint: NSLayoutConstraint!
    private var bubbleToActionConstraint: NSLayoutConstraint!

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        selectionStyle = .none
        backgroundColor = .systemBackground
        contentView.backgroundColor = .systemBackground

        timestampLabel.font = .preferredFont(forTextStyle: .caption2)
        timestampLabel.textColor = .tertiaryLabel
        timestampLabel.setContentCompressionResistancePriority(.defaultLow, for: .horizontal)
        timestampLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(timestampLabel)

        bubbleView.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(bubbleView)
        messageLabel.font = .preferredFont(forTextStyle: .body)
        messageLabel.numberOfLines = 0
        messageLabel.translatesAutoresizingMaskIntoConstraints = false
        bubbleView.addSubview(messageLabel)

        let copyImage = UIImage(systemName: "doc.on.doc", withConfiguration: UIImage.SymbolConfiguration(pointSize: 10, weight: .regular))
        copyButton.setImage(copyImage, for: .normal)
        copyButton.tintColor = .secondaryLabel
        copyButton.backgroundColor = .clear
        copyButton.contentHorizontalAlignment = .left
        copyButton.accessibilityLabel = "复制"
        copyButton.addTarget(self, action: #selector(copyTapped), for: .touchUpInside)
        copyButton.widthAnchor.constraint(equalToConstant: 28).isActive = true
        copyButton.heightAnchor.constraint(equalToConstant: 28).isActive = true
        actionStack.axis = .horizontal
        actionStack.alignment = .center
        actionStack.spacing = 0
        actionStack.addArrangedSubview(copyButton)
        actionStack.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(actionStack)

        userLeadingConstraint = bubbleView.leadingAnchor.constraint(greaterThanOrEqualTo: contentView.layoutMarginsGuide.leadingAnchor, constant: 44)
        userTrailingConstraint = bubbleView.trailingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.trailingAnchor)
        assistantLeadingConstraint = bubbleView.leadingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.leadingAnchor)
        assistantTrailingConstraint = bubbleView.trailingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.trailingAnchor)
        maxWidthConstraint = bubbleView.widthAnchor.constraint(lessThanOrEqualTo: contentView.widthAnchor, multiplier: 0.82)
        timestampLeadingConstraint = timestampLabel.leadingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.leadingAnchor)
        timestampTrailingConstraint = timestampLabel.trailingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.trailingAnchor)
        actionLeadingConstraint = actionStack.leadingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.leadingAnchor)
        timestampToBubbleConstraint = bubbleView.topAnchor.constraint(equalTo: timestampLabel.bottomAnchor, constant: 3)
        bubbleToActionConstraint = actionStack.topAnchor.constraint(equalTo: bubbleView.bottomAnchor, constant: 4)

        NSLayoutConstraint.activate([
            timestampLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 7),
            timestampLeadingConstraint,
            timestampTrailingConstraint,
            timestampToBubbleConstraint,
            messageLabel.leadingAnchor.constraint(equalTo: bubbleView.leadingAnchor, constant: 12),
            messageLabel.trailingAnchor.constraint(equalTo: bubbleView.trailingAnchor, constant: -12),
            messageLabel.topAnchor.constraint(equalTo: bubbleView.topAnchor, constant: 9),
            messageLabel.bottomAnchor.constraint(equalTo: bubbleView.bottomAnchor, constant: -9),
            bubbleToActionConstraint,
            actionLeadingConstraint,
            actionStack.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -7)
        ])
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func prepareForReuse() {
        super.prepareForReuse()
        onCopy = nil
    }

    func configure(with message: ConversationMessage, showTimestamp: Bool, onCopy: (() -> Void)?) {
        self.onCopy = onCopy
        messageLabel.text = message.text
        timestampLabel.text = showTimestamp ? Self.timestampText(for: message.createTime) : nil
        timestampLabel.isHidden = timestampLabel.text == nil
        timestampToBubbleConstraint.constant = timestampLabel.isHidden ? 0 : 3
        NSLayoutConstraint.deactivate([userLeadingConstraint, userTrailingConstraint, assistantLeadingConstraint, assistantTrailingConstraint, maxWidthConstraint])
        switch message.role {
        case .user:
            bubbleView.backgroundColor = .secondarySystemBackground
            bubbleView.layer.cornerRadius = 18
            copyButton.isHidden = true
            bubbleToActionConstraint.constant = 0
            timestampLabel.textAlignment = .right
            NSLayoutConstraint.activate([userLeadingConstraint, userTrailingConstraint, maxWidthConstraint])
        case .assistant:
            bubbleView.backgroundColor = .clear
            bubbleView.layer.cornerRadius = 0
            copyButton.isHidden = false
            bubbleToActionConstraint.constant = 4
            timestampLabel.textAlignment = .left
            NSLayoutConstraint.activate([assistantLeadingConstraint, assistantTrailingConstraint])
        }
    }

    @objc private func copyTapped() { onCopy?() }

    private static func timestampText(for createTime: TimeInterval?) -> String? {
        guard let createTime, createTime > 0 else { return nil }
        let date = Date(timeIntervalSince1970: createTime)
        let formatter = DateFormatter()
        formatter.locale = Locale.autoupdatingCurrent
        formatter.timeZone = TimeZone.autoupdatingCurrent
        if Calendar.autoupdatingCurrent.isDate(date, inSameDayAs: Date()) {
            formatter.dateStyle = .none
            formatter.timeStyle = .short
        } else {
            formatter.dateStyle = .medium
            formatter.timeStyle = .short
        }
        return formatter.string(from: date)
    }
}