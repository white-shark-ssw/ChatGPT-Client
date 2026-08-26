# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Record background execution / local-notification strategy and TrollStore true-background research references.
- **User intent / acceptance criteria**: Prefer local completion notification; keep a response alive in background as long as practical; investigate TrollStore-only true-background techniques before accepting ordinary iOS background limits; do not invent a fake 30m/1h guarantee.
- **Baseline**: `main@a43762d255e699a753011103b7e1a6bb5416cb30`; rules branch `rules/background-execution-plan-20260826`.
- **Evidence / reason**: Public `巨魔真后台` distribution identifies developer `bswbw` and TrollStore/iOS 14–17 scope, but no public GitHub source was found. Open-source TrollSpeed/UIDaemon-derived projects provide current reference evidence for root-persona, private-entitlement, non-freezable/jetsam-managed long-running TrollStore processes. Apple public background APIs remain limited/system-scheduled.
- **Files in scope**: `docs/project/BACKGROUND_EXECUTION_PLAN.md`, `docs/project/PROJECT_SPECIFIC_RULES.md`, `docs/project/TECHNICAL_DECISIONS.md`, this checkpoint.
- **Do-not-touch**: Product source; active `DEV-conversation-recovery` checkpoint/branch/PR #10; `DEVELOPMENT_PLAN.md` and `PROJECT_STATE.md` while PR #10 is active because it already modifies them.
- **Completed**: Repository baseline/conflict scan; exact app public-source search; TrollSpeed source/entitlement/jetsam reference inspection; Apple background-strategy check.
- **Validation state**: Planning/evidence only; no product code/build/candidate/runtime changes.
- **Pending**: Write durable background plan and decision/rules; compare docs-only diff; open/merge rules PR if non-overlapping; reset rules checkpoint to Idle.
- **Next exact action**: Persist the two-stage plan: standard background-task + local notification baseline, then isolated TrollStore true-background experiment only after send/stream is stable.
- **Rejected / do-not-repeat**: Do not claim `巨魔真后台` implementation details without source; do not promise 30m/1h via public iOS APIs; do not copy private entitlements/root helper into production before a dedicated real-device experiment.
- **Open questions / risks**: Whether the main ChatGPT client process can safely remain non-freezable while preserving network streaming, or requires a helper/assertion architecture, remains Unverified until implementation/testing.

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

When complete, move durable rules to permanent rule files, reset only this file to `Idle`, and do not modify/delete/reset any Active development checkpoint merely to finish rules work.
