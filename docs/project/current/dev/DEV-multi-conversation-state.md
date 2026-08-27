# DEV-multi-conversation-state

## Status

**Active — b17 core real-device multi-conversation sequences accepted for tested iPhone/iOS17 scope; b18 reserved for the reproduced P1 semantic per-conversation scroll restoration; Stable acceptance still pending**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 send/stream 所需的多会话 freshness 与异步所有权基线。
- **Baseline**: `0.1.0 (15)` Stable recovery; base `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; recovery PR #10 merged.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; PR `Not created`.
- **Last runtime-tested candidate**: `DEV-multi-conversation-state-0.1.0-b17`, version `0.1.0 (17)`.
- **Reserved next candidate**: `DEV-multi-conversation-state-0.1.0-b18`, version `0.1.0 (18)`; product source pending.
- **Exact b17 product/config source**: `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`.
- **Current pre-b18 docs head before product implementation**: Build/Test reservation commit `88dde44b92e4c1839fb7e57ac4b89c0c8a00b4aa`; prior branch head `5603ea7d0ab22cd9c42e6de73e3eb81048bcdafb` was docs-only.
- **b18 uniqueness/conflict gate**: `main` remains `f155ddb873540f7c80d6e66ebbfeb59ded26f011`; no open PR; `current/dev/` contains only this Active Work plus README; branch Actions contain only historical b16 and b17 product runs; Build/Test Index had no b18 before reservation.

## Candidate history

### b16 — historical / rejected before runtime

- Exact source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; CI Run `33009246356` succeeded.
- Artifact `9621830284` was identity-rejected because `scripts/build_ipa.sh` embedded recovery-b15 candidate/default IPA slug.
- Second source review also found stale-scope, waiter, hidden-Sync, list-freshness, task-handle and owner-domain gaps.
- No real-device run. b16 must never be reused.

### b17 — identity-valid / core runtime-evidenced

- **Static/local**: final `ConversationFeature.swift` blob `1034cff72dea36d6d7e835bdf52dcfe2cdc8e38d`; local Git-blob hash matched; `swiftc -frontend -parse` passed.
- **CI**: Run `33045536770`, job `98428537619`, success. Exact checkout `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; Xcode 16.4 / build 16F6; Release target `arm64-apple-ios14.0`; log ends `BUILD SUCCEEDED`.
- **Artifact**: `9635486304`, name `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b17`, uploaded ZIP digest `sha256:bf6aed8cebcb08153fbe8fac6868ce60c0ef4bd7876340246912ba8edbed1c33`.
- **IPA**: `ChatGPTClient-0.1.0-b17-dev-multi-conversation-state.ipa`; SHA-256 `ed551deac0335e47da56da36ec2a8a20550613ac072ac1ddf0b84790278318dc`; independent SHA equals generated sidecar.
- **Independent package inspection**: `CFBundleShortVersionString=0.1.0`; `CFBundleVersion=17`; `DiagnosticsCandidate=DEV-multi-conversation-state-0.1.0-b17`; `DiagnosticsSourceCommit=bc69d58b3245`; `MinimumOSVersion=14.0`; `UIDeviceFamily=[1,2]`; Mach-O 64-bit arm64.
- **Disposition**: core runtime evidence accepted for the exact tested sequences below; Work remains Active.

## b17 real-device evidence — 2026-08-27

Exact exported diagnostics identify `0.1.0 (17)`, candidate `DEV-multi-conversation-state-0.1.0-b17`, source `bc69d58b3245`, iPhone / iOS17.0. User followed the requested core switching/coalescing/hidden-completion/Sync/rapid-switch sequences and reported no major functional issue except scroll-position restoration.

Accepted evidence for the tested sequences:

1. **Resident return**: repeated returns to already-loaded conversations logged `resident.hit` and `resident.firstVisible` without a new same-target Detail request solely because of navigation. Observed `resident.firstVisible.elapsedMs` values are approximately `0.23–0.78 ms`.
2. **Same-target coalescing while loading**: returning to an in-flight conversation logged `detail.coalesced completionCount=2`; the original Detail operation remained the owner rather than starting a duplicate target request.
3. **Hidden completion**: a Detail operation completed while another conversation was foreground and logged `resident.stored visibility=hidden`; later navigation returned through `resident.hit`.
4. **Sync A -> B -> A**: conversation `sha256:8922c7c08d04` started Sync generation 2; after switching away and returning before terminal, the return logged `resident.hit activeOperationKind=sync` and `detail.coalesced completionCount=2`; the same Sync later returned HTTP200 and `latestSync.end status=ok` with 832 visible messages and no duplicate Sync caused by return.
5. **Rapid multi-conversation overlap**: diagnostics reached `activeOperationCount=3`; different conversations completed independently, including hidden resident stores. No HTTP429 event appears in the supplied b17 diagnostic export.
6. **Residency scale observed, not capacity evidence**: resident count reached 6 and `residentTotalApproximateTextBytes` reached `6724764`. This remains approximate text correlation only and is not process-memory/LRU-capacity evidence.

### Reproduced P1 defect — per-conversation scroll anchor

User reproduced the previously planned P1 gap: leave conversation A around ~10% scroll position, switch to B and scroll B, then return to A; A no longer stays at the same semantic/visual position. This is **not a resident-data ownership failure**: b17 still returns A from resident state, but the single visible detail presentation does not yet preserve a per-conversation semantic scroll anchor.

The current diagnostic schema does not record table/collection scroll anchor identity/offset, so the defect is grounded by direct user runtime observation rather than inferred from diagnostics.

### User-confirmed future Send/Stream scroll semantics — anchor vs follow-tail

- Per-conversation scroll presentation must distinguish **historical-reading anchor** from **follow-tail/bottom-following intent**; one raw global `contentOffset` is not the product contract.
- If A is at/near bottom when the user leaves it **and A has an active response**, A is in `follow-tail` semantics. If A continues reasoning/generating hidden and appends content, returning A must show A's current latest bottom, not restore the older pre-answer position.
- If the user intentionally scrolls upward in A while A is generating, that exits `follow-tail`; later return restores the semantic reading anchor rather than forcing bottom.
- B scrolling never mutates A presentation state; A hidden growth never mutates B scroll state.
- This is a user-confirmed product requirement, but automatic hidden-response advancement cannot be Runtime-tested until `DEV-send-stream` establishes the authoritative per-conversation response lifecycle. Do not invent stream protocol/state in b18.

## b18 implementation boundary — semantic historical anchor only

Real source review before coding found the reproduced cause in `ConversationDetailViewController`:

- one shared `UITableView` is reused for every selected conversation;
- `showConversation` / `apply` replace `messages` and call `reloadData()`;
- there is currently no per-conversation scroll presentation state;
- therefore B's table geometry/content offset can affect the next A presentation even though A's resident data is correct.

Smallest supported correction:

1. Keep scroll state in the existing detail presentation owner; do **not** move it into `ConversationRepository` and do not create a second conversation-data store.
2. Track the actually displayed conversation separately from repository selection so A's current anchor can be captured before A's rows are replaced by B.
3. Capture a lightweight semantic anchor from the top visible message identity plus its relative vertical offset.
4. After a conversation's rows are reloaded, find that message in the target's current visible branch, scroll to that row, lay it out, then reapply the relative offset with normal bounds clamping.
5. If the target has no saved anchor, start from its normal top rather than inheriting the previous conversation's raw offset.
6. Clear presentation anchors on account-scope reset.
7. When Sync/Reload refreshes the same visible conversation, preserve the current historical anchor when the anchored message still exists; if the anchored message no longer exists on the new branch, do not invent a cross-message fallback.
8. Add only privacy-safe diagnostics needed to prove save/restore/missing-anchor behavior; never log raw message IDs or bodies.
9. Do **not** add a fake `isStreaming`, timer, response flag, or unused future follow-tail enum. Future `DEV-send-stream` will extend this presentation contract from the real per-conversation response owner.

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

### b17
- **Code written**: Yes.
- **Static/local checks**: Passed.
- **CI passed**: Yes — Run `33045536770`.
- **Artifact produced**: Yes — Artifact `9635486304`, identity independently accepted.
- **Runtime/manual/real-device**: Yes, partial/core accepted for tested iPhone/iOS17 sequences; P1 scroll-anchor defect reproduced.
- **Stable/Frozen**: No.

### b18
- **Candidate identity**: Reserved — `DEV-multi-conversation-state-0.1.0-b18` / `0.1.0 (18)`.
- **Code written**: No yet.
- **Static/local checks**: Pending.
- **CI passed**: Pending.
- **Artifact produced**: Pending.
- **Runtime/manual/real-device**: Pending.
- **Stable/Frozen**: No.

## Remaining acceptance / risks

- b18 must prove ordinary historical anchor A≈10% -> B scroll -> A returns to the same semantic/visual point, including long conversations.
- b18 should also prove B maintains its own independent anchor on A<->B repeated switching and that first-time/new target presentation does not inherit another conversation's raw offset.
- Future follow-tail runtime behavior remains a Send/Stream acceptance gate, not a reason to invent response state in b18.
- Account-context purge/late-callback isolation still needs a real supported runtime account-switch/logout route before claiming that criterion Runtime-tested.
- Normal-operation resident/LRU capacity remains Unknown until device/system memory evidence; approximate text bytes are insufficient.
- Current `userID + accountID` scope remains personal-account evidence only; non-personal workspace isolation is Unknown/Unverified.
- No XCTest/UI-test target exists.

- **Next exact action**: implement the minimal `ConversationDetailViewController` historical semantic-anchor preservation described above, update Xcode/workflow/build identity to b18 in the same intended Candidate product/config commit, run exact Swift parse/static checks, then publish one atomic b18 product/config source and inspect its exact CI/Artifact before real-device A/B anchor validation. Do not rebuild/reuse b17.
