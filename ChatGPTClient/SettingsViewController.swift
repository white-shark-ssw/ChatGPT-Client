import UIKit

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
        protocolSendProbeButton.setTitle("Native 输入 / Web Send（b51诊断）", for: .normal)
        protocolSendProbeButton.addTarget(self, action: #selector(openProtocolSendProbe), for: .touchUpInside)

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