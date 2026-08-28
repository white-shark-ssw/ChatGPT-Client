# Project Profile

## Initialization

**Initialized — 2026-08-25; product/runtime profile refreshed 2026-08-28 through b29 Candidate evidence**

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
- **Sidebar presentation**: `ConversationSidebarViewController`; presentation only. b29 keeps right-top refresh/status within fixed navigation height and keeps native pull-to-refresh separate without creating another request/list owner.
- **Message presentation**: `ConversationMessageCell`; message body, authoritative timestamp display and assistant Copy visual only.
- **Settings owner**: `AppPreferences` in `SettingsViewController.swift`; persisted display/interaction booleans only.
- **Round/answer derivation**: `ConversationRoundProjection`; derived from authoritative visible `ConversationDetail.messages`, not mutable conversation authority.
- **Test roots**: no XCTest/UI-test target yet.

## Build and validation

- Packaging: `bash scripts/build_ipa.sh`.
- Underlying build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- CI: GitHub Actions macOS15; current pipeline compiles `arm64-apple-ios14.0`; b29 uses Xcode 16.4 / iPhoneOS18.5 SDK.
- Artifact scheme: `build/artifacts/ChatGPTClient-<version>-b<build>-dev-<work-slug>.ipa` + SHA-256 sidecar.
- Package identity authority: expanded built `Info.plist` is authoritative for version/build/Candidate. Build script reads built metadata, validates Candidate/version/build agreement, derives the work slug and emits the identity-matched IPA. Workflow container label alone is not identity proof.
- Historical packaging defects: b16 and b24 had identity mismatches and are permanently rejected. b25+ use the corrected identity-safe packaging contract.

## Accepted baselines

- Foundation: b1 Stable/merged.
- Auth/account: b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic protocol-read: b7 accepted/merged for recorded read scope.
- Production native read: b9 Stable/merged.
- Recovery: b15 Stable/merged; PR #10.
- Multi-conversation read state: b21 Stable/merged; PR #23; resident/coalescing/historical-scroll/title/replacement behavior accepted for recorded Plus/personal iPhone/iOS17 scope. Frozen No.
- Conversation-list cache core: b23 Stable/merged; PR #24; provisional cache/recent-skip/offline/manual-refresh/real `28 + 1 -> 29` first-page behavior accepted for recorded scope. Frozen No.
- Active metadata Work additionally has real-device evidence from b26 accepting the authoritative-total cap for cold `30 -> 29` plus repeated `29/29`; that active correction remains unmerged and is unchanged in b29.

## Current conversation-metadata Work

`DEV-conversation-round-count` remains Active on `dev/conversation-round-count-20260828`, PR #27. Stable/Frozen No.

### Historical candidates

- b24: Artifact identity rejected/permanently reserved.
- b25: Runtime partial/failing; Copy function, historical time and preference persistence accepted; header/jump/refresh failed and `30/29` list issue exposed.
- reused-b25 source-fix output: identity-invalid, never test.
- b26: Runtime partial/failing; accepted bounded list reconciliation, sequential answer targets and compact title-first header; smoothness/Copy/refresh presentation still failed.
- b27: Runtime partial/failing; on 1063 visible messages semantic targets stayed sequential but jump execution paused/hitched; right-top refresh inflated adjusted top inset about 34pt while list remained correct; Copy visual too large.
- b28: exact source `eacd3e68469e976f6cb41a600729c211f6cd32af`, Run `33149698659`, Artifact `9677214430`, IPA SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f`. Runtime partial/failing: 1577-message diagnostics showed material off-screen target geometry drift, direction changes during programmatic taps without real drag, no-anchor first entry at top rather than latest, and the right-top refresh blank band still reproduced after refresh-control attributed-title removal. Superseded.

### Current b29 Runtime Candidate

- Candidate: `DEV-conversation-round-count-0.1.0-b29`
- Version/build: `0.1.0 (29)`
- Exact product/config source: `0b0c2fea44503423e75696f777fbf627aefac500`
- Product corrections: disables the fixed 96pt table estimated-row geometry for answer targets and resolves after layout; retains current clicked programmatic direction until real drag/boundary; implements nonanimated latest/bottom placement when no saved reading anchor exists; removes ordinary list-refresh/cache feedback from `navigationItem.prompt` and keeps native pull presentation separate.
- Exact push Run/Job: `33155124626` / `98795968389`, success.
- Runtime Artifact: `9679291236`; ZIP `sha256:a6b481acd410c97a7db37c467decc11504f3925e2a45fa9b7e2e5ba3a10e907c`.
- IPA: `ChatGPTClient-0.1.0-b29-dev-conversation-round-count.ipa`; SHA `4378fe9b6a7340ea64a5c82063b0f7e3368e92deaf567d5e0ac40c08055a5360`.
- Independent package inspection: `0.1.0 (29)`, Candidate b29, source marker `0b0c2fea4450`, minimum iOS14, device families `[1,2]`, Mach-O arm64.
- Initial PR merge-view Run/Job: `33155126832` / `98795975759`; merge `a9a0cc286856e36df7378aa62be67f379ca631c2` explicitly merged b29 product source into unchanged main; merge-view Artifact `9679295199`, IPA SHA `15dfed506a9ddc725c2b072222b2111ae23cc8e8d51079eebccbf75f76e4a3d9`. Merge-view output is merge evidence only.
- Evidence level: **Code + scoped source/static audit + exact Candidate CI + identity-valid Artifact + initial merge-view CI. Runtime/manual b29 Pending. Stable/Frozen No.**

## Versioning and candidate identity

- Marketing version source: `MARKETING_VERSION`.
- Build source: `CURRENT_PROJECT_VERSION`.
- Candidate scheme: `DEV-<work-slug>-<marketing-version>-b<build>`.
- Bundle ID: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.
- Current active Candidate: `0.1.0 (29)` / `DEV-conversation-round-count-0.1.0-b29`.
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
- b29 Runtime behavior is **not accepted yet**. CI/Artifact success does not prove long-conversation answer accuracy/smoothness, direction retention, first-entry latest placement or refresh-inset correction.
- Current source has no evidenced authoritative Chat/Work type owner; do not infer `工作` from title/presentation text.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or current validation evidence changes.
