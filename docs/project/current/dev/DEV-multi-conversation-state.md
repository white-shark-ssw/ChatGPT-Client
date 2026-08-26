# DEV-multi-conversation-state

## Status

**Active — b16 Candidate allocated; CI / Artifact / Runtime pending**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 send/stream 所需的多会话 freshness 与异步所有权基线。
- **Acceptance boundary**: A -> B -> A 普通导航不能销毁 A、不能因为 selection change 丢弃 A 的有效返回、不能仅因返回 A 再次联网；不同会话状态隔离；同会话等价请求 coalesce；Sync/Reload 只替换目标会话；旧 generation / 旧 account callback 不得覆盖新状态；失败终态不得因普通导航隐式重试；保留已验证的 `current_node` 身份；最终 resident 容量必须由真实设备测量决定。完整边界以 `MULTI_CONVERSATION_STATE_PLAN.md` 为准。
- **Baseline**: `0.1.0 (15)` Stable recovery; `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; recovery PR #10 merged.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; PR `Not created`.
- **Candidate identity**: **Reserved `DEV-multi-conversation-state-0.1.0-b16` / version `0.1.0 (16)`**. Product/config source for this exact Candidate is **`81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`**. Do not reuse b16 for later product-code changes after an Artifact is produced.
- **Expected artifact identity**: `ChatGPTClient-0.1.0-b16-dev-multi-conversation-state.ipa` from `scripts/build_ipa.sh`; CI upload bundle `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b16`.
- **Parallel/conflict check before b16 allocation**: `main` still `f155ddb...`; current dev directory contains only this Active Work + README; `BUILD_TEST_INDEX.md` ends at b15; GitHub has no open PR; therefore b16 was unique at allocation.

## b16 product changes

- `ConversationRepository` remains the sole production conversation-data authority.
- Selection is now mutated only by the Root navigation transition; sidebar and detail rendering no longer independently change selected ID.
- Resident keys are verified account scope (`userID + accountID`) + conversation ID.
- Parsed resident detail retains `currentNodeID` from the already-verified `current_node` field; raw mapping/body is not cached.
- Detail operation generation/task ownership is per conversation instead of one global selected slot.
- A valid detail response is committed to its target resident even when that conversation is hidden; selection controls presentation only.
- Equivalent same-conversation loads attach additional completions to the existing operation instead of launching another request.
- Initial account/transient-session acquisition is single-flight inside the repository, so rapid A/B opening before a cached native session exists does not start duplicate repository probes.
- Resident terminal state records either loaded detail or failure. Returning to a failed conversation returns the retained failure and exposes explicit Reload instead of silently retrying network I/O.
- Sync preserves an already-loaded target resident on failure; Reload explicitly clears and replaces only the target resident/request.
- `AuthSessionStore` remains the sole auth/account owner; it now exposes a lock-protected verified context snapshot and a context-change notification. Repository scope changes invalidate the old transient session, resident/list state and per-conversation operations.
- List success/failure delivery is scope-guarded so old-account callbacks cannot repopulate the new account UI.
- Root clears sidebar/detail presentation on account-scope reset.
- Detail recovery UI has a presentation generation guard so a hidden A Sync/Reload completion cannot hide/reset B's current toast/menu/spinner.
- Memory warning evicts non-selected resident terminal states and logs the trim. No arbitrary normal-operation LRU bound has been added.
- Diagnostics include resident hit/miss/state, same-conversation coalescing, hidden/foreground store, approximate resident text bytes, terminal state, memory-pressure eviction and account-scope reset. Existing protocol endpoint/header semantics were not changed.

## Files changed for b16

- `ChatGPTClient/Authentication/AuthSessionStore.swift`
- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient/RootViewController.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `.github/workflows/ios-foundation.yml`
- this checkpoint

## Evidence / validation state

- **Code written**: **Yes** — product/config source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`.
- **Static/source review**: **Yes, source-level only** — diff confined to expected owner/auth/root/build/workflow scope; global selected-detail task/generation removed; speculative access-order/LRU bookkeeping removed before Candidate allocation; account/session acquisition duplicate discovered in review and replaced with single-flight waiter ownership.
- **Compiler/local build**: **Not yet proven** in this environment; local container has no iOS SDK/repository network checkout path. GitHub CI is the authoritative compile/package gate.
- **CI passed**: **Pending**.
- **Artifact produced**: **Pending**.
- **Runtime/manual/real-device**: **Not tested**.
- **Stable/Frozen**: **No**.

## Still pending after b16 build gate

1. Confirm b16 compiles/packages; any product fix after a produced b16 Artifact must allocate b17 rather than reusing b16.
2. Real-device A -> B -> A and A -> B -> C tests: verify first-open requests, hidden A store, resident return without request, state isolation, same-ID coalescing, target-only Sync/Reload and no unexpected HTTP429 under different-conversation overlap.
3. Measure resident count / approximate text bytes / memory-warning behavior on the target iPhone/iOS17 setup. Only then choose a bounded LRU policy; do not guess a capacity from source alone.
4. Add semantic per-conversation scroll restoration before Stable if runtime confirms the current reused detail table loses meaningful position. Keep this as presentation state, not repository data authority.
5. Decide whether a minimal deterministic XCTest target remains conflict-light enough to justify in the next Candidate. No test target was added to b16 because the current Xcode project has only one explicit app target and adding a test target would be substantial project-file churn before the first compile/measurement gate.
6. After verified milestones, update `BUILD_TEST_INDEX.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md` and `TECHNICAL_DECISIONS.md` with exact evidence labels.

- **Next exact action**: inspect the GitHub Actions run triggered by `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; if CI fails, classify the exact compiler/build error and allocate a new Candidate before product fixes if b16 Artifact already exists. If CI succeeds, record run/artifact/checksum identity and prepare the b16 real-device matrix without claiming runtime acceptance.
- **Rejected / do-not-repeat**: separate repository per screen/conversation; retained VC/cell cache as data owner; load/sync/reload changing selection; cancellation on ordinary navigation; reload-on-every-navigation; unlimited retention as final architecture; speculative retry/timer/watchdog/fallback/global concurrency cap; persistent chat-body cache; future-only access-order bookkeeping before an actual LRU decision; treating title/text/list position as identity; guessing send/stream graph beyond `current_node` evidence.
- **Open risks**: b16 has not compiled yet; different-conversation concurrent detail requests may expose service-side pressure only measurable on device; final LRU bound is intentionally Unknown until measurement; semantic scroll restoration is not yet implemented; no runtime evidence exists for account switching under the new resident owner.
