# DEV-multi-conversation-state

## Status

**Active — b16 compiled/packaged but Artifact identity rejected; second source review found P0 owner gaps that must be fixed before the first valid runtime Candidate**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 send/stream 所需的多会话 freshness 与异步所有权基线。
- **Acceptance boundary**: A -> B -> A 普通导航不能销毁 A、不能因为 selection change 丢弃 A 的有效返回、不能仅因返回 A 再次联网；不同会话状态隔离；同会话等价请求 coalesce；Sync/Reload 只替换目标会话；旧 generation / 旧 account callback 不得覆盖新状态；失败终态不得因普通导航隐式重试；保留已验证的 `current_node` 身份；最终 resident 容量必须由真实设备测量决定。完整边界以 `MULTI_CONVERSATION_STATE_PLAN.md` 为准。
- **Baseline**: `0.1.0 (15)` Stable recovery; `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; recovery PR #10 merged.
- **Working branch / PR / head commit**: `dev/multi-conversation-state-20260827`; PR `Not created`; current branch head `07af43156c4699c064d57a05fcf0f286821a231c` is documentation-only after b16 evidence updates; exact b16 product/config source remains `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`.
- **Parallel/conflict guard refreshed**: current branch is the only Active checkpoint under `docs/project/current/dev/`; GitHub has no open PR; `main` is still `f155ddb873540f7c80d6e66ebbfeb59ded26f011`. No branch/base conflict currently blocks this Work.

## Candidate history

### b16 — compile/package evidence only; runtime identity rejected

- **Candidate reservation**: `DEV-multi-conversation-state-0.1.0-b16`, version `0.1.0 (16)`.
- **Exact product/config source**: `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`.
- **CI**: Run `33009246356`, job `98310915318`, success; checkout/toolchain/build/inspect/upload all succeeded.
- **Artifact**: `9621830284`; upload ZIP digest `sha256:8b2925d26b1bc30d9cf63ddaa10bee3056b034c65972f35173d594f08ca520a5`.
- **Actual IPA**: `ChatGPTClient-0.1.0-b16-dev-conversation-recovery.ipa`; SHA-256 `114762593790795032daebb6d4b49a77ea98d46b9f99a3709d9c06c7feed1b3f`.
- **Package inspection**: embedded version/build `0.1.0 (16)`, `DiagnosticsSourceCommit=81e6774ae1f5`, minimum iOS14.0, device families `[1,2]`, Mach-O arm64.
- **Identity failure**: embedded `DiagnosticsCandidate` remained `DEV-conversation-recovery-0.1.0-b15`, and IPA suffix remained `dev-conversation-recovery` because `scripts/build_ipa.sh` still hard-coded both recovery defaults.
- **Disposition**: **Artifact identity rejected / superseded before real-device runtime**. b16 must never be rebuilt/reused for corrections because Artifact `9621830284` already exists.

## b16 implementation that is source/CI evidenced

- `ConversationRepository` remains the sole production conversation-data authority.
- Foreground selection is mutated only by Root navigation transition; loading/sync/reload no longer change selected ID as a side effect.
- Resident keys currently use verified `userID + accountID + conversationID`; this is evidenced for current personal-account source only, not proof of non-personal workspace scoping.
- Parsed detail retains `currentNodeID`; raw mapping/body is not cached.
- Detail generation/task ownership is per conversation; valid hidden ordinary-load results can be retained.
- Equivalent same-conversation ordinary loads coalesce and collect waiters.
- Initial account/transient-session acquisition is single-flight inside `ConversationRepository`.
- Resident terminal state retains loaded or failed result so ordinary return to a failed conversation does not intentionally issue another network request.
- Sync preserves an existing loaded resident on failure; Reload clears/replaces only its target.
- `AuthSessionStore` remains the auth/account owner and exposes a read-only verified context plus context-change notification; `.probing` itself does not invalidate an existing verified context.
- List/detail commits have account-scope checks; account reset clears list/residents/selection/native session and active detail operation records.
- Recovery UI has a presentation-generation guard that prevents a hidden old recovery callback from directly overwriting a newer visible conversation.
- Memory warning removes non-selected terminal resident states; active in-flight detail operations are not resident-map eviction victims.
- Diagnostics currently cover resident hit/miss/state, coalescing, terminal store/failure, approximate visible-text bytes, memory-warning eviction and account reset.

## Second source-review findings — must not be lost

These findings are source-backed against branch source `81e6774ae1f5...`; they downgrade the current implementation from “candidate-ready” even though b16 compiled.

1. **Critical stale account-scope re-adoption path**: `beginDetailOperation` calls `adoptAccountScope(context.scope)`. If a delayed old `ConversationTransportContext` executes after the repository has already reset to a newly verified scope, that operation can reset the repository back to the old scope instead of being rejected. A stale operation context is not account authority. Required fix: operation/list/detail contexts may only compare against the current authoritative verified scope; only a currently verified `AuthSessionStore` snapshot may establish/change repository scope.
2. **Probe-result freshness is not rechecked at commit**: after account probe success, the queued main-thread commit should verify that `AuthSessionStore.verifiedAccountContext()` still matches the returned scope before installing the transient session/scope. Otherwise an older probe result can be accepted after a newer context transition. Do not invent a second account owner; verify against the existing owner.
3. **Superseded/account-reset operation waiters are silently abandoned**: `cancelDetailOperation` removes the operation and cancellation returns without completing its collected closures; `resetAccountScope` also clears operations without terminally completing waiters. This violates the coalescing terminal-result contract. Superseded and old-account consumers need deterministic termination, while presentation generations prevent obsolete UI mutation.
4. **Ordinary detail presentation lacks its own freshness token**: `showConversation`'s ordinary load completion checks selected ID only. Silent waiter abandonment currently masks some stale-presentation cases. Before completing superseded waiters explicitly, ordinary load presentation must also reject stale generations/selection cycles deterministically.
5. **Hidden Sync -> return-to-A bug**: Sync preserves A's loaded resident while its replacement request is in flight. If user switches A -> B -> A before Sync completes, `showConversation(A)` immediately renders the old resident and does not attach to A's active Sync because a loaded resident exists. The original Sync callback is then ignored by the global presentation generation, so visible A can remain stale even after repository A is updated. Returning to A must restore/observe A's active recovery state or otherwise receive its terminal update without starting a duplicate request.
6. **Recovery presentation is guarded but not truly per conversation**: one global `recoveryActionInProgress`/generation prevents cross-conversation overwrite, but navigating away/back loses A's active recovery presentation and can re-enable another manual recovery while A still has one in flight. Before Stable, recovery presentation needs conversation-targeted operation identity/state (lightweight presentation state only, not a second data owner).
7. **List freshness owner is incomplete**: repository list loads have account-scope guards but no same-scope list generation/coalescing contract. Sidebar's current `loading` flag prevents ordinary UI reentry only; after an account reset, a late old-list completion can still clear the sidebar `loading` presentation while a new-scope list request is active. List request/presentation freshness must be deterministic before claiming account-switch isolation complete.
8. **Request task handle attachment has an avoidable cancellation window**: `requestConversationDetail` is entered from the main repository owner, but stores the already-resumed `URLSessionDataTask` back into `detailOperations` through a later `DispatchQueue.main.async`. The b15 contract requires same-target replacement to cancel the old task before starting replacement. Attach the handle synchronously on the owner domain so `taskPresent=false` is not an incidental window.
9. **Repository execution-domain rule is not fully enforced**: URLSession callbacks call `diagnosticsFields(for:)`, which reads mutable `conversations`, while that array is owned/mutated on main. Current public repository APIs also rely on current UI call sites being main-threaded rather than enforcing the owner. Background parsing is fine, but mutable repository reads/writes and list-position lookup must stay on one explicit owner domain.
10. **Selection diagnostics are insufficient for the planned runtime proof**: current `conversation.selected`/resident logs carry the new conversation hash/list position, but not one explicit old->new hashed selection transition. Add privacy-safe old/new hashes at the single selection owner so A/B/C traces can prove one transition rather than infer it from multiple events.
11. **Return-to-resident timing/protected counts are not yet measured**: the plan calls for return-to-resident first-visible timing plus resident/protected counts. Current approximate text-byte logging is useful correlation only and is not actual memory-footprint evidence. Do not choose/freeze an LRU capacity from text bytes alone.
12. **Account/workspace scope claim remains limited**: current scope key is `userID + accountID`; current runtime baseline is personal account only. Correct isolation for non-personal workspace variants remains `Unknown / Unverified` until current protocol/account evidence identifies any additional workspace identity required.
13. **b17 must be one atomic Candidate commit**: the workflow runs on pushes touching product/Xcode/script/workflow paths. Sequential GitHub Contents API edits after setting b17 could create multiple Artifacts sharing the same candidate/build identity. All b17 product/config/package/workflow changes must be assembled into one Git tree/commit and the branch ref advanced once; docs-only commits may remain separate because they do not trigger the candidate workflow.

## Evidence labels

- **Code written**: **Yes** — b16 source implementation exists.
- **Static/source review**: **Performed; unresolved P0 findings remain**. Do not describe the b16 source as source-review-passed/candidate-ready after the second review above.
- **CI passed**: **Yes**, b16 Run `33009246356`, proving compile/package path only for exact source `81e6774...`.
- **Artifact produced**: **Yes**, but b16 Artifact identity is **rejected** as above.
- **Runtime/manual/real-device**: **No** for this Work.
- **Stable/Frozen**: **No**.

## Pending / ordering after review

1. Keep b16 permanently historical/rejected; do not touch its identity again.
2. Before allocating b17, perform the normal uniqueness/conflict gate again against `main`, Active checkpoints, open PRs, Build Index and real Xcode/workflow identities.
3. Build **one atomic b17 product/config commit** that fixes the P0 owner defects above that are required for a valid multi-conversation runtime Candidate, together with the two evidenced package hard-codes and the b17 Xcode/workflow identity. Do not publish an intermediate b17 source/Artifact.
4. Re-review exact b17 source before accepting CI as useful evidence. In particular verify stale-scope rejection, waiter termination, hidden-Sync return, list freshness/presentation, synchronous task ownership and repository execution-domain confinement.
5. Produce/inspect exactly one intended b17 CI Artifact. Verify IPA filename, embedded candidate, embedded source, version/build, IPA SHA, arm64/iOS14 identity and workflow Artifact identity before offering it for device testing.
6. First real-device core tests: A loaded -> B loaded -> A with no new detail request; A loading -> B -> hidden A completion retained; A loading -> B -> A before completion coalesces; Sync A -> B -> A before Sync terminal; target-only Sync/Reload; failed A -> B -> A no implicit network retry; rapid A/B/C in-flight overlap and HTTP429 observation.
7. Account-context runtime isolation remains required before Stable, but the exact user-facing account-switch/logout test route is currently not established by source. Do not claim this criterion Runtime-tested until a real supported route exists and is exercised.
8. Use real-device residency behavior plus actual device/system memory observation where available, memory-warning behavior, resident/protected counts and timing evidence to choose a bounded normal-operation LRU policy. Approximate text bytes alone are not a memory-capacity measurement.
9. **Semantic per-conversation scroll-anchor restoration is P1 in `CLIENT_ARCHITECTURE_GAP_REVIEW.md`; it is not a blocker for the first valid b17 core runtime Candidate.** Implement it after the core owner/runtime evidence unless a new explicit requirement raises its priority. Do not delay the first valid Candidate solely for scroll restoration.
10. Decide whether a minimal XCTest target is justified after the first valid runtime Candidate; current one-target Xcode project means adding tests is nontrivial project-file churn.
11. Keep durable project docs synchronized with the active implementation/evidence state; do not leave multi-conversation marked merely “future / Planned” after source+CI implementation exists.

- **Next exact action**: update the durable state/module/plan documents to reflect this second review, then—only when product work resumes—re-run the b17 uniqueness gate and prepare one atomic b17 commit containing the required owner fixes + package identity correction + Xcode/workflow bump. Do not include semantic scroll restoration as a b17 blocker.
- **Rejected / do-not-repeat**: reuse b16; let an incoming stale operation context reset repository account scope; silently abandon coalesced waiters as the long-term contract; separate repository per screen/conversation; retained VC/cell cache as data owner; load/sync/reload changing selection; cancellation on ordinary navigation; reload-on-every-navigation; unlimited retention as final architecture; speculative retry/timer/watchdog/fallback/global concurrency cap; persistent chat-body cache; future-only access-order bookkeeping before actual LRU decision; treating title/text/list position as identity; choosing LRU capacity from approximate text bytes alone; guessing send/stream graph beyond `current_node` evidence.
- **Open risks**: no multi-conversation real-device evidence yet; different-conversation concurrent requests may expose service-side pressure only on device; LRU bound remains Unknown by rule; non-personal workspace scope remains Unknown; user-facing account-switch test route is not established; b16 packaging identity is rejected; current source has the P0 defects enumerated above.
