import Foundation

enum ConversationAsyncStatus: String {
    case isStreaming = "IS_STREAMING"
    case complete = "COMPLETE"
}

private final class NativeConversationContinuationRuntime {
    var scheduledPolls: [String: DispatchWorkItem] = [:]
}

private var nativeConversationContinuationRuntimeAssociationKey: UInt8 = 0

extension ConversationRepository {
    private static let nativeConversationContinuationInterval: TimeInterval = 10

    private var nativeConversationContinuationRuntime: NativeConversationContinuationRuntime {
        precondition(Thread.isMainThread)
        if let runtime = objc_getAssociatedObject(self, &nativeConversationContinuationRuntimeAssociationKey) as? NativeConversationContinuationRuntime { return runtime }
        let runtime = NativeConversationContinuationRuntime()
        objc_setAssociatedObject(self, &nativeConversationContinuationRuntimeAssociationKey, runtime, .OBJC_ASSOCIATION_RETAIN_NONATOMIC)
        return runtime
    }

    func isNativeConversationContinuationActive(for conversationID: String) -> Bool {
        precondition(Thread.isMainThread)
        return nativeConversationContinuationRuntime.scheduledPolls[conversationID] != nil
    }

    func handleNativeConversationAuthoritativeDetail(_ detail: ConversationDetail) {
        precondition(Thread.isMainThread)
        let conversationID = detail.id
        var fields = diagnosticsFields(for: conversationID)
        fields["asyncStatus"] = detail.asyncStatus?.rawValue ?? "missing_or_unknown"
        fields["trailingTimelineItemCount"] = String(detail.trailingResponseTimeline.count)
        fields["visibleMessageCount"] = String(detail.messages.count)
        DiagnosticsLogger.shared.info(category: "conversation", name: "nativeContinuation.authoritativeDetail", fields: fields)

        if let snapshot = liveResponse(for: conversationID), snapshot.phase.isActive, !snapshot.promptText.isEmpty {
            stopNativeConversationContinuation(conversationID: conversationID, reason: "client_owned_response_active")
            return
        }

        if detail.asyncStatus == .isStreaming, !isLiveResponseActive(for: conversationID) { _ = beginExternalLiveResponse(conversationID: conversationID) }
        _ = adoptExternalAuthoritativeDetailTimeline(conversationID: conversationID, timeline: detail.trailingResponseTimeline, reasoningDurationSeconds: detail.trailingReasoningDurationSeconds, authoritativeVisibleMessageCount: detail.messages.count, latestVisibleRole: detail.messages.last?.role)

        guard detail.asyncStatus == .isStreaming else {
            stopNativeConversationContinuation(conversationID: conversationID, reason: detail.asyncStatus == .complete ? "backend_streaming_completed" : "async_status_not_streaming")
            return
        }
        scheduleNativeConversationContinuation(conversationID: conversationID)
    }

    func cancelAllNativeConversationContinuations(reason: String) {
        precondition(Thread.isMainThread)
        let ids = Array(nativeConversationContinuationRuntime.scheduledPolls.keys)
        for id in ids { stopNativeConversationContinuation(conversationID: id, reason: reason) }
    }

    private func scheduleNativeConversationContinuation(conversationID: String) {
        precondition(Thread.isMainThread)
        guard nativeConversationContinuationRuntime.scheduledPolls[conversationID] == nil else { return }
        let workItem = DispatchWorkItem { [weak self] in
            guard let self else { return }
            self.nativeConversationContinuationRuntime.scheduledPolls.removeValue(forKey: conversationID)
            if let snapshot = self.liveResponse(for: conversationID), snapshot.phase.isActive, !snapshot.promptText.isEmpty {
                self.stopNativeConversationContinuation(conversationID: conversationID, reason: "client_owned_response_active")
                return
            }
            guard self.detailOperationSnapshot(for: conversationID) == nil else {
                self.stopNativeConversationContinuation(conversationID: conversationID, reason: "detail_operation_in_flight")
                return
            }
            var fields = self.diagnosticsFields(for: conversationID)
            fields["intervalSeconds"] = String(Int(Self.nativeConversationContinuationInterval))
            DiagnosticsLogger.shared.info(category: "conversation", name: "nativeContinuation.pollRequested", fields: fields)
            self.syncLatestMessages(id: conversationID) { [weak self] result in
                guard let self else { return }
                if case .failure(let error) = result {
                    var fields = self.diagnosticsFields(for: conversationID)
                    fields["errorType"] = String(describing: type(of: error))
                    DiagnosticsLogger.shared.warning(category: "conversation", name: "nativeContinuation.pollStopped", fields: fields)
                    self.stopNativeConversationContinuation(conversationID: conversationID, reason: "detail_refresh_failed")
                }
            }
        }
        nativeConversationContinuationRuntime.scheduledPolls[conversationID] = workItem
        var fields = diagnosticsFields(for: conversationID)
        fields["intervalSeconds"] = String(Int(Self.nativeConversationContinuationInterval))
        DiagnosticsLogger.shared.info(category: "conversation", name: "nativeContinuation.scheduled", fields: fields)
        DispatchQueue.main.asyncAfter(deadline: .now() + Self.nativeConversationContinuationInterval, execute: workItem)
    }

    private func stopNativeConversationContinuation(conversationID: String, reason: String) {
        precondition(Thread.isMainThread)
        guard let workItem = nativeConversationContinuationRuntime.scheduledPolls.removeValue(forKey: conversationID) else { return }
        workItem.cancel()
        var fields = diagnosticsFields(for: conversationID)
        fields["reason"] = reason
        DiagnosticsLogger.shared.info(category: "conversation", name: "nativeContinuation.stopped", fields: fields)
    }
}
