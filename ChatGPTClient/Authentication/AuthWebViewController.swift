import UIKit
import WebKit

final class AuthWebViewController: UIViewController {
    private static let loginURL = URL(string: "https://chatgpt.com/auth/login")!

    private let diagnostics = DiagnosticsLogger.shared
    private let sessionStore = AuthSessionStore.shared
    private let webView: WKWebView
    private var bootstrapSpan: DiagnosticsSpan?
    private var nativeProbeStarted = false
    private var accountProbeStarted = false

    init() {
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
        title = "登录验证"
        view.backgroundColor = .systemBackground

        webView.navigationDelegate = self
        webView.uiDelegate = self
        webView.allowsBackForwardNavigationGestures = true
        webView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(webView)

        NSLayoutConstraint.activate([
            webView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            webView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            webView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            webView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])

        navigationItem.rightBarButtonItem = UIBarButtonItem(title: "重新开始", style: .plain, target: self, action: #selector(restartLogin))
        startLogin()
    }

    private func startLogin() {
        nativeProbeStarted = false
        accountProbeStarted = false
        title = "登录验证"
        bootstrapSpan?.end(status: "restarted")
        bootstrapSpan = diagnostics.startSpan(category: "auth", name: "webBootstrap", fields: ["entry": "chatgpt_login"])
        diagnostics.info(category: "auth", name: "webBootstrap.load", traceID: bootstrapSpan?.traceID, fields: Self.safeLocationFields(Self.loginURL))
        webView.load(URLRequest(url: Self.loginURL))
    }

    @objc private func restartLogin() {
        diagnostics.info(category: "auth", name: "webBootstrap.restart")
        startLogin()
    }

    private func startNativeProbeIfNeeded() {
        guard !nativeProbeStarted else { return }
        nativeProbeStarted = true
        title = "网页登录成功 · 原生验证中"
        diagnostics.info(category: "auth", name: "nativeSessionProbe.requested")
        sessionStore.probeNativeSession(using: webView.configuration.websiteDataStore.httpCookieStore) { [weak self] state in
            DispatchQueue.main.async {
                guard let self else { return }
                switch state {
                case .verified:
                    self.title = "网页登录成功 · 原生会话通过"
                    self.startAccountProbeIfNeeded()
                case .notAuthenticated:
                    self.title = "网页登录成功 · 原生会话未通过"
                case .failed:
                    self.title = "网页登录成功 · 原生验证失败"
                case .unknown, .probing:
                    break
                }
            }
        }
    }

    private func startAccountProbeIfNeeded() {
        guard !accountProbeStarted else { return }
        accountProbeStarted = true
        title = "原生会话通过 · 账户验证中"
        diagnostics.info(category: "auth", name: "accountContextProbe.requested")
        sessionStore.probeAccountContext(using: webView.configuration.websiteDataStore.httpCookieStore) { [weak self] state in
            DispatchQueue.main.async {
                guard let self else { return }
                switch state {
                case .verified:
                    self.title = "登录会话 · 账户上下文通过"
                case .notAvailable:
                    self.title = "原生会话通过 · 账户上下文未通过"
                case .failed:
                    self.title = "原生会话通过 · 账户验证失败"
                case .unknown, .probing:
                    break
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
        diagnostics.info(category: "auth", name: "web.navigation.request", fields: fields)
        decisionHandler(.allow)
    }

    func webView(_ webView: WKWebView, decidePolicyFor navigationResponse: WKNavigationResponse, decisionHandler: @escaping (WKNavigationResponsePolicy) -> Void) {
        var fields = Self.safeLocationFields(navigationResponse.response.url)
        if let response = navigationResponse.response as? HTTPURLResponse { fields["httpStatus"] = String(response.statusCode) }
        diagnostics.info(category: "auth", name: "web.navigation.response", fields: fields)
        decisionHandler(.allow)
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "auth", name: "web.navigation.finished", fields: Self.safeLocationFields(webView.url))
        let webState = sessionStore.observeWebLocation(webView.url)
        if let bootstrapSpan {
            bootstrapSpan.end(fields: Self.safeLocationFields(webView.url))
            self.bootstrapSpan = nil
        }
        if webState == .authenticated { startNativeProbeIfNeeded() }
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        diagnostics.error(category: "auth", name: "web.navigation.failed", error: error, fields: Self.safeLocationFields(webView.url))
    }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {
        diagnostics.error(category: "auth", name: "web.navigation.provisionalFailed", error: error, fields: Self.safeLocationFields(webView.url))
        if let bootstrapSpan {
            bootstrapSpan.end(status: "failed", fields: Self.safeLocationFields(webView.url))
            self.bootstrapSpan = nil
        }
    }
}

extension AuthWebViewController: WKUIDelegate {
    func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {
        guard navigationAction.targetFrame == nil else { return nil }
        diagnostics.info(category: "auth", name: "web.navigation.newWindow", fields: Self.safeLocationFields(navigationAction.request.url))
        webView.load(navigationAction.request)
        return nil
    }
}
