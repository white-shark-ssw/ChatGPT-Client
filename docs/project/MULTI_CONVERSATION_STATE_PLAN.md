# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27; completed through PR #23 merge / Stable b21 read-state baseline._

## Purpose

Support normal use of several ChatGPT development conversations at the same time without making UI navigation destroy already-loaded state.

Core invariant:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned work merely because A became hidden, or force A to reload merely because A is no longer selected.

This Work is complete for the recorded Plus/personal iPhone/iOS17 read-state scope and is the structural prerequisite for later production Send/Stream ownership. Exact historical candidate/evidence remains in `BUILD_TEST_INDEX.md`; broader pre-Send gaps remain in `CLIENT_ARCHITECTURE_GAP_REVIEW.md`.

## Stable merged baseline and final Candidate

### Recovery baseline

`DEV-conversation-recovery-0.1.0-b15` is merged Stable for recorded Plus/personal iPhone/iOS17 recovery scope.

### Historical b16

b16 source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08` compiled, but Artifact `9621830284` embedded the wrong recovery candidate/slug and was rejected before Runtime. Source review also found owner/race gaps. Never reuse b16.

### b17 core Runtime evidence

Exact b17 source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`, Run `33045536770`, Artifact `9635486304`.

Accepted on iPhone/iOS17:

1. resident A -> B -> A without navigation-only Detail refetch;
2. hidden valid completion retained;
3. returning to in-flight same target coalesces;
4. Sync A -> B -> A rejoins same active Sync;
5. rapid different-conversation overlap reached three active operations without HTTP429 in supplied export.

The same run reproduced the historical-scroll defect.

### b18 historical-scroll Runtime evidence

Exact b18 source `f30c13b4ac2c40dcda829585682825ca906dceae`, Run `33054012226`, Artifact `9638821912`.

Exact iPhone/iOS17 Runtime accepted historical A/B anchor restoration, independent anchors, first-time target isolation, visible Sync/Reload anchor preservation when anchored message remains, resident return and active Sync re-coalescing. Missing-anchor-message discard remained Runtime-unexercised.

### b19 process-memory Runtime evidence

Exact b19 source `c6accf16c8cf80c719f1e569e356b2bbe664e91e`, Run `33063446367`, Artifact `9642715296`.

Exact iPhone/iOS17 run reached 8 residents and captured 53 valid task-VM samples. Physical footprint was approximately 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents. Observed HTTP statuses were all 200 with no error/HTTP429. `processMemoryLimitRemainingBytes` was absent, so exact process-limit headroom remains Unverified.

Decision: this run provides no evidence for urgent normal-LRU eviction at 8 residents. Do not choose a normal capacity from physical RAM or approximate text bytes. Existing memory-warning trimming remains the evidence-backed eviction behavior; normal LRU stays unfrozen unless stronger future pressure/headroom evidence creates a real requirement.

### b20 title Runtime defect

Exact b20 source `754580fad96efa69f8a0ce7ea2bf542cacaf156e`, Run `33067148782`, Artifact `9644208203`.

b20 added immediate navigation title handoff from selected `ConversationSummary.title`, but first unloaded entry still showed `新对话`: first loading path caused `ConversationDetailViewController.viewDidLoad()` to run after Root installed the summary title, and neutral initialization overwrote it. Second resident-backed entry was correct. The export's earlier cold-start auth HTTP403 was not causal because later account/list verification succeeded before reproduction. No retry/fallback is justified.

### Stable b21 Runtime Candidate

- Candidate: `DEV-multi-conversation-state-0.1.0-b21`, version `0.1.0 (21)`.
- Exact product/config source: `6b50ead167bfde305d2ad58dd16fee6edaabf597`.
- Tree: `01168ce7be8d9cf4888ad1d0718238826730c30d`.
- Product delta from b20: one Root behavior line, `detailViewController.loadViewIfNeeded()`, after selection and before assigning target summary title.
- CI: Run `33070183417`, Job `98510113281`, success.
- Runtime Artifact: `9645439329`; ZIP `sha256:b3e2da46ce9ac99fc7028b7f5186476b3264c4a8c0323a426ee275b62c0d7d14`.
- IPA: `ChatGPTClient-0.1.0-b21-dev-multi-conversation-state.ipa`; SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`.
- Independent package identity: `0.1.0 (21)`, b21, source `6b50ead167bf`, minimum iOS14.0, `[1,2]`, arm64.
- Title Runtime: accepted for first unloaded entry, re-entry and rapid A -> B -> C on tested iPhone/iOS17.
- Reload-under-load Runtime: exact diagnostics contain two ordinary-load generation 1 -> Reload generation 2 replacements. Old task is cancelled, replacement returns HTTP200. In the strengthened case the user switches to an unrelated conversation while Reload remains active, returns to the target and logs `detail.coalesced completionCount=2`; the same replacement finishes without duplicate request or stale overwrite, and unrelated conversation work remains independent.
- PR merge-view validation: Run `33093117645`, Job `98590935774`, merge view `0520f118d4ada5eacfbac4ff444d9572e322efe1`, success; Artifact `9655230149` is merge-view CI evidence only and does not replace the Runtime Artifact.
- Merge: PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`.

**Stable for the recorded Plus/personal iPhone/iOS17 read-state scope. Frozen remains No.**

## State ownership model

`verified account/workspace scope -> conversation ID -> resident conversation state`

`ConversationRepository` remains the sole production conversation-data authority.

Resident/operation state owns only evidence-backed data needed now: parsed detail, directly evidenced current branch-tip/current-node identity, terminal state, target-specific operation kind/generation/task/waiters. Mounted cells/view controllers are never conversation-data cache. Raw HTTP payloads are discarded after parsing unless later evidence establishes a concrete need.

Foreground `selectedConversationID` is presentation state only. Loading, Sync, Reload and future response work target explicit authoritative identity and never mutate selection as a request side effect.

## Account/session ownership

`AuthSessionStore` remains sole account/auth-context owner. Default persistent WebKit storage remains sole persistent auth-secret authority.

- cached transient session stays bound to verified scope;
- delayed transport/operation context cannot re-adopt old scope;
- queued probe success is rechecked against current verified scope before commit;
- verified different scope purges old list/residents/operations/session/selection and rejects late old-scope results;
- invalidated consumers terminate deterministically.

Current source uses `userID + accountID` for personal-account residency. There is no real supported account-switch/logout route in the current product and no accepted non-personal workspace identity evidence. Those conditions remain Unknown / Unverified after this Work's closure; do not invent fake routes to claim Runtime proof.

## Detail operation ownership

- A and B may have independent detail operations.
- Selecting B does not cancel A.
- Explicit Reload/Sync A may supersede/cancel only A's older same-target detail operation.
- Same-target replacement preserves accepted cancellation-before-replacement behavior.
- Equivalent same-target loads may coalesce.
- Operation identity includes account scope + conversation ID + generation.
- Late obsolete target cannot overwrite newer state.
- Every waiter terminates on success, failure, supersede or account invalidation.
- No arbitrary global concurrency limit, retry, timer, watchdog or fallback without evidence.

Exact b21 directly accepts the multi-conversation replacement-under-load invariant in addition to earlier independent overlap/coalescing evidence.

## Resident navigation semantics

On navigation to B:

1. Root changes foreground selection once.
2. If B has active operation, presentation joins/observes it.
3. Otherwise loaded B renders immediately with no Detail request.
4. Failed B remains failed; ordinary navigation does not implicitly retry.
5. Only missing/evicted B starts one ordinary load.

Loaded return and active same-target coalescing are Runtime accepted. Natural terminal failed-resident navigation remains Runtime-unverified because no natural terminal failure occurred; it is not a known defect and is not a reason to manufacture failure/retry behavior.

## Recovery semantics

### Sync

Sync captures its target, does not change selection, may replace only same-target older work, preserves loaded resident on failure where applicable and leaves other conversations independent. b17 accepts A -> B -> A before Sync terminal. b18 additionally accepts anchor preservation on visible Sync and re-coalescing when returning to B while B Sync is active.

### Reload

Reload captures its target, rebuilds that target from one fresh server Detail, never resends/regenerates and leaves other conversations independent. b18 accepts ordinary visible Reload with anchor preservation when the anchored message remains. Exact b21 additionally accepts same-target replacement while the older ordinary Detail is in flight, including old-task cancellation, hidden unrelated-conversation independence and rejoin coalescing onto the same active Reload.

## Per-conversation historical scroll presentation

Representation:

`conversation ID -> { visible message ID, relative vertical offset }`

The message ID is in-memory only and is never logged. There is no global raw `contentOffset` copied between conversations and no retained view hierarchy per conversation.

Rules:

- `displayedConversationID` tracks actually displayed conversation separately from repository selection.
- Before outgoing A rows become B, capture A top-visible message identity + relative offset.
- After target rows reload, find the same target message and reapply relative offset with bounds clamping.
- No-anchor target starts at normal top.
- Account-scope reset clears all anchors.
- Visible Sync/Reload captures before refresh and restores only when the same anchored message remains.
- If anchored message disappears, discard anchor and return top; do not guess another message.

Exact b18 Runtime accepts the tested matrix. Anchored-message disappearance remains Runtime-unproven and is not manufactured solely for proof.

## Selected-title presentation lifecycle

The visible conversation list already holds server-backed `ConversationSummary.title`. Selection may use this summary immediately while Detail is still missing; loaded Detail later confirms via `detail.title`.

Current b21 ordering is:

`selectConversation(id:) -> loadViewIfNeeded() -> assign selected summary title -> showConversation(id:)`.

This ensures neutral initialization happens before the selected title handoff. Direct real-device testing accepts the requested first-entry/re-entry/rapid A→B→C title matrix. It does not create a second title owner/cache and does not change request or resident ownership.

## Future follow-tail contract

Historical anchor and future active-response follow-tail are different semantics.

- If A is at/near bottom and A has an authoritative active response, future Send/Stream may mark A as following its tail.
- If A grows/completes while hidden, returning A must show A's current latest bottom, not an older pre-growth position.
- If user intentionally scrolls upward while A generates, that exits follow-tail and establishes historical-reading intent.
- B scrolling never mutates A state; hidden A growth never mutates B state.

Whether a response is active/terminal must come from future authoritative per-conversation Send/Stream response owner. Completed read-state work adds no `isStreaming`, response flag, timer, fake follow-tail state or future response authority.

## Residency / memory policy

Current rules:

- b19 shows no immediate footprint pressure through 8 residents on tested device;
- exact process-limit headroom remains Unverified;
- selected resident protected;
- active detail/recovery resident protected;
- future active response protected;
- memory warning trims only eligible inactive terminal residents;
- no persistent chat-body disk cache;
- approximate visible-text bytes are correlation only and cannot justify capacity.

No ordinary LRU capacity is implemented or frozen in this Work. Revisit only when stronger future evidence makes it necessary.

## Stable acceptance boundary

Accepted:

- b17 resident return / hidden completion / same-target coalescing / rapid switching / Sync return / rapid overlap.
- b18 historical A/B anchor restoration, independent anchors, first-time target isolation, visible Sync/Reload anchor preservation when same message remains, resident return and active Sync re-coalescing.
- b19 observed process-footprint 0→8 resident matrix; no evidence for urgent normal LRU.
- b21 first-unloaded-entry/re-entry/rapid A -> B -> C title lifecycle matrix.
- b21 same-target ordinary-load -> Reload replacement-under-load with old-task cancellation, hidden unrelated-conversation independence and return coalescing onto the same replacement.
- PR #23 merge-view CI succeeded and the PR merged without a product/config change after exact b21 Runtime source.

Superseded/failing:

- b20 first-unloaded-entry title presentation failed due first-view lifecycle overwrite.

Explicit non-blocking Unknown / Unverified boundaries:

1. natural terminal failed-resident navigation;
2. supported account switch purge/late-callback isolation when a real route exists;
3. non-personal workspace identity/isolation;
4. missing-anchor-message discard Runtime path;
5. normal LRU capacity if stronger future memory pressure/headroom evidence creates a requirement.

These are evidence boundaries, not claims of success. They do not justify fabricating unsupported behavior.

## Closure

`DEV-multi-conversation-state` is complete and merged. No b22 is justified by current evidence. Historical task checkpoint is removed at completion; durable evidence remains in this plan, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md` and `BUILD_TEST_INDEX.md`.

The next serialized roadmap priority is `DEV-conversation-list-cache-core`; its activation, branch/checkpoint/candidate identity and implementation belong to its own development session.

## Non-goals / prohibited shortcuts

- No separate authoritative repository per screen/conversation.
- No retained UIKit hierarchy/navigation stack as conversation-data authority.
- No selection-driven cancellation or reload-on-every-navigation.
- No stale operation context restoring old account scope.
- No silently abandoned waiters.
- No arbitrary normal LRU capacity.
- No persistent chat-body/draft cache without separate privacy/storage requirement.
- No speculative retry, timer, watchdog, fallback, global rate limiter or compatibility shim.
- No copied persistent auth secrets or second account owner.
- No raw mapping retention to anticipate future Send/Edit/Regenerate.
- No capacity chosen from approximate text bytes or device physical RAM alone.
- No full retained view hierarchy per conversation merely to preserve scroll position.
- No claim about concurrent A/B server safety beyond exact Runtime evidence.