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

Both uploaded diagnostics reported exact b45 identity:

- Candidate `DEV-send-stream-0.1.0-b45`
- app `0.1.0`, build `45`
- source `accd7bdf29e4`
- Release
- iPhone / iOS17.0

Both exports are accepted as exact-b45 real-device evidence for the structural observations below.

## Capture A — uninterrupted existing-conversation classified page

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

## Capture C — clean default-primary new-chat with repeated active background / lock

The user explicitly states this was a **new conversation** and deliberately performed several suspend/lock cycles while the answer was still active.

### Request structure

- Probe page initially loaded as `new_or_other` at `12:44:05Z`.
- One pre-Send background interval lasted about 64 seconds and is not part of active-response evidence.
- Send began at `12:45:20Z`: `POST /backend-api/f/conversation` via `fetch`.
- HTTP200 `text/event-stream` returned in the same second.
- The observed Send body had **no top-level `conversation_id`** and **no `conversation_mode.gizmo_id`**.
- Together with the user's explicit statement, Capture C is accepted as the clean default-primary new-chat sample despite the probe classifying the page as `existing_conversation` by Send time.
- Original SSE event 2 again emitted `resume_conversation_token`.
- Events 3/4 exposed conversation identity and then `conversation_id + request_id`; event 13 exposed message identity.
- Official Web again opened `GET /backend-api/conversation/{id}/stream_status`; it returned HTTP200 JSON with structural `{status:string}` only.

### Active-response background intervals

While the original Send SSE remained active:

1. `12:45:27Z` -> `12:46:02Z`: approximately **35 seconds** background.
2. `12:46:15Z` -> `12:46:49Z`: approximately **34 seconds** background.
3. `12:47:01Z` -> `12:49:07Z`: approximately **126 seconds** background.

Total observed active-response background time: approximately **195 seconds / 3m15s**.

Send-to-terminal elapsed time: approximately **227 seconds / 3m47s**.

### Foreground completion behavior

Before the first active background interval the probe had observed original-stream event 13 (`message_marker`).

At the end of the final ~126-second background interval, `willEnterForeground` occurred at `12:49:07Z`. In that same second the **same original `conversation_send` / `fetch` stream** emitted:

- event 464 `server_ste_metadata`;
- event 465 `message_stream_complete`;
- event 466 `conversation_detail_metadata`;
- event 467 terminal `[DONE]`.

No second `conversation_send`, no new `text/event-stream` response, and no resume/handoff/turn-stream/subscribe/EventSource/WebSocket continuation connection was observed after any of the three active-response background intervals.

The user did not need a manual refresh or prompt resend for this capture.

## What Capture C proves

1. On exact b45 / primary iPhone / iOS17.0, the tested official-Web response path can **survive or buffer across multiple ordinary background/lock intervals**, including one approximately 126 seconds long, and still reach normal stream completion without a second Send.
2. The original `/backend-api/f/conversation` fetch remained the observable transport owner from Send to terminal.
3. Natural short-to-medium backgrounding on this device did not force official Web to expose a separate reconnect transport.
4. The clean default-primary new-chat request shape is now evidenced without top-level `conversation_id` and without `gizmo_id` in this capture.

## What Capture C does not prove

- It does **not** prove that WebKit delivered every SSE event continuously while the app was suspended. The probe cannot distinguish continuous background delivery from server/network/WebKit continuation plus buffered delivery on foreground.
- It does **not** prove 5-minute, 15-minute, network-transition, WebContent-process-termination or battery/thermal behavior.
- It does **not** prove Native same-response handoff.
- It does **not** authorize Native use/replay of `resume_conversation_token`.
- It does **not** prove that no official reconnect mechanism exists after a genuine TCP/network/WebContent failure, because the original transport evidently remained viable here.

## Updated architecture conclusion

Current desired architecture remains conditional:

`user-visible official Web legal Send -> Native no-resend attach/resume to same response -> Native owns visible realtime response lifecycle`.

The second b45 Runtime capture improves the WebKit/background side of the architecture: ordinary background/lock did not break this response, including across a ~126-second interval.

However it still provides **no separate official continuation channel** that Native can reproduce. The early `resume_conversation_token` remains only an observed structural field.

Therefore b46 Native continuation implementation is still not justified.

## Next exact Runtime experiment — force the transport to really break, reuse b45

Natural short background is now a weak discovery mechanism because the original WebKit fetch survived all three active-response intervals.

Use the same exact b45 instrumentation and force one controlled connectivity interruption instead:

1. Clear diagnostics.
2. Use default ChatGPT / primary assistant in an **existing long conversation**.
3. Start a response expected to stream long enough to observe recovery.
4. While visibly streaming, deliberately break connectivity for about **10–15 seconds** and then restore it. Preferred deterministic test: Airplane Mode / both Wi-Fi and cellular unavailable, then restore. A Wi-Fi -> cellular transition is also useful after a stable Wi-Fi baseline.
5. Do not refresh, resend, Stop, switch GPT or navigate away.
6. Let official Web recover or fail naturally.
7. Export diagnostics.

Evidence question: after a genuine transport break, does official Web open an official status/resume/handoff/turn-stream/subscription connection that continues the same response without a second Send, or does it only expose failure / eventual history recovery?

Only an exact observed reconnect mechanism may justify a later b46 Native no-resend parity experiment. If no reconnect path appears, record the negative evidence and reassess the architecture ceiling rather than guessing an endpoint.

## Evidence classification

- Code written: Yes
- CI passed: Yes
- Artifact produced: Yes
- Package identity verified: Yes
- Runtime/manual/real-device: **Yes — uninterrupted protocol capture + repeated active-background/lock capture**
- Short active-response WebKit/original-fetch background survival: **Positive on exact recorded scope, up to ~126s continuous interval / ~195s cumulative**
- 5/15-minute hybrid background matrix: **Unknown / Unverified**
- Forced network-failure reconnect behavior: **Unknown / Unverified**
- Native same-response handoff capability: **Unknown / Unverified**
- Stable/Frozen Send: **No**