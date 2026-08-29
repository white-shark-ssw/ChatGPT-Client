# DEV-send-stream b41 — Runtime Protocol Evidence

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b41`
- Version/build: `0.1.0 (41)`
- Exact product/config source: `a2899e8bfdacd9b642c026c14f484735c1ac60fa`
- Push Run / Job: `33234523162` / `99053041864`
- Runtime Artifact: `9709515645`
- Artifact ZIP digest: `sha256:1707aa7d51956ece34301d1143513aeff2358c4ae3ccded2e23a052110811c31`
- IPA SHA-256: `0941b73ccbaf7552870adc85aa03e631dcb4181ab13df14da6b5041b860acc83`
- Runtime: iPhone / iOS 17.0; diagnostics exported `2026-08-29T05:00:13Z`
- Evidence class: **real-device protocol-probe Runtime**, not native production Send acceptance.

## Existing primary-assistant Send

- `POST /backend-api/f/conversation` -> HTTP 200 `text/event-stream`.
- Safe observed semantics: `action=next`, `client_prepare_state=success`, `conversation_mode.kind=primary_assistant`, `model=gpt-5-6-thinking`, `thinking_effort=extended`, `supported_encodings=["v1"]`, buffering/followups enabled, `force_parallel_switch=auto`, CoT-summary override `allow`, one user text message and one response contract protocol v1.
- Existing conversation ID shape is opaque. User-message ID and parent-message ID are UUID-shaped and distinct.
- Normal stream: first structural frame about 500 ms; 12 data frames; `"v1"`, early `resume_conversation_token`, input/message/patch events, `message_stream_complete`, trailing `conversation_detail_metadata`, then `[DONE]`.

## New-conversation sample caveat

- Send omitted `conversation_id`; authoritative conversation ID appeared by `resume_conversation_token`; `title_generation` was present.
- This specific b41 new-chat sample was `conversation_mode.kind=gizmo_interaction` with `gizmo_id`, so its mode/parent semantics are **not** authority for ordinary default ChatGPT new chat.
- It still confirms the new-conversation identity handoff and stream family, but b42 must use default ChatGPT / primary assistant for the remaining mode/protection decision.

## Server Stop

- Official Stop request: `POST /backend-api/stop_conversation`.
- Body shape: `{ conversation_id: string, exclude_async_types: [] }`.
- Request included current transient auth/client headers and `x-conduit-token`.
- Response: HTTP 200 `application/json`; observed shape `{ status: string, last_message_id: null }`.
- The associated Send stream ended with `doneSeen=false` after 21 frames and without the normal `message_stream_complete` / `[DONE]` tail.
- Architecture implication: server Stop is distinct from local task cancellation. The exact repository-owned active response must transition once to `user-stopped` on accepted server Stop semantics; later stream closure must not become a duplicate network-failure or normal-completion terminal.

## Protection / precursor structure

- `/backend-api/f/conversation/prepare` returns `{ conduit_token: string, status: string }`; successful Send uses `x-conduit-token`.
- Sentinel prepare structure: `{ persona, prepare_token, proofofwork:{required,seed,difficulty}, so:{required,collector_dx,snapshot_dx}, turnstile:{required,dx} }`.
- Sentinel finalize request: `{ prepare_token, proofofwork, turnstile }`; response: `{ token, persona, expire_after, expire_at }`.
- Successful Send carries Sentinel requirements/proof/turnstile header names.
- No token/proof/header values, prompt, answer, reasoning text or raw IDs were captured.

## Remaining P0 evidence gap

b41 records the structure but not the boolean values of `proofofwork.required`, `turnstile.required`, `so.required`, and not whether finalize proof/turnstile submissions are empty. Therefore b41 cannot yet distinguish:

- a normal no-challenge native precursor path; from
- a flow requiring browser-side PoW/Turnstile/other anti-abuse challenge execution.

Do not implement or copy a Sentinel/PoW/Turnstile solver, challenge bypass, browser-fingerprint replay or captured proof/token replay. Exact b42 is reserved solely to record those non-secret booleans/presence facts and decide the path.
