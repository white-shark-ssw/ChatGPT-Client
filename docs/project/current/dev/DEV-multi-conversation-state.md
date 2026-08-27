# DEV-multi-conversation-state

## Status

**Active — b17 exact source passed static/local parse + CI + independent Artifact identity inspection; ready for real-device multi-conversation validation; Runtime/Stable still pending**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 send/stream 所需的多会话 freshness 与异步所有权基线。
- **Baseline**: `0.1.0 (15)` Stable recovery; base `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; recovery PR #10 merged.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; PR `Not created`.
- **Current candidate**: `DEV-multi-conversation-state-0.1.0-b17`, version `0.1.0 (17)`.
- **Exact b17 product/config source**: `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`.
- **Atomicity evidence**: b17 source was assembled as Git blobs/tree/commit off-branch, reviewed, then branch ref advanced exactly once. Compared with parent `76728a4a24e1825df8ee9f356ecdc32b052a035b`, exactly four files changed: `ConversationFeature.swift`, Xcode project, workflow and `scripts/build_ipa.sh`.
- **Final artifact conflict gate**: before accepting the Artifact, `main` was still `f155ddb873540f7c80d6e66ebbfeb59ded26f011`, `current/dev/` still contained only this Active Work plus README, and GitHub had no open PR. No parallel/base conflict invalidated b17.

## Candidate history

### b16 — historical / rejected before runtime

- Exact source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; CI Run `33009246356` succeeded.
- Artifact `9621830284` was identity-rejected because `scripts/build_ipa.sh` embedded recovery-b15 candidate/default IPA slug.
- Second source review also found stale-scope, waiter, hidden-Sync, list-freshness, task-handle and owner-domain gaps.
- No real-device run. b16 must never be reused.

### b17 — valid runtime Candidate

- **Static/local**: final `ConversationFeature.swift` blob `1034cff72dea36d6d7e835bdf52dcfe2cdc8e38d`; local Git-blob hash matched; `swiftc -frontend -parse` passed.
- **CI**: Run `33045536770`, job `98428537619`, success. Exact checkout `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; Xcode 16.4 / build 16F6; Release target `arm64-apple-ios14.0`; log ends `BUILD SUCCEEDED`.
- **CI identity inputs**: `DIAGNOSTICS_CANDIDATE=DEV-multi-conversation-state-0.1.0-b17`; `SOURCE_COMMIT=bc69d58b3245`.
- **Artifact**: `9635486304`, name `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b17`, uploaded ZIP digest `sha256:bf6aed8cebcb08153fbe8fac6868ce60c0ef4bd7876340246912ba8edbed1c33`.
- **IPA**: `ChatGPTClient-0.1.0-b17-dev-multi-conversation-state.ipa`; SHA-256 `ed551deac0335e47da56da36ec2a8a20550613ac072ac1ddf0b84790278318dc`; independent SHA equals generated sidecar.
- **Independent package inspection**: `CFBundleShortVersionString=0.1.0`; `CFBundleVersion=17`; `DiagnosticsCandidate=DEV-multi-conversation-state-0.1.0-b17`; `DiagnosticsSourceCommit=bc69d58b3245`; `MinimumOSVersion=14.0`; `UIDeviceFamily=[1,2]`; Mach-O 64-bit arm64.
- **Disposition**: **valid exact runtime Candidate**. This is Artifact identity acceptance only, not runtime acceptance.

## b17 owner fixes written and compiled

1. **Stale account context cannot re-adopt scope**: request/transport context only validates against the current Auth owner; repository scope changes are driven by a currently verified `AuthSessionStore` snapshot/change signal.
2. **Probe commit freshness**: completed account probe rechecks `verifiedAccountContext()` on the main owner before installing its transient session/scope.
3. **Waiter terminal contract**: replaced same-target operations cancel the old task and deterministically complete old waiters with `operationSuperseded`; account reset completes cancelled operation waiters with `accountContextChanged`.
4. **Replacement ordering**: new operation owner is installed; old task is cancelled; replacement task is created and its handle synchronously attached on the main owner; only then are old waiters notified.
5. **Operation-first resident lookup**: an existing per-conversation operation is joined before a loaded/failed resident is returned, allowing return-to-A to observe an in-flight Sync/Reload instead of silently rendering only stale resident data.
6. **Target-specific recovery**: Sync/Reload capture an explicit conversation ID; they do not derive mutation target from foreground selection after invocation.
7. **Recovery presentation derives from selected conversation operation**: no global recovery-in-progress authority. Returning to A during active Sync/Reload restores A presentation and coalesces onto its existing operation; B/C remain independent.
8. **Ordinary presentation freshness**: detail controller uses presentation generation + selected ID guard so obsolete selection-cycle completions cannot overwrite the visible conversation.
9. **List freshness**: repository list generation rejects obsolete same-scope/account-reset results; sidebar has presentation generation so late old-list completion cannot end a newer presentation state.
10. **Repository execution domain**: mutable repository state is main-thread confined with explicit preconditions; URLSession callbacks use immutable captured diagnostics fields and commit results through main.
11. **Memory warning protection**: resident entries belonging to selected or active detail/recovery operations are protected; only eligible inactive terminal residents are trimmed.
12. **Diagnostics**: one owner logs old->new hashed selection transition; resident diagnostics expose resident/active/protected counts; immediate resident render logs `resident.firstVisible` timing. Approximate text bytes remain correlation only, not process-memory evidence.
13. **Package identity**: Xcode build/candidate is b17; workflow Artifact name is b17; build-script default candidate is b17 and IPA slug is `dev-multi-conversation-state`.

## Evidence labels

- **Code written**: **Yes — b17 exact source published**.
- **Static/local checks**: **Passed — Swift parse + exact blob identity**.
- **CI passed**: **Yes — Run `33045536770`**.
- **Artifact produced**: **Yes — Artifact `9635486304`, identity independently accepted**.
- **Runtime/manual/real-device**: **No yet for b17**.
- **Stable/Frozen**: **No**. b15 remains the accepted Stable/runtime baseline.

## Real-device core matrix for b17

Use the exact b17 IPA and capture diagnostics after each sequence when practical. Do not infer success only from UI appearance.

1. **Resident return**: load A fully -> load B fully -> return A. Expected: A renders from resident state; no new A detail request solely because of navigation; `resident.firstVisible`/resident counts are available.
2. **Hidden completion**: start A detail -> switch B before A completes -> let A finish hidden -> return A. Expected: valid hidden A result is stored; B is never overwritten; return A does not refetch.
3. **Same-target coalescing**: start A -> B -> return A before original A finishes. Expected: return joins A's active operation; no duplicate A detail request.
4. **Sync A -> B -> A**: with A loaded, start `同步最新消息`, switch B, then return A before Sync terminal. Expected: A shows/restores active Sync presentation, joins the same operation, and applies terminal result when it completes; no duplicate Sync/detail request caused by return.
5. **Reload target isolation**: start Reload A, switch B. Expected: A replacement owns only A; B remains independent; obsolete A waiter/callback cannot mutate B.
6. **Failure residency**: make/observe a genuine A detail terminal failure if naturally encountered -> B -> A. Expected: ordinary return to A does not issue an implicit retry; explicit Reload remains available. Do not manufacture unsafe network conditions solely for this case.
7. **Rapid A/B/C overlap**: open three different conversations while prior detail loads are still active. Expected: different conversations do not cancel each other; watch for HTTP429/service pressure without adding automatic retry/global concurrency cap.
8. **Manual replacement regression**: while A ordinary load is active, trigger Sync/Reload A. Expected: same-target old task is cancelled before replacement; no stale mutation; compare against b15 accepted behavior and observe HTTP429.
9. **Memory behavior**: exercise multiple small and large residents, capture resident/active/protected counts and device/system memory observations where available. Do not choose LRU capacity from approximate text bytes alone.

## Remaining acceptance / risks

- Account-context purge/late-callback isolation still needs a real supported runtime account-switch/logout route before claiming that criterion Runtime-tested.
- Normal-operation resident/LRU capacity remains Unknown until device/system memory evidence; approximate text bytes are insufficient.
- Current `userID + accountID` scope remains personal-account evidence only; non-personal workspace isolation is Unknown/Unverified.
- Semantic scroll-anchor restoration remains P1 and does not block core multi-conversation acceptance.
- No XCTest/UI-test target exists; this Candidate's automated evidence is syntax/static + real Xcode Release CI + package inspection.

- **Next exact action**: install and test exact `DEV-multi-conversation-state-0.1.0-b17` on the target iPhone/iOS17 scope using the core matrix above. Record exact user/runtime results and diagnostics against b17. If a product defect is found, mark b17 runtime result accordingly and allocate b18 before any product-code correction; never rebuild/reuse b17.
