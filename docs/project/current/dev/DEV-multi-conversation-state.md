# DEV-multi-conversation-state

## Status

**Active — b16 compiled/packaged but Artifact identity rejected; b17 correction required**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 send/stream 所需的多会话 freshness 与异步所有权基线。
- **Acceptance boundary**: A -> B -> A 普通导航不能销毁 A、不能因为 selection change 丢弃 A 的有效返回、不能仅因返回 A 再次联网；不同会话状态隔离；同会话等价请求 coalesce；Sync/Reload 只替换目标会话；旧 generation / 旧 account callback 不得覆盖新状态；失败终态不得因普通导航隐式重试；保留已验证的 `current_node` 身份；最终 resident 容量必须由真实设备测量决定。完整边界以 `MULTI_CONVERSATION_STATE_PLAN.md` 为准。
- **Baseline**: `0.1.0 (15)` Stable recovery; `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; recovery PR #10 merged.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; PR `Not created`.

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

## b16 product changes that compiled successfully

- `ConversationRepository` remains the sole production conversation-data authority.
- Selection is mutated only by Root navigation transition; sidebar/detail rendering no longer independently mutate selected ID.
- Resident keys are verified account scope (`userID + accountID`) + conversation ID.
- Parsed detail retains `currentNodeID`; raw mapping/body is not cached.
- Detail generation/task ownership is per conversation; valid hidden-conversation results are retained.
- Equivalent same-conversation loads coalesce and retain all waiters.
- Initial account/transient-session acquisition is single-flight.
- Resident terminal state retains loaded or failed result so ordinary return to a failed conversation does not become implicit retry.
- Sync preserves existing loaded resident on failure; Reload clears/replaces only its target.
- Auth remains owned by `AuthSessionStore`; verified scope change invalidates old native transient session, residents/list, selection and per-conversation operations.
- List callbacks are account-scope guarded.
- Recovery UI uses presentation generation so stale hidden A completion cannot reset B feedback.
- Memory warning evicts non-selected resident terminal states; no guessed normal-operation LRU cap exists.
- Diagnostics cover hit/miss/state/coalescing/hidden store/terminal state/text-byte estimate/memory-pressure eviction/account reset.

## Evidence labels

- **Code written**: **Yes**.
- **Static/source review**: **Yes** for b16 source scope and owner invariants.
- **CI passed**: **Yes**, b16 Run `33009246356`.
- **Artifact produced**: **Yes**, but b16 Artifact identity is **rejected** as above.
- **Runtime/manual/real-device**: **No** for this Work.
- **Stable/Frozen**: **No**.

## Pending

1. Allocate b17 only after rechecking `main`, Active checkpoints, PRs and `BUILD_TEST_INDEX.md` (which now records b16).
2. In b17 fix only the evidenced packaging hard-codes in `scripts/build_ipa.sh`, bump Xcode/CI Candidate identity, and preserve correct source/candidate/IPA naming.
3. Before the first valid runtime Candidate, add semantic per-conversation scroll restoration as presentation state if it can be done without changing repository authority. This is an explicit multi-conversation acceptance item and should not wait for LRU measurement.
4. Produce/inspect b17 CI Artifact. Verify filename, embedded candidate, embedded source, build, IPA SHA and arm64/iOS14 identity before offering it for device testing.
5. Real-device A -> B -> A / A -> B -> C / same-ID coalescing / failure-return / target-only Sync/Reload / memory-warning tests. Record whether different-conversation overlap causes HTTP429 or other pressure.
6. Use b17 runtime resident count/text-byte/memory-pressure evidence to choose a bounded LRU capacity. Do not guess a bound from CI/source.
7. Decide whether a minimal XCTest target is justified after the first valid runtime Candidate; current explicit one-target Xcode project means adding tests is nontrivial project-file churn.
8. Update `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md` after the next verified milestone, keeping Runtime/Stable labels separate from CI/Artifact.

- **Next exact action**: perform the b17 uniqueness/conflict gate, then bump Xcode/CI to `DEV-multi-conversation-state-0.1.0-b17` and remove the two evidenced recovery hard-codes from `scripts/build_ipa.sh`; no other packaging abstraction or fallback should be introduced.
- **Rejected / do-not-repeat**: reuse b16; separate repository per screen/conversation; retained VC/cell cache as data owner; load/sync/reload changing selection; cancellation on ordinary navigation; reload-on-every-navigation; unlimited retention as final architecture; speculative retry/timer/watchdog/fallback/global concurrency cap; persistent chat-body cache; future-only access-order bookkeeping before actual LRU decision; treating title/text/list position as identity; guessing send/stream graph beyond `current_node` evidence.
- **Open risks**: no runtime evidence yet; different-conversation concurrent requests may expose service-side pressure only on device; LRU bound remains Unknown by rule; account-switch runtime still unverified; semantic scroll restoration is not yet implemented.
