# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Plan multi-conversation residency and independent response ownership.
- **User intent / acceptance criteria**: Switching from conversation A to B must not discard A's loaded state or cancel A's future reasoning/streaming work; returning to A should be instant when its state remains resident, without another detail request merely because the UI selection changed.
- **Baseline**: `main@4b0390a071f0f92b0a5753d5f55092e16ab975c2`; planning branch `rules/multi-conversation-state-plan-20260827`. Active product PR #10 remains separate.
- **Evidence / reason**: Current b9/main and PR #10 repository keep a single `selectedConversation`; selecting another ID clears the prior detail, and a detail response that completes after selection changes is discarded with `selection_changed`. This does not satisfy multi-session development use and would also be unsafe for future parallel streams.
- **Files in scope**: `docs/project/MULTI_CONVERSATION_STATE_PLAN.md`, `docs/project/PROJECT_SPECIFIC_RULES.md`, `docs/project/TECHNICAL_DECISIONS.md`, this checkpoint.
- **Do-not-touch**: Product source; active `DEV-conversation-recovery` checkpoint/branch/PR #10; `DEVELOPMENT_PLAN.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `BUILD_TEST_INDEX.md` while PR #10 owns overlapping planning/status surfaces.
- **Completed**: Repository/current PR identity check; current/PR source inspection; failure mode confirmed.
- **Validation state**: Planning/evidence only; no product code/build/candidate/runtime changes.
- **Pending**: Persist durable multi-conversation ownership/cache/eviction/stream rules, diff-check, merge docs-only planning PR, reset this checkpoint to Idle.
- **Next exact action**: Record `DEV-multi-conversation-state` as a prerequisite before send/stream and define per-conversation cached data plus future per-conversation response lifecycle independent of UI selection.
- **Rejected / do-not-repeat**: Do not create one repository per screen; do not keep all UIKit views alive as the cache; do not cancel a response merely because another conversation becomes selected; do not retain unlimited large conversations without an eviction policy.
- **Open questions / risks**: Exact resident-cache capacity must be chosen from real-device memory evidence; active/streaming sessions must be protected from ordinary LRU eviction.

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
