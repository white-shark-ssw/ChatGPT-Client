# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Record the official ChatGPT iOS composer interaction baseline from the user-supplied 55.1s / 30fps recording and place the resulting 1:1 composer-parity work into the post-Send roadmap without interfering with active `DEV-send-stream` PR #29.
- **User intent / acceptance criteria**: Preserve the official composer interaction as the product baseline: collapsed/focused/multiline/maximized editor states, file/photo selection and local previews, attachment tap preview, plus-menu behavior, and the previously required reasoning-effort controls for ordinary Chat and Work mode. Determine the correct development boundary and keep exact option labels/protocol mappings evidence-driven where the current recording does not show them.
- **Baseline**: `main@1ac202c972f2dee6945fe8d0688df8e10f5d462c`; rules branch `rules/composer-parity-plan-20260831`. Active development remains `DEV-send-stream` on `dev/send-stream-20260829`, PR #29; latest checkpoint records exact b65 Artifact pending Runtime.
- **Evidence / reason**: User supplied `RPReplay_Final1788118003.mp4`; media metadata is 510×1108, 30fps, 55.1s, 1653 frames. Full-frame difference scan plus dense review around every major transition establishes official composer state changes and attachment-preview interactions. PR #29 currently changes `START_HERE.md`, `DEVELOPMENT_PLAN.md`, attachment plan and other shared dev docs, so this Rules task must not edit those overlapping files.
- **Files in scope**: this rules checkpoint and a new non-overlapping durable `docs/project/COMPOSER_PARITY_PLAN.md`.
- **Do-not-touch**: PR #29 branch/checkpoint/product source/Candidate/Artifact; `DEVELOPMENT_PLAN.md`, `START_HERE.md`, `ATTACHMENT_TRANSFER_PLAN.md`, `PROJECT_STATE.md`, `PROJECT_SPECIFIC_RULES.md`, or other files currently changed by PR #29.
- **Completed**: governance startup read; current main and active Send/Stream identity checked; PR #29 overlap scanned; recording metadata and major frame transitions reviewed; initial placement decision is a dedicated `DEV-composer-parity` stage after accepted Send/Stream and before native attachment-transfer implementation.
- **Validation state**: Rules/planning only; no product Code/CI/Artifact/Runtime changes.
- **Pending**: write the durable composer-parity plan, verify branch diff stays non-overlapping with PR #29, open/merge rules PR if clean, then reset this checkpoint to Idle.
- **Next exact action**: create `docs/project/COMPOSER_PARITY_PLAN.md` with the observed state machine, 1:1 interaction contract, reasoning-effort evidence boundary, ownership, acceptance matrix and development ordering.
- **Rejected / do-not-repeat**: broadening active b65 Send/Stream Runtime gate with unrelated composer polish; hard-coding unverified reasoning-effort labels/levels; implementing file/image upload protocol from UI recording alone; duplicating per-conversation draft/response authorities.
- **Open questions / risks**: exact current ordinary-Chat and Work-mode reasoning-effort option labels/request mapping are not visible in this recording and remain current-service evidence items; active PR #29 must later reconcile its roadmap wording after merge/closure.

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
