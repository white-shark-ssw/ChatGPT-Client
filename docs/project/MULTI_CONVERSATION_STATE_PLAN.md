# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27; source-level review refreshed from merged b15 recovery baseline._

## Purpose

Support normal use of several ChatGPT development conversations at the same time without making UI navigation destroy already-loaded state.

Core invariant:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned work, or force A to reload merely because A is no longer selected.

This Work is the structural prerequisite for production send/stream ownership.

See also `CLIENT_ARCHITECTURE_GAP_REVIEW.md` for the broader pre-send requirements.

## Current accepted baseline

`DEV-conversation-recovery-0.1.0-b15` is merged Stable for the recorded Plus/personal iPhone/iOS17 recovery scope. Current `main` baseline is `f155ddb873540f7c80d6e66ebbfeb59ded26f011` after recovery checkpoint completion.

The accepted b15 source still intentionally uses a single-selected conversation model:

- `selectedConversationID` = foreground identity;
- `selectedConversation` = one loaded detail;
- one global `selectedDetailOperationGeneration`;
- one global selected-detail task/generation slot;
- one cached `AuthTransientSession` not yet bound to a repository-visible account-scope identity.

b15 proved same-conversation explicit recovery replacement: the newer generation takes ownership, cancels the old selected-detail task, and stale callbacks cannot mutate current state. Multi-conversation must generalize that accepted lifecycle rather than replace it with retry/fallback machinery.

## Work identity / ordering

- **Work ID**: `DEV-multi-conversation-state`
- **User-facing name**: **多会话驻留与快速切换**
- **Current branch**: `dev/multi-conversation-state-20260827`
- **Dependency**: merged b15 recovery baseline.
- **Next serialized tasks**: `DEV-conversation-round-count` -> `DEV-send-stream`.

Do not create a separate auth-resume task; cold-start WebKit warm-up is already accepted inside the recovery baseline.

## Concrete source gaps found before implementation

### 1. Foreground selection currently has multiple write paths

Current source mutates selection from all of these paths:

- sidebar row selection calls `repository.selectConversation(id:)`;
- detail `showConversation(id:)` calls `repository.selectConversation(id:)` again;
- repository `loadConversation(id:)` directly assigns `selectedConversationID = id`.

That is unsafe once hidden conversations may continue loading.

Required invariant:

- exactly one explicit UI/navigation transition owns foreground selection;
- loading, syncing, reloading or later streaming **by conversation ID must never change foreground selection as a side effect**;
- capture/persist any outgoing lightweight UI state before the selected ID changes;
- do not let duplicate selection calls become LRU/access-generation side effects.

### 2. Repository mutable state needs one execution domain

Current URLSession/account callbacks and UI calls can touch request/session bookkeeping from different callback contexts. A resident dictionary/LRU/request registry must not rely on incidental thread timing.

Required direction:

- choose one authoritative execution domain for mutable repository state, preferably consistent with existing main-thread UI ownership unless implementation evidence justifies a dedicated serial owner;
- resident entries, operation generations/tasks, LRU metadata, account-scope binding and cached-session state mutate only on that domain;
- network transfer and expensive JSON parsing may occur off-main;
- commit parsed results back through the one repository owner.

Do not create a second cache/state authority merely for thread safety.

### 3. Account/session acquisition must be scope-bound and single-flight

Current `withTransientSession` can start more than one `probeAccountContext` if A/B requests arrive before the cached transient session exists. Multi-conversation makes that race realistic.

Required direction:

- only one account-context/transient-session acquisition may be in flight for the repository at a time;
- concurrent conversation loads wait for/share that result rather than independently creating sessions;
- the cached transient session is bound to the verified account/workspace scope that created it;
- when a newly verified account/workspace scope differs, invalidate the old transient session, resident/list state and old operations before new data is committed;
- old-scope callbacks are rejected even if a conversation ID string matches;
- WebKit remains the sole persistent auth-secret authority; no copied-secret persistence.

`AuthSessionStore` currently keeps `accountContext` private, so implementation needs the smallest read-only/snapshot or change signal required for repository isolation. Do not move account ownership into `ConversationRepository`.

### 4. Detail operation ownership becomes per conversation

Replace the single selected-detail generation/task slot with conversation-targeted operation ownership.

Required semantics:

- A and B may have independent detail operations;
- selecting B does not cancel A;
- explicit Reload/Sync A may supersede/cancel only A's older detail operation;
- B is untouched;
- an equivalent missing-detail request for A is coalesced instead of duplicated;
- a late obsolete A result cannot overwrite newer A state;
- operation identity includes account scope + conversation ID + generation/token.

Do not impose an arbitrary global concurrency limit before current service/runtime evidence.

### 5. Coalescing must have a terminal-result contract

If A is already loading and the user navigates A -> B -> A before A completes, returning to A must attach to/render the existing operation.

Coalescing is not allowed to strand a caller or spinner.

Implementation may use waiters or repository state observation, but there must be one clear contract:

- all still-relevant consumers see the terminal loaded/failed state;
- hidden A completion is stored under A and does not mutate B's presentation;
- obsolete/superseded consumers terminate cleanly.

### 6. Resident entries need explicit load state, not only optional detail

A missing `ConversationDetail?` cannot represent all cases safely once navigation no longer reloads every time.

Resident state must distinguish at least the semantics of:

- not loaded / locally evicted;
- loading;
- loaded;
- terminal load failure;
- explicit reload/rebuild in progress.

Exact Swift enum/type names are not frozen.

Important behavior:

- returning to a previously failed A shows A's retained failure and explicit Reload;
- ordinary navigation must not become an implicit network retry;
- returning to an evicted A may perform a normal load because eviction is not a prior server/network failure;
- Sync failure preserves an already loaded A when current recovery semantics require preservation.

### 7. Current recovery presentation state is global to the visible detail controller

`ConversationDetailViewController` currently has one `recoveryActionInProgress`, one toast, one hide work item and one visible `messages` projection.

In a multi-conversation world, a late hidden A completion must never hide/reset B's toast, menu state, spinner, title or visible messages.

Required direction:

- target feedback by selected conversation + operation identity, or derive it from the selected resident operation state;
- a completion for hidden A updates A's repository state only;
- UIKit-local `messages` remains a render projection of the selected resident state, never a second conversation authority.

### 8. `current_node` is validated then discarded

Current parsing validates `current_node` and uses it to derive the active branch, then `ConversationDetail` stores only ID/title/visible messages.

For this Work, retain the directly evidenced active branch-tip/current-node identity as small authoritative metadata in the resident detail/state.

Do **not** store the raw multi-megabyte mapping or invent a complete send/branch graph before Send protocol evidence proves what else is required.

### 9. List results also need account/freshness isolation

Conversation-list state belongs to the same verified account/workspace boundary.

Required behavior:

- an old-account list response cannot repopulate the repository after account scope changes;
- list operation freshness is deterministic if future refreshes overlap;
- first-page refresh/reordering does not destroy resident details merely because an ID is absent from the current 28-item page;
- list position remains diagnostic metadata only, never conversation identity.

Pagination remains its own later Work.

### 10. In-flight work participates in residency/eviction policy

Ordinary LRU capacity eviction must not silently drop:

- the foreground conversation;
- a conversation with an active detail/recovery operation;
- a future conversation with an active response/stream.

If severe memory pressure later requires cancelling a hidden in-flight detail load, that path must have an explicit cancellation/consumer-terminal policy and diagnostics. Do not silently remove its operation record and leave UI waiters hanging.

### 11. Memory-warning plumbing is currently missing

`AppDelegate.applicationDidReceiveMemoryWarning` currently only logs. The repository itself is owned inside `RootViewController`.

This Work must route the system memory-pressure signal to the authoritative repository so it can trim only eligible resident entries. The signal route must not create a second cache owner.

### 12. Different-conversation concurrency needs real-device evidence

b15's HTTP429 evidence concerned overlapping replacement requests for the same selected conversation; b15 fixed that by cancelling the obsolete request before replacement.

Multi-conversation intentionally allows A/B detail requests to coexist. Therefore real-device acceptance must include rapid A -> B -> C selection while earlier details are still in flight.

Record:

- HTTP status per hashed conversation target;
- cancellation/replacement reason;
- whether A/B/C complete and remain resident;
- any HTTP429/rate-pressure signal;
- memory/first-return timing.

If a cross-conversation concurrency limit later becomes necessary, it must be justified by that evidence. No speculative retry or arbitrary global serialization now.

## State ownership model

Conceptually:

`verified account/workspace scope -> conversation ID -> resident conversation state`

`ConversationRepository` remains the sole production conversation-data authority.

A resident entry may own only the data needed for current requirements:

- current parsed/detail state;
- directly evidenced current-node/branch-tip identity;
- load/recovery operation state and freshness token;
- last-access/LRU metadata;
- lightweight future response linkage;
- lightweight presentation state only where the architecture chooses a single clear owner.

Mounted cells/view controllers are never the resident cache. Raw HTTP payloads are discarded after parsing unless later evidence establishes a concrete need.

## Selection and rendering

Foreground `selectedConversationID` is presentation state only.

On A -> B:

1. capture A's lightweight presentation state if current scope implements it;
2. update selection once;
3. inspect B's resident state;
4. if B is loaded, render immediately with no detail request;
5. if B is loading, render B's loading state and join/observe the existing operation;
6. if B previously failed, render B's retained failure and explicit Reload;
7. if B is not loaded/was evicted, start one normal B load.

Returning B -> A follows the same rules; resident A is shown immediately.

## Recovery semantics

Recovery remains target-specific and user-explicit.

### Sync A

- targets A captured at invocation;
- never changes selection as a request side effect;
- may replace only A's older equivalent detail operation according to b15-style same-target ownership;
- preserves loaded A on failure where accepted recovery semantics require it;
- does not mutate B/C.

### Reload A

- targets A captured at invocation;
- deliberately rebuilds A from server state;
- may clear A's loaded detail according to accepted reload semantics;
- supersedes/cancels only A's older detail operation;
- never resends/regenerates;
- B/C stay resident and untouched.

Future active-response Sync/Reload transitions remain defined by current Send/Stream evidence, not guessed here.

## Residency / memory policy

The repository has real multi-megabyte, 2,000+ node conversations, so unlimited permanent residency is not acceptable.

Use a bounded LRU-style working set after real-device measurement.

Rules:

- foreground entry protected;
- active detail/recovery entry protected from ordinary capacity eviction;
- future active response/stream entry protected;
- recently used loaded entries remain resident for fast A/B/C switching;
- inactive loaded entries are LRU eviction candidates;
- terminal failed entries are lightweight and may be retained without holding large message payloads if implementation makes that natural;
- memory warning trims eligible entries through the repository owner;
- no persistent chat-body disk cache is introduced by this Work.

Do not freeze a permanent capacity number before real-device measurement. The first concrete capacity becomes evidence only after the exact Candidate is tested with multiple real development conversations.

Useful privacy-safe capacity diagnostics include resident count, eligible/protected counts, total visible-message count and approximate text/count metrics; never log bodies/raw IDs.

## Diagnostics

Add enough evidence to distinguish navigation, cache, operation and account-scope behavior:

- selection changed once + old/new conversation hashes;
- resident hit/miss/state;
- detail operation started/coalesced/superseded/cancelled/completed;
- account-scope bind/change/purge using safe hashed/non-secret identity metadata;
- hidden-conversation result stored;
- obsolete completion rejected + reason;
- resident eviction + reason (`capacity` / `memory_warning`);
- protected operation prevented from eviction;
- return-to-resident first-visible timing;
- resident/protected counts for real-device capacity tests.

Do not log raw conversation/account IDs, titles, bodies, payloads, Cookie/Authorization values or tokens.

## Acceptance criteria for this Work

Before calling multi-conversation residency Stable, real-device evidence should prove at minimum:

1. A loaded -> B loaded -> A: A renders without a new Detail request.
2. A is still loading -> select B -> A completes hidden: A result is retained; B UI is untouched.
3. A still loading -> B -> return A before completion: no duplicate A Detail request; A reaches one terminal result.
4. Rapid A/B/C switching never displays another conversation's title/messages/error/recovery feedback.
5. Explicit Reload/Sync A cancels/replaces only A's older same-target detail operation; B's request/state is untouched.
6. An obsolete A completion cannot overwrite newer A state.
7. A terminal failed load remains failed when navigating away/back; returning does not silently retry.
8. Verified account/workspace change purges old list/resident/session/operations and rejects late old-scope callbacks.
9. Concurrent first loads share one account/transient-session acquisition rather than creating duplicate account probes/sessions.
10. The resident model retains current-node/branch-tip identity without retaining raw mapping payloads.
11. Memory warning/capacity eviction affects only eligible inactive entries and is observable.
12. Several real development conversations, including at least one large one, can be switched repeatedly without unbounded memory growth or repeat requests for still-resident entries.
13. Rapid different-conversation in-flight loads record whether service-side rate pressure exists; no speculative retry is used.
14. Current b15 manual Sync/Reload behavior remains functionally intact for the selected target.

Future Send/Stream acceptance separately proves A streaming while B is visible and actual simultaneous A/B response support.

## Deterministic testing guidance

There is no XCTest target yet. If adding a minimal test target can remain isolated and does not delay the first Candidate materially, highest-value pure tests are:

- selection changes only through the explicit selection path;
- resident hit/miss/failed/evicted state decisions;
- same-A load coalescing;
- Reload A cancels A only, not B;
- per-conversation stale-generation rejection;
- account-scope purge/late-old-scope rejection;
- single-flight transient-session acquisition state machine;
- LRU eligibility/protected in-flight entries.

Real-device tests remain mandatory for real networking, HTTP429 behavior, UI switching, memory pressure and performance.

## Non-goals / prohibited shortcuts

- No separate authoritative repository per screen/conversation.
- No retained UIKit hierarchy per conversation as the cache.
- No navigation stack as conversation-state authority.
- No load/sync/reload method that changes foreground selection merely because it targets an ID.
- No cancellation merely because a conversation becomes hidden.
- No reload on every navigation.
- No unlimited resident detail retention.
- No persistent chat-body/draft cache without a separate privacy/storage requirement.
- No speculative retry, timer, watchdog, fallback, global rate limiter or compatibility shim.
- No copied persistent auth secrets or second account owner.
- No raw mapping retention merely to anticipate future Send/Edit/Regenerate.
- No claim that concurrent A/B server operations are safe/unsafe until the exact Candidate produces runtime evidence.
