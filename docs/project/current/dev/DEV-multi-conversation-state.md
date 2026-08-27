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
- Never reuse b16.

### b17 — identity-valid / core runtime accepted

- Exact product/config source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; tree `3451585f83c7bac69368709fe6273b90a0294d29`.
- CI Run `33045536770`, job `98428537619`, success; Artifact `9635486304` identity accepted.
- iPhone/iOS17 runtime accepted core resident/coalescing/hidden-Sync/overlap paths; user reproduced historical-scroll defect.

### b18 — historical semantic scroll correction / runtime accepted for tested matrix

- Exact product/config source `f30c13b4ac2c40dcda829585682825ca906dceae`; tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- Run `33054012226`, Job `98456174184`: success; Artifact `9638821912`; IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.
- Exact iPhone/iOS17 runtime accepted historical A/B anchor restoration, independent anchors, first-time target isolation, visible Sync/Reload preservation when anchor remains, resident return and active same-target Sync coalescing.

## b19 — real process-memory measurement Candidate

### Scope / ownership boundary

- **Measurement only. No LRU eviction policy is implemented in b19.**
- No resident capacity number is selected in source.
- No automatic retry, timer, watchdog, fallback, memory-pressure polling loop or global concurrency limiter.
- `ConversationRepository`, `AuthSessionStore`, protocol routes/headers and parsing are unchanged.
- Memory samples stay in the existing bounded diagnostics store/export.
- No raw conversation/message identity or body is added to diagnostics.

### Instrumentation

`DiagnosticsLogger` enriches only `conversation / resident.*` events with current-process task VM memory fields so they line up with existing resident/active/protected counts:

- `processPhysFootprintBytes`;
- `processResidentSizeBytes`;
- `processMemoryLimitRemainingBytes` when returned by the kernel;
- `devicePhysicalMemoryBytes`;
- sampling status / kern return on failure.

No new sampling timer exists. Existing `resident.miss`, `resident.stored`, `resident.hit`, `resident.firstVisible`, `resident.evicted`, and `resident.evictionSkipped` provide natural sample points.

### Candidate identity / publication record

- Candidate: `DEV-multi-conversation-state-0.1.0-b19`.
- Version/build: `0.1.0 (19)`.
- b19 repository search before reservation: no existing identity; branch Actions contained b16/b17/b18 only.
- Docs reservation: `1785bd43b2ae76f40121e0faa7fac009a1703681` and `593490ddeb82cd173ccde5cfe90d79002545f3d7`.
- Two intermediate off-branch commits (`54a5850b...`, `ea523254...`) became sibling commits after docs-only checkpoint advancement and were deliberately **not force-pushed**; they are not Candidate product sources.
- **Exact final product commit prepared from latest docs-only parent `b6f16ec9e1467578d2d67100fbb3354b2660ef26`: `0afb9c1072de521784cd5b2ca97d239a41338991`; tree `393879742f55203730d86c84165ae4f94cbf1e06`.**
- Exact final diff is 4 files only: `ChatGPTClient/Diagnostics/Diagnostics.swift`, `ChatGPTClient.xcodeproj/project.pbxproj`, `.github/workflows/ios-foundation.yml`, `scripts/build_ipa.sh`.
- Product blobs: Diagnostics `5e927b43792535586d8406e1ca5f46cf51c6f041`; Xcode `8530571220ba034d49d629031483cccaa6af61a1`; workflow `da751e26c2cd0da15b15f3e7aac9730e3b7158fc`; build script `5cac0fcb7a7a201afa57dfe2895eca84970ffad4`.
- `ConversationFeature.swift` / Repository remain unchanged from b18.
- Local syntax-only `swiftc -frontend -parse` passed for the exact new task-VM sampling construct; exact macOS/iPhoneOS compile remains CI-pending.
- `main@0ea4d729...` differs from prior target only in merged planning docs; open PR list is empty; no product/config overlap exists.

## Evidence labels

### b18
- **Code written**: Yes.
- **Static/source checks**: Passed.
- **CI passed**: Yes.
- **Artifact produced**: Yes.
- **Runtime/manual/real-device**: Passed for tested historical-scroll / Sync / Reload-preservation / resident-regression matrix.
- **Stable/Frozen**: No.

### b19
- **Code written**: Exact product commit prepared; publication/CI pending at this checkpoint revision.
- **Static/source checks**: Source review + syntax parse passed; iPhoneOS compile pending.
- **CI passed**: Pending.
- **Artifact produced**: Pending.
- **Runtime/manual/real-device memory evidence**: Pending.
- **Stable/Frozen**: No.

## Remaining Work before Stable

- Collect exact b19 process-memory evidence while several small and large conversations become resident and are repeatedly switched.
- Decide from measured footprint/headroom trend whether a normal bounded LRU is required now. If evidence does not justify code, do not manufacture it.
- If LRU is justified, allocate a new unique Candidate after b19; never rebuild/reuse b19.
- Isolated target-only Reload replacement while older same-target Detail is in flight remains open.
- Natural failed-resident navigation remains open until a natural terminal failure occurs.
- Supported account-switch/logout purge and late-callback rejection remain open until a real supported route exists.
- Non-personal workspace isolation remains Unknown / Unverified.

## Next exact action

Publish exact final b19 product commit `0afb9c1072de521784cd5b2ca97d239a41338991` by fast-forward branch ref, inspect the one intended b19 CI run and Artifact identity, then install exact b19 on iPhone/iOS17 and run the resident-memory matrix before any LRU decision.

Before final Work merge, synchronize with `main@0ea4d7296f574722ec665b40633ecba42fc680e8` and preserve merged planning.