import UIKit

final class RootViewController: UISplitViewController {
    private let diagnostics = DiagnosticsLogger.shared
    private let repository = ConversationRepository()
    private let sidebarViewController: ConversationSidebarViewController
    private let detailViewController: ConversationDetailViewController

    init() {
        sidebarViewController = ConversationSidebarViewController(repository: repository)
        detailViewController = ConversationDetailViewController(repository: repository)
        super.init(style: .doubleColumn)
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
        AuthSessionStore.shared.warmDefaultWebDataStore { [weak self] in self?.configureConversationShell() }
    }

    private func configureConversationShell() {
        let sidebarNavigationController = UINavigationController(rootViewController: sidebarViewController)
        let detailNavigationController = UINavigationController(rootViewController: detailViewController)
        setViewController(sidebarNavigationController, for: .primary)
        setViewController(detailNavigationController, for: .secondary)
        detailViewController.navigationItem.leftItemsSupplementBackButton = true
        detailViewController.navigationItem.leftBarButtonItem = displayModeButtonItem

        sidebarViewController.onSelectConversation = { [weak self] id in
            guard let self else { return }
            self.detailViewController.showConversation(id: id)
            self.show(.secondary)
        }

        diagnostics.info(category: "ui", name: "nativeConversationShell.loaded")
    }
}