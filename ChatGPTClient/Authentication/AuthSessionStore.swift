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

final class AuthSessionStore {
    static let shared = AuthSessionStore()

    private static let loginURL = URL(string: "https://chatgpt.com/auth/login")!

    private let diagnostics = DiagnosticsLogger.shared
    private let lock = NSLock()
    private var webState: AuthWebSessionState = .unknown
    private var nativeState: AuthNativeSessionState = .unknown

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

    private func setNativeState(_ state: AuthNativeSessionState) {
        lock.lock()
        nativeState = state
        lock.unlock()
        diagnostics.info(category: "auth", name: "session.nativeState", fields: ["state": state.rawValue])
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
