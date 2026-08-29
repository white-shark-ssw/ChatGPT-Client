import UIKit

final class RootViewController: UISplitViewController, UISplitViewControllerDelegate {
    private let diagnostics = DiagnosticsLogger.shared
    private let repository = ConversationRepository()
    private let sidebarViewController: ConversationSidebarViewController
    private let detailViewController: ConversationDetailViewController
    private let detailNavigationController: UINavigationController

    init() {
        sidebarViewController = ConversationSidebarViewController(repository: repository)
        detailViewController = ConversationDetailViewController(repository: repository)
        detailNavigationController = UINavigationController(rootViewController: detailViewController)
        super.init(style: .doubleColumn)
        delegate = self

        let sidebarNavigationController = UINavigationController(rootViewController: sidebarViewController)
        setViewController(sidebarNavigationController, for: .primary)
        setViewController(detailNavigationController, for: .secondary)
        configureHybridSendToolbar()

        repository.onAccountScopeReset = { [weak self] in
            guard let self else { return }
            self.sidebarViewController.resetForAccountScopeChange()
            self.detailViewController.resetForAccountScopeChange()
            self.detailNavigationController.setToolbarHidden(true, animated: false)
            self.show(.primary)
        }
        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.repository.selectConversation(id: id)
            self.detailViewController.loadViewIfNeeded()
            self.detailViewController.title = self.repository.conversations.first(where: { $0.id == id })?.title ?? "新对话"
            self.detailViewController.showConversation(id: id)
            self.detailNavigationController.setToolbarHidden(false, animated: false)
            self.show(.secondary)
        }
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
        detailNavigationController.setToolbarHidden(repository.selectedConversationID == nil, animated: false)
        diagnostics.info(category: "ui", name: "nativeConversationShell.loaded")
    }

    func splitViewController(_ svc: UISplitViewController, topColumnForCollapsingToProposedTopColumn proposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column {
        repository.selectedConversationID == nil ? .primary : .secondary
    }

    private func configureHybridSendToolbar() {
        let button = UIButton(type: .system)
        button.setTitle("发送消息…", for: .normal)
        button.setImage(UIImage(systemName: "paperplane"), for: .normal)
        button.titleLabel?.font = .systemFont(ofSize: 16, weight: .medium)
        button.tintColor = .label
        button.backgroundColor = .secondarySystemBackground
        button.layer.cornerRadius = 18
        button.contentEdgeInsets = UIEdgeInsets(top: 8, left: 18, bottom: 8, right: 18)
        button.addTarget(self, action: #selector(openHybridSend), for: .touchUpInside)
        button.translatesAutoresizingMaskIntoConstraints = false
        button.heightAnchor.constraint(equalToConstant: 36).isActive = true
        button.widthAnchor.constraint(greaterThanOrEqualToConstant: 220).isActive = true
        let flexible = UIBarButtonItem(barButtonSystemItem: .flexibleSpace, target: nil, action: nil)
        detailViewController.toolbarItems = [flexible, UIBarButtonItem(customView: button), UIBarButtonItem(barButtonSystemItem: .flexibleSpace, target: nil, action: nil)]
    }

    @objc private func openHybridSend() {
        guard let conversationID = repository.selectedConversationID else { return }
        let controller = AuthWebViewController.hybridChat
        guard controller.navigationController == nil else { return }
        controller.prepareForConversation(id: conversationID) { [weak self] in self?.syncAfterHybridSend(conversationID: conversationID) }
        diagnostics.info(category: "navigation", name: "hybridSend.open", fields: ["entry": "native_detail"])
        detailNavigationController.pushViewController(controller, animated: true)
    }

    private func syncAfterHybridSend(conversationID: String) {
        diagnostics.info(category: "webSend", name: "nativeReconcile.requested")
        repository.syncLatestMessages(id: conversationID) { [weak self] result in
            guard let self else { return }
            switch result {
            case .success:
                self.diagnostics.info(category: "webSend", name: "nativeReconcile.completed")
                if self.repository.selectedConversationID == conversationID { self.detailViewController.showConversation(id: conversationID) }
            case .failure(let error):
                self.diagnostics.error(category: "webSend", name: "nativeReconcile.failed", error: error)
            }
        }
    }
}
