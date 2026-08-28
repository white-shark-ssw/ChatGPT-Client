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

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open against `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2` at the latest checked state.
- **Exact current Runtime Candidate product/config source**: `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`. Later docs-only commits do not redefine this product source.
- **Current Candidate**: `DEV-conversation-round-count-0.1.0-b27`, `0.1.0 (27)`.
- **Scope**: compact official-style conversation header, shared derived active-branch round count/answer anchors, authoritative historical message timestamps, visible-text Copy, one adaptive previous/next answer navigation control, centralized persisted Preferences, plus evidence-backed list-refresh presentation corrections.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns display/interaction booleans only. `ConversationRoundProjection` is derived from authoritative visible `ConversationDetail.messages`; no second mutable counter/index authority and no new network path.
- **Type metadata boundary**: current ordinary-chat detail may present `聊天 · N轮` (`聊天` when round count is Off). `工作` still requires an authoritative Work/Project type source and must not be inferred from title/presentation text.
- **Preferences defaults**: round count On, message timestamps On, answer quick navigation On.

### Candidate history

#### Rejected b24

`DEV-conversation-round-count-0.1.0-b24` / `0.1.0 (24)` is permanently reserved and Artifact-identity rejected. Never rebuild or reuse it.

#### b25 Runtime partial/failing

- Candidate `DEV-conversation-round-count-0.1.0-b25`, `0.1.0 (25)`, exact source `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`.
- Run `33110228837`, Artifact `9662219000`, IPA SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`.
- Runtime accepted assistant Copy function, historical timestamp display and persistence of all three preferences.
- Runtime rejected the prompt-based header hierarchy, repeated same-target rapid answer jumps, redundant refresh presentation and unbounded `28 + 2 -> 30` list reconciliation.
- Source-fix commit `2a0d313346d44dae548d996c9037fa0ac305b974` later triggered an already-used b25 output; that build is identity-invalid for testing.

#### b26 Runtime partial/failing

- Candidate `DEV-conversation-round-count-0.1.0-b26`, `0.1.0 (26)`, exact source `7f845662185ef4e65a741bd37b09f9e9baebd723`.
- Push Run `33114798354`, Job `98666564839`, Artifact `9664109976`, IPA SHA `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`.
- **Runtime accepted/improved**: authoritative-total reconciliation bounded the tested `pageCount=28 / totalCount=29` sequence to `resultCount=29`, including discarding one stale excess off-page cached row and remaining at 29 on repeated manual refresh; compact title-first header was present; rapid answer targets progressed sequentially rather than repeatedly requesting the same row.
- **Runtime blocking**: occasional tap-to-scroll start delay and mid-animation hitch remained; user requested timestamps above each message; assistant Copy visual treatment was too large/prominent; top list pull/refresh could still expose a blank region with no visible refresh indication.
- The accepted total-count reconciliation is now evidence-backed and must not be changed without new contradictory evidence.

#### Current b27 Runtime Candidate

- **Candidate**: `DEV-conversation-round-count-0.1.0-b27`, `0.1.0 (27)`.
- **Exact product/config source**: `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`.
- **Exact push CI**: Run `33144420732`, Job `98762229798`, success on Xcode 16.4; target `arm64-apple-ios14.0`.
- **Exact Runtime Artifact**: `9675208202`; ZIP digest `sha256:038d3fe60ea49257a1f6ad0f09752facce8aeaecda484042b5df5cdb0f854cbd`.
- **IPA**: `ChatGPTClient-0.1.0-b27-dev-conversation-round-count.ipa`; SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b`.
- **Embedded identity**: Candidate `DEV-conversation-round-count-0.1.0-b27`; source marker `3bda8d8d78ec`.
- **PR merge-view CI**: Run `33144422834`, Job `98762236037`, success after checkout of `refs/pull/27/merge` at `3080dee98e3f6a1029dd66c992b99bfcb09e28a4`, explicitly merging b27 product head into unchanged main.
- **Corrections written**: removed answer-button recomputation from programmatic scroll frames; update direction/control state only at semantic drag/animation/tap boundaries; moved timestamps above their messages; restyled assistant Copy to compact dynamic-system treatment; added visible refresh-control presentation and top-overscroll normalization diagnostics without changing repository reconciliation/network semantics.
- **Evidence level**: Code written + source/static diff audit + exact CI + identity-valid Artifact + PR merge-view CI. **Runtime/manual/real-device: Pending. Stable/Frozen: No.**

## Stable predecessor boundaries retained

### Multi-conversation b21

PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`; exact Runtime Candidate `DEV-multi-conversation-state-0.1.0-b21`, product source `6b50ead167bfde305d2ad58dd16fee6edaabf597`. Accepted scope includes resident return, hidden completion, same-target coalescing/replacement, historical scroll and title lifecycle for tested Plus/personal iPhone/iOS17. Conditional account/workspace/natural-failure boundaries remain Unverified. Not Frozen.

### Conversation-list cache b23

PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`; exact Runtime Candidate `DEV-conversation-list-cache-core-0.1.0-b23`, source `d2af0fc157f6e2d037636c55f963c18071a332d5`, Run `33101116431`, Artifact `9658508764`. Runtime accepted provisional cache in ~4 ms, `recent_skip`, offline cache retention, explicit manual-refresh failure/success presentation, and a genuine `28 + 1 -> 29` page-1 reconciliation. b25 later exposed that unconstrained stale off-page candidates could violate authoritative total; the b26 Active-Work bounded correction is now real-device accepted for the tested `28 / total 29` sequence, while the surrounding Phase 8 Work remains unmerged and not Stable.

Cache/privacy ownership remains unchanged: `ConversationRepository` is sole in-memory list owner; `ConversationListCacheStore` is storage-only; `AuthSessionStore` is sole verified auth/account owner; default persistent WebKit storage is sole persistent auth-secret authority. No retry/timer/watchdog/polling or alternate endpoint is introduced.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner with account-scoped residents and persistent-list-cache integration; authoritative-total reconciliation bounding is retained unchanged in b27.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope namespace hint.
- `ConversationDetailViewController`: detail/messages/recovery presentation, per-conversation historical scroll metadata, compact header metadata and adaptive answer-jump presentation.
- `ConversationMessageCell`: visible message/timestamp/assistant-Copy presentation; b27 places timestamp above the owning message and uses compact dynamic Copy styling.
- `ConversationSidebarViewController`: list presentation and single manual refresh presentation; b27 adds visible refresh affordance/top normalization only, not list authority.
- `AppPreferences`: centralized persisted display/interaction preference owner; not conversation authority.
- `ConversationRoundProjection`: derived active-branch round/answer projection; not mutable data authority.
- `DiagnosticsLogger`: accepted structured diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Roadmap handoff

`DEV-conversation-round-count` remains Active. b26 is Runtime partial/failing and permanently superseded for correction testing. b27 is the current identity-valid Runtime Candidate and awaits focused real-device acceptance. Do not merge/close or describe this Work as Stable until b27 passes Runtime. After accepted merge, the next serialized development priority remains `DEV-send-stream`.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen acceptance. CI/Artifact success is not Runtime proof.
