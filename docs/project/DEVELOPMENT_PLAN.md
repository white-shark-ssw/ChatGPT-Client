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
10. High-frequency daily operations such as image/file transfer and one-tap Copy move ahead of lower-frequency polish once the authoritative Send/Stream owner exists.

## Usability milestones

- **V0.1 read-use**: native shell + conversation list/detail/message rendering + manual sync/full reload + usable cold-start login-state recovery.
- **V0.2 chat-use**: V0.1 + stable multi-conversation state ownership + conversation metadata/preferences + basic one-tap message Copy + long-conversation answer navigation + text send/new conversation + streaming + stop + user-visible reasoning interaction/haptics + recovery integration.
- **V0.2 attachment-use increment**: accepted V0.2 text chat + image/file sending + assistant-file tap-download-share.
- **V0.3 daily-use refinement**: Markdown/code rendering with scoped Copy, instant cache-backed conversation-list startup + clipped list previews, Markdown export, long-conversation tuning, download-manager/pagination/search and remaining daily-use features.

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

Implement the small conversation metadata/navigation/preferences/basic-message-actions bundle immediately after multi-conversation state and before Send/Stream:

- conversation header round count: `聊天 · N轮` / `工作 · N轮`;
- per-message timestamp display for every visible user message and visible assistant reply;
- adaptive quick navigation for `上一轮回答` / `下一轮回答`;
- **basic one-tap Copy for visible user and assistant message text**;
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
- Format using the device's current locale/time zone; same-day messages may use time-only while older messages include enough date context to disambiguate.
- If a historical message has no authoritative `createTime`, omit its timestamp rather than fabricate one.
- The default value for `显示消息时间` is not yet frozen by an explicit user requirement; choose/document it when this Work starts rather than silently assuming.

### Basic one-tap Copy

- Provide an official-style compact Copy action for visible user and assistant textual messages.
- Copy current user-visible message text through the system pasteboard; never include hidden reasoning/tool/system material.
- Copy is a local presentation action: no network request, no message-state mutation and no separate content authority.
- Provide immediate compact feedback after a successful Copy.
- Future Markdown/code rendering adds content-scoped Copy controls such as one-tap code-block Copy without removing the basic message-level action.

### Quick previous/next answer navigation

- Setting: one centralized persisted toggle such as `显示回答快速跳转`; exact final label/default may be tuned when the Work starts, but view controllers/cells must not invent independent preference keys.
- Presentation: use one small adaptive floating control rather than two permanently visible large controls.
- Placement on compact iPhone: trailing safe-area side, approximately 12–16 pt from the right edge; bottom approximately 12–16 pt above the current composer when a composer exists, otherwise above the bottom safe area. It must move with the composer/keyboard layout rather than overlap it.
- Keep the visible control compact while preserving at least a 44 pt hit target; prefer native material/system background and iOS14-compatible SF Symbols.
- Direction is driven by the user's most recent actual drag direction; programmatic animated scrolling must not feed back and flip direction as though it were a user drag.
- Boundary availability overrides the last direction; hide the control if no useful adjacent answer exists.
- The target is the adjacent derived answer anchor in the chosen direction, not a raw percentage/row guess and not another network load.
- Tap behavior must visibly animate the existing conversation scroll container to the target answer start using native `UIScrollView`/`UITableView` animation semantics; do not instant-teleport or fake scrolling with timers.
- Conversation switch, Sync and Reload must use the same per-conversation presentation owner established by multi-conversation work.

### Future Send/Stream handoff

Production Send must not create a second durable timestamp authority. If optimistic local presentation needs an immediate provisional time before the service supplies authoritative message time, that provisional value belongs to the pending response/message presentation and hands off to authoritative server-backed time once available.

Quick answer navigation is initially defined against server-backed/current visible branch answers. When real Send/Stream exists, `DEV-send-stream` integrates active-response/follow-tail behavior through the authoritative per-conversation response owner: navigating away from a generating answer must never Stop/cancel it merely because the user chose another historical round.

### Acceptance focus

- Long conversations: repeated up/down answer navigation lands on the intended adjacent answer with visible smooth movement and no extra Detail request.
- A/B switching preserves independent semantic scroll anchors.
- Sync/Reload re-derives answer anchors.
- Toggle Off removes the control without changing message data or scroll state.
- Scrolling performance remains bounded; no O(n) full-message scan on every scroll callback.
- One-tap Copy works for both user and assistant visible text and excludes hidden material.

## Phase 8 — `DEV-send-stream`

After read/recovery/multi-conversation ownership and the metadata/navigation/preferences bundle are stable: evidence current text-send/new-conversation/stream/stop protocol, implement composer/stream/stop, bind response identity correctly under switching, integrate manual recovery without automatic resend, and connect answer-navigation/follow-tail behavior to the real per-conversation response owner.

**As soon as this phase reaches accepted real-device text chat/stream behavior, issue the earliest practical daily-chat Candidate. Do not wait for attachment/cache/persistence breadth.**

## Phase 9 — `DEV-attachments`

### Priority / durable design

Image/file sending and assistant-file download/share are explicitly high-frequency user operations and are promoted to the first major capability immediately after accepted text Send/Stream. Durable design: `docs/project/ATTACHMENT_TRANSFER_PLAN.md`.

### Core first Candidate

- evidence current upload/message-attachment protocol before production code;
- select/send images through native iOS photo-picker behavior;
- select/send generic files/documents through the system document picker;
- show pending attachment thumbnails/cards in the owning conversation composer and allow removal before Send;
- bind uploaded assets to the exact pending message/conversation owner from `DEV-send-stream`;
- parse/render evidenced user-visible assistant file attachments;
- tap assistant file card -> explicit download -> app-private temporary/cache file -> immediately present `UIActivityViewController` for Save to Files/AirDrop/other system share actions;
- visible transfer failure/cancel state; no automatic retry/watchdog loop;
- use file-backed download semantics where appropriate rather than retaining large files fully in memory;
- no persistent auth-secret store and no sensitive URL/file-content diagnostics.

A full custom download-management UI does **not** block this phase.

## Phase 10 — `DEV-message-rendering`

Improve development-chat readability after the high-frequency transfer path is usable:

- Markdown paragraphs/headings/lists/links;
- inline/fenced code;
- dedicated one-tap Copy on code blocks/content surfaces where semantics are clear;
- tables when current content requires them;
- preserve basic message-level Copy;
- do not broad-reparse/reload the whole conversation on every streamed token.

## Phase 11 — `DEV-conversation-list-cache-preview`

### Goal

Make the sidebar feel immediate on process cold start and add useful clipped message previews without causing a Detail-request storm. Durable design: `docs/project/CONVERSATION_LIST_CACHE_PLAN.md`.

### Required behavior

- after current account/workspace scope verification, load that scope's persistent list snapshot and render it before waiting for the normal list network response;
- issue exactly one normal current list refresh and incrementally reconcile returned summaries;
- current first-page absence is not deletion evidence because the list route is limited to 28 items;
- add one clipped secondary preview line under the title when preview data is available;
- first verify whether the current list response already supplies a usable preview field by key/type presence only;
- if not, update previews only from Detail/Sync/Reload already fetched by normal user activity and from authoritative local Send/Stream events; never request every Detail solely to fill previews;
- persist only bounded preview text + list metadata; no full Detail/raw mapping/body cache;
- cache is account-scoped and never displayed before current scope verification;
- use the centralized preferences owner for `显示会话消息预览`.

### Performance / freshness semantics

- cold start uses cache-first / stale-while-refresh presentation;
- network refresh failure keeps valid cache visible and surfaces a non-destructive refresh error; no retry loop;
- merge by conversation ID/update time and update changed rows rather than clearing the visible list;
- future Streaming must not persist preview text token-by-token.

## Phase 12 — `DEV-markdown-export`

Export authoritative current user-visible branch to Markdown; never scrape mounted cells or expose hidden/internal reasoning/tool content.

## Phase 13 — `DEV-long-conversation`

Measure/improve parse/model/render timing, first-visible latency, mounted-view bounds, memory growth, scrolling/input latency and lifecycle behavior.

## Phase 14 — remaining daily-use features

Split into isolated Work IDs as dependencies stabilize:

- `DEV-download-manager` — persistent download history/progress/re-share/storage controls, intentionally lower priority than core tap-download-share;
- conversation pagination/load-more;
- background wait/completion notification and later TrollStore true-background experiment according to `BACKGROUND_EXECUTION_PLAN.md`;
- search;
- rename/archive/delete;
- edit/regenerate/branch switching;
- model selection/temporary chat;
- settings/diagnostics refinement and other evidenced daily-use capabilities.

Future pagination must reuse the same list-cache/reconciliation owner rather than introduce a second list store.

## Phase 15 — advanced capabilities

Later candidates: Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other current ChatGPT-specific capabilities.

## Current next action

No development Work is automatically activated by this plan. Finish the currently active multi-conversation Work through its own checkpoint/runtime gate. After it is Stable/merged, the serialized near-term route is:

`DEV-conversation-round-count (metadata/settings + basic Copy) -> DEV-send-stream -> earliest daily-chat Candidate -> DEV-attachments -> DEV-message-rendering -> DEV-conversation-list-cache-preview`

This ordering intentionally gets text chat usable first, then raises high-frequency image/file transfer and copy-rich development use ahead of lower-priority download management and broader polish.
