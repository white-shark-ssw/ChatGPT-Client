# DEV-send-stream

## Status

**Active — exact b82 Runtime remains Partial. Automatic cross-platform final acquisition works, but the current generic Web user-socket exact-conversation trigger is completion-time rather than start-time. The follow-up Human Gate is now resolved Negative: an already-open visible official ChatGPT Web page on the same conversation does not automatically show the remote user turn, active response, or even the completed turn without an explicit page refresh/navigation. Therefore passive official-Web visibility/focus is rejected as the missing early acquisition mechanism. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Exact branch head before this checkpoint write: `7d050c22bf47dfb0a5597b8db92090075450d59a`
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b82 product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- Guarded assembly attempt 2: `33534965707 / 99946924531` — success
- Formal Push CI: `33535342383 / 99948156535` — success
- Formal PR CI: `33535347654 / 99948174293` — success
- Canonical Push Artifact: `9811406038`
- Artifact ZIP SHA-256: `bcb9c65f7cee7680580acd6238d3dd9f03f30b3c5f9024cd251b31690ac13681`
- IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- b39-b82 permanently reserved
- b82 Runtime: **Partial — automatic final acquisition positive / live acquisition timing rejected**
- visible official-Web already-open-A gate: **Negative — no passive cross-device refresh even after completion**
- b83: **not allocated**
- Stable/Frozen Send: No

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b81-device-runtime-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b82-allocation-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b82-build-artifact-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-b82-device-runtime-20260902.md`
- pending this documentation batch: visible-Web negative gate + official-iOS static realtime architecture evidence

## Exact b82 Runtime finding — 2026-09-02

User supplied exact b82 diagnostics `ChatGPTClient-Diagnostics-20260901-175030.json`; metadata confirms Release `0.1.0`, Build82, Candidate `DEV-send-stream-0.1.0-b82`, source marker `c7a274786dfd`, iPhone / iOS17.0.

Observed sequence:

1. 17:48:33Z A is selected and the covered executor begins observing the existing conversation.
2. 17:48:37Z/38Z the `ws.chatgpt.com` user socket is created/opened; 17:48:39Z initial JSON-array frame is `targetMatch=false`.
3. During the long remote turn there is no earlier `websocket_structure message`, no `externalStreamingObserved`, no `externalSnapshot`, and no Repository external live-response start.
4. 17:49:56Z one JSON-array socket frame arrives with exact `targetMatch=true`; b82 immediately starts `externalAcquisitionSync`.
5. 17:49:57Z authoritative Detail returns HTTP200 with visible messages **8 -> 10**, `addedVisibleMessageCount=2`, and `latestUserChanged=true`.
6. The user reports that at this point both the remotely sent user message and the assistant answer appeared, and the assistant answer had already completely generated.
7. b82 then performs its one re-arm. The covered page reloads by 17:49:58Z and opens a new user socket at 17:50:00Z/01Z, but no `externalStreamingObserved`, no external snapshot and no live Repository response follows. This is consistent with the response already being complete before the trigger/re-arm.

The current `CoveredWebSendExecutor` WebSocket probe is injected at document start and records every interesting incoming socket message up to a 200-message budget, including string/JSON/binary shape. Therefore the absence of another incoming frame in this reproduction is meaningful evidence: the current observed user-level `targetMatch=true` frame is not an early request-start signal for this flow.

## Visible official-Web Human Gate result — 2026-09-02

The user tested the same conversation with visible official ChatGPT Web already open before the cross-platform turn.

Result:

- the visible Web page did **not** automatically show the remote user message;
- it did **not** show live reasoning/final progression;
- it still did **not** automatically refresh the conversation after the remote answer had completely finished;
- an explicit refresh/navigation is required before that page reflects the changed conversation.

Classification:

- visible/foreground Web as an earlier acquisition trigger: **Rejected**;
- passive covered-page observation as a route to request-received visibility: **Rejected**;
- the user's hypothesis that a server-side notification may exist but Web does not use it to refresh the current page is **plausible but Unverified**; the Runtime result proves the missing page refresh behavior, not the server's internal notification semantics.

This closes the b82 visible-Web Human Gate. Do not spend another Candidate on visibility/focus simulation unless new direct evidence contradicts this result.

## Current source implication

Current b82 product source confirms `CoveredWebSendExecutor` only **observes** page-owned `stream_status` and plural-conversation requests. It does not create or schedule those reads. Therefore an already-open page that never issues them cannot provide early active-response state through the existing interceptor.

The b82 user-level socket observation remains useful only as currently evidenced: its exact-conversation target match can trigger one bounded authoritative completion/update Sync. It is not message-body authority and is not an evidenced start/live trigger.

## Official iOS static realtime architecture evidence — investigation direction

The user-supplied decrypted official ChatGPT iOS artifact (`com.openai.chat`, `1.2026.202`, build `30140022279`, MinimumOSVersion 17.0) contains stronger static evidence that the native official client has a separate realtime layer rather than depending on passive Web refresh:

- `Conversations/WebSocketConversationObserver.swift`;
- `Conversations/WebSocketConversationEventsService.swift`;
- `Conversations/ConversationPollingManager.swift`;
- `APIClient/WebSocketService.swift` and `APIClient/WebSocketModels.swift`;
- WebSocket command raw strings `connect`, `subscribe`, `presence`;
- topic/event model fields including `topicId`, `offset`, message `id/type/payload/offset`, and topic event cases `catchup` / `live`;
- conversation event/update raw values `conversation-update`, `add-messages`, `title-update`, `set-conversation-async-status`, `async-task-update-message`, `async-task-completed`;
- `ConversationPollingManager` diagnostics including `ios.conversation_polling.is_streaming_message`, `is_waiting_for_server_streaming`, `chat_has_active_async_tasks`, and explicit polling termination reasons.

This is **static architecture evidence only**. It does not yet prove the exact current WebSocket URL acquisition, topic ID, subscribe envelope, auth/cookie/header requirements, offset/cursor semantics, or which event is emitted at remote request start for the user's account. Do not guess those fields from names alone.

## Runtime classification

- Automatic refresh without pressing Sync: **Positive at completion**.
- Remote user-message visibility before answer completion: **Rejected**.
- Automatic acquisition of an active external response: **Rejected for timing**.
- External reasoning/tools/final live stream in b82 reproduction: **Not acquired**.
- `targetMatch=true` user-socket event as a completion/update trigger: **Positive**.
- `targetMatch=true` as request-start/live-stream trigger: **Rejected by b82 reproduction**.
- already-open visible Web passive refresh: **Rejected, including after completion**.
- fake typewriter/synthetic progressive final: **Still prohibited**.

The user's current requirement remains explicit: for a long cross-platform response, Native must show promptly that the request was received and then expose real progressive response state rather than remaining unchanged until completion.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole response/content owner.
- `AuthSessionStore` remains sole native auth/account owner; default persistent WebKit store remains sole persistent auth-secret owner.
- WebSocket content is not promoted into Native user/reasoning/final body authority without separate exact evidence.
- no duplicate Send, resend, fake stream, speculative retry/watchdog/fallback or second response store.

## Current protocol boundary

Passive Web acquisition is now ruled out for the tested flow. The next safe direction is to evidence the official native realtime mechanism before choosing product behavior.

Investigation priority:

1. determine the official native WebSocket URL/config acquisition path;
2. determine the exact conversation topic ID and `connect`/`subscribe` envelope for the current account;
3. determine whether a `conversation-update` / `add-messages` / async-status event arrives near remote request start and what non-body identity it provides;
4. only then decide whether that event can trigger existing authoritative Detail/stream-status/resume acquisition without becoming a second message authority;
5. if no usable realtime start signal can be evidenced, explicitly design a bounded selected-conversation status-monitoring path using the official client's polling evidence as a reference. Do not smuggle fixed polling into the product before that decision is documented.

Current b82 source and the official-app static strings do **not** authorize constructing a guessed subscribe command, guessed topic ID, guessed offset, guessed websocket URL, or guessed auth framing.

## Documentation batch recovery point

This checkpoint write starts a docs-only evidence batch after the visible-Web Human Gate result.

Known baseline before batch:

- formal branch head `7d050c22bf47dfb0a5597b8db92090075450d59a`;
- exact tested product source remains `c7a274786dfd175e8f476fc15c4964840e112a1d`;
- Candidate b82 remains unchanged; b83 is not allocated.

Intended deterministic docs batch:

1. checkpoint this visible-Web negative result and static official-iOS realtime evidence;
2. add one runtime/static evidence document;
3. update `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, and `WEB_SEND_ADAPTER.md` only where current truth changed;
4. update PR #29 summary after durable docs are synchronized;
5. close this recovery point with the resulting formal docs head and exact next action.

Do not touch product/config/version files in this batch and do not allocate b83.

## Session round counter

Conversation round count was explicitly reset by the user. Current work is **round 2**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Complete the docs-only evidence batch, then continue static/protocol investigation of the official native WebSocket conversation-events path. Do not allocate b83 until the exact WebSocket URL/topic/subscribe/auth/offset semantics and an earlier useful event are evidenced, or until the project explicitly chooses a bounded selected-conversation status-monitoring design because no subscribable early signal can be established.
