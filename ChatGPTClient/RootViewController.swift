import ObjectiveC
import UIKit
import WebKit

private final class WeakCoveredWebSendMessageHandler: NSObject, WKScriptMessageHandler {
    weak var target: WKScriptMessageHandler?
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) { target?.userContentController(userContentController, didReceive: message) }
}

enum CoveredWebSendEvent {
    case externalResumeObserved
    case externalStreamingObserved
    case externalAcquisitionHint
    case externalConversationSnapshot(messages: [[String: Any]], complete: Bool)
    case composerReady
    case sendObserved
    case responseAccepted
    case thinkingActive
    case reasoningPreamble(String, segmentStart: Bool)
    case reasoningDelta(String)
    case reasoningEnded(Int?)
    case finalDelta(String)
    case toolActivity(slot: Int, title: String, completed: Bool, inputJSON: String, outputJSON: String, iconKind: ConversationToolIconKind)
    case terminal
    case failed(String)
}

final class CoveredWebSendExecutor: NSObject, WKNavigationDelegate, WKScriptMessageHandler {
    private static let handlerName = "coveredWebSendExecutor"
    private static let chatURL = URL(string: "https://chatgpt.com/")!

    private struct PendingSend {
        let conversationID: String
        let text: String
        let events: (CoveredWebSendEvent) -> Void
    }

    private let diagnostics = DiagnosticsLogger.shared
    private let scriptHandler: WeakCoveredWebSendMessageHandler
    private let webView: WKWebView
    private var currentConversationID: String?
    private var composerReadyConversationID: String?
    private var pendingSend: PendingSend?
    private var observationEvents: ((CoveredWebSendEvent) -> Void)?
    private var activeEvents: ((CoveredWebSendEvent) -> Void)?
    private var responseActive = false
    private var observingExternalResponse = false

    var isBusy: Bool { activeEvents != nil }

    override init() {
        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .default()
        let handler = WeakCoveredWebSendMessageHandler()
        configuration.userContentController.add(handler, name: Self.handlerName)
        configuration.userContentController.addUserScript(WKUserScript(source: Self.bridgeScript, injectionTime: .atDocumentStart, forMainFrameOnly: true))
        scriptHandler = handler
        webView = WKWebView(frame: .zero, configuration: configuration)
        super.init()
        handler.target = self
        webView.navigationDelegate = self
        webView.isUserInteractionEnabled = false
        webView.scrollView.isScrollEnabled = false
        webView.load(URLRequest(url: Self.chatURL))
    }

    deinit {
        webView.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName)
        webView.removeFromSuperview()
    }

    func attachCoveredWebView(to hostView: UIView) {
        precondition(Thread.isMainThread)
        guard webView.superview !== hostView else { return }
        webView.removeFromSuperview()
        webView.translatesAutoresizingMaskIntoConstraints = false
        hostView.insertSubview(webView, at: 0)
        NSLayoutConstraint.activate([
            webView.leadingAnchor.constraint(equalTo: hostView.leadingAnchor),
            webView.trailingAnchor.constraint(equalTo: hostView.trailingAnchor),
            webView.topAnchor.constraint(equalTo: hostView.topAnchor),
            webView.bottomAnchor.constraint(equalTo: hostView.bottomAnchor)
        ])
        diagnostics.info(category: "webSend", name: "coveredExecutor.attached", fields: ["store": "default", "visibility": "covered"])
    }

    func observeExistingConversation(conversationID: String, forceReload: Bool = false, events: @escaping (CoveredWebSendEvent) -> Void) {
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
        guard let encoded = conversationID.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed), let url = URL(string: "https://chatgpt.com/c/\(encoded)") else { return }
        webView.load(URLRequest(url: url))
        diagnostics.info(category: "webSend", name: "coveredExecutor.observing", fields: ["target": "existing_conversation", "mode": forceReload ? "manual_sync_rearm" : "selection"])
    }

    func sendExistingConversation(text: String, conversationID: String, events: @escaping (CoveredWebSendEvent) -> Void) {
        precondition(Thread.isMainThread)
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty, !conversationID.isEmpty else {
            events(.failed("invalid_input"))
            return
        }
        guard !isBusy else {
            events(.failed("executor_busy"))
            return
        }
        observingExternalResponse = false
        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
        activeEvents = events
        diagnostics.info(category: "webSend", name: "coveredExecutor.requested", fields: ["promptCharacters": String(trimmed.count), "target": "existing_conversation"])
        if composerReadyConversationID == conversationID, currentConversationID == conversationID {
            submitPendingSendIfReady()
            return
        }
        composerReadyConversationID = nil
        currentConversationID = conversationID
        guard let encoded = conversationID.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed), let url = URL(string: "https://chatgpt.com/c/\(encoded)") else {
            failCurrent("invalid_conversation_url")
            return
        }
        webView.load(URLRequest(url: url))
    }

    func resetForAccountChange() {
        precondition(Thread.isMainThread)
        let events = activeEvents ?? pendingSend?.events
        pendingSend = nil
        observationEvents = nil
        activeEvents = nil
        responseActive = false
        observingExternalResponse = false
        currentConversationID = nil
        composerReadyConversationID = nil
        events?(.failed("account_changed"))
        webView.load(URLRequest(url: Self.chatURL))
        diagnostics.info(category: "webSend", name: "coveredExecutor.reset", fields: ["reason": "account_changed"])
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "webSend", name: "coveredExecutor.page", fields: ["state": "loaded", "target": currentConversationID == nil ? "root" : "existing_conversation"])
        webView.evaluateJavaScript("window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.probeComposer(true);", completionHandler: nil)
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) { navigationFailed(error) }
    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) { navigationFailed(error) }

    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        diagnostics.error(category: "webSend", name: "coveredExecutor.webProcess", fields: ["state": "terminated"])
        failCurrent("web_process_terminated")
    }

    private func navigationFailed(_ error: Error) {
        let nsError = error as NSError
        diagnostics.warning(category: "webSend", name: "coveredExecutor.page", fields: ["state": "failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
        failCurrent("navigation_failed")
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        guard message.name == Self.handlerName, let body = message.body as? [String: Any], let kind = body["kind"] as? String else { return }
        switch kind {
        case "external_stream_status_request":
            guard observingExternalResponse else { return }
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalStreamStatusRequest", fields: ["target": "existing_conversation"])
        case "external_stream_status_response":
            guard observingExternalResponse else { return }
            let status = (body["status"] as? NSNumber)?.intValue ?? 0
            let streamState = Self.safeToken(body["streamState"] as? String ?? "")
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalStreamStatusResponse", fields: ["httpStatus": String(status), "streamState": streamState])
        case "external_resume_request":
            guard observingExternalResponse else { return }
            let hasOffset = (body["hasOffset"] as? NSNumber)?.boolValue ?? false
            let offsetType = Self.safeToken(body["offsetType"] as? String ?? "missing")
            let offsetValue = (body["offsetValue"] as? NSNumber)?.intValue ?? -1
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalResumeRequest", fields: ["hasOffset": hasOffset ? "true" : "false", "offsetType": offsetType, "offsetValue": String(offsetValue)])
        case "external_resume_observed":
            guard observingExternalResponse else { return }
            observationEvents?(.externalResumeObserved)
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalResumeObserved", fields: ["target": "existing_conversation"])
        case "external_streaming":
            guard observingExternalResponse else { return }
            if activeEvents == nil { activeEvents = observationEvents }
            activeEvents?(.externalStreamingObserved)
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalStreamingObserved", fields: ["target": "existing_conversation"])
        case "external_snapshot":
            guard observingExternalResponse, let messages = body["messages"] as? [[String: Any]] else { return }
            if activeEvents == nil { activeEvents = observationEvents }
            let complete = (body["complete"] as? NSNumber)?.boolValue ?? false
            activeEvents?(.externalConversationSnapshot(messages: messages, complete: complete))
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalSnapshot", fields: ["serviceMessageCount": String(messages.count), "complete": complete ? "true" : "false"])
        case "external_dom_structure":
            guard observingExternalResponse else { return }
            let assistantNodeCount = (body["assistantNodeCount"] as? NSNumber)?.intValue ?? 0
            let textCharacters = (body["textCharacters"] as? NSNumber)?.intValue ?? 0
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalDOMStructure", fields: ["assistantNodeCount": String(assistantNodeCount), "textCharacters": String(textCharacters)])
        case "websocket_structure":
            guard observingExternalResponse else { return }
            let state = Self.safeToken(body["state"] as? String ?? "unknown")
            let host = Self.safeToken(body["host"] as? String ?? "")
            let path = Self.safeToken(body["path"] as? String ?? "")
            let dataType = Self.safeToken(body["dataType"] as? String ?? "none")
            let topKeys = Self.safeToken(body["topKeys"] as? String ?? "")
            let nestedKeys = Self.safeToken(body["nestedKeys"] as? String ?? "")
            let typeToken = Self.safeToken(body["typeToken"] as? String ?? "")
            let eventToken = Self.safeToken(body["eventToken"] as? String ?? "")
            let kindToken = Self.safeToken(body["kindToken"] as? String ?? "")
            let actionToken = Self.safeToken(body["actionToken"] as? String ?? "")
            let topicToken = Self.safeToken(body["topicToken"] as? String ?? "")
            let nameToken = Self.safeToken(body["nameToken"] as? String ?? "")
            let length = (body["length"] as? NSNumber)?.intValue ?? 0
            let hasConversationKey = (body["hasConversationKey"] as? NSNumber)?.boolValue ?? false
            let targetMatch = (body["targetMatch"] as? NSNumber)?.boolValue ?? false
            diagnostics.info(category: "webSend", name: "coveredExecutor.webSocketStructure", fields: ["state": state, "host": host, "path": path, "dataType": dataType, "length": String(length), "topKeys": topKeys, "nestedKeys": nestedKeys, "typeToken": typeToken, "eventToken": eventToken, "kindToken": kindToken, "actionToken": actionToken, "topicToken": topicToken, "nameToken": nameToken, "hasConversationKey": hasConversationKey ? "true" : "false", "targetMatch": targetMatch ? "true" : "false"])
            if state == "message", targetMatch, activeEvents == nil {
                observationEvents?(.externalAcquisitionHint)
                diagnostics.info(category: "webSend", name: "coveredExecutor.externalAcquisitionHint", fields: ["source": "websocket_target_match", "target": "existing_conversation"])
            }
        case "resume_response":
            let status = (body["status"] as? NSNumber)?.intValue ?? 0
            let contentType = body["contentType"] as? String ?? ""
            diagnostics.info(category: "webSend", name: "coveredExecutor.resumeResponse", fields: ["httpStatus": String(status), "contentType": Self.safeToken(contentType)])
            if status == 200 && contentType == "text/event-stream" {
                if activeEvents == nil, observingExternalResponse { activeEvents = observationEvents }
                responseActive = true
                activeEvents?(.responseAccepted)
            } else if activeEvents != nil, !observingExternalResponse {
                failCurrent("resume_not_sse")
            } else if observingExternalResponse {
                diagnostics.info(category: "webSend", name: "coveredExecutor.resumeFallback", fields: ["state": "page_owned_read_path", "httpStatus": String(status)])
            }
        case "composer_state":
            let ready = (body["ready"] as? NSNumber)?.boolValue ?? false
            let pageConversationID = body["conversationID"] as? String
            guard ready, let pageConversationID, pageConversationID == currentConversationID else { return }
            composerReadyConversationID = pageConversationID
            activeEvents?(.composerReady)
            submitPendingSendIfReady()
        case "submit_result":
            let state = body["state"] as? String ?? "unknown"
            diagnostics.info(category: "webSend", name: "coveredExecutor.submitResult", fields: ["state": Self.safeToken(state)])
            if state != "submitted" { failCurrent(state) }
        case "send_observed":
            responseActive = true
            pendingSend = nil
            activeEvents?(.sendObserved)
            diagnostics.info(category: "webSend", name: "coveredExecutor.sendObserved", fields: ["target": "existing_conversation"])
        case "send_response":
            let status = (body["status"] as? NSNumber)?.intValue ?? 0
            let contentType = body["contentType"] as? String ?? ""
            diagnostics.info(category: "webSend", name: "coveredExecutor.sendResponse", fields: ["httpStatus": String(status), "contentType": Self.safeToken(contentType)])
            if status == 200 && contentType == "text/event-stream" { activeEvents?(.responseAccepted) }
            else { failCurrent("send_not_sse") }
        case "thinking_active": activeEvents?(.thinkingActive)
        case "reasoning_preamble":
            guard let text = body["text"] as? String, !text.isEmpty else { return }
            activeEvents?(.reasoningPreamble(text, segmentStart: (body["segmentStart"] as? NSNumber)?.boolValue ?? false))
        case "reasoning_delta":
            guard let text = body["text"] as? String, !text.isEmpty else { return }
            activeEvents?(.reasoningDelta(text))
        case "reasoning_ended": activeEvents?(.reasoningEnded((body["durationSec"] as? NSNumber)?.intValue))
        case "final_delta":
            guard let text = body["text"] as? String, !text.isEmpty else { return }
            activeEvents?(.finalDelta(text))
        case "tool_activity":
            let slot = (body["slot"] as? NSNumber)?.intValue ?? -1
            guard slot >= 0 else { return }
            let title = (body["title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
            let inputJSON = body["detailInput"] as? String ?? ""
            let outputJSON = body["detailOutput"] as? String ?? ""
            let iconKind = ConversationToolIconKind(rawValue: body["iconKind"] as? String ?? "") ?? .generic
            activeEvents?(.toolActivity(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: (body["completed"] as? NSNumber)?.boolValue ?? false, inputJSON: inputJSON, outputJSON: outputJSON, iconKind: iconKind))
        case "terminal":
            let terminalEvents = activeEvents
            responseActive = false
            pendingSend = nil
            activeEvents = nil
            composerReadyConversationID = nil
            terminalEvents?(.terminal)
            diagnostics.info(category: "webSend", name: "coveredExecutor.terminal", fields: ["terminal": "true"])
            webView.evaluateJavaScript("window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.probeComposer(true);", completionHandler: nil)
        case "stream_error": failCurrent(body["state"] as? String ?? "stream_error")
        default: break
        }
    }

    private func submitPendingSendIfReady() {
        guard let pendingSend, composerReadyConversationID == pendingSend.conversationID, currentConversationID == pendingSend.conversationID else { return }
        guard let data = try? JSONSerialization.data(withJSONObject: pendingSend.text, options: [.fragmentsAllowed]), let literal = String(data: data, encoding: .utf8) else {
            failCurrent("text_encoding_failed")
            return
        }
        self.pendingSend = nil
        let script = "window.__coveredWebSendExecutor && window.__coveredWebSendExecutor.submit(\(literal));"
        webView.evaluateJavaScript(script) { [weak self] _, error in
            guard let self else { return }
            self.webView.endEditing(true)
            guard let error else { return }
            let nsError = error as NSError
            self.diagnostics.warning(category: "webSend", name: "coveredExecutor.bridge", fields: ["state": "evaluate_failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
            self.failCurrent("bridge_failed")
        }
    }

    private func failCurrent(_ reason: String) {
        let events = activeEvents ?? pendingSend?.events
        pendingSend = nil
        responseActive = false
        observingExternalResponse = false
        activeEvents = nil
        composerReadyConversationID = nil
        diagnostics.warning(category: "webSend", name: "coveredExecutor.failed", fields: ["reason": Self.safeToken(reason)])
        events?(.failed(reason))
    }

    private static let safeTokenCharacters = CharacterSet(charactersIn: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_./:{}-+,")
    private static func safeToken(_ value: String) -> String { value.count <= 160 && value.unicodeScalars.allSatisfy { safeTokenCharacters.contains($0) } ? value : "redacted" }

    private static let bridgeScript = #"""
    (() => {
      if (window.__coveredWebSendExecutorInstalled) return;
      window.__coveredWebSendExecutorInstalled = true;
      const bridge = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.coveredWebSendExecutor;
      if (!bridge) return;
      const post = value => { try { bridge.postMessage(value); } catch (_) {} };
      const originalFetch = window.fetch.bind(window);
      const encoder = new TextEncoder();
      const decoder = new TextDecoder();
      let activeSend = false;
      let lastComposer = null;
      const externalStreamingState = { active: false, completePending: false, resumeSSE: false };
      let lastExternalAssistantTextCharacters = -1;
      const reportExternalAssistantDOM = () => {
        if (!externalStreamingState.active && !externalStreamingState.completePending) return;
        const nodes = document.querySelectorAll('[data-message-author-role="assistant"]');
        if (!nodes.length) return;
        const latest = nodes[nodes.length - 1];
        const textCharacters = String(latest.textContent || '').length;
        if (textCharacters === lastExternalAssistantTextCharacters) return;
        lastExternalAssistantTextCharacters = textCharacters;
        post({ kind: 'external_dom_structure', assistantNodeCount: nodes.length, textCharacters });
      };
      new MutationObserver(reportExternalAssistantDOM).observe(document.documentElement, { subtree: true, childList: true, characterData: true });

      const currentConversationID = () => {
        const match = location.pathname.match(/^\/c\/([^/?#]+)/);
        return match ? decodeURIComponent(match[1]) : null;
      };
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');
      const safeStructureToken = value => typeof value === 'string' && value.length <= 64 && /^[A-Za-z][A-Za-z0-9_.:/-]{0,63}$/.test(value) ? value : '';
      const scrubSocketPath = value => String(value || '').split('/').map(segment => /^[A-Za-z0-9_-]{20,}$/.test(segment) ? '{id}' : segment).join('/').slice(0, 150);
      const containsExactTarget = value => {
        const target = currentConversationID();
        if (!target) return false;
        const visit = (node, depth) => {
          if (depth > 5) return false;
          if (typeof node === 'string') return node === target;
          if (Array.isArray(node)) return node.slice(0, 40).some(item => visit(item, depth + 1));
          if (!node || typeof node !== 'object') return false;
          return Object.values(node).slice(0, 40).some(item => visit(item, depth + 1));
        };
        return visit(value, 0);
      };
      const socketFrameShape = data => {
        let dataType = typeof data;
        let length = 0;
        let parsed = null;
        if (typeof data === 'string') {
          dataType = 'string';
          length = data.length;
          if (length <= 65536) { try { parsed = JSON.parse(data); } catch (_) {} }
        } else if (data instanceof ArrayBuffer) {
          dataType = 'arraybuffer';
          length = data.byteLength;
        } else if (ArrayBuffer.isView(data)) {
          dataType = 'typed_array';
          length = data.byteLength;
        } else if (typeof Blob !== 'undefined' && data instanceof Blob) {
          dataType = 'blob';
          length = data.size;
        }
        if (!parsed || typeof parsed !== 'object') return { dataType, length, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false };
        const topKeysArray = Array.isArray(parsed) ? [] : Object.keys(parsed).sort().slice(0, 24);
        const nested = [];
        if (!Array.isArray(parsed)) {
          for (const key of ['payload', 'data', 'body', 'message', 'detail']) {
            const value = parsed[key];
            if (value && typeof value === 'object' && !Array.isArray(value)) nested.push(...Object.keys(value));
          }
        }
        const nestedKeysArray = [...new Set(nested)].sort().slice(0, 24);
        const hasConversationKey = [...topKeysArray, ...nestedKeysArray].some(key => key === 'conversation_id' || key === 'conversationId' || key === 'conversation');
        const token = key => !Array.isArray(parsed) ? safeStructureToken(parsed[key]) : '';
        return { dataType: Array.isArray(parsed) ? 'json_array' : 'json_object', length, topKeys: topKeysArray.join(',').slice(0, 150), nestedKeys: nestedKeysArray.join(',').slice(0, 150), typeToken: token('type'), eventToken: token('event'), kindToken: token('kind'), actionToken: token('action'), topicToken: token('topic'), nameToken: token('name'), hasConversationKey, targetMatch: containsExactTarget(parsed) };
      };
      const NativeWebSocket = window.WebSocket;
      if (NativeWebSocket) {
        let structuralMessageBudget = 200;
        window.WebSocket = new Proxy(NativeWebSocket, {
          construct(target, args) {
            const socket = Reflect.construct(target, args, target);
            let parsedURL = null;
            try { parsedURL = new URL(String(args[0] || ''), location.href); } catch (_) {}
            const host = parsedURL ? parsedURL.hostname.toLowerCase() : '';
            const path = parsedURL ? scrubSocketPath(parsedURL.pathname) : '';
            const interesting = host === 'ws.chatgpt.com' || isChatGPTHost(host);
            if (interesting) post({ kind: 'websocket_structure', state: 'created', host, path, dataType: 'none', length: 0, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false });
            if (interesting) socket.addEventListener('open', () => post({ kind: 'websocket_structure', state: 'open', host, path, dataType: 'none', length: 0, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false }));
            if (interesting) socket.addEventListener('message', event => {
              if (structuralMessageBudget <= 0) return;
              structuralMessageBudget -= 1;
              const shape = socketFrameShape(event.data);
              post({ kind: 'websocket_structure', state: 'message', host, path, ...shape });
            });
            if (interesting) socket.addEventListener('close', event => post({ kind: 'websocket_structure', state: 'close', host, path, dataType: 'none', length: Number(event.code) || 0, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false }));
            if (interesting) socket.addEventListener('error', () => post({ kind: 'websocket_structure', state: 'error', host, path, dataType: 'none', length: 0, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false }));
            return socket;
          }
        });
      }
      const installRenderSuppression = () => {
        if (document.getElementById('__covered_web_send_render_suppression')) return;
        const style = document.createElement('style');
        style.id = '__covered_web_send_render_suppression';
        style.textContent = '[data-message-author-role="user"],[data-message-author-role="assistant"]{display:none!important;}';
        (document.head || document.documentElement || document).appendChild(style);
      };
      const findComposer = () => {
        const byID = document.querySelector('#prompt-textarea');
        if (byID) return byID;
        return document.querySelector('[contenteditable="true"][role="textbox"]');
      };
      const probeComposer = (force = false) => {
        installRenderSuppression();
        const composer = findComposer();
        if (force || composer !== lastComposer) post({ kind: 'composer_state', ready: !!composer && !activeSend, conversationID: currentConversationID() });
        lastComposer = composer || null;
        return composer;
      };
      const setComposerText = (element, text) => {
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
      const submit = text => {
        const composer = probeComposer(true);
        if (!composer || typeof text !== 'string' || !text.trim()) { post({ kind: 'submit_result', state: 'composer_not_ready' }); return; }
        if (!setComposerText(composer, text)) { post({ kind: 'submit_result', state: 'input_state_failed' }); return; }
        activeSend = true;
        probeComposer(true);
        queueMicrotask(() => {
          const form = composer.closest('form');
          const submitButton = form && form.querySelector('button[type="submit"]:not([disabled])');
          if (form && typeof form.requestSubmit === 'function') {
            try { submitButton ? form.requestSubmit(submitButton) : form.requestSubmit(); post({ kind: 'submit_result', state: 'submitted' }); return; } catch (_) {}
          }
          const sendButton = document.querySelector('button[data-testid="send-button"]:not([disabled])');
          if (sendButton) { sendButton.click(); post({ kind: 'submit_result', state: 'submitted' }); return; }
          activeSend = false;
          post({ kind: 'submit_result', state: 'submit_control_missing' });
          probeComposer(true);
        });
      };
      const findMessage = (node, depth = 0) => {
        if (!node || typeof node !== 'object' || depth > 5) return null;
        if (!Array.isArray(node) && node.message && typeof node.message === 'object') return node.message;
        if (!Array.isArray(node) && node.author && node.content && typeof node.author === 'object' && typeof node.content === 'object') return node;
        const children = Array.isArray(node) ? node : Object.values(node);
        for (const child of children) { const message = findMessage(child, depth + 1); if (message) return message; }
        return null;
      };
      const postTextDelta = (text, state) => {
        if (!text) return;
        post({ kind: state.reasoningEnded ? 'final_delta' : 'reasoning_delta', text });
      };
      const observeReasoningActive = (payload, state) => {
        if (state.reasoningEnded) return;
        const message = findMessage(payload);
        if (!message || !message.author || message.author.role !== 'assistant' || message.status !== 'finished_successfully' || message.recipient !== 'all' || typeof message.id !== 'string' || !message.id || state.reasoningActiveSeen.has(message.id)) return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        if (!content || content.content_type !== 'thoughts' || !metadata || metadata.reasoning_status !== 'is_reasoning') return;
        state.reasoningActiveSeen.add(message.id);
        post({ kind: 'thinking_active' });
      };
      const observeReasoningPreamble = (payload, state) => {
        if (state.reasoningEnded) return;
        const message = findMessage(payload);
        if (!message || !message.author || message.author.role !== 'assistant' || message.status !== 'in_progress' || message.recipient !== 'all' || typeof message.id !== 'string' || !message.id || state.reasoningPreambleSeen.has(message.id)) return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        if (!content || content.content_type !== 'text' || !metadata || metadata.is_thinking_preamble_message !== true || !Array.isArray(content.parts) || content.parts.length !== 1 || typeof content.parts[0] !== 'string' || !content.parts[0]) return;
        const segmentStart = state.reasoningPreambleCount > 0;
        state.reasoningPreambleSeen.add(message.id);
        state.reasoningPreambleCount += 1;
        post({ kind: 'reasoning_preamble', text: content.parts[0], segmentStart });
      };
      const observeReasoningEnd = (payload, state) => {
        const message = findMessage(payload);
        if (!message || !message.author || message.author.role !== 'assistant' || message.status !== 'finished_successfully' || message.recipient !== 'all' || state.reasoningEnded) return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        if (!content || content.content_type !== 'reasoning_recap' || typeof content.content !== 'string' || !content.content.trim()) return;
        if (!metadata || metadata.reasoning_status !== 'reasoning_ended' || metadata.reasoning_recap_type !== 'collapse') return;
        state.reasoningEnded = true;
        const rawDuration = metadata.finished_duration_sec;
        const durationSec = typeof rawDuration === 'number' && Number.isFinite(rawDuration) && rawDuration >= 0 ? Math.round(rawDuration) : null;
        post({ kind: 'reasoning_ended', durationSec });
      };
      const observeToolActivity = (payload, state) => {
        const message = findMessage(payload);
        if (!message || !message.author || typeof message.id !== 'string' || !message.id) return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        const role = message.author.role;
        const contentType = content && content.content_type;
        const rawTitle = metadata && typeof metadata.reasoning_title === 'string' ? metadata.reasoning_title.trim() : '';
        const title = rawTitle.slice(0, 160);
        if (role === 'assistant' && contentType === 'code' && typeof message.recipient === 'string' && message.recipient && message.recipient !== 'all') {
          if (!state.invocations.has(message.id)) state.invocations.set(message.id, { recipient: message.recipient, slot: state.nextToolSlot++, connectorPayload: '', iconKind: message.recipient === 'api_tool.call_tool' ? 'connector' : 'code' });
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
      const scrubTextPatches = (node, state) => {
        if (Array.isArray(node)) {
          const output = [];
          for (const item of node) {
            const result = scrubTextPatches(item, state);
            if (!result.skip) output.push(result.value);
          }
          return { value: output, skip: false };
        }
        if (node && typeof node === 'object') {
          if (node.o === 'append' && node.p === '/message/content/parts/0' && typeof node.v === 'string') {
            postTextDelta(node.v, state);
            return { value: null, skip: true };
          }
          const output = {};
          for (const [key, child] of Object.entries(node)) {
            const result = scrubTextPatches(child, state);
            if (!result.skip) output[key] = result.value;
          }
          return { value: output, skip: false };
        }
        return { value: node, skip: false };
      };
      const filterFrame = (frame, state) => {
        const lines = String(frame || '').split('\n');
        const dataLines = lines.filter(line => line.startsWith('data:'));
        if (!dataLines.length) return frame + '\n\n';
        const data = dataLines.map(line => line.slice(5).trimStart()).join('\n');
        if (data.trim() === '[DONE]') {
          state.terminal = true;
          state.textContinuationActive = false;
          activeSend = false;
          queueMicrotask(() => { probeComposer(true); post({ kind: 'terminal' }); });
          return frame + '\n\n';
        }
        let payload;
        try { payload = JSON.parse(data); }
        catch (_) { state.textContinuationActive = false; return frame + '\n\n'; }
        observeReasoningActive(payload, state);
        observeReasoningPreamble(payload, state);
        observeToolActivity(payload, state);
        observeReasoningEnd(payload, state);
        const payloadKeys = payload && typeof payload === 'object' && !Array.isArray(payload) ? Object.keys(payload) : [];
        const rootTextAppend = payload && typeof payload === 'object' && !Array.isArray(payload) && payload.o === 'append' && payload.p === '/message/content/parts/0' && typeof payload.v === 'string';
        const exactTopLevelTextAppend = payloadKeys.length === 3 && payloadKeys.includes('o') && payloadKeys.includes('p') && payloadKeys.includes('v') && rootTextAppend;
        if (exactTopLevelTextAppend) {
          state.textContinuationActive = true;
          postTextDelta(payload.v, state);
          return '';
        }
        const contextualValueString = state.textContinuationActive && payloadKeys.length === 1 && payloadKeys[0] === 'v' && typeof payload.v === 'string';
        if (contextualValueString) {
          postTextDelta(payload.v, state);
          return '';
        }
        const titleGenerationWhileContinuation = state.textContinuationActive && payload && typeof payload === 'object' && !Array.isArray(payload) && payload.type === 'title_generation' && !Object.prototype.hasOwnProperty.call(payload, 'o') && !Object.prototype.hasOwnProperty.call(payload, 'p');
        if (titleGenerationWhileContinuation) {
          const nonDataLines = lines.filter(line => !line.startsWith('data:'));
          return nonDataLines.concat(['data: ' + JSON.stringify(payload)]).join('\n') + '\n\n';
        }
        state.textContinuationActive = false;
        const result = scrubTextPatches(payload, state);
        if (result.skip) return '';
        const nonDataLines = lines.filter(line => !line.startsWith('data:'));
        return nonDataLines.concat(['data: ' + JSON.stringify(result.value)]).join('\n') + '\n\n';
      };
      const observedResponse = response => {
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
                buffer = (buffer + decoder.decode()).replace(/\r\n/g, '\n');
                if (buffer.trim()) filterFrame(buffer, state);
                if (!state.terminal) post({ kind: 'stream_error', state: 'stream_ended_without_done' });
                return;
              }
              buffer = (buffer + decoder.decode(result.value || new Uint8Array(), { stream: true })).replace(/\r\n/g, '\n');
              let boundary;
              while ((boundary = buffer.indexOf('\n\n')) >= 0) {
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
        if (!response.body || typeof response.body.getReader !== 'function' || typeof ReadableStream !== 'function') return response;
        const reader = response.body.getReader();
        const state = { reasoningEnded: false, textContinuationActive: false, reasoningPreambleSeen: new Set(), reasoningPreambleCount: 0, reasoningActiveSeen: new Set(), invocations: new Map(), toolSeen: new Set(), nextToolSlot: 0, terminal: false };
        let buffer = '';
        const body = new ReadableStream({
          async pull(controller) {
            try {
              while (true) {
                const result = await reader.read();
                if (result.done) {
                  buffer = (buffer + decoder.decode()).replace(/\r\n/g, '\n');
                  if (buffer.trim()) {
                    const filtered = filterFrame(buffer, state);
                    if (filtered) controller.enqueue(encoder.encode(filtered));
                    buffer = '';
                  }
                  if (!state.terminal) {
                    state.textContinuationActive = false;
                    activeSend = false;
                    probeComposer(true);
                    post({ kind: 'stream_error', state: 'stream_ended_without_done' });
                  }
                  controller.close();
                  return;
                }
                buffer = (buffer + decoder.decode(result.value || new Uint8Array(), { stream: true })).replace(/\r\n/g, '\n');
                let output = '';
                let boundary;
                while ((boundary = buffer.indexOf('\n\n')) >= 0) {
                  const frame = buffer.slice(0, boundary);
                  buffer = buffer.slice(boundary + 2);
                  output += filterFrame(frame, state);
                }
                if (output) {
                  controller.enqueue(encoder.encode(output));
                  return;
                }
              }
            } catch (_) {
              state.textContinuationActive = false;
              activeSend = false;
              post({ kind: 'stream_error', state: 'reader_failed' });
              try { controller.error(new Error('covered_web_send_stream_failed')); } catch (_) {}
            }
          },
          cancel(reason) { state.textContinuationActive = false; try { reader.cancel(reason); } catch (_) {} }
        });
        return new Response(body, { status: response.status, statusText: response.statusText, headers: response.headers });
      };
      window.fetch = async function(input, init) {
        let url = null;
        try { url = new URL(typeof input === 'string' ? input : input && input.url || '', location.href); } catch (_) {}
        const chatHost = !!url && isChatGPTHost(url.hostname.toLowerCase());
        const method = String(init && init.method || input && input.method || 'GET').toUpperCase();
        const pageConversationID = currentConversationID();
        const isSend = chatHost && url.pathname === '/backend-api/f/conversation';
        const isResume = chatHost && url.pathname === '/backend-api/f/conversation/resume';
        const streamStatusMatch = chatHost ? url.pathname.match(/^\/backend-api\/conversation\/([^/]+)\/stream_status$/) : null;
        const pluralConversationMatch = chatHost ? url.pathname.match(/^\/backend-api\/conversations\/([^/]+)$/) : null;
        const decodedPathID = match => {
          if (!match) return null;
          try { return decodeURIComponent(match[1]); } catch (_) { return null; }
        };
        const isStreamStatus = !activeSend && method === 'GET' && pageConversationID && decodedPathID(streamStatusMatch) === pageConversationID;
        const isPluralConversation = !activeSend && method === 'GET' && pageConversationID && decodedPathID(pluralConversationMatch) === pageConversationID;
        if (isResume) {
          let resumeConversationID = null;
          let resumeOffsetType = 'missing';
          let resumeOffsetValue = -1;
          if (init && typeof init.body === 'string') {
            try {
              const resumeBody = JSON.parse(init.body);
              if (resumeBody && typeof resumeBody === 'object' && !Array.isArray(resumeBody)) {
                if (typeof resumeBody.conversation_id === 'string') resumeConversationID = resumeBody.conversation_id;
                if (Object.prototype.hasOwnProperty.call(resumeBody, 'offset')) {
                  resumeOffsetType = typeof resumeBody.offset;
                  if (typeof resumeBody.offset === 'number' && Number.isSafeInteger(resumeBody.offset)) resumeOffsetValue = resumeBody.offset;
                  else if (typeof resumeBody.offset === 'string' && /^\d+$/.test(resumeBody.offset)) resumeOffsetValue = Number(resumeBody.offset);
                }
              }
            } catch (_) {}
          }
          if (resumeConversationID && resumeConversationID === pageConversationID) {
            post({ kind: 'external_resume_request', hasOffset: resumeOffsetType !== 'missing', offsetType: resumeOffsetType, offsetValue: resumeOffsetValue });
            post({ kind: 'external_resume_observed' });
            try {
              const response = await originalFetch(input, init);
              const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
              post({ kind: 'resume_response', status: response.status, contentType });
              if (response.status === 200 && contentType === 'text/event-stream') {
                externalStreamingState.resumeSSE = true;
                observedResponse(response);
              }
              return response;
            } catch (error) {
              post({ kind: 'stream_error', state: 'resume_transport_error' });
              throw error;
            }
          }
        }
        if (isStreamStatus && !externalStreamingState.resumeSSE) {
          post({ kind: 'external_stream_status_request' });
          const response = await originalFetch(input, init);
          let streamState = '';
          if (response.status === 200) {
            try {
              const payload = await response.clone().json();
              if (payload && typeof payload.status === 'string') streamState = payload.status;
              if (payload && payload.status === 'IS_STREAMING') {
                externalStreamingState.completePending = false;
                if (!externalStreamingState.active) {
                  externalStreamingState.active = true;
                  lastExternalAssistantTextCharacters = -1;
                  post({ kind: 'external_streaming' });
                  reportExternalAssistantDOM();
                }
              } else if (payload && payload.status === 'COMPLETE' && externalStreamingState.active) {
                externalStreamingState.completePending = true;
              }
            } catch (_) {}
          }
          post({ kind: 'external_stream_status_response', status: response.status, streamState });
          return response;
        }
        if (isPluralConversation && !externalStreamingState.resumeSSE) {
          const response = await originalFetch(input, init);
          if (response.status === 200 && (externalStreamingState.active || externalStreamingState.completePending)) {
            try {
              const payload = await response.clone().json();
              if (payload && payload.conversation_id === pageConversationID && Array.isArray(payload.messages)) {
                let latestUserIndex = -1;
                for (let index = 0; index < payload.messages.length; index += 1) {
                  const serviceMessage = payload.messages[index];
                  if (serviceMessage && serviceMessage.author && serviceMessage.author.role === 'user') latestUserIndex = index;
                }
                if (latestUserIndex >= 0) {
                  const serviceMessages = payload.messages.slice(latestUserIndex + 1);
                  post({ kind: 'external_snapshot', complete: externalStreamingState.completePending, messages: serviceMessages });
                  reportExternalAssistantDOM();
                }
              }
            } catch (_) {}
          }
          return response;
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
      const observer = new MutationObserver(() => probeComposer(false));
      const start = () => {
        installRenderSuppression();
        probeComposer(true);
        observer.observe(document.documentElement || document, { childList: true, subtree: true });
      };
      if (document.documentElement) start(); else document.addEventListener('DOMContentLoaded', start, { once: true });
      window.__coveredWebSendExecutor = { submit, probeComposer };
    })();
    """#
}

enum ConversationLiveResponsePhase: String {
    case preparing
    case thinking
    case reasoning
    case final
    case completed
    case failed

    var isActive: Bool {
        switch self {
        case .preparing, .thinking, .reasoning, .final: return true
        case .completed, .failed: return false
        }
    }
}

struct ConversationLiveResponseSnapshot {
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

enum ConversationLiveResponseError: LocalizedError {
    case responseAlreadyActive

    var errorDescription: String? { "当前会话已有正在进行的回答。" }
}

private final class ConversationResponseRuntime {
    var generations: [String: Int] = [:]
    var snapshots: [String: ConversationLiveResponseSnapshot] = [:]
    var onChange: ((String) -> Void)?
}

private var conversationResponseRuntimeAssociationKey: UInt8 = 0

extension ConversationRepository {
    private var responseRuntime: ConversationResponseRuntime {
        precondition(Thread.isMainThread)
        if let runtime = objc_getAssociatedObject(self, &conversationResponseRuntimeAssociationKey) as? ConversationResponseRuntime { return runtime }
        let runtime = ConversationResponseRuntime()
        objc_setAssociatedObject(self, &conversationResponseRuntimeAssociationKey, runtime, .OBJC_ASSOCIATION_RETAIN_NONATOMIC)
        return runtime
    }

    var onLiveResponseChanged: ((String) -> Void)? {
        get { responseRuntime.onChange }
        set { responseRuntime.onChange = newValue }
    }

    func liveResponse(for conversationID: String) -> ConversationLiveResponseSnapshot? {
        precondition(Thread.isMainThread)
        return responseRuntime.snapshots[conversationID]
    }

    func isLiveResponseActive(for conversationID: String) -> Bool {
        precondition(Thread.isMainThread)
        return responseRuntime.snapshots[conversationID]?.phase.isActive ?? false
    }

    @discardableResult
    func beginExternalLiveResponse(conversationID: String) -> Result<Int, Error> {
        precondition(Thread.isMainThread)
        if responseRuntime.snapshots[conversationID]?.phase.isActive == true { return .failure(ConversationLiveResponseError.responseAlreadyActive) }
        let generation = (responseRuntime.generations[conversationID] ?? 0) + 1
        responseRuntime.generations[conversationID] = generation
        let baselineVisibleMessageCount = selectedConversationID == conversationID ? (selectedConversation?.messages.count ?? 0) : 0
        responseRuntime.snapshots[conversationID] = ConversationLiveResponseSnapshot(generation: generation, conversationID: conversationID, baselineVisibleMessageCount: baselineVisibleMessageCount, promptText: "", phase: .thinking, timeline: [], finalText: "", reasoningEnded: false, reasoningDurationSeconds: nil, failureReason: nil)
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["phase"] = ConversationLiveResponsePhase.thinking.rawValue
        fields["source"] = "external_page_owned"
        fields["baselineVisibleMessageCount"] = String(baselineVisibleMessageCount)
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.started", fields: fields)
        responseRuntime.onChange?(conversationID)
        return .success(generation)
    }

    @discardableResult
    func beginLiveResponse(conversationID: String, promptText: String) -> Result<Int, Error> {
        precondition(Thread.isMainThread)
        if responseRuntime.snapshots[conversationID]?.phase.isActive == true { return .failure(ConversationLiveResponseError.responseAlreadyActive) }
        let generation = (responseRuntime.generations[conversationID] ?? 0) + 1
        responseRuntime.generations[conversationID] = generation
        let baselineVisibleMessageCount = selectedConversationID == conversationID ? (selectedConversation?.messages.count ?? 0) : 0
        responseRuntime.snapshots[conversationID] = ConversationLiveResponseSnapshot(generation: generation, conversationID: conversationID, baselineVisibleMessageCount: baselineVisibleMessageCount, promptText: promptText, phase: .preparing, timeline: [], finalText: "", reasoningEnded: false, reasoningDurationSeconds: nil, failureReason: nil)
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["phase"] = ConversationLiveResponsePhase.preparing.rawValue
        fields["promptCharacters"] = String(promptText.count)
        fields["baselineVisibleMessageCount"] = String(baselineVisibleMessageCount)
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.started", fields: fields)
        responseRuntime.onChange?(conversationID)
        return .success(generation)
    }

    private struct ExternalPageProjection {
        let timeline: [ConversationResponseTimelineItem]
        let finalText: String
        let reasoningEnded: Bool
        let reasoningDurationSeconds: Int?
        let hasFinalMessage: Bool
    }

    private static func externalPageVisibleText(_ content: [String: Any]) -> String {
        var parts: [String] = []
        if let text = content["text"] as? String, !text.isEmpty { parts.append(text) }
        if let values = content["parts"] as? [Any] {
            for value in values {
                if let text = value as? String, !text.isEmpty { parts.append(text) }
                else if let object = value as? [String: Any], let text = object["text"] as? String, !text.isEmpty { parts.append(text) }
            }
        }
        return parts.joined(separator: "\n").trimmingCharacters(in: .whitespacesAndNewlines)
    }

    private static func projectExternalPageMessages(_ rawMessages: [[String: Any]]) -> ExternalPageProjection {
        var timeline: [ConversationResponseTimelineItem] = []
        var finalText = ""
        var reasoningEnded = false
        var reasoningDurationSeconds: Int?
        var hasFinalMessage = false
        var toolIndexByServiceID: [String: Int] = [:]
        var toolRecipientByServiceID: [String: String] = [:]
        var toolInputByServiceID: [String: String] = [:]

        for message in rawMessages {
            guard let author = message["author"] as? [String: Any], let rawRole = author["role"] as? String else { continue }
            let metadata = message["metadata"] as? [String: Any]
            if rawRole == "tool" {
                if message["status"] as? String == "finished_successfully", message["recipient"] as? String == "all", let parentID = metadata?["parent_id"] as? String, let index = toolIndexByServiceID[parentID], timeline.indices.contains(index), timeline[index].kind == .tool {
                    timeline[index].completed = true
                    if toolRecipientByServiceID[parentID] == "api_tool.call_tool", let inputJSON = toolInputByServiceID[parentID], !inputJSON.isEmpty, let invokedResource = metadata?["invoked_resource"] as? [String: Any], invokedResource["app_name"] as? String == "GitHub", let resultContent = message["content"] as? [String: Any], JSONSerialization.isValidJSONObject(resultContent), let data = try? JSONSerialization.data(withJSONObject: resultContent), let outputJSON = String(data: data, encoding: .utf8) {
                        timeline[index].toolInputJSON = inputJSON
                        timeline[index].toolOutputJSON = outputJSON
                        timeline[index].toolIconKind = .github
                    }
                }
                continue
            }
            guard rawRole == "assistant", let content = message["content"] as? [String: Any] else { continue }
            if let recipient = message["recipient"] as? String {
                let normalizedRecipient = recipient.trimmingCharacters(in: .whitespacesAndNewlines)
                if !normalizedRecipient.isEmpty, normalizedRecipient != "all" {
                    if message["status"] as? String == "finished_successfully", content["content_type"] as? String == "code", (metadata?["is_complete"] as? Bool) == true {
                        let rawTitle = (metadata?["reasoning_title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
                        let title = rawTitle.isEmpty ? "工具调用" : String(rawTitle.prefix(160))
                        let slot = timeline.count
                        let iconKind: ConversationToolIconKind = normalizedRecipient == "api_tool.call_tool" ? .connector : .code
                        timeline.append(.tool(slot: slot, title: title, completed: false, iconKind: iconKind))
                        if let serviceID = message["id"] as? String, !serviceID.isEmpty {
                            toolIndexByServiceID[serviceID] = timeline.count - 1
                            toolRecipientByServiceID[serviceID] = normalizedRecipient
                            if normalizedRecipient == "api_tool.call_tool", let connectorPayload = metadata?["connector_tool_payload"] as? String, !connectorPayload.isEmpty { toolInputByServiceID[serviceID] = connectorPayload }
                        }
                    }
                    continue
                }
            }
            if content["content_type"] as? String == "reasoning_recap", message["status"] as? String == "finished_successfully", let summary = content["content"] as? String, let metadata, metadata["reasoning_status"] as? String == "reasoning_ended", metadata["reasoning_recap_type"] as? String == "collapse" {
                let normalized = summary.trimmingCharacters(in: .whitespacesAndNewlines)
                if !normalized.isEmpty, !timeline.contains(where: { $0.kind == .reasoning }) { timeline.append(.reasoning(normalized)) }
                reasoningEnded = true
                if let duration = metadata["finished_duration_sec"] as? NSNumber {
                    let seconds = Int(duration.doubleValue.rounded())
                    if seconds >= 0 { reasoningDurationSeconds = seconds }
                }
                continue
            }
            if (metadata?["is_thinking_preamble_message"] as? Bool) == true {
                let reasoning = externalPageVisibleText(content)
                if !reasoning.isEmpty { timeline.append(.reasoning(reasoning)) }
                continue
            }
            if let contentType = content["content_type"] as? String, contentType == "thoughts" || contentType == "inline_cot_expandable_content" { continue }
            if content["content_type"] as? String == "text" {
                hasFinalMessage = true
                finalText = externalPageVisibleText(content)
            }
        }
        return ExternalPageProjection(timeline: timeline, finalText: finalText, reasoningEnded: reasoningEnded, reasoningDurationSeconds: reasoningDurationSeconds, hasFinalMessage: hasFinalMessage)
    }

    @discardableResult
    func adoptExternalAuthoritativeDetailTimeline(conversationID: String, timeline: [ConversationResponseTimelineItem], reasoningDurationSeconds: Int?, authoritativeVisibleMessageCount: Int, latestVisibleRole: ConversationMessage.Role?) -> Int? {
        precondition(Thread.isMainThread)
        if timeline.isEmpty {
            guard let snapshot = responseRuntime.snapshots[conversationID], snapshot.phase.isActive, snapshot.promptText.isEmpty else { return nil }
            guard authoritativeVisibleMessageCount > snapshot.baselineVisibleMessageCount, latestVisibleRole == .assistant else { return snapshot.generation }
            responseRuntime.snapshots.removeValue(forKey: conversationID)
            var fields = diagnosticsFields(for: conversationID)
            fields["responseGeneration"] = String(snapshot.generation)
            fields["authoritativeVisibleMessageCount"] = String(authoritativeVisibleMessageCount)
            fields["baselineVisibleMessageCount"] = String(snapshot.baselineVisibleMessageCount)
            fields["reason"] = "authoritative_assistant_materialized"
            DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.externalDetailReconciled", fields: fields)
            responseRuntime.onChange?(conversationID)
            return nil
        }

        if let active = responseRuntime.snapshots[conversationID], active.phase.isActive, !active.promptText.isEmpty {
            var fields = diagnosticsFields(for: conversationID)
            fields["responseGeneration"] = String(active.generation)
            fields["reason"] = "client_owned_response_active"
            DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.externalDetailDiscarded", fields: fields)
            return nil
        }

        let generation: Int
        var snapshot: ConversationLiveResponseSnapshot
        if let active = responseRuntime.snapshots[conversationID], active.phase.isActive, active.promptText.isEmpty {
            generation = active.generation
            snapshot = active
        } else {
            generation = (responseRuntime.generations[conversationID] ?? 0) + 1
            responseRuntime.generations[conversationID] = generation
            snapshot = ConversationLiveResponseSnapshot(generation: generation, conversationID: conversationID, baselineVisibleMessageCount: authoritativeVisibleMessageCount, promptText: "", phase: .reasoning, timeline: [], finalText: "", reasoningEnded: false, reasoningDurationSeconds: nil, failureReason: nil)
            var fields = diagnosticsFields(for: conversationID)
            fields["responseGeneration"] = String(generation)
            fields["phase"] = ConversationLiveResponsePhase.reasoning.rawValue
            fields["source"] = "external_authoritative_detail"
            fields["baselineVisibleMessageCount"] = String(authoritativeVisibleMessageCount)
            DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.started", fields: fields)
        }

        let changed = snapshot.phase != .reasoning || snapshot.timeline != timeline || snapshot.reasoningDurationSeconds != reasoningDurationSeconds || !snapshot.finalText.isEmpty
        snapshot.phase = .reasoning
        snapshot.timeline = timeline
        snapshot.finalText = ""
        snapshot.reasoningDurationSeconds = reasoningDurationSeconds
        snapshot.failureReason = nil
        responseRuntime.snapshots[conversationID] = snapshot
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["changed"] = changed ? "true" : "false"
        fields["timelineItemCount"] = String(timeline.count)
        fields["reasoningItemCount"] = String(timeline.filter { $0.kind == .reasoning }.count)
        fields["toolCount"] = String(timeline.filter { $0.kind == .tool }.count)
        fields["source"] = "authoritative_detail"
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.externalDetailSnapshot", fields: fields)
        if changed { responseRuntime.onChange?(conversationID) }
        return generation
    }

    func consumeExternalConversationSnapshot(_ serviceMessages: [[String: Any]], conversationID: String, generation: Int) {
        precondition(Thread.isMainThread)
        guard var snapshot = responseRuntime.snapshots[conversationID], snapshot.generation == generation, snapshot.phase.isActive else {
            var fields = diagnosticsFields(for: conversationID)
            fields["responseGeneration"] = String(generation)
            fields["reason"] = "generation_mismatch_missing_or_terminal"
            DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.externalSnapshotDiscarded", fields: fields)
            return
        }
        let projection = Self.projectExternalPageMessages(serviceMessages)
        let nextPhase: ConversationLiveResponsePhase
        if projection.hasFinalMessage || projection.reasoningEnded { nextPhase = .final }
        else if !projection.timeline.isEmpty { nextPhase = .reasoning }
        else { nextPhase = .thinking }
        let changed = snapshot.phase != nextPhase || snapshot.timeline != projection.timeline || snapshot.finalText != projection.finalText || snapshot.reasoningEnded != projection.reasoningEnded || snapshot.reasoningDurationSeconds != projection.reasoningDurationSeconds
        snapshot.phase = nextPhase
        snapshot.timeline = projection.timeline
        snapshot.finalText = projection.finalText
        snapshot.reasoningEnded = projection.reasoningEnded
        snapshot.reasoningDurationSeconds = projection.reasoningDurationSeconds
        snapshot.failureReason = nil
        responseRuntime.snapshots[conversationID] = snapshot
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["serviceMessageCount"] = String(serviceMessages.count)
        fields["phase"] = snapshot.phase.rawValue
        fields["changed"] = changed ? "true" : "false"
        fields["reasoningCharacters"] = String(snapshot.timeline.filter { $0.kind == .reasoning }.reduce(0) { $0 + $1.text.count })
        fields["finalCharacters"] = String(snapshot.finalText.count)
        fields["toolCount"] = String(snapshot.timeline.filter { $0.kind == .tool }.count)
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.externalSnapshot", fields: fields)
        if changed { responseRuntime.onChange?(conversationID) }
    }

    func consumeLiveResponseEvent(_ event: CoveredWebSendEvent, conversationID: String, generation: Int) {
        precondition(Thread.isMainThread)
        guard var snapshot = responseRuntime.snapshots[conversationID], snapshot.generation == generation else {
            var fields = diagnosticsFields(for: conversationID)
            fields["responseGeneration"] = String(generation)
            fields["reason"] = "generation_mismatch_or_missing"
            DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.eventDiscarded", fields: fields)
            return
        }
        guard snapshot.phase.isActive else {
            var fields = diagnosticsFields(for: conversationID)
            fields["responseGeneration"] = String(generation)
            fields["reason"] = "already_terminal"
            DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.eventDiscarded", fields: fields)
            return
        }

        var eventName = "unknown"
    switch event {
    case .externalResumeObserved: eventName = "external_resume_observed"
    case .externalStreamingObserved: eventName = "external_streaming_observed"
    case .externalAcquisitionHint: eventName = "external_acquisition_hint"
    case .externalConversationSnapshot(_, _): eventName = "external_conversation_snapshot"
    case .composerReady: eventName = "composer_ready"
    case .sendObserved: eventName = "send_observed"
    case .responseAccepted:
        snapshot.phase = .thinking
        eventName = "response_accepted"
    case .thinkingActive:
        if snapshot.phase != .final { snapshot.phase = .thinking }
        eventName = "thinking_active"
    case .reasoningPreamble(let text, let segmentStart):
        if segmentStart || snapshot.timeline.last?.kind != .reasoning { snapshot.timeline.append(.reasoning(text)) }
        else { snapshot.timeline[snapshot.timeline.count - 1].text += text }
        snapshot.phase = .reasoning
        eventName = "reasoning_preamble"
    case .reasoningDelta(let text):
        if snapshot.timeline.last?.kind == .reasoning { snapshot.timeline[snapshot.timeline.count - 1].text += text }
        else { snapshot.timeline.append(.reasoning(text)) }
        snapshot.phase = .reasoning
        eventName = "reasoning_delta"
    case .reasoningEnded(let durationSeconds):
        snapshot.reasoningEnded = true
        snapshot.reasoningDurationSeconds = durationSeconds
        snapshot.phase = .final
        eventName = "reasoning_ended"
    case .finalDelta(let text):
        snapshot.finalText += text
        snapshot.phase = .final
        eventName = "final_delta"
    case .toolActivity(let slot, let title, let completed, let inputJSON, let outputJSON, let iconKind):
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
    case .terminal:
        if !snapshot.reasoningEnded, snapshot.finalText.isEmpty, !snapshot.promptText.isEmpty {
            let provisionalFinal = snapshot.timeline.filter { $0.kind == .reasoning }.map(\.text).joined(separator: "\n\n").trimmingCharacters(in: .whitespacesAndNewlines)
            if !provisionalFinal.isEmpty {
                snapshot.finalText = provisionalFinal
                snapshot.timeline.removeAll { $0.kind == .reasoning }
            }
        }
        snapshot.phase = .completed
        eventName = "terminal"
    case .failed(let reason):
        snapshot.phase = .failed
        snapshot.failureReason = reason
        eventName = "failed"
    }

        responseRuntime.snapshots[conversationID] = snapshot
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["event"] = eventName
        fields["phase"] = snapshot.phase.rawValue
        fields["reasoningCharacters"] = String(snapshot.timeline.filter { $0.kind == .reasoning }.reduce(0) { $0 + $1.text.count })
        fields["finalCharacters"] = String(snapshot.finalText.count)
        fields["toolCount"] = String(snapshot.timeline.filter { $0.kind == .tool }.count)
        fields["timelineItemCount"] = String(snapshot.timeline.count)
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.event", fields: fields)
        responseRuntime.onChange?(conversationID)
    }

    func clearLiveResponseAfterAuthoritativeReconcile(conversationID: String, generation: Int, authoritativeVisibleMessageCount: Int) -> Bool {
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

    func resetAllLiveResponsesForAccountChange() {
        precondition(Thread.isMainThread)
        let ids = Array(responseRuntime.snapshots.keys)
        responseRuntime.snapshots.removeAll()
        responseRuntime.generations.removeAll()
        for id in ids { responseRuntime.onChange?(id) }
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.reset", fields: ["reason": "account_change", "responseCount": String(ids.count)])
    }
}

final class RootViewController: UISplitViewController, UISplitViewControllerDelegate {
    private let diagnostics = DiagnosticsLogger.shared
    private let repository = ConversationRepository()
    private var sendExecutors: [String: CoveredWebSendExecutor] = [:]
    private var externalAcquisitionSyncs: Set<String> = []
    private let validationSendButton = UIButton(type: .system)
    private let sidebarViewController: ConversationSidebarViewController
    private let detailViewController: ConversationDetailViewController
    private let detailNavigationController: UINavigationController

    init() {
        sidebarViewController = ConversationSidebarViewController(repository: repository)
        detailViewController = ConversationDetailViewController(repository: repository)
        detailNavigationController = UINavigationController(rootViewController: detailViewController)
        super.init(style: .doubleColumn)
        delegate = self

        let sidebarNavigationController = UINavigationController(rootViewController: sidebarViewController)
        setViewController(sidebarNavigationController, for: .primary)
        setViewController(detailNavigationController, for: .secondary)
        configureValidationSendToolbar()

        repository.onLiveResponseChanged = { [weak self] id in self?.liveResponseDidChange(id: id) }
        repository.onAccountScopeReset = { [weak self] in
            guard let self else { return }
            let executors = Array(self.sendExecutors.values)
            self.sendExecutors.removeAll()
            self.externalAcquisitionSyncs.removeAll()
            for executor in executors { executor.resetForAccountChange() }
            self.repository.resetAllLiveResponsesForAccountChange()
            self.sidebarViewController.resetForAccountScopeChange()
            self.detailViewController.resetForAccountScopeChange()
            self.detailNavigationController.setToolbarHidden(true, animated: false)
            self.show(.primary)
        }
        sidebarViewController.onSelectConversation = { [weak self] id in
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
        detailViewController.onManualLatestSyncApplied = { [weak self] id, _ in
            guard let self, self.repository.selectedConversationID == id else { return }
            if let snapshot = self.repository.liveResponse(for: id), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }
            self.observeExternalResponseIfNeeded(conversationID: id, forcePageReload: true)
        }
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        preferredDisplayMode = .oneBesideSecondary
        preferredSplitBehavior = .tile
        presentsWithGesture = true
        detailNavigationController.setToolbarHidden(repository.selectedConversationID == nil, animated: false)
        updateLivePresentation()
        diagnostics.info(category: "ui", name: "nativeConversationShell.loaded")
    }

    func splitViewController(_ svc: UISplitViewController, topColumnForCollapsingToProposedTopColumn proposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column {
        repository.selectedConversationID == nil ? .primary : .secondary
    }

    private func configureValidationSendToolbar() {
        validationSendButton.setTitle("测试发送…", for: .normal)
        validationSendButton.setImage(UIImage(systemName: "paperplane"), for: .normal)
        validationSendButton.titleLabel?.font = .systemFont(ofSize: 16, weight: .medium)
        validationSendButton.tintColor = .label
        validationSendButton.backgroundColor = .secondarySystemBackground
        validationSendButton.layer.cornerRadius = 18
        validationSendButton.contentEdgeInsets = UIEdgeInsets(top: 8, left: 18, bottom: 8, right: 18)
        validationSendButton.addTarget(self, action: #selector(openValidationSendPrompt), for: .touchUpInside)
        validationSendButton.translatesAutoresizingMaskIntoConstraints = false
        validationSendButton.heightAnchor.constraint(equalToConstant: 36).isActive = true
        validationSendButton.widthAnchor.constraint(greaterThanOrEqualToConstant: 220).isActive = true
        let flexible = UIBarButtonItem(barButtonSystemItem: .flexibleSpace, target: nil, action: nil)
        detailViewController.toolbarItems = [flexible, UIBarButtonItem(customView: validationSendButton), UIBarButtonItem(barButtonSystemItem: .flexibleSpace, target: nil, action: nil)]
    }

    @objc private func openValidationSendPrompt() {
        guard let conversationID = repository.selectedConversationID, !repository.isLiveResponseActive(for: conversationID) else { return }
        let alert = UIAlertController(title: "Send/Stream 验证", message: "临时验证入口；最终输入框由 DEV-composer-parity 实现。", preferredStyle: .alert)
        alert.addTextField { textField in
            textField.placeholder = "输入本轮测试消息"
            textField.autocorrectionType = .yes
            textField.clearButtonMode = .whileEditing
        }
        alert.addAction(UIAlertAction(title: "取消", style: .cancel))
        alert.addAction(UIAlertAction(title: "发送", style: .default) { [weak self, weak alert] _ in
            guard let self, let text = alert?.textFields?.first?.text else { return }
            self.startValidationSend(text: text, conversationID: conversationID)
        })
        present(alert, animated: true)
    }

    private func executor(for conversationID: String) -> CoveredWebSendExecutor {
        if let executor = sendExecutors[conversationID] { return executor }
        let executor = CoveredWebSendExecutor()
        executor.attachCoveredWebView(to: view)
        sendExecutors[conversationID] = executor
        diagnostics.info(category: "webSend", name: "coveredExecutor.created", fields: ["activeExecutorCount": String(sendExecutors.count)])
        return executor
    }

    private func releaseExecutor(for conversationID: String, expected: CoveredWebSendExecutor) {
        guard sendExecutors[conversationID] === expected else { return }
        sendExecutors.removeValue(forKey: conversationID)
        diagnostics.info(category: "webSend", name: "coveredExecutor.released", fields: ["activeExecutorCount": String(sendExecutors.count)])
    }

    private func releaseIdleExecutors(except conversationID: String) {
        let idle = sendExecutors.filter { $0.key != conversationID && !$0.value.isBusy }
        for (id, executor) in idle { releaseExecutor(for: id, expected: executor) }
    }

    private func observeExternalResponseIfNeeded(conversationID: String, forcePageReload: Bool = false) {
        guard repository.selectedConversationID == conversationID else { return }
        let existingSnapshot = repository.liveResponse(for: conversationID)
        guard existingSnapshot?.phase.isActive != true || existingSnapshot?.promptText.isEmpty == true else { return }
        let sendExecutor = executor(for: conversationID)
        var externalGeneration: Int? = existingSnapshot?.phase.isActive == true ? existingSnapshot?.generation : nil
        sendExecutor.observeExistingConversation(conversationID: conversationID, forceReload: forcePageReload) { [weak self, weak sendExecutor] event in
            guard let self, let sendExecutor else { return }
            func ensureGeneration() -> Int? {
                if let externalGeneration { return externalGeneration }
                guard !self.repository.isLiveResponseActive(for: conversationID) else {
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    return nil
                }
                switch self.repository.beginExternalLiveResponse(conversationID: conversationID) {
                case .success(let generation):
                    externalGeneration = generation
                    self.updateLivePresentation()
                    return generation
                case .failure:
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    return nil
                }
            }
            switch event {
            case .externalAcquisitionHint:
                guard externalGeneration == nil else { return }
                self.handleExternalAcquisitionHint(conversationID: conversationID, sendExecutor: sendExecutor)
                return
            case .externalResumeObserved:
                return
            case .externalStreamingObserved:
                guard let generation = ensureGeneration() else { return }
                self.repository.consumeLiveResponseEvent(.thinkingActive, conversationID: conversationID, generation: generation)
            case .externalConversationSnapshot(let messages, let complete):
                guard let generation = ensureGeneration() else { return }
                self.repository.consumeExternalConversationSnapshot(messages, conversationID: conversationID, generation: generation)
                if complete {
                    guard let snapshot = self.repository.liveResponse(for: conversationID), snapshot.generation == generation else { return }
                    if snapshot.reasoningEnded && snapshot.finalText.isEmpty {
                        var fields = self.repository.diagnosticsFields(for: conversationID)
                        fields["responseGeneration"] = String(generation)
                        fields["reason"] = "final_not_materialized"
                        self.diagnostics.info(category: "webSend", name: "coveredExecutor.externalCompletionDeferred", fields: fields)
                        return
                    }
                    self.repository.consumeLiveResponseEvent(.terminal, conversationID: conversationID, generation: generation)
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)
                }
            case .responseAccepted:
                guard let generation = ensureGeneration() else { return }
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

    private func handleExternalAcquisitionHint(conversationID: String, sendExecutor: CoveredWebSendExecutor) {
        guard repository.selectedConversationID == conversationID else {
            diagnostics.info(category: "webSend", name: "externalAcquisitionSync.skipped", fields: ["reason": "conversation_not_selected"])
            return
        }
        guard !repository.isLiveResponseActive(for: conversationID) else {
            diagnostics.info(category: "webSend", name: "externalAcquisitionSync.skipped", fields: ["reason": "live_response_active"])
            return
        }
        guard !externalAcquisitionSyncs.contains(conversationID) else {
            diagnostics.info(category: "webSend", name: "externalAcquisitionSync.skipped", fields: ["reason": "sync_in_flight"])
            return
        }
        guard repository.detailOperationSnapshot(for: conversationID) == nil else {
            diagnostics.info(category: "webSend", name: "externalAcquisitionSync.skipped", fields: ["reason": "detail_operation_in_flight"])
            return
        }

        let previousLatestUserID = repository.selectedConversation?.messages.last(where: { $0.role == .user })?.id
        externalAcquisitionSyncs.insert(conversationID)
        diagnostics.info(category: "webSend", name: "externalAcquisitionSync.started", fields: repository.diagnosticsFields(for: conversationID))
        repository.syncLatestMessages(id: conversationID) { [weak self, weak sendExecutor] result in
            guard let self else { return }
            self.externalAcquisitionSyncs.remove(conversationID)
            guard let sendExecutor else { return }
            switch result {
            case .success(let detail):
                let latestUserID = detail.messages.last(where: { $0.role == .user })?.id
                let latestUserChanged = latestUserID != nil && latestUserID != previousLatestUserID
                _ = self.repository.clearTerminalExternalLiveResponseAfterAuthoritativeRefresh(conversationID: conversationID)
                var fields = self.repository.diagnosticsFields(for: conversationID)
                fields["latestUserChanged"] = latestUserChanged ? "true" : "false"
                fields["visibleMessageCount"] = String(detail.messages.count)
                self.diagnostics.info(category: "webSend", name: "externalAcquisitionSync.completed", fields: fields)
                if self.repository.selectedConversationID == conversationID { self.detailViewController.showConversation(id: conversationID) }
                guard latestUserChanged, self.repository.selectedConversationID == conversationID, !self.repository.isLiveResponseActive(for: conversationID), self.sendExecutors[conversationID] === sendExecutor else { return }
                self.observeExternalResponseIfNeeded(conversationID: conversationID, forcePageReload: true)
            case .failure(let error):
                self.diagnostics.error(category: "webSend", name: "externalAcquisitionSync.failed", error: error, fields: self.repository.diagnosticsFields(for: conversationID))
            }
        }
    }

    private func startValidationSend(text: String, conversationID: String) {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty, repository.selectedConversationID == conversationID else { return }
        let generation: Int
        switch repository.beginLiveResponse(conversationID: conversationID, promptText: trimmed) {
        case .success(let value): generation = value
        case .failure(let error):
            showValidationError(error.localizedDescription)
            return
        }
        updateLivePresentation()
        let sendExecutor = executor(for: conversationID)
        sendExecutor.sendExistingConversation(text: trimmed, conversationID: conversationID) { [weak self, weak sendExecutor] event in
            guard let self, let sendExecutor else { return }
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

    private func reconcileTerminalResponse(conversationID: String, generation: Int) {
        diagnostics.info(category: "webSend", name: "authoritativeReconcile.requested", fields: repository.diagnosticsFields(for: conversationID))
        repository.syncLatestMessages(id: conversationID) { [weak self] result in
            guard let self else { return }
            switch result {
            case .success(let detail):
                let cleared = self.repository.clearLiveResponseAfterAuthoritativeReconcile(conversationID: conversationID, generation: generation, authoritativeVisibleMessageCount: detail.messages.count)
                self.diagnostics.info(category: "webSend", name: "authoritativeReconcile.completed", fields: ["liveSnapshotCleared": cleared ? "true" : "false", "authoritativeVisibleMessageCount": String(detail.messages.count)])
                if self.repository.selectedConversationID == conversationID { self.detailViewController.showConversation(id: conversationID) }
            case .failure(let error):
                self.diagnostics.error(category: "webSend", name: "authoritativeReconcile.failed", error: error)
            }
            self.updateLivePresentation()
            if self.repository.selectedConversationID == conversationID, !self.repository.isLiveResponseActive(for: conversationID) { self.observeExternalResponseIfNeeded(conversationID: conversationID) }
        }
    }

    private func liveResponseDidChange(id: String) {
        guard repository.selectedConversationID == id else { return }
        detailViewController.liveResponseDidChange(id: id)
        updateLivePresentation()
    }

    private func updateLivePresentation() {
        guard let conversationID = repository.selectedConversationID else {
            validationSendButton.isEnabled = false
            detailViewController.navigationItem.rightBarButtonItem?.isEnabled = false
            return
        }
        let snapshot = repository.liveResponse(for: conversationID)
        let selectedResponseActive = snapshot?.phase.isActive ?? false
        let localResponseActive = selectedResponseActive && !(snapshot?.promptText.isEmpty ?? true)
        validationSendButton.isEnabled = !selectedResponseActive
        validationSendButton.setTitle(selectedResponseActive ? "回答中…" : "测试发送…", for: .normal)
        detailViewController.navigationItem.rightBarButtonItem?.isEnabled = !localResponseActive
    }

    private func showValidationError(_ message: String) {
        let alert = UIAlertController(title: "无法发送", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "好", style: .default))
        present(alert, animated: true)
    }
}
