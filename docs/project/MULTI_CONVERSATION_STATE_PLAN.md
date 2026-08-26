# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27._

## Purpose

Support the user's normal workflow of keeping several ChatGPT development conversations in use at the same time without making UI navigation destroy already-loaded conversation state.

The key invariant is:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned response, or force A to reload merely because it is no longer selected.

This plan is a prerequisite for robust multi-conversation send/stream behavior.

## Current evidence / problem

The current b9/main repository and active recovery PR #10 use a single-slot model:

- `selectedConversationID` identifies the foreground conversation;
- `selectedConversation` holds only one detail;
- `selectConversation(id:)` clears that detail when another ID is selected;
- if a detail request for A finishes after selection changed to B, the result is discarded as `selection_changed`.

That behavior was acceptable for proving the first native-read path but is not the desired daily-use architecture.

## Planned Work

### Work ID

`DEV-multi-conversation-state`

### User-facing name

**多会话驻留与快速切换**

### Scheduling

Implement after the current manual recovery work is merged and before production send/stream becomes authoritative.

The intended ordering is:

1. `DEV-conversation-recovery`
2. `DEV-multi-conversation-state`
3. `DEV-conversation-round-count`
4. `DEV-send-stream`

If the recovery branch later materially changes ownership/files, run the normal conflict scan before starting this Work.

## State ownership

### Conversation data

`ConversationRepository` remains the production conversation-data authority, but it must evolve from one loaded-detail slot to **per-conversation state keyed by authoritative conversation ID**.

Conceptually:

`conversationID -> resident conversation state`

Each resident entry may own the parsed/current conversation data needed to render that conversation. Exact Swift type/property names are not frozen by this planning document.

### Foreground selection

The selected conversation ID remains only the **presentation selection**.

Changing selected ID must not mean deleting another conversation's model.

### UI/view state

Do not use retained view controllers/cells as the cache.

Lightweight per-conversation presentation state may be owned separately where needed, for example:

- unsent composer draft;
- scroll anchor / last visible message identity;
- reasoning-detail expanded/collapsed presentation where appropriate.

Exact ownership should be chosen from real source when implemented so there is only one authority for each value.

### Future response/stream lifecycle

A response lifecycle must be keyed to its real conversation/message identity, never to whichever conversation is currently visible.

Example:

- A starts reasoning/streaming;
- user switches to B;
- A continues through the same response owner;
- B can be read or can later start its own independent response if current protocol/product constraints allow;
- A updates A's resident model while hidden;
- returning to A shows current A state without reconstructing the response from UI state.

Switching UI selection must never call stop/cancel on another conversation's response simply because it became hidden.

## Read/load behavior

### First open

If a conversation has no resident detail, request it normally and store the successful result under that conversation ID.

### Switch while request is in flight

If A is loading and the user selects B:

- A's request may continue;
- B may start/load independently;
- successful A data is stored under A even though A is no longer foreground;
- returning to A uses the stored result rather than starting a duplicate request.

A stale request must still be rejected if it does not match its own authoritative conversation identity, but **selection change alone is not a reason to discard valid data**.

### Return to an already resident conversation

Render the resident model immediately.

Do not issue a fresh detail request solely because the user navigated A -> B -> A.

Freshness remains explicit:

- `同步最新消息` = reconcile that conversation with current server state;
- `重载当前会话` = discard/rebuild that conversation deliberately.

This avoids turning ordinary navigation into hidden network traffic.

## Recovery semantics in the multi-conversation model

Recovery actions always target the authoritative conversation ID that the user invoked them on.

- Sync A updates A only.
- Reload A clears/rebuilds A only.
- B/C resident states remain untouched.
- A recovery must not change another conversation's selection, stream or draft.

## Residency / memory policy

The project has real conversations measured at several MB and more than 2,000 mapping nodes, so unlimited retention of every opened conversation is not acceptable.

Use a bounded resident working set.

Rules:

- the foreground conversation is resident;
- any conversation with an active owned response/stream is protected from ordinary eviction;
- recently used loaded conversations remain resident so normal A/B/C switching is instant;
- non-streaming least-recently-used conversation models are the first eviction candidates when the bound is exceeded or memory pressure requires release;
- UIKit cells/view controllers are never the retained cache;
- raw HTTP payloads should not be retained after parsing unless later evidence proves they are required.

Do **not** freeze an arbitrary permanent cache count during planning. Choose the first concrete bound from real-device measurements on the target iPhone/iOS 17.0 baseline, then document it as evidence.

A useful validation target is repeated switching among several development conversations, including at least one large conversation, without repeat detail requests after their first successful load.

## Memory warning / process lifecycle

A system memory warning may evict non-active, non-streaming resident conversation models. That is different from ordinary navigation and is acceptable when logged/observable.

If iOS terminates the whole process, in-memory residency is naturally lost. This plan does not introduce persistent on-disk chat-body caching merely to survive process death; such persistence would require its own privacy/storage requirement and evidence.

## Diagnostics

Add privacy-safe events sufficient to prove behavior without logging raw conversation IDs or bodies, for example:

- resident cache hit/miss;
- load started/completed for hashed conversation identity;
- valid hidden-conversation load stored rather than discarded;
- selection switched A/B;
- resident entry evicted + reason (`capacity` / `memory_warning`);
- active response protected from eviction;
- return-to-resident first-visible timing.

Reuse the accepted short irreversible conversation hash/list-position diagnostics convention.

## Acceptance criteria

At minimum real-device acceptance should prove:

1. Load A, load B, return A: A renders without a new detail request.
2. A detail request finishing while B is selected is retained for A, not discarded merely due to selection change.
3. A/B/C switching never shows another conversation's messages, title, round count, draft or scroll state.
4. Manual sync/reload affects only the target conversation.
5. Once send/stream exists, A can continue an owned response while B is foreground; switching does not cancel A.
6. Returning to a hidden actively-updating A shows its latest local stream state.
7. An actively streaming conversation is not removed by normal LRU eviction.
8. Memory-pressure eviction is bounded, observable and affects only eligible inactive/non-streaming entries.
9. Large-conversation residency is measured on real device before declaring the cache policy Stable.

## Non-goals / prohibited shortcuts

- Do not instantiate a separate authoritative `ConversationRepository` per screen/conversation.
- Do not keep one full UIKit hierarchy alive for every opened conversation to simulate caching.
- Do not use the current navigation controller stack as conversation-state authority.
- Do not cancel network/stream work merely on `viewDidDisappear` or selection change.
- Do not reload every time a conversation becomes visible.
- Do not retain an unlimited number of large conversations.
- Do not add persistent chat-body disk caching unless a later explicit requirement establishes its privacy/storage contract.
