# DEV-send-stream

## Status

**Active — Control B remains Runtime Positive: fresh full navigation to exact official `/g/{scope}/c/{conversation}` starts official page-owned continuation with transient user activation false. New visible-Web trace proves the project scope is already encoded in the official sidebar conversation anchor href before project entry; trusted SPA entry from an ordinary `/c/{id}` conversation to that anchor immediately issues page-owned `stream_status`. The earlier `gizmo_id` payload hypothesis is not Runtime-confirmed and is no longer the only pre-b89 path. Next evidence decision is whether b89 can safely reuse/resolve the official canonical href without inventing service fields. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Latest verified docs head before PR-summary sync: `4633f18a113710276838c2d65c0ea58c144d9752`
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
- Resource Timing not saturated;
- page-owned `plural_snapshot=9`, `stream_status=8`, `resume=0`;
- therefore exact scoped fresh navigation can start genuine official status/snapshot continuation without trusted click or same-document SPA entry.

## Control A / B causal matrix

| Entry | Route | Result |
|---|---|---|
| Full load | `/c/{id}` | Negative in b88 project samples |
| Full load | exact official `/g/{scope}/c/{id}` | **Positive — Control B** |
| SPA programmatic click | exact official `/g/{scope}/c/{id}` | Router/bootstrap Positive; continuation Negative |
| SPA trusted click | exact official `/g/{scope}/c/{id}` | Positive — visible-Web samples |

The strongest evidenced defect remains production loss of project/GPT scoped route identity. Native must not synthesize `stream_status`, `/resume`, offsets or cadence.

## Canonical-href Runtime evidence — 2026-09-03

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-official-project-canonical-anchor-20260903.md`.

Latest privacy-safe visible-Web observer started on an already loaded project route, then the user entered an ordinary conversation and clicked back to the target project conversation.

Observed ordinary entry:

- trusted click anchor target `/c/{id}`;
- official `history.pushState` to `/c/{id}`;
- official `GET /backend-api/conversations/{id}` with query keys `include_has_versions,num_turns` -> HTTP 200 JSON;
- that ordinary payload exposed `gizmo_id=null`, `gizmo_type=null`, non-matching `memory_scope`, empty `context_scopes`;
- official ordinary page then issued `GET /backend-api/conversation/{id}/stream_status` -> HTTP 200.

Observed project re-entry:

- trusted click target was already the exact official anchor `/g/{scope}/c/{conversation}` **before** navigation;
- official `history.pushState` used that exact scoped target;
- after route change, page issued `POST /backend-api/conversation/init`, `GET /backend-api/conversation/{conversation}/stream_status`, and sentinel prepare/finalize requests;
- project `stream_status` returned HTTP 200;
- no project `GET /backend-api/conversations/{conversation}` response was needed in this captured transition, so no project payload field can be claimed as the source of the scope from this sample.

Interpretation:

1. current official Web possesses the canonical scoped route in the conversation anchor itself before target entry;
2. the route scope does not need to be rediscovered from a project Detail request during this successful transition;
3. `gizmo_id` remains plausible external corroboration but is **not** a Runtime-confirmed service contract for this client;
4. b89 should prefer an evidenced official canonical-route source over guessing an API field;
5. whether the covered production Web can resolve that canonical href deterministically for a Native-selected conversation without manual sidebar expansion remains the key implementation evidence gap.

## Confirmed source gap

Current source still has:

- `ConversationSummary`: `id`, `title`, `updateTime` only;
- `ConversationDetail`: no project/GPT scoped route identity;
- list cache persists only `id/title/updateTime`;
- `parseConversationSummary` reads only `id/title/update_time`;
- `CoveredWebSendExecutor.observeExistingConversation` and `sendExistingConversation` hard-load `https://chatgpt.com/c/<conversationID>`.

Therefore production cannot reproduce the exact scoped route that Control B proved works.

## Next exact action

Do **not** allocate b89 yet and do not guess `gizmo_id`.

First inspect current covered-Web source and existing Web-side state to determine whether, for a Native-selected `conversationID`, the official page already exposes a deterministic canonical conversation href independent of manually expanding project/sidebar UI. Candidate evidence surfaces must be current official DOM/page state or an already-used official response; do not add broad auto-discovery, timers, retries, polling, router emulation or a guessed project endpoint.

If a deterministic canonical href is available, b89 may be narrowly scoped to using exact fresh full navigation to that official href for scoped conversations while leaving ordinary `/c/<conversation>` unchanged. If not, one further privacy-safe Web Rule Lab structure probe may be needed before product code.

## Documentation batch status

Canonical-href evidence docs are complete:

- recovery checkpoint: `190cbfca019c3aa0f3f2d20e5538d56cf2e08f96`;
- durable Runtime evidence: `b13806e6ef50179acecc29e6a61facfbe246f302`;
- verification checkpoint: `4633f18a113710276838c2d65c0ea58c144d9752`;
- PR #29 remained open / mergeable / unmerged throughout the verified batch;
- PR summary should reflect canonical-href evidence; no product source, version/build, Candidate, Artifact or IPA changed.

## Evidence ladder / preserved boundaries

- Control B: Runtime Positive for exact scoped full navigation continuation.
- Canonical-href trace: Runtime Positive that official project scope is already encoded in visible-Web anchor href and project entry immediately starts `stream_status`.
- No product source changed yet.
- No new Candidate / CI / Artifact / IPA.
- `ConversationRepository` remains sole Native response/content authority.
- Native must not construct `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send or WebSocket-body authority.
- hidden thoughts remain non-presentational; b80 presentation/final boundaries remain preserved.

## Session round counter

This user turn is **round 49**.
