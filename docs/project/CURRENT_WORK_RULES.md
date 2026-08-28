# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Reload current repository governance and codify non-atomic GitHub write-chain batch recovery points.
- **User intent / acceptance criteria**: Current `AGENTS.md` and `docs/project/START_HERE.md` override conflicting historical session rules. Preserve autonomous continuous development to genuine human-only gates, rolling checkpoints, and add an explicit rule for multi-step GitHub mutation chains that cannot be atomic: establish a small batch recovery point before the chain, record completed vs remaining writes/next exact action, verify real GitHub state after each batch, and resume only missing deterministic writes after interruption rather than blindly replaying the chain. Routine progress updates are not approval gates.
- **Baseline**: Started from `main@8d48869ed435040bd19f20b5e3dc2d923ee86df6`. Live predecessor PR #27 remains open/unmerged, so `DEV-send-stream` activation gate remains closed.
- **Evidence / reason**: Latest explicit user requirement plus current repository governance. Repository search found no durable current-main wording for the requested non-atomic GitHub write-chain recovery rule before this task.
- **Files in scope**: `AGENTS.md`, `docs/project/DOCUMENTATION_POLICY.md`, `docs/project/CURRENT_WORK_RULES.md`.
- **Do-not-touch**: `ChatGPTClient/**`, Xcode/workflow Candidate identity, `docs/project/current/dev/**`, PR #27 branch/checkpoint, `DEV-send-stream` development branch/checkpoint/Candidate.
- **Completed**: Re-read latest `AGENTS.md` -> `START_HERE.md`; loaded required current project/router/state/rules documents; verified initial main baseline; verified PR #27 open/unmerged; confirmed existing §16 autonomous-continuation rule. **Batch A complete and verified**: `AGENTS.md` now has §17 `Non-atomic GitHub write chains and batch recovery points`; commit `c13468166394dff0720c6389acfd9490dc1183ff`; blob `4451a4ac54bacd16d10aa06d46f1713ff45c2a62`.
- **Validation state**: Rules-only work in progress. Batch A durable rule verified from real GitHub content. No product Code / CI / Artifact / Runtime claim.
- **Batch recovery point**: Batch A is confirmed complete; do not replay it. Batch B = align `DOCUMENTATION_POLICY.md` session-limit/checkpoint guidance with §17. Batch C = re-read `AGENTS.md` + `DOCUMENTATION_POLICY.md` + real main head, then reset only this Rules checkpoint to Idle. If interrupted now, inspect actual GitHub content/head and resume at Batch B unless it is already present.
- **Pending**: Batch B, final verification, checkpoint reset.
- **Next exact action**: Update `DOCUMENTATION_POLICY.md` with concise batch-recovery guidance for non-atomic GitHub write chains, preserving checkpoint isolation and stronger identity rules.
- **Rejected / do-not-repeat**: Do not replay Batch A; do not treat checkpoint commits as transactional rollback; do not claim partial Candidate identity is safe merely because a recovery point exists; do not add blind retries/polling/watchdogs; do not activate Send/Stream from this Rules message.
- **Open questions / risks**: GitHub Contents API writes are sequential and can be interrupted between files. Recovery must reconcile actual repository state before continuing. PR #27 may continue moving independently and remains outside this rules write chain.

## Active task template

When a multi-step rules task starts, switch to `Active` early and maintain:

- **Task**
- **User intent / acceptance criteria**
- **Baseline**: rule files / branch / PR / commit
- **Evidence / reason**
- **Files in scope**
- **Do-not-touch**
- **Completed**
- **Validation state**: Rule drafted / documented / PR opened / merged
- **Pending**
- **Next exact action**
- **Rejected / do-not-repeat**
- **Open questions / risks**

## Proactive checkpoint rule

The conversation/context limit is unpredictable. Once the rules problem and usable direction are clear, establish an Active checkpoint. Refresh at meaningful rule decisions, permanent-rule edits, PR state changes, or direction changes.

## Completion

When complete, move durable rules to permanent files, reset only this file to `Idle`, and do not modify/delete/reset any Active development checkpoint merely to finish rules work.
