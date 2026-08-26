# Project Profile

## Initialization

**Initialized — 2026-08-25; product/runtime profile refreshed 2026-08-27**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Project purpose**: Develop an iOS native third-party ChatGPT client.
- **Primary users/runtime**: iOS; intended user-device environment does not exceed iOS 17.0; lower compatibility preferred where practical.

## Technology stack

- **Primary language**: Swift 5.
- **UI framework**: UIKit.
- **System frameworks**: UIKit, Foundation, WebKit, OSLog, CryptoKit.
- **Third-party dependencies**: None.
- **Important config**: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared Xcode scheme, `.github/workflows/ios-foundation.yml`.

## Repository structure and state owners

- **Main source root**: `ChatGPTClient/`.
- **Application entry**: `AppDelegate.swift`.
- **Application shell**: `RootViewController.swift`, `SettingsViewController.swift`.
- **Build/runtime metadata owner**: `Support/AppBuildInfo.swift` + Xcode/Info.plist settings.
- **Diagnostics owner**: `Diagnostics/Diagnostics.swift`.
- **Embedded login owner**: `Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore`.
- **Auth/account-context owner**: `Authentication/AuthSessionStore.swift`; copied cookies and `/api/auth/session` bearer are transient only.
- **Protocol-read diagnostic owner**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation owner**: `Conversation/ConversationFeature.swift` / `ConversationRepository`; owns production list summaries, selected conversation identity, loaded detail and current visible branch. b13 additionally owns a minimum selected-detail operation generation so a newer explicit recovery can supersede an older ordinary load.
- **Test roots**: None yet.

## Build and validation

- **Packaging**: `bash scripts/build_ipa.sh`.
- **Underlying build**: Release `xcodebuild` for iphoneos with signing disabled for TrollStore packaging.
- **CI**: GitHub Actions on `macos-15`; current accepted pipeline uses Xcode 16.4 / iPhoneOS 18.5 and compile target `arm64-apple-ios14.0`.
- **Artifact output**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` + SHA-256 sidecar.
- **Current validation level**: Foundation, embedded Google/WebKit auth architecture, Plus/personal account context, b7 diagnostic list/detail, b9 production native read, b10 recovery core, and b12 public WebKit cold-start warm-up + centered sync feedback have real-device evidence on iPhone/iOS17. b13 startup/list sequencing and recovery-during-load are Code+CI+Artifact only and await real-device confirmation.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in Xcode project settings.
- **Build source**: `CURRENT_PROJECT_VERSION`.
- **Accepted foundation**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted auth/account baseline**: `0.1.0 (6)` / `DEV-auth-bootstrap-0.1.0-b6`.
- **Accepted diagnostic protocol-read baseline**: `0.1.0 (7)` / `DEV-protocol-read-0.1.0-b7`.
- **Accepted production native-read baseline**: `0.1.0 (9)` / `DEV-native-read-path-0.1.0-b9`; source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.
- **Active candidate**: `0.1.0 (13)` / `DEV-conversation-recovery-0.1.0-b13`; product/config head `fcc74ac4015449dba6c77f3136eede82cec3ec54`; run `32997544435`; artifact `9617184873`; IPA SHA `2af6334278bcb88683cc123d47617e6956c0efb83aceb9b294961827f3e80040`.
- **Candidate scheme**: `DEV-<work-slug>-<marketing-version>-b<build>`.
- **Bundle ID**: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.

## Runtime / deployment

- **Platform**: Native iOS application.
- **Deployment target**: iOS 14.0 build target.
- **Intended environment ceiling**: iOS 17.0.
- **Distribution**: TrollStore IPA.
- **Device families**: iPhone + iPad build setting; real-device evidence currently covers iPhone only.
- **Artifact architecture**: arm64.

## Current evidence highlights

- b7 accepted the tested personal-account diagnostic list + detail path.
- b9 accepted the production shell/list/two distinct detail reads and current visible branch on iPhone/iOS17.
- b10 accepted loaded-state manual latest-sync/full reload core behavior.
- b12 cold-start export proved public default-WebKit-data-store warm-up can hydrate persisted auth for the tested run: cookie visibility moved from 0/0 to 41/22 in 194.97 ms; the later single normal account probe and conversation list succeeded without visible Login.
- The same b12 run exposed that first conversation-list loading was delayed by compact-iPhone lazy sidebar view loading, not authentication. b13 explicitly starts the sidebar/list load after warm-up.
- b12 centered sync feedback is real-device accepted; b13 keeps it unchanged.

## Evidence notes

- iOS17 runtime success does not prove iOS14–16 or iPad runtime compatibility.
- Read/recovery evidence is scoped to the tested Plus/personal account; it does not prove send/streaming/attachments or non-personal workspaces.
- b13 stale-operation generation is scoped to the current single-selected conversation owner and is not the future multi-conversation residency architecture.
- Large-conversation performance decomposition remains Unverified.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline/candidate changes.