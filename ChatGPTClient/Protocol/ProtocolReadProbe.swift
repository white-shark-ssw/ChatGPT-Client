import Foundation
import UIKit
import WebKit

enum ProtocolReadState {
    case verified
    case listNotAvailable
    case detailNotAvailable
    case failed
}

final class ProtocolReadProbe {
    private static let listURL: URL = {
        var components = URLComponents(string: "https://chatgpt.com/backend-api/conversations")!
        components.queryItems = [
            URLQueryItem(name: "offset", value: "0"),
            URLQueryItem(name: "limit", value: "28"),
            URLQueryItem(name: "order", value: "updated")
        ]
        return components.url!
    }()

    private let diagnostics = DiagnosticsLogger.shared

    func run(using session: AuthTransientSession, completion: @escaping (ProtocolReadState) -> Void) {
        let span = diagnostics.startSpan(category: "protocol", name: "conversationReadProbe")
        diagnostics.info(category: "protocol", name: "conversationList.request", traceID: span.traceID, fields: ["method": "GET", "route": "conversation_list", "offset": "0", "limit": "28", "order": "updated"])
        var request = URLRequest(url: Self.listURL)
        request.httpMethod = "GET"
        session.dataTask(with: request) { [weak self] data, response, error in
            self?.handleListResponse(data: data, response: response, error: error, session: session, span: span, completion: completion)
        }
    }

    private func handleListResponse(data: Data?, response: URLResponse?, error: Error?, session: AuthTransientSession, span: DiagnosticsSpan, completion: @escaping (ProtocolReadState) -> Void) {
        if let error {
            diagnostics.error(category: "protocol", name: "conversationList.failed", traceID: span.traceID, error: error)
            finish(.failed, session: session, span: span, fields: ["stage": "list"], completion: completion)
            return
        }
        guard let response = response as? HTTPURLResponse, let data else {
            finish(.failed, session: session, span: span, fields: ["stage": "list", "reason": "non_http_response"], completion: completion)
            return
        }
        guard (200..<300).contains(response.statusCode) else {
            finish(.listNotAvailable, session: session, span: span, fields: ["stage": "list", "httpStatus": String(response.statusCode)], completion: completion)
            return
        }
        guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let items = payload["items"] as? [Any] else {
            finish(.listNotAvailable, session: session, span: span, fields: ["stage": "list", "httpStatus": String(response.statusCode), "reason": "missing_items"], completion: completion)
            return
        }

        var fields = ["httpStatus": String(response.statusCode), "byteCount": String(data.count), "itemCount": String(items.count)]
        Self.copyIntegerField("total", from: payload, to: "totalCount", fields: &fields)
        Self.copyIntegerField("limit", from: payload, to: "responseLimit", fields: &fields)
        Self.copyIntegerField("offset", from: payload, to: "responseOffset", fields: &fields)
        diagnostics.info(category: "protocol", name: "conversationList.response", traceID: span.traceID, fields: fields)

        var conversationID: String?
        for item in items {
            guard let item = item as? [String: Any], let id = item["id"] as? String, !id.isEmpty else { continue }
            conversationID = id
            break
        }
        guard let conversationID else {
            fields["stage"] = "detail"
            fields["reason"] = "missing_conversation_id"
            finish(.detailNotAvailable, session: session, span: span, fields: fields, completion: completion)
            return
        }
        requestDetail(conversationID: conversationID, session: session, span: span, listFields: fields, completion: completion)
    }

    private func requestDetail(conversationID: String, session: AuthTransientSession, span: DiagnosticsSpan, listFields: [String: String], completion: @escaping (ProtocolReadState) -> Void) {
        let baseURL = URL(string: "https://chatgpt.com/backend-api/conversation")!
        let detailURL = baseURL.appendingPathComponent(conversationID)
        diagnostics.info(category: "protocol", name: "conversationDetail.request", traceID: span.traceID, fields: ["method": "GET", "route": "conversation_detail", "selection": "first_list_item"])
        var request = URLRequest(url: detailURL)
        request.httpMethod = "GET"
        session.dataTask(with: request) { [weak self] data, response, error in
            self?.handleDetailResponse(data: data, response: response, error: error, conversationID: conversationID, session: session, span: span, listFields: listFields, completion: completion)
        }
    }

    private func handleDetailResponse(data: Data?, response: URLResponse?, error: Error?, conversationID: String, session: AuthTransientSession, span: DiagnosticsSpan, listFields: [String: String], completion: @escaping (ProtocolReadState) -> Void) {
        if let error {
            diagnostics.error(category: "protocol", name: "conversationDetail.failed", traceID: span.traceID, error: error)
            finish(.failed, session: session, span: span, fields: ["stage": "detail"], completion: completion)
            return
        }
        guard let response = response as? HTTPURLResponse, let data else {
            finish(.failed, session: session, span: span, fields: ["stage": "detail", "reason": "non_http_response"], completion: completion)
            return
        }
        guard (200..<300).contains(response.statusCode) else {
            finish(.detailNotAvailable, session: session, span: span, fields: ["stage": "detail", "httpStatus": String(response.statusCode)], completion: completion)
            return
        }
        guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let mapping = payload["mapping"] as? [String: Any] else {
            finish(.detailNotAvailable, session: session, span: span, fields: ["stage": "detail", "httpStatus": String(response.statusCode), "reason": "missing_mapping"], completion: completion)
            return
        }

        let summary = summarize(mapping: mapping)
        let currentNode = payload["current_node"] as? String
        let returnedConversationID = payload["conversation_id"] as? String
        var fields: [String: String] = [:]
        fields["httpStatus"] = String(response.statusCode)
        fields["byteCount"] = String(data.count)
        fields["mappingCount"] = String(mapping.count)
        fields["messageNodeCount"] = String(summary.messageNodeCount)
        fields["nullMessageNodeCount"] = String(summary.nullMessageNodeCount)
        fields["rootNodeCount"] = String(summary.rootNodeCount)
        fields["branchingNodeCount"] = String(summary.branchingNodeCount)
        fields["maxChildrenCount"] = String(summary.maxChildrenCount)
        fields["userRoleCount"] = String(summary.userRoleCount)
        fields["assistantRoleCount"] = String(summary.assistantRoleCount)
        fields["systemRoleCount"] = String(summary.systemRoleCount)
        fields["toolRoleCount"] = String(summary.toolRoleCount)
        fields["otherRoleCount"] = String(summary.otherRoleCount)
        fields["contentTypeCount"] = String(summary.contentTypeCount)
        fields["currentNodePresent"] = String(currentNode?.isEmpty == false)
        fields["currentNodeMapped"] = String(currentNode.map { mapping[$0] != nil } ?? false)
        fields["conversationIdentityPresent"] = String(returnedConversationID?.isEmpty == false)
        fields["conversationIdentityMatches"] = String(returnedConversationID == conversationID)
        for (key, value) in listFields { fields["list_\(key)"] = value }
        diagnostics.info(category: "protocol", name: "conversationDetail.response", traceID: span.traceID, fields: fields)
        finish(.verified, session: session, span: span, fields: ["stage": "detail", "listItemCount": listFields["itemCount"] ?? "unknown", "mappingCount": String(mapping.count), "messageNodeCount": String(summary.messageNodeCount)], completion: completion)
    }

    private func summarize(mapping: [String: Any]) -> DetailSummary {
        var summary = DetailSummary()
        var contentTypes = Set<String>()
        for value in mapping.values {
            guard let node = value as? [String: Any] else { continue }
            let parent = node["parent"]
            if parent == nil || parent is NSNull { summary.rootNodeCount += 1 }
            let childrenCount = (node["children"] as? [Any])?.count ?? 0
            if childrenCount > 1 { summary.branchingNodeCount += 1 }
            summary.maxChildrenCount = max(summary.maxChildrenCount, childrenCount)

            guard let message = node["message"] as? [String: Any] else {
                summary.nullMessageNodeCount += 1
                continue
            }
            summary.messageNodeCount += 1
            let author = message["author"] as? [String: Any]
            let role = author?["role"] as? String ?? ""
            switch role {
            case "user": summary.userRoleCount += 1
            case "assistant": summary.assistantRoleCount += 1
            case "system": summary.systemRoleCount += 1
            case "tool": summary.toolRoleCount += 1
            default: summary.otherRoleCount += 1
            }
            let content = message["content"] as? [String: Any]
            if let contentType = content?["content_type"] as? String, !contentType.isEmpty { contentTypes.insert(contentType) }
        }
        summary.contentTypeCount = contentTypes.count
        return summary
    }

    private func finish(_ state: ProtocolReadState, session: AuthTransientSession, span: DiagnosticsSpan, fields: [String: String], completion: @escaping (ProtocolReadState) -> Void) {
        session.finishTasksAndInvalidate()
        let status: String
        switch state {
        case .verified: status = "ok"
        case .listNotAvailable, .detailNotAvailable: status = "not_available"
        case .failed: status = "failed"
        }
        span.end(status: status, fields: fields)
        completion(state)
    }

    private static func copyIntegerField(_ sourceKey: String, from payload: [String: Any], to destinationKey: String, fields: inout [String: String]) {
        if let value = payload[sourceKey] as? NSNumber { fields[destinationKey] = value.stringValue }
    }
}

private struct DetailSummary {
    var messageNodeCount = 0
    var nullMessageNodeCount = 0
    var rootNodeCount = 0
    var branchingNodeCount = 0
    var maxChildrenCount = 0
    var userRoleCount = 0
    var assistantRoleCount = 0
    var systemRoleCount = 0
    var toolRoleCount = 0
    var otherRoleCount = 0
    var contentTypeCount = 0
}

private final class WeakProtocolSendProbeScriptHandler: NSObject, WKScriptMessageHandler {
    weak var target: WKScriptMessageHandler?

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        target?.userContentController(userContentController, didReceive: message)
    }
}

final class ProtocolSendProbeViewController: UIViewController, WKNavigationDelegate, WKScriptMessageHandler {
    private static let handlerName = "protocolSendProbe"
    private static let chatURL = URL(string: "https://chatgpt.com/")!

    private let diagnostics = DiagnosticsLogger.shared
    private let statusLabel = UILabel()
    private let scriptHandler = WeakProtocolSendProbeScriptHandler()
    private var webView: WKWebView!
    private var sendRequestCount = 0
    private var streamSignatureCount = 0
    private var streamTerminalCount = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Send 协议探测"
        view.backgroundColor = .systemBackground
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadPage))

        let explanationLabel = UILabel()
        explanationLabel.font = .preferredFont(forTextStyle: .footnote)
        explanationLabel.textColor = .secondaryLabel
        explanationLabel.numberOfLines = 0
        explanationLabel.text = "诊断专用：页面由 ChatGPT 官方 Web 自己发送。记录协议枚举、ID 形态、Header 名称、JSON 键/类型和流事件结构；不记录提示词、回复正文、Cookie、Authorization、Sentinel/Turnstile/Proof/Conduit Token 值或原始 ID。"

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
        diagnostics.info(category: "protocol", name: "conversationSendProbe.opened", fields: ["mode": "visible_official_web_structural_only_v2"])
        webView.load(URLRequest(url: Self.chatURL))
    }

    deinit {
        webView?.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName)
    }

    @objc private func reloadPage() { webView.reload() }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        let pageKind = Self.pageKind(for: webView.url)
        diagnostics.info(category: "protocol", name: "conversationSendProbe.page", fields: ["state": "loaded", "pageKind": pageKind])
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    private func logNavigationFailure(_ error: Error) {
        let nsError = error as NSError
        diagnostics.warning(category: "protocol", name: "conversationSendProbe.page", fields: ["state": "failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        guard message.name == Self.handlerName, let body = message.body as? [String: Any], let kind = body["kind"] as? String else { return }
        switch kind {
        case "request":
            let route = Self.safeToken(body["route"] as? String)
            if route == "conversation_send" { sendRequestCount += 1 }
            var fields = baseFields(body)
            fields["method"] = Self.safeToken(body["method"] as? String)
            fields["headerNames"] = Self.safeStringArray(body["headerNames"])
            fields["bodyShape"] = Self.structuralJSON(body["bodyShape"])
            fields["requestSemantic"] = Self.structuralJSON(body["requestSemantic"])
            diagnostics.info(category: "protocol", name: "conversationSendProbe.request", fields: fields)
            updateStatusLabel()
        case "response":
            var fields = baseFields(body)
            fields["httpStatus"] = Self.safeNumberString(body["status"])
            fields["contentType"] = Self.safeToken(body["contentType"] as? String)
            fields["responseHeaderNames"] = Self.safeStringArray(body["responseHeaderNames"])
            diagnostics.info(category: "protocol", name: "conversationSendProbe.response", fields: fields)
        case "response_shape":
            var fields = baseFields(body)
            fields["contentType"] = Self.safeToken(body["contentType"] as? String)
            fields["responseShape"] = Self.structuralJSON(body["responseShape"])
            diagnostics.info(category: "protocol", name: "conversationSendProbe.responseShape", fields: fields)
        case "stream_signature":
            streamSignatureCount += 1
            var fields = baseFields(body)
            fields["eventIndex"] = Self.safeNumberString(body["eventIndex"])
            fields["signature"] = Self.safeToken(body["signature"] as? String)
            fields["eventType"] = Self.safeToken(body["eventType"] as? String)
            fields["operation"] = Self.safeToken(body["operation"] as? String)
            fields["patchPath"] = Self.safeToken(body["patchPath"] as? String)
            fields["messageRole"] = Self.safeToken(body["messageRole"] as? String)
            fields["contentType"] = Self.safeToken(body["messageContentType"] as? String)
            fields["messageStatus"] = Self.safeToken(body["messageStatus"] as? String)
            fields["hasConversationID"] = Self.safeBoolString(body["hasConversationID"])
            fields["hasMessageID"] = Self.safeBoolString(body["hasMessageID"])
            fields["conversationIDSource"] = Self.safeToken(body["conversationIDSource"] as? String)
            fields["messageIDSource"] = Self.safeToken(body["messageIDSource"] as? String)
            fields["eventKeys"] = Self.safeStringArray(body["eventKeys"])
            fields["valueKeys"] = Self.safeStringArray(body["valueKeys"])
            fields["hasTitle"] = Self.safeBoolString(body["hasTitle"])
            fields["endTurn"] = Self.safeBoolString(body["endTurn"])
            fields["batchPatches"] = Self.structuralJSON(body["batchPatches"])
            diagnostics.info(category: "protocol", name: "conversationSendProbe.streamSignature", fields: fields)
            updateStatusLabel()
        case "stream_terminal":
            streamTerminalCount += 1
            var fields = baseFields(body)
            fields["eventCount"] = Self.safeNumberString(body["eventCount"])
            fields["firstEventMs"] = Self.safeNumberString(body["firstEventMs"])
            fields["doneSeen"] = Self.safeBoolString(body["doneSeen"])
            fields["signatureCounts"] = Self.structuralJSON(body["signatureCounts"])
            diagnostics.info(category: "protocol", name: "conversationSendProbe.streamTerminal", fields: fields)
            updateStatusLabel()
        case "fetch_error":
            var fields = baseFields(body)
            fields["method"] = Self.safeToken(body["method"] as? String)
            diagnostics.warning(category: "protocol", name: "conversationSendProbe.fetchFailed", fields: fields)
        default:
            break
        }
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
        statusLabel.text = "Send 请求 \(sendRequestCount) · Stream 结构 \(streamSignatureCount) · Terminal \(streamTerminalCount)\n完成 existing + new-chat 各一次后，回到设置导出诊断 JSON。"
    }

    private static func pageKind(for url: URL?) -> String {
        guard let url, let host = url.host?.lowercased(), host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") else { return "external_or_unknown" }
        if url.path.hasPrefix("/c/") { return "existing_conversation" }
        if url.path.hasPrefix("/auth") { return "authentication" }
        return "new_or_other"
    }

    private static let safeTokenCharacters = CharacterSet(charactersIn: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_./:{}-+,")

    private static func safeToken(_ value: String?) -> String {
        guard let value, !value.isEmpty, value.count <= 160, value.unicodeScalars.allSatisfy({ safeTokenCharacters.contains($0) }) else { return "none_or_redacted" }
        return value
    }

    private static func safeStringArray(_ value: Any?) -> String {
        guard let values = value as? [Any] else { return "none" }
        return values.prefix(40).compactMap { $0 as? String }.map(safeToken).joined(separator: ",")
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
      if (window.__chatgptNativeSendProbeInstalled) return;
      window.__chatgptNativeSendProbeInstalled = true;
      const bridge = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.protocolSendProbe;
      if (!bridge) return;
      const post = value => { try { bridge.postMessage(value); } catch (_) {} };
      const pageKind = () => location.pathname.startsWith('/c/') ? 'existing_conversation' : (location.pathname.startsWith('/auth') ? 'authentication' : 'new_or_other');
      const protocolValue = value => {
        if (typeof value !== 'string') return 'none';
        const s = value.trim();
        return /^[A-Za-z][A-Za-z0-9_.:+-]{0,47}$/.test(s) ? s : 'other_or_redacted';
      };
      const safeStructuralKey = value => {
        const s = String(value || '');
        if (/^[A-Za-z_][A-Za-z0-9_.:-]{0,63}$/.test(s)) return s;
        return '{key}';
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
      const classify = value => {
        try {
          const u = new URL(typeof value === 'string' ? value : value && value.url || '', location.href);
          const host = u.hostname.toLowerCase();
          if (!(host === 'chatgpt.com' || host.endsWith('.chatgpt.com'))) return null;
          const p = u.pathname;
          let route = null;
          if (p === '/backend-api/f/conversation') route = 'conversation_send';
          else if (p === '/backend-api/f/conversation/prepare') route = 'conversation_prepare';
          else if (p === '/backend-api/conversation/init') route = 'conversation_init';
          else if (p === '/backend-api/sentinel/chat-requirements') route = 'sentinel_requirements';
          else if (p === '/backend-api/sentinel/chat-requirements/prepare') route = 'sentinel_prepare';
          else if (p === '/backend-api/sentinel/chat-requirements/finalize') route = 'sentinel_finalize';
          else if (/(stop|abort|cancel)/i.test(p) && p.startsWith('/backend-api/')) route = 'stop_candidate';
          if (!route) return null;
          return { route, safePath: safePath(p) };
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
      const parseBodyObject = body => {
        if (typeof body !== 'string' || !body) return null;
        try {
          const value = JSON.parse(body);
          return value && typeof value === 'object' && !Array.isArray(value) ? value : null;
        } catch (_) { return null; }
      };
      const requestSemantic = body => {
        const payload = parseBodyObject(body);
        if (!payload) return {};
        const messages = Array.isArray(payload.messages) ? payload.messages : [];
        const first = messages.length && messages[0] && typeof messages[0] === 'object' ? messages[0] : null;
        const author = first && first.author && typeof first.author === 'object' ? first.author : null;
        const content = first && first.content && typeof first.content === 'object' ? first.content : null;
        const contracts = Array.isArray(payload.model_response_contracts) ? payload.model_response_contracts : [];
        return {
          conversationKind: Object.prototype.hasOwnProperty.call(payload, 'conversation_id') ? 'existing' : 'new',
          action: protocolValue(payload.action),
          model: protocolValue(payload.model),
          clientPrepareState: protocolValue(payload.client_prepare_state),
          conversationModeKind: protocolValue(payload.conversation_mode && payload.conversation_mode.kind),
          thinkingEffort: protocolValue(payload.thinking_effort),
          forceParallelSwitch: protocolValue(payload.force_parallel_switch),
          cotSummaryOverride: protocolValue(payload.paragen_cot_summary_display_override),
          supportedEncodings: Array.isArray(payload.supported_encodings) ? payload.supported_encodings.slice(0, 8).map(protocolValue) : [],
          supportsBuffering: payload.supports_buffering === true,
          enableMessageFollowups: payload.enable_message_followups === true,
          localFunctionNameCount: Array.isArray(payload.local_function_names) ? payload.local_function_names.length : -1,
          systemHintCount: Array.isArray(payload.system_hints) ? payload.system_hints.length : -1,
          responseContractCount: contracts.length,
          responseProtocolVersions: contracts.slice(0, 8).map(item => item && typeof item.protocol_version === 'number' ? item.protocol_version : -1),
          messageCount: messages.length,
          firstMessageRole: protocolValue(author && author.role),
          firstMessageContentType: protocolValue(content && content.content_type),
          firstMessagePartsCount: content && Array.isArray(content.parts) ? content.parts.length : -1,
          firstMessageIDShape: idShape(first && first.id),
          parentMessageIDShape: idShape(payload.parent_message_id),
          conversationIDShape: idShape(payload.conversation_id),
          firstMessageEqualsParent: !!(first && typeof first.id === 'string' && typeof payload.parent_message_id === 'string' && first.id === payload.parent_message_id)
        };
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
      const emitRequest = (info, method, transport, headers, body) => post({ kind: 'request', transport, route: info.route, safePath: info.safePath, pageKind: pageKind(), method, headerNames: headers, bodyShape: bodyShape(body), requestSemantic: info.route === 'conversation_send' ? requestSemantic(body) : {} });
      const observeFetchRequest = (input, init, info, method) => {
        if (!info) return;
        const headers = headerNames(input, init);
        if (init && Object.prototype.hasOwnProperty.call(init, 'body')) {
          emitRequest(info, method, 'fetch', headers, init.body);
          return;
        }
        if (input instanceof Request) {
          try {
            input.clone().text().then(text => emitRequest(info, method, 'fetch', headers, text)).catch(() => emitRequest(info, method, 'fetch', headers, null));
            return;
          } catch (_) {}
        }
        emitRequest(info, method, 'fetch', headers, null);
      };
      const observeResponseShape = (response, info, contentType) => {
        if (!info || contentType !== 'application/json' || info.route === 'conversation_send') return;
        try {
          response.clone().json().then(payload => post({ kind: 'response_shape', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), contentType, responseShape: describe(payload) })).catch(() => {});
        } catch (_) {}
      };
      const messageFrom = obj => obj && typeof obj === 'object' ? (obj.message || (obj.v && typeof obj.v === 'object' && !Array.isArray(obj.v) ? obj.v.message : null)) : null;
      const summarizeSSE = data => {
        const trimmed = String(data || '').trim();
        if (trimmed === '[DONE]') return { signature: 'done', terminal: true, eventKeys: [], valueKeys: [], conversationIDSource: 'none', messageIDSource: 'none' };
        let obj;
        try { obj = JSON.parse(trimmed); } catch (_) { return { signature: 'non_json', terminal: false, eventKeys: [], valueKeys: [], conversationIDSource: 'none', messageIDSource: 'none' }; }
        if (typeof obj === 'string') return { signature: obj === 'v1' ? 'marker:v1' : 'json_string', terminal: false, eventKeys: [], valueKeys: [], conversationIDSource: 'none', messageIDSource: 'none' };
        if (!obj || typeof obj !== 'object') return { signature: 'json_primitive', terminal: false, eventKeys: [], valueKeys: [], conversationIDSource: 'none', messageIDSource: 'none' };
        const valueObject = obj.v && typeof obj.v === 'object' && !Array.isArray(obj.v) ? obj.v : null;
        const eventType = typeof obj.type === 'string' ? obj.type : '';
        const operation = typeof obj.o === 'string' ? obj.o : '';
        const patchPath = typeof obj.p === 'string' ? obj.p : '';
        const message = messageFrom(obj);
        const role = message && message.author && typeof message.author.role === 'string' ? message.author.role : '';
        const contentType = message && message.content && typeof message.content.content_type === 'string' ? message.content.content_type : '';
        const status = message && typeof message.status === 'string' ? message.status : '';
        const endTurn = !!(message && message.end_turn === true);
        let conversationIDSource = 'none';
        if (typeof obj.conversation_id === 'string' && obj.conversation_id) conversationIDSource = 'conversation_id';
        else if (valueObject && typeof valueObject.conversation_id === 'string' && valueObject.conversation_id) conversationIDSource = 'v.conversation_id';
        let messageIDSource = 'none';
        if (message && typeof message.id === 'string' && message.id) messageIDSource = 'message.id';
        else if (typeof obj.message_id === 'string' && obj.message_id) messageIDSource = 'message_id';
        else if (valueObject && typeof valueObject.message_id === 'string' && valueObject.message_id) messageIDSource = 'v.message_id';
        const hasConversationID = conversationIDSource !== 'none';
        const hasMessageID = messageIDSource !== 'none';
        const hasTitle = eventType === 'title_generation' || Object.prototype.hasOwnProperty.call(obj, 'title');
        const eventKeys = Object.keys(obj).slice(0, 48).map(safeStructuralKey).sort();
        const valueKeys = valueObject ? Object.keys(valueObject).slice(0, 48).map(safeStructuralKey).sort() : [];
        let batchPatches = [];
        if (operation === 'patch' && Array.isArray(obj.v)) batchPatches = obj.v.slice(0, 16).map(item => ({ operation: item && typeof item.o === 'string' ? item.o : '', patchPath: item && typeof item.p === 'string' ? item.p : '' }));
        let signature = 'object';
        if (eventType) signature = 'type:' + eventType;
        else if (operation) signature = 'patch:' + operation + ':' + (patchPath || 'root');
        else if (message) signature = 'message:' + (role || 'unknown') + ':' + (status || 'unknown');
        else if (obj.v && typeof obj.v === 'string') signature = 'value_string_patch';
        return { signature, terminal: false, eventType, operation, patchPath, messageRole: role, messageContentType: contentType, messageStatus: status, hasConversationID, hasMessageID, conversationIDSource, messageIDSource, eventKeys, valueKeys, hasTitle, endTurn, batchPatches };
      };
      const inspectSSE = async (response, startedAt, info) => {
        const reader = response.body && response.body.getReader ? response.body.getReader() : null;
        if (!reader) return;
        const decoder = new TextDecoder();
        let buffer = '';
        let eventCount = 0;
        let firstEventMs = null;
        let doneSeen = false;
        const signatureCounts = {};
        const seen = new Set();
        const consumeData = data => {
          if (!String(data || '').trim()) return;
          eventCount += 1;
          if (firstEventMs === null) firstEventMs = Math.max(0, performance.now() - startedAt);
          const summary = summarizeSSE(data);
          signatureCounts[summary.signature] = (signatureCounts[summary.signature] || 0) + 1;
          const evidenceKey = [summary.signature, summary.conversationIDSource || 'none', summary.messageIDSource || 'none'].join('|');
          if (!seen.has(evidenceKey)) {
            seen.add(evidenceKey);
            post({ kind: 'stream_signature', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), eventIndex: eventCount, signature: summary.signature, eventType: summary.eventType || '', operation: summary.operation || '', patchPath: summary.patchPath || '', messageRole: summary.messageRole || '', messageContentType: summary.messageContentType || '', messageStatus: summary.messageStatus || '', hasConversationID: !!summary.hasConversationID, hasMessageID: !!summary.hasMessageID, conversationIDSource: summary.conversationIDSource || 'none', messageIDSource: summary.messageIDSource || 'none', eventKeys: summary.eventKeys || [], valueKeys: summary.valueKeys || [], hasTitle: !!summary.hasTitle, endTurn: !!summary.endTurn, batchPatches: summary.batchPatches || [] });
          }
          if (summary.terminal) doneSeen = true;
        };
        try {
          while (eventCount < 5000) {
            const result = await reader.read();
            buffer = (buffer + decoder.decode(result.value || new Uint8Array(), { stream: !result.done })).replace(/\r\n/g, '\n');
            let boundary;
            while ((boundary = buffer.indexOf('\n\n')) >= 0) {
              const frame = buffer.slice(0, boundary);
              buffer = buffer.slice(boundary + 2);
              const data = frame.split('\n').filter(line => line.startsWith('data:')).map(line => line.slice(5).trimStart()).join('\n');
              consumeData(data);
            }
            if (result.done) break;
          }
        } catch (_) {}
        try { reader.cancel(); } catch (_) {}
        post({ kind: 'stream_terminal', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), eventCount, firstEventMs: firstEventMs === null ? -1 : Math.round(firstEventMs * 100) / 100, doneSeen, signatureCounts });
      };

      const originalFetch = window.fetch.bind(window);
      window.fetch = async function(input, init) {
        const info = classify(input);
        const method = String((init && init.method) || (input instanceof Request && input.method) || 'GET').toUpperCase();
        const startedAt = performance.now();
        observeFetchRequest(input, init, info, method);
        try {
          const response = await originalFetch(input, init);
          if (info) {
            const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
            post({ kind: 'response', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), status: response.status, contentType, responseHeaderNames: responseHeaderNames(response) });
            observeResponseShape(response, info, contentType);
            if (info.route === 'conversation_send' && contentType === 'text/event-stream') inspectSSE(response.clone(), startedAt, info);
          }
          return response;
        } catch (error) {
          if (info) post({ kind: 'fetch_error', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), method });
          throw error;
        }
      };

      const originalOpen = XMLHttpRequest.prototype.open;
      const originalSetRequestHeader = XMLHttpRequest.prototype.setRequestHeader;
      const originalSend = XMLHttpRequest.prototype.send;
      XMLHttpRequest.prototype.open = function(method, url) {
        this.__nativeSendProbe = { info: classify(url), method: String(method || 'GET').toUpperCase(), headerNames: [] };
        return originalOpen.apply(this, arguments);
      };
      XMLHttpRequest.prototype.setRequestHeader = function(name, value) {
        if (this.__nativeSendProbe && this.__nativeSendProbe.info) this.__nativeSendProbe.headerNames.push(String(name || '').toLowerCase());
        return originalSetRequestHeader.apply(this, arguments);
      };
      XMLHttpRequest.prototype.send = function(body) {
        const probe = this.__nativeSendProbe;
        if (probe && probe.info) {
          emitRequest(probe.info, probe.method, 'xhr', Array.from(new Set(probe.headerNames)).sort(), body);
          this.addEventListener('loadend', () => {
            const contentType = String(this.getResponseHeader('content-type') || '').split(';')[0].trim().toLowerCase();
            let responseHeaderNames = [];
            try { responseHeaderNames = String(this.getAllResponseHeaders() || '').split(/\r?\n/).map(line => line.split(':', 1)[0].trim().toLowerCase()).filter(Boolean).slice(0, 48).sort(); } catch (_) {}
            post({ kind: 'response', transport: 'xhr', route: probe.info.route, safePath: probe.info.safePath, pageKind: pageKind(), status: this.status, contentType, responseHeaderNames });
            if (contentType === 'application/json' && probe.info.route !== 'conversation_send') {
              try { post({ kind: 'response_shape', transport: 'xhr', route: probe.info.route, safePath: probe.info.safePath, pageKind: pageKind(), contentType, responseShape: describe(JSON.parse(this.responseText)) }); } catch (_) {}
            }
          }, { once: true });
        }
        return originalSend.apply(this, arguments);
      };
    })();
    """#
}
