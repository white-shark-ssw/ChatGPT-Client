import UIKit

@main
final class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?

    private let diagnostics = DiagnosticsLogger.shared

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        let launchSpan = diagnostics.startSpan(category: "app", name: "launch", fields: ["launchOptionsPresent": launchOptions == nil ? "false" : "true"])
        let window = UIWindow(frame: UIScreen.main.bounds)
        window.rootViewController = RootViewController()
        window.makeKeyAndVisible()
        self.window = window
        diagnostics.info(category: "app", name: "ready", fields: ["root": "RootViewController", "candidate": AppBuildInfo.current.candidate])
        launchSpan.end()
        return true
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        diagnostics.info(category: "lifecycle", name: "willEnterForeground")
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        diagnostics.info(category: "lifecycle", name: "didBecomeActive")
    }

    func applicationWillResignActive(_ application: UIApplication) {
        diagnostics.info(category: "lifecycle", name: "willResignActive")
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        diagnostics.info(category: "lifecycle", name: "didEnterBackground")
        diagnostics.flush()
    }

    func applicationDidReceiveMemoryWarning(_ application: UIApplication) {
        diagnostics.warning(category: "lifecycle", name: "memoryWarning")
    }
}
