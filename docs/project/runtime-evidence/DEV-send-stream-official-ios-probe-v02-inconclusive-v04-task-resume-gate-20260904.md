# DEV-send-stream — official iOS Probe v0.2 Inconclusive / v0.4 task-resume gate — 2026-09-04

## v0.2 Human Runtime

JSONL `sha256:f4f7e6f897e73262473a296ecbccc012477c5e1b44bdfe5ca7e3a43006148513`: 76,447,285 bytes, 392,033 valid events, zero parse errors, begins with `probe.log_cleared`. A user-WebSocket `NSPOSIXErrorDomain/53` was followed by repeated receive invocations on the failed task; v0.2 emitted 196,002 receive-arm and 195,999 receive-error records. The resulting ~76 MB logging storm materially perturbed the process. Overall late-join is Inconclusive; absence of target HTTP/SSE/per-turn-WebSocket events is not a protocol rejection.

## Official static evidence

The exact supplied official framework contains `ConversationPollingManager`, resume-fetch recovery, stream-status polling/fetch diagnostics, `ConversationStreamStatusResponse`, `KnownConversationStreamStatus`, `IS_STREAMING`, `ios.conversation_polling`, `chatgpt-ios-inline-polling`, and resumable streaming symbols. It imports Swift async URLSession `data(for:)` / `bytes(for:)`. This justifies task-level observation, not guessed polling cadence or product ownership.

## Probe v0.4 identity

- source `db3f8a7d01f39f364f6166cf72245db426cadef1`
- trigger/head `ce43a7fc3fb4f581dd7614bac541c44dff8af512`
- CI `33795191324 / 100781074234` success
- Artifact `9908872470`
- Artifact digest `sha256:29675f185f8b0919821e6fdb44a3cc4ff3673187c346dd00e1f45fc3f47a8ccc`
- dylib SHA `cc6a2b29b19441f56f214b199e5e7512c1739b3ae8563bc7968c0eb26779ecf9`
- official source ZIP SHA `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`
- research IPA SHA `b4c0e53ea07bea92787ef7186b5ad79e1aa5f7bb52ebd2c2272e7060261d3d6e`
- official identity unchanged: `com.openai.chat` / `1.2026.202` / `30140022279`
- extracted diff: exactly three intended files

v0.4 emits one privacy-safe `http.task.resume` per observed NSURLSession task and keeps v0.3 failed-socket error de-duplication. Human Runtime pending; product/b96 blocked until a current-account target acquisition path is observed.
