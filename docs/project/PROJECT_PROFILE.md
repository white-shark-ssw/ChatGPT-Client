# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-29 through exact b38 Runtime acceptance and final merge preparation.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS.
- **Primary distribution**: TrollStore IPA.
- **Primary tested runtime**: iPhone / iOS17; lower iOS compatibility preferred where practical.

## Technology stack

- Swift 5 + UIKit.
- Foundation, WebKit, OSLog, CryptoKit.
- No third-party dependencies.
- Deployment target iOS14.0; product Artifact architecture arm64.
- Important config: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared Xcode scheme, `.github/workflows/ios-foundation.yml`.

## State owners / major modules

- **App lifecycle/root**: `AppDelegate.swift`, `RootViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore` only.
- **Auth/account authority**: `Authentication/AuthSessionStore.swift`; copied cookies/session bearer are transient only.
- **Embedded login**: `Authentication/AuthWebViewController.swift`; visible fallback only.
- **Diagnostic protocol probe**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation/list/read/recovery authority**: one `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only, never list/account authority.
- **Settings owner**: `AppPreferences`; persisted display/interaction booleans only.
- **Semantic round derivation**: `ConversationRoundProjection`; derived from authoritative visible `ConversationDetail.messages`, never mutable conversation authority.
- **Conversation presentation owner**: `ConversationDetailViewController`; historical reading anchors, first-entry latest placement and round-jump presentation.
- **Message presentation geometry**: `ConversationMessagePresentationProjection` derives bounded plain-text display chunks, deterministic row heights/prefix offsets and authoritative-message→first-row mapping. It is ephemeral presentation state only.
- **Message cell**: `ConversationMessageCell` uses deterministic manual frame layout for one bounded display chunk; timestamps/assistant Copy remain presentation only. Copy reads the complete authoritative message.
- **Round-jump presentation**: one transient target cursor + one cancellable `UIViewPropertyAnimator`; accepted b38 continuously animates from current viewport offset to an O(1) deterministic target offset.
- **Diagnostics**: `DiagnosticsLogger` is the structured privacy-safe diagnostics authority.
- **Test roots**: no XCTest/UI-test target yet.

## Build / CI / package identity

- Packaging: `bash scripts/build_ipa.sh`.
- Build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- CI: GitHub Actions macOS15.
- Artifact scheme: `build/artifacts/ChatGPTClient-<version>-b<build>-dev-<work-slug>.ipa` + SHA-256 sidecar.
- Marketing version source: `MARKETING_VERSION`.
- Build source: `CURRENT_PROJECT_VERSION`.
- Candidate scheme: `DEV-<work-slug>-<marketing-version>-b<build>`.
- Expanded built `Info.plist` is package identity authority for version/build/Candidate/source marker. Workflow Artifact name alone is not proof.
- Once an Artifact identity is emitted it is permanently reserved; corrected product code must use a new Candidate/build.

## Stable / accepted baselines

- Foundation b1 Stable/merged.
- Auth/account b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic read b7 accepted/merged.
- Production native read b9 Stable/merged.
- Recovery b15 Stable/merged; PR #10.
- Multi-conversation read state b21 Stable/merged; PR #23; Frozen No.
- Conversation-list cache core b23 Stable/merged; PR #24; Frozen No.
- Phase 8 `DEV-conversation-round-count` exact b38 is **Runtime accepted** on the recorded iPhone/iOS17 scope and awaiting final PR merge/state sync before durable Stable promotion. Frozen remains No.

## Accepted Phase 8 product identity / evidence

- Candidate `DEV-conversation-round-count-0.1.0-b38`, version/build `0.1.0 (38)`.
- Exact product/config source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact push Run / Job `33230823568` / `99043233637`, success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: Candidate b38, `0.1.0 (38)`, source marker `0d1801137e4e`, MinimumOSVersion 14.0, arm64.
- Product-head PR merge-view Run / Job `33230825189` / `99043238346` succeeded on synthetic merge `fd1ed7508f04e9045b99239cad88dca8f6e01450` against then-current `main@a6e3b2bc...`; final merge still requires a fresh current-head/current-main check after docs-only commits.
- User exact-device acceptance after b38: **“没问题了”**. No new diagnostics file accompanied the acceptance; do not invent numerical b38 Runtime timings.

## Accepted Phase 8 behavior / architecture

- b26 authoritative-total list reconciliation cap: stale `30 -> 29`, repeated `29/29`.
- b29 right-top refresh/top blank-region correction.
- b31 semantic quick-navigation target: authoritative user-message round start.
- b32 recipient/tool/internal filtering and compact assistant Copy direction.
- b33 physical-bottom/rubber-band direction.
- b36 Runtime identified long-message/table self-sizing geometry as the major stutter owner, including severe right-side scroll-indicator stutter.
- b37 replaced deferred giant-row self-sizing with bounded long-message display chunks, deterministic row heights/prefix offsets and manual cell layout; user accepted the no-stutter result.
- b38 preserved b37 geometry and restored genuine continuous full-distance round animation using deterministic O(1) target offsets; user accepted the resulting behavior.
- Short and long round jumps use one method. Rapid taps retarget from the current visual position; real drag immediately regains viewport ownership.
- First no-anchor entry shows latest/bottom; A/B semantic historical anchors and Sync/Reload re-derivation remain.

## Rendering scope boundary

Current message body remains plain-string presentation. Markdown headings/lists/links/emphasis/code/tables and rich citation/annotation rendering belong to future `DEV-message-rendering`. Supplied comparison material showed raw Markdown/table syntax and raw `filecite`-adjacent boxed glyphs; do not strip/reinterpret them speculatively in Phase 8.

## Runtime / evidence boundaries

- Exact b38 Runtime is accepted on recorded iPhone/iOS17 scope.
- Final Stable promotion is pending only PR merge and post-merge state/document synchronization; Frozen remains No.
- iOS17 evidence does not prove iOS14–16 or iPad.
- Read/recovery/multi-conversation/cache evidence remains primarily Plus/personal; non-personal workspace isolation remains Unknown/Unverified.
- Supported real account-switch paths, some corrupt/provisional cache paths and other explicitly untested branches remain conditional/Unverified.
- Current source has no evidenced authoritative Chat/Work type owner; never infer `工作` from title text.
- CI/Artifact/merge-view success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
