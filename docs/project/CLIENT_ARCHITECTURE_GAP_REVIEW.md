# Client Architecture Gap Review

_Last reviewed: 2026-08-27; refreshed through b20 title Runtime evidence and exact b21 Artifact._

## Purpose

Focused pre-Send/Stream architecture review for the native TrollStore ChatGPT client. It exists to prevent state/concurrency mistakes once multiple conversations, streaming, background execution and long conversations coexist.

Product rule: **reach a usable daily-chat candidate early; only P0 structural invariants may block the first production Send/Stream path.**

## Current evidence baseline

- `DEV-conversation-recovery-0.1.0-b15` is merged Stable for recorded Plus/personal iPhone/iOS17 recovery scope.
- `DEV-multi-conversation-state` remains Active on `dev/multi-conversation-state-20260827`; no open PR currently owns overlapping product source.
- b16 is historical/rejected before Runtime and must not be reused.
- b17 exact source `bc69d58b3245...` has accepted core iPhone/iOS17 Runtime evidence for resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid different-conversation overlap. It reproduced the historical-scroll defect.
- b18 exact source `f30c13b4ac2c...` has accepted iPhone/iOS17 Runtime for the tested historical-scroll / Sync / Reload-preservation / resident-regression matrix. Missing-anchor-message discard remains Runtime-unexercised.
- b19 exact source `c6accf16c8cf...` has accepted real-device process-footprint evidence for an observed 0→8 resident matrix: 53 valid samples, physical footprint about 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents; all observed HTTP statuses 200 and no HTTP429/error. `processMemoryLimitRemainingBytes` was absent, so exact process-limit headroom remains Unverified. There is no evidence for urgent normal-LRU eviction at 8 residents and no normal capacity is frozen.
- b20 exact source `754580fad96e...` is Code/Static/CI/Artifact valid but real-device Runtime exposed a presentation lifecycle defect: first entry into an unloaded conversation showed `新对话` while loading; re-entry after the Detail became resident was correct. Source proves Root assigned the list-summary title before first Detail view load, then `ConversationDetailViewController.viewDidLoad()` overwrote it with the neutral title.
- Exact b21 product/config source is `6b50ead167bfde305d2ad58dd16fee6edaabf597`, tree `01168ce7be8d9cf4888ad1d0718238826730c30d`; Run `33070183417` / Job `98510113281` succeeded; Artifact `9645439329` is identity-valid; IPA SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`. b21 adds only `detailViewController.loadViewIfNeeded()` before assigning the selected list-summary title. Runtime proof is pending.
- The b20 export also contained an earlier cold-start auth probe HTTP403, followed by successful account verification and conversation-list HTTP200 before the title reproduction. That event is not causal for the title defect and does not justify automatic retry/fallback.
- Current `main@3cbb5c9acce26c0004e1d78c9607f2361d83fe05` contains merged planning PR #18. Its planning files must be preserved during final synchronization.
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

b17 addresses the evidenced pre-Send owner/race/account-scope portion of 1–4 and has direct Runtime evidence for tested navigation/coalescing/hidden-Sync paths. b18 adds Runtime-accepted historical presentation isolation. b19 measures memory without changing owners. b20/b21 are title-presentation lifecycle corrections only. Items 5–7 require current Send/Stream protocol evidence and must not be guessed.

### P1 — around first daily-chat candidates

1. Basic Markdown/code-block rendering.
2. Conversation-list pagination/load-more beyond first 28 items.
3. Per-conversation draft and semantic scroll presentation state.
4. Hidden-conversation generating/completed status after streaming exists.
5. One centralized app-settings preference owner.
6. Background continuation over an active response set, not global Boolean.
7. Large-conversation phase timing: network / parse-model / first-visible-render.

Historical-reading anchor restoration is Runtime accepted on exact b18 for the tested matrix. Active-response `follow-tail` remains future Send/Stream integration because response activity must come from authoritative response ownership.

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

b17 Runtime confirms same-target coalescing and A Sync rejoin. b18 re-confirms coalescing when returning to B while B Sync is active. b20 rapid switching also retained multiple independent operations; its defect was title initialization, not request ownership.

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

Exact b18 implements and Runtime-validates historical-reading mode for the tested iPhone/iOS17 paths. Follow-tail eligibility/transition must consume future authoritative Send/Stream response lifecycle; current work adds no UI streaming authority.

### Selected title presentation lifecycle

The conversation list already owns a server-backed `ConversationSummary.title` for each displayed list row. Selecting a target may use that summary immediately for navigation presentation while its Detail remains unloaded; loaded Detail later confirms with `detail.title`.

b20 proved one lifecycle hazard: assigning the summary title before the Detail VC's first view load allowed `viewDidLoad()` neutral initialization to overwrite it. b21 resolves only the ordering by ensuring first view initialization happens before the summary title assignment. This is presentation metadata, not a second conversation/title authority, and does not alter Repository selection or request ownership.

### Conversation pagination / Markdown / settings / background

- Current accepted list call returns first page `offset=0&limit=28&order=updated`; pagination must use current service evidence and never clear resident detail solely because list page/order changes.
- Markdown/code rendering should prioritize development-chat usefulness without broad reparse/reload on every streamed token.
- First real preference toggle should establish one centralized app preference owner; view controllers consume it rather than inventing independent keys/defaults.
- Background protection is over an active response set, not a global Boolean.

## Residency / memory policy

Unlimited permanent residency is not acceptable as a final principle, but normal eviction policy must be evidence-based.

Current evidence/rules:

- b19 real task-VM evidence shows no immediate pressure at 8 residents on tested iPhone/iOS17.
- exact process-limit headroom was not returned; therefore no normal LRU capacity is frozen or guessed.
- selected resident protected;
- active detail/recovery resident protected;
- future active response protected;
- memory warning trims only eligible inactive terminal residents;
- no persistent chat-body disk cache;
- approximate visible-text bytes remain correlation only.

## Additional correctness constraints

- `同步最新消息` remains explicit reconciliation; list `update_time` must not silently become automatic reload policy.
- UI `聊天` / `工作` derivation remains Unverified unless current service evidence supplies authoritative identity.
- In-memory residency/presentation may disappear after process termination; do not add persistent chat-body cache solely to hide relaunch cost.
- Keep network/rate-limit failures observable. No reachability resend, speculative retry chain or global concurrency limiter without evidence.
- A transient cold-start auth failure must not be converted into hidden automatic retry merely because a later user/list generation succeeds.

## Testing gap

No test target today. Add only smallest deterministic support when state logic justifies project-file churn.

Real-device evidence remains mandatory for WebKit auth, real networking, HTTP429 behavior, UI switching, memory behavior, background execution and TrollStore mechanisms.

## Current serialized development state

1. `DEV-conversation-recovery` — Completed / merged / Stable b15.
2. `DEV-multi-conversation-state` — Active; b17 core Runtime, b18 historical-scroll Runtime and b19 observed memory Runtime accepted; b20 title lifecycle defect reproduced; b21 Code/Static/CI/Artifact accepted and Runtime pending.
3. Current durable roadmap is `DEVELOPMENT_PLAN.md`; current `main` planning updates must be preserved during final synchronization.
4. `DEV-send-stream` remains the stage where real response ownership/follow-tail can be implemented and tested.

## Current multi-conversation Runtime gate

Accepted on b17/b18/b19:

- loaded A -> B -> A without navigation-only A Detail refetch;
- hidden completion retained;
- same-target in-flight return coalesces;
- Sync A -> B -> A remains attached to same Sync;
- rapid different-conversation overlap without HTTP429 in supplied export;
- independent historical A/B anchors and first-time target isolation;
- visible Sync/Reload anchor preservation when anchored message remains;
- real process footprint observed through 8 residents without evidence for urgent normal LRU.

Rejected/superseded on b20:

- first unloaded Detail entry title presentation: Runtime showed `新对话` during loading due first-view lifecycle overwrite; second resident-backed entry was correct.

Pending on exact b21:

- first unloaded target immediately displays its list-summary title while loading and never gets overwritten by neutral `新对话`;
- rapid unloaded A -> B -> C title follows current selection immediately;
- late A/B completion cannot overwrite C title/content;
- resident return/historical scroll remains intact.

Still open before full Work Stable acceptance:

- isolated same-target Reload replacement while an older Detail is actually in flight;
- failed resident navigation with no implicit retry when a natural terminal failure is available;
- supported account-scope Runtime isolation when a real switch/logout route exists;
- stronger headroom/pressure evidence if a bounded normal LRU capacity is eventually needed;
- non-personal workspace isolation remains Unknown / Unverified.

Future Send/Stream adds separate scroll gate: A active at bottom -> B -> A grows/completes hidden -> return A at current latest bottom; A active -> user scrolls upward -> B -> return A at preserved historical anchor.

## Next exact action

Install exact b21 and run the first-unloaded-entry plus rapid unloaded A->B->C title matrix. Do not infer Runtime success from CI or Artifact. After title Runtime is accepted, continue only the remaining evidence-backed gates; do not invent normal LRU capacity or auth retry behavior without new evidence.

Before final PR/merge, synchronize with current `main@3cbb5c9acce26c0004e1d78c9607f2361d83fe05` without overwriting its planning documents, then rerun only validation materially affected by synchronized product source.