from pathlib import Path

path = Path("ChatGPTClient/Conversation/ConversationFeature.swift")
text = path.read_text()


def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one match, got {count}: {old[:120]!r}")
    text = text.replace(old, new, 1)

replace_once(
'''    private struct ScrollAnchor {
        let messageID: String
        let chunkIndex: Int
        let relativeOffset: CGFloat
    }
''',
'''    private struct ScrollAnchor {
        let messageID: String
        let chunkIndex: Int
        let relativeOffset: CGFloat
    }

    private struct HistoricalPresentationGeometryCacheEntry {
        let currentNodeID: String
        let authoritativeMessageCount: Int
        let rowCount: Int
        let chunkedMessageCount: Int
        let maxChunkCharacterCount: Int
        let roundCount: Int
        let layoutWidth: CGFloat
        let showsMessageTimestamps: Bool
        let expandedReasoningMessageIDs: Set<String>
        let rowMetrics: [ConversationMessageCell.Metrics]
        let rowOffsets: [CGFloat]
        let contentHeight: CGFloat
    }
''')

replace_once(
'''    private var displayedConversationID: String?
    private var scrollAnchorsByConversationID: [String: ScrollAnchor] = [:]
    private var expandedReasoningMessageIDsByConversationID: [String: Set<String>] = [:]
''',
'''    private var displayedConversationID: String?
    private var displayedCurrentNodeID: String?
    private var scrollAnchorsByConversationID: [String: ScrollAnchor] = [:]
    private var historicalPresentationGeometryCacheByConversationID: [String: HistoricalPresentationGeometryCacheEntry] = [:]
    private var expandedReasoningMessageIDsByConversationID: [String: Set<String>] = [:]
''')

replace_once(
'''        displayedConversationID = nil
        scrollAnchorsByConversationID.removeAll()
        expandedReasoningMessageIDsByConversationID.removeAll()
''',
'''        displayedConversationID = nil
        displayedCurrentNodeID = nil
        scrollAnchorsByConversationID.removeAll()
        historicalPresentationGeometryCacheByConversationID.removeAll()
        expandedReasoningMessageIDsByConversationID.removeAll()
''')

replace_once(
'''        displayedConversationID = detail.id
        title = detail.title
        messages = detail.messages
''',
'''        displayedConversationID = detail.id
        displayedCurrentNodeID = detail.currentNodeID
        title = detail.title
        messages = detail.messages
''')

replace_once(
'''        stopAnswerJumpAnimation(clearTarget: true)
        messages = []
        roundProjection = ConversationRoundProjection(rounds: [])
''',
'''        stopAnswerJumpAnimation(clearTarget: true)
        displayedCurrentNodeID = nil
        messages = []
        roundProjection = ConversationRoundProjection(rounds: [])
''')

replace_once(
'''        roundProjection = ConversationRoundProjection.derive(from: messages)
        messagePresentation = ConversationMessagePresentationProjection.derive(from: messages)
        let geometryDurationMs = rebuildPresentationGeometry(width: effectivePresentationWidth())
        answerRows = roundProjection.rounds.compactMap { messagePresentation.firstRowByMessageID[$0.userMessageID] }
        let totalDurationMs = (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
        diagnostics.info(category: "ui", name: "messagePresentation.rebuilt", fields: ["authoritativeMessageCount": String(messages.count), "presentationRowCount": String(messagePresentation.rows.count), "chunkedMessageCount": String(messagePresentation.chunkedMessageCount), "chunkCharacterLimit": String(ConversationMessagePresentationProjection.chunkCharacterLimit), "maxChunkCharacterCount": String(messagePresentation.maxChunkCharacterCount), "geometryDurationMs": String(format: "%.2f", geometryDurationMs), "durationMs": String(format: "%.2f", totalDurationMs), "layoutWidthPoints": String(format: "%.2f", presentationLayoutWidth), "contentHeightPoints": String(format: "%.2f", presentationContentHeight)])
''',
'''        roundProjection = ConversationRoundProjection.derive(from: messages)
        messagePresentation = ConversationMessagePresentationProjection.derive(from: messages)
        let geometryStartedAt = ProcessInfo.processInfo.systemUptime
        let geometryReused = restoreHistoricalPresentationGeometryIfPossible(width: effectivePresentationWidth())
        let geometryDurationMs = geometryReused ? (ProcessInfo.processInfo.systemUptime - geometryStartedAt) * 1000 : rebuildPresentationGeometry(width: effectivePresentationWidth())
        answerRows = roundProjection.rounds.compactMap { messagePresentation.firstRowByMessageID[$0.userMessageID] }
        let totalDurationMs = (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
        diagnostics.info(category: "ui", name: "messagePresentation.rebuilt", fields: ["authoritativeMessageCount": String(messages.count), "presentationRowCount": String(messagePresentation.rows.count), "chunkedMessageCount": String(messagePresentation.chunkedMessageCount), "chunkCharacterLimit": String(ConversationMessagePresentationProjection.chunkCharacterLimit), "maxChunkCharacterCount": String(messagePresentation.maxChunkCharacterCount), "geometryReused": geometryReused ? "true" : "false", "geometryDurationMs": String(format: "%.2f", geometryDurationMs), "durationMs": String(format: "%.2f", totalDurationMs), "layoutWidthPoints": String(format: "%.2f", presentationLayoutWidth), "contentHeightPoints": String(format: "%.2f", presentationContentHeight)])
''')

replace_once(
'''    @discardableResult
    private func rebuildPresentationGeometry(width: CGFloat) -> Double {
''',
'''    private func restoreHistoricalPresentationGeometryIfPossible(width: CGFloat) -> Bool {
        guard let conversationID = displayedConversationID, let currentNodeID = displayedCurrentNodeID, let cached = historicalPresentationGeometryCacheByConversationID[conversationID] else { return false }
        let resolvedWidth = max(1, width)
        let expandedReasoningMessageIDs = expandedReasoningMessageIDsByConversationID[conversationID] ?? []
        guard cached.currentNodeID == currentNodeID,
              cached.authoritativeMessageCount == messages.count,
              cached.rowCount == messagePresentation.rows.count,
              cached.chunkedMessageCount == messagePresentation.chunkedMessageCount,
              cached.maxChunkCharacterCount == messagePresentation.maxChunkCharacterCount,
              cached.roundCount == roundProjection.rounds.count,
              abs(cached.layoutWidth - resolvedWidth) <= 0.5,
              cached.showsMessageTimestamps == preferences.showsMessageTimestamps,
              cached.expandedReasoningMessageIDs == expandedReasoningMessageIDs,
              cached.rowMetrics.count == messagePresentation.rows.count,
              cached.rowOffsets.count == messagePresentation.rows.count else { return false }
        presentationLayoutWidth = resolvedWidth
        presentationRowMetrics = cached.rowMetrics
        presentationRowOffsets = cached.rowOffsets
        presentationContentHeight = cached.contentHeight
        return true
    }

    private func storeHistoricalPresentationGeometryIfPossible() {
        guard let conversationID = displayedConversationID, let currentNodeID = displayedCurrentNodeID, presentationRowMetrics.count == messagePresentation.rows.count, presentationRowOffsets.count == messagePresentation.rows.count else { return }
        historicalPresentationGeometryCacheByConversationID[conversationID] = HistoricalPresentationGeometryCacheEntry(currentNodeID: currentNodeID, authoritativeMessageCount: messages.count, rowCount: messagePresentation.rows.count, chunkedMessageCount: messagePresentation.chunkedMessageCount, maxChunkCharacterCount: messagePresentation.maxChunkCharacterCount, roundCount: roundProjection.rounds.count, layoutWidth: presentationLayoutWidth, showsMessageTimestamps: preferences.showsMessageTimestamps, expandedReasoningMessageIDs: expandedReasoningMessageIDsByConversationID[conversationID] ?? [], rowMetrics: presentationRowMetrics, rowOffsets: presentationRowOffsets, contentHeight: presentationContentHeight)
    }

    @discardableResult
    private func rebuildPresentationGeometry(width: CGFloat) -> Double {
''')

replace_once(
'''        presentationContentHeight = offset
        return (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
    }

    private func rebuildLiveResponsePresentation(width: CGFloat) {
''',
'''        presentationContentHeight = offset
        storeHistoricalPresentationGeometryIfPossible()
        return (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
    }

    private func rebuildLiveResponsePresentation(width: CGFloat) {
''')

replace_once(
'''            presentationContentHeight += heightDelta
        }
        UIView.performWithoutAnimation {
''',
'''            presentationContentHeight += heightDelta
            storeHistoricalPresentationGeometryIfPossible()
        }
        UIView.performWithoutAnimation {
''')

replace_once(
'''        let toolParagraph = NSMutableParagraphStyle()
        toolParagraph.minimumLineHeight = 30
        toolParagraph.paragraphSpacing = 9
''',
'''        let toolParagraph = NSMutableParagraphStyle()
        toolParagraph.minimumLineHeight = 34
        toolParagraph.lineSpacing = 2
        toolParagraph.paragraphSpacingBefore = 5
        toolParagraph.paragraphSpacing = 12
''')

path.write_text(text)
