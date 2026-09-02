# DEV-send-stream

## Status

**Active — Control B remains Runtime Positive: fresh full navigation to exact official `/g/{scope}/c/{conversation}` starts official page-owned continuation with transient user activation false. New visible-Web trace proves the project scope is already encoded in the official sidebar conversation anchor href before project entry; trusted SPA entry from an ordinary `/c/{id}` conversation to that anchor immediately issues page-owned `stream_status`. The earlier `gizmo_id` payload hypothesis is not Runtime-confirmed and is no longer the only pre-b89 path. Next evidence decision is whether b89 can safely reuse/resolve the official canonical href without inventing service fields. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Latest feature/docs head before PR-summary synchronization: `ea8017a2e300f37d216ef9d6eb0d6e37cb5a9faf`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Control B Runtime — exact scoped full navigation Positive

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-scoped-full-navigation-continuation-positive-20260903.md`.

- `phase=full_navigation_started`, `activationAtNavigation=false`;
- Navigation Timing `type=navigate`;
- final route `/g/{x}/c/{x}`;
- page-owned `plural_snapshot=9`, `stream_status=8`, `resume=0`;
- exact scoped fresh navigation can therefore start genuine official status/snapshot continuation without trusted click or same-document SPA entry.

## Canonical-href Runtime evidence — 2026-09-03

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-official-project-canonical-anchor-20260903.md`.

Visible-Web observer result:

- ordinary conversation anchor targeted `/c/{id}` and official page used that exact href via `history.pushState`;
- ordinary `GET /backend-api/conversations/{id}` returned HTTP 200 with `gizmo_id=null`, `gizmo_type=null`, a non-matching `memory_scope`, and empty `context_scopes`;
- when user clicked back to the project conversation, the anchor target was already `/g/{scope}/c/{conversation}` before navigation;
- official `history.pushState` used that exact scoped href;
- project entry immediately issued `POST /backend-api/conversation/init`, `GET /backend-api/conversation/{conversation}/stream_status`, and sentinel prepare/finalize; project `stream_status` returned HTTP 200;
- no project `GET /backend-api/conversations/{conversation}` payload was needed in this captured transition.

Interpretation:

1. official Web already possesses the project scope inside the canonical conversation href before project entry;
2. successful project entry does not need to rediscover that scope from a project Detail response in this sample;
3. `gizmo_id` remains external corroboration only, not Runtime-confirmed contract;
4. b89 should prefer an evidenced official canonical-route source instead of guessing a service field;
5. implementation evidence gap: can covered production Web resolve the canonical href for a Native-selected conversation without manual sidebar/project expansion?

## Confirmed source gap

Current source still has only unscoped conversation identity and hard-loads `https://chatgpt.com/c/<conversationID>` for existing-conversation covered Web observation/send. Production therefore cannot reproduce the exact scoped full navigation that Control B proved works.

## Next exact action

Do **not** allocate b89 yet and do not guess `gizmo_id`.

Inspect current covered-Web source and existing Web-side state for a deterministic canonical conversation href keyed by Native-selected `conversationID`, independent of manual sidebar/project expansion. Use only current official DOM/page state or an already-used official response. Do not add broad discovery, timers, retries, polling, router emulation or guessed project endpoints.

If deterministic canonical href resolution exists, b89 may be narrow: exact fresh full navigation to that official href for scoped conversations, ordinary `/c/<conversation>` unchanged.

## Documentation batch recovery state

Confirmed writes:

- recovery checkpoint `190cbfca019c3aa0f3f2d20e5538d56cf2e08f96`;
- durable canonical-href Runtime evidence `b13806e6ef50179acecc29e6a61facfbe246f302`;
- recovery/checkpoint adjustments through `ea8017a2e300f37d216ef9d6eb0d6e37cb5a9faf`.

Still pending: PR #29 title/body synchronization, PR/head verification, final checkpoint identity close. Do not replay prior writes. No product source, version/build, Candidate, Artifact or IPA may change in this docs-only batch.

## Evidence ladder / preserved boundaries

- Control B: Runtime Positive for exact scoped full navigation continuation.
- Canonical-href trace: Runtime Positive that official project scope is encoded in visible-Web anchor href and project entry immediately starts `stream_status`.
- No product source changed; no new Candidate / CI / Artifact / IPA.
- `ConversationRepository` remains sole Native response/content authority.
- Native must not construct `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send or WebSocket-body authority.
- hidden thoughts remain non-presentational; b80 presentation/final boundaries remain preserved.

## Session round counter

This user turn is **round 49**.
