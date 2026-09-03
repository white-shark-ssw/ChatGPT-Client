from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    assert count == 1, f"{label}: expected 1 match, got {count}"
    return text.replace(old, new, 1)

root_path = Path('ChatGPTClient/RootViewController.swift')
root = root_path.read_text()

root = replace_once(root, '''        detailViewController.onManualLatestSyncApplied = { [weak self] id, _ in
            guard let self, self.repository.selectedConversationID == id else { return }
            if let snapshot = self.repository.liveResponse(for: id), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }
            self.observeExternalResponseIfNeeded(conversationID: id, forcePageReload: true)
        }
''', '''        detailViewController.onManualLatestSyncApplied = { [weak self] id, _ in
            guard let self, self.repository.selectedConversationID == id else { return }
            if let snapshot = self.repository.liveResponse(for: id), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }
            self.observeExternalResponseIfNeeded(conversationID: id, forcePageReload: true)
        }
        detailViewController.onManualReloadRequested = { [weak self] id in
            guard let self, self.repository.selectedConversationID == id else { return }
            self.externalAcquisitionSyncs.remove(id)
            let executorReleased: Bool
            if let executor = self.sendExecutors[id] {
                self.releaseExecutor(for: id, expected: executor)
                executorReleased = true
            } else {
                executorReleased = false
            }
            let liveSnapshotCleared = self.repository.resetLiveResponseForManualReload(conversationID: id)
            var fields = self.repository.diagnosticsFields(for: id)
            fields["executorReleased"] = executorReleased ? "true" : "false"
            fields["liveSnapshotCleared"] = liveSnapshotCleared ? "true" : "false"
            self.diagnostics.info(category: "conversation", name: "manualReload.hardReset", fields: fields)
            self.updateLivePresentation()
        }
        detailViewController.onManualReloadApplied = { [weak self] id in
            guard let self, self.repository.selectedConversationID == id else { return }
            self.updateLivePresentation()
            self.observeExternalResponseIfNeeded(conversationID: id)
        }
''', 'root reload callbacks')

root = replace_once(root, '''        let selectedResponseActive = snapshot?.phase.isActive ?? false
        let localResponseActive = selectedResponseActive && !(snapshot?.promptText.isEmpty ?? true)
        validationSendButton.isEnabled = !selectedResponseActive
        validationSendButton.setTitle(selectedResponseActive ? "回答中…" : "测试发送…", for: .normal)
        detailViewController.navigationItem.rightBarButtonItem?.isEnabled = !localResponseActive
''', '''        let selectedResponseActive = snapshot?.phase.isActive ?? false
        validationSendButton.isEnabled = !selectedResponseActive
        validationSendButton.setTitle(selectedResponseActive ? "回答中…" : "测试发送…", for: .normal)
        detailViewController.navigationItem.rightBarButtonItem?.isEnabled = true
''', 'root keep recovery menu reachable')

root = replace_once(root, '''    func resetAllLiveResponsesForAccountChange() {
''', '''    @discardableResult
    func resetLiveResponseForManualReload(conversationID: String) -> Bool {
        precondition(Thread.isMainThread)
        guard let snapshot = responseRuntime.snapshots.removeValue(forKey: conversationID) else { return false }
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(snapshot.generation)
        fields["phase"] = snapshot.phase.rawValue
        fields["source"] = snapshot.promptText.isEmpty ? "external_page_owned" : "local_send"
        fields["reason"] = "manual_reload"
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.reset", fields: fields)
        responseRuntime.onChange?(conversationID)
        return true
    }

    func resetAllLiveResponsesForAccountChange() {
''', 'repository per-conversation manual reset')
root_path.write_text(root)

conversation_path = Path('ChatGPTClient/Conversation/ConversationFeature.swift')
conversation = conversation_path.read_text()
conversation = replace_once(conversation, '''final class ConversationDetailViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    var onManualLatestSyncApplied: ((String, Bool) -> Void)?
''', '''final class ConversationDetailViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    var onManualLatestSyncApplied: ((String, Bool) -> Void)?
    var onManualReloadRequested: ((String) -> Void)?
    var onManualReloadApplied: ((String) -> Void)?
''', 'detail reload callbacks')
conversation = replace_once(conversation, '''        let canReload = selectedID != nil && !recoveryInProgress && !responseActive
''', '''        let canReload = selectedID != nil
''', 'reload menu always enabled')

start = conversation.index('    @objc private func reloadCurrentConversation() {')
end = conversation.index('    func scrollViewWillBeginDragging(_ scrollView: UIScrollView) {', start)
old_reload = conversation[start:end]
new_reload = '''    @objc private func reloadCurrentConversation() {
        guard let id = repository.selectedConversationID else { return }
        captureScrollAnchor(for: id)
        onManualReloadRequested?(id)
        presentationGeneration += 1
        let currentPresentationGeneration = presentationGeneration
        hideSyncToast()
        diagnostics.info(category: "navigation", name: "conversation.detailReload.requested", fields: repository.diagnosticsFields(for: id))
        loadingConversationID = id
        clearVisibleMessagePresentation()
        resetScrollPositionToTop()
        stateLabel.text = "正在重新加载会话…"
        stateLabel.isHidden = false
        retryButton.isHidden = true
        activityIndicator.startAnimating()
        repository.reloadConversation(id: id) { [weak self] result in
            guard let self, self.repository.selectedConversationID == id, self.presentationGeneration == currentPresentationGeneration else { return }
            self.loadingConversationID = nil
            self.activityIndicator.stopAnimating()
            switch result {
            case .success(let detail):
                _ = self.repository.adoptExternalAuthoritativeDetailTimeline(conversationID: id, timeline: detail.trailingResponseTimeline, reasoningDurationSeconds: detail.trailingReasoningDurationSeconds, authoritativeVisibleMessageCount: detail.messages.count, latestVisibleRole: detail.messages.last?.role)
                self.apply(detail, captureCurrentAnchor: false) { [weak self] in self?.onManualReloadApplied?(id) }
            case .failure(let error):
                guard !ConversationRepository.isLifecycleTermination(error) else { return }
                self.stateLabel.text = "读取失败\\n\\(error.localizedDescription)"
                self.stateLabel.isHidden = false
                self.retryButton.isHidden = false
            }
            self.updateConversationMenu()
        }
        updateConversationMenu()
    }

'''
assert 'guard !repository.isLiveResponseActive(for: id)' in old_reload
assert 'kind == .sync || kind == .reload' in old_reload
conversation = conversation[:start] + new_reload + conversation[end:]
conversation_path.write_text(conversation)

project_path = Path('ChatGPTClient.xcodeproj/project.pbxproj')
project = project_path.read_text()
assert project.count('CURRENT_PROJECT_VERSION = 94;') == 2
assert project.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b94";') == 2
project = project.replace('CURRENT_PROJECT_VERSION = 94;', 'CURRENT_PROJECT_VERSION = 95;')
project = project.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b94";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b95";')
project_path.write_text(project)
