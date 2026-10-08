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
    static let handlerName = "protocolSendProbe"
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
        explanationLabel.text = "诊断专用：页面由 ChatGPT 官方 Web 自己发送。记录协议枚举、required 布尔、受保护字符串是否为空、ID 形态、Header 名称、JSON 键/类型和流事件结构；不记录提示词、回复正文、Cookie、Authorization、Sentinel/Turnstile/Proof/Conduit Token 值或原始 ID。"

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
        diagnostics.info(category: "protocol", name: "conversationSendProbe.opened", fields: ["mode": "visible_official_web_structural_only_v3"])
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
            fields["responseSemantic"] = Self.structuralJSON(body["responseSemantic"])
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
        statusLabel.text = "Send 请求 \(sendRequestCount) · Stream 结构 \(streamSignatureCount) · Terminal \(streamTerminalCount)\n本版请在默认 ChatGPT（非 GPT/Gizmo）新会话发送一次，完成后回设置导出诊断 JSON。"
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

    static let probeScript = #"""
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
      const stringPresence = value => typeof value !== 'string' ? 'none' : (value.length === 0 ? 'empty' : 'nonempty');
      const triBool = value => value === true ? true : (value === false ? false : null);
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
      const sendRequestSemantic = body => {
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
      const supportRequestSemantic = (info, body) => {
        const payload = parseBodyObject(body);
        if (!payload || !info) return {};
        if (info.route === 'conversation_prepare') {
          const contracts = Array.isArray(payload.model_response_contracts) ? payload.model_response_contracts : [];
          return {
            conversationKind: Object.prototype.hasOwnProperty.call(payload, 'conversation_id') ? 'existing' : 'new',
            action: protocolValue(payload.action),
            model: protocolValue(payload.model),
            clientPrepareDispatch: protocolValue(payload.client_prepare_dispatch),
            clientPrepareSource: protocolValue(payload.client_prepare_source),
            clientPrepareState: protocolValue(payload.client_prepare_state),
            conversationModeKind: protocolValue(payload.conversation_mode && payload.conversation_mode.kind),
            thinkingEffort: protocolValue(payload.thinking_effort),
            supportedEncodings: Array.isArray(payload.supported_encodings) ? payload.supported_encodings.slice(0, 8).map(protocolValue) : [],
            supportsBuffering: payload.supports_buffering === true,
            localFunctionNameCount: Array.isArray(payload.local_function_names) ? payload.local_function_names.length : -1,
            systemHintCount: Array.isArray(payload.system_hints) ? payload.system_hints.length : -1,
            responseContractCount: contracts.length,
            responseProtocolVersions: contracts.slice(0, 8).map(item => item && typeof item.protocol_version === 'number' ? item.protocol_version : -1),
            parentMessageIDShape: idShape(payload.parent_message_id),
            conversationIDShape: idShape(payload.conversation_id),
            partialQueryPresent: !!(payload.partial_query && typeof payload.partial_query === 'object'),
            asyncTaskIDPresent: typeof payload.async_task_id === 'string' && payload.async_task_id.length > 0
          };
        }
        if (info.route === 'sentinel_prepare') return { pPresence: stringPresence(payload.p), pShape: idShape(payload.p) };
        if (info.route === 'sentinel_finalize') return { prepareToken: stringPresence(payload.prepare_token), proofOfWork: stringPresence(payload.proofofwork), turnstile: stringPresence(payload.turnstile) };
        if (info.route === 'stop_candidate') return { conversationIDShape: idShape(payload.conversation_id), excludeAsyncTypeCount: Array.isArray(payload.exclude_async_types) ? payload.exclude_async_types.length : -1 };
        return {};
      };
      const responseSemantic = (info, payload) => {
        if (!info || !payload || typeof payload !== 'object' || Array.isArray(payload)) return {};
        if (info.route === 'conversation_prepare') return { status: protocolValue(payload.status), conduitToken: stringPresence(payload.conduit_token) };
        if (info.route === 'sentinel_prepare') {
          const pow = payload.proofofwork && typeof payload.proofofwork === 'object' ? payload.proofofwork : null;
          const turnstile = payload.turnstile && typeof payload.turnstile === 'object' ? payload.turnstile : null;
          const so = payload.so && typeof payload.so === 'object' ? payload.so : null;
          return { persona: protocolValue(payload.persona), prepareToken: stringPresence(payload.prepare_token), proofOfWorkRequired: triBool(pow && pow.required), turnstileRequired: triBool(turnstile && turnstile.required), soRequired: triBool(so && so.required) };
        }
        if (info.route === 'sentinel_finalize') return { persona: protocolValue(payload.persona), token: stringPresence(payload.token), expireAfterPresent: typeof payload.expire_after === 'number', expireAtPresent: typeof payload.expire_at === 'number' };
        if (info.route === 'stop_candidate') return { status: protocolValue(payload.status), lastMessageIDShape: idShape(payload.last_message_id) };
        if (info.route === 'conversation_init') return { type: protocolValue(payload.type), defaultModel: protocolValue(payload.default_model_slug), intendedDefaultModel: protocolValue(payload.intended_default_model_slug) };
        return {};
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
      const emitRequest = (info, method, transport, headers, body) => post({ kind: 'request', transport, route: info.route, safePath: info.safePath, pageKind: pageKind(), method, headerNames: headers, bodyShape: bodyShape(body), requestSemantic: info.route === 'conversation_send' ? sendRequestSemantic(body) : supportRequestSemantic(info, body) });
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
          response.clone().json().then(payload => post({ kind: 'response_shape', transport: 'fetch', route: info.route, safePath: info.safePath, pageKind: pageKind(), contentType, responseShape: describe(payload), responseSemantic: responseSemantic(info, payload) })).catch(() => {});
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
              try {
                const payload = JSON.parse(this.responseText);
                post({ kind: 'response_shape', transport: 'xhr', route: probe.info.route, safePath: probe.info.safePath, pageKind: pageKind(), contentType, responseShape: describe(payload), responseSemantic: responseSemantic(probe.info, payload) });
              } catch (_) {}
            }
          }, { once: true });
        }
        return originalSend.apply(this, arguments);
      };
    })();

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
    """#
}

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
