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
- **Current validation level**: Foundation, Google/WebKit auth, account context, and b7 personal-account conversation list + one-detail diagnostic read are real-device accepted on iPhone / iOS 17.0. b8 production native shell/list reached real-device testing but failed detail acceptance on one HTTP 500 response. b9 is Code + CI + Artifact and awaits real-device discrimination testing. Send/streaming and attachments remain Unverified.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in Xcode project settings.
- **Build source**: `CURRENT_PROJECT_VERSION`.
- **Accepted foundation**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted auth/account baseline**: `0.1.0 (6)` / `DEV-auth-bootstrap-0.1.0-b6`; source `19c0cd22923d8c6f4c96e676258b31814d02a942`.
- **Accepted protocol-read baseline**: `0.1.0 (7)` / `DEV-protocol-read-0.1.0-b7`; exact product/workflow source `44a137b973e29e2a313e9114fdacb7727dccefb9`; run `32938912018`; artifact ID `9595827498`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`; PR #7 merged at `6208102eb3df79a1916b356cc95ff7916ff8f593`.
- **Current active candidate**: `0.1.0 (9)` / `DEV-native-read-path-0.1.0-b9`; product/config source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact ID `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; draft PR #9. Runtime acceptance pending.
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
- b6 source `19c0cd22923d8c6f4c96e676258b31814d02a942` accepted plus/personal account context.
- b7 source `44a137b973e29e2a313e9114fdacb7727dccefb9` accepted the personal-account list + first-detail diagnostic read path on iPhone / iOS 17.0. List HTTP 200: 28 items / total 29. First detail HTTP 200: 13,152,411 bytes, mapping 2068 / messages 2067, current node mapped, identity matched; end-to-end probe `status=ok` in 13,573.66 ms.
- b8 source `e312acc3dd17cdcdb01746bb76f70556510a0304` established the first production native shell/repository candidate. On device the shell launched and, after explicit login verification, production list GET repeatedly returned HTTP 200 / 28 of 29; one selected detail GET returned HTTP 500 after 30,935.12 ms before parse/render. Initial b8 launch observed 0/0 WebKit cookies, so install/update auth persistence remains Unverified.
- b9 source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7` adds privacy-safe selected-conversation hash/list-position diagnostics plus explicit terminal manual detail reload only; it changes no auth/endpoint/header/retry behavior. CI/artifact passed; runtime pending.

## Historical reference material

Previous-project material is experience/reference only and does not make historical endpoint names, request shapes or workarounds current facts.

## Evidence notes

- iOS 17.0 runtime success does not prove iOS 14–16 or iPad runtime compatibility.
- Accepted b7 read evidence is scoped to the tested Plus/personal account and the list + one-detail path. It does not prove send/streaming/attachments or non-personal workspace behavior.
- b8's HTTP 500 is response-stage evidence only; it does not prove a local JSON parser/render problem and does not yet prove whether failure is conversation-specific or systematic.
- The 13.57 s b7 probe duration is end-to-end and does not by itself identify network, parsing or rendering bottlenecks.
- The observed 13.15 MB / 2068-node detail is a real design input for production native read handling.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline changes.
