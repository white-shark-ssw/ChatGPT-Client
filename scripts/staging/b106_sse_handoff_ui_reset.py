from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


project = Path("ChatGPTClient.xcodeproj/project.pbxproj")
ptext = project.read_text()
if ptext.count("CURRENT_PROJECT_VERSION = 105;") != 2:
    raise SystemExit("unexpected Build105 occurrence count")
if ptext.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b105";') != 2:
    raise SystemExit("unexpected b105 candidate occurrence count")
ptext = ptext.replace("CURRENT_PROJECT_VERSION = 105;", "CURRENT_PROJECT_VERSION = 106;")
ptext = ptext.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b105";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b106";')
project.write_text(ptext)

root = Path("ChatGPTClient/RootViewController.swift")
text = root.read_text()

text = replace_once(
    text,
    '''    private var rootComposerReady = false
    private var sendingNewConversation = false
    private var pendingSend: PendingSend?
''',
    '''    private var rootComposerReady = false
    private var sendingNewConversation = false
    private var pendingNewConversationEvents: [CoveredWebSendEvent] = []
    private var pendingSend: PendingSend?
''',
    "executor preidentity event staging"
)

text = replace_once(
    text,
    '''        clientSendAccepted = false
        sendingNewConversation = false
        rootComposerReady = false
        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
''',
    '''        clientSendAccepted = false
        sendingNewConversation = false
        pendingNewConversationEvents.removeAll(keepingCapacity: true)
        rootComposerReady = false
        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
''',
    "existing send clears preidentity events"
)

text = replace_once(
    text,
    '''        clientSendAccepted = false
        sendingNewConversation = true
        pendingSend = PendingSend(conversationID: nil, text: trimmed, events: events)
''',
    '''        clientSendAccepted = false
        sendingNewConversation = true
        pendingNewConversationEvents.removeAll(keepingCapacity: true)
        pendingSend = PendingSend(conversationID: nil, text: trimmed, events: events)
''',
    "new send clears preidentity events"
)

text = replace_once(
    text,
    '''        manualSyncFocusProbePending = false
        sendingNewConversation = false
        currentConversationID = nil
''',
    '''        manualSyncFocusProbePending = false
        sendingNewConversation = false
        pendingNewConversationEvents.removeAll(keepingCapacity: true)
        currentConversationID = nil
''',
    "account reset clears preidentity events"
)

text = replace_once(
    text,
    '''        if clientSendAccepted, responseActive, let interruptedEvents = activeEvents {
''',
    '''        if clientSendAccepted, responseActive, currentConversationID != nil, let interruptedEvents = activeEvents {
''',
    "accepted recovery requires authoritative identity"
)

old_observed = '''        case "send_observed":
            let wasNewConversation = sendingNewConversation
            if wasNewConversation {
                guard let createdConversationID = body["conversationID"] as? String, !createdConversationID.isEmpty else {
                    failCurrent("new_conversation_identity_missing")
                    return
                }
                currentConversationID = createdConversationID
                composerReadyConversationID = nil
                rootComposerReady = false
                sendingNewConversation = false
                activeEvents?(.conversationCreated(createdConversationID))
            }
            responseActive = true
            pendingSend = nil
            activeEvents?(.sendObserved)
            diagnostics.info(category: "webSend", name: "coveredExecutor.sendObserved", fields: ["target": wasNewConversation ? "new_conversation" : "existing_conversation"])
'''
new_observed = '''        case "conversation_created":
            guard sendingNewConversation, let createdConversationID = body["conversationID"] as? String, !createdConversationID.isEmpty else { return }
            if let existingConversationID = currentConversationID {
                guard existingConversationID == createdConversationID else {
                    failCurrent("new_conversation_identity_conflict")
                    return
                }
                return
            }
            currentConversationID = createdConversationID
            composerReadyConversationID = nil
            rootComposerReady = false
            let stagedEvents = pendingNewConversationEvents
            pendingNewConversationEvents.removeAll(keepingCapacity: true)
            sendingNewConversation = false
            activeEvents?(.conversationCreated(createdConversationID))
            for stagedEvent in stagedEvents { activeEvents?(stagedEvent) }
            diagnostics.info(category: "webSend", name: "coveredExecutor.newConversationIdentity", fields: ["source": "protected_send_sse_conversation_id", "stagedEventCount": String(stagedEvents.count)])
        case "send_observed":
            let wasNewConversation = sendingNewConversation
            responseActive = true
            pendingSend = nil
            emitClientEvent(.sendObserved)
            diagnostics.info(category: "webSend", name: "coveredExecutor.sendObserved", fields: ["target": wasNewConversation ? "new_conversation" : "existing_conversation"])
'''
text = replace_once(text, old_observed, new_observed, "SSE authoritative identity handler")

text = replace_once(
    text,
    '''                clientSendAccepted = true
                activeEvents?(.responseAccepted)
''',
    '''                clientSendAccepted = true
                emitClientEvent(.responseAccepted)
''',
    "response accepted staging"
)

text = replace_once(text, '''        case "thinking_active": activeEvents?(.thinkingActive)
''', '''        case "thinking_active": emitClientEvent(.thinkingActive)
''', "thinking staging")
text = replace_once(text, '''            activeEvents?(.reasoningPreamble(text, segmentStart: (body["segmentStart"] as? NSNumber)?.boolValue ?? false))
''', '''            emitClientEvent(.reasoningPreamble(text, segmentStart: (body["segmentStart"] as? NSNumber)?.boolValue ?? false))
''', "preamble staging")
text = replace_once(text, '''            activeEvents?(.reasoningDelta(text))
''', '''            emitClientEvent(.reasoningDelta(text))
''', "reasoning staging")
text = replace_once(text, '''        case "reasoning_ended": activeEvents?(.reasoningEnded((body["durationSec"] as? NSNumber)?.intValue))
''', '''        case "reasoning_ended": emitClientEvent(.reasoningEnded((body["durationSec"] as? NSNumber)?.intValue))
''', "reasoning end staging")
text = replace_once(text, '''            activeEvents?(.finalDelta(text))
''', '''            emitClientEvent(.finalDelta(text))
''', "final staging")
text = replace_once(
    text,
    '''            activeEvents?(.toolActivity(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: (body["completed"] as? NSNumber)?.boolValue ?? false, inputJSON: inputJSON, outputJSON: outputJSON, iconKind: iconKind))
''',
    '''            emitClientEvent(.toolActivity(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: (body["completed"] as? NSNumber)?.boolValue ?? false, inputJSON: inputJSON, outputJSON: outputJSON, iconKind: iconKind))
''',
    "tool staging"
)

text = replace_once(
    text,
    '''        case "terminal":
            let terminalEvents = activeEvents
''',
    '''        case "terminal":
            if sendingNewConversation, currentConversationID == nil {
                failCurrent("new_conversation_identity_missing_at_terminal")
                return
            }
            let terminalEvents = activeEvents
''',
    "terminal requires authoritative identity"
)

old_submit_helper = '''    private func submitPendingSendIfReady() {
'''
new_submit_helper = '''    private func emitClientEvent(_ event: CoveredWebSendEvent) {
        if sendingNewConversation, currentConversationID == nil {
            pendingNewConversationEvents.append(event)
            return
        }
        activeEvents?(event)
    }

    private func submitPendingSendIfReady() {
'''
text = replace_once(text, old_submit_helper, new_submit_helper, "client event staging helper")

text = replace_once(
    text,
    '''        sendingNewConversation = false
        activeEvents = nil
''',
    '''        sendingNewConversation = false
        pendingNewConversationEvents.removeAll(keepingCapacity: true)
        activeEvents = nil
''',
    "failure clears preidentity events"
)

old_js_gate = '''        if (!isSend || !activeSend) return originalFetch(input, init);
        if (newConversationSend && !pageConversationID) {
          activeSend = false;
          newConversationSend = false;
          probeComposer(true);
          post({ kind: 'stream_error', state: 'new_conversation_identity_missing' });
          throw new Error('new_conversation_identity_missing');
        }
        post({ kind: 'send_observed', conversationID: pageConversationID, newConversation: newConversationSend });
'''
new_js_gate = '''        if (!isSend || !activeSend) return originalFetch(input, init);
        post({ kind: 'send_observed', newConversation: newConversationSend, pageRoute: pageRouteShape() });
'''
text = replace_once(text, old_js_gate, new_js_gate, "remove pre-fetch route identity gate")

old_filter_parse = '''        let payload;
        try { payload = JSON.parse(data); }
        catch (_) { state.textContinuationActive = false; return frame + '\\n\\n'; }
        observeReasoningActive(payload, state);
'''
new_filter_parse = '''        let payload;
        try { payload = JSON.parse(data); }
        catch (_) { state.textContinuationActive = false; return frame + '\\n\\n'; }
        if (newConversationSend && payload && typeof payload === 'object' && !Array.isArray(payload) && typeof payload.conversation_id === 'string' && payload.conversation_id.trim()) {
          const streamConversationID = payload.conversation_id.trim();
          if (state.authoritativeConversationID && state.authoritativeConversationID !== streamConversationID) {
            activeSend = false;
            newConversationSend = false;
            post({ kind: 'stream_error', state: 'new_conversation_identity_conflict' });
            return frame + '\\n\\n';
          }
          if (!state.authoritativeConversationID) {
            state.authoritativeConversationID = streamConversationID;
            post({ kind: 'conversation_created', conversationID: streamConversationID });
          }
        }
        observeReasoningActive(payload, state);
'''
text = replace_once(text, old_filter_parse, new_filter_parse, "SSE conversation identity observation")

old_state = '''const state = { reasoningEnded: false, textContinuationActive: false, reasoningPreambleSeen: new Set(), reasoningPreambleCount: 0, reasoningActiveSeen: new Set(), invocations: new Map(), toolSeen: new Set(), nextToolSlot: 0, terminal: false };'''
new_state = '''const state = { reasoningEnded: false, textContinuationActive: false, reasoningPreambleSeen: new Set(), reasoningPreambleCount: 0, reasoningActiveSeen: new Set(), invocations: new Map(), toolSeen: new Set(), nextToolSlot: 0, terminal: false, authoritativeConversationID: null };'''
if text.count(old_state) != 2:
    raise SystemExit(f"stream state: expected two matches, found {text.count(old_state)}")
text = text.replace(old_state, new_state)

text = replace_once(
    text,
    '''                fields["source"] = "official_page_route_before_protected_send"
''',
    '''                fields["source"] = "protected_send_sse_conversation_id"
''',
    "handoff diagnostic source"
)

root.write_text(text)

feature = Path("ChatGPTClient/Conversation/ConversationFeature.swift")
text = feature.read_text()

text = replace_once(
    text,
    '''        messageLabel.text = nil
        messageLabel.attributedText = nil
        reasoningTextView.attributedText = nil
''',
    '''        messageLabel.text = nil
        messageLabel.attributedText = nil
        messageLabel.isHighlighted = false
        messageLabel.textColor = .label
        messageLabel.highlightedTextColor = .label
        messageLabel.tintColor = .label
        reasoningTextView.attributedText = nil
''',
    "reuse assistant label state reset"
)

text = replace_once(
    text,
    '''    layoutMetrics = metrics
    switch message.role {
    case .assistant: messageLabel.attributedText = Self.assistantBodyAttributedText(text)
    case .user: messageLabel.attributedText = Self.userBodyAttributedText(text)
    }
''',
    '''    layoutMetrics = metrics
    messageLabel.isHighlighted = false
    messageLabel.textColor = .label
    messageLabel.highlightedTextColor = .label
    messageLabel.tintColor = .label
    switch message.role {
    case .assistant: messageLabel.attributedText = Self.assistantBodyAttributedText(text)
    case .user: messageLabel.attributedText = Self.userBodyAttributedText(text)
    }
''',
    "configure assistant label state reset"
)

feature.write_text(text)
print("b106 product patch complete")
