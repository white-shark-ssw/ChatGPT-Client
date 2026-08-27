# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-27._

## Purpose

This is the durable implementation sequence for the iOS-native ChatGPT client. Current source, CI/artifact evidence, real-device evidence and specialized plans under `docs/project/` take priority over stale historical wording.

Current constraints: native UIKit iOS client; TrollStore IPA; intended primary runtime iPhone/iOS17; deployment target iOS14; current ChatGPT private/internal behavior must be evidenced rather than guessed.

## Delivery principles

1. Fast usable loop before breadth.
2. Diagnosability before complexity.
3. Authentication/session ownership before protocol assumptions.
4. One authoritative owner per identity/state domain.
5. Native model/state separate from mounted UI.
6. Official ChatGPT iOS interaction is the default visual/interaction baseline unless explicit requirements or runtime pain points justify deviation.
7. Core owner work is serial; edge work parallelizes only after conflict scanning.
8. Always distinguish Code, static checks, CI, Artifact, Runtime and Stable/Frozen evidence.
9. Do not add speculative retry, fallback, watchdog, duplicate state or compatibility machinery.

## Usability milestones

- **V0.1 read-use**: native shell + conversation list/detail/message rendering + manual sync/full reload + usable cold-start login-state recovery.
- **V0.2 chat-use**: V0.1 + stable multi-conversation state ownership + conversation metadata/preferences + long-conversation answer navigation + text send/new conversation + streaming + stop + user-visible reasoning interaction/haptics + recovery integration.
- **V0.3 daily-use refinement**: instant cache-backed conversation-list startup + clipped list previews + Markdown export + long-conversation tuning + attachments and remaining daily-use conversation features.

## Completed foundations

### Phase 1 — `DEV-app-foundation`
Completed / merged / Stable.

### Phase 2 — `DEV-auth-bootstrap`
Completed / merged / Stable for tested scope. Default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority; native auth consumption remains transient.

### Phase 3 — `DEV-protocol-read`
Completed / merged / Stable for accepted diagnostic read scope.

### Phase 4 — `DEV-native-read-path`
Completed / merged / Stable for tested b9 scope. `ConversationRepository` owns production conversation summaries/selected detail/current visible branch.

## Phase 5 — `DEV-conversation-recovery`

**Completed / merged / Stable for recorded Plus/personal iPhone/iOS17 scope.** PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

Final candidate: `DEV-conversation-recovery-0.1.0-b15`, `0.1.0 (15)`; run `33004536664`; artifact `9619988065`; IPA SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`.

Accepted recovery progression:

- b10: core `同步最新消息` and full `重载当前会话`.
- b12: centered sync feedback + public default-WebKit cold-start warm-up.
- b14: compact startup/list-detail navigation; initial useful root is conversation list; duplicate sidebar control removed.
- b15: selected-detail replacement lifecycle; manual recovery cancels the obsolete in-flight detail task after the new generation takes ownership, then starts one replacement request; stale-generation rejection remains.

Final b15 runtime proved two independent replacement sequences:

- generation 1 -> 2 reload: old task cancelled; replacement HTTP200 / 168 visible messages / reload success;
- generation 3 -> 4 latest-sync: old task cancelled; replacement HTTP200 / 591 visible messages / sync success;
- no HTTP429 reproduced in either accepted case.

No retry/timer/watchdog/fallback/resend/regenerate/hidden-WebView/second-state-owner machinery was added. Auth/header/cookie/endpoint semantics remain unchanged by the task-handle exposure used for cancellation.

## Phase 6 — `DEV-multi-conversation-state`

### Goal

Establish stable multi-conversation session/runtime ownership before send/stream work. See `docs/project/MULTI_CONVERSATION_STATE_PLAN.md` and the post-recovery sequencing in `CLIENT_ARCHITECTURE_GAP_REVIEW.md`.

### Scheduling

This Work is serialized before conversation metadata/preferences and production send/stream. Its owning development session maintains the exact active candidate/runtime status; planning documents do not overwrite that checkpoint.

The Work generalizes the prior single-selected freshness/request-lifecycle model into account-scoped resident per-conversation state. Do not reuse the recovery checkpoint/branch/candidate identity.

## Phase 7 — `DEV-conversation-round-count`

### User-facing scope

Implement the small conversation metadata/navigation/preferences bundle immediately after multi-conversation state and before Send/Stream:

- conversation header round count: `聊天 · N轮` / `工作 · N轮`;
- per-message timestamp display for every visible user message and visible assistant reply;
- adaptive quick navigation for `上一轮回答` / `下一轮回答`;
- the first centralized app preference owner shared by these toggles and future settings.

### Shared round derivation

Round count and answer-jump navigation must share one derived active-branch round projection instead of maintaining parallel mutable counters/indexes.

- Each authoritative visible user message starts one round.
- For navigation, the historical answer anchor for that round is the first visible assistant reply following that user message before the next user message.
- Tool/reasoning/system nodes do not independently create rounds merely because they exist in the protocol graph or UI.
- If a historical round has no visible assistant answer, it has no fabricated answer anchor.
- Recompute the lightweight derived round/answer-anchor list when the authoritative visible message projection changes (initial load, Sync, Reload, later branch change). Do not rescan the entire conversation on every scroll callback.

### Round count

- Derive from authoritative active-branch user messages.
- No second mutable counter and no extra network request.
- Existing planned `显示会话轮数` setting persists; round-count default remains On per prior confirmed planning.

### Message timestamps

- Historical/server-backed timestamp source is the message's existing authoritative `createTime` / current service `create_time`; do not issue another Detail request only to obtain time.
- User-message timestamp is subdued metadata below the user bubble, aligned with the user-message side.
- Assistant timestamp is subdued metadata below that assistant response, aligned with the assistant/document side.
- `显示消息时间` is one centralized persisted preference consumed by message presentation; individual cells/view controllers must not invent their own keys/defaults.
- Format using the device's current locale/time zone; same-day messages may use time-only while older messages include enough date context to disambiguate. Exact localized strings/spacing are implementation-level and must be validated visually on device.
- If a historical message has no authoritative `createTime`, omit its timestamp rather than fabricate one.
- The default value for `显示消息时间` is **not yet frozen by an explicit user requirement**; choose/document it when this Work starts rather than silently assuming.

### Quick previous/next answer navigation

- Setting: one centralized persisted toggle such as `显示回答快速跳转`; exact final label/default may be tuned when the Work starts, but view controllers/cells must not invent independent preference keys.
- Presentation: use one small adaptive floating control rather than two permanently visible large controls.
- Placement on compact iPhone: trailing safe-area side, approximately 12–16 pt from the right edge; bottom approximately 12–16 pt above the current composer when a composer exists, otherwise above the bottom safe area. It must move with the composer/keyboard layout rather than overlap it.
- Keep the visible control compact (roughly 36–40 pt) while preserving at least a 44 pt hit target; prefer native material/system background and SF Symbols compatible with the deployment target.
- Direction is driven by the user's most recent **actual drag direction**: browsing toward older content presents the upward/`上一轮回答` state; browsing toward newer content presents the downward/`下一轮回答` state. Programmatic animated scrolling must not feed back and flip the button direction as though it were a user drag.
- Boundary availability overrides the last direction: if only one valid adjacent answer exists, present that valid direction; if the conversation does not have a useful adjacent answer target, hide the control.
- The target is the adjacent derived answer anchor in the chosen direction, not a raw percentage/row guess and not another network load.
- Tap behavior must visibly animate the existing conversation scroll container to the target answer start using native `UIScrollView`/`UITableView` animation semantics. Do not instant-teleport by assigning a final raw offset without animation, and do not implement staged timer-driven fake scrolling.
- Land the target answer start with a modest readable top inset below the navigation area rather than burying the first line directly under the bar.
- User touch/drag remains authoritative and may interrupt a programmatic animation naturally.
- Conversation switch, Sync and Reload must use the same per-conversation presentation owner established by multi-conversation work; quick navigation must not create a second scroll-position authority or mutate another conversation's saved anchor.

### Future Send/Stream handoff

Production Send must not create a second durable timestamp authority. If optimistic local presentation needs an immediate provisional time before the service supplies authoritative message time, that provisional value belongs to the pending response/message presentation and must hand off to the authoritative server-backed message timestamp once available.

Quick answer navigation is initially defined against server-backed/current visible branch answers. When real Send/Stream exists, `DEV-send-stream` must integrate active-response/follow-tail behavior through the authoritative per-conversation response owner: navigating away from a generating answer must never Stop/cancel it merely because the user chose another historical round, and synthetic scrolling must not masquerade as user follow-tail intent.

### Acceptance focus

- Long conversations with many rounds: repeated up/down answer navigation lands on the intended adjacent answer with visible smooth movement and no extra Detail request.
- A/B multi-conversation switching: each conversation preserves its own semantic scroll anchor; using the jump control in B never changes A.
- Sync/Reload: answer anchors are re-derived from the refreshed visible branch; stale row indexes are not retained as authority.
- Toggle Off removes the control without changing round count/message data or scroll state.
- Scrolling performance remains bounded; no O(n) full-message scan on every `scrollViewDidScroll` event.

## Phase 8 — `DEV-send-stream`

After read/recovery/multi-conversation ownership and the small metadata/navigation/preferences bundle are stable: evidence current text-send/new-conversation protocol, implement composer/stream/stop, bind response identity correctly under switching, integrate manual recovery without automatic resend, and connect the answer-navigation/follow-tail behavior to the real per-conversation response owner.

**As soon as this phase reaches accepted real-device text chat/stream behavior, issue the earliest practical daily-chat Candidate. Do not wait for list-cache/persistence breadth.**

## Phase 9 — `DEV-conversation-list-cache-preview`

### Goal

Make the sidebar feel immediate on process cold start and add useful clipped message previews without causing a Detail-request storm. Durable design: `docs/project/CONVERSATION_LIST_CACHE_PLAN.md`.

### Required behavior

- After the current account/workspace scope is verified, load that scope's persistent list snapshot and render it before waiting for the normal list network response.
- Then issue exactly one normal current list refresh and incrementally reconcile returned summaries into the cache/UI.
- Current first-page absence is not deletion evidence because the list route is limited to 28 items; keep older cached rows unless complete pagination or an explicit authoritative action proves removal.
- Add one clipped secondary preview line under the title when preview data is available.
- First verify whether the current list response already supplies a usable preview field by inspecting key/type presence only; never log preview values/raw items.
- If the list response does not supply preview content, update previews only from Detail/Sync/Reload already fetched by normal user activity and later from authoritative local Send/Stream events. **Never request every Detail solely to fill previews.**
- Persist only bounded preview text + list metadata; no full Detail/raw mapping/body cache in this Work.
- Cache is account-scoped and never displayed before current scope verification.
- `ConversationRepository` remains the in-memory product authority; a disk cache store is durable snapshot storage only.
- Use the centralized preferences owner for `显示会话消息预览`; presentation changes must not trigger network requests.

### Performance / freshness semantics

- Cold start follows cache-first / stale-while-refresh presentation: cached rows first, one server list refresh second.
- Network refresh failures keep a valid cache visible and surface a non-destructive refresh error; no retry loop.
- Merge by conversation ID/update time and update changed rows rather than clearing the visible list.
- A locally cached preview may be stale if another client changed the conversation and the list endpoint does not provide preview text; do not hide that uncertainty behind automatic Detail fetches.
- Disk writes are atomic and meaningful-event based; future Streaming must not persist preview text token-by-token.

### Scheduling

This Work is deliberately **after the first accepted Send/Stream daily-chat Candidate** so persistence/performance polish does not delay basic chatting. It touches `ConversationRepository`/sidebar ownership and should not run as an unsafe parallel task against an active unmerged Send/Stream implementation.

## Phase 10 — `DEV-markdown-export`

Export authoritative current user-visible branch to Markdown; never scrape mounted cells or expose hidden/internal reasoning/tool content.

## Phase 11 — `DEV-long-conversation`

Measure/improve parse/model/render timing, first-visible latency, mounted-view bounds, memory growth, scrolling/input latency and lifecycle behavior.

## Phase 12 — `DEV-attachments`

Add native photo/file/video attachment flows after text-chat ownership is stable; evidence current upload protocol before production implementation.

## Phase 13 — remaining daily-use features

Split into isolated Work IDs as dependencies stabilize: conversation pagination/load-more, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement and other evidenced daily-use capabilities. Future pagination must reuse the same list-cache/reconciliation owner rather than introduce a second list store.

## Phase 14 — advanced capabilities

Later candidates: Projects, web search, image/multimodal, Voice, Memory, Deep Research, GPTs and other current ChatGPT-specific capabilities.

## Current next action

No development Work is automatically activated by this plan. Finish the currently active multi-conversation Work through its own checkpoint/runtime gate. After it is Stable/merged, the serialized core remains:

`DEV-conversation-round-count -> DEV-send-stream -> earliest daily-chat Candidate -> DEV-conversation-list-cache-preview`

The list-cache/preview Work then improves cold-start/sidebar performance before broader daily-use refinements.
