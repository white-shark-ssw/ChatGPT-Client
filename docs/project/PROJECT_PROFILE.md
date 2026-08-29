# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-29 through valid b43 hybrid CI/Artifact.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS, with a TD-024 explicit user-visible official-Web Send surface for ChatGPT-account sending after pure-native account-session Send was proven browser-challenge blocked.
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
- **Embedded visible Web surfaces**: `Authentication/AuthWebViewController.swift` owns the visible login fallback and TD-024's explicit user-visible `hybridChat` official ChatGPT Send surface. The hybrid surface uses the same default persistent WebKit data store; hidden/shadow Web transport remains prohibited.
- **Diagnostic protocol probe**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production native conversation/list/read/recovery authority**: one `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only, never list/account authority.
- **Settings owner**: `AppPreferences`; persisted display/interaction booleans only. Settings also exposes the explicit hybrid Web entry without owning Web/chat state.
- **Semantic round derivation**: `ConversationRoundProjection`; derived from authoritative visible `ConversationDetail.messages`, never mutable conversation authority.
- **Conversation presentation owner**: `ConversationDetailViewController`; historical reading anchors, first-entry latest placement and round-jump presentation.
- **Message presentation geometry**: `ConversationMessagePresentationProjection` derives bounded plain-text display chunks, deterministic row heights/prefix offsets and authoritative-message→first-row mapping. It is ephemeral presentation state only.
- **Message cell**: `ConversationMessageCell` uses deterministic manual frame layout for one bounded display chunk; timestamps/assistant Copy remain presentation only. Copy reads the complete authoritative message.
- **Round-jump presentation**: one transient target cursor + one cancellable `UIViewPropertyAnimator`; accepted b38 continuously animates from current viewport offset to an O(1) deterministic target offset.
- **Diagnostics**: `DiagnosticsLogger` is the structured privacy-safe diagnostics authority. b43 adds safe `webSend` presentation/reuse/navigation fields only.
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

## Stable / accepted merged baselines

- Foundation b1 Stable/merged.
- Auth/account b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic read b7 accepted/merged.
- Production native read b9 Stable/merged.
- Recovery b15 Stable/merged; PR #10.
- Multi-conversation read state b21 Stable/merged; PR #23; Frozen No.
- Conversation-list cache core b23 Stable/merged; PR #24; Frozen No.
- **Conversation metadata/settings/round navigation b38 Stable/merged; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

## Phase 8 accepted product identity / evidence

- Work `DEV-conversation-round-count` completed and merged.
- Candidate `DEV-conversation-round-count-0.1.0-b38`, version/build `0.1.0 (38)`.
- Exact tested product/config source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact push Run / Job `33230823568` / `99043233637`, success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: Candidate b38, `0.1.0 (38)`, source marker `0d1801137e4e`, MinimumOSVersion 14.0, arm64.
- User exact-device acceptance after b37 no-stutter baseline and b38 animation restoration: **“没问题了”**.
- Final PR head `57b3efe576dbf187171439a68d6d2dfe2fba0ebc`; product source→final PR head delta was docs-only.
- Fresh current-head synthetic merge before merge: `8168fc1aad006ab665f13f77972159f633361b61`, explicitly merging final PR head into then-current `main@a6e3b2bc...`.
- Actual merged main commit: `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.

## Current Phase 9 test Candidate

- Work `DEV-send-stream` remains Active; PR #29 open.
- Pure-native ChatGPT-account Send is blocked by exact b42 browser anti-abuse evidence; user selected TD-024's visible hybrid Web Send architecture.
- Current Candidate: `DEV-send-stream-0.1.0-b43`, `0.1.0 (43)`.
- Exact product/config source: `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`.
- Push Run / Job: `33241032864` / `99070294478`, success.
- PR Run / Job: `33241035013` / `99070299776`, success.
- Artifact: `9711364573`; ZIP `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`.
- IPA: `ChatGPTClient-0.1.0-b43-dev-send-stream.ipa`; SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.
- Independent package inspection: Candidate b43, `0.1.0 (43)`, source marker `f602d68ae95d`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.
- **Evidence level**: Code/CI/Artifact valid and identity-verified; exact-device Runtime pending; Stable/Frozen No.
- Accidental newer-code Artifact `9710515489` carrying b42 identity is permanently rejected and must never be installed. Legitimate b42 remains Artifact `9709824510`.

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

## Current hybrid Send architecture boundary

- `AuthWebViewController.hybridChat` is a **user-visible** official ChatGPT surface, not a hidden transport.
- First visible presentation loads `https://chatgpt.com/`; ordinary return/re-entry is designed to reuse one process-resident controller/WebView without automatic reload.
- No DOM mirroring, prompt/answer/reasoning scraping, challenge/proof/token capture or native replay is part of b43.
- Functional Send is not enough: exact-device Runtime must accept first-entry responsiveness, resident reuse, keyboard/typing, streamed-response scrolling, rapid scrolling, native return and attachment `+` responsiveness.
- Native-picker→official-Web attachment handoff remains Unknown/Unverified.

## Rendering scope boundary

Current native message body remains plain-string presentation. Markdown headings/lists/links/emphasis/code/tables and rich citation/annotation rendering belong to future `DEV-message-rendering`. Supplied comparison material showed raw Markdown/table syntax and raw `filecite`-adjacent boxed glyphs; do not strip/reinterpret them speculatively in completed Phase 8 behavior.

## Runtime / evidence boundaries

- Exact b38 Runtime is accepted on recorded iPhone/iOS17 scope and the recorded Phase 8 scope is Stable/merged. Frozen No.
- Exact b42 Runtime is accepted as Phase 9 protocol/security-boundary evidence; it does not prove native production Send.
- Exact b43 is currently only Code/CI/Artifact evidence; hybrid Runtime acceptance is pending.
- iOS17 evidence does not prove iOS14–16 or iPad.
- Read/recovery/multi-conversation/cache evidence remains primarily Plus/personal; non-personal workspace isolation remains Unknown/Unverified.
- Supported real account-switch paths, native-to-Web attachment handoff and other explicitly untested branches remain conditional/Unverified.
- Current native source has no evidenced authoritative Chat/Work type owner; never infer `工作` from title text.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
