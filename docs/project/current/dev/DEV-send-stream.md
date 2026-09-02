# DEV-send-stream

## Status

**Active — exact scoped full navigation `/g/{scope}/c/{conversation}` is Runtime Positive for official page-owned continuation, and latest visible-Web trace proves the official project conversation anchor already contains this scoped canonical href before entry. `gizmo_id` is not Runtime-confirmed. Remaining pre-b89 question: deterministic canonical-href resolution for a Native-selected conversation without manual sidebar/project expansion. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Latest feature/docs head before PR sync: `619afd0e000ef1e64638fe2201444679faad056c`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 product / Artifact / IPA identity unchanged
- Stable/Frozen Send: No

## Runtime evidence

- Control B: `docs/project/runtime-evidence/DEV-send-stream-scoped-full-navigation-continuation-positive-20260903.md`
- Canonical href: `docs/project/runtime-evidence/DEV-send-stream-official-project-canonical-anchor-20260903.md`

Latest trace proves the project anchor target was already `/g/{scope}/c/{conversation}` before navigation; project entry immediately issued page-owned `stream_status` and did not first require a project Detail response exposing the scope. The ordinary comparison Detail had `gizmo_id=null`, so `gizmo_id` is not our Runtime-confirmed route contract.

## Next exact action

Do not allocate b89 yet. Inspect current covered-Web source/page state for deterministic official canonical-href resolution keyed by Native-selected `conversationID`, independent of manual sidebar/project expansion. If available, b89 may use exact fresh full navigation to that official href for scoped conversations while ordinary `/c/<conversation>` remains unchanged. No guessed `gizmo_id`, router internals, project endpoints, polling, timers, retries or Native continuation protocol synthesis.

## Batch recovery state

Docs-only canonical-href evidence is complete through feature head `619afd0e000ef1e64638fe2201444679faad056c`. Pending only: synchronize PR #29 title/body, verify PR/head, then final checkpoint close. Do not replay prior docs writes; do not touch product/version/Candidate/Artifact/IPA.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 49**.
