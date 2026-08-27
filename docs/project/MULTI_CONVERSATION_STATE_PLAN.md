# Multi-Conversation State / Residency Plan

_Last updated: 2026-08-27; refreshed after b17 static/CI/Artifact validation._

## Purpose

Support normal use of several ChatGPT development conversations at the same time without making UI navigation destroy already-loaded state.

Core invariant:

> Selecting conversation B changes what is visible; it does not destroy conversation A's authoritative local state, cancel A's owned work merely because A became hidden, or force A to reload merely because A is no longer selected.

This Work is the structural prerequisite for production send/stream ownership.

See `CLIENT_ARCHITECTURE_GAP_REVIEW.md` for the broader pre-send architecture and `current/dev/DEV-multi-conversation-state.md` for exact branch/candidate evidence and the current next action.

## Accepted baseline vs Active implementation

### Accepted Stable baseline

`DEV-conversation-recovery-0.1.0-b15` is merged Stable for the recorded Plus/personal iPhone/iOS17 recovery scope. Current accepted runtime baseline remains `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`.

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
- **No b17 runtime/manual/real-device evidence exists yet.** Code/static/CI/Artifact success must not be described as runtime correctness.

## b16 P0 findings and b17 static closure

The b16 second review identified the following P0 source defects. b17 now contains source-level fixes and has compiled/package evidence for each affected source path; real-device behavior remains to be proven.

1. **Stale scope re-adoption** -> b17 operation/transport context only validates against the current `AuthSessionStore` verified scope; stale transport cannot establish repository scope.
2. **Probe commit freshness** -> b17 rechecks current `verifiedAccountContext()` before installing completed probe session/scope.
3. **Abandoned waiters** -> b17 superseded operations resolve old waiters with `operationSuperseded`; account reset resolves invalidated waiters with `accountContextChanged`.
4. **Ordinary presentation freshness** -> b17 detail presentation uses selected identity + presentation generation.
5. **Sync A -> B -> A stale-visible bug** -> b17 checks/joins an active per-conversation operation before returning a loaded resident, so returning A can observe A's existing Sync/Reload terminal result.
6. **Global recovery presentation** -> b17 derives recovery presentation from the selected conversation's active operation rather than a global recovery-in-progress authority.
7. **List freshness** -> b17 adds repository list generation plus sidebar presentation generation.
8. **Task-handle window** -> b17 installs the replacement owner, cancels old task, starts/attaches the replacement task synchronously on the owner domain, then resolves old waiters.
9. **Repository execution domain** -> b17 main-thread-confines mutable repository state and avoids background reads of mutable list state.
10. **Missing runtime diagnostics** -> b17 includes explicit old->new hashed selection transition, resident/active/protected counts and resident first-visible timing.
11. **Memory-warning active resident protection** -> b17 protects selected and active-operation residents; only eligible inactive terminal entries are trimmed.
12. **Package identity** -> b17 removes the b16 recovery candidate/slug hard-codes and independently verifies the correct package identity.

These are source/CI/Artifact closure statements only. They become accepted behavior only after exact b17 real-device evidence.

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

Returning B -> A follows the same rules.

## Recovery semantics

### Sync A

- captures A at invocation;
- does not change selection;
- may replace only A's older same-target detail operation;
- preserves loaded A on failure when applicable;
- B/C remain untouched.

If user switches A -> B -> A before Sync terminal, returning A must remain attached to A's already-active Sync and advance to its terminal result without another network request.

### Reload A

- captures A at invocation;
- rebuilds A from one fresh server detail request;
- may clear A's resident according to accepted Reload semantics;
- replaces only A's older target operation;
- never resend/regenerate;
- B/C remain resident and independent.

### Recovery presentation

The visible detail controller owns lightweight presentation only. It derives active Sync/Reload state from the selected conversation's repository operation identity and uses presentation freshness so hidden/obsolete completions cannot mutate another visible conversation.

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

Use device/system memory observation where available, resident/protected counts, first-visible timing, memory warnings and repeated switching across small/large conversations.

## Diagnostics

Privacy-safe runtime evidence should include:

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

Never log raw conversation/account IDs, titles, bodies, payloads, Cookie/Authorization values or tokens.

## Acceptance criteria

Before calling this Work Stable, exact real-device evidence should prove at minimum:

1. A loaded -> B loaded -> A renders A without a new Detail request.
2. A loading -> B -> A completes hidden: A is retained and B is untouched.
3. A loading -> B -> A before completion coalesces onto one A operation.
4. Rapid A/B/C switching never shows another conversation's title/messages/error/recovery feedback.
5. Sync A -> B -> A before terminal restores/observes the same active Sync and applies terminal state without a duplicate request.
6. Reload/Sync A cancels/replaces only A's older target operation; B remains independent.
7. Superseded/obsolete A cannot overwrite newer A; old waiters terminate without stale UI mutation.
8. A terminal failed load stays failed across navigation and does not silently retry.
9. Verified account change purges old state and rejects late old-scope callbacks; stale transport cannot re-adopt old scope.
10. Concurrent first loads share one transient-session acquisition.
11. Stale list callbacks cannot overwrite/reset a newer list request or sidebar state.
12. `current_node` remains available without raw mapping retention.
13. Memory warning trims only eligible inactive residents.
14. Several real conversations including at least one large conversation switch repeatedly without unbounded growth or repeat requests for still-resident entries.
15. Rapid different-conversation in-flight loads record HTTP429/service pressure without automatic retry/global rate limiting.
16. Accepted b15 manual Sync/Reload behavior remains intact for the target conversation.

Account/workspace runtime evidence beyond the current personal account remains separately Unknown until a real supported route exists and is tested.

## First valid Candidate boundary

b17 is now the first identity-valid core runtime Candidate. Its P0 source boundary is:

- stale-scope rejection/current-auth-owner verification;
- deterministic waiter lifecycle and matching UI freshness;
- hidden Sync return correctness;
- list freshness/presentation correctness;
- deterministic same-target cancellation/task ownership;
- one repository execution domain;
- privacy-safe runtime diagnostics;
- correct unique Candidate/IPA identity.

**Semantic scroll-anchor restoration is P1 and does not block b17 runtime proof.**

## Deterministic testing guidance

There is still no XCTest target. Adding one is separate project-file work and must not be used as a substitute for b17 real-device validation.

Highest-value future pure tests include resident decisions, coalescing/waiter termination, target-isolated replacement, stale-generation rejection, stale-account rejection, account purge, single-flight auth acquisition, list freshness, LRU eligibility and current-branch normalization.

Real-device tests remain mandatory for networking, HTTP429 behavior, UI switching, account/WebKit behavior, memory pressure and performance.

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
- No claim that concurrent A/B server operations are safe/unsafe until exact runtime evidence exists.
