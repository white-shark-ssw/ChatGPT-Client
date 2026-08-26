# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27._

## Purpose

Support the user's normal workflow of keeping several ChatGPT development conversations in use at the same time without making UI navigation destroy already-loaded conversation state.

The key invariant is:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned response, or force A to reload merely because it is no longer selected.

This plan is a prerequisite for robust multi-conversation send/stream behavior.

See also `docs/project/CLIENT_ARCHITECTURE_GAP_REVIEW.md` for the broader pre-send/stream gap review and current post-recovery sequencing.

## Current evidence / problem

The current b9/main repository and active recovery PR #10 use a single-slot model:

- `selectedConversationID` identifies the foreground conversation;
- `selectedConversation` holds only one detail;
- `selectConversation(id:)` clears that detail when another ID is selected;
- if a detail request for A finishes after selection changed to B, the result is discarded as `selection_changed`;
- current detail parsing derives visible messages from `mapping/current_node` but does not retain `current_node`/graph relationships in the resident `ConversationDetail` result.

That behavior was acceptable for proving the first native-read path but is not the desired daily-use architecture.

## Planned Work

### Work ID

`DEV-multi-conversation-state`

### User-facing name

**多会话驻留与快速切换**

### Scheduling

Implement after the current manual recovery work is merged and before production send/stream becomes authoritative.

The intended ordering is:

1. `DEV-conversation-recovery` — including the user's cold-start background login-state verification requirement;
2. `DEV-multi-conversation-state`;
3. `DEV-conversation-round-count`;
4. `DEV-send-stream`.

Do **not** create a separate `DEV-auth-resume` task. The user's latest requirement assigns that cold-start verification/recovery path to the active conversation-recovery work: background/invisible WebKit-store verification first, visible foreground verification only after background failure evidence.

If the recovery branch later materially changes ownership/files, run the normal conflict scan before starting this Work.

## State ownership

### Account/workspace scope

Resident state must be scoped to the currently verified account/workspace context, not only a bare conversation ID.

Conceptually:

`account/workspace context + conversationID -> resident conversation state`

On explicit logout/account-context change:

- invalidate the old transient native session;
- clear old-account resident conversation/message/draft/response state;
- reject late callbacks that belong to the old account/context;
- never display old-account resident content under a newly verified account.

Exact account-scope key/type is not frozen here; use the accepted authentication/account owner when implemented.

### Conversation data

`ConversationRepository` remains the production conversation-data authority, but it must evolve from one loaded-detail slot to **per-conversation state keyed by authoritative identity inside the current account/workspace scope**.

Each resident entry may own:

- parsed/current conversation data needed to render that conversation;
- minimum current-branch/node identity needed by current protocol evidence;
- load/recovery freshness metadata owned by the repository;
- future response lifecycle linkage.

Exact Swift type/property names are not frozen by this planning document.

### Authoritative node identity

The user-visible message list is a projection, not the entire authoritative conversation representation.

Before production send/stream, retain the minimum detail identity proven necessary by the send protocol, such as `current_node`/parent/message-node identity if current evidence requires it.

Rules:

- do not throw away required identity and then issue a fresh detail request merely to recover it;
- do not retain raw multi-megabyte HTTP JSON payloads merely for convenience;
- normalize only evidence-backed node/branch metadata;
- keep visible messages derived from the authoritative conversation state.

### Foreground selection

The selected conversation ID remains only the **presentation selection**.

Changing selected ID must not mean deleting another conversation's model.

### UI/view state

Do not use retained view controllers/cells as the cache.

Lightweight per-conversation presentation state may be owned separately where needed, for example:

- unsent composer draft;
- semantic scroll anchor / last visible message identity;
- reasoning-detail expanded/collapsed presentation where appropriate;
- local hidden-completion/unseen presentation state after send/stream exists.

Use semantic message/anchor identity rather than only raw pixel offset when long content can grow.

Do not persist chat drafts/bodies to disk merely because in-memory residency exists. Cross-process persistence requires a separate privacy/storage decision.

### Future response/stream lifecycle

A response lifecycle must be keyed to its real conversation/message identity, never to whichever conversation is currently visible.

Example:

- A starts reasoning/streaming;
- user switches to B;
- A continues through the same response owner;
- B can be read or can later start its own independent response if current protocol/runtime evidence allows;
- A updates A's resident model while hidden;
- returning to A shows current A state without reconstructing the response from UI state.

Switching UI selection must never call stop/cancel on another conversation's response simply because it became hidden.

Initial concurrency rule:

- architecturally support independent responses in different conversations;
- assume at most one active response per conversation unless current protocol/runtime evidence explicitly proves same-conversation overlap is valid;
- actual simultaneous A/B server-stream support remains Unknown / Unverified until `DEV-send-stream` real-device testing;
- Stop targets one exact response/conversation, never a global streaming flag.

## Async freshness / race protection

Removing the old `selection_changed` discard is necessary but not sufficient.

A valid old operation must not regress a newer authoritative state.

Examples:

- ordinary load A starts, then explicit reload A starts; old load must not overwrite the newer reload result;
- sync A starts while A is streaming; an older server snapshot must not blindly overwrite later local stream progress;
- stop/cancel becomes terminal; late stream callbacks must not resurrect the response;
- account changes while an old request is in flight; old-account data must never populate the new context.

Required direction:

- bind every async operation to its account/context + target conversation identity;
- use a per-conversation load/reload generation, operation token or another single-owner freshness mechanism to reject obsolete completions;
- this freshness guard is not a second conversation state authority;
- selection change alone is not a discard reason;
- coalesce equivalent in-flight detail loads where the current owner can do so cleanly instead of issuing duplicate requests;
- no arbitrary timer/watchdog/retry loop is introduced for this purpose.

## Read/load behavior

### First open

If a conversation has no resident detail, request it normally and store the successful result under that conversation ID/account scope.

If an equivalent load is already in flight, reuse/coalesce that operation instead of starting another equivalent request when practical.

### Switch while request is in flight

If A is loading and the user selects B:

- A's request may continue;
- B may start/load independently;
- successful A data is stored under A even though A is no longer foreground;
- returning to A uses the stored result rather than starting a duplicate request.

A stale request must still be rejected if it fails identity/account/freshness checks, but **selection change alone is not a reason to discard valid data**.

### Return to an already resident conversation

Render the resident model immediately.

Do not issue a fresh detail request solely because the user navigated A -> B -> A.

Freshness remains explicit:

- `同步最新消息` = reconcile that conversation with current server state;
- `重载当前会话` = discard/rebuild that conversation deliberately.

This avoids turning ordinary navigation into hidden network traffic.

### Resident server freshness signal

The conversation list already exposes `update_time`.

A later implementation may use a newer list `update_time` as a **stale hint** for a resident conversation, but not as permission to silently reload it.

- mark/diagnose potential staleness if evidence supports it;
- `同步最新消息` remains the explicit reconciliation action unless a later product rule accepts automatic freshness behavior.

## Recovery semantics in the multi-conversation model

Recovery actions always target the authoritative conversation ID that the user invoked them on.

- Sync A updates A only.
- Reload A clears/rebuilds A only.
- B/C resident states remain untouched.
- A recovery must not change another conversation's selection, stream or draft.

### Sync while A is active

- sync may fetch server detail without resending the prompt;
- reconciliation must not regress newer local authoritative progress;
- if server evidence proves A is already complete, the local stale response can transition to that server-backed terminal state and obsolete callbacks must no longer mutate it;
- if server still reports an in-progress state, keep the response owner unless current protocol evidence provides a terminal reason.

### Reload while A is active

Reload is stronger and user-explicit.

- define one clear response-owner transition so an old stream cannot later overwrite/revive the reloaded state;
- do not resend/regenerate;
- exact cancel/detach behavior must follow actual send/stream protocol evidence rather than being guessed before `DEV-send-stream`.

## Hidden-conversation status

After production streaming exists, the sidebar may derive lightweight status from the response owner:

- thinking/generating indicator while a hidden conversation has an active response;
- completed/unseen marker when a hidden response reaches final state;
- clear according to accepted UI behavior when the user views that conversation.

This is presentation state only. It is not an OpenAI server-side unread authority and must not own the response lifecycle.

## Residency / memory policy

The project has real conversations measured at several MB and more than 2,000 mapping nodes, so unlimited retention of every opened conversation is not acceptable.

Use a bounded resident working set.

Rules:

- the foreground conversation is resident;
- any conversation with an active owned response/stream is protected from ordinary eviction;
- recently used loaded conversations remain resident so normal A/B/C switching is instant;
- non-streaming least-recently-used conversation models are the first eviction candidates when the bound is exceeded or memory pressure requires release;
- UIKit cells/view controllers are never the retained cache;
- raw HTTP payloads should not be retained after parsing unless later evidence proves they are required;
- presentation/render caches should be releasable independently from the minimum authoritative model where practical.

Do **not** freeze an arbitrary permanent cache count during planning. Choose the first concrete bound from real-device measurements on the target iPhone/iOS 17.0 baseline, then document it as evidence.

A useful validation target is repeated switching among several development conversations, including at least one large conversation, without repeat detail requests after their first successful load.

## Memory warning / process lifecycle

A system memory warning may evict non-active, non-streaming resident conversation models. That is different from ordinary navigation and is acceptable when logged/observable.

If iOS terminates the whole process, in-memory residency is naturally lost. This plan does not introduce persistent on-disk chat-body caching merely to survive process death; such persistence would require its own privacy/storage requirement and evidence.

## Diagnostics

Add privacy-safe events sufficient to prove behavior without logging raw conversation IDs or bodies, for example:

- resident cache hit/miss;
- load started/completed for hashed conversation identity;
- in-flight equivalent load reused/coalesced;
- obsolete async result discarded + reason (`operation_superseded` / `account_changed` / identity mismatch);
- valid hidden-conversation load stored rather than discarded;
- selection switched A/B;
- resident entry evicted + reason (`capacity` / `memory_warning`);
- active response protected from eviction;
- return-to-resident first-visible timing;
- hidden response status transition.

Reuse the accepted short irreversible conversation hash/list-position diagnostics convention.

## Acceptance criteria

At minimum real-device acceptance should prove:

1. Load A, load B, return A: A renders without a new detail request.
2. A detail request finishing while B is selected is retained for A, not discarded merely due to selection change.
3. A/B/C switching never shows another conversation's messages, title, round count, draft or scroll state.
4. Manual sync/reload affects only the target conversation.
5. A late older load/reload/sync completion cannot overwrite a newer authoritative A state.
6. Account/logout change prevents old-account resident data/late callbacks from appearing in the new context.
7. The resident model retains the minimum current-node/message identity required by the later accepted send protocol without retaining the raw payload.
8. Once send/stream exists, A can continue an owned response while B is foreground; switching does not cancel A.
9. Returning to a hidden actively-updating A shows its latest local stream state.
10. An actively streaming conversation is not removed by normal LRU eviction.
11. Memory-pressure eviction is bounded, observable and affects only eligible inactive/non-streaming entries.
12. Large-conversation residency is measured on real device before declaring the cache policy Stable.
13. If A/B concurrent streaming is supported by the current service, each response updates only its owning conversation and Stop targets only the selected response.

## Testing guidance

There is no XCTest target today. When implementing this Work, strongly prefer extracting deterministic state logic so a minimal test target can cover high-risk non-network behavior if adding the target is compatible with the task's conflict/build plan.

High-value pure tests include:

- resident lookup/hit/miss;
- LRU eligibility/protected active response;
- operation-generation stale-result rejection;
- account-scope purge;
- current-branch/node normalization;
- round-count derivation later.

Real-device evidence remains required for actual networking, UI switching, memory behavior and future stream concurrency.

## Non-goals / prohibited shortcuts

- Do not instantiate a separate authoritative `ConversationRepository` per screen/conversation.
- Do not keep one full UIKit hierarchy alive for every opened conversation to simulate caching.
- Do not use the current navigation controller stack as conversation-state authority.
- Do not cancel network/stream work merely on `viewDidDisappear` or selection change.
- Do not reload every time a conversation becomes visible.
- Do not retain an unlimited number of large conversations.
- Do not let old async completions regress a newer authoritative state.
- Do not carry resident conversation state across explicit account/logout changes.
- Do not add persistent chat-body disk caching unless a later explicit requirement establishes its privacy/storage contract.
