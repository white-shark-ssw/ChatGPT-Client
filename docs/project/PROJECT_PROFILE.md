# Project Profile

## Initialization

**Initialized — 2026-08-25; product baseline refreshed 2026-08-26**

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
- **Protocol-read diagnostic owner**: `Protocol/ProtocolReadProbe.swift`; accepted for diagnostic list/detail evidence only and persists no production conversation state.
- **Production conversation owner**: `Conversation/ConversationFeature.swift` / `ConversationRepository`; owns production list summaries, selected conversation identity, loaded detail and current visible user/assistant branch. UI titles/text are consumers only.
- **Test roots**: None yet.

## Build and validation

- **Packaging**: `bash scripts/build_ipa.sh`.
- **Underlying build**: Release `xcodebuild` for iphoneos with signing disabled for TrollStore candidate packaging.
- **CI**: GitHub Actions on `macos-15`; b7-b9 used Xcode 16.4 / iPhoneOS 18.5 and compile target `arm64-apple-ios14.0`.
- **Artifact output**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` + SHA-256 sidecar.
- **Current validation level**: Foundation, embedded Google/WebKit auth architecture, Plus/personal account context, b7 diagnostic list/detail protocol, and b9 production native shell/list/two-detail/current-branch message rendering have real-device evidence on iPhone / iOS 17.0. b9 terminal reload failure path, install/update auth persistence, send/streaming and attachments remain Unverified.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in Xcode project settings.
- **Build source**: `CURRENT_PROJECT_VERSION`.
- **Accepted foundation**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted auth/account baseline**: `0.1.0 (6)` / `DEV-auth-bootstrap-0.1.0-b6`; source `19c0cd22923d8c6f4c96e676258b31814d02a942`.
- **Accepted diagnostic protocol-read baseline**: `0.1.0 (7)` / `DEV-protocol-read-0.1.0-b7`; source `44a137b973e29e2a313e9114fdacb7727dccefb9`; run `32938912018`; artifact `9595827498`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`; PR #7 merged at `6208102eb3df79a1916b356cc95ff7916ff8f593`.
- **Accepted production native-read baseline**: `0.1.0 (9)` / `DEV-native-read-path-0.1.0-b9`; source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`. Stable for tested scope, not Frozen.
- **Candidate scheme**: `DEV-<work-slug>-<marketing-version>-b<build>`.
- **Bundle ID**: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.

## Runtime / deployment

- **Platform**: Native iOS application.
- **Deployment target**: iOS 14.0 build target.
- **Intended environment ceiling**: iOS 17.0.
- **Distribution**: TrollStore IPA.
- **Device families**: iPhone + iPad build setting; real-device evidence currently covers iPhone only.
- **Artifact architecture**: arm64.

## Current source/candidate baselines

- Foundation PR #5 merged at `9e7a06801715b0002d3e9a720d57041e830b776e`.
- Auth PR #6 merged at `78f42a06e6254088e3b495cb4529e549a1d4717f`.
- Protocol-read PR #7 merged at `6208102eb3df79a1916b356cc95ff7916ff8f593`.
- Native-read PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.
- b6 source `19c0cd22923d8c6f4c96e676258b31814d02a942` accepted Plus/personal account context.
- b7 source `44a137b973e29e2a313e9114fdacb7727dccefb9` accepted the tested personal-account diagnostic list + first-detail path: list HTTP 200 28/29; detail HTTP 200 13,152,411 bytes, mapping 2068 / messages 2067, identity matched; `status=ok` 13,573.66 ms.
- b8 source `e312acc3dd17cdcdb01746bb76f70556510a0304` established the first production native shell/repository candidate but one detail returned HTTP 500 after 30,935.12 ms before parse/render. Initial b8 launch had 0/0 WebKit cookies.
- b9 source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7` kept auth/endpoint/header behavior unchanged, added safe selected-conversation diagnostics and explicit terminal manual reload, and passed two distinct production detail reads on device. Position 1: 1,529,866 bytes / mapping 337 / visible 154 / 5,668.41 ms. Position 13: 7,503,328 bytes / mapping 2023 / visible 843 / 20,742.89 ms. User confirmed both fully readable.

## Historical reference material

Previous-project material is experience/reference only and does not make historical endpoint names, request shapes or workarounds current facts.

## Evidence notes

- iOS 17.0 runtime success does not prove iOS 14–16 or iPad runtime compatibility.
- b9 native-read acceptance is scoped to the tested Plus/personal account and two selected conversations. It does not prove all conversation/content variants, send/streaming/attachments or non-personal workspaces.
- b9 again began with 0/0 WebKit cookies until explicit login verification; install/update auth persistence remains Unknown / Unverified.
- The terminal `重新加载` failure path was not exercised because both b9 details succeeded.
- b9's 20.74 s 7.50 MB / 2023-node detail is an end-to-end performance signal; current diagnostics do not prove which phase is the bottleneck.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline changes.
