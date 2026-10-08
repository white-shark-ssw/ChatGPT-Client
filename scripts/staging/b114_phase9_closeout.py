from pathlib import Path

PROJECT = Path("ChatGPTClient.xcodeproj/project.pbxproj")
CONVERSATION = Path("ChatGPTClient/Conversation/ConversationFeature.swift")


def replace_exact(text: str, old: str, new: str, count: int = 1) -> str:
    actual = text.count(old)
    if actual != count:
        raise SystemExit(f"expected {count} occurrences, found {actual}: {old[:100]!r}")
    return text.replace(old, new)


project = PROJECT.read_text()
project = replace_exact(project, "CURRENT_PROJECT_VERSION = 113;", "CURRENT_PROJECT_VERSION = 114;", 2)
project = replace_exact(project, 'DIAGNOSTICS_CANDIDATE = "DEV-message-rendering-0.1.0-b113";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b114";', 2)
PROJECT.write_text(project)

text = CONVERSATION.read_text()

capture_old = '''    private func captureScrollAnchor(for id: String) {
        guard !messagePresentation.rows.isEmpty, let indexPath = tableView.indexPathsForVisibleRows?.min(by: { $0.row < $1.row }), messagePresentation.rows.indices.contains(indexPath.row), presentationRowOffsets.indices.contains(indexPath.row) else { return }
'''
capture_new = '''    private func captureScrollAnchor(for id: String) {
        if displayedConversationID == id, repository.liveResponse(for: id)?.phase.isActive == true {
            let bounds = answerJumpScrollBounds()
            if tableView.contentOffset.y >= bounds.maximumY - 0.5 {
                scrollAnchorsByConversationID.removeValue(forKey: id)
                var fields = repository.diagnosticsFields(for: id)
                fields["contentOffsetY"] = String(format: "%.2f", tableView.contentOffset.y)
                fields["maximumY"] = String(format: "%.2f", bounds.maximumY)
                fields["policy"] = "active_at_physical_bottom"
                diagnostics.info(category: "conversation", name: "scrollAnchor.followTailPreserved", fields: fields)
                return
            }
        }
        guard !messagePresentation.rows.isEmpty, let indexPath = tableView.indexPathsForVisibleRows?.min(by: { $0.row < $1.row }), messagePresentation.rows.indices.contains(indexPath.row), presentationRowOffsets.indices.contains(indexPath.row) else { return }
'''
text = replace_exact(text, capture_old, capture_new)

text = replace_exact(text, "        let canReload = selectedID != nil\n", "        let canReload = selectedID != nil && !recoveryInProgress && !responseActive\n")

reload_old = '''    @objc private func reloadCurrentConversation() {
        guard let id = repository.selectedConversationID else { return }
        captureScrollAnchor(for: id)
'''
reload_new = '''    @objc private func reloadCurrentConversation() {
        guard let id = repository.selectedConversationID else { return }
        guard repository.liveResponse(for: id)?.phase.isActive != true else {
            var fields = repository.diagnosticsFields(for: id)
            fields["reason"] = "active_response"
            diagnostics.info(category: "navigation", name: "conversation.detailReload.blocked", fields: fields)
            updateConversationMenu()
            return
        }
        captureScrollAnchor(for: id)
'''
text = replace_exact(text, reload_old, reload_new)

will_display_start = text.index("    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {")
context_menu_start = text.index("    func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration? {", will_display_start)
text = text[:will_display_start] + text[context_menu_start:]

text = replace_exact(text, "    private static var diagnosticCellOrdinalSeed = 0\n", "")
text = replace_exact(text, '''    private var diagnosticCellOrdinal = 0
    private var lastConfiguredRoleForDiagnostics = "none"
    private var reusedFromRoleForDiagnostics = "none"
    private var reusedFromLinkRunCountForDiagnostics = 0
''', "")
text = replace_exact(text, '''        Self.diagnosticCellOrdinalSeed += 1
        diagnosticCellOrdinal = Self.diagnosticCellOrdinalSeed
''', "")
text = replace_exact(text, '''        reusedFromRoleForDiagnostics = lastConfiguredRoleForDiagnostics
        reusedFromLinkRunCountForDiagnostics = attributedLinkRunCount(messageLabel.attributedText)
''', "")
text = replace_exact(text, "    lastConfiguredRoleForDiagnostics = message.role.rawValue\n", "")

diagnostic_start = text.index("    func bodyColorDiagnostics() -> [String: String] {")
layout_start = text.index("    override func layoutSubviews() {", diagnostic_start)
text = text[:diagnostic_start] + text[layout_start:]

for forbidden in [
    "assistantChunkColor.willDisplay",
    "assistantChunkRender.afterDisplay",
    "bodyRenderedColorDiagnostics",
    "bodyColorDiagnostics",
    "diagnosticCellOrdinal",
    "reusedFromRoleForDiagnostics",
    "labelLayerTransparent",
    "directAttributedTransparent",
]:
    if forbidden in text:
        raise SystemExit(f"diagnostic marker still present: {forbidden}")

for required in [
    'static let userReuseIdentifier = "ConversationMessageCell.user"',
    'static let assistantReuseIdentifier = "ConversationMessageCell.assistant"',
    "enum ConversationMessageRichTextRenderer",
    'return location.map { "〔文件引用 \\($0)〕" } ?? "〔文件引用〕"',
]:
    if required not in text:
        raise SystemExit(f"required inherited marker missing: {required}")

CONVERSATION.write_text(text)
