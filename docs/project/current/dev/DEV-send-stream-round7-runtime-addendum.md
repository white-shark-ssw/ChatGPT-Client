# DEV-send-stream round 7 Runtime addendum

## Probe v0.8 batch package / single Human Runtime gate — 2026-09-04

User feedback changes the research optimization target: repeated one-small-delta official-app installs/tests are too expensive in human time. Probe v0.8 is therefore a **batched research diagnostic**, not another single-callback experiment. It still changes no ChatGPTClient product behavior and uses only response surfaces already Runtime-evidenced by Probe v0.6.

Exact v0.8 batch research source is `43384aa0e348762b0c8bc6192f580d8cd06064b4`. It adds `ProbeBatchHooks.m`, updates the export UI to clear/share both base and batch logs in one action, and compiles the batch hooks into the existing research dylib. The base v0.7 observer remains present so the same run still captures HTTP/task/WebSocket evidence; batch-only events are written separately to `ChatGPTRealtimeProbeBatch.jsonl` with `probeVersion=0.8` to avoid mixed-writer corruption.

The batched observer covers only the exact Probe v0.6 Runtime-evidenced private surfaces, with exact type-encoding guards before installation:

- `_task_onqueue_didReceiveDispatchData:completionHandler:` — `v32@0:8@16@?24`
- `_onqueue_didReceiveDispatchData:completion:` — `v32@0:8@16@?24`
- `_onqueue_didFinishWithError:` — `v24@0:8@16`
- `connection:didReceiveData:completion:` — `v40@0:8@16@24@?32`
- `_dataTaskData` — `NSObject<OS_dispatch_data>`
- `_pendingResponseBytes` — `NSObject<OS_dispatch_data>`

If any selector encoding differs at Runtime, v0.8 does not install that hook and records `batch.private_surface_skipped` instead of guessing a signature. For authoritative Conversation Detail tasks it records privacy-safe callback selector/order/count, dispatch byte/region count, coarse leading payload class, HTTP/error/task correlation, finish-time presence/structure of the two evidenced dispatch-data buffers, exact `conversation_async_status` key presence and safe token when observable. It never logs response body/auth/raw conversation ID and initiates no request, poll, timer, retry, resume or product action. Per-task callback event logging is capped while total selector counts remain summarized at finish.

Validation identity:

- dedicated research run: `33847432865 / 100942332793` — success
- canonical Artifact: `9927040454`
- Artifact digest / downloaded ZIP SHA-256: `07ae29e866d3791b13a396efa23278994574c834a28855064d81965f0662421a`
- Probe dylib SHA-256: `d636267227b1f9fb4c92ba13b3fe49973e9f0abe5a4812b77303f9480a87b3ec`
- regular PR CI on the same research head: `33847437016` — success
- pristine official source ZIP SHA-256: `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`
- repacked research IPA SHA-256: `d9072fad0e8bb020e8b9681d7d4e29e3bba473bb357af5197b5c90d259422970`
- outer delivery ZIP SHA-256: `ec48a33262e65392b003c33dc5e3f0df515297b522bddfb8891182b976d06f0b`
- official identity preserved: `com.openai.chat / 1.2026.202 / 30140022279`
- exact content diff versus pristine source: zero removed, exactly two added paths (original enhancer backup + research marker), exactly one modified path (enhancer load entry replaced by the batch Probe); replacement and backup keep executable mode `0755`.

Evidence ladder: **batched research code written / exact v0.6 selector-type guards encoded / dedicated research CI passed / regular PR CI passed / Artifact produced / dylib and research IPA independently verified / Human Runtime pending / ChatGPTClient product remains exact b95 / b96 unallocated / Stable-Frozen Send No.**

**Next exact action / intended only Human Runtime round:** install exact v0.8 batch research IPA, fully relaunch official ChatGPT, press `清空` once, run one deliberately long cross-platform response in the target conversation through active-to-terminal if possible, then press `Probe` once. The share sheet exports both `ChatGPTRealtimeProbe.jsonl` and `ChatGPTRealtimeProbeBatch.jsonl` together. Analyze them jointly for callback invocation/order, finish-buffer availability, exact async-status key/token, target Detail polling and any target WebSocket event. Do not request another Probe run merely because one of the already-evidenced surfaces was omitted; this version is intentionally instrumented to collapse those branches into this single run.

Do not allocate b96 or add Native polling cadence, guessed `/resume`, retry/watchdog/timer, duplicate Send, WebSocket-body authority, or a second response store before this batch result.

## Human Runtime cost override — batch the next evidenced Probe — 2026-09-04

The user explicitly rejected the prior one-small-delta-per-human-run research cadence as too costly: Probe had already progressed through v0.7, and repeatedly installing/relaunching/reproducing/exporting one tiny observation at a time is an unacceptable human-time burden. This changes the research execution strategy, not the product evidence standard.

For research Probe instrumentation, optimize for **minimum human Runtime rounds** while staying evidence-first. Research tooling may observe several **already evidenced** response surfaces in parallel because its purpose is to collapse mutually exclusive diagnostic branches into one Human Runtime run. Do not add guessed selectors, guessed protocol requests, polling, timers, retries or product behavior.

Product remains exact b95; b96 remains unallocated; Stable-Frozen Send remains No.

## Probe v0.7 Human Runtime — 2026-09-04

- Exact user-uploaded `ChatGPTRealtimeProbe(1)(1).jsonl` is clean Probe v0.7 Human Runtime evidence: `sha256:fa16a0d01366ea037fffa158c5e7f4a3818f1d97a3a2f8ee1ffa6a26d46fcda2`, 41,879 bytes / 122 valid JSONL events / zero parse errors / all `probeVersion=0.7`. The test window begins with `probe.log_cleared` at `2026-09-04T06:43:12.222Z` and contains no mixed Probe revision.
- Target conversation hash `0df178903e95` issued 16 authoritative `GET /backend-api/conversation/<id>` Detail tasks at `06:43:51.475`, `06:44:14.463`, `06:44:24.677`, `06:44:34.822`, `06:44:44.429`, `06:44:54.675`, `06:45:04.911`, `06:45:21.523`, `06:45:32.525`, `06:45:43.393`, `06:45:54.931`, `06:46:05.461`, `06:46:15.053`, `06:46:25.518`, `06:46:35.301`, and `06:46:45.667Z`. Intervals are `22.988 / 10.214 / 10.145 / 9.607 / 10.246 / 10.236 / 16.612 / 11.002 / 10.868 / 11.538 / 10.530 / 9.592 / 10.465 / 9.783 / 10.366s`. Native authoritative Detail polling is Runtime Positive again.
- The sample contains zero `conversation_stream_status`, zero `conversation_resume`, and no target conversation/per-turn WebSocket update. The only WebSocket frames are foreground/background `presence` commands plus their `reply` frames. This again does not support the ordinary user WebSocket as the current late-join response owner.
- There are zero `http.conversation_detail.async_status` events despite the 16 target Detail GETs. This rejects only the proposition that Probe v0.7 already yields the desired async-status signal in this Runtime. It does **not** prove `conversation_async_status` is absent from authoritative Detail responses.
- Important instrumentation boundary: Probe v0.7's `_task_onqueue_didReceiveDispatchData:completionHandler:` hook writes no standalone callback-invocation event. It only emits `http.conversation_detail.async_status` after the exact field scanner succeeds. Therefore v0.7 cannot distinguish `private callback not invoked` from `callback invoked but scanner saw no usable field/value`.
- Product evidence classification remains unchanged: official Native Detail polling Runtime Positive; exact `conversation_async_status` value and official active/terminal stop contract Unverified. ChatGPTClient product remains exact b95; b96 remains unallocated; Stable-Frozen Send No.

## Probe v0.7 package identity — 2026-09-04

- Probe v0.7 research source/head: `718accba952bea2cb59005d17b8bf44317624f1c`
- dedicated research `build-probe`: `33844386493 / 100933029519` — success
- canonical Artifact: `9925975675`
- Artifact digest: `sha256:26aff9c1c911dd74f88f587df248fdf5552d636fc9f5f549d5afd76e5bff1835`
- Probe dylib: `sha256:398d21e114f76b16e590b769878e3fb2a00899b2d95dccda5db69b84d1771101`
- repacked IPA: `sha256:c4b2e81b60d34a4e9926585881b87cf8ebf4527b9890f15497cc95acd96fab94`
- outer ZIP: `sha256:5bd576c42fced0812fdfc775f88482668316b0aaf8ce1db12fc02c6bac18fcf9`
- official identity: `com.openai.chat / 1.2026.202 / 30140022279`
