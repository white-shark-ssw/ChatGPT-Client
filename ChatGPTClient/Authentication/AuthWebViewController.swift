import UIKit
import WebKit

enum AuthVerificationMode {
    case authentication
    case protocolRead
    case hybridChat
}

final class AuthWebViewController: UIViewController {
    static let hybridChat = AuthWebViewController(mode: .hybridChat)

    private static let loginURL = URL(string: "https://chatgpt.com/auth/login")!
    private static let chatURL = URL(string: "https://chatgpt.com/")!

    private let diagnostics = DiagnosticsLogger.shared
    private let sessionStore = AuthSessionStore.shared
    private let mode: AuthVerificationMode
    private let webView: WKWebView
    private var bootstrapSpan: DiagnosticsSpan?
    private var accountProbeStarted = false
    private var protocolProbe: ProtocolReadProbe?
    private var hybridPageLoaded = false
    private var hybridPresentationCount = 0
    private var hybridNavigationStartedAt: TimeInterval?
    private var hybridTargetConversationID: String?
    private var hybridSyncHandler: (() -> Void)?

    init(mode: AuthVerificationMode = .authentication) {
        self.mode = mode
        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .default()
        webView = WKWebView(frame: .zero, configuration: configuration)
        super.init(nibName: nil, bundle: nil)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = initialTitle
        view.backgroundColor = .systemBackground

        webView.navigationDelegate = self
        webView.uiDelegate = self
        webView.allowsBackForwardNavigationGestures = true
        webView.scrollView.keyboardDismissMode = .interactive
        webView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(webView)

        NSLayoutConstraint.activate([
            webView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            webView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            webView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            webView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])

        switch mode {
        case .hybridChat:
            navigationItem.rightBarButtonItems = [
                UIBarButtonItem(title: "返回并同步", style: .done, target: self, action: #selector(returnAndSyncHybridChat)),
                UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadHybridChat))
            ]
        case .authentication, .protocolRead:
            navigationItem.rightBarButtonItem = UIBarButtonItem(title: "重新开始", style: .plain, target: self, action: #selector(restartLogin))
            startLogin()
        }
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        guard mode == .hybridChat else { return }
        navigationController?.setToolbarHidden(true, animated: false)
        hybridPresentationCount += 1
        let targetMatch = hybridTargetConversationID.map { Self.webConversationID(from: webView.url) == $0 } ?? false
        diagnostics.info(category: "webSend", name: "surface.presented", fields: ["presentationCount": String(hybridPresentationCount), "residentReuse": targetMatch ? "true" : "false", "targetMatch": targetMatch ? "true" : "false"])
        loadHybridTargetIfNeeded()
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        guard mode == .hybridChat, isMovingFromParent else { return }
        navigationController?.setToolbarHidden(false, animated: false)
    }

    func prepareForConversation(id: String, onSyncRequested: @escaping () -> Void) {
        guard mode == .hybridChat else { return }
        hybridTargetConversationID = id
        hybridSyncHandler = onSyncRequested
        title = "发送消息"
    }

    private var initialTitle: String {
        switch mode {
        case .authentication: return "登录验证"
        case .protocolRead: return "协议读取验证"
        case .hybridChat: return "发送消息"
        }
    }

    private func startLogin() {
        guard mode != .hybridChat else { return }
        accountProbeStarted = false
        protocolProbe = nil
        title = initialTitle
        bootstrapSpan?.end(status: "restarted")
        bootstrapSpan = diagnostics.startSpan(category: "auth", name: "webBootstrap", fields: ["entry": "chatgpt_login"])
        diagnostics.info(category: "auth", name: "webBootstrap.load", traceID: bootstrapSpan?.traceID, fields: Self.safeLocationFields(Self.loginURL))
        webView.load(URLRequest(url: Self.loginURL))
    }

    private func loadHybridTargetIfNeeded() {
        guard mode == .hybridChat else { return }
        let destination: URL
        if let id = hybridTargetConversationID {
            if Self.webConversationID(from: webView.url) == id {
                hybridPageLoaded = true
                return
            }
            destination = Self.chatURL.appendingPathComponent("c").appendingPathComponent(id)
        } else {
            guard !hybridPageLoaded else { return }
            destination = Self.chatURL
        }
        hybridPageLoaded = true
        hybridNavigationStartedAt = ProcessInfo.processInfo.systemUptime
        diagnostics.info(category: "webSend", name: "surface.targetLoad", fields: ["route": hybridTargetConversationID == nil ? "root" : "conversation", "residentReuse": "false"])
        webView.load(URLRequest(url: destination))
    }

    @objc private func restartLogin() {
        diagnostics.info(category: "auth", name: "webBootstrap.restart")
        startLogin()
    }

    @objc private func reloadHybridChat() {
        guard mode == .hybridChat else { return }
        hybridNavigationStartedAt = ProcessInfo.processInfo.systemUptime
        diagnostics.info(category: "webSend", name: "surface.reload", fields: Self.safeLocationFields(webView.url))
        webView.reload()
    }

    @objc private func returnAndSyncHybridChat() {
        guard mode == .hybridChat else { return }
        diagnostics.info(category: "webSend", name: "nativeReturn.syncRequested", fields: ["targetMatch": currentHybridTargetMatches ? "true" : "false"])
        hybridSyncHandler?()
        navigationController?.popViewController(animated: true)
    }

    private var currentHybridTargetMatches: Bool {
        guard let id = hybridTargetConversationID else { return false }
        return Self.webConversationID(from: webView.url) == id
    }

    private func startAccountProbeIfNeeded() {
        guard mode != .hybridChat, !accountProbeStarted else { return }
        accountProbeStarted = true
        title = "网页登录成功 · 账户验证中"
        diagnostics.info(category: "auth", name: "accountContextProbe.requested")
        sessionStore.probeAccountContext(using: webView.configuration.websiteDataStore.httpCookieStore, createTransientSession: mode == .protocolRead) { [weak self] state, transientSession in
            DispatchQueue.main.async {
                guard let self else {
                    transientSession?.finishTasksAndInvalidate()
                    return
                }
                switch state {
                case .verified:
                    if self.mode == .protocolRead, let transientSession {
                        self.startProtocolProbe(using: transientSession)
                    } else {
                        transientSession?.finishTasksAndInvalidate()
                        self.title = "登录会话 · 账户上下文通过"
                    }
                case .notAvailable:
                    transientSession?.finishTasksAndInvalidate()
                    self.title = "网页登录成功 · 账户上下文未通过"
                case .failed:
                    transientSession?.finishTasksAndInvalidate()
                    self.title = "网页登录成功 · 账户验证失败"
                case .unknown, .probing:
                    transientSession?.finishTasksAndInvalidate()
                }
            }
        }
    }

    private func startProtocolProbe(using transientSession: AuthTransientSession) {
        title = "登录会话 · 协议读取中"
        diagnostics.info(category: "protocol", name: "conversationReadProbe.requested")
        let probe = ProtocolReadProbe()
        protocolProbe = probe
        probe.run(using: transientSession) { [weak self, weak probe] state in
            DispatchQueue.main.async {
                guard let self else { return }
                if self.protocolProbe === probe { self.protocolProbe = nil }
                switch state {
                case .verified:
                    self.title = "会话列表 · 会话详情通过"
                case .listNotAvailable:
                    self.title = "账户通过 · 会话列表未通过"
                case .detailNotAvailable:
                    self.title = "会话列表通过 · 会话详情未通过"
                case .failed:
                    self.title = "账户通过 · 协议读取失败"
                }
            }
        }
    }

    private static func webConversationID(from url: URL?) -> String? {
        guard let url, let host = url.host?.lowercased(), host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") else { return nil }
        let components = url.pathComponents.filter { $0 != "/" }
        guard components.count >= 2, components[0] == "c" else { return nil }
        return components[1]
    }

    private static func safeLocationFields(_ url: URL?) -> [String: String] {
        guard let url, let host = url.host?.lowercased() else { return ["destination": "unknown"] }
        let destination: String
        if host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") {
            if url.path.hasPrefix("/auth") {
                destination = "chatgpt_auth"
            } else if webConversationID(from: url) != nil {
                destination = "chatgpt_conversation"
            } else {
                destination = "chatgpt"
            }
        } else if host == "auth.openai.com" || host.hasSuffix(".openai.com") {
            destination = "openai_auth"
        } else if host == "accounts.google.com" {
            destination = "google_accounts"
        } else if host.hasSuffix(".google.com") {
            destination = "google"
        } else {
            destination = "external"
        }
        return ["host": host, "destination": destination]
    }

    private static func navigationTypeName(_ type: WKNavigationType) -> String {
        switch type {
        case .linkActivated: return "linkActivated"
        case .formSubmitted: return "formSubmitted"
        case .backForward: return "backForward"
        case .reload: return "reload"
        case .formResubmitted: return "formResubmitted"
        case .other: return "other"
        @unknown default: return "unknown"
        }
    }
}

extension AuthWebViewController: WKNavigationDelegate {
    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        var fields = Self.safeLocationFields(navigationAction.request.url)
        fields["navigationType"] = Self.navigationTypeName(navigationAction.navigationType)
        if mode == .hybridChat, let target = hybridTargetConversationID { fields["targetMatch"] = Self.webConversationID(from: navigationAction.request.url) == target ? "true" : "false" }
        diagnostics.info(category: mode == .hybridChat ? "webSend" : "auth", name: "web.navigation.request", fields: fields)
        decisionHandler(.allow)
    }

    func webView(_ webView: WKWebView, decidePolicyFor navigationResponse: WKNavigationResponse, decisionHandler: @escaping (WKNavigationResponsePolicy) -> Void) {
        var fields = Self.safeLocationFields(navigationResponse.response.url)
        if let response = navigationResponse.response as? HTTPURLResponse { fields["httpStatus"] = String(response.statusCode) }
        if mode == .hybridChat, let target = hybridTargetConversationID { fields["targetMatch"] = Self.webConversationID(from: navigationResponse.response.url) == target ? "true" : "false" }
        diagnostics.info(category: mode == .hybridChat ? "webSend" : "auth", name: "web.navigation.response", fields: fields)
        decisionHandler(.allow)
    }

    func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
        guard mode == .hybridChat else { return }
        if hybridNavigationStartedAt == nil { hybridNavigationStartedAt = ProcessInfo.processInfo.systemUptime }
        var fields = Self.safeLocationFields(webView.url)
        fields["targetMatch"] = currentHybridTargetMatches ? "true" : "false"
        diagnostics.info(category: "webSend", name: "navigation.started", fields: fields)
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        var fields = Self.safeLocationFields(webView.url)
        if mode == .hybridChat {
            fields["targetMatch"] = currentHybridTargetMatches ? "true" : "false"
            if let hybridNavigationStartedAt { fields["durationMs"] = String(format: "%.2f", (ProcessInfo.processInfo.systemUptime - hybridNavigationStartedAt) * 1000) }
            self.hybridNavigationStartedAt = nil
            diagnostics.info(category: "webSend", name: "navigation.finished", fields: fields)
            return
        }

        diagnostics.info(category: "auth", name: "web.navigation.finished", fields: fields)
        let webState = sessionStore.observeWebLocation(webView.url)
        if let bootstrapSpan {
            bootstrapSpan.end(fields: fields)
            self.bootstrapSpan = nil
        }
        if webState == .authenticated { startAccountProbeIfNeeded() }
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        if mode == .hybridChat { hybridNavigationStartedAt = nil }
        diagnostics.error(category: mode == .hybridChat ? "webSend" : "auth", name: "web.navigation.failed", error: error, fields: Self.safeLocationFields(webView.url))
    }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {
        if mode == .hybridChat { hybridNavigationStartedAt = nil }
        diagnostics.error(category: mode == .hybridChat ? "webSend" : "auth", name: "web.navigation.provisionalFailed", error: error, fields: Self.safeLocationFields(webView.url))
        if mode != .hybridChat, let bootstrapSpan {
            bootstrapSpan.end(status: "failed", fields: Self.safeLocationFields(webView.url))
            self.bootstrapSpan = nil
        }
    }
}

extension AuthWebViewController: WKUIDelegate {
    func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {
        guard navigationAction.targetFrame == nil else { return nil }
        diagnostics.info(category: mode == .hybridChat ? "webSend" : "auth", name: "web.navigation.newWindow", fields: Self.safeLocationFields(navigationAction.request.url))
        webView.load(navigationAction.request)
        return nil
    }
}
