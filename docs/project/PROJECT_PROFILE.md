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
- **Auth/account-context owner**: `Authentication/AuthSessionStore.swift`; copied cookies and `/api/auth/session` bearer are transient only.
- **Protocol-read diagnostic owner**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation data owner**: `Conversation/ConversationFeature.swift` / the single `ConversationRepository`; b17 generalizes it to account-scoped per-conversation resident/operation entries while foreground selection remains presentation-only.
- **Conversation presentation owner**: `ConversationDetailViewController`; b18 adds lightweight per-conversation historical scroll anchor metadata here. Exact b18 iPhone/iOS17 Runtime accepts the tested historical anchor matrix. This metadata is not a second conversation-data or response authority.
- **Test roots**: None yet.

## Build and validation

- **Packaging**: `bash scripts/build_ipa.sh`.
- **Underlying build**: Release `xcodebuild` for iphoneos with signing disabled for TrollStore packaging.
- **CI**: GitHub Actions on macOS15; exact b18 run uses Xcode 16.4 / iPhoneOS18.5 and compile target `arm64-apple-ios14.0`.
- **Intended artifact scheme**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` + SHA-256 sidecar.
- **Packaging status**: b16 historically exposed recovery hard-codes and is rejected. b17 corrected multi-conversation package identity. b18 independently verifies exact filename/version/build/candidate/source/SHA/arm64/iOS14 identity.
- **Current accepted validation level**: Foundation, embedded Google/WebKit auth architecture, Plus/personal account context, diagnostic list/detail, production native read, manual sync/full reload, public WebKit cold-start warm-up, centered sync feedback, compact startup/native list-detail navigation, stale-generation rejection and selected-detail cancellation/replacement have real-device evidence on iPhone/iOS17 for recorded scopes.
- **Current Active Work validation**: b17 core multi-conversation switching/coalescing/hidden-Sync Runtime accepted and reproduced the historical-scroll defect. Exact b18 has Code + static/source + CI + Artifact + **real-device Runtime acceptance for the tested historical scroll, independent A/B anchors, first-time target isolation, Sync/Reload anchor preservation and resident/coalescing regression matrix**. Work remains Active and not Stable/Frozen because remaining failure/account/LRU/replacement gates are separate.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in Xcode project settings.
- **Build source**: `CURRENT_PROJECT_VERSION`.
- **Candidate scheme**: `DEV-<work-slug>-<marketing-version>-b<build>`.
- **Bundle ID**: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.
- **Accepted foundation**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted auth/account baseline**: `0.1.0 (6)` / `DEV-auth-bootstrap-0.1.0-b6`.
- **Accepted diagnostic protocol-read baseline**: `0.1.0 (7)` / `DEV-protocol-read-0.1.0-b7`.
- **Accepted production native-read baseline**: `0.1.0 (9)` / `DEV-native-read-path-0.1.0-b9`.
- **Accepted recovery baseline**: `0.1.0 (15)` / `DEV-conversation-recovery-0.1.0-b15`; PR #10 merged.
- **Historical rejected multi-conversation candidate**: `0.1.0 (16)` / `DEV-multi-conversation-state-0.1.0-b16`; Artifact identity rejected before runtime; never reuse.
- **Core runtime predecessor**: `0.1.0 (17)` / b17; exact source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; Run `33045536770`; Artifact `9635486304`; core Runtime accepted with reproduced historical-scroll defect.
- **Current exact multi-conversation Candidate**: `0.1.0 (18)` / `DEV-multi-conversation-state-0.1.0-b18`; product/config source `f30c13b4ac2c40dcda829585682825ca906dceae`; tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`; Run `33054012226`; Artifact `9638821912`; IPA `ChatGPTClient-0.1.0-b18-dev-multi-conversation-state.ipa`; IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`; **historical-scroll Runtime accepted for tested iPhone/iOS17 matrix; Work not Stable**.

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
- b14 accepted compact startup/list-detail navigation.
- b15 accepted selected-detail cancellation/replacement and is merged Stable recovery baseline.
- b17 accepted core multi-conversation resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid overlap; user reproduced A≈10% -> B scroll -> A position drift.
- b18 exact device export identifies iPhone/iOS17, candidate b18, build 18, source `f30c13b4ac2c`. User reported no issue in the requested matrix; diagnostics show 21 anchor saves, 19 restores, 17 resident hits/first-visible events, all 17 recorded HTTP statuses 200, no error/HTTP429/anchor discard.
- b18 therefore closes the reproduced historical-scroll defect for the tested matrix, but does not close natural failure residency, supported account-switch isolation, normal resident/LRU capacity, non-personal workspace isolation or future Send/Stream follow-tail.
- Current `main` is `2c33dacbefa613292eb89cbf606b0172a241e81e`; its post-b18 advancement is docs-only and must be synchronized before final merge.

## Evidence notes

- iOS17 runtime success does not prove iOS14–16 or iPad runtime compatibility.
- Read/recovery evidence is scoped to tested Plus/personal account; it does not prove Send/Stream/attachments or non-personal workspaces.
- Active multi-conversation source keys account residency with `userID + accountID`; whether non-personal workspaces require additional identity remains Unknown / Unverified.
- Approximate resident visible-text bytes are correlation metrics only, not proof of actual process memory or a safe LRU capacity.
- b18 historical scroll presentation is in-memory only; future active-response follow-tail eligibility remains unimplemented until the real Send/Stream response owner exists.
- Missing-anchor-message discard was not naturally exercised in exact b18 runtime; source/CI contract exists but no device proof is claimed.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline/candidate changes.
