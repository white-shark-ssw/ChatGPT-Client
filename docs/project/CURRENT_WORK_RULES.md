# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Correct cold-start auth-resume ownership and finalize the post-recovery development sequence.
- **User intent / acceptance criteria**: Cold-start login-state recovery is not a separate future Work; it is already assigned to the active `DEV-conversation-recovery` task, using background/invisible WebKit-store verification first and only moving to visible foreground verification if that fails. Plan the remaining client work for fastest usable delivery without reintroducing duplicate state owners or blocking send/stream on nonessential breadth.
- **Baseline**: `main@522be766538742139c4f7906dc08303556d55949`; planning branch `rules/post-recovery-roadmap-20260827`; active product PR #10 remains separate/unmerged.
- **Evidence / reason**: User's latest explicit requirement supersedes the current planning text that still lists `DEV-auth-resume` separately. PR #10/checkpoint are owned by another development session and must not be edited from this Rules session.
- **Files in scope**: `docs/project/CLIENT_ARCHITECTURE_GAP_REVIEW.md`, `docs/project/MULTI_CONVERSATION_STATE_PLAN.md`, optional non-overlapping durable planning/entry docs, this rules checkpoint.
- **Do-not-touch**: PR #10 product source, its development checkpoint, candidate/build/CI files, and its owned `DEVELOPMENT_PLAN.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `BUILD_TEST_INDEX.md` until that task completes/merges.
- **Completed**: Fresh governance read; current main/project docs read; PR #10/checkpoint verified; conflict with stale separate-auth-resume planning identified.
- **Validation state**: Planning/docs only; no product code/build/candidate/runtime changes.
- **Pending**: Remove separate auth-resume scheduling from non-overlapping durable plans; record exact post-recovery sequence and per-task gates; diff-check and merge docs-only PR; reset this checkpoint to Idle.
- **Next exact action**: Update the architecture gap review and multi-conversation plan so recovery includes cold-start auth verification, then order multi-conversation state, round-count/preferences, send/stream, rendering/pagination, background notification/true-background, export/performance/attachments.
- **Rejected / do-not-repeat**: Do not create a second `DEV-auth-resume` Work; do not edit another session's recovery checkpoint; do not let Markdown/rendering/pagination/background experiments block the first working send/stream candidate.
- **Open questions / risks**: PR #10 must later synchronize its own durable roadmap/status docs with this latest user requirement before merge; send protocol details and simultaneous multi-conversation server-stream behavior remain Unverified until dedicated runtime evidence.

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
