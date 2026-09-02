from pathlib import Path

root_path = Path("ChatGPTClient/RootViewController.swift")
root = root_path.read_text()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, got {count}")
    return text.replace(old, new, 1)


old_attach = '''        diagnostics.info(category: "webSend", name: "coveredExecutor.attached", fields: ["store": "default", "visibility": "covered"])
    }

    func observeExistingConversation'''
new_attach = '''        diagnostics.info(category: "webSend", name: "coveredExecutor.attached", fields: ["store": "default", "visibility": "covered"])
        logWebViewActivationState(stage: "attached")
    }

    private func logWebViewActivationState(stage: String) {
        let window = webView.window
        let boundsEmpty = webView.bounds.isEmpty
        let frameInWindow = window.map { webView.convert(webView.bounds, to: $0) }
        let intersectsWindow = window.map { !boundsEmpty && $0.bounds.intersects(frameInWindow ?? .zero) } ?? false
        let siblings = webView.superview?.subviews ?? []
        let subviewIndex = siblings.firstIndex(where: { $0 === webView }) ?? -1
        let visibleSiblingCountAbove: Int
        if subviewIndex >= 0 { visibleSiblingCountAbove = siblings.dropFirst(subviewIndex + 1).filter { !$0.isHidden && $0.alpha > 0.01 && !$0.bounds.isEmpty }.count }
        else { visibleSiblingCountAbove = 0 }
        diagnostics.info(category: "webSend", name: "coveredExecutor.webViewActivation", fields: ["stage": stage, "windowAttached": window == nil ? "false" : "true", "windowIsKey": window?.isKeyWindow == true ? "true" : "false", "hidden": webView.isHidden ? "true" : "false", "alphaZero": webView.alpha <= 0.01 ? "true" : "false", "boundsEmpty": boundsEmpty ? "true" : "false", "intersectsWindow": intersectsWindow ? "true" : "false", "subviewIndex": String(subviewIndex), "siblingCount": String(siblings.count), "visibleSiblingCountAbove": String(visibleSiblingCountAbove), "userInteractionEnabled": webView.isUserInteractionEnabled ? "true" : "false"])
    }

    func observeExistingConversation'''
root = replace_once(root, old_attach, new_attach, "native activation helper")

old_observe_load = '''        guard let encoded = conversationID.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed), let url = URL(string: "https://chatgpt.com/c/\\(encoded)") else { return }
        webView.load(URLRequest(url: url))
        diagnostics.info(category: "webSend", name: "coveredExecutor.observing", fields: ["target": "existing_conversation", "mode": forceReload ? "manual_sync_rearm" : "selection"])
'''
new_observe_load = '''        guard let encoded = conversationID.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed), let url = URL(string: "https://chatgpt.com/c/\\(encoded)") else { return }
        logWebViewActivationState(stage: "before_observe_load")
        webView.load(URLRequest(url: url))
        diagnostics.info(category: "webSend", name: "coveredExecutor.observing", fields: ["target": "existing_conversation", "mode": forceReload ? "manual_sync_rearm" : "selection"])
'''
root = replace_once(root, old_observe_load, new_observe_load, "observe load activation log")

old_did_finish = '''    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "webSend", name: "coveredExecutor.page", fields: ["state": "loaded", "target": currentConversationID == nil ? "root" : "existing_conversation"])
        webView.evaluateJavaScript("window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.probeComposer(true);", completionHandler: nil)
    }
'''
new_did_finish = '''    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "webSend", name: "coveredExecutor.page", fields: ["state": "loaded", "target": currentConversationID == nil ? "root" : "existing_conversation"])
        logWebViewActivationState(stage: "did_finish")
        webView.evaluateJavaScript("window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.probeComposer(true);", completionHandler: nil)
    }
'''
root = replace_once(root, old_did_finish, new_did_finish, "didFinish activation log")

old_switch = '''        switch kind {
        case "external_stream_status_request":
'''
new_switch = '''        switch kind {
        case "page_activation_state":
            guard observingExternalResponse else { return }
            let reason = Self.safeToken(body["reason"] as? String ?? "unknown")
            let visibilityState = Self.safeToken(body["visibilityState"] as? String ?? "unknown")
            let readyState = Self.safeToken(body["readyState"] as? String ?? "unknown")
            let route = Self.safeToken(body["route"] as? String ?? "unknown")
            let hidden = (body["hidden"] as? NSNumber)?.boolValue ?? false
            let hasFocus = (body["hasFocus"] as? NSNumber)?.boolValue ?? false
            diagnostics.info(category: "webSend", name: "coveredExecutor.pageActivation", fields: ["reason": reason, "visibilityState": visibilityState, "hidden": hidden ? "true" : "false", "hasFocus": hasFocus ? "true" : "false", "readyState": readyState, "route": route])
        case "external_stream_status_request":
'''
root = replace_once(root, old_switch, new_switch, "Swift page activation handler")

old_js_anchor = '''      const currentConversationID = () => {
        const match = location.pathname.match(/^\\/c\\/([^/?#]+)/);
        return match ? decodeURIComponent(match[1]) : null;
      };
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');
'''
new_js_anchor = '''      const currentConversationID = () => {
        const match = location.pathname.match(/^\\/c\\/([^/?#]+)/);
        return match ? decodeURIComponent(match[1]) : null;
      };
      const pageRouteShape = () => currentConversationID() ? 'conversation' : location.pathname === '/' ? 'root' : 'other';
      const reportPageActivation = reason => {
        const visibilityState = ['visible', 'hidden', 'prerender'].includes(document.visibilityState) ? document.visibilityState : 'other';
        const readyState = ['loading', 'interactive', 'complete'].includes(document.readyState) ? document.readyState : 'other';
        post({ kind: 'page_activation_state', reason, visibilityState, hidden: !!document.hidden, hasFocus: typeof document.hasFocus === 'function' ? document.hasFocus() : false, readyState, route: pageRouteShape() });
      };
      document.addEventListener('readystatechange', () => reportPageActivation('readystatechange'));
      document.addEventListener('visibilitychange', () => reportPageActivation('visibilitychange'));
      window.addEventListener('focus', () => reportPageActivation('focus'));
      window.addEventListener('blur', () => reportPageActivation('blur'));
      window.addEventListener('pageshow', () => reportPageActivation('pageshow'));
      window.addEventListener('pagehide', () => reportPageActivation('pagehide'));
      window.addEventListener('popstate', () => reportPageActivation('popstate'));
      reportPageActivation('initial');
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');
'''
root = replace_once(root, old_js_anchor, new_js_anchor, "JS page activation reporter")

root_path.write_text(root)

project_path = Path("ChatGPTClient.xcodeproj/project.pbxproj")
project = project_path.read_text()
if project.count("CURRENT_PROJECT_VERSION = 86;") != 2:
    raise SystemExit(f"build number: expected 2 b86 matches, got {project.count('CURRENT_PROJECT_VERSION = 86;')}")
if project.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b86";') != 2:
    raise SystemExit(f"candidate: expected 2 b86 matches, got {project.count('DIAGNOSTICS_CANDIDATE = \"DEV-send-stream-0.1.0-b86\";')}")
project = project.replace("CURRENT_PROJECT_VERSION = 86;", "CURRENT_PROJECT_VERSION = 87;")
project = project.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b86";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b87";')
project_path.write_text(project)

print("b87 guarded activation diagnostics patch applied")
