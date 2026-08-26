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
        titleLabel.text = "登录与原生会话验证"
        titleLabel.numberOfLines = 0

        let detailLabel = UILabel()
        detailLabel.font = .preferredFont(forTextStyle: .body)
        detailLabel.textColor = .secondaryLabel
        detailLabel.numberOfLines = 0
        detailLabel.text = "当前已验证 Continue with Google 与网页登录持久化。本候选会在网页确认已登录后，自动把当前 WebKit 会话临时复制到内存中的原生 URLSession，再请求同一个登录入口验证服务器是否接受原生会话。不会记录 Cookie、Token 或 Authorization 值。"

        let loginButton = UIButton(type: .system)
        loginButton.setTitle("开始登录与原生会话验证", for: .normal)
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
