# Project Profile

## Initialization

**Initialized — 2026-08-25; product baseline refreshed 2026-08-26**

Bootstrap inspection completed against the real repository state. Product implementation facts below are backed by the accepted and merged `DEV-app-foundation-0.1.0-b1` candidate where stated; unsupported compatibility details remain `Unknown / Unverified`.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Project purpose**: Develop an iOS native ChatGPT client.
- **Product type**: Native iOS third-party ChatGPT client application.
- **Primary users/runtime**: iOS users. The intended user-device environment does not exceed iOS 17.0; compatibility with lower iOS versions is preferred where practical.

## Technology stack

- **Primary language(s)**: Swift 5.
- **Primary UI framework**: UIKit.
- **System frameworks used by the foundation**: UIKit, Foundation, OSLog, CryptoKit.
- **Package/dependency manager(s)**: None; the foundation has no third-party dependencies.
- **Important manifests/configs**: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared Xcode scheme under `ChatGPTClient.xcodeproj/xcshareddata/xcschemes/`, `.github/workflows/ios-foundation.yml`.

## Repository structure

- **Main source root**: `ChatGPTClient/`.
- **Application entry point**: `ChatGPTClient/AppDelegate.swift`.
- **Application shell**: `RootViewController.swift` and `SettingsViewController.swift`.
- **Build/runtime metadata owner**: `ChatGPTClient/Support/AppBuildInfo.swift` plus build settings/Info.plist expansion.
- **Diagnostics owner**: `ChatGPTClient/Diagnostics/Diagnostics.swift` (`DiagnosticsLogger`, bounded store, spans, sanitizer, exporter).
- **Test roots**: None yet.

## Build and validation

- **Primary packaging command**: `bash scripts/build_ipa.sh` on macOS with Xcode.
- **Underlying build**: `xcodebuild -project ChatGPTClient.xcodeproj -scheme ChatGPTClient -configuration Release -sdk iphoneos ... build` with signing disabled for the TrollStore candidate packaging path.
- **Lint/static checks**: No separate lint tool configured.
- **CI workflow**: `.github/workflows/ios-foundation.yml` on GitHub-hosted `macos-15`; observed successful run used Xcode 16.4 / iPhoneOS 18.5 SDK and compiled for `arm64-apple-ios14.0`.
- **Artifact/package output**: `build/artifacts/ChatGPTClient-<version>-b<build>-dev-app-foundation.ipa` plus `.sha256`.
- **Current validation level**: Code written; CI passed; IPA artifact produced and inspected; TrollStore install/launch, Settings/sample diagnostic event, diagnostic JSON export and cross-restart persistence were real-device tested successfully on iPhone / iOS 17.0 for `DEV-app-foundation-0.1.0-b1`.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in `ChatGPTClient.xcodeproj/project.pbxproj`.
- **Build number source**: `CURRENT_PROJECT_VERSION` in `ChatGPTClient.xcodeproj/project.pbxproj`.
- **Current version/build**: `0.1.0 (1)`.
- **Parallel test-candidate scheme**: `DEV-<work-slug>-<marketing-version>-b<build>`; build/candidate identities must remain unique across Active tasks.
- **Accepted foundation candidate**: `DEV-app-foundation-0.1.0-b1`.
- **Artifact naming rule**: `ChatGPTClient-<marketing-version>-b<build>-<work-slug>.ipa`.
- **Current bundle identifier**: `com.whitesharkssw.chatgptclient`; this is the accepted foundation identity but is not Frozen as a permanent signing/product contract yet.

## Runtime / deployment

- **Supported runtime/OS/platform**: Native iOS application.
- **Current minimum deployment target**: iOS 14.0, verified in Xcode build settings and generated IPA `MinimumOSVersion` for the foundation candidate.
- **Compatibility ceiling**: The intended user environment does not exceed iOS 17.0.
- **Deployment / installation**: IPA through TrollStore. `DEV-app-foundation-0.1.0-b1` was installed and launched successfully through TrollStore on an iPhone running iOS 17.0.
- **Device family build setting**: iPhone + iPad (`UIDeviceFamily` 1,2) in the foundation artifact. Real-device validation currently covers an iPhone only; iPad and iOS versions below 17.0 remain unverified.
- **Architecture verified in artifact**: arm64 Mach-O.
- **Environment/configuration sources**: Xcode project build settings and `Info.plist`; no external runtime configuration exists yet.

## Current source/candidate baselines

- Foundation merged to `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`.
- Runtime-tested product/workflow source: `89b29434e4d81486d395b8ddb093a031f6f919a7`; exported diagnostic identity reports `89b29434e4d8`.
- GitHub Actions run `32876352123` succeeded and produced artifact ID `9574034381` for `DEV-app-foundation-0.1.0-b1`.
- Later PR material/completion heads passed CI runs `32877096378` and `32878347358`; completion-only commits did not change the runtime-tested product/workflow files.
- Accepted runtime evidence: user-confirmed TrollStore install/launch and no observed problems; exported diagnostics show two launch sequences, successful Settings/sample/export operations and pre-restart events still present after relaunch.
- No Active `DEV-app-foundation` checkpoint remains after merge; the next serial development phase is `DEV-auth-bootstrap`.

## Historical reference material

The user supplied `ChatGPT_iOS_Native_Client_History_Pack_2026-08-25.zip` as experience/reference from a previous project. It is not the current source baseline and does not make historical endpoint names, WebView implementations, diagnoses, framework choices, or MVP suggestions current facts. Durable extracted lessons and evidence boundaries are summarized in `docs/project/HISTORICAL_REFERENCE.md`.

## Evidence notes

- User requirement: current project theme is development of an iOS native ChatGPT client distributed as a TrollStore IPA; intended iOS systems do not exceed iOS 17.0 and lower compatibility is preferred.
- `DEV-app-foundation` source establishes Swift/UIKit, no third-party dependency, iOS 14.0 deployment target, build metadata, bounded diagnostics, settings/export entry, Xcode project and packaging script.
- CI produced and inspected `DEV-app-foundation-0.1.0-b1`; the user then successfully tested that exact candidate through TrollStore on iPhone / iOS 17.0.
- Exported diagnostic JSON identifies version `0.1.0 (1)`, candidate `DEV-app-foundation-0.1.0-b1`, Release configuration, deployment target 14.0, iPhone / iOS 17.0 and source `89b29434e4d8`; it demonstrates cross-relaunch log persistence and contains no observed password/token/Cookie/Authorization/OAuth secret fields.
- Runtime success on iOS 17.0 does not by itself prove runtime compatibility on every OS version down to the compiled iOS 14.0 minimum.

## Auto-refresh rule

Update this file proactively when project purpose, language/framework, build/test commands, version scheme, deployment/runtime, repository structure, or major state ownership changes.
