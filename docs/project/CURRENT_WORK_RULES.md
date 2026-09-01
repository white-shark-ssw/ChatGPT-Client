# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Revert the immediately preceding Send/Composer stacked-parallel planning change and restore strict serial task execution.
- **User intent / acceptance criteria**: Run development tasks one by one. `DEV-composer-parity` must remain future work until `DEV-send-stream` is completed/merged; remove the just-added stacked/dependent overlap allowance without touching the confirmed video-upload/picker requirements.
- **Baseline**: current `main` after the rules-only PR #33 merge and cleanup of the accidental `noop` tool write; active development remains `DEV-send-stream` on PR #29. This Rules task must not modify that branch/checkpoint/product/Candidate.
- **Evidence / reason**: latest explicit user requirement supersedes the immediately prior parallel-development preference.
- **Files in scope**: this Rules checkpoint and `docs/project/COMPOSER_PARITY_PLAN.md` only.
- **Do-not-touch**: PR #29 branch/checkpoint/product code/Candidate/Artifact and all unrelated durable docs.
- **Completed**: governance startup re-read; current main verified; the previous parallel rule is localized to `COMPOSER_PARITY_PLAN.md`; accidental `noop` file was removed from main immediately after creation.
- **Validation state**: Rules/docs only; no product Code/CI/Artifact/Runtime changes.
- **Pending**: remove the stacked/dependent section, restore serial-only wording while preserving the confirmed direct-Photos-video requirement, merge the rules-only change, reset this checkpoint Idle.
- **Next exact action**: update `COMPOSER_PARITY_PLAN.md` to require `DEV-send-stream` completion/merge before activating `DEV-composer-parity`.
- **Rejected / do-not-repeat**: starting Composer from a stacked Send branch while the user wants one task at a time; reverting unrelated video/file-picker requirements.

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
