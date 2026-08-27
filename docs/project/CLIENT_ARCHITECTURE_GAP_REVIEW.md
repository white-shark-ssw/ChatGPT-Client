# Client Architecture Gap Review

_Last reviewed: 2026-08-27; refreshed after b18 semantic-scroll Candidate CI/Artifact validation._

## Purpose

Focused pre-send/stream architecture review for the native TrollStore ChatGPT client. It exists to prevent state/concurrency mistakes once multiple conversations, streaming, background execution and long conversations coexist.

Product rule: **reach a usable daily-chat candidate early; only P0 structural invariants may block the first production send/stream path.**

## Current evidence baseline

- `DEV-conversation-recovery-0.1.0-b15` is merged Stable for recorded Plus/personal iPhone/iOS17 recovery scope.
- Merged Stable baseline remains b15 / `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011` until Active Work completes/merges.
- `DEV-multi-conversation-state` is Active on `dev/multi-conversation-state-20260827`.
- b16 is historical/rejected before runtime and must not be reused.
- b17 exact source `bc69d58b3245...` has accepted core iPhone/iOS17 runtime evidence for resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid different-conversation overlap; no HTTP429 in supplied export. b17 reproduced the P1 semantic-scroll defect.
- Current exact b18 product/config source is `f30c13b4ac2c40dcda829585682825ca906dceae`, tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- b18 Run `33054012226` / Job `98456174184` succeeded; Artifact `9638821912` is identity-valid; IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.
- b18 adds only historical per-conversation scroll presentation metadata in `ConversationDetailViewController`; `ConversationRepository`, account/protocol ownership and network routes are unchanged.
- **b18 Runtime/manual/real-device is pending.** CI/Artifact does not prove the scroll defect is fixed.
- There is still no XCTest/UI-test target.

Cold-start login-state recovery belongs to completed recovery baseline. Do not create a separate `DEV-auth-resume` task. Default persistent WebKit storage remains sole persistent auth-secret authority.

## Priority classification

### P0 — required before production send/stream becomes authoritative

1. Per-conversation resident state instead of one loaded-detail slot.
2. Async operation freshness / stale-result protection with deterministic consumer termination.
3. Retain minimum authoritative conversation/node identity required by current evidence.
4. Scope resident/draft/response state to verified account/workspace context and purge/reject on context change.
5. Define new-conversation identity handoff from local pending UI to authoritative server identity.
6. Own responses per conversation/message identity instead of a global streaming flag.
7. Define Sync/Reload ownership transitions when target conversation has an active response.

b17 addresses the evidenced pre-send owner/race/account-scope portion of 1–4 and has direct runtime evidence for tested navigation/coalescing/hidden-Sync paths. Items 5–7 require current Send/Stream protocol evidence and must not be guessed.

### P1 — around first daily-chat candidates

1. Basic Markdown/code-block rendering.
2. Conversation-list pagination/load-more beyond first 28 items.
3. Per-conversation draft and **semantic scroll presentation state**, including historical-reading anchor restoration and future active-response `follow-tail` semantics while process remains alive.
4. Hidden-conversation generating/completed status after streaming exists.
5. One centralized app-settings preference owner.
6. Background continuation over an active response set, not global Boolean.
7. Large-conversation phase timing: network / parse-model / first-visible-render.

b18 is the exact historical-scroll correction Candidate. Active-response follow-tail remains future Send/Stream integration work because response activity must come from authoritative response ownership.

### P2 — after daily-chat loop is stable

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

Selecting B must not destroy A, cancel A merely because it becomes hidden, or force A to reload on return. Use one production conversation authority with per-conversation entries; do not create one repository per screen and do not keep full UIKit hierarchies alive as data cache.

### Single state-owner execution domain

Resident dictionaries, list state, operation generations/tasks, account-scope binding and transient-session ownership read/mutate through one explicit repository execution domain. Network transfer and pure parsing may occur off-owner. Thread safety must fix owner invariant, not create second store.

### Async freshness / race protection

Selection change alone must not discard valid target result, but obsolete operations cannot overwrite newer authoritative state.

Every operation binds account/context + target conversation + generation/token.

- Same-target replacement cancels older target task before replacement request ownership proceeds, preserving b15 behavior.
- Equivalent same-target loads may coalesce.
- Superseded/account-invalidated waiters terminate deterministically.
- Presentation has target/freshness identity so obsolete completion cannot mutate wrong conversation.
- No timer/retry/watchdog/fallback machinery.

b17 runtime directly confirms same-target coalescing and A Sync rejoin for supplied sequences.

### Account/workspace isolation

`AuthSessionStore` remains account authority. Repository operation/transport contexts are consumers, not account authorities.

A newly verified different context must invalidate old transient session, purge old list/resident/draft/response state, cancel/invalidate old operations and resolve waiters, reject late old-scope callbacks, never allow stale transport to re-adopt old scope, and never display old-account content under new context.

Current source keys personal scope with `userID + accountID`; non-personal workspace identity remains Unknown / Unverified.

### Preserve authoritative node identity

Visible message array is a projection, not complete authoritative conversation representation. Current Detail evidence supplies `current_node`, so branch-tip identity is retained. Do not retain raw multi-megabyte Detail JSON or invent future graph fields before Send evidence.

### New-conversation identity handoff

Send protocol probe must establish conversation identity creation, parent/current-node requirements, message/request/response lifecycle, and when new conversation can safely enter list/resident state. Temporary local identity, if required, gets one explicit handoff to authoritative identity; temporary and server identities must not remain independent owners.

### Per-conversation response ownership

Future response ownership is conceptually:

`conversation identity + response/message identity -> response lifecycle`

A may continue generating while B is visible. Navigation never calls Stop just because A becomes hidden. Initial rule: at most one active response per conversation unless current protocol/runtime proves overlap; Stop targets one exact response/conversation, never global `isStreaming`.

### Sync/Reload while response active

`同步最新消息` targets one conversation and never resends. `重载当前会话` rebuilds one conversation only. Exact interaction with active future response follows current Send/Stream evidence and is not guessed pre-send.

## P1 implementation notes

### Markdown/code rendering

Prioritize paragraphs/headings/lists, inline/fenced code, code-copy, links and tables when current content requires them. Do not broad-reload/reparse whole conversation on every streamed token.

### Conversation pagination

Current accepted list call returns first page (`offset=0&limit=28&order=updated`). Pagination must use current service evidence, deduplicate by authoritative conversation ID and never clear resident detail because list page/order changes.

### Per-conversation UI state

Within live process preserve lightweight semantic scroll presentation, later composer draft, and useful reasoning-detail expansion state. Avoid raw pixel-only restoration for growing long conversations.

Two scroll modes are user-confirmed:

1. **Historical-reading anchor** — if user is reading away from bottom, preserve anchor tied to message identity plus relative visual offset where practical. A->B->A restores A's own anchor; B scrolling does not move A.
2. **Follow-tail** — if user leaves A at/near bottom while authoritative A response is active, hidden growth/completion keeps A attached to newest tail; returning A shows current latest bottom, not old pre-growth anchor.

Intentional upward scroll while A is generating exits follow-tail and establishes historical-reading intent.

b18 implements only historical-reading mode using lightweight presentation metadata. It tracks actually displayed conversation separately from repository selection, captures top visible message identity + relative offset, restores after rows reload, resets no-anchor target to top, clears anchors on account reset, and preserves through visible Sync/Reload only when same anchor message remains. If anchor message disappears, it discards anchor and returns top rather than inventing fallback.

Follow-tail eligibility/transition must consume future authoritative Send/Stream response lifecycle; b18 does not add UI streaming authority.

### Hidden response status

After Send/Stream exists, sidebar may derive generating/completed-unseen presentation from authoritative response owner; it is not a second response store and not a claim about service unread API.

### Central settings owner

First real preference toggle should establish one small app preference owner around `UserDefaults`/system state. View controllers consume settings; they do not invent independent keys/defaults.

### Multi-response background semantics

Background protection is over active protected-response set. A finishing must not release protection while B remains active. Completion notification is deduplicated per response lifecycle.

### Long-conversation timing

Before major performance rewrites, instrument safe phase timing for network completion, JSON parse/model construction, first visible presentation and later Markdown/layout. End-to-end duration alone does not identify bottleneck.

## Additional correctness constraints

### Resident freshness

Conversation may change on another client. Newer list `update_time` may be stale hint but must not silently trigger reload without accepted product rule. `同步最新消息` remains explicit reconciliation.

### `聊天` / `工作` derivation

UI requirement exists, but authoritative service field distinguishing modes remains Unverified. Do not infer from title/UI text.

### Process death

In-memory residency/presentation may disappear after process termination/force quit. Acceptable early. Do not add persistent chat-body cache solely to hide relaunch cost.

### Network/rate-limit failures

Keep failures observable. No reachability-driven resend, duplicate stream after network transition, speculative retry chain or global concurrency limiter without evidence. b17 rapid overlap reached three active operations without HTTP429 for supplied run only.

## Testing gap

No test target today. Add only smallest deterministic support when state logic justifies project-file churn.

High-value future pure tests include current-branch/node normalization, resident lookup/eviction eligibility, same-target coalescing/waiter termination, stale-generation/account rejection, list freshness, semantic scroll anchor<->follow-tail transitions once authoritative response activity exists, and future response lifecycle/stream parser.

Real-device evidence remains mandatory for WebKit auth, real networking, HTTP429 behavior, UI switching, memory behavior, background execution and TrollStore mechanisms.

## Current serialized development sequence

1. `DEV-conversation-recovery` — Completed / merged / Stable b15.
2. `DEV-multi-conversation-state` — Active; b18 exact Candidate now awaits real-device historical-scroll validation.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

Do not create separate `DEV-auth-resume` Work.

## Current multi-conversation runtime gate

Accepted on b17:

- A loaded -> B loaded -> A without navigation-only A Detail refetch.
- hidden A completion retained while B untouched.
- A -> B -> A before completion coalesces onto one A operation.
- Sync A -> B -> A before terminal remains attached to same Sync and applies terminal state.
- rapid A/B/C overlap without HTTP429 in supplied export.
- resident/active/protected counts across several conversations including large ones.

Pending on exact b18:

- A around ~10% -> B scroll -> A returns to same semantic/visual historical anchor.
- A and B maintain independent saved anchors over repeated switching.
- first-time/new target with no anchor starts at normal top, not previous conversation's offset.
- visible Sync/Reload preserve anchor when same anchor message remains; absent anchor message discards to top.
- spot-check no regression in resident/coalesced navigation behavior.

Still open before full Work Stable acceptance:

- isolated target-only Reload replacement as applicable;
- failed resident navigation with no implicit retry when natural failure available;
- supported account-scope runtime isolation only when real switch/logout route exists;
- real process/system memory evidence sufficient to choose bounded normal LRU capacity.

Future Send/Stream adds separate scroll gate: A active at bottom -> B -> A grows/completes hidden -> return A at current latest bottom; A active -> user scrolls upward -> B -> return A at preserved historical anchor.

Normal LRU capacity remains Unknown until device evidence exists. Approximate text bytes cannot freeze capacity.
