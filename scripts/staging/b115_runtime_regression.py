from pathlib import Path

PROJECT = Path("ChatGPTClient.xcodeproj/project.pbxproj")
CONVERSATION = Path("ChatGPTClient/Conversation/ConversationFeature.swift")


def replace_exact(text: str, old: str, new: str, count: int = 1) -> str:
    actual = text.count(old)
    if actual != count:
        raise SystemExit(f"expected {count} occurrences, found {actual}: {old[:120]!r}")
    return text.replace(old, new)


project = PROJECT.read_text()
project = replace_exact(project, "CURRENT_PROJECT_VERSION = 114;", "CURRENT_PROJECT_VERSION = 115;", 2)
project = replace_exact(project, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b114";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b115";', 2)
PROJECT.write_text(project)

text = CONVERSATION.read_text()

menu_old = '''        let selectedID = repository.selectedConversationID
        let operationKind = selectedID.flatMap { repository.detailOperationSnapshot(for: $0)?.kind }
        let recoveryInProgress = operationKind == .sync || operationKind == .reload
        let liveSnapshot = selectedID.flatMap { repository.liveResponse(for: $0) }
        let responseActive = liveSnapshot?.phase.isActive == true
        let localResponseActive = responseActive && !(liveSnapshot?.promptText.isEmpty ?? true)
        let canSync = selectedID != nil && !recoveryInProgress && !localResponseActive
        let canReload = selectedID != nil && !recoveryInProgress && !responseActive
'''
menu_new = '''        let selectedID = repository.selectedConversationID
        let operationKind = selectedID.flatMap { repository.detailOperationSnapshot(for: $0)?.kind }
        let recoveryInProgress = operationKind == .sync || operationKind == .reload
        let canSync = selectedID != nil && !recoveryInProgress
        let canReload = selectedID != nil
'''
text = replace_exact(text, menu_old, menu_new)

sync_guard = '''        if let snapshot = repository.liveResponse(for: id), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }
'''
text = replace_exact(text, sync_guard, "")

reload_guard = '''        guard repository.liveResponse(for: id)?.phase.isActive != true else {
            var fields = repository.diagnosticsFields(for: id)
            fields["reason"] = "active_response"
            diagnostics.info(category: "navigation", name: "conversation.detailReload.blocked", fields: fields)
            updateConversationMenu()
            return
        }
'''
text = replace_exact(text, reload_guard, "")

live_user_old = '''    let userMessage = snapshot.promptText.isEmpty ? nil : ConversationMessage(id: "local-live-user-\\(snapshot.generation)", role: .user, text: snapshot.promptText, responseTimeline: [], reasoningDurationSeconds: nil, createTime: nil)
    let assistantMessage = ConversationMessage(id: "local-live-response-\\(snapshot.generation)", role: .assistant, text: bodyText, responseTimeline: snapshot.timeline, reasoningDurationSeconds: snapshot.reasoningDurationSeconds, createTime: nil)
'''
live_user_new = '''    let authoritativeSuffixStart = min(snapshot.baselineVisibleMessageCount, messages.count)
    let authoritativeUserMaterialized = !snapshot.promptText.isEmpty && messages.dropFirst(authoritativeSuffixStart).contains { $0.role == .user }
    let userMessage = snapshot.promptText.isEmpty || authoritativeUserMaterialized ? nil : ConversationMessage(id: "local-live-user-\\(snapshot.generation)", role: .user, text: snapshot.promptText, responseTimeline: [], reasoningDurationSeconds: nil, createTime: nil)
    let assistantMessage = ConversationMessage(id: "local-live-response-\\(snapshot.generation)", role: .assistant, text: bodyText, responseTimeline: snapshot.timeline, reasoningDurationSeconds: snapshot.reasoningDurationSeconds, createTime: nil)
'''
text = replace_exact(text, live_user_old, live_user_new)

presentation_fields_old = '''        fields["livePresentationRowCount"] = String(liveMessagePresentation.rows.count)
        fields["liveContentHeightPoints"] = String(format: "%.2f", livePresentationContentHeight)
        fields["followedPhysicalBottom"] = wasAtPhysicalBottom ? "true" : "false"
'''
presentation_fields_new = '''        fields["livePresentationRowCount"] = String(liveMessagePresentation.rows.count)
        fields["liveUserPresentationCount"] = String(livePresentationMessages.filter { $0.role == .user }.count)
        fields["liveContentHeightPoints"] = String(format: "%.2f", livePresentationContentHeight)
        fields["followedPhysicalBottom"] = wasAtPhysicalBottom ? "true" : "false"
'''
text = replace_exact(text, presentation_fields_old, presentation_fields_new)

rebuilt_log_old = '''        diagnostics.info(category: "ui", name: "messagePresentation.rebuilt", fields: ["authoritativeMessageCount": String(messages.count), "presentationRowCount": String(messagePresentation.rows.count), "chunkedMessageCount": String(messagePresentation.chunkedMessageCount), "chunkCharacterLimit": String(ConversationMessagePresentationProjection.chunkCharacterLimit), "maxChunkCharacterCount": String(messagePresentation.maxChunkCharacterCount), "geometryReused": geometryReused ? "true" : "false", "geometryMode": geometryReused ? "resident_cache" : "cooperative_main_queue", "geometryDurationMs": String(format: "%.2f", geometryDurationMs), "durationMs": String(format: "%.2f", totalDurationMs), "layoutWidthPoints": String(format: "%.2f", presentationLayoutWidth), "contentHeightPoints": String(format: "%.2f", presentationContentHeight)])
'''
rebuilt_log_new = '''        diagnostics.info(category: "ui", name: "messagePresentation.rebuilt", fields: ["authoritativeMessageCount": String(messages.count), "presentationRowCount": String(messagePresentation.rows.count), "livePresentationRowCount": String(liveMessagePresentation.rows.count), "liveUserPresentationCount": String(livePresentationMessages.filter { $0.role == .user }.count), "chunkedMessageCount": String(messagePresentation.chunkedMessageCount), "chunkCharacterLimit": String(ConversationMessagePresentationProjection.chunkCharacterLimit), "maxChunkCharacterCount": String(messagePresentation.maxChunkCharacterCount), "geometryReused": geometryReused ? "true" : "false", "geometryMode": geometryReused ? "resident_cache" : "cooperative_main_queue", "geometryDurationMs": String(format: "%.2f", geometryDurationMs), "durationMs": String(format: "%.2f", totalDurationMs), "layoutWidthPoints": String(format: "%.2f", presentationLayoutWidth), "contentHeightPoints": String(format: "%.2f", presentationContentHeight)])
'''
text = replace_exact(text, rebuilt_log_old, rebuilt_log_new)

for forbidden in [
    'let localResponseActive =',
    'let canReload = selectedID != nil && !recoveryInProgress && !responseActive',
    'conversation.detailReload.blocked',
    'snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }',
]:
    if forbidden in text:
        raise SystemExit(f"rejected b114 active-control marker remains: {forbidden}")

for required in [
    'let canSync = selectedID != nil && !recoveryInProgress',
    'let canReload = selectedID != nil',
    'let authoritativeSuffixStart = min(snapshot.baselineVisibleMessageCount, messages.count)',
    'let authoritativeUserMaterialized = !snapshot.promptText.isEmpty && messages.dropFirst(authoritativeSuffixStart).contains { $0.role == .user }',
    'fields["liveUserPresentationCount"]',
    'scrollAnchor.followTailPreserved',
    'static let userReuseIdentifier = "ConversationMessageCell.user"',
    'static let assistantReuseIdentifier = "ConversationMessageCell.assistant"',
    'enum ConversationMessageRichTextRenderer',
]:
    if required not in text:
        raise SystemExit(f"required b115/inherited marker missing: {required}")

CONVERSATION.write_text(text)
