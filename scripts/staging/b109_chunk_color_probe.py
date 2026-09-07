from pathlib import Path

PROJECT = Path("ChatGPTClient.xcodeproj/project.pbxproj")
FEATURE = Path("ChatGPTClient/Conversation/ConversationFeature.swift")


def replace_exact(path: Path, old: str, new: str, expected_count: int = 1) -> None:
    text = path.read_text()
    actual = text.count(old)
    if actual != expected_count:
        raise SystemExit(f"{path}: expected {expected_count} occurrences, found {actual}: {old!r}")
    path.write_text(text.replace(old, new, expected_count))


replace_exact(PROJECT, "CURRENT_PROJECT_VERSION = 108;", "CURRENT_PROJECT_VERSION = 109;", 2)
replace_exact(PROJECT, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b108";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b109";', 2)

prepare_marker = """        copyButton.isHidden = true
    }

    override func layoutSubviews() {
"""
prepare_replacement = """        copyButton.isHidden = true
    }

    func bodyColorDiagnostics() -> [String: String] {
        var fields: [String: String] = [
            "labelTextColor": diagnosticsColor(messageLabel.textColor),
            "labelHighlightedTextColor": diagnosticsColor(messageLabel.highlightedTextColor),
            "labelTintColor": diagnosticsColor(messageLabel.tintColor),
            "labelIsHighlighted": String(messageLabel.isHighlighted),
            "cellIsHighlighted": String(isHighlighted),
            "cellIsSelected": String(isSelected),
            "interfaceStyle": traitCollection.userInterfaceStyle == .dark ? "dark" : (traitCollection.userInterfaceStyle == .light ? "light" : "unspecified")
        ]
        if let attributedText = messageLabel.attributedText, attributedText.length > 0 {
            fields["attributedForegroundColor"] = diagnosticsColor(attributedText.attribute(.foregroundColor, at: 0, effectiveRange: nil) as? UIColor)
        } else {
            fields["attributedForegroundColor"] = "none"
        }
        return fields
    }

    private func diagnosticsColor(_ color: UIColor?) -> String {
        guard let color else { return "none" }
        let resolved = color.resolvedColor(with: traitCollection)
        var red: CGFloat = 0
        var green: CGFloat = 0
        var blue: CGFloat = 0
        var alpha: CGFloat = 0
        if resolved.getRed(&red, green: &green, blue: &blue, alpha: &alpha) {
            return String(format: "rgba:%.3f,%.3f,%.3f,%.3f", red, green, blue, alpha)
        }
        var white: CGFloat = 0
        if resolved.getWhite(&white, alpha: &alpha) { return String(format: "white:%.3f,%.3f", white, alpha) }
        return resolved.description
    }

    override func layoutSubviews() {
"""
replace_exact(FEATURE, prepare_marker, prepare_replacement)

cell_marker = """    return cell
}

    func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration? {
"""
cell_replacement = """    return cell
}

    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        guard let messageCell = cell as? ConversationMessageCell else { return }
        if indexPath.row < messagePresentation.rows.count {
            guard messagePresentation.rows.indices.contains(indexPath.row) else { return }
            let row = messagePresentation.rows[indexPath.row]
            guard messages.indices.contains(row.messageIndex), messages[row.messageIndex].role == .assistant, row.chunkCount > 1 else { return }
            var fields = messageCell.bodyColorDiagnostics()
            fields["surface"] = "authoritative"
            fields["rowIndex"] = String(indexPath.row)
            fields["chunkIndex"] = String(row.chunkIndex)
            fields["chunkCount"] = String(row.chunkCount)
            diagnostics.info(category: "ui", name: "assistantChunkColor.willDisplay", fields: fields)
            return
        }
        let liveRow = indexPath.row - messagePresentation.rows.count
        guard liveMessagePresentation.rows.indices.contains(liveRow) else { return }
        let row = liveMessagePresentation.rows[liveRow]
        guard livePresentationMessages.indices.contains(row.messageIndex), livePresentationMessages[row.messageIndex].role == .assistant, row.chunkCount > 1 else { return }
        var fields = messageCell.bodyColorDiagnostics()
        fields["surface"] = "live"
        fields["rowIndex"] = String(indexPath.row)
        fields["chunkIndex"] = String(row.chunkIndex)
        fields["chunkCount"] = String(row.chunkCount)
        diagnostics.info(category: "ui", name: "assistantChunkColor.willDisplay", fields: fields)
    }

    func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration? {
"""
replace_exact(FEATURE, cell_marker, cell_replacement)
