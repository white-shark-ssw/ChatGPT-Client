from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


project = Path("ChatGPTClient.xcodeproj/project.pbxproj")
ptext = project.read_text()
if ptext.count("CURRENT_PROJECT_VERSION = 104;") != 2:
    raise SystemExit("unexpected Build104 occurrence count")
if ptext.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b104";') != 2:
    raise SystemExit("unexpected b104 candidate occurrence count")
ptext = ptext.replace("CURRENT_PROJECT_VERSION = 104;", "CURRENT_PROJECT_VERSION = 105;")
ptext = ptext.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b104";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b105";')
project.write_text(ptext)

feature = Path("ChatGPTClient/Conversation/ConversationFeature.swift")
text = feature.read_text()
text = replace_once(text, '''final class ConversationSidebarViewController: UITableViewController {
    var onSelectConversation: ((String) -> Void)?
''', '''final class ConversationSidebarViewController: UITableViewController {
    var onSelectConversation: ((String) -> Void)?
    var onNewConversation: (() -> Void)?
''', "sidebar callback")
text = replace_once(text, '''        navigationItem.leftBarButtonItem = UIBarButtonItem(title: "设置", style: .plain, target: self, action: #selector(openSettings))
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadConversationsFromButton))
''', '''        navigationItem.leftBarButtonItem = UIBarButtonItem(title: "设置", style: .plain, target: self, action: #selector(openSettings))
        let refreshButton = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadConversationsFromButton))
        let newConversationButton = UIBarButtonItem(barButtonSystemItem: .compose, target: self, action: #selector(newConversationRequested))
        navigationItem.rightBarButtonItems = [newConversationButton, refreshButton]
''', "sidebar buttons")
text = replace_once(text, '''    @objc private func reloadConversationsFromButton() {
        diagnostics.info(category: "ui", name: "conversationList.manualRefreshRequested", fields: ["source": "button"])
        loadConversations(forceRefresh: true)
    }
''', '''    @objc private func newConversationRequested() {
        diagnostics.info(category: "navigation", name: "conversation.new.requested")
        onNewConversation?()
    }

    @objc private func reloadConversationsFromButton() {
        diagnostics.info(category: "ui", name: "conversationList.manualRefreshRequested", fields: ["source": "button"])
        loadConversations(forceRefresh: true)
    }
''', "sidebar new action")
text = replace_once(text, '''    func selectConversation(id: String) {
        requireMainThread()
        let previousID = selectedConversationID
        selectedConversationID = id
''', '''    func clearConversationSelection() {
        requireMainThread()
        guard let previousID = selectedConversationID else { return }
        selectedConversationID = nil
        diagnostics.info(category: "navigation", name: "conversation.selectionCleared", fields: ["previousConversationHash": Self.shortHash(previousID)])
    }

    func selectConversation(id: String) {
        requireMainThread()
        let previousID = selectedConversationID
        selectedConversationID = id
''', "clear selection")
text = replace_once(text, '''    func resetForAccountScopeChange() {
        presentationGeneration += 1
''', '''    func showNewConversationDraft() {
        presentationGeneration += 1
        historicalGeometryBuildGeneration += 1
        stopAnswerJumpAnimation(clearTarget: true)
        hideSyncToast()
        loadingConversationID = nil
        displayedConversationID = nil
        displayedCurrentNodeID = nil
        activityIndicator.stopAnimating()
        title = "新对话"
        clearVisibleMessagePresentation()
        resetScrollPositionToTop()
        stateLabel.text = "开始一个新对话"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        updateHeaderMetadata()
        updateConversationMenu()
    }

    func showNewConversationIdentity(id: String) {
        guard repository.selectedConversationID == id else { return }
        presentationGeneration += 1
        historicalGeometryBuildGeneration += 1
        stopAnswerJumpAnimation(clearTarget: true)
        hideSyncToast()
        loadingConversationID = nil
        displayedConversationID = id
        displayedCurrentNodeID = nil
        activityIndicator.stopAnimating()
        title = "新对话"
        clearVisibleMessagePresentation()
        displayedConversationID = id
        stateLabel.text = nil
        stateLabel.isHidden = true
        retryButton.isHidden = true
        rebuildLiveResponsePresentation(width: effectivePresentationWidth())
        tableView.reloadData()
        tableView.layoutIfNeeded()
        updateHeaderMetadata()
        updateAnswerJumpButton()
        updateConversationMenu()
    }

    func resetForAccountScopeChange() {
        presentationGeneration += 1
''', "new conversation detail presentation")
feature.write_text(text)

root = Path("ChatGPTClient/RootViewController.swift")
text = root.read_text()
text = replace_once(text, '''    case composerReady
    case sendObserved
''', '''    case composerReady
    case conversationCreated(String)
    case sendObserved
''', "event conversation created")
text = replace_once(text, '''    private struct PendingSend {
        let conversationID: String
        let text: String
        let events: (CoveredWebSendEvent) -> Void
    }
''', '''    private struct PendingSend {
        let conversationID: String?
        let text: String
        let events: (CoveredWebSendEvent) -> Void
    }
''', "pending optional identity")
text = replace_once(text, '''    private var currentConversationID: String?
    private var composerReadyConversationID: String?
    private var pendingSend: PendingSend?
''', '''    private var currentConversationID: String?
    private var composerReadyConversationID: String?
    private var rootComposerReady = false
    private var sendingNewConversation = false
    private var pendingSend: PendingSend?
''', "executor new chat state")
text = replace_once(text, '''        composerReadyConversationID = nil
        currentConversationID = conversationID
''', '''        composerReadyConversationID = nil
        rootComposerReady = false
        currentConversationID = conversationID
''', "observe clears root composer")
text = replace_once(text, '''        manualSyncFocusProbePending = false
        observingExternalResponse = false
        clientSendAccepted = false
        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
''', '''        manualSyncFocusProbePending = false
        observingExternalResponse = false
        clientSendAccepted = false
        sendingNewConversation = false
        rootComposerReady = false
        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
''', "existing send state")
existing_send_end = '''        webView.load(URLRequest(url: url))
    }

    func resetForAccountChange() {'''
new_send_block = '''        webView.load(URLRequest(url: url))
    }

    func sendNewConversation(text: String, events: @escaping (CoveredWebSendEvent) -> Void) {
        precondition(Thread.isMainThread)
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty else {
            events(.failed("invalid_input"))
            return
        }
        guard !isBusy else {
            events(.failed("executor_busy"))
            return
        }
        manualSyncFocusProbePending = false
        observingExternalResponse = false
        clientSendAccepted = false
        sendingNewConversation = true
        pendingSend = PendingSend(conversationID: nil, text: trimmed, events: events)
        activeEvents = events
        diagnostics.info(category: "webSend", name: "coveredExecutor.requested", fields: ["promptCharacters": String(trimmed.count), "target": "new_conversation"])
        if rootComposerReady, currentConversationID == nil {
            submitPendingSendIfReady()
            return
        }
        composerReadyConversationID = nil
        rootComposerReady = false
        currentConversationID = nil
        webView.load(URLRequest(url: Self.chatURL))
    }

    func resetForAccountChange() {'''
text = replace_once(text, existing_send_end, new_send_block, "new send method")
text = replace_once(text, '''        observingExternalResponse = false
        manualSyncFocusProbePending = false
        currentConversationID = nil
        composerReadyConversationID = nil
''', '''        observingExternalResponse = false
        manualSyncFocusProbePending = false
        sendingNewConversation = false
        currentConversationID = nil
        composerReadyConversationID = nil
        rootComposerReady = false
''', "reset new send state")
old_composer = '''        case "composer_state":
            let ready = (body["ready"] as? NSNumber)?.boolValue ?? false
            let pageConversationID = body["conversationID"] as? String
            guard ready, let pageConversationID, pageConversationID == currentConversationID else { return }
            composerReadyConversationID = pageConversationID
            activeEvents?(.composerReady)
            submitPendingSendIfReady()
'''
new_composer = '''        case "composer_state":
            let ready = (body["ready"] as? NSNumber)?.boolValue ?? false
            let route = body["route"] as? String ?? "other"
            let pageConversationID = body["conversationID"] as? String
            if route == "root" {
                rootComposerReady = ready
                if ready { submitPendingSendIfReady() }
                return
            }
            rootComposerReady = false
            guard ready, let pageConversationID, pageConversationID == currentConversationID else { return }
            composerReadyConversationID = pageConversationID
            activeEvents?(.composerReady)
            submitPendingSendIfReady()
'''
text = replace_once(text, old_composer, new_composer, "composer route state")
old_observed = '''        case "send_observed":
            responseActive = true
            pendingSend = nil
            activeEvents?(.sendObserved)
            diagnostics.info(category: "webSend", name: "coveredExecutor.sendObserved", fields: ["target": "existing_conversation"])
'''
new_observed = '''        case "send_observed":
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
text = replace_once(text, old_observed, new_observed, "send observed identity")
old_submit = '''    private func submitPendingSendIfReady() {
        guard let pendingSend, composerReadyConversationID == pendingSend.conversationID, currentConversationID == pendingSend.conversationID else { return }
        guard let data = try? JSONSerialization.data(withJSONObject: pendingSend.text, options: [.fragmentsAllowed]), let literal = String(data: data, encoding: .utf8) else {
            failCurrent("text_encoding_failed")
            return
        }
        self.pendingSend = nil
        let script = "window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.submit(\\(literal));"
'''
new_submit = '''    private func submitPendingSendIfReady() {
        guard let pendingSend else { return }
        let isNewConversation = pendingSend.conversationID == nil
        if isNewConversation {
            guard rootComposerReady, currentConversationID == nil else { return }
        } else {
            guard composerReadyConversationID == pendingSend.conversationID, currentConversationID == pendingSend.conversationID else { return }
        }
        guard let data = try? JSONSerialization.data(withJSONObject: pendingSend.text, options: [.fragmentsAllowed]), let literal = String(data: data, encoding: .utf8) else {
            failCurrent("text_encoding_failed")
            return
        }
        self.pendingSend = nil
        let script = "window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.submit(\\(literal), \\(isNewConversation ? \"true\" : \"false\"));"
'''
text = replace_once(text, old_submit, new_submit, "submit root/existing")
text = replace_once(text, '''        responseActive = false
        clientSendAccepted = false
        observingExternalResponse = false
        activeEvents = nil
        composerReadyConversationID = nil
''', '''        responseActive = false
        clientSendAccepted = false
        observingExternalResponse = false
        sendingNewConversation = false
        activeEvents = nil
        composerReadyConversationID = nil
        rootComposerReady = false
''', "fail clears new state")
text = replace_once(text, '''      let activeSend = false;
      let lastComposer = null;
''', '''      let activeSend = false;
      let newConversationSend = false;
      let lastComposer = null;
''', "js new send state")
text = replace_once(text, '''        if (force || composer !== lastComposer) post({ kind: 'composer_state', ready: !!composer && !activeSend, conversationID: currentConversationID() });
''', '''        if (force || composer !== lastComposer) post({ kind: 'composer_state', ready: !!composer && !activeSend, conversationID: currentConversationID(), route: pageRouteShape() });
''', "js composer route")
text = replace_once(text, '''      const submit = text => {
        const composer = probeComposer(true);
''', '''      const submit = (text, newConversation = false) => {
        const composer = probeComposer(true);
''', "js submit signature")
text = replace_once(text, '''        activeSend = true;
        probeComposer(true);
''', '''        activeSend = true;
        newConversationSend = !!newConversation;
        probeComposer(true);
''', "js submit mode")
text = replace_once(text, '''          activeSend = false;
          post({ kind: 'submit_result', state: 'submit_control_missing' });
''', '''          activeSend = false;
          newConversationSend = false;
          post({ kind: 'submit_result', state: 'submit_control_missing' });
''', "js submit failure reset")
text = replace_once(text, '''          activeSend = false;
          queueMicrotask(() => { probeComposer(true); post({ kind: 'terminal' }); });
''', '''          activeSend = false;
          newConversationSend = false;
          queueMicrotask(() => { probeComposer(true); post({ kind: 'terminal' }); });
''', "js terminal reset")
text = replace_once(text, '''        if (!isSend || !activeSend) return originalFetch(input, init);
        post({ kind: 'send_observed' });
        probeComposer(true);
''', '''        if (!isSend || !activeSend) return originalFetch(input, init);
        if (newConversationSend && !pageConversationID) {
          activeSend = false;
          newConversationSend = false;
          probeComposer(true);
          post({ kind: 'stream_error', state: 'new_conversation_identity_missing' });
          throw new Error('new_conversation_identity_missing');
        }
        post({ kind: 'send_observed', conversationID: pageConversationID, newConversation: newConversationSend });
        probeComposer(true);
''', "js send identity gate")
text = replace_once(text, '''            activeSend = false;
            probeComposer(true);
            post({ kind: 'stream_error', state: 'send_not_sse' });
''', '''            activeSend = false;
            newConversationSend = false;
            probeComposer(true);
            post({ kind: 'stream_error', state: 'send_not_sse' });
''', "js non sse reset")
text = replace_once(text, '''          activeSend = false;
          probeComposer(true);
          post({ kind: 'stream_error', state: 'send_transport_error' });
''', '''          activeSend = false;
          newConversationSend = false;
          probeComposer(true);
          post({ kind: 'stream_error', state: 'send_transport_error' });
''', "js transport reset")
text = replace_once(text, '''    case .composerReady: eventName = "composer_ready"
    case .sendObserved: eventName = "send_observed"
''', '''    case .composerReady: eventName = "composer_ready"
    case .conversationCreated: eventName = "conversation_created"
    case .sendObserved: eventName = "send_observed"
''', "repository event enum handling")
text = replace_once(text, '''    private let repository = ConversationRepository()
    private var sendExecutors: [String: CoveredWebSendExecutor] = [:]
    private var externalAcquisitionSyncs: Set<String> = []
''', '''    private let repository = ConversationRepository()
    private var sendExecutors: [String: CoveredWebSendExecutor] = [:]
    private var pendingNewConversationExecutor: CoveredWebSendExecutor?
    private var newConversationDraftActive = false
    private var newConversationIDsPendingListReconciliation = Set<String>()
    private var externalAcquisitionSyncs: Set<String> = []
''', "root new state")
text = replace_once(text, '''        repository.onLiveResponseChanged = { [weak self] id in self?.liveResponseDidChange(id: id) }
        repository.onAccountScopeReset = { [weak self] in
''', '''        repository.onLiveResponseChanged = { [weak self] id in self?.liveResponseDidChange(id: id) }
        sidebarViewController.onNewConversation = { [weak self] in self?.beginNewConversationDraft() }
        repository.onAccountScopeReset = { [weak self] in
''', "root new callback")
text = replace_once(text, '''            let executors = Array(self.sendExecutors.values)
            self.sendExecutors.removeAll()
            self.externalAcquisitionSyncs.removeAll()
            for executor in executors { executor.resetForAccountChange() }
''', '''            let executors = Array(self.sendExecutors.values)
            let pendingNewExecutor = self.pendingNewConversationExecutor
            self.sendExecutors.removeAll()
            self.pendingNewConversationExecutor = nil
            self.newConversationDraftActive = false
            self.newConversationIDsPendingListReconciliation.removeAll()
            self.externalAcquisitionSyncs.removeAll()
            for executor in executors { executor.resetForAccountChange() }
            pendingNewExecutor?.resetForAccountChange()
''', "account reset pending new")
text = replace_once(text, '''        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.releaseIdleExecutors(except: id)
''', '''        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.newConversationDraftActive = false
            self.releaseIdleExecutors(except: id)
''', "selection exits new draft")
text = replace_once(text, '''    private func configureValidationSendToolbar() {
''', '''    private func beginNewConversationDraft() {
        guard pendingNewConversationExecutor == nil else { return }
        newConversationDraftActive = true
        releaseIdleExecutors(except: "")
        repository.clearConversationSelection()
        sidebarViewController.tableView.reloadData()
        detailViewController.loadViewIfNeeded()
        detailViewController.showNewConversationDraft()
        detailNavigationController.setToolbarHidden(false, animated: false)
        diagnostics.info(category: "conversation", name: "newConversation.draftOpened")
        updateLivePresentation()
        show(.secondary)
    }

    private func configureValidationSendToolbar() {
''', "begin new draft")
old_prompt = '''    @objc private func openValidationSendPrompt() {
        guard let conversationID = repository.selectedConversationID, !repository.isLiveResponseActive(for: conversationID) else { return }
        let alert = UIAlertController(title: "Send/Stream 验证", message: "临时验证入口；最终输入框由 DEV-composer-parity 实现。", preferredStyle: .alert)
'''
new_prompt = '''    @objc private func openValidationSendPrompt() {
        let conversationID = repository.selectedConversationID
        if let conversationID {
            guard !repository.isLiveResponseActive(for: conversationID) else { return }
        } else {
            guard newConversationDraftActive, pendingNewConversationExecutor == nil else { return }
        }
        let alert = UIAlertController(title: "Send/Stream 验证", message: "临时验证入口；最终输入框由 DEV-composer-parity 实现。", preferredStyle: .alert)
'''
text = replace_once(text, old_prompt, new_prompt, "new chat prompt guard")
text = replace_once(text, '''            guard let self, let text = alert?.textFields?.first?.text else { return }
            self.startValidationSend(text: text, conversationID: conversationID)
''', '''            guard let self, let text = alert?.textFields?.first?.text else { return }
            if let conversationID { self.startValidationSend(text: text, conversationID: conversationID) }
            else { self.startNewConversationSend(text: text) }
''', "new chat prompt action")
old_executor = '''    private func executor(for conversationID: String) -> CoveredWebSendExecutor {
        if let executor = sendExecutors[conversationID] { return executor }
        let executor = CoveredWebSendExecutor()
        executor.attachCoveredWebView(to: view)
        sendExecutors[conversationID] = executor
        diagnostics.info(category: "webSend", name: "coveredExecutor.created", fields: ["activeExecutorCount": String(sendExecutors.count)])
        return executor
    }
'''
new_executor = '''    private func makeCoveredExecutor() -> CoveredWebSendExecutor {
        let executor = CoveredWebSendExecutor()
        executor.attachCoveredWebView(to: view)
        return executor
    }

    private func executor(for conversationID: String) -> CoveredWebSendExecutor {
        if let executor = sendExecutors[conversationID] { return executor }
        let executor = makeCoveredExecutor()
        sendExecutors[conversationID] = executor
        diagnostics.info(category: "webSend", name: "coveredExecutor.created", fields: ["activeExecutorCount": String(sendExecutors.count)])
        return executor
    }
'''
text = replace_once(text, old_executor, new_executor, "executor factory")
text = replace_once(text, '''    private func releaseIdleExecutors(except conversationID: String) {
        let idle = sendExecutors.filter { $0.key != conversationID && !$0.value.isBusy }
        for (id, executor) in idle { releaseExecutor(for: id, expected: executor) }
    }

    private func observeExternalResponseIfNeeded''', '''    private func releaseIdleExecutors(except conversationID: String) {
        let idle = sendExecutors.filter { $0.key != conversationID && !$0.value.isBusy }
        for (id, executor) in idle { releaseExecutor(for: id, expected: executor) }
    }

    private func releasePendingNewConversationExecutor(expected: CoveredWebSendExecutor) {
        guard pendingNewConversationExecutor === expected else { return }
        pendingNewConversationExecutor = nil
        diagnostics.info(category: "webSend", name: "coveredExecutor.pendingNewReleased")
    }

    private func observeExternalResponseIfNeeded''', "pending new release")
insert_before_existing_send = '''    private func startValidationSend(text: String, conversationID: String) {'''
new_chat_method = '''    private func startNewConversationSend(text: String) {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty, newConversationDraftActive, pendingNewConversationExecutor == nil else { return }
        let sendExecutor = makeCoveredExecutor()
        pendingNewConversationExecutor = sendExecutor
        var authoritativeConversationID: String?
        var generation: Int?
        updateLivePresentation()
        sendExecutor.sendNewConversation(text: trimmed) { [weak self, weak sendExecutor] event in
            guard let self, let sendExecutor else { return }
            switch event {
            case .conversationCreated(let conversationID):
                guard authoritativeConversationID == nil else { return }
                authoritativeConversationID = conversationID
                self.releasePendingNewConversationExecutor(expected: sendExecutor)
                guard self.sendExecutors[conversationID] == nil else {
                    self.diagnostics.error(category: "webSend", name: "newConversation.handoffFailed", fields: ["reason": "executor_identity_collision"])
                    return
                }
                self.sendExecutors[conversationID] = sendExecutor
                let shouldPresent = self.newConversationDraftActive && self.repository.selectedConversationID == nil
                if shouldPresent { self.repository.selectConversation(id: conversationID) }
                switch self.repository.beginLiveResponse(conversationID: conversationID, promptText: trimmed) {
                case .success(let value): generation = value
                case .failure(let error):
                    self.diagnostics.error(category: "webSend", name: "newConversation.handoffFailed", error: error, fields: self.repository.diagnosticsFields(for: conversationID))
                    return
                }
                self.newConversationIDsPendingListReconciliation.insert(conversationID)
                self.newConversationDraftActive = false
                if shouldPresent {
                    self.sidebarViewController.tableView.reloadData()
                    self.detailViewController.showNewConversationIdentity(id: conversationID)
                }
                var fields = self.repository.diagnosticsFields(for: conversationID)
                fields["responseGeneration"] = generation.map(String.init) ?? "none"
                fields["presented"] = shouldPresent ? "true" : "false"
                fields["source"] = "official_page_route_before_protected_send"
                self.diagnostics.info(category: "conversation", name: "newConversation.authoritativeHandoff", fields: fields)
                self.updateLivePresentation()
            case .acceptedClientWebProcessInterrupted:
                guard let conversationID = authoritativeConversationID, let generation else { return }
                self.releaseExecutor(for: conversationID, expected: sendExecutor)
                var fields = self.repository.diagnosticsFields(for: conversationID)
                fields["responseGeneration"] = String(generation)
                fields["applicationState"] = UIApplication.shared.applicationState == .active ? "active" : "inactive_or_background"
                self.diagnostics.warning(category: "webSend", name: "acceptedClientRecovery.interrupted", fields: fields)
                if UIApplication.shared.applicationState == .active { self.recoverAcceptedClientResponse(conversationID: conversationID, generation: generation, trigger: "web_process_terminated") }
            case .failed(let reason):
                if let conversationID = authoritativeConversationID, let generation {
                    self.repository.consumeLiveResponseEvent(.failed(reason), conversationID: conversationID, generation: generation)
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                } else {
                    self.releasePendingNewConversationExecutor(expected: sendExecutor)
                    self.diagnostics.warning(category: "webSend", name: "newConversation.preHandoffFailed", fields: ["reason": reason])
                    self.showValidationError("新会话发送失败，请重试。")
                }
                self.updateLivePresentation()
            default:
                guard let conversationID = authoritativeConversationID, let generation else { return }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
                if case .terminal = event {
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)
                }
            }
        }
    }

'''
text = replace_once(text, insert_before_existing_send, new_chat_method + insert_before_existing_send, "new chat root flow")
text = replace_once(text, '''            case .success(let detail):
                let cleared = self.repository.clearLiveResponseAfterAuthoritativeReconcile(conversationID: conversationID, generation: generation, authoritativeVisibleMessageCount: detail.messages.count)
                self.diagnostics.info(category: "webSend", name: "authoritativeReconcile.completed", fields: ["liveSnapshotCleared": cleared ? "true" : "false", "authoritativeVisibleMessageCount": String(detail.messages.count)])
                if self.repository.selectedConversationID == conversationID { self.detailViewController.showConversation(id: conversationID) }
''', '''            case .success(let detail):
                let cleared = self.repository.clearLiveResponseAfterAuthoritativeReconcile(conversationID: conversationID, generation: generation, authoritativeVisibleMessageCount: detail.messages.count)
                self.diagnostics.info(category: "webSend", name: "authoritativeReconcile.completed", fields: ["liveSnapshotCleared": cleared ? "true" : "false", "authoritativeVisibleMessageCount": String(detail.messages.count)])
                if self.repository.selectedConversationID == conversationID { self.detailViewController.showConversation(id: conversationID) }
                if self.newConversationIDsPendingListReconciliation.remove(conversationID) != nil {
                    self.repository.loadConversations(forceRefresh: true) { result in
                        switch result {
                        case .success(let summaries): self.diagnostics.info(category: "conversation", name: "newConversation.listReconciled", fields: ["itemCount": String(summaries.count)])
                        case .failure(let error): self.diagnostics.error(category: "conversation", name: "newConversation.listReconcileFailed", error: error)
                        }
                    }
                }
''', "new list reconciliation")
old_update = '''    private func updateLivePresentation() {
        guard let conversationID = repository.selectedConversationID else {
            validationSendButton.isEnabled = false
            detailViewController.navigationItem.rightBarButtonItem?.isEnabled = false
            return
        }
'''
new_update = '''    private func updateLivePresentation() {
        guard let conversationID = repository.selectedConversationID else {
            let newConversationReady = newConversationDraftActive && pendingNewConversationExecutor == nil
            validationSendButton.isEnabled = newConversationReady
            validationSendButton.setTitle(pendingNewConversationExecutor == nil ? "测试发送…" : "创建中…", for: .normal)
            detailViewController.navigationItem.rightBarButtonItem?.isEnabled = false
            return
        }
'''
text = replace_once(text, old_update, new_update, "new draft send button")
root.write_text(text)
