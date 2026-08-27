# Current Work — Rules

## Status

**Active**

- **Task**: Reprioritize attachment transfer and message-copy capabilities in the durable development sequence.
- **User intent / acceptance criteria**: Preserve one-tap copy behavior; raise image/file sending and assistant-file download/share because they are high-frequency; keep a full download manager lower priority if needed.
- **Baseline**: `main` at `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`; rules branch `rules/attachment-priority-plan-20260827`.
- **Evidence / reason**: Current roadmap leaves `DEV-attachments` late even though the user explicitly identifies image/file send as high-frequency. Current active `DEV-multi-conversation-state` b21 is isolated on its own branch and does not modify the durable files planned here.
- **Files in scope**: `DEVELOPMENT_PLAN.md`, `UI_INTERACTION_BASELINE.md`, `START_HERE.md`, new attachment-transfer plan, this rules checkpoint.
- **Do-not-touch**: product source, current `DEV-multi-conversation-state` checkpoint/branch/Candidate, its overlapping state/governance docs, auth/protocol behavior.
- **Completed**: repository/governance read; current roadmap and active b21 checkpoint verified; conflict scan completed.
- **Validation state**: planning/rules only; no product implementation/CI/Artifact/Runtime change.
- **Pending**: document priority split, copy semantics, send/upload/download/share core scope, lower-priority download-manager scope; PR/merge; reset rules checkpoint to Idle.
- **Next exact action**: add durable attachment-transfer plan and update non-overlapping roadmap/UI/entry-point documents.
- **Rejected / do-not-repeat**: do not bundle a persistent download manager into the first attachment Candidate; do not guess private upload/download endpoints; do not treat CI as transfer-runtime proof.
- **Open questions / risks**: exact current attachment/upload/download protocol and authenticated URL semantics remain Unknown/Unverified until dedicated development evidence.

## Active task template

When a multi-step rules task starts, switch to `Active` early and maintain Task, user intent, baseline, evidence, files in scope, do-not-touch, completed, validation, pending, next exact action, rejected routes and open risks.

## Completion

When complete, move durable rules to permanent rule files, reset only this file to `Idle`, and do not modify/delete/reset any Active development checkpoint merely to finish rules work.
