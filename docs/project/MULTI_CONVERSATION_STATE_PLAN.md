# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27; refreshed after b17 real-device core validation._

## Purpose

Support normal use of several ChatGPT development conversations at the same time without making UI navigation destroy already-loaded state.

Core invariant:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned work merely because A became hidden, or force A to reload merely because A is no longer selected.

This Work is the structural prerequisite for production send/stream ownership.

See `CLIENT_ARCHITECTURE_GAP_REVIEW.md` for the broader pre-send architecture and `current/dev/DEV-multi-conversation-state.md` for exact branch/candidate evidence and the current next action.

## Accepted baseline vs Active implementation

### Accepted Stable baseline

`DEV-conversation-recovery-0.1.0-b15` is merged Stable for the recorded Plus/personal iPhone/iOS17 recovery scope. Current merged Stable baseline remains `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011` until this Work completes/merges.

b15 proved the same-conversation explicit replacement rule: a newer manual recovery owns a new generation, cancels the older selected-detail task before replacement, and stale callbacks cannot mutate current state.

### b16 historical review

b16 source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08` compiled in Run `33009246356`, but Artifact `9621830284` had the wrong recovery candidate/IPA slug and was rejected before runtime. Second source review also found stale-scope, waiter, hidden-Sync-return, list-freshness, task-handle and execution-domain defects. b16 must never be reused.

### Current b17 Candidate

- Work: `DEV-multi-conversation-state`.
- Branch: `dev/multi-conversation-state-20260827`.
- Candidate: `DEV-multi-conversation-state-0.1.0-b17`, `0.1.0 (17)`.
- Exact product/config source: `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; tree `3451585f83c7bac69368709fe6273b90a0294d29`.
- Static/local: exact ConversationFeature blob `1034cff72dea36d6d7e835bdf52dcfe2cdc8e38d`; Git-blob identity matched; `swiftc -frontend -parse` passed.
- CI: Run `33045536770`, job `98428537619`, success on Xcode16.4; Release target `arm64-apple-ios14.0`.
- Artifact: `9635486304`; IPA `ChatGPTClient-0.1.0-b17-dev-multi-conversation-state.ipa`; IPA SHA `ed551deac0335e47da56da36ec2a8a20550613ac072ac1ddf0b84790278318dc`; ZIP digest `sha256:bf6aed8cebcb08153fbe8fac6868ce60c0ef4bd7876340246912ba8edbed1c33`.
- Independent package inspection confirms embedded `0.1.0 (17)`, candidate b17, source `bc69d58b3245`, minimum iOS14.0, device families `[1,2]`, arm64.
- **Real-device**: exact b17 on iPhone/iOS17 now has accepted evidence for resident return, hidden completion, same-target in-flight coalescing, Sync A->B->A rejoin and rapid multi-conversation overlap. No HTTP429 appears in the supplied diagnostic export.
- **Not Stable**: Reload-target isolation, failure residency, supported account-switch purge and measured normal LRU capacity remain separate acceptance work.

## b17 real-device core evidence

The 2026-08-27 exact b17 export and user observation support these current conclusions:

1. Loaded resident return logs `resident.hit` and `resident.firstVisible` without a navigation-only refetch; observed first-visible timings are approximately `0.23–0.78 ms`.
2. Returning to an in-flight same target logs `detail.coalesced completionCount=2`, so the original operation remains owner instead of starting a duplicate target Detail request.
3. Hidden valid completion logs `resident.stored visibility=hidden`; later return resolves through resident hit.
4. Sync A -> B -> A: returning A while its Sync is still active logs `resident.hit activeOperationKind=sync` and coalesces onto the same Sync; that operation later finishes HTTP200 / `latestSync.end status=ok`.
5. Rapid different-conversation overlap reached `activeOperationCount=3`; hidden/foreground completions stayed target-specific; no HTTP429 appears in the supplied export.
6. Resident count reached 6 and `residentTotalApproximateTextBytes=6724764`; this remains an approximate text correlation metric, not process-memory evidence or an LRU-capacity decision.

### Reproduced P1 — semantic per-conversation scroll anchor

The previously planned P1 gap is now reproduced on exact b17:

- leave conversation A around ~10% scroll position;
- switch to conversation B;
- scroll B;
- return to A;
- A's prior position has shifted instead of restoring the same semantic/visual location.

This does **not** invalidate the accepted resident-data result: A is still returned from its resident state without a Detail refetch. The defect belongs to presentation residency: the single visible detail presentation does not yet retain/restore a per-conversation semantic scroll anchor.

Implementation rule for the correction:

- scroll state remains presentation metadata, not a second conversation-data authority;
- prefer a semantic anchor tied to visible message identity plus relative offset where possible, rather than copying one global raw `contentOffset` between conversations;
- restoration must tolerate layout/height changes and large conversations;
- do not retain one full UIKit hierarchy per conversation merely to preserve scroll position.

Because b17 already exists, any product-code correction must use a new unique Candidate/build (next expected b18 after conflict/uniqueness gate). Never rebuild/reuse b17.

## b16 P0 findings and b17 closure

The b16 second review identified the following P0 defects. b17 contains source fixes, compiled/package evidence, and the user/device run now supplies direct evidence for the core navigation/coalescing/hidden-Sync portions noted below.

1. **Stale scope re-adoption** -> operation/transport context only validates against the current `AuthSessionStore` verified scope; stale transport cannot establish repository scope. Runtime account-switch purge remains untested because no supported switch route was exercised.
2. **Probe commit freshness** -> current `verifiedAccountContext()` is rechecked before installing completed probe session/scope.
3. **Abandoned waiters** -> superseded operations resolve old waiters with `operationSuperseded`; account reset resolves invalidated waiters with `accountContextChanged`.
4. **Ordinary presentation freshness** -> detail presentation uses selected identity + presentation generation.
5. **Sync A -> B -> A stale-visible bug** -> operation-first return/coalescing is now directly observed in exact b17 runtime.
6. **Global recovery presentation** -> recovery presentation derives from the selected conversation's active operation; exact b17 Sync-return behavior is accepted for the tested sequence.
7. **List freshness** -> repository list generation plus sidebar presentation generation; destructive stale-list overlap was not separately manufactured in the supplied runtime run.
8. **Task-handle window** -> replacement owner/cancel/start+attach/waiter ordering is compiled; b15 remains the accepted isolated replacement-under-load runtime baseline until b17-specific replacement is separately exercised.
9. **Repository execution domain** -> mutable repository state is main-thread-confined.
10. **Runtime diagnostics** -> exact b17 runtime demonstrates old->new selection hashes, resident/active/protected counts, coalescing and first-visible timing.
11. **Memory-warning active resident protection** -> source/CI covered; no system memory-warning acceptance event was captured in the supplied runtime run.
12. **Package identity** -> independently accepted for exact b17.

## Work identity / ordering

- **Work ID**: `DEV-multi-conversation-state`
- **User-facing name**: **多会话驻留与快速切换**
- **Dependency**: merged b15 recovery baseline.
- **Next serialized tasks**: `DEV-conversation-round-count` -> `DEV-send-stream`.

Do not create a separate auth-resume task; cold-start WebKit warm-up is already accepted inside recovery.

## State ownership model

Conceptually:

`verified account/workspace scope -> conversation ID -> resident conversation state`

`ConversationRepository` remains the sole production conversation-data authority.

Resident/operation state may own only evidence-backed data needed now:

- parsed current conversation detail needed to render;
- directly evidenced current branch-tip/current-node identity;
- terminal loaded/failed state;
- load/recovery operation kind, generation, task and waiters;
- later LRU metadata only once a measured policy exists;
- future response linkage only when Send/Stream evidence exists.

Mounted cells/view controllers are never the conversation-data cache. Raw HTTP payloads are discarded after parsing unless later evidence establishes a concrete requirement.

Foreground `selectedConversationID` is presentation state only. Loading, Sync, Reload and future response operations target an explicit identity and never mutate selection as a request side effect.

## Account/session ownership

`AuthSessionStore` remains the sole account-context/auth owner. Default persistent WebKit storage remains the sole persistent auth-secret authority.

Repository rules:

- only one repository account/transient-session acquisition may be in flight; concurrent first loads may share it;
- cached transient session is bound to the verified scope that created it;
- only a currently verified auth-owner snapshot/change signal may establish/change repository scope;
- list/detail/operation transport context is a consumer and cannot re-adopt an older scope;
- queued probe results are rechecked against the current auth-owner scope before commit;
- verified different scope purges old list/residents/operations/session/selection and rejects late old-scope results;
- invalidated consumers terminate deterministically.

Current source uses `userID + accountID` as the resident account key. This is evidence-backed for current personal-account source only. Non-personal workspace identity remains Unknown / Unverified.

## Single repository execution domain

Mutable repository authority uses one explicit execution domain. In b17 that owner is main-thread-confined for resident/list/account/session/operation state and diagnostics lookups that read those values.

Network transfer and pure parsing may occur off-main. Thread safety must fix the owner invariant, not create a second cache or duplicate state authority.

## Detail operation ownership

Required semantics:

- A and B may have independent detail operations;
- selecting B does not cancel A;
- explicit Reload/Sync A may supersede/cancel only A's older detail operation;
- same-target replacement preserves b15 cancel-before-replace behavior;
- equivalent same-A requests coalesce instead of duplicating network work;
- operation identity includes account scope + conversation ID + generation;
- late obsolete A cannot overwrite newer A;
- every waiter terminates on success, failure, supersede or account invalidation;
- do not impose an arbitrary global concurrency limit before device evidence.

Exact b17 runtime now confirms independent overlap and same-target coalescing for the supplied sequences.

## Resident terminal state / navigation

Resident logic distinguishes:

- not loaded / evicted;
- active operation;
- loaded;
- terminal failure;
- explicit Sync/Reload over that target.

On navigation to B:

1. Root changes foreground selection once.
2. If B has an active operation, the presentation joins/observes it.
3. Otherwise loaded B renders immediately with no Detail request.
4. Failed B remains failed; ordinary navigation does not implicitly retry.
5. Only missing/evicted B starts one ordinary load.

Returning B -> A follows the same rules. Exact b17 runtime accepts loaded return and in-flight coalescing. Failure residency remains unproven because no natural terminal failure was exercised.

## Recovery semantics

### Sync A

- captures A at invocation;
- does not change selection;
- may replace only A's older same-target detail operation;
- preserves loaded A on failure when applicable;
- B/C remain untouched.

Exact b17 runtime now accepts A -> B -> A before Sync terminal: returning A rejoined the same active Sync and applied its successful terminal result without a duplicate Sync caused by return.

### Reload A

- captures A at invocation;
- rebuilds A from one fresh server detail request;
- may clear A's resident according to accepted Reload semantics;
- replaces only A's older target operation;
- never resend/regenerate;
- B/C remain resident and independent.

Reload target isolation was not separately isolated in the supplied b17 run.

### Recovery presentation

The visible detail controller owns lightweight presentation only. It derives active Sync/Reload state from the selected conversation's repository operation identity and uses presentation freshness so hidden/obsolete completions cannot mutate another visible conversation.

Scroll anchor is also presentation state, but unlike recovery status it still needs per-conversation preservation/restoration as described in the reproduced P1 section.

Future Sync/Reload behavior while a Send/Stream response is active must follow actual Send/Stream protocol evidence; do not guess it here.

## List freshness/account isolation

- old-account list response cannot populate new-account state;
- obsolete same-scope list completion cannot overwrite a newer list generation;
- sidebar stale completion cannot mark a newer presentation idle;
- first-page refresh/reordering does not destroy resident detail because an ID is absent from the current first 28 items;
- list position is diagnostics only, never identity.

Pagination remains later Work.

## Current-node identity

Detail validates and walks `mapping/current_node` to build the visible branch. b17 retains `current_node` as the minimum directly evidenced branch-tip identity.

Do not re-fetch Detail merely to recover an identity already present, retain raw multi-megabyte mapping for convenience, or invent future Send graph requirements before protocol evidence.

## Residency / memory policy

Unlimited permanent residency is not acceptable because real conversations can be large.

A bounded LRU-style normal working set will be chosen **after real-device measurement**.

Current rules:

- selected entry protected;
- active detail/recovery operation protected;
- future active response/stream protected;
- memory warning may trim only eligible inactive terminal residents;
- no persistent chat-body disk cache;
- approximate visible-text bytes are correlation only and cannot justify/freeze capacity;
- do not add future-only access-order bookkeeping before a measured normal LRU policy is implemented.

The supplied b17 run exercised multiple large conversations and reached 6 residents, which is useful runtime behavior evidence but still insufficient to freeze a normal capacity without process/system memory evidence.

## Diagnostics

Privacy-safe runtime evidence includes/should include:

- explicit old/new irreversible selection hashes;
- resident hit/miss/state;
- detail started/coalesced/superseded/cancelled/completed;
- waiter count and terminal reason;
- hidden valid result stored;
- obsolete completion discard reason;
- account-scope bind/change/purge without raw IDs;
- list generation/stale discard;
- resident/active/protected counts;
- memory-warning eviction reason;
- return-to-resident first-visible timing.

The current schema does **not** log semantic scroll anchors; the b17 scroll-position defect is user-observed runtime evidence, not inferred from logs. Do not add raw message bodies/titles merely for anchor diagnostics.

Never log raw conversation/account IDs, titles, bodies, payloads, Cookie/Authorization values or tokens.

## Acceptance criteria

Before calling this Work Stable, exact real-device evidence should prove at minimum:

1. A loaded -> B loaded -> A renders A without a new Detail request. **Accepted in b17 supplied run.**
2. A loading -> B -> A completes hidden: A is retained and B is untouched. **Accepted in b17 supplied run.**
3. A loading -> B -> A before completion coalesces onto one A operation. **Accepted in b17 supplied run.**
4. Rapid A/B/C switching never shows another conversation's title/messages/error/recovery feedback. **Accepted for the observed b17 run.**
5. Sync A -> B -> A before terminal restores/observes the same active Sync and applies terminal state without a duplicate request. **Accepted in b17 supplied run.**
6. Reload/Sync A cancels/replaces only A's older target operation; B remains independent. **Sync target behavior observed; isolated Reload replacement remains open.**
7. Superseded/obsolete A cannot overwrite newer A; old waiters terminate without stale UI mutation. **Source/CI plus observed coalescing; isolated supersede terminal test remains open.**
8. A terminal failed load stays failed across navigation and does not silently retry. **Open — no natural failure exercised.**
9. Verified account change purges old state and rejects late old-scope callbacks; stale transport cannot re-adopt old scope. **Open runtime — no supported account switch exercised.**
10. Concurrent first loads share one transient-session acquisition. **No duplicate auth-probe issue observed in supplied overlap, but keep exact runtime criterion open unless explicitly isolated.**
11. Stale list callbacks cannot overwrite/reset a newer list request or sidebar state. **Open as destructive overlap criterion.**
12. `current_node` remains available without raw mapping retention. **Source/CI-backed; no contrary runtime result.**
13. Memory warning trims only eligible inactive residents. **Open — no memory-warning event captured.**
14. Several real conversations including at least one large conversation switch repeatedly without unbounded growth or repeat requests for still-resident entries. **Partially accepted: large conversations and 6 residents exercised; bounded-policy conclusion remains open.**
15. Rapid different-conversation in-flight loads record HTTP429/service pressure without automatic retry/global rate limiting. **Accepted for supplied run: up to 3 active operations; no HTTP429 observed.**
16. Accepted b15 manual Sync/Reload behavior remains intact for the target conversation. **Sync accepted in supplied b17 run; b15 remains accepted Reload/replacement baseline.**

Account/workspace runtime evidence beyond the current personal account remains separately Unknown until a real supported route exists and is tested.

## Candidate boundary / next correction

b17 is the first identity-valid Candidate and now carries accepted core real-device evidence for the tested switching/coalescing/hidden-Sync/rapid-overlap paths.

**Semantic scroll-anchor restoration remains P1 in architecture priority, but is now a reproduced b17 runtime defect rather than a hypothetical item.** It does not retroactively invalidate b17 core residency evidence.

If this P1 correction is implemented next, run the normal candidate/branch/conflict uniqueness gate and allocate b18 before touching product Candidate identity. Do not rebuild/reuse b17.

## Deterministic testing guidance

There is still no XCTest target. Adding one is separate project-file work and must not substitute for real-device validation.

Highest-value future pure tests include resident decisions, coalescing/waiter termination, target-isolated replacement, stale-generation rejection, stale-account rejection, account purge, single-flight auth acquisition, list freshness, LRU eligibility and current-branch normalization.

For scroll-anchor restoration, highest-value runtime checks are:

- A at top/middle/deep position -> B scroll -> A returns to the same semantic message/relative offset;
- repeat with a long A where cells have very different heights;
- Sync A while hidden/visible must not restore an obsolete anchor over a user scroll performed after return;
- resident eviction/reload should define whether the anchor remains valid or is discarded rather than guessing.

## Non-goals / prohibited shortcuts

- No separate authoritative repository per screen/conversation.
- No retained UIKit hierarchy/navigation stack as conversation-data authority.
- No selection mutation from load/sync/reload side effects.
- No cancellation merely because a conversation becomes hidden.
- No stale operation context restoring old account scope.
- No silently abandoned waiters.
- No reload-on-every-navigation.
- No unlimited final resident retention.
- No persistent chat-body/draft cache without separate privacy/storage requirement.
- No speculative retry, timer, watchdog, fallback, global rate limiter or compatibility shim.
- No copied persistent auth secrets or second account owner.
- No raw mapping retention to anticipate future Send/Edit/Regenerate.
- No capacity chosen from approximate text bytes alone.
- No full retained view hierarchy per conversation merely to preserve scroll position.
- No claim that concurrent A/B server operations are safe/unsafe beyond exact runtime evidence.
