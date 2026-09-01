# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Evaluate and record whether `DEV-send-stream` and `DEV-composer-parity` may be developed concurrently.
- **Baseline**: `main@d323b9eed2dda75b9986fc06e14014d3e9b365fb`; active `DEV-send-stream` branch `dev/send-stream-20260829`, PR #29; PR head `340318d471087e455df3eb26fd10111eeb2a4c12`; b80 allocated and product assembly in progress.
- **Evidence / reason**: active Send/Stream b80 explicitly owns `ConversationFeature.swift`, `RootViewController.swift`, Xcode identity and workflow changes. `RootViewController` still contains the temporary validation send UI and explicitly states the final input box belongs to `DEV-composer-parity`. Both Works therefore share the final integration point and response lifecycle dependency.
- **Decision direction**: independent sibling development from `main` is unsafe. Controlled stacked/dependent development is allowed after the current Send/Stream product Candidate is code-frozen for Runtime: Composer may branch from that exact Send/Stream head, keep its own Work/checkpoint/branch, and develop isolated presentation/draft/picker code while final Send/Stop integration remains dependent on the parent lifecycle. If the parent changes, rebase/revalidate before Composer Artifact/Runtime.
- **Files in scope**: this Rules checkpoint and `docs/project/COMPOSER_PARITY_PLAN.md` only.
- **Do-not-touch**: PR #29 branch/checkpoint/product/Candidate/Artifact; no Composer development branch or product code activation in this Rules session.
- **Validation state**: Rules/planning only.
- **Next exact action**: record the stacked/dependent parallel-development gate in `COMPOSER_PARITY_PLAN.md`, merge the rules-only change, then reset this checkpoint to Idle.

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
