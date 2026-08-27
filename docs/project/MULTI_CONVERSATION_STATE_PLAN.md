# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27; refreshed after exact b18 historical-scroll real-device acceptance._

## Purpose

Support normal use of several ChatGPT development conversations at the same time without making UI navigation destroy already-loaded state.

Core invariant:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned work merely because A became hidden, or force A to reload merely because A is no longer selected.

This Work is the structural prerequisite for production Send/Stream ownership. Exact candidate/evidence handoff remains in `current/dev/DEV-multi-conversation-state.md`; broader pre-Send gaps remain in `CLIENT_ARCHITECTURE_GAP_REVIEW.md`.

## Accepted baseline and active Candidate

### Stable baseline

`DEV-conversation-recovery-0.1.0-b15` is merged Stable for recorded Plus/personal iPhone/iOS17 recovery scope.

Current `main` head is `2c33dacbefa613292eb89cbf606b0172a241e81e`; it advanced after b18 Artifact through docs-only message-timestamp/display-preference planning. Exact b18 product/runtime evidence remains tied to source `f30c13b4ac2c40dcda829585682825ca906dceae`. Final merge must synchronize these docs-only main changes without overwriting them.

### Historical b16

b16 source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08` compiled, but Artifact `9621830284` embedded the wrong recovery candidate/slug and was rejected before runtime. Source review also found owner/race gaps. Never reuse b16.

### b17 core Runtime evidence

Exact b17 source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`, Run `33045536770`, Artifact `9635486304`.

Exact iPhone/iOS17 Runtime accepted:

1. resident A -> B -> A without navigation-only Detail refetch;
2. hidden valid completion retained;
3. returning to in-flight same target coalesces;
4. Sync A -> B -> A rejoins same active Sync;
5. rapid different-conversation overlap reached three active operations without HTTP429 in supplied export.

The same run reproduced the historical-scroll defect: A around ~10% -> B scroll -> return A shifted.

### Current b18 Candidate

- Candidate: `DEV-multi-conversation-state-0.1.0-b18`, version `0.1.0 (18)`.
- Exact product/config source: `f30c13b4ac2c40dcda829585682825ca906dceae`.
- Tree: `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- CI: Run `33054012226`, Job `98456174184`, success; `arm64-apple-ios14.0`; exact candidate/source inputs.
- Artifact: `9638821912`; ZIP `sha256:36b59b8c4d3bdcadedd463a3554528452ff46478651671b50f4bd9f7fa2b5d2c`.
- IPA: `ChatGPTClient-0.1.0-b18-dev-multi-conversation-state.ipa`; SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.
- Independent package identity: `0.1.0 (18)`, b18, source `f30c13b4ac2c`, minimum iOS14.0, `[1,2]`, arm64.
- **Runtime/manual/real-device: Accepted for the tested historical-scroll / Sync / Reload-preservation / resident-regression matrix on exact iPhone/iOS17 b18. Stable/Frozen: No.**

## State ownership model

`verified account/workspace scope -> conversation ID -> resident conversation state`

`ConversationRepository` remains the sole production conversation-data authority.

Resident/operation state owns only evidence-backed data needed now: parsed detail, directly evidenced current branch-tip/current-node identity, terminal state, target-specific operation kind/generation/task/waiters, and later LRU metadata only after measured policy exists.

Mounted cells/view controllers are never conversation-data cache. Raw HTTP payloads are discarded after parsing unless later evidence establishes a concrete need.

Foreground `selectedConversationID` is presentation state only. Loading, Sync, Reload and future response work target explicit authoritative identity and never mutate selection as a request side effect.

## Account/session ownership

`AuthSessionStore` remains sole account/auth-context owner. Default persistent WebKit storage remains sole persistent auth-secret authority.

- cached transient session stays bound to verified scope;
- delayed transport/operation context cannot re-adopt an old scope;
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

b17 Runtime confirms independent overlap and same-target coalescing. b18 re-confirms same-target coalescing when returning to B while B Sync is active.

## Resident navigation semantics

Resident logic distinguishes missing/evicted, active operation, loaded, terminal failure and explicit Sync/Reload.

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

An isolated older-in-flight Detail -> newer same-target Reload replacement sequence was not exercised in b18; b15 remains accepted replacement-under-load baseline and the multi-conversation regression spot-check stays open.

## b18 per-conversation historical scroll presentation

The b17 defect belongs to presentation residency, not conversation-data ownership. b18 changes only the existing detail presentation owner.

### Representation

`conversation ID -> { visible message ID, relative vertical offset }`

The message ID is in-memory only and is never logged. There is no global raw `contentOffset` copied between conversations and no retained view hierarchy per conversation.

### Capture / restore

- `displayedConversationID` tracks actually displayed conversation separately from repository selection.
- Before outgoing A rows become B, capture A top-visible message identity + relative offset.
- After target rows reload, find the same target message and reapply relative offset with bounds clamping.
- No-anchor target starts at normal top.
- Account-scope reset clears all anchors.
- Visible Sync/Reload captures before refresh and restores only when the same anchored message remains.
- If anchored message disappears, discard anchor and return top; do not guess another message.

### Exact b18 Runtime evidence

User installed exact b18 on iPhone/iOS17, executed requested matrix and reported no issue. Export metadata identifies b18/build18/source `f30c13b4ac2c`.

Observed diagnostics:

- 195 events, all `info`;
- 21 `scrollAnchor.saved`, 19 `scrollAnchor.restored`;
- 17 `resident.hit`, 17 `resident.firstVisible`;
- all 17 recorded HTTP statuses are 200;
- no error, HTTP429 or `scrollAnchor.discarded`.

Accepted:

1. A -> B -> A historical position restoration.
2. Independent A/B anchors across repeated switching.
3. First-time third target starts without inheriting prior offset.
4. Visible Sync preserves anchor when the anchored message remains.
5. Reload preserves anchor when the anchored message remains.
6. B Sync survives B -> A -> B, restores B anchor and `detail.coalesced completionCount=2` re-attaches to the same Sync before hidden HTTP200 completion.
7. Already-resident returns remain resident hits with no navigation-only Detail refetch.

Not Runtime-proven: anchored-message disappearance -> `scrollAnchor.discarded` -> top, because the condition did not occur naturally. Do not manufacture destructive branch mutation solely to prove it.

## Future follow-tail contract

Historical anchor and future active-response follow-tail are different semantics.

- If A is at/near bottom and A has an authoritative active response, future Send/Stream may mark A as following its tail.
- If A grows/completes while hidden, returning A must show A's current latest bottom, not an older pre-growth position.
- If user intentionally scrolls upward while A generates, that exits follow-tail and establishes historical-reading intent.
- B scrolling never mutates A state; hidden A growth never mutates B state.

Whether a response is active/terminal must come from future authoritative per-conversation Send/Stream response owner. b18 intentionally adds no `isStreaming`, response flag, timer, fake follow-tail state or future response authority.

## Residency / memory policy

Unlimited permanent residency is not acceptable. A bounded normal LRU-style working set will be selected **after real-device process/system memory evidence**.

Current rules:

- selected resident protected;
- active detail/recovery resident protected;
- future active response protected;
- memory warning trims only eligible inactive terminal residents;
- no persistent chat-body disk cache;
- approximate visible-text bytes are correlation only and cannot justify capacity.

b17 reached six residents and `residentTotalApproximateTextBytes=6724764`; b18 reached three residents in the scroll run. Neither number alone is process-memory evidence.

## Acceptance before Stable

Accepted:

- b17 resident return / hidden completion / same-target coalescing / rapid switching / Sync return / rapid overlap for tested scope.
- b18 historical A/B anchor restoration, independent anchors, first-time target isolation, visible Sync/Reload anchor preservation when same message remains, resident return and active Sync re-coalescing for tested scope.

Still open:

1. isolated same-target Reload replacement while older same-target Detail is actually in flight;
2. terminal failed A remains failed across navigation with no implicit retry when a natural failure is available;
3. supported account switch purges old scope and rejects late callbacks when a real supported route exists;
4. normal resident capacity is chosen from real process/system memory evidence, not approximate text bytes;
5. non-personal workspace isolation remains Unknown / Unverified.

Conditional anchored-message disappearance path remains source/CI-defined but Runtime-unexercised.

## Next exact action

**Do not change product code yet. Collect real iPhone process/system memory evidence while several small and large conversations remain resident and are switched repeatedly. Use that evidence to decide whether a bounded normal LRU policy is needed now and what capacity is defensible.**

Before final PR/merge, synchronize with current `main@2c33dacbefa613292eb89cbf606b0172a241e81e` and preserve its docs-only message-timestamp/display-preference planning. Re-run only validation materially affected by synchronized product source.

## Non-goals / prohibited shortcuts

- No separate authoritative repository per screen/conversation.
- No retained UIKit hierarchy/navigation stack as conversation-data authority.
- No selection-driven cancellation or reload-on-every-navigation.
- No stale operation context restoring old account scope.
- No silently abandoned waiters.
- No unlimited final resident retention.
- No persistent chat-body/draft cache without separate privacy/storage requirement.
- No speculative retry, timer, watchdog, fallback, global rate limiter or compatibility shim.
- No copied persistent auth secrets or second account owner.
- No raw mapping retention to anticipate future Send/Edit/Regenerate.
- No capacity chosen from approximate text bytes alone.
- No full retained view hierarchy per conversation merely to preserve scroll position.
- No claim about concurrent A/B server safety beyond exact Runtime evidence.
