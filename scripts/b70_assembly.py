from pathlib import Path
import re

ROOT = Path.cwd()


def read(path):
    return (ROOT / path).read_text()


def write(path, text):
    (ROOT / path).write_text(text)


def replace_once(path, old, new):
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one exact anchor, found {count}: {old[:100]!r}")
    write(path, text.replace(old, new, 1))


def replace_between(path, start, end, new):
    text = read(path)
    if text.count(start) != 1:
        raise SystemExit(f"{path}: start anchor count != 1: {start!r}")
    i = text.index(start)
    j = text.index(end, i)
    write(path, text[:i] + new + text[j:])


# -----------------------------------------------------------------------------
# RootViewController.swift — covered executor keyboard suppression, b65-authorized
# GitHub detail payload, bounded icon kind, optimistic prompt ownership.
# -----------------------------------------------------------------------------
root = "ChatGPTClient/RootViewController.swift"

replace_once(root,
r'''    case finalDelta(String)
    case toolActivity(slot: Int, title: String, completed: Bool)
    case terminal
''',
r'''    case finalDelta(String)
    case toolActivity(slot: Int, title: String, completed: Bool, inputJSON: String, outputJSON: String, iconKind: ConversationToolIconKind)
    case terminal
''')

replace_once(root,
r'''        case "tool_activity":
            let slot = (body["slot"] as? NSNumber)?.intValue ?? -1
            guard slot >= 0 else { return }
            let title = (body["title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
            activeEvents?(.toolActivity(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: (body["completed"] as? NSNumber)?.boolValue ?? false))
''',
r'''        case "tool_activity":
            let slot = (body["slot"] as? NSNumber)?.intValue ?? -1
            guard slot >= 0 else { return }
            let title = (body["title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
            let inputJSON = body["detailInput"] as? String ?? ""
            let outputJSON = body["detailOutput"] as? String ?? ""
            let iconKind = ConversationToolIconKind(rawValue: body["iconKind"] as? String ?? "") ?? .generic
            activeEvents?(.toolActivity(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: (body["completed"] as? NSNumber)?.boolValue ?? false, inputJSON: inputJSON, outputJSON: outputJSON, iconKind: iconKind))
''')

replace_between(root,
"      const setComposerText = (element, text) => {\n",
"      const submit = text => {\n",
r'''      const setComposerText = (element, text) => {
        const previousInputMode = element.getAttribute('inputmode');
        element.setAttribute('inputmode', 'none');
        let succeeded = false;
        try {
          try { element.focus({ preventScroll: true }); } catch (_) { element.focus(); }
          if (element instanceof HTMLTextAreaElement || element instanceof HTMLInputElement) {
            const prototype = element instanceof HTMLTextAreaElement ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
            const descriptor = Object.getOwnPropertyDescriptor(prototype, 'value');
            if (!descriptor || !descriptor.set) return false;
            descriptor.set.call(element, text);
            element.dispatchEvent(new InputEvent('input', { bubbles: true, inputType: 'insertText', data: text }));
            succeeded = true;
            return true;
          }
          if (!element.isContentEditable) return false;
          const selection = window.getSelection();
          const range = document.createRange();
          range.selectNodeContents(element);
          selection.removeAllRanges();
          selection.addRange(range);
          let inserted = false;
          try { inserted = document.execCommand('insertText', false, text); } catch (_) {}
          if (!inserted) {
            element.textContent = text;
            element.dispatchEvent(new InputEvent('input', { bubbles: true, inputType: 'insertText', data: text }));
          }
          selection.removeAllRanges();
          succeeded = true;
          return true;
        } finally {
          try { element.blur(); } catch (_) {}
          if (previousInputMode === null) element.removeAttribute('inputmode');
          else element.setAttribute('inputmode', previousInputMode);
          if (!succeeded) {
            const selection = window.getSelection();
            if (selection) selection.removeAllRanges();
          }
        }
      };
''')

replace_between(root,
"      const observeToolActivity = (payload, state) => {\n",
"      const scrubTextPatches = (node, state) => {\n",
r'''      const observeToolActivity = (payload, state) => {
        const message = findMessage(payload);
        if (!message || !message.author || typeof message.id !== 'string' || !message.id) return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        const role = message.author.role;
        const contentType = content && content.content_type;
        const rawTitle = metadata && typeof metadata.reasoning_title === 'string' ? metadata.reasoning_title.trim() : '';
        const title = rawTitle.slice(0, 160);
        if (role === 'assistant' && contentType === 'code' && typeof message.recipient === 'string' && message.recipient && message.recipient !== 'all') {
          if (!state.invocations.has(message.id)) state.invocations.set(message.id, { recipient: message.recipient, slot: state.nextToolSlot++, connectorPayload: '', iconKind: message.recipient === 'api_tool.call_tool' ? 'generic' : 'code' });
          const identity = state.invocations.get(message.id);
          if (metadata && typeof metadata.connector_tool_payload === 'string' && metadata.connector_tool_payload) identity.connectorPayload = metadata.connector_tool_payload;
          if (message.status !== 'finished_successfully' || !metadata || metadata.is_complete !== true || state.toolSeen.has(message.id)) return;
          state.toolSeen.add(message.id);
          post({ kind: 'tool_activity', slot: identity.slot, title, completed: false, detailInput: '', detailOutput: '', iconKind: identity.iconKind });
          return;
        }
        if (role !== 'tool' || message.recipient !== 'all' || message.status !== 'finished_successfully' || state.toolSeen.has(message.id)) return;
        state.toolSeen.add(message.id);
        const parentID = metadata && typeof metadata.parent_id === 'string' && metadata.parent_id ? metadata.parent_id : '';
        const identity = parentID ? state.invocations.get(parentID) : null;
        if (!identity) return;
        const invokedResource = metadata && metadata.invoked_resource && typeof metadata.invoked_resource === 'object' && !Array.isArray(metadata.invoked_resource) ? metadata.invoked_resource : null;
        const githubDetail = identity.recipient === 'api_tool.call_tool' && invokedResource && invokedResource.app_name === 'GitHub' && typeof identity.connectorPayload === 'string' && !!identity.connectorPayload && !!content;
        let detailOutput = '';
        if (githubDetail) {
          try { detailOutput = JSON.stringify(content); } catch (_) {}
        }
        post({ kind: 'tool_activity', slot: identity.slot, title, completed: true, detailInput: githubDetail ? identity.connectorPayload : '', detailOutput, iconKind: githubDetail ? 'github' : identity.iconKind });
      };
''')

replace_once(root,
r'''        self.pendingSend = nil
        let script = "window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.submit(\(literal));"
        webView.evaluateJavaScript(script) { [weak self] _, error in
            guard let self, let error else { return }
            let nsError = error as NSError
''',
r'''        self.pendingSend = nil
        let script = "window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.submit(\(literal));"
        webView.evaluateJavaScript(script) { [weak self] _, error in
            guard let self else { return }
            self.webView.endEditing(true)
            guard let error else { return }
            let nsError = error as NSError
''')

replace_once(root,
r'''    let baselineVisibleMessageCount: Int
    var phase: ConversationLiveResponsePhase
''',
r'''    let baselineVisibleMessageCount: Int
    let promptText: String
    var phase: ConversationLiveResponsePhase
''')

replace_once(root,
r'''    func beginLiveResponse(conversationID: String, promptCharacterCount: Int) -> Result<Int, Error> {
        precondition(Thread.isMainThread)
        if responseRuntime.snapshots[conversationID]?.phase.isActive == true { return .failure(ConversationLiveResponseError.responseAlreadyActive) }
        let generation = (responseRuntime.generations[conversationID] ?? 0) + 1
        responseRuntime.generations[conversationID] = generation
        let baselineVisibleMessageCount = selectedConversationID == conversationID ? (selectedConversation?.messages.count ?? 0) : 0
        responseRuntime.snapshots[conversationID] = ConversationLiveResponseSnapshot(generation: generation, conversationID: conversationID, baselineVisibleMessageCount: baselineVisibleMessageCount, phase: .preparing, timeline: [], finalText: "", reasoningEnded: false, failureReason: nil)
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["phase"] = ConversationLiveResponsePhase.preparing.rawValue
        fields["promptCharacters"] = String(promptCharacterCount)
''',
r'''    func beginLiveResponse(conversationID: String, promptText: String) -> Result<Int, Error> {
        precondition(Thread.isMainThread)
        if responseRuntime.snapshots[conversationID]?.phase.isActive == true { return .failure(ConversationLiveResponseError.responseAlreadyActive) }
        let generation = (responseRuntime.generations[conversationID] ?? 0) + 1
        responseRuntime.generations[conversationID] = generation
        let baselineVisibleMessageCount = selectedConversationID == conversationID ? (selectedConversation?.messages.count ?? 0) : 0
        responseRuntime.snapshots[conversationID] = ConversationLiveResponseSnapshot(generation: generation, conversationID: conversationID, baselineVisibleMessageCount: baselineVisibleMessageCount, promptText: promptText, phase: .preparing, timeline: [], finalText: "", reasoningEnded: false, failureReason: nil)
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["phase"] = ConversationLiveResponsePhase.preparing.rawValue
        fields["promptCharacters"] = String(promptText.count)
''')

replace_once(root,
r'''    case .toolActivity(let slot, let title, let completed):
        if let index = snapshot.timeline.firstIndex(where: { $0.kind == .tool && $0.toolSlot == slot }) {
            if !title.isEmpty { snapshot.timeline[index].text = title }
            snapshot.timeline[index].completed = snapshot.timeline[index].completed || completed
        } else {
            snapshot.timeline.append(.tool(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: completed))
        }
        eventName = completed ? "tool_completed" : "tool_invoked"
''',
r'''    case .toolActivity(let slot, let title, let completed, let inputJSON, let outputJSON, let iconKind):
        if let index = snapshot.timeline.firstIndex(where: { $0.kind == .tool && $0.toolSlot == slot }) {
            if !title.isEmpty { snapshot.timeline[index].text = title }
            snapshot.timeline[index].completed = snapshot.timeline[index].completed || completed
            if !inputJSON.isEmpty { snapshot.timeline[index].toolInputJSON = inputJSON }
            if !outputJSON.isEmpty { snapshot.timeline[index].toolOutputJSON = outputJSON }
            if iconKind != .generic || snapshot.timeline[index].toolIconKind == .generic { snapshot.timeline[index].toolIconKind = iconKind }
        } else {
            snapshot.timeline.append(.tool(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: completed, inputJSON: inputJSON, outputJSON: outputJSON, iconKind: iconKind))
        }
        eventName = completed ? "tool_completed" : "tool_invoked"
''')

replace_once(root,
r'''        switch repository.beginLiveResponse(conversationID: conversationID, promptCharacterCount: trimmed.count) {
''',
r'''        switch repository.beginLiveResponse(conversationID: conversationID, promptText: trimmed) {
''')

conv = "ChatGPTClient/Conversation/ConversationFeature.swift"

replace_between(conv,
"struct ConversationResponseTimelineItem: Equatable {\n",
"struct ConversationMessage {\n",
r'''enum ConversationToolIconKind: String, Equatable {
    case generic
    case code
    case github
}

enum ConversationToolDetailSection {
    case input
    case output
}

struct ConversationToolDisclosureState {
    static let empty = ConversationToolDisclosureState(expandedInputSlots: [], expandedOutputSlots: [])
    let expandedInputSlots: Set<Int>
    let expandedOutputSlots: Set<Int>
    var hasExpandedDetail: Bool { !expandedInputSlots.isEmpty || !expandedOutputSlots.isEmpty }
}

struct ConversationResponseTimelineItem: Equatable {
    enum Kind: String {
        case reasoning
        case tool
    }

    let kind: Kind
    var text: String
    let toolSlot: Int?
    var completed: Bool
    var toolInputJSON: String
    var toolOutputJSON: String
    var toolIconKind: ConversationToolIconKind

    static func reasoning(_ text: String) -> ConversationResponseTimelineItem { ConversationResponseTimelineItem(kind: .reasoning, text: text, toolSlot: nil, completed: false, toolInputJSON: "", toolOutputJSON: "", toolIconKind: .generic) }
    static func tool(slot: Int, title: String, completed: Bool, inputJSON: String = "", outputJSON: String = "", iconKind: ConversationToolIconKind = .generic) -> ConversationResponseTimelineItem { ConversationResponseTimelineItem(kind: .tool, text: title, toolSlot: slot, completed: completed, toolInputJSON: inputJSON, toolOutputJSON: outputJSON, toolIconKind: iconKind) }
}

''')

replace_once(conv,
r'''    private func finishTransientSessionProbe(_ result: Result<ConversationTransportContext, Error>) {
        requireMainThread()
        let completions = transientSessionProbeCompletions ?? []
        transientSessionProbeCompletions = nil
        for completion in completions { completion(result) }
    }

''',
r'''    private func finishTransientSessionProbe(_ result: Result<ConversationTransportContext, Error>) {
        requireMainThread()
        let completions = transientSessionProbeCompletions ?? []
        transientSessionProbeCompletions = nil
        for completion in completions { completion(result) }
    }

    private func invalidateTransientSessionIfCurrent(_ context: ConversationTransportContext, httpStatus: Int, route: String) {
        requireMainThread()
        guard Self.isUnauthorizedStatus(httpStatus), let transientSession, transientSession === context.session, transientSessionScope == context.scope else { return }
        transientSession.invalidateAndCancel()
        self.transientSession = nil
        transientSessionScope = nil
        diagnostics.info(category: "conversation", name: "authTransport.invalidated", fields: ["route": route, "httpStatus": String(httpStatus), "reason": "unauthorized_current_transient"])
    }

    private static func isUnauthorizedStatus(_ status: Int) -> Bool { status == 401 || status == 403 }

    private static func isUnauthorizedError(_ error: Error) -> Bool {
        guard let repositoryError = error as? ConversationRepositoryError, case .httpStatus(let status) = repositoryError else { return false }
        return isUnauthorizedStatus(status)
    }

''')

replace_once(conv,
r'''            guard self.listOperationGeneration == operationGeneration else {
                var fields = statusFields
                fields["reason"] = "operation_superseded"
                span.end(status: "discarded", fields: fields)
                completion(.failure(ConversationRepositoryError.operationSuperseded))
                return
            }
            switch result {
''',
r'''            guard self.listOperationGeneration == operationGeneration else {
                var fields = statusFields
                fields["reason"] = "operation_superseded"
                span.end(status: "discarded", fields: fields)
                completion(.failure(ConversationRepositoryError.operationSuperseded))
                return
            }
            if let statusString = statusFields["httpStatus"], let status = Int(statusString), Self.isUnauthorizedStatus(status) { self.invalidateTransientSessionIfCurrent(context, httpStatus: status, route: "conversation_list") }
            switch result {
''')

replace_once(conv,
r'''            guard (200..<300).contains(response.statusCode) else {
                span.end(status: "failed", fields: ["stage": "response", "httpStatus": String(response.statusCode)])
                self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .failure(ConversationRepositoryError.httpStatus(response.statusCode)))
                return
            }
''',
r'''            guard (200..<300).contains(response.statusCode) else {
                if Self.isUnauthorizedStatus(response.statusCode) {
                    DispatchQueue.main.async { self.invalidateTransientSessionIfCurrent(context, httpStatus: response.statusCode, route: "conversation_detail") }
                }
                span.end(status: "failed", fields: ["stage": "response", "httpStatus": String(response.statusCode)])
                self.finishDetailOperation(key: key, operationGeneration: operationGeneration, result: .failure(ConversationRepositoryError.httpStatus(response.statusCode)))
                return
            }
''')

replace_once(conv,
r'''            case .failure(let error):
                let hasLoadedResident: Bool
                if let existingState = self.residentStates[key], case .loaded = existingState { hasLoadedResident = true } else { hasLoadedResident = false }
                if !operation.preserveLoadedResidentOnFailure || !hasLoadedResident { self.residentStates[key] = .failed(error) }
                var fields = self.residentDiagnosticsFields(for: key.conversationID)
                fields["state"] = operation.preserveLoadedResidentOnFailure && hasLoadedResident ? "loaded_preserved" : "failed"
                fields["operationKind"] = operation.kind.rawValue
                self.diagnostics.info(category: "conversation", name: "resident.terminal", fields: fields)
''',
r'''            case .failure(let error):
                let hasLoadedResident: Bool
                if let existingState = self.residentStates[key], case .loaded = existingState { hasLoadedResident = true } else { hasLoadedResident = false }
                let authorizationFailure = Self.isUnauthorizedError(error)
                if authorizationFailure, !hasLoadedResident { self.residentStates.removeValue(forKey: key) }
                else if !operation.preserveLoadedResidentOnFailure || !hasLoadedResident { self.residentStates[key] = .failed(error) }
                var fields = self.residentDiagnosticsFields(for: key.conversationID)
                if authorizationFailure, !hasLoadedResident { fields["state"] = "authorization_failed_not_resident" }
                else { fields["state"] = operation.preserveLoadedResidentOnFailure && hasLoadedResident ? "loaded_preserved" : "failed" }
                fields["operationKind"] = operation.kind.rawValue
                self.diagnostics.info(category: "conversation", name: "resident.terminal", fields: fields)
''')

replace_between(conv,
"    private static func parseCurrentBranch(mapping: [String: Any], currentNode: String) -> (messages: [ConversationMessage], filteredRecipientMessageCount: Int) {\n",
"    private static func collapsedReasoningSummary(from message: [String: Any], content: [String: Any]) -> String? {\n",
r'''    private static func parseCurrentBranch(mapping: [String: Any], currentNode: String) -> (messages: [ConversationMessage], filteredRecipientMessageCount: Int) {
    var nodeIDs: [String] = []
    var visited = Set<String>()
    var nodeID: String? = currentNode
    while let currentID = nodeID, !currentID.isEmpty, visited.insert(currentID).inserted {
        nodeIDs.append(currentID)
        guard let node = mapping[currentID] as? [String: Any] else { break }
        nodeID = node["parent"] as? String
    }

    var messages: [ConversationMessage] = []
    var filteredRecipientMessageCount = 0
    var pendingTimeline: [ConversationResponseTimelineItem] = []
    var pendingToolIndexByServiceID: [String: Int] = [:]
    var pendingToolRecipientByServiceID: [String: String] = [:]
    var pendingToolInputByServiceID: [String: String] = [:]
    for id in nodeIDs.reversed() {
        guard let node = mapping[id] as? [String: Any], let message = node["message"] as? [String: Any], let author = message["author"] as? [String: Any], let rawRole = author["role"] as? String else { continue }
        let metadata = message["metadata"] as? [String: Any]
        if rawRole == "tool" {
            if message["status"] as? String == "finished_successfully", message["recipient"] as? String == "all", let parentID = metadata?["parent_id"] as? String, let index = pendingToolIndexByServiceID[parentID], pendingTimeline.indices.contains(index), pendingTimeline[index].kind == .tool {
                pendingTimeline[index].completed = true
                if pendingToolRecipientByServiceID[parentID] == "api_tool.call_tool", let inputJSON = pendingToolInputByServiceID[parentID], !inputJSON.isEmpty, let invokedResource = metadata?["invoked_resource"] as? [String: Any], invokedResource["app_name"] as? String == "GitHub", let resultContent = message["content"] as? [String: Any], JSONSerialization.isValidJSONObject(resultContent), let data = try? JSONSerialization.data(withJSONObject: resultContent), let outputJSON = String(data: data, encoding: .utf8) {
                    pendingTimeline[index].toolInputJSON = inputJSON
                    pendingTimeline[index].toolOutputJSON = outputJSON
                    pendingTimeline[index].toolIconKind = .github
                }
            }
            continue
        }
        guard let role = ConversationMessage.Role(rawValue: rawRole), let content = message["content"] as? [String: Any] else { continue }
        if role == .assistant, let recipient = message["recipient"] as? String {
            let normalizedRecipient = recipient.trimmingCharacters(in: .whitespacesAndNewlines)
            if !normalizedRecipient.isEmpty, normalizedRecipient != "all" {
                filteredRecipientMessageCount += 1
                if message["status"] as? String == "finished_successfully", content["content_type"] as? String == "code", (metadata?["is_complete"] as? Bool) == true {
                    let rawTitle = (metadata?["reasoning_title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
                    let title = rawTitle.isEmpty ? "工具调用" : String(rawTitle.prefix(160))
                    let serviceID = (message["id"] as? String).flatMap { $0.isEmpty ? nil : $0 } ?? id
                    pendingToolIndexByServiceID[serviceID] = pendingTimeline.count
                    pendingToolRecipientByServiceID[serviceID] = normalizedRecipient
                    if normalizedRecipient == "api_tool.call_tool", let connectorPayload = metadata?["connector_tool_payload"] as? String, !connectorPayload.isEmpty { pendingToolInputByServiceID[serviceID] = connectorPayload }
                    let iconKind: ConversationToolIconKind = normalizedRecipient == "api_tool.call_tool" ? .generic : .code
                    pendingTimeline.append(.tool(slot: pendingTimeline.count, title: title, completed: false, iconKind: iconKind))
                }
                continue
            }
        }
        if role == .assistant, let summary = collapsedReasoningSummary(from: message, content: content) {
            if !pendingTimeline.contains(where: { $0.kind == .reasoning }) { pendingTimeline.append(.reasoning(summary)) }
            continue
        }
        let isThinkingPreamble = role == .assistant && (metadata?["is_thinking_preamble_message"] as? Bool) == true
        if isThinkingPreamble {
            let reasoning = visibleText(from: content)
            if !reasoning.isEmpty { pendingTimeline.append(.reasoning(reasoning)) }
            continue
        }
        if role == .assistant, let contentType = content["content_type"] as? String, contentType == "thoughts" || contentType == "inline_cot_expandable_content" { continue }
        let visible = visibleText(from: content)
        guard !visible.isEmpty else { continue }
        if role == .user {
            pendingTimeline.removeAll()
            pendingToolIndexByServiceID.removeAll()
            pendingToolRecipientByServiceID.removeAll()
            pendingToolInputByServiceID.removeAll()
        }
        let timeline = role == .assistant ? pendingTimeline : []
        let messageID = (message["id"] as? String).flatMap { $0.isEmpty ? nil : $0 } ?? id
        messages.append(ConversationMessage(id: messageID, role: role, text: visible, responseTimeline: timeline, createTime: (message["create_time"] as? NSNumber)?.doubleValue))
        if role == .assistant {
            pendingTimeline.removeAll()
            pendingToolIndexByServiceID.removeAll()
            pendingToolRecipientByServiceID.removeAll()
            pendingToolInputByServiceID.removeAll()
        }
    }
    return (messages, filteredRecipientMessageCount)
}

''')

replace_once(conv,
r'''    private var loading = false
    private var loadPresentationGeneration = 0
    private var errorView: UIView?
''',
r'''    private var loading = false
    private var loadPresentationGeneration = 0
    private var errorView: UIView?
    private var refreshAfterLoginReturn = false
''')

replace_once(conv,
r'''        loadConversations(forceRefresh: false)
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int { repository.conversations.count }
''',
r'''        loadConversations(forceRefresh: false)
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        guard refreshAfterLoginReturn else { return }
        refreshAfterLoginReturn = false
        diagnostics.info(category: "navigation", name: "nativeRead.login.returnRefresh")
        loadConversations(forceRefresh: true)
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int { repository.conversations.count }
''')

replace_once(conv,
r'''    @objc private func openLogin() {
        diagnostics.info(category: "navigation", name: "nativeRead.login.open")
        navigationController?.pushViewController(AuthWebViewController(mode: .authentication), animated: true)
    }
''',
r'''    @objc private func openLogin() {
        diagnostics.info(category: "navigation", name: "nativeRead.login.open")
        refreshAfterLoginReturn = true
        navigationController?.pushViewController(AuthWebViewController(mode: .authentication), animated: true)
    }
''')

replace_once(conv,
r'''    private var messagePresentation = ConversationMessagePresentationProjection.empty
    private var livePresentationMessage: ConversationMessage?
    private var liveMessagePresentation = ConversationMessagePresentationProjection.empty
''',
r'''    private var messagePresentation = ConversationMessagePresentationProjection.empty
    private var livePresentationMessages: [ConversationMessage] = []
    private var liveMessagePresentation = ConversationMessagePresentationProjection.empty
''')

replace_once(conv,
r'''    private var expandedReasoningMessageIDsByConversationID: [String: Set<String>] = [:]
    private var presentationRowMetrics: [ConversationMessageCell.Metrics] = []
''',
r'''    private var expandedReasoningMessageIDsByConversationID: [String: Set<String>] = [:]
    private var expandedToolInputSlotsByMessageKey: [String: Set<Int>] = [:]
    private var expandedToolOutputSlotsByMessageKey: [String: Set<Int>] = [:]
    private var presentationRowMetrics: [ConversationMessageCell.Metrics] = []
''')

replace_once(conv,
r'''        expandedReasoningMessageIDsByConversationID.removeAll()
        activityIndicator.stopAnimating()
''',
r'''        expandedReasoningMessageIDsByConversationID.removeAll()
        expandedToolInputSlotsByMessageKey.removeAll()
        expandedToolOutputSlotsByMessageKey.removeAll()
        activityIndicator.stopAnimating()
''')

replace_once(conv,
r'''        messagePresentation = .empty
        livePresentationMessage = nil
        liveMessagePresentation = .empty
''',
r'''        messagePresentation = .empty
        livePresentationMessages = []
        liveMessagePresentation = .empty
''')

replace_once(conv,
r'''            let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
            let reasoningExpanded = !responseTimeline.isEmpty && isReasoningExpanded(messageID: message.id)
            let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: showsTimestamp, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded)
''',
r'''            let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
            let reasoningExpanded = !responseTimeline.isEmpty && isReasoningExpanded(messageID: message.id)
            let toolDisclosureState = self.toolDisclosureState(messageID: message.id)
            let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: showsTimestamp, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: toolDisclosureState, showsReasoningDivider: reasoningExpanded && !responseTimeline.isEmpty)
''')

replace_between(conv,
"    private func rebuildLiveResponsePresentation(width: CGFloat) {\n",
"    func liveResponseDidChange(id: String) {\n",
r'''    private func rebuildLiveResponsePresentation(width: CGFloat) {
    let resolvedWidth = max(1, width)
    guard let id = displayedConversationID, let snapshot = repository.liveResponse(for: id) else {
        livePresentationMessages = []
        liveMessagePresentation = .empty
        livePresentationRowMetrics = []
        livePresentationContentHeight = 0
        return
    }
    let bodyText: String
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
    let userMessage = ConversationMessage(id: "local-live-user-\(snapshot.generation)", role: .user, text: snapshot.promptText, responseTimeline: [], createTime: nil)
    let assistantMessage = ConversationMessage(id: "local-live-response-\(snapshot.generation)", role: .assistant, text: bodyText, responseTimeline: snapshot.timeline, createTime: nil)
    livePresentationMessages = [userMessage, assistantMessage]
    liveMessagePresentation = ConversationMessagePresentationProjection.derive(from: livePresentationMessages)
    livePresentationRowMetrics.removeAll(keepingCapacity: true)
    livePresentationRowMetrics.reserveCapacity(liveMessagePresentation.rows.count)
    var height: CGFloat = 0
    for row in liveMessagePresentation.rows {
        guard livePresentationMessages.indices.contains(row.messageIndex) else { continue }
        let message = livePresentationMessages[row.messageIndex]
        let responseTimeline = row.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
        let reasoningExpanded = !responseTimeline.isEmpty && (!snapshot.reasoningEnded || isReasoningExpanded(messageID: message.id))
        let showsCopy = message.role == .assistant && !snapshot.phase.isActive && row.isLastChunk
        let toolDisclosureState = self.toolDisclosureState(messageID: message.id)
        let metrics = ConversationMessageCell.metrics(for: row.text, role: message.role, tableWidth: resolvedWidth, showsTimestamp: false, showsCopy: showsCopy, isFirstChunk: row.isFirstChunk, isLastChunk: row.isLastChunk, isChunked: row.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: toolDisclosureState, showsReasoningDivider: reasoningExpanded && !responseTimeline.isEmpty && !snapshot.finalText.isEmpty)
        livePresentationRowMetrics.append(metrics)
        height += metrics.rowHeight
    }
    livePresentationContentHeight = height
}

''')

replace_between(conv,
"    private func isReasoningExpanded(messageID: String) -> Bool {\n",
"    private func reloadMessageTable(reason: String, restoreConversationID: String?) {\n",
r'''    private func isReasoningExpanded(messageID: String) -> Bool {
    guard let id = displayedConversationID else { return false }
    return expandedReasoningMessageIDsByConversationID[id]?.contains(messageID) ?? false
}

    private func toggleReasoning(messageID: String) {
    guard let id = displayedConversationID else { return }
    if expandedReasoningMessageIDsByConversationID[id]?.contains(messageID) == true { expandedReasoningMessageIDsByConversationID[id]?.remove(messageID) }
    else { expandedReasoningMessageIDsByConversationID[id, default: []].insert(messageID) }
    if livePresentationMessages.contains(where: { $0.id == messageID }) {
        liveResponseDidChange(id: id)
        return
    }
    captureScrollAnchor(for: id)
    let durationMs = rebuildPresentationGeometry(width: effectivePresentationWidth())
    reloadMessageTable(reason: "reasoning_toggle", restoreConversationID: id)
    diagnostics.info(category: "interaction", name: "reasoningSummary.toggled", fields: ["expanded": isReasoningExpanded(messageID: messageID) ? "true" : "false", "geometryDurationMs": String(format: "%.2f", durationMs)])
}

    private func toolDisclosureKey(conversationID: String, messageID: String) -> String { conversationID + "\u{0}" + messageID }

    private func toolDisclosureState(messageID: String) -> ConversationToolDisclosureState {
        guard let conversationID = displayedConversationID else { return .empty }
        let key = toolDisclosureKey(conversationID: conversationID, messageID: messageID)
        return ConversationToolDisclosureState(expandedInputSlots: expandedToolInputSlotsByMessageKey[key] ?? [], expandedOutputSlots: expandedToolOutputSlotsByMessageKey[key] ?? [])
    }

    private func toggleToolDetail(messageID: String, slot: Int, section: ConversationToolDetailSection) {
        guard let conversationID = displayedConversationID else { return }
        let key = toolDisclosureKey(conversationID: conversationID, messageID: messageID)
        switch section {
        case .input:
            if expandedToolInputSlotsByMessageKey[key]?.contains(slot) == true { expandedToolInputSlotsByMessageKey[key]?.remove(slot) }
            else { expandedToolInputSlotsByMessageKey[key, default: []].insert(slot) }
        case .output:
            if expandedToolOutputSlotsByMessageKey[key]?.contains(slot) == true { expandedToolOutputSlotsByMessageKey[key]?.remove(slot) }
            else { expandedToolOutputSlotsByMessageKey[key, default: []].insert(slot) }
        }
        if livePresentationMessages.contains(where: { $0.id == messageID }) {
            liveResponseDidChange(id: conversationID)
            return
        }
        captureScrollAnchor(for: conversationID)
        let durationMs = rebuildPresentationGeometry(width: effectivePresentationWidth())
        reloadMessageTable(reason: "tool_detail_toggle", restoreConversationID: conversationID)
        diagnostics.info(category: "interaction", name: "toolDetail.toggled", fields: ["slot": String(slot), "section": section == .input ? "input" : "output", "geometryDurationMs": String(format: "%.2f", durationMs)])
    }

''')

replace_between(conv,
"    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {\n",
"    func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration? {\n",
r'''    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: ConversationMessageCell.reuseIdentifier, for: indexPath) as! ConversationMessageCell
    if indexPath.row < messagePresentation.rows.count {
        guard messagePresentation.rows.indices.contains(indexPath.row), presentationRowMetrics.indices.contains(indexPath.row) else { return cell }
        let presentationRow = messagePresentation.rows[indexPath.row]
        guard messages.indices.contains(presentationRow.messageIndex) else { return cell }
        let message = messages[presentationRow.messageIndex]
        let showsTimestamp = presentationRow.isFirstChunk && preferences.showsMessageTimestamps
        let showsCopy = message.role == .assistant && presentationRow.isLastChunk
        let responseTimeline = presentationRow.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
        let reasoningExpanded = !responseTimeline.isEmpty && isReasoningExpanded(messageID: message.id)
        let disclosureState = toolDisclosureState(messageID: message.id)
        cell.configure(with: message, text: presentationRow.text, showTimestamp: showsTimestamp, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: disclosureState, showsReasoningDivider: reasoningExpanded && !responseTimeline.isEmpty, metrics: presentationRowMetrics[indexPath.row], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: responseTimeline.isEmpty ? nil : { [weak self] in self?.toggleReasoning(messageID: message.id) }, onToggleToolDetail: responseTimeline.isEmpty ? nil : { [weak self] slot, section in self?.toggleToolDetail(messageID: message.id, slot: slot, section: section) })
        return cell
    }
    let liveRow = indexPath.row - messagePresentation.rows.count
    guard liveMessagePresentation.rows.indices.contains(liveRow), livePresentationRowMetrics.indices.contains(liveRow), let id = displayedConversationID, let snapshot = repository.liveResponse(for: id) else { return cell }
    let presentationRow = liveMessagePresentation.rows[liveRow]
    guard livePresentationMessages.indices.contains(presentationRow.messageIndex) else { return cell }
    let message = livePresentationMessages[presentationRow.messageIndex]
    let showsCopy = message.role == .assistant && !snapshot.phase.isActive && presentationRow.isLastChunk
    let responseTimeline = presentationRow.isFirstChunk && message.role == .assistant ? message.responseTimeline : []
    let reasoningExpanded = !responseTimeline.isEmpty && (!snapshot.reasoningEnded || isReasoningExpanded(messageID: message.id))
    let canToggleReasoning = !responseTimeline.isEmpty && snapshot.reasoningEnded
    let disclosureState = toolDisclosureState(messageID: message.id)
    cell.configure(with: message, text: presentationRow.text, showTimestamp: false, showCopy: showsCopy, isFirstChunk: presentationRow.isFirstChunk, isLastChunk: presentationRow.isLastChunk, isChunked: presentationRow.chunkCount > 1, responseTimeline: responseTimeline, reasoningExpanded: reasoningExpanded, toolDisclosureState: disclosureState, showsReasoningDivider: reasoningExpanded && !responseTimeline.isEmpty && !snapshot.finalText.isEmpty, metrics: livePresentationRowMetrics[liveRow], onCopy: showsCopy ? { [weak self] in self?.copyVisibleMessage(message) } : nil, onToggleReasoning: canToggleReasoning ? { [weak self] in self?.toggleReasoning(messageID: message.id) } : nil, onToggleToolDetail: responseTimeline.isEmpty ? nil : { [weak self] slot, section in self?.toggleToolDetail(messageID: message.id, slot: slot, section: section) })
    return cell
}

''')

text = read(conv)
cell_start = "final class ConversationMessageCell: UITableViewCell {\n"
if text.count(cell_start) != 1:
    raise SystemExit("ConversationMessageCell marker mismatch")
idx = text.index(cell_start)
new_cell = r'''final class ConversationMessageCell: UITableViewCell, UITextViewDelegate {
    struct Metrics {
        let rowHeight: CGFloat
        let timestampFrame: CGRect
        let bubbleFrame: CGRect
        let reasoningButtonFrame: CGRect
        let reasoningBodyFrame: CGRect
        let reasoningDividerFrame: CGRect
        let messageFrame: CGRect
        let copyFrame: CGRect
    }

    static let reuseIdentifier = "ConversationMessageCell"

    private static let horizontalMargin: CGFloat = 16
    private static let userLeadingGap: CGFloat = 44
    private static let userMaxWidthRatio: CGFloat = 0.82
    private static let bubbleHorizontalPadding: CGFloat = 12
    private static let bubbleVerticalPadding: CGFloat = 9
    private static let outerVerticalPadding: CGFloat = 7
    private static let timestampGap: CGFloat = 3
    private static let reasoningButtonHeight: CGFloat = 28
    private static let reasoningBodyGap: CGFloat = 2
    private static let reasoningMessageGap: CGFloat = 5
    private static let reasoningDividerGap: CGFloat = 7
    private static let toolDetailMaximumBodyHeight: CGFloat = 260
    private static let copyGap: CGFloat = 4
    private static let copySize: CGFloat = 28
    private static let bodyFont = UIFont.preferredFont(forTextStyle: .body)
    private static let reasoningFont = UIFont.preferredFont(forTextStyle: .subheadline)
    private static let toolFont = UIFont.systemFont(ofSize: reasoningFont.pointSize, weight: .medium)
    private static let detailFont = UIFont.monospacedSystemFont(ofSize: max(11, reasoningFont.pointSize - 1), weight: .regular)
    private static let timestampFont = UIFont.preferredFont(forTextStyle: .caption2)
    private static let timeFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.locale = Locale.autoupdatingCurrent
        formatter.timeZone = TimeZone.autoupdatingCurrent
        formatter.dateStyle = .none
        formatter.timeStyle = .short
        return formatter
    }()
    private static let dateTimeFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.locale = Locale.autoupdatingCurrent
        formatter.timeZone = TimeZone.autoupdatingCurrent
        formatter.dateStyle = .medium
        formatter.timeStyle = .short
        return formatter
    }()

    private let bubbleView = UIView()
    private let messageLabel = UILabel()
    private let reasoningButton = UIButton(type: .system)
    private let reasoningTextView = UITextView()
    private let reasoningDividerView = UIView()
    private let timestampLabel = UILabel()
    private let copyButton = UIButton(type: .system)
    private var onCopy: (() -> Void)?
    private var onToggleReasoning: (() -> Void)?
    private var onToggleToolDetail: ((Int, ConversationToolDetailSection) -> Void)?
    private var layoutMetrics = Metrics(rowHeight: 44, timestampFrame: .zero, bubbleFrame: .zero, reasoningButtonFrame: .zero, reasoningBodyFrame: .zero, reasoningDividerFrame: .zero, messageFrame: .zero, copyFrame: .zero)

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        selectionStyle = .none
        backgroundColor = .systemBackground
        contentView.backgroundColor = .systemBackground
        timestampLabel.font = Self.timestampFont
        timestampLabel.textColor = .tertiaryLabel
        contentView.addSubview(timestampLabel)
        contentView.addSubview(bubbleView)
        reasoningButton.tintColor = .secondaryLabel
        reasoningButton.setTitleColor(.secondaryLabel, for: .normal)
        reasoningButton.titleLabel?.font = .preferredFont(forTextStyle: .subheadline)
        reasoningButton.contentHorizontalAlignment = .left
        reasoningButton.addTarget(self, action: #selector(reasoningTapped), for: .touchUpInside)
        bubbleView.addSubview(reasoningButton)
        reasoningTextView.delegate = self
        reasoningTextView.isEditable = false
        reasoningTextView.isSelectable = true
        reasoningTextView.isScrollEnabled = false
        reasoningTextView.backgroundColor = .clear
        reasoningTextView.textContainerInset = .zero
        reasoningTextView.textContainer.lineFragmentPadding = 0
        reasoningTextView.linkTextAttributes = [.foregroundColor: UIColor.label]
        bubbleView.addSubview(reasoningTextView)
        reasoningDividerView.backgroundColor = .separator
        bubbleView.addSubview(reasoningDividerView)
        messageLabel.font = Self.bodyFont
        messageLabel.numberOfLines = 0
        bubbleView.addSubview(messageLabel)
        let copyImage = UIImage(systemName: "square.on.square", withConfiguration: UIImage.SymbolConfiguration(pointSize: 10, weight: .regular))
        copyButton.setImage(copyImage, for: .normal)
        copyButton.tintColor = .secondaryLabel
        copyButton.backgroundColor = .clear
        copyButton.contentHorizontalAlignment = .left
        copyButton.accessibilityLabel = "复制"
        copyButton.addTarget(self, action: #selector(copyTapped), for: .touchUpInside)
        contentView.addSubview(copyButton)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func prepareForReuse() {
        super.prepareForReuse()
        onCopy = nil
        onToggleReasoning = nil
        onToggleToolDetail = nil
        messageLabel.text = nil
        reasoningTextView.attributedText = nil
        reasoningButton.setTitle(nil, for: .normal)
        reasoningButton.setImage(nil, for: .normal)
        timestampLabel.text = nil
        reasoningButton.isHidden = true
        reasoningTextView.isHidden = true
        reasoningDividerView.isHidden = true
        copyButton.isHidden = true
    }

    override func layoutSubviews() {
        super.layoutSubviews()
        timestampLabel.frame = layoutMetrics.timestampFrame
        bubbleView.frame = layoutMetrics.bubbleFrame
        reasoningButton.frame = layoutMetrics.reasoningButtonFrame
        reasoningTextView.frame = layoutMetrics.reasoningBodyFrame
        reasoningDividerView.frame = layoutMetrics.reasoningDividerFrame
        messageLabel.frame = layoutMetrics.messageFrame
        copyButton.frame = layoutMetrics.copyFrame
    }

    func configure(with message: ConversationMessage, text: String, showTimestamp: Bool, showCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, toolDisclosureState: ConversationToolDisclosureState, showsReasoningDivider: Bool, metrics: Metrics, onCopy: (() -> Void)?, onToggleReasoning: (() -> Void)?, onToggleToolDetail: ((Int, ConversationToolDetailSection) -> Void)?) {
        self.onCopy = onCopy
        self.onToggleReasoning = onToggleReasoning
        self.onToggleToolDetail = onToggleToolDetail
        layoutMetrics = metrics
        messageLabel.text = text
        let showsReasoning = message.role == .assistant && isFirstChunk && !responseTimeline.isEmpty
        reasoningButton.isHidden = !showsReasoning
        reasoningButton.isUserInteractionEnabled = onToggleReasoning != nil
        reasoningButton.setTitle(showsReasoning ? "思考过程" : nil, for: .normal)
        reasoningButton.setImage(showsReasoning ? UIImage(systemName: reasoningExpanded ? "chevron.down" : "chevron.right") : nil, for: .normal)
        reasoningTextView.attributedText = showsReasoning && reasoningExpanded ? Self.responseTimelineAttributedText(responseTimeline, disclosureState: toolDisclosureState) : nil
        reasoningTextView.isHidden = reasoningTextView.attributedText == nil
        reasoningTextView.isScrollEnabled = showsReasoning && reasoningExpanded && toolDisclosureState.hasExpandedDetail && Self.measuredTimelineSize(responseTimeline, maxWidth: max(1, metrics.reasoningBodyFrame.width), disclosureState: toolDisclosureState).height > metrics.reasoningBodyFrame.height + 0.5
        reasoningDividerView.isHidden = !(showsReasoning && reasoningExpanded && showsReasoningDivider && !metrics.reasoningDividerFrame.isEmpty)
        timestampLabel.text = showTimestamp ? Self.timestampText(for: message.createTime) : nil
        timestampLabel.isHidden = timestampLabel.text == nil
        copyButton.isHidden = !showCopy
        switch message.role {
        case .user:
            bubbleView.backgroundColor = .secondarySystemBackground
            bubbleView.layer.cornerRadius = 18
            if isFirstChunk && isLastChunk { bubbleView.layer.maskedCorners = [.layerMinXMinYCorner, .layerMaxXMinYCorner, .layerMinXMaxYCorner, .layerMaxXMaxYCorner] }
            else if isFirstChunk { bubbleView.layer.maskedCorners = [.layerMinXMinYCorner, .layerMaxXMinYCorner] }
            else if isLastChunk { bubbleView.layer.maskedCorners = [.layerMinXMaxYCorner, .layerMaxXMaxYCorner] }
            else { bubbleView.layer.maskedCorners = [] }
            timestampLabel.textAlignment = .right
        case .assistant:
            bubbleView.backgroundColor = .clear
            bubbleView.layer.cornerRadius = 0
            bubbleView.layer.maskedCorners = []
            timestampLabel.textAlignment = .left
        }
        setNeedsLayout()
    }

    static func metrics(for text: String, role: ConversationMessage.Role, tableWidth: CGFloat, showsTimestamp: Bool, showsCopy: Bool, isFirstChunk: Bool, isLastChunk: Bool, isChunked: Bool, responseTimeline: [ConversationResponseTimelineItem], reasoningExpanded: Bool, toolDisclosureState: ConversationToolDisclosureState, showsReasoningDivider: Bool) -> Metrics {
        let width = max(1, tableWidth)
        var y = isFirstChunk ? outerVerticalPadding : 0
        var timestampFrame = CGRect.zero
        if showsTimestamp {
            let timestampHeight = ceil(timestampFont.lineHeight)
            timestampFrame = CGRect(x: horizontalMargin, y: y, width: max(1, width - horizontalMargin * 2), height: timestampHeight)
            y += timestampHeight + timestampGap
        }
        let maxBubbleWidth: CGFloat
        let maxTextWidth: CGFloat
        switch role {
        case .user:
            maxBubbleWidth = max(36, min(width * userMaxWidthRatio, width - horizontalMargin * 2 - userLeadingGap))
            maxTextWidth = max(1, maxBubbleWidth - bubbleHorizontalPadding * 2)
        case .assistant:
            maxBubbleWidth = max(1, width - horizontalMargin * 2)
            maxTextWidth = max(1, maxBubbleWidth - bubbleHorizontalPadding * 2)
        }
        let textSize = measuredTextSize(text, maxWidth: maxTextWidth)
        let bubbleWidth: CGFloat
        switch role {
        case .user: bubbleWidth = isChunked ? maxBubbleWidth : min(maxBubbleWidth, max(36, ceil(textSize.width) + bubbleHorizontalPadding * 2))
        case .assistant: bubbleWidth = maxBubbleWidth
        }
        let bubbleX = role == .user ? width - horizontalMargin - bubbleWidth : horizontalMargin
        var bubbleY: CGFloat = isFirstChunk ? bubbleVerticalPadding : 0
        var reasoningButtonFrame = CGRect.zero
        var reasoningBodyFrame = CGRect.zero
        var reasoningDividerFrame = CGRect.zero
        if role == .assistant, isFirstChunk, !responseTimeline.isEmpty {
            reasoningButtonFrame = CGRect(x: bubbleHorizontalPadding, y: bubbleY, width: maxTextWidth, height: reasoningButtonHeight)
            bubbleY = reasoningButtonFrame.maxY
            if reasoningExpanded {
                bubbleY += reasoningBodyGap
                let reasoningSize = measuredTimelineSize(responseTimeline, maxWidth: maxTextWidth, disclosureState: toolDisclosureState)
                let bodyHeight = toolDisclosureState.hasExpandedDetail ? min(reasoningSize.height, toolDetailMaximumBodyHeight) : reasoningSize.height
                reasoningBodyFrame = CGRect(x: bubbleHorizontalPadding, y: bubbleY, width: maxTextWidth, height: bodyHeight)
                bubbleY = reasoningBodyFrame.maxY
                if showsReasoningDivider {
                    bubbleY += reasoningDividerGap
                    reasoningDividerFrame = CGRect(x: bubbleHorizontalPadding, y: bubbleY, width: maxTextWidth, height: 1 / UIScreen.main.scale)
                    bubbleY = reasoningDividerFrame.maxY + reasoningDividerGap
                } else {
                    bubbleY += reasoningMessageGap
                }
            } else {
                bubbleY += reasoningMessageGap
            }
        }
        let messageFrame = CGRect(x: bubbleHorizontalPadding, y: bubbleY, width: maxTextWidth, height: textSize.height)
        let bubbleHeight = messageFrame.maxY + (isLastChunk ? bubbleVerticalPadding : 0)
        let bubbleFrame = CGRect(x: bubbleX, y: y, width: bubbleWidth, height: bubbleHeight)
        y = bubbleFrame.maxY
        var copyFrame = CGRect.zero
        if showsCopy {
            y += copyGap
            copyFrame = CGRect(x: horizontalMargin, y: y, width: copySize, height: copySize)
            y = copyFrame.maxY
        }
        if isLastChunk { y += outerVerticalPadding }
        return Metrics(rowHeight: max(1, ceil(y)), timestampFrame: timestampFrame, bubbleFrame: bubbleFrame, reasoningButtonFrame: reasoningButtonFrame, reasoningBodyFrame: reasoningBodyFrame, reasoningDividerFrame: reasoningDividerFrame, messageFrame: messageFrame, copyFrame: copyFrame)
    }

    private static func responseTimelineAttributedText(_ timeline: [ConversationResponseTimelineItem], disclosureState: ConversationToolDisclosureState) -> NSAttributedString {
        let output = NSMutableAttributedString()
        let reasoningParagraph = NSMutableParagraphStyle()
        reasoningParagraph.paragraphSpacing = 3
        let toolParagraph = NSMutableParagraphStyle()
        toolParagraph.paragraphSpacing = 2
        let reasoningAttributes: [NSAttributedString.Key: Any] = [.font: reasoningFont, .foregroundColor: UIColor.secondaryLabel, .paragraphStyle: reasoningParagraph]
        let toolAttributes: [NSAttributedString.Key: Any] = [.font: toolFont, .foregroundColor: UIColor.secondaryLabel, .paragraphStyle: toolParagraph]
        let disclosureAttributes: [NSAttributedString.Key: Any] = [.font: UIFont.systemFont(ofSize: reasoningFont.pointSize - 1, weight: .semibold), .foregroundColor: UIColor.label]
        let detailAttributes: [NSAttributedString.Key: Any] = [.font: detailFont, .foregroundColor: UIColor.secondaryLabel]
        for item in timeline {
            let normalized = item.text.trimmingCharacters(in: .whitespacesAndNewlines)
            guard !normalized.isEmpty else { continue }
            if output.length > 0 { output.append(NSAttributedString(string: "\n", attributes: reasoningAttributes)) }
            switch item.kind {
            case .reasoning:
                output.append(NSAttributedString(string: normalized, attributes: reasoningAttributes))
            case .tool:
                appendToolIcon(item.toolIconKind, to: output)
                output.append(NSAttributedString(string: " \(normalized) · \(item.completed ? "已完成" : "调用中")", attributes: toolAttributes))
                guard let slot = item.toolSlot else { continue }
                if !item.toolInputJSON.isEmpty {
                    let expanded = disclosureState.expandedInputSlots.contains(slot)
                    var attributes = disclosureAttributes
                    if let url = URL(string: "chatgpt-tool-input://slot/\(slot)") { attributes[.link] = url }
                    output.append(NSAttributedString(string: "\n  \(expanded ? "▾" : "▸") 工具输入", attributes: attributes))
                    if expanded { output.append(NSAttributedString(string: "\n" + prettyJSONString(item.toolInputJSON), attributes: detailAttributes)) }
                }
                if !item.toolOutputJSON.isEmpty {
                    let expanded = disclosureState.expandedOutputSlots.contains(slot)
                    var attributes = disclosureAttributes
                    if let url = URL(string: "chatgpt-tool-output://slot/\(slot)") { attributes[.link] = url }
                    output.append(NSAttributedString(string: "\n  \(expanded ? "▾" : "▸") 工具输出", attributes: attributes))
                    if expanded { output.append(NSAttributedString(string: "\n" + formattedToolOutput(item.toolOutputJSON), attributes: detailAttributes)) }
                }
            }
        }
        return output
    }

    private static func appendToolIcon(_ kind: ConversationToolIconKind, to output: NSMutableAttributedString) {
        if kind == .github {
            output.append(NSAttributedString(string: "GH", attributes: [.font: UIFont.monospacedSystemFont(ofSize: max(10, reasoningFont.pointSize - 2), weight: .bold), .foregroundColor: UIColor.secondaryLabel]))
            return
        }
        let symbolName = kind == .code ? "chevron.left.slash.chevron.right" : "wrench"
        guard let image = UIImage(systemName: symbolName, withConfiguration: UIImage.SymbolConfiguration(pointSize: max(10, reasoningFont.pointSize - 1), weight: .medium))?.withTintColor(.secondaryLabel, renderingMode: .alwaysOriginal) else {
            output.append(NSAttributedString(string: kind == .code ? "<>" : "•", attributes: [.font: toolFont, .foregroundColor: UIColor.secondaryLabel]))
            return
        }
        let attachment = NSTextAttachment()
        attachment.image = image
        attachment.bounds = CGRect(x: 0, y: -2, width: image.size.width, height: image.size.height)
        output.append(NSAttributedString(attachment: attachment))
    }

    private static func measuredTextSize(_ text: String, maxWidth: CGFloat) -> CGSize {
        guard !text.isEmpty else { return CGSize(width: 0, height: ceil(bodyFont.lineHeight)) }
        let rect = (text as NSString).boundingRect(with: CGSize(width: maxWidth, height: .greatestFiniteMagnitude), options: [.usesLineFragmentOrigin, .usesFontLeading], attributes: [.font: bodyFont], context: nil)
        return CGSize(width: min(maxWidth, ceil(rect.width)), height: max(ceil(bodyFont.lineHeight), ceil(rect.height) + 1))
    }

    private static func measuredTimelineSize(_ timeline: [ConversationResponseTimelineItem], maxWidth: CGFloat, disclosureState: ConversationToolDisclosureState) -> CGSize {
        let attributed = responseTimelineAttributedText(timeline, disclosureState: disclosureState)
        guard attributed.length > 0 else { return .zero }
        let rect = attributed.boundingRect(with: CGSize(width: maxWidth, height: .greatestFiniteMagnitude), options: [.usesLineFragmentOrigin, .usesFontLeading], context: nil)
        return CGSize(width: min(maxWidth, ceil(rect.width)), height: max(ceil(reasoningFont.lineHeight), ceil(rect.height) + 2))
    }

    private static func prettyJSONString(_ raw: String) -> String {
        guard let data = raw.data(using: .utf8), let object = try? JSONSerialization.jsonObject(with: data), JSONSerialization.isValidJSONObject(object), let pretty = try? JSONSerialization.data(withJSONObject: object, options: [.prettyPrinted]), let text = String(data: pretty, encoding: .utf8) else { return raw }
        return text
    }

    private static func formattedToolOutput(_ raw: String) -> String {
        guard let data = raw.data(using: .utf8), let object = try? JSONSerialization.jsonObject(with: data) else { return raw }
        return formatToolValue(object, indent: 0)
    }

    private static func formatToolValue(_ value: Any, indent: Int) -> String {
        let prefix = String(repeating: "  ", count: indent)
        if let dictionary = value as? [String: Any] {
            if dictionary.isEmpty { return prefix + "{}" }
            return orderedToolKeys(dictionary).compactMap { key -> String? in
                guard let child = dictionary[key] else { return nil }
                if let string = child as? String {
                    if let nested = decodedJSONContainer(string) { return prefix + key + ":\n" + formatToolValue(nested, indent: indent + 1) }
                    if string.contains("\n") { return prefix + key + ":\n" + indentToolString(string, indent: indent + 1) }
                    return prefix + key + ": " + string
                }
                if child is [String: Any] || child is [Any] { return prefix + key + ":\n" + formatToolValue(child, indent: indent + 1) }
                return prefix + key + ": " + formatToolScalar(child)
            }.joined(separator: "\n")
        }
        if let array = value as? [Any] {
            if array.isEmpty { return prefix + "Array(0)" }
            var lines = [prefix + "Array(\(array.count))"]
            for (index, child) in array.enumerated() {
                let itemPrefix = prefix + "  \(index):"
                if let string = child as? String {
                    if let nested = decodedJSONContainer(string) { lines.append(itemPrefix + "\n" + formatToolValue(nested, indent: indent + 2)) }
                    else if string.contains("\n") { lines.append(itemPrefix + "\n" + indentToolString(string, indent: indent + 2)) }
                    else { lines.append(itemPrefix + " " + string) }
                } else if child is [String: Any] || child is [Any] {
                    lines.append(itemPrefix + "\n" + formatToolValue(child, indent: indent + 2))
                } else {
                    lines.append(itemPrefix + " " + formatToolScalar(child))
                }
            }
            return lines.joined(separator: "\n")
        }
        if let string = value as? String { return prefix + string }
        return prefix + formatToolScalar(value)
    }

    private static func orderedToolKeys(_ dictionary: [String: Any]) -> [String] {
        let preferred = ["content_type", "language", "response_format_name", "text", "parts"]
        let first = preferred.filter { dictionary[$0] != nil }
        let remaining = dictionary.keys.filter { !preferred.contains($0) }.sorted()
        return first + remaining
    }

    private static func decodedJSONContainer(_ string: String) -> Any? {
        let trimmed = string.trimmingCharacters(in: .whitespacesAndNewlines)
        guard let first = trimmed.first, first == "{" || first == "[", let data = trimmed.data(using: .utf8), let object = try? JSONSerialization.jsonObject(with: data), object is [String: Any] || object is [Any] else { return nil }
        return object
    }

    private static func indentToolString(_ string: String, indent: Int) -> String {
        let prefix = String(repeating: "  ", count: indent)
        return string.components(separatedBy: "\n").map { prefix + $0 }.joined(separator: "\n")
    }

    private static func formatToolScalar(_ value: Any) -> String {
        if value is NSNull { return "null" }
        if let boolean = value as? Bool { return boolean ? "true" : "false" }
        if let number = value as? NSNumber { return number.stringValue }
        return String(describing: value)
    }

    func textView(_ textView: UITextView, shouldInteractWith URL: URL, in characterRange: NSRange, interaction: UITextItemInteraction) -> Bool {
        guard let slot = Int(URL.lastPathComponent) else { return true }
        switch URL.scheme {
        case "chatgpt-tool-input": onToggleToolDetail?(slot, .input); return false
        case "chatgpt-tool-output": onToggleToolDetail?(slot, .output); return false
        default: return true
        }
    }

    @objc private func copyTapped() { onCopy?() }
    @objc private func reasoningTapped() { onToggleReasoning?() }

    private static func timestampText(for createTime: TimeInterval?) -> String? {
        guard let createTime, createTime > 0 else { return nil }
        let date = Date(timeIntervalSince1970: createTime)
        return Calendar.autoupdatingCurrent.isDate(date, inSameDayAs: Date()) ? timeFormatter.string(from: date) : dateTimeFormatter.string(from: date)
    }
}
'''
write(conv, text[:idx] + new_cell)

auth = "ChatGPTClient/Authentication/AuthSessionStore.swift"

replace_once(auth,
r'''                guard let response = response as? HTTPURLResponse, let data, (200..<300).contains(response.statusCode) else {
                    session.finishTasksAndInvalidate()
                    let status = (response as? HTTPURLResponse).map { String($0.statusCode) } ?? "none"
                    self.finishAccountProbe(.notAvailable, span: span, fields: ["stage": "session", "httpStatus": status], completion: completion)
                    return
                }
''',
r'''                guard let response = response as? HTTPURLResponse, let data, (200..<300).contains(response.statusCode) else {
                    session.finishTasksAndInvalidate()
                    let statusCode = (response as? HTTPURLResponse)?.statusCode
                    let status = statusCode.map(String.init) ?? "none"
                    let state: AuthAccountContextState = statusCode == 403 ? .failed : .notAvailable
                    var fields = ["stage": "session", "httpStatus": status]
                    if statusCode == 403 { fields["reason"] = "temporary_forbidden" }
                    self.finishAccountProbe(state, span: span, fields: fields, completion: completion)
                    return
                }
''')

replace_once(auth,
r'''                    guard let response = response as? HTTPURLResponse, let data, (200..<300).contains(response.statusCode) else {
                        let status = (response as? HTTPURLResponse).map { String($0.statusCode) } ?? "none"
                        self.finishAccountProbe(.notAvailable, span: span, fields: ["stage": "accounts", "httpStatus": status], completion: completion)
                        return
                    }
''',
r'''                    guard let response = response as? HTTPURLResponse, let data, (200..<300).contains(response.statusCode) else {
                        let statusCode = (response as? HTTPURLResponse)?.statusCode
                        let status = statusCode.map(String.init) ?? "none"
                        let state: AuthAccountContextState = statusCode == 403 ? .failed : .notAvailable
                        var fields = ["stage": "accounts", "httpStatus": status]
                        if statusCode == 403 { fields["reason"] = "temporary_forbidden" }
                        self.finishAccountProbe(state, span: span, fields: fields, completion: completion)
                        return
                    }
''')

replace_once(auth,
r'''        accountState = state
        if state == .notAvailable || state == .failed || state == .unknown { accountContext = nil }
        let contextInvalidated = hadContext && accountContext == nil
''',
r'''        accountState = state
        if state == .notAvailable || state == .unknown { accountContext = nil }
        let contextInvalidated = hadContext && accountContext == nil
''')

pbx = "ChatGPTClient.xcodeproj/project.pbxproj"
replace_once(pbx, "CURRENT_PROJECT_VERSION = 69;", "CURRENT_PROJECT_VERSION = 70;")
replace_once(pbx, "CURRENT_PROJECT_VERSION = 69;", "CURRENT_PROJECT_VERSION = 70;")
replace_once(pbx, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b69";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b70";')
replace_once(pbx, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b69";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b70";')

workflow = ".github/workflows/ios-foundation.yml"
replace_once(workflow, "# Candidate: DEV-send-stream-0.1.0-b69", "# Candidate: DEV-send-stream-0.1.0-b70")
replace_once(workflow, "ChatGPTClient-DEV-send-stream-0.1.0-b69", "ChatGPTClient-DEV-send-stream-0.1.0-b70")

root_text = read(root)
conv_text = read(conv)
auth_text = read(auth)
pbx_text = read(pbx)
wf_text = read(workflow)
assert "element.setAttribute('inputmode', 'none')" in root_text
assert "self.webView.endEditing(true)" in root_text
assert "promptText: String" in root_text and "promptCharacterCount" not in root_text
assert "detailInput" in root_text and "invokedResource.app_name === 'GitHub'" in root_text
assert "livePresentationMessages = [userMessage, assistantMessage]" in conv_text
assert "chatgpt-tool-input://slot/" in conv_text and "chatgpt-tool-output://slot/" in conv_text
assert "reasoningDividerFrame" in conv_text and "toolDetailMaximumBodyHeight" in conv_text
assert "authTransport.invalidated" in conv_text and "status == 401 || status == 403" in conv_text
assert "nativeRead.login.returnRefresh" in conv_text
assert "statusCode == 403 ? .failed : .notAvailable" in auth_text
assert "state == .notAvailable || state == .unknown" in auth_text
assert "CURRENT_PROJECT_VERSION = 70;" in pbx_text and "DEV-send-stream-0.1.0-b70" in pbx_text
assert "DEV-send-stream-0.1.0-b70" in wf_text
print("b70 exact-anchor assembly patch complete")
