# DEV-send-stream — official iOS Probe v0.1 Runtime / v0.2 observation expansion — 2026-09-04

## Input identity

- User-exported file: `ChatGPTRealtimeProbe.jsonl`
- SHA-256: `c74a66702bd670f81a393afea1c306d2a0cce415961c9fe11be15589eeb83093`
- Size: 7,166 bytes
- Parsed JSONL events: 29
- Parse errors: 0
- Probe version in file: `0.1`
- Bundle ID: `com.openai.chat`

This is Human Runtime evidence from the research-modified official iOS package. It is not ChatGPTClient product Runtime and does not allocate b96.

## Runtime result

The Probe loaded and installed four hooks. It observed a real official `NSURLSessionWebSocketTask` to `ws.chatgpt.com` under the privacy-sensitive user-socket route family with one query item.

Initial outbound frames contained `connect` with presence `foreground`, subscribe `app_notifications`, subscribe `calpico-chatgpt`, and subscribe `push_auth_challenge` with a string offset. All four received reply frames. Later presence commands also received reply frames.

At `2026-09-03T17:49:18.799Z` and `.810Z`, receive returned `NSPOSIXErrorDomain / 53`. At `17:49:20.010Z` the official app created a new user WebSocket and repeated the same connect + three base subscriptions. Therefore official user-socket reconnect behavior is Runtime Positive for this sample.

Across the complete file there is **no** observed conversation-specific/per-turn topic subscription, target `conversationHash` frame, `conversation-update`, `add-messages`, async-status update, or catchup/live target event.

Classification: **Negative for the simple hypothesis that this captured official user WebSocket directly exposed the target late-join response through an observed conversation/per-turn subscription in this sample. Inconclusive for the overall official late-join mechanism.**

## Probe v0.1 blind spot

The v0.1 HTTP hooks logged only paths containing celsius/websocket/ws. They ignored ordinary conversation Detail, plural conversations, `stream_status`, `/f/conversation/resume`, protected conversation routes, and delegate-based HTTP/SSE response lifecycle. Therefore this file cannot distinguish between late-join acquisition through ordinary HTTP/Detail/status/resume/SSE plus the base user socket, a conversation-specific transport implemented through a URLSession delegate path that v0.1 did not report, or another official mechanism outside the current observation surface.

The user-visible exact moment/condition of late-join is also not encoded in the JSONL, so this evidence cannot claim that the official UI visibly joined at a particular log timestamp.

## Privacy correction

v0.1 `RPTURLShape` recorded the raw WebSocket path. In the supplied file that path contains an opaque user-specific segment. Do not repeat or promote that segment into durable docs/product logic. Probe v0.2 replaces raw path logging with a privacy-safe shape that redacts opaque path components and hashes known conversation IDs only for correlation.

## Probe v0.2 authorized research delta

Research tooling only: redact opaque URL path components; observe privacy-safe conversation/realtime HTTP request path kind/shape/method; record response status/MIME/body-size/JSON key names where available without body text or headers; hash known conversation IDs from URL/body for correlation; hook URLSession delegate response/completion methods so streaming response start/end is observable; retain WebSocket structural observation; record direct presence command state; add an in-app `清空` control with confirmation and a fresh `probe.log_cleared` marker.

Do not log Cookie/Authorization/signed query values/prompt/answer/reasoning/tool text. Do not modify ChatGPTClient product code or allocate b96 from this result.

## Next decisive Runtime

Use the v0.2 official research package. Clear the log immediately before the test, reproduce the known cross-platform late-join flow, then export JSONL after the answer finishes or after the late-join mechanism is visibly established. Decisive evidence is the earliest target-correlated acquisition path before terminal: conversation Detail/status/resume/SSE response, conversation/per-turn WebSocket subscribe/update, or another newly observed official route. Product implementation remains blocked until that current-account path is evidenced.
