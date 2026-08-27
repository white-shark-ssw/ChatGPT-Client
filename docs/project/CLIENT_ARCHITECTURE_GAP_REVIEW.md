# Client Architecture Gap Review

_Last reviewed: 2026-08-27; refreshed after b17 real-device multi-conversation validation and scroll-semantics clarification._

## Purpose

This is the focused pre-send/stream architecture review for the native TrollStore ChatGPT client. It exists to prevent state/concurrency mistakes that would otherwise force expensive rework once multiple conversations, streaming, background execution and long conversations are active together.

Product rule: **reach a usable daily-chat candidate as early as possible; only P0 structural invariants may block the first production send/stream path.**

## Current evidence baseline

- `DEV-conversation-recovery-0.1.0-b15` is merged Stable for the recorded Plus/personal iPhone/iOS17 recovery scope. PR #10 is no longer Active.
- Current merged Stable baseline remains b15 / `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011` until the Active Work completes/merges.
- `DEV-multi-conversation-state` is the Active serialized Work on `dev/multi-conversation-state-20260827`.
- b16 is historical/rejected before runtime: source `81e6774...` compiled, but Artifact `9621830284` had wrong recovery candidate/slug and second source review found owner/race gaps.
- b17 is the first identity-valid multi-conversation runtime Candidate: exact product/config source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`; static parse passed; Run `33045536770` succeeded; Artifact `9635486304` independently verifies version/build/candidate/source/SHA/arm64/iOS14 identity.
- b17 source includes per-conversation residency/operations, stale Auth-scope rejection, deterministic waiter termination, target-specific recovery, list/detail/presentation freshness, same-target cancel-before-replace ordering, one repository execution domain, `current_node` retention, active-resident memory-warning protection and privacy-safe residency diagnostics.
- Exact b17 iPhone/iOS17 runtime now accepts the tested core sequences: resident A->B->A return without navigation-only refetch, hidden completion retention, same-target in-flight coalescing, Sync A->B->A rejoin, and rapid different-conversation overlap with up to 3 active operations and no HTTP429 in the supplied diagnostic export.
- b17 also reproduces a P1 presentation defect: per-conversation semantic scroll position is not preserved when switching A->B->A.
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

b17 addresses the pre-send owner/race/account-scope portion of items 1–4 and has direct runtime evidence for the tested navigation/coalescing/hidden-Sync portions. Items 5–7 require current Send/Stream protocol evidence and must not be guessed in advance.

### P1 — around the first daily-chat candidates

1. Basic Markdown/code-block rendering.
2. Conversation-list pagination/load-more beyond the first 28 items.
3. Per-conversation draft and **semantic scroll presentation state**, including historical-reading anchor restoration and future active-response `follow-tail` semantics while the process remains alive.
4. Hidden-conversation generating/completed status in the sidebar after streaming exists.
5. One centralized app-settings preference owner.
6. Background continuation over an active response **set**, not a global Boolean.
7. Large-conversation phase timing: network / parse-model / first-visible-render.

Semantic scroll restoration does **not** invalidate the accepted b17 core residency proof. The ordinary A->B->A anchor defect is now runtime reproduced and is the next small user-visible correction; active-response `follow-tail` behavior becomes runtime-testable only after Send/Stream owns real per-conversation response lifecycle state.

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

b17 main-thread-confines mutable repository authority; the supplied runtime sequences did not expose cross-conversation presentation/operation corruption.

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

Exact b17 runtime now directly confirms same-target coalescing and A Sync rejoin for the supplied sequences.

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

Within the live process preserve lightweight state such as semantic scroll presentation, later composer draft, and useful reasoning-detail expansion state. Avoid raw pixel-only restoration for growing long conversations.

The user-confirmed scroll contract has two distinct semantic modes:

1. **Historical-reading anchor** — if the user is reading away from the bottom, preserve an anchor tied to message identity plus relative visual offset where practical. Switching A->B->A must restore A's own anchor; B's scrolling must not move A.
2. **Follow-tail** — if the user leaves A while A is at/near the bottom and an authoritative A response is active, A remains semantically attached to its newest tail while hidden. If that response appends/completes while B is visible, returning to A must show A's **current latest bottom**, not the older pre-response anchor.

User intent changes the mode: intentionally scrolling upward while A is generating exits `follow-tail` and establishes a historical-reading anchor. After that, leaving/returning must preserve that reading location rather than force-scroll to the newest bottom.

This presentation state is per conversation and lightweight; it is not a second conversation-data or response authority. `follow-tail` eligibility/transition must consume the future authoritative per-conversation response lifecycle from Send/Stream rather than invent a separate UI streaming flag now.

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

Keep failures observable. No reachability-driven resend, duplicate stream after network transition, speculative retry chain or global concurrency limiter without evidence. Exact b17 rapid A/B/C detail overlap reached 3 active operations without HTTP429 in the supplied export; this is evidence for that run only, not proof of unlimited service concurrency.

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
- semantic scroll state transition: anchor <-> follow-tail based on user scroll intent and authoritative response activity;
- future response lifecycle terminal transitions;
- stream parser once event format is evidenced.

Real-device evidence remains mandatory for WebKit auth, real networking, HTTP429 behavior, UI switching, memory behavior, background execution and TrollStore mechanisms.

## Current serialized development sequence

1. `DEV-conversation-recovery` — **Completed / merged / Stable b15**.
2. `DEV-multi-conversation-state` — **Active; b17 core runtime switching/coalescing/hidden-Sync sequences accepted; reproduced P1 scroll presentation defect is the next small correction before Work completion**.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

Do not create a separate `DEV-auth-resume` Work.

## Current multi-conversation runtime gate

Current b17 evidence covers:

- A loaded -> B loaded -> A with no new A Detail request;
- hidden A completion retained while B remains untouched;
- A -> B -> A before A completion coalesces one A operation;
- Sync A -> B -> A before terminal remains attached to the same Sync and applies terminal state;
- rapid A/B/C overlap with no HTTP429 in the supplied export;
- resident/active/protected counts across several conversations including large ones.

Still open before full Work Stable acceptance:

- semantic A->B->A historical scroll-anchor correction and real-device proof;
- target-only Reload replacement regression on b17/b18 as applicable;
- failed A -> B -> A with no implicit retry when a natural failure is available;
- supported account-scope runtime isolation only when a real switch/logout route exists;
- real device/system memory evidence sufficient to choose a bounded normal LRU capacity.

Future Send/Stream must add a separate scroll-semantic runtime gate: A active response while at bottom -> switch to B/use B -> A appends/completes hidden -> return A at **current latest bottom**; and A active response -> user intentionally scrolls upward -> switch B -> return A at preserved historical-reading anchor rather than forced bottom.

Normal LRU capacity remains Unknown until device evidence exists. Approximate visible-text bytes cannot freeze capacity.
