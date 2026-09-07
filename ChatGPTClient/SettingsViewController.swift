import UIKit
import WebKit

final class AppPreferences {
    static let shared = AppPreferences()
    static let didChangeNotification = Notification.Name("AppPreferences.didChange")

    private enum Key: String {
        case showsConversationRoundCount = "preferences.conversation.showsRoundCount"
        case showsMessageTimestamps = "preferences.conversation.showsMessageTimestamps"
        case showsAnswerQuickNavigation = "preferences.conversation.showsAnswerQuickNavigation"
    }

    private let defaults: UserDefaults

    private init(defaults: UserDefaults = .standard) {
        self.defaults = defaults
        defaults.register(defaults: [
            Key.showsConversationRoundCount.rawValue: true,
            Key.showsMessageTimestamps.rawValue: true,
            Key.showsAnswerQuickNavigation.rawValue: true
        ])
    }

    var showsConversationRoundCount: Bool {
        get { defaults.bool(forKey: Key.showsConversationRoundCount.rawValue) }
        set { setPreference(newValue, for: .showsConversationRoundCount) }
    }

    var showsMessageTimestamps: Bool {
        get { defaults.bool(forKey: Key.showsMessageTimestamps.rawValue) }
        set { setPreference(newValue, for: .showsMessageTimestamps) }
    }

    var showsAnswerQuickNavigation: Bool {
        get { defaults.bool(forKey: Key.showsAnswerQuickNavigation.rawValue) }
        set { setPreference(newValue, for: .showsAnswerQuickNavigation) }
    }

    private func setPreference(_ value: Bool, for key: Key) {
        guard defaults.bool(forKey: key.rawValue) != value else { return }
        defaults.set(value, forKey: key.rawValue)
        NotificationCenter.default.post(name: Self.didChangeNotification, object: self)
    }
}

final class SettingsViewController: UIViewController {
    private let diagnostics = DiagnosticsLogger.shared
    private let preferences = AppPreferences.shared
    private let roundCountSwitch = UISwitch()
    private let messageTimeSwitch = UISwitch()
    private let answerJumpSwitch = UISwitch()
    private let exportButton = UIButton(type: .system)
    private let clearButton = UIButton(type: .system)

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "设置"
        view.backgroundColor = .systemBackground

        let scrollView = UIScrollView()
        scrollView.alwaysBounceVertical = true
        scrollView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(scrollView)

        let contentView = UIView()
        contentView.translatesAutoresizingMaskIntoConstraints = false
        scrollView.addSubview(contentView)

        let preferencesTitle = UILabel()
        preferencesTitle.font = .preferredFont(forTextStyle: .headline)
        preferencesTitle.text = "会话显示"

        roundCountSwitch.isOn = preferences.showsConversationRoundCount
        roundCountSwitch.addTarget(self, action: #selector(roundCountPreferenceChanged), for: .valueChanged)
        messageTimeSwitch.isOn = preferences.showsMessageTimestamps
        messageTimeSwitch.addTarget(self, action: #selector(messageTimePreferenceChanged), for: .valueChanged)
        answerJumpSwitch.isOn = preferences.showsAnswerQuickNavigation
        answerJumpSwitch.addTarget(self, action: #selector(answerJumpPreferenceChanged), for: .valueChanged)

        let metadataTitle = UILabel()
        metadataTitle.font = .preferredFont(forTextStyle: .headline)
        metadataTitle.text = "构建与运行信息"

        let metadataLabel = UILabel()
        metadataLabel.font = .monospacedSystemFont(ofSize: 12, weight: .regular)
        metadataLabel.textColor = .secondaryLabel
        metadataLabel.numberOfLines = 0
        metadataLabel.text = AppBuildInfo.current.displayText

        let diagnosticsTitle = UILabel()
        diagnosticsTitle.font = .preferredFont(forTextStyle: .headline)
        diagnosticsTitle.text = "诊断"

        let diagnosticsDetail = UILabel()
        diagnosticsDetail.font = .preferredFont(forTextStyle: .body)
        diagnosticsDetail.textColor = .secondaryLabel
        diagnosticsDetail.numberOfLines = 0
        diagnosticsDetail.text = "日志只保存有界的本地结构化元数据。默认不记录密码、OAuth Code、Token、Cookie、完整聊天正文、请求/响应正文或附件内容；导出时会再次脱敏敏感标识。"

        let protocolSendProbeButton = UIButton(type: .system)
        protocolSendProbeButton.setTitle("Native 输入 / Web Send（b65诊断）", for: .normal)
        protocolSendProbeButton.addTarget(self, action: #selector(openProtocolSendProbe), for: .touchUpInside)

        let webRuleLabButton = UIButton(type: .system)
        webRuleLabButton.setTitle("Web Rule Lab", for: .normal)
        webRuleLabButton.addTarget(self, action: #selector(openWebRuleLab), for: .touchUpInside)

        let sampleButton = UIButton(type: .system)
        sampleButton.setTitle("写入测试诊断事件", for: .normal)
        sampleButton.addTarget(self, action: #selector(writeSampleEvent), for: .touchUpInside)

        exportButton.setTitle("导出诊断 JSON", for: .normal)
        exportButton.addTarget(self, action: #selector(exportDiagnostics), for: .touchUpInside)

        clearButton.setTitle("清理诊断日志", for: .normal)
        clearButton.addTarget(self, action: #selector(clearDiagnostics), for: .touchUpInside)

        let stack = UIStackView(arrangedSubviews: [
            preferencesTitle,
            makePreferenceRow(title: "显示会话轮数", control: roundCountSwitch),
            makePreferenceRow(title: "显示消息时间", control: messageTimeSwitch),
            makePreferenceRow(title: "显示轮次快速跳转", control: answerJumpSwitch),
            metadataTitle,
            metadataLabel,
            diagnosticsTitle,
            diagnosticsDetail,
            protocolSendProbeButton,
            webRuleLabButton,
            sampleButton,
            exportButton,
            clearButton
        ])
        stack.axis = .vertical
        stack.spacing = 16
        stack.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(stack)

        NSLayoutConstraint.activate([
            scrollView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            scrollView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            scrollView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            scrollView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            contentView.leadingAnchor.constraint(equalTo: scrollView.contentLayoutGuide.leadingAnchor),
            contentView.trailingAnchor.constraint(equalTo: scrollView.contentLayoutGuide.trailingAnchor),
            contentView.topAnchor.constraint(equalTo: scrollView.contentLayoutGuide.topAnchor),
            contentView.bottomAnchor.constraint(equalTo: scrollView.contentLayoutGuide.bottomAnchor),
            contentView.widthAnchor.constraint(equalTo: scrollView.frameLayoutGuide.widthAnchor),
            stack.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 24),
            stack.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -24),
            stack.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 24),
            stack.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -24)
        ])

        diagnostics.info(category: "ui", name: "settings.loaded")
    }

    private func makePreferenceRow(title: String, control: UISwitch) -> UIView {
        let label = UILabel()
        label.font = .preferredFont(forTextStyle: .body)
        label.text = title
        label.numberOfLines = 0
        let row = UIStackView(arrangedSubviews: [label, control])
        row.axis = .horizontal
        row.alignment = .center
        row.spacing = 12
        return row
    }

    @objc private func roundCountPreferenceChanged() { preferences.showsConversationRoundCount = roundCountSwitch.isOn }
    @objc private func messageTimePreferenceChanged() { preferences.showsMessageTimestamps = messageTimeSwitch.isOn }
    @objc private func answerJumpPreferenceChanged() { preferences.showsAnswerQuickNavigation = answerJumpSwitch.isOn }

    @objc private func openProtocolSendProbe() {
        diagnostics.info(category: "navigation", name: "nativeWebSendEngineProbe.open")
        navigationController?.pushViewController(NativeWebSendEngineProbeViewController(), animated: true)
    }

    @objc private func openWebRuleLab() {
        diagnostics.info(category: "navigation", name: "webRuleLab.open")
        navigationController?.pushViewController(WebRuleLabViewController(), animated: true)
    }

    @objc private func writeSampleEvent() {
        let span = diagnostics.startSpan(category: "diagnostics", name: "sample", fields: ["origin": "settings"])
        diagnostics.info(category: "diagnostics", name: "sample.event", traceID: span.traceID, fields: ["itemCount": "1", "status": "ok"])
        span.end()
        showAlert(title: "已写入", message: "已记录一组带 trace/span 的测试诊断事件。")
    }

    @objc private func exportDiagnostics() {
        exportButton.isEnabled = false
        DiagnosticsExporter.shared.export { [weak self] result in
            guard let self else { return }
            self.exportButton.isEnabled = true
            switch result {
            case .success(let url):
                let activity = UIActivityViewController(activityItems: [url], applicationActivities: nil)
                activity.popoverPresentationController?.sourceView = self.exportButton
                activity.popoverPresentationController?.sourceRect = self.exportButton.bounds
                self.present(activity, animated: true)
            case .failure(let error):
                self.showAlert(title: "导出失败", message: error.localizedDescription)
            }
        }
    }

    @objc private func clearDiagnostics() {
        do {
            try diagnostics.clearStoredLogs()
            showAlert(title: "已清理", message: "本地诊断日志已清空，之后产生的新日志会重新累计。")
        } catch {
            showAlert(title: "清理失败", message: error.localizedDescription)
        }
    }

    private func showAlert(title: String, message: String) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "好", style: .default))
        present(alert, animated: true)
    }
}

final class WebRuleLabViewController: UIViewController, WKNavigationDelegate {
    private static let chatURL = URL(string: "https://chatgpt.com/")!

    private let diagnostics = DiagnosticsLogger.shared
    private let webView: WKWebView
    private let scriptTextView = UITextView()
    private let resultTextView = UITextView()
    private let executeButton = UIButton(type: .system)
    private let shareButton = UIButton(type: .system)

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
        title = "Web Rule Lab"
        view.backgroundColor = .systemBackground

        let note = UILabel()
        note.font = .preferredFont(forTextStyle: .footnote)
        note.textColor = .secondaryLabel
        note.numberOfLines = 0
        note.text = "开发工具：使用与正式客户端相同的 ChatGPT Web 登录态。脚本只在你点击“执行”时运行；脚本与结果不会写入日志、偏好或文件。"

        webView.navigationDelegate = self
        webView.allowsBackForwardNavigationGestures = true
        webView.scrollView.keyboardDismissMode = .interactive
        webView.translatesAutoresizingMaskIntoConstraints = false
        webView.heightAnchor.constraint(equalToConstant: 330).isActive = true

        scriptTextView.font = .monospacedSystemFont(ofSize: 12, weight: .regular)
        scriptTextView.backgroundColor = .secondarySystemBackground
        scriptTextView.layer.cornerRadius = 10
        scriptTextView.textContainerInset = UIEdgeInsets(top: 9, left: 8, bottom: 9, right: 8)
        scriptTextView.autocorrectionType = .no
        scriptTextView.autocapitalizationType = .none
        scriptTextView.smartQuotesType = .no
        scriptTextView.smartDashesType = .no
        scriptTextView.text = "// 粘贴一次性 Web 结构探针；不会自动执行。"
        scriptTextView.heightAnchor.constraint(equalToConstant: 130).isActive = true

        resultTextView.isEditable = false
        resultTextView.isSelectable = true
        resultTextView.font = .monospacedSystemFont(ofSize: 12, weight: .regular)
        resultTextView.backgroundColor = .tertiarySystemBackground
        resultTextView.layer.cornerRadius = 10
        resultTextView.textContainerInset = UIEdgeInsets(top: 9, left: 8, bottom: 9, right: 8)
        resultTextView.text = "等待执行…"
        resultTextView.heightAnchor.constraint(equalToConstant: 150).isActive = true

        executeButton.setTitle("执行", for: .normal)
        executeButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
        executeButton.addTarget(self, action: #selector(executeScript), for: .touchUpInside)

        let copyButton = UIButton(type: .system)
        copyButton.setTitle("复制结果", for: .normal)
        copyButton.addTarget(self, action: #selector(copyResult), for: .touchUpInside)

        shareButton.setTitle("分享结果", for: .normal)
        shareButton.addTarget(self, action: #selector(shareResult), for: .touchUpInside)

        let buttons = UIStackView(arrangedSubviews: [executeButton, copyButton, shareButton])
        buttons.axis = .horizontal
        buttons.distribution = .fillEqually
        buttons.spacing = 8

        let stack = UIStackView(arrangedSubviews: [note, webView, scriptTextView, buttons, resultTextView])
        stack.axis = .vertical
        stack.spacing = 10
        stack.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(stack)
        NSLayoutConstraint.activate([
            stack.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 12),
            stack.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -12),
            stack.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 8),
            stack.bottomAnchor.constraint(lessThanOrEqualTo: view.safeAreaLayoutGuide.bottomAnchor, constant: -8)
        ])

        diagnostics.info(category: "webRuleLab", name: "opened", fields: ["store": "default", "autoRun": "false"])
        webView.load(URLRequest(url: Self.chatURL))
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "webRuleLab", name: "page", fields: ["state": "loaded", "host": webView.url?.host == "chatgpt.com" ? "chatgpt.com" : "other"])
    }

    @objc private func executeScript() {
        let script = scriptTextView.text ?? ""
        guard !script.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else { return }
        executeButton.isEnabled = false
        resultTextView.text = "执行中…"
        diagnostics.info(category: "webRuleLab", name: "execution", fields: ["state": "started", "scriptCharacters": String(script.count)])
        webView.evaluateJavaScript(script) { [weak self] result, error in
            guard let self else { return }
            self.executeButton.isEnabled = true
            if let error {
                let nsError = error as NSError
                let text = "JavaScript 执行失败\n\(nsError.domain) \(nsError.code)\n\(nsError.localizedDescription)"
                self.resultTextView.text = text
                self.diagnostics.warning(category: "webRuleLab", name: "execution", fields: ["state": "failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code), "resultCharacters": String(text.count)])
                return
            }
            let text = Self.displayText(for: result)
            self.resultTextView.text = text
            self.diagnostics.info(category: "webRuleLab", name: "execution", fields: ["state": "completed", "resultType": Self.resultType(result), "resultCharacters": String(text.count)])
        }
    }

    @objc private func copyResult() {
        UIPasteboard.general.string = resultTextView.text
        diagnostics.info(category: "webRuleLab", name: "resultAction", fields: ["action": "copy", "resultCharacters": String(resultTextView.text.count)])
    }

    @objc private func shareResult() {
        let text = resultTextView.text ?? ""
        guard !text.isEmpty else { return }
        let controller = UIActivityViewController(activityItems: [text], applicationActivities: nil)
        controller.popoverPresentationController?.sourceView = shareButton
        controller.popoverPresentationController?.sourceRect = shareButton.bounds
        present(controller, animated: true)
        diagnostics.info(category: "webRuleLab", name: "resultAction", fields: ["action": "share", "resultCharacters": String(text.count)])
    }

    private static func displayText(for result: Any?) -> String {
        guard let result else { return "undefined / null" }
        if JSONSerialization.isValidJSONObject(result), let data = try? JSONSerialization.data(withJSONObject: result, options: [.prettyPrinted, .sortedKeys]), let text = String(data: data, encoding: .utf8) { return text }
        if let string = result as? String { return string }
        return String(describing: result)
    }

    private static func resultType(_ result: Any?) -> String {
        guard let result else { return "null" }
        if result is String { return "string" }
        if result is NSNumber { return "number_or_bool" }
        if result is [Any] { return "array" }
        if result is [String: Any] { return "object" }
        return "other"
    }

    private static let safeTokenCharacters = CharacterSet(charactersIn: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_./:{}-+,")
    private static func safeToken(_ value: String) -> String { value.count <= 120 && value.unicodeScalars.allSatisfy { safeTokenCharacters.contains($0) } ? value : "redacted" }
}
