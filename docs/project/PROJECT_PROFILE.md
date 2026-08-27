# Project Profile

## Initialization

**Initialized — 2026-08-25; product/runtime profile refreshed 2026-08-28**

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
- **Application shell**: `RootViewController.swift`, `SettingsViewController.swift`; compact iPhone startup uses native list/detail navigation with the conversation list as useful initial root. Exact b21 Root ensures first Detail view initialization occurs before assigning the selected list-summary title; this title lifecycle ordering is real-device accepted for the requested b21 matrix.
- **Build/runtime metadata owner**: `Support/AppBuildInfo.swift` + Xcode/Info.plist settings.
- **Diagnostics owner**: `Diagnostics/Diagnostics.swift`; b19 added real task-VM process-memory enrichment to resident diagnostics and b23 adds privacy-safe list-cache diagnostics at conversation call sites.
- **Embedded login owner**: `Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore`.
- **Auth/account-context owner**: `Authentication/AuthSessionStore.swift`; copied cookies and `/api/auth/session` bearer are transient only.
- **Protocol-read diagnostic owner**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation data owner**: `Conversation/ConversationFeature.swift` / the single `ConversationRepository`; b17 generalized it to account-scoped per-conversation resident/operation entries while foreground selection remains presentation-only; merged b23 adds storage-only persistent list-cache integration without creating a second list authority.
- **Conversation-list persistent storage**: private `ConversationListCacheStore` in `ConversationFeature.swift`; stores schema-versioned summary snapshots and a privacy-safe SHA-256 last-verified scope namespace hint only. It is not auth/account or conversation authority.
- **Conversation presentation owner**: `ConversationDetailViewController`; b18 adds lightweight per-conversation historical scroll anchor metadata. Exact b18 iPhone/iOS17 Runtime accepts the tested historical anchor matrix. This metadata is not a second conversation-data or response authority.
- **Test roots**: None yet.

## Build and validation

- **Packaging**: `bash scripts/build_ipa.sh`.
- **Underlying build**: Release `xcodebuild` for iphoneos with signing disabled for TrollStore packaging.
- **CI**: GitHub Actions on macOS15; current pipeline compiles `arm64-apple-ios14.0` and b21/b23 validation used Xcode 16.4 / iPhoneOS18.5.
- **Intended artifact scheme**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` + SHA-256 sidecar.
- **Packaging status**: b16 historically exposed recovery hard-codes and is rejected. b17 corrected multi-conversation identity. Exact b21 and b23 independently verify filename/version/build/candidate/source/SHA/arm64/iOS14 identity. PR #24 merge-view CI also succeeded on the GitHub-generated merge commit.
- **Current accepted validation level**: Foundation, embedded Google/WebKit auth architecture, Plus/personal account context, diagnostic list/detail, production native read, manual sync/full reload, public WebKit cold-start warm-up, centered sync feedback, compact startup/native list-detail navigation, stale-generation rejection, selected-detail cancellation/replacement, the recorded multi-conversation read-state matrix, and the recorded persistent conversation-list cache-core matrix have real-device evidence on iPhone/iOS17 for their stated scopes.
- **Merged multi-conversation validation**: b17 core switching/coalescing/hidden completion accepted; b18 historical scroll accepted; b19 real process-footprint 0→8 resident matrix accepted; b20 first Detail-view-load title lifecycle defect reproduced and superseded; exact b21 title lifecycle plus same-target Reload replacement-under-load/hidden-rejoin coalescing are real-device accepted. PR #23 merged this Work at `2057a6241839afabeaf9b81c9daea24d3a0978f6`, making b21 the **Stable merged multi-conversation read-state baseline for the tested Plus/personal iPhone/iOS17 scope**. Remaining natural-failure/account-switch/non-personal/missing-anchor conditions remain explicit Unknown/Unverified boundaries; normal LRU is not implemented because b19 supplies no evidence that one is currently needed. Frozen remains No.
- **Merged conversation-list cache validation**: historical b22 is Runtime-partial/failing. Exact b23 real-device evidence accepts immediate provisional cached rows before slow auth, `recent_skip`, stale one-refresh, offline `-1005 -> offline_cache`, retained-list refresh-failure feedback, manual one-request refresh, and real first-page `28 + preservedOffPageCount=1 -> 29` safety. PR #24 merge-view Run `33103769517` / Job `98628067286` succeeded and PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`, making b23 the **Stable merged conversation-list cache-core baseline for the recorded Plus/personal iPhone/iOS17 scope**. Conditional account-switch/provisional-row-tap/corrupt-schema/iPad/lower-iOS/non-personal boundaries remain Unknown / Unverified. Frozen remains No.

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
- **Stable merged multi-conversation baseline**: `0.1.0 (21)` / `DEV-multi-conversation-state-0.1.0-b21`; product/config source `6b50ead167bfde305d2ad58dd16fee6edaabf597`; Run `33070183417`; Artifact `9645439329`; IPA SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`; PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`. Stable for the recorded scope; Frozen No.
- **Historical cache-core failing predecessor**: `0.1.0 (22)` / `DEV-conversation-list-cache-core-0.1.0-b22`; exact identity remains permanently reserved and superseded after partial/failing Runtime.
- **Stable merged conversation-list cache-core baseline**: `0.1.0 (23)` / `DEV-conversation-list-cache-core-0.1.0-b23`; product/config source `d2af0fc157f6e2d037636c55f963c18071a332d5`; Runtime Run `33101116431`; Job `98618762016`; Artifact `9658508764`; IPA SHA `8f6911616fff1e93885191fcaec0f31a1e3c9488b7f4522fdbdb7dc5518be516`; PR merge-view Run `33103769517`, Job `98628067286`, tested merge `26297ff0683966c2c82fd7a8a95f53f1ad51d3d6`; PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`. Stable for the recorded cache-core scope; Frozen No.

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
- b20 exact real-device export identifies `0.1.0 (20)`, source `754580fad96e`. User reproduced first-entry `新对话`; source proves first Detail `viewDidLoad()` overwrote the summary title. Second resident-backed entry was correct.
- b21 fixes lifecycle ordering in Root via `loadViewIfNeeded()` before assigning the selected summary title. Direct real-device testing accepts first-entry/re-entry/rapid-switch title behavior. Exact diagnostics also accept same-target ordinary-load -> Reload replacement with old-task cancellation and hidden/rejoin coalescing. PR #23 merged.
- b22 proved core snapshot/freshness mechanics but failed visible warm-cache ordering, offline fallback and refresh feedback; it is superseded and never reused.
- b23 exact real-device export identifies `0.1.0 (23)`, source `d2af0fc157f6`. Provisional cache publication occurred in about 4 ms before ~4.5 s account verification; rapid relaunch skipped automatic list refresh; offline auth transport failure kept 29 cached rows; online manual refresh sent exactly one request; page-1 reconciliation preserved the real 29th cached row. User reported no new issue. PR #24 merged after merge-view CI success.
- PR #24 merge-view CI Run `33103769517`, Job `98628067286` checked out merge view `26297ff0683966c2c82fd7a8a95f53f1ad51d3d6` and succeeded; merge-view Artifact `9659600955` is CI evidence only and does not replace the exact b23 Runtime Artifact.
- Current roadmap next serialized development priority is `DEV-conversation-round-count`, followed by `DEV-send-stream`.

## Evidence notes

- iOS17 Runtime success does not prove iOS14–16 or iPad Runtime compatibility.
- Read/recovery/multi-conversation/cache evidence is scoped to tested Plus/personal account; it does not prove Send/Stream/attachments or non-personal workspaces.
- Current source keys account residency with `userID + accountID`; whether non-personal workspaces require additional identity remains Unknown / Unverified.
- Approximate resident visible-text bytes are correlation metrics only; b19 real task-VM footprint is the process-memory evidence. Exact process-limit headroom is still Unverified, but current evidence does not justify an arbitrary normal LRU capacity.
- Natural terminal failed-resident navigation and supported account-switch purge remain Runtime-unverified until those conditions/routes exist naturally; completed Work did not manufacture them.
- Historical scroll presentation is in-memory only; future active-response follow-tail eligibility remains unimplemented until the real Send/Stream response owner exists.
- Missing-anchor-message discard was not naturally exercised in exact b18 Runtime; source/CI contract exists but no device proof is claimed.
- Cache-core supported real verified-scope mismatch, provisional-row Detail-block tap, corrupt/schema rejection, iPad, iOS below 17 and non-personal workspace identity remain conditional Unknown / Unverified; they are not current known defects.

## Auto-refresh rule

Update this file proactively when project purpose, stack, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline/candidate changes.