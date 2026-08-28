# Project Profile

## Initialization

**Initialized — 2026-08-25; product/runtime profile refreshed 2026-08-29 through exact b33 Runtime and exact b34 Candidate/CI/Artifact evidence.**

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
- **Message presentation**: `ConversationMessageCell`; visible plain message body, authoritative timestamp and assistant Copy visual only. Automatic self-sizing restored in b30 and retained through b34. Markdown/rich annotation is not implemented yet.
- **Settings owner**: `AppPreferences` in `SettingsViewController.swift`; persisted display/interaction booleans only.
- **Round derivation**: `ConversationRoundProjection`; derived from authoritative visible `ConversationDetail.messages`, not mutable conversation authority.
- **Test roots**: no XCTest/UI-test target yet.

## Build and validation

- Packaging: `bash scripts/build_ipa.sh`.
- Underlying build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- CI: GitHub Actions macOS15; current pipeline compiles `arm64-apple-ios14.0`; b34 uses Xcode 16.4 / iPhoneOS18.5 SDK.
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
- b32: Runtime accepts recipient/tool filtering, compact Copy direction and precise semantic user-round landing; long-jump smoothness and physical-bottom rubber-band direction remained.
- b33: Runtime accepts physical-bottom/rubber-band direction and final semantic precision; long-distance/rapid jump remains gear-like. Diagnostics show 14 corrections across 74 completed jumps, including extreme rapid-retarget native errors up to about 8258.67pt before correction.

### Current b34 Runtime Candidate

- Candidate `DEV-conversation-round-count-0.1.0-b34`.
- Version/build `0.1.0 (34)`.
- Exact product/config source `bf66c7080347660e0154952a261230a24bb94f7d`.
- Product correction is intentionally narrow: when an animation-completion callback arrives, the existing >1pt landing correction is allowed only if the **current target row is visible**. If it is not visible, log `answerJump.completionIgnored` / `current_target_not_visible`, preserve the newer animation/cursor ownership and do not snap/correct.
- Native animated `scrollToRow` remains movement owner. Accepted b33 bottom-direction behavior, semantic round derivation, b32 recipient filtering, Copy, list reconciliation, network behavior and state ownership remain unchanged.
- Exact push Run/Job `33200768537` / `98949366655`, success on exact source `bf66c708...`.
- Runtime Artifact `9697664416`; ZIP `sha256:0b05a435888c041286b331c554f31f7e64dda0a30d214014bf2a144d8b696c65`.
- IPA `ChatGPTClient-0.1.0-b34-dev-conversation-round-count.ipa`; SHA `1705a2a39941ab6aee88e13b53d68d55b2fd9ff3d43d1c50d9cdcb6613c2b9b6`.
- Independent package inspection: `0.1.0 (34)`, Candidate b34, source `bf66c7080347`, minimum iOS14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.
- Current-main PR merge-view against unchanged `main@a6e3b2bc185b8d5df90b846040387262a64e6154`: Run/Job `33200813591` / `98949517057`, success on merge `a42408a64a4ff7fba7d799f39c897ae6930daf6f`; merge Artifact `9697686876`. Merge-view output is CI evidence only.
- Evidence level: **Code written + exact source/static audit + exact Candidate CI + identity-valid Artifact + current-main merge-view CI. Runtime/manual b34 Pending. Stable/Frozen No.**

## Rendering scope boundary

The current client has plain `UILabel.text` message presentation and no Markdown/rich-annotation renderer. The supplied official-app comparison recording confirms raw Markdown/table syntax and raw `filecite`-adjacent boxed glyphs in this client. Markdown/rich citation presentation belongs to Phase 11 `DEV-message-rendering`, not the current metadata/settings Work; do not strip or reinterpret those markers speculatively here.

## Versioning and candidate identity

- Marketing version source: `MARKETING_VERSION`.
- Build source: `CURRENT_PROJECT_VERSION`.
- Candidate scheme: `DEV-<work-slug>-<marketing-version>-b<build>`.
- Bundle ID: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.
- Current active Candidate: `0.1.0 (34)` / `DEV-conversation-round-count-0.1.0-b34`.
- Exact produced identities b24-b34 are reserved and are never reused for corrected product output.

## Runtime / deployment

- Native iOS application, TrollStore IPA.
- Deployment target iOS14.0; intended environment ceiling iOS17.0.
- Build device families iPhone+iPad; real-device evidence currently covers iPhone only unless explicitly stated.
- Artifact architecture arm64.

## Evidence boundaries

- b33 Runtime is partial/failing; b34 Runtime is Pending.
- iOS17 success does not prove iOS14–16 or iPad.
- Recorded read/recovery/multi-conversation/cache evidence is primarily Plus/personal; non-personal workspace identity remains Unknown/Unverified.
- Current personal scope uses `userID + accountID`; do not invent extra workspace identity without evidence.
- Supported account-switch purge, natural terminal failed-resident navigation, missing-anchor-message discard and some corrupt/provisional cache paths remain conditional Runtime-unverified.
- Current source has no evidenced authoritative Chat/Work type owner; do not infer `工作` from title/presentation text.
- CI/Artifact success does not prove b34 smoothness or regression behavior.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or current validation evidence changes.
