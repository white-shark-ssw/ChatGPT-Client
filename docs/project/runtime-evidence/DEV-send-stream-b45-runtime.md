# DEV-send-stream b45 Runtime Evidence

_Date: 2026-08-29_

## Exact Candidate

- Candidate: `DEV-send-stream-0.1.0-b45`
- Version/build: `0.1.0 (45)`
- Exact product/config source: `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`
- Push Run / Job: `33248952646` / `99091176390` — success
- PR Run / Job: `33248954018` / `99091179731` — success
- Artifact: `9713774868`
- Artifact ZIP digest: `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`
- IPA: `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`
- IPA SHA-256: `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`
- Package inspection: Release; source marker `accd7bdf29e4`; deployment target iOS14.0; UIDeviceFamily `[1,2]`; arm64

## Device / export identity

All accepted exports reported exact b45 identity: Candidate `DEV-send-stream-0.1.0-b45`, app `0.1.0`, build `45`, source `accd7bdf29e4`, Release, iPhone / iOS17.0.

## Capture A — uninterrupted existing-conversation path

- `POST /backend-api/f/conversation` -> HTTP200 `text/event-stream`.
- Original stream emitted protocol marker `v1`, then very early `resume_conversation_token`, conversation/request/message identity structure, and normal terminal events.
- `GET /backend-api/conversation/{id}/stream_status` returned HTTP200 JSON with structural `{status:string}` only.
- No secondary continuation stream was needed while the original Send SSE remained intact.

Accepted conclusion: uninterrupted Web keeps the original Send SSE as response transport; token existence/name alone did not establish a Native continuation contract.

## Capture B — Gizmo/custom-GPT-associated uninterrupted sample

- Same Send route/framing as Capture A.
- Request structure included `conversation_mode.gizmo_id`; therefore this sample is not a clean default-primary new-chat sample.
- Original Send SSE again remained transport through completion.

## Capture C — clean default-primary new-chat with repeated active background / lock

The user explicitly identified this as a new conversation. The Send body had no top-level `conversation_id` and no `conversation_mode.gizmo_id`, so it is accepted as a clean default-primary new-chat sample.

While the same original Send SSE remained active, the app was backgrounded/locked for approximately 35s, 34s and 126s; cumulative active-response background time was ~195s / 3m15s. Send-to-terminal was ~227s / 3m47s.

On final foreground return, the same original `conversation_send` / `fetch` stream immediately delivered `server_ste_metadata -> message_stream_complete -> conversation_detail_metadata -> [DONE]`. No second Send, new SSE, resume/handoff/turn-stream/subscription connection, manual refresh or resend was observed.

Accepted conclusion: on the primary iPhone/iOS17 runtime, the tested WebKit/original-fetch response path can survive or buffer across repeated ordinary background/lock intervals, including ~126s continuous, and still complete normally. This does not prove continuous background event delivery or 5/15-minute behavior.

## Capture D — official no-resend resume transport confirmed

Uploaded export time: `2026-08-29T13:35:23Z`.

This sample's initial Send request contained both top-level `conversation_id` and `conversation_mode.gizmo_id`, so it is an existing/Gizmo-associated response. It is accepted for the generic official resume transport structure, not as default-primary parity proof.

### Original response before interruption

- Send request: `POST /backend-api/f/conversation` at `13:28:44Z`.
- Send response: HTTP200 `text/event-stream` at `13:28:56Z`.
- Original stream event 2: `resume_conversation_token` with conversation identity structurally present.
- Events 3/4: conversation + request identity structure.
- Original event 11: `message_marker` at `13:29:08Z`.
- The original Send stream did not later produce terminal events in this export; recovery traffic took over after the interruption.

### Official resume request contract

After the original transport was disrupted, the official page repeatedly opened:

`POST /backend-api/f/conversation/resume`

Observed JSON body shape on every captured attempt:

`{ conversation_id: string, offset: number }`

Observed request header names included `accept`, `authorization`, `content-type`, normal OAI client/session/route headers and `x-conduit-token`. No Sentinel proof, Turnstile or PoW header names were present on the resume request. Diagnostics captured header **names only**, never values.

### Offline/error phase

From `13:29:23Z` through `13:29:46Z`, the official page repeatedly attempted the same resume route and each attempt ended in `transportError` while connectivity was unavailable. This is official Web retry behavior; it is Runtime evidence only and does not authorize Native retry machinery.

### First successful continuation

At `13:29:50Z` official Web opened `/resume` again. At `13:29:53Z` it returned:

- HTTP200;
- `Content-Type: text/event-stream`;
- continuation event 1 with `conversation_id + request_id` identity structure.

No second `/f/conversation` Send was observed.

### Second successful continuation after another interruption

A later interruption produced further official resume traffic. At `13:32:10Z`, `/resume` again returned HTTP200 `text/event-stream` with continuation event 1 carrying conversation + request identity structure.

### Third successful continuation and normal terminal tail

After a later background interval, official Web opened `/resume` at `13:35:00Z`. It returned HTTP200 `text/event-stream` at `13:35:02Z`.

That continuation stream then emitted:

- event 1: conversation + request identity structure;
- event 9: `message_marker` with conversation + message identity;
- event 85: `server_ste_metadata` with conversation/message/request identity and metadata keys including `turn_exchange_id`, `working_turn_id`, `resume_with_websockets`, `streaming_async_status` and related structural fields;
- event 86: `message_stream_complete`;
- event 87: `conversation_detail_metadata`;
- event 88: terminal `[DONE]`.

The continuation reached the same normal terminal grammar previously seen on the original Send stream.

## What Capture D proves

1. Current official ChatGPT Web has a real post-Send no-resend continuation endpoint: `POST /backend-api/f/conversation/resume`.
2. The observed request body structural contract is exactly `{conversation_id: string, offset: number}`.
3. A successful resume returns HTTP200 `text/event-stream` and can carry the already-started response through ordinary message identity, metadata, `message_stream_complete`, `conversation_detail_metadata`, and `[DONE]`.
4. The official page can perform this recovery repeatedly across multiple interruptions without a second `conversation_send`.
5. The endpoint is a continuation/read path after browser-owned Send; it does not bypass the b42 protected Send challenge boundary.

## What Capture D does not prove

- Exact numeric `offset` semantics/value relationship to the original stream cursor were not logged by b45.
- Required resume headers beyond the already accepted transient cookies + bearer are not yet known. Header-name presence is not proof every browser header is mandatory.
- Native access to `/resume` is not yet proven.
- Default-primary Native resume parity is not yet proven because Capture D's Send was Gizmo-associated.
- Current `AuthTransientSession.dataTask` buffers the full response; incremental Native streaming is still unimplemented/unverified.
- Official Web's repeated retry schedule is not a design contract for Native and must not be copied as timer/retry machinery.

## Architecture consequence

The prior condition for a minimal Native no-resend parity experiment is now satisfied.

The next candidate may test only this narrow question:

> After visible official Web performs the protected Send and official Web itself exposes a successful `/resume` body, can Native use the same `conversation_id + offset` once through the existing WebKit-derived transient cookie + bearer boundary and receive the same endpoint's SSE without copying browser challenge or Conduit values?

This experiment must remain diagnostic-only, one attempt, no retries, no production `ConversationRepository` mutation and no second Send.

## Evidence classification

- Code written: Yes
- CI passed: Yes
- Artifact produced: Yes
- Package identity verified: Yes
- Runtime/manual/real-device: **Yes — uninterrupted, short-background, and forced-interruption official-resume captures**
- Ordinary active-response background survival/buffering: **Positive on exact recorded scope up to ~126s continuous / ~195s cumulative**
- Official no-resend resume route/method/body-shape/SSE framing: **Runtime Confirmed for captured existing/Gizmo response**
- Native `/resume` parity: **Unknown / Unverified — b46 gate**
- Default-primary Native continuation: **Unknown / Unverified**
- Incremental Native response ownership/reasoning/follow-tail/background lifecycle: **Unknown / Unverified**
- Stable/Frozen Send: **No**