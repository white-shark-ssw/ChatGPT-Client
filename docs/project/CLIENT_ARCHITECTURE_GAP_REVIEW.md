# Client Architecture Gap Review

_Last reviewed: 2026-08-27; refreshed after b17 static/CI/Artifact validation._

## Purpose

This is the focused pre-send/stream architecture review for the native TrollStore ChatGPT client. It exists to prevent state/concurrency mistakes that would otherwise force expensive rework once multiple conversations, streaming, background execution and long conversations are active together.

Product rule: **reach a usable daily-chat candidate as early as possible; only P0 structural invariants may block the first production send/stream path.**

## Current evidence baseline

- `DEV-conversation-recovery-0.1.0-b15` is merged Stable for the recorded Plus/personal iPhone/iOS17 recovery scope. PR #10 is no longer Active.
- Current accepted runtime baseline remains b15 / `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`.
- `DEV-multi-conversation-state` is the Active serialized Work on `dev/multi-conversation-state-20260827`.
- b16 is historical/rejected before runtime: source `81e6774...` compiled, but Artifact `9621830284` had wrong recovery candidate/slug and second source review found owner/race gaps.
- b17 is the first identity-valid multi-conversation runtime Candidate: exact product/config source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`; static parse passed; Run `33045536770` succeeded; Artifact `9635486304` independently verifies version/build/candidate/source/SHA/arm64/iOS14 identity.
- b17 source includes per-conversation residency/operations, stale Auth-scope rejection, deterministic waiter termination, target-specific recovery, list/detail/presentation freshness, same-target cancel-before-replace ordering, one repository execution domain, `current_node` retention, active-resident memory-warning protection and privacy-safe residency diagnostics.
- **No b17 real-device multi-conversation evidence exists yet.** CI/Artifact success does not prove runtime behavior.
- There is still no XCTest/UI-test target.

Cold-start login-state recovery belongs to the completed recovery baseline. **Do not create a separate `DEV-auth-resume` task.** Default persistent WebKit storage remains the sole persistent auth-secret authority.

## Priority classification

### P0 — required before production send/stream becomes authoritative

1. **Per-conversation resident state instead of one loaded-detail slot.**
2. **Async operation freshness / stale-result protection with deterministic consumer termination.**
3. **Retain the minimum authoritative conversation/node identity required by current evidence.**
4. **Scope resident/draft/response state to verified account/workspace context and purge/reject on context change.**
5. **Define the new-conversation identity handoff from local pending UI to authoritative server identity.**
6. **Own responses per conversation/message identity instead of a global streaming flag.**
7. **Define Sync/Reload ownership transitions when the target conversation has an active response.**

b17 addresses the pre-send owner/race/account-scope portion of items 1–4 at source/CI/Artifact level. Items 5–7 require current Send/Stream protocol evidence and must not be guessed in advance.

### P1 — around the first daily-chat candidates

1. Basic Markdown/code-block rendering.
2. Conversation-list pagination/load-more beyond the first 28 items.
3. Per-conversation draft and **semantic scroll-anchor restoration** while the process remains alive.
4. Hidden-conversation generating/completed status in the sidebar after streaming exists.
5. One centralized app-settings preference owner.
6. Background continuation over an active response **set**, not a global Boolean.
7. Large-conversation phase timing: network / parse-model / first-visible-render.

Semantic scroll restoration is useful but does **not** block b17 core runtime proof unless a later explicit requirement raises its priority.

### P2 — after the daily-chat loop is stable

1. Optional cross-process state restoration beyond normal WebKit auth persistence.
2. Persistent chat-body/disk cache only after explicit privacy/storage requirement.
3. Advanced edit/regenerate/branch cache optimization.
4. Advanced unread/history synchronization with other clients.
5. Broad lower-iOS/iPad optimization after exact runtime evidence.

## P0 invariants

### Per-conversation residency

Foreground selection is presentation state only.

Conceptually:

`verified account/workspace context + conversation ID -> resident conversation state`

Selecting B must not destroy A, cancel A's owned work merely because A becomes hidden, or force A to reload when returning.

Use one production conversation authority with per-conversation entries. Do not create one authoritative repository per screen and do not keep full UIKit view hierarchies alive as the data cache.

### Single state-owner execution domain

Resident dictionaries, list state, operation generations/tasks, account-scope binding and cached transient-session ownership must read/mutate through one explicit repository execution domain.

Network transfer and pure/expensive parsing may occur off-owner. Thread safety must fix the owner invariant, not create a second store.

b17 main-thread-confines mutable repository authority; runtime validation still needs to confirm no presentation/operation regression.

### Async freshness / race protection

Selection change alone must not discard a valid result, but obsolete operations must not overwrite newer authoritative state.

Examples:

- ordinary load A starts, then Reload A starts;
- Sync A starts, user navigates A -> B -> A before terminal;
- account context changes while old list/detail/session work is queued or in flight;
- future Stop/terminal response state occurs, then a late stream callback arrives.

Every operation binds account/context + target conversation + generation/token.

- Same-target replacement cancels the old target task before replacement request ownership proceeds, preserving accepted b15 behavior.
- Equivalent same-target loads may coalesce.
- Superseded/account-invalidated waiters terminate deterministically.
- Presentation uses its own target/freshness identity so lifecycle termination cannot mutate the wrong conversation.
- No timer/retry/watchdog/fallback machinery.

### Account/workspace isolation

`AuthSessionStore` remains account authority. Repository transport/operation contexts are consumers, not account authorities.

A newly verified different context must:

- invalidate old transient native session;
- purge old list/resident/draft/response state;
- cancel/invalidate old operations and resolve relevant waiters;
- reject late old-scope callbacks;
- never allow old transport context to re-adopt previous scope;
- never display old-account content under new context.

Current source keys scope with `userID + accountID`; current evidence is Plus/personal only. Whether non-personal workspaces require another identity remains **Unknown / Unverified**.

### Preserve authoritative node identity

Visible message array is a projection, not the complete authoritative conversation representation.

Current Detail evidence supplies `current_node`, so b17 retains that branch-tip identity. Before production Send, protocol evidence must establish whether parent/message/request identities beyond this are required.

Do not retain raw multi-megabyte Detail JSON for convenience and do not invent future graph fields before evidence.

### New-conversation identity handoff

The Send protocol probe must prove:

- whether conversation identity is client-generated or service-established;
- parent/current-node requirements;
- message/request/response identity lifecycle;
- when a new conversation is safe to insert into list/resident state.

If a temporary local identity is required, it gets one explicit handoff to authoritative conversation identity. Temporary and server identities must never remain independent owners. Rapid double-send must not duplicate unresolved conversations/messages.

### Per-conversation response ownership

Future response ownership is conceptually:

`conversation identity + response/message identity -> response lifecycle`

A may continue generating while B is visible. Navigation never calls Stop merely because A becomes hidden.

Initial rule:

- at most one active response per conversation unless current protocol/runtime proves overlap;
- different conversations are architecturally independent;
- whether A and B can maintain simultaneous server streams is **Unknown / Unverified** until Send/Stream device testing;
- Stop targets one exact response/conversation, never a global `isStreaming` flag.

### Sync/Reload while a response is active

`同步最新消息` targets one conversation, never resends, and reconciles server state without regressing newer local authoritative progress.

`重载当前会话` is stronger/user-explicit and rebuilds one conversation only. Exact cancel/detach behavior for an active future response follows current Send/Stream evidence and is not guessed pre-send.

## P1 implementation notes

### Markdown/code rendering

Prioritize development-chat usefulness: paragraphs/headings/lists, inline/fenced code, code-copy, links, and tables when current content requires them. Do not broad-reload/reparse the entire conversation on every streamed token.

### Conversation pagination

Current accepted list call returns first page (`offset=0&limit=28&order=updated`). Pagination must use current service evidence, deduplicate by authoritative conversation ID and never clear resident detail because list order/page membership changes.

### Per-conversation UI state

Within the live process preserve lightweight state such as semantic scroll anchor, later composer draft, and useful reasoning-detail expansion state. Avoid raw pixel-only restoration for growing long conversations.

Do not persist drafts/chat bodies to disk without separate privacy/storage decision.

### Hidden response status

After Send/Stream exists, sidebar may derive thinking/generating/completed-unseen presentation from authoritative response owner. It is not a second response store and not a claim about an OpenAI unread API.

### Central settings owner

The first real preference toggle should establish one small app preference owner around `UserDefaults`/system state. View controllers consume settings; they do not invent independent keys/defaults.

### Multi-response background semantics

Background protection is over an active protected-response set. A finishing must not release protection while B remains active. Completion notification is deduplicated per response lifecycle.

### Long-conversation timing

Before major performance rewrites, instrument safe phase timing for network completion, JSON parse/model construction, first visible presentation and later Markdown/layout. End-to-end duration alone does not identify the bottleneck.

## Additional correctness constraints

### Resident freshness

A conversation can change on another client. A newer list `update_time` may later be a stale hint but must not silently trigger reload without an accepted product rule. `同步最新消息` remains explicit reconciliation.

### `聊天` / `工作` derivation

UI requirement exists, but authoritative service field distinguishing these modes remains Unverified. Do not infer from title/UI text.

### Process death

In-memory residency may disappear after process termination/force quit. This is acceptable early. Do not add persistent chat-body cache solely to hide relaunch cost.

### Network/rate-limit failures

Keep failures observable. No reachability-driven resend, duplicate stream after network transition, speculative retry chain or global concurrency limiter without evidence. b17 runtime must record whether rapid A/B/C detail loads trigger HTTP429/service pressure.

## Testing gap

There is no test target today. Add only the smallest deterministic support when state logic justifies the project-file churn.

High-value future pure tests include:

- current-branch/node normalization;
- resident lookup/eviction eligibility;
- same-target coalescing and waiter termination;
- stale-operation generation rejection;
- stale-account context rejection and account purge;
- single-flight transient-session acquisition;
- list generation/freshness;
- future response lifecycle terminal transitions;
- stream parser once event format is evidenced.

Real-device evidence remains mandatory for WebKit auth, real networking, HTTP429 behavior, UI switching, memory behavior, background execution and TrollStore mechanisms.

## Current serialized development sequence

1. `DEV-conversation-recovery` — **Completed / merged / Stable b15**.
2. `DEV-multi-conversation-state` — **Active; b17 is identity-valid and awaits exact real-device core matrix**.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

Do not create a separate `DEV-auth-resume` Work.

## Current b17 runtime gate

Before calling multi-conversation residency Runtime-accepted/Stable, exact b17 evidence must cover at least:

- A loaded -> B loaded -> A with no new A Detail request;
- hidden A completion retained while B remains untouched;
- A -> B -> A before A completion coalesces one A operation;
- Sync A -> B -> A before terminal remains attached to the same Sync and applies terminal state;
- target-only Sync/Reload replacement and b15 cancellation regression;
- failed A -> B -> A with no implicit retry;
- rapid A/B/C overlap and HTTP429 observation;
- resident/active/protected counts and real device/system memory observation across several conversations including a large one;
- account-scope runtime isolation only when a real supported switch/logout route is available.

Normal LRU capacity remains Unknown until that device evidence exists. Approximate visible-text bytes cannot freeze capacity.
