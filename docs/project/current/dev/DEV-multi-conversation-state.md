# DEV-multi-conversation-state

## Status

**Active — exact b18 historical scroll restoration is real-device accepted for the tested iPhone/iOS17 matrix; b19 is reserved as a measurement-only Candidate to collect real process-memory evidence; no LRU behavior has been chosen or implemented; Stable/Frozen = No**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 Send/Stream 所需的多会话 freshness、异步所有权与轻量 per-conversation presentation 基线。
- **Stable product baseline**: `DEV-conversation-recovery-0.1.0-b15`, version `0.1.0 (15)`.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; product PR `Not created`.
- **Current target branch**: `main@2c33dacbefa613292eb89cbf606b0172a241e81e`.
- **Parallel conflict note**: open PR #17 (`rules/turn-jump-plan-20260827`) is planning-only and targets `DEVELOPMENT_PLAN.md` / `UI_INTERACTION_BASELINE.md`; it does not overlap b19 runtime instrumentation files. Preserve it during final synchronization.
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

Apple's documented memory model provides actual process footprint through `task_info` / `task_vm_info_data_t.phys_footprint`, and the same task VM information exposes current memory-limit remaining bytes. b19 will use those current-process values only for diagnostics correlation.

### Scope / ownership boundary

- **Measurement only. No LRU eviction policy is implemented in b19.**
- No resident capacity number is selected in source.
- No automatic retry, timer, watchdog, fallback, memory-pressure polling loop or global concurrency limiter.
- `ConversationRepository` data/operation ownership remains unchanged.
- `AuthSessionStore`, protocol routes/headers and conversation parsing remain unchanged.
- Do not persist memory samples outside the existing bounded diagnostics store/export.
- No raw conversation/message identity or content is added to diagnostics.

### Planned instrumentation

Use the existing `DiagnosticsLogger` path and enrich only conversation `resident.*` events with current-process memory fields so samples naturally line up with resident-count transitions and visible resident returns:

- `processPhysFootprintBytes` — current app physical footprint from `task_vm_info_data_t.phys_footprint`;
- `processResidentSizeBytes` — task resident size for correlation;
- `processMemoryLimitRemainingBytes` — current task memory-limit remainder from task VM info;
- `devicePhysicalMemoryBytes` — device physical-memory total from `ProcessInfo.processInfo.physicalMemory`.

Expected useful sample points already present in product flow include `resident.miss`, `resident.stored`, `resident.hit`, `resident.firstVisible`, `resident.evicted`, and `resident.evictionSkipped`. No new timer/cadence is introduced.

### Candidate identity / uniqueness gate

- Candidate: `DEV-multi-conversation-state-0.1.0-b19`.
- Version/build: `0.1.0 (19)`.
- Branch: `dev/multi-conversation-state-20260827`.
- b19 search in repository: no existing identity found before reservation.
- Branch Actions before reservation: exactly three historical product runs for b16/b17/b18; no b19 run/artifact exists.
- Current branch at gate: `ca2a18224d4fa10d724380144a21532f3c574da6`.
- Current main at gate: `2c33dacbefa613292eb89cbf606b0172a241e81e`.
- Open PR #17 is planning-only and non-overlapping with b19 product instrumentation.

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
- **Code written**: Pending publication.
- **Static/source checks**: Pending.
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

Implement the smallest b19 diagnostics-only process-memory snapshot in `Diagnostics.swift`, update exact b19 version/build/workflow/package identity atomically, run static/source checks, then publish one exact b19 product source and validate CI/Artifact identity. After Artifact exists, install exact b19 on the target iPhone/iOS17 and exercise a resident-memory matrix before making any LRU decision.

Before final Work merge, synchronize with current `main@2c33dacbefa613292eb89cbf606b0172a241e81e` and preserve parallel planning changes including PR #17 if merged.