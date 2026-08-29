# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Replace the long autonomous-continuation / non-atomic-write prose in root `AGENTS.md` with concise atomic rules, and add explicit Full-vs-Light Resume identity guard reuse for continuous same-session development.
- **User intent / acceptance criteria**: Preserve all previously accepted behavior: autonomous continuation to a testable IPA/Artifact when no real Human Gate exists; early/rolling checkpoints without per-micro-step GitHub noise; grouped recovery for non-atomic GitHub writes; same-session reuse of already-verified task identity; Full Guard only on real resume/identity-risk events; Light Guard for one local uncertainty; resume checks must not become a new `继续` gate.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; `AGENTS.md` blob `4451a4ac54bacd16d10aa06d46f1713ff45c2a62`.
- **Evidence / reason**: User observed repeated complete recovery checks on continuous turns and requested the previously discussed rules be rewritten into short, one-constraint-per-line governance rules for clearer execution and lower redundant GitHub read latency.
- **Files in scope**: `AGENTS.md`, this Rules checkpoint only.
- **Do-not-touch**: Product source, build/version/Candidate identity, `PROJECT_STATE.md`, active/future Development checkpoints, Phase 9 planning/source.
- **Completed**: Repository startup/governance documents re-read; current main and current rule baseline verified.
- **Validation state**: Rule structure agreed in conversation; permanent edit pending.
- **Pending**: Rewrite root `AGENTS.md`; re-read resulting rule; reset Rules checkpoint to Idle.
- **Next exact action**: Replace current sections 16–17 with one structured `Autonomous continuation / checkpoint / resume` section containing atomic bullets and preserving the non-atomic recovery safety boundary.
- **Rejected / do-not-repeat**: Do not weaken new-session/identity-risk verification; do not require Full Guard on every ordinary follow-up turn; do not checkpoint every blob/tree/commit/ref micro-operation.
- **Open questions / risks**: None; this is governance wording/behavior only.

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
