# DEV-send-stream b45 — Native realtime handoff probe

## Identity

- Candidate: `DEV-send-stream-0.1.0-b45`
- Version / Build: `0.1.0 (45)`
- Exact product/config source: `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`
- Push Run / Job: `33248952646` / `99091176390` — success
- PR Run / Job: `33248954018` / `99091179731` — success
- Push Artifact: `9713774868`
- Artifact ZIP digest: `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`
- IPA: `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`
- IPA SHA-256: `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`
- Package inspection: Candidate b45, `0.1.0 (45)`, source marker `accd7bdf29e4`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.

Evidence classification at creation: **Code / CI / Artifact / package identity passed. Runtime handoff behavior pending. Stable/Frozen Send No.**

## Question being tested

Can official ChatGPT Web perform the required protected Send while Native subsequently attaches/resumes/subscribes to the **same already-started response** without issuing another Send?

Desired architecture if supported:

`Native composer/history/presentation -> user-visible official Web legal Send -> Native no-resend realtime continuation -> Native reasoning/final presentation -> Native-owned background lifecycle`

This is not yet established.

## Why this probe exists

b42 proved that successful ChatGPT-account Send on the tested account requires browser-owned anti-abuse challenge output. b43 proved visible official Web Send can be responsive enough. b44 proved that leaving Web as the realtime-response owner and then reconciling Native Detail is product-poor and eventually consistent: assistant output already visible in Web could remain absent from immediate Native Sync until later.

b40 also observed early `resume_conversation_token` in the original Send SSE. Its role as a true response-continuation credential/identity remained Unknown / Unverified. b45 therefore measures official-page continuation behavior before any Native replay is attempted.

## Probe behavior

b45 adds `ProtocolHandoffProbeViewController`, exposed in Settings as `实时接管协议探测（诊断）`.

Observation-only instrumentation covers:

- original `POST /backend-api/f/conversation` SSE;
- structural presence/value-shape only for `resume_conversation_token`, `response_id`, `turn_id`, `conversation_id`, `message_id`, `async_task_id`/task identity;
- official-page same-origin fetch/XHR/EventSource/WebSocket connections opened after Send;
- route classes for `/conversation/<id>/stream_status`, turn-stream, handoff, resume, subscribe, continuation and similar backend paths;
- method, transport, sanitized path class, response status/content type, header **names only**, query **names only**, structural JSON shape and identity shape;
- continuation-like events naturally received by a later official-page connection.

The probe does not create or replay a continuation request.

## Privacy / security boundary

Never record/export:

- prompt text;
- assistant/final answer text;
- reasoning text;
- raw request/response bodies;
- raw conversation/message/response/turn/resume IDs or token values;
- Cookie or Authorization values;
- Sentinel/Turnstile/PoW/conduit values.

Never use this probe to implement:

- PoW/Turnstile/Sentinel bypass;
- captured proof/token replay;
- hidden/shadow WebView Send;
- Native composer injection into a covered/hidden Web composer;
- synthetic hidden Send clicks;
- DOM answer/reasoning scraping.

## Runtime matrix

Primary authority: iPhone 15 Pro Max / iOS17.0 TrollStore runtime.

1. Clear diagnostics if practical.
2. Open Settings -> `实时接管协议探测（诊断）`.
3. Use default ChatGPT / primary assistant, not custom GPT/Gizmo.
4. New chat: send one prompt long enough to expose noticeable reasoning/stream behavior; let it run normally without refresh.
5. Existing chat: if practical, send one additional prompt and let it run normally.
6. Export diagnostics JSON.

## Interpretation

Positive evidence requires a naturally observed official-page same-response continuation mechanism after the original Send, with enough structural route/identity evidence to justify a later **Native no-resend parity** experiment.

Absence of a follow-up continuation path is not permission to guess one. If ordinary ChatGPT keeps the entire live response only on the original `/f/conversation` SSE, record that negative evidence and reassess the architecture ceiling.

Background/WebKit true-background and polished hybrid UI work remain downstream of this handoff result. If Native can own the response stream, background preservation should protect the Native response lifecycle instead of WebKit.
