# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27; refreshed through exact b21 title Runtime acceptance._

## Purpose

Support normal use of several ChatGPT development conversations at the same time without making UI navigation destroy already-loaded state.

Core invariant:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned work merely because A became hidden, or force A to reload merely because A is no longer selected.

This Work is the structural prerequisite for production Send/Stream ownership. Exact candidate/evidence handoff remains in `current/dev/DEV-multi-conversation-state.md`; broader pre-Send gaps remain in `CLIENT_ARCHITECTURE_GAP_REVIEW.md`.

## Accepted baseline and active Candidate

### Stable baseline

`DEV-conversation-recovery-0.1.0-b15` is merged Stable for recorded Plus/personal iPhone/iOS17 recovery scope.

Current `main` is `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`; its merged planning PR #18 must be preserved during final synchronization.

### Historical b16

b16 source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08` compiled, but Artifact `9621830284` embedded the wrong recovery candidate/slug and was rejected before Runtime. Source review also found owner/race gaps. Never reuse b16.

### b17 core Runtime evidence

Exact b17 source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`, Run `33045536770`, Artifact `9635486304`.

Exact iPhone/iOS17 Runtime accepted:

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

Decision: this run provides no evidence for urgent normal-LRU eviction at 8 residents. Do not choose a normal capacity from physical RAM or approximate text bytes. Existing memory-warning trimming remains the evidence-backed eviction behavior; normal LRU stays unfrozen.

### b20 title Runtime defect

Exact b20 source `754580fad96efa69f8a0ce7ea2bf542cacaf156e`, Run `33067148782`, Artifact `9644208203`.

b20 added immediate navigation title handoff from the selected `ConversationSummary.title`. Real-device export `0.1.0 (20)` / source `754580fad96e` reproduced a first-entry defect:

- first unloaded target selected at `11:48:37Z`, `resident.miss`;
- Detail returned HTTP200 after about 9565.84 ms;
- same target reselected at `11:48:48Z` as `resident.hit` and became first-visible in about 28.70 ms;
- user observed `新对话` only on the first loading entry; second resident-backed entry was correct.

Source proves the summary lookup itself was valid. The first loading path caused `ConversationDetailViewController.viewDidLoad()` to run after Root had installed the summary title; its neutral `title = "新对话"` initialization overwrote the real title. The export's earlier cold-start auth HTTP403 is not causal because a later account/list generation succeeded before reproduction. No retry/fallback is justified.

### Current b21 Candidate

- Candidate: `DEV-multi-conversation-state-0.1.0-b21`, version `0.1.0 (21)`.
- Exact product/config source: `6b50ead167bfde305d2ad58dd16fee6edaabf597`.
- Tree: `01168ce7be8d9cf4888ad1d0718238826730c30d`.
- Product delta from b20: exactly one Root behavior line, `detailViewController.loadViewIfNeeded()`, after selection and before assigning target summary title.
- CI: Run `33070183417`, Job `98510113281`, success.
- Artifact: `9645439329`; ZIP `sha256:b3e2da46ce9ac99fc7028b7f5186476b3264c4a8c0323a426ee275b62c0d7d14`.
- IPA: `ChatGPTClient-0.1.0-b21-dev-multi-conversation-state.ipa`; SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`.
- Independent package identity: `0.1.0 (21)`, b21, source `6b50ead167bf`, minimum iOS14.0, `[1,2]`, arm64.
- **Runtime/manual/real-device: Accepted for the requested first-unloaded-entry / re-entry / rapid A -> B -> C title matrix on tested iPhone/iOS17; user reported no issue. No new diagnostics export accompanied this acceptance. Stable/Frozen: No.**

## State ownership model

`verified account/workspace scope -> conversation ID -> resident conversation state`

`ConversationRepository` remains the sole production conversation-data authority.

Resident/operation state owns only evidence-backed data needed now: parsed detail, directly evidenced current branch-tip/current-node identity, terminal state, target-specific operation kind/generation/task/waiters, and later LRU metadata only after measured policy exists.

Mounted cells/view controllers are never conversation-data cache. Raw HTTP payloads are discarded after parsing unless later evidence establishes a concrete need.

Foreground `selectedConversationID` is presentation state only. Loading, Sync, Reload and future response work target explicit authoritative identity and never mutate selection as a request side effect.

## Account/session ownership

`AuthSessionStore` remains sole account/auth-context owner. Default persistent WebKit storage remains sole persistent auth-secret authority.

- cached transient session stays bound to verified scope;
- delayed transport/operation context cannot re-adopt old scope;
- queued probe success is rechecked against current verified scope before commit;
- verified different scope purges old list/residents/operations/session/selection and rejects late old-scope results;
- invalidated consumers terminate deterministically.

Current source uses `userID + accountID` for personal-account residency. Supported account-switch Runtime proof and non-personal workspace identity remain Unknown / Unverified.

## Detail operation ownership

- A and B may have independent detail operations.
- Selecting B does not cancel A.
- Explicit Reload/Sync A may supersede/cancel only A's older same-target detail operation.
- Same-target replacement preserves accepted b15 cancel-before-replace behavior.
- Equivalent same-target loads may coalesce.
- Operation identity includes account scope + conversation ID + generation.
- Late obsolete target cannot overwrite newer state.
- Every waiter terminates on success, failure, supersede or account invalidation.
- No arbitrary global concurrency limit, retry, timer, watchdog or fallback without evidence.

b17/b18 Runtime confirm independent overlap and same-target coalescing. b20 title failure and b21 title correction do not change these operation owners.

## Resident navigation semantics

On navigation to B:

1. Root changes foreground selection once.
2. If B has active operation, presentation joins/observes it.
3. Otherwise loaded B renders immediately with no Detail request.
4. Failed B remains failed; ordinary navigation does not implicitly retry.
5. Only missing/evicted B starts one ordinary load.

Exact b17/b18 Runtime accepts loaded return and active same-target coalescing for tested paths. Terminal failure residency remains Runtime-open because no natural terminal failure occurred.

## Recovery semantics

### Sync

Sync captures its target, does not change selection, may replace only same-target older work, preserves loaded resident on failure where applicable and leaves other conversations independent. b17 accepts A -> B -> A before Sync terminal. b18 additionally accepts anchor preservation on visible Sync and re-coalescing when returning to B while B Sync is active.

### Reload

Reload captures its target, rebuilds that target from one fresh server Detail, never resends/regenerates and leaves other conversations independent. Exact b18 ordinary Reload completed HTTP200 and restored the same historical anchor when the anchored message remained.

An isolated older-in-flight Detail -> newer same-target Reload replacement sequence remains unexercised in multi-conversation Runtime; b15 remains accepted replacement-under-load baseline.

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

Exact b18 Runtime accepts the tested matrix. Anchored-message disappearance remains Runtime-unproven.

## Selected-title presentation lifecycle

The visible conversation list already holds server-backed `ConversationSummary.title`. Selection may use this summary immediately while Detail is still missing; loaded Detail later confirms via `detail.title`.

b20 proved that this must respect UIViewController first-load ordering. Current b21 ordering is:

`selectConversation(id:) -> loadViewIfNeeded() -> assign selected summary title -> showConversation(id:)`.

This ensures neutral initialization happens before the selected title handoff. Direct real-device testing now accepts the requested first-entry/re-entry/rapid A→B→C title matrix. It does not create a second title owner/cache and does not change request or resident ownership.

## Future follow-tail contract

Historical anchor and future active-response follow-tail are different semantics.

- If A is at/near bottom and A has an authoritative active response, future Send/Stream may mark A as following its tail.
- If A grows/completes while hidden, returning A must show A's current latest bottom, not an older pre-growth position.
- If user intentionally scrolls upward while A generates, that exits follow-tail and establishes historical-reading intent.
- B scrolling never mutates A state; hidden A growth never mutates B state.

Whether a response is active/terminal must come from future authoritative per-conversation Send/Stream response owner. Current work adds no `isStreaming`, response flag, timer, fake follow-tail state or future response authority.

## Residency / memory policy

Unlimited permanent residency is not a final principle, but a bounded normal LRU capacity is selected only from real evidence.

Current rules:

- b19 shows no immediate footprint pressure through 8 residents on tested device;
- exact process-limit headroom remains Unverified;
- selected resident protected;
- active detail/recovery resident protected;
- future active response protected;
- memory warning trims only eligible inactive terminal residents;
- no persistent chat-body disk cache;
- approximate visible-text bytes are correlation only and cannot justify capacity.

## Acceptance before Stable

Accepted:

- b17 resident return / hidden completion / same-target coalescing / rapid switching / Sync return / rapid overlap for tested scope.
- b18 historical A/B anchor restoration, independent anchors, first-time target isolation, visible Sync/Reload anchor preservation when same message remains, resident return and active Sync re-coalescing for tested scope.
- b19 observed real process-footprint 0→8 resident matrix; no evidence for urgent normal LRU at 8 residents.
- b21 first-unloaded-entry/re-entry/rapid A -> B -> C title lifecycle matrix; user reported no issue on the tested iPhone/iOS17 environment.

Superseded/failing:

- b20 first-unloaded-entry title presentation failed due first-view lifecycle overwrite.

Still open:

1. isolated same-target Reload replacement while older same-target Detail is actually in flight;
2. terminal failed A remains failed across navigation with no implicit retry when a natural failure is available;
3. supported account switch purges old scope and rejects late callbacks when a real supported route exists;
4. stronger process-limit/headroom or pressure evidence if normal LRU capacity becomes necessary;
5. non-personal workspace isolation remains Unknown / Unverified.

Conditional anchored-message disappearance remains source/CI-defined but Runtime-unexercised.

## Next exact action

Use exact b21 on iPhone/iOS17 for the isolated same-target Reload replacement-under-load Runtime spot-check: start an unloaded/slow Detail and trigger `重载当前会话` before the older ordinary Detail finishes. Expected: the older same-target request is cancelled/superseded, the Reload becomes authoritative without stale overwrite or HTTP429 regression, and unrelated conversations remain independent. This tests existing code; do not allocate b22 unless a real defect appears.

Before final PR/merge, synchronize with `main@3cbb5c9acce26c0004e1d78c9607f2361d83fe05` and preserve its planning docs. Re-run only validation materially affected by synchronized product source.

## Non-goals / prohibited shortcuts

- No separate authoritative repository per screen/conversation.
- No retained UIKit hierarchy/navigation stack as conversation-data authority.
- No selection-driven cancellation or reload-on-every-navigation.
- No stale operation context restoring old account scope.
- No silently abandoned waiters.
- No unlimited final resident retention principle.
- No persistent chat-body/draft cache without separate privacy/storage requirement.
- No speculative retry, timer, watchdog, fallback, global rate limiter or compatibility shim.
- No copied persistent auth secrets or second account owner.
- No raw mapping retention to anticipate future Send/Edit/Regenerate.
- No capacity chosen from approximate text bytes or device physical RAM alone.
- No full retained view hierarchy per conversation merely to preserve scroll position.
- No claim about concurrent A/B server safety beyond exact Runtime evidence.