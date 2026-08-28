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

The merged accepted list/read baseline remains b23. `DEV-conversation-round-count` is the current Active Work layered on it and is not yet Stable.

## Active development — DEV-conversation-round-count

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open against unchanged `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2` at b28 product-CI time.
- **Current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b28`, `0.1.0 (28)`.
- **Exact product/config source**: `eacd3e68469e976f6cb41a600729c211f6cd32af`; later docs-only commits do not redefine the Runtime Candidate source.
- **Scope**: compact title-first conversation metadata, shared derived round count/answer anchors, authoritative timestamps, visible-text Copy, adaptive previous/next answer navigation, centralized persisted Preferences, and evidence-backed list-refresh presentation corrections.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns display/interaction booleans only. `ConversationRoundProjection` is derived from authoritative visible messages. No second mutable semantic index, list owner or network path exists.
- **Type boundary**: ordinary supported detail may show `聊天 · N轮`; `工作` still requires an authoritative Work/Project source and must never be inferred from title/presentation text.
- **Preferences defaults**: round count On, message timestamps On, answer quick navigation On.

### Candidate history

- **b24**: package identity rejected; permanently reserved, never reuse.
- **b25**: Runtime partial/failing. Copy function, historical time and settings persistence accepted; header, rapid answer-jump progression, refresh presentation and `30/29` reconcile behavior rejected.
- **b26**: Runtime partial/failing. Real-device accepted authoritative-total bound for the tested `28/29` sequence, sequential answer targets and compact header; still failed jump smoothness and requested timestamp/Copy/refresh presentation changes.
- **b27**: exact source `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`, Run `33144420732`, Runtime Artifact `9675208202`, IPA SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b`. Real-device evidence on a 1063-visible-message conversation retained sequential targets but still showed tap/start and mid-animation hitch. Right-top refresh changed `adjustedInsetTop` from about `97.67` to `131.67` while list data remained `28/29 -> 29`, proving the blank region was refresh-control/inset presentation rather than missing data or stranded overscroll. Assistant Copy visual remained too large. **b27 is Runtime partial/failing and superseded.**

### Current b28

- **Candidate**: `DEV-conversation-round-count-0.1.0-b28`, `0.1.0 (28)`.
- **Exact product/config source**: `eacd3e68469e976f6cb41a600729c211f6cd32af`.
- **Corrections written**:
  - answer jump preserves the same derived semantics but replaces repeated `scrollToRow(animated:)` with interruptible native content-offset animation; rapid retargeting stops the old programmatic motion at the current visible position before targeting the next derived answer;
  - right-top refresh and pull-to-refresh now have separate presentation sources; right-top refresh no longer alters `UIRefreshControl`; attributed refresh titles and b27 top-offset normalization were removed; real pull uses native spinner/endRefreshing only;
  - assistant Copy remains visible-text/system-pasteboard behavior but uses a 14pt `doc.on.doc` in a compact 28×28 left-aligned clear slot with `.secondaryLabel` tint.
- **Static/source audit**: pre-branch product audit changed only `ConversationFeature.swift`; final Candidate commit changes exactly that file plus Xcode build/Candidate identity and workflow Candidate/Artifact label. Repository/network/reconciliation/Preferences owners are unchanged.
- **Exact push CI**: Run `33149698659`, Job `98778576898`, success on Xcode 16.4; checkout exact b28 product source; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9677214430`; ZIP `sha256:0f51b3172aad23471991f3c04c467bb9da1b6256558001c8f60e55fca5f26c7b`; IPA `ChatGPTClient-0.1.0-b28-dev-conversation-round-count.ipa`; IPA SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f`.
- **Independent package inspection**: embedded version/build `0.1.0 (28)`, Candidate `DEV-conversation-round-count-0.1.0-b28`, source marker `eacd3e68469e`, minimum iOS14, device families iPhone+iPad, executable arm64.
- **PR merge-view evidence**: Run `33149701577`, Job `98778585595`, success on `f548cc8f568136d08128cc024612f89667680616`, explicitly merging `eacd3e68469e976f6cb41a600729c211f6cd32af` into unchanged main. Merge-view Artifact `9677198538`, IPA SHA `6bdc868fc1e673554a8bd2badf10d9667e4d497bc7953fd079b7f2f571d99a48`; merge-view output is CI evidence only.
- **Evidence level**: Code + scoped source/static audit + exact Candidate CI + identity-valid Artifact + initial PR merge-view CI. **Runtime/manual/real-device for b28: Pending. Stable/Frozen: No.**

## Stable predecessor boundaries retained

### Multi-conversation b21

PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`; exact Runtime Candidate `DEV-multi-conversation-state-0.1.0-b21`, product source `6b50ead167bfde305d2ad58dd16fee6edaabf597`. Accepted scope includes resident return, hidden completion, same-target coalescing/replacement, historical scroll and title lifecycle for tested Plus/personal iPhone/iOS17. Conditional account/workspace/natural-failure boundaries remain Unverified. Not Frozen.

### Conversation-list cache b23 + active bounded correction

PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`; exact Runtime Candidate `DEV-conversation-list-cache-core-0.1.0-b23`, source `d2af0fc157f6e2d037636c55f963c18071a332d5`, Run `33101116431`, Artifact `9658508764`. b23 accepted provisional cache, `recent_skip`, offline retention, explicit manual-refresh feedback, and real `28 + 1 -> 29` page-1 preservation. b26 within the Active metadata Work later real-device accepted the authoritative-total cap for cold `30 -> 29` plus repeated `29/29`. That correction remains unchanged in b28.

Cache/privacy ownership remains unchanged: `ConversationRepository` is sole in-memory list owner; `ConversationListCacheStore` is storage-only; `AuthSessionStore` is sole verified auth/account owner; default persistent WebKit storage is sole persistent auth-secret authority. No retry/timer/watchdog/polling or alternate endpoint is introduced.

## Current architecture

- `AppDelegate`: lifecycle + accepted WebKit warm-up sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner; accepted total-count reconciliation unchanged in b28.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope hint.
- `ConversationDetailViewController`: detail/messages/recovery presentation, historical scroll metadata, compact header and b28 interruptible answer-jump presentation.
- `ConversationMessageCell`: message/timestamp/assistant-Copy presentation; timestamp remains above its owning message; b28 shrinks assistant Copy visual only.
- `ConversationSidebarViewController`: list presentation; b28 separates right-top button refresh presentation from native pull-to-refresh without changing repository request authority.
- `AppPreferences`: centralized persisted display/interaction preference owner.
- `ConversationRoundProjection`: derived round/answer projection, not mutable authority.
- `DiagnosticsLogger`: structured diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Roadmap handoff

`DEV-conversation-round-count` remains Active at the **b28 Runtime gate**. Do not merge/close PR #27 or describe this Work as Stable until exact b28 real-device acceptance. After accepted merge, the next serialized priority remains `DEV-send-stream`.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen. CI/Artifact success is not Runtime proof.
