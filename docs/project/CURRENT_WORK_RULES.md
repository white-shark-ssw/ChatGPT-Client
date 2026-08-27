# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Sync newly merged attachment/copy priority into the durable UI interaction baseline.
- **User intent / acceptance criteria**: official-style one-tap Copy must not be lost; assistant files need tap-download then immediate system share; image/file sending is high-frequency; download manager remains later.
- **Baseline**: `main` at `3befd50cd62957f790ca2907adb606ed32a34e6f`; PR #19 already merged the roadmap and `ATTACHMENT_TRANSFER_PLAN.md`.
- **Files in scope**: `docs/project/UI_INTERACTION_BASELINE.md`, this rules checkpoint only.
- **Do-not-touch**: active `DEV-multi-conversation-state` product branch/checkpoint/product code and its overlapping durable state docs.
- **Completed**: verified PR #19 already covers roadmap/transfer ownership and protocol boundaries; identified UI baseline as the only remaining durable interaction-doc gap.
- **Validation state**: Rules/docs only; no product code, build, Candidate, CI, Artifact or Runtime change.
- **Pending**: add compact copy + attachment interaction requirements; diff/conflict check; merge; reset checkpoint Idle.
- **Next exact action**: update `UI_INTERACTION_BASELINE.md` only.
- **Rejected / do-not-repeat**: no duplicate attachment roadmap/plan; no second attachment plan; no product implementation in this rules session.
- **Open questions / risks**: exact current upload/download protocol remains Unverified and belongs to future `DEV-attachments` evidence work.

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
