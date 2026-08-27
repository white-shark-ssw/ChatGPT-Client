# Client Architecture Gap Review

_Last reviewed: 2026-08-27; refreshed through exact b21 Reload-under-load Runtime acceptance and current-main synchronization._

## Purpose

Focused pre-Send/Stream architecture review for the native TrollStore ChatGPT client. It exists to prevent state/concurrency mistakes once multiple conversations, streaming, background execution and long conversations coexist.

Product rule: **reach a usable daily-chat candidate early; only P0 structural invariants may block the first production Send/Stream path.**

## Current evidence baseline

- `DEV-conversation-recovery-0.1.0-b15` is merged Stable for recorded Plus/personal iPhone/iOS17 recovery scope.
- `DEV-multi-conversation-state` is ready for PR/closure on `dev/multi-conversation-state-20260827` for the tested Plus/personal iPhone/iOS17 read-state scope.
- b16 is historical/rejected before Runtime and must not be reused.
- b17 exact source `bc69d58b3245...` accepts resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid different-conversation overlap; it reproduced the historical-scroll defect.
- b18 exact source `f30c13b4ac2c...` accepts the tested historical-scroll / Sync / Reload-preservation / resident-regression matrix. Missing-anchor-message discard remains Runtime-unexercised.
- b19 exact source `c6accf16c8cf...` accepts a real-device 0→8 resident process-footprint matrix: 53 valid samples, physical footprint about 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents; all observed HTTP statuses 200 and no HTTP429/error. `processMemoryLimitRemainingBytes` was absent, so exact process-limit headroom remains Unverified. There is no evidence for urgent normal-LRU eviction at 8 residents and no normal capacity is frozen.
- b20 exact source `754580fad96e...` is Code/Static/CI/Artifact valid but Runtime exposed the first unloaded Detail title lifecycle overwrite; it is superseded.
- Exact b21 source `6b50ead167bfde305d2ad58dd16fee6edaabf597`, tree `01168ce7be8d9cf4888ad1d0718238826730c30d`, Run `33070183417`, Job `98510113281`, Artifact `9645439329`, IPA SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d` is the final Runtime Candidate for this Work. Direct user testing accepts first-unloaded-entry/re-entry/rapid A→B→C title behavior. Exact diagnostics additionally accept two same-target ordinary-load -> Reload replacement-under-load sequences, including hidden unrelated-conversation independence and return coalescing onto the same active Reload.
- Current `main@4f38cdace0c94fed852534448f1362f1125270de` is synchronized into the development branch by two-parent merge commit `7f2a9776cc419f8e8b30aebbf731e82b3bc24a92`. Its six planning/rules files are preserved exactly. GitHub reports `behind_by=0`; from exact b21 product source to the synchronized head only docs changed.
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

The completed multi-conversation read-state work addresses the evidenced pre-Send owner/race/account-scope portion of 1–4 for the tested Plus/personal scope. Items 5–7 require current Send/Stream protocol evidence and must not be guessed. Supported account-switch Runtime proof and non-personal workspace identity remain explicit Unknown/Unverified boundaries rather than reasons to fabricate product behavior before Send/Stream.

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

Runtime now directly covers both same-target coalescing and the multi-conversation replacement-under-load invariant. Exact b21 diagnostics show generation 1 ordinary Detail cancellation, generation 2 Reload ownership/HTTP200, unrelated-conversation independence while Reload is hidden, and return coalescing onto that same generation without duplicate Reload or stale overwrite.

### Account/workspace isolation

`AuthSessionStore` remains account authority. Repository operation/transport contexts are consumers, not account authorities.

A newly verified different context must invalidate old transient session, purge old list/resident/draft/response state, cancel/invalidate old operations and resolve waiters, reject late old-scope callbacks, never allow stale transport to re-adopt old scope, and never display old-account content under new context.

Current source keys personal scope with `userID + accountID`. There is no supported account-switch/logout path in the current product and no accepted non-personal workspace identity evidence, so those Runtime conditions remain Unknown / Unverified at read-state closure. Do not manufacture fake transitions merely to claim a matrix pass.

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

Exact b18 implements and Runtime-validates historical-reading mode for the tested iPhone/iOS17 paths. Follow-tail eligibility/transition must consume future authoritative Send/Stream response lifecycle; current read-state work adds no UI streaming authority.

### Selected title presentation lifecycle

The conversation list already owns a server-backed `ConversationSummary.title` for each displayed list row. Selecting a target may use that summary immediately for navigation presentation while its Detail remains unloaded; loaded Detail later confirms with `detail.title`.

b20 proved one lifecycle hazard: assigning the summary title before the Detail VC's first view load allowed `viewDidLoad()` neutral initialization to overwrite it. b21 resolves only the ordering by ensuring first view initialization happens before the summary title assignment. Direct real-device testing accepts the requested first-entry/re-entry/rapid A→B→C title matrix. This is presentation metadata, not a second conversation/title authority, and does not alter Repository selection or request ownership.

### Conversation pagination / Markdown / settings / background

- Current accepted list call returns first page `offset=0&limit=28&order=updated`; pagination must use current service evidence and never clear resident detail solely because list page/order changes.
- Current main roadmap now places `DEV-conversation-list-cache-core` immediately after multi-conversation becomes Stable/merged. It adds an account-scoped durable list snapshot behind `ConversationRepository`; it must not become a second list authority or prefetch every Detail.
- Markdown/code rendering should prioritize development-chat usefulness without broad reparse/reload on every streamed token.
- First real preference toggle should establish one centralized app preference owner; view controllers consume it rather than inventing independent keys/defaults.
- Background protection is over an active response set, not a global Boolean.

## Residency / memory policy

Unlimited permanent residency is not accepted as an abstract final principle, but normal eviction policy must remain evidence-based.

Current evidence/rules:

- b19 real task-VM evidence shows no immediate pressure at 8 residents on tested iPhone/iOS17.
- exact process-limit headroom was not returned; therefore no normal LRU capacity is frozen or guessed.
- selected resident protected;
- active detail/recovery resident protected;
- future active response protected;
- memory warning trims only eligible inactive terminal residents;
- no persistent chat-body disk cache;
- approximate visible-text bytes remain correlation only.

Therefore normal LRU is not a current read-state closure requirement. Revisit only when stronger process-limit/headroom/pressure evidence creates a real requirement.

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
2. `DEV-multi-conversation-state` — Ready for PR/closure; exact b21 is final Runtime Candidate for tested Plus/personal iPhone/iOS17 read-state scope.
3. `DEV-conversation-list-cache-core` — current roadmap priority immediately after multi-conversation is Stable/merged; durable scope in `CONVERSATION_LIST_CACHE_PLAN.md`.
4. `DEV-send-stream` remains the stage where real response ownership/follow-tail can be implemented and tested after the intervening roadmap work.

## Multi-conversation closure boundary

Accepted on b17/b18/b19/b21:

- loaded A -> B -> A without navigation-only A Detail refetch;
- hidden completion retained;
- same-target in-flight return coalesces;
- Sync A -> B -> A remains attached to same Sync;
- rapid different-conversation overlap without HTTP429 in supplied export;
- independent historical A/B anchors and first-time target isolation;
- visible Sync/Reload anchor preservation when anchored message remains;
- real process footprint observed through 8 residents without evidence for urgent normal LRU;
- b21 first-unloaded-entry/re-entry/rapid A→B→C title lifecycle matrix;
- b21 same-target ordinary-load -> Reload replacement-under-load, old-task cancellation, hidden unrelated-conversation independence, and rejoin coalescing onto the same Reload.

Superseded/failing:

- b20 first unloaded Detail entry title presentation: Runtime showed `新对话` during loading due first-view lifecycle overwrite; second resident-backed entry was correct.

Conditional boundaries retained without claiming Runtime pass:

- natural terminal failed-resident navigation;
- supported account-switch purge when a real route exists;
- non-personal workspace isolation;
- missing-anchor-message discard;
- normal LRU capacity if future pressure/headroom evidence creates a need.

These are not current known defects and are not reasons to fabricate unsupported behavior to keep the read-state Work open.

Future Send/Stream adds separate scroll gate: A active at bottom -> B -> A grows/completes hidden -> return A at current latest bottom; A active -> user scrolls upward -> B -> return A at preserved historical anchor.

## Next exact action

Create and review the multi-conversation PR against synchronized `main@4f38cdace0c94fed852534448f1362f1125270de`. If PR CI/merge review exposes no product/config conflict, merge and promote the tested Plus/personal iPhone/iOS17 read-state scope to Stable, preserve all conditional boundaries above as Unknown/Unverified, and remove the Active checkpoint. No b22 is justified by current evidence.