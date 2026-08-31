from pathlib import Path
import re

BASE = 'd43661ef4dd9a01480b11b4d70af5a79e6792bff'


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 match, got {count}')
    return text.replace(old, new, 1)

root_path = Path('ChatGPTClient/RootViewController.swift')
root = root_path.read_text()
root = replace_once(root, '''        case "external_resume_observed":
            if activeEvents == nil, let observationEvents {
                activeEvents = observationEvents
                responseActive = true
                activeEvents?(.externalResumeObserved)
                diagnostics.info(category: "webSend", name: "coveredExecutor.externalResumeObserved", fields: ["target": "existing_conversation"])
            }
        case "resume_response":
            let status = (body["status"] as? NSNumber)?.intValue ?? 0
            let contentType = body["contentType"] as? String ?? ""
            diagnostics.info(category: "webSend", name: "coveredExecutor.resumeResponse", fields: ["httpStatus": String(status), "contentType": Self.safeToken(contentType)])
            if status == 200 && contentType == "text/event-stream" { activeEvents?(.responseAccepted) }
            else if activeEvents != nil { failCurrent("resume_not_sse") }
''', '''        case "external_resume_observed":
            if activeEvents == nil, let observationEvents {
                activeEvents = observationEvents
                activeEvents?(.externalResumeObserved)
                diagnostics.info(category: "webSend", name: "coveredExecutor.externalResumeObserved", fields: ["target": "existing_conversation"])
            }
        case "resume_response":
            let status = (body["status"] as? NSNumber)?.intValue ?? 0
            let contentType = body["contentType"] as? String ?? ""
            diagnostics.info(category: "webSend", name: "coveredExecutor.resumeResponse", fields: ["httpStatus": String(status), "contentType": Self.safeToken(contentType)])
            if status == 200 && contentType == "text/event-stream" {
                responseActive = true
                activeEvents?(.responseAccepted)
            } else if activeEvents != nil {
                failCurrent("resume_not_sse")
            }
''', 'validated resume response gate')

old_observer = '''    private func observeExternalResponseIfNeeded(conversationID: String) {
        guard repository.selectedConversationID == conversationID, !repository.isLiveResponseActive(for: conversationID) else { return }
        let sendExecutor = executor(for: conversationID)
        var externalGeneration: Int?
        sendExecutor.observeExistingConversation(conversationID: conversationID) { [weak self, weak sendExecutor] event in
            guard let self, let sendExecutor else { return }
            if case .externalResumeObserved = event {
                guard externalGeneration == nil, !self.repository.isLiveResponseActive(for: conversationID) else { return }
                switch self.repository.beginExternalLiveResponse(conversationID: conversationID) {
                case .success(let generation):
                    externalGeneration = generation
                    self.updateLivePresentation()
                case .failure:
                    return
                }
                return
            }
            guard let generation = externalGeneration else { return }
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
new_observer = '''    private func observeExternalResponseIfNeeded(conversationID: String) {
        guard repository.selectedConversationID == conversationID, !repository.isLiveResponseActive(for: conversationID) else { return }
        let sendExecutor = executor(for: conversationID)
        var externalGeneration: Int?
        sendExecutor.observeExistingConversation(conversationID: conversationID) { [weak self, weak sendExecutor] event in
            guard let self, let sendExecutor else { return }
            switch event {
            case .externalResumeObserved:
                return
            case .responseAccepted:
                if externalGeneration == nil {
                    guard !self.repository.isLiveResponseActive(for: conversationID) else {
                        self.releaseExecutor(for: conversationID, expected: sendExecutor)
                        return
                    }
                    switch self.repository.beginExternalLiveResponse(conversationID: conversationID) {
                    case .success(let generation):
                        externalGeneration = generation
                        self.updateLivePresentation()
                    case .failure:
                        self.releaseExecutor(for: conversationID, expected: sendExecutor)
                        return
                    }
                }
                guard let generation = externalGeneration else { return }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            case .terminal:
                guard let generation = externalGeneration else {
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    return
                }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
                self.releaseExecutor(for: conversationID, expected: sendExecutor)
                self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)
            case .failed:
                if let generation = externalGeneration { self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation) }
                self.releaseExecutor(for: conversationID, expected: sendExecutor)
            default:
                guard let generation = externalGeneration else { return }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            }
        }
    }
'''
root = replace_once(root, old_observer, new_observer, 'external observer promotion gate')
root_path.write_text(root)

conv_path = Path('ChatGPTClient/Conversation/ConversationFeature.swift')
conv = conv_path.read_text()
conv = replace_once(conv, '''    private var presentationGeneration = 0
    private var displayedConversationID: String?
''', '''    private var presentationGeneration = 0
    private var historicalGeometryBuildGeneration = 0
    private var displayedConversationID: String?
''', 'geometry build generation')

conv = replace_once(conv, '''        captureScrollAnchorForDisplayedConversation()
        displayedConversationID = id
        lastUserDragDirection = .previous
''', '''        captureScrollAnchorForDisplayedConversation()
        lastUserDragDirection = .previous
''', 'defer displayed identity until apply')

conv = replace_once(conv, '''        if let detail = existingDetail {
            loadingConversationID = operationSnapshot == nil ? nil : id
            activityIndicator.stopAnimating()
            apply(detail, captureCurrentAnchor: false)
            logResidentFirstVisible(id: id, startedAt: presentationStart, operationKind: operationSnapshot?.kind)
        } else {
            loadingConversationID = id
            clearVisibleMessagePresentation()
''', '''        if let detail = existingDetail {
            loadingConversationID = operationSnapshot == nil ? nil : id
            activityIndicator.stopAnimating()
            apply(detail, captureCurrentAnchor: false) { [weak self] in
                self?.logResidentFirstVisible(id: id, startedAt: presentationStart, operationKind: operationSnapshot?.kind)
            }
        } else {
            loadingConversationID = id
            displayedConversationID = id
            clearVisibleMessagePresentation()
''', 'resident first visible completion')

conv = replace_once(conv, '''    func resetForAccountScopeChange() {
        presentationGeneration += 1
        stopAnswerJumpAnimation(clearTarget: true)
''', '''    func resetForAccountScopeChange() {
        presentationGeneration += 1
        historicalGeometryBuildGeneration += 1
        stopAnswerJumpAnimation(clearTarget: true)
''', 'cancel geometry on account reset')

start = conv.index('    private func apply(_ detail: ConversationDetail, captureCurrentAnchor: Bool = true) {')
end = conv.index('    private func rebuildLiveResponsePresentation(width: CGFloat) {', start)
new_block = r'''    private func apply(_ detail: ConversationDetail, captureCurrentAnchor: Bool = true, completion: (() -> Void)? = nil) {
        if captureCurrentAnchor, displayedConversationID == detail.id, !messages.isEmpty { captureScrollAnchor(for: detail.id) }
        stopAnswerJumpAnimation(clearTarget: true)
        historicalGeometryBuildGeneration += 1
        let geometryBuildGeneration = historicalGeometryBuildGeneration
        let currentPresentationGeneration = presentationGeneration
        let startedAt = ProcessInfo.processInfo.systemUptime
        let nextRoundProjection = ConversationRoundProjection.derive(from: detail.messages)
        let nextMessagePresentation = ConversationMessagePresentationProjection.derive(from: detail.messages)
        let width = effectivePresentationWidth()
        let geometryStartedAt = ProcessInfo.processInfo.systemUptime
        let previousDisplayedConversationID = displayedConversationID

        if let cached = cachedHistoricalPresentationGeometry(for: detail, roundProjection: nextRoundProjection, messagePresentation: nextMessagePresentation, width: width) {
            let geometryDurationMs = (ProcessInfo.processInfo.systemUptime - geometryStartedAt) * 1000
            installDetailPresentation(detail, roundProjection: nextRoundProjection, messagePresentation: nextMessagePresentation, width: max(1, width), rowMetrics: cached.rowMetrics, rowOffsets: cached.rowOffsets, contentHeight: cached.contentHeight, geometryReused: true, geometryDurationMs: geometryDurationMs, startedAt: startedAt, completion: completion)
            return
        }

        displayedConversationID = detail.id
        title = detail.title
        if previousDisplayedConversationID != detail.id {
            clearVisibleMessagePresentation()
            displayedConversationID = detail.id
            title = detail.title
        }
        stateLabel.text = "正在准备会话…"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        activityIndicator.startAnimating()
        updateHeaderMetadata()
        buildHistoricalPresentationGeometryCooperatively(detail: detail, roundProjection: nextRoundProjection, messagePresentation: nextMessagePresentation, width: width, presentationGeneration: currentPresentationGeneration, geometryBuildGeneration: geometryBuildGeneration, geometryStartedAt: geometryStartedAt, startedAt: startedAt, completion: completion)
    }

    private func clearVisibleMessagePresentation() {
        stopAnswerJumpAnimation(clearTarget: true)
        displayedCurrentNodeID = nil
        messages = []
        roundProjection = ConversationRoundProjection(rounds: [])
        messagePresentation = .empty
        livePresentationMessages = []
        liveMessagePresentation = .empty
        livePresentationRowMetrics = []
        livePresentationContentHeight = 0
        presentationRowMetrics = []
        presentationRowOffsets = []
        presentationContentHeight = 0
        presentationLayoutWidth = 0
        answerRows = []
        currentAnswerJumpDirection = nil
        navigationItem.prompt = nil
        answerJumpButton.isHidden = true
        tableView.reloadData()
        updateHeaderMetadata()
    }

    private func effectivePresentationWidth() -> CGFloat {
        if tableView.bounds.width > 1 { return tableView.bounds.width }
        if view.bounds.width > 1 { return view.bounds.width }
        return UIScreen.main.bounds.width
    }

    private func cachedHistoricalPresentationGeometry(for detail: ConversationDetail, roundProjection: ConversationRoundProjection, messagePresentation: ConversationMessagePresentationProjection, width: CGFloat) -> HistoricalPresentationGeometryCacheEntry? {
        guard let cached = historicalPresentationGeometryCacheByConversationID[detail.id] else { return nil }
        let resolvedWidth = max(1, width)
        let expandedReasoningMessageIDs = expandedReasoningMessageIDsByConversationID[detail.id] ?? []
        guard cached.currentNodeID == detail.currentNodeID,
              cached.authoritativeMessageCount == detail.messages.count,
              cached.rowCount == messagePresentation.rows.count,
              cached.chunkedMessageCount == messagePresentation.chunkedMessageCount,
              cached.maxChunkCharacterCount == messagePresentation.maxChunkCharacterCount,
              cached.roundCount == roundProjection.rounds.count,
              abs(cached.layoutWidth - resolvedWidth) <= 0.5,
              cached.showsMessageTimestamps == preferences.showsMessageTimestamps,
              cached.expandedReasoningMessageIDs == expandedReasoningMessageIDs,
              cached.rowMetrics.count == messagePresentation.rows.count,
              cached.rowOffsets.count == messagePresentation.rows.count else { return nil }
        return cached
    }

    private func storeHistoricalPresentationGeometryIfPossible() {
        guard let conversationID = displayedConversationID, let currentNodeID = displayedCurrentNodeID, presentationRowMetrics.count == messagePresentation.rows.count, presentationRowOffsets.count == messagePresentation.rows.count else { return }
        historicalPresentationGeometryCacheByConversationID[conversationID] = HistoricalPresentationGeometryCacheEntry(currentNodeID: currentNodeID, authoritativeMessageCount: messages.count, rowCount: messagePresentation.rows.count, chunkedMessageCount: messagePresentation.chunkedMessageCount, maxChunkCharacterCount: messagePresentation.maxChunkCharacterCount, roundCount: roundProjection.rounds.count, layoutWidth: presentationLayoutWidth, showsMessageTimestamps: preferences.showsMessageTimestamps, expandedReasoningMessageIDs: expandedReasoningMessageIDsByConversationID[conversationID] ?? [], rowMetrics: presentationRowMetrics, rowOffsets: presentationRowOffsets, contentHeight: presentationContentHeight)
    }

    @discardableResult
    private func rebuildPresentationGeometry(width: CGFloat) -> Double {
        let startedAt = ProcessInfo.processInfo.systemUptime
        let resolvedWidth = max(1, width)
        presentationLayoutWidth = resolvedWidth
        presentationRowMetrics.removeAll(keepingCapacity: true)
        presentationRowOffsets.removeAll(keepingCapacity: true)
        presentationRowMetrics.reserveCapacity(messagePresentation.rows.count)
        presentationRowOffsets.reserveCapacity(messagePresentation.rows.count)
        var offset: CGFloat = 0
        for row in messagePresentation.rows {
            guard messages.indices.contains(row.messageIndex) else { continue }
            let message = messages[row.messageIndex]
            let showsTimestamp = row.isFirstChunk && preferences.showsMessageTimestamps && (message.createTime ?? 0) > 0
            let showsCopy = message.role == .assistant && row.isLastChunk
            let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
            let reasoningExpanded = displayedConversationID.map { isReasoningExpanded(messageID: message.id, conversationID: $0) } ?? false
            let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: showsTimestamp, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !row.text.isEmpty)
            presentationRowOffsets.append(offset)
            presentationRowMetrics.append(metrics)
            offset += metrics.rowHeight
        }
        presentationContentHeight = offset
        storeHistoricalPresentationGeometryIfPossible()
        return (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
    }

    private func buildHistoricalPresentationGeometryCooperatively(detail: ConversationDetail, roundProjection: ConversationRoundProjection, messagePresentation: ConversationMessagePresentationProjection, width: CGFloat, presentationGeneration: Int, geometryBuildGeneration: Int, geometryStartedAt: TimeInterval, startedAt: TimeInterval, completion: (() -> Void)?) {
        let resolvedWidth = max(1, width)
        let showsMessageTimestamps = preferences.showsMessageTimestamps
        let expandedReasoningMessageIDs = expandedReasoningMessageIDsByConversationID[detail.id] ?? []
        var rowMetrics: [ConversationMessageCell.Metrics] = []
        var rowOffsets: [CGFloat] = []
        rowMetrics.reserveCapacity(messagePresentation.rows.count)
        rowOffsets.reserveCapacity(messagePresentation.rows.count)
        var offset: CGFloat = 0

        func processBatch(startingAt startIndex: Int) {
            guard self.repository.selectedConversationID == detail.id,
                  self.presentationGeneration == presentationGeneration,
                  self.historicalGeometryBuildGeneration == geometryBuildGeneration else {
                var fields = self.repository.diagnosticsFields(for: detail.id)
                fields["reason"] = "presentation_superseded"
                fields["completedRowCount"] = String(rowMetrics.count)
                self.diagnostics.info(category: "ui", name: "messagePresentation.geometryBuildDiscarded", fields: fields)
                return
            }
            let endIndex = min(startIndex + 1, messagePresentation.rows.count)
            if startIndex < endIndex {
                for rowIndex in startIndex..<endIndex {
                    let row = messagePresentation.rows[rowIndex]
                    guard detail.messages.indices.contains(row.messageIndex) else { continue }
                    let message = detail.messages[row.messageIndex]
                    let showsTimestamp = row.isFirstChunk && showsMessageTimestamps && (message.createTime ?? 0) > 0
                    let showsCopy = message.role == .assistant && row.isLastChunk
                    let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
                    let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: showsTimestamp, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: expandedReasoningMessageIDs.contains(message.id), toolDisclosureState: .empty, showsReasoningDivider: !responseTimeline.isEmpty && !row.text.isEmpty)
                    rowOffsets.append(offset)
                    rowMetrics.append(metrics)
                    offset += metrics.rowHeight
                }
            }
            if endIndex < messagePresentation.rows.count {
                DispatchQueue.main.async { processBatch(startingAt: endIndex) }
                return
            }
            let geometryDurationMs = (ProcessInfo.processInfo.systemUptime - geometryStartedAt) * 1000
            self.installDetailPresentation(detail, roundProjection: roundProjection, messagePresentation: messagePresentation, width: resolvedWidth, rowMetrics: rowMetrics, rowOffsets: rowOffsets, contentHeight: offset, geometryReused: false, geometryDurationMs: geometryDurationMs, startedAt: startedAt, completion: completion)
        }

        DispatchQueue.main.async { processBatch(startingAt: 0) }
    }

    private func installDetailPresentation(_ detail: ConversationDetail, roundProjection: ConversationRoundProjection, messagePresentation: ConversationMessagePresentationProjection, width: CGFloat, rowMetrics: [ConversationMessageCell.Metrics], rowOffsets: [CGFloat], contentHeight: CGFloat, geometryReused: Bool, geometryDurationMs: Double, startedAt: TimeInterval, completion: (() -> Void)?) {
        guard repository.selectedConversationID == detail.id else { return }
        displayedConversationID = detail.id
        displayedCurrentNodeID = detail.currentNodeID
        title = detail.title
        messages = detail.messages
        self.roundProjection = roundProjection
        self.messagePresentation = messagePresentation
        presentationLayoutWidth = width
        presentationRowMetrics = rowMetrics
        presentationRowOffsets = rowOffsets
        presentationContentHeight = contentHeight
        answerRows = roundProjection.rounds.compactMap { messagePresentation.firstRowByMessageID[$0.userMessageID] }
        if !geometryReused { storeHistoricalPresentationGeometryIfPossible() }
        rebuildLiveResponsePresentation(width: width)
        stateLabel.text = detail.messages.isEmpty ? "当前分支没有可显示的用户或助手文本消息" : nil
        stateLabel.isHidden = !detail.messages.isEmpty
        retryButton.isHidden = true
        loadingConversationID = nil
        activityIndicator.stopAnimating()
        reloadMessageTable(reason: "detail_apply", restoreConversationID: detail.id)
        updateHeaderMetadata()
        updateAnswerJumpButton()
        let totalDurationMs = (ProcessInfo.processInfo.systemUptime - startedAt) * 1000
        diagnostics.info(category: "ui", name: "messagePresentation.rebuilt", fields: ["authoritativeMessageCount": String(messages.count), "presentationRowCount": String(messagePresentation.rows.count), "chunkedMessageCount": String(messagePresentation.chunkedMessageCount), "chunkCharacterLimit": String(ConversationMessagePresentationProjection.chunkCharacterLimit), "maxChunkCharacterCount": String(messagePresentation.maxChunkCharacterCount), "geometryReused": geometryReused ? "true" : "false", "geometryMode": geometryReused ? "resident_cache" : "cooperative_main_queue", "geometryDurationMs": String(format: "%.2f", geometryDurationMs), "durationMs": String(format: "%.2f", totalDurationMs), "layoutWidthPoints": String(format: "%.2f", presentationLayoutWidth), "contentHeightPoints": String(format: "%.2f", presentationContentHeight)])
        completion?()
    }

'''
conv = conv[:start] + new_block + conv[end:]

# Clear only a terminal external snapshot after a successful explicit authoritative refresh.
needle = '''    func clearLiveResponseAfterAuthoritativeReconcile(conversationID: String, generation: Int, authoritativeVisibleMessageCount: Int) -> Bool {
        precondition(Thread.isMainThread)
        guard let snapshot = responseRuntime.snapshots[conversationID], snapshot.generation == generation, !snapshot.phase.isActive, authoritativeVisibleMessageCount > snapshot.baselineVisibleMessageCount else { return false }
        responseRuntime.snapshots.removeValue(forKey: conversationID)
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["authoritativeVisibleMessageCount"] = String(authoritativeVisibleMessageCount)
        fields["baselineVisibleMessageCount"] = String(snapshot.baselineVisibleMessageCount)
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.reconciled", fields: fields)
        responseRuntime.onChange?(conversationID)
        return true
    }
'''
addition = needle + '''
    func clearTerminalExternalLiveResponseAfterAuthoritativeRefresh(conversationID: String) -> Bool {
        precondition(Thread.isMainThread)
        guard let snapshot = responseRuntime.snapshots[conversationID], !snapshot.phase.isActive, snapshot.promptText.isEmpty else { return false }
        responseRuntime.snapshots.removeValue(forKey: conversationID)
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(snapshot.generation)
        fields["reason"] = "authoritative_refresh"
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.externalTerminalCleared", fields: fields)
        responseRuntime.onChange?(conversationID)
        return true
    }
'''
conv = replace_once(conv, needle, addition, 'external terminal authoritative refresh')

conv = replace_once(conv, '''            case .success(let detail):
                let changed = self.hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
                self.apply(detail)
                self.showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0)
''', '''            case .success(let detail):
                let changed = self.hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
                _ = self.repository.clearTerminalExternalLiveResponseAfterAuthoritativeRefresh(conversationID: id)
                self.apply(detail) { [weak self] in self?.showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0) }
''', 'sync clears terminal external')

conv = replace_once(conv, '''        case .success(let detail):
            let changed = hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
            apply(detail)
            if kind == .sync { showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0) }
''', '''        case .success(let detail):
            let changed = hasVisibleMessageChanges(from: previousMessages, to: detail.messages)
            if kind == .sync || kind == .reload { _ = repository.clearTerminalExternalLiveResponseAfterAuthoritativeRefresh(conversationID: id) }
            apply(detail) { [weak self] in
                guard let self else { return }
                if kind == .sync { self.showSyncToast(changed ? "已同步最新消息" : "已是最新", autoHideAfter: 2.0) }
            }
''', 'visible recovery clears terminal external')

# Explicit line-height contract and matching assistant final measurement/rendering.
conv = replace_once(conv, '''    private static let bodyFont = UIFont.preferredFont(forTextStyle: .body)
    private static let reasoningFont = bodyFont
    private static let toolFont = UIFont.systemFont(ofSize: bodyFont.pointSize, weight: .regular)
''', '''    private static let bodyFont = UIFont.preferredFont(forTextStyle: .body)
    private static let reasoningFont = bodyFont
    private static let toolFont = UIFont.systemFont(ofSize: bodyFont.pointSize, weight: .regular)
    private static let toolLineHeight: CGFloat = 26
    private static let compactAssistantLineHeight: CGFloat = toolLineHeight * 0.70
''', 'line-height constants')

conv = replace_once(conv, '''        messageLabel.text = nil
        reasoningTextView.attributedText = nil
''', '''        messageLabel.text = nil
        messageLabel.attributedText = nil
        reasoningTextView.attributedText = nil
''', 'clear attributed body')

conv = replace_once(conv, '''    layoutMetrics = metrics
    messageLabel.text = text
    let showsReasoning = message.role == .assistant && isFirstChunk && !responseTimeline.isEmpty
''', '''    layoutMetrics = metrics
    if message.role == .assistant {
        messageLabel.attributedText = Self.assistantBodyAttributedText(text)
    } else {
        messageLabel.attributedText = nil
        messageLabel.text = text
    }
    let showsReasoning = message.role == .assistant && isFirstChunk && !responseTimeline.isEmpty
''', 'assistant body attributed rendering')

conv = replace_once(conv, '    let textSize = measuredTextSize(text, maxWidth: maxTextWidth)\n', '    let textSize = measuredTextSize(text, role: role, maxWidth: maxTextWidth)\n', 'role-aware body measurement')

conv = replace_once(conv, '''        let reasoningParagraph = NSMutableParagraphStyle()
        reasoningParagraph.minimumLineHeight = 26
        reasoningParagraph.lineSpacing = 2
        reasoningParagraph.paragraphSpacing = 8
        let toolParagraph = NSMutableParagraphStyle()
        toolParagraph.minimumLineHeight = 34
        toolParagraph.lineSpacing = 2
        toolParagraph.paragraphSpacingBefore = 5
        toolParagraph.paragraphSpacing = 12
''', '''        let reasoningParagraph = NSMutableParagraphStyle()
        reasoningParagraph.minimumLineHeight = compactAssistantLineHeight
        reasoningParagraph.maximumLineHeight = compactAssistantLineHeight
        reasoningParagraph.paragraphSpacing = 8
        let toolParagraph = NSMutableParagraphStyle()
        toolParagraph.minimumLineHeight = toolLineHeight
        toolParagraph.maximumLineHeight = toolLineHeight
        toolParagraph.paragraphSpacingBefore = 5
        toolParagraph.paragraphSpacing = 12
''', 'reasoning tool exact line heights')

old_measure = '''    private static func measuredTextSize(_ text: String, maxWidth: CGFloat) -> CGSize {
        guard !text.isEmpty else { return CGSize(width: 0, height: ceil(bodyFont.lineHeight)) }
        let rect = (text as NSString).boundingRect(with: CGSize(width: maxWidth, height: .greatestFiniteMagnitude), options: [.usesLineFragmentOrigin, .usesFontLeading], attributes: [.font: bodyFont], context: nil)
        return CGSize(width: min(maxWidth, ceil(rect.width)), height: max(ceil(bodyFont.lineHeight), ceil(rect.height) + 1))
    }
'''
new_measure = '''    private static func assistantBodyAttributedText(_ text: String) -> NSAttributedString {
        let paragraph = NSMutableParagraphStyle()
        paragraph.minimumLineHeight = compactAssistantLineHeight
        paragraph.maximumLineHeight = compactAssistantLineHeight
        return NSAttributedString(string: text, attributes: [.font: bodyFont, .foregroundColor: UIColor.label, .paragraphStyle: paragraph])
    }

    private static func measuredTextSize(_ text: String, role: ConversationMessage.Role, maxWidth: CGFloat) -> CGSize {
        if text.isEmpty { return CGSize(width: 0, height: ceil(role == .assistant ? compactAssistantLineHeight : bodyFont.lineHeight)) }
        if role == .assistant {
            let rect = assistantBodyAttributedText(text).boundingRect(with: CGSize(width: maxWidth, height: .greatestFiniteMagnitude), options: [.usesLineFragmentOrigin, .usesFontLeading], context: nil)
            return CGSize(width: min(maxWidth, ceil(rect.width)), height: max(ceil(compactAssistantLineHeight), ceil(rect.height) + 1))
        }
        let rect = (text as NSString).boundingRect(with: CGSize(width: maxWidth, height: .greatestFiniteMagnitude), options: [.usesLineFragmentOrigin, .usesFontLeading], attributes: [.font: bodyFont], context: nil)
        return CGSize(width: min(maxWidth, ceil(rect.width)), height: max(ceil(bodyFont.lineHeight), ceil(rect.height) + 1))
    }
'''
conv = replace_once(conv, old_measure, new_measure, 'assistant final measurement')
conv_path.write_text(conv)

# Build identity.
proj_path = Path('ChatGPTClient.xcodeproj/project.pbxproj')
proj = proj_path.read_text()
if proj.count('CURRENT_PROJECT_VERSION = 74;') != 2 or proj.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b74";') != 2:
    raise SystemExit('unexpected b74 project identity count')
proj = proj.replace('CURRENT_PROJECT_VERSION = 74;', 'CURRENT_PROJECT_VERSION = 75;')
proj = proj.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b74";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b75";')
proj_path.write_text(proj)

wf_path = Path('.github/workflows/ios-foundation.yml')
wf = wf_path.read_text()
wf = replace_once(wf, '# Candidate: DEV-send-stream-0.1.0-b74', '# Candidate: DEV-send-stream-0.1.0-b75', 'workflow candidate')
wf = replace_once(wf, 'name: ChatGPTClient-DEV-send-stream-0.1.0-b74', 'name: ChatGPTClient-DEV-send-stream-0.1.0-b75', 'workflow artifact')
wf_path.write_text(wf)
