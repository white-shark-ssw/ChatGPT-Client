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

- `Conversations/WebSocketConfiguration.swift`;
- `Conversations/WebSocketConversationObserver.swift`;
- `Conversations/WebSocketConversationEventsService.swift`;
- `Conversations/ConversationPollingManager.swift`;
- `APIClient/WebSocketService.swift`;
- `APIClient/WebSocketModels.swift`.

It also contains startup/storage names indicating the WebSocket conversation service is a distinct account/workspace service rather than a Web page renderer:

- `startWebSocketServiceTask`;
- `startWebSocketConversationEventsServiceTask`;
- `webSocketConversationEventsService`;
- `conversationPollingManager`.

Swift reflection further shows:

- `DefaultWebSocketConversationEventsService` fields: `accountID`, event subject, lazy WebSocket service, WebSocket events task, bag, injected dependencies;
- its injected/provider dependencies include `userWorkspaceID`;
- `WebSocketConversationObserver` fields include `accountID`, `conversationCoordinator`, `conversationService`, `webSocketService`, `eventStream`, application-state observation and live-activity service.

Static inference supported by these names: the native official client has dedicated account/workspace-scoped realtime/polling infrastructure. Exact service behavior still requires protocol/Runtime evidence.

## 5. WebSocket service model evidence

Swift reflection metadata in the official framework exposes the following exact type/field shapes.

### Topic

`APIClient.WebSocketTopic` contains:

- `topicId`;
- `offset`.

`APIClient.WebSocketTopic.Event` has cases:

- `catchup`;
- `live`.

`APIClient.WebSocketTopic.Frame` has cases:

- `message`;
- `reply`;
- `unknown`.

`APIClient.WebSocketTopic.Frame.MessageEnvelope` contains:

- `topicId`;
- `payload`;
- `offset`.

`APIClient.WebSocketTopic.Frame.SubscribePayload` contains stored fields:

- `topicId`;
- `lastOffset`;
- `recovered`;
- backing `_catchups`.

Its CodingKeys are:

- `topicId`;
- `lastOffset`;
- `recovered`;
- `catchups`.

`APIClient.WebSocketTopic.Frame.Reply.Payload` supports:

- `subscribe`;
- `connect`;
- `presence`;
- `unknown`.

### Commands / service

`APIClient.WebSocketTopic.Command` has cases:

- `connect`;
- `subscribe`;
- `presence`.

`APIClient.WebSocketTopic.CommandEnvelope` contains:

- `id`;
- `command`.

`APIClient.DefaultWebSocketService` stores fields including:

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

`APIClient.WebSocketRegisterResponse` contains `websocketURL`.

### Evidence boundary

This establishes a topic-based WebSocket protocol with connection registration, subscribe commands, offsets, catch-up and live frames in the official iOS client. It does **not** establish:

- the endpoint that returns `websocketURL`;
- the exact WebSocket URL for the user's current account;
- exact serialized connect/subscribe envelope bytes;
- exact topic ID used for conversation updates;
- exact initial `lastOffset` / recovery / catchup rules;
- auth/cookie/account headers required;
- whether the same endpoint/protocol is available to this third-party client under the current accepted auth boundary.

Those values must not be guessed from the field names.

## 6. Conversation WebSocket event model evidence

Exact Swift reflection names establish the following hierarchy:

- `ConversationsInterface.WebSocketConversationEvent` with case `conversationUpdate`;
- `WebSocketConversationEvent.KnownType` with `conversationUpdate`;
- `WebSocketConversationEvent.ConversationUpdate`;
- `ConversationUpdate.KnownUpdateType`;
- `ConversationUpdate.Content` and concrete update-content models.

### Conversation update structure

`ConversationsInterface.WebSocketConversationEvent.ConversationUpdate` stores:

- `conversationId`;
- `content`.

Its CodingKeys are:

- `conversationId`;
- `updateType`;
- `content`.

`ConversationUpdate.KnownUpdateType` contains:

- `addMessages`;
- `titleUpdate`;
- `setConversationAsyncStatus`;
- `asyncTaskUpdateMessage`;
- `asyncTaskCompleted`;
- `stop`.

`ConversationUpdate.Content` contains:

- `addMessages`;
- `titleUpdate`;
- `stop`;
- `setAsyncStatus`;
- `asyncTaskUpdateMessage`;
- `asyncTaskCompleted`;
- `unknown`.

Concrete payloads include:

- `AddMessagesUpdateContent` -> CodingKey `messages`;
- `AsyncTaskMessageUpdate` -> `message`;
- `AsyncTaskCompletedUpdate` -> `message`;
- `TitleUpdateContent` -> `title`;
- `AsyncStatusUpdate` -> `conversationAsyncStatus`;
- `StopUpdateContent` -> `runId`.

Raw event/update strings in the binary include:

- `conversation-update`;
- `add-messages`;
- `title-update`;
- `set-conversation-async-status`;
- `async-task-update-message`;
- `async-task-completed`.

`WebSocketConversationObserver` static diagnostics include:

- `Failed to refresh conversation after web socket reconnected`;
- `Failed fetching conversation`;
- recovery/merge diagnostics after WebSocket reconnection.

### Working implication

This is substantially stronger evidence than the Web page's generic user-socket completion hint: the official iOS app contains a conversation-specific WebSocket update layer with explicit conversation identity and message/async-status update models.

The `add-messages` payload model statically contains `messages`, but static type information alone does not establish delivery timing, completeness, branch semantics, authorization boundary, or whether these WebSocket message objects can safely replace current Repository Detail/SSE authority. Product code must not promote the payload directly into message authority until exact Runtime/protocol evidence establishes that contract.

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

Static reflection also shows `ConversationPollingManager` owns account ID, conversation coordinator/repository/clock dependencies, start state, initial backend-streaming snapshot state, turn-exchange reload tracker and per-conversation `pollingTasks`.

### Working implication

The official native client has a bounded, state-aware conversation polling mechanism in addition to the WebSocket event layer. This supports keeping a bounded selected-conversation status-monitoring design as a legitimate fallback direction **if** the exact WebSocket subscription path cannot be evidenced.

It does not authorize copying an unknown polling cadence or adding a hidden fixed timer now. Exact trigger, endpoint, cadence/termination and authority semantics remain unknown.

## 8. External cross-check — hypothesis only

A current third-party open-source implementation independently reports a protocol shape that strongly overlaps the official-iOS static models:

- `GET /backend-api/celsius/ws/user` -> JSON `websocket_url`;
- WebSocket command envelope containing `connect` and `subscribe`;
- base topics including `conversations`;
- conversation event type `conversation-update`;
- per-turn topic subscriptions with offsets.

Source: `tianya518/gptclient-go`, `sentinel/chat_ws.go`, inspected 2026-09-02. This source is **Hypothesis / cross-check evidence only**, not current product authority. Its value is that these route/topic names are now narrow candidates for direct verification in the existing Web Rule Lab.

## 9. Current investigation decision

Order of investigation is now:

1. verify the WebSocket registration route and URL shape on the current logged-in account;
2. verify the exact conversation topic ID and serialized connect/subscribe behavior;
3. verify auth/account/workspace binding and offset/catchup/live semantics;
4. determine whether `conversation-update`, `add-messages` or async-status events appear near remote request start and what exact identity/status/content they supply;
5. if an early event exists, initially use it only to activate/reconcile through the existing authoritative Repository path unless exact evidence separately authorizes WebSocket message content;
6. if an early subscribable signal cannot be established, explicitly design a bounded selected-conversation status monitor using the official polling architecture as reference.

No b83 product Candidate is allocated yet.

## 10. Next Human protocol gate

Use the existing Web Rule Lab with the same `.default()` logged-in WebKit store. Run a bounded, read-only protocol probe that:

- does not send a chat message from the Lab;
- does not alter conversation state;
- never outputs full signed WebSocket URLs, query parameters, Cookie, Authorization or challenge values;
- tests the hypothesized registration route and returns only HTTP status / JSON keys / WebSocket host+path shape;
- opens one diagnostic socket if registration succeeds;
- sends only `connect` / `subscribe` control frames;
- tests the `conversations` topic as a hypothesis;
- records only bounded structural frame information and whether a frame's `conversation_id` matches the already-open target conversation;
- during the observation window, the user sends one long turn from another platform.

The decisive result is whether an exact target-matching conversation event arrives **before** the assistant finishes. If yes, inspect its update type/timing and use it as the next evidence source. If no, the WebSocket-start hypothesis is rejected for this account/flow and the official polling architecture becomes the next explicit design branch.

## Prohibited shortcuts retained

Do not:

- guess the topic ID in product code;
- guess the websocket URL or config route in product code;
- guess offset/cursor/recovery semantics;
- promote generic WebSocket payload bodies to Native message authority;
- add fixed polling/timers/watchdogs as a concealed workaround;
- synthesize remote user/final rows;
- fake progressive final text;
- create a second conversation/response store.

`ConversationRepository` remains the sole Native conversation/response authority.
