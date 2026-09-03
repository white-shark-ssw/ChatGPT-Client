from pathlib import Path

checkpoint = Path('docs/project/current/dev/DEV-send-stream.md')
state = Path('docs/project/PROJECT_STATE.md')
evidence = Path('docs/project/runtime-evidence/DEV-send-stream-official-ios-probe-v04-native-detail-polling-20260904.md')

cp = checkpoint.read_text()
title = '## Official iOS Probe v0.4 Runtime — Native Detail polling observed — 2026-09-04'
assert '# DEV-send-stream\n' in cp
assert 'Official iOS Probe v0.4 package-ready research override' in cp
if title not in cp:
    block = '''## Official iOS Probe v0.4 Runtime — Native Detail polling observed — 2026-09-04

Exact user-exported Probe v0.4 JSONL `sha256:cd2b1693a423a37504d96e410c97c04a7987e76283c6458b90ff2db17dc09bd5` is a clean Human Runtime sample: 58,776 bytes / 185 events / zero parse errors / all `probeVersion=0.4`, beginning with `probe.log_cleared`. Probe v0.4 task-resume observation is therefore Runtime Positive and the v0.2 instrumentation-storm defect is absent.

The strongest target conversation is privacy hash `0df178903e95`. After the official user WebSocket emitted foreground presence at `19:30:48.034Z` and immediately failed send with `NSPOSIXErrorDomain/53`, HTTPS task-level observation continued independently. The same target then issued `GET /backend-api/conversation/<id>` at `19:30:48.044`, `19:30:57.378`, `19:31:07.526`, `19:31:17.369`, and `19:31:26.920Z`; consecutive intervals are approximately `9.334 / 10.148 / 9.843 / 9.551s` (median `9.697s`). These are `__NSCFLocalDataTask` tasks that were invisible to the earlier public URLSession-constructor hooks.

This Runtime pattern aligns tightly with exact official-binary static evidence for `ChatGPTConversation/TriggerAsyncStatusPollingConversationObserver.swift`, `ConversationPollingManager`, `poll(conversationID:...)`, `Starting polling for conversation`, `default_interval`, `model_slug_intervals`, `Conversation async status ... is no longer streaming, stopping polling`, `backend_streaming_completed`, and `conversation_async_status`. It is therefore the strongest current evidence that official iOS cross-platform late-join/recovery uses Native authoritative Conversation Detail polling rather than the ordinary user WebSocket. Exact internal call ownership remains an inference until response-state correlation is captured.

Do **not** misclassify the repeated `POST /backend-api/f/conversation/prepare` tasks as continuation polling. The exact official binary associates them with `MessageInputPrepareConversationViewModel`, `prepareConversation(...)`, `chatgpt-ios-prepare-debounce-period`, and client prepare dispatch/source fields. They are composer/send preparation traffic, not the observed late-join acquisition loop.

In this sample there is no `conversation_stream_status`, no `conversation_resume`, no target conversation/per-turn WebSocket subscription/update frame, and no observed response body/completion for the Swift-async-created Detail tasks. Therefore the request path and approximate polling cadence are Runtime-observed, while exact Detail `async_status` value, response evolution, official start/stop condition, and whether this exact interval was visually correlated with live UI advancement remain Unverified from the JSONL alone.

Static product review shows `ConversationRepository` already owns an authoritative `GET https://chatgpt.com/backend-api/conversation/{id}` Detail path and parses `mapping/current_node`, but does not currently parse top-level `async_status`. This means no new response store or guessed `/resume` is required for the next design; however product b96 must not be allocated solely from cadence inference. First capture/confirm the Detail response state that causes official polling to continue/stop, or obtain explicit Human visual correlation for this exact polling window plus the active/terminal state signal.

Evidence ladder: **Probe v0.4 research code/CI/Artifact/package verified; task-level observer Runtime Positive; Native target Detail polling Runtime observed; ordinary user-WebSocket late-join unsupported in this sample; stream-status/resume not observed; exact async-status response semantics and product polling trigger/stop contract Unverified; product remains b95; b96 unallocated; Stable/Frozen Send No.**

**Next exact action:** keep product frozen at b95. Resolve one remaining state-ownership question before b96: identify the authoritative Detail `async_status` / equivalent active-vs-terminal signal on the same current-account path and correlate it with the observed ~10s Detail loop. Do not copy a timer blindly and do not add Native `/resume`, retry/watchdog, or a second response store.

'''
    cp = cp.replace('# DEV-send-stream\n\n', '# DEV-send-stream\n\n' + block, 1)
    checkpoint.write_text(cp)

ps = state.read_text()
state_title = '## 2026-09-04 — Probe v0.4 Runtime observes Native Conversation Detail polling'
assert '# Project State\n' in ps
if state_title not in ps:
    state_block = '''## 2026-09-04 — Probe v0.4 Runtime observes Native Conversation Detail polling

- Exact v0.4 JSONL `sha256:cd2b1693a423a37504d96e410c97c04a7987e76283c6458b90ff2db17dc09bd5`: 58,776 bytes / 185 events / zero parse errors / clean-log start. v0.4 task-resume observer is Runtime Positive; no v0.2-style log storm.
- Target hash `0df178903e95` issued authoritative `GET /backend-api/conversation/<id>` tasks after foreground at `48.044 / 57.378 / 67.526 / 77.369 / 86.920s`, intervals ~`9.334 / 10.148 / 9.843 / 9.551s` (median ~`9.697s`). The user WebSocket concurrently failed with POSIX 53, so this HTTPS loop is independent of that socket.
- Official binary independently contains `TriggerAsyncStatusPollingConversationObserver`, `ConversationPollingManager`, polling start/stop diagnostics, `default_interval`, `conversation_async_status`, and `backend_streaming_completed`. Runtime + static evidence strongly support Native Conversation Detail polling as the cross-platform acquisition/recovery mechanism. Exact response-state trigger/stop semantics remain Unverified.
- Repeated `/f/conversation/prepare` is send/composer preparation (`MessageInputPrepareConversationViewModel`), not late-join polling. No target `stream_status`, `/resume`, or conversation WebSocket update was observed in this sample.
- Existing product `ConversationRepository` already owns authoritative Conversation Detail GET and content projection, but currently ignores top-level `async_status`. Product stays b95; b96 remains unallocated pending authoritative active/terminal state correlation. Stable/Frozen Send No.

'''
    ps = ps.replace('# Project State\n\n', '# Project State\n\n' + state_block, 1)
    state.write_text(ps)

if not evidence.exists():
    evidence.write_text('''# DEV-send-stream — official iOS Probe v0.4 Native Detail polling — 2026-09-04

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

This static evidence and the Runtime cadence strongly align with a Native polling manager that refreshes authoritative Conversation Detail while backend streaming is active.

## Important exclusion: `/f/conversation/prepare`

Probe v0.4 also records many `POST /backend-api/f/conversation/prepare` tasks. These must not be treated as continuation polling. The official binary independently maps prepare traffic to `MessageInputPrepareConversationViewModel`, `prepareConversation(...)`, `chatgpt-ios-prepare-debounce-period`, `clientPrepareDispatch`, and `clientPrepareSource`: it is composer/send preparation.

## Classification

- Probe v0.4 task-resume observer: **Runtime Positive**.
- Native target Conversation Detail polling: **Runtime observed / strongly correlated with official ConversationPollingManager**.
- Ordinary user WebSocket as the conversation late-join content path: **not supported by this sample**; its presence sends fail while HTTPS polling continues.
- `conversation/{id}/stream_status`: **not observed in this sample**.
- `/f/conversation/resume`: **not observed in this sample**.
- Exact Detail response `async_status`, response evolution, polling start/stop predicate, and visible-UI correlation for this exact time window: **Unverified from JSONL alone**.

## Product implication

Current `ConversationRepository` already owns an authoritative `GET /backend-api/conversation/{id}` and projects Detail content from `mapping/current_node`; it does not currently parse top-level `async_status`. This points toward preserving the existing Native content authority and adding only evidence-backed active/terminal polling state later, rather than adding a second response store or guessed resume protocol.

## Next exact action

Keep product at b95 / b96 unallocated until the authoritative Detail active-vs-terminal state is confirmed for this same current-account path. Then decide whether a minimal official-style state-driven Detail polling loop is justified. Do not copy cadence blindly and do not add `/resume`, retry/watchdog, or duplicate Send.
''')
