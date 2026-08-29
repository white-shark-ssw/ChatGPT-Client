import UIKit
import WebKit

final class RootViewController: UISplitViewController, UISplitViewControllerDelegate {
    private let diagnostics = DiagnosticsLogger.shared
    private let repository = ConversationRepository()
    private let sidebarViewController: ConversationSidebarViewController
    private let detailViewController: ConversationDetailViewController
    private let officialChatWebViewController = OfficialChatWebViewController()

    init() {
        sidebarViewController = ConversationSidebarViewController(repository: repository)
        detailViewController = ConversationDetailViewController(repository: repository)
        super.init(style: .doubleColumn)
        delegate = self

        let sidebarNavigationController = UINavigationController(rootViewController: sidebarViewController)
        let detailNavigationController = UINavigationController(rootViewController: detailViewController)
        setViewController(sidebarNavigationController, for: .primary)
        setViewController(detailNavigationController, for: .secondary)

        repository.onAccountScopeReset = { [weak self] in
            guard let self else { return }
            self.sidebarViewController.resetForAccountScopeChange()
            self.detailViewController.resetForAccountScopeChange()
            self.show(.primary)
        }
        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.repository.selectConversation(id: id)
            self.detailViewController.loadViewIfNeeded()
            self.detailViewController.title = self.repository.conversations.first(where: { $0.id == id })?.title ?? "新对话"
            self.detailViewController.showConversation(id: id)
            self.show(.secondary)
        }
        detailViewController.onOpenOfficialWebChat = { [weak self] in self?.openOfficialWebChat() }
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        preferredDisplayMode = .oneBesideSecondary
        preferredSplitBehavior = .tile
        presentsWithGesture = true
        diagnostics.info(category: "ui", name: "nativeConversationShell.loaded")
    }

    private func openOfficialWebChat() {
        guard officialChatWebViewController.navigationController == nil else { return }
        diagnostics.info(category: "navigation", name: "officialWebChat.open", fields: ["entry": "conversation_menu"])
        detailViewController.navigationController?.pushViewController(officialChatWebViewController, animated: true)
        show(.secondary)
    }

    func splitViewController(_ svc: UISplitViewController, topColumnForCollapsingToProposedTopColumn proposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column {
        repository.selectedConversationID == nil ? .primary : .secondary
    }
}

private final class OfficialChatWebViewController: UIViewController, WKNavigationDelegate, WKUIDelegate {
    private static let chatURL = URL(string: "https://chatgpt.com/")!

    private let diagnostics = DiagnosticsLogger.shared
    private let webView: WKWebView
    private var hasLoadedInitialPage = false
    private var navigationStartedAt: TimeInterval?
    private var presentationCount = 0

    init() {
        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .default()
        webView = WKWebView(frame: .zero, configuration: configuration)
        super.init(nibName: nil, bundle: nil)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "官方 ChatGPT"
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
            webView.topAnchor.constraint(equalTo: view.topAnchor),
            webView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])

        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadPage))
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        presentationCount += 1
        diagnostics.info(category: "webSend", name: "surface.presented", fields: ["presentationCount": String(presentationCount), "residentReuse": hasLoadedInitialPage ? "true" : "false"])
        guard !hasLoadedInitialPage else { return }
        hasLoadedInitialPage = true
        navigationStartedAt = ProcessInfo.processInfo.systemUptime
        diagnostics.info(category: "webSend", name: "surface.initialLoad", fields: ["destination": "chatgpt"])
        webView.load(URLRequest(url: Self.chatURL))
    }

    @objc private func reloadPage() {
        navigationStartedAt = ProcessInfo.processInfo.systemUptime
        diagnostics.info(category: "webSend", name: "surface.reload", fields: Self.safeLocationFields(webView.url))
        webView.reload()
    }

    private static func safeLocationFields(_ url: URL?) -> [String: String] {
        guard let host = url?.host?.lowercased() else { return ["destination": "unknown"] }
        let destination: String
        if host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") { destination = "chatgpt" }
        else if host == "openai.com" || host.hasSuffix(".openai.com") { destination = "openai" }
        else { destination = "external" }
        return ["destination": destination, "host": host]
    }
}

extension OfficialChatWebViewController {
    func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
        if navigationStartedAt == nil { navigationStartedAt = ProcessInfo.processInfo.systemUptime }
        diagnostics.info(category: "webSend", name: "navigation.started", fields: Self.safeLocationFields(webView.url))
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        var fields = Self.safeLocationFields(webView.url)
        if let navigationStartedAt { fields["durationMs"] = String(format: "%.2f", (ProcessInfo.processInfo.systemUptime - navigationStartedAt) * 1000) }
        self.navigationStartedAt = nil
        diagnostics.info(category: "webSend", name: "navigation.finished", fields: fields)
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        navigationStartedAt = nil
        diagnostics.error(category: "webSend", name: "navigation.failed", error: error, fields: Self.safeLocationFields(webView.url))
    }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {
        navigationStartedAt = nil
        diagnostics.error(category: "webSend", name: "navigation.provisionalFailed", error: error, fields: Self.safeLocationFields(webView.url))
    }

    func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {
        guard navigationAction.targetFrame == nil else { return nil }
        diagnostics.info(category: "webSend", name: "navigation.newWindow", fields: Self.safeLocationFields(navigationAction.request.url))
        webView.load(navigationAction.request)
        return nil
    }
}
