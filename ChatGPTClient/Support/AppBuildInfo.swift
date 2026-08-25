import Foundation
import UIKit

struct AppBuildInfo: Codable {
    let appVersion: String
    let buildNumber: String
    let candidate: String
    let sourceCommit: String
    let buildConfiguration: String
    let deploymentTarget: String
    let bundleIdentifier: String
    let deviceClass: String
    let systemName: String
    let systemVersion: String
    let localeIdentifier: String

    static var current: AppBuildInfo {
        let info = Bundle.main.infoDictionary ?? [:]
        return AppBuildInfo(
            appVersion: info["CFBundleShortVersionString"] as? String ?? "unknown",
            buildNumber: info["CFBundleVersion"] as? String ?? "unknown",
            candidate: info["DiagnosticsCandidate"] as? String ?? "unknown",
            sourceCommit: info["DiagnosticsSourceCommit"] as? String ?? "unknown",
            buildConfiguration: info["DiagnosticsBuildConfiguration"] as? String ?? "unknown",
            deploymentTarget: info["DiagnosticsDeploymentTarget"] as? String ?? "unknown",
            bundleIdentifier: Bundle.main.bundleIdentifier ?? "unknown",
            deviceClass: UIDevice.current.model,
            systemName: UIDevice.current.systemName,
            systemVersion: UIDevice.current.systemVersion,
            localeIdentifier: Locale.current.identifier
        )
    }

    var displayText: String {
        [
            "版本：\(appVersion) (\(buildNumber))",
            "候选：\(candidate)",
            "Commit：\(sourceCommit)",
            "配置：\(buildConfiguration)",
            "Deployment Target：iOS \(deploymentTarget)",
            "Bundle ID：\(bundleIdentifier)",
            "设备：\(deviceClass) / \(systemName) \(systemVersion)"
        ].joined(separator: "\n")
    }
}
