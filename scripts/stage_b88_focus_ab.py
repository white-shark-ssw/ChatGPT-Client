from pathlib import Path

root = Path('.')
root_vc = root / 'ChatGPTClient/RootViewController.swift'
pbx = root / 'ChatGPTClient.xcodeproj/project.pbxproj'
workflow = root / '.github/workflows/ios-foundation.yml'

text = root_vc.read_text()

old = '''    private var responseActive = false
    private var observingExternalResponse = false

    var isBusy: Bool { activeEvents != nil }
'''
new = '''    private var responseActive = false
    private var observingExternalResponse = false
    private var manualSyncFocusProbePending = false

    var isBusy: Bool { activeEvents != nil }
'''
assert text.count(old) == 1, 'focus probe state anchor mismatch'
text = text.replace(old, new, 1)

old = '''        observationEvents = events
        observingExternalResponse = true
        if currentConversationID == conversationID, !forceReload {
'''
new = '''        observationEvents = events
        observingExternalResponse = true
        manualSyncFocusProbePending = forceReload
        if currentConversationID == conversationID, !forceReload {
'''
assert text.count(old) == 1, 'observe focus arm anchor mismatch'
text = text.replace(old, new, 1)

old = '''        guard !isBusy else {
            events(.failed("executor_busy"))
            return
        }
        observingExternalResponse = false
        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
'''
new = '''        guard !isBusy else {
            events(.failed("executor_busy"))
            return
        }
        manualSyncFocusProbePending = false
        observingExternalResponse = false
        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
'''
assert text.count(old) == 1, 'local send focus clear anchor mismatch'
text = text.replace(old, new, 1)

old = '''        responseActive = false
        observingExternalResponse = false
        currentConversationID = nil
'''
new = '''        responseActive = false
        observingExternalResponse = false
        manualSyncFocusProbePending = false
        currentConversationID = nil
'''
assert text.count(old) == 1, 'account reset focus clear anchor mismatch'
text = text.replace(old, new, 1)

old = '''    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "webSend", name: "coveredExecutor.page", fields: ["state": "loaded", "target": currentConversationID == nil ? "root" : "existing_conversation"])
        logWebViewActivationState(stage: "did_finish")
        webView.evaluateJavaScript("window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.probeComposer(true);", completionHandler: nil)
    }
'''
new = '''    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "webSend", name: "coveredExecutor.page", fields: ["state": "loaded", "target": currentConversationID == nil ? "root" : "existing_conversation"])
        logWebViewActivationState(stage: "did_finish")
        if observingExternalResponse, manualSyncFocusProbePending {
            manualSyncFocusProbePending = false
            let nativeFirstResponder = webView.becomeFirstResponder()
            diagnostics.info(category: "webSend", name: "coveredExecutor.focusActivationAttempt", fields: ["mode": "manual_sync_rearm", "nativeFirstResponder": nativeFirstResponder ? "true" : "false"])
            webView.evaluateJavaScript("document.hasFocus()") { [weak self] result, error in
                guard let self else { return }
                let documentHasFocus = (result as? Bool) == true
                self.diagnostics.info(category: "webSend", name: "coveredExecutor.focusActivationResult", fields: ["mode": "manual_sync_rearm", "nativeFirstResponder": nativeFirstResponder ? "true" : "false", "documentHasFocus": documentHasFocus ? "true" : "false", "evaluation": error == nil ? "succeeded" : "failed"])
            }
        }
        webView.evaluateJavaScript("window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.probeComposer(true);", completionHandler: nil)
    }
'''
assert text.count(old) == 1, 'didFinish focus activation anchor mismatch'
text = text.replace(old, new, 1)

old = '''    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        diagnostics.error(category: "webSend", name: "coveredExecutor.webProcess", fields: ["state": "terminated"])
        failCurrent("web_process_terminated")
    }
'''
new = '''    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        manualSyncFocusProbePending = false
        diagnostics.error(category: "webSend", name: "coveredExecutor.webProcess", fields: ["state": "terminated"])
        failCurrent("web_process_terminated")
    }
'''
assert text.count(old) == 1, 'web process focus clear anchor mismatch'
text = text.replace(old, new, 1)

old = '''    private func navigationFailed(_ error: Error) {
        let nsError = error as NSError
'''
new = '''    private func navigationFailed(_ error: Error) {
        manualSyncFocusProbePending = false
        let nsError = error as NSError
'''
assert text.count(old) == 1, 'navigation focus clear anchor mismatch'
text = text.replace(old, new, 1)

root_vc.write_text(text)

text = pbx.read_text()
assert text.count('CURRENT_PROJECT_VERSION = 87;') == 2, 'expected two build 87 settings'
assert text.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b87";') == 2, 'expected two b87 candidate settings'
text = text.replace('CURRENT_PROJECT_VERSION = 87;', 'CURRENT_PROJECT_VERSION = 88;')
text = text.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b87";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b88";')
pbx.write_text(text)

text = workflow.read_text()
assert text.count('# Candidate: DEV-send-stream-0.1.0-b87') == 1, 'workflow candidate anchor mismatch'
assert text.count('name: iOS Send Page Activation Diagnostics b87') == 1, 'workflow name anchor mismatch'
assert text.count('name: ChatGPTClient-DEV-send-stream-0.1.0-b87') == 1, 'workflow artifact anchor mismatch'
text = text.replace('# Candidate: DEV-send-stream-0.1.0-b87', '# Candidate: DEV-send-stream-0.1.0-b88', 1)
text = text.replace('# Product source: 6f98816f37c749c8d4cb8dfef4c4645df2c0f27a', '# Product scope: focus-only causal A/B after visible-Web Runtime evidence', 1)
text = text.replace('name: iOS Send Page Activation Diagnostics b87', 'name: iOS Send Focus Activation A-B b88', 1)
text = text.replace('name: ChatGPTClient-DEV-send-stream-0.1.0-b87', 'name: ChatGPTClient-DEV-send-stream-0.1.0-b88', 1)
workflow.write_text(text)

assert 'manualSyncFocusProbePending = forceReload' in root_vc.read_text()
assert 'coveredExecutor.focusActivationAttempt' in root_vc.read_text()
assert 'coveredExecutor.focusActivationResult' in root_vc.read_text()
assert root_vc.read_text().count('webView.isUserInteractionEnabled = false') == 1
assert 'CURRENT_PROJECT_VERSION = 87;' not in pbx.read_text()
assert pbx.read_text().count('CURRENT_PROJECT_VERSION = 88;') == 2
assert pbx.read_text().count('DEV-send-stream-0.1.0-b88') == 2
assert 'DEV-send-stream-0.1.0-b87' not in workflow.read_text()
