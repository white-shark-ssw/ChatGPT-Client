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
- **V0.2 chat-use**: V0.1 + stable multi-conversation state ownership + conversation metadata/preferences + text send/new conversation + streaming + stop + user-visible reasoning interaction/haptics + recovery integration.
- **V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments and remaining daily-use conversation features.

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

Implement the small conversation metadata/preferences bundle immediately after multi-conversation state and before Send/Stream:

- conversation header round count: `聊天 · N轮` / `工作 · N轮`;
- per-message timestamp display for every visible user message and visible assistant reply;
- the first centralized app preference owner shared by both toggles and future settings.

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

### Future Send/Stream handoff

Production Send must not create a second durable timestamp authority. If optimistic local presentation needs an immediate provisional time before the service supplies authoritative message time, that provisional value belongs to the pending response/message presentation and must hand off to the authoritative server-backed message timestamp once available.

## Phase 8 — `DEV-send-stream`

After read/recovery/multi-conversation ownership and the small metadata/preferences bundle are stable: evidence current text-send/new-conversation protocol, implement composer/stream/stop, bind response identity correctly under switching, and integrate manual recovery without automatic resend.

## Phase 9 — `DEV-markdown-export`

Export authoritative current user-visible branch to Markdown; never scrape mounted cells or expose hidden/internal reasoning/tool content.

## Phase 10 — `DEV-long-conversation`

Measure/improve parse/model/render timing, first-visible latency, mounted-view bounds, memory growth, scrolling/input latency and lifecycle behavior.

## Phase 11 — `DEV-attachments`

Add native photo/file/video attachment flows after text-chat ownership is stable; evidence current upload protocol before production implementation.

## Phase 12 — remaining daily-use features

Split into isolated Work IDs as dependencies stabilize: search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement and other evidenced daily-use capabilities.

## Phase 13 — advanced capabilities

Later candidates: Projects, web search, image/multimodal, Voice, Memory, Deep Research, GPTs and other current ChatGPT-specific capabilities.

## Current next action

No development Work is automatically activated by this plan. Finish the currently active multi-conversation Work through its own checkpoint/runtime gate. After it is Stable/merged, the next serialized Work is `DEV-conversation-round-count` with the expanded scope above: round count + message timestamps + first centralized preference owner; then proceed directly to `DEV-send-stream`.
