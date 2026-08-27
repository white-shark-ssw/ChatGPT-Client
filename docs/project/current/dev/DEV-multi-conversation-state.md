# DEV-multi-conversation-state

## Status

**Active — b17 gate in progress after b16 Artifact identity rejection and second source review P0 findings**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 send/stream 所需的多会话 freshness 与异步所有权基线。
- **Baseline**: `0.1.0 (15)` Stable recovery; `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; recovery PR #10 merged.
- **Working branch / PR / head commit**: `dev/multi-conversation-state-20260827`; PR `Not created`; current branch head before b17 product allocation is documentation-only.
- **b16**: `DEV-multi-conversation-state-0.1.0-b16`, source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; CI Run `33009246356` success; Artifact `9621830284` identity rejected because build script embedded recovery b15 candidate/default slug. No b16 runtime claim. Never reuse b16.
- **Evidence**: Code written = Yes (b16 source); Static/source review = performed with unresolved P0 findings; CI = Yes for b16 compile/package only; Artifact = produced but rejected identity; Runtime/manual = No; Stable/Frozen = No.

## Required P0 fixes before first valid runtime Candidate

1. Reject delayed old transport/account contexts; a request context must never re-adopt stale account scope.
2. Recheck the authoritative verified `AuthSessionStore` context before committing a completed probe/transient session.
3. Complete superseded/account-reset coalesced waiters deterministically instead of silently dropping closures.
4. Give ordinary detail presentation a selection-cycle/freshness identity before obsolete waiter completions are surfaced.
5. Fix Sync A -> B -> A: returning to A while A recovery is active must observe/attach to its active operation and receive terminal state without duplicate network request.
6. Make recovery presentation conversation-targeted enough that navigating away/back does not lose the fact that A is still recovering or allow a conflicting second recovery.
7. Add deterministic same-scope list request/presentation freshness; account reset must not let an old list completion mutate new-list UI state.
8. Attach the already-resumed detail task handle synchronously on the repository owner domain so b15 cancel-before-replace semantics do not have a scheduling window.
9. Confine mutable repository reads/writes to one explicit owner domain; URLSession callbacks must not read mutable `conversations` directly.
10. Add privacy-safe old->new selection transition diagnostics and resident/protected/timing signals needed for A/B/C runtime proof.
11. Keep normal LRU capacity Unknown until real-device evidence; approximate text bytes are not process-memory evidence.
12. Current `userID + accountID` scope is personal-account evidence only; non-personal workspace isolation remains Unknown/Unverified.

## Candidate rule for b17

- Re-run uniqueness/conflict gate against current `main`, all Active DEV checkpoints, open PRs, `BUILD_TEST_INDEX.md`, Xcode build source and workflow.
- If b17 is unique, assemble **one atomic product/config commit** containing P0 owner fixes + package identity correction + Xcode/workflow b17 identity. Advance branch ref once so one candidate identity maps to one source/config tree and intended Artifact.
- Semantic per-conversation scroll-anchor restoration is P1 and is not a blocker for the first valid core b17 runtime Candidate.

## Runtime acceptance after valid Artifact

- A loaded -> B loaded -> A without a new Detail request.
- A loading -> B -> hidden A completion retained and B untouched.
- A loading -> B -> A before completion coalesces and reaches one terminal result.
- Sync A -> B -> A before Sync terminal updates visible A correctly without duplicate request.
- Reload/Sync replace only their target conversation.
- Failed A -> B -> A does not implicitly retry.
- Rapid A/B/C in-flight overlap records HTTP status/429 pressure without speculative retry/global rate limiter.
- Account-context purge/late-callback isolation requires a real supported runtime route before claiming acceptance.
- Memory-warning/residency evidence plus actual device/system memory observations inform later bounded LRU; do not infer capacity from text-byte estimates.

- **Next exact action**: finish the b17 uniqueness/conflict gate. If clean, prepare and publish exactly one atomic b17 product/config commit; then source-review exact b17 before accepting CI/Artifact as useful evidence.
