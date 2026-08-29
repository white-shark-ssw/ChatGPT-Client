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
            navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadHybridChat))
        case .authentication, .protocolRead:
            navigationItem.rightBarButtonItem = UIBarButtonItem(title: "重新开始", style: .plain, target: self, action: #selector(restartLogin))
            startLogin()
        }
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        guard mode == .hybridChat else { return }
        hybridPresentationCount += 1
        diagnostics.info(category: "webSend", name: "surface.presented", fields: ["presentationCount": String(hybridPresentationCount), "residentReuse": hybridPageLoaded ? "true" : "false"])
        guard !hybridPageLoaded else { return }
        hybridPageLoaded = true
        hybridNavigationStartedAt = ProcessInfo.processInfo.systemUptime
        diagnostics.info(category: "webSend", name: "surface.initialLoad", fields: ["destination": "chatgpt"])
        webView.load(URLRequest(url: Self.chatURL))
    }

    private var initialTitle: String {
        switch mode {
        case .authentication: return "登录验证"
        case .protocolRead: return "协议读取验证"
        case .hybridChat: return "官方 ChatGPT"
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

    private static func safeLocationFields(_ url: URL?) -> [String: String] {
        guard let url, let host = url.host?.lowercased() else { return ["destination": "unknown"] }
        let destination: String
        if host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") {
            destination = url.path.hasPrefix("/auth") ? "chatgpt_auth" : "chatgpt"
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
        diagnostics.info(category: mode == .hybridChat ? "webSend" : "auth", name: "web.navigation.request", fields: fields)
        decisionHandler(.allow)
    }

    func webView(_ webView: WKWebView, decidePolicyFor navigationResponse: WKNavigationResponse, decisionHandler: @escaping (WKNavigationResponsePolicy) -> Void) {
        var fields = Self.safeLocationFields(navigationResponse.response.url)
        if let response = navigationResponse.response as? HTTPURLResponse { fields["httpStatus"] = String(response.statusCode) }
        diagnostics.info(category: mode == .hybridChat ? "webSend" : "auth", name: "web.navigation.response", fields: fields)
        decisionHandler(.allow)
    }

    func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
        guard mode == .hybridChat else { return }
        if hybridNavigationStartedAt == nil { hybridNavigationStartedAt = ProcessInfo.processInfo.systemUptime }
        diagnostics.info(category: "webSend", name: "navigation.started", fields: Self.safeLocationFields(webView.url))
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        let fields = Self.safeLocationFields(webView.url)
        if mode == .hybridChat {
            var hybridFields = fields
            if let hybridNavigationStartedAt { hybridFields["durationMs"] = String(format: "%.2f", (ProcessInfo.processInfo.systemUptime - hybridNavigationStartedAt) * 1000) }
            self.hybridNavigationStartedAt = nil
            diagnostics.info(category: "webSend", name: "navigation.finished", fields: hybridFields)
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
