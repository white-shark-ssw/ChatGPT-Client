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
- **Application entry**: `AppDelegate.swift`; accepted recovery baseline sequences public WebKit warm-up before installing the product root.
- **Application shell**: `RootViewController.swift`, `SettingsViewController.swift`; compact iPhone startup uses native list/detail navigation with the conversation list as useful initial root.
- **Build/runtime metadata owner**: `Support/AppBuildInfo.swift` + Xcode/Info.plist settings.
- **Diagnostics owner**: `Diagnostics/Diagnostics.swift`.
- **Embedded login owner**: `Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore`.
- **Auth/account-context owner**: `Authentication/AuthSessionStore.swift`; copied cookies and `/api/auth/session` bearer are transient only. `AuthTransientSession.dataTask` may expose its already-created task handle; auth semantics are unchanged.
- **Protocol-read diagnostic owner**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation owner — accepted b15 baseline**: `Conversation/ConversationFeature.swift` / `ConversationRepository`; owns production list summaries, selected conversation identity/detail/current visible branch, manual recovery, selected-detail operation freshness and selected-detail request lifecycle.
- **Production conversation owner — Active `DEV-multi-conversation-state` direction**: the same single `ConversationRepository` is generalized to account-scoped per-conversation resident/operation entries while foreground selection remains presentation-only. Exact b17 source has static/local + CI + Artifact identity evidence; real-device runtime acceptance is still pending.
- **Test roots**: None yet.

## Build and validation

- **Packaging**: `bash scripts/build_ipa.sh`.
- **Underlying build**: Release `xcodebuild` for iphoneos with signing disabled for TrollStore packaging.
- **CI**: GitHub Actions on `macos-15`; current b17 pipeline uses Xcode 16.4 / iPhoneOS 18.5 and compile target `arm64-apple-ios14.0`.
- **Intended artifact scheme**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` + SHA-256 sidecar.
- **Packaging status**: b16 historically exposed recovery hard-codes in `scripts/build_ipa.sh`. b17 corrected those evidenced values; exact b17 Artifact independently satisfies the intended multi-conversation candidate/slug/version/source identity.
- **Current accepted validation level**: Foundation, embedded Google/WebKit auth architecture, Plus/personal account context, diagnostic list/detail, production native read, manual sync/full reload, public WebKit cold-start warm-up, centered sync feedback, compact startup/native list-detail navigation, stale-generation rejection and selected-detail cancellation/replacement all have real-device evidence on iPhone/iOS17 for their recorded scope.
- **Current Active Work validation**: b17 multi-conversation exact source has Code + static/local parse + CI + Artifact identity evidence. It has not yet been Runtime/manual/real-device tested.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in Xcode project settings.
- **Build source**: `CURRENT_PROJECT_VERSION`.
- **Accepted foundation**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted auth/account baseline**: `0.1.0 (6)` / `DEV-auth-bootstrap-0.1.0-b6`.
- **Accepted diagnostic protocol-read baseline**: `0.1.0 (7)` / `DEV-protocol-read-0.1.0-b7`.
- **Accepted production native-read baseline**: `0.1.0 (9)` / `DEV-native-read-path-0.1.0-b9`.
- **Accepted recovery baseline**: `0.1.0 (15)` / `DEV-conversation-recovery-0.1.0-b15`; product/config head `159e8ea4f7baf6cd890d1f9bbebeac41feefbf52`; tested merge `fb0c6d75362e111758b62a98f89696b7f1cb6c92`; tree `7a988bcad27d023eac77683985c5d7d92b22c176`; run `33004536664`; artifact `9619988065`; IPA SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`; PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.
- **Historical rejected multi-conversation candidate**: `0.1.0 (16)` / `DEV-multi-conversation-state-0.1.0-b16`; exact source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; CI succeeded but Artifact `9621830284` embedded the wrong recovery candidate/slug and is rejected before runtime. Build 16 must not be reused.
- **Current valid multi-conversation runtime Candidate**: `0.1.0 (17)` / `DEV-multi-conversation-state-0.1.0-b17`; exact product/config source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; tree `3451585f83c7bac69368709fe6273b90a0294d29`; Run `33045536770`; Artifact `9635486304`; IPA `ChatGPTClient-0.1.0-b17-dev-multi-conversation-state.ipa`; IPA SHA `ed551deac0335e47da56da36ec2a8a20550613ac072ac1ddf0b84790278318dc`; runtime pending.
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

- b9 accepted production shell/list/two distinct detail reads/current visible branch.
- b10 accepted loaded-state manual latest-sync/full reload core behavior.
- b12 accepted public default-WebKit-data-store warm-up for tested persisted cold start and centered sync feedback.
- b14 accepted compact startup/list-detail navigation: list is the useful initial root, duplicate sidebar controls are gone, native navigation is usable.
- b15 accepted selected-detail cancellation/replacement: obsolete generations were cancelled and replacement generations returned HTTP200 without reproducing the b13 HTTP429 overlap in two tested cases.
- Recovery PR #10 is merged; b15 is the current Stable recovery baseline for recorded Plus/personal iPhone/iOS17 scope.
- b16 remains historical/rejected before runtime.
- b17 is the first identity-valid multi-conversation runtime Candidate: exact source compiles on Xcode 16.4 CI and independent extraction verifies correct filename/version/build/candidate/source/SHA/arm64/iOS14 package identity. This does **not** prove runtime correctness.

## Evidence notes

- iOS17 runtime success does not prove iOS14–16 or iPad runtime compatibility.
- Read/recovery evidence is scoped to the tested Plus/personal account; it does not prove send/streaming/attachments or non-personal workspaces.
- Active multi-conversation source keys account residency with `userID + accountID`; whether non-personal workspaces require additional identity remains Unknown / Unverified.
- Approximate resident visible-text bytes are correlation metrics only, not proof of actual process memory or a safe LRU capacity.
- Account/list/detail durations are end-to-end signals; bottleneck decomposition remains Unverified.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline/candidate changes.
