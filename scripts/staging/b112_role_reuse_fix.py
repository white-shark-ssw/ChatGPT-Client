from pathlib import Path

PROJECT = Path("ChatGPTClient.xcodeproj/project.pbxproj")
FEATURE = Path("ChatGPTClient/Conversation/ConversationFeature.swift")


def replace_exact(path: Path, old: str, new: str, expected_count: int = 1) -> None:
    text = path.read_text()
    actual = text.count(old)
    if actual != expected_count:
        raise SystemExit(f"{path}: expected {expected_count} occurrences, found {actual}: {old!r}")
    path.write_text(text.replace(old, new, expected_count))


replace_exact(PROJECT, "CURRENT_PROJECT_VERSION = 111;", "CURRENT_PROJECT_VERSION = 112;", 2)
replace_exact(PROJECT, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b111";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b112";', 2)

register_old = "        tableView.register(ConversationMessageCell.self, forCellReuseIdentifier: ConversationMessageCell.reuseIdentifier)\n"
register_new = "        tableView.register(ConversationMessageCell.self, forCellReuseIdentifier: ConversationMessageCell.userReuseIdentifier)\n        tableView.register(ConversationMessageCell.self, forCellReuseIdentifier: ConversationMessageCell.assistantReuseIdentifier)\n"
replace_exact(FEATURE, register_old, register_new)

cell_for_old = "    let cell = tableView.dequeueReusableCell(withIdentifier: ConversationMessageCell.reuseIdentifier, for: indexPath) as! ConversationMessageCell\n"
cell_for_new = """    let cellRole: ConversationMessage.Role
    if indexPath.row < messagePresentation.rows.count, messagePresentation.rows.indices.contains(indexPath.row) {
        let presentationRow = messagePresentation.rows[indexPath.row]
        cellRole = messages.indices.contains(presentationRow.messageIndex) ? messages[presentationRow.messageIndex].role : .assistant
    } else {
        let liveRow = indexPath.row - messagePresentation.rows.count
        if liveMessagePresentation.rows.indices.contains(liveRow) {
            let presentationRow = liveMessagePresentation.rows[liveRow]
            cellRole = livePresentationMessages.indices.contains(presentationRow.messageIndex) ? livePresentationMessages[presentationRow.messageIndex].role : .assistant
        } else {
            cellRole = .assistant
        }
    }
    let cell = tableView.dequeueReusableCell(withIdentifier: ConversationMessageCell.reuseIdentifier(for: cellRole), for: indexPath) as! ConversationMessageCell
"""
replace_exact(FEATURE, cell_for_old, cell_for_new)

reuse_old = """    static let reuseIdentifier = "ConversationMessageCell"
    private static var diagnosticCellOrdinalSeed = 0
"""
reuse_new = """    static let userReuseIdentifier = "ConversationMessageCell.user"
    static let assistantReuseIdentifier = "ConversationMessageCell.assistant"
    static func reuseIdentifier(for role: ConversationMessage.Role) -> String { switch role { case .user: return userReuseIdentifier; case .assistant: return assistantReuseIdentifier } }
    private static var diagnosticCellOrdinalSeed = 0
"""
replace_exact(FEATURE, reuse_old, reuse_new)
