# DEV-send-stream — official iOS Probe v0.4 Native Detail polling — 2026-09-04

## Human Runtime input

- File: `ChatGPTRealtimeProbe(3).jsonl`
- SHA-256: `cd2b1693a423a37504d96e410c97c04a7987e76283c6458b90ff2db17dc09bd5`
- Size: 58,776 bytes
- Events: 185
- Parse errors: 0
- Probe version: `0.4` for all events
- First event: `probe.log_cleared`

## Key Runtime timeline

The strongest recurring target is conversation hash `0df178903e95`.

At `19:30:46.207Z` the official user WebSocket sent background presence and failed with `NSPOSIXErrorDomain/53`. At `19:30:48.034Z` it sent foreground presence and failed again with the same error. Despite that WebSocket failure, task-level HTTPS observation then captured:

- `19:30:48.044Z` — `GET /backend-api/conversation/<id>`
- `19:30:57.378Z` — same target Detail GET (`+9.334s`)
- `19:31:07.526Z` — same target Detail GET (`+10.148s`)
- `19:31:17.369Z` — same target Detail GET (`+9.843s`)
- `19:31:26.920Z` — same target Detail GET (`+9.551s`)

Median interval is ~`9.697s`. All are `__NSCFLocalDataTask`, explaining why Probe v0.3 public constructor/delegate coverage did not reveal them.

A later process/probe reload begins at `19:31:32.869Z`. After the new launch, Detail fetches occur on conversation selection/foreground but the same continuous ~10s run is not present in the remainder of this exported sample.

## Human visual observation after v0.4 review

The user does not remember whether the exact `19:30:48–19:31:27Z` polling window was the same visible advancement interval, so no exact timestamp/UI correlation is claimed. However, the user independently recalls that official iOS cross-platform continuation does **not** look character-by-character/SSE-like; it appears **batched/chunked**, with a larger block of new content appearing at once. Treat this as qualitative Human Runtime support for periodic authoritative Detail refresh rather than direct token streaming, not as proof of the exact polling cadence.

## Static correlation

The exact supplied official ChatGPT framework contains:

- `ChatGPTConversation/TriggerAsyncStatusPollingConversationObserver.swift`
- `ConversationPollingManager`
- `poll(conversationID:file:line:function:)`
- `Starting polling for conversation:`
- `Conversation async status ... is no longer streaming, stopping polling for conversation:`
- `Conversation async status changed from`
- `Polling stopped while conversation was still backend streaming`
- `backend_streaming_completed`
- `default_interval`
- `model_slug_intervals`
- `conversation_async_status`
- `KnownConversationAsyncStatus`
- `IS_STREAMING`
- `COMPLETE`

`conversation_async_status`, `KnownConversationAsyncStatus`, `IS_STREAMING`, and `COMPLETE` occur together in the official `ConversationsCore/ConversationModels.swift` string region. Combined with the polling-manager stop/change diagnostics, this is strong static evidence that authoritative Conversation Detail carries an active/terminal async-status contract. It still does not prove the exact current-account Runtime response value sequence until a real Detail response is structurally observed.

This static evidence and the Runtime cadence strongly align with a Native polling manager that refreshes authoritative Conversation Detail while backend streaming is active.

## Important exclusion: `/f/conversation/prepare`

Probe v0.4 also records many `POST /backend-api/f/conversation/prepare` tasks. These must not be treated as continuation polling. The official binary independently maps prepare traffic to `MessageInputPrepareConversationViewModel`, `prepareConversation(...)`, `chatgpt-ios-prepare-debounce-period`, `clientPrepareDispatch`, and `clientPrepareSource`: it is composer/send preparation.

## Classification

- Probe v0.4 task-resume observer: **Runtime Positive**.
- Native target Conversation Detail polling: **Runtime observed / strongly correlated with official ConversationPollingManager**.
- Official iOS batched/chunked visual continuation: **qualitative Human Runtime support** for periodic Detail refresh; exact timestamp correlation Unverified.
- Ordinary user WebSocket as the conversation late-join content path: **not supported by this sample**; its presence sends fail while HTTPS polling continues.
- `conversation/{id}/stream_status`: **not observed in this sample**.
- `/f/conversation/resume`: **not observed in this sample**.
- Exact Detail response `conversation_async_status` sequence, response evolution, polling start/stop predicate, and exact visible-UI correlation for the measured time window: **Unverified from JSONL alone**.

## Product implication

Current `ConversationRepository` already owns an authoritative `GET /backend-api/conversation/{id}` and projects Detail content from `mapping/current_node`; it does not currently parse top-level `conversation_async_status`. This points toward preserving the existing Native content authority and adding only evidence-backed active/terminal polling state later, rather than adding a second response store or guessed resume protocol.

## Next exact action

Keep product at b95 / b96 unallocated until the authoritative Detail `conversation_async_status` value is confirmed on this same current-account Runtime path. The remaining research question is now narrow: observe only the top-level async-status transition (`IS_STREAMING` → `COMPLETE` or equivalent) and correlate it with the already-observed Detail polling. Then decide whether a minimal state-driven Detail polling loop is justified. Do not copy cadence blindly and do not add `/resume`, retry/watchdog, or duplicate Send.
