import UIKit
import WebKit

private final class WeakNativeResumeParityProbeHandler: NSObject, WKScriptMessageHandler {
    weak var target: WKScriptMessageHandler?

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        target?.userContentController(userContentController, didReceive: message)
    }
}

final class NativeResumeParityProbeViewController: UIViewController, WKNavigationDelegate, WKScriptMessageHandler {
    private static let handlerName = "nativeResumeParityProbe"
    private static let chatURL = URL(string: "https://chatgpt.com/")!
    private static let resumeURL = URL(string: "https://chatgpt.com/backend-api/f/conversation/resume")!

    private let diagnostics = DiagnosticsLogger.shared
    private let statusLabel = UILabel()
    private let scriptHandler = WeakNativeResumeParityProbeHandler()
    private var webView: WKWebView!
    private var transientSession: AuthTransientSession?
    private var officialResumeOpenCount = 0
    private var officialResumeSuccessCount = 0
    private var nativeParityStarted = false
    private var nativeParityStatus = "等待官方 resume"

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Native 续流接管探测"
        view.backgroundColor = .systemBackground
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadPage))

        let explanationLabel = UILabel()
        explanationLabel.font = .preferredFont(forTextStyle: .footnote)
        explanationLabel.textColor = .secondaryLabel
        explanationLabel.numberOfLines = 0
        explanationLabel.text = "b46 诊断：请在官方 ChatGPT Web 正常发送，并在流式回答时短暂断网再恢复。官方 Web 自己成功打开 /backend-api/f/conversation/resume 后，本页会把该次真实 conversation_id + offset 仅暂存在内存，并用现有 WebKit 派生的临时 Cookie + Bearer 发一次 Native 同 body resume。不会复制 Conduit、Sentinel、Turnstile、PoW 或其他浏览器挑战值；不会记录提示词、回复/思考正文、原始 ID，也不会重发提示词或写入原生会话状态。"

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
        diagnostics.info(category: "protocol", name: "nativeResumeParityProbe.opened", fields: ["mode": "visible_web_official_resume_to_native_once_v1"])
        webView.load(URLRequest(url: Self.chatURL))
    }

    deinit {
        webView?.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName)
        transientSession?.invalidateAndCancel()
    }

    @objc private func reloadPage() { webView.reload() }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "protocol", name: "nativeResumeParityProbe.page", fields: ["state": "loaded", "pageKind": Self.pageKind(for: webView.url)])
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    private func logNavigationFailure(_ error: Error) {
        let nsError = error as NSError
        diagnostics.warning(category: "protocol", name: "nativeResumeParityProbe.page", fields: ["state": "failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        guard message.name == Self.handlerName, let body = message.body as? [String: Any], let kind = body["kind"] as? String else { return }
        switch kind {
        case "send_observed":
            diagnostics.info(category: "protocol", name: "nativeResumeParityProbe.sendObserved", fields: ["pageKind": Self.safeToken(body["pageKind"] as? String)])
        case "official_resume_open":
            officialResumeOpenCount += 1
            var fields = ["bodyValid": Self.safeBoolString(body["bodyValid"]), "pageKind": Self.safeToken(body["pageKind"] as? String)]
            if let offset = body["offset"] as? NSNumber { fields["offset"] = offset.stringValue }
            diagnostics.info(category: "protocol", name: "nativeResumeParityProbe.officialResumeOpen", fields: fields)
            updateStatusLabel()
        case "official_resume_transport_error":
            diagnostics.warning(category: "protocol", name: "nativeResumeParityProbe.officialResumeTransportError", fields: ["pageKind": Self.safeToken(body["pageKind"] as? String)])
        case "official_resume_response":
            var fields = [
                "httpStatus": Self.safeNumberString(body["status"]),
                "contentType": Self.safeToken(body["contentType"] as? String),
                "bodyValid": Self.safeBoolString(body["bodyValid"]),
                "pageKind": Self.safeToken(body["pageKind"] as? String)
            ]
            if let offset = body["offset"] as? NSNumber { fields["offset"] = offset.stringValue }
            diagnostics.info(category: "protocol", name: "nativeResumeParityProbe.officialResumeResponse", fields: fields)
        case "native_resume_ready":
            guard let conversationID = body["conversationID"] as? String, !conversationID.isEmpty, let offsetNumber = body["offset"] as? NSNumber else { return }
            officialResumeSuccessCount += 1
            updateStatusLabel()
            startNativeResumeParity(conversationID: conversationID, offset: offsetNumber.intValue)
        default:
            break
        }
    }

    private func startNativeResumeParity(conversationID: String, offset: Int) {
        guard !nativeParityStarted else { return }
        nativeParityStarted = true
        nativeParityStatus = "准备 Native resume"
        updateStatusLabel()
        diagnostics.info(category: "protocol", name: "nativeResumeParityProbe.nativeStart", fields: ["offset": String(offset), "conversationID": "present", "attempt": "1"])

        let cookieStore = webView.configuration.websiteDataStore.httpCookieStore
        AuthSessionStore.shared.probeAccountContext(using: cookieStore, createTransientSession: true) { [weak self] state, transientSession in
            guard let self else { return }
            guard state == .verified, let transientSession else {
                self.finishNativeParity(status: "auth_unavailable", fields: ["accountState": state.rawValue])
                return
            }

            self.transientSession = transientSession
            var request = URLRequest(url: Self.resumeURL)
            request.httpMethod = "POST"
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")
            request.setValue("text/event-stream", forHTTPHeaderField: "Accept")
            do {
                request.httpBody = try JSONSerialization.data(withJSONObject: ["conversation_id": conversationID, "offset": offset], options: [])
            } catch {
                transientSession.finishTasksAndInvalidate()
                self.transientSession = nil
                self.finishNativeParity(status: "body_encode_failed", error: error)
                return
            }

            let startedAt = Date()
            transientSession.dataTask(with: request) { [weak self] data, response, error in
                guard let self else { return }
                defer {
                    transientSession.finishTasksAndInvalidate()
                    self.transientSession = nil
                }

                var fields = ["durationMs": String(Int(Date().timeIntervalSince(startedAt) * 1000))]
                if let error {
                    self.finishNativeParity(status: "transport_error", fields: fields, error: error)
                    return
                }

                guard let httpResponse = response as? HTTPURLResponse else {
                    self.finishNativeParity(status: "non_http_response", fields: fields)
                    return
                }

                let contentType = (httpResponse.value(forHTTPHeaderField: "Content-Type") ?? "").split(separator: ";", maxSplits: 1).first.map(String.init)?.lowercased() ?? "none"
                fields["httpStatus"] = String(httpResponse.statusCode)
                fields["contentType"] = Self.safeToken(contentType)
                if let data {
                    fields.merge(Self.summarizeSSE(data), uniquingKeysWith: { _, new in new })
                } else {
                    fields["byteCount"] = "0"
                    fields["frameCount"] = "0"
                    fields["terminal"] = "false"
                }

                let accepted = (200..<300).contains(httpResponse.statusCode) && contentType == "text/event-stream"
                self.finishNativeParity(status: accepted ? "http_sse_received" : "http_rejected", fields: fields)
            }
        }
    }

    private func finishNativeParity(status: String, fields: [String: String] = [:], error: Error? = nil) {
        var resultFields = fields
        resultFields["status"] = status
        if let error {
            let nsError = error as NSError
            resultFields["errorDomain"] = Self.safeToken(nsError.domain)
            resultFields["errorCode"] = String(nsError.code)
        }
        diagnostics.info(category: "protocol", name: "nativeResumeParityProbe.nativeResult", fields: resultFields)
        DispatchQueue.main.async { [weak self] in
            guard let self else { return }
            self.nativeParityStatus = status
            self.updateStatusLabel()
        }
    }

    private func updateStatusLabel() {
        statusLabel.text = "官方 resume 打开 \(officialResumeOpenCount) · 成功 \(officialResumeSuccessCount)\nNative parity：\(nativeParityStatus)"
    }

    private static func summarizeSSE(_ data: Data) -> [String: String] {
        guard let text = String(data: data, encoding: .utf8) else { return ["byteCount": String(data.count), "frameCount": "0", "terminal": "false", "parse": "non_utf8"] }
        let normalized = text.replacingOccurrences(of: "\r\n", with: "\n")
        var frameCount = 0
        var jsonFrameCount = 0
        var terminal = false
        var eventTypes = Set<String>()
        var identityKeys = Set<String>()

        for frame in normalized.components(separatedBy: "\n\n") {
            let payload = frame.split(separator: "\n").filter { $0.hasPrefix("data:") }.map { String($0.dropFirst(5)).trimmingCharacters(in: .whitespaces) }.joined(separator: "\n")
            guard !payload.isEmpty else { continue }
            frameCount += 1
            if payload == "[DONE]" {
                terminal = true
                continue
            }
            guard let payloadData = payload.data(using: .utf8), let object = try? JSONSerialization.jsonObject(with: payloadData) else { continue }
            jsonFrameCount += 1
            scanStructure(object, depth: 0, eventTypes: &eventTypes, identityKeys: &identityKeys)
        }

        return [
            "byteCount": String(data.count),
            "frameCount": String(frameCount),
            "jsonFrameCount": String(jsonFrameCount),
            "terminal": terminal ? "true" : "false",
            "eventTypes": eventTypes.sorted().prefix(24).joined(separator: ","),
            "identityKeys": identityKeys.sorted().joined(separator: ",")
        ]
    }

    private static func scanStructure(_ value: Any, depth: Int, eventTypes: inout Set<String>, identityKeys: inout Set<String>) {
        guard depth <= 7 else { return }
        if let array = value as? [Any] {
            for item in array.prefix(48) { scanStructure(item, depth: depth + 1, eventTypes: &eventTypes, identityKeys: &identityKeys) }
            return
        }
        guard let dictionary = value as? [String: Any] else { return }
        for (rawKey, child) in dictionary.prefix(96) {
            let key = rawKey.lowercased()
            if ["conversation_id", "request_id", "message_id", "turn_exchange_id", "working_turn_id"].contains(key) { identityKeys.insert(key) }
            if key == "type", let type = child as? String {
                let safe = safeToken(type)
                if safe != "none_or_redacted" { eventTypes.insert(safe) }
            }
            scanStructure(child, depth: depth + 1, eventTypes: &eventTypes, identityKeys: &identityKeys)
        }
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

    private static func safeNumberString(_ value: Any?) -> String {
        guard let number = value as? NSNumber else { return "none" }
        return number.stringValue
    }

    private static func safeBoolString(_ value: Any?) -> String {
        guard let number = value as? NSNumber else { return "false" }
        return number.boolValue ? "true" : "false"
    }

    private static let probeScript = #"""
    (() => {
      if (window.__chatgptNativeResumeParityProbeInstalled) return;
      window.__chatgptNativeResumeParityProbeInstalled = true;
      const bridge = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.nativeResumeParityProbe;
      if (!bridge) return;
      const post = value => { try { bridge.postMessage(value); } catch (_) {} };
      const pageKind = () => location.pathname.startsWith('/c/') ? 'existing_conversation' : (location.pathname.startsWith('/auth') ? 'authentication' : 'new_or_other');
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');
      const originalFetch = window.fetch.bind(window);
      let sendSeen = false;

      const parseResumeBody = body => {
        if (typeof body !== 'string') return null;
        try {
          const value = JSON.parse(body);
          if (!value || typeof value !== 'object' || typeof value.conversation_id !== 'string' || !value.conversation_id || typeof value.offset !== 'number' || !Number.isFinite(value.offset)) return null;
          return { conversationID: value.conversation_id, offset: value.offset };
        } catch (_) { return null; }
      };

      window.fetch = async function(input, init) {
        let path = '';
        let host = '';
        try {
          const url = new URL(typeof input === 'string' ? input : input && input.url || '', location.href);
          path = url.pathname;
          host = url.hostname.toLowerCase();
        } catch (_) {}

        const isChatGPT = isChatGPTHost(host);
        const isSend = isChatGPT && path === '/backend-api/f/conversation';
        const isResume = isChatGPT && path === '/backend-api/f/conversation/resume' && sendSeen;
        if (isSend) {
          sendSeen = true;
          post({ kind: 'send_observed', pageKind: pageKind() });
        }

        const candidate = isResume ? parseResumeBody(init && Object.prototype.hasOwnProperty.call(init, 'body') ? init.body : null) : null;
        if (isResume) post({ kind: 'official_resume_open', pageKind: pageKind(), bodyValid: !!candidate, offset: candidate ? candidate.offset : null });

        try {
          const response = await originalFetch(input, init);
          if (isResume) {
            const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
            post({ kind: 'official_resume_response', pageKind: pageKind(), status: response.status, contentType, bodyValid: !!candidate, offset: candidate ? candidate.offset : null });
            if (candidate && response.status === 200 && contentType === 'text/event-stream') {
              post({ kind: 'native_resume_ready', conversationID: candidate.conversationID, offset: candidate.offset });
            }
          }
          return response;
        } catch (error) {
          if (isResume) post({ kind: 'official_resume_transport_error', pageKind: pageKind() });
          throw error;
        }
      };
    })();
    """#
}