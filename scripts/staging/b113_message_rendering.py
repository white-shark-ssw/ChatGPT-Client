from pathlib import Path

project_path = Path("ChatGPTClient.xcodeproj/project.pbxproj")
source_path = Path("ChatGPTClient/Conversation/ConversationFeature.swift")

project = project_path.read_text()
source = source_path.read_text()

if project.count("CURRENT_PROJECT_VERSION = 112;") != 2:
    raise SystemExit("expected exact Build112 baseline")
if project.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b112";') != 2:
    raise SystemExit("expected exact b112 candidate baseline")
project = project.replace("CURRENT_PROJECT_VERSION = 112;", "CURRENT_PROJECT_VERSION = 113;")
project = project.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b112";', 'DIAGNOSTICS_CANDIDATE = "DEV-message-rendering-0.1.0-b113";')

projection_start = source.index("struct ConversationMessagePresentationProjection {")
projection_end = source.index("\n\nstruct ConversationDetail {", projection_start)
renderer_and_projection = r'''enum ConversationMessageRichTextRenderer {
    static let bodyFont = UIFont.preferredFont(forTextStyle: .body)
    static let assistantLineHeight: CGFloat = 36 * 0.70

    static func render(_ text: String, role: ConversationMessage.Role, renderAssistantMarkdown: Bool = true) -> NSAttributedString {
        switch role {
        case .user: return renderUser(text)
        case .assistant: return renderAssistantMarkdown ? renderAssistant(text) : renderAssistantPlain(text)
        }
    }

    private static func renderUser(_ text: String) -> NSAttributedString {
        let paragraph = NSMutableParagraphStyle()
        paragraph.lineBreakMode = .byCharWrapping
        let output = NSMutableAttributedString()
        appendInline(text, to: output, font: bodyFont, color: .label, paragraph: paragraph)
        return output
    }

    private static func renderAssistantPlain(_ text: String) -> NSAttributedString {
        let paragraph = assistantParagraph()
        return NSAttributedString(string: text, attributes: textAttributes(font: bodyFont, color: .label, paragraph: paragraph))
    }

    private static func renderAssistant(_ text: String) -> NSAttributedString {
        let lines = text.components(separatedBy: "\n")
        let output = NSMutableAttributedString()
        var index = 0
        while index < lines.count {
            let line = lines[index]
            let trimmed = line.trimmingCharacters(in: .whitespaces)
            if trimmed.hasPrefix("```") {
                var codeLines: [String] = []
                index += 1
                while index < lines.count && !lines[index].trimmingCharacters(in: .whitespaces).hasPrefix("```") {
                    codeLines.append(lines[index])
                    index += 1
                }
                if index < lines.count { index += 1 }
                appendCodeBlock(codeLines, to: output)
                if index < lines.count { appendNewline(to: output) }
                continue
            }
            if index + 1 < lines.count, let headerCells = tableCells(line), isTableSeparator(lines[index + 1]) {
                var rows: [[String]] = [headerCells]
                var next = index + 2
                while next < lines.count, let cells = tableCells(lines[next]), !isTableSeparator(lines[next]) {
                    rows.append(cells)
                    next += 1
                }
                appendTable(rows, to: output)
                index = next
                if index < lines.count { appendNewline(to: output) }
                continue
            }
            if let heading = heading(line) {
                let scale: CGFloat
                switch heading.level { case 1: scale = 1.40; case 2: scale = 1.30; case 3: scale = 1.20; default: scale = 1.10 }
                let headingFont = UIFont.systemFont(ofSize: bodyFont.pointSize * scale, weight: .semibold)
                let paragraph = assistantParagraph(lineHeight: max(assistantLineHeight, ceil(headingFont.lineHeight) + 2), spacingAfter: 4)
                appendInline(heading.text, to: output, font: headingFont, color: .label, paragraph: paragraph)
            } else if let item = unorderedListItem(line) {
                let paragraph = assistantParagraph(); paragraph.headIndent = 18; paragraph.firstLineHeadIndent = 0
                output.append(NSAttributedString(string: "• ", attributes: textAttributes(font: bodyFont, color: .label, paragraph: paragraph)))
                appendInline(item, to: output, font: bodyFont, color: .label, paragraph: paragraph)
            } else if let item = orderedListItem(line) {
                let paragraph = assistantParagraph(); paragraph.headIndent = 24; paragraph.firstLineHeadIndent = 0
                output.append(NSAttributedString(string: item.prefix + " ", attributes: textAttributes(font: bodyFont, color: .label, paragraph: paragraph)))
                appendInline(item.text, to: output, font: bodyFont, color: .label, paragraph: paragraph)
            } else if trimmed.hasPrefix("> ") {
                let paragraph = assistantParagraph(); paragraph.headIndent = 14; paragraph.firstLineHeadIndent = 0
                output.append(NSAttributedString(string: "│ ", attributes: textAttributes(font: bodyFont, color: .secondaryLabel, paragraph: paragraph)))
                appendInline(String(trimmed.dropFirst(2)), to: output, font: bodyFont, color: .secondaryLabel, paragraph: paragraph)
            } else if isHorizontalRule(trimmed) {
                output.append(NSAttributedString(string: "────────", attributes: textAttributes(font: bodyFont, color: .separator, paragraph: assistantParagraph())))
            } else {
                appendInline(line, to: output, font: bodyFont, color: .label, paragraph: assistantParagraph())
            }
            if index + 1 < lines.count { appendNewline(to: output) }
            index += 1
        }
        return output
    }

    private static func assistantParagraph(lineHeight: CGFloat = assistantLineHeight, spacingAfter: CGFloat = 0) -> NSMutableParagraphStyle {
        let paragraph = NSMutableParagraphStyle()
        paragraph.minimumLineHeight = lineHeight
        paragraph.maximumLineHeight = lineHeight
        paragraph.paragraphSpacing = spacingAfter
        paragraph.lineBreakMode = .byCharWrapping
        return paragraph
    }

    private static func textAttributes(font: UIFont, color: UIColor, paragraph: NSParagraphStyle, backgroundColor: UIColor? = nil) -> [NSAttributedString.Key: Any] {
        var attributes: [NSAttributedString.Key: Any] = [.font: font, .foregroundColor: color, .paragraphStyle: paragraph]
        if let backgroundColor { attributes[.backgroundColor] = backgroundColor }
        return attributes
    }

    private static func appendNewline(to output: NSMutableAttributedString) {
        output.append(NSAttributedString(string: "\n", attributes: textAttributes(font: bodyFont, color: .label, paragraph: assistantParagraph())))
    }

    private static func appendCodeBlock(_ lines: [String], to output: NSMutableAttributedString) {
        let paragraph = assistantParagraph(lineHeight: max(assistantLineHeight, ceil(bodyFont.lineHeight) + 2))
        let font = UIFont.monospacedSystemFont(ofSize: max(12, bodyFont.pointSize - 1), weight: .regular)
        let value = lines.joined(separator: "\n")
        output.append(NSAttributedString(string: value, attributes: textAttributes(font: font, color: .label, paragraph: paragraph, backgroundColor: .secondarySystemBackground)))
    }

    private static func appendTable(_ rows: [[String]], to output: NSMutableAttributedString) {
        let paragraph = assistantParagraph(lineHeight: max(assistantLineHeight, ceil(bodyFont.lineHeight) + 2))
        for (rowIndex, cells) in rows.enumerated() {
            let font = rowIndex == 0 ? UIFont.systemFont(ofSize: bodyFont.pointSize, weight: .semibold) : bodyFont
            for (cellIndex, cell) in cells.enumerated() {
                if cellIndex > 0 { output.append(NSAttributedString(string: "  │  ", attributes: textAttributes(font: font, color: .tertiaryLabel, paragraph: paragraph))) }
                appendInline(cell, to: output, font: font, color: .label, paragraph: paragraph)
            }
            if rowIndex + 1 < rows.count { output.append(NSAttributedString(string: "\n", attributes: textAttributes(font: font, color: .label, paragraph: paragraph))) }
        }
    }

    private static func appendInline(_ text: String, to output: NSMutableAttributedString, font: UIFont, color: UIColor, paragraph: NSParagraphStyle) {
        var index = text.startIndex
        var buffer = ""
        func flush() {
            guard !buffer.isEmpty else { return }
            output.append(NSAttributedString(string: buffer, attributes: textAttributes(font: font, color: color, paragraph: paragraph)))
            buffer.removeAll(keepingCapacity: true)
        }
        while index < text.endIndex {
            if text[index] == "\u{E200}", let close = text[index...].firstIndex(of: "\u{E201}") {
                let tokenEnd = text.index(after: close)
                let token = String(text[index..<tokenEnd])
                if let citation = citationLabel(token) {
                    flush()
                    let citationFont = UIFont.systemFont(ofSize: max(11, font.pointSize - 2), weight: .medium)
                    output.append(NSAttributedString(string: citation, attributes: textAttributes(font: citationFont, color: .secondaryLabel, paragraph: paragraph, backgroundColor: .secondarySystemFill)))
                    index = tokenEnd
                    continue
                }
            }
            if text[index...].hasPrefix("**") || text[index...].hasPrefix("__") {
                let marker = text[index...].hasPrefix("**") ? "**" : "__"
                let contentStart = text.index(index, offsetBy: 2)
                if let closing = text.range(of: marker, range: contentStart..<text.endIndex), contentStart < closing.lowerBound {
                    flush()
                    appendInline(String(text[contentStart..<closing.lowerBound]), to: output, font: fontByAdding(.traitBold, to: font), color: color, paragraph: paragraph)
                    index = closing.upperBound
                    continue
                }
            }
            if text[index...].hasPrefix("~~") {
                let contentStart = text.index(index, offsetBy: 2)
                if let closing = text.range(of: "~~", range: contentStart..<text.endIndex), contentStart < closing.lowerBound {
                    flush()
                    let value = NSMutableAttributedString()
                    appendInline(String(text[contentStart..<closing.lowerBound]), to: value, font: font, color: color, paragraph: paragraph)
                    if value.length > 0 { value.addAttribute(.strikethroughStyle, value: NSUnderlineStyle.single.rawValue, range: NSRange(location: 0, length: value.length)) }
                    output.append(value)
                    index = closing.upperBound
                    continue
                }
            }
            if text[index] == "`", !text[index...].hasPrefix("```") {
                let contentStart = text.index(after: index)
                if let close = text[contentStart...].firstIndex(of: "`"), contentStart < close {
                    flush()
                    let codeFont = UIFont.monospacedSystemFont(ofSize: max(12, font.pointSize - 1), weight: .regular)
                    output.append(NSAttributedString(string: String(text[contentStart..<close]), attributes: textAttributes(font: codeFont, color: color, paragraph: paragraph, backgroundColor: .secondarySystemBackground)))
                    index = text.index(after: close)
                    continue
                }
            }
            if text[index] == "[", let link = explicitLink(in: text, from: index) {
                flush()
                appendInline(link.label, to: output, font: font, color: .systemBlue, paragraph: paragraph)
                index = link.end
                continue
            }
            if text[index...].hasPrefix("https://") || text[index...].hasPrefix("http://"), let range = bareURLRange(in: text, from: index) {
                flush()
                output.append(NSAttributedString(string: String(text[range]), attributes: textAttributes(font: font, color: .systemBlue, paragraph: paragraph)))
                index = range.upperBound
                continue
            }
            if text[index] == "*" || text[index] == "_" {
                let marker = String(text[index])
                let contentStart = text.index(after: index)
                if let close = text[contentStart...].firstIndex(of: text[index]), contentStart < close {
                    flush()
                    appendInline(String(text[contentStart..<close]), to: output, font: fontByAdding(.traitItalic, to: font), color: color, paragraph: paragraph)
                    index = text.index(after: close)
                    continue
                }
                _ = marker
            }
            buffer.append(text[index])
            index = text.index(after: index)
        }
        flush()
    }

    private static func fontByAdding(_ trait: UIFontDescriptor.SymbolicTraits, to font: UIFont) -> UIFont {
        let traits = font.fontDescriptor.symbolicTraits.union(trait)
        guard let descriptor = font.fontDescriptor.withSymbolicTraits(traits) else { return font }
        return UIFont(descriptor: descriptor, size: font.pointSize)
    }

    private static func explicitLink(in text: String, from start: String.Index) -> (label: String, end: String.Index)? {
        guard let closeBracket = text[start...].firstIndex(of: "]") else { return nil }
        let openParen = text.index(after: closeBracket)
        guard openParen < text.endIndex, text[openParen] == "(" else { return nil }
        let urlStart = text.index(after: openParen)
        guard let closeParen = text[urlStart...].firstIndex(of: ")") else { return nil }
        let url = String(text[urlStart..<closeParen])
        guard url.hasPrefix("https://") || url.hasPrefix("http://") else { return nil }
        return (String(text[text.index(after: start)..<closeBracket]), text.index(after: closeParen))
    }

    private static let bareURLCharacters = CharacterSet(charactersIn: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=%")
    private static let trailingURLPunctuation = CharacterSet(charactersIn: ".,!?;:")

    private static func bareURLRange(in text: String, from start: String.Index) -> Range<String.Index>? {
        var end = start
        while end < text.endIndex {
            let character = text[end]
            guard character.unicodeScalars.count == 1, let scalar = character.unicodeScalars.first, scalar.value < 128, bareURLCharacters.contains(scalar) else { break }
            end = text.index(after: end)
        }
        while end > start {
            let previous = text.index(before: end)
            guard let scalar = text[previous].unicodeScalars.first, trailingURLPunctuation.contains(scalar) else { break }
            end = previous
        }
        let minimumLength = text[start...].hasPrefix("https://") ? 9 : 8
        guard text.distance(from: start, to: end) >= minimumLength else { return nil }
        return start..<end
    }

    private static func citationLabel(_ token: String) -> String? {
        guard token.first == "\u{E200}", token.last == "\u{E201}" else { return nil }
        let inner = String(token.dropFirst().dropLast())
        let fields = inner.split(separator: "\u{E202}", omittingEmptySubsequences: false).map(String.init)
        guard let kind = fields.first else { return nil }
        if kind == "filecite" {
            let location = fields.dropFirst().last(where: { $0.hasPrefix("L") })
            return location.map { "〔文件引用 \($0)〕" } ?? "〔文件引用〕"
        }
        if kind == "cite" { return "〔引用〕" }
        return nil
    }

    private static func heading(_ line: String) -> (level: Int, text: String)? {
        let trimmed = line.trimmingCharacters(in: .whitespaces)
        var level = 0
        var index = trimmed.startIndex
        while index < trimmed.endIndex, trimmed[index] == "#", level < 6 { level += 1; index = trimmed.index(after: index) }
        guard level > 0, index < trimmed.endIndex, trimmed[index].isWhitespace else { return nil }
        return (level, String(trimmed[trimmed.index(after: index)...]))
    }

    private static func unorderedListItem(_ line: String) -> String? {
        let trimmed = line.trimmingCharacters(in: .whitespaces)
        for marker in ["- ", "* ", "+ "] where trimmed.hasPrefix(marker) { return String(trimmed.dropFirst(2)) }
        return nil
    }

    private static func orderedListItem(_ line: String) -> (prefix: String, text: String)? {
        let trimmed = line.trimmingCharacters(in: .whitespaces)
        var index = trimmed.startIndex
        while index < trimmed.endIndex, trimmed[index].isNumber { index = trimmed.index(after: index) }
        guard index > trimmed.startIndex, index < trimmed.endIndex, trimmed[index] == "." else { return nil }
        let afterDot = trimmed.index(after: index)
        guard afterDot < trimmed.endIndex, trimmed[afterDot].isWhitespace else { return nil }
        return (String(trimmed[trimmed.startIndex...index]), String(trimmed[trimmed.index(after: afterDot)...]))
    }

    private static func isHorizontalRule(_ line: String) -> Bool {
        let compact = line.replacingOccurrences(of: " ", with: "")
        guard compact.count >= 3, let first = compact.first, first == "-" || first == "*" || first == "_" else { return false }
        return compact.allSatisfy { $0 == first }
    }

    private static func tableCells(_ line: String) -> [String]? {
        var value = line.trimmingCharacters(in: .whitespaces)
        guard value.contains("|") else { return nil }
        if value.hasPrefix("|") { value.removeFirst() }
        if value.hasSuffix("|") { value.removeLast() }
        let cells = value.split(separator: "|", omittingEmptySubsequences: false).map { $0.trimmingCharacters(in: .whitespaces) }
        return cells.count >= 2 ? cells : nil
    }

    private static func isTableSeparator(_ line: String) -> Bool {
        guard let cells = tableCells(line) else { return false }
        return cells.allSatisfy { cell in
            let compact = cell.replacingOccurrences(of: ":", with: "").replacingOccurrences(of: " ", with: "")
            return compact.count >= 3 && compact.allSatisfy { $0 == "-" }
        }
    }
}

struct ConversationMessagePresentationProjection {
    struct Row {
        let messageIndex: Int
        let chunkIndex: Int
        let chunkCount: Int
        let attributedText: NSAttributedString

        var text: String { attributedText.string }
        var isFirstChunk: Bool { chunkIndex == 0 }
        var isLastChunk: Bool { chunkIndex == chunkCount - 1 }
    }

    static let chunkCharacterLimit = 1200
    static let empty = ConversationMessagePresentationProjection(rows: [], firstRowByMessageID: [:], chunkedMessageCount: 0, maxChunkCharacterCount: 0)

    let rows: [Row]
    let firstRowByMessageID: [String: Int]
    let chunkedMessageCount: Int
    let maxChunkCharacterCount: Int

    static func derive(from messages: [ConversationMessage], renderAssistantMarkdown: Bool = true) -> ConversationMessagePresentationProjection {
        var rows: [Row] = []
        var firstRowByMessageID: [String: Int] = [:]
        var chunkedMessageCount = 0
        var maxChunkCharacterCount = 0
        for (messageIndex, message) in messages.enumerated() {
            let rendered = ConversationMessageRichTextRenderer.render(message.text, role: message.role, renderAssistantMarkdown: renderAssistantMarkdown)
            let chunks = presentationChunks(for: rendered)
            if chunks.count > 1 { chunkedMessageCount += 1 }
            for (chunkIndex, chunk) in chunks.enumerated() {
                if firstRowByMessageID[message.id] == nil { firstRowByMessageID[message.id] = rows.count }
                maxChunkCharacterCount = max(maxChunkCharacterCount, chunk.string.count)
                rows.append(Row(messageIndex: messageIndex, chunkIndex: chunkIndex, chunkCount: chunks.count, attributedText: chunk))
            }
        }
        return ConversationMessagePresentationProjection(rows: rows, firstRowByMessageID: firstRowByMessageID, chunkedMessageCount: chunkedMessageCount, maxChunkCharacterCount: maxChunkCharacterCount)
    }

    private static func presentationChunks(for attributedText: NSAttributedString) -> [NSAttributedString] {
        let text = attributedText.string
        guard text.count > chunkCharacterLimit else { return [attributedText] }
        var chunks: [NSAttributedString] = []
        var start = text.startIndex
        while start < text.endIndex {
            guard let hardEnd = text.index(start, offsetBy: chunkCharacterLimit, limitedBy: text.endIndex) else {
                chunks.append(attributedText.attributedSubstring(from: NSRange(start..<text.endIndex, in: text)))
                break
            }
            var end = hardEnd
            if hardEnd < text.endIndex {
                let preferredRange = start..<hardEnd
                if let newline = text.range(of: "\n", options: .backwards, range: preferredRange), text.distance(from: start, to: newline.upperBound) >= chunkCharacterLimit / 2 {
                    end = newline.upperBound
                } else if let whitespace = text.rangeOfCharacter(from: .whitespaces, options: .backwards, range: preferredRange), text.distance(from: start, to: whitespace.upperBound) >= chunkCharacterLimit * 3 / 4 {
                    end = whitespace.upperBound
                }
            }
            if end == start { end = text.index(after: start) }
            chunks.append(attributedText.attributedSubstring(from: NSRange(start..<end, in: text)))
            start = end
        }
        return chunks.isEmpty ? [attributedText] : chunks
    }
}'''
source = source[:projection_start] + renderer_and_projection + source[projection_end:]

source = source.replace("private static let bodyFont = UIFont.preferredFont(forTextStyle: .body)", "private static let bodyFont = ConversationMessageRichTextRenderer.bodyFont", 1)
source = source.replace("private static let compactAssistantLineHeight: CGFloat = toolLineHeight * 0.70", "private static let compactAssistantLineHeight = ConversationMessageRichTextRenderer.assistantLineHeight", 1)

old_config = "func configure(with message: ConversationMessage, text: String, showTimestamp: Bool, showCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, toolDisclosureState: ConversationToolDisclosureState, showsReasoningDivider: Bool, reasoningTitle: String? = nil, metrics: Metrics, onCopy: (() -> Void)?, onToggleReasoning: (() -> Void)?, onToggleToolDetail: ((Int, ConversationToolDetailSection) -> Void)?) {"
new_config = "func configure(with message: ConversationMessage, attributedText: NSAttributedString, showTimestamp: Bool, showCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, toolDisclosureState: ConversationToolDisclosureState, showsReasoningDivider: Bool, reasoningTitle: String? = nil, metrics: Metrics, onCopy: (() -> Void)?, onToggleReasoning: (() -> Void)?, onToggleToolDetail: ((Int, ConversationToolDetailSection) -> Void)?) {"
if source.count(old_config) != 1:
    raise SystemExit("configure signature baseline missing")
source = source.replace(old_config, new_config, 1)
old_switch = """    switch message.role {
    case .assistant: messageLabel.attributedText = Self.assistantBodyAttributedText(text); messageLabel.textColor = .label
    case .user: messageLabel.attributedText = Self.userBodyAttributedText(text)
    }"""
new_switch = """    messageLabel.attributedText = attributedText
    if message.role == .assistant { messageLabel.textColor = .label }"""
if source.count(old_switch) != 1:
    raise SystemExit("configure role renderer baseline missing")
source = source.replace(old_switch, new_switch, 1)

old_metrics_signature = "static func metrics(for text: String, role: ConversationMessage.Role, tableWidth: CGFloat, showsTimestamp: Bool, showsCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, toolDisclosureState: ConversationToolDisclosureState, showsReasoningDivider: Bool) -> Metrics {"
new_metrics_signature = "static func metrics(for attributedText: NSAttributedString, role: ConversationMessage.Role, tableWidth: CGFloat, showsTimestamp: Bool, showsCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, toolDisclosureState: ConversationToolDisclosureState, showsReasoningDivider: Bool) -> Metrics {"
if source.count(old_metrics_signature) != 1:
    raise SystemExit("metrics signature baseline missing")
source = source.replace(old_metrics_signature, new_metrics_signature, 1)
source = source.replace("let textSize = measuredTextSize(text, role: role, maxWidth: maxTextWidth)", "let textSize = measuredTextSize(attributedText, role: role, maxWidth: maxTextWidth)", 1)

render_start = source.index("    private static func assistantBodyAttributedText(_ text: String) -> NSAttributedString {")
render_end = source.index("\n\n    private static func measuredTimelineSize", render_start)
new_measure = r'''    private static func measuredTextSize(_ attributedText: NSAttributedString, role: ConversationMessage.Role, maxWidth: CGFloat) -> CGSize {
        if attributedText.length == 0 { return CGSize(width: 0, height: ceil(role == .assistant ? compactAssistantLineHeight : bodyFont.lineHeight)) }
        let rect = attributedText.boundingRect(with: CGSize(width: maxWidth, height: .greatestFiniteMagnitude), options: [.usesLineFragmentOrigin, .usesFontLeading], context: nil)
        let minimumHeight = role == .assistant ? compactAssistantLineHeight : bodyFont.lineHeight
        return CGSize(width: min(maxWidth, ceil(rect.width)), height: max(ceil(minimumHeight), ceil(rect.height) + 1))
    }'''
source = source[:render_start] + new_measure + source[render_end:]

source = source.replace("ConversationMessageCell.metrics(for: row.text,", "ConversationMessageCell.metrics(for: row.attributedText,", 5)
source = source.replace("cell.configure(with: message, text: presentationRow.text,", "cell.configure(with: message, attributedText: presentationRow.attributedText,", 2)
old_live_derive = "liveMessagePresentation = ConversationMessagePresentationProjection.derive(from: livePresentationMessages)"
new_live_derive = "liveMessagePresentation = ConversationMessagePresentationProjection.derive(from: livePresentationMessages, renderAssistantMarkdown: !snapshot.phase.isActive)"
if source.count(old_live_derive) != 1:
    raise SystemExit("live presentation derive baseline missing")
source = source.replace(old_live_derive, new_live_derive, 1)

if "assistantBodyAttributedText" in source or "userBodyAttributedText" in source:
    raise SystemExit("legacy body renderers still present")
if source.count("ConversationMessageCell.metrics(for: row.attributedText,") != 5:
    raise SystemExit("not all row metric call sites migrated")
if source.count("cell.configure(with: message, attributedText: presentationRow.attributedText,") != 2:
    raise SystemExit("not all cell configure call sites migrated")
if source.count('static let userReuseIdentifier = "ConversationMessageCell.user"') != 1 or source.count('static let assistantReuseIdentifier = "ConversationMessageCell.assistant"') != 1:
    raise SystemExit("b112 role-isolated reuse invariant missing")

project_path.write_text(project)
source_path.write_text(source)
