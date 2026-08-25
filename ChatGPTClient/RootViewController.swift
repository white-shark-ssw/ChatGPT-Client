import UIKit

final class RootViewController: UIViewController {
    private let diagnostics = DiagnosticsLogger.shared

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "ChatGPT Client"
        view.backgroundColor = .systemBackground
        navigationItem.rightBarButtonItem = UIBarButtonItem(title: "设置", style: .plain, target: self, action: #selector(openSettings))

        let titleLabel = UILabel()
        titleLabel.font = .preferredFont(forTextStyle: .largeTitle)
        titleLabel.text = "应用基础已就绪"
        titleLabel.numberOfLines = 0

        let detailLabel = UILabel()
        detailLabel.font = .preferredFont(forTextStyle: .body)
        detailLabel.textColor = .secondaryLabel
        detailLabel.numberOfLines = 0
        detailLabel.text = "当前阶段只建立原生应用骨架、构建身份和安全诊断能力。登录、ChatGPT 私有协议与聊天功能将在后续独立任务中实现。"

        let buildLabel = UILabel()
        buildLabel.font = .monospacedSystemFont(ofSize: 12, weight: .regular)
        buildLabel.textColor = .secondaryLabel
        buildLabel.numberOfLines = 0
        buildLabel.text = AppBuildInfo.current.displayText

        let stack = UIStackView(arrangedSubviews: [titleLabel, detailLabel, buildLabel])
        stack.axis = .vertical
        stack.spacing = 20
        stack.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(stack)

        NSLayoutConstraint.activate([
            stack.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 24),
            stack.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -24),
            stack.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32)
        ])

        diagnostics.info(category: "ui", name: "root.loaded")
    }

    @objc private func openSettings() {
        diagnostics.info(category: "navigation", name: "settings.open")
        navigationController?.pushViewController(SettingsViewController(), animated: true)
    }
}
