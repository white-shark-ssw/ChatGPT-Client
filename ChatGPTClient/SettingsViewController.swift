import UIKit

final class SettingsViewController: UIViewController {
    private let diagnostics = DiagnosticsLogger.shared
    private let exportButton = UIButton(type: .system)

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "设置"
        view.backgroundColor = .systemBackground

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

        let sampleButton = UIButton(type: .system)
        sampleButton.setTitle("写入测试诊断事件", for: .normal)
        sampleButton.addTarget(self, action: #selector(writeSampleEvent), for: .touchUpInside)

        exportButton.setTitle("导出诊断 JSON", for: .normal)
        exportButton.addTarget(self, action: #selector(exportDiagnostics), for: .touchUpInside)

        let stack = UIStackView(arrangedSubviews: [metadataTitle, metadataLabel, diagnosticsTitle, diagnosticsDetail, sampleButton, exportButton])
        stack.axis = .vertical
        stack.spacing = 16
        stack.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(stack)

        NSLayoutConstraint.activate([
            stack.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 24),
            stack.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -24),
            stack.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 24)
        ])

        diagnostics.info(category: "ui", name: "settings.loaded")
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

    private func showAlert(title: String, message: String) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "好", style: .default))
        present(alert, animated: true)
    }
}
