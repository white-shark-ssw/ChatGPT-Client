# DEV-multi-conversation-state

## Status

**Active — exact b18 historical scroll restoration is real-device accepted for the tested iPhone/iOS17 matrix; b19 is reserved as a measurement-only Candidate to collect real process-memory evidence; no LRU behavior has been chosen or implemented; Stable/Frozen = No**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 Send/Stream 所需的多会话 freshness、异步所有权与轻量 per-conversation presentation 基线。
- **Stable product baseline**: `DEV-conversation-recovery-0.1.0-b15`, version `0.1.0 (15)`.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; product PR `Not created`.
- **Current target branch**: `main@0ea4d7296f574722ec665b40633ecba42fc680e8`.
- **Parallel conflict note**: PR #17 has merged into `main`. The merge changed only `docs/project/DEVELOPMENT_PLAN.md` and `docs/project/UI_INTERACTION_BASELINE.md`; it does not overlap b19 runtime instrumentation files. Preserve these planning changes during final synchronization.
- **Last runtime-tested Candidate**: `DEV-multi-conversation-state-0.1.0-b18`, version `0.1.0 (18)`.
- **Reserved next Candidate**: `DEV-multi-conversation-state-0.1.0-b19`, version `0.1.0 (19)` — **memory measurement only**.

## Candidate history

### b16 — historical / rejected before runtime

- Exact source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; CI Run `33009246356` succeeded.
- Artifact `9621830284` embedded wrong recovery candidate/slug and is permanently rejected/superseded before runtime.
- Source review also found stale-scope, waiter, hidden-Sync, list-freshness, task-handle and owner-domain gaps.
- Never reuse b16.

### b17 — identity-valid / core runtime accepted

- Exact product/config source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; tree `3451585f83c7bac69368709fe6273b90a0294d29`.
- CI Run `33045536770`, job `98428537619`, success; Artifact `9635486304` identity accepted.
- iPhone/iOS17 runtime accepted resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid different-conversation overlap up to three active operations with no HTTP429 in that export.
- User reproduced historical-scroll defect: A near ~10% -> B scroll -> A returned shifted.

### b18 — historical semantic scroll correction / runtime accepted for tested matrix

- Exact product/config source `f30c13b4ac2c40dcda829585682825ca906dceae`; tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- Run `33054012226`, Job `98456174184`: success; Artifact `9638821912`; IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.
- Exact device export identifies iPhone/iOS17, b18/build18/source `f30c13b4ac2c`.
- User executed the requested matrix and reported no issue.
- Runtime accepted for tested scope: historical A->B->A anchor restoration, independent A/B anchors, first-time target isolation, visible Sync/Reload anchor preservation when message remains, resident return and active same-target Sync coalescing.
- Missing-anchor-message discard did not occur naturally and remains Runtime-unverified.

## b19 — real process-memory measurement Candidate

### Why b19 exists

The current repository only logs `residentApproximateTextBytes`. That is a text-size correlation metric and cannot establish actual process memory or a safe resident capacity. The Work explicitly prohibits choosing normal LRU capacity from that metric.

b19 samples current-process task VM information only for diagnostics correlation so real resident-count transitions can be compared against actual process footprint and task memory headroom.

### Scope / ownership boundary

- **Measurement only. No LRU eviction policy is implemented in b19.**
- No resident capacity number is selected in source.
- No automatic retry, timer, watchdog, fallback, memory-pressure polling loop or global concurrency limiter.
- `ConversationRepository` data/operation ownership remains unchanged.
- `AuthSessionStore`, protocol routes/headers and conversation parsing remain unchanged.
- Do not persist memory samples outside the existing bounded diagnostics store/export.
- No raw conversation/message identity or content is added to diagnostics.

### Instrumentation design

The existing `DiagnosticsLogger` enriches only `conversation / resident.*` events. This naturally aligns memory samples with existing resident count / active operation / protected resident fields without adding a new timer or lifecycle owner.

Fields:

- `processPhysFootprintBytes` — current app `task_vm_info_data_t.phys_footprint`;
- `processResidentSizeBytes` — current task `resident_size` correlation;
- `processMemoryLimitRemainingBytes` — task VM `limit_bytes_remaining` when returned by the current kernel;
- `devicePhysicalMemoryBytes` — `ProcessInfo.processInfo.physicalMemory`;
- `processMemorySampleStatus` / `processMemorySampleKernReturn` make sampling failure observable without affecting product behavior.

Useful existing sample points include `resident.miss`, `resident.stored`, `resident.hit`, `resident.firstVisible`, `resident.evicted`, and `resident.evictionSkipped`.

### Candidate identity / publication gate

- Candidate: `DEV-multi-conversation-state-0.1.0-b19`.
- Version/build: `0.1.0 (19)`.
- b19 repository search before reservation: no existing identity.
- Branch Actions before reservation: b16/b17/b18 only; no b19 run/artifact.
- Docs reservation commits: checkpoint `1785bd43b2ae76f40121e0faa7fac009a1703681`; Build Index `593490ddeb82cd173ccde5cfe90d79002545f3d7`.
- Exact off-branch product commit prepared from parent `593490ddeb82cd173ccde5cfe90d79002545f3d7`: `54a5850b8fc22f18a044c7c80bbff8a5be2cc52e`; tree `fec22bb6eed3e2d64e82ced747116f6ad8bdeaa4`.
- Exact product diff is 4 files only: `ChatGPTClient/Diagnostics/Diagnostics.swift`, Xcode project, workflow, build script. `ConversationFeature.swift` / Repository are unchanged.
- Local syntax-only `swiftc -frontend -parse` passed for the exact new task-VM sampling construct. macOS/iPhoneOS SDK/type availability still requires exact CI compile proof.
- Publication recheck: branch remained `593490d...`; `main` advanced to `0ea4d729...` only through merged PR #17 docs (`DEVELOPMENT_PLAN.md`, `UI_INTERACTION_BASELINE.md`); open PR list is now empty. No product/config overlap exists.

## User-confirmed future Send/Stream scroll semantics

- Per-conversation presentation distinguishes historical-reading anchor from future follow-tail intent.
- If A is at/near bottom and has an authoritative active response, hidden growth/completion must make return-to-A land at A's current latest bottom.
- Intentional upward scrolling while A generates exits follow-tail and later restores historical reading position.
- b19 does not implement response lifecycle/follow-tail.

## Evidence labels

### b18
- **Code written**: Yes.
- **Static/source checks**: Passed.
- **CI passed**: Yes.
- **Artifact produced**: Yes.
- **Runtime/manual/real-device**: Passed for tested historical-scroll / Sync / Reload-preservation / resident-regression matrix.
- **Stable/Frozen**: No.

### b19
- **Code written**: Prepared off-branch; not yet published at this checkpoint revision.
- **Static/source checks**: Syntax/source review passed; exact iPhoneOS compile pending.
- **CI passed**: Pending.
- **Artifact produced**: Pending.
- **Runtime/manual/real-device memory evidence**: Pending.
- **Stable/Frozen**: No.

## Remaining Work before Stable

- Collect exact b19 process-memory evidence while several small and large conversations become resident and are repeatedly switched.
- Decide from measured footprint / remaining-limit trend whether a normal bounded LRU is required now. If evidence does not justify a source change, do not manufacture one.
- If an LRU is justified, allocate a new unique Candidate after b19; never rebuild/reuse b19 for corrected behavior.
- Isolated target-only Reload replacement while older same-target Detail is actually in flight remains open as a regression spot-check.
- Terminal failed resident A -> B -> A with no implicit retry remains open until a natural terminal failure is available.
- Supported account-switch/logout purge and late-callback rejection remain runtime-open until a real supported route exists.
- Non-personal workspace isolation remains Unknown / Unverified.

## Next exact action

Publish exact off-branch b19 commit `54a5850b8fc22f18a044c7c80bbff8a5be2cc52e` with one branch ref move, then inspect the one intended b19 CI run and Artifact identity. After exact Artifact exists, install it on iPhone/iOS17 and exercise the resident-memory matrix before making any LRU decision.

Before final Work merge, synchronize with current `main@0ea4d7296f574722ec665b40633ecba42fc680e8` and preserve its merged message-timestamp / adaptive-answer-navigation planning.