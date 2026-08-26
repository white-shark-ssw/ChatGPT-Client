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

struct AuthAccountContext {
    let userID: String
    let accountID: String
    let planType: String?
    let structure: String?
}

final class AuthSessionStore {
    static let shared = AuthSessionStore()

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

    func probeAccountContext(using cookieStore: WKHTTPCookieStore, completion: @escaping (AuthAccountContextState) -> Void) {
        setAccountState(.probing)
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
                    let status = (response as? HTTPURLResponse).map { String($0.statusCode) } ?? "none"
                    self.finishAccountProbe(.notAvailable, span: span, fields: ["stage": "session", "httpStatus": status], completion: completion)
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
                        let status = (response as? HTTPURLResponse).map { String($0.statusCode) } ?? "none"
                        self.finishAccountProbe(.notAvailable, span: span, fields: ["stage": "accounts", "httpStatus": status], completion: completion)
                        return
                    }
                    guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let accounts = payload["accounts"] as? [String: Any], let defaultEntry = accounts["default"] as? [String: Any], let account = defaultEntry["account"] as? [String: Any], let accountID = account["id"] as? String, !accountID.isEmpty else {
                        self.finishAccountProbe(.notAvailable, span: span, fields: ["stage": "accounts", "httpStatus": String(response.statusCode), "reason": "missing_default_account"], completion: completion)
                        return
                    }

                    let context = AuthAccountContext(userID: userID, accountID: accountID, planType: account["plan_type"] as? String, structure: account["structure"] as? String)
                    self.lock.lock()
                    self.accountContext = context
                    self.lock.unlock()
                    var fields = ["httpStatus": String(response.statusCode), "userID": userID, "accountID": accountID]
                    if let planType = context.planType { fields["planType"] = planType }
                    if let structure = context.structure { fields["structure"] = structure }
                    self.diagnostics.info(category: "auth", name: "accountContextProbe.accounts", traceID: span.traceID, fields: fields)
                    self.finishAccountProbe(.verified, span: span, fields: fields, completion: completion)
                }.resume()
            }.resume()
        }
    }

    private func finishAccountProbe(_ state: AuthAccountContextState, span: DiagnosticsSpan, fields: [String: String] = [:], completion: @escaping (AuthAccountContextState) -> Void) {
        setAccountState(state)
        span.end(status: state == .verified ? "ok" : state == .notAvailable ? "not_available" : "failed", fields: fields)
        completion(state)
    }

    private func setNativeState(_ state: AuthNativeSessionState) {
        lock.lock()
        nativeState = state
        lock.unlock()
        diagnostics.info(category: "auth", name: "session.nativeState", fields: ["state": state.rawValue])
    }

    private func setAccountState(_ state: AuthAccountContextState) {
        lock.lock()
        accountState = state
        if state != .verified { accountContext = nil }
        lock.unlock()
        diagnostics.info(category: "auth", name: "session.accountState", fields: ["state": state.rawValue])
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
