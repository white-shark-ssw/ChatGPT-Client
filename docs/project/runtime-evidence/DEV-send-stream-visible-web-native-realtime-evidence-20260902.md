# DEV-send-stream — visible-Web negative gate + official-iOS realtime evidence — 2026-09-02

## Scope

This document records the evidence that supersedes the b82 passive-Web acquisition hypothesis:

1. direct visible official-Web Runtime behavior;
2. static inspection of the supplied decrypted official ChatGPT iOS package;
3. whole-package static-search limits;
4. the research-only runtime observation path now justified by the package's existing injection setup.

No product Candidate is allocated by this document. Exact b82 product identity remains unchanged.

## Visible official-Web Runtime result

The user kept official ChatGPT Web already open on the same target conversation before a remote cross-platform turn.

Observed:

- remote user message did not automatically appear;
- active reasoning/final did not automatically appear;
- even after the remote answer completed, the open Web conversation still did not refresh until explicit refresh/navigation.

Classification:

- visible/foreground Web as earlier live source: **Runtime Rejected**;
- passive Web as request-start trigger: **Runtime Rejected**;
- passive Web as guaranteed completion refresh: **Runtime Rejected for this flow**.

The hypothesis that the server emits a notification which the Web page simply does not use is plausible but Unverified. Runtime proves page behavior, not server internals.

## b82 source implication

b82 observes page-owned `stream_status`, plural-conversation and resume activity; it does not schedule those reads. An idle page therefore supplies no early active-response state through the current interceptor.

The b82 generic user-socket exact-conversation `targetMatch=true` event remains accepted only as a completion/update hint in the tested flow. It is not body authority and is not an evidenced request-start/live-stream signal.

## Supplied official iOS artifact

Static inspection target:

- bundle ID `com.openai.chat`;
- version `1.2026.202`;
- build `30140022279`;
- MinimumOSVersion `17.0`;
- main framework `Payload/ChatGPT.app/Frameworks/ChatGPT.framework/ChatGPT`.

The supplied package is a TrollStore/research-modified package and includes an injected enhancer, so evidence is classified as static binary evidence, not pristine App Store package proof.

## Native realtime architecture

The official framework contains source/type evidence for:

- `Conversations/WebSocketConfiguration.swift`;
- `Conversations/WebSocketConversationObserver.swift`;
- `Conversations/WebSocketConversationEventsService.swift`;
- `Conversations/ConversationPollingManager.swift`;
- `APIClient/WebSocketService.swift`;
- `APIClient/WebSocketModels.swift`.

Reflection/model evidence includes:

- `WebSocketRegisterResponse.websocketURL`;
- `WebSocketTopic(topicId, offset)`;
- topic events `catchup` / `live`;
- frame kinds `message` / `reply` / `unknown`;
- `SubscribePayload(topicId, lastOffset, recovered, catchups)`;
- commands `connect`, `subscribe`, `presence`;
- `DefaultWebSocketConversationEventsService` scoped by account/workspace dependencies;
- `WebSocketConversationObserver`;
- `WebSocketConversationEvent.conversationUpdate`;
- known update types `addMessages`, `titleUpdate`, `setConversationAsyncStatus`, `asyncTaskUpdateMessage`, `asyncTaskCompleted`, `stop`;
- concrete payload fields including `messages`, `message`, `title`, `conversationAsyncStatus`, `runId`.

Raw strings include `conversation-update`, `add-messages`, `title-update`, `set-conversation-async-status`, `async-task-update-message`, `async-task-completed`.

This is strong evidence that official iOS owns a separate native realtime conversation-update layer instead of depending on passive Web refresh.

## Official polling evidence

`ConversationPollingManager` exposes bounded/state-aware guards and terminal reasons including:

- polling task already exists;
- conversation is streaming messages;
- chat has active async tasks;
- waiting for server streaming;
- async status changed;
- maximum polling time reached;
- polling timed out.

This supports a deliberately bounded selected-conversation status-monitor design only if native realtime subscription cannot be reproduced. It does not authorize hidden fixed polling now.

## Whole-package static-search limit

The complete extracted `Payload/ChatGPT.app` was searched, not only `ChatGPT.framework`.

Neither the literal path `/backend-api/celsius/ws/user` nor JSON spelling `websocket_url` exists as an ordinary searchable string in the supplied package.

Therefore the third-party report of that route remains cross-check/hypothesis evidence only. The static result is consistent with the registration call being supplied through generated API/configuration/closure wiring rather than a simple hard-coded cstring in `DefaultWebSocketService`.

Do not treat absence of the literal as evidence that the route is false; equally, do not promote the third-party path into product code without direct current-account evidence.

## Existing official-package injection path

The supplied package already contains:

- `Frameworks/CydiaSubstrate.framework/CydiaSubstrate`;
- `Frameworks/CydiaSubstrate.framework/.troll-fools`;
- `Frameworks/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`.

Mach-O load-command inspection confirms `Frameworks/Assets.framework/Assets` weak-loads `@rpath/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`.

This gives a concrete research path: build a small observation-only injected dylib for the official app and let the official implementation reveal its actual current registration request, connect/subscribe frames and conversation-update timing.

## External cross-check — hypothesis only

A current third-party implementation (`tianya518/gptclient-go`, `sentinel/chat_ws.go`, inspected 2026-09-02) independently reports:

- `GET /backend-api/celsius/ws/user` -> `websocket_url`;
- `connect` plus `subscribe` command envelopes;
- base topics including `conversations`;
- `conversation-update` frames;
- per-turn topic subscriptions with offsets.

This aligns well with the official static model names but remains **Hypothesis / cross-check evidence only**.

## Runtime observation plan

Use the official app as an evidence oracle, not a product dependency.

A research observer should capture only privacy-safe structure:

### Registration

- request method;
- normalized path;
- HTTP status;
- response JSON key names;
- returned WebSocket host/path shape.

Never capture the signed URL query, Cookie, Authorization, tokens or anti-abuse/challenge material.

### Outbound WebSocket

Capture only:

- array/object envelope shape;
- command ID;
- command type;
- key names;
- non-secret symbolic topic ID;
- offset/last-offset presence/value class;
- presence state.

### Inbound WebSocket

Capture only:

- frame type;
- topic ID;
- offset/catchup/live/reply classification;
- target-conversation match as boolean/privacy-safe marker;
- update type;
- update-content key names and counts;
- timing relative to remote Send and completion.

Do not export prompt/answer/reasoning/tool bodies.

## Product integration decision

Do **not** embed, link, call or redistribute official `ChatGPT.framework` inside ChatGPTClient.

Reasons:

- private internal Swift ABI and DI/container dependencies;
- code-signing/bundle assumptions;
- brittle version coupling;
- redistribution/licensing risk;
- risk of creating a second auth/conversation/response authority.

Preferred production path after exact evidence:

`AuthSessionStore verified transient context -> our URLSession / URLSessionWebSocketTask -> verified registration + topic subscription -> realtime event -> existing ConversationRepository acquisition/response owner`.

Initially treat WebSocket conversation events as notification/state evidence. Continue using the existing authoritative Detail/SSE/resume/plural paths for message/reasoning/final bodies until exact Runtime evidence proves WebSocket payload completeness, identity, branch and lifecycle semantics.

## Next gate

Run one official-app research observation during a long cross-platform turn and determine:

1. exact registration path/status/key shape;
2. exact connect/subscribe serialized structure;
3. base conversation topic;
4. initial/reconnect offset/catchup behavior;
5. first exact target-matching event and its update type;
6. whether that event arrives before the assistant finishes.

A positive early event can define the minimal b83 acquisition scope. If native topic subscription cannot be reproduced under our accepted auth boundary, deliberately specify the bounded polling branch using official polling evidence.

## Prohibited shortcuts

Do not:

- borrow/link official framework as product code;
- guess the topic/URL/auth/cursor in product code;
- promote WebSocket bodies directly into Native message authority before proof;
- add fixed hidden polling/timers/watchdogs;
- synthesize remote user/final rows;
- fake progressive final text;
- create a second conversation/response store.

`ConversationRepository` remains the sole Native conversation/response authority.
