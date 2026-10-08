import XCTest
@testable import ChatGPTClient

final class ConversationRepositorySimulatorTests: XCTestCase {
    override func setUpWithError() throws {
        try super.setUpWithError()
        XCTAssertEqual(SimulatorFixtureTransport.mode?.rawValue, "baseline")
    }

    @MainActor
    func testFixtureLoadsListDetailAndLongConversationThroughRealRepository() async throws {
        SimulatorFixtureTransport.resetRequestState()
        let repository = ConversationRepository()
        let conversations = try await loadConversations(repository, forceRefresh: true)
        XCTAssertEqual(conversations.map(\.id), ["fixture-alpha", "fixture-beta", "fixture-slow", "fixture-long"])
        XCTAssertEqual(SimulatorFixtureTransport.requestCount(for: "list"), 1)

        repository.selectConversation(id: "fixture-alpha")
        let alpha = try await loadConversation(repository, id: "fixture-alpha")
        XCTAssertEqual(alpha.messages.count, 6)
        XCTAssertEqual(alpha.messages.last?.text, "Alpha answer 3")
        XCTAssertEqual(ConversationRoundProjection.derive(from: alpha.messages).rounds.count, 3)
        let rendered = ConversationMessageRichTextRenderer.render(alpha.messages[1].text, role: .assistant)
        XCTAssertTrue(rendered.string.contains("Alpha heading"))
        XCTAssertTrue(rendered.string.contains("deterministic list item"))
        XCTAssertTrue(rendered.string.contains("let value = 1"))

        repository.selectConversation(id: "fixture-long")
        let long = try await loadConversation(repository, id: "fixture-long")
        XCTAssertEqual(long.messages.count, 1004)
        XCTAssertEqual(ConversationRoundProjection.derive(from: long.messages).rounds.count, 502)
        XCTAssertEqual(long.messages.last?.text, "Long answer 502")
        XCTAssertEqual(SimulatorFixtureTransport.requestCount(for: "detail:fixture-long"), 1)
    }

    @MainActor
    func testReloadSupersedesInFlightDetailAndKeepsReplacementAuthoritative() async throws {
        SimulatorFixtureTransport.resetRequestState()
        let repository = ConversationRepository()
        _ = try await loadConversations(repository, forceRefresh: true)
        repository.selectConversation(id: "fixture-slow")

        let firstRequestStarted = expectation(description: "first slow fixture request started")
        SimulatorFixtureTransport.setRequestObserver { key in
            if key == "detail:fixture-slow" { firstRequestStarted.fulfill() }
        }
        let firstCompletion = expectation(description: "superseded detail completion")
        let replacementCompletion = expectation(description: "replacement detail completion")
        var firstError: Error?
        var replacementDetail: ConversationDetail?
        var replacementError: Error?

        repository.loadConversation(id: "fixture-slow") { result in
            if case .failure(let error) = result { firstError = error }
            firstCompletion.fulfill()
        }
        await fulfillment(of: [firstRequestStarted], timeout: 2)
        SimulatorFixtureTransport.setRequestObserver(nil)
        repository.reloadConversation(id: "fixture-slow") { result in
            switch result {
            case .success(let detail): replacementDetail = detail
            case .failure(let error): replacementError = error
            }
            replacementCompletion.fulfill()
        }

        await fulfillment(of: [firstCompletion, replacementCompletion], timeout: 5)
        XCTAssertEqual(firstError as? ConversationRepositoryError, .operationSuperseded)
        XCTAssertNil(replacementError)
        XCTAssertEqual(replacementDetail?.messages.last?.text, "Slow replacement answer")
        XCTAssertEqual(repository.selectedConversation?.messages.last?.text, "Slow replacement answer")
        XCTAssertEqual(SimulatorFixtureTransport.requestCount(for: "detail:fixture-slow"), 2)
    }


    func testSanitizedProtocolReplayFixtureReplaysStopRequestAndAckWithoutNetwork() async throws {
        SimulatorFixtureTransport.resetRequestState()
        let fixtureURL = URL(fileURLWithPath: #filePath).deletingLastPathComponent().deletingLastPathComponent().appendingPathComponent("fixtures/protocol/stop-request-ack-v1.json")
        try SimulatorFixtureTransport.installProtocolReplayFixture(data: Data(contentsOf: fixtureURL))
        defer { SimulatorFixtureTransport.resetRequestState() }

        var request = URLRequest(url: URL(string: "https://chatgpt.com/backend-api/stop_conversation")!)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONSerialization.data(withJSONObject: ["conversation_id": "id-0001", "exclude_async_types": []], options: [.sortedKeys])
        let (data, response) = try await performFixtureRequest(request)
        XCTAssertEqual(response.statusCode, 200)
        XCTAssertEqual(response.value(forHTTPHeaderField: "Content-Type"), "application/json")
        let payload = try XCTUnwrap(try JSONSerialization.jsonObject(with: data) as? [String: Any])
        XCTAssertEqual(payload["status"] as? String, "ok")
        XCTAssertTrue(payload["last_message_id"] is NSNull)
        XCTAssertEqual(SimulatorFixtureTransport.requestCount(for: "replay:POST:/backend-api/stop_conversation"), 1)
    }

    @MainActor
    private func loadConversations(_ repository: ConversationRepository, forceRefresh: Bool) async throws -> [ConversationSummary] {
        try await withCheckedThrowingContinuation { continuation in
            repository.loadConversations(forceRefresh: forceRefresh) { continuation.resume(with: $0) }
        }
    }


    private func performFixtureRequest(_ request: URLRequest) async throws -> (Data, HTTPURLResponse) {
        try await withCheckedThrowingContinuation { continuation in
            let session = URLSession(configuration: SimulatorFixtureTransport.makeSessionConfiguration())
            session.dataTask(with: request) { data, response, error in
                defer { session.finishTasksAndInvalidate() }
                if let error { continuation.resume(throwing: error); return }
                guard let data, let response = response as? HTTPURLResponse else {
                    continuation.resume(throwing: NSError(domain: "ConversationRepositorySimulatorTests", code: 1, userInfo: [NSLocalizedDescriptionKey: "missing fixture response"]))
                    return
                }
                continuation.resume(returning: (data, response))
            }.resume()
        }
    }

    @MainActor
    private func loadConversation(_ repository: ConversationRepository, id: String) async throws -> ConversationDetail {
        try await withCheckedThrowingContinuation { continuation in
            repository.loadConversation(id: id) { continuation.resume(with: $0) }
        }
    }
}
