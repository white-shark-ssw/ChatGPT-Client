# Project State

_Last updated: 2026-08-28._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope; PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.
- `DEV-multi-conversation-state-0.1.0-b21`: merged Stable multi-conversation read-state baseline for tested Plus/personal iPhone/iOS17 scope; PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`.
- `DEV-conversation-list-cache-core-0.1.0-b23`: merged Stable conversation-list cache-core baseline for the recorded Plus/personal iPhone/iOS17 scope; PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`.

The merged accepted baseline remains b23 for conversation-list cache/read behavior. `DEV-conversation-round-count` is the current Active Work layered on that baseline and is not yet Stable.

## Active development — DEV-conversation-round-count

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable against `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2` at the latest checked state.
- **Exact current Runtime Candidate product/config source**: `7f845662185ef4e65a741bd37b09f9e9baebd723`. Later docs-only commits do not redefine this product source.
- **Scope**: compact official-style conversation header, shared derived active-branch round count/answer anchors, authoritative historical message timestamps, visible-text Copy, one adaptive previous/next answer navigation control, centralized persisted Preferences, plus evidence-backed corrections to redundant list refresh presentation and total-bounded page-1 cache reconciliation exposed by b25 Runtime.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns display/interaction booleans only. `ConversationRoundProjection` is derived from authoritative visible `ConversationDetail.messages`; no second mutable counter/index authority and no new network path.
- **Type metadata boundary**: b25 official-app comparison establishes the compact hierarchy `title` then second-line type/round metadata. Current ordinary-chat detail may present `聊天 · N轮` (`聊天` when round count is Off). `工作` still requires an authoritative Work/Project type source and must not be inferred from title/presentation text.
- **Preferences defaults**: round count On, message timestamps On, answer quick navigation On.

### Candidate history

#### Rejected b24

`DEV-conversation-round-count-0.1.0-b24` / `0.1.0 (24)` is permanently reserved and Artifact-identity rejected. Exact product source `3eefc34d9fd279e2913509591446f8f2c4575f41`; Run `33109613596`; Job `98648639389`; uploaded container Artifact `9661977997`. Build logs prove stale packaging embedded cache-core b23 Candidate and emitted a cache-core-slug IPA. b24 was never installed/tested and must never be rebuilt or reused.

#### b25 Runtime partial/failing

- Candidate `DEV-conversation-round-count-0.1.0-b25`, `0.1.0 (25)`.
- Exact product/config source `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`.
- Exact CI Run `33110228837`, Job `98650799276`, Artifact `9662219000`, IPA SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`.
- **Runtime accepted sub-results**: assistant Copy works; historical message times display acceptably in the tested case; all three settings persist across relaunch.
- **Runtime rejected**: prompt-based `N轮` header appeared above title and made navigation bar too tall; rapid repeated answer-jump taps could repeatedly target the same answer row and sometimes not land at the intended answer start; pull-refresh during an existing list load could leave an empty refresh area until the older load ended.
- **Additional log defect**: service returned `pageCount=28`, authoritative `totalCount=29`, while reconciliation preserved two off-page cached rows and produced `resultCount=30`.

Source-fix commit `2a0d313346d44dae548d996c9037fa0ac305b974` auto-triggered Run `33114539883` before the b26 allocation landed. That output reused the already-tested b25 identity and is permanently identity-invalid for testing regardless of compile success.

#### Current b26 Runtime Candidate

- **Candidate**: `DEV-conversation-round-count-0.1.0-b26`, `0.1.0 (26)`.
- **Exact product/config source**: `7f845662185ef4e65a741bd37b09f9e9baebd723`.
- **Exact CI**: push Run `33114798354`, Job `98666564839`, success on Xcode 16.4; target `arm64-apple-ios14.0`.
- **Artifact**: `9664109976`; ZIP `sha256:c93951d3756f2440b04f895e8aeca85ad66b4499617ff686cb7c4735d5fa51af`.
- **IPA**: `ChatGPTClient-0.1.0-b26-dev-conversation-round-count.ipa`; SHA `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`.
- **Embedded identity**: Candidate `DEV-conversation-round-count-0.1.0-b26`; source marker `7f845662185e`.
- **Corrections written**: compact two-line `navigationItem.titleView`; transient programmatic answer-target cursor so consecutive taps advance from the last requested answer until a real user drag resets it; native `scrollToRow(..., .top, animated: true)` target positioning; redundant refresh-control early-return cleanup; authoritative-total-bounded off-page reconciliation with excess-discard diagnostics.
- **Evidence level**: Code written + source/static review + exact CI + identity-valid Artifact. **Runtime/manual/real-device: Pending. Stable/Frozen: No.**

## Stable predecessor boundaries retained

### Multi-conversation b21

PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`; exact Runtime Candidate `DEV-multi-conversation-state-0.1.0-b21`, product source `6b50ead167bfde305d2ad58dd16fee6edaabf597`. Accepted scope includes resident return, hidden completion, same-target coalescing/replacement, historical scroll and title lifecycle for tested Plus/personal iPhone/iOS17. Conditional account/workspace/natural-failure boundaries remain Unverified. Not Frozen.

### Conversation-list cache b23

PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`; exact Runtime Candidate `DEV-conversation-list-cache-core-0.1.0-b23`, source `d2af0fc157f6e2d037636c55f963c18071a332d5`, Run `33101116431`, Artifact `9658508764`. Runtime accepted provisional cache in ~4 ms, `recent_skip`, offline cache retention, explicit manual-refresh failure/success presentation, and a genuine `28 + 1 -> 29` page-1 reconciliation. b25 later proved that unconstrained stale off-page candidates can violate authoritative total; b26's bounded correction is an Active-Work correction and is not yet Runtime accepted.

Cache/privacy ownership remains unchanged: `ConversationRepository` is sole in-memory list owner; `ConversationListCacheStore` is storage-only; `AuthSessionStore` is sole verified auth/account owner; default persistent WebKit storage is sole persistent auth-secret authority. No retry/timer/watchdog/polling or alternate endpoint is introduced.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner with account-scoped residents and persistent-list-cache integration; b26 adds only authoritative-total reconciliation bounding.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope namespace hint.
- `ConversationDetailViewController`: detail/messages/recovery presentation, per-conversation historical scroll metadata, compact header metadata and answer-jump presentation.
- `ConversationMessageCell`: visible message/timestamp/assistant-Copy presentation.
- `AppPreferences`: centralized persisted display/interaction preference owner; not conversation authority.
- `ConversationRoundProjection`: derived active-branch round/answer projection; not mutable data authority.
- `DiagnosticsLogger`: accepted structured diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Roadmap handoff

`DEV-conversation-round-count` remains Active. b25 is Runtime partial/failing; b26 is the current identity-valid Runtime Candidate and awaits real-device acceptance. Do not merge/close or describe this Work as Stable until b26 passes the focused Runtime retest. After accepted merge, the next serialized development priority remains `DEV-send-stream`.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen acceptance. CI/Artifact success is not Runtime proof.
