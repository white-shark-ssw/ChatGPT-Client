import CryptoKit
import Foundation
import OSLog

private enum DiagnosticsLevel: String, Codable {
    case debug
    case info
    case warning
    case error
    case fault

    var osLogType: OSLogType {
        switch self {
        case .debug: return .debug
        case .info: return .info
        case .warning: return .default
        case .error: return .error
        case .fault: return .fault
        }
    }
}

private struct DiagnosticsEvent: Codable {
    let id: UUID
    let timestamp: Date
    let level: DiagnosticsLevel
    let category: String
    let name: String
    let traceID: String?
    let fields: [String: String]

    init(id: UUID = UUID(), timestamp: Date = Date(), level: DiagnosticsLevel, category: String, name: String, traceID: String?, fields: [String: String]) {
        self.id = id
        self.timestamp = timestamp
        self.level = level
        self.category = category
        self.name = name
        self.traceID = traceID
        self.fields = fields
    }

    func redactedForExport() -> DiagnosticsEvent {
        DiagnosticsEvent(id: id, timestamp: timestamp, level: level, category: category, name: name, traceID: traceID, fields: DiagnosticsSanitizer.sanitizeExportFields(fields))
    }
}

private enum DiagnosticsSanitizer {
    private static let secretFragments = ["password", "token", "cookie", "authorization", "oauthcode", "secret", "credential", "messagebody", "requestbody", "responsebody", "attachmentcontent"]
    private static let hashedIdentifierKeys: Set<String> = ["accountid", "conversationid", "messageid", "sessionid", "userid", "workspaceid"]

    static func sanitizeLocalFields(_ fields: [String: String]) -> [String: String] {
        var sanitized: [String: String] = [:]
        for (key, value) in fields {
            let normalized = normalize(key)
            sanitized[key] = secretFragments.contains(where: { normalized.contains($0) }) ? "<redacted>" : value
        }
        return sanitized
    }

    static func sanitizeExportFields(_ fields: [String: String]) -> [String: String] {
        var sanitized = sanitizeLocalFields(fields)
        for (key, value) in sanitized where hashedIdentifierKeys.contains(normalize(key)) && value != "<redacted>" {
            sanitized[key] = "sha256:\(shortHash(value))"
        }
        return sanitized
    }

    private static func normalize(_ key: String) -> String {
        key.lowercased().replacingOccurrences(of: "_", with: "").replacingOccurrences(of: "-", with: "").replacingOccurrences(of: ".", with: "")
    }

    private static func shortHash(_ value: String) -> String {
        SHA256.hash(data: Data(value.utf8)).prefix(6).map { String(format: "%02x", $0) }.joined()
    }
}

private final class DiagnosticsStore {
    static let shared = DiagnosticsStore()

    private let queue = DispatchQueue(label: "com.whitesharkssw.chatgptclient.diagnostics.store")
    private let fileManager = FileManager.default
    private let currentURL: URL
    private let maxFileBytes = 2 * 1024 * 1024
    private let maxArchiveCount = 3

    private init() {
        let root = fileManager.urls(for: .applicationSupportDirectory, in: .userDomainMask).first ?? fileManager.temporaryDirectory
        let directory = root.appendingPathComponent("Diagnostics", isDirectory: true)
        try? fileManager.createDirectory(at: directory, withIntermediateDirectories: true)
        currentURL = directory.appendingPathComponent("events.jsonl")
    }

    func append(_ event: DiagnosticsEvent) {
        queue.async {
            do {
                let encoder = JSONEncoder()
                encoder.dateEncodingStrategy = .iso8601
                var data = try encoder.encode(event)
                data.append(0x0A)
                try self.rotateIfNeeded(additionalBytes: data.count)
                if !self.fileManager.fileExists(atPath: self.currentURL.path) {
                    self.fileManager.createFile(atPath: self.currentURL.path, contents: nil)
                }
                let handle = try FileHandle(forWritingTo: self.currentURL)
                handle.seekToEndOfFile()
                handle.write(data)
                handle.closeFile()
            } catch {
                NSLog("[DiagnosticsStore] append failed: %@", String(describing: error))
            }
        }
    }

    func snapshot() throws -> [DiagnosticsEvent] {
        try queue.sync { try loadEventsLocked() }
    }

    func flush() {
        queue.sync { }
    }

    func clear() throws {
        try queue.sync {
            let urls = [currentURL] + (1...maxArchiveCount).map(archiveURL)
            for url in urls where fileManager.fileExists(atPath: url.path) { try fileManager.removeItem(at: url) }
        }
    }

    private func rotateIfNeeded(additionalBytes: Int) throws {
        let attributes = try? fileManager.attributesOfItem(atPath: currentURL.path)
        let currentSize = (attributes?[.size] as? NSNumber)?.intValue ?? 0
        guard currentSize + additionalBytes > maxFileBytes else { return }

        for index in stride(from: maxArchiveCount, through: 1, by: -1) {
            let source = index == 1 ? currentURL : archiveURL(index - 1)
            let destination = archiveURL(index)
            if fileManager.fileExists(atPath: destination.path) { try fileManager.removeItem(at: destination) }
            if fileManager.fileExists(atPath: source.path) { try fileManager.moveItem(at: source, to: destination) }
        }
    }

    private func loadEventsLocked() throws -> [DiagnosticsEvent] {
        let urls = (1...maxArchiveCount).reversed().map(archiveURL) + [currentURL]
        let decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .iso8601
        var events: [DiagnosticsEvent] = []

        for url in urls where fileManager.fileExists(atPath: url.path) {
            let data = try Data(contentsOf: url)
            for line in data.split(separator: 0x0A) {
                events.append(try decoder.decode(DiagnosticsEvent.self, from: Data(line)))
            }
        }
        return events
    }

    private func archiveURL(_ index: Int) -> URL {
        currentURL.deletingLastPathComponent().appendingPathComponent("events.\(index).jsonl")
    }
}

final class DiagnosticsLogger {
    static let shared = DiagnosticsLogger()

    private let store = DiagnosticsStore.shared
    private let subsystem = Bundle.main.bundleIdentifier ?? "com.whitesharkssw.chatgptclient"

    private init() { }

    func debug(category: String, name: String, traceID: String? = nil, fields: [String: String] = [:]) {
        log(level: .debug, category: category, name: name, traceID: traceID, fields: fields)
    }

    func info(category: String, name: String, traceID: String? = nil, fields: [String: String] = [:]) {
        log(level: .info, category: category, name: name, traceID: traceID, fields: fields)
    }

    func warning(category: String, name: String, traceID: String? = nil, fields: [String: String] = [:]) {
        log(level: .warning, category: category, name: name, traceID: traceID, fields: fields)
    }

    func error(category: String, name: String, traceID: String? = nil, error: Error? = nil, fields: [String: String] = [:]) {
        var merged = fields
        if let error {
            let nsError = error as NSError
            merged["errorDomain"] = nsError.domain
            merged["errorCode"] = String(nsError.code)
        }
        log(level: .error, category: category, name: name, traceID: traceID, fields: merged)
    }

    func startSpan(category: String, name: String, fields: [String: String] = [:]) -> DiagnosticsSpan {
        DiagnosticsSpan(logger: self, category: category, name: name, fields: fields)
    }

    func flush() {
        store.flush()
    }

    func clearStoredLogs() throws {
        try store.clear()
    }

    fileprivate func log(level: DiagnosticsLevel, category: String, name: String, traceID: String?, fields: [String: String]) {
        let sanitized = DiagnosticsSanitizer.sanitizeLocalFields(fields)
        var consoleFields = sanitized
        if let traceID { consoleFields["trace_id"] = traceID }
        let summary = consoleFields.map { "\($0.key)=\($0.value)" }.sorted().joined(separator: " ")
        Logger(subsystem: subsystem, category: category).log(level: level.osLogType, "\(name, privacy: .public) \(summary, privacy: .public)")
        store.append(DiagnosticsEvent(level: level, category: category, name: name, traceID: traceID, fields: sanitized))
    }
}

final class DiagnosticsSpan {
    let traceID = UUID().uuidString

    private let logger: DiagnosticsLogger
    private let category: String
    private let name: String
    private let initialFields: [String: String]
    private let startedAt = DispatchTime.now().uptimeNanoseconds
    private let lock = NSLock()
    private var ended = false

    fileprivate init(logger: DiagnosticsLogger, category: String, name: String, fields: [String: String]) {
        self.logger = logger
        self.category = category
        self.name = name
        initialFields = fields
        logger.info(category: category, name: "\(name).start", traceID: traceID, fields: fields)
    }

    func end(status: String = "ok", fields: [String: String] = [:]) {
        lock.lock()
        guard !ended else {
            lock.unlock()
            return
        }
        ended = true
        lock.unlock()

        let elapsedMilliseconds = Double(DispatchTime.now().uptimeNanoseconds - startedAt) / 1_000_000
        var merged = initialFields
        fields.forEach { merged[$0.key] = $0.value }
        merged["durationMs"] = String(format: "%.2f", elapsedMilliseconds)
        merged["status"] = status
        logger.info(category: category, name: "\(name).end", traceID: traceID, fields: merged)
    }
}

private struct DiagnosticsBundle: Codable {
    let exportedAt: Date
    let metadata: AppBuildInfo
    let events: [DiagnosticsEvent]
}

final class DiagnosticsExporter {
    static let shared = DiagnosticsExporter()

    private let queue = DispatchQueue(label: "com.whitesharkssw.chatgptclient.diagnostics.export", qos: .utility)
    private let logger = DiagnosticsLogger.shared

    private init() { }

    func export(completion: @escaping (Result<URL, Error>) -> Void) {
        let traceID = UUID().uuidString
        let metadata = AppBuildInfo.current
        logger.info(category: "diagnostics", name: "export.start", traceID: traceID)

        queue.async {
            do {
                let events = try DiagnosticsStore.shared.snapshot().map { $0.redactedForExport() }
                let bundle = DiagnosticsBundle(exportedAt: Date(), metadata: metadata, events: events)
                let encoder = JSONEncoder()
                encoder.dateEncodingStrategy = .iso8601
                encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
                let data = try encoder.encode(bundle)
                let directory = FileManager.default.temporaryDirectory.appendingPathComponent("DiagnosticsExports", isDirectory: true)
                try FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true)
                let url = directory.appendingPathComponent(Self.exportFileName())
                try data.write(to: url, options: .atomic)
                self.logger.info(category: "diagnostics", name: "export.end", traceID: traceID, fields: ["eventCount": String(events.count), "byteCount": String(data.count), "status": "ok"])
                DispatchQueue.main.async { completion(.success(url)) }
            } catch {
                self.logger.error(category: "diagnostics", name: "export.end", traceID: traceID, error: error, fields: ["status": "failed"])
                DispatchQueue.main.async { completion(.failure(error)) }
            }
        }
    }

    private static func exportFileName() -> String {
        let formatter = DateFormatter()
        formatter.locale = Locale(identifier: "en_US_POSIX")
        formatter.timeZone = TimeZone(secondsFromGMT: 0)
        formatter.dateFormat = "yyyyMMdd-HHmmss"
        return "ChatGPTClient-Diagnostics-\(formatter.string(from: Date())).json"
    }
}
