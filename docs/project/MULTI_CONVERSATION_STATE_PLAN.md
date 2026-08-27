# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27; refreshed after b16 CI and second source review._

## Purpose

Support normal use of several ChatGPT development conversations at the same time without making UI navigation destroy already-loaded state.

Core invariant:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned work merely because A became hidden, or force A to reload merely because A is no longer selected.

This Work is the structural prerequisite for production send/stream ownership.

See also `CLIENT_ARCHITECTURE_GAP_REVIEW.md` for broader pre-send requirements and the Active checkpoint `current/dev/DEV-multi-conversation-state.md` for exact branch/candidate evidence and next action.

## Accepted baseline vs Active implementation

### Accepted Stable baseline

`DEV-conversation-recovery-0.1.0-b15` is merged Stable for the recorded Plus/personal iPhone/iOS17 recovery scope. Current `main` baseline is `f155ddb873540f7c80d6e66ebbfeb59ded26f011`.

The accepted b15 runtime architecture intentionally uses one selected detail/generation/task owner. b15 proved the same-conversation explicit recovery replacement rule: a newer manual recovery owns a new generation, cancels the older selected-detail task before replacement, and stale callbacks cannot mutate current state.

### Active `DEV-multi-conversation-state` implementation

- Branch: `dev/multi-conversation-state-20260827`.
- Exact b16 product/config source: `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`.
- b16 Run `33009246356` succeeded, so that source compiled and packaged on CI.
- Artifact `9621830284` is **identity-rejected** before runtime because `scripts/build_ipa.sh` still emitted recovery-b15 candidate/slug values. b16 must never be reused.
- Active source already introduces one account-scoped/per-conversation repository direction, per-conversation detail generations/tasks, ordinary-load coalescing, failed terminal residency, single-flight repository auth acquisition, current-node retention, account reset/list guards and memory-warning trimming.
- **No multi-conversation runtime evidence exists yet.**

### Second source review — unresolved P0 findings

The first implementation is not yet candidate-ready despite b16 CI success:

1. a delayed old `ConversationTransportContext` can currently call `adoptAccountScope` and reset the repository back to an older scope after a newer verified account transition;
2. a queued probe result is not rechecked against the current `AuthSessionStore.verifiedAccountContext()` before installing repository session/scope;
3. superseded/account-reset detail operations remove collected completion closures without deterministic terminal completion;
4. ordinary detail presentation has no explicit presentation generation, so safely terminating superseded waiters needs a UI freshness guard too;
5. Sync A -> B -> A before Sync terminal can render the preserved old A resident, fail to attach to A's active Sync, then ignore the original Sync presentation callback, leaving visible A stale after repository A advances;
6. one global recovery presentation flag/generation prevents direct cross-conversation overwrite but does not restore per-conversation in-flight recovery presentation when returning to A;
7. list commits are account-scoped, but same-scope list generation/freshness and sidebar stale-completion presentation ownership are incomplete;
8. the already-resumed detail task handle is attached to operation state through a later main-queue hop, leaving an avoidable window against deterministic b15-style cancel-before-replace ordering;
9. mutable repository state is not fully confined to one execution domain because URLSession diagnostics paths can read `conversations` off-main;
10. planned runtime diagnostics still lack one explicit old->new hashed selection transition, return-to-resident first-visible timing and protected/in-flight counts.

These are P0 owner/correctness gaps for the first valid core multi-conversation Candidate. Semantic scroll-anchor restoration is P1 and does not block that first core Candidate.

## Work identity / ordering

- **Work ID**: `DEV-multi-conversation-state`
- **User-facing name**: **多会话驻留与快速切换**
- **Current branch**: `dev/multi-conversation-state-20260827`
- **Dependency**: merged b15 recovery baseline.
- **Next serialized tasks**: `DEV-conversation-round-count` -> `DEV-send-stream`.

Do not create a separate auth-resume task; cold-start WebKit warm-up is already accepted inside recovery.

## State ownership model

Conceptually:

`verified account/workspace scope -> conversation ID -> resident conversation state`

`ConversationRepository` remains the sole production conversation-data authority.

A resident/operation model may own only current-requirement data:

- parsed current conversation detail needed to render;
- directly evidenced current branch-tip/current-node identity;
- terminal loaded/failed state;
- load/recovery operation generation/task/waiters;
- later LRU metadata after a measured policy exists;
- future response linkage only when Send/Stream evidence exists.

Mounted cells/view controllers are never the conversation-data cache. Raw HTTP payloads are discarded after parsing unless later evidence establishes a concrete requirement.

Foreground `selectedConversationID` is presentation state only. Loading, Sync, Reload and future response operations target an identity and never mutate selection as a request side effect.

## Account/session ownership

`AuthSessionStore` remains the sole account-context/auth owner. Default persistent WebKit storage remains the sole persistent auth-secret authority.

Repository rules:

- only one repository account/transient-session acquisition is in flight at a time;
- concurrent A/B loads may share that acquisition;
- cached native transient session is bound to the verified scope that created it;
- a currently verified auth-owner snapshot may establish/change repository scope;
- an incoming list/detail/operation context is only a consumer and **must never re-adopt an older scope** after a newer verified context exists;
- before committing a queued probe result, verify the auth owner's current snapshot still matches that result;
- verified different scope purges old list/residents/operations/session/selection and rejects late old-scope results;
- obsolete waiters terminate deterministically rather than being silently abandoned.

Current active source uses `userID + accountID` as the resident account key. This is evidence-backed for current personal-account source only. Non-personal workspace identity remains Unknown / Unverified until current service evidence says whether another key is needed.

## Single repository execution domain

Mutable repository authority uses one explicit execution domain.

- resident dictionaries/state;
- conversations/list state;
- account-scope/session binding;
- detail/list operation generations/tasks/waiters;
- future LRU/protected-entry metadata.

Network transfer and expensive JSON parsing may occur off-main. Mutable repository reads/writes, including list-position lookup for diagnostics, must not race across URLSession and UIKit callbacks.

Do not create a second cache/state owner merely for thread safety.

## Detail operation ownership

Replace the old global selected-detail generation/task with conversation-targeted ownership.

Required semantics:

- A and B may have independent detail operations;
- selecting B does not cancel A;
- explicit Reload/Sync A may supersede/cancel only A's older detail operation;
- same-target replacement preserves the accepted b15 rule: cancel the old target task before starting the replacement request;
- B is untouched;
- equivalent missing-detail A loads coalesce instead of duplicating network work;
- operation identity includes current account scope + conversation ID + generation/token;
- late obsolete A cannot overwrite newer A;
- every collected waiter has a deterministic terminal result when the operation succeeds, fails, is superseded or is invalidated by account change.

Do not impose an arbitrary global concurrency limit before device evidence.

## Resident terminal state / navigation

Resident logic distinguishes semantics of:

- not loaded / evicted;
- active operation;
- loaded;
- terminal failure;
- explicit Sync/Reload operation over that target.

Exact Swift type names are not frozen; operation and terminal maps may together represent these semantics.

On A -> B:

1. update foreground selection exactly once at the navigation owner;
2. inspect B's resident/operation state;
3. loaded B renders immediately with no Detail request;
4. B already loading joins/observes the existing operation;
5. failed B renders retained failure and explicit Reload rather than silently retrying;
6. evicted/not-loaded B may start one normal load.

Returning B -> A follows the same rules.

A terminal failure remains failure across ordinary navigation. Explicit Reload is the retry/rebuild action.

## Recovery semantics in the multi-conversation model

Recovery is target-specific and user-explicit.

### Sync A

- targets A captured at invocation;
- never changes selection as a side effect;
- may supersede/cancel only A's older same-target detail operation;
- preserves loaded A on failure where accepted recovery semantics require it;
- does not mutate B/C.

If loaded A is preserved during active Sync, returning A -> B -> A before Sync terminal must render old A immediately **and remain attached to/aware of A's active Sync terminal**. When Sync succeeds while A is visible again, visible A must advance to the new resident result without another request.

### Reload A

- targets A captured at invocation;
- deliberately rebuilds A from server state;
- may clear A's loaded detail according to accepted reload semantics;
- supersedes/cancels only A's older target operation;
- never resends/regenerates;
- B/C stay resident and untouched.

### Recovery presentation

A single visible detail controller may own lightweight presentation state, but that state is keyed/validated by target conversation + operation/presentation generation.

- hidden A completion must not alter B toast/spinner/title/messages;
- returning to A while A recovery is active must not accidentally re-enable unlimited duplicate recovery taps or lose the terminal update;
- repository remains the data authority; UIKit presentation state never becomes a duplicate conversation store.

Future active-response Sync/Reload transitions follow actual Send/Stream protocol evidence rather than pre-send guesses.

## List freshness/account isolation

Conversation-list state belongs to the verified account scope.

- old-account list response cannot populate the new account;
- same-scope overlapping list refreshes need deterministic generation/freshness ownership before callers may overlap;
- sidebar/UI `loading` presentation must reject stale completions so an old request cannot mark a newer request idle;
- first-page refresh/reordering never destroys resident details merely because an ID is absent from the current first 28 items;
- list position remains diagnostics only, never identity.

Pagination remains later Work.

## Current-node identity

Detail validates and walks `mapping/current_node` to build the visible branch. Active multi-conversation source retains that directly evidenced branch-tip/current-node identity.

Rules:

- do not throw away current identity and issue another Detail merely to recover it later;
- do not retain raw multi-megabyte mapping just for convenience;
- do not guess parent/message/request/send graph requirements before Send protocol evidence.

## Residency / memory policy

Unlimited permanent residency is not acceptable because real conversations can be multi-megabyte / 2,000+ mapping nodes.

A bounded LRU-style normal working set will be chosen **after real-device measurement**.

Rules:

- foreground entry protected;
- active detail/recovery operation protected from ordinary capacity eviction;
- future active response/stream protected;
- recently used loaded conversations remain resident;
- inactive loaded conversations become LRU candidates once a normal capacity exists;
- memory warning may trim eligible inactive terminal states through repository owner;
- no persistent chat-body disk cache is introduced.

Current approximate visible-text-byte diagnostics are correlation data only. They are **not actual process-memory measurement and cannot alone justify/freeze a capacity**. Use exact real-device behavior, resident/protected counts, timing, system/device memory observation where available, memory warnings and large-conversation switching evidence.

Do not add future-only access-order bookkeeping until a concrete normal LRU policy is actually implemented.

## Diagnostics

For the first valid runtime Candidate, collect enough privacy-safe evidence to prove ownership rather than infer it:

- one explicit selection transition with old/new irreversible conversation hashes;
- resident hit/miss/state;
- detail started/coalesced/superseded/cancelled/completed;
- collected waiter count and deterministic terminal reason when superseded/account-invalidated;
- hidden valid result stored;
- obsolete completion rejected + reason;
- account-scope bind/change/purge without raw account IDs;
- list generation/stale discard as applicable;
- memory-warning/capacity eviction reason;
- resident/protected/in-flight counts;
- return-to-resident first-visible timing.

Never log raw conversation/account IDs, titles, bodies, payloads, Cookie/Authorization values or tokens.

## Acceptance criteria for this Work

Before calling multi-conversation residency Stable, real-device evidence should prove at minimum:

1. A loaded -> B loaded -> A: A renders without a new Detail request.
2. A loading -> select B -> A completes hidden: A result is retained; B UI is untouched.
3. A loading -> B -> A before completion: no duplicate A Detail request; A reaches one terminal result.
4. Rapid A/B/C switching never displays another conversation's title/messages/error/recovery feedback.
5. Sync A -> B -> A before Sync terminal: returning A observes the active Sync and visible A advances when Sync succeeds without another Detail request.
6. Explicit Reload/Sync A cancels/replaces only A's older same-target detail operation; B's request/state is untouched.
7. An obsolete A completion cannot overwrite newer A state; superseded waiters terminate without mutating stale UI.
8. A terminal failed load remains failed when navigating away/back; return does not silently retry.
9. Verified account change purges old list/resident/session/operations and rejects late old-scope callbacks; an old operation context cannot re-adopt the previous scope.
10. Concurrent first loads share one account/transient-session acquisition rather than creating duplicate repository probes/sessions.
11. List old-scope/superseded callbacks do not reset or overwrite a newer list request's data/presentation state.
12. Resident model retains current-node identity without raw mapping payload retention.
13. Memory warning/capacity eviction affects only eligible inactive entries and is observable.
14. Several real development conversations, including at least one large one, switch repeatedly without unbounded memory growth or repeat requests for still-resident entries.
15. Rapid different-conversation in-flight loads record whether service-side rate pressure exists; no speculative retry/global rate limiter is used.
16. Accepted b15 manual Sync/Reload semantics remain functionally intact for the selected target.

Account/workspace runtime evidence beyond the current personal account remains separately Unknown until a real supported switch/workspace route is established and tested.

Future Send/Stream acceptance separately proves A streaming while B is visible and actual simultaneous A/B response support.

## First valid Candidate boundary

The first valid core runtime Candidate should include only what protects P0 ownership/correctness and exact artifact identity:

- stale-scope rejection / current-auth-owner verification;
- deterministic waiter termination + matching UI presentation freshness;
- hidden Sync return correctness;
- list freshness/presentation correctness needed for account isolation;
- deterministic task-handle ownership preserving b15 replacement ordering;
- one repository execution domain;
- missing privacy-safe selection/timing evidence needed for the runtime test;
- corrected unique build/candidate/IPA identity.

**Semantic scroll-anchor restoration is P1 and should not delay this first core Candidate.** Add it after core runtime evidence unless explicit user priority changes.

Because CI triggers on product/Xcode/script/workflow pushes, build/candidate-defining changes for one Candidate must be committed atomically enough that one build identity maps to one intended product/config source. b16 already exists and cannot be reused.

## Deterministic testing guidance

There is no XCTest target yet. If a minimal test target can remain isolated and does not delay the first useful Candidate materially, highest-value pure tests are:

- resident hit/miss/failed/evicted decisions;
- same-A load coalescing and waiter termination;
- Reload/Sync A cancels A only, not B;
- per-conversation stale-generation rejection;
- stale old account context cannot re-adopt scope;
- account-scope purge / late old-scope rejection;
- single-flight transient-session acquisition;
- list generation/freshness;
- later LRU eligibility/protected operations;
- current-branch/node normalization.

Real-device tests remain mandatory for actual networking, HTTP429 behavior, UI switching, account/WebKit behavior, memory pressure and performance.

## Non-goals / prohibited shortcuts

- No separate authoritative `ConversationRepository` per screen/conversation.
- No retained UIKit hierarchy per conversation as the cache.
- No navigation stack as conversation-state authority.
- No load/sync/reload method that changes foreground selection merely because it targets an ID.
- No cancellation merely because a conversation becomes hidden.
- No stale operation context restoring an old account scope.
- No silently abandoned coalesced waiters as the final contract.
- No reload on every navigation.
- No unlimited resident detail retention.
- No persistent chat-body/draft cache without a separate privacy/storage requirement.
- No speculative retry, timer, watchdog, fallback, global rate limiter or compatibility shim.
- No copied persistent auth secrets or second account owner.
- No raw mapping retention merely to anticipate future Send/Edit/Regenerate.
- No capacity chosen from approximate text bytes alone.
- No claim that concurrent A/B server operations are safe/unsafe until exact runtime evidence exists.
