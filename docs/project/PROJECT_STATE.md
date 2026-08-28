# Project State

_Last updated: 2026-08-28 through b31 exact Candidate/Artifact evidence; b31 Runtime pending._

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

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Current main checked before b31 finalization**: `55216bde139f1058517ad852d98669f1c5cb54f1`; the advance from former `e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2` is docs-only (`SEND_STREAM_PREFLIGHT.md` + one `START_HERE.md` line) and has no product/Candidate/state-owner conflict with this Work.
- **Current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b31`, `0.1.0 (31)`.
- **Exact product/config source**: `9b0fae856380b44a5d0495f32618ea6da31a0e0d`; later docs-only commits do not redefine this Runtime Candidate source.
- **Scope**: compact title-first metadata, user-message-derived round count, authoritative timestamps, visible-text Copy, adaptive previous/next **round** navigation, persisted Preferences, first-entry latest placement, and evidence-backed list-refresh presentation.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns presentation booleans only. `ConversationRoundProjection` is derived from authoritative visible messages. No second mutable semantic index/list owner/network path.
- **Round navigation boundary**: a visible user message starts a round. In b31 the physical quick-jump target is that round-start user message row (`rounds[].userMessageID`), using direct `UITableView.scrollToRow(..., .top, animated:true)` rather than fixing a long-distance assistant-answer Y offset. The first assistant may remain derived metadata but is not the b31 physical target.
- **Type boundary**: ordinary supported detail may show `聊天 · N轮`; `工作` still requires authoritative Work/Project evidence.
- **Preference defaults**: round count On, message timestamps On, round quick navigation On. Settings label is `显示轮次快速跳转`.

### Candidate history

- **b24**: package identity rejected/permanently reserved.
- **b25**: Runtime partial/failing. Copy function, historical time and settings persistence accepted; header/jump/refresh and `30/29` reconcile rejected.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound (`30 -> 29`, repeated `29/29`), sequential targets and compact header.
- **b27**: Runtime partial/failing. 1063-message target progression remained sequential but jump paused/hitched; right-top refresh grew adjusted top inset; Copy visual rejected as too large.
- **b28**: Runtime partial/failing. 1577-message assistant-answer landing errors grew to thousands of points; direction could flip without real drag; first entry stayed at top; refresh blank band persisted.
- **b29**: Runtime partial/failing. **Accepted**: right-top list refresh no longer leaves the blank top region; normal adjusted top inset remained stable and list stayed `28/29 -> 29`. **Rejected**: message self-sizing/body presentation broke after `estimatedRowHeight=0`.
- **b30**: Runtime partial/failing. Automatic body sizing was restored and former severe jump hitch materially improved, but Copy visual remained too large and long-distance assistant-answer landing was grossly inaccurate (multi-thousand-point errors).
- **Invalid duplicate b30 during b31 staging**: source `50ec1c72b1638eebc2b485ed423f4d5d294ae4c9`, Run `33167629825`, Job `98836731029`, Artifact `9684234692`, ZIP `sha256:b001c5fdac2f9f8caf92a814314047ad88b798eeb38d53b451a8b4c59ac6720b`, IPA SHA `d6b2102079accd864cef9334a2f7760b39516ab07a7fb7cabe24e4ca7ff7516f`. It reused the already-produced b30 identity and is permanently identity-invalid; never install/test it.

### Current b31

- **Candidate**: `DEV-conversation-round-count-0.1.0-b31`, `0.1.0 (31)`.
- **Exact product/config source**: `9b0fae856380b44a5d0495f32618ea6da31a0e0d`.
- **Evidence-backed product correction**: navigation rows now derive from `ConversationRoundProjection.rounds[].userMessageID`; the target user row is requested with native row-identity scrolling and re-anchored to the same row at animation completion. Rapid-tap semantic progression and real-drag direction ownership remain. Accessibility wording is `上一轮` / `下一轮`.
- **Copy correction**: visible assistant `doc.on.doc` symbol reduced to 10pt regular based on exact b30 real-device size evidence while preserving the existing 28×28pt invisible hit/layout slot, clear background and dynamic tint.
- **Message sizing retained**: `rowHeight` and `estimatedRowHeight` remain `UITableView.automaticDimension`; b29's disabling-estimation regression is not reintroduced.
- **Repository/network retained**: b29 accepted list-refresh presentation and b26 authoritative-total reconcile are unchanged; no new request/retry/timer/watchdog/fallback/state owner was added.
- **Scoped source audit**: from pre-b31 product branch source `50ec1c72...`, the final b31 product/config delta is exactly workflow identity, Xcode build/Candidate identity and `ConversationFeature.swift` user-turn targeting/10pt Copy. No Repository/network/reconcile file path changed.
- **Exact push CI**: Run `33169669050`, Job `98843431963`, success; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9685082018`; ZIP `sha256:166d13cd8f298903e3620e3fbf286f50ca5d3d67caeac6f6528add31c3132bde`; IPA `ChatGPTClient-0.1.0-b31-dev-conversation-round-count.ipa`; IPA SHA `bd3cb30630538c6e3bb9c3f8e9d4d8e1d426691e8c06c8291b530f41fc81f422`.
- **Independent package inspection**: embedded `0.1.0 (31)`, Candidate b31, source marker `9b0fae856380`, minimum iOS14, device families `[1,2]`; executable Mach-O 64-bit arm64; local IPA SHA and Artifact ZIP digest match CI evidence.
- **PR merge-view evidence against current main**: Run `33169672792`, Job `98843444383`, success on `64a906bc4bc8cdc4c0c67d52efe566eafc715201`, with checkout log explicitly `Merge 9b0fae856380... into 55216bde139f...`. Merge-view Artifact `9685080936`, ZIP `sha256:66eeff33891f6e9505938337e584aced7ad23aad44aaba8d61cbd04bc354b275`, IPA SHA `2778e21cc519af82d0821ddbb7dc39b7c3d1ad55c1344eccd9a26ce5b5c35deb`. Merge-view output is merge evidence only, not the Runtime Artifact.
- **Evidence level**: Code written + scoped source/static audit + exact Candidate CI passed + identity-valid Artifact produced + PR merge-view CI passed. **Runtime/manual/real-device for b31: Pending. Stable/Frozen: No.**

## Stable predecessor boundaries retained

### Multi-conversation b21

PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`; exact Runtime Candidate source `6b50ead167bfde305d2ad58dd16fee6edaabf597`. Accepted scope includes resident return, hidden completion, same-target coalescing/replacement, historical scroll and title lifecycle for tested Plus/personal iPhone/iOS17. Conditional account/workspace/natural-failure boundaries remain Unverified. Not Frozen.

### Conversation-list cache b23 + active bounded correction

PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`; exact Runtime Candidate source `d2af0fc157f6e2d037636c55f963c18071a332d5`, Run `33101116431`, Artifact `9658508764`. b23 accepted provisional cache, `recent_skip`, offline retention, explicit manual-refresh feedback and real `28 + 1 -> 29` preservation. b26 later accepted the authoritative-total cap for cold `30 -> 29` plus repeated `29/29`. That correction remains unchanged in b31.

Cache/privacy ownership remains unchanged: `ConversationRepository` is sole in-memory list owner; `ConversationListCacheStore` is storage-only; `AuthSessionStore` is sole verified account owner; default persistent WebKit storage is sole persistent auth-secret authority. No retry/timer/watchdog/polling or alternate endpoint is introduced.

## Current architecture

- `AppDelegate`: lifecycle + accepted WebKit warm-up sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner; accepted list reconciliation unchanged in b31.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope hint.
- `ConversationDetailViewController`: detail/recovery presentation, per-conversation semantic anchors, first-entry latest path and user-turn quick-navigation presentation.
- `ConversationMessageCell`: message/timestamp/assistant-Copy presentation; b31 visible assistant Copy symbol is 10pt regular with existing 28×28pt hit/layout slot.
- `ConversationSidebarViewController`: list presentation; b29 Runtime accepts removal of prompt-induced right-refresh blank band.
- `AppPreferences`: centralized persisted display/interaction preference owner.
- `ConversationRoundProjection`: derived round projection from authoritative visible user/assistant messages, not mutable authority.
- `DiagnosticsLogger`: structured diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Roadmap handoff

`DEV-conversation-round-count` remains Active at the **b31 Runtime gate**. Install only exact Runtime Artifact `9685082018`. Primary acceptance is precise adjacent-round landing at the corresponding **user-message row**, including rapid repeated taps, long-distance travel and real-drag interruption; separately assess residual animation hitch. Recheck Copy visual against the official reference plus automatic message sizing, first-entry latest/bottom, accepted list-refresh/list-total behavior, timestamps/preferences, A/B anchors, Sync/Reload and basic accessibility. Do not merge/close PR #27 or describe this Work as Stable until exact b31 real-device acceptance. After accepted merge, next serialized priority remains `DEV-send-stream`.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen. CI/Artifact success is not Runtime proof.
