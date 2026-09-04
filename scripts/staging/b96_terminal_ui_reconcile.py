from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FEATURE = ROOT / "ChatGPTClient/Conversation/ConversationFeature.swift"
text = FEATURE.read_text()
old = '''    func liveResponseDidChange(id: String) {
    guard displayedConversationID == id, repository.selectedConversationID == id else { return }
    let boundsBefore = answerJumpScrollBounds()
    let wasAtPhysicalBottom = tableView.contentOffset.y >= boundsBefore.maximumY - 0.5
    rebuildLiveResponsePresentation(width: effectivePresentationWidth())
    tableView.reloadData()
    tableView.layoutIfNeeded()
    if wasAtPhysicalBottom { setScrollOffsetY(answerJumpScrollBounds().maximumY) }
    updateAnswerJumpButton()
    var fields = repository.diagnosticsFields(for: id)
    fields["livePresentationRowCount"] = String(liveMessagePresentation.rows.count)
    fields["liveContentHeightPoints"] = String(format: "%.2f", livePresentationContentHeight)
    fields["followedPhysicalBottom"] = wasAtPhysicalBottom ? "true" : "false"
    diagnostics.info(category: "ui", name: "liveResponse.presentationApplied", fields: fields)
    updateConversationMenu()
}
'''
new = '''    func liveResponseDidChange(id: String) {
    guard displayedConversationID == id, repository.selectedConversationID == id else { return }
    if repository.liveResponse(for: id) == nil, let detail = repository.selectedConversation, detail.id == id, detail.currentNodeID != displayedCurrentNodeID || hasVisibleMessageChanges(from: messages, to: detail.messages) {
        apply(detail)
        return
    }
    let boundsBefore = answerJumpScrollBounds()
    let wasAtPhysicalBottom = tableView.contentOffset.y >= boundsBefore.maximumY - 0.5
    rebuildLiveResponsePresentation(width: effectivePresentationWidth())
    tableView.reloadData()
    tableView.layoutIfNeeded()
    if wasAtPhysicalBottom { setScrollOffsetY(answerJumpScrollBounds().maximumY) }
    updateAnswerJumpButton()
    var fields = repository.diagnosticsFields(for: id)
    fields["livePresentationRowCount"] = String(liveMessagePresentation.rows.count)
    fields["liveContentHeightPoints"] = String(format: "%.2f", livePresentationContentHeight)
    fields["followedPhysicalBottom"] = wasAtPhysicalBottom ? "true" : "false"
    diagnostics.info(category: "ui", name: "liveResponse.presentationApplied", fields: fields)
    updateConversationMenu()
}
'''
if text.count(old) != 1:
    raise SystemExit(f"anchor mismatch: expected 1, found {text.count(old)}")
FEATURE.write_text(text.replace(old, new, 1))
Path(__file__).unlink()
print("b96 terminal UI reconcile applied")
