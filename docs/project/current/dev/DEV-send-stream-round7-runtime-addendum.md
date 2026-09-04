# DEV-send-stream round 7 Runtime addendum

## Human Runtime cost override — batch the next evidenced Probe — 2026-09-04

The user explicitly rejected the current one-small-delta-per-human-run research cadence as too costly: Probe has already progressed through v0.7, and repeatedly installing/relaunching/reproducing/exporting one tiny observation at a time is an unacceptable human-time burden. This changes the research execution strategy, not the product evidence standard.

For research Probe instrumentation, optimize for **minimum human Runtime rounds** while staying evidence-first. The next Probe must batch all response-delivery surfaces already proven to exist by Probe v0.6 instead of requiring one human run per surface. Do not add guessed selectors, guessed protocol requests, polling, timers, retries or product behavior.

The batch Probe should, for authoritative target Conversation Detail tasks only, capture enough privacy-safe structure in one run to answer the currently branching questions together:

- whether each already Runtime-evidenced private response callback is actually invoked, with per-task callback order/count and exact selector identity;
- dispatch-data region/byte counts and coarse payload class only, without logging body bytes/content;
- exact `conversation_async_status` field presence and safe token when observable on any evidenced callback path;
- invocation of the already evidenced finish path and structural state of the already evidenced `_dataTaskData` / `_pendingResponseBytes` dispatch-data buffers at finish;
- bounded whole-buffer scanning for the exact `conversation_async_status` key/value when a Runtime-evidenced buffer is available, without persisting the buffer;
- response status/error/task identity correlation sufficient to relate all of the above to the same Conversation Detail task.

The v0.6 Runtime method/ivar snapshot is the selector/type authority for this batch. Do not guess method signatures from names. If a surface cannot be safely hooked from its exact Runtime-recorded type encoding, leave that surface unhooked and record that limitation rather than inventing a signature.

This broader research instrumentation is intentionally different from production candidate discipline: it may observe several **already evidenced** surfaces in parallel because its purpose is to collapse multiple mutually exclusive diagnostic branches into one Human Runtime run. ChatGPTClient product ownership and product candidate rules remain unchanged.

**New Human Runtime goal:** one install / one clean-log / one deliberately long cross-platform response / one export should ideally determine callback invocation, callback order, buffered-response availability, async-status presence/value, and whether the ordinary user WebSocket contributes a target update. Do not ask the user to run another Probe merely because one of those already-known surfaces was omitted from instrumentation.

Product remains exact b95; b96 remains unallocated; Stable-Frozen Send remains No.

## Probe v0.7 Human Runtime / batch diagnostic gate — 2026-09-04

- Exact user-uploaded `ChatGPTRealtimeProbe(1)(1).jsonl` is clean Probe v0.7 Human Runtime evidence: `sha256:fa16a0d01366ea037fffa158c5e7f4a3818f1d97a3a2f8ee1ffa6a26d46fcda2`, 41,879 bytes / 122 valid JSONL events / zero parse errors / all `probeVersion=0.7`. The test window begins with `probe.log_cleared` at `2026-09-04T06:43:12.222Z` and contains no mixed Probe revision.
- Target conversation hash `0df178903e95` issued 16 authoritative `GET /backend-api/conversation/<id>` Detail tasks at `06:43:51.475`, `06:44:14.463`, `06:44:24.677`, `06:44:34.822`, `06:44:44.429`, `06:44:54.675`, `06:45:04.911`, `06:45:21.523`, `06:45:32.525`, `06:45:43.393`, `06:45:54.931`, `06:46:05.461`, `06:46:15.053`, `06:46:25.518`, `06:46:35.301`, and `06:46:45.667Z`. Intervals are `22.988 / 10.214 / 10.145 / 9.607 / 10.246 / 10.236 / 16.612 / 11.002 / 10.868 / 11.538 / 10.530 / 9.592 / 10.465 / 9.783 / 10.366s`. Native authoritative Detail polling is therefore Runtime Positive again.
- The sample contains zero `conversation_stream_status`, zero `conversation_resume`, and no target conversation/per-turn WebSocket update. The only WebSocket frames are foreground/background `presence` commands plus their `reply` frames. This again does not support the ordinary user WebSocket as the current late-join response owner.
- There are zero `http.conversation_detail.async_status` events despite the 16 target Detail GETs. This rejects only the proposition that Probe v0.7 already yields the desired async-status signal in this Runtime. It does **not** prove `conversation_async_status` is absent from authoritative Detail responses.
- Important instrumentation boundary: Probe v0.7's `_task_onqueue_didReceiveDispatchData:completionHandler:` hook writes no standalone callback-invocation event. It only emits `http.conversation_detail.async_status` after the exact field scanner succeeds. Therefore this Runtime cannot distinguish `private callback not invoked` from `callback invoked but scanner saw no usable field/value`.
- Product evidence classification remains unchanged: official Native Detail polling Runtime Positive; exact `conversation_async_status` value and official active/terminal stop contract Unverified. ChatGPTClient product remains exact b95; b96 remains unallocated; Stable-Frozen Send No.
- **Next exact action:** replace the former single-callback v0.8 plan with one batch research Probe that covers all v0.6 Runtime-evidenced response callback/buffer surfaces needed to distinguish the remaining branches in one Human Runtime run. It must remain observation-only and privacy-safe, initiate no request/poll/timer/retry/resume, and use exact Runtime-recorded selector signatures rather than guessed signatures. Do not allocate b96 before this batch result.

## Probe v0.7 package / Human Runtime gate — 2026-09-04

- User-uploaded `ChatGPTRealtimeProbe(6).jsonl` is byte-identical to the already analyzed Probe v0.6 Runtime file: `sha256:1cb6eb096c5748e7f781afbd761906bda39d55227a115a4e2dcea8c240de7a43`, 78,828 bytes / 207 valid events / zero parse errors / all `probeVersion=0.6`. It is not a v0.7 sample and adds no new Runtime evidence.
- The duplicate file still reconfirms the prior v0.6 result only: target `0df178903e95` authoritative Conversation Detail GET polling is Runtime Positive and `probe.detail_task_callback_surface` exposes `_task_onqueue_didReceiveDispatchData:completionHandler:` plus dispatch-data storage/callback surface. `http.conversation_detail.async_status` remains absent because v0.6 did not hook this path.
- Probe v0.7 research source/head is `718accba952bea2cb59005d17b8bf44317624f1c`. Dedicated research `build-probe` `33844386493 / 100933029519` passed; canonical Artifact `9925975675`; Artifact digest / downloaded ZIP SHA `sha256:26aff9c1c911dd74f88f587df248fdf5552d636fc9f5f549d5afd76e5bff1835`; Probe dylib `sha256:398d21e114f76b16e590b769878e3fb2a00899b2d95dccda5db69b84d1771101` matching sidecar.
- Against pristine official source ZIP `sha256:bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`, independently repacked `ChatGPT-Official-RealtimeProbe-v07-TrollStore-20260904.ipa` is `sha256:c4b2e81b60d34a4e9926585881b87cf8ebf4527b9890f15497cc95acd96fab94`; outer ZIP is `sha256:5bd576c42fced0812fdfc775f88482668316b0aaf8ce1db12fc02c6bac18fcf9`. Package preserves `com.openai.chat / 1.2026.202 / 30140022279`, passes ZIP integrity, preserves dylib mode `0755`, and differs from pristine source in exactly three intended paths: original enhancer backup added, enhancer load entry replaced by Probe v0.7, research marker added.
- Probe v0.7 remains research-only. It observes only the Runtime-evidenced dispatch-data callback and scans authoritative Detail data for exact `conversation_async_status`; it adds no request, polling cadence, timer, retry, `/resume`, duplicate Send, response store or product authority.
- Evidence ladder: **v0.6 Human Runtime already analyzed / duplicate v0.6 re-upload identified / v0.7 research code + dedicated CI + Artifact + package verified / v0.7 Human Runtime completed but async-status unresolved / product remains b95 / b96 unallocated / Stable-Frozen Send No.**
