from pathlib import Path

root = Path('ChatGPTClient/RootViewController.swift')
text = root.read_text()

def rep(old, new, label):
    global text
    if old not in text:
        raise SystemExit(f'missing root anchor: {label}')
    text = text.replace(old, new, 1)

rep('''enum CoveredWebSendEvent {
    case composerReady
''','''enum CoveredWebSendEvent {
    case externalResumeObserved
    case composerReady
''','event case')

rep('''    private var pendingSend: PendingSend?
    private var activeEvents: ((CoveredWebSendEvent) -> Void)?
    private var responseActive = false
''','''    private var pendingSend: PendingSend?
    private var observationEvents: ((CoveredWebSendEvent) -> Void)?
    private var activeEvents: ((CoveredWebSendEvent) -> Void)?
    private var responseActive = false
''','observation state')

rep('''    func sendExistingConversation(text: String, conversationID: String, events: @escaping (CoveredWebSendEvent) -> Void) {
''','''    func observeExistingConversation(conversationID: String, events: @escaping (CoveredWebSendEvent) -> Void) {
        precondition(Thread.isMainThread)
        guard !conversationID.isEmpty else { return }
        observationEvents = events
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

    func sendExistingConversation(text: String, conversationID: String, events: @escaping (CoveredWebSendEvent) -> Void) {
''','observe method')

rep('''        pendingSend = nil
        activeEvents = nil
        responseActive = false
''','''        pendingSend = nil
        observationEvents = nil
        activeEvents = nil
        responseActive = false
''','reset observation')

rep('''        switch kind {
        case "composer_state":
''','''        switch kind {
        case "external_resume_observed":
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
        case "composer_state":
''','resume native events')

rep('''      const filteredResponse = response => {
''','''      const observedResponse = response => {
        let cloned;
        try { cloned = response.clone(); } catch (_) { return; }
        if (!cloned.body || typeof cloned.body.getReader !== 'function') return;
        const reader = cloned.body.getReader();
        const state = { reasoningEnded: false, textContinuationActive: false, reasoningPreambleSeen: new Set(), reasoningPreambleCount: 0, reasoningActiveSeen: new Set(), invocations: new Map(), toolSeen: new Set(), nextToolSlot: 0, terminal: false };
        let buffer = '';
        (async () => {
          try {
            while (true) {
              const result = await reader.read();
              if (result.done) {
                buffer = (buffer + decoder.decode()).replace(/\\r\\n/g, '\\n');
                if (buffer.trim()) filterFrame(buffer, state);
                if (!state.terminal) post({ kind: 'stream_error', state: 'stream_ended_without_done' });
                return;
              }
              buffer = (buffer + decoder.decode(result.value || new Uint8Array(), { stream: true })).replace(/\\r\\n/g, '\\n');
              let boundary;
              while ((boundary = buffer.indexOf('\\n\\n')) >= 0) {
                const frame = buffer.slice(0, boundary);
                buffer = buffer.slice(boundary + 2);
                filterFrame(frame, state);
              }
            }
          } catch (_) {
            post({ kind: 'stream_error', state: 'reader_failed' });
          }
        })();
      };
      const filteredResponse = response => {
''','observer parser')

old_fetch = '''      window.fetch = async function(input, init) {
        let url = null;
        try { url = new URL(typeof input === 'string' ? input : input && input.url || '', location.href); } catch (_) {}
        const isSend = !!url && isChatGPTHost(url.hostname.toLowerCase()) && url.pathname === '/backend-api/f/conversation';
        if (!isSend || !activeSend) return originalFetch(input, init);
        post({ kind: 'send_observed' });
        probeComposer(true);
        try {
          const response = await originalFetch(input, init);
          const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
          post({ kind: 'send_response', status: response.status, contentType });
          if (response.status !== 200 || contentType !== 'text/event-stream') {
            activeSend = false;
            probeComposer(true);
            post({ kind: 'stream_error', state: 'send_not_sse' });
            return response;
          }
          return filteredResponse(response);
        } catch (error) {
          activeSend = false;
          probeComposer(true);
          post({ kind: 'stream_error', state: 'send_transport_error' });
          throw error;
        }
      };
'''
new_fetch = '''      window.fetch = async function(input, init) {
        let url = null;
        try { url = new URL(typeof input === 'string' ? input : input && input.url || '', location.href); } catch (_) {}
        const chatHost = !!url && isChatGPTHost(url.hostname.toLowerCase());
        const isSend = chatHost && url.pathname === '/backend-api/f/conversation';
        const isResume = chatHost && url.pathname === '/backend-api/f/conversation/resume';
        if (isResume) {
          let resumeConversationID = null;
          if (init && typeof init.body === 'string') {
            try {
              const resumeBody = JSON.parse(init.body);
              if (resumeBody && typeof resumeBody === 'object' && !Array.isArray(resumeBody) && typeof resumeBody.conversation_id === 'string') resumeConversationID = resumeBody.conversation_id;
            } catch (_) {}
          }
          if (resumeConversationID && resumeConversationID === currentConversationID()) {
            post({ kind: 'external_resume_observed' });
            try {
              const response = await originalFetch(input, init);
              const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
              post({ kind: 'resume_response', status: response.status, contentType });
              if (response.status === 200 && contentType === 'text/event-stream') observedResponse(response);
              return response;
            } catch (error) {
              post({ kind: 'stream_error', state: 'resume_transport_error' });
              throw error;
            }
          }
        }
        if (!isSend || !activeSend) return originalFetch(input, init);
        post({ kind: 'send_observed' });
        probeComposer(true);
        try {
          const response = await originalFetch(input, init);
          const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
          post({ kind: 'send_response', status: response.status, contentType });
          if (response.status !== 200 || contentType !== 'text/event-stream') {
            activeSend = false;
            probeComposer(true);
            post({ kind: 'stream_error', state: 'send_not_sse' });
            return response;
          }
          return filteredResponse(response);
        } catch (error) {
          activeSend = false;
          probeComposer(true);
          post({ kind: 'stream_error', state: 'send_transport_error' });
          throw error;
        }
      };
'''
rep(old_fetch, new_fetch, 'fetch wrapper')

rep('''    func beginLiveResponse(conversationID: String, promptText: String) -> Result<Int, Error> {
''','''    func beginExternalLiveResponse(conversationID: String) -> Result<Int, Error> {
        precondition(Thread.isMainThread)
        if responseRuntime.snapshots[conversationID]?.phase.isActive == true { return .failure(ConversationLiveResponseError.responseAlreadyActive) }
        let generation = (responseRuntime.generations[conversationID] ?? 0) + 1
        responseRuntime.generations[conversationID] = generation
        let baselineVisibleMessageCount = selectedConversationID == conversationID ? (selectedConversation?.messages.count ?? 0) : 0
        responseRuntime.snapshots[conversationID] = ConversationLiveResponseSnapshot(generation: generation, conversationID: conversationID, baselineVisibleMessageCount: baselineVisibleMessageCount, promptText: "", phase: .thinking, timeline: [], finalText: "", reasoningEnded: false, reasoningDurationSeconds: nil, failureReason: nil)
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["phase"] = ConversationLiveResponsePhase.thinking.rawValue
        fields["source"] = "external_resume"
        fields["baselineVisibleMessageCount"] = String(baselineVisibleMessageCount)
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.started", fields: fields)
        responseRuntime.onChange?(conversationID)
        return .success(generation)
    }

    @discardableResult
    func beginLiveResponse(conversationID: String, promptText: String) -> Result<Int, Error> {
''','external begin')

rep('''    switch event {
    case .composerReady: eventName = "composer_ready"
''','''    switch event {
    case .externalResumeObserved: eventName = "external_resume_observed"
    case .composerReady: eventName = "composer_ready"
''','consume event')

rep('''        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.repository.selectConversation(id: id)
''','''        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.releaseIdleExecutors(except: id)
            self.repository.selectConversation(id: id)
''','selection release idle')

rep('''            self.updateLivePresentation()
            self.show(.secondary)
        }
''','''            self.updateLivePresentation()
            self.show(.secondary)
            self.observeExternalResponseIfNeeded(conversationID: id)
        }
''','selection observe')

rep('''    private func releaseExecutor(for conversationID: String, expected: CoveredWebSendExecutor) {
        guard sendExecutors[conversationID] === expected else { return }
        sendExecutors.removeValue(forKey: conversationID)
        diagnostics.info(category: "webSend", name: "coveredExecutor.released", fields: ["activeExecutorCount": String(sendExecutors.count)])
    }

    private func startValidationSend(text: String, conversationID: String) {
''','''    private func releaseExecutor(for conversationID: String, expected: CoveredWebSendExecutor) {
        guard sendExecutors[conversationID] === expected else { return }
        sendExecutors.removeValue(forKey: conversationID)
        diagnostics.info(category: "webSend", name: "coveredExecutor.released", fields: ["activeExecutorCount": String(sendExecutors.count)])
    }

    private func releaseIdleExecutors(except conversationID: String) {
        let idle = sendExecutors.filter { $0.key != conversationID && !$0.value.isBusy }
        for (id, executor) in idle { releaseExecutor(for: id, expected: executor) }
    }

    private func observeExternalResponseIfNeeded(conversationID: String) {
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

    private func startValidationSend(text: String, conversationID: String) {
''','external observer')

rep('''            self.updateLivePresentation()
        }
    }

    private func liveResponseDidChange(id: String) {
''','''            self.updateLivePresentation()
            if self.repository.selectedConversationID == conversationID, !self.repository.isLiveResponseActive(for: conversationID) { self.observeExternalResponseIfNeeded(conversationID: conversationID) }
        }
    }

    private func liveResponseDidChange(id: String) {
''','reobserve after reconcile')

root.write_text(text)

conv = Path('ChatGPTClient/Conversation/ConversationFeature.swift')
ct = conv.read_text()
old = '''    let userMessage = ConversationMessage(id: "live-user-\\(snapshot.generation)", role: .user, text: snapshot.promptText, responseTimeline: [], reasoningDurationSeconds: nil, createTime: nil)
'''
if old in ct:
    ct = ct.replace(old, '''    let userMessage = snapshot.promptText.isEmpty ? nil : ConversationMessage(id: "live-user-\\(snapshot.generation)", role: .user, text: snapshot.promptText, responseTimeline: [], reasoningDurationSeconds: nil, createTime: nil)
''', 1)
    old2 = '''    livePresentationMessages = [userMessage, assistantMessage]
'''
    if old2 not in ct:
        raise SystemExit('missing livePresentationMessages anchor')
    ct = ct.replace(old2, '''    livePresentationMessages = userMessage.map { [$0, assistantMessage] } ?? [assistantMessage]
''', 1)
else:
    if 'snapshot.promptText.isEmpty' not in ct:
        raise SystemExit('missing live user anchor')
conv.write_text(ct)

project = Path('ChatGPTClient.xcodeproj/project.pbxproj')
p = project.read_text()
if 'CURRENT_PROJECT_VERSION = 73;' not in p or 'DEV-send-stream-0.1.0-b73' not in p:
    raise SystemExit('project identity anchors missing')
p = p.replace('CURRENT_PROJECT_VERSION = 73;', 'CURRENT_PROJECT_VERSION = 74;')
p = p.replace('DEV-send-stream-0.1.0-b73', 'DEV-send-stream-0.1.0-b74')
project.write_text(p)
