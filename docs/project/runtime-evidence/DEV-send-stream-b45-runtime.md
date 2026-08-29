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

Uploaded diagnostics reported:

- Candidate `DEV-send-stream-0.1.0-b45`
- app `0.1.0`, build `45`
- source `accd7bdf29e4`
- Release
- iPhone / iOS17.0

The export is therefore accepted as exact-b45 real-device evidence for the structural observations below.

## Capture A — existing-conversation classified page

- Send at `2026-08-29T11:17:15Z`.
- `POST /backend-api/f/conversation` via `fetch`.
- HTTP200 `text/event-stream` at `11:17:16Z`.
- Original stream event 1: protocol marker `v1`.
- Event 2: `resume_conversation_token`; `conversation_id` structurally present; token value redacted.
- Later original-stream structure exposes `conversation_id`, then `conversation_id + request_id`, then `message_id` markers.
- At `11:17:16Z`, official page opened `GET /backend-api/conversation/{id}/stream_status` via `fetch`.
- `stream_status` returned HTTP200 `application/json`; observed payload shape was `{status: string}` only.
- No EventSource, WebSocket, turn-stream, handoff, resume, subscribe, or other continuation-event transport was observed while the response was active.
- Original Send SSE remained the active response transport until `message_stream_complete` around `11:17:46Z`, `conversation_detail_metadata`, and `[DONE]` around `11:17:47Z`.
- Approximate observed Send-to-DONE duration: 32 seconds.

## Capture B — `new_or_other` page with Gizmo structure

- Send at `2026-08-29T11:19:39Z`.
- `POST /backend-api/f/conversation` via `fetch`.
- HTTP200 `text/event-stream` at `11:19:40Z`.
- Original stream again emitted `resume_conversation_token` at event 2.
- Original-stream structure again exposed `conversation_id + request_id` and later `message_id`.
- Request structure contained both top-level `conversation_id` and `conversation_mode.gizmo_id`.
- Therefore this capture is **not accepted as a clean default-primary new-chat sample**; it is Gizmo/custom-GPT-associated structural evidence only.
- No follow-up continuation transport was observed while this response was active.
- Original Send SSE reached `message_stream_complete`, `conversation_detail_metadata`, and `[DONE]` around `11:20:11Z`.
- Approximate observed Send-to-DONE duration: 32 seconds.

## What b45 proves

1. `resume_conversation_token` is emitted very early by the original official-Web Send SSE in both captured sequences.
2. The normal uninterrupted official page keeps the original `/backend-api/f/conversation` `fetch` SSE as the live answer transport through completion.
3. The observed `/conversation/{id}/stream_status` follow-up is a JSON status endpoint in this capture, not an answer-event stream.
4. No naturally occurring secondary same-response continuation stream was observed during either uninterrupted answer.
5. No response ID or turn ID was surfaced by this probe in the captured signals; `request_id`, conversation identity and message identity structure were observed on the original stream.

## What b45 does not prove

- It does **not** prove that no official reconnect/resume mechanism exists.
- It does **not** justify Native replay/use of `resume_conversation_token`.
- It does **not** establish `stream_status` as a continuation endpoint.
- It does **not** prove a Native same-response handoff path.
- It does **not** provide a clean default-primary new-chat sample for Capture B because `gizmo_id` was present.

The key missing condition is an interruption while the original Send SSE is still active. Every background/foreground interval in this export occurred before a Send or after the corresponding SSE had already completed, so the official page never needed to demonstrate active-response reconnect behavior.

## Architecture conclusion

Current desired architecture remains conditional:

`user-visible official Web legal Send -> Native no-resend attach/resume to same response -> Native owns visible realtime response lifecycle`.

This first b45 Runtime capture is **insufficient to implement Native parity**. The absence of a second stream during an uninterrupted response is expected and cannot be promoted into a No-go conclusion.

Do not guess a resume endpoint, reinterpret the token name as an API contract, or allocate a Native continuation implementation yet.

## Next exact Runtime experiment — same exact b45

No product change is required to collect the missing evidence because b45 already observes fetch/XHR/EventSource/WebSocket plus continuation-like route classes.

1. Clear diagnostics.
2. Use default ChatGPT / primary assistant only; avoid custom GPT/Gizmo.
3. Start a prompt long enough to stream well beyond 30 seconds.
4. While output is visibly still streaming, background or lock the device for roughly 20–30 seconds.
5. Return before the response would normally have completed.
6. Do not refresh, resend, Stop, or switch GPTs.
7. Let official Web recover/continue/finish naturally and export diagnostics.

Evidence question: after foreground return, does the page continue the same original transport, or does it open an official status/resume/handoff/turn-stream/subscription connection that receives the same response without a second Send?

## Evidence classification

- Code written: Yes
- CI passed: Yes
- Artifact produced: Yes
- Package identity verified: Yes
- Runtime/manual/real-device: **Yes for this structural capture**
- Native same-response handoff capability: **Unknown / Unverified**
- Stable/Frozen Send: **No**
