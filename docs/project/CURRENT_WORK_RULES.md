# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Prepare the evidence-first rules/design handoff for future `DEV-send-stream` without activating that Development Work.
- **User intent / acceptance criteria**: Document current Send/Stream protocol evidence gates, state ownership, pending-to-authoritative new-conversation identity handoff, per-conversation response lifecycle, Stop/reasoning/follow-tail, new-chat navigation, expected modification surface, conflict with active `DEV-conversation-round-count`, diagnostics and real-device acceptance. Keep uncertain protocol/runtime facts `Unknown / Unverified`. Do not activate `DEV-send-stream`, create a product development branch/Candidate, modify product code, or modify any development checkpoint. After the predecessor is merged, the future Development session must re-check latest `main` and wait for the user's explicit `当前为开发会话，新任务：DEV-send-stream` before activation.
- **Baseline**: rules branch `rules/send-stream-preflight-20260828` from `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`. Live predecessor evidence: `dev/conversation-round-count-20260828@375e71888976502eb5201093c3c6bcfc4fcae997`, PR #27 open, task checkpoint Active with b31 correction in progress when this checkpoint was established.
- **Evidence / reason**: `AGENTS.md`, `START_HERE.md`, current project state/rules/plans, live GitHub branch/PR facts, current `main` source owners and current predecessor branch checkpoint/files. Current accepted protocol evidence covers list/detail reads only; Send/new-chat/stream/Stop are not accepted contracts.
- **Files in scope**: `docs/project/CURRENT_WORK_RULES.md`, new durable Send/Stream preflight document, and minimal startup routing documentation if needed.
- **Do-not-touch**: all `ChatGPTClient/**` product source, Xcode/workflow Candidate identity, `docs/project/current/dev/**`, PR #27 branch/checkpoint, any future `DEV-send-stream` development checkpoint/branch/Candidate.
- **Completed**: startup/governance read; live `main` resolved; active predecessor branch/PR/checkpoint resolved; current repository/auth/presentation owner source inspected; direct overlap with predecessor confirmed; current incremental-stream transport gap identified.
- **Validation state**: Rules/documentation preparation only. No product Code / CI / Artifact / Runtime claim.
- **Pending**: write durable preflight; route future Send/Stream sessions to it; re-check predecessor live state before closing this Rules Work.
- **Next exact action**: add `SEND_STREAM_PREFLIGHT.md` containing only evidence-backed invariants plus explicit Unknown/Unverified gates, then update startup routing and close this rules checkpoint if documentation review is consistent.
- **Rejected / do-not-repeat**: do not guess private Send/SSE/Stop endpoints or payloads; do not create global `isStreaming`; do not create a second conversation/auth/stream owner; do not activate Send in parallel with the current overlapping predecessor; do not pre-allocate the next build number.
- **Open questions / risks**: exact current Send/new-chat request contract, stream framing/events, server authoritative identity timing, Stop semantics, explicit user-visible reasoning fields, concurrent response support, Sync/Reload interaction while response active, non-personal workspace scope, and exact follow-tail threshold are all Unknown / Unverified until current protocol/runtime evidence exists.

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
