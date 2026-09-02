# DEV-send-stream

## Status

**Active — exact scoped full navigation `/g/{scope}/c/{conversation}` is Runtime Positive for official page-owned continuation, and the latest visible-Web trace proves that the official project conversation anchor already contains this scoped canonical href before entry. `gizmo_id` is not Runtime-confirmed. The remaining pre-b89 question is deterministic canonical-href resolution for a Native-selected conversation without manual sidebar/project expansion. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Latest feature/docs head: `c16dd44f5708e75766df2ef6c3ccbc44e79ef4c5`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 product / Artifact / IPA identity unchanged
- Stable/Frozen Send: No

## Runtime evidence

Control B durable evidence: `docs/project/runtime-evidence/DEV-send-stream-scoped-full-navigation-continuation-positive-20260903.md`.

Canonical-href durable evidence: `docs/project/runtime-evidence/DEV-send-stream-official-project-canonical-anchor-20260903.md`.

Latest trace proves:

- ordinary anchor target `/c/{id}` -> ordinary `history.pushState` and ordinary Detail/status requests;
- project anchor target was already `/g/{scope}/c/{conversation}` before click/navigation;
- project `history.pushState` used that exact scoped href;
- project entry immediately issued `POST /backend-api/conversation/init` and `GET /backend-api/conversation/{conversation}/stream_status`; status returned HTTP 200;
- no project Detail fetch exposing the scope was required in this successful transition;
- ordinary comparison Detail had `gizmo_id=null`; no current Runtime evidence identifies `gizmo_id` as the project scope source.

## Source gap / next exact action

Current Native covered-Web path still hard-loads unscoped `/c/<conversationID>` and does not preserve canonical scoped route identity.

Do not allocate b89 yet. Inspect current covered-Web source/page state for a deterministic official canonical href keyed by Native-selected `conversationID`, independent of manual sidebar/project expansion. Prefer existing official href/page-state/response evidence; do not guess `gizmo_id`, project endpoints, router internals, polling or retries.

If deterministic resolution exists, b89 may use exact fresh full navigation to the official canonical href for scoped conversations while ordinary `/c/<conversation>` remains unchanged.

## Batch recovery state

Docs-only canonical-href evidence writes are complete through head `c16dd44f5708e75766df2ef6c3ccbc44e79ef4c5`. The only remaining write in this batch is PR #29 title/body synchronization, followed by PR/head verification and one final checkpoint close. Do not replay prior docs writes and do not touch product source/version/Candidate/Artifact/IPA.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority, or second response store.

## Session round counter

This user turn is **round 49**.
