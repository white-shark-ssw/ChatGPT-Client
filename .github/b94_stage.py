from pathlib import Path
import sys

ROOT = Path('ChatGPTClient/RootViewController.swift')
PBX = Path('ChatGPTClient.xcodeproj/project.pbxproj')
CHECKPOINT = Path('docs/project/current/dev/DEV-send-stream.md')


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'missing expected text: {label}')
    return text.replace(old, new, 1)


def allocate():
    text = CHECKPOINT.read_text()
    text = replace_once(
        text,
        'The next isolated evidence target is official-page rebootstrap on foreground for one active external response; b94 is not yet allocated.',
        'The next isolated evidence target is exact b94 official-page rebootstrap on foreground for one active external response; b94 is allocated only for that A/B.',
        'status allocation')
    text = replace_once(text, '## b94 exact minimum A/B — not yet allocated', '## b94 exact minimum A/B — allocated', 'b94 heading')
    text = replace_once(
        text,
        '- b93 IPA SHA-256: `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d`\n- Stable/Frozen Send: No',
        '- b93 IPA SHA-256: `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d`\n- b94 Candidate / Build: `DEV-send-stream-0.1.0-b94` / `0.1.0 (94)` permanently reserved; product/package pending at allocation checkpoint\n- Stable/Frozen Send: No',
        'identity allocation')
    text = replace_once(
        text,
        '**Closed for b93 Runtime classification. Next exact action:** perform a fresh resume/conflict guard, then allocate b94 only for foreground official-page rebootstrap of one already-active external response. Do not combine selection rebootstrap into b94 and do not modify continuation protocol.',
        '**Open for b94 foreground page-rebootstrap A/B. Next exact action:** apply only foreground rebootstrap of the selected already-active external executor, validate exact two-product-file scope + Simulator, package exact b94, then stop at Human Runtime. Selection-triggered page rebootstrap remains separate.',
        'allocation next action')
    CHECKPOINT.write_text(text)


def product():
    root = ROOT.read_text()
    anchor = '''    func reactivateExternalObservationFocus() {
        precondition(Thread.isMainThread)
        guard observingExternalResponse else { return }
        logWebViewActivationState(stage: "selection_external_focus_rearm")
        let nativeFirstResponder = webView.becomeFirstResponder()
        diagnostics.info(category: "webSend", name: "coveredExecutor.selectionFocusActivationAttempt", fields: ["nativeFirstResponder": nativeFirstResponder ? "true" : "false"])
        webView.evaluateJavaScript("document.hasFocus()") { [weak self] result, error in
            guard let self else { return }
            let documentHasFocus = (result as? Bool) == true
            self.diagnostics.info(category: "webSend", name: "coveredExecutor.selectionFocusActivationResult", fields: ["nativeFirstResponder": nativeFirstResponder ? "true" : "false", "documentHasFocus": documentHasFocus ? "true" : "false", "evaluation": error == nil ? "succeeded" : "failed"])
        }
    }
'''
    addition = anchor + '''
    func rebootstrapExternalObservationPageOnForeground() {
        precondition(Thread.isMainThread)
        guard observingExternalResponse, let conversationID = currentConversationID, !conversationID.isEmpty else { return }
        composerReadyConversationID = nil
        guard let encoded = conversationID.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed), let url = URL(string: "https://chatgpt.com/c/\\(encoded)") else { return }
        logWebViewActivationState(stage: "foreground_external_page_rebootstrap")
        webView.load(URLRequest(url: url))
        diagnostics.info(category: "webSend", name: "coveredExecutor.foregroundPageRebootstrap", fields: ["target": "existing_conversation"])
    }
'''
    root = replace_once(root, anchor, addition, 'executor foreground rebootstrap method')

    init_anchor = '''        detailViewController.onManualLatestSyncApplied = { [weak self] id, _ in
            guard let self, self.repository.selectedConversationID == id else { return }
            if let snapshot = self.repository.liveResponse(for: id), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }
            self.observeExternalResponseIfNeeded(conversationID: id, forcePageReload: true)
        }
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }
'''
    init_new = '''        detailViewController.onManualLatestSyncApplied = { [weak self] id, _ in
            guard let self, self.repository.selectedConversationID == id else { return }
            if let snapshot = self.repository.liveResponse(for: id), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }
            self.observeExternalResponseIfNeeded(conversationID: id, forcePageReload: true)
        }
        NotificationCenter.default.addObserver(self, selector: #selector(applicationWillEnterForeground(_:)), name: UIApplication.willEnterForegroundNotification, object: nil)
    }

    deinit { NotificationCenter.default.removeObserver(self, name: UIApplication.willEnterForegroundNotification, object: nil) }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }
'''
    root = replace_once(root, init_anchor, init_new, 'foreground notification registration')

    view_anchor = '''    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        preferredDisplayMode = .oneBesideSecondary
        preferredSplitBehavior = .tile
        presentsWithGesture = true
        detailNavigationController.setToolbarHidden(repository.selectedConversationID == nil, animated: false)
        updateLivePresentation()
        diagnostics.info(category: "ui", name: "nativeConversationShell.loaded")
    }
'''
    view_new = view_anchor + '''
    @objc private func applicationWillEnterForeground(_ notification: Notification) {
        guard let conversationID = repository.selectedConversationID, let snapshot = repository.liveResponse(for: conversationID), snapshot.phase.isActive, snapshot.promptText.isEmpty, let sendExecutor = sendExecutors[conversationID] else { return }
        diagnostics.info(category: "webSend", name: "foregroundExternalRebootstrap.requested", fields: repository.diagnosticsFields(for: conversationID))
        sendExecutor.rebootstrapExternalObservationPageOnForeground()
    }
'''
    root = replace_once(root, view_anchor, view_new, 'foreground handler')
    ROOT.write_text(root)

    pbx = PBX.read_text()
    if pbx.count('CURRENT_PROJECT_VERSION = 93;') != 2:
        raise SystemExit('expected exactly two build 93 settings')
    if pbx.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b93";') != 2:
        raise SystemExit('expected exactly two b93 candidate settings')
    pbx = pbx.replace('CURRENT_PROJECT_VERSION = 93;', 'CURRENT_PROJECT_VERSION = 94;')
    pbx = pbx.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b93";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b94";')
    PBX.write_text(pbx)


if len(sys.argv) != 2 or sys.argv[1] not in {'allocate', 'product'}:
    raise SystemExit('usage: b94_stage.py allocate|product')
allocate() if sys.argv[1] == 'allocate' else product()
