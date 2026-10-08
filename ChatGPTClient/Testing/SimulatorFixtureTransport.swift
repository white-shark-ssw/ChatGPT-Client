#if DEBUG
import Foundation

enum SimulatorFixtureTransport {
    enum Mode: String {
        case baseline
        case offlineCache = "offline-cache"
    }

    static let environmentKey = "CHATGPTCLIENT_SIMULATOR_FIXTURE"

    static var mode: Mode? {
        if let rawValue = ProcessInfo.processInfo.environment[environmentKey] { return Mode(rawValue: rawValue) }
        if ProcessInfo.processInfo.environment["XCTestConfigurationFilePath"] != nil { return .baseline }
        return nil
    }

    static var isEnabled: Bool { mode != nil }

    static func makeSessionConfiguration() -> URLSessionConfiguration {
        let configuration = URLSessionConfiguration.ephemeral
        configuration.protocolClasses = [SimulatorFixtureURLProtocol.self]
        return configuration
    }

    static func resetRequestState() { SimulatorFixtureURLProtocol.reset() }
    static func requestCount(for key: String) -> Int { SimulatorFixtureURLProtocol.requestCount(for: key) }
    static func setRequestObserver(_ observer: ((String) -> Void)?) { SimulatorFixtureURLProtocol.setRequestObserver(observer) }
}

private final class SimulatorFixtureURLProtocol: URLProtocol {
    private enum FixtureResponse {
        case success([String: Any])
        case failure(String)
    }

    private static let lock = NSLock()
    private static var requestCounts: [String: Int] = [:]
    private static var requestObserver: ((String) -> Void)?
    private var workItem: DispatchWorkItem?

    override class func canInit(with request: URLRequest) -> Bool {
        guard let url = request.url, url.host?.lowercased() == "chatgpt.com" else { return false }
        return url.path == "/backend-api/conversations" || url.path.hasPrefix("/backend-api/conversation/")
    }

    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }

    override func startLoading() {
        guard let url = request.url else {
            finishWithError("missing_url")
            return
        }
        let key = Self.requestKey(for: url)
        let count = Self.recordRequest(for: key)
        let response = Self.fixtureResponse(for: url, requestCount: count)
        let workItem = DispatchWorkItem { [weak self] in
            guard let self else { return }
            switch response {
            case .success(let payload): self.finish(payload: payload)
            case .failure(let reason): self.finishWithError(reason)
            }
        }
        self.workItem = workItem
        if key == "detail:fixture-slow" { DispatchQueue.global(qos: .userInitiated).asyncAfter(deadline: .now() + 0.6, execute: workItem) }
        else { DispatchQueue.global(qos: .userInitiated).async(execute: workItem) }
    }

    override func stopLoading() { workItem?.cancel() }

    private func finish(payload: [String: Any]) {
        guard !workItemCancelled, let url = request.url else { return }
        do {
            let data = try JSONSerialization.data(withJSONObject: payload, options: [.sortedKeys])
            let response = HTTPURLResponse(url: url, statusCode: 200, httpVersion: "HTTP/1.1", headerFields: ["Content-Type": "application/json", "Content-Length": String(data.count)])!
            client?.urlProtocol(self, didReceive: response, cacheStoragePolicy: .notAllowed)
            client?.urlProtocol(self, didLoad: data)
            client?.urlProtocolDidFinishLoading(self)
        } catch {
            client?.urlProtocol(self, didFailWithError: error)
        }
    }

    private var workItemCancelled: Bool { workItem?.isCancelled == true }

    private func finishWithError(_ reason: String) {
        guard !workItemCancelled else { return }
        client?.urlProtocol(self, didFailWithError: NSError(domain: "SimulatorFixtureTransport", code: 1, userInfo: [NSLocalizedDescriptionKey: reason]))
    }

    fileprivate static func reset() {
        lock.lock()
        requestCounts.removeAll()
        requestObserver = nil
        lock.unlock()
    }

    fileprivate static func requestCount(for key: String) -> Int {
        lock.lock()
        defer { lock.unlock() }
        return requestCounts[key] ?? 0
    }

    fileprivate static func setRequestObserver(_ observer: ((String) -> Void)?) {
        lock.lock()
        requestObserver = observer
        lock.unlock()
    }

    private static func recordRequest(for key: String) -> Int {
        lock.lock()
        let next = (requestCounts[key] ?? 0) + 1
        requestCounts[key] = next
        let observer = requestObserver
        lock.unlock()
        observer?(key)
        return next
    }

    private static func requestKey(for url: URL) -> String {
        if url.path == "/backend-api/conversations" { return "list" }
        return "detail:" + String(url.path.dropFirst("/backend-api/conversation/".count))
    }

    private static func fixtureResponse(for url: URL, requestCount: Int) -> FixtureResponse {
        if url.path == "/backend-api/conversations" {
            let alphaTitle = requestCount == 1 ? "Fixture Alpha" : "Fixture Alpha Refreshed"
            return .success([
                "items": [
                    ["id": "fixture-alpha", "title": alphaTitle, "update_time": 1_700_000_400],
                    ["id": "fixture-beta", "title": "Fixture Beta", "update_time": 1_700_000_300],
                    ["id": "fixture-slow", "title": "Fixture Slow", "update_time": 1_700_000_200],
                    ["id": "fixture-long", "title": "Fixture Long 1000+", "update_time": 1_700_000_100]
                ],
                "total": 4
            ])
        }
        let id = String(url.path.dropFirst("/backend-api/conversation/".count))
        switch id {
        case "fixture-alpha": return .success(detailPayload(id: id, title: "Fixture Alpha", messages: alphaMessages))
        case "fixture-beta": return .success(detailPayload(id: id, title: "Fixture Beta", messages: betaMessages))
        case "fixture-slow":
            let answer = requestCount == 1 ? "Slow initial answer" : "Slow replacement answer"
            return .success(detailPayload(id: id, title: "Fixture Slow", messages: [("user", "Slow request"), ("assistant", answer)]))
        case "fixture-long": return .success(detailPayload(id: id, title: "Fixture Long 1000+", messages: longMessages))
        default: return .failure("unexpected_detail_\(id)")
        }
    }

    private static var alphaMessages: [(String, String)] {
        [
            ("user", "Alpha user 1"),
            ("assistant", "# Alpha heading\n- deterministic list item\n\n```swift\nlet value = 1\n```\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\nAlpha answer 1"),
            ("user", "Alpha user 2"),
            ("assistant", "Alpha answer 2"),
            ("user", "Alpha user 3"),
            ("assistant", "Alpha answer 3")
        ]
    }

    private static var betaMessages: [(String, String)] { [("user", "Beta user"), ("assistant", "Beta answer")] }

    private static var longMessages: [(String, String)] {
        var messages: [(String, String)] = []
        messages.reserveCapacity(1004)
        for round in 1...502 {
            messages.append(("user", "Long user \(round)"))
            let body = round == 1 ? "## Long fixture Markdown\n\n- one\n- two\n\n`inline` and **bold**\n\nLong answer 1" : "Long answer \(round)"
            messages.append(("assistant", body))
        }
        return messages
    }

    private static func detailPayload(id: String, title: String, messages: [(String, String)]) -> [String: Any] {
        var mapping: [String: Any] = [:]
        var parentID: String?
        for (index, entry) in messages.enumerated() {
            let nodeID = "\(id)-node-\(index + 1)"
            let messageID = "\(id)-message-\(index + 1)"
            var message: [String: Any] = [
                "id": messageID,
                "author": ["role": entry.0],
                "content": ["content_type": "text", "parts": [entry.1]],
                "create_time": 1_700_000_000 + index,
                "status": "finished_successfully"
            ]
            if entry.0 == "assistant" { message["recipient"] = "all" }
            let parentValue: Any = parentID.map { $0 as Any } ?? NSNull()
            mapping[nodeID] = ["id": nodeID, "parent": parentValue, "children": [], "message": message]
            parentID = nodeID
        }
        return [
            "conversation_id": id,
            "title": title,
            "current_node": parentID ?? "",
            "mapping": mapping,
            "conversation_async_status": "complete"
        ]
    }
}
#endif
