# Project Profile

## Initialization

**Initialized — 2026-08-25; product/runtime profile refreshed 2026-08-27**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Project purpose**: Develop an iOS native third-party ChatGPT client.
- **Primary users/runtime**: iOS; intended user-device environment does not exceed iOS17.0; lower compatibility preferred where practical.

## Technology stack

- **Primary language**: Swift 5.
- **UI framework**: UIKit.
- **System frameworks**: UIKit, Foundation, WebKit, OSLog, CryptoKit.
- **Third-party dependencies**: None.
- **Important config**: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared Xcode scheme, `.github/workflows/ios-foundation.yml`.

## Repository structure and state owners

- **Main source root**: `ChatGPTClient/`.
- **Application entry**: `AppDelegate.swift`; b14 sequences accepted WebKit warm-up before installing the product root.
- **Application shell**: `RootViewController.swift`, `SettingsViewController.swift`; b14 uses synchronously constructed UISplitViewController columns with native compact list/detail navigation.
- **Build/runtime metadata owner**: `Support/AppBuildInfo.swift` + Xcode/Info.plist settings.
- **Diagnostics owner**: `Diagnostics/Diagnostics.swift`.
- **Embedded login owner**: `Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore`.
- **Auth/account-context owner**: `Authentication/AuthSessionStore.swift`; copied cookies and `/api/auth/session` bearer are transient only.
- **Protocol-read diagnostic owner**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation owner**: `Conversation/ConversationFeature.swift` / `ConversationRepository`; owns production list summaries, selected conversation identity, loaded detail/current visible branch, manual recovery and selected-detail operation freshness.
- **Test roots**: None yet.

## Build and validation

- **Packaging**: `bash scripts/build_ipa.sh`.
- **Underlying build**: Release `xcodebuild` for iphoneos with signing disabled for TrollStore packaging.
- **CI**: GitHub Actions on `macos-15`; current pipeline uses Xcode 16.4 / iPhoneOS 18.5 and compile target `arm64-apple-ios14.0`.
- **Artifact output**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` + SHA-256 sidecar.
- **Current validation level**: Foundation, embedded Google/WebKit auth architecture, Plus/personal account context, b7 diagnostic list/detail, b9 production native read, b10 recovery core, b12 public WebKit cold-start warm-up + centered sync feedback, b13 immediate list initiation/stale-generation rejection, and b14 compact startup/native list-detail navigation have real-device evidence on iPhone/iOS17. The selected-detail replacement-overlap HTTP429 defect remains unresolved and is still inside `DEV-conversation-recovery`.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in Xcode project settings.
- **Build source**: `CURRENT_PROJECT_VERSION`.
- **Accepted foundation**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted auth/account baseline**: `0.1.0 (6)` / `DEV-auth-bootstrap-0.1.0-b6`.
- **Accepted diagnostic protocol-read baseline**: `0.1.0 (7)` / `DEV-protocol-read-0.1.0-b7`.
- **Accepted production native-read baseline**: `0.1.0 (9)` / `DEV-native-read-path-0.1.0-b9`; source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.
- **Latest tested recovery candidate**: `0.1.0 (14)` / `DEV-conversation-recovery-0.1.0-b14`; product/config head `82d96bf085dbee3877bcb16e27bbf69f4dc0990f`; run `33000566633`; artifact `9618410313`; IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`; compact startup/navigation Runtime accepted.
- **Next recovery candidate**: not allocated; must be unique after a fresh conflict/build-index check.
- **Candidate scheme**: `DEV-<work-slug>-<marketing-version>-b<build>`.
- **Bundle ID**: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.

## Runtime / deployment

- **Platform**: Native iOS application.
- **Deployment target**: iOS14.0 build target.
- **Intended environment ceiling**: iOS17.0.
- **Distribution**: TrollStore IPA.
- **Device families**: iPhone + iPad build setting; real-device evidence currently covers iPhone only.
- **Artifact architecture**: arm64.

## Current evidence highlights

- b7 accepted the tested personal-account diagnostic list + detail path.
- b9 accepted production shell/list/two distinct detail reads/current visible branch on iPhone/iOS17.
- b10 accepted loaded-state manual latest-sync/full reload core behavior.
- b12 proved public default-WebKit-data-store warm-up can hydrate persisted auth for one tested cold start and centered sync feedback is accepted.
- b13 proved first list load begins immediately after warm-up and selected-detail generation rejects older stale completion; it also exposed HTTP429 when a manual replacement request overlaps the older in-flight detail request.
- b14 is real-device accepted for compact startup/list-detail navigation: list is the useful initial root, duplicate sidebar controls are gone, and native navigation is usable.
- The overlap defect is not fixed by b14 and remains the next correction inside the same `DEV-conversation-recovery` Work.

## Evidence notes

- iOS17 runtime success does not prove iOS14–16 or iPad runtime compatibility.
- Read/recovery evidence is scoped to the tested Plus/personal account; it does not prove send/streaming/attachments or non-personal workspaces.
- Current selected-detail generation is scoped to the single-selected conversation owner and is not future multi-conversation residency architecture.
- Account/list/detail durations are end-to-end signals; bottleneck decomposition remains Unverified.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline/candidate changes.
