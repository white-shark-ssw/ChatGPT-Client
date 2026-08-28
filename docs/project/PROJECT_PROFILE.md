# Project Profile

## Initialization

**Initialized — 2026-08-25; product/runtime profile refreshed 2026-08-29 through exact b33 Candidate/Artifact evidence and b32 Runtime result.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: iOS native third-party ChatGPT client.
- **Primary runtime**: iOS; intended user-device ceiling iOS17.0; lower compatibility preferred where practical.

## Technology stack

- Swift 5 + UIKit.
- Foundation, WebKit, OSLog, CryptoKit.
- No third-party dependencies.
- Important config: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared Xcode scheme, `.github/workflows/ios-foundation.yml`.

## Repository structure and state owners

- **App entry**: `AppDelegate.swift`; accepted recovery baseline warms public default WebKit data store before product root.
- **Shell**: `RootViewController.swift`, `SettingsViewController.swift`; compact iPhone startup uses native list/detail navigation.
- **Build/runtime metadata**: `Support/AppBuildInfo.swift` + Xcode/Info.plist settings.
- **Diagnostics**: `Diagnostics/Diagnostics.swift` and privacy-safe call sites.
- **Embedded login**: `Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore` only.
- **Auth/account authority**: `Authentication/AuthSessionStore.swift`; copied cookies/session bearer are transient only.
- **Diagnostic protocol probe**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation/list/read/recovery authority**: single `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only, schema-versioned summary snapshot + privacy-safe last-verified scope namespace hint. It is not list/account authority.
- **Conversation presentation**: `ConversationDetailViewController`; owns lightweight per-conversation historical reading anchors, no-anchor first-entry placement, metadata and round-jump presentation.
- **Sidebar presentation**: `ConversationSidebarViewController`; presentation only. b29 Runtime accepts the right-top refresh blank-region correction.
- **Message presentation**: `ConversationMessageCell`; visible message body, authoritative timestamp and assistant Copy visual only. Automatic self-sizing restored in b30 and retained through b33.
- **Settings owner**: `AppPreferences` in `SettingsViewController.swift`; persisted display/interaction booleans only.
- **Round derivation**: `ConversationRoundProjection`; derived from authoritative visible `ConversationDetail.messages`, not mutable conversation authority.
- **Test roots**: no XCTest/UI-test target yet.

## Build and validation

- Packaging: `bash scripts/build_ipa.sh`.
- Underlying build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- CI: GitHub Actions macOS15; current pipeline compiles `arm64-apple-ios14.0`; b33 uses Xcode 16.4 / iPhoneOS18.5 SDK.
- Artifact scheme: `build/artifacts/ChatGPTClient-<version>-b<build>-dev-<work-slug>.ipa` + SHA-256 sidecar.
- Package identity authority: expanded built `Info.plist` is authoritative for version/build/Candidate. Build script validates Candidate/version/build agreement and emitted IPA identity. Workflow container label alone is not identity proof.
- Historical packaging defects: b16 and b24 had identity mismatches and are permanently rejected. Exact produced identities are never reused after Artifact production.

## Accepted baselines

- Foundation b1 Stable/merged.
- Auth/account b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic read b7 accepted/merged.
- Production native read b9 Stable/merged.
- Recovery b15 Stable/merged; PR #10.
- Multi-conversation read state b21 Stable/merged; PR #23; recorded resident/coalescing/historical-scroll/title/replacement scope accepted. Frozen No.
- Conversation-list cache core b23 Stable/merged; PR #24; provisional cache/recent-skip/offline/manual-refresh/real `28 + 1 -> 29` behavior accepted. Frozen No.
- Active metadata Work additionally carries b26 Runtime acceptance for authoritative-total stale-row cap (`30 -> 29`, repeated `29/29`) and b29 Runtime acceptance for right-top list refresh/top-blank correction. These active corrections remain unmerged.

## Current conversation-metadata Work

`DEV-conversation-round-count` remains Active on `dev/conversation-round-count-20260828`, PR #27. Stable/Frozen No.

### Runtime progression

- b24: Artifact identity rejected/permanently reserved.
- b25-b30: partial/failing iterations that established accepted Copy/time/preferences, compact header, bounded list reconciliation, right-top refresh correction and restored automatic message self-sizing while exposing answer-jump geometry/smoothness defects.
- b31: precise user-message round-start landing accepted; remaining hitch/internal-row/Copy issues required correction.
- b32: exact Runtime accepts recipient/tool filtering, compact Copy direction and precise semantic user-round landing; remaining defects are long-jump smoothness and physical-bottom rubber-band direction.

### Current b33 Runtime Candidate

- Candidate `DEV-conversation-round-count-0.1.0-b33`.
- Version/build `0.1.0 (33)`.
- Exact product/config source `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- Product correction is intentionally narrow: physical top/bottom boundaries outrank drag delta (including rubber-band overscroll); retain native animated `scrollToRow`; after animation, measure native landing and apply one same-target nonanimated re-anchor only when absolute error exceeds `1pt`; add privacy-safe `nativeLandingErrorPoints` / `landingCorrectionApplied` diagnostics.
- b32 recipient filtering, round derivation, Copy, list reconciliation, network behavior and ownership remain unchanged.
- Exact push Run/Job `33195740528` / `98932282377`, success.
- Runtime Artifact `9695669835`; ZIP `sha256:841b682ffe27a2788b2c297225705c0b4fb6bc18b527fd4e8f30c62e10312407`.
- IPA `ChatGPTClient-0.1.0-b33-dev-conversation-round-count.ipa`; SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`.
- Independent package inspection: `0.1.0 (33)`, Candidate b33, source `0ba15ec48fe8`, minimum iOS14.0, Mach-O arm64.
- Current-main PR merge-view Run/Job `33195744651` / `98932296906`, success on merge view `ca28819de6e5ed345087d04005ed05d74508881c` against `main@a6e3b2bc185b8d5df90b846040387262a64e6154`; merge Artifact `9695673573` is CI evidence only.
- Evidence level: **Code written + scoped source/static audit + exact Candidate CI + identity-valid Artifact + current-main merge-view CI. Runtime/manual b33 Pending. Stable/Frozen No.**

## Versioning and candidate identity

- Marketing version source: `MARKETING_VERSION`.
- Build source: `CURRENT_PROJECT_VERSION`.
- Candidate scheme: `DEV-<work-slug>-<marketing-version>-b<build>`.
- Bundle ID: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.
- Current active Candidate: `0.1.0 (33)` / `DEV-conversation-round-count-0.1.0-b33`.
- Exact produced identities b24-b33 are reserved and are never reused for corrected product output.

## Runtime / deployment

- Native iOS application, TrollStore IPA.
- Deployment target iOS14.0; intended environment ceiling iOS17.0.
- Build device families iPhone+iPad; real-device evidence currently covers iPhone only unless explicitly stated.
- Artifact architecture arm64.

## Evidence boundaries

- iOS17 success does not prove iOS14–16 or iPad.
- Recorded read/recovery/multi-conversation/cache evidence is primarily Plus/personal; non-personal workspace identity remains Unknown/Unverified.
- Current personal scope uses `userID + accountID`; do not invent extra workspace identity without evidence.
- Supported account-switch purge, natural terminal failed-resident navigation, missing-anchor-message discard and some corrupt/provisional cache paths remain conditional Runtime-unverified.
- b33 Runtime behavior is **not accepted yet**. CI/Artifact success does not prove bottom-rubber-band direction, long-jump smoothness, landing-correction behavior, first-entry latest placement or regressions.
- Current source has no evidenced authoritative Chat/Work type owner; do not infer `工作` from title/presentation text.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or current validation evidence changes.