# DEV-send-stream

## Status

**Active — exact scoped full navigation `/g/{scope}/c/{conversation}` is Runtime Positive for official page-owned continuation. Latest visible-Web trace proves the official project conversation anchor already contains this scoped canonical href before entry. `gizmo_id` is not Runtime-confirmed. Remaining pre-b89 question: deterministic canonical-href resolution for a Native-selected conversation without manual sidebar/project expansion. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Latest feature/docs head before PR metadata synchronization: `6e680e21f88dec2b0c16e6409c619ae8644ad8be`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 product / Artifact / IPA identity unchanged
- Stable/Frozen Send: No

## Runtime evidence

- `docs/project/runtime-evidence/DEV-send-stream-scoped-full-navigation-continuation-positive-20260903.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-project-canonical-anchor-20260903.md`

Latest trace:

- ordinary anchor target `/c/{id}` -> ordinary `history.pushState`, Detail and status requests;
- project anchor target already `/g/{scope}/c/{conversation}` before navigation;
- official project `history.pushState` used that exact scoped href;
- project entry immediately issued `POST /backend-api/conversation/init` and `GET /backend-api/conversation/{conversation}/stream_status`, status HTTP 200;
- no project Detail response exposing scope was required in that successful transition;
- ordinary comparison Detail had `gizmo_id=null`; therefore `gizmo_id` is external corroboration only, not current Runtime contract.

## Next exact action

Do not allocate b89 yet. Inspect current covered-Web source/page state for deterministic official canonical-href resolution keyed by Native-selected `conversationID`, independent of manual sidebar/project expansion. If available, b89 may use exact fresh full navigation to that official href for scoped conversations, leaving ordinary `/c/<conversation>` unchanged. No guessed `gizmo_id`, router internals, project endpoints, polling, timers, retries or Native continuation protocol synthesis.

## Batch recovery state

Canonical-href evidence docs are complete. The only missing batch operation is PR #29 title/body synchronization, followed by PR/head verification and one final checkpoint close. Exact head before that operation: `6e680e21f88dec2b0c16e6409c619ae8644ad8be`. Do not replay prior docs writes; do not touch product/version/Candidate/Artifact/IPA.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 49**.
