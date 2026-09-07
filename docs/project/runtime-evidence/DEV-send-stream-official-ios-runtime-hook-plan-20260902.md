# DEV-send-stream — official iOS runtime WebSocket hook plan — 2026-09-02

## Purpose

Record the next evidence path after static inspection of the user-supplied decrypted official ChatGPT iOS package reached the point where protocol structure is visible but dynamic registration/topic values are not fully recoverable from ordinary strings.

This is research/tooling evidence only. It does not allocate b83, does not change product code, and does not authorize redistributing or linking the official ChatGPT framework into ChatGPTClient.

## Whole-package static result

The supplied `ChatGPT_Decrypted.zip` was expanded and the complete `Payload/ChatGPT.app` was searched, not only the main `ChatGPT.framework`.

Confirmed in `ChatGPT.framework/ChatGPT`:

- `WebSocketRegisterResponse` / `websocketURL`;
- `WebSocketTopic(topicId, offset)`;
- `SubscribePayload(topicId, lastOffset, recovered, catchups)`;
- command kinds `connect`, `subscribe`, `presence`;
- topic frame semantics including `catchup`, `live`, `message`, `reply`;
- `conversation-update`;
- `add-messages`;
- conversation async-status/update payload models;
- `WebSocketConversationEventsService`, `WebSocketConversationObserver`, `ConversationPollingManager`.

The complete app package does **not** contain the literal `/backend-api/celsius/ws/user` or JSON spelling `websocket_url` as an ordinary searchable string. The third-party route remains cross-check/hypothesis evidence, not official-package static proof.

This strongly suggests the registration request is supplied through generated API/configuration/closure wiring rather than hard-coded as an ordinary cstring inside `DefaultWebSocketService`.

## Existing research injection path in the supplied package

The supplied package is already modified for TrollStore research and contains:

- `Payload/ChatGPT.app/Frameworks/CydiaSubstrate.framework/CydiaSubstrate`;
- `Payload/ChatGPT.app/Frameworks/CydiaSubstrate.framework/.troll-fools`;
- `Payload/ChatGPT.app/Frameworks/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`.

Mach-O load-command inspection confirms:

- `Payload/ChatGPT.app/Frameworks/Assets.framework/Assets` weak-loads `@rpath/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`;
- that injected dylib has `LC_ID_DYLIB @rpath/ChatGPTEnhancer.dylib`.

Therefore a research-only runtime observer can use the same already-proven injection style instead of attempting to embed the official ChatGPT framework into our product.

## Recommended runtime evidence probe

Build a small research-only injected dylib for the official app. Its job is observation, not protocol ownership.

### Registration observation

Observe URLSession requests and filter only the WebSocket-registration candidate path.

Record only:

- method;
- normalized path;
- HTTP status;
- response JSON key names;
- returned WebSocket host/path shape.

Never record/export:

- Cookie;
- Authorization;
- signed WebSocket query parameters;
- access/session tokens;
- DeviceCheck/Sentinel/challenge values.

### WebSocket connection observation

Observe creation of `NSURLSessionWebSocketTask` / equivalent public URLSession WebSocket transport.

Record only:

- host;
- path;
- whether query parameters are present, without their values;
- open/close/error state.

### Outbound command observation

Observe WebSocket text/data sends and decode only bounded JSON structure.

Capture:

- top-level frame array/object;
- command ID;
- command type (`connect`, `subscribe`, `presence` or unknown);
- command key names;
- topic ID when it is a non-secret symbolic topic;
- offset/last-offset presence and value class;
- presence state token.

Do not capture unrelated message bodies or auth/challenge material.

### Inbound conversation-event observation

Observe WebSocket receive completions and decode only the known topic/conversation envelope structure.

Capture:

- frame type;
- topic ID;
- offset type/value where safe;
- reply vs live/catchup classification;
- `conversation-update` presence;
- exact target-conversation match as a boolean or privacy-safe hash;
- update type (`add-messages`, async-status, stop, etc.);
- update-content key names;
- message count/status metadata only until body authority is separately proven;
- timestamp relative to remote Send start and assistant completion.

Never export prompt/answer/reasoning/tool bodies.

## Decisive Runtime test

1. Install/run the research official-app build on the same iPhone/iOS17 account environment.
2. Keep conversation A available in the official app.
3. Start the observer before the remote turn.
4. From another platform, send one deliberately long text turn to A.
5. Determine which event arrives first and when:
   - registration / base subscribe;
   - conversation-update;
   - add-messages;
   - async-status;
   - per-turn topic subscribe;
   - completion/update notification.
6. Compare event time with remote user-message creation and response completion.

A target-matching event before completion is sufficient to define an early-acquisition trigger. It is **not** automatically sufficient to make WebSocket message bodies authoritative.

## Product integration rule after evidence

Do not borrow/link the official framework in ChatGPTClient.

Preferred production shape after exact evidence:

`AuthSessionStore transient verified context -> our URLSession/URLSessionWebSocketTask -> verified registration + topic subscription -> event trigger -> existing ConversationRepository response/acquisition owner`.

Initially treat conversation WebSocket events as realtime notification/state evidence and continue using the existing authoritative Repository Detail/SSE/resume/plural paths for message/reasoning/final content. Promote WebSocket payload content only if exact Runtime evidence proves completeness, identity, branch semantics and lifecycle ownership.

## Why direct framework reuse is rejected

Directly embedding/calling the official `ChatGPT.framework` would create unsupported coupling to:

- private internal Swift ABI/types;
- official app dependency injection/container state;
- account/workspace services not owned by our app;
- code signing and bundle assumptions;
- version-specific implementation details;
- redistribution/licensing risk;
- a second conversation/auth/response authority.

The official package is therefore an **evidence oracle**, not a product dependency.

## Fallback

If exact native WebSocket subscription cannot be reproduced under our accepted auth boundary, use the official `ConversationPollingManager` evidence to design an explicitly bounded selected-conversation status monitor. Do not add concealed fixed polling before that branch is deliberately specified.

## Evidence classification

- official native realtime architecture: Static Positive;
- full-package literal registration route: Not found / Unverified;
- existing official-package injection path: Static Positive;
- runtime registration URL/topic/envelope: Pending;
- b83: not allocated;
- Stable/Frozen Send: No.
