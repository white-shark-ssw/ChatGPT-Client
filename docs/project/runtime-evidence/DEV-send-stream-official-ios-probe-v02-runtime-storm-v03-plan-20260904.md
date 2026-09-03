# DEV-send-stream — official iOS Probe v0.2 Runtime / v0.3 minimum observation plan — 2026-09-04

## Input identity

- User-exported file: `ChatGPTRealtimeProbe(1).jsonl`
- SHA-256: `f4f7e6f897e73262473a296ecbccc012477c5e1b44bdfe5ca7e3a43006148513`
- Size: 76,447,285 bytes
- Parsed JSONL events: 392,033
- Parse errors: 0
- Probe version in file: `0.2`
- First event: `2026-09-03T18:35:51.569Z`
- Last event: `2026-09-03T18:38:48.162Z`

This is Human Runtime evidence from the research-modified official iOS package. It is not ChatGPTClient product Runtime and does not allocate b96.

## What is Runtime Positive

- `probe.log_cleared` is the first event, proving the v0.2 clear-log control worked for this sample.
- URL path privacy redaction is active: the observed official user socket is recorded as `/p24/ws/user/<opaque>` rather than the raw opaque user-specific segment.
- Direct presence state is now observable. Immediately after log clear, the existing user socket emitted a `presence` command with `commandState=background`; later foreground/background transitions are recorded structurally.
- The Probe can still observe the official `ws.chatgpt.com` user WebSocket and, after a later app relaunch, sees a fresh `connect` plus the same three base subscriptions: `calpico-chatgpt`, `app_notifications`, `push_auth_challenge`.

## Socket-error storm

The existing user WebSocket returned `NSPOSIXErrorDomain / 53` at `18:36:31.101Z`. After that, the app repeatedly invoked `receiveMessageWithCompletionHandler:` on the failed task and immediately received the same error.

The Probe recorded:

- `ws.receive.arm`: 196,002
- `ws.receive.error`: 195,999, all `NSPOSIXErrorDomain / 53`
- first storm block: 147,987 errors from `18:36:31.101Z` through `18:37:21.523Z` (~50.422 s)
- second storm block: 48,012 errors from `18:37:31.026Z` through `18:37:53.295Z` (~22.269 s)
- `ws.send.error`: 7, also code 53

The Probe source does not itself schedule another receive after an error; it logs and forwards the original callback. Therefore this file does not prove the Probe caused the repeated receive calls. However logging every arm/error produced a 76 MB file and substantial instrumentation work, so this sample is observationally perturbed and must not be used as a clean negative late-join result.

A later process relaunch at `18:38:45Z` reloaded Probe v0.2, installed 94 hooks, created a fresh user WebSocket, sent `connect` plus the same three base subscriptions, and received four reply frames.

## Late-join observation result

Across all 392,033 events:

- zero events contain a `conversationHash`;
- zero conversation-specific/per-turn WebSocket subscribe/update/catchup/live frames appear;
- zero `http.observed.request` events appear;
- the only `http.*` event is `http.observed.complete` for the failed WebSocket handshake/task itself (`status=101`, code 53);
- no conversation Detail, `stream_status`, resume, conversation fetch, SSE or other target-correlated HTTP event is observed.

Classification: **overall official cross-platform late-join remains Inconclusive.** The absence of target events is not decisive because the socket-error storm materially pollutes this run and v0.2 still has a concrete URLSession coverage gap described below. The JSONL does not encode whether the official iOS UI visibly joined/continued the remote answer, so that user-observed UI fact must be kept separate from transport evidence.

## Static official-iOS evidence that changes the next probe

Inspection of the exact supplied decrypted official ChatGPT framework shows current native symbols/strings for:

- `DefaultWebSocketConversationEventsService` / `WebSocketConversationObserver`;
- `stream_handoff`, `resume_conversation_token`, `turn_exchange_id`, `topic`, `resume_sse_endpoint`;
- `Conversations/ConversationResumeFetchRecovery.swift`;
- `conversation_resuming.recover_with_new_polling_attempt` / `recover_with_fetch_attempt`;
- `Failed to fetch conversation stream status during inline recovery polling`;
- `Inline polling reached complete status but conversation fetch failed`.

This proves the official iOS client contains native stream-handoff and fetch/status recovery machinery. It does **not** prove which branch owns cross-platform late-join in this Runtime sample and does not authorize ChatGPTClient to copy a polling cadence yet.

The same official binary exposes both `dataTaskWithRequest:` and `dataTaskWithURL:` / `dataTaskWithURL:completionHandler:` URLSession entry forms. Probe v0.2 hooks only the request forms. That is a concrete observation blind spot, not a guessed protocol.

## Probe v0.3 minimum research delta

Research tooling only; no ChatGPTClient product change and no b96 allocation:

1. stop logging every `ws.receive.arm`;
2. record only the first repeated receive error for a failed WebSocket task until that same task later receives a real message, preventing another 76 MB error storm while preserving the failure signal;
3. retain all existing privacy-safe WebSocket structural logging and the `清空` control;
4. add privacy-safe observation wrappers for `dataTaskWithURL:` and `dataTaskWithURL:completionHandler:` alongside the existing request variants;
5. keep URL/query/body privacy rules unchanged: no Cookie/Authorization/signed query values/prompt/answer/reasoning/tool text;
6. do not yet add a more invasive task-level global `resume` hook. If v0.3 still misses target traffic during a visually confirmed official late-join, that negative result will justify the broader task-level observer as the next isolated research step.

## Batch recovery / next exact action

Current product identity remains b95: product `ac5e621aa69f5f27ef3167b4a951812be8b8e2c2`, package source `a10320e589acd551a8dc53f56aaf28a0a08f5b4a`, canonical Artifact `9901461763`; b96 remains unallocated. Current feature branch is `dev/send-stream-20260829`, PR #29 open/unmerged, and `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.

Before source writes, update the selected checkpoint with this exact v0.2 Runtime classification and v0.3 research-only scope. Then change only the research Probe source/README as needed, run the dedicated research Probe CI, independently package against the exact official source ZIP `sha256:bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`, verify the research IPA diff/identity, update checkpoint/PROJECT_STATE/PR, and remove all temporary v0.2/v0.3 apply/finalize tooling. Do not touch `ChatGPTClient/**`, `ChatGPTClient.xcodeproj/**`, or allocate a production Candidate from this research result.
