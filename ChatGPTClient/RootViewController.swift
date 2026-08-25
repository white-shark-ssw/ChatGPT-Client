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
        titleLabel.text = "网页登录验证"
        titleLabel.numberOfLines = 0

        let detailLabel = UILabel()
        detailLabel.font = .preferredFont(forTextStyle: .body)
        detailLabel.textColor = .secondaryLabel
        detailLabel.numberOfLines = 0
        detailLabel.text = "当前阶段只验证 ChatGPT 现行网页登录与 Continue with Google 路径。请进入登录页并按你平时的方式选择 Google 登录；如果出现阻止或错误页面，保持现场并从设置导出诊断 JSON。"

        let loginButton = UIButton(type: .system)
        loginButton.setTitle("开始网页登录验证", for: .normal)
        loginButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
        loginButton.addTarget(self, action: #selector(openLoginVerification), for: .touchUpInside)

        let buildLabel = UILabel()
        buildLabel.font = .monospacedSystemFont(ofSize: 12, weight: .regular)
        buildLabel.textColor = .secondaryLabel
        buildLabel.numberOfLines = 0
        buildLabel.text = AppBuildInfo.current.displayText

        let stack = UIStackView(arrangedSubviews: [titleLabel, detailLabel, loginButton, buildLabel])
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

    @objc private func openLoginVerification() {
        diagnostics.info(category: "navigation", name: "authVerification.open")
        navigationController?.pushViewController(AuthWebViewController(), animated: true)
    }

    @objc private func openSettings() {
        diagnostics.info(category: "navigation", name: "settings.open")
        navigationController?.pushViewController(SettingsViewController(), animated: true)
    }
}
