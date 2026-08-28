# Project State

_Last updated: 2026-08-28 through b29 Candidate evidence and b28 Runtime failure._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope; PR #10.
- `DEV-multi-conversation-state-0.1.0-b21`: merged Stable multi-conversation read-state baseline for tested Plus/personal iPhone/iOS17 scope; PR #23.
- `DEV-conversation-list-cache-core-0.1.0-b23`: merged Stable conversation-list cache-core baseline for recorded Plus/personal iPhone/iOS17 scope; PR #24.

The merged accepted list/read baseline remains b23. `DEV-conversation-round-count` is the current Active Work layered on it and is not yet Stable.

## Active development — DEV-conversation-round-count

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable against `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2` at b29 product-CI time.
- **Current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b29`, `0.1.0 (29)`.
- **Exact product/config source**: `0b0c2fea44503423e75696f777fbf627aefac500`; later docs-only commits do not redefine the Runtime Candidate source.
- **Scope**: compact title-first conversation metadata, shared derived round count/answer anchors, authoritative timestamps, visible-text Copy, adaptive previous/next answer navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list-refresh presentation correction.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns display/interaction booleans only. `ConversationRoundProjection` is derived from authoritative visible messages. No second mutable semantic index, list owner or network path exists.
- **Type boundary**: ordinary supported detail may show `聊天 · N轮`; `工作` still requires an authoritative Work/Project source and must never be inferred from title/presentation text.
- **Preferences defaults**: round count On, message timestamps On, answer quick navigation On.

### Candidate history

- **b24**: package identity rejected; permanently reserved, never reuse.
- **b25**: Runtime partial/failing. Copy function, historical time and settings persistence accepted; header, rapid answer-jump behavior, refresh presentation and `30/29` reconcile behavior rejected.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound for the tested `28/29` sequence, sequential answer targets and compact header; jump smoothness/presentation still failed.
- **b27**: Runtime partial/failing. On 1063 visible messages semantic targets stayed sequential but jump execution paused/hitched; right-top refresh increased adjusted top inset ~34pt while list stayed correct; Copy visual too large. Superseded.
- **b28**: exact source `eacd3e68469e976f6cb41a600729c211f6cd32af`, Run `33149698659`, Artifact `9677214430`, IPA SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f`. Runtime partial/failing. On a 1577-visible-message conversation, answer-target completion showed material geometry drift (examples about `-1950`, `-7330`, `-11407` pt), programmatic taps could flip `next/previous` without real drag, first entry remained at ordinary top (`contentOffsetY≈-97.67`) despite the latest/bottom contract, and right-top refresh still produced the blank top region after refresh-control attributed text had already been removed. Superseded by b29.

### Current b29

- **Candidate**: `DEV-conversation-round-count-0.1.0-b29`, `0.1.0 (29)`.
- **Exact product/config source**: `0b0c2fea44503423e75696f777fbf627aefac500`.
- **Corrections written**:
  - disables the fixed 96pt estimated-row geometry and lays out before resolving long-distance answer offsets while retaining the same derived semantic answer authority and interruptible native offset animation;
  - while a programmatic target exists and both directions remain valid, preserves the current clicked direction; only real drag or a boundary overrides it;
  - no-saved-anchor first presentation now nonanimated-scrolls to the latest/bottom visible message, while established A/B semantic anchors remain independently restored;
  - right-top list refresh/status no longer uses `navigationItem.prompt`; fixed-height title feedback is used instead, and `UIRefreshControl.endRefreshing()` is called only for a real pull presentation.
- **Repository/network/reconcile/Preferences**: unchanged.
- **Static/source audit**: temporary product audit changed only `ConversationFeature.swift`; final Candidate commit changes exactly that file plus Xcode Build/Candidate identity and workflow Candidate/Artifact label.
- **Exact push CI**: Run `33155124626`, Job `98795968389`, success on Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9679291236`; ZIP `sha256:a6b481acd410c97a7db37c467decc11504f3925e2a45fa9b7e2e5ba3a10e907c`; IPA `ChatGPTClient-0.1.0-b29-dev-conversation-round-count.ipa`; IPA SHA `4378fe9b6a7340ea64a5c82063b0f7e3368e92deaf567d5e0ac40c08055a5360`.
- **Independent package inspection**: embedded `0.1.0 (29)`, Candidate b29, source marker `0b0c2fea4450`, minimum iOS14, device families iPhone+iPad, executable Mach-O arm64.
- **Initial PR merge-view evidence**: Run `33155126832`, Job `98795975759`, success on merge `a9a0cc286856e36df7378aa62be67f379ca631c2`, explicitly merging b29 product source into unchanged main. Merge-view Artifact `9679295199`, ZIP `sha256:873fe48beef6d5626e3fc1eae5b42ff0c3fba5cb37eba77f586f6f9f950c7fd1`, IPA SHA `15dfed506a9ddc725c2b072222b2111ae23cc8e8d51079eebccbf75f76e4a3d9`; merge-view output is CI evidence only.
- **Evidence level**: Code + scoped source/static audit + exact Candidate CI + identity-valid Artifact + initial PR merge-view CI. **Runtime/manual/real-device for b29: Pending. Stable/Frozen: No.**

## Stable predecessor boundaries retained

### Multi-conversation b21

PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`; exact Runtime Candidate `DEV-multi-conversation-state-0.1.0-b21`, product source `6b50ead167bfde305d2ad58dd16fee6edaabf597`. Accepted scope includes resident return, hidden completion, same-target coalescing/replacement, historical scroll and title lifecycle for tested Plus/personal iPhone/iOS17. Conditional account/workspace/natural-failure boundaries remain Unverified. Not Frozen.

### Conversation-list cache b23 + active bounded correction

PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`; exact Runtime Candidate `DEV-conversation-list-cache-core-0.1.0-b23`, source `d2af0fc157f6e2d037636c55f963c18071a332d5`, Run `33101116431`, Artifact `9658508764`. b23 accepted provisional cache, `recent_skip`, offline retention, explicit manual-refresh feedback, and real `28 + 1 -> 29` page-1 preservation. b26 within the Active metadata Work later accepted the authoritative-total cap for cold `30 -> 29` plus repeated `29/29`. That correction remains unchanged in b29.

Cache/privacy ownership remains unchanged: `ConversationRepository` is sole in-memory list owner; `ConversationListCacheStore` is storage-only; `AuthSessionStore` is sole verified auth/account owner; default persistent WebKit storage is sole persistent auth-secret authority. No retry/timer/watchdog/polling or alternate endpoint is introduced.

## Current architecture

- `AppDelegate`: lifecycle + accepted WebKit warm-up sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner; accepted total-count reconciliation unchanged in b29.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope hint.
- `ConversationDetailViewController`: detail/messages/recovery presentation, per-conversation semantic reading anchors, first-entry latest placement and b29 answer-jump presentation.
- `ConversationMessageCell`: message/timestamp/assistant-Copy presentation.
- `ConversationSidebarViewController`: list presentation; b29 keeps refresh feedback within fixed navigation height and native pull control separate from right-button refresh.
- `AppPreferences`: centralized persisted display/interaction preference owner.
- `ConversationRoundProjection`: derived round/answer projection, not mutable authority.
- `DiagnosticsLogger`: structured diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Roadmap handoff

`DEV-conversation-round-count` remains Active at the **b29 Runtime gate**. Do not merge/close PR #27 or describe this Work as Stable until exact b29 real-device acceptance. After accepted merge, the next serialized priority remains `DEV-send-stream`.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen. CI/Artifact success is not Runtime proof.
