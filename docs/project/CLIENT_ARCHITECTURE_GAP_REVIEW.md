# Client Architecture Gap Review

_Last reviewed: 2026-08-27; refreshed after b16 multi-conversation CI/source review._

## Purpose

This is the focused pre-send/stream architecture review for the native TrollStore ChatGPT client. It exists to prevent the small number of state/concurrency mistakes that would otherwise force expensive rework once multiple conversations, streaming, background execution and long conversations are active together.

Product rule: **reach a usable daily-chat candidate as early as possible; only P0 structural invariants may block the first production send/stream path.**

## Current evidence baseline

- `DEV-conversation-recovery-0.1.0-b15` is merged Stable for the recorded Plus/personal iPhone/iOS17 recovery scope. PR #10 is no longer Active.
- Current accepted runtime baseline remains b15 / `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`.
- `DEV-multi-conversation-state` is now the Active serialized Work on `dev/multi-conversation-state-20260827`.
- b16 product/config source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08` compiled/packaged in Run `33009246356`, but Artifact `9621830284` is identity-rejected because the build script still emitted recovery candidate/slug values. b16 has no runtime evidence and cannot be reused.
- Active source already introduces account-scoped/per-conversation residency direction, per-conversation detail generations/tasks, ordinary-load coalescing, failed terminal residency, current-node retention, account reset/list guards and memory-warning trim.
- Second source review found unresolved P0 defects before a valid runtime Candidate: stale operation context can re-adopt an old account scope; superseded/account-reset waiters can be abandoned; hidden Sync A -> B -> A can leave visible A stale; list freshness/presentation is incomplete; detail task-handle attachment has an avoidable ownership window; mutable repository reads are not fully confined to one owner domain.
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

Items 5–7 become concretely implementable only after current Send/Stream protocol evidence exists. `DEV-multi-conversation-state` closes the pre-send owner/race/account-scope portion without guessing send protocol behavior.

### P1 — around the first daily-chat candidates; do not block the first valid core multi-conversation runtime proof

1. Basic Markdown/code-block rendering.
2. Conversation-list pagination/load-more beyond the first 28 items.
3. Per-conversation draft and **semantic scroll-anchor restoration** while the process remains alive.
4. Hidden-conversation generating/completed status in the sidebar after streaming exists.
5. One centralized app-settings preference owner.
6. Background continuation over an active response **set**, not a global Boolean.
7. Large-conversation phase timing: network / parse-model / first-visible-render.

Semantic scroll restoration is useful but is **not** a blocker for the first valid `DEV-multi-conversation-state` core runtime Candidate unless a later explicit requirement changes its priority.

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

Selecting B must not destroy A, cancel A's owned request/response merely because A became hidden, or force A to reload when returning to it.

Use one production conversation authority with per-conversation entries. Do not create one authoritative repository per screen and do not keep full UIKit view hierarchies alive as the cache.

### Single state-owner execution domain

Resident dictionaries, list state, operation generations/tasks, account-scope binding and cached transient-session ownership must mutate/read through one explicit repository execution domain.

- Network transfer and expensive JSON parsing may occur off-main.
- Mutable repository state and list-position/state lookup must not race across URLSession and UIKit callbacks.
- Thread safety must fix the owner invariant, not create a second cache or duplicate state authority.

### Async freshness / race protection

Selection change alone must no longer discard a valid result, but an **obsolete** operation must not overwrite newer authoritative state.

Examples:

- ordinary load A starts, then Reload A starts;
- Sync A starts, user navigates A -> B -> A before Sync terminal;
- account context changes while old list/detail/session work is queued or in flight;
- future Stop/terminal response state occurs, then a late stream callback arrives.

Every operation is bound to account/context + target conversation identity + generation/token.

- Same-target replacement cancels the old target task before starting the replacement request, preserving accepted b15 ordering.
- Equivalent missing-detail requests may coalesce.
- Coalesced/superseded/account-invalidated consumers require deterministic terminal semantics; do not silently strand callbacks/spinners as the final contract.
- Presentation callbacks use their own freshness/target identity so explicitly terminating obsolete repository consumers cannot mutate the wrong visible conversation.
- No timer/retry/watchdog/fallback machinery is introduced.

### Account/workspace isolation

`AuthSessionStore` remains account authority. Repository operation contexts are consumers, not account authorities.

Explicit logout/account switch or a newly verified different context must:

- invalidate the old transient native session;
- purge old-account list/resident/draft/response state;
- cancel/invalidate old operations and terminally resolve relevant waiters;
- reject late old-scope callbacks;
- never allow an old operation context to re-adopt the previous scope after a newer verified context exists;
- never display old-account content under the new context.

Current Active source keys scope with `userID + accountID`; current evidence is Plus/personal only. Whether non-personal workspaces require another identity is **Unknown / Unverified**.

### Preserve authoritative node identity

The visible message array is a projection, not the complete authoritative conversation representation.

Current detail evidence supplies `current_node`, so the Active branch retains that branch-tip identity instead of throwing it away. Before production Send, the Send probe must establish whether parent/message/request identities beyond this are required.

Do not retain multi-megabyte raw detail JSON just for convenience and do not invent a complete future graph before evidence.

### Per-conversation recovery ownership

`同步最新消息` and `重载当前会话` always target one captured authoritative conversation ID.

- Sync A never resends, preserves loaded A on failure when applicable, and does not mutate B/C.
- Reload A deliberately rebuilds A and may supersede/cancel only A's older detail operation.
- A loaded resident may stay visible while Sync is in flight, but A -> B -> A must either restore/observe A's active Sync or receive its terminal repository update; returning to A must not freeze the old projection after repository A advances.
- Lightweight recovery presentation state may be per conversation/operation, but it is never a second conversation-data authority.

Future Sync/Reload interaction with active response streams follows Send/Stream evidence rather than guesses.

### List freshness/account isolation

Conversation-list state belongs to the verified account scope too.

- Old-scope list callbacks cannot repopulate the new account.
- Same-scope overlapping refreshes need deterministic freshness/generation semantics at the owner before repository callers can overlap.
- UIKit `loading` state must also reject stale completion so an old request cannot mark a newer list load idle.
- First-page refresh/reordering does not evict resident detail merely because an ID is absent from the first 28 items.

Pagination remains a later Work.

### New-conversation identity handoff

The future Send protocol probe must prove:

- whether conversation identity is client-generated or server-established;
- parent/current-node requirements;
- message/request/response identity lifecycle;
- when the new conversation is safe to insert into list/resident state.

If a temporary local presentation identity is needed, it gets **one explicit handoff** to authoritative conversation identity. Temporary and server identities must never remain independent state owners. Rapid double-send must not produce duplicate conversations/messages while handoff is unresolved.

### Per-conversation response ownership

Required future conceptual ownership:

`conversation identity + response/message identity -> response lifecycle`

A may continue reasoning/streaming while B is visible. Navigation never calls Stop merely because A became hidden.

Initial rule:

- at most one active response per conversation unless current protocol/runtime evidence proves same-conversation overlap;
- different conversations are architecturally independent;
- actual simultaneous A/B server streams remain **Unknown / Unverified** until real-device Send/Stream testing;
- Stop targets one exact response/conversation, never a global `isStreaming` state.

### Sync/Reload while a future response is active

Sync targets one conversation and reconciles server state without regressing newer local authoritative progress. Reload is stronger and must create a clear response-owner transition so old callbacks cannot resurrect overwritten state. Exact stream cancel/detach behavior follows current Send/Stream evidence, not planning guesses.

## Residency / memory policy

The project already has multi-megabyte / 2,000+ node conversations, so unlimited permanent resident detail is not acceptable.

Use a bounded LRU-style working set **after real-device measurement**.

- foreground entry is protected;
- active detail/recovery entry is protected from ordinary capacity eviction;
- future active response/stream entry is protected;
- recently used loaded entries remain resident for fast switching;
- inactive loaded entries become LRU candidates;
- memory warning may trim eligible resident terminal states through the same repository owner;
- no persistent chat-body disk cache is introduced by this Work.

Useful metrics include resident count, protected/in-flight count, visible-message count, timing and approximate text/count values. **Approximate text bytes are correlation only, not actual process-memory evidence and not sufficient alone to choose a capacity.**

A permanent normal-operation capacity is not Stable until exact real-device candidate evidence supports it.

## Diagnostics required for the multi-conversation runtime proof

Use privacy-safe correlation only:

- one explicit selection transition with old/new irreversible conversation hashes;
- resident hit/miss/state;
- detail operation started/coalesced/superseded/cancelled/completed;
- hidden valid result stored;
- obsolete completion rejected + reason;
- account-scope change/purge without raw account IDs;
- list request generation/stale discard where applicable;
- resident eviction + reason;
- protected/in-flight/resident counts;
- return-to-resident first-visible timing.

Never log raw conversation/account IDs, titles, bodies, payloads, Cookie/Authorization values or tokens.

## P1 implementation notes

### Per-conversation UI state

Within the live process preserve lightweight state such as semantic scroll anchor, unsent composer draft after composer exists, and reasoning-detail expanded state where useful. Avoid raw pixel-only restoration for long content that grows. Do not persist drafts/chat bodies to disk without a separate privacy/storage decision.

### Hidden-conversation response status

After Send/Stream exists, sidebar may derive thinking/generating and completed/unseen presentation from the response owner. It is not a second response authority or a claim about an OpenAI unread API.

### Central settings owner

The first real preference toggle establishes one small settings owner around `UserDefaults`/system state. View controllers consume it rather than invent independent keys/defaults.

### Multi-response background semantics

Background protection is over an active protected-response set. A finishing must not release protection while B remains active; completion notification is deduplicated per response lifecycle.

### Long-conversation timing

Before major performance rewrites, measure network completion, parse/model construction and first-visible presentation. Later add Markdown/layout phase timing. Existing end-to-end duration alone is not bottleneck proof.

## Additional correctness constraints

### Resident freshness

A resident conversation may change on another client. A newer list `update_time` may later be a stale hint, but it does not silently trigger a detail reload without a later accepted product rule. `同步最新消息` remains explicit reconciliation.

### `聊天` / `工作` derivation

UI requirement exists, but authoritative current service field remains Unverified. Do not infer it from title/UI text.

### Process death

In-memory residency may disappear after process termination/force quit. This is acceptable for the early client. Do not introduce persistent chat-body cache solely to survive process death.

### Network/rate-limit failures

Keep explicit failures observable. No reachability-driven resend, duplicate stream after network transition or speculative retry chain. Different-conversation concurrent Detail loads must be measured on device; no arbitrary global rate limiter is added preemptively.

## Testing gap

There is no test target today. Add only the smallest deterministic test support when justified and when project-file churn does not delay a useful candidate.

High-value pure tests include:

- resident state decisions;
- same-target coalescing + terminal waiter behavior;
- same-target replacement cancels only that target;
- stale-generation rejection;
- old-account callback rejection / stale-scope cannot be re-adopted;
- list freshness generation;
- account-scope purge;
- future LRU eligibility/protected entries;
- current-branch/node normalization.

Real-device evidence remains mandatory for actual networking, HTTP429 behavior, UI switching, memory behavior, WebKit auth and future streaming/background mechanisms.

## Post-recovery development sequence

Serialized core:

1. **`DEV-multi-conversation-state` — 多会话驻留与快速切换** — **Active**
   - Close current P0 account-scope/freshness/waiter/presentation/task-owner/execution-domain findings.
   - Produce a uniquely identified valid runtime Candidate; b16 is rejected and cannot be reused.
   - Test A/B/C navigation/in-flight coexistence and same-target recovery ownership on device.
   - Choose bounded normal resident capacity only after device evidence.
   - Do not delay the first valid core Candidate solely for semantic scroll restoration.
2. **`DEV-conversation-round-count` — 会话轮数显示 + 首个统一设置 owner**.
3. **`DEV-send-stream` — 消息发送、流式回复与推理交互**.
   - First capture current Send/new-conversation/stream/stop protocol evidence.
   - Define pending->authoritative new-conversation identity handoff.
   - Own responses by conversation/message identity; no global stream owner.
   - Integrate target-specific Sync/Reload ownership transitions.
   - As soon as text send/stream works on device, issue the earliest practical daily-chat Candidate.
4. `DEV-message-rendering`.
5. `DEV-conversation-pagination`.
6. `DEV-background-notify`.
7. `DEV-trollstore-true-background`.
8. `DEV-markdown-export`.
9. `DEV-long-conversation`.
10. `DEV-attachments`.
11. Remaining daily-use conversation features.
12. Advanced capabilities based on current evidence.

After Send/Stream owner is merged/stable, rendering, pagination and some settings/UI edges may parallelize only after normal branch/file/state-owner conflict scan. Background-notify depends on the accepted response lifecycle and must not be built against a duplicate/unmerged response owner.

## Acceptance mindset

Continue shipping small TrollStore candidates. A planning item blocks the next candidate only when it protects a core invariant that would otherwise make the candidate unsafe or cause immediate rework.

Do not wait for P1/P2 breadth before using the App. CI/Artifact never substitutes for Runtime evidence.
