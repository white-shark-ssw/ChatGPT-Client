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
- **Application shell**: `RootViewController.swift`, `SettingsViewController.swift`; compact iPhone startup uses native list/detail navigation with the conversation list as useful initial root. Active b21 Root also ensures first Detail view initialization occurs before assigning the selected list-summary title.
- **Build/runtime metadata owner**: `Support/AppBuildInfo.swift` + Xcode/Info.plist settings.
- **Diagnostics owner**: `Diagnostics/Diagnostics.swift`; b19 added real task-VM process-memory enrichment to resident diagnostics.
- **Embedded login owner**: `Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore`.
- **Auth/account-context owner**: `Authentication/AuthSessionStore.swift`; copied cookies and `/api/auth/session` bearer are transient only.
- **Protocol-read diagnostic owner**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation data owner**: `Conversation/ConversationFeature.swift` / the single `ConversationRepository`; b17 generalized it to account-scoped per-conversation resident/operation entries while foreground selection remains presentation-only.
- **Conversation presentation owner**: `ConversationDetailViewController`; b18 adds lightweight per-conversation historical scroll anchor metadata. Exact b18 iPhone/iOS17 Runtime accepts the tested historical anchor matrix. This metadata is not a second conversation-data or response authority.
- **Test roots**: None yet.

## Build and validation

- **Packaging**: `bash scripts/build_ipa.sh`.
- **Underlying build**: Release `xcodebuild` for iphoneos with signing disabled for TrollStore packaging.
- **CI**: GitHub Actions on macOS15; current pipeline compiles `arm64-apple-ios14.0` and b18 used Xcode 16.4 / iPhoneOS18.5.
- **Intended artifact scheme**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` + SHA-256 sidecar.
- **Packaging status**: b16 historically exposed recovery hard-codes and is rejected. b17 corrected multi-conversation identity. Exact b21 independently verifies filename/version/build/candidate/source/SHA/arm64/iOS14 identity.
- **Current accepted validation level**: Foundation, embedded Google/WebKit auth architecture, Plus/personal account context, diagnostic list/detail, production native read, manual sync/full reload, public WebKit cold-start warm-up, centered sync feedback, compact startup/native list-detail navigation, stale-generation rejection and selected-detail cancellation/replacement have real-device evidence on iPhone/iOS17 for recorded scopes.
- **Current Active Work validation**: b17 core multi-conversation switching/coalescing/hidden completion Runtime accepted; b18 historical scroll Runtime accepted; b19 real process-footprint 0→8 resident matrix accepted. b20 real-device Runtime exposed a first Detail-view-load title lifecycle overwrite. b21 has Code + Static + CI + identity-valid Artifact and awaits exact title Runtime. Work remains Active and not Stable/Frozen.

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
- **Historical rejected multi-conversation candidate**: `0.1.0 (16)` / b16; Artifact identity rejected before Runtime; never reuse.
- **Core Runtime predecessor**: `0.1.0 (17)` / b17; core Runtime accepted with reproduced historical-scroll defect.
- **Historical-scroll Runtime Candidate**: `0.1.0 (18)` / b18; exact historical-scroll matrix accepted.
- **Process-memory Runtime Candidate**: `0.1.0 (19)` / b19; observed 0→8 resident footprint matrix accepted, process-limit headroom Unverified.
- **Title lifecycle failing predecessor**: `0.1.0 (20)` / b20; Code/CI/Artifact valid but first unloaded Detail entry Runtime showed neutral-title overwrite.
- **Current exact multi-conversation Candidate**: `0.1.0 (21)` / `DEV-multi-conversation-state-0.1.0-b21`; product/config source `6b50ead167bfde305d2ad58dd16fee6edaabf597`; tree `01168ce7be8d9cf4888ad1d0718238826730c30d`; Run `33070183417`; Job `98510113281`; Artifact `9645439329`; IPA `ChatGPTClient-0.1.0-b21-dev-multi-conversation-state.ipa`; IPA SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`; **Runtime pending; Work not Stable**.

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
- b17 accepted core multi-conversation resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid overlap; historical-scroll defect reproduced.
- b18 accepted independent historical anchors, first-time target isolation, Sync/Reload anchor preservation, resident/coalescing regression matrix on iPhone/iOS17.
- b19 reached 8 residents with 53 valid process-memory samples; physical footprint remained about 16.3–78.1 MiB and generally 55–65 MiB during repeated 8-resident switching. No urgent normal-LRU pressure is evidenced; exact process-limit headroom was unavailable.
- b20 exact real-device export identifies `0.1.0 (20)`, source `754580fad96e`. User reproduced first-entry `新对话`; source proves first Detail `viewDidLoad()` overwrote the summary title. Second resident-backed entry was correct. The export's earlier auth HTTP403 is not causal because later verification/list HTTP200 succeeded before the reproduction.
- b21 fixes only lifecycle ordering in Root via `loadViewIfNeeded()` before assigning the selected summary title. CI and Artifact identity pass; real-device first-entry/rapid-switch title behavior remains pending.
- Current `main` is `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`; its planning-only changes must be synchronized before final merge.

## Evidence notes

- iOS17 Runtime success does not prove iOS14–16 or iPad Runtime compatibility.
- Read/recovery evidence is scoped to tested Plus/personal account; it does not prove Send/Stream/attachments or non-personal workspaces.
- Active multi-conversation source keys account residency with `userID + accountID`; whether non-personal workspaces require additional identity remains Unknown / Unverified.
- Approximate resident visible-text bytes are correlation metrics only; b19 real task-VM footprint is the process-memory evidence. Exact process-limit headroom is still Unverified.
- Historical scroll presentation is in-memory only; future active-response follow-tail eligibility remains unimplemented until the real Send/Stream response owner exists.
- Missing-anchor-message discard was not naturally exercised in exact b18 Runtime; source/CI contract exists but no device proof is claimed.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline/candidate changes.
