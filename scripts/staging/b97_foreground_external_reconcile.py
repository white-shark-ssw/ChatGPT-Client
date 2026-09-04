from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "ChatGPTClient.xcodeproj/project.pbxproj"
ROOT_VC = ROOT / "ChatGPTClient/RootViewController.swift"
FEATURE = ROOT / "ChatGPTClient/Conversation/ConversationFeature.swift"
CONTINUATION = ROOT / "ChatGPTClient/Conversation/NativeConversationContinuation.swift"


def replace_exact(text: str, old: str, new: str, count: int = 1) -> str:
    actual = text.count(old)
    if actual != count:
        raise SystemExit(f"anchor mismatch: expected {count}, found {actual}: {old[:160]!r}")
    return text.replace(old, new, count)


project = PROJECT.read_text()
project = replace_exact(project, "CURRENT_PROJECT_VERSION = 96;", "CURRENT_PROJECT_VERSION = 97;", 2)
project = replace_exact(project, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b96";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b97";', 2)
PROJECT.write_text(project)

feature = FEATURE.read_text()
feature = replace_exact(feature, '        cancelAllNativeConversationContinuations(reason: "account_scope_reset")\n', "")
FEATURE.write_text(feature)

old_foreground = '''    @objc private func applicationWillEnterForeground(_ notification: Notification) {
        guard let conversationID = repository.selectedConversationID, let snapshot = repository.liveResponse(for: conversationID), snapshot.phase.isActive, snapshot.promptText.isEmpty, let sendExecutor = sendExecutors[conversationID] else { return }
        diagnostics.info(category: "webSend", name: "foregroundExternalRebootstrap.requested", fields: repository.diagnosticsFields(for: conversationID))
        sendExecutor.rebootstrapExternalObservationPageOnForeground()
    }
'''
new_foreground = '''    @objc private func applicationWillEnterForeground(_ notification: Notification) {
        guard let conversationID = repository.selectedConversationID, let snapshot = repository.liveResponse(for: conversationID), snapshot.phase.isActive, snapshot.promptText.isEmpty else { return }
        if repository.detailOperationSnapshot(for: conversationID) == nil {
            diagnostics.info(category: "conversation", name: "foregroundExternalDetailReconcile.requested", fields: repository.diagnosticsFields(for: conversationID))
            repository.syncLatestMessages(id: conversationID) { [weak self] result in
                guard let self else { return }
                switch result {
                case .success(let detail):
                    var fields = self.repository.diagnosticsFields(for: conversationID)
                    fields["visibleMessageCount"] = String(detail.messages.count)
                    fields["liveResponseActive"] = self.repository.isLiveResponseActive(for: conversationID) ? "true" : "false"
                    self.diagnostics.info(category: "conversation", name: "foregroundExternalDetailReconcile.completed", fields: fields)
                    if self.repository.selectedConversationID == conversationID { self.detailViewController.showConversation(id: conversationID) }
                    if !self.repository.isLiveResponseActive(for: conversationID), let executor = self.sendExecutors[conversationID] { self.releaseExecutor(for: conversationID, expected: executor) }
                case .failure(let error):
                    self.diagnostics.error(category: "conversation", name: "foregroundExternalDetailReconcile.failed", error: error, fields: self.repository.diagnosticsFields(for: conversationID))
                }
                self.updateLivePresentation()
            }
        } else {
            diagnostics.info(category: "conversation", name: "foregroundExternalDetailReconcile.skipped", fields: ["reason": "detail_operation_in_flight"])
        }
        if let sendExecutor = sendExecutors[conversationID] {
            diagnostics.info(category: "webSend", name: "foregroundExternalRebootstrap.requested", fields: repository.diagnosticsFields(for: conversationID))
            sendExecutor.rebootstrapExternalObservationPageOnForeground()
        }
    }
'''
root = ROOT_VC.read_text()
root = replace_exact(root, old_foreground, new_foreground)
ROOT_VC.write_text(root)

CONTINUATION.write_text('''import Foundation

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
''')

print("b97 foreground external Detail reconcile applied")