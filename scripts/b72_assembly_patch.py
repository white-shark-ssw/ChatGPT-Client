from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)

conversation_path = Path("ChatGPTClient/Conversation/ConversationFeature.swift")
conversation = conversation_path.read_text()

conversation = replace_once(conversation,
'''enum ConversationToolIconKind: String, Equatable {
    case generic
    case code
    case github
}''',
'''enum ConversationToolIconKind: String, Equatable {
    case generic
    case connector
    case code
    case github
}''', "tool icon enum")

conversation = replace_once(conversation,
'''                    let iconKind: ConversationToolIconKind = normalizedRecipient == "api_tool.call_tool" ? .generic : .code''',
'''                    let iconKind: ConversationToolIconKind = normalizedRecipient == "api_tool.call_tool" ? .connector : .code''', "historical connector icon")

conversation = replace_once(conversation,
'''    private var displayedConversationID: String?
    private var scrollAnchorsByConversationID: [String: ScrollAnchor] = [:]''',
'''    private var displayedConversationID: String?
    private var scrollAnchorsByConversationID: [String: ScrollAnchor] = [:]
    private var expandedReasoningMessageIDsByConversationID: [String: Set<String>] = [:]''', "reasoning expansion state")

conversation = replace_once(conversation,
'''        displayedConversationID = nil
        scrollAnchorsByConversationID.removeAll()
        activityIndicator.stopAnimating()''',
'''        displayedConversationID = nil
        scrollAnchorsByConversationID.removeAll()
        expandedReasoningMessageIDsByConversationID.removeAll()
        activityIndicator.stopAnimating()''', "account reset expansion")

conversation = replace_once(conversation,
'''            let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
            let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: showsTimestamp, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: false, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !row.text.isEmpty)''',
'''            let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
            let reasoningExpanded = displayedConversationID.map { isReasoningExpanded(messageID: message.id, conversationID: $0) } ?? false
            let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: showsTimestamp, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !row.text.isEmpty)''', "historical geometry expansion")

conversation = replace_once(conversation,
'''        let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
        let showsCopy = message.role == .assistant && !snapshot.phase.isActive && row.isLastChunk
        let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: false, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: false, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !snapshot.finalText.isEmpty)''',
'''        let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
        let showsCopy = message.role == .assistant && !snapshot.phase.isActive && row.isLastChunk
        let reasoningExpanded = isReasoningExpanded(messageID: message.id, conversationID: id)
        let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: false, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !snapshot.finalText.isEmpty)''', "live geometry expansion")

old_present = '''    private func presentReasoningDetail(message: ConversationMessage) {
    guard !message.responseTimeline.isEmpty else { return }
    let controller = ConversationReasoningDetailViewController(timeline: message.responseTimeline, durationSeconds: message.reasoningDurationSeconds)
    controller.modalPresentationStyle = .pageSheet
    if #available(iOS 15.0, *), let sheet = controller.sheetPresentationController {
        sheet.prefersGrabberVisible = true
        sheet.preferredCornerRadius = 28
        sheet.prefersScrollingExpandsWhenScrolledToEdge = false
        if #available(iOS 16.0, *) {
            let identifier = UISheetPresentationController.Detent.Identifier("reasoning-detail")
            sheet.detents = [.custom(identifier: identifier) { context in min(context.maximumDetentValue, max(360, context.maximumDetentValue * 0.62)) }, .large()]
            sheet.selectedDetentIdentifier = identifier
        } else {
            sheet.detents = [.medium(), .large()]
            sheet.selectedDetentIdentifier = .medium
        }
    }
    present(controller, animated: true)
    diagnostics.info(category: "interaction", name: "reasoningDetail.presented", fields: ["timelineCount": String(message.responseTimeline.count), "durationKnown": message.reasoningDurationSeconds == nil ? "false" : "true"])
}
'''
new_present = '''    private func isReasoningExpanded(messageID: String, conversationID: String) -> Bool {
        expandedReasoningMessageIDsByConversationID[conversationID]?.contains(messageID) == true
    }

    private func toggleReasoningDisclosure(message: ConversationMessage, indexPath: IndexPath, live: Bool) {
        guard let conversationID = displayedConversationID, !message.responseTimeline.isEmpty else { return }
        let startedAt = ProcessInfo.processInfo.systemUptime
        var expandedIDs = expandedReasoningMessageIDsByConversationID[conversationID] ?? []
        let expanded: Bool
        if expandedIDs.remove(message.id) != nil { expanded = false } else { expandedIDs.insert(message.id); expanded = true }
        expandedReasoningMessageIDsByConversationID[conversationID] = expandedIDs
        var heightDelta: CGFloat = 0
        if live {
            let liveRow = indexPath.row - messagePresentation.rows.count
            guard liveMessagePresentation.rows.indices.contains(liveRow), livePresentationRowMetrics.indices.contains(liveRow), let snapshot = repository.liveResponse(for: conversationID) else { return }
            let row = liveMessagePresentation.rows[liveRow]
            let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
            let showsCopy = message.role == .assistant && !snapshot.phase.isActive && row.isLastChunk
            let oldMetrics = livePresentationRowMetrics[liveRow]
            let newMetrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: effectivePresentationWidth(), showsTimestamp: false, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: expanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !snapshot.finalText.isEmpty)
            heightDelta = newMetrics.rowHeight - oldMetrics.rowHeight
            livePresentationRowMetrics[liveRow] = newMetrics
            livePresentationContentHeight += heightDelta
        } else {
            let rowIndex = indexPath.row
            guard messagePresentation.rows.indices.contains(rowIndex), presentationRowMetrics.indices.contains(rowIndex) else { return }
            let row = messagePresentation.rows[rowIndex]
            let showsTimestamp = row.isFirstChunk && preferences.showsMessageTimestamps && (message.createTime ?? 0) > 0
            let showsCopy = message.role == .assistant && row.isLastChunk
            let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
            let oldMetrics = presentationRowMetrics[rowIndex]
            let newMetrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: effectivePresentationWidth(), showsTimestamp: showsTimestamp, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: expanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !row.text.isEmpty)
            heightDelta = newMetrics.rowHeight - oldMetrics.rowHeight
            presentationRowMetrics[rowIndex] = newMetrics
            if rowIndex + 1 < presentationRowOffsets.count {
                for offsetIndex in (rowIndex + 1)..<presentationRowOffsets.count { presentationRowOffsets[offsetIndex] += heightDelta }
            }
            presentationContentHeight += heightDelta
        }
        UIView.performWithoutAnimation {
            tableView.reloadRows(at: [indexPath], with: .none)
            tableView.layoutIfNeeded()
        }
        diagnostics.info(category: "interaction", name: "reasoningDisclosure.toggled", fields: ["state": expanded ? "expanded" : "collapsed", "surface": live ? "live" : "historical", "heightDeltaPoints": String(format: "%.2f", heightDelta), "durationMs": String(format: "%.2f", (ProcessInfo.processInfo.systemUptime - startedAt) * 1000)])
    }

    private func presentToolList(message: ConversationMessage) {
        let tools = ConversationReasoningPresentation.visibleToolItems(message.responseTimeline)
        guard !tools.isEmpty else { return }
        let controller = ConversationReasoningDetailViewController(timeline: tools, durationSeconds: message.reasoningDurationSeconds)
        controller.modalPresentationStyle = .pageSheet
        if #available(iOS 15.0, *), let sheet = controller.sheetPresentationController {
            sheet.prefersGrabberVisible = true
            sheet.preferredCornerRadius = 28
            sheet.prefersScrollingExpandsWhenScrolledToEdge = false
            if #available(iOS 16.0, *) {
                let identifier = UISheetPresentationController.Detent.Identifier("tool-list")
                sheet.detents = [.custom(identifier: identifier) { context in min(context.maximumDetentValue, max(360, context.maximumDetentValue * 0.62)) }, .large()]
                sheet.selectedDetentIdentifier = identifier
            } else {
                sheet.detents = [.medium(), .large()]
                sheet.selectedDetentIdentifier = .medium
            }
        }
        present(controller, animated: true)
        diagnostics.info(category: "interaction", name: "toolList.presented", fields: ["toolCount": String(tools.count), "durationKnown": message.reasoningDurationSeconds == nil ? "false" : "true"])
    }
'''
conversation = replace_once(conversation, old_present, new_present, "reasoning/tool presentation helpers")

old_hist_cell = '''        let responseTimeline = presentationRow.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
        cell.configure(with: message, text: presentationRow.text, showTimestamp: showsTimestamp, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: false, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !presentationRow.text.isEmpty, metrics: presentationRowMetrics[indexPath.row], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: responseTimeline.isEmpty ? nil : { [weak self] in self?.presentReasoningDetail(message: message) }, onToggleToolDetail: nil)'''
new_hist_cell = '''        let responseTimeline = presentationRow.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
        let reasoningExpanded = displayedConversationID.map { isReasoningExpanded(messageID: message.id, conversationID: $0) } ?? false
        let hasTools = !ConversationReasoningPresentation.visibleToolItems(responseTimeline).isEmpty
        cell.configure(with: message, text: presentationRow.text, showTimestamp: showsTimestamp, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !presentationRow.text.isEmpty, metrics: presentationRowMetrics[indexPath.row], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: responseTimeline.isEmpty ? nil : { [weak self] in self?.toggleReasoningDisclosure(message: message, indexPath: indexPath, live: false) }, onToggleToolDetail: reasoningExpanded && hasTools ? { [weak self] _, _ in self?.presentToolList(message: message) } : nil)'''
conversation = replace_once(conversation, old_hist_cell, new_hist_cell, "historical cell behavior")

old_live_cell = '''    let responseTimeline = presentationRow.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
    let canShowReasoning = !responseTimeline.isEmpty && snapshot.reasoningEnded
    cell.configure(with: message, text: presentationRow.text, showTimestamp: false, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: false, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !snapshot.finalText.isEmpty, metrics: livePresentationRowMetrics[liveRow], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: canShowReasoning ? { [weak self] in self?.presentReasoningDetail(message: message) } : nil, onToggleToolDetail: nil)'''
new_live_cell = '''    let responseTimeline = presentationRow.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
    let reasoningExpanded = isReasoningExpanded(messageID: message.id, conversationID: id)
    let hasTools = !ConversationReasoningPresentation.visibleToolItems(responseTimeline).isEmpty
    cell.configure(with: message, text: presentationRow.text, showTimestamp: false, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !snapshot.finalText.isEmpty, metrics: livePresentationRowMetrics[liveRow], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: responseTimeline.isEmpty ? nil : { [weak self] in self?.toggleReasoningDisclosure(message: message, indexPath: indexPath, live: true) }, onToggleToolDetail: reasoningExpanded && hasTools ? { [weak self] _, _ in self?.presentToolList(message: message) } : nil)'''
conversation = replace_once(conversation, old_live_cell, new_live_cell, "live cell behavior")

conversation = replace_once(conversation,
'''    static func summaryTitle(durationSeconds: Int?) -> String { durationSeconds.map { "思考了 \($0)s⌄" } ?? "思考过程⌄" }''',
'''    static func durationText(seconds: Int?) -> String? {
        guard let seconds, seconds >= 0 else { return nil }
        if seconds < 60 { return "\(seconds)s" }
        let minutes = seconds / 60
        let remainder = seconds % 60
        return remainder == 0 ? "\(minutes)m" : "\(minutes)m \(remainder)s"
    }

    static func summaryTitle(durationSeconds: Int?) -> String { durationText(seconds: durationSeconds).map { "思考了 \($0)" } ?? "思考过程" }''', "duration formatter")

conversation = replace_once(conversation,
'''        case .github:
            let renderer = UIGraphicsImageRenderer(size: CGSize(width: 16, height: 16))''',
'''        case .github:
            let renderer = UIGraphicsImageRenderer(size: CGSize(width: 16, height: 16))''', "github icon anchor")
# Insert connector switch case immediately before code.
conversation = replace_once(conversation,
'''            }
        case .code:
            return UIImage(systemName: "chevron.left.slash.chevron.right", withConfiguration: UIImage.SymbolConfiguration(pointSize: 14, weight: .medium))?.withTintColor(.secondaryLabel, renderingMode: .alwaysOriginal)''',
'''            }
        case .connector:
            return UIImage(systemName: "puzzlepiece.extension", withConfiguration: UIImage.SymbolConfiguration(pointSize: 14, weight: .medium))?.withTintColor(.secondaryLabel, renderingMode: .alwaysOriginal)
        case .code:
            return UIImage(systemName: "chevron.left.slash.chevron.right", withConfiguration: UIImage.SymbolConfiguration(pointSize: 14, weight: .medium))?.withTintColor(.secondaryLabel, renderingMode: .alwaysOriginal)''', "connector icon image")

old_tool_details = '''        content.addArrangedSubview(titleLabel)
        if !item.toolInputJSON.isEmpty { content.addArrangedSubview(ConversationReasoningDisclosureView(title: "工具输入", body: ConversationReasoningPresentation.prettyJSONString(item.toolInputJSON), expanded: true)) }
        if !item.toolOutputJSON.isEmpty { content.addArrangedSubview(ConversationReasoningDisclosureView(title: "工具输出", body: ConversationReasoningPresentation.formattedToolOutput(item.toolOutputJSON), expanded: false)) }
        NSLayoutConstraint.activate(['''
new_tool_details = '''        content.addArrangedSubview(titleLabel)
        if !item.toolInputJSON.isEmpty {
            let inputContainer = UIView()
            inputContainer.backgroundColor = .secondarySystemBackground
            inputContainer.layer.cornerRadius = 12
            let inputLabel = UILabel()
            inputLabel.font = .monospacedSystemFont(ofSize: 13, weight: .regular)
            inputLabel.textColor = .secondaryLabel
            inputLabel.numberOfLines = 0
            inputLabel.lineBreakMode = .byCharWrapping
            inputLabel.text = ConversationReasoningPresentation.prettyJSONString(item.toolInputJSON)
            inputLabel.translatesAutoresizingMaskIntoConstraints = false
            inputContainer.addSubview(inputLabel)
            content.addArrangedSubview(inputContainer)
            NSLayoutConstraint.activate([
                inputLabel.leadingAnchor.constraint(equalTo: inputContainer.leadingAnchor, constant: 12), inputLabel.trailingAnchor.constraint(equalTo: inputContainer.trailingAnchor, constant: -12), inputLabel.topAnchor.constraint(equalTo: inputContainer.topAnchor, constant: 12), inputLabel.bottomAnchor.constraint(equalTo: inputContainer.bottomAnchor, constant: -12)
            ])
        }
        NSLayoutConstraint.activate(['''
conversation = replace_once(conversation, old_tool_details, new_tool_details, "input-only tool view")

old_sheet_loop = '''        for item in timeline {
            switch item.kind {
            case .reasoning:
                let normalized = item.text.trimmingCharacters(in: .whitespacesAndNewlines)
                guard !normalized.isEmpty else { continue }
                let label = UILabel()
                label.font = .systemFont(ofSize: 16, weight: .regular)
                label.textColor = .secondaryLabel
                label.numberOfLines = 0
                let paragraph = NSMutableParagraphStyle(); paragraph.lineSpacing = 4
                label.attributedText = NSAttributedString(string: normalized, attributes: [.font: label.font as Any, .foregroundColor: UIColor.secondaryLabel, .paragraphStyle: paragraph])
                contentStack.addArrangedSubview(label)
            case .tool:
                guard ConversationReasoningPresentation.visibleToolItems([item]).isEmpty == false else { continue }
                contentStack.addArrangedSubview(ConversationReasoningToolView(item: item))
            }
        }'''
new_sheet_loop = '''        for item in ConversationReasoningPresentation.visibleToolItems(timeline) { contentStack.addArrangedSubview(ConversationReasoningToolView(item: item)) }'''
conversation = replace_once(conversation, old_sheet_loop, new_sheet_loop, "tool-only sheet")

conversation = replace_once(conversation,
'''        duration.text = durationSeconds.map { "思考了 \($0)s" } ?? "思考过程"''',
'''        duration.text = ConversationReasoningPresentation.durationText(seconds: durationSeconds).map { "思考了 \($0)" } ?? "思考过程"''', "sheet duration")

conversation = replace_once(conversation,
'''        reasoningButton.addTarget(self, action: #selector(reasoningTapped), for: .touchUpInside)
        bubbleView.addSubview(reasoningButton)
        reasoningTextView.delegate = self
        reasoningTextView.isEditable = false
        reasoningTextView.isSelectable = false''',
'''        reasoningButton.addTarget(self, action: #selector(reasoningTapped), for: .touchUpInside)
        reasoningButton.semanticContentAttribute = .forceRightToLeft
        bubbleView.addSubview(reasoningButton)
        reasoningTextView.delegate = self
        reasoningTextView.isEditable = false
        reasoningTextView.isSelectable = true''', "reasoning controls")

conversation = replace_once(conversation,
'''        reasoningTextView.textContainer.lineFragmentPadding = 0
        reasoningTextView.linkTextAttributes = [.foregroundColor: UIColor.label]
        reasoningTextView.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(reasoningTapped)))
        bubbleView.addSubview(reasoningTextView)''',
'''        reasoningTextView.textContainer.lineFragmentPadding = 0
        reasoningTextView.linkTextAttributes = [.foregroundColor: UIColor.secondaryLabel]
        bubbleView.addSubview(reasoningTextView)''', "remove whole reasoning body tap")

old_config = '''    reasoningButton.isHidden = !showsReasoning
    reasoningButton.isUserInteractionEnabled = showsReasoning && onToggleReasoning != nil
    reasoningButton.setTitle(showsReasoning ? ConversationReasoningPresentation.summaryTitle(durationSeconds: message.reasoningDurationSeconds) : nil, for: .normal)
    reasoningButton.setImage(nil, for: .normal)
    let compact = showsReasoning ? ConversationReasoningPresentation.compactAttributedText(responseTimeline) : NSAttributedString()
    reasoningTextView.attributedText = compact.length > 0 ? compact : nil
    reasoningTextView.isHidden = compact.length == 0
    reasoningTextView.isScrollEnabled = false
    reasoningTextView.isUserInteractionEnabled = compact.length > 0 && onToggleReasoning != nil'''
new_config = '''    reasoningButton.isHidden = !showsReasoning
    reasoningButton.isUserInteractionEnabled = showsReasoning && onToggleReasoning != nil
    reasoningButton.setTitle(showsReasoning ? ConversationReasoningPresentation.summaryTitle(durationSeconds: message.reasoningDurationSeconds) : nil, for: .normal)
    let chevron = UIImage(systemName: reasoningExpanded ? "chevron.up" : "chevron.down", withConfiguration: UIImage.SymbolConfiguration(pointSize: 9, weight: .semibold))
    reasoningButton.setImage(showsReasoning ? chevron : nil, for: .normal)
    reasoningButton.imageEdgeInsets = UIEdgeInsets(top: 0, left: 6, bottom: 0, right: -6)
    let timelineText = showsReasoning && reasoningExpanded ? Self.responseTimelineAttributedText(responseTimeline, disclosureState: toolDisclosureState) : NSAttributedString()
    reasoningTextView.attributedText = timelineText.length > 0 ? timelineText : nil
    reasoningTextView.isHidden = timelineText.length == 0
    reasoningTextView.isScrollEnabled = false
    reasoningTextView.isUserInteractionEnabled = timelineText.length > 0 && onToggleToolDetail != nil'''
conversation = replace_once(conversation, old_config, new_config, "cell expanded presentation")

conversation = replace_once(conversation,
'''        let compactSize = ConversationReasoningPresentation.measuredCompactSize(responseTimeline, maxWidth: maxTextWidth)
        if compactSize.height > 0 {
            bubbleY += 6
            reasoningBodyFrame = CGRect(x: contentInset, y: bubbleY, width: maxTextWidth, height: compactSize.height)
            bubbleY = reasoningBodyFrame.maxY
        }''',
'''        let timelineSize = reasoningExpanded ? measuredTimelineSize(responseTimeline, maxWidth: maxTextWidth, disclosureState: toolDisclosureState) : .zero
        if timelineSize.height > 0 {
            bubbleY += 6
            reasoningBodyFrame = CGRect(x: contentInset, y: bubbleY, width: maxTextWidth, height: timelineSize.height)
            bubbleY = reasoningBodyFrame.maxY
        }''', "expanded timeline metrics")

start = conversation.index('    private static func responseTimelineAttributedText(_ timeline: [ConversationResponseTimelineItem], disclosureState: ConversationToolDisclosureState) -> NSAttributedString {')
end = conversation.index('    private static func measuredTextSize(_ text: String, maxWidth: CGFloat) -> CGSize {', start)
new_timeline_renderer = '''    private static func responseTimelineAttributedText(_ timeline: [ConversationResponseTimelineItem], disclosureState: ConversationToolDisclosureState) -> NSAttributedString {
        let output = NSMutableAttributedString()
        let reasoningParagraph = NSMutableParagraphStyle()
        reasoningParagraph.paragraphSpacing = 5
        let toolParagraph = NSMutableParagraphStyle()
        toolParagraph.paragraphSpacing = 5
        let reasoningAttributes: [NSAttributedString.Key: Any] = [.font: reasoningFont, .foregroundColor: UIColor.secondaryLabel, .paragraphStyle: reasoningParagraph]
        let toolAttributes: [NSAttributedString.Key: Any] = [.font: toolFont, .foregroundColor: UIColor.secondaryLabel, .paragraphStyle: toolParagraph]
        for item in timeline {
            let normalized = item.text.trimmingCharacters(in: .whitespacesAndNewlines)
            guard !normalized.isEmpty else { continue }
            if item.kind == .tool, ConversationReasoningPresentation.visibleToolItems([item]).isEmpty { continue }
            if output.length > 0 { output.append(NSAttributedString(string: "\\n", attributes: reasoningAttributes)) }
            switch item.kind {
            case .reasoning:
                output.append(NSAttributedString(string: normalized, attributes: reasoningAttributes))
            case .tool:
                let start = output.length
                appendToolIcon(item.toolIconKind, to: output)
                if output.length > start { output.append(NSAttributedString(string: "  ", attributes: toolAttributes)) }
                output.append(NSAttributedString(string: normalized, attributes: toolAttributes))
                if !item.completed { output.append(NSAttributedString(string: "  调用中", attributes: [.font: UIFont.systemFont(ofSize: reasoningFont.pointSize - 2, weight: .regular), .foregroundColor: UIColor.tertiaryLabel, .paragraphStyle: toolParagraph])) }
                if let slot = item.toolSlot, let url = URL(string: "chatgpt-tool-list://slot/\\(slot)") { output.addAttribute(.link, value: url, range: NSRange(location: start, length: output.length - start)) }
            }
        }
        return output
    }

    private static func appendToolIcon(_ kind: ConversationToolIconKind, to output: NSMutableAttributedString) {
        guard let image = ConversationReasoningPresentation.toolIconImage(kind) else {
            output.append(NSAttributedString(string: "•", attributes: [.font: toolFont, .foregroundColor: UIColor.secondaryLabel]))
            return
        }
        let attachment = NSTextAttachment()
        attachment.image = image
        attachment.bounds = CGRect(x: 0, y: -2, width: 16, height: 16)
        output.append(NSAttributedString(attachment: attachment))
    }

'''
conversation = conversation[:start] + new_timeline_renderer + conversation[end:]

conversation = replace_once(conversation,
'''        switch URL.scheme {
        case "chatgpt-tool-input": onToggleToolDetail?(slot, .input); return false
        case "chatgpt-tool-output": onToggleToolDetail?(slot, .output); return false
        default: return true
        }''',
'''        switch URL.scheme {
        case "chatgpt-tool-list": onToggleToolDetail?(slot, .input); return false
        case "chatgpt-tool-input": onToggleToolDetail?(slot, .input); return false
        case "chatgpt-tool-output": onToggleToolDetail?(slot, .output); return false
        default: return true
        }''', "tool list link")

conversation_path.write_text(conversation)

root_path = Path("ChatGPTClient/RootViewController.swift")
root = root_path.read_text()

root = replace_once(root,
'''    deinit { webView.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName) }''',
'''    deinit {
        webView.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName)
        webView.removeFromSuperview()
    }''', "executor deinit")

root = replace_once(root,
'''if (!state.invocations.has(message.id)) state.invocations.set(message.id, { recipient: message.recipient, slot: state.nextToolSlot++, connectorPayload: '', iconKind: message.recipient === 'api_tool.call_tool' ? 'generic' : 'code' });''',
'''if (!state.invocations.has(message.id)) state.invocations.set(message.id, { recipient: message.recipient, slot: state.nextToolSlot++, connectorPayload: '', iconKind: message.recipient === 'api_tool.call_tool' ? 'connector' : 'code' });''', "live connector icon")

root = replace_once(root,
'''    private let repository = ConversationRepository()
    private let sendExecutor = CoveredWebSendExecutor()
    private let validationSendButton = UIButton(type: .system)''',
'''    private let repository = ConversationRepository()
    private var sendExecutors: [String: CoveredWebSendExecutor] = [:]
    private let validationSendButton = UIButton(type: .system)''', "executor registry")

root = replace_once(root,
'''            self.sendExecutor.resetForAccountChange()
            self.repository.resetAllLiveResponsesForAccountChange()''',
'''            let executors = Array(self.sendExecutors.values)
            self.sendExecutors.removeAll()
            for executor in executors { executor.resetForAccountChange() }
            self.repository.resetAllLiveResponsesForAccountChange()''', "account reset executors")

root = replace_once(root,
'''        sendExecutor.attachCoveredWebView(to: view)
        detailNavigationController.setToolbarHidden(repository.selectedConversationID == nil, animated: false)''',
'''        detailNavigationController.setToolbarHidden(repository.selectedConversationID == nil, animated: false)''', "remove global executor attachment")

root = replace_once(root,
'''    @objc private func openValidationSendPrompt() {
        guard let conversationID = repository.selectedConversationID, !repository.isLiveResponseActive(for: conversationID), !sendExecutor.isBusy else { return }''',
'''    @objc private func openValidationSendPrompt() {
        guard let conversationID = repository.selectedConversationID, !repository.isLiveResponseActive(for: conversationID) else { return }''', "selected send prompt gate")

old_start = '''    private func startValidationSend(text: String, conversationID: String) {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty, repository.selectedConversationID == conversationID, !sendExecutor.isBusy else { return }
        let generation: Int
        switch repository.beginLiveResponse(conversationID: conversationID, promptText: trimmed) {
        case .success(let value): generation = value
        case .failure(let error):
            showValidationError(error.localizedDescription)
            return
        }
        updateLivePresentation()
        sendExecutor.sendExistingConversation(text: trimmed, conversationID: conversationID) { [weak self] event in
            guard let self else { return }
            self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            if case .terminal = event { self.reconcileTerminalResponse(conversationID: conversationID, generation: generation) }
        }
    }
'''
new_start = '''    private func executor(for conversationID: String) -> CoveredWebSendExecutor {
        if let executor = sendExecutors[conversationID] { return executor }
        let executor = CoveredWebSendExecutor()
        executor.attachCoveredWebView(to: view)
        sendExecutors[conversationID] = executor
        diagnostics.info(category: "webSend", name: "coveredExecutor.created", fields: ["activeExecutorCount": String(sendExecutors.count)])
        return executor
    }

    private func releaseExecutor(for conversationID: String, expected: CoveredWebSendExecutor) {
        guard sendExecutors[conversationID] === expected else { return }
        sendExecutors.removeValue(forKey: conversationID)
        diagnostics.info(category: "webSend", name: "coveredExecutor.released", fields: ["activeExecutorCount": String(sendExecutors.count)])
    }

    private func startValidationSend(text: String, conversationID: String) {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty, repository.selectedConversationID == conversationID else { return }
        let generation: Int
        switch repository.beginLiveResponse(conversationID: conversationID, promptText: trimmed) {
        case .success(let value): generation = value
        case .failure(let error):
            showValidationError(error.localizedDescription)
            return
        }
        updateLivePresentation()
        let sendExecutor = executor(for: conversationID)
        sendExecutor.sendExistingConversation(text: trimmed, conversationID: conversationID) { [weak self, weak sendExecutor] event in
            guard let self, let sendExecutor else { return }
            self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            switch event {
            case .terminal:
                self.releaseExecutor(for: conversationID, expected: sendExecutor)
                self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)
            case .failed:
                self.releaseExecutor(for: conversationID, expected: sendExecutor)
            default: break
            }
        }
    }
'''
root = replace_once(root, old_start, new_start, "per-conversation executor send")

root = replace_once(root,
'''        validationSendButton.isEnabled = !selectedResponseActive && !sendExecutor.isBusy
        validationSendButton.setTitle(selectedResponseActive ? "回答中…" : (sendExecutor.isBusy ? "其他会话回答中…" : "测试发送…"), for: .normal)''',
'''        validationSendButton.isEnabled = !selectedResponseActive
        validationSendButton.setTitle(selectedResponseActive ? "回答中…" : "测试发送…", for: .normal)''', "selected send control")

root_path.write_text(root)

project_path = Path("ChatGPTClient.xcodeproj/project.pbxproj")
project = project_path.read_text()
if project.count("CURRENT_PROJECT_VERSION = 71;") != 2 or project.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b71";') != 2:
    raise SystemExit("project identity anchors changed")
project = project.replace("CURRENT_PROJECT_VERSION = 71;", "CURRENT_PROJECT_VERSION = 72;")
project = project.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b71";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b72";')
project_path.write_text(project)

workflow_path = Path(".github/workflows/ios-foundation.yml")
workflow = workflow_path.read_text()
if workflow.count("DEV-send-stream-0.1.0-b71") != 2:
    raise SystemExit("workflow b71 identity anchors changed")
workflow = workflow.replace("DEV-send-stream-0.1.0-b71", "DEV-send-stream-0.1.0-b72")
workflow_path.write_text(workflow)
