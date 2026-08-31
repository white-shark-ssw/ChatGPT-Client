import ObjectiveC
import UIKit
import WebKit

private final class WeakCoveredWebSendMessageHandler: NSObject, WKScriptMessageHandler {
    weak var target: WKScriptMessageHandler?
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) { target?.userContentController(userContentController, didReceive: message) }
}

enum CoveredWebSendEvent {
    case composerReady
    case sendObserved
    case responseAccepted
    case thinkingActive
    case reasoningPreamble(String, segmentStart: Bool)
    case reasoningDelta(String)
    case reasoningEnded
    case finalDelta(String)
    case toolActivity(slot: Int, title: String, completed: Bool)
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
    private var activeEvents: ((CoveredWebSendEvent) -> Void)?
    private var responseActive = false

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

    deinit { webView.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName) }

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
        activeEvents = nil
        responseActive = false
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
        case "reasoning_ended": activeEvents?(.reasoningEnded)
        case "final_delta":
            guard let text = body["text"] as? String, !text.isEmpty else { return }
            activeEvents?(.finalDelta(text))
        case "tool_activity":
            let slot = (body["slot"] as? NSNumber)?.intValue ?? -1
            guard slot >= 0 else { return }
            let title = (body["title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
            activeEvents?(.toolActivity(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: (body["completed"] as? NSNumber)?.boolValue ?? false))
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
            guard let self, let error else { return }
            let nsError = error as NSError
            self.diagnostics.warning(category: "webSend", name: "coveredExecutor.bridge", fields: ["state": "evaluate_failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
            self.failCurrent("bridge_failed")
        }
    }

    private func failCurrent(_ reason: String) {
        let events = activeEvents ?? pendingSend?.events
        pendingSend = nil
        responseActive = false
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

      const currentConversationID = () => {
        const match = location.pathname.match(/^\/c\/([^/?#]+)/);
        return match ? decodeURIComponent(match[1]) : null;
      };
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');
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
        element.focus();
        if (element instanceof HTMLTextAreaElement || element instanceof HTMLInputElement) {
          const prototype = element instanceof HTMLTextAreaElement ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
          const descriptor = Object.getOwnPropertyDescriptor(prototype, 'value');
          if (!descriptor || !descriptor.set) return false;
          descriptor.set.call(element, text);
          element.dispatchEvent(new InputEvent('input', { bubbles: true, inputType: 'insertText', data: text }));
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
        return true;
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
        post({ kind: 'reasoning_ended' });
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
          if (!state.invocations.has(message.id)) state.invocations.set(message.id, { recipient: message.recipient, slot: state.nextToolSlot++ });
          const identity = state.invocations.get(message.id);
          if (message.status !== 'finished_successfully' || !metadata || metadata.is_complete !== true || state.toolSeen.has(message.id)) return;
          state.toolSeen.add(message.id);
          post({ kind: 'tool_activity', slot: identity.slot, title, completed: false });
          return;
        }
        if (role !== 'tool' || message.recipient !== 'all' || message.status !== 'finished_successfully' || state.toolSeen.has(message.id)) return;
        state.toolSeen.add(message.id);
        const parentID = metadata && typeof metadata.parent_id === 'string' && metadata.parent_id ? metadata.parent_id : '';
        const identity = parentID ? state.invocations.get(parentID) : null;
        if (identity) post({ kind: 'tool_activity', slot: identity.slot, title, completed: true });
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

struct ConversationLiveTool: Equatable {
    let slot: Int
    var title: String
    var completed: Bool
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
    var phase: ConversationLiveResponsePhase
    var reasoningText: String
    var finalText: String
    var tools: [ConversationLiveTool]
    var reasoningEnded: Bool
    var failureReason: String?
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
    func beginLiveResponse(conversationID: String, promptCharacterCount: Int) -> Result<Int, Error> {
        precondition(Thread.isMainThread)
        if responseRuntime.snapshots[conversationID]?.phase.isActive == true { return .failure(ConversationLiveResponseError.responseAlreadyActive) }
        let generation = (responseRuntime.generations[conversationID] ?? 0) + 1
        responseRuntime.generations[conversationID] = generation
        let baselineVisibleMessageCount = selectedConversationID == conversationID ? (selectedConversation?.messages.count ?? 0) : 0
        responseRuntime.snapshots[conversationID] = ConversationLiveResponseSnapshot(generation: generation, conversationID: conversationID, baselineVisibleMessageCount: baselineVisibleMessageCount, phase: .preparing, reasoningText: "", finalText: "", tools: [], reasoningEnded: false, failureReason: nil)
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["phase"] = ConversationLiveResponsePhase.preparing.rawValue
        fields["promptCharacters"] = String(promptCharacterCount)
        fields["baselineVisibleMessageCount"] = String(baselineVisibleMessageCount)
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.started", fields: fields)
        responseRuntime.onChange?(conversationID)
        return .success(generation)
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
        case .composerReady: eventName = "composer_ready"
        case .sendObserved: eventName = "send_observed"
        case .responseAccepted:
            snapshot.phase = .thinking
            eventName = "response_accepted"
        case .thinkingActive:
            if snapshot.phase != .final { snapshot.phase = .thinking }
            eventName = "thinking_active"
        case .reasoningPreamble(let text, let segmentStart):
            if segmentStart, !snapshot.reasoningText.isEmpty, !snapshot.reasoningText.hasSuffix("\n\n") { snapshot.reasoningText += "\n\n" }
            snapshot.reasoningText += text
            snapshot.phase = .reasoning
            eventName = "reasoning_preamble"
        case .reasoningDelta(let text):
            snapshot.reasoningText += text
            snapshot.phase = .reasoning
            eventName = "reasoning_delta"
        case .reasoningEnded:
            snapshot.reasoningEnded = true
            snapshot.phase = .final
            eventName = "reasoning_ended"
        case .finalDelta(let text):
            snapshot.finalText += text
            snapshot.phase = .final
            eventName = "final_delta"
        case .toolActivity(let slot, let title, let completed):
            if let index = snapshot.tools.firstIndex(where: { $0.slot == slot }) {
                if !title.isEmpty { snapshot.tools[index].title = title }
                snapshot.tools[index].completed = snapshot.tools[index].completed || completed
            } else {
                snapshot.tools.append(ConversationLiveTool(slot: slot, title: title.isEmpty ? "工具调用" : title, completed: completed))
                snapshot.tools.sort { $0.slot < $1.slot }
            }
            eventName = completed ? "tool_completed" : "tool_invoked"
        case .terminal:
            if !snapshot.reasoningEnded, snapshot.finalText.isEmpty, !snapshot.reasoningText.isEmpty {
                snapshot.finalText = snapshot.reasoningText
                snapshot.reasoningText = ""
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
        fields["reasoningCharacters"] = String(snapshot.reasoningText.count)
        fields["finalCharacters"] = String(snapshot.finalText.count)
        fields["toolCount"] = String(snapshot.tools.count)
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
    private let sendExecutor = CoveredWebSendExecutor()
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
            self.sendExecutor.resetForAccountChange()
            self.repository.resetAllLiveResponsesForAccountChange()
            self.sidebarViewController.resetForAccountScopeChange()
            self.detailViewController.resetForAccountScopeChange()
            self.detailNavigationController.setToolbarHidden(true, animated: false)
            self.show(.primary)
        }
        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.repository.selectConversation(id: id)
            self.detailViewController.loadViewIfNeeded()
            self.detailViewController.title = self.repository.conversations.first(where: { $0.id == id })?.title ?? "新对话"
            self.detailViewController.showConversation(id: id)
            self.detailNavigationController.setToolbarHidden(false, animated: false)
            self.updateLivePresentation()
            self.show(.secondary)
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
        sendExecutor.attachCoveredWebView(to: view)
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
        guard let conversationID = repository.selectedConversationID, !repository.isLiveResponseActive(for: conversationID), !sendExecutor.isBusy else { return }
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

    private func startValidationSend(text: String, conversationID: String) {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty, repository.selectedConversationID == conversationID, !sendExecutor.isBusy else { return }
        let generation: Int
        switch repository.beginLiveResponse(conversationID: conversationID, promptCharacterCount: trimmed.count) {
        case .success(let value): generation = value
        case .failure(let error):
            showValidationError(error.localizedDescription)
            return
        }
        updateLivePresentation()
        sendExecutor.sendExistingConversation(text: trimmed, conversationID: conversationID) { [weak self] event in
            guard let self else { return }
            self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            if case .terminal = event { self.reconcileTerminalResponse(conversationID: conversationID, generation: generation) }
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
        validationSendButton.isEnabled = !selectedResponseActive && !sendExecutor.isBusy
        validationSendButton.setTitle(selectedResponseActive ? "回答中…" : (sendExecutor.isBusy ? "其他会话回答中…" : "测试发送…"), for: .normal)
        detailViewController.navigationItem.rightBarButtonItem?.isEnabled = !selectedResponseActive
    }

    private func showValidationError(_ message: String) {
        let alert = UIAlertController(title: "无法发送", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "好", style: .default))
        present(alert, animated: true)
    }
}
