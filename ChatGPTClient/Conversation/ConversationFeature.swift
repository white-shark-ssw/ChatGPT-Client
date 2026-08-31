import CryptoKit
import Foundation
import UIKit
import WebKit

struct ConversationSummary {
    let id: String
    let title: String
    let updateTime: TimeInterval?
}

struct ConversationResponseTimelineItem: Equatable {
    enum Kind: String {
        case reasoning
        case tool
    }

    let kind: Kind
    var text: String
    let toolSlot: Int?
    var completed: Bool

    static func reasoning(_ text: String) -> ConversationResponseTimelineItem { ConversationResponseTimelineItem(kind: .reasoning, text: text, toolSlot: nil, completed: false) }
    static func tool(slot: Int, title: String, completed: Bool) -> ConversationResponseTimelineItem { ConversationResponseTimelineItem(kind: .tool, text: title, toolSlot: slot, completed: completed) }
}

struct ConversationMessage {
    enum Role: String {
        case user
        case assistant
    }

    let id: String
    let role: Role
    let text: String
    let responseTimeline: [ConversationResponseTimelineItem]
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

struct ConversationMessagePresentationProjection {
    struct Row {
        let messageIndex: Int
        let chunkIndex: Int
        let chunkCount: Int
        let text: String

        var isFirstChunk: Bool { chunkIndex == 0 }
        var isLastChunk: Bool { chunkIndex == chunkCount - 1 }
    }

    static let chunkCharacterLimit = 1200
    static let empty = ConversationMessagePresentationProjection(rows: [], firstRowByMessageID: [:], chunkedMessageCount: 0, maxChunkCharacterCount: 0)

    let rows: [Row]
    let firstRowByMessageID: [String: Int]
    let chunkedMessageCount: Int
    let maxChunkCharacterCount: Int

    static func derive(from messages: [ConversationMessage]) -> ConversationMessagePresentationProjection {
        var rows: [Row] = []
        var firstRowByMessageID: [String: Int] = [:]
        var chunkedMessageCount = 0
        var maxChunkCharacterCount = 0
        for (messageIndex, message) in messages.enumerated() {
            let chunks = presentationChunks(for: message.text)
            if chunks.count > 1 { chunkedMessageCount += 1 }
            for (chunkIndex, chunk) in chunks.enumerated() {
                if firstRowByMessageID[message.id] == nil { firstRowByMessageID[message.id] = rows.count }
                maxChunkCharacterCount = max(maxChunkCharacterCount, chunk.count)
                rows.append(Row(messageIndex: messageIndex, chunkIndex: chunkIndex, chunkCount: chunks.count, text: chunk))
            }
        }
        return ConversationMessagePresentationProjection(rows: rows, firstRowByMessageID: firstRowByMessageID, chunkedMessageCount: chunkedMessageCount, maxChunkCharacterCount: maxChunkCharacterCount)
    }

    private static func presentationChunks(for text: String) -> [String] {
        guard text.count > chunkCharacterLimit else { return [text] }
        var chunks: [String] = []
        var start = text.startIndex
        while start < text.endIndex {
            guard let hardEnd = text.index(start, offsetBy: chunkCharacterLimit, limitedBy: text.endIndex) else {
                chunks.append(String(text[start...]))
                break
            }
            var end = hardEnd
            if hardEnd < text.endIndex {
                let preferredRange = start..<hardEnd
                if let newline = text.range(of: "\n", options: .backwards, range: preferredRange), text.distance(from: start, to: newline.upperBound) >= chunkCharacterLimit / 2 {
                    end = newline.upperBound
                } else if let whitespace = text.rangeOfCharacter(from: .whitespaces, options: .backwards, range: preferredRange), text.distance(from: start, to: whitespace.upperBound) >= chunkCharacterLimit * 3 / 4 {
                    end = whitespace.upperBound
                }
            }
            if end == start { end = text.index(after: start) }
            chunks.append(String(text[start..<end]))
            start = end
        }
        return chunks.isEmpty ? [text] : chunks
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

            let projection = Self.parseCurrentBranch(mapping: mapping, currentNode: currentNode)
            let messages = projection.messages
            let title = Self.normalizedTitle(payload["title"] as? String)
            let detail = ConversationDetail(id: id, title: title, currentNodeID: currentNode, messages: messages)
            var fields = callbackFields
            fields["httpStatus"] = String(response.statusCode)
            fields["byteCount"] = String(data.count)
            fields["mappingCount"] = String(mapping.count)
            fields["visibleMessageCount"] = String(messages.count)
            fields["filteredRecipientMessageCount"] = String(projection.filteredRecipientMessageCount)
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
            return count + ((old.role != message.role || old.text != message.text || old.responseTimeline != message.responseTimeline || old.createTime != message.createTime) ? 1 : 0)
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

    private static func approximateTextBytes(_ detail: ConversationDetail) -> Int { detail.messages.reduce(0) { $0 + $1.text.utf8.count + $1.responseTimeline.reduce(0) { $0 + $1.text.utf8.count } } }

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

    private static func parseCurrentBranch(mapping: [String: Any], currentNode: String) -> (messages: [ConversationMessage], filteredRecipientMessageCount: Int) {
    var nodeIDs: [String] = []
    var visited = Set<String>()
    var nodeID: String? = currentNode
    while let currentID = nodeID, !currentID.isEmpty, visited.insert(currentID).inserted {
        nodeIDs.append(currentID)
        guard let node = mapping[currentID] as? [String: Any] else { break }
        nodeID = node["parent"] as? String
    }

    var messages: [ConversationMessage] = []
    var filteredRecipientMessageCount = 0
    var pendingTimeline: [ConversationResponseTimelineItem] = []
    var pendingToolIndexByServiceID: [String: Int] = [:]
    for id in nodeIDs.reversed() {
        guard let node = mapping[id] as? [String: Any], let message = node["message"] as? [String: Any], let author = message["author"] as? [String: Any], let rawRole = author["role"] as? String else { continue }
        let metadata = message["metadata"] as? [String: Any]
        if rawRole == "tool" {
            if message["status"] as? String == "finished_successfully", message["recipient"] as? String == "all", let parentID = metadata?["parent_id"] as? String, let index = pendingToolIndexByServiceID[parentID], pendingTimeline.indices.contains(index), pendingTimeline[index].kind == .tool {
                pendingTimeline[index].completed = true
            }
            continue
        }
        guard let role = ConversationMessage.Role(rawValue: rawRole), let content = message["content"] as? [String: Any] else { continue }
        if role == .assistant, let recipient = message["recipient"] as? String {
            let normalizedRecipient = recipient.trimmingCharacters(in: .whitespacesAndNewlines)
            if !normalizedRecipient.isEmpty, normalizedRecipient != "all" {
                filteredRecipientMessageCount += 1
                if message["status"] as? String == "finished_successfully", content["content_type"] as? String == "code", (metadata?["is_complete"] as? Bool) == true {
                    let rawTitle = (metadata?["reasoning_title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
                    let title = rawTitle.isEmpty ? "工具调用" : String(rawTitle.prefix(160))
                    let serviceID = (message["id"] as? String).flatMap { $0.isEmpty ? nil : $0 } ?? id
                    pendingToolIndexByServiceID[serviceID] = pendingTimeline.count
                    pendingTimeline.append(.tool(slot: pendingTimeline.count, title: title, completed: false))
                }
                continue
            }
        }
        if role == .assistant, let summary = collapsedReasoningSummary(from: message, content: content) {
            if !pendingTimeline.contains(where: { $0.kind == .reasoning }) { pendingTimeline.append(.reasoning(summary)) }
            continue
        }
        let isThinkingPreamble = role == .assistant && (metadata?["is_thinking_preamble_message"] as? Bool) == true
        if isThinkingPreamble {
            let reasoning = visibleText(from: content)
            if !reasoning.isEmpty { pendingTimeline.append(.reasoning(reasoning)) }
            continue
        }
        if role == .assistant, let contentType = content["content_type"] as? String, contentType == "thoughts" || contentType == "inline_cot_expandable_content" { continue }
        let visible = visibleText(from: content)
        guard !visible.isEmpty else { continue }
        if role == .user {
            pendingTimeline.removeAll()
            pendingToolIndexByServiceID.removeAll()
        }
        let timeline = role == .assistant ? pendingTimeline : []
        let messageID = (message["id"] as? String).flatMap { $0.isEmpty ? nil : $0 } ?? id
        messages.append(ConversationMessage(id: messageID, role: role, text: visible, responseTimeline: timeline, createTime: (message["create_time"] as? NSNumber)?.doubleValue))
        if role == .assistant {
            pendingTimeline.removeAll()
            pendingToolIndexByServiceID.removeAll()
        }
    }
    return (messages, filteredRecipientMessageCount)
}

    private static func collapsedReasoningSummary(from message: [String: Any], content: [String: Any]) -> String? {
    guard message["status"] as? String == "finished_successfully", message["recipient"] as? String == "all", content["content_type"] as? String == "reasoning_recap", let rawSummary = content["content"] as? String else { return nil }
    let summary = rawSummary.trimmingCharacters(in: .whitespacesAndNewlines)
    guard !summary.isEmpty, let metadata = message["metadata"] as? [String: Any], metadata["reasoning_status"] as? String == "reasoning_ended", metadata["reasoning_recap_type"] as? String == "collapse" else { return nil }
    return summary
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
        let chunkIndex: Int
        let relativeOffset: CGFloat
    }

    private enum AnswerJumpDirection: String {
        case previous
        case next
    }

    private static let answerJumpAnimationDuration: TimeInterval = 0.35

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
    private var messagePresentation = ConversationMessagePresentationProjection.empty
    private var livePresentationMessage: ConversationMessage?
    private var liveMessagePresentation = ConversationMessagePresentationProjection.empty
    private var livePresentationRowMetrics: [ConversationMessageCell.Metrics] = []
    private var livePresentationContentHeight: CGFloat = 0
    private var expandedReasoningMessageIDsByConversationID: [String: Set<String>] = [:]
    private var presentationRowMetrics: [ConversationMessageCell.Metrics] = []
    private var presentationRowOffsets: [CGFloat] = []
    private var presentationContentHeight: CGFloat = 0
    private var presentationLayoutWidth: CGFloat = 0
    private var answerRows: [Int] = []
    private var programmaticAnswerTargetRow: Int?
    private var answerJumpAnimator: UIViewPropertyAnimator?
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
        answerJumpAnimator?.stopAnimation(true)
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
        tableView.rowHeight = 44
        tableView.estimatedRowHeight = 44
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
        let width = tableView.bounds.width
        if (!messagePresentation.rows.isEmpty || !liveMessagePresentation.rows.isEmpty), width > 1, abs(width - presentationLayoutWidth) > 0.5 {
            let id = displayedConversationID
            if let id { captureScrollAnchor(for: id) }
            let durationMs = rebuildPresentationGeometry(width: width)
            rebuildLiveResponsePresentation(width: width)
            reloadMessageTable(reason: "width_change", restoreConversationID: id)
            diagnostics.info(category: "ui", name: "messagePresentation.geometryRebuilt", fields: ["reason": "width_change", "durationMs": String(format: "%.2f", durationMs), "presentationRowCount": String(messagePresentation.rows.count), "layoutWidthPoints": String(format: "%.2f", width), "contentHeightPoints": String(format: "%.2f", presentationContentHeight)])
        }
        updateAnswerJumpButton()
    }

    func showConversation(id: String) {
        guard repository.selectedConversationID == id else { return }
        stopAnswerJumpAnimation(clearTarget: true)
        captureScrollAnchorForDisplayedConversation()
        displayedConversationID = id
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
        stopAnswerJumpAnimation(clearTarget: true)
        hideSyncToast()
        loadingConversationID = nil
        displayedConversationID = nil
        scrollAnchorsByConversationID.removeAll()
        expandedReasoningMessageIDsByConversationID.removeAll()
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
        rebuildLiveResponsePresentation(width: effectivePresentationWidth())
        stateLabel.text = detail.messages.isEmpty ? "当前分支没有可显示的用户或助手文本消息" : nil
        stateLabel.isHidden = !detail.messages.isEmpty
        retryButton.isHidden = true
        reloadMessageTable(reason: "detail_apply", restoreConversationID: detail.id)
        updateHeaderMetadata()
        updateAnswerJumpButton()
    }

    private func clearVisibleMessagePresentation() {
        stopAnswerJumpAnimation(clearTarget: true)
        messages = []
        roundProjection = ConversationRoundProjection(rounds: [])
        messagePresentation = .empty
        livePresentationMessage = nil
        liveMessagePresentation = .empty
        livePresentationRowMetrics = []
        livePresentationContentHeight = 0
        presentationRowMetrics = []
        presentationRowOffsets = []
        presentationContentHeight = 0
        presentationLayoutWidth = 0
        answerRows = []
        currentAnswerJumpDirection = nil
        navigationItem.prompt = nil
        answerJumpButton.isHidden = true
        tableView.reloadData()
        updateHeaderMetadata()
    }

    private func rebuildRoundProjection() {
        stopAnswerJumpAnimation(clearTarget: true)
        let startedAt = ProcessInfo.processInfo.systemUptime
        roundProjection = ConversationRoundProjection.derive(from: messages)
        messagePresentation = ConversationMessagePresentationProjection.derive(from: messages)
        let geometryDurationMs = rebuildPresentationGeometry(width: effectivePresentationWidth())
        answerRows = roundProjection.rounds.compactMap { messagePresentation.firstRowByMessageID[$0.userMessageID] }
        let totalDurationMs = (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
        diagnostics.info(category: "ui", name: "messagePresentation.rebuilt", fields: ["authoritativeMessageCount": String(messages.count), "presentationRowCount": String(messagePresentation.rows.count), "chunkedMessageCount": String(messagePresentation.chunkedMessageCount), "chunkCharacterLimit": String(ConversationMessagePresentationProjection.chunkCharacterLimit), "maxChunkCharacterCount": String(messagePresentation.maxChunkCharacterCount), "geometryDurationMs": String(format: "%.2f", geometryDurationMs), "durationMs": String(format: "%.2f", totalDurationMs), "layoutWidthPoints": String(format: "%.2f", presentationLayoutWidth), "contentHeightPoints": String(format: "%.2f", presentationContentHeight)])
    }

    private func effectivePresentationWidth() -> CGFloat {
        if tableView.bounds.width > 1 { return tableView.bounds.width }
        if view.bounds.width > 1 { return view.bounds.width }
        return UIScreen.main.bounds.width
    }

    @discardableResult
    private func rebuildPresentationGeometry(width: CGFloat) -> Double {
        let startedAt = ProcessInfo.processInfo.systemUptime
        let resolvedWidth = max(1, width)
        presentationLayoutWidth = resolvedWidth
        presentationRowMetrics.removeAll(keepingCapacity: true)
        presentationRowOffsets.removeAll(keepingCapacity: true)
        presentationRowMetrics.reserveCapacity(messagePresentation.rows.count)
        presentationRowOffsets.reserveCapacity(messagePresentation.rows.count)
        var offset: CGFloat = 0
        for row in messagePresentation.rows {
            guard messages.indices.contains(row.messageIndex) else { continue }
            let message = messages[row.messageIndex]
            let showsTimestamp = row.isFirstChunk && preferences.showsMessageTimestamps && (message.createTime ?? 0) > 0
            let showsCopy = message.role == .assistant && row.isLastChunk
            let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
            let reasoningExpanded = !responseTimeline.isEmpty && isReasoningExpanded(messageID: message.id)
            let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: showsTimestamp, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded)
            presentationRowOffsets.append(offset)
            presentationRowMetrics.append(metrics)
            offset += metrics.rowHeight
        }
        presentationContentHeight = offset
        return (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
    }

    private func rebuildLiveResponsePresentation(width: CGFloat) {
    let resolvedWidth = max(1, width)
    guard let id = displayedConversationID, let snapshot = repository.liveResponse(for: id) else {
        livePresentationMessage = nil
        liveMessagePresentation = .empty
        livePresentationRowMetrics = []
        livePresentationContentHeight = 0
        return
    }
    let bodyText: String
    if !snapshot.finalText.isEmpty { bodyText = snapshot.finalText }
    else {
        switch snapshot.phase {
        case .preparing: bodyText = "正在发送…"
        case .thinking, .reasoning: bodyText = "正在思考…"
        case .final: bodyText = "正在生成回答…"
        case .completed: bodyText = "正在同步最新消息…"
        case .failed: bodyText = "回答失败"
        }
    }
    let message = ConversationMessage(id: "local-live-response-\(snapshot.generation)", role: .assistant, text: bodyText, responseTimeline: snapshot.timeline, createTime: nil)
    livePresentationMessage = message
    liveMessagePresentation = ConversationMessagePresentationProjection.derive(from: [message])
    livePresentationRowMetrics.removeAll(keepingCapacity: true)
    livePresentationRowMetrics.reserveCapacity(liveMessagePresentation.rows.count)
    var height: CGFloat = 0
    let reasoningExpanded = !snapshot.timeline.isEmpty && (!snapshot.reasoningEnded || isReasoningExpanded(messageID: message.id))
    for row in liveMessagePresentation.rows {
        let showsCopy = !snapshot.phase.isActive && row.isLastChunk
        let metrics = ConversationMessageCell.metrics(for: row.text, role: .assistant, tableWidth: resolvedWidth, showsTimestamp: false, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: row.isFirstChunk ? snapshot.timeline : [], reasoningExpanded: reasoningExpanded)
        livePresentationRowMetrics.append(metrics)
        height += metrics.rowHeight
    }
    livePresentationContentHeight = height
}

    func liveResponseDidChange(id: String) {
    guard displayedConversationID == id, repository.selectedConversationID == id else { return }
    let boundsBefore = answerJumpScrollBounds()
    let wasAtPhysicalBottom = tableView.contentOffset.y >= boundsBefore.maximumY - 0.5
    rebuildLiveResponsePresentation(width: effectivePresentationWidth())
    tableView.reloadData()
    tableView.layoutIfNeeded()
    if wasAtPhysicalBottom { setScrollOffsetY(answerJumpScrollBounds().maximumY) }
    updateAnswerJumpButton()
    var fields = repository.diagnosticsFields(for: id)
    fields["livePresentationRowCount"] = String(liveMessagePresentation.rows.count)
    fields["liveContentHeightPoints"] = String(format: "%.2f", livePresentationContentHeight)
    fields["followedPhysicalBottom"] = wasAtPhysicalBottom ? "true" : "false"
    diagnostics.info(category: "ui", name: "liveResponse.presentationApplied", fields: fields)
}

    private func isReasoningExpanded(messageID: String) -> Bool {
    guard let id = displayedConversationID else { return false }
    return expandedReasoningMessageIDsByConversationID[id]?.contains(messageID) ?? false
}

    private func toggleReasoning(messageID: String) {
    guard let id = displayedConversationID else { return }
    if expandedReasoningMessageIDsByConversationID[id]?.contains(messageID) == true { expandedReasoningMessageIDsByConversationID[id]?.remove(messageID) }
    else { expandedReasoningMessageIDsByConversationID[id, default: []].insert(messageID) }
    if livePresentationMessage?.id == messageID {
        liveResponseDidChange(id: id)
        return
    }
    captureScrollAnchor(for: id)
    let durationMs = rebuildPresentationGeometry(width: effectivePresentationWidth())
    reloadMessageTable(reason: "reasoning_toggle", restoreConversationID: id)
    diagnostics.info(category: "interaction", name: "reasoningSummary.toggled", fields: ["expanded": isReasoningExpanded(messageID: messageID) ? "true" : "false", "geometryDurationMs": String(format: "%.2f", durationMs)])
}

    private func reloadMessageTable(reason: String, restoreConversationID: String?) {
        let startedAt = ProcessInfo.processInfo.systemUptime
        tableView.reloadData()
        tableView.layoutIfNeeded()
        let layoutDurationMs = (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
        diagnostics.info(category: "ui", name: "messagePresentation.applied", fields: ["reason": reason, "presentationRowCount": String(messagePresentation.rows.count), "livePresentationRowCount": String(liveMessagePresentation.rows.count), "layoutDurationMs": String(format: "%.2f", layoutDurationMs), "derivedContentHeightPoints": String(format: "%.2f", presentationContentHeight), "liveContentHeightPoints": String(format: "%.2f", livePresentationContentHeight), "tableContentHeightPoints": String(format: "%.2f", tableView.contentSize.height)])
        if let restoreConversationID { restoreScrollAnchor(for: restoreConversationID) }
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
        let id = displayedConversationID
        if let id { captureScrollAnchor(for: id) }
        if !messagePresentation.rows.isEmpty || !liveMessagePresentation.rows.isEmpty {
            let durationMs = rebuildPresentationGeometry(width: effectivePresentationWidth())
            rebuildLiveResponsePresentation(width: effectivePresentationWidth())
            reloadMessageTable(reason: "preferences", restoreConversationID: id)
            diagnostics.info(category: "ui", name: "messagePresentation.geometryRebuilt", fields: ["reason": "preferences", "durationMs": String(format: "%.2f", durationMs), "presentationRowCount": String(messagePresentation.rows.count), "layoutWidthPoints": String(format: "%.2f", presentationLayoutWidth), "contentHeightPoints": String(format: "%.2f", presentationContentHeight)])
        } else {
            tableView.reloadData()
        }
        updateAnswerJumpButton()
    }

    private func captureScrollAnchorForDisplayedConversation() {
        guard let id = displayedConversationID else { return }
        captureScrollAnchor(for: id)
    }

    private func captureScrollAnchor(for id: String) {
        guard !messagePresentation.rows.isEmpty, let indexPath = tableView.indexPathsForVisibleRows?.min(by: { $0.row < $1.row }), messagePresentation.rows.indices.contains(indexPath.row), presentationRowOffsets.indices.contains(indexPath.row) else { return }
        let presentationRow = messagePresentation.rows[indexPath.row]
        guard messages.indices.contains(presentationRow.messageIndex) else { return }
        let message = messages[presentationRow.messageIndex]
        let relativeOffset = tableView.contentOffset.y - presentationRowOffsets[indexPath.row]
        scrollAnchorsByConversationID[id] = ScrollAnchor(messageID: message.id, chunkIndex: presentationRow.chunkIndex, relativeOffset: relativeOffset)
        var fields = repository.diagnosticsFields(for: id)
        fields["anchorRowIndex"] = String(indexPath.row)
        fields["anchorChunkIndex"] = String(presentationRow.chunkIndex)
        fields["relativeOffsetPoints"] = String(format: "%.2f", relativeOffset)
        diagnostics.info(category: "conversation", name: "scrollAnchor.saved", fields: fields)
    }

    private func restoreScrollAnchor(for id: String) {
        guard !messagePresentation.rows.isEmpty else {
            resetScrollPositionToTop()
            return
        }
        guard let anchor = scrollAnchorsByConversationID[id] else {
            scrollToLatestMessage(for: id)
            return
        }
        guard let firstRow = messagePresentation.firstRowByMessageID[anchor.messageID] else {
            scrollAnchorsByConversationID.removeValue(forKey: id)
            resetScrollPositionToTop()
            var fields = repository.diagnosticsFields(for: id)
            fields["reason"] = "message_not_found"
            diagnostics.info(category: "conversation", name: "scrollAnchor.discarded", fields: fields)
            return
        }
        let row = firstRow + anchor.chunkIndex
        guard messagePresentation.rows.indices.contains(row), presentationRowOffsets.indices.contains(row), messages.indices.contains(messagePresentation.rows[row].messageIndex), messages[messagePresentation.rows[row].messageIndex].id == anchor.messageID else {
            scrollAnchorsByConversationID.removeValue(forKey: id)
            resetScrollPositionToTop()
            var fields = repository.diagnosticsFields(for: id)
            fields["reason"] = "chunk_not_found"
            diagnostics.info(category: "conversation", name: "scrollAnchor.discarded", fields: fields)
            return
        }
        setScrollOffsetY(presentationRowOffsets[row] + anchor.relativeOffset)
        var fields = repository.diagnosticsFields(for: id)
        fields["anchorRowIndex"] = String(row)
        fields["anchorChunkIndex"] = String(anchor.chunkIndex)
        fields["relativeOffsetPoints"] = String(format: "%.2f", anchor.relativeOffset)
        diagnostics.info(category: "conversation", name: "scrollAnchor.restored", fields: fields)
    }

    private func scrollToLatestMessage(for id: String) {
        guard let lastRow = messagePresentation.rows.indices.last else {
            resetScrollPositionToTop()
            return
        }
        setScrollOffsetY(answerJumpScrollBounds().maximumY)
        previousContentOffsetY = tableView.contentOffset.y
        var fields = repository.diagnosticsFields(for: id)
        fields["targetRowIndex"] = String(lastRow)
        fields["contentOffsetY"] = String(format: "%.2f", tableView.contentOffset.y)
        fields["derivedContentHeightPoints"] = String(format: "%.2f", presentationContentHeight)
        diagnostics.info(category: "conversation", name: "scrollAnchor.defaultLatest", fields: fields)
    }

    private func resetScrollPositionToTop() {
        setScrollOffsetY(-tableView.adjustedContentInset.top)
    }

    private func setScrollOffsetY(_ value: CGFloat) {
        let bounds = answerJumpScrollBounds()
        tableView.setContentOffset(CGPoint(x: tableView.contentOffset.x, y: min(max(value, bounds.minimumY), bounds.maximumY)), animated: false)
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
        return zip(previous, current).contains { old, new in old.id != new.id || old.role != new.role || old.text != new.text || old.responseTimeline != new.responseTimeline || old.createTime != new.createTime }
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
        let visibleMiddle = firstVisible + (lastVisible - firstVisible) / 2
        var visibleUserTarget: (row: Int, distance: Int)?
        for visibleRow in visibleRows where messagePresentation.rows.indices.contains(visibleRow) {
            let presentationRow = messagePresentation.rows[visibleRow]
            guard messages.indices.contains(presentationRow.messageIndex) else { continue }
            let message = messages[presentationRow.messageIndex]
            guard message.role == .user, let targetRow = messagePresentation.firstRowByMessageID[message.id] else { continue }
            let candidate = (row: targetRow, distance: abs(visibleRow - visibleMiddle))
            if visibleUserTarget == nil || candidate.distance < visibleUserTarget!.distance { visibleUserTarget = candidate }
        }
        if let visibleUserTarget {
            let currentIndex = lowerBoundAnswerIndex(for: visibleUserTarget.row)
            if currentIndex < answerRows.count, answerRows[currentIndex] == visibleUserTarget.row {
                return (currentIndex > 0 ? answerRows[currentIndex - 1] : nil, currentIndex + 1 < answerRows.count ? answerRows[currentIndex + 1] : nil)
            }
        }

        let firstVisibleAnswerIndex = lowerBoundAnswerIndex(for: firstVisible)
        if firstVisibleAnswerIndex < answerRows.count, answerRows[firstVisibleAnswerIndex] <= lastVisible {
            var currentIndex = firstVisibleAnswerIndex
            var index = firstVisibleAnswerIndex + 1
            while index < answerRows.count, answerRows[index] <= lastVisible {
                if abs(answerRows[index] - visibleMiddle) < abs(answerRows[currentIndex] - visibleMiddle) { currentIndex = index }
                index += 1
            }
            return (currentIndex > 0 ? answerRows[currentIndex - 1] : nil, currentIndex + 1 < answerRows.count ? answerRows[currentIndex + 1] : nil)
        }

        let insertionIndex = lowerBoundAnswerIndex(for: visibleMiddle)
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

    private func answerJumpScrollBounds() -> (minimumY: CGFloat, maximumY: CGFloat) {
        let minimumY = -tableView.adjustedContentInset.top
        let derivedContentHeight = presentationContentHeight + livePresentationContentHeight
        let contentHeight = derivedContentHeight > 0 ? derivedContentHeight : tableView.contentSize.height
        let maximumY = max(minimumY, contentHeight - tableView.bounds.height + tableView.adjustedContentInset.bottom)
        return (minimumY, maximumY)
    }

    private func answerTargetOffsetY(for row: Int) -> CGFloat {
        guard presentationRowOffsets.indices.contains(row) else { return tableView.contentOffset.y }
        let bounds = answerJumpScrollBounds()
        return min(max(presentationRowOffsets[row] - tableView.adjustedContentInset.top, bounds.minimumY), bounds.maximumY)
    }

    private func stopAnswerJumpAnimation(clearTarget: Bool) {
        if let animator = answerJumpAnimator {
            if animator.state == .active { animator.pauseAnimation() }
            let currentOffset = tableView.contentOffset
            animator.stopAnimation(true)
            answerJumpAnimator = nil
            tableView.setContentOffset(currentOffset, animated: false)
        }
        if clearTarget { programmaticAnswerTargetRow = nil }
    }

    private func updateAnswerJumpButton() {
        guard preferences.showsAnswerQuickNavigation else {
            currentAnswerJumpDirection = nil
            answerJumpButton.setTitle(nil, for: .normal)
            answerJumpButton.isHidden = true
            return
        }
        let targets = effectiveAdjacentAnswerRows()
        let bounds = answerJumpScrollBounds()
        let currentY = tableView.contentOffset.y
        let direction: AnswerJumpDirection?
        if targets.previous != nil, currentY >= bounds.maximumY - 0.5 { direction = .previous }
        else if targets.next != nil, currentY <= bounds.minimumY + 0.5 { direction = .next }
        else if targets.previous == nil { direction = targets.next == nil ? nil : .next }
        else if targets.next == nil { direction = .previous }
        else if programmaticAnswerTargetRow != nil, let currentAnswerJumpDirection { direction = currentAnswerJumpDirection }
        else { direction = lastUserDragDirection }
        guard let direction else {
            currentAnswerJumpDirection = nil
            answerJumpButton.setTitle(nil, for: .normal)
            answerJumpButton.isHidden = true
            return
        }
        if currentAnswerJumpDirection != direction || answerJumpButton.currentImage == nil {
            currentAnswerJumpDirection = direction
            answerJumpButton.setTitle(nil, for: .normal)
            answerJumpButton.setImage(UIImage(systemName: direction == .previous ? "chevron.up" : "chevron.down"), for: .normal)
            answerJumpButton.accessibilityLabel = direction == .previous ? "上一轮" : "下一轮"
        }
        if answerJumpButton.isHidden { answerJumpButton.isHidden = false }
    }

    @objc private func jumpToAdjacentAnswer() {
        let targets = effectiveAdjacentAnswerRows()
        guard let direction = currentAnswerJumpDirection else { return }
        let targetRow = direction == .previous ? targets.previous : targets.next
        guard let targetRow, messagePresentation.rows.indices.contains(targetRow) else {
            updateAnswerJumpButton()
            return
        }
        let retargeting = answerJumpAnimator != nil
        stopAnswerJumpAnimation(clearTarget: false)
        let currentOffsetY = tableView.contentOffset.y
        programmaticAnswerTargetRow = targetRow
        let finalOffsetY = answerTargetOffsetY(for: targetRow)
        let travelDistance = abs(finalOffsetY - currentOffsetY)
        diagnostics.info(category: "interaction", name: "answerJump.requested", fields: ["direction": direction.rawValue, "targetRow": String(targetRow), "targetRole": "user", "retargeting": retargeting ? "true" : "false", "currentOffsetY": String(format: "%.2f", currentOffsetY), "travelDistancePoints": String(format: "%.2f", travelDistance), "presentationMode": "continuous_geometry_animation"])
        updateAnswerJumpButton()
        guard travelDistance > 0.5 else {
            diagnostics.info(category: "interaction", name: "answerJump.completed", fields: ["targetRow": String(targetRow), "targetRole": "user", "presentationMode": "continuous_geometry_animation", "travelDistancePoints": String(format: "%.2f", travelDistance), "landingErrorPoints": String(format: "%.2f", tableView.contentOffset.y - finalOffsetY)])
            return
        }
        let finalOffset = CGPoint(x: tableView.contentOffset.x, y: finalOffsetY)
        let animator = UIViewPropertyAnimator(duration: Self.answerJumpAnimationDuration, curve: .easeInOut) { [weak self] in self?.tableView.contentOffset = finalOffset }
        answerJumpAnimator = animator
        animator.addCompletion { [weak self, weak animator] _ in
            guard let self, let animator, self.answerJumpAnimator === animator, self.programmaticAnswerTargetRow == targetRow else { return }
            self.answerJumpAnimator = nil
            let landingError = self.tableView.contentOffset.y - finalOffsetY
            self.diagnostics.info(category: "interaction", name: "answerJump.completed", fields: ["targetRow": String(targetRow), "targetRole": "user", "presentationMode": "continuous_geometry_animation", "travelDistancePoints": String(format: "%.2f", travelDistance), "landingErrorPoints": String(format: "%.2f", landingError)])
            self.updateAnswerJumpButton()
        }
        animator.startAnimation()
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
        stopAnswerJumpAnimation(clearTarget: true)
        previousContentOffsetY = scrollView.contentOffset.y
        updateAnswerJumpButton()
    }

    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        let currentY = scrollView.contentOffset.y
        if scrollView.isDragging {
            let delta = currentY - previousContentOffsetY
            let targets = effectiveAdjacentAnswerRows()
            let bounds = answerJumpScrollBounds()
            let newDirection: AnswerJumpDirection?
            if targets.previous != nil, currentY >= bounds.maximumY - 0.5 { newDirection = .previous }
            else if targets.next != nil, currentY <= bounds.minimumY + 0.5 { newDirection = .next }
            else if delta > 0.5 { newDirection = .next }
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

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int { messagePresentation.rows.count + liveMessagePresentation.rows.count }

    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
    if indexPath.row < messagePresentation.rows.count {
        guard presentationRowMetrics.indices.contains(indexPath.row) else { return 44 }
        return presentationRowMetrics[indexPath.row].rowHeight
    }
    let liveRow = indexPath.row - messagePresentation.rows.count
    guard livePresentationRowMetrics.indices.contains(liveRow) else { return 44 }
    return livePresentationRowMetrics[liveRow].rowHeight
}

    func tableView(_ tableView: UITableView, estimatedHeightForRowAt indexPath: IndexPath) -> CGFloat { self.tableView(tableView, heightForRowAt: indexPath) }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: ConversationMessageCell.reuseIdentifier, for: indexPath) as! ConversationMessageCell
    if indexPath.row < messagePresentation.rows.count {
        guard messagePresentation.rows.indices.contains(indexPath.row), presentationRowMetrics.indices.contains(indexPath.row) else { return cell }
        let presentationRow = messagePresentation.rows[indexPath.row]
        guard messages.indices.contains(presentationRow.messageIndex) else { return cell }
        let message = messages[presentationRow.messageIndex]
        let showsTimestamp = presentationRow.isFirstChunk && preferences.showsMessageTimestamps
        let showsCopy = message.role == .assistant && presentationRow.isLastChunk
        let responseTimeline = presentationRow.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
        let reasoningExpanded = !responseTimeline.isEmpty && isReasoningExpanded(messageID: message.id)
        cell.configure(with: message, text: presentationRow.text, showTimestamp: showsTimestamp, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, metrics: presentationRowMetrics[indexPath.row], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: responseTimeline.isEmpty ? nil : { [weak self] in self?.toggleReasoning(messageID: message.id) })
        return cell
    }
    let liveRow = indexPath.row - messagePresentation.rows.count
    guard let message = livePresentationMessage, liveMessagePresentation.rows.indices.contains(liveRow), livePresentationRowMetrics.indices.contains(liveRow), let id = displayedConversationID, let snapshot = repository.liveResponse(for: id) else { return cell }
    let presentationRow = liveMessagePresentation.rows[liveRow]
    let showsCopy = !snapshot.phase.isActive && presentationRow.isLastChunk
    let responseTimeline = presentationRow.isFirstChunk ? message.responseTimeline : []
    let reasoningExpanded = !responseTimeline.isEmpty && (!snapshot.reasoningEnded || isReasoningExpanded(messageID: message.id))
    let canToggleReasoning = !responseTimeline.isEmpty && snapshot.reasoningEnded
    cell.configure(with: message, text: presentationRow.text, showTimestamp: false, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, metrics: livePresentationRowMetrics[liveRow], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: canToggleReasoning ? { [weak self] in self?.toggleReasoning(messageID: message.id) } : nil)
    return cell
}

    func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration? {
    guard indexPath.row < messagePresentation.rows.count, messagePresentation.rows.indices.contains(indexPath.row) else { return nil }
    let presentationRow = messagePresentation.rows[indexPath.row]
    guard messages.indices.contains(presentationRow.messageIndex) else { return nil }
    let message = messages[presentationRow.messageIndex]
    guard message.role == .user else { return nil }
    return UIContextMenuConfiguration(identifier: message.id as NSString, previewProvider: nil) { [weak self] _ in
        let copy = UIAction(title: "复制", image: UIImage(systemName: "doc.on.doc")) { [weak self] _ in self?.copyVisibleMessage(message) }
        return UIMenu(children: [copy])
    }
}
}

final class ConversationMessageCell: UITableViewCell {
    struct Metrics {
        let rowHeight: CGFloat
        let timestampFrame: CGRect
        let bubbleFrame: CGRect
        let reasoningButtonFrame: CGRect
        let reasoningBodyFrame: CGRect
        let messageFrame: CGRect
        let copyFrame: CGRect
    }

    static let reuseIdentifier = "ConversationMessageCell"

    private static let horizontalMargin: CGFloat = 16
    private static let userLeadingGap: CGFloat = 44
    private static let userMaxWidthRatio: CGFloat = 0.82
    private static let bubbleHorizontalPadding: CGFloat = 12
    private static let bubbleVerticalPadding: CGFloat = 9
    private static let outerVerticalPadding: CGFloat = 7
    private static let timestampGap: CGFloat = 3
    private static let reasoningButtonHeight: CGFloat = 30
    private static let reasoningBodyGap: CGFloat = 4
    private static let reasoningMessageGap: CGFloat = 7
    private static let copyGap: CGFloat = 4
    private static let copySize: CGFloat = 28
    private static let bodyFont = UIFont.preferredFont(forTextStyle: .body)
    private static let reasoningFont = UIFont.preferredFont(forTextStyle: .subheadline)
    private static let toolFont = UIFont.systemFont(ofSize: reasoningFont.pointSize, weight: .medium)
    private static let timestampFont = UIFont.preferredFont(forTextStyle: .caption2)
    private static let timeFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.locale = Locale.autoupdatingCurrent
        formatter.timeZone = TimeZone.autoupdatingCurrent
        formatter.dateStyle = .none
        formatter.timeStyle = .short
        return formatter
    }()
    private static let dateTimeFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.locale = Locale.autoupdatingCurrent
        formatter.timeZone = TimeZone.autoupdatingCurrent
        formatter.dateStyle = .medium
        formatter.timeStyle = .short
        return formatter
    }()

    private let bubbleView = UIView()
    private let messageLabel = UILabel()
    private let reasoningButton = UIButton(type: .system)
    private let reasoningLabel = UILabel()
    private let timestampLabel = UILabel()
    private let copyButton = UIButton(type: .system)
    private var onCopy: (() -> Void)?
    private var onToggleReasoning: (() -> Void)?
    private var layoutMetrics = Metrics(rowHeight: 44, timestampFrame: .zero, bubbleFrame: .zero, reasoningButtonFrame: .zero, reasoningBodyFrame: .zero, messageFrame: .zero, copyFrame: .zero)

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        selectionStyle = .none
        backgroundColor = .systemBackground
        contentView.backgroundColor = .systemBackground
        timestampLabel.font = Self.timestampFont
        timestampLabel.textColor = .tertiaryLabel
        contentView.addSubview(timestampLabel)
        contentView.addSubview(bubbleView)
        reasoningButton.tintColor = .secondaryLabel
        reasoningButton.setTitleColor(.secondaryLabel, for: .normal)
        reasoningButton.titleLabel?.font = .preferredFont(forTextStyle: .subheadline)
        reasoningButton.contentHorizontalAlignment = .left
        reasoningButton.addTarget(self, action: #selector(reasoningTapped), for: .touchUpInside)
        bubbleView.addSubview(reasoningButton)
        reasoningLabel.numberOfLines = 0
        bubbleView.addSubview(reasoningLabel)
        messageLabel.font = Self.bodyFont
        messageLabel.numberOfLines = 0
        bubbleView.addSubview(messageLabel)
        let copyImage = UIImage(systemName: "square.on.square", withConfiguration: UIImage.SymbolConfiguration(pointSize: 10, weight: .regular))
        copyButton.setImage(copyImage, for: .normal)
        copyButton.tintColor = .secondaryLabel
        copyButton.backgroundColor = .clear
        copyButton.contentHorizontalAlignment = .left
        copyButton.accessibilityLabel = "复制"
        copyButton.addTarget(self, action: #selector(copyTapped), for: .touchUpInside)
        contentView.addSubview(copyButton)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func prepareForReuse() {
        super.prepareForReuse()
        onCopy = nil
        onToggleReasoning = nil
        messageLabel.text = nil
        reasoningLabel.attributedText = nil
        reasoningButton.setTitle(nil, for: .normal)
        reasoningButton.setImage(nil, for: .normal)
        timestampLabel.text = nil
        reasoningButton.isHidden = true
        reasoningLabel.isHidden = true
        copyButton.isHidden = true
    }

    override func layoutSubviews() {
        super.layoutSubviews()
        timestampLabel.frame = layoutMetrics.timestampFrame
        bubbleView.frame = layoutMetrics.bubbleFrame
        reasoningButton.frame = layoutMetrics.reasoningButtonFrame
        reasoningLabel.frame = layoutMetrics.reasoningBodyFrame
        messageLabel.frame = layoutMetrics.messageFrame
        copyButton.frame = layoutMetrics.copyFrame
    }

    func configure(with message: ConversationMessage, text: String, showTimestamp: Bool, showCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, metrics: Metrics, onCopy: (() -> Void)?, onToggleReasoning: (() -> Void)?) {
        self.onCopy = onCopy
        self.onToggleReasoning = onToggleReasoning
        layoutMetrics = metrics
        messageLabel.text = text
        let showsReasoning = message.role == .assistant && isFirstChunk && !responseTimeline.isEmpty
        reasoningButton.isHidden = !showsReasoning
        reasoningButton.isUserInteractionEnabled = onToggleReasoning != nil
        reasoningButton.setTitle(showsReasoning ? "思考过程" : nil, for: .normal)
        reasoningButton.setImage(showsReasoning ? UIImage(systemName: reasoningExpanded ? "chevron.down" : "chevron.right") : nil, for: .normal)
        reasoningLabel.attributedText = showsReasoning && reasoningExpanded ? Self.responseTimelineAttributedText(responseTimeline) : nil
        reasoningLabel.isHidden = reasoningLabel.attributedText == nil
        timestampLabel.text = showTimestamp ? Self.timestampText(for: message.createTime) : nil
        timestampLabel.isHidden = timestampLabel.text == nil
        copyButton.isHidden = !showCopy
        switch message.role {
        case .user:
            bubbleView.backgroundColor = .secondarySystemBackground
            bubbleView.layer.cornerRadius = 18
            if isFirstChunk && isLastChunk { bubbleView.layer.maskedCorners = [.layerMinXMinYCorner, .layerMaxXMinYCorner, .layerMinXMaxYCorner, .layerMaxXMaxYCorner] }
            else if isFirstChunk { bubbleView.layer.maskedCorners = [.layerMinXMinYCorner, .layerMaxXMinYCorner] }
            else if isLastChunk { bubbleView.layer.maskedCorners = [.layerMinXMaxYCorner, .layerMaxXMaxYCorner] }
            else { bubbleView.layer.maskedCorners = [] }
            timestampLabel.textAlignment = .right
        case .assistant:
            bubbleView.backgroundColor = .clear
            bubbleView.layer.cornerRadius = 0
            bubbleView.layer.maskedCorners = []
            timestampLabel.textAlignment = .left
        }
        setNeedsLayout()
    }

    static func metrics(for text: String, role: ConversationMessage.Role, tableWidth: CGFloat, showsTimestamp: Bool, showsCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool) -> Metrics {
        let width = max(1, tableWidth)
        var y = isFirstChunk ? outerVerticalPadding : 0
        var timestampFrame = CGRect.zero
        if showsTimestamp {
            let timestampHeight = ceil(timestampFont.lineHeight)
            timestampFrame = CGRect(x: horizontalMargin, y: y, width: max(1, width - horizontalMargin * 2), height: timestampHeight)
            y += timestampHeight + timestampGap
        }
        let maxBubbleWidth: CGFloat
        let maxTextWidth: CGFloat
        switch role {
        case .user:
            maxBubbleWidth = max(36, min(width * userMaxWidthRatio, width - horizontalMargin * 2 - userLeadingGap))
            maxTextWidth = max(1, maxBubbleWidth - bubbleHorizontalPadding * 2)
        case .assistant:
            maxBubbleWidth = max(1, width - horizontalMargin * 2)
            maxTextWidth = max(1, maxBubbleWidth - bubbleHorizontalPadding * 2)
        }
        let textSize = measuredTextSize(text, maxWidth: maxTextWidth)
        let bubbleWidth: CGFloat
        switch role {
        case .user: bubbleWidth = isChunked ? maxBubbleWidth : min(maxBubbleWidth, max(36, ceil(textSize.width) + bubbleHorizontalPadding * 2))
        case .assistant: bubbleWidth = maxBubbleWidth
        }
        let bubbleX = role == .user ? width - horizontalMargin - bubbleWidth : horizontalMargin
        var bubbleY: CGFloat = isFirstChunk ? bubbleVerticalPadding : 0
        var reasoningButtonFrame = CGRect.zero
        var reasoningBodyFrame = CGRect.zero
        if role == .assistant, isFirstChunk, !responseTimeline.isEmpty {
            reasoningButtonFrame = CGRect(x: bubbleHorizontalPadding, y: bubbleY, width: maxTextWidth, height: reasoningButtonHeight)
            bubbleY = reasoningButtonFrame.maxY
            if reasoningExpanded {
                bubbleY += reasoningBodyGap
                let reasoningSize = measuredTimelineSize(responseTimeline, maxWidth: maxTextWidth)
                reasoningBodyFrame = CGRect(x: bubbleHorizontalPadding, y: bubbleY, width: maxTextWidth, height: reasoningSize.height)
                bubbleY = reasoningBodyFrame.maxY
            }
            bubbleY += reasoningMessageGap
        }
        let messageFrame = CGRect(x: bubbleHorizontalPadding, y: bubbleY, width: maxTextWidth, height: textSize.height)
        let bubbleHeight = messageFrame.maxY + (isLastChunk ? bubbleVerticalPadding : 0)
        let bubbleFrame = CGRect(x: bubbleX, y: y, width: bubbleWidth, height: bubbleHeight)
        y = bubbleFrame.maxY
        var copyFrame = CGRect.zero
        if showsCopy {
            y += copyGap
            copyFrame = CGRect(x: horizontalMargin, y: y, width: copySize, height: copySize)
            y = copyFrame.maxY
        }
        if isLastChunk { y += outerVerticalPadding }
        return Metrics(rowHeight: max(1, ceil(y)), timestampFrame: timestampFrame, bubbleFrame: bubbleFrame, reasoningButtonFrame: reasoningButtonFrame, reasoningBodyFrame: reasoningBodyFrame, messageFrame: messageFrame, copyFrame: copyFrame)
    }

    private static func responseTimelineAttributedText(_ timeline: [ConversationResponseTimelineItem]) -> NSAttributedString {
        let output = NSMutableAttributedString()
        for (index, item) in timeline.enumerated() {
            let normalized = item.text.trimmingCharacters(in: .whitespacesAndNewlines)
            guard !normalized.isEmpty else { continue }
            if output.length > 0 { output.append(NSAttributedString(string: "\n\n")) }
            switch item.kind {
            case .reasoning:
                output.append(NSAttributedString(string: normalized, attributes: [.font: reasoningFont, .foregroundColor: UIColor.secondaryLabel]))
            case .tool:
                let text = "\(item.completed ? "✓" : "•") \(normalized) · \(item.completed ? "已完成" : "调用中")"
                output.append(NSAttributedString(string: text, attributes: [.font: toolFont, .foregroundColor: UIColor.secondaryLabel]))
            }
        }
        return output
    }

    private static func measuredTextSize(_ text: String, maxWidth: CGFloat) -> CGSize {
        guard !text.isEmpty else { return CGSize(width: 0, height: ceil(bodyFont.lineHeight)) }
        let rect = (text as NSString).boundingRect(with: CGSize(width: maxWidth, height: .greatestFiniteMagnitude), options: [.usesLineFragmentOrigin, .usesFontLeading], attributes: [.font: bodyFont], context: nil)
        return CGSize(width: min(maxWidth, ceil(rect.width)), height: max(ceil(bodyFont.lineHeight), ceil(rect.height) + 1))
    }

    private static func measuredTimelineSize(_ timeline: [ConversationResponseTimelineItem], maxWidth: CGFloat) -> CGSize {
        let attributed = responseTimelineAttributedText(timeline)
        guard attributed.length > 0 else { return .zero }
        let rect = attributed.boundingRect(with: CGSize(width: maxWidth, height: .greatestFiniteMagnitude), options: [.usesLineFragmentOrigin, .usesFontLeading], context: nil)
        return CGSize(width: min(maxWidth, ceil(rect.width)), height: max(ceil(reasoningFont.lineHeight), ceil(rect.height) + 1))
    }

    @objc private func copyTapped() { onCopy?() }
    @objc private func reasoningTapped() { onToggleReasoning?() }

    private static func timestampText(for createTime: TimeInterval?) -> String? {
        guard let createTime, createTime > 0 else { return nil }
        let date = Date(timeIntervalSince1970: createTime)
        return Calendar.autoupdatingCurrent.isDate(date, inSameDayAs: Date()) ? timeFormatter.string(from: date) : dateTimeFormatter.string(from: date)
    }
}
