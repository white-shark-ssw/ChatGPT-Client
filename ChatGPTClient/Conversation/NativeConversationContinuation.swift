import Foundation

enum ConversationAsyncStatus: String {
    case isStreaming = "IS_STREAMING"
    case complete = "COMPLETE"
}

extension ConversationRepository {
    func handleNativeConversationAuthoritativeDetail(_ detail: ConversationDetail) {
        precondition(Thread.isMainThread)
        let conversationID = detail.id
        var fields = diagnosticsFields(for: conversationID)
        fields["asyncStatus"] = detail.asyncStatus?.rawValue ?? "missing_or_unknown"
        fields["trailingTimelineItemCount"] = String(detail.trailingResponseTimeline.count)
        fields["visibleMessageCount"] = String(detail.messages.count)
        DiagnosticsLogger.shared.info(category: "conversation", name: "nativeContinuation.authoritativeDetail", fields: fields)

        if let snapshot = liveResponse(for: conversationID), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }
        _ = adoptExternalAuthoritativeDetailTimeline(conversationID: conversationID, timeline: detail.trailingResponseTimeline, reasoningDurationSeconds: detail.trailingReasoningDurationSeconds, authoritativeVisibleMessageCount: detail.messages.count, latestVisibleRole: detail.messages.last?.role)
    }
}
