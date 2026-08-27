# DEV-multi-conversation-state

## Status

**Active — b18 Runtime accepted for tested historical-scroll matrix; b19 measurement-only product source is prepared from the latest docs-only head and is awaiting one fast-forward publication; no LRU behavior has been chosen or implemented; Stable/Frozen = No**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: account-scoped per-conversation resident state, async freshness, lightweight per-conversation presentation, and evidence-backed resident-memory policy.
- **Stable baseline**: `DEV-conversation-recovery-0.1.0-b15`.
- **Branch**: `dev/multi-conversation-state-20260827`.
- **Target main**: `0ea4d7296f574722ec665b40633ecba42fc680e8`; latest main advancement is planning-doc only and non-overlapping with b19 instrumentation.
- **Last Runtime Candidate**: `DEV-multi-conversation-state-0.1.0-b18` / `0.1.0 (18)`.
- **Reserved Candidate**: `DEV-multi-conversation-state-0.1.0-b19` / `0.1.0 (19)` — measurement only.

## b18 accepted Runtime

Exact b18 source `f30c13b4ac2c40dcda829585682825ca906dceae`, Run `33054012226`, Artifact `9638821912`, IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.

Accepted on iPhone/iOS17 for tested scope: resident return, active same-target coalescing, historical A/B independent anchor restoration, first-time target isolation, visible Sync/Reload anchor preservation when anchor remains. Missing-anchor-message discard remains Runtime-unexercised.

## b19 measurement-only scope

The repository's existing `residentApproximateTextBytes` is not actual process-memory evidence and cannot select normal LRU capacity. b19 therefore adds diagnostics-only current-process task VM sampling to existing `conversation / resident.*` events.

Fields:
- `processPhysFootprintBytes`
- `processResidentSizeBytes`
- `processMemoryLimitRemainingBytes` when returned
- `devicePhysicalMemoryBytes`
- sampling status / kernel return on failure

No timer/polling, no retry/fallback/watchdog, no LRU eviction, no resident capacity constant, no Repository/auth/protocol/parser change, no raw conversation/message content in logs.

## b19 exact preparation evidence

- Candidate identity was unique at reservation; no b19 run/artifact existed.
- Diagnostics blob: `5e927b43792535586d8406e1ca5f46cf51c6f041`.
- Xcode blob: `8530571220ba034d49d629031483cccaa6af61a1` (`CURRENT_PROJECT_VERSION=19`, b19 candidate).
- Workflow blob: `da751e26c2cd0da15b15f3e7aac9730e3b7158fc`.
- Build script blob: `5cac0fcb7a7a201afa57dfe2895eca84970ffad4`.
- Local syntax-only parse passed for the new task-VM sampling construct.
- Several earlier off-branch product commits became siblings solely because checkpoint updates advanced the docs-only branch and were deliberately never force-pushed. They are not Candidate sources.
- **Current prepared product commit**: `467444fba2b7b61e68279bafc1485fdd41dda3db`, tree `481e9f26f39f752688667c3c6a8f33110fd5c2bb`, parent `6e31c44dbd6bf1a561a5f29415bfb335a57f22ff`.
- Exact diff from that parent is exactly four files: Diagnostics.swift, Xcode project, workflow, build script. `ConversationFeature.swift` remains unchanged.

## Evidence labels

### b19
- Code written: prepared, publication pending.
- Static/source: source review + syntax parse passed; iPhoneOS compile pending.
- CI: pending.
- Artifact: pending.
- Runtime memory evidence: pending.
- Stable/Frozen: No.

## Remaining Work

1. Publish b19 product source and validate exact CI/Artifact.
2. Collect real iPhone footprint/headroom evidence across several small/large residents and repeated switching.
3. Only then decide whether normal bounded LRU is needed and what capacity is defensible. If source changes are justified, use a new Candidate after b19.
4. Remaining conditional gates: isolated Reload replacement-under-load; natural failed-resident no-implicit-retry; supported account-switch isolation; non-personal workspace remains Unknown/Unverified.

## Next exact action

Fast-forward branch to prepared product commit `467444fba2b7b61e68279bafc1485fdd41dda3db`, then inspect the single intended b19 CI run and Artifact identity. Do not write another pre-publication checkpoint before the ref move.