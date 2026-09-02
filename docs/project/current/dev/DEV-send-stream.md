# DEV-send-stream

## Status

**Active — Control B remains Runtime Positive: fresh full navigation to exact official `/g/{scope}/c/{conversation}` starts official page-owned continuation with transient user activation false. New visible-Web trace proves the project scope is already encoded in the official sidebar conversation anchor href before project entry; trusted SPA entry from an ordinary `/c/{id}` conversation to that anchor immediately issues page-owned `stream_status`. The earlier `gizmo_id` payload hypothesis is not Runtime-confirmed and is no longer the only pre-b89 path. Next evidence decision is whether b89 can safely reuse/resolve the official canonical href without inventing service fields. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Latest feature/docs head before PR-summary synchronization: `591e4108d230af55ac5b6b230232f5e30873cf6c`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Runtime conclusions

- Control B: exact scoped fresh navigation `/g/{scope}/c/{conversation}` with transient activation false is Runtime Positive for official page-owned continuation (`stream_status + plural_snapshot`).
- Canonical-href trace: when returning from an ordinary conversation to the project conversation, the trusted click target already contained the exact `/g/{scope}/c/{conversation}` href before navigation; project entry immediately issued page-owned `stream_status` and did not first require a project Detail fetch that exposed the scope.
- Ordinary `GET /backend-api/conversations/{id}` in the comparison sample returned `gizmo_id=null`, `gizmo_type=null`, non-matching `memory_scope`, empty `context_scopes`; this does not identify the project scope source.
- Therefore the official canonical href itself is current Runtime evidence; `gizmo_id` remains external corroboration only.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-scoped-full-navigation-continuation-positive-20260903.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-project-canonical-anchor-20260903.md`

## Confirmed source gap

Current Native model/cache does not preserve scoped canonical route identity and existing covered-Web observation/send hard-loads `https://chatgpt.com/c/<conversationID>`. Production cannot reproduce Control B's exact scoped full navigation.

## Next exact action

Do **not** allocate b89 yet and do not guess `gizmo_id`.

Inspect current covered-Web source and existing Web-side state for a deterministic official canonical conversation href keyed by Native-selected `conversationID`, independent of manual sidebar/project expansion. Use only current official DOM/page state or an already-used official response. Do not add broad discovery, timers, retries, polling, router emulation or guessed project endpoints.

If deterministic canonical href resolution exists, b89 may be narrow: exact fresh full navigation to that official href for scoped conversations, ordinary `/c/<conversation>` unchanged.

## Documentation batch recovery state

Confirmed: recovery checkpoint, durable canonical-href evidence, and subsequent checkpoint synchronization through feature/docs head `591e4108d230af55ac5b6b230232f5e30873cf6c`.

Still pending: PR #29 title/body synchronization, PR/head verification, final checkpoint identity close. Do not replay earlier writes. No product source, version/build, Candidate, Artifact or IPA may change in this docs-only batch.

## Preserved boundaries

- official page remains continuation executor;
- `ConversationRepository` remains sole Native response/content authority;
- no Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send or WebSocket-body authority;
- no new Candidate / CI / Artifact / IPA;
- Stable/Frozen Send: No.

## Session round counter

This user turn is **round 49**.
