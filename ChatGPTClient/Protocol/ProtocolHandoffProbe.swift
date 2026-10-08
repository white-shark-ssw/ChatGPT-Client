import UIKit
import WebKit

private final class WeakProtocolHandoffProbeHandler: NSObject, WKScriptMessageHandler {
    weak var target: WKScriptMessageHandler?

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        target?.userContentController(userContentController, didReceive: message)
    }
}

final class ProtocolHandoffProbeViewController: UIViewController, WKNavigationDelegate, WKScriptMessageHandler {
    private static let handlerName = "protocolHandoffProbe"
    private static let chatURL = URL(string: "https://chatgpt.com/")!

    private let diagnostics = DiagnosticsLogger.shared
    private let statusLabel = UILabel()
    private let scriptHandler = WeakProtocolHandoffProbeHandler()
    private var webView: WKWebView!
    private var sendCount = 0
    private var originalStreamSignalCount = 0
    private var followupConnectionCount = 0
    private var continuationSignalCount = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "实时接管探测"
        view.backgroundColor = .systemBackground
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadPage))

        let explanationLabel = UILabel()
        explanationLabel.font = .preferredFont(forTextStyle: .footnote)
        explanationLabel.textColor = .secondaryLabel
        explanationLabel.numberOfLines = 0
        explanationLabel.text = "诊断专用：请直接使用官方 ChatGPT Web 正常发送。仅观察原始 Send SSE 中的 resume/turn/response 身份存在性，以及 Send 后官方页面自己建立的 fetch/XHR/EventSource/WebSocket 续流候选。不会记录提示词、回复/思考正文、Cookie、Authorization、原始 ID、resume token 值或 Sentinel/Turnstile/PoW/Conduit 值。"

        statusLabel.font = .monospacedSystemFont(ofSize: 11, weight: .regular)
        statusLabel.textColor = .secondaryLabel
        statusLabel.numberOfLines = 0

        let headerStack = UIStackView(arrangedSubviews: [explanationLabel, statusLabel])
        headerStack.axis = .vertical
        headerStack.spacing = 6
        headerStack.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(headerStack)

        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .default()
        scriptHandler.target = self
        configuration.userContentController.add(scriptHandler, name: Self.handlerName)
        configuration.userContentController.addUserScript(WKUserScript(source: Self.probeScript, injectionTime: .atDocumentStart, forMainFrameOnly: true))

        webView = WKWebView(frame: .zero, configuration: configuration)
        webView.navigationDelegate = self
        webView.allowsBackForwardNavigationGestures = true
        webView.scrollView.keyboardDismissMode = .interactive
        webView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(webView)

        NSLayoutConstraint.activate([
            headerStack.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 12),
            headerStack.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -12),
            headerStack.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 8),
            webView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            webView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            webView.topAnchor.constraint(equalTo: headerStack.bottomAnchor, constant: 8),
            webView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])

        updateStatusLabel()
        diagnostics.info(category: "protocol", name: "conversationHandoffProbe.opened", fields: ["mode": "visible_official_web_handoff_structural_v1"])
        webView.load(URLRequest(url: Self.chatURL))
    }

    deinit {
        webView?.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName)
    }

    @objc private func reloadPage() { webView.reload() }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "protocol", name: "conversationHandoffProbe.page", fields: ["state": "loaded", "pageKind": Self.pageKind(for: webView.url)])
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    private func logNavigationFailure(_ error: Error) {
        let nsError = error as NSError
        diagnostics.warning(category: "protocol", name: "conversationHandoffProbe.page", fields: ["state": "failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        guard message.name == Self.handlerName, let body = message.body as? [String: Any], let kind = body["kind"] as? String else { return }
        switch kind {
        case "send_request":
            sendCount += 1
            var fields = baseFields(body)
            fields["method"] = Self.safeToken(body["method"] as? String)
            fields["headerNames"] = Self.safeStringArray(body["headerNames"])
            fields["queryNames"] = Self.safeStringArray(body["queryNames"])
            fields["bodyShape"] = Self.structuralJSON(body["bodyShape"])
            diagnostics.info(category: "protocol", name: "conversationHandoffProbe.sendRequest", fields: fields)
            updateStatusLabel()
        case "response":
            var fields = baseFields(body)
            fields["httpStatus"] = Self.safeNumberString(body["status"])
            fields["contentType"] = Self.safeToken(body["contentType"] as? String)
            fields["responseHeaderNames"] = Self.safeStringArray(body["responseHeaderNames"])
            diagnostics.info(category: "protocol", name: "conversationHandoffProbe.response", fields: fields)
        case "original_stream_signal":
            originalStreamSignalCount += 1
            var fields = baseFields(body)
            appendSignalFields(body, to: &fields)
            diagnostics.info(category: "protocol", name: "conversationHandoffProbe.originalStreamSignal", fields: fields)
            updateStatusLabel()
        case "followup_open":
            followupConnectionCount += 1
            var fields = baseFields(body)
            fields["method"] = Self.safeToken(body["method"] as? String)
            fields["headerNames"] = Self.safeStringArray(body["headerNames"])
            fields["queryNames"] = Self.safeStringArray(body["queryNames"])
            fields["bodyShape"] = Self.structuralJSON(body["bodyShape"])
            diagnostics.info(category: "protocol", name: "conversationHandoffProbe.followupOpen", fields: fields)
            updateStatusLabel()
        case "continuation_signal":
            continuationSignalCount += 1
            var fields = baseFields(body)
            appendSignalFields(body, to: &fields)
            fields["payloadShape"] = Self.structuralJSON(body["payloadShape"])
            diagnostics.info(category: "protocol", name: "conversationHandoffProbe.continuationSignal", fields: fields)
            updateStatusLabel()
        case "transport_state":
            var fields = baseFields(body)
            fields["state"] = Self.safeToken(body["state"] as? String)
            fields["code"] = Self.safeNumberString(body["code"])
            diagnostics.info(category: "protocol", name: "conversationHandoffProbe.transportState", fields: fields)
        case "transport_error":
            diagnostics.warning(category: "protocol", name: "conversationHandoffProbe.transportError", fields: baseFields(body))
        default:
            break
        }
    }

    private func appendSignalFields(_ body: [String: Any], to fields: inout [String: String]) {
        fields["eventIndex"] = Self.safeNumberString(body["eventIndex"])
        fields["signature"] = Self.safeToken(body["signature"] as? String)
        fields["eventType"] = Self.safeToken(body["eventType"] as? String)
        fields["identityKeys"] = Self.safeStringArray(body["identityKeys"])
        fields["resumeConversationToken"] = Self.safeToken(body["resumeConversationToken"] as? String)
        fields["responseID"] = Self.safeToken(body["responseID"] as? String)
        fields["turnID"] = Self.safeToken(body["turnID"] as? String)
        fields["conversationID"] = Self.safeToken(body["conversationID"] as? String)
        fields["messageID"] = Self.safeToken(body["messageID"] as? String)
        fields["asyncTaskID"] = Self.safeToken(body["asyncTaskID"] as? String)
        fields["handoffLike"] = Self.safeBoolString(body["handoffLike"])
        fields["streamLike"] = Self.safeBoolString(body["streamLike"])
        fields["terminal"] = Self.safeBoolString(body["terminal"])
    }

    private func baseFields(_ body: [String: Any]) -> [String: String] {
        [
            "route": Self.safeToken(body["route"] as? String),
            "safePath": Self.safeToken(body["safePath"] as? String),
            "pageKind": Self.safeToken(body["pageKind"] as? String),
            "transport": Self.safeToken(body["transport"] as? String)
        ]
    }

    private func updateStatusLabel() {
        statusLabel.text = "Send \(sendCount) · 原流身份信号 \(originalStreamSignalCount) · 后续连接 \(followupConnectionCount) · 续流信号 \(continuationSignalCount)\n建议分别完成一次新会话和已有会话发送，再导出诊断 JSON。"
    }

    private static func pageKind(for url: URL?) -> String {
        guard let url, let host = url.host?.lowercased(), host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") else { return "external_or_unknown" }
        if url.path.hasPrefix("/c/") { return "existing_conversation" }
        if url.path.hasPrefix("/auth") { return "authentication" }
        return "new_or_other"
    }

    private static let safeTokenCharacters = CharacterSet(charactersIn: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_./:{}-+,")

    private static func safeToken(_ value: String?) -> String {
        guard let value, !value.isEmpty, value.count <= 180, value.unicodeScalars.allSatisfy({ safeTokenCharacters.contains($0) }) else { return "none_or_redacted" }
        return value
    }

    private static func safeStringArray(_ value: Any?) -> String {
        guard let values = value as? [Any] else { return "none" }
        return values.prefix(48).compactMap { $0 as? String }.map(safeToken).joined(separator: ",")
    }

    private static func safeNumberString(_ value: Any?) -> String {
        guard let number = value as? NSNumber else { return "none" }
        return number.stringValue
    }

    private static func safeBoolString(_ value: Any?) -> String {
        guard let number = value as? NSNumber else { return "false" }
        return number.boolValue ? "true" : "false"
    }

    private static func structuralJSON(_ value: Any?) -> String {
        guard let value, let sanitized = sanitizeStructure(value, depth: 0), JSONSerialization.isValidJSONObject(sanitized), let data = try? JSONSerialization.data(withJSONObject: sanitized, options: [.sortedKeys]), let text = String(data: data, encoding: .utf8) else { return "none" }
        return String(text.prefix(5000))
    }

    private static func sanitizeStructure(_ value: Any, depth: Int) -> Any? {
        guard depth <= 7 else { return "depth_limit" }
        if value is NSNull { return NSNull() }
        if let number = value as? NSNumber { return number }
        if let string = value as? String { return safeToken(string) }
        if let array = value as? [Any] { return array.prefix(32).compactMap { sanitizeStructure($0, depth: depth + 1) } }
        if let dictionary = value as? [String: Any] {
            var result: [String: Any] = [:]
            for key in dictionary.keys.sorted().prefix(64) {
                let safeKey = safeToken(key)
                guard safeKey != "none_or_redacted", let rawValue = dictionary[key], let sanitized = sanitizeStructure(rawValue, depth: depth + 1) else { continue }
                result[safeKey] = sanitized
            }
            return result
        }
        return "unsupported"
    }

    private static let probeScript = #"""
    (() => {
      if (window.__chatgptNativeHandoffProbeInstalled) return;
      window.__chatgptNativeHandoffProbeInstalled = true;
      const bridge = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.protocolHandoffProbe;
      if (!bridge) return;
      const post = value => { try { bridge.postMessage(value); } catch (_) {} };
      const pageKind = () => location.pathname.startsWith('/c/') ? 'existing_conversation' : (location.pathname.startsWith('/auth') ? 'authentication' : 'new_or_other');
      const safeProtocolValue = value => {
        if (typeof value !== 'string') return 'none';
        const s = value.trim();
        return /^[A-Za-z][A-Za-z0-9_.:+-]{0,63}$/.test(s) ? s : 'other_or_redacted';
      };
      const safeStructuralKey = value => {
        const s = String(value || '');
        return /^[A-Za-z_][A-Za-z0-9_.:-]{0,79}$/.test(s) ? s : '{key}';
      };
      const idShape = value => {
        if (typeof value !== 'string' || !value) return 'none';
        if (/^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(value)) return 'uuid';
        if (/^[A-Za-z0-9_-]{16,}$/.test(value)) return 'opaque';
        return 'other';
      };
      const sanitizeSegment = value => {
        const s = String(value || '');
        if (/^[0-9a-f]{8}-[0-9a-f-]{20,}$/i.test(s) || s.length > 28) return '{id}';
        return /^[A-Za-z0-9_.:{}+-]+$/.test(s) ? s : '{segment}';
      };
      const safePath = pathname => String(pathname || '').split('/').map(sanitizeSegment).join('/');
      const queryNames = url => {
        try { return Array.from(new URL(url, location.href).searchParams.keys()).map(safeStructuralKey).sort().slice(0, 32); }
        catch (_) { return []; }
      };
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');
      const classify = value => {
        try {
          const u = new URL(typeof value === 'string' ? value : value && value.url || '', location.href);
          const host = u.hostname.toLowerCase();
          if (!isChatGPTHost(host)) return null;
          const p = u.pathname;
          let route = null;
          if (p === '/backend-api/f/conversation') route = 'conversation_send';
          else if (/^\/backend-api\/conversation\/[^/]+\/stream_status$/.test(p)) route = 'stream_status';
          else if (/conversation-turn-|conversation_turn|turn-stream|turn_stream/i.test(p)) route = 'turn_stream';
          else if (/stream[_-]?handoff|handoff/i.test(p)) route = 'handoff_candidate';
          else if (p.startsWith('/backend-api/') && /(resume|subscribe|continuation|stream|turn|status)/i.test(p)) route = 'continuation_candidate';
          if (!route) return null;
          return { route, safePath: safePath(p), queryNames: queryNames(u.href) };
        } catch (_) { return null; }
      };
      const describe = (value, depth = 0) => {
        if (depth > 6) return { type: 'depth_limit' };
        if (value === null) return { type: 'null' };
        if (Array.isArray(value)) return { type: 'array', count: value.length, item: value.length ? describe(value[0], depth + 1) : { type: 'empty' } };
        const type = typeof value;
        if (type === 'object') {
          const rawKeys = Object.keys(value).slice(0, 64).sort();
          const keys = rawKeys.map(safeStructuralKey);
          const fields = {};
          rawKeys.forEach((rawKey, index) => { fields[keys[index]] = describe(value[rawKey], depth + 1); });
          return { type: 'object', keys, fields };
        }
        return { type };
      };
      const bodyShape = body => {
        if (body == null || body === '') return { type: 'none' };
        if (typeof body === 'string') {
          try { return describe(JSON.parse(body)); } catch (_) { return { type: 'string', json: false }; }
        }
        if (body instanceof URLSearchParams) return { type: 'url_search_params', keys: Array.from(body.keys()).slice(0, 40).map(safeStructuralKey).sort() };
        if (body instanceof FormData) return { type: 'form_data', keys: Array.from(body.keys()).slice(0, 40).map(safeStructuralKey).sort() };
        return { type: Object.prototype.toString.call(body).replace(/[^A-Za-z]/g, '_') };
      };
      const headerNames = (input, init) => {
        try {
          const headers = new Headers();
          if (input instanceof Request) input.headers.forEach((_, key) => headers.set(key, '1'));
          if (init && init.headers) new Headers(init.headers).forEach((_, key) => headers.set(key, '1'));
          return Array.from(headers.keys()).map(v => String(v).toLowerCase()).sort().slice(0, 48);
        } catch (_) { return []; }
      };
      const responseHeaderNames = response => {
        try { return Array.from(response.headers.keys()).map(v => String(v).toLowerCase()).sort().slice(0, 48); }
        catch (_) { return []; }
      };
      const scanIdentity = value => {
        const found = new Map();
        let handoffLike = false;
        let streamLike = false;
        let visited = 0;
        const walk = (node, depth) => {
          if (depth > 6 || visited > 300 || node == null) return;
          visited += 1;
          if (Array.isArray(node)) { node.slice(0, 32).forEach(item => walk(item, depth + 1)); return; }
          if (typeof node !== 'object') return;
          Object.keys(node).slice(0, 64).forEach(rawKey => {
            const key = String(rawKey || '').toLowerCase();
            const child = node[rawKey];
            if (key.includes('handoff')) handoffLike = true;
            if (key.includes('stream') || key.includes('resume') || key.includes('turn')) streamLike = true;
            if (['resume_conversation_token', 'response_id', 'turn_id', 'conversation_id', 'message_id', 'async_task_id', 'task_id', 'request_id'].includes(key) && !found.has(key)) found.set(key, idShape(child));
            walk(child, depth + 1);
          });
        };
        walk(value, 0);
        return {
          identityKeys: Array.from(found.keys()).sort(),
          resumeConversationToken: found.get('resume_conversation_token') || 'none',
          responseID: found.get('response_id') || 'none',
          turnID: found.get('turn_id') || 'none',
          conversationID: found.get('conversation_id') || 'none',
          messageID: found.get('message_id') || 'none',
          asyncTaskID: found.get('async_task_id') || found.get('task_id') || 'none',
          handoffLike,
          streamLike
        };
      };
      const summarizeData = data => {
        const trimmed = String(data || '').trim();
        if (trimmed === '[DONE]') return { signature: 'done', terminal: true, eventType: '', identityKeys: [], resumeConversationToken: 'none', responseID: 'none', turnID: 'none', conversationID: 'none', messageID: 'none', asyncTaskID: 'none', handoffLike: false, streamLike: false, payloadShape: { type: 'done' } };
        let payload;
        try { payload = JSON.parse(trimmed); } catch (_) { return { signature: 'non_json', terminal: false, eventType: '', identityKeys: [], resumeConversationToken: 'none', responseID: 'none', turnID: 'none', conversationID: 'none', messageID: 'none', asyncTaskID: 'none', handoffLike: false, streamLike: false, payloadShape: { type: 'non_json' } }; }
        if (typeof payload === 'string') return { signature: payload === 'v1' ? 'marker:v1' : 'json_string', terminal: false, eventType: '', identityKeys: [], resumeConversationToken: 'none', responseID: 'none', turnID: 'none', conversationID: 'none', messageID: 'none', asyncTaskID: 'none', handoffLike: false, streamLike: false, payloadShape: { type: 'string' } };
        const eventType = payload && typeof payload.type === 'string' ? safeProtocolValue(payload.type) : 'none';
        const identity = scanIdentity(payload);
        const signature = eventType !== 'none' ? 'type:' + eventType : (identity.identityKeys.length ? 'identity:' + identity.identityKeys.join('+') : 'object');
        return Object.assign({ signature, terminal: false, eventType, payloadShape: describe(payload) }, identity);
      };
      const postSignal = (kind, info, transport, eventIndex, summary) => post(Object.assign({ kind, transport, route: info.route, safePath: info.safePath, pageKind: pageKind(), eventIndex, signature: summary.signature, eventType: summary.eventType, terminal: !!summary.terminal, payloadShape: summary.payloadShape }, summary));
      const inspectSSE = async (response, info, kind) => {
        const reader = response.body && response.body.getReader ? response.body.getReader() : null;
        if (!reader) return;
        const decoder = new TextDecoder();
        let buffer = '';
        let eventIndex = 0;
        const seen = new Set();
        const consume = data => {
          if (!String(data || '').trim()) return;
          eventIndex += 1;
          const summary = summarizeData(data);
          const evidenceKey = [summary.signature, summary.identityKeys.join(','), summary.handoffLike ? 'h' : '', summary.streamLike ? 's' : ''].join('|');
          const interesting = summary.terminal || summary.identityKeys.length > 0 || summary.handoffLike || summary.eventType !== 'none';
          if (interesting && !seen.has(evidenceKey)) { seen.add(evidenceKey); postSignal(kind, info, 'fetch', eventIndex, summary); }
        };
        try {
          while (eventIndex < 5000) {
            const result = await reader.read();
            buffer = (buffer + decoder.decode(result.value || new Uint8Array(), { stream: !result.done })).replace(/\r\n/g, '\n');
            let boundary;
            while ((boundary = buffer.indexOf('\n\n')) >= 0) {
              const frame = buffer.slice(0, boundary);
              buffer = buffer.slice(boundary + 2);
              const data = frame.split('\n').filter(line => line.startsWith('data:')).map(line => line.slice(5).trimStart()).join('\n');
              consume(data);
            }
            if (result.done) break;
          }
        } catch (_) {}
        try { reader.cancel(); } catch (_) {}
      };
      let sendSeen = false;
      const originalFetch = window.fetch.bind(window);
      window.fetch = async function(input, init) {
        const info = classify(input);
        const method = String((init && init.method) || (input instanceof Request && input.method) || 'GET').toUpperCase();
        const isSend = info && info.route === 'conversation_send';
        if (isSend) {
          sendSeen = true;
          post({ kind: 'send_request', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), method, headerNames: headerNames(input, init), queryNames: info.queryNames, bodyShape: init && Object.prototype.hasOwnProperty.call(init, 'body') ? bodyShape(init.body) : { type: 'request_or_none' } });
        } else if (sendSeen && info) {
          post({ kind: 'followup_open', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), method, headerNames: headerNames(input, init), queryNames: info.queryNames, bodyShape: init && Object.prototype.hasOwnProperty.call(init, 'body') ? bodyShape(init.body) : { type: 'request_or_none' } });
        }
        try {
          const response = await originalFetch(input, init);
          if (info && (isSend || sendSeen)) {
            const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
            post({ kind: 'response', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), status: response.status, contentType, responseHeaderNames: responseHeaderNames(response) });
            if (contentType === 'text/event-stream') inspectSSE(response.clone(), info, isSend ? 'original_stream_signal' : 'continuation_signal');
            else if (!isSend && contentType === 'application/json') {
              try { response.clone().json().then(payload => postSignal('continuation_signal', info, 'fetch', 1, Object.assign(summarizeData(JSON.stringify(payload)), { payloadShape: describe(payload) }))).catch(() => {}); } catch (_) {}
            }
          }
          return response;
        } catch (error) {
          if (info && (isSend || sendSeen)) post({ kind: 'transport_error', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind() });
          throw error;
        }
      };
      const OriginalEventSource = window.EventSource;
      if (OriginalEventSource) {
        try {
          const WrappedEventSource = function(url, configuration) {
            const info = classify(url);
            const instance = new OriginalEventSource(url, configuration);
            if (sendSeen && info) {
              post({ kind: 'followup_open', transport: 'eventsource', route: info.route, safePath: info.safePath, pageKind: pageKind(), method: 'GET', headerNames: [], queryNames: info.queryNames, bodyShape: { type: 'none' } });
              instance.addEventListener('open', () => post({ kind: 'transport_state', transport: 'eventsource', route: info.route, safePath: info.safePath, pageKind: pageKind(), state: 'open' }));
              instance.addEventListener('message', event => postSignal('continuation_signal', info, 'eventsource', 1, summarizeData(event.data)));
              instance.addEventListener('error', () => post({ kind: 'transport_error', transport: 'eventsource', route: info.route, safePath: info.safePath, pageKind: pageKind() }));
            }
            return instance;
          };
          WrappedEventSource.prototype = OriginalEventSource.prototype;
          Object.setPrototypeOf(WrappedEventSource, OriginalEventSource);
          window.EventSource = WrappedEventSource;
        } catch (_) {}
      }
      const OriginalWebSocket = window.WebSocket;
      if (OriginalWebSocket) {
        try {
          const WrappedWebSocket = function(url, protocols) {
            const info = classify(url);
            const instance = protocols === undefined ? new OriginalWebSocket(url) : new OriginalWebSocket(url, protocols);
            if (sendSeen && info) {
              post({ kind: 'followup_open', transport: 'websocket', route: info.route, safePath: info.safePath, pageKind: pageKind(), method: 'CONNECT', headerNames: [], queryNames: info.queryNames, bodyShape: { type: 'none' } });
              instance.addEventListener('open', () => post({ kind: 'transport_state', transport: 'websocket', route: info.route, safePath: info.safePath, pageKind: pageKind(), state: 'open' }));
              instance.addEventListener('message', event => {
                if (typeof event.data === 'string') postSignal('continuation_signal', info, 'websocket', 1, summarizeData(event.data));
                else post({ kind: 'continuation_signal', transport: 'websocket', route: info.route, safePath: info.safePath, pageKind: pageKind(), eventIndex: 1, signature: 'binary', eventType: 'none', identityKeys: [], resumeConversationToken: 'none', responseID: 'none', turnID: 'none', conversationID: 'none', messageID: 'none', asyncTaskID: 'none', handoffLike: false, streamLike: true, terminal: false, payloadShape: { type: 'binary' } });
              });
              instance.addEventListener('close', event => post({ kind: 'transport_state', transport: 'websocket', route: info.route, safePath: info.safePath, pageKind: pageKind(), state: 'close', code: event.code }));
              instance.addEventListener('error', () => post({ kind: 'transport_error', transport: 'websocket', route: info.route, safePath: info.safePath, pageKind: pageKind() }));
            }
            return instance;
          };
          WrappedWebSocket.prototype = OriginalWebSocket.prototype;
          Object.setPrototypeOf(WrappedWebSocket, OriginalWebSocket);
          window.WebSocket = WrappedWebSocket;
        } catch (_) {}
      }
      const originalOpen = XMLHttpRequest.prototype.open;
      const originalSetRequestHeader = XMLHttpRequest.prototype.setRequestHeader;
      const originalSend = XMLHttpRequest.prototype.send;
      XMLHttpRequest.prototype.open = function(method, url) {
        this.__handoffProbe = { info: classify(url), method: String(method || 'GET').toUpperCase(), headerNames: [] };
        return originalOpen.apply(this, arguments);
      };
      XMLHttpRequest.prototype.setRequestHeader = function(name, value) {
        if (this.__handoffProbe && this.__handoffProbe.info) this.__handoffProbe.headerNames.push(String(name || '').toLowerCase());
        return originalSetRequestHeader.apply(this, arguments);
      };
      XMLHttpRequest.prototype.send = function(body) {
        const probe = this.__handoffProbe;
        if (probe && probe.info) {
          const isSend = probe.info.route === 'conversation_send';
          if (isSend) sendSeen = true;
          if (isSend || sendSeen) post({ kind: isSend ? 'send_request' : 'followup_open', transport: 'xhr', route: probe.info.route, safePath: probe.info.safePath, pageKind: pageKind(), method: probe.method, headerNames: Array.from(new Set(probe.headerNames)).sort(), queryNames: probe.info.queryNames, bodyShape: bodyShape(body) });
          this.addEventListener('loadend', () => {
            const contentType = String(this.getResponseHeader('content-type') || '').split(';')[0].trim().toLowerCase();
            post({ kind: 'response', transport: 'xhr', route: probe.info.route, safePath: probe.info.safePath, pageKind: pageKind(), status: this.status, contentType, responseHeaderNames: [] });
            if (!isSend && contentType === 'application/json') {
              try { const payload = JSON.parse(this.responseText); postSignal('continuation_signal', probe.info, 'xhr', 1, Object.assign(summarizeData(JSON.stringify(payload)), { payloadShape: describe(payload) })); } catch (_) {}
            }
          }, { once: true });
        }
        return originalSend.apply(this, arguments);
      };
    })();
    """#
}
