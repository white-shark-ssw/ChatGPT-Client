# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-29 through exact b36 Runtime failure, b37 no-stutter Runtime acceptance, and exact b38 Code/Static/CI/Artifact/current-main merge-view evidence.**

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
- **b37 message presentation geometry**: `ConversationMessagePresentationProjection` derives bounded plain-text display chunks, deterministic row heights/prefix offsets and message→first-row mapping from authoritative messages. It is ephemeral presentation state only.
- **Message cell**: `ConversationMessageCell` uses deterministic manual frame layout for one bounded display chunk; timestamps/assistant Copy remain presentation only. Copy reads the complete authoritative message.
- **Round-jump presentation**: one transient target cursor + one cancellable `UIViewPropertyAnimator`; b38 animates from the current viewport offset to an O(1) deterministic target offset.
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

## Stable / accepted merged baselines

- Foundation b1 Stable/merged.
- Auth/account b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic read b7 accepted/merged.
- Production native read b9 Stable/merged.
- Recovery b15 Stable/merged; PR #10.
- Multi-conversation read state b21 Stable/merged; PR #23; Frozen No.
- Conversation-list cache core b23 Stable/merged; PR #24; Frozen No.
- Active Phase 8 Work additionally carries b26 Runtime acceptance for authoritative-total stale-row cap (`30 -> 29`, repeated `29/29`) and b29 acceptance for the right-top refresh/top-blank presentation correction. Those remain unmerged until Phase 8 completes.

## Current Phase 8 — DEV-conversation-round-count

- Branch `dev/conversation-round-count-20260828`; PR #27 open, mergeable, not merged at exact b38 product validation.
- Stable/Frozen: No/No.
- b24-b38 emitted identities are reserved.

### Evidence progression relevant to the current gate

- b31 accepted precise semantic user-message round-start landing.
- b32 accepted recipient/tool/internal filtering and compact Copy direction.
- b33 accepted physical-bottom/rubber-band direction.
- b34 showed removing final correction ownership did not solve the remaining movement feel.
- b35 direct+short-ease retained multi-second tap-to-position stalls around long messages.
- **b36 Runtime partial/failing**: direct-position duration over 47 samples had median ~187ms, P90 ~780ms, max ~3952ms; ordinary right-side scroll-indicator dragging also severely stuttered. In the same 161-visible-message conversation, initially estimated bottom geometry around 13.8k points later reached about 154.6k points as giant self-sizing rows became realized. This moved root ownership from animation to long-message/table geometry.
- **b37 Runtime performance baseline accepted**: bounded display chunks + deterministic row metrics/prefix offsets + manual frame layout removed the reported stutter. Latest user feedback on exact b37: **“这次确实不卡了”**. This is acceptance of the geometry/performance direction, not yet final Phase 8 Stable.
- User then explicitly requested restoring genuine visible full-distance animation for another Runtime trial.

### Current b38 Runtime Candidate

- Candidate `DEV-conversation-round-count-0.1.0-b38`.
- Version/build `0.1.0 (38)`.
- Exact product/config source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact product diff from checkpoint parent `73d09cb83c3eda7b255e09b17b2bd9b0897cea49` is exactly three files: workflow 2+/2-, Xcode identity 4+/4-, `ConversationFeature.swift` 8+/20-.
- b37 deterministic message geometry/cell/projection code is unchanged.
- b38 removes the nonanimated ~120pt lead teleport and lead-position phase. One `UIViewPropertyAnimator` now continuously animates from current viewport offset to the already-derived target offset for 0.35s ease-in-out; short and long jumps use one method.
- Rapid retargeting stops the active animation at the current presentation position and continues toward the next semantic target. Real drag cancels programmatic intent immediately.
- No `scrollToRow` geometry discovery, final correction snap, timer, debounce, retry, watchdog, persistent row-height cache or second state owner.
- Exact push Run/Job `33230823568` / `99043233637`, success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: `0.1.0 (38)`, Candidate b38, source `0d1801137e4e`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.
- Current main remained `a6e3b2bc185b8d5df90b846040387262a64e6154` at product validation.
- PR Run/Job `33230825189` / `99043238346`, success on synthetic merge `fd1ed7508f04e9045b99239cad88dca8f6e01450`, which explicitly merges exact b38 source into current main. Merge Artifact `9708423606` is CI evidence only.
- Evidence level: **Code written + Static/source audit + exact push CI + identity-valid Runtime Artifact + current-main merge-view CI. Runtime Pending. Stable/Frozen No.**

## Rendering scope boundary

Current message body remains plain-string presentation. Markdown headings/lists/links/emphasis/code/tables and rich citation/annotation rendering belong to future `DEV-message-rendering`. Supplied comparison material showed raw Markdown/table syntax and raw `filecite`-adjacent boxed glyphs in this client; do not strip/reinterpret them speculatively in Phase 8.

## Runtime / evidence boundaries

- b36 Runtime is partial/failing.
- b37 Runtime accepts the no-stutter geometry/performance result.
- b38 Runtime is Pending and is the current human gate.
- iOS17 evidence does not prove iOS14–16 or iPad.
- Read/recovery/multi-conversation/cache evidence remains primarily Plus/personal; non-personal workspace isolation remains Unknown/Unverified.
- Supported real account-switch paths, some corrupt/provisional cache paths and other explicitly untested branches remain conditional/Unverified.
- Current source has no evidenced authoritative Chat/Work type owner; never infer `工作` from title text.
- CI/Artifact/merge-view success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
