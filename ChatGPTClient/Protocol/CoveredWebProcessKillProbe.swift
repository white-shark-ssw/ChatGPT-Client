import Foundation
import ObjectiveC.runtime
import WebKit

private enum CoveredWebProcessKillProbe {
    private static let candidate = "DEV-send-stream-0.1.0-b102"
    private static let delaySeconds: TimeInterval = 120
    private static let submitMarker = "window.__coveredWebSendExecutor.submit("
    private static var installed = false
    private static var armed = false

    static func install() {
        precondition(Thread.isMainThread)
        guard AppBuildInfo.current.candidate == candidate, !installed else { return }
        let originalSelector = #selector(WKWebView.evaluateJavaScript(_:completionHandler:))
        let probeSelector = #selector(WKWebView.b102_evaluateJavaScript(_:completionHandler:))
        guard let originalMethod = class_getInstanceMethod(WKWebView.self, originalSelector), let probeMethod = class_getInstanceMethod(WKWebView.self, probeSelector) else {
            DiagnosticsLogger.shared.error(category: "webSend", name: "coveredExecutor.killProbe", fields: ["state": "install_failed"])
            return
        }
        method_exchangeImplementations(originalMethod, probeMethod)
        installed = true
        DiagnosticsLogger.shared.warning(category: "webSend", name: "coveredExecutor.killProbe", fields: ["state": "installed", "delaySeconds": String(Int(delaySeconds))])
    }

    static func observe(script: String, webView: WKWebView) {
        precondition(Thread.isMainThread)
        guard installed, !armed, script.contains(submitMarker) else { return }
        armed = true
        DiagnosticsLogger.shared.warning(category: "webSend", name: "coveredExecutor.killProbe", fields: ["state": "armed", "delaySeconds": String(Int(delaySeconds))])
        DispatchQueue.main.asyncAfter(deadline: .now() + delaySeconds) { [weak webView] in
            guard let webView else {
                DiagnosticsLogger.shared.warning(category: "webSend", name: "coveredExecutor.killProbe", fields: ["state": "webview_released"])
                return
            }
            let selector = NSSelectorFromString("_killWebContentProcessAndResetState")
            guard webView.responds(to: selector) else {
                DiagnosticsLogger.shared.error(category: "webSend", name: "coveredExecutor.killProbe", fields: ["state": "spi_unavailable"])
                return
            }
            DiagnosticsLogger.shared.warning(category: "webSend", name: "coveredExecutor.killProbe", fields: ["state": "firing"])
            _ = webView.perform(selector)
        }
    }
}

private extension WKWebView {
    @objc func b102_evaluateJavaScript(_ javaScriptString: String, completionHandler: ((Any?, Error?) -> Void)?) {
        CoveredWebProcessKillProbe.observe(script: javaScriptString, webView: self)
        b102_evaluateJavaScript(javaScriptString, completionHandler: completionHandler)
    }
}
