from pathlib import Path
from textwrap import dedent
import json

ROOT = Path('.')
PROTOCOL = ROOT / 'ChatGPTClient/Protocol/ProtocolReadProbe.swift'
SETTINGS = ROOT / 'ChatGPTClient/SettingsViewController.swift'
FIXTURE_TRANSPORT = ROOT / 'ChatGPTClient/Testing/SimulatorFixtureTransport.swift'
TESTS = ROOT / 'ChatGPTClientTests/ConversationRepositorySimulatorTests.swift'
SIM_WORKFLOW = ROOT / '.github/workflows/ios-simulator-preflight.yml'
SANITIZER = ROOT / 'scripts/protocol_capture/sanitize_capture.py'
SANITIZER_README = ROOT / 'scripts/protocol_capture/README.md'
STOP_FIXTURE = ROOT / 'fixtures/protocol/stop-request-ack-v1.json'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly one match, found {count}')
    return text.replace(old, new, 1)


capture_js = r'''
    (() => {
      if (window.__authenticatedProtocolCaptureInstalled) return;
      window.__authenticatedProtocolCaptureInstalled = true;
      const bridge = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.protocolSendProbe;
      if (!bridge) return;
      const emit = event => { try { bridge.postMessage({ kind: 'authenticated_capture_event', event }); } catch (_) {} };
      const documentID = (globalThis.crypto && typeof globalThis.crypto.randomUUID === 'function') ? globalThis.crypto.randomUUID() : String(Date.now()) + '-' + String(Math.random()).slice(2);
      let requestSequence = 0;
      const secretPattern = /(password|passwd|token|cookie|authorization|credential|secret|oauth|session|proof|turnstile|conduit)/i;
      const identifierPattern = /(^id$|_id$|Id$|conversation|message|parent|response|request_id|user_id|account_id|workspace_id|node_id)/i;
      const safeTokenKeyPattern = /^(action|status|state|type|kind|role|recipient|content_type|conversation_async_status|finish_type|model|thinking_effort)$/i;
      const safeKey = value => /^[A-Za-z_][A-Za-z0-9_.:-]{0,79}$/.test(String(value || '')) ? String(value) : '{key}';
      const idRef = value => ({ __captureID: String(value) });
      const safeToken = value => typeof value === 'string' && /^[A-Za-z0-9_.:/+-]{0,100}$/.test(value) ? value : null;
      const sanitizeValue = (value, key = '', depth = 0) => {
        if (depth > 7) return { type: 'depth_limit' };
        if (secretPattern.test(String(key || ''))) return { type: 'redacted' };
        if (value === null) return null;
        if (Array.isArray(value)) return { type: 'array', count: value.length, items: value.slice(0, 64).map(item => sanitizeValue(item, key, depth + 1)) };
        const type = typeof value;
        if (type === 'boolean' || type === 'number') return value;
        if (type === 'string') {
          if (identifierPattern.test(String(key || '')) && value) return idRef(value);
          if (safeTokenKeyPattern.test(String(key || ''))) {
            const token = safeToken(value);
            if (token !== null) return token;
          }
          return { type: 'string', length: value.length };
        }
        if (type === 'object') {
          const result = {};
          Object.keys(value).slice(0, 96).sort().forEach(rawKey => {
            const keyName = safeKey(rawKey);
            result[keyName] = sanitizeValue(value[rawKey], rawKey, depth + 1);
          });
          return result;
        }
        return { type };
      };
      const parseBody = body => {
        if (body == null || body === '') return null;
        if (typeof body === 'string') { try { return JSON.parse(body); } catch (_) { return null; } }
        if (body instanceof URLSearchParams) {
          const value = {};
          body.forEach((entry, key) => { value[key] = entry; });
          return value;
        }
        return null;
      };
      const summarizeBody = body => {
        const parsed = parseBody(body);
        return parsed === null ? { type: body == null || body === '' ? 'none' : 'non_json' } : sanitizeValue(parsed);
      };
      const safePathSegment = value => {
        const s = String(value || '');
        if (/^[A-Za-z0-9_.:{}+-]{1,36}$/.test(s)) return s;
        return '{opaque}';
      };
      const requestInfo = raw => {
        try {
          const url = new URL(raw instanceof Request ? raw.url : String(raw || ''), location.href);
          const host = url.hostname.toLowerCase();
          if (!(host === 'chatgpt.com' || host.endsWith('.chatgpt.com'))) return null;
          if (!url.pathname.startsWith('/backend-api/')) return null;
          const p = url.pathname;
          let route = 'backend_api';
          let pathTemplate = p.split('/').map(safePathSegment).join('/');
          let pathParameters = {};
          if (p === '/backend-api/stop_conversation') { route = 'stop_conversation'; pathTemplate = p; }
          else if (p === '/backend-api/f/conversation') { route = 'conversation_send'; pathTemplate = p; }
          else {
            const pluralDetail = p.match(/^\/backend-api\/conversations\/([^/]+)\/?$/);
            if (pluralDetail) {
              route = 'conversation_detail_web';
              pathTemplate = '/backend-api/conversations/{conversation_id}';
              pathParameters = { conversation_id: idRef(decodeURIComponent(pluralDetail[1])) };
            }
          }
          const query = {};
          url.searchParams.forEach((value, key) => { query[safeKey(key)] = sanitizeValue(value, key); });
          return { route, pathTemplate, pathParameters, query };
        } catch (_) { return null; }
      };
      const headerNames = (input, init) => {
        try {
          const headers = new Headers();
          if (input instanceof Request) input.headers.forEach((_, key) => headers.set(key, '1'));
          if (init && init.headers) new Headers(init.headers).forEach((_, key) => headers.set(key, '1'));
          return Array.from(headers.keys()).map(v => String(v).toLowerCase()).sort().slice(0, 64);
        } catch (_) { return []; }
      };
      const stopRequestFixture = body => {
        const payload = parseBody(body);
        if (!payload || typeof payload !== 'object' || Array.isArray(payload)) return null;
        if (typeof payload.conversation_id !== 'string' || !Array.isArray(payload.exclude_async_types)) return null;
        return { conversation_id: idRef(payload.conversation_id), exclude_async_types: payload.exclude_async_types.slice(0, 32).map(value => sanitizeValue(value, 'exclude_async_types')) };
      };
      const stopResponseFixture = payload => {
        if (!payload || typeof payload !== 'object' || Array.isArray(payload)) return null;
        return {
          last_message_id: payload.last_message_id === null ? null : (typeof payload.last_message_id === 'string' ? idRef(payload.last_message_id) : sanitizeValue(payload.last_message_id, 'last_message_id')),
          status: safeToken(payload.status) || sanitizeValue(payload.status, 'status')
        };
      };
      const messageProjection = message => {
        if (!message || typeof message !== 'object') return null;
        const content = message.content && typeof message.content === 'object' ? message.content : {};
        const parts = Array.isArray(content.parts) ? content.parts : [];
        const metadata = message.metadata && typeof message.metadata === 'object' ? message.metadata : {};
        const finishDetails = metadata.finish_details && typeof metadata.finish_details === 'object' ? metadata.finish_details : null;
        return {
          messageID: typeof message.id === 'string' ? idRef(message.id) : null,
          role: safeToken(message.author && message.author.role) || null,
          status: safeToken(message.status) || null,
          endTurn: typeof message.end_turn === 'boolean' ? message.end_turn : null,
          recipient: safeToken(message.recipient) || null,
          contentType: safeToken(content.content_type) || null,
          partCount: parts.length,
          textCharacters: parts.reduce((sum, part) => sum + (typeof part === 'string' ? part.length : 0), 0),
          metadataKeys: Object.keys(metadata).slice(0, 96).map(safeKey).sort(),
          finishType: finishDetails ? (safeToken(finishDetails.type) || null) : null
        };
      };
      const detailProjection = payload => {
        if (!payload || typeof payload !== 'object' || Array.isArray(payload)) return null;
        const mapping = payload.mapping && typeof payload.mapping === 'object' && !Array.isArray(payload.mapping) ? payload.mapping : {};
        const currentNode = typeof payload.current_node === 'string' ? payload.current_node : null;
        const nodes = [];
        let cursor = currentNode;
        let depth = 0;
        const seen = new Set();
        while (cursor && mapping[cursor] && depth < 16 && !seen.has(cursor)) {
          seen.add(cursor);
          const node = mapping[cursor];
          nodes.push({
            nodeID: idRef(cursor),
            parentID: typeof node.parent === 'string' ? idRef(node.parent) : null,
            message: messageProjection(node.message)
          });
          cursor = typeof node.parent === 'string' ? node.parent : null;
          depth += 1;
        }
        nodes.reverse();
        const conversationID = typeof payload.conversation_id === 'string' ? payload.conversation_id : (typeof payload.id === 'string' ? payload.id : null);
        return {
          conversationID: conversationID ? idRef(conversationID) : null,
          currentNode: currentNode ? idRef(currentNode) : null,
          asyncStatus: sanitizeValue(payload.conversation_async_status, 'conversation_async_status'),
          mappingCount: Object.keys(mapping).length,
          nodes
        };
      };
      const emitRequest = (requestID, info, method, transport, headers, body) => emit({
        kind: 'request', documentID, requestID, transport, method, route: info.route, pathTemplate: info.pathTemplate,
        pathParameters: info.pathParameters, query: info.query, headerNames: headers, body: summarizeBody(body),
        fixtureBody: info.route === 'stop_conversation' ? stopRequestFixture(body) : null,
        relativeMs: Math.round(performance.now() * 100) / 100
      });
      const emitRequestBody = (requestID, info, body) => emit({
        kind: 'request_body', documentID, requestID, route: info.route, body: summarizeBody(body),
        fixtureBody: info.route === 'stop_conversation' ? stopRequestFixture(body) : null,
        relativeMs: Math.round(performance.now() * 100) / 100
      });
      const inspectSSE = async (response, requestID, info) => {
        const reader = response.body && response.body.getReader ? response.body.getReader() : null;
        if (!reader) return;
        const decoder = new TextDecoder();
        let buffer = '';
        let eventIndex = 0;
        try {
          while (eventIndex < 5000) {
            const result = await reader.read();
            buffer = (buffer + decoder.decode(result.value || new Uint8Array(), { stream: !result.done })).replace(/\r\n/g, '\n');
            let boundary;
            while ((boundary = buffer.indexOf('\n\n')) >= 0 && eventIndex < 5000) {
              const frame = buffer.slice(0, boundary);
              buffer = buffer.slice(boundary + 2);
              const data = frame.split('\n').filter(line => line.startsWith('data:')).map(line => line.slice(5).trimStart()).join('\n');
              if (!data.trim()) continue;
              eventIndex += 1;
              let payload;
              if (data.trim() === '[DONE]') payload = { terminal: true, marker: 'DONE' };
              else { try { payload = sanitizeValue(JSON.parse(data)); } catch (_) { payload = { type: 'non_json', length: data.length }; } }
              emit({ kind: 'sse_event', documentID, requestID, route: info.route, eventIndex, payload, relativeMs: Math.round(performance.now() * 100) / 100 });
            }
            if (result.done) break;
          }
        } catch (_) {}
        try { reader.cancel(); } catch (_) {}
        emit({ kind: 'sse_end', documentID, requestID, route: info.route, eventCount: eventIndex, relativeMs: Math.round(performance.now() * 100) / 100 });
      };
      const previousFetch = window.fetch.bind(window);
      window.fetch = async function(input, init) {
        const info = requestInfo(input);
        if (!info) return previousFetch(input, init);
        const requestID = documentID + ':' + String(++requestSequence);
        const method = String((init && init.method) || (input instanceof Request && input.method) || 'GET').toUpperCase();
        const headers = headerNames(input, init);
        if (init && Object.prototype.hasOwnProperty.call(init, 'body')) emitRequest(requestID, info, method, 'fetch', headers, init.body);
        else {
          emitRequest(requestID, info, method, 'fetch', headers, null);
          if (input instanceof Request) {
            try { input.clone().text().then(body => emitRequestBody(requestID, info, body)).catch(() => {}); } catch (_) {}
          }
        }
        try {
          const response = await previousFetch(input, init);
          const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
          emit({ kind: 'response', documentID, requestID, route: info.route, status: response.status, contentType, relativeMs: Math.round(performance.now() * 100) / 100 });
          if (contentType === 'application/json') {
            try {
              response.clone().json().then(payload => emit({
                kind: 'response_body', documentID, requestID, route: info.route, body: sanitizeValue(payload),
                fixtureBody: info.route === 'stop_conversation' ? stopResponseFixture(payload) : null,
                detailProjection: info.route === 'conversation_detail_web' ? detailProjection(payload) : null,
                relativeMs: Math.round(performance.now() * 100) / 100
              })).catch(() => {});
            } catch (_) {}
          } else if (contentType === 'text/event-stream') {
            try { inspectSSE(response.clone(), requestID, info); } catch (_) {}
          }
          return response;
        } catch (error) {
          emit({ kind: 'transport_error', documentID, requestID, route: info.route, errorName: safeToken(error && error.name) || 'error', relativeMs: Math.round(performance.now() * 100) / 100 });
          throw error;
        }
      };
      const previousOpen = XMLHttpRequest.prototype.open;
      const previousSend = XMLHttpRequest.prototype.send;
      const previousSetRequestHeader = XMLHttpRequest.prototype.setRequestHeader;
      XMLHttpRequest.prototype.open = function(method, url) {
        this.__authenticatedCapture = { info: requestInfo(String(url || '')), method: String(method || 'GET').toUpperCase(), requestID: documentID + ':x' + String(++requestSequence), headerNames: [] };
        return previousOpen.apply(this, arguments);
      };
      XMLHttpRequest.prototype.setRequestHeader = function(name, value) {
        if (this.__authenticatedCapture && this.__authenticatedCapture.info) this.__authenticatedCapture.headerNames.push(String(name || '').toLowerCase());
        return previousSetRequestHeader.apply(this, arguments);
      };
      XMLHttpRequest.prototype.send = function(body) {
        const capture = this.__authenticatedCapture;
        if (capture && capture.info) {
          emitRequest(capture.requestID, capture.info, capture.method, 'xhr', Array.from(new Set(capture.headerNames)).sort(), body);
          this.addEventListener('loadend', () => {
            const contentType = String(this.getResponseHeader('content-type') || '').split(';')[0].trim().toLowerCase();
            emit({ kind: 'response', documentID, requestID: capture.requestID, route: capture.info.route, status: this.status, contentType, relativeMs: Math.round(performance.now() * 100) / 100 });
            if (contentType === 'application/json') {
              try {
                const payload = JSON.parse(this.responseText);
                emit({ kind: 'response_body', documentID, requestID: capture.requestID, route: capture.info.route, body: sanitizeValue(payload), fixtureBody: capture.info.route === 'stop_conversation' ? stopResponseFixture(payload) : null, detailProjection: capture.info.route === 'conversation_detail_web' ? detailProjection(payload) : null, relativeMs: Math.round(performance.now() * 100) / 100 });
              } catch (_) {}
            }
          }, { once: true });
        }
        return previousSend.apply(this, arguments);
      };
      try {
        const previousBeacon = navigator.sendBeacon && navigator.sendBeacon.bind(navigator);
        if (previousBeacon) navigator.sendBeacon = function(url, data) {
          const info = requestInfo(String(url || ''));
          if (info) emitRequest(documentID + ':b' + String(++requestSequence), info, 'POST', 'beacon', [], data);
          return previousBeacon(url, data);
        };
      } catch (_) {}
    })();
'''.rstrip()


capture_swift = r'''

private final class AuthenticatedProtocolCaptureStore {
    private static let schema = "authenticated-protocol-capture-v1"
    private static let maxEvents = 5000
    private static let secretFragments = ["password", "passwd", "token", "cookie", "authorization", "credential", "secret", "oauth", "session", "proof", "turnstile", "conduit"]

    private let lock = NSLock()
    private let diagnostics = DiagnosticsLogger.shared
    private var active = false
    private var captureID = UUID().uuidString
    private var startedAt: Date?
    private var stoppedAt: Date?
    private var events: [[String: Any]] = []
    private var identifierAliases: [String: String] = [:]

    var isActive: Bool { lock.withLock { active } }
    var eventCount: Int { lock.withLock { events.count } }

    func start() {
        lock.withLock {
            active = true
            captureID = UUID().uuidString
            startedAt = Date()
            stoppedAt = nil
            events.removeAll(keepingCapacity: true)
            identifierAliases.removeAll(keepingCapacity: true)
        }
        diagnostics.info(category: "protocolCapture", name: "capture.started", fields: ["schema": Self.schema])
    }

    func stop() {
        let count: Int = lock.withLock {
            active = false
            stoppedAt = Date()
            return events.count
        }
        diagnostics.info(category: "protocolCapture", name: "capture.stopped", fields: ["eventCount": String(count)])
    }

    func clear() {
        lock.withLock {
            active = false
            startedAt = nil
            stoppedAt = nil
            events.removeAll(keepingCapacity: false)
            identifierAliases.removeAll(keepingCapacity: false)
            captureID = UUID().uuidString
        }
        diagnostics.info(category: "protocolCapture", name: "capture.cleared")
    }

    func append(rawEvent: [String: Any]) {
        lock.withLock {
            guard active, events.count < Self.maxEvents, let event = sanitize(rawEvent, key: nil, depth: 0) as? [String: Any] else { return }
            events.append([
                "sequence": events.count + 1,
                "capturedAt": ISO8601DateFormatter().string(from: Date()),
                "event": event
            ])
        }
    }

    func export() throws -> URL {
        let snapshot: [String: Any] = lock.withLock {
            let metadata = AppBuildInfo.current
            return [
                "schema": Self.schema,
                "captureID": captureID,
                "startedAt": startedAt.map { ISO8601DateFormatter().string(from: $0) } ?? NSNull(),
                "stoppedAt": stoppedAt.map { ISO8601DateFormatter().string(from: $0) } ?? NSNull(),
                "sensitiveLocalEvidence": true,
                "credentialsPersisted": false,
                "metadata": [
                    "appVersion": metadata.appVersion,
                    "buildNumber": metadata.buildNumber,
                    "candidate": metadata.candidate,
                    "sourceCommit": metadata.sourceCommit,
                    "buildConfiguration": metadata.buildConfiguration,
                    "deploymentTarget": metadata.deploymentTarget,
                    "bundleIdentifier": metadata.bundleIdentifier,
                    "deviceClass": metadata.deviceClass,
                    "systemName": metadata.systemName,
                    "systemVersion": metadata.systemVersion
                ],
                "events": events
            ]
        }
        guard JSONSerialization.isValidJSONObject(snapshot) else { throw NSError(domain: "AuthenticatedProtocolCapture", code: 1, userInfo: [NSLocalizedDescriptionKey: "capture snapshot is not valid JSON"]) }
        let data = try JSONSerialization.data(withJSONObject: snapshot, options: [.prettyPrinted, .sortedKeys])
        let directory = FileManager.default.temporaryDirectory.appendingPathComponent("ProtocolCaptureExports", isDirectory: true)
        try FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true)
        let formatter = DateFormatter()
        formatter.locale = Locale(identifier: "en_US_POSIX")
        formatter.timeZone = TimeZone(secondsFromGMT: 0)
        formatter.dateFormat = "yyyyMMdd-HHmmss"
        let url = directory.appendingPathComponent("ChatGPTClient-ProtocolCapture-\(formatter.string(from: Date())).json")
        try data.write(to: url, options: .atomic)
        diagnostics.info(category: "protocolCapture", name: "capture.exported", fields: ["eventCount": String(snapshot["events"].flatMap { ($0 as? [[String: Any]])?.count } ?? 0), "byteCount": String(data.count)])
        return url
    }

    private func sanitize(_ value: Any, key: String?, depth: Int) -> Any? {
        if depth > 10 { return ["type": "depth_limit"] }
        if let dictionary = value as? [String: Any] {
            if dictionary.count == 1, let rawIdentifier = dictionary["__captureID"] as? String, !rawIdentifier.isEmpty { return alias(for: rawIdentifier) }
            var output: [String: Any] = [:]
            for rawKey in dictionary.keys.sorted().prefix(128) {
                let normalized = Self.normalize(rawKey)
                if Self.secretFragments.contains(where: { normalized.contains($0) }) { output[Self.safeKey(rawKey)] = "<redacted>"; continue }
                guard let child = dictionary[rawKey], let sanitized = sanitize(child, key: rawKey, depth: depth + 1) else { continue }
                output[Self.safeKey(rawKey)] = sanitized
            }
            return output
        }
        if let array = value as? [Any] { return array.prefix(256).compactMap { sanitize($0, key: key, depth: depth + 1) } }
        if value is NSNull { return NSNull() }
        if let number = value as? NSNumber { return number }
        if let string = value as? String {
            if let key, Self.secretFragments.contains(where: { Self.normalize(key).contains($0) }) { return "<redacted>" }
            let lower = string.lowercased()
            if lower.contains("bearer ") || lower.contains("set-cookie:") || lower.contains("authorization:") { return "<redacted>" }
            if string.range(of: #"^[A-Za-z0-9_./:{}+\-]{0,256}$"#, options: .regularExpression) != nil { return string }
            return ["type": "string", "length": string.count]
        }
        return nil
    }

    private func alias(for rawIdentifier: String) -> String {
        if let existing = identifierAliases[rawIdentifier] { return existing }
        let alias = String(format: "id-%04d", identifierAliases.count + 1)
        identifierAliases[rawIdentifier] = alias
        return alias
    }

    private static func normalize(_ key: String) -> String { key.lowercased().replacingOccurrences(of: "_", with: "").replacingOccurrences(of: "-", with: "").replacingOccurrences(of: ".", with: "") }
    private static func safeKey(_ key: String) -> String { key.range(of: #"^[A-Za-z_][A-Za-z0-9_.:-]{0,79}$"#, options: .regularExpression) != nil ? key : "{key}" }
}

private extension NSLock {
    func withLock<T>(_ body: () throws -> T) rethrows -> T { lock(); defer { unlock() }; return try body() }
}

final class AuthenticatedProtocolCaptureViewController: UIViewController, WKNavigationDelegate, WKScriptMessageHandler {
    private let diagnostics = DiagnosticsLogger.shared
    private let captureStore = AuthenticatedProtocolCaptureStore()
    private let scriptHandler = WeakProtocolSendProbeScriptHandler()
    private let statusLabel = UILabel()
    private let startButton = UIButton(type: .system)
    private let stopButton = UIButton(type: .system)
    private let exportButton = UIButton(type: .system)
    private let clearButton = UIButton(type: .system)
    private var webView: WKWebView!

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Authenticated Protocol Capture"
        view.backgroundColor = .systemBackground

        let explanation = UILabel()
        explanation.font = .preferredFont(forTextStyle: .footnote)
        explanation.textColor = .secondaryLabel
        explanation.numberOfLines = 0
        explanation.text = "开发诊断：使用当前设备默认 ChatGPT Web 登录态。开始后正常操作官方 Web；采集器自动记录协议结构、必要安全值、SSE 顺序和一次采集内稳定 ID 别名。Cookie、Authorization、Session/Access Token、密码和可复用认证值不会写入采集包。导出的采集包默认视为本地敏感证据，不会自动上传或提交仓库。"

        statusLabel.font = .monospacedSystemFont(ofSize: 11, weight: .regular)
        statusLabel.textColor = .secondaryLabel
        statusLabel.numberOfLines = 0

        startButton.setTitle("开始采集", for: .normal)
        startButton.addTarget(self, action: #selector(startCapture), for: .touchUpInside)
        stopButton.setTitle("停止采集", for: .normal)
        stopButton.addTarget(self, action: #selector(stopCapture), for: .touchUpInside)
        exportButton.setTitle("导出采集包", for: .normal)
        exportButton.addTarget(self, action: #selector(exportCapture), for: .touchUpInside)
        clearButton.setTitle("清空", for: .normal)
        clearButton.addTarget(self, action: #selector(clearCapture), for: .touchUpInside)
        let buttons = UIStackView(arrangedSubviews: [startButton, stopButton, exportButton, clearButton])
        buttons.axis = .horizontal
        buttons.distribution = .fillEqually
        buttons.spacing = 6

        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .default()
        scriptHandler.target = self
        configuration.userContentController.add(scriptHandler, name: ProtocolSendProbeViewController.handlerName)
        configuration.userContentController.addUserScript(WKUserScript(source: ProtocolSendProbeViewController.probeScript, injectionTime: .atDocumentStart, forMainFrameOnly: true))
        webView = WKWebView(frame: .zero, configuration: configuration)
        webView.navigationDelegate = self
        webView.allowsBackForwardNavigationGestures = true
        webView.translatesAutoresizingMaskIntoConstraints = false

        let header = UIStackView(arrangedSubviews: [explanation, statusLabel, buttons])
        header.axis = .vertical
        header.spacing = 8
        header.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(header)
        view.addSubview(webView)
        NSLayoutConstraint.activate([
            header.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 12),
            header.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -12),
            header.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 8),
            webView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            webView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            webView.topAnchor.constraint(equalTo: header.bottomAnchor, constant: 8),
            webView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])
        updateControls()
        diagnostics.info(category: "protocolCapture", name: "captureUI.opened", fields: ["store": "default_webkit", "autoInjected": "true"])
        webView.load(URLRequest(url: URL(string: "https://chatgpt.com/")!))
    }

    deinit { webView?.configuration.userContentController.removeScriptMessageHandler(forName: ProtocolSendProbeViewController.handlerName) }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) { updateControls() }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        guard message.name == ProtocolSendProbeViewController.handlerName, let body = message.body as? [String: Any], body["kind"] as? String == "authenticated_capture_event", let event = body["event"] as? [String: Any] else { return }
        captureStore.append(rawEvent: event)
        updateControls()
    }

    @objc private func startCapture() { captureStore.start(); updateControls() }
    @objc private func stopCapture() { captureStore.stop(); updateControls() }
    @objc private func clearCapture() { captureStore.clear(); updateControls() }

    @objc private func exportCapture() {
        guard !captureStore.isActive else { showAlert(title: "请先停止采集", message: "停止采集后再导出，确保采集边界明确。") ; return }
        exportButton.isEnabled = false
        DispatchQueue.global(qos: .utility).async { [weak self] in
            guard let self else { return }
            do {
                let url = try self.captureStore.export()
                DispatchQueue.main.async {
                    self.exportButton.isEnabled = true
                    let activity = UIActivityViewController(activityItems: [url], applicationActivities: nil)
                    activity.popoverPresentationController?.sourceView = self.exportButton
                    activity.popoverPresentationController?.sourceRect = self.exportButton.bounds
                    self.present(activity, animated: true)
                }
            } catch {
                DispatchQueue.main.async { self.exportButton.isEnabled = true; self.showAlert(title: "导出失败", message: error.localizedDescription) }
            }
        }
    }

    private func updateControls() {
        let active = captureStore.isActive
        startButton.isEnabled = !active
        stopButton.isEnabled = active
        clearButton.isEnabled = !active
        exportButton.isEnabled = !active && captureStore.eventCount > 0
        let host = webView?.url?.host ?? "未加载"
        statusLabel.text = "状态：\(active ? "采集中" : "未采集")\n事件：\(captureStore.eventCount)\n页面：\(host)"
    }

    private func showAlert(title: String, message: String) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "好", style: .default))
        present(alert, animated: true)
    }
}
'''.rstrip() + '\n'


protocol_text = PROTOCOL.read_text()
protocol_text = replace_once(protocol_text, '    private static let handlerName = "protocolSendProbe"', '    static let handlerName = "protocolSendProbe"', 'handlerName visibility')
protocol_text = replace_once(protocol_text, '    private static let probeScript = #"""', '    static let probeScript = #"""', 'probeScript visibility')
end_marker = '    })();\n    """#\n}'
protocol_text = replace_once(protocol_text, end_marker, '    })();\n' + capture_js + '\n    """#\n}' + capture_swift, 'protocol capture append')
PROTOCOL.write_text(protocol_text)

settings_text = SETTINGS.read_text()
settings_text = replace_once(
    settings_text,
    '        let protocolSendProbeButton = UIButton(type: .system)\n        protocolSendProbeButton.setTitle("Native 输入 / Web Send（b65诊断）", for: .normal)\n        protocolSendProbeButton.addTarget(self, action: #selector(openProtocolSendProbe), for: .touchUpInside)\n\n        let webRuleLabButton = UIButton(type: .system)',
    '        let protocolSendProbeButton = UIButton(type: .system)\n        protocolSendProbeButton.setTitle("Native 输入 / Web Send（b65诊断）", for: .normal)\n        protocolSendProbeButton.addTarget(self, action: #selector(openProtocolSendProbe), for: .touchUpInside)\n\n        let protocolCaptureButton = UIButton(type: .system)\n        protocolCaptureButton.setTitle("Authenticated Protocol Capture", for: .normal)\n        protocolCaptureButton.addTarget(self, action: #selector(openAuthenticatedProtocolCapture), for: .touchUpInside)\n\n        let webRuleLabButton = UIButton(type: .system)',
    'settings capture button')
settings_text = replace_once(settings_text, '            protocolSendProbeButton,\n            webRuleLabButton,', '            protocolSendProbeButton,\n            protocolCaptureButton,\n            webRuleLabButton,', 'settings stack')
settings_text = replace_once(
    settings_text,
    '    @objc private func openProtocolSendProbe() {\n        diagnostics.info(category: "navigation", name: "nativeWebSendEngineProbe.open")\n        navigationController?.pushViewController(NativeWebSendEngineProbeViewController(), animated: true)\n    }\n\n    @objc private func openWebRuleLab() {',
    '    @objc private func openProtocolSendProbe() {\n        diagnostics.info(category: "navigation", name: "nativeWebSendEngineProbe.open")\n        navigationController?.pushViewController(NativeWebSendEngineProbeViewController(), animated: true)\n    }\n\n    @objc private func openAuthenticatedProtocolCapture() {\n        diagnostics.info(category: "navigation", name: "authenticatedProtocolCapture.open")\n        navigationController?.pushViewController(AuthenticatedProtocolCaptureViewController(), animated: true)\n    }\n\n    @objc private func openWebRuleLab() {',
    'settings capture action')
SETTINGS.write_text(settings_text)

fixture_text = FIXTURE_TRANSPORT.read_text()
fixture_text = replace_once(fixture_text, '    static func resetRequestState() { SimulatorFixtureURLProtocol.reset() }\n    static func requestCount(for key: String) -> Int { SimulatorFixtureURLProtocol.requestCount(for: key) }', '    static func resetRequestState() { SimulatorFixtureURLProtocol.reset() }\n    static func installProtocolReplayFixture(data: Data) throws { try SimulatorFixtureURLProtocol.installProtocolReplayFixture(data: data) }\n    static func requestCount(for key: String) -> Int { SimulatorFixtureURLProtocol.requestCount(for: key) }', 'fixture public install')
fixture_text = replace_once(fixture_text, '        case success([String: Any])\n        case failure(String)', '        case success([String: Any])\n        case replay(statusCode: Int, contentType: String, payload: [String: Any])\n        case failure(String)', 'fixture replay enum')
fixture_text = replace_once(fixture_text, '    private static var requestCounts: [String: Int] = [:]\n    private static var requestObserver: ((String) -> Void)?', '    private static var requestCounts: [String: Int] = [:]\n    private static var requestObserver: ((String) -> Void)?\n    private static var replayInteractions: [[String: Any]] = []', 'fixture replay storage')
fixture_text = replace_once(fixture_text, '        guard let url = request.url, url.host?.lowercased() == "chatgpt.com" else { return false }\n        return url.path == "/backend-api/conversations" || url.path.hasPrefix("/backend-api/conversation/")', '        guard let url = request.url, url.host?.lowercased() == "chatgpt.com" else { return false }\n        if replayCanHandle(request) { return true }\n        return url.path == "/backend-api/conversations" || url.path.hasPrefix("/backend-api/conversation/")', 'fixture canInit')
fixture_text = replace_once(fixture_text, '        let key = Self.requestKey(for: url)\n        let count = Self.recordRequest(for: key)\n        let response = Self.fixtureResponse(for: url, requestCount: count)', '        let key = Self.requestKey(for: request)\n        let count = Self.recordRequest(for: key)\n        let response = Self.replayResponse(for: request, requestCount: count) ?? Self.fixtureResponse(for: url, requestCount: count)', 'fixture start replay')
fixture_text = replace_once(fixture_text, '            switch response {\n            case .success(let payload): self.finish(payload: payload)\n            case .failure(let reason): self.finishWithError(reason)\n            }', '            switch response {\n            case .success(let payload): self.finish(payload: payload)\n            case .replay(let statusCode, let contentType, let payload): self.finish(statusCode: statusCode, contentType: contentType, payload: payload)\n            case .failure(let reason): self.finishWithError(reason)\n            }', 'fixture response switch')
fixture_text = replace_once(fixture_text, '    private func finish(payload: [String: Any]) {\n        guard !workItemCancelled, let url = request.url else { return }\n        do {\n            let data = try JSONSerialization.data(withJSONObject: payload, options: [.sortedKeys])\n            let response = HTTPURLResponse(url: url, statusCode: 200, httpVersion: "HTTP/1.1", headerFields: ["Content-Type": "application/json", "Content-Length": String(data.count)])!\n            client?.urlProtocol(self, didReceive: response, cacheStoragePolicy: .notAllowed)\n            client?.urlProtocol(self, didLoad: data)\n            client?.urlProtocolDidFinishLoading(self)\n        } catch {\n            client?.urlProtocol(self, didFailWithError: error)\n        }\n    }', '    private func finish(payload: [String: Any]) { finish(statusCode: 200, contentType: "application/json", payload: payload) }\n\n    private func finish(statusCode: Int, contentType: String, payload: [String: Any]) {\n        guard !workItemCancelled, let url = request.url else { return }\n        do {\n            let data = try JSONSerialization.data(withJSONObject: payload, options: [.sortedKeys])\n            let response = HTTPURLResponse(url: url, statusCode: statusCode, httpVersion: "HTTP/1.1", headerFields: ["Content-Type": contentType, "Content-Length": String(data.count)])!\n            client?.urlProtocol(self, didReceive: response, cacheStoragePolicy: .notAllowed)\n            client?.urlProtocol(self, didLoad: data)\n            client?.urlProtocolDidFinishLoading(self)\n        } catch {\n            client?.urlProtocol(self, didFailWithError: error)\n        }\n    }', 'fixture finish status')
fixture_text = replace_once(fixture_text, '        requestCounts.removeAll()\n        requestObserver = nil', '        requestCounts.removeAll()\n        requestObserver = nil\n        replayInteractions.removeAll()', 'fixture reset replay')
fixture_text = replace_once(fixture_text, '    private static func requestKey(for url: URL) -> String {\n        if url.path == "/backend-api/conversations" { return "list" }\n        return "detail:" + String(url.path.dropFirst("/backend-api/conversation/".count))\n    }', '''    fileprivate static func installProtocolReplayFixture(data: Data) throws {
        guard let root = try JSONSerialization.jsonObject(with: data) as? [String: Any], root["schema"] as? String == "protocol-replay-fixture-v1", let interactions = root["interactions"] as? [[String: Any]], !interactions.isEmpty else {
            throw NSError(domain: "SimulatorFixtureTransport", code: 2, userInfo: [NSLocalizedDescriptionKey: "invalid protocol replay fixture"])
        }
        lock.lock()
        replayInteractions = interactions
        requestCounts.removeAll()
        lock.unlock()
    }

    private static func replayCanHandle(_ request: URLRequest) -> Bool {
        guard let url = request.url else { return false }
        let method = (request.httpMethod ?? "GET").uppercased()
        lock.lock()
        let result = replayInteractions.contains { interaction in
            guard let fixtureRequest = interaction["request"] as? [String: Any] else { return false }
            return (fixtureRequest["method"] as? String)?.uppercased() == method && fixtureRequest["path"] as? String == url.path
        }
        lock.unlock()
        return result
    }

    private static func replayResponse(for request: URLRequest, requestCount: Int) -> FixtureResponse? {
        guard let url = request.url else { return nil }
        let method = (request.httpMethod ?? "GET").uppercased()
        lock.lock()
        let matches = replayInteractions.filter { interaction in
            guard let fixtureRequest = interaction["request"] as? [String: Any] else { return false }
            return (fixtureRequest["method"] as? String)?.uppercased() == method && fixtureRequest["path"] as? String == url.path
        }
        lock.unlock()
        guard !matches.isEmpty else { return nil }
        let interaction = matches[min(max(requestCount - 1, 0), matches.count - 1)]
        guard let fixtureRequest = interaction["request"] as? [String: Any], let fixtureResponse = interaction["response"] as? [String: Any], let statusCode = (fixtureResponse["status"] as? NSNumber)?.intValue, let contentType = fixtureResponse["contentType"] as? String, let payload = fixtureResponse["body"] as? [String: Any] else { return .failure("invalid_protocol_replay_interaction") }
        if let expectedBody = fixtureRequest["body"] as? [String: Any] {
            guard let body = request.httpBody, let actualBody = try? JSONSerialization.jsonObject(with: body) as? [String: Any], jsonObjectsEqual(expectedBody, actualBody) else { return .failure("protocol_replay_request_body_mismatch") }
        }
        return .replay(statusCode: statusCode, contentType: contentType, payload: payload)
    }

    private static func jsonObjectsEqual(_ lhs: [String: Any], _ rhs: [String: Any]) -> Bool {
        guard let leftData = try? JSONSerialization.data(withJSONObject: lhs, options: [.sortedKeys]), let rightData = try? JSONSerialization.data(withJSONObject: rhs, options: [.sortedKeys]) else { return false }
        return leftData == rightData
    }

    private static func requestKey(for request: URLRequest) -> String {
        guard let url = request.url else { return "missing-url" }
        if replayCanHandle(request) { return "replay:\((request.httpMethod ?? "GET").uppercased()):\(url.path)" }
        if url.path == "/backend-api/conversations" { return "list" }
        return "detail:" + String(url.path.dropFirst("/backend-api/conversation/".count))
    }''', 'fixture replay helpers')
FIXTURE_TRANSPORT.write_text(fixture_text)

tests_text = TESTS.read_text()
new_test = r'''

    func testSanitizedProtocolReplayFixtureReplaysStopRequestAndAckWithoutNetwork() async throws {
        SimulatorFixtureTransport.resetRequestState()
        let fixtureURL = URL(fileURLWithPath: #filePath).deletingLastPathComponent().deletingLastPathComponent().appendingPathComponent("fixtures/protocol/stop-request-ack-v1.json")
        try SimulatorFixtureTransport.installProtocolReplayFixture(data: Data(contentsOf: fixtureURL))
        defer { SimulatorFixtureTransport.resetRequestState() }

        var request = URLRequest(url: URL(string: "https://chatgpt.com/backend-api/stop_conversation")!)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONSerialization.data(withJSONObject: ["conversation_id": "id-0001", "exclude_async_types": []], options: [.sortedKeys])
        let (data, response) = try await performFixtureRequest(request)
        XCTAssertEqual(response.statusCode, 200)
        XCTAssertEqual(response.value(forHTTPHeaderField: "Content-Type"), "application/json")
        let payload = try XCTUnwrap(try JSONSerialization.jsonObject(with: data) as? [String: Any])
        XCTAssertEqual(payload["status"] as? String, "ok")
        XCTAssertTrue(payload["last_message_id"] is NSNull)
        XCTAssertEqual(SimulatorFixtureTransport.requestCount(for: "replay:POST:/backend-api/stop_conversation"), 1)
    }
'''
tests_text = replace_once(tests_text, '\n    @MainActor\n    private func loadConversations', new_test + '\n    @MainActor\n    private func loadConversations', 'protocol replay test insert')
helper = r'''

    private func performFixtureRequest(_ request: URLRequest) async throws -> (Data, HTTPURLResponse) {
        try await withCheckedThrowingContinuation { continuation in
            let session = URLSession(configuration: SimulatorFixtureTransport.makeSessionConfiguration())
            session.dataTask(with: request) { data, response, error in
                defer { session.finishTasksAndInvalidate() }
                if let error { continuation.resume(throwing: error); return }
                guard let data, let response = response as? HTTPURLResponse else {
                    continuation.resume(throwing: NSError(domain: "ConversationRepositorySimulatorTests", code: 1, userInfo: [NSLocalizedDescriptionKey: "missing fixture response"]))
                    return
                }
                continuation.resume(returning: (data, response))
            }.resume()
        }
    }
'''
tests_text = replace_once(tests_text, '\n    @MainActor\n    private func loadConversation(_ repository: ConversationRepository, id: String) async throws -> ConversationDetail {', helper + '\n    @MainActor\n    private func loadConversation(_ repository: ConversationRepository, id: String) async throws -> ConversationDetail {', 'protocol replay helper insert')
TESTS.write_text(tests_text)

workflow_text = SIM_WORKFLOW.read_text()
workflow_text = replace_once(workflow_text, '      - name: Run XCTest and XCUITest\n        id: tests', '      - name: Validate protocol capture sanitizer\n        run: python3 scripts/protocol_capture/sanitize_capture.py --self-test\n\n      - name: Run XCTest and XCUITest\n        id: tests', 'simulator sanitizer self-test')
SIM_WORKFLOW.write_text(workflow_text)

SANITIZER.parent.mkdir(parents=True, exist_ok=True)
SANITIZER.write_text(dedent(r'''#!/usr/bin/env python3
import argparse
import json
import re
import tempfile
from pathlib import Path

SECRET_PATTERN = re.compile(r"password|passwd|token|cookie|authorization|credential|secret|oauth|session|proof|turnstile|conduit", re.I)
SECRET_VALUE_PATTERN = re.compile(r"bearer\s+|set-cookie:|authorization:|password=|session(token)?=", re.I)
SAFE_ALIAS = re.compile(r"^id-\d{4}$")


def scrub(value, key=""):
    if SECRET_PATTERN.search(key):
        return "<redacted>"
    if isinstance(value, dict):
        return {str(k): scrub(v, str(k)) for k, v in sorted(value.items()) if not SECRET_PATTERN.search(str(k))}
    if isinstance(value, list):
        return [scrub(item, key) for item in value]
    if isinstance(value, str):
        if SECRET_VALUE_PATTERN.search(value):
            return "<redacted>"
        return value
    return value


def materialize_path(template, parameters):
    path = str(template or "")
    for key, value in (parameters or {}).items():
        if not isinstance(value, str) or not SAFE_ALIAS.fullmatch(value):
            raise ValueError(f"unsafe or missing path alias for {key}")
        path = path.replace("{" + key + "}", value)
    if "{" in path or not path.startswith("/backend-api/"):
        raise ValueError(f"unresolved or unsafe replay path: {path}")
    return path


def detail_projection_to_body(projection):
    if not isinstance(projection, dict):
        raise ValueError("detail projection must be an object")
    conversation_id = projection.get("conversationID")
    current_node = projection.get("currentNode")
    if not isinstance(conversation_id, str) or not SAFE_ALIAS.fullmatch(conversation_id):
        raise ValueError("detail projection is missing a safe conversation alias")
    if not isinstance(current_node, str) or not SAFE_ALIAS.fullmatch(current_node):
        raise ValueError("detail projection is missing a safe current-node alias")
    nodes = projection.get("nodes") or []
    included = {node.get("nodeID") for node in nodes if isinstance(node, dict) and isinstance(node.get("nodeID"), str)}
    mapping = {}
    child_by_parent = {}
    for node in nodes:
        node_id = node.get("nodeID")
        if not isinstance(node_id, str) or not SAFE_ALIAS.fullmatch(node_id):
            continue
        raw_parent = node.get("parentID")
        parent_id = raw_parent if isinstance(raw_parent, str) and raw_parent in included else None
        if parent_id:
            child_by_parent.setdefault(parent_id, []).append(node_id)
        message_projection = node.get("message")
        message = None
        if isinstance(message_projection, dict):
            message_id = message_projection.get("messageID")
            text_characters = int(message_projection.get("textCharacters") or 0)
            placeholder = f"[captured-text:{text_characters}]" if text_characters > 0 else ""
            message = {
                "id": message_id if isinstance(message_id, str) and SAFE_ALIAS.fullmatch(message_id) else f"{node_id}-message",
                "author": {"role": message_projection.get("role") or "unknown"},
                "content": {"content_type": message_projection.get("contentType") or "text", "parts": [placeholder] if placeholder else []},
                "status": message_projection.get("status") or "unknown",
                "end_turn": message_projection.get("endTurn"),
                "metadata": {"capture_original_text_characters": text_characters}
            }
            if message_projection.get("recipient"):
                message["recipient"] = message_projection["recipient"]
            if message_projection.get("finishType"):
                message["metadata"]["finish_details"] = {"type": message_projection["finishType"]}
        mapping[node_id] = {"id": node_id, "parent": parent_id, "children": [], "message": message}
    for parent, children in child_by_parent.items():
        if parent in mapping:
            mapping[parent]["children"] = children
    return {
        "conversation_id": conversation_id,
        "id": conversation_id,
        "current_node": current_node,
        "mapping": mapping,
        "conversation_async_status": projection.get("asyncStatus")
    }


def compile_fixture(capture):
    if capture.get("schema") != "authenticated-protocol-capture-v1":
        raise ValueError("unsupported capture schema")
    requests = {}
    responses = {}
    response_bodies = {}
    request_bodies = {}
    stream_events = {}
    for wrapper in capture.get("events") or []:
        event = wrapper.get("event") if isinstance(wrapper, dict) else None
        if not isinstance(event, dict):
            continue
        request_id = event.get("requestID")
        if not isinstance(request_id, str):
            continue
        kind = event.get("kind")
        if kind == "request": requests[request_id] = event
        elif kind == "request_body": request_bodies[request_id] = event
        elif kind == "response": responses[request_id] = event
        elif kind == "response_body": response_bodies[request_id] = event
        elif kind == "sse_event": stream_events.setdefault(request_id, []).append(event)

    interactions = []
    observations = []
    for request_id, request in requests.items():
        response = responses.get(request_id)
        body_event = response_bodies.get(request_id)
        if not response:
            continue
        route = request.get("route")
        fixture_request_body = request.get("fixtureBody")
        if fixture_request_body is None and request_id in request_bodies:
            fixture_request_body = request_bodies[request_id].get("fixtureBody")
        fixture_response_body = body_event.get("fixtureBody") if isinstance(body_event, dict) else None
        detail_projection = body_event.get("detailProjection") if isinstance(body_event, dict) else None
        replay_body = None
        if route == "stop_conversation" and isinstance(fixture_response_body, dict):
            replay_body = fixture_response_body
        elif route == "conversation_detail_web" and isinstance(detail_projection, dict):
            replay_body = detail_projection_to_body(detail_projection)
        if replay_body is not None:
            path = materialize_path(request.get("pathTemplate"), request.get("pathParameters") or {})
            interaction = {
                "request": {"method": request.get("method") or "GET", "path": path},
                "response": {"status": int(response.get("status") or 0), "contentType": response.get("contentType") or "application/json", "body": replay_body}
            }
            if isinstance(fixture_request_body, dict):
                interaction["request"]["body"] = fixture_request_body
            query = request.get("query")
            if isinstance(query, dict) and query:
                interaction["request"]["query"] = query
            interactions.append(interaction)
        if request_id in stream_events:
            observations.append({"route": route, "pathTemplate": request.get("pathTemplate"), "sseEvents": [event.get("payload") for event in stream_events[request_id]]})

    if not interactions and not observations:
        raise ValueError("capture contains no replayable protocol evidence")
    fixture = {"schema": "protocol-replay-fixture-v1", "sourceCaptureSchema": capture.get("schema"), "interactions": interactions}
    if observations:
        fixture["observations"] = observations
    fixture = scrub(fixture)
    encoded = json.dumps(fixture, ensure_ascii=False, sort_keys=True)
    if SECRET_VALUE_PATTERN.search(encoded) or re.search(r'"(?:authorization|cookie|accessToken|sessionToken|password)"', encoded, re.I):
        raise ValueError("secret-like value survived fixture compilation")
    return fixture


def self_test():
    capture = {
        "schema": "authenticated-protocol-capture-v1",
        "Authorization": "Bearer SHOULD-NOT-SURVIVE",
        "events": [
            {"event": {"kind": "request", "requestID": "doc:1", "route": "stop_conversation", "method": "POST", "pathTemplate": "/backend-api/stop_conversation", "pathParameters": {}, "query": {}, "fixtureBody": {"conversation_id": "id-0001", "exclude_async_types": []}, "cookie": "secret"}},
            {"event": {"kind": "response", "requestID": "doc:1", "route": "stop_conversation", "status": 200, "contentType": "application/json"}},
            {"event": {"kind": "response_body", "requestID": "doc:1", "route": "stop_conversation", "fixtureBody": {"last_message_id": None, "status": "ok", "sessionToken": "secret"}}}
        ]
    }
    fixture = compile_fixture(capture)
    text = json.dumps(fixture, sort_keys=True)
    assert "SHOULD-NOT-SURVIVE" not in text and "Bearer" not in text and "sessionToken" not in text and "cookie" not in text.lower()
    assert fixture["interactions"][0]["request"]["body"]["conversation_id"] == "id-0001"
    assert fixture["interactions"][0]["response"]["body"]["status"] == "ok"
    print("protocol capture sanitizer self-test: ok")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?")
    parser.add_argument("output", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.input or not args.output:
        parser.error("input and output are required unless --self-test is used")
    capture = json.loads(Path(args.input).read_text())
    fixture = compile_fixture(capture)
    Path(args.output).write_text(json.dumps(fixture, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
'''))

SANITIZER_README.write_text(dedent('''# Authenticated Protocol Capture fixtures

`sanitize_capture.py` converts a user-controlled real-device `authenticated-protocol-capture-v1` export into deterministic `protocol-replay-fixture-v1` input for the integrated Simulator fixture transport.

Security boundary:

- raw capture exports are local sensitive evidence and are never an automatic repository/CI input;
- the compiler drops secret-like keys and values and fails closed if reusable auth-shaped material survives output validation;
- repository fixtures may contain only endpoint/method/query structure, capture-local aliases, safe protocol enums/scalars, reduced authoritative state projections and placeholder message text lengths;
- Cookie, Authorization, access/session tokens, passwords, challenge/proof values and raw user/assistant text must never enter committed fixtures;
- aliases such as `id-0001` are capture-local correlation identities, not reversible service identifiers.

Typical developer flow:

1. On a logged-in user-controlled iPhone, open Settings -> Authenticated Protocol Capture.
2. Tap `开始采集`, perform the target operation normally in the embedded official Web surface, then tap `停止采集` and `导出采集包`.
3. Keep that export local/private. Run `python3 scripts/protocol_capture/sanitize_capture.py <capture.json> <fixture.json>` on the development side.
4. Review the generated fixture, then commit only the sanitized fixture if it is needed for regression coverage.
5. Simulator tests replay committed fixtures through the existing Debug-only `SimulatorFixtureTransport`; production `ConversationRepository`, `AuthSessionStore` and Web execution ownership remain unchanged.

Run `python3 scripts/protocol_capture/sanitize_capture.py --self-test` to verify the sanitizer's secret rejection/redaction path.
'''))

STOP_FIXTURE.parent.mkdir(parents=True, exist_ok=True)
STOP_FIXTURE.write_text(json.dumps({
    "schema": "protocol-replay-fixture-v1",
    "source": "Runtime-proven official Web Stop request/ack contract; no post-Stop Detail semantics inferred",
    "interactions": [{
        "request": {"method": "POST", "path": "/backend-api/stop_conversation", "body": {"conversation_id": "id-0001", "exclude_async_types": []}},
        "response": {"status": 200, "contentType": "application/json", "body": {"last_message_id": None, "status": "ok"}}
    }]
}, ensure_ascii=False, indent=2, sort_keys=True) + '\n')

print('authenticated protocol capture source staging applied')
