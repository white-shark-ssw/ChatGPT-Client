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
- **Production conversation owner**: Not established yet. `DEV-native-read-path` must establish repository, selected-conversation identity and message-tree ownership.
- **Test roots**: None yet.

## Build and validation

- **Packaging**: `bash scripts/build_ipa.sh`.
- **Underlying build**: Release `xcodebuild` for iphoneos with signing disabled for TrollStore candidate packaging.
- **CI**: GitHub Actions on `macos-15`; accepted b7 run used Xcode 16.4 / iPhoneOS 18.5 and compiled `arm64-apple-ios14.0`.
- **Artifact output**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` + SHA-256 sidecar.
- **Current validation level**: Foundation, Google/WebKit auth, account context, and current personal-account conversation list + one-detail read path are all **Code + CI + Artifact + real-device tested** on iPhone / iOS 17.0 through b7. Native production conversation UI/state, send/streaming and attachments remain Unverified.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in Xcode project settings.
- **Build source**: `CURRENT_PROJECT_VERSION`.
- **Accepted foundation**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted auth/account baseline**: `0.1.0 (6)` / `DEV-auth-bootstrap-0.1.0-b6`; source `19c0cd22923d8c6f4c96e676258b31814d02a942`.
- **Accepted protocol-read baseline**: `0.1.0 (7)` / `DEV-protocol-read-0.1.0-b7`; exact product/workflow source `44a137b973e29e2a313e9114fdacb7727dccefb9`; run `32938912018`; artifact ID `9595827498`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`. PR #7 integration is completing.
- **Next candidate**: Not allocated. Future `DEV-native-read-path` must re-check all Active checkpoints and `BUILD_TEST_INDEX.md` immediately before its first artifact.
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
- b6 source `19c0cd22923d8c6f4c96e676258b31814d02a942` accepted plus/personal account context.
- b7 source `44a137b973e29e2a313e9114fdacb7727dccefb9` accepted the current personal-account list + first-detail read path on iPhone / iOS 17.0. Runtime export metadata matched source `44a137b973e2` exactly.
- b7 list HTTP 200: 28 items / total 29. First detail HTTP 200: 13,152,411 bytes, mapping 2068 / messages 2067, current node mapped, identity matched; end-to-end probe `status=ok` in 13,573.66 ms.
- b7 again observed first-attempt session 403 followed by success only after explicit user `重新开始`; no automatic retry exists.

## Historical reference material

Previous-project material is experience/reference only and does not make historical endpoint names, request shapes or workarounds current facts.

## Evidence notes

- iOS 17.0 runtime success does not prove iOS 14–16 or iPad runtime compatibility.
- Accepted b7 read evidence is scoped to the tested Plus/personal account and the list + one-detail path. It does not prove send/streaming/attachments or non-personal workspace behavior.
- The 13.57 s b7 probe duration is end-to-end and does not by itself identify network, parsing or rendering bottlenecks.
- The observed 13.15 MB / 2068-node detail is a real design input for `DEV-native-read-path`.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline changes.
