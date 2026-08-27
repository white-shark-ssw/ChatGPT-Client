# Client Architecture Gap Review

_Last reviewed: 2026-08-27; refreshed after exact b18 historical-scroll real-device acceptance._

## Purpose

Focused pre-Send/Stream architecture review for the native TrollStore ChatGPT client. It exists to prevent state/concurrency mistakes once multiple conversations, streaming, background execution and long conversations coexist.

Product rule: **reach a usable daily-chat candidate early; only P0 structural invariants may block the first production Send/Stream path.**

## Current evidence baseline

- `DEV-conversation-recovery-0.1.0-b15` is merged Stable for recorded Plus/personal iPhone/iOS17 recovery scope.
- `DEV-multi-conversation-state` remains Active on `dev/multi-conversation-state-20260827`.
- b16 is historical/rejected before runtime and must not be reused.
- b17 exact source `bc69d58b3245...` has accepted core iPhone/iOS17 Runtime evidence for resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid different-conversation overlap. It reproduced the historical-scroll defect.
- Exact b18 product/config source is `f30c13b4ac2c40dcda829585682825ca906dceae`, tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`; Run `33054012226` / Job `98456174184` succeeded; Artifact `9638821912` is identity-valid; IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.
- b18 changes only historical per-conversation scroll presentation metadata in `ConversationDetailViewController`; `ConversationRepository`, account/protocol ownership and network routes are unchanged.
- Exact b18 iPhone/iOS17 Runtime now accepts the tested historical-scroll matrix: independent A/B anchors, first-time target isolation, visible Sync/Reload anchor preservation when the anchored message remains, resident return and active same-target Sync coalescing. The user reported no issue.
- b18 export: 195 events, all `info`; 21 anchor saves, 19 restores, 17 resident hits/first-visible events; all 17 recorded HTTP statuses are 200; no error, HTTP429 or anchor discard.
- Missing-anchor-message discard did not occur naturally and remains source/CI-defined rather than device-proven.
- Current `main@2c33dacbefa613292eb89cbf606b0172a241e81e` advanced after b18 Artifact through docs-only message-timestamp planning. This does not invalidate exact b18 product/runtime evidence; synchronize before final merge.
- There is still no XCTest/UI-test target.

Cold-start login-state recovery belongs to completed recovery baseline. Do not create a separate `DEV-auth-resume` task. Default persistent WebKit storage remains sole persistent auth-secret authority.

## Priority classification

### P0 — required before production Send/Stream becomes authoritative

1. Per-conversation resident state instead of one loaded-detail slot.
2. Async operation freshness / stale-result protection with deterministic consumer termination.
3. Retain minimum authoritative conversation/node identity required by current evidence.
4. Scope resident/draft/response state to verified account/workspace context and purge/reject on context change.
5. Define new-conversation identity handoff from local pending UI to authoritative server identity.
6. Own responses per conversation/message identity instead of a global streaming flag.
7. Define Sync/Reload ownership transitions when target conversation has an active response.

b17 addresses the evidenced pre-Send owner/race/account-scope portion of 1–4 and has direct Runtime evidence for tested navigation/coalescing/hidden-Sync paths. b18 does not alter those owners and adds Runtime-accepted presentation isolation for historical scroll. Items 5–7 require current Send/Stream protocol evidence and must not be guessed.

### P1 — around first daily-chat candidates

1. Basic Markdown/code-block rendering.
2. Conversation-list pagination/load-more beyond first 28 items.
3. Per-conversation draft and semantic scroll presentation state.
4. Hidden-conversation generating/completed status after streaming exists.
5. One centralized app-settings preference owner.
6. Background continuation over an active response set, not global Boolean.
7. Large-conversation phase timing: network / parse-model / first-visible-render.

Historical-reading anchor restoration is now Runtime accepted on exact b18 for the tested matrix. Active-response `follow-tail` remains future Send/Stream integration because response activity must come from authoritative response ownership.

### P2 — after daily-chat loop is stable

1. Optional cross-process state restoration beyond normal WebKit auth persistence.
2. Persistent chat-body/disk cache only after explicit privacy/storage requirement.
3. Advanced edit/regenerate/branch cache optimization.
4. Advanced unread/history synchronization with other clients.
5. Broad lower-iOS/iPad optimization after exact Runtime evidence.

## P0 invariants

### Per-conversation residency

Foreground selection is presentation state only.

`verified account/workspace context + conversation ID -> resident conversation state`

Selecting B must not destroy A, cancel A merely because it becomes hidden, or force A to reload on return. Use one production conversation authority with per-conversation entries; do not create one repository per screen and do not keep full UIKit hierarchies alive as data cache.

### Single state-owner execution domain

Resident dictionaries, list state, operation generations/tasks, account-scope binding and transient-session ownership read/mutate through one explicit repository execution domain. Network transfer and pure parsing may occur off-owner. Thread safety must fix owner invariant, not create a second store.

### Async freshness / race protection

Every operation binds account/context + target conversation + generation/token.

- Same-target replacement cancels older target task before replacement request ownership proceeds, preserving b15 behavior.
- Equivalent same-target loads may coalesce.
- Superseded/account-invalidated waiters terminate deterministically.
- Presentation has target/freshness identity so obsolete completion cannot mutate wrong conversation.
- No timer/retry/watchdog/fallback machinery.

b17 Runtime directly confirms same-target coalescing and A Sync rejoin. b18 also re-confirms coalescing when returning to B while B Sync is active.

### Account/workspace isolation

`AuthSessionStore` remains account authority. Repository operation/transport contexts are consumers, not account authorities.

A newly verified different context must invalidate old transient session, purge old list/resident/draft/response state, cancel/invalidate old operations and resolve waiters, reject late old-scope callbacks, never allow stale transport to re-adopt old scope, and never display old-account content under new context.

Current source keys personal scope with `userID + accountID`; supported account-switch Runtime proof and non-personal workspace identity remain open.

### Preserve authoritative node identity

Visible message array is a projection, not complete authoritative conversation representation. Current Detail evidence supplies `current_node`, so branch-tip identity is retained. Do not retain raw multi-megabyte Detail JSON or invent future graph fields before Send evidence.

### New-conversation identity handoff

Send protocol evidence must establish conversation identity creation, parent/current-node requirements, message/request/response lifecycle, and when a new conversation can safely enter list/resident state. Temporary local identity, if required, gets one explicit handoff to authoritative identity; temporary and server identities must not remain independent owners.

### Per-conversation response ownership

Future response ownership is conceptually:

`conversation identity + response/message identity -> response lifecycle`

A may continue generating while B is visible. Navigation never calls Stop just because A becomes hidden. Initial rule: at most one active response per conversation unless current protocol/runtime proves overlap; Stop targets one exact response/conversation, never global `isStreaming`.

### Sync/Reload while response active

`同步最新消息` targets one conversation and never resends. `重载当前会话` rebuilds one conversation only. Exact interaction with active future response follows current Send/Stream evidence and is not guessed pre-Send.

## P1 implementation notes

### Per-conversation UI state

Within the live process preserve lightweight semantic scroll presentation, later composer draft, and useful reasoning-detail expansion state. Avoid raw pixel-only restoration for growing long conversations.

Two scroll modes are user-confirmed:

1. **Historical-reading anchor** — preserve message identity + relative visual offset; A->B->A restores A's own anchor and B scrolling does not move A.
2. **Follow-tail** — if the user leaves A at/near bottom while authoritative A response is active, hidden growth/completion keeps A attached to newest tail; returning A shows current latest bottom, not old pre-growth anchor.

Intentional upward scroll while A generates exits follow-tail and establishes historical-reading intent.

Exact b18 implements and Runtime-validates the historical-reading mode for the tested iPhone/iOS17 paths. It tracks actually displayed conversation separately from repository selection, captures top visible message identity + relative offset, restores after rows reload, resets no-anchor target to top, clears anchors on account reset, and preserves through visible Sync/Reload only when the same anchor message remains.

The anchored-message-disappears branch was not naturally triggered on device; `scrollAnchor.discarded -> top` remains source/CI-defined and must not be reported as Runtime-proven.

Follow-tail eligibility/transition must consume future authoritative Send/Stream response lifecycle; b18 adds no UI streaming authority.

### Conversation pagination / Markdown / settings / background

- Current accepted list call returns first page `offset=0&limit=28&order=updated`; pagination must use current service evidence and never clear resident detail solely because list page/order changes.
- Markdown/code rendering should prioritize development-chat usefulness without broad reparse/reload on every streamed token.
- First real preference toggle should establish one centralized app preference owner; view controllers consume it rather than inventing independent keys/defaults.
- Background protection is over an active response set, not a global Boolean.

## Additional correctness constraints

- `同步最新消息` remains explicit reconciliation; list `update_time` must not silently become automatic reload policy.
- UI `聊天` / `工作` derivation remains Unverified unless current service evidence supplies authoritative identity.
- In-memory residency/presentation may disappear after process termination; do not add persistent chat-body cache solely to hide relaunch cost.
- Keep network/rate-limit failures observable. No reachability resend, speculative retry chain or global concurrency limiter without evidence.

## Testing gap

No test target today. Add only smallest deterministic support when state logic justifies project-file churn.

Real-device evidence remains mandatory for WebKit auth, real networking, HTTP429 behavior, UI switching, memory behavior, background execution and TrollStore mechanisms.

## Current serialized development state

1. `DEV-conversation-recovery` — Completed / merged / Stable b15.
2. `DEV-multi-conversation-state` — Active; b17 core Runtime and b18 historical-scroll Runtime accepted for tested scope; remaining owner/memory gates below.
3. Current durable roadmap is `DEVELOPMENT_PLAN.md`; current `main` includes message-timestamp/display-preference planning that must be preserved during final synchronization.
4. `DEV-send-stream` remains the stage where real response ownership/follow-tail can be implemented and tested.

## Current multi-conversation Runtime gate

Accepted on b17:

- loaded A -> B -> A without navigation-only A Detail refetch;
- hidden completion retained;
- same-target in-flight return coalesces;
- Sync A -> B -> A remains attached to same Sync;
- rapid A/B/C overlap without HTTP429 in supplied export.

Accepted on exact b18:

- A historical position -> B scroll -> A restores same practical semantic/visual anchor;
- A and B maintain independent anchors over repeated switching;
- first-time third target does not inherit previous conversation offset;
- visible Sync preserves the historical anchor when the anchored message remains;
- Reload preserves the historical anchor when the anchored message remains;
- active B Sync survives B->A->B and re-coalesces onto the same operation;
- resident returns continue without navigation-only refetch;
- no issue reported by user; export contains only info-level events, HTTP200 statuses, no HTTP429/error.

Still open before full Work Stable acceptance:

- isolated same-target Reload replacement while an older Detail is actually in flight;
- failed resident navigation with no implicit retry when a natural terminal failure is available;
- supported account-scope Runtime isolation when a real switch/logout route exists;
- real process/system memory evidence sufficient to choose a bounded normal LRU policy;
- non-personal workspace isolation remains Unknown / Unverified.

Future Send/Stream adds separate scroll gate: A active at bottom -> B -> A grows/completes hidden -> return A at current latest bottom; A active -> user scrolls upward -> B -> return A at preserved historical anchor.

## Next exact action

Do not change product code yet. Collect real iPhone process/system memory evidence while several small and large conversations remain resident and are repeatedly switched. Use that evidence, not approximate visible-text bytes, to decide whether a normal bounded LRU policy is needed now and what capacity is defensible.

Before final PR/merge, synchronize with current `main@2c33dacbefa613292eb89cbf606b0172a241e81e` without overwriting its message-timestamp planning, then rerun only validation materially affected by synchronized product source.
