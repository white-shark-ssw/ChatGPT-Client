import Foundation
import WebKit

enum AuthWebSessionState: String {
    case unknown
    case unauthenticated
    case authenticated
}

enum AuthNativeSessionState: String {
    case unknown
    case probing
    case verified
    case notAuthenticated
    case failed
}

enum AuthAccountContextState: String {
    case unknown
    case probing
    case verified
    case notAvailable
    case failed
}

struct AuthAccountContext: Equatable {
    let userID: String
    let accountID: String
    let planType: String?
    let structure: String?
}

final class AuthTransientSession {
    private let session: URLSession
    private let accessToken: String

    fileprivate init?(cookies: [HTTPCookie], accessToken: String) {
        let configuration = URLSessionConfiguration.ephemeral
        configuration.httpShouldSetCookies = true
        guard let storage = configuration.httpCookieStorage else { return nil }
        for cookie in cookies { storage.setCookie(cookie) }
        session = URLSession(configuration: configuration)
        self.accessToken = accessToken
    }

    @discardableResult
    func dataTask(with request: URLRequest, completion: @escaping (Data?, URLResponse?, Error?) -> Void) -> URLSessionDataTask {
        var authorizedRequest = request
        authorizedRequest.setValue("Bearer \(accessToken)", forHTTPHeaderField: "Authorization")
        let task = session.dataTask(with: authorizedRequest, completionHandler: completion)
        task.resume()
        return task
    }

    func finishTasksAndInvalidate() {
        session.finishTasksAndInvalidate()
    }

    func invalidateAndCancel() {
        session.invalidateAndCancel()
    }
}

final class AuthSessionStore {
    static let shared = AuthSessionStore()
    static let accountContextDidChangeNotification = Notification.Name("AuthSessionStore.accountContextDidChange")

    private static let loginURL = URL(string: "https://chatgpt.com/auth/login")!
    private static let sessionURL = URL(string: "https://chatgpt.com/api/auth/session")!

    private let diagnostics = DiagnosticsLogger.shared
    private let lock = NSLock()
    private var webState: AuthWebSessionState = .unknown
    private var nativeState: AuthNativeSessionState = .unknown
    private var accountState: AuthAccountContextState = .unknown
    private var accountContext: AuthAccountContext?

    private init() { }

    @discardableResult
    func observeWebLocation(_ url: URL?) -> AuthWebSessionState {
        let state = Self.webState(for: url)
        guard state != .unknown else { return state }
        lock.lock()
        let changed = webState != state
        webState = state
        lock.unlock()
        if changed { diagnostics.info(category: "auth", name: "session.webState", fields: ["state": state.rawValue]) }
        return state
    }

    func verifiedAccountContext() -> AuthAccountContext? {
        lock.lock()
        defer { lock.unlock() }
        guard accountState == .verified else { return nil }
        return accountContext
    }

    func warmDefaultWebDataStore(completion: @escaping () -> Void) {
        let dataStore = WKWebsiteDataStore.default()
        let cookieStore = dataStore.httpCookieStore
        let span = diagnostics.startSpan(category: "auth", name: "webDataWarmup")
        cookieStore.getAllCookies { [weak self] beforeCookies in
            guard let self else { return }
            let beforeMatched = beforeCookies.filter(Self.isAuthCookieDomain)
            let beforeFields = ["itemCount": String(beforeCookies.count), "matchedItemCount": String(beforeMatched.count)]
            self.diagnostics.info(category: "auth", name: "webDataWarmup.before", traceID: span.traceID, fields: beforeFields)
            dataStore.fetchDataRecords(ofTypes: WKWebsiteDataStore.allWebsiteDataTypes()) { records in
                cookieStore.getAllCookies { afterCookies in
                    let afterMatched = afterCookies.filter(Self.isAuthCookieDomain)
                    let fields = [
                        "beforeItemCount": String(beforeCookies.count),
                        "beforeMatchedItemCount": String(beforeMatched.count),
                        "websiteDataRecordCount": String(records.count),
                        "afterItemCount": String(afterCookies.count),
                        "afterMatchedItemCount": String(afterMatched.count)
                    ]
                    self.diagnostics.info(category: "auth", name: "webDataWarmup.after", traceID: span.traceID, fields: fields)
                    span.end(status: "ok", fields: fields)
                    DispatchQueue.main.async { completion() }
                }
            }
        }
    }

    func probeNativeSession(using cookieStore: WKHTTPCookieStore, completion: @escaping (AuthNativeSessionState) -> Void) {
        setNativeState(.probing)
        let span = diagnostics.startSpan(category: "auth", name: "nativeSessionProbe")
        cookieStore.getAllCookies { [weak self] cookies in
            guard let self else { return }
            let matchedCookies = cookies.filter(Self.isAuthCookieDomain)
            self.diagnostics.info(category: "auth", name: "nativeSessionProbe.webData", traceID: span.traceID, fields: ["itemCount": String(cookies.count), "matchedItemCount": String(matchedCookies.count)])

            let configuration = URLSessionConfiguration.ephemeral
            configuration.httpShouldSetCookies = true
            guard let storage = configuration.httpCookieStorage else {
                self.setNativeState(.failed)
                span.end(status: "failed", fields: ["reason": "missing_http_cookie_storage"])
                completion(.failed)
                return
            }
            for cookie in matchedCookies { storage.setCookie(cookie) }

            let session = URLSession(configuration: configuration)
            session.dataTask(with: URLRequest(url: Self.loginURL)) { [weak self] _, response, error in
                defer { session.finishTasksAndInvalidate() }
                guard let self else { return }
                if let error {
                    self.setNativeState(.failed)
                    self.diagnostics.error(category: "auth", name: "nativeSessionProbe.failed", traceID: span.traceID, error: error)
                    span.end(status: "failed")
                    completion(.failed)
                    return
                }
                guard let response = response as? HTTPURLResponse else {
                    self.setNativeState(.failed)
                    span.end(status: "failed", fields: ["reason": "non_http_response"])
                    completion(.failed)
                    return
                }

                var fields = Self.safeLocationFields(response.url)
                fields["httpStatus"] = String(response.statusCode)
                let accepted = Self.webState(for: response.url) == .authenticated && (200..<400).contains(response.statusCode)
                let result: AuthNativeSessionState = accepted ? .verified : .notAuthenticated
                self.setNativeState(result)
                span.end(status: accepted ? "ok" : "not_authenticated", fields: fields)
                completion(result)
            }.resume()
        }
    }

    func probeAccountContext(using cookieStore: WKHTTPCookieStore, createTransientSession: Bool = false, completion: @escaping (AuthAccountContextState, AuthTransientSession?) -> Void) {
        if verifiedAccountContext() == nil { setAccountState(.probing) }
        let span = diagnostics.startSpan(category: "auth", name: "accountContextProbe")
        cookieStore.getAllCookies { [weak self] cookies in
            guard let self else { return }
            let matchedCookies = cookies.filter(Self.isAuthCookieDomain)
            self.diagnostics.info(category: "auth", name: "accountContextProbe.webData", traceID: span.traceID, fields: ["itemCount": String(cookies.count), "matchedItemCount": String(matchedCookies.count)])
            let configuration = URLSessionConfiguration.ephemeral
            configuration.httpShouldSetCookies = true
            guard let storage = configuration.httpCookieStorage else {
                self.finishAccountProbe(.failed, span: span, fields: ["reason": "missing_http_cookie_storage"], completion: completion)
                return
            }
            for cookie in matchedCookies { storage.setCookie(cookie) }

            let session = URLSession(configuration: configuration)
            session.dataTask(with: URLRequest(url: Self.sessionURL)) { [weak self] data, response, error in
                guard let self else { return }
                if let error {
                    session.finishTasksAndInvalidate()
                    self.diagnostics.error(category: "auth", name: "accountContextProbe.sessionFailed", traceID: span.traceID, error: error)
                    self.finishAccountProbe(.failed, span: span, completion: completion)
                    return
                }
                guard let response = response as? HTTPURLResponse, let data, (200..<300).contains(response.statusCode) else {
                    session.finishTasksAndInvalidate()
                    let statusCode = (response as? HTTPURLResponse)?.statusCode
                    let status = statusCode.map(String.init) ?? "none"
                    let state: AuthAccountContextState = statusCode == 403 ? .failed : .notAvailable
                    var fields = ["stage": "session", "httpStatus": status]
                    if statusCode == 403 { fields["reason"] = "temporary_forbidden" }
                    self.finishAccountProbe(state, span: span, fields: fields, completion: completion)
                    return
                }
                guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let user = payload["user"] as? [String: Any], let userID = user["id"] as? String, !userID.isEmpty, let accessToken = payload["accessToken"] as? String, !accessToken.isEmpty else {
                    session.finishTasksAndInvalidate()
                    self.finishAccountProbe(.notAvailable, span: span, fields: ["stage": "session", "httpStatus": String(response.statusCode), "reason": "missing_required_session_fields"], completion: completion)
                    return
                }

                self.diagnostics.info(category: "auth", name: "accountContextProbe.session", traceID: span.traceID, fields: ["httpStatus": String(response.statusCode), "userID": userID])
                let offsetMinutes = -TimeZone.current.secondsFromGMT() / 60
                guard let accountsURL = URL(string: "https://chatgpt.com/backend-api/accounts/check/v4-2023-04-27?timezone_offset_min=\(offsetMinutes)") else {
                    session.finishTasksAndInvalidate()
                    self.finishAccountProbe(.failed, span: span, fields: ["reason": "invalid_accounts_url"], completion: completion)
                    return
                }
                var request = URLRequest(url: accountsURL)
                request.setValue("Bearer \(accessToken)", forHTTPHeaderField: "Authorization")
                session.dataTask(with: request) { [weak self] data, response, error in
                    defer { session.finishTasksAndInvalidate() }
                    guard let self else { return }
                    if let error {
                        self.diagnostics.error(category: "auth", name: "accountContextProbe.accountsFailed", traceID: span.traceID, error: error)
                        self.finishAccountProbe(.failed, span: span, completion: completion)
                        return
                    }
                    guard let response = response as? HTTPURLResponse, let data, (200..<300).contains(response.statusCode) else {
                        let statusCode = (response as? HTTPURLResponse)?.statusCode
                        let status = statusCode.map(String.init) ?? "none"
                        let state: AuthAccountContextState = statusCode == 403 ? .failed : .notAvailable
                        var fields = ["stage": "accounts", "httpStatus": status]
                        if statusCode == 403 { fields["reason"] = "temporary_forbidden" }
                        self.finishAccountProbe(state, span: span, fields: fields, completion: completion)
                        return
                    }
                    guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let accounts = payload["accounts"] as? [String: Any], let accountOrdering = payload["account_ordering"] as? [String], !accountOrdering.isEmpty else {
                        self.finishAccountProbe(.notAvailable, span: span, fields: ["stage": "accounts", "httpStatus": String(response.statusCode), "reason": "missing_account_ordering"], completion: completion)
                        return
                    }

                    var selectedAccount: [String: Any]?
                    var selectedAccountID: String?
                    for key in accountOrdering {
                        guard let entry = accounts[key] as? [String: Any] else { continue }
                        if let canAccess = entry["can_access_with_session"] as? Bool, !canAccess { continue }
                        guard let account = entry["account"] as? [String: Any], let accountID = account["account_id"] as? String, !accountID.isEmpty else { continue }
                        selectedAccount = account
                        selectedAccountID = accountID
                        break
                    }
                    guard let account = selectedAccount, let accountID = selectedAccountID else {
                        self.finishAccountProbe(.notAvailable, span: span, fields: ["stage": "accounts", "httpStatus": String(response.statusCode), "reason": "missing_usable_ordered_account", "accountCount": String(accounts.count), "accountOrderingCount": String(accountOrdering.count)], completion: completion)
                        return
                    }

                    let context = AuthAccountContext(userID: userID, accountID: accountID, planType: account["plan_type"] as? String, structure: account["structure"] as? String)
                    self.setVerifiedAccountContext(context)
                    var fields = ["httpStatus": String(response.statusCode), "userID": userID, "accountID": accountID, "accountCount": String(accounts.count), "accountOrderingCount": String(accountOrdering.count)]
                    if let planType = context.planType { fields["planType"] = planType }
                    if let structure = context.structure { fields["structure"] = structure }
                    self.diagnostics.info(category: "auth", name: "accountContextProbe.accounts", traceID: span.traceID, fields: fields)

                    var transientSession: AuthTransientSession?
                    if createTransientSession {
                        guard let createdSession = AuthTransientSession(cookies: matchedCookies, accessToken: accessToken) else {
                            self.finishAccountProbe(.failed, span: span, fields: ["stage": "transient_session", "reason": "missing_http_cookie_storage"], completion: completion)
                            return
                        }
                        transientSession = createdSession
                    }
                    self.finishAccountProbe(.verified, span: span, fields: fields, transientSession: transientSession, completion: completion)
                }.resume()
            }.resume()
        }
    }

    private func finishAccountProbe(_ state: AuthAccountContextState, span: DiagnosticsSpan, fields: [String: String] = [:], transientSession: AuthTransientSession? = nil, completion: @escaping (AuthAccountContextState, AuthTransientSession?) -> Void) {
        if state != .verified {
            if state == .failed, verifiedAccountContext() != nil { diagnostics.info(category: "auth", name: "session.accountStatePreserved", fields: ["state": AuthAccountContextState.verified.rawValue, "probeResult": AuthAccountContextState.failed.rawValue]) }
            else { setAccountState(state) }
        }
        span.end(status: state == .verified ? "ok" : state == .notAvailable ? "not_available" : "failed", fields: fields)
        completion(state, transientSession)
    }

    private func setNativeState(_ state: AuthNativeSessionState) {
        lock.lock()
        nativeState = state
        lock.unlock()
        diagnostics.info(category: "auth", name: "session.nativeState", fields: ["state": state.rawValue])
    }

    private func setVerifiedAccountContext(_ context: AuthAccountContext) {
        lock.lock()
        let previousContext = accountContext
        let stateChanged = accountState != .verified
        accountContext = context
        accountState = .verified
        lock.unlock()
        if stateChanged { diagnostics.info(category: "auth", name: "session.accountState", fields: ["state": AuthAccountContextState.verified.rawValue]) }
        if previousContext != context { NotificationCenter.default.post(name: Self.accountContextDidChangeNotification, object: self) }
    }

    private func setAccountState(_ state: AuthAccountContextState) {
        lock.lock()
        let previousState = accountState
        let hadContext = accountContext != nil
        accountState = state
        if state == .notAvailable || state == .unknown { accountContext = nil }
        let contextInvalidated = hadContext && accountContext == nil
        lock.unlock()
        if previousState != state { diagnostics.info(category: "auth", name: "session.accountState", fields: ["state": state.rawValue]) }
        if contextInvalidated { NotificationCenter.default.post(name: Self.accountContextDidChangeNotification, object: self) }
    }

    private static func webState(for url: URL?) -> AuthWebSessionState {
        guard let url, let host = url.host?.lowercased(), host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") else { return .unknown }
        return url.path.hasPrefix("/auth") ? .unauthenticated : .authenticated
    }

    private static func isAuthCookieDomain(_ cookie: HTTPCookie) -> Bool {
        let domain = cookie.domain.lowercased().trimmingCharacters(in: CharacterSet(charactersIn: "."))
        return domain == "chatgpt.com" || domain.hasSuffix(".chatgpt.com") || domain == "openai.com" || domain.hasSuffix(".openai.com")
    }

    private static func safeLocationFields(_ url: URL?) -> [String: String] {
        guard let url, let host = url.host?.lowercased() else { return ["destination": "unknown"] }
        let destination: String
        if host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") {
            destination = url.path.hasPrefix("/auth") ? "chatgpt_auth" : "chatgpt"
        } else if host == "auth.openai.com" || host.hasSuffix(".openai.com") {
            destination = "openai_auth"
        } else {
            destination = "external"
        }
        return ["host": host, "destination": destination]
    }
}
