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
        titleLabel.text = "会话读取协议验证"
        titleLabel.numberOfLines = 0

        let detailLabel = UILabel()
        detailLabel.font = .preferredFont(forTextStyle: .body)
        detailLabel.textColor = .secondaryLabel
        detailLabel.numberOfLines = 0
        detailLabel.text = "Google 登录、WebKit 持久会话和账户上下文已经完成真机验证。协议读取入口会先复用同一认证链，再用临时原生会话请求当前会话列表与其中一条会话详情；诊断只记录 HTTP 状态、耗时、数量和树结构统计，不记录聊天正文、Cookie、Token 或 Authorization 值。"

        let authButton = UIButton(type: .system)
        authButton.setTitle("登录与账户上下文回归验证", for: .normal)
        authButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
        authButton.addTarget(self, action: #selector(openLoginVerification), for: .touchUpInside)

        let protocolButton = UIButton(type: .system)
        protocolButton.setTitle("开始会话列表与详情验证", for: .normal)
        protocolButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
        protocolButton.addTarget(self, action: #selector(openProtocolReadVerification), for: .touchUpInside)

        let buildLabel = UILabel()
        buildLabel.font = .monospacedSystemFont(ofSize: 12, weight: .regular)
        buildLabel.textColor = .secondaryLabel
        buildLabel.numberOfLines = 0
        buildLabel.text = AppBuildInfo.current.displayText

        let stack = UIStackView(arrangedSubviews: [titleLabel, detailLabel, authButton, protocolButton, buildLabel])
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
        navigationController?.pushViewController(AuthWebViewController(mode: .authentication), animated: true)
    }

    @objc private func openProtocolReadVerification() {
        diagnostics.info(category: "navigation", name: "protocolReadVerification.open")
        navigationController?.pushViewController(AuthWebViewController(mode: .protocolRead), animated: true)
    }

    @objc private func openSettings() {
        diagnostics.info(category: "navigation", name: "settings.open")
        navigationController?.pushViewController(SettingsViewController(), animated: true)
    }
}
