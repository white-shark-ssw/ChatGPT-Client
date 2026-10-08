import XCTest
@testable import ChatGPTClient

final class ConversationRepositorySimulatorTests: XCTestCase {
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

        let firstCompletion = expectation(description: "superseded detail completion")
        let replacementCompletion = expectation(description: "replacement detail completion")
        var firstError: Error?
        var replacementDetail: ConversationDetail?
        var replacementError: Error?

        repository.loadConversation(id: "fixture-slow") { result in
            if case .failure(let error) = result { firstError = error }
            firstCompletion.fulfill()
        }
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

    @MainActor
    private func loadConversations(_ repository: ConversationRepository, forceRefresh: Bool) async throws -> [ConversationSummary] {
        try await withCheckedThrowingContinuation { continuation in
            repository.loadConversations(forceRefresh: forceRefresh) { continuation.resume(with: $0) }
        }
    }

    @MainActor
    private func loadConversation(_ repository: ConversationRepository, id: String) async throws -> ConversationDetail {
        try await withCheckedThrowingContinuation { continuation in
            repository.loadConversation(id: id) { continuation.resume(with: $0) }
        }
    }
}
