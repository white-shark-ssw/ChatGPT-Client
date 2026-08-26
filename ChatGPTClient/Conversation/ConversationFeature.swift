import UIKit
import WebKit

struct ConversationSummary {
    let id: String
    let title: String
    let updateTime: TimeInterval?
}

struct ConversationMessage {
    enum Role: String {
        case user
        case assistant
    }

    let id: String
    let role: Role
    let text: String
    let createTime: TimeInterval?
}

struct ConversationDetail {
    let id: String
    let title: String
    let messages: [ConversationMessage]
}

enum ConversationRepositoryError: LocalizedError {
    case authenticationNotAvailable
    case missingTransientSession
    case invalidResponse
    case httpStatus(Int)
    case invalidPayload
    case missingCurrentNode
    case conversationIdentityMismatch

    var errorDescription: String? {
        switch self {
        case .authenticationNotAvailable: return "当前登录会话不可用，请先完成登录或账户验证。"
        case .missingTransientSession: return "未建立可用的原生读取会话。"
        case .invalidResponse: return "服务器返回了无法识别的响应。"
        case .httpStatus(let status): return "服务器请求失败（HTTP \(status)）。"
        case .invalidPayload: return "会话数据格式不完整。"
        case .missingCurrentNode: return "会话缺少当前消息分支。"
        case .conversationIdentityMismatch: return "返回的会话身份与当前选择不一致。"
        }
    }
}

final class ConversationRepository {
    private static let listURL: URL = {
        var components = URLComponents(string: "https://chatgpt.com/backend-api/conversations")!
        components.queryItems = [
            URLQueryItem(name: "offset", value: "0"),
            URLQueryItem(name: "limit", value: "28"),
            URLQueryItem(name: "order", value: "updated")
        ]
        return components.url!
    }()

    private let diagnostics = DiagnosticsLogger.shared
    private let authSessionStore = AuthSessionStore.shared
    private var transientSession: AuthTransientSession?

    private(set) var conversations: [ConversationSummary] = []
    private(set) var selectedConversationID: String?
    private(set) var selectedConversation: ConversationDetail?

    deinit {
        transientSession?.finishTasksAndInvalidate()
    }

    func selectConversation(id: String) {
        selectedConversationID = id
        if selectedConversation?.id != id { selectedConversation = nil }
    }

    func loadConversations(completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        let span = diagnostics.startSpan(category: "conversation", name: "listLoad")
        withTransientSession { [weak self] result in
            guard let self else { return }
            switch result {
            case .failure(let error):
                span.end(status: "failed", fields: ["stage": "auth"])
                self.finishOnMain(.failure(error), completion: completion)
            case .success(let session):
                self.requestConversationList(using: session, span: span, completion: completion)
            }
        }
    }

    func loadSelectedConversation(completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        guard let id = selectedConversationID else {
            finishOnMain(.failure(ConversationRepositoryError.invalidPayload), completion: completion)
            return
        }
        loadConversation(id: id, completion: completion)
    }

    func loadConversation(id: String, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        selectedConversationID = id
        let span = diagnostics.startSpan(category: "conversation", name: "detailLoad")
        withTransientSession { [weak self] result in
            guard let self else { return }
            switch result {
            case .failure(let error):
                span.end(status: "failed", fields: ["stage": "auth"])
                self.finishOnMain(.failure(error), completion: completion)
            case .success(let session):
                self.requestConversationDetail(id: id, using: session, span: span, completion: completion)
            }
        }
    }

    private func withTransientSession(completion: @escaping (Result<AuthTransientSession, Error>) -> Void) {
        if let transientSession {
            completion(.success(transientSession))
            return
        }
        diagnostics.info(category: "conversation", name: "authContext.requested")
        let cookieStore = WKWebsiteDataStore.default().httpCookieStore
        authSessionStore.probeAccountContext(using: cookieStore, createTransientSession: true) { [weak self] state, session in
            guard let self else {
                session?.finishTasksAndInvalidate()
                return
            }
            guard state == .verified, let session else {
                session?.finishTasksAndInvalidate()
                completion(.failure(ConversationRepositoryError.authenticationNotAvailable))
                return
            }
            self.transientSession = session
            completion(.success(session))
        }
    }

    private func requestConversationList(using session: AuthTransientSession, span: DiagnosticsSpan, completion: @escaping (Result<[ConversationSummary], Error>) -> Void) {
        diagnostics.info(category: "conversation", name: "list.request", traceID: span.traceID, fields: ["method": "GET", "route": "conversation_list", "offset": "0", "limit": "28", "order": "updated"])
        var request = URLRequest(url: Self.listURL)
        request.httpMethod = "GET"
        session.dataTask(with: request) { [weak self] data, response, error in
            guard let self else { return }
            if let error {
                self.diagnostics.error(category: "conversation", name: "list.failed", traceID: span.traceID, error: error)
                span.end(status: "failed", fields: ["stage": "network"])
                self.finishOnMain(.failure(error), completion: completion)
                return
            }
            guard let response = response as? HTTPURLResponse, let data else {
                span.end(status: "failed", fields: ["stage": "response", "reason": "non_http_response"])
                self.finishOnMain(.failure(ConversationRepositoryError.invalidResponse), completion: completion)
                return
            }
            guard (200..<300).contains(response.statusCode) else {
                span.end(status: "failed", fields: ["stage": "response", "httpStatus": String(response.statusCode)])
                self.finishOnMain(.failure(ConversationRepositoryError.httpStatus(response.statusCode)), completion: completion)
                return
            }
            guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let rawItems = payload["items"] as? [[String: Any]] else {
                span.end(status: "failed", fields: ["stage": "parse", "reason": "missing_items"])
                self.finishOnMain(.failure(ConversationRepositoryError.invalidPayload), completion: completion)
                return
            }

            let items = rawItems.compactMap(Self.parseConversationSummary)
            var fields = ["httpStatus": String(response.statusCode), "byteCount": String(data.count), "itemCount": String(items.count)]
            if let total = payload["total"] as? NSNumber { fields["totalCount"] = total.stringValue }
            self.diagnostics.info(category: "conversation", name: "list.response", traceID: span.traceID, fields: fields)
            span.end(status: "ok", fields: fields)
            DispatchQueue.main.async {
                self.conversations = items
                self.finishOnMain(.success(items), completion: completion)
            }
        }
    }

    private func requestConversationDetail(id: String, using session: AuthTransientSession, span: DiagnosticsSpan, completion: @escaping (Result<ConversationDetail, Error>) -> Void) {
        let detailURL = URL(string: "https://chatgpt.com/backend-api/conversation")!.appendingPathComponent(id)
        diagnostics.info(category: "conversation", name: "detail.request", traceID: span.traceID, fields: ["method": "GET", "route": "conversation_detail"])
        var request = URLRequest(url: detailURL)
        request.httpMethod = "GET"
        session.dataTask(with: request) { [weak self] data, response, error in
            guard let self else { return }
            if let error {
                self.diagnostics.error(category: "conversation", name: "detail.failed", traceID: span.traceID, error: error)
                span.end(status: "failed", fields: ["stage": "network"])
                self.finishOnMain(.failure(error), completion: completion)
                return
            }
            guard let response = response as? HTTPURLResponse, let data else {
                span.end(status: "failed", fields: ["stage": "response", "reason": "non_http_response"])
                self.finishOnMain(.failure(ConversationRepositoryError.invalidResponse), completion: completion)
                return
            }
            guard (200..<300).contains(response.statusCode) else {
                span.end(status: "failed", fields: ["stage": "response", "httpStatus": String(response.statusCode)])
                self.finishOnMain(.failure(ConversationRepositoryError.httpStatus(response.statusCode)), completion: completion)
                return
            }
            guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let mapping = payload["mapping"] as? [String: Any], let currentNode = payload["current_node"] as? String, !currentNode.isEmpty else {
                span.end(status: "failed", fields: ["stage": "parse", "reason": "missing_mapping_or_current_node"])
                self.finishOnMain(.failure(ConversationRepositoryError.missingCurrentNode), completion: completion)
                return
            }
            if let returnedID = payload["conversation_id"] as? String, !returnedID.isEmpty, returnedID != id {
                span.end(status: "failed", fields: ["stage": "identity", "reason": "conversation_identity_mismatch"])
                self.finishOnMain(.failure(ConversationRepositoryError.conversationIdentityMismatch), completion: completion)
                return
            }

            let messages = Self.parseCurrentBranch(mapping: mapping, currentNode: currentNode)
            let title = Self.normalizedTitle(payload["title"] as? String)
            let detail = ConversationDetail(id: id, title: title, messages: messages)
            let fields = ["httpStatus": String(response.statusCode), "byteCount": String(data.count), "mappingCount": String(mapping.count), "visibleMessageCount": String(messages.count)]
            self.diagnostics.info(category: "conversation", name: "detail.response", traceID: span.traceID, fields: fields)
            span.end(status: "ok", fields: fields)
            DispatchQueue.main.async {
                guard self.selectedConversationID == id else {
                    self.diagnostics.info(category: "conversation", name: "detail.discarded", fields: ["reason": "selection_changed"])
                    return
                }
                self.selectedConversation = detail
                self.finishOnMain(.success(detail), completion: completion)
            }
        }
    }

    private func finishOnMain<T>(_ result: Result<T, Error>, completion: @escaping (Result<T, Error>) -> Void) {
        if Thread.isMainThread { completion(result) } else { DispatchQueue.main.async { completion(result) } }
    }

    private static func parseConversationSummary(_ item: [String: Any]) -> ConversationSummary? {
        guard let id = item["id"] as? String, !id.isEmpty else { return nil }
        return ConversationSummary(id: id, title: normalizedTitle(item["title"] as? String), updateTime: (item["update_time"] as? NSNumber)?.doubleValue)
    }

    private static func normalizedTitle(_ title: String?) -> String {
        let trimmed = title?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
        return trimmed.isEmpty ? "未命名会话" : trimmed
    }

    private static func parseCurrentBranch(mapping: [String: Any], currentNode: String) -> [ConversationMessage] {
        var nodeIDs: [String] = []
        var visited = Set<String>()
        var nodeID: String? = currentNode
        while let currentID = nodeID, !currentID.isEmpty, visited.insert(currentID).inserted {
            nodeIDs.append(currentID)
            guard let node = mapping[currentID] as? [String: Any] else { break }
            nodeID = node["parent"] as? String
        }

        var messages: [ConversationMessage] = []
        for id in nodeIDs.reversed() {
            guard let node = mapping[id] as? [String: Any], let message = node["message"] as? [String: Any], let author = message["author"] as? [String: Any], let rawRole = author["role"] as? String, let role = ConversationMessage.Role(rawValue: rawRole), let content = message["content"] as? [String: Any] else { continue }
            let text = visibleText(from: content)
            guard !text.isEmpty else { continue }
            let messageID = (message["id"] as? String).flatMap { $0.isEmpty ? nil : $0 } ?? id
            messages.append(ConversationMessage(id: messageID, role: role, text: text, createTime: (message["create_time"] as? NSNumber)?.doubleValue))
        }
        return messages
    }

    private static func visibleText(from content: [String: Any]) -> String {
        var textParts: [String] = []
        if let text = content["text"] as? String, !text.isEmpty { textParts.append(text) }
        if let parts = content["parts"] as? [Any] {
            for part in parts {
                if let text = part as? String, !text.isEmpty { textParts.append(text) }
                else if let object = part as? [String: Any], let text = object["text"] as? String, !text.isEmpty { textParts.append(text) }
            }
        }
        return textParts.joined(separator: "\n").trimmingCharacters(in: .whitespacesAndNewlines)
    }
}

final class ConversationSidebarViewController: UITableViewController {
    var onSelectConversation: ((String) -> Void)?

    private let repository: ConversationRepository
    private let diagnostics = DiagnosticsLogger.shared
    private var loading = false
    private var errorView: UIView?

    init(repository: ConversationRepository) {
        self.repository = repository
        super.init(style: .plain)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "ChatGPT"
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "ConversationCell")
        tableView.rowHeight = 58
        navigationItem.leftBarButtonItem = UIBarButtonItem(title: "设置", style: .plain, target: self, action: #selector(openSettings))
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(reloadConversations))
        refreshControl = UIRefreshControl()
        refreshControl?.addTarget(self, action: #selector(reloadConversations), for: .valueChanged)
        loadConversations()
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        repository.conversations.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let item = repository.conversations[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "ConversationCell", for: indexPath)
        cell.textLabel?.text = item.title
        cell.textLabel?.font = .preferredFont(forTextStyle: .body)
        cell.textLabel?.numberOfLines = 2
        cell.accessoryType = repository.selectedConversationID == item.id ? .checkmark : .none
        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        let item = repository.conversations[indexPath.row]
        repository.selectConversation(id: item.id)
        tableView.reloadData()
        diagnostics.info(category: "navigation", name: "conversation.selected")
        onSelectConversation?(item.id)
    }

    @objc private func reloadConversations() {
        loadConversations()
    }

    private func loadConversations() {
        guard !loading else { return }
        loading = true
        errorView?.removeFromSuperview()
        errorView = nil
        navigationItem.rightBarButtonItem?.isEnabled = false
        repository.loadConversations { [weak self] result in
            guard let self else { return }
            self.loading = false
            self.refreshControl?.endRefreshing()
            self.navigationItem.rightBarButtonItem?.isEnabled = true
            switch result {
            case .success:
                self.tableView.reloadData()
            case .failure(let error):
                self.showError(error)
            }
        }
    }

    private func showError(_ error: Error) {
        let label = UILabel()
        label.font = .preferredFont(forTextStyle: .body)
        label.textColor = .secondaryLabel
        label.textAlignment = .center
        label.numberOfLines = 0
        label.text = error.localizedDescription

        let retryButton = UIButton(type: .system)
        retryButton.setTitle("重新加载", for: .normal)
        retryButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
        retryButton.addTarget(self, action: #selector(reloadConversations), for: .touchUpInside)

        let loginButton = UIButton(type: .system)
        loginButton.setTitle("登录 / 账户验证", for: .normal)
        loginButton.addTarget(self, action: #selector(openLogin), for: .touchUpInside)

        let stack = UIStackView(arrangedSubviews: [label, retryButton, loginButton])
        stack.axis = .vertical
        stack.alignment = .center
        stack.spacing = 12
        stack.translatesAutoresizingMaskIntoConstraints = false
        tableView.addSubview(stack)
        NSLayoutConstraint.activate([
            stack.centerXAnchor.constraint(equalTo: tableView.frameLayoutGuide.centerXAnchor),
            stack.centerYAnchor.constraint(equalTo: tableView.frameLayoutGuide.centerYAnchor),
            stack.widthAnchor.constraint(lessThanOrEqualTo: tableView.frameLayoutGuide.widthAnchor, multiplier: 0.8)
        ])
        errorView = stack
    }

    @objc private func openLogin() {
        diagnostics.info(category: "navigation", name: "nativeRead.login.open")
        navigationController?.pushViewController(AuthWebViewController(mode: .authentication), animated: true)
    }

    @objc private func openSettings() {
        diagnostics.info(category: "navigation", name: "settings.open")
        navigationController?.pushViewController(SettingsViewController(), animated: true)
    }
}

final class ConversationDetailViewController: UIViewController, UITableViewDataSource {
    private let repository: ConversationRepository
    private let tableView = UITableView(frame: .zero, style: .plain)
    private let activityIndicator = UIActivityIndicatorView(style: .medium)
    private let stateLabel = UILabel()
    private var messages: [ConversationMessage] = []
    private var loadingConversationID: String?

    init(repository: ConversationRepository) {
        self.repository = repository
        super.init(nibName: nil, bundle: nil)
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        title = "新对话"

        tableView.dataSource = self
        tableView.separatorStyle = .none
        tableView.keyboardDismissMode = .interactive
        tableView.rowHeight = UITableView.automaticDimension
        tableView.estimatedRowHeight = 96
        tableView.register(ConversationMessageCell.self, forCellReuseIdentifier: ConversationMessageCell.reuseIdentifier)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(tableView)

        stateLabel.font = .preferredFont(forTextStyle: .body)
        stateLabel.textColor = .secondaryLabel
        stateLabel.textAlignment = .center
        stateLabel.numberOfLines = 0
        stateLabel.text = "从侧边栏选择一个会话"
        stateLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(stateLabel)

        activityIndicator.hidesWhenStopped = true
        activityIndicator.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(activityIndicator)

        NSLayoutConstraint.activate([
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            tableView.topAnchor.constraint(equalTo: view.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            stateLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            stateLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            stateLabel.leadingAnchor.constraint(greaterThanOrEqualTo: view.leadingAnchor, constant: 24),
            stateLabel.trailingAnchor.constraint(lessThanOrEqualTo: view.trailingAnchor, constant: -24),
            activityIndicator.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicator.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -36)
        ])
    }

    func showConversation(id: String) {
        guard loadingConversationID != id || repository.selectedConversation?.id != id else { return }
        repository.selectConversation(id: id)
        loadingConversationID = id
        messages = []
        tableView.reloadData()
        stateLabel.text = "正在读取会话…"
        stateLabel.isHidden = false
        activityIndicator.startAnimating()
        repository.loadConversation(id: id) { [weak self] result in
            guard let self, self.repository.selectedConversationID == id else { return }
            self.loadingConversationID = nil
            self.activityIndicator.stopAnimating()
            switch result {
            case .success(let detail):
                self.title = detail.title
                self.messages = detail.messages
                self.stateLabel.text = detail.messages.isEmpty ? "当前分支没有可显示的用户或助手文本消息" : nil
                self.stateLabel.isHidden = !detail.messages.isEmpty
                self.tableView.reloadData()
            case .failure(let error):
                self.stateLabel.text = "读取失败\n\(error.localizedDescription)"
                self.stateLabel.isHidden = false
            }
        }
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        messages.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: ConversationMessageCell.reuseIdentifier, for: indexPath) as! ConversationMessageCell
        cell.configure(with: messages[indexPath.row])
        return cell
    }
}

final class ConversationMessageCell: UITableViewCell {
    static let reuseIdentifier = "ConversationMessageCell"

    private let bubbleView = UIView()
    private let messageLabel = UILabel()
    private var userLeadingConstraint: NSLayoutConstraint!
    private var userTrailingConstraint: NSLayoutConstraint!
    private var assistantLeadingConstraint: NSLayoutConstraint!
    private var assistantTrailingConstraint: NSLayoutConstraint!
    private var maxWidthConstraint: NSLayoutConstraint!

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        selectionStyle = .none
        backgroundColor = .systemBackground
        contentView.backgroundColor = .systemBackground

        bubbleView.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(bubbleView)
        messageLabel.font = .preferredFont(forTextStyle: .body)
        messageLabel.numberOfLines = 0
        messageLabel.translatesAutoresizingMaskIntoConstraints = false
        bubbleView.addSubview(messageLabel)

        userLeadingConstraint = bubbleView.leadingAnchor.constraint(greaterThanOrEqualTo: contentView.layoutMarginsGuide.leadingAnchor, constant: 44)
        userTrailingConstraint = bubbleView.trailingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.trailingAnchor)
        assistantLeadingConstraint = bubbleView.leadingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.leadingAnchor)
        assistantTrailingConstraint = bubbleView.trailingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.trailingAnchor)
        maxWidthConstraint = bubbleView.widthAnchor.constraint(lessThanOrEqualTo: contentView.widthAnchor, multiplier: 0.82)

        NSLayoutConstraint.activate([
            bubbleView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 7),
            bubbleView.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -7),
            messageLabel.leadingAnchor.constraint(equalTo: bubbleView.leadingAnchor, constant: 12),
            messageLabel.trailingAnchor.constraint(equalTo: bubbleView.trailingAnchor, constant: -12),
            messageLabel.topAnchor.constraint(equalTo: bubbleView.topAnchor, constant: 9),
            messageLabel.bottomAnchor.constraint(equalTo: bubbleView.bottomAnchor, constant: -9)
        ])
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    func configure(with message: ConversationMessage) {
        messageLabel.text = message.text
        NSLayoutConstraint.deactivate([userLeadingConstraint, userTrailingConstraint, assistantLeadingConstraint, assistantTrailingConstraint, maxWidthConstraint])
        switch message.role {
        case .user:
            bubbleView.backgroundColor = .secondarySystemBackground
            bubbleView.layer.cornerRadius = 18
            NSLayoutConstraint.activate([userLeadingConstraint, userTrailingConstraint, maxWidthConstraint])
        case .assistant:
            bubbleView.backgroundColor = .clear
            bubbleView.layer.cornerRadius = 0
            NSLayoutConstraint.activate([assistantLeadingConstraint, assistantTrailingConstraint])
        }
    }
}
