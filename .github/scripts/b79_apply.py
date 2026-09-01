from pathlib import Path


def replace_exact(path, old, new, expected=1):
    p = Path(path)
    text = p.read_text()
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{path}: expected {expected} matches, found {count}")
    p.write_text(text.replace(old, new, expected))


root = "ChatGPTClient/RootViewController.swift"
feature = "ChatGPTClient/Conversation/ConversationFeature.swift"

replace_exact(root, '''    func observeExistingConversation(conversationID: String, events: @escaping (CoveredWebSendEvent) -> Void) {
        precondition(Thread.isMainThread)
        guard !conversationID.isEmpty else { return }
        observationEvents = events
        observingExternalResponse = true
        if currentConversationID == conversationID {
            webView.evaluateJavaScript("window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.probeComposer(true);", completionHandler: nil)
            return
        }
        composerReadyConversationID = nil
        currentConversationID = conversationID
        guard let encoded = conversationID.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed), let url = URL(string: "https://chatgpt.com/c/\\(encoded)") else { return }
        webView.load(URLRequest(url: url))
        diagnostics.info(category: "webSend", name: "coveredExecutor.observing", fields: ["target": "existing_conversation"])
    }
''', '''    func observeExistingConversation(conversationID: String, forceReload: Bool = false, events: @escaping (CoveredWebSendEvent) -> Void) {
        precondition(Thread.isMainThread)
        guard !conversationID.isEmpty else { return }
        observationEvents = events
        observingExternalResponse = true
        if currentConversationID == conversationID, !forceReload {
            webView.evaluateJavaScript("window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.probeComposer(true);", completionHandler: nil)
            return
        }
        composerReadyConversationID = nil
        currentConversationID = conversationID
        guard let encoded = conversationID.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed), let url = URL(string: "https://chatgpt.com/c/\\(encoded)") else { return }
        webView.load(URLRequest(url: url))
        diagnostics.info(category: "webSend", name: "coveredExecutor.observing", fields: ["target": "existing_conversation", "mode": forceReload ? "manual_sync_rearm" : "selection"])
    }
''')

replace_exact(root, '''struct ConversationLiveResponseSnapshot {
    let generation: Int
    let conversationID: String
    let baselineVisibleMessageCount: Int
    let promptText: String
    var phase: ConversationLiveResponsePhase
    var timeline: [ConversationResponseTimelineItem]
    var finalText: String
    var reasoningEnded: Bool
    var reasoningDurationSeconds: Int?
    var failureReason: String?
}
''', '''struct ConversationLiveResponseSnapshot {
    let generation: Int
    let conversationID: String
    let baselineVisibleMessageCount: Int
    let promptText: String
    var phase: ConversationLiveResponsePhase
    var timeline: [ConversationResponseTimelineItem]
    var finalText: String
    var reasoningEnded: Bool
    var reasoningDurationSeconds: Int?
    var failureReason: String?

    var isExternalStoppedWithoutFinal: Bool { promptText.isEmpty && phase == .completed && !reasoningEnded && finalText.isEmpty && !timeline.isEmpty }
}
''')

replace_exact(root, '''    case .terminal:
        if !snapshot.reasoningEnded, snapshot.finalText.isEmpty {
            let provisionalFinal = snapshot.timeline.filter { $0.kind == .reasoning }.map(\\.text).joined(separator: "\\n\\n").trimmingCharacters(in: .whitespacesAndNewlines)
            if !provisionalFinal.isEmpty {
                snapshot.finalText = provisionalFinal
                snapshot.timeline.removeAll { $0.kind == .reasoning }
            }
        }
        snapshot.phase = .completed
        eventName = "terminal"
''', '''    case .terminal:
        if !snapshot.reasoningEnded, snapshot.finalText.isEmpty, !snapshot.promptText.isEmpty {
            let provisionalFinal = snapshot.timeline.filter { $0.kind == .reasoning }.map(\\.text).joined(separator: "\\n\\n").trimmingCharacters(in: .whitespacesAndNewlines)
            if !provisionalFinal.isEmpty {
                snapshot.finalText = provisionalFinal
                snapshot.timeline.removeAll { $0.kind == .reasoning }
            }
        }
        snapshot.phase = .completed
        eventName = "terminal"
''')

replace_exact(root, '''        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.releaseIdleExecutors(except: id)
            self.repository.selectConversation(id: id)
            self.detailViewController.loadViewIfNeeded()
            self.detailViewController.title = self.repository.conversations.first(where: { $0.id == id })?.title ?? "新对话"
            self.detailViewController.showConversation(id: id)
            self.detailNavigationController.setToolbarHidden(false, animated: false)
            self.updateLivePresentation()
            self.show(.secondary)
            self.observeExternalResponseIfNeeded(conversationID: id)
        }
''', '''        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.releaseIdleExecutors(except: id)
            self.repository.selectConversation(id: id)
            self.detailViewController.loadViewIfNeeded()
            self.detailViewController.title = self.repository.conversations.first(where: { $0.id == id })?.title ?? "新对话"
            self.detailViewController.showConversation(id: id)
            self.detailNavigationController.setToolbarHidden(false, animated: false)
            self.updateLivePresentation()
            self.show(.secondary)
            self.observeExternalResponseIfNeeded(conversationID: id)
        }
        detailViewController.onManualLatestSyncApplied = { [weak self] id, latestUserChanged in
            guard let self, latestUserChanged, self.repository.selectedConversationID == id, !self.repository.isLiveResponseActive(for: id) else { return }
            self.observeExternalResponseIfNeeded(conversationID: id, forcePageReload: true)
        }
''')

replace_exact(root, '''    private func observeExternalResponseIfNeeded(conversationID: String) {
        guard repository.selectedConversationID == conversationID, !repository.isLiveResponseActive(for: conversationID) else { return }
        let sendExecutor = executor(for: conversationID)
        var externalGeneration: Int?
        sendExecutor.observeExistingConversation(conversationID: conversationID) { [weak self, weak sendExecutor] event in
''', '''    private func observeExternalResponseIfNeeded(conversationID: String, forcePageReload: Bool = false) {
        guard repository.selectedConversationID == conversationID, !repository.isLiveResponseActive(for: conversationID) else { return }
        let sendExecutor = executor(for: conversationID)
        var externalGeneration: Int?
        sendExecutor.observeExistingConversation(conversationID: conversationID, forceReload: forcePageReload) { [weak self, weak sendExecutor] event in
''')

replace_exact(feature, '''final class ConversationDetailViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    private struct ScrollAnchor {
''', '''final class ConversationDetailViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    var onManualLatestSyncApplied: ((String, Bool) -> Void)?

    private struct ScrollAnchor {
''')

replace_exact(feature, '''    let bodyText: String
    if !snapshot.finalText.isEmpty { bodyText = snapshot.finalText }
    else {
        switch snapshot.phase {
        case .preparing: bodyText = "正在发送…"
        case .thinking, .reasoning: bodyText = "正在思考…"
        case .final: bodyText = "正在生成回答…"
        case .completed: bodyText = "正在同步最新消息…"
        case .failed: bodyText = "回答失败"
        }
    }
''', '''    let bodyText: String
    if snapshot.isExternalStoppedWithoutFinal { bodyText = "" }
    else if !snapshot.finalText.isEmpty { bodyText = snapshot.finalText }
    else {
        switch snapshot.phase {
        case .preparing: bodyText = "正在发送…"
        case .thinking, .reasoning: bodyText = "正在思考…"
        case .final: bodyText = "正在生成回答…"
        case .completed: bodyText = "正在同步最新消息…"
        case .failed: bodyText = "回答失败"
        }
    }
''')

replace_exact(feature, '        let showsCopy = message.role == .assistant && !snapshot.phase.isActive && row.isLastChunk\n', '        let showsCopy = message.role == .assistant && !snapshot.phase.isActive && !message.text.isEmpty && row.isLastChunk\n')

replace_exact(feature, '''        if !snapshot.reasoningEnded, !autoOpened.contains(messageID) {
            autoOpened.insert(messageID)
            expanded.insert(messageID)
            expansionChanged = true
        }
        if snapshot.reasoningEnded, !autoCollapsed.contains(messageID) {
            autoCollapsed.insert(messageID)
            expanded.remove(messageID)
            expansionChanged = true
        }
''', '''        if snapshot.phase.isActive, !snapshot.reasoningEnded, !autoOpened.contains(messageID) {
            autoOpened.insert(messageID)
            expanded.insert(messageID)
            expansionChanged = true
        }
        if (snapshot.reasoningEnded || snapshot.isExternalStoppedWithoutFinal), !autoCollapsed.contains(messageID) {
            autoCollapsed.insert(messageID)
            expanded.remove(messageID)
            expansionChanged = true
        }
''')

replace_exact(feature, '''        let previousMessages = messages
        let hadLoadedDetail = repository.selectedConversation?.id == id
''', '''        let previousMessages = messages
        let previousLatestUserID = previousMessages.last(where: { $0.role == .user })?.id
        let hadLoadedDetail = repository.selectedConversation?.id == id
''')

replace_exact(feature, '''            case .success(let detail):
                let changed = self.hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
                _ = self.repository.clearTerminalExternalLiveResponseAfterAuthoritativeRefresh(conversationID: id)
                self.apply(detail) { [weak self] in self?.showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0) }
''', '''            case .success(let detail):
                let changed = self.hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
                let latestUserChanged = detail.messages.last(where: { $0.role == .user })?.id != previousLatestUserID
                _ = self.repository.clearTerminalExternalLiveResponseAfterAuthoritativeRefresh(conversationID: id)
                self.apply(detail) { [weak self] in
                    guard let self else { return }
                    self.showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0)
                    self.onManualLatestSyncApplied?(id, latestUserChanged)
                }
''')

replace_exact(feature, '    let showsCopy = message.role == .assistant && !snapshot.phase.isActive && presentationRow.isLastChunk\n', '    let showsCopy = message.role == .assistant && !snapshot.phase.isActive && !message.text.isEmpty && presentationRow.isLastChunk\n')

replace_exact(feature, '''    cell.configure(with: message, text: presentationRow.text, showTimestamp: false, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !snapshot.finalText.isEmpty, metrics: livePresentationRowMetrics[liveRow], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: responseTimeline.isEmpty ? nil : { [weak self] in self?.toggleReasoningDisclosure(message: message, indexPath: indexPath, live: true) }, onToggleToolDetail: reasoningExpanded && hasTools ? { [weak self] _, _ in self?.presentToolList(message: message) } : nil)
''', '''    cell.configure(with: message, text: presentationRow.text, showTimestamp: false, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !snapshot.finalText.isEmpty, reasoningTitle: snapshot.isExternalStoppedWithoutFinal ? "已停止思考" : nil, metrics: livePresentationRowMetrics[liveRow], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: responseTimeline.isEmpty ? nil : { [weak self] in self?.toggleReasoningDisclosure(message: message, indexPath: indexPath, live: true) }, onToggleToolDetail: reasoningExpanded && hasTools ? { [weak self] _, _ in self?.presentToolList(message: message) } : nil)
''')

replace_exact(feature, '''    func configure(with message: ConversationMessage, text: String, showTimestamp: Bool, showCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, toolDisclosureState: ConversationToolDisclosureState, showsReasoningDivider: Bool, metrics: Metrics, onCopy: (() -> Void)?, onToggleReasoning: (() -> Void)?, onToggleToolDetail: ((Int, ConversationToolDetailSection) -> Void)?) {
''', '''    func configure(with message: ConversationMessage, text: String, showTimestamp: Bool, showCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, toolDisclosureState: ConversationToolDisclosureState, showsReasoningDivider: Bool, reasoningTitle: String? = nil, metrics: Metrics, onCopy: (() -> Void)?, onToggleReasoning: (() -> Void)?, onToggleToolDetail: ((Int, ConversationToolDetailSection) -> Void)?) {
''')

replace_exact(feature, '    reasoningButton.setTitle(showsReasoning ? ConversationReasoningPresentation.summaryTitle(durationSeconds: message.reasoningDurationSeconds) : nil, for: .normal)\n', '    reasoningButton.setTitle(showsReasoning ? (reasoningTitle ?? ConversationReasoningPresentation.summaryTitle(durationSeconds: message.reasoningDurationSeconds)) : nil, for: .normal)\n')

replace_exact(feature, '''        reasoningParagraph.paragraphSpacing = 12
        let toolParagraph = NSMutableParagraphStyle()
        toolParagraph.minimumLineHeight = toolLineHeight
        toolParagraph.maximumLineHeight = toolLineHeight
        toolParagraph.paragraphSpacingBefore = 0
        toolParagraph.paragraphSpacing = 12
        let reasoningAttributes: [NSAttributedString.Key: Any] = [.font: reasoningFont, .foregroundColor: UIColor.label, .paragraphStyle: reasoningParagraph]
        let toolAttributes: [NSAttributedString.Key: Any] = [.font: toolFont, .foregroundColor: UIColor.label, .paragraphStyle: toolParagraph]
        var separatorAttributes: [NSAttributedString.Key: Any]?
''', '''        reasoningParagraph.paragraphSpacing = 0
        let toolParagraph = NSMutableParagraphStyle()
        toolParagraph.minimumLineHeight = toolLineHeight
        toolParagraph.maximumLineHeight = toolLineHeight
        toolParagraph.paragraphSpacingBefore = 0
        toolParagraph.paragraphSpacing = 0
        let separatorParagraph = NSMutableParagraphStyle()
        separatorParagraph.minimumLineHeight = 12
        separatorParagraph.maximumLineHeight = 12
        let reasoningAttributes: [NSAttributedString.Key: Any] = [.font: reasoningFont, .foregroundColor: UIColor.label, .paragraphStyle: reasoningParagraph]
        let toolAttributes: [NSAttributedString.Key: Any] = [.font: toolFont, .foregroundColor: UIColor.label, .paragraphStyle: toolParagraph]
        let separatorAttributes: [NSAttributedString.Key: Any] = [.font: UIFont.systemFont(ofSize: 1), .foregroundColor: UIColor.clear, .paragraphStyle: separatorParagraph]
''')
replace_exact(feature, '            if output.length > 0, let separatorAttributes { output.append(NSAttributedString(string: "\\n", attributes: separatorAttributes)) }\n', '            if output.length > 0 { output.append(NSAttributedString(string: "\\n\\u{200B}\\n", attributes: separatorAttributes)) }\n')
replace_exact(feature, '                output.append(NSAttributedString(string: normalized, attributes: reasoningAttributes))\n                separatorAttributes = reasoningAttributes\n', '                output.append(NSAttributedString(string: normalized, attributes: reasoningAttributes))\n')
replace_exact(feature, '                if let slot = item.toolSlot, let url = URL(string: "chatgpt-tool-list://slot/\\(slot)") { output.addAttribute(.link, value: url, range: NSRange(location: start, length: output.length - start)) }\n                separatorAttributes = toolAttributes\n', '                if let slot = item.toolSlot, let url = URL(string: "chatgpt-tool-list://slot/\\(slot)") { output.addAttribute(.link, value: url, range: NSRange(location: start, length: output.length - start)) }\n')

p = Path("ChatGPTClient.xcodeproj/project.pbxproj")
text = p.read_text()
if text.count("CURRENT_PROJECT_VERSION = 78;") != 2 or text.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b78";') != 2:
    raise SystemExit("unexpected b78 Xcode identity count")
text = text.replace("CURRENT_PROJECT_VERSION = 78;", "CURRENT_PROJECT_VERSION = 79;")
text = text.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b78";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b79";')
p.write_text(text)

p = Path(".github/workflows/ios-foundation.yml")
text = p.read_text()
if text.count("DEV-send-stream-0.1.0-b78") != 2:
    raise SystemExit("unexpected b78 workflow identity count")
p.write_text(text.replace("DEV-send-stream-0.1.0-b78", "DEV-send-stream-0.1.0-b79"))
