# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Remove ChatGPT-Notify / Bark completion-notification integration and correct the near-term development handoff.
- **User intent / acceptance criteria**: Stop using the GitHub-comment/Bark notification workflow because tool invocation and transient-comment redaction proved unreliable; remove it from the repository startup/Agent rules. Confirm the next real development task from current merged project state.
- **Baseline**: `main@65405c67605ddef77b032d4c6993218882dde759`; rules branch `rules/remove-chatgpt-notify-20260828`; no open PR and no Active development checkpoint at preflight.
- **Evidence / reason**: User explicitly rejected the notification-repository workflow after repeated testing. Current `PROJECT_STATE.md` proves `DEV-conversation-list-cache-core-0.1.0-b23` is merged Stable and names `DEV-conversation-round-count` as the next serialized priority, while `DEVELOPMENT_PLAN.md` still contains stale pre-completion Phase 7 wording.
- **Files in scope**: `AGENTS.md`, `docs/project/START_HERE.md`, `docs/automation/CHATGPT_NOTIFY_RULES.md`, `docs/project/DEVELOPMENT_PLAN.md`, this rules checkpoint.
- **Do-not-touch**: product source, build/version/candidate/CI/artifact files, development checkpoints, accepted cache/multi-conversation evidence.
- **Completed**: repository/startup truth inspected; no Active development Work or open PR found; notification removal direction established.
- **Validation state**: Rules cleanup in progress; no product Code/CI/Artifact/Runtime changes.
- **Pending**: remove notification startup rules/file, correct Development Plan Phase 7/current next action, diff-check, PR/merge, verify merged files, reset this checkpoint to Idle.
- **Next exact action**: Restore pre-notification `AGENTS.md` and `START_HERE.md`, delete `docs/automation/CHATGPT_NOTIFY_RULES.md`, then update stale development-plan handoff to `DEV-conversation-round-count`.
- **Rejected / do-not-repeat**: GitHub-comment/Bark completion notification as mandatory per-reply Agent behavior; pretending best-effort notification is reliable; leaving stale Phase 7 as future work after b23 merged Stable.
- **Open questions / risks**: None for rules removal. Future product notification/deep-link capability remains separate and is not implemented or removed by this governance cleanup.

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
