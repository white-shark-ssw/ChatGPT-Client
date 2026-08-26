# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Whole-client architecture gap review after multi-conversation/background planning.
- **User intent / acceptance criteria**: Re-check the current native-client plan for missing state/lifecycle/reliability details before send/stream work; keep the path to first usable client fast; do not mix this rules review into the active recovery product task.
- **Baseline**: `main@e42bfecdb5d4526b6963d96ae5eafd675922b21b`; rules branch `rules/client-gap-review-20260827`; active product PR #10 remains separate.
- **Evidence / reason**: Current source still uses a single loaded conversation slot; current detail parsing discards `current_node` after deriving visible messages; b9 cold launch repeatedly showed 0/0 WebKit cookies; list transport currently requests only 28 items; Settings has no preference owner yet; no test target exists. New multi-conversation/background plans expose additional concurrency, account-scope and notification-lifecycle requirements.
- **Files in scope**: New architecture gap-review document plus non-overlapping durable planning/rule docs such as `MULTI_CONVERSATION_STATE_PLAN.md`, `BACKGROUND_EXECUTION_PLAN.md`, `PROJECT_SPECIFIC_RULES.md`, `TECHNICAL_DECISIONS.md`, this checkpoint.
- **Do-not-touch**: Product source; active `DEV-conversation-recovery` branch/checkpoint/PR #10; `DEVELOPMENT_PLAN.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `BUILD_TEST_INDEX.md`, Xcode/build/CI files while PR #10 owns those surfaces.
- **Completed**: Fresh governance read; current source/profile/state/UI/background/multi-conversation review; PR #10 conflict scan; initial gap classification.
- **Validation state**: Planning/evidence only; no product code/build/candidate/runtime changes.
- **Pending**: Persist prioritized gap review and clarified invariants; compare docs-only diff; merge non-overlapping planning PR; reset rules checkpoint to Idle.
- **Next exact action**: Record P0 pre-send invariants (account-scoped per-conversation state, async freshness, node identity retention, cold-start auth resume, send identity/concurrency), then P1/P2 daily-use gaps without blocking early candidates.
- **Rejected / do-not-repeat**: Do not solve every future feature now; do not add automatic retry/watchdog/offline persistence speculatively; do not create disk chat-body cache without explicit privacy/storage need; do not let old async callbacks regress newer state.
- **Open questions / risks**: Exact multi-stream server concurrency, conversation `聊天/工作` type field, concrete resident-cache bound, and cold-start WebKit warm-up mechanism remain Unverified until dedicated implementation/runtime evidence.

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
