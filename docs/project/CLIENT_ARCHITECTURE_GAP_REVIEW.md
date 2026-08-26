# Client Architecture Gap Review

_Last reviewed: 2026-08-27._

## Purpose

This is the focused pre-send/stream architecture review for the native TrollStore ChatGPT client. It exists to prevent a small number of state/concurrency mistakes that would otherwise force expensive rework once multiple conversations, streaming, background execution and long conversations are active together.

The product rule remains: **reach a usable daily-chat candidate as early as possible; only P0 structural invariants may block the first production send/stream path.**

## Latest ownership correction — cold-start authentication

The user's latest explicit requirement supersedes the earlier plan that proposed a separate `DEV-auth-resume` Work.

**Cold-start login-state recovery is part of the active `DEV-conversation-recovery` work. Do not create a second `DEV-auth-resume` task.**

Required order inside that recovery work:

1. verify/warm the default `WKWebsiteDataStore` in the background/invisibly first;
2. perform the normal account/session verification through the accepted auth owner;
3. if background verification cannot recover the usable WebKit state, preserve the exact failure evidence and only then move to the smallest visible foreground verification flow;
4. keep default WebKit storage as the sole persistent auth-secret authority;
5. no hidden/shadow login WebView, copied-token persistence, retry/watchdog loop or second auth store.

The active recovery development session owns its own checkpoint/branch/PR and must update those records itself. Rules/planning sessions must not edit that development checkpoint.

## Current evidence baseline

- `DEV-native-read-path-0.1.0-b9` is the accepted production read baseline for the tested iPhone / iOS 17.0 scope.
- `ConversationRepository` is the production conversation owner.
- Current merged read source still uses one foreground `selectedConversationID` and one loaded `selectedConversation` slot.
- Current detail parsing walks `mapping` from `current_node`, builds the visible branch, then keeps a simplified message projection; the authoritative current-node/graph identity required by future send/branch work is not yet retained as a resident model.
- Current list transport uses `offset=0&limit=28&order=updated`; accepted runs already showed `total` can exceed the returned page.
- `SettingsViewController` has build/diagnostic controls but no centralized preference owner for the planned feature toggles.
- There is no XCTest/UI-test target yet.
- Active PR #10 owns recovery product code and overlapping `DEVELOPMENT_PLAN.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `BUILD_TEST_INDEX.md`; this planning work deliberately does not modify those surfaces while PR #10 is active.

## Priority classification

### P0 — required before production send/stream becomes authoritative

After the cold-start auth work is folded into recovery, the remaining P0 items are:

1. **Per-conversation resident state instead of one loaded-detail slot.**
2. **Async operation freshness / stale-result protection.**
3. **Retain the minimum authoritative conversation/node identity required by the current send protocol.**
4. **Scope resident/draft/response state to verified account/workspace context and purge on logout/account change.**
5. **Define the new-conversation identity handoff from local pending UI to authoritative server identity.**
6. **Own responses per conversation/message identity instead of a global streaming flag.**
7. **Define Sync/Reload ownership transitions when the target conversation has an active response.**

### P1 — around the first daily-chat candidates; do not block first send proof

1. Basic Markdown/code-block rendering.
2. Conversation-list pagination/load-more beyond the first 28 items.
3. Per-conversation draft and scroll-anchor restoration while the process remains alive.
4. Hidden-conversation generating/completed status in the sidebar after streaming exists.
5. One centralized app-settings preference owner.
6. Background continuation over an active response **set**, not a global Boolean.
7. Large-conversation phase timing: network / parse-model / first-visible-render.

### P2 — after the daily-chat loop is stable

1. Optional cross-process state restoration beyond normal WebKit auth persistence.
2. Persistent chat-body/disk cache only after an explicit privacy/storage requirement.
3. Advanced edit/regenerate/branch cache optimization.
4. Advanced unread/history synchronization with other clients.
5. Broad lower-iOS/iPad optimization after exact runtime evidence.

## P0 invariants

### Per-conversation residency

Foreground selection is presentation state only.

Conceptually:

`verified account/workspace context + conversation ID -> resident conversation state`

Selecting B must not destroy A, cancel A's owned request/response, or force A to reload when returning to it.

Use one production conversation authority with per-conversation entries. Do not create one authoritative repository per screen and do not keep full UIKit view hierarchies alive as the cache.

### Async freshness / race protection

Selection change alone must no longer discard a valid result, but an **obsolete** operation still must not overwrite a newer authoritative state.

Examples that require deterministic protection:

- ordinary load A starts, then Reload A starts;
- Sync A starts while A is progressing locally;
- Stop/terminal state occurs, then a late stream callback arrives;
- account context changes while an old request is in flight.

Every operation must be bound to its account/context + target conversation identity. A per-conversation generation/token or equivalent single-owner freshness guard may reject obsolete completions. This guard is not a second state authority and must not become a timer/retry system.

Equivalent missing-detail requests should be coalesced when the repository can do so cleanly.

### Preserve authoritative node identity

The visible message array is a projection, not the complete authoritative conversation representation.

Before production Send is implemented, the send-protocol evidence must establish the exact identities required, such as current-node/parent/message/request IDs. The resident model then keeps only that **minimum evidence-backed identity**.

Do not throw away an identity already present in Detail and re-fetch merely to recover it. Do not retain multi-megabyte raw HTTP JSON just for convenience.

### Account/workspace isolation

Resident conversations, drafts, local response owners and presentation status belong to a verified account/workspace scope.

Explicit logout/account switch must:

- invalidate the old transient native session;
- purge old-account resident/draft/response state;
- reject late callbacks from the old context;
- never display old-account content under the newly verified account.

### New-conversation identity handoff

The Send protocol probe must prove:

- whether conversation identity is client-generated or returned/established by the service;
- parent/current-node requirements;
- message/request/response identity lifecycle;
- when the new conversation is safe to insert into list/resident state.

If a temporary local presentation identity is needed, it gets **one explicit handoff** to the authoritative conversation identity. Temporary and server identities must never remain independent state owners. Rapid double-send must not produce duplicate conversations/messages while handoff is unresolved.

### Per-conversation response ownership

Required conceptual ownership:

`conversation identity + response/message identity -> response lifecycle`

A may continue reasoning/streaming while B is visible. UI navigation never calls Stop merely because A becomes hidden.

Initial product rule:

- at most one active response per conversation unless current protocol/runtime evidence proves same-conversation overlap;
- different conversations are architecturally independent;
- whether A and B can actually maintain simultaneous server streams remains **Unknown / Unverified** until real-device Send/Stream testing;
- Stop targets one exact response/conversation, never a global `isStreaming` state.

### Sync/Reload while a response is active

`同步最新消息` targets one conversation, never resends, and reconciles server state without regressing newer local authoritative progress. If server evidence proves completion, the stale local response can become server-backed terminal and obsolete callbacks must lose mutation authority.

`重载当前会话` is stronger and user-explicit. It rebuilds one conversation only and must establish a clear owner transition so an old response callback cannot later resurrect/overwrite the reloaded state. Exact cancel/detach behavior follows current send/stream evidence; it is not guessed in advance.

## P1 implementation notes

### `DEV-message-rendering` — Markdown 与代码块渲染

Prioritize development-chat usefulness:

- paragraphs/headings/lists;
- inline/fenced code;
- code-copy;
- links;
- tables when current content requires them;
- clean text selection/copy where UIKit permits.

Do not broad-reload/reparse the whole conversation on each streamed token.

### `DEV-conversation-pagination` — 会话列表加载更多

Once repository ownership is stable:

- use current protocol evidence for offset/cursor behavior;
- deduplicate by authoritative conversation ID;
- list refresh/reordering never clears resident detail merely because list position changes;
- Search remains separate.

### Per-conversation UI state

Within the live process preserve lightweight state such as semantic scroll anchor, unsent composer draft after the composer exists, and reasoning-detail expanded state where useful. Avoid raw pixel-only restoration for long conversations that grow.

Do not persist drafts/chat bodies to disk without a separate privacy/storage decision.

### Hidden-conversation response status

After Send/Stream exists, the sidebar may derive:

- thinking/generating status for a hidden active response;
- completed/unseen marker after a hidden response reaches final;
- marker clear when viewed according to accepted UI behavior.

This is presentation state derived from the response owner, not a second response authority and not a claim about an OpenAI unread API.

### Central settings owner

The first real preference toggle should establish one small app preference owner around `UserDefaults`/system state. Planned consumers include:

- `显示会话轮数`;
- `后台等待回答完成`;
- `回答完成时通知`;
- `TrollStore 真后台（实验）`;
- later appearance/diagnostic options.

View controllers consume settings; they do not independently invent keys/defaults.

### Multi-response background semantics

Background protection is over an active protected-response set.

If A and B are active when the App backgrounds, A finishing must not release protection while B remains active. Completion notification is deduplicated per response lifecycle. The final protected response leaving the set releases the public background assertion or accepted TrollStore preservation state.

### Long-conversation timing

Before major performance rewrites, instrument safe phase timing for:

- response bytes/network completion;
- JSON parse + branch/model construction;
- first visible message presentation;
- Markdown/layout when it becomes relevant.

The existing 20.74 s large-detail observation is end-to-end only and does not identify the bottleneck.

## Additional correctness constraints

### Resident freshness

A resident conversation can change on another client. A newer list `update_time` may later be used as a stale hint, but must not silently trigger a reload without a later accepted product rule. `同步最新消息` remains the explicit reconciliation action.

### `聊天` / `工作` derivation

The UI requirement is confirmed, but the current service field that authoritatively distinguishes these modes remains Unverified. Do not infer it from title/UI text. Capture the actual current service context before dynamic type display becomes authoritative.

### Process death

In-memory residency may disappear after iOS process termination/force quit. This is acceptable for the early client. Do not introduce persistent chat-body caching solely to hide relaunch cost.

### Network/rate-limit failures

Keep explicit failures observable. No reachability-driven resend, duplicate stream after network transition, or speculative retry chain. Manual Sync/Reload remains the accepted recovery path unless new evidence justifies something else.

## Testing gap

There is no test target today. Add only the smallest deterministic test support when the state logic justifies it.

High-value pure tests include:

- current-branch/node normalization;
- resident lookup/LRU eligibility and protected-response eviction rules;
- stale-operation generation rejection;
- account-scope purge;
- round-count derivation;
- response lifecycle terminal transitions;
- actual stream parser once the event format is evidenced;
- Markdown export transformation later.

Real-device evidence remains mandatory for WebKit auth, real networking, haptics, memory behavior, background execution and TrollStore-specific mechanisms.

## Post-recovery development sequence

This is the current sequence after applying the user's latest ownership correction. It supersedes older planning text that listed a separate `DEV-auth-resume` task.

0. **`DEV-conversation-recovery` — 会话同步与重载 + 冷启动后台登录态验证**
   - Current active task/PR #10.
   - Finish Sync/Reload feedback and cold-start background WebKit verification; visible foreground verification only after background failure evidence.
   - This task owns its own final candidate/runtime/merge records.

1. **`DEV-multi-conversation-state` — 多会话驻留与快速切换**
   - Convert the repository from one loaded slot to account-scoped per-conversation resident entries.
   - Add stale-operation/freshness guards and request coalescing where appropriate.
   - Retain the minimum authoritative current-node/message identity needed for upcoming Send work without retaining raw payloads.
   - Preserve semantic scroll state; prepare per-conversation draft/response linkage.
   - Measure a bounded LRU working set on real device; active responses are protected from ordinary eviction.
   - Add the first small deterministic XCTest coverage here if it can be isolated without delaying the candidate.

2. **`DEV-conversation-round-count` — 会话轮数显示 + 首个统一设置 owner**
   - `聊天 · N轮` / `工作 · N轮`, derived from active-branch user turns.
   - Default display On; setting persists.
   - Establish the small centralized preference owner if one does not yet exist.
   - No extra network request and no mutable round counter.

3. **`DEV-send-stream` — 消息发送、流式回复与推理交互**
   - First capture current Send/new-conversation/stream/stop protocol evidence.
   - Define the pending-to-authoritative new-conversation identity handoff.
   - Own each response by conversation/message identity; no global stream owner.
   - Incrementally update only the affected assistant/reasoning presentation.
   - Implement official-style gray shimmer reasoning, tap expand/collapse of explicit user-visible detail, completed `思考了 Xs` when evidenced, and the two-pulse reasoning-to-final haptic.
   - Integrate Sync/Reload ownership transitions for stalled/abandoned streams.
   - Test A generating -> view B -> return A, and test simultaneous A/B streams only if the current service permits them.
   - **As soon as this loop works on device, issue the earliest practical daily-chat Candidate. Do not wait for P1 breadth.**

4. **`DEV-message-rendering` — Markdown 与代码块渲染**
   - Improve actual development-chat readability immediately after the first Send/Stream loop.

5. **`DEV-conversation-pagination` — 会话列表加载更多**
   - Remove the current first-page/28-item practical limitation without disturbing resident identity/state.

6. **`DEV-background-notify` — 后台等待与完成通知**
   - Continue the existing response owner using normal iOS background-task time.
   - Support an active protected-response set.
   - Local `回答已完成` notification once per completed response lifecycle.
   - Expiration never resends; foreground uses Sync when reconciliation is required.

7. **`DEV-trollstore-true-background` — TrollStore 真后台实验**
   - Only after the normal background path is measurable.
   - Response-scoped, minimal privilege, no auth/chat secrets in a privileged helper.
   - 5/15/30/60-minute runs are validation targets, not promises.

8. **`DEV-markdown-export` — Markdown 会话导出**
   - Export the authoritative current user-visible branch, not mounted cells.

9. **`DEV-long-conversation` — 超长会话性能优化**
   - Use phase timing and real large conversations to optimize only proven bottlenecks.

10. **`DEV-attachments` — 附件上传与文件处理**
    - After text-chat ownership is stable; evidence current upload protocol first.

11. **Daily-use conversation features**
    - Search, rename/archive/delete, Edit/Regenerate/branch switching, model/temporary chat, settings/diagnostics refinement.

12. **Advanced capabilities**
    - Projects, Web Search, image/multimodal, Voice, Memory, Deep Research, GPTs and other current capabilities, each with current protocol/UI evidence.

### Parallelization after Send/Stream

The serialized core remains:

`recovery -> multi-conversation state -> round-count/preferences -> send/stream`

After the Send/Stream owner is merged/stable, `message-rendering`, `pagination`, and some settings/UI edges may run in parallel only after the normal branch/file/state-owner conflict scan. `background-notify` depends on the accepted response lifecycle and must not be implemented against an unmerged/unstable duplicate response owner.

## Acceptance mindset

Continue shipping small TrollStore candidates. A planning item blocks the next candidate only when it protects a core invariant that would otherwise make that candidate unsafe or cause immediate rework.

Do not wait for this whole document to be implemented before using the App.
