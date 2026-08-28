# Project Profile

## Initialization

**Initialized — 2026-08-25; product/runtime profile refreshed 2026-08-28 through b30 Candidate evidence and b29 Runtime failure**

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
- Important config: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared scheme, `.github/workflows/ios-foundation.yml`.

## Repository structure and state owners

- **App entry**: `AppDelegate.swift`; accepted recovery baseline warms public default WebKit data store before product root.
- **Shell**: `RootViewController.swift`, `SettingsViewController.swift`; compact iPhone startup uses native list/detail navigation.
- **Build/runtime metadata**: `Support/AppBuildInfo.swift` + Xcode/Info.plist settings.
- **Diagnostics**: `Diagnostics/Diagnostics.swift` and accepted privacy-safe call sites.
- **Embedded login**: `Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore` only.
- **Auth/account authority**: `Authentication/AuthSessionStore.swift`; copied cookies/session bearer are transient only.
- **Diagnostic protocol probe**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation/list/read/recovery authority**: single `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only, schema-versioned summary snapshot + privacy-safe last-verified scope namespace hint. It is not list/account authority.
- **Conversation presentation**: `ConversationDetailViewController`; owns lightweight per-conversation historical reading anchors, no-anchor first-entry placement, current metadata and answer-jump presentation.
- **Sidebar presentation**: `ConversationSidebarViewController`; presentation only. b29 Runtime accepts fixed-height right-top refresh/status presentation without `navigationItem.prompt`; native pull-to-refresh remains separate.
- **Message presentation**: `ConversationMessageCell`; message body, authoritative timestamp and assistant Copy visual only. b29 Runtime exposed a self-sizing row regression caused by `estimatedRowHeight=0`; b30 restores automatic estimated self-sizing.
- **Settings owner**: `AppPreferences` in `SettingsViewController.swift`; persisted display/interaction booleans only.
- **Round/answer derivation**: `ConversationRoundProjection`; derived from authoritative visible `ConversationDetail.messages`, not mutable conversation authority.
- **Test roots**: no XCTest/UI-test target yet.

## Build and validation

- Packaging: `bash scripts/build_ipa.sh`.
- Underlying build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- CI: GitHub Actions macOS15; current pipeline compiles `arm64-apple-ios14.0`; b30 uses Xcode 16.4 / iPhoneOS18.5 SDK.
- Artifact scheme: `build/artifacts/ChatGPTClient-<version>-b<build>-dev-<work-slug>.ipa` + SHA-256 sidecar.
- Package identity authority: expanded built `Info.plist` is authoritative for version/build/Candidate. Build script validates Candidate/version/build agreement and emits identity-matched IPA. Workflow container label alone is not identity proof.
- Historical packaging defects: b16 and b24 had identity mismatches and are permanently rejected. b25+ use the corrected identity-safe packaging contract.

## Accepted baselines

- Foundation: b1 Stable/merged.
- Auth/account: b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic protocol-read: b7 accepted/merged for recorded read scope.
- Production native read: b9 Stable/merged.
- Recovery: b15 Stable/merged; PR #10.
- Multi-conversation read state: b21 Stable/merged; PR #23; resident/coalescing/historical-scroll/title/replacement behavior accepted for recorded scope. Frozen No.
- Conversation-list cache core: b23 Stable/merged; PR #24; provisional cache/recent-skip/offline/manual-refresh/real `28 + 1 -> 29` first-page behavior accepted. Frozen No.
- Active metadata Work additionally has b26 Runtime acceptance for the authoritative-total cap (`30 -> 29`, repeated `29/29`) and b29 Runtime acceptance for the right-top list blank-region presentation correction. These active corrections remain unmerged.

## Current conversation-metadata Work

`DEV-conversation-round-count` remains Active on `dev/conversation-round-count-20260828`, PR #27. Stable/Frozen No.

### Candidate progression

- b24: Artifact identity rejected/permanently reserved.
- b25: Runtime partial/failing; Copy function, historical time and preference persistence accepted; header/jump/refresh failed and `30/29` exposed.
- reused-b25 source-fix output: identity-invalid, never test.
- b26: Runtime partial/failing; bounded list reconciliation, sequential answer targets and compact title-first header accepted.
- b27: Runtime partial/failing; 1063-message jump still paused/hitched; right-top refresh inflated adjusted top inset ~34pt; Copy visual rejected.
- b28: Runtime partial/failing; 1577-message large answer-offset drift, programmatic direction flips, no-anchor first entry at top and refresh blank band.
- b29: Runtime partial/failing. **Accepted** right-top list refresh/top blank fix and stable `28/29 -> 29` list result. **Rejected** message-body/self-sizing presentation: rows deformed/collapsed/invisible even though Detail parsing still returned hundreds/thousands of visible messages. The b29 `estimatedRowHeight=0` optimization route is rejected.

### Current b30 Runtime Candidate

- Candidate: `DEV-conversation-round-count-0.1.0-b30`
- Version/build: `0.1.0 (30)`
- Exact product/config source: `a091327508d8393822784bb286245aff64c028a8`
- Product correction: restore `tableView.estimatedRowHeight = UITableView.automaticDimension` while retaining automatic row height. This is the only product-code delta from the preceding formal docs head; Repository/list/cache/Preferences/answer semantic owners are unchanged.
- Official Copy reference: user-supplied ChatGPT screenshot measures roughly 14.7pt for the Copy glyph on a 430pt @3x presentation. Current message cell keeps a 14pt regular `doc.on.doc`, dynamic `.secondaryLabel`, clear background and left alignment. Final visual acceptance is Runtime pending under restored normal row layout.
- Exact push Run/Job: `33160005440` / `98811893174`, success.
- Runtime Artifact: `9681236213`; ZIP `sha256:18de824c977fc825f041a6ae1e38974011f92888c6a7ba1eb38fb155f5ecd52f`.
- IPA: `ChatGPTClient-0.1.0-b30-dev-conversation-round-count.ipa`; SHA `91f5ee21e904fbe66932e306b7184dc645f33006e5bb10c33f8b3e3b22639db9`.
- Independent package inspection: `0.1.0 (30)`, Candidate b30, source marker `a091327508d8`, minimum iOS14, device families `[1,2]`, Mach-O arm64.
- Initial PR merge-view Run/Job: `33160008270` / `98811903542`; merge `fe7eb9f15bd06279338d96b5628f9873f813968d` explicitly merged b30 product source into unchanged main; merge-view Artifact `9681226498`, IPA SHA `cb2eca27416e61f18cc0e432023ae43ce97fe0e27f32a7ae90c1a7fb9898efcf`. Merge-view output is merge evidence only.
- Evidence level: **Code + scoped source/static audit + exact Candidate CI + identity-valid Artifact + initial merge-view CI. Runtime/manual b30 Pending. Stable/Frozen No.**

## Versioning and candidate identity

- Marketing version source: `MARKETING_VERSION`.
- Build source: `CURRENT_PROJECT_VERSION`.
- Candidate scheme: `DEV-<work-slug>-<marketing-version>-b<build>`.
- Bundle ID: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.
- Current active Candidate: `0.1.0 (30)` / `DEV-conversation-round-count-0.1.0-b30`.
- Exact produced identities are never reused after Artifact production.

## Runtime / deployment

- Native iOS application, TrollStore IPA.
- Deployment target iOS14.0; intended environment ceiling iOS17.0.
- Build device families iPhone+iPad; real-device evidence currently covers iPhone only unless explicitly stated.
- Artifact architecture arm64.

## Evidence boundaries

- iOS17 success does not prove iOS14–16 or iPad.
- Recorded read/recovery/multi-conversation/cache evidence is primarily Plus/personal; non-personal workspace identity remains Unknown/Unverified.
- Current source keys personal scope with `userID + accountID`; do not invent extra workspace identity without evidence.
- Supported account-switch purge, natural terminal failed-resident navigation, missing-anchor-message discard and some corrupt/provisional cache paths remain conditional Runtime-unverified.
- b30 Runtime behavior is **not accepted yet**. CI/Artifact success does not prove message-layout restoration, official Copy visual match, first-entry latest placement, or long-conversation answer accuracy/smoothness/direction.
- Current source has no evidenced authoritative Chat/Work type owner; do not infer `工作` from title/presentation text.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or current validation evidence changes.
