# DEV-send-stream — visible-Web negative gate + official-iOS realtime static evidence — 2026-09-02

## Scope

This document records two pieces of evidence that supersede the b82 next-gate hypothesis:

1. the user's direct visible official-Web cross-platform Runtime result;
2. static inspection of the user-supplied decrypted ChatGPT iOS app bundle for native realtime architecture clues.

No product Candidate is allocated by this document. Exact b82 product identity remains unchanged.

## 1. Visible official-Web Runtime result

Test condition supplied by the user:

- official ChatGPT Web was already open on the same target conversation before a remote cross-platform turn;
- the remote turn was allowed to complete;
- the page was observed without relying on Native Sync as the update mechanism.

Observed result:

- the remote user message did not automatically appear in the already-open Web conversation;
- active reasoning/final generation did not automatically appear;
- even after the remote assistant answer had completely finished, the already-open Web conversation still did not automatically refresh to show the completed turn;
- explicit refresh/navigation is required for the page to reflect the new conversation state.

### Classification

- visible/foreground official Web as an earlier live-acquisition source: **Runtime Rejected**;
- passive official-page observation as a request-start mechanism: **Runtime Rejected**;
- passive official-page observation as even a guaranteed completion refresh mechanism: **Runtime Rejected for this test**.

The user's explanation that the server may send some notification while the Web UI simply does not act on it is plausible, but remains **Unverified**. The Runtime evidence proves the page behavior, not the server's internal notification semantics.

This result means another Candidate must not be spent on visibility/focus simulation unless new direct evidence contradicts this reproduction.

## 2. Current b82 source implication

Current b82 `CoveredWebSendExecutor` observes page-owned network activity:

- matching page-owned `stream_status` reads;
- matching page-owned plural-conversation reads;
- matching page-owned resume responses;
- user-level WebSocket structure.

For external continuation, the bridge only consumes `stream_status` / plural reads when the official page itself issues them. It does not schedule those reads.

Therefore the visible-Web Runtime result explains the current passive observation failure without requiring a new hypothesis: if the official page remains idle and never issues those reads, the interceptor has no early active-response source to consume.

The b82 user socket exact-conversation `targetMatch=true` event remains accepted only as a completion/update hint for the tested flow. It is not body authority and is not an evidenced request-start/live-stream signal.

## 3. User-supplied official iOS artifact identity

Static inspection target:

- bundle ID: `com.openai.chat`;
- `CFBundleShortVersionString`: `1.2026.202`;
- `CFBundleVersion`: `30140022279`;
- `MinimumOSVersion`: `17.0`;
- inspected main framework binary: `Payload/ChatGPT.app/Frameworks/ChatGPT.framework/ChatGPT`.

The supplied app bundle also contains an injected `ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`, so the overall package is not treated as a pristine App Store artifact. The realtime strings and Swift reflection fields below were taken from the large `ChatGPT.framework/ChatGPT` main framework binary and are treated as **static binary evidence**, not Runtime proof.

## 4. Native realtime architecture strings

The official framework contains explicit source/type strings:

- `Conversations/WebSocketConversationObserver.swift`;
- `Conversations/WebSocketConversationEventsService.swift`;
- `Conversations/ConversationPollingManager.swift`;
- `Conversations/WebSocketConfiguration.swift`;
- `APIClient/WebSocketService.swift`;
- `APIClient/WebSocketModels.swift`.

It also contains startup/storage names indicating the WebSocket conversation service is a distinct account/workspace service rather than a Web page renderer:

- `startWebSocketServiceTask`;
- `startWebSocketConversationEventsServiceTask`;
- `webSocketConversationEventsService`;
- `conversationPollingManager`.

Static inference supported by these names: the native official client has dedicated realtime/polling infrastructure. Exact service behavior still requires protocol/Runtime evidence.

## 5. WebSocket service model evidence

Swift reflection metadata in the official framework exposes the following WebSocket model/state field shapes:

### Topic

A topic model contains:

- `topicId`;
- `offset`.

A topic message model contains:

- `id`;
- `type`;
- `payload`;
- `offset`.

The topic event enum exposes raw cases:

- `catchup`;
- `live`.

### Service

The default WebSocket service stores fields including:

- `registerWebSocket`;
- `connection`;
- `topicSubjects`;
- `sendData`;
- `nextCommandID`;
- `hasSentConnectCommand`;
- `activeSubscriptions`;
- `presenceState`;
- `webSocketPresenceEnabled`;
- `makeWebSocket`;
- application-state observation.

The binary contains WebSocket command raw strings:

- `connect`;
- `subscribe`;
- `presence`.

Diagnostics include:

- `Failed to send web socket subscribe command for topic:`;
- `Failed to send web socket connect command`;
- `Failed to send web socket presence command`;
- `Unknown WebSocket topic frame type:`;
- `Failed to decode WebSocket topic message type`.

A registration/config response model contains `websocketURL`.

### Evidence boundary

This establishes the existence of a topic-based WebSocket protocol with offsets and live/catchup semantics in the official iOS client. It does **not** establish:

- the endpoint that returns `websocketURL`;
- the exact WebSocket URL for the user's current account;
- exact connect/subscribe JSON envelope shape;
- exact topic ID used for conversation updates;
- exact offset/cursor acquisition and reconnect rules;
- auth/cookie/account headers required;
- whether the same endpoint/protocol is available to this third-party client under the current accepted auth boundary.

Those values must not be guessed from the field names.

## 6. Conversation WebSocket event model evidence

The official framework exposes `WebSocketConversationEvent`, `ConversationUpdate`, `KnownUpdateType`, and update-content types including:

- `AddMessagesUpdateContent`;
- `AsyncTaskMessageUpdate`;
- `AsyncTaskCompletedUpdate`;
- `TitleUpdateContent`;
- `AsyncStatusUpdate`;
- `StopUpdateContent`.

Raw update/event strings include:

- `conversation-update`;
- `add-messages`;
- `title-update`;
- `set-conversation-async-status`;
- `async-task-update-message`;
- `async-task-completed`.

Conversation-update model field names include:

- `conversationId`;
- `updateType`;
- `updateContent`.

`WebSocketConversationObserver` static diagnostics include:

- `Failed to refresh conversation after web socket reconnected`;
- `Failed fetching conversation`;
- recovery/merge diagnostics after WebSocket reconnection.

### Working implication

This is substantially stronger evidence than the Web page's generic user-socket completion hint: the official iOS app contains a conversation-specific WebSocket update layer with explicit conversation identity and message/async-status update classes.

However, static names do not prove which event arrives first for a cross-platform text turn or whether `add-messages` contains authoritative full message data versus an update hint. Product code must not promote these static names directly into message authority.

## 7. Official conversation polling evidence

`ConversationPollingManager` contains explicit guards and finish diagnostics:

- `ConversationPollingManager must be started before polling`;
- `Attempted to poll a conversation with active tasks or streams`;
- `ios.conversation_polling.polling_task_already_exists`;
- `ios.conversation_polling.is_streaming_message`;
- `ios.conversation_polling.chat_has_active_async_tasks`;
- `ios.conversation_polling.is_waiting_for_server_streaming`;
- `Conversation async status changed from ...`;
- `Conversation is streaming messages, stopping polling for conversation:`;
- `Conversation has async tasks, stopping polling for conversation:`;
- `Maximum polling time reached, stopping polling for conversation:`;
- `Polling timed out`;
- `polling_finish_reason`.

### Working implication

The official native client has a bounded, state-aware conversation polling mechanism in addition to the WebSocket event layer. This supports keeping a bounded selected-conversation status-monitoring design as a legitimate fallback direction **if** the exact WebSocket subscription path cannot be evidenced.

It does not authorize copying an unknown polling cadence or adding a hidden fixed timer now. Exact trigger, endpoint, cadence/termination and authority semantics remain unknown.

## 8. Current investigation decision

Order of investigation is now:

1. evidence the official native `websocketURL` acquisition path;
2. evidence the exact conversation topic ID and connect/subscribe envelope;
3. evidence auth/account binding and offset/catchup/live semantics;
4. determine whether a conversation update appears near remote request start and what exact non-body identity/status it supplies;
5. if an early event exists, use it only to activate the existing authoritative Repository acquisition path unless exact evidence separately authorizes message content;
6. if an early subscribable signal cannot be established, explicitly design a bounded selected-conversation status monitor using the official polling architecture as reference.

No b83 product Candidate is allocated yet.

## Prohibited shortcuts retained

Do not:

- guess the topic ID;
- guess the websocket URL or config route;
- guess offset/cursor semantics;
- replay guessed connect/subscribe payloads;
- promote generic WebSocket payload bodies to Native message authority;
- add fixed polling/timers/watchdogs as a concealed workaround;
- synthesize remote user/final rows;
- fake progressive final text;
- create a second conversation/response store.

`ConversationRepository` remains the sole Native conversation/response authority.
