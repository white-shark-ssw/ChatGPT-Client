# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27; refreshed for exact b18 scroll-anchor Candidate and pending real-device validation._

## Purpose

Support normal use of several ChatGPT development conversations at the same time without making UI navigation destroy already-loaded state.

Core invariant:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned work merely because A became hidden, or force A to reload merely because A is no longer selected.

This Work is the structural prerequisite for production Send/Stream ownership. Exact candidate/evidence handoff remains in `current/dev/DEV-multi-conversation-state.md`; broader pre-send gaps remain in `CLIENT_ARCHITECTURE_GAP_REVIEW.md`.

## Accepted baseline and active Candidate

### Stable baseline

`DEV-conversation-recovery-0.1.0-b15` is merged Stable for the recorded Plus/personal iPhone/iOS17 recovery scope. The merged Stable baseline remains `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011` until this Work completes and merges.

b15 proved same-target explicit replacement: newer manual recovery owns a new generation, cancels the older tracked detail task before replacement, and stale callbacks cannot mutate current state.

### Historical b16

b16 source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08` compiled, but Artifact `9621830284` embedded the wrong recovery candidate/slug and was rejected before runtime. Source review also found stale-scope, waiter, hidden-Sync-return, list-freshness, task-handle and execution-domain gaps. Never reuse b16.

### b17 core runtime evidence

Exact b17 source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`, Run `33045536770`, Artifact `9635486304`.

Exact iPhone/iOS17 runtime accepted the tested core sequences:

1. resident A -> B -> A return without navigation-only Detail refetch;
2. hidden valid completion retained and later returned from resident state;
3. returning to an in-flight same target coalesces onto one operation;
4. Sync A -> B -> A rejoins the same active Sync and applies its terminal result;
5. rapid different-conversation overlap reached three active operations with no HTTP429 in the supplied export.

The same run reproduced the P1 presentation defect: A around ~10% -> B scroll -> return A shifted instead of restoring A's prior semantic/visual reading position.

### Current b18 Candidate

- Candidate: `DEV-multi-conversation-state-0.1.0-b18`, version `0.1.0 (18)`.
- Branch: `dev/multi-conversation-state-20260827`.
- Exact product/config source: `f30c13b4ac2c40dcda829585682825ca906dceae`.
- Exact product tree: `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- Product parent: docs-only `49be4de3b2918ae72b22e3de7a386136d92c2523`.
- Exact product diff: workflow, Xcode project, `ConversationFeature.swift`, `scripts/build_ipa.sh` only.
- `ConversationFeature.swift` blob: `daf60d76b1295a9662a119b28766511039a52e8e`.
- CI: Run `33054012226`, Job `98456174184`, success on Xcode16.4; Release target `arm64-apple-ios14.0`; exact b18 candidate/source inputs; `BUILD SUCCEEDED`.
- Artifact: `9638821912`; ZIP `sha256:36b59b8c4d3bdcadedd463a3554528452ff46478651671b50f4bd9f7fa2b5d2c`.
- IPA: `ChatGPTClient-0.1.0-b18-dev-multi-conversation-state.ipa`; SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.
- Independent package identity: `0.1.0 (18)`, b18 candidate, source `f30c13b4ac2c`, minimum iOS14.0, `[1,2]`, arm64.
- **Runtime/manual/real-device: Pending. Stable/Frozen: No.**

## State ownership model

Conceptually:

`verified account/workspace scope -> conversation ID -> resident conversation state`

`ConversationRepository` remains the sole production conversation-data authority.

Resident/operation state owns only evidence-backed data needed now:

- parsed current conversation detail needed to render;
- directly evidenced current branch-tip/current-node identity;
- terminal loaded/failed state;
- load/recovery operation kind, generation, task and waiters;
- later normal-LRU metadata only after a measured policy exists;
- future response linkage only after Send/Stream evidence exists.

Mounted cells/view controllers are never the conversation-data cache. Raw HTTP payloads are discarded after parsing unless later evidence establishes a concrete need.

Foreground `selectedConversationID` is presentation state only. Loading, Sync, Reload and future response work target explicit authoritative conversation identity and never mutate selection as a request side effect.

## Account/session ownership

`AuthSessionStore` remains the sole account/auth-context owner. Default persistent WebKit storage remains the sole persistent auth-secret authority.

Repository rules:

- concurrent first loads may share one transient-session acquisition;
- cached transient session remains bound to the verified scope that created it;
- only current Auth-owner evidence may establish/change repository scope;
- delayed transport/operation context cannot re-adopt an old scope;
- queued probe success is rechecked against current verified scope before commit;
- verified different scope purges old list/residents/operations/session/selection and rejects late old-scope results;
- invalidated consumers terminate deterministically.

Current source uses `userID + accountID` for personal-account residency. Non-personal workspace identity remains Unknown / Unverified.

## Detail operation ownership

- A and B may have independent detail operations.
- Selecting B does not cancel A.
- Explicit Reload/Sync A may supersede/cancel only A's older same-target detail operation.
- Same-target replacement preserves accepted b15 cancel-before-replace behavior.
- Equivalent same-target loads may coalesce.
- Operation identity includes account scope + conversation ID + generation.
- Late obsolete A cannot overwrite newer A.
- Every waiter terminates on success, failure, supersede or account invalidation.
- No arbitrary global concurrency limit, retry, timer, watchdog or fallback is added without evidence.

b17 runtime directly confirms independent overlap and same-target coalescing for the supplied sequences.

## Resident navigation semantics

Resident logic distinguishes missing/evicted, active operation, loaded, terminal failure, and explicit Sync/Reload.

On navigation to B:

1. Root changes foreground selection once.
2. If B has an active operation, presentation joins/observes it.
3. Otherwise loaded B renders immediately with no Detail request.
4. Failed B remains failed; ordinary navigation does not implicitly retry.
5. Only missing/evicted B starts one ordinary load.

Returning B -> A follows the same rules. b17 accepts loaded return and in-flight coalescing; terminal failure residency remains runtime-open because no natural failure was exercised.

## Recovery semantics

### Sync A

Sync captures A at invocation, does not change selection, may replace only A's older same-target detail work, preserves loaded A on failure where applicable, and leaves B/C independent. b17 runtime accepts A -> B -> A before Sync terminal.

### Reload A

Reload captures A at invocation, rebuilds A from one fresh server Detail request, may clear A according to accepted Reload semantics, replaces only A's older target operation, never resends/regenerates, and leaves B/C independent. Isolated multi-conversation Reload replacement remains an open runtime spot-check.

## b18 per-conversation historical scroll presentation

The b17 defect belongs to presentation residency, not conversation-data ownership. b18 therefore changes only the existing detail presentation owner.

### Representation

Each live-process historical anchor is lightweight:

`conversation ID -> { visible message ID, relative vertical offset }`

The message ID is used in memory only and is never logged. There is no global raw `contentOffset` copied between conversations and no retained view hierarchy per conversation.

### Capture / restore

- `displayedConversationID` tracks the actually displayed conversation separately from repository selection, allowing outgoing A to be captured even after Root has selected B.
- Before A's rows are replaced by B, capture A's top visible message identity plus relative offset.
- After target rows reload, find that same target message in the target's current visible branch, position it, then reapply relative offset with normal bounds clamping.
- A target with no saved anchor starts at its normal top, never at the previous conversation's offset.
- Account-scope reset clears all presentation anchors.
- Visible Sync/Reload captures the current historical anchor before rows refresh and restores it when the anchored message still exists.
- If the anchored message no longer exists in the refreshed current branch, discard the anchor and return to normal top. Do not guess another message.

### Diagnostics

b18 adds privacy-safe:

- `scrollAnchor.saved`;
- `scrollAnchor.restored`;
- `scrollAnchor.discarded`.

Diagnostics may include existing irreversible conversation marker/list position plus row index, relative offset and discard reason. Never log raw message IDs, titles, bodies or secrets.

## Future follow-tail contract

Historical anchor and future active-response follow-tail are different semantics.

- If A is at/near bottom **and A has an authoritative active response**, future Send/Stream may mark A as following its tail.
- If A grows/completes while hidden, returning A must then show A's current latest bottom, not an older pre-growth position.
- If the user intentionally scrolls upward while A generates, that exits follow-tail and establishes historical-reading intent.
- B scrolling never mutates A state; hidden A growth never mutates B state.

Whether a response is active/terminal must come from the future authoritative per-conversation Send/Stream response owner. b18 intentionally adds no `isStreaming`, response flag, timer, fake follow-tail state or future response authority.

## Residency / memory policy

Unlimited permanent residency is not acceptable. A bounded normal LRU-style working set will be selected **after real-device process/system memory evidence**.

Current rules:

- selected resident protected;
- active detail/recovery resident protected;
- future active response protected;
- memory warning trims only eligible inactive terminal residents;
- no persistent chat-body disk cache;
- approximate visible-text bytes are correlation only and cannot justify a capacity.

b17 reached six residents and `residentTotalApproximateTextBytes=6724764`; this is useful correlation, not memory-capacity proof.

## Acceptance before Stable

Already accepted from exact b17 for the supplied scope:

1. loaded resident return without navigation-only refetch;
2. hidden valid completion retained;
3. same-target in-flight return coalesces;
4. rapid switching does not cross-present another conversation in the observed run;
5. Sync A -> B -> A rejoins the same Sync;
6. rapid different-conversation overlap up to three active operations with no HTTP429 in supplied diagnostics.

Still open:

1. **b18 historical scroll**: A ~10% -> B scroll -> A restores same practical semantic/visual point.
2. A and B independently restore their own anchors across repeated switching.
3. First-time/no-anchor C starts normally at top.
4. Historical Sync/Reload preserves anchor when the same message remains; missing message discards rather than guesses.
5. Isolated target-only Reload replacement regression as applicable.
6. Terminal failed A remains failed across navigation with no implicit retry when a natural failure is available.
7. Supported account switch purges old scope and rejects late callbacks when a real supported route exists.
8. Normal resident capacity is chosen from real process/system memory evidence, not approximate text bytes.
9. Non-personal workspace isolation remains Unknown / Unverified.

## Next exact action

Install exact b18 Artifact `9638821912` / IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c` on the target iPhone/iOS17 device and execute the b18 scroll acceptance matrix in the active checkpoint. Export diagnostics if an anchor case fails or exact save/restore evidence is needed.

Do not call b18 Runtime-accepted or Stable until real-device evidence exists. Do not rebuild/reuse b18 after this Artifact identity has been produced; corrected product code would require a new unique Candidate/build.

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
- No claim about concurrent A/B server safety beyond exact runtime evidence.
