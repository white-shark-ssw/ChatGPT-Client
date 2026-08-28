# Project State

_Last updated: 2026-08-28 through b30 Candidate evidence and b29 Runtime failure._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery baseline; PR #10.
- `DEV-multi-conversation-state-0.1.0-b21`: merged Stable multi-conversation read-state baseline; PR #23.
- `DEV-conversation-list-cache-core-0.1.0-b23`: merged Stable list-cache-core baseline; PR #24.

The merged accepted list/read baseline remains b23. `DEV-conversation-round-count` is the current Active Work layered on it and is not yet Stable.

## Active development — DEV-conversation-round-count

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable against `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2` at b30 product-CI time.
- **Current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b30`, `0.1.0 (30)`.
- **Exact product/config source**: `a091327508d8393822784bb286245aff64c028a8`; later docs-only commits do not redefine this Runtime Candidate source.
- **Scope**: compact title-first metadata, shared derived round count/answer anchors, authoritative timestamps, visible-text Copy, adaptive previous/next answer navigation, persisted Preferences, first-entry latest placement, and evidence-backed list-refresh presentation.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns presentation booleans only. `ConversationRoundProjection` is derived from authoritative visible messages. No second mutable semantic index/list owner/network path.
- **Type boundary**: ordinary supported detail may show `聊天 · N轮`; `工作` still requires authoritative Work/Project evidence.
- **Preference defaults**: round count On, message timestamps On, answer quick navigation On.

### Candidate history

- **b24**: package identity rejected/permanently reserved.
- **b25**: Runtime partial/failing. Copy function, historical time and settings persistence accepted; header/jump/refresh and `30/29` reconcile rejected.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound (`30 -> 29`, repeated `29/29`), sequential answer targets and compact header.
- **b27**: Runtime partial/failing. 1063-message target progression remained sequential but jump paused/hitched; right-top refresh grew adjusted top inset ~34pt; Copy visual rejected as too large.
- **b28**: Runtime partial/failing. 1577-message answer landing errors grew to thousands of points; direction could flip without real drag; first entry stayed at top; refresh blank band persisted.
- **b29**: Runtime partial/failing. **Accepted**: right-top list refresh no longer leaves the blank top region; normal adjusted top inset remains stable and list remains `28/29 -> 29`. **Rejected**: message self-sizing layout catastrophically deformed/collapsed after `estimatedRowHeight=0`; Detail data still parsed hundreds/thousands of visible messages, so network/parser were not the cause. Jump and first-entry visual behavior are not accepted from this broken-body run.

### Current b30

- **Candidate**: `DEV-conversation-round-count-0.1.0-b30`, `0.1.0 (30)`.
- **Exact product/config source**: `a091327508d8393822784bb286245aff64c028a8`.
- **Correction written**: restores `tableView.estimatedRowHeight = UITableView.automaticDimension` while retaining `rowHeight = UITableView.automaticDimension`. This is the sole product-code delta from the preceding formal branch head.
- **Retained accepted behavior**: b29 list refresh no-prompt/no-blank presentation, b26 total-count reconcile, Repository/network/cache ownership, Preferences, semantic answer projection/cursor and first-entry-latest code paths are unchanged.
- **Copy reference**: user supplied official ChatGPT iOS screenshot. Measured glyph is about 14.7pt on the @3x reference. Current 14pt regular `doc.on.doc`, `.secondaryLabel`, clear background and left alignment is retained for b30; final visual acceptance remains Runtime pending after normal row layout is restored.
- **Scoped source audit**: formal b30 Candidate changes exactly `ConversationFeature.swift` (one line), Xcode Build/Candidate identity, and workflow Candidate/Artifact label.
- **Exact push CI**: Run `33160005440`, Job `98811893174`, success; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9681236213`; ZIP `sha256:18de824c977fc825f041a6ae1e38974011f92888c6a7ba1eb38fb155f5ecd52f`; IPA `ChatGPTClient-0.1.0-b30-dev-conversation-round-count.ipa`; IPA SHA `91f5ee21e904fbe66932e306b7184dc645f33006e5bb10c33f8b3e3b22639db9`.
- **Independent package inspection**: embedded `0.1.0 (30)`, Candidate b30, source marker `a091327508d8`, minimum iOS14, device families iPhone+iPad; executable Mach-O arm64; local IPA SHA matches CI sidecar.
- **Initial PR merge-view evidence**: Run `33160008270`, Job `98811903542`, success on merge `fe7eb9f15bd06279338d96b5628f9873f813968d`, explicitly merging b30 product source into unchanged main. Merge-view Artifact `9681226498`, ZIP `sha256:03d1f259fb77b907ad4709516734751f67a2a81df24080317626abf22cd3ea4d`, IPA SHA `cb2eca27416e61f18cc0e432023ae43ce97fe0e27f32a7ae90c1a7fb9898efcf`; merge-view output is CI evidence only.
- **Evidence level**: Code + scoped source/static audit + exact Candidate CI + identity-valid Artifact + initial PR merge-view CI. **Runtime/manual/real-device for b30: Pending. Stable/Frozen: No.**

## Stable predecessor boundaries retained

### Multi-conversation b21

PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`; exact Runtime Candidate source `6b50ead167bfde305d2ad58dd16fee6edaabf597`. Accepted scope includes resident return, hidden completion, same-target coalescing/replacement, historical scroll and title lifecycle for tested Plus/personal iPhone/iOS17. Conditional account/workspace/natural-failure boundaries remain Unverified. Not Frozen.

### Conversation-list cache b23 + active bounded correction

PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`; exact Runtime Candidate source `d2af0fc157f6e2d037636c55f963c18071a332d5`, Run `33101116431`, Artifact `9658508764`. b23 accepted provisional cache, `recent_skip`, offline retention, explicit manual-refresh feedback and real `28 + 1 -> 29` preservation. b26 later accepted the authoritative-total cap for cold `30 -> 29` plus repeated `29/29`. That correction remains unchanged in b30.

Cache/privacy ownership remains unchanged: `ConversationRepository` is sole in-memory list owner; `ConversationListCacheStore` is storage-only; `AuthSessionStore` is sole verified account owner; default persistent WebKit storage is sole persistent auth-secret authority. No retry/timer/watchdog/polling or alternate endpoint is introduced.

## Current architecture

- `AppDelegate`: lifecycle + accepted WebKit warm-up sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner; accepted list reconciliation unchanged in b30.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope hint.
- `ConversationDetailViewController`: detail/recovery presentation, per-conversation semantic anchors, first-entry latest code path and answer-jump presentation.
- `ConversationMessageCell`: message/timestamp/assistant-Copy presentation.
- `ConversationSidebarViewController`: list presentation; b29 Runtime accepts removal of prompt-induced right-refresh blank band.
- `AppPreferences`: centralized persisted display/interaction preference owner.
- `ConversationRoundProjection`: derived round/answer projection, not mutable authority.
- `DiagnosticsLogger`: structured diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Roadmap handoff

`DEV-conversation-round-count` remains Active at the **b30 Runtime gate**. First gate is normal message/body row layout. After that, re-evaluate Copy visual, first-entry latest placement and answer-jump accuracy/smoothness/direction. Do not merge/close PR #27 or describe this Work as Stable until exact b30 real-device acceptance. After accepted merge, next serialized priority remains `DEV-send-stream`.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen. CI/Artifact success is not Runtime proof.
