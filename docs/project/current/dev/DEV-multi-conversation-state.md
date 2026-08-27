# DEV-multi-conversation-state

## Status

**Active — b17 atomic product/config source published; static/local parse passed; CI/Artifact and runtime evidence pending**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 send/stream 所需的多会话 freshness 与异步所有权基线。
- **Baseline**: `0.1.0 (15)` Stable recovery; base `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; recovery PR #10 merged.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; PR `Not created`.
- **Current candidate**: `DEV-multi-conversation-state-0.1.0-b17`, version `0.1.0 (17)`.
- **Exact b17 product/config source**: `bc69d58b3245a1ab21b250e16612c11d39ddbf33`, tree `3451585f83c7bac69368709fe6273b90a0294d29`.
- **Atomicity evidence**: b17 source was assembled as Git blobs/tree/commit off-branch, reviewed, then branch ref advanced exactly once. Compared with parent `76728a4a24e1825df8ee9f356ecdc32b052a035b`, exactly four files changed: `ConversationFeature.swift`, Xcode project, workflow and `scripts/build_ipa.sh`.
- **Local/static evidence**: exact final `ConversationFeature.swift` blob is `1034cff72dea36d6d7e835bdf52dcfe2cdc8e38d`; local Git-blob hash matched exactly; `swiftc -frontend -parse` passed. This is syntax/static evidence only, not iOS compile/runtime proof.

## b16 history

- b16 source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; CI Run `33009246356` succeeded; Artifact `9621830284` was identity-rejected because build script embedded recovery b15 candidate/default IPA slug.
- b16 had no real-device run and must never be reused.

## b17 owner fixes now written

1. **Stale account context cannot re-adopt scope**: request/transport context only validates against the current Auth owner; repository scope changes are driven by a currently verified `AuthSessionStore` snapshot/change signal.
2. **Probe commit freshness**: completed account probe rechecks `verifiedAccountContext()` on the main owner before installing its transient session/scope.
3. **Waiter terminal contract**: replaced same-target operations cancel the old task and deterministically complete old waiters with `operationSuperseded`; account reset completes cancelled operation waiters with `accountContextChanged`.
4. **Replacement ordering**: new operation owner is installed; old task is cancelled; replacement task is created and its handle synchronously attached on the main owner; only then are old waiters notified. This preserves b15 cancel-before-replace while avoiding completion re-entry before the new task handle exists.
5. **Operation-first resident lookup**: an existing per-conversation operation is joined before a loaded/failed resident is returned, allowing return-to-A to observe an in-flight Sync/Reload instead of silently rendering only stale resident data.
6. **Target-specific recovery**: Sync/Reload capture an explicit conversation ID; they do not derive mutation target from foreground selection after invocation.
7. **Recovery presentation derives from selected conversation operation**: no global recovery-in-progress authority. Returning to A during active Sync/Reload restores A's appropriate presentation and coalesces onto its existing operation; B/C remain independent.
8. **Ordinary presentation freshness**: detail controller uses a presentation generation plus selected ID guard so lifecycle completions for an obsolete selection cycle cannot overwrite the current conversation.
9. **List freshness**: repository list generation rejects obsolete same-scope/account-reset results; sidebar has a presentation generation so late old-list completion cannot end a newer presentation state.
10. **Repository execution domain**: mutable repository state is main-thread confined with explicit preconditions; URLSession callbacks use immutable captured diagnostics fields and commit results through main.
11. **Memory warning protection**: resident entries belonging to selected or active detail/recovery operations are protected; only eligible inactive terminal residents are trimmed.
12. **Diagnostics**: one owner logs old->new hashed selection transition; resident diagnostics expose resident/active/protected counts; immediate resident render logs `resident.firstVisible` timing. Approximate text bytes remain correlation only, not process-memory evidence.
13. **Package identity**: Xcode build/candidate advanced to b17; workflow Artifact name is b17; build-script default candidate is b17 and IPA slug is `dev-multi-conversation-state`.

## Evidence labels

- **Code written**: **Yes — b17 exact source published**.
- **Static/local checks**: **Swift parse passed + exact blob identity matched**.
- **CI passed**: **Pending for b17**. b16 CI does not prove b17.
- **Artifact produced**: **Pending for b17**.
- **Runtime/manual/real-device**: **No for this Work**.
- **Stable/Frozen**: **No**.

## Remaining acceptance / risks

- CI must compile/package exact b17 and Artifact inspection must prove filename, candidate, source commit, version/build, SHA, arm64/iOS14 identity before device testing.
- Real-device core matrix: A loaded -> B loaded -> A with no new Detail request; hidden A completion; A->B->A coalescing while loading; Sync A->B->A before terminal; target-only Sync/Reload; failed A return without implicit network retry; rapid A/B/C overlap and HTTP429 observation.
- Account-context purge/late-callback isolation still needs a real supported runtime account-switch/logout route before claiming runtime acceptance.
- Normal-operation resident/LRU capacity remains Unknown until device/system memory evidence; approximate text bytes are insufficient.
- Current `userID + accountID` scope remains personal-account evidence only; non-personal workspace isolation is Unknown/Unverified.
- Semantic scroll-anchor restoration remains P1 and does not block this core Candidate.

- **Next exact action**: verify the GitHub Actions run triggered by exact b17 source `bc69d58b...`; if CI succeeds, inspect the exact Artifact identity/checksums before offering it for real-device testing. If b17 CI/source fails, record b17 as failed and allocate a new candidate rather than silently reusing b17.
