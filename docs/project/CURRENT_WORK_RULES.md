# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Add an autonomous development continuation / human test gate rule to repository governance.
- **User intent / acceptance criteria**: Once a concrete development task is selected and safe to continue, routine intermediate milestones such as code completion, checks, commit/push, PR/CI progress, fixable CI failures, packaging preparation, or checkpoint updates must not become artificial “reply continue” gates. For tasks whose next evidence gate is real-device testing, the agent should autonomously advance as far as the current execution allows toward a uniquely identified, verified testable IPA, then stop for the user's runtime feedback. Stop earlier only for a real human-only decision/information requirement, a governance/identity conflict, or a genuine external blocker. Status updates remain non-blocking. Tool-timeout/email-alert behavior is explicitly out of scope for this rule.
- **Baseline**: `AGENTS.md` on `main@55216bde139f1058517ad852d98669f1c5cb54f1`; rules checkpoint was Idle at task start.
- **Evidence / reason**: User reports repeated low-value manual “继续” replies during normal development and primarily wants to intervene when an IPA is ready for real-device testing and feedback.
- **Files in scope**: `AGENTS.md`, `docs/project/CURRENT_WORK_RULES.md`.
- **Do-not-touch**: Product source, development checkpoints/branches/candidates, GitHub timeout handling, Gmail/email notification behavior.
- **Completed**: Re-read repository governance entry documents and required current project state; routed this request to Rules; confirmed initialized project profile and current `main` baseline.
- **Validation state**: Rule direction confirmed by explicit user requirement; permanent rule edit pending.
- **Pending**: Add the rule to `AGENTS.md`, re-read the resulting file, then reset this Rules checkpoint to Idle.
- **Next exact action**: Append a minimal repository-wide autonomous continuation / human test gate section to `AGENTS.md` without weakening evidence, conflict, candidate-identity, or no-speculative-retry rules.
- **Rejected / do-not-repeat**: Do not add watchdogs, polling, arbitrary retries, or email/GitHub timeout notification rules as part of this change.
- **Open questions / risks**: Platform/tool execution may sometimes return control or terminate outside the agent's control; the rule must not promise background execution after the current execution context can no longer act.

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
