# DEV-multi-conversation-state

## Status

**Active — b17 exact source passed static/local + CI + Artifact; core real-device multi-conversation sequences accepted for tested iPhone/iOS17 scope; semantic scroll-anchor restoration is a reproduced P1 defect; full Work Stable acceptance still pending**

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

### b17 — identity-valid runtime Candidate

- **Static/local**: final `ConversationFeature.swift` blob `1034cff72dea36d6d7e835bdf52dcfe2cdc8e38d`; local Git-blob hash matched; `swiftc -frontend -parse` passed.
- **CI**: Run `33045536770`, job `98428537619`, success. Exact checkout `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; Xcode 16.4 / build 16F6; Release target `arm64-apple-ios14.0`; log ends `BUILD SUCCEEDED`.
- **CI identity inputs**: `DIAGNOSTICS_CANDIDATE=DEV-multi-conversation-state-0.1.0-b17`; `SOURCE_COMMIT=bc69d58b3245`.
- **Artifact**: `9635486304`, name `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b17`, uploaded ZIP digest `sha256:bf6aed8cebcb08153fbe8fac6868ce60c0ef4bd7876340246912ba8edbed1c33`.
- **IPA**: `ChatGPTClient-0.1.0-b17-dev-multi-conversation-state.ipa`; SHA-256 `ed551deac0335e47da56da36ec2a8a20550613ac072ac1ddf0b84790278318dc`; independent SHA equals generated sidecar.
- **Independent package inspection**: `CFBundleShortVersionString=0.1.0`; `CFBundleVersion=17`; `DiagnosticsCandidate=DEV-multi-conversation-state-0.1.0-b17`; `DiagnosticsSourceCommit=bc69d58b3245`; `MinimumOSVersion=14.0`; `UIDeviceFamily=[1,2]`; Mach-O 64-bit arm64.
- **Disposition**: valid exact runtime Candidate. Artifact identity acceptance is distinct from runtime acceptance.

## b17 real-device evidence — 2026-08-27

Exact exported diagnostics identify `0.1.0 (17)`, candidate `DEV-multi-conversation-state-0.1.0-b17`, source `bc69d58b3245`, iPhone / iOS17.0. User followed the requested core switching/coalescing/hidden-completion/Sync/rapid-switch sequences and reported no major functional issue except scroll-position restoration.

Accepted evidence for the tested sequences:

1. **Resident return**: repeated returns to already-loaded conversations logged `resident.hit` and `resident.firstVisible` without a new same-target Detail request solely because of navigation. Observed `resident.firstVisible.elapsedMs` values in the export are approximately `0.23–0.78 ms`.
2. **Same-target coalescing while loading**: returning to an in-flight conversation logged `detail.coalesced` with `completionCount=2`; the original Detail operation remained the owner rather than starting a duplicate target request.
3. **Hidden completion**: a Detail operation completed while another conversation was foreground and logged `resident.stored visibility=hidden`; later navigation returned through `resident.hit`.
4. **Sync A -> B -> A**: conversation `sha256:8922c7c08d04` started Sync generation 2; after switching away and returning before terminal, the return logged `resident.hit activeOperationKind=sync` and `detail.coalesced completionCount=2`; the same Sync later returned HTTP200 and `latestSync.end status=ok` with 832 visible messages and no duplicate Sync caused by the return.
5. **Rapid multi-conversation overlap**: diagnostics reached `activeOperationCount=3`; different conversations completed independently, including hidden resident stores. No HTTP429 event appears in the supplied b17 diagnostic export.
6. **Residency scale observed, not capacity evidence**: resident count reached 6 and `residentTotalApproximateTextBytes` reached `6724764` in the export. This is only the existing approximate text correlation metric and is not process-memory evidence or a basis for freezing LRU capacity.

### Reproduced P1 defect — per-conversation scroll anchor

User reproduced the previously planned P1 gap: leave conversation A around ~10% scroll position, switch to B and scroll B, then return to A; A no longer stays at the same semantic/visual position. This is **not a resident-data ownership failure**: b17 still returns A from resident state, but the single visible detail presentation does not yet preserve a per-conversation semantic scroll anchor.

This issue was already explicitly scoped in project docs as **P1 semantic per-conversation scroll-anchor restoration** and did not block the first core b17 runtime proof. It is now upgraded from planned P1 work to **runtime-reproduced P1 defect**.

The current diagnostic schema does not record table/collection scroll anchor identity/offset, so the scroll-position defect is grounded by the user's direct runtime observation rather than inferred from diagnostics.

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
- **Runtime/manual/real-device**: **Yes, partial/core accepted for the tested iPhone/iOS17 sequences above; P1 scroll-anchor defect reproduced**.
- **Stable/Frozen**: **No**. b15 remains the merged Stable baseline until this Work completes/merges.

## Real-device core matrix status for b17

1. **Resident return**: **Accepted in supplied run** — resident hits/first-visible observed; no navigation-only refetch observed.
2. **Hidden completion**: **Accepted in supplied run** — valid hidden result stored and later hit.
3. **Same-target coalescing**: **Accepted in supplied run** — `detail.coalesced completionCount=2` observed.
4. **Sync A -> B -> A**: **Accepted in supplied run** — return rejoined active Sync and same operation completed HTTP200/ok.
5. **Reload target isolation**: not separately proven by the supplied run.
6. **Failure residency**: not naturally encountered/proven in the supplied run.
7. **Rapid A/B/C overlap / rate pressure**: **Accepted for observed run** — up to 3 active operations, independent completions, no HTTP429 in export.
8. **Manual replacement regression**: b15 remains the accepted replacement baseline; b17-specific replacement-under-load was not separately isolated in this supplied run.
9. **Memory behavior**: multiple large residents were exercised and counts captured, but no process-memory/LRU capacity acceptance yet.

## Remaining acceptance / risks

- **P1 scroll anchor**: runtime reproduced as described above. Fix should preserve a semantic/per-conversation anchor rather than copy B's raw scroll offset into A; implementation must remain presentation state and must not create a second conversation-data authority.
- Account-context purge/late-callback isolation still needs a real supported runtime account-switch/logout route before claiming that criterion Runtime-tested.
- Normal-operation resident/LRU capacity remains Unknown until device/system memory evidence; approximate text bytes are insufficient.
- Current `userID + accountID` scope remains personal-account evidence only; non-personal workspace isolation is Unknown/Unverified.
- No XCTest/UI-test target exists; this Candidate's automated evidence is syntax/static + real Xcode Release CI + package inspection.

- **Next exact action**: treat b17 as the accepted core runtime evidence for the tested switching/coalescing/hidden-Sync/rapid-overlap sequences, while keeping the Work Active. Before any product-code correction, run candidate/branch conflict uniqueness again and allocate **b18**; the next smallest user-visible correction is the now-reproduced P1 per-conversation semantic scroll-anchor restoration. Do not rebuild or reuse b17. Remaining account-switch/failure/LRU acceptance stays separate and must not be guessed from this run.
