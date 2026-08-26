import UIKit

final class RootViewController: UISplitViewController, UISplitViewControllerDelegate {
    private let diagnostics = DiagnosticsLogger.shared
    private let repository = ConversationRepository()
    private let sidebarViewController: ConversationSidebarViewController
    private let detailViewController: ConversationDetailViewController

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
            self.detailViewController.showConversation(id: id)
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
        diagnostics.info(category: "ui", name: "nativeConversationShell.loaded")
    }

    func splitViewController(_ svc: UISplitViewController, topColumnForCollapsingToProposedTopColumn proposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column {
        repository.selectedConversationID == nil ? .primary : .secondary
    }
}
