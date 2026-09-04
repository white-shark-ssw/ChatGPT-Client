# DEV-send-stream

> Latest round-7 Runtime evidence and exact continuation action are maintained in `docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md`. As of 2026-09-04, Probe v0.7 Human Runtime is complete; product remains b95 and b96 remains unallocated. Read the addendum first before acting on older sections below.

## Official iOS Probe v0.6 Runtime / v0.7 dispatch-data gate — 2026-09-04

Exact v0.6 JSONL `sha256:1cb6eb096c5748e7f781afbd761906bda39d55227a115a4e2dcea8c240de7a43` is valid Human Runtime: 78,828 bytes / 207 events / zero parse errors / all v0.6. The file spans `probe.log_cleared` and one later full process relaunch but contains no mixed Probe revision.

The decisive `probe.detail_task_callback_surface` fired for `__NSCFLocalDataTask`. Runtime-evidenced response/data surface includes `connection:didReceiveData:completion:`, `_task_onqueue_didReceiveDispatchData:completionHandler:`, `_onqueue_didReceiveDispatchData:completion:`, `_onqueue_didFinishWithError:`, plus `_dataTaskData` / `_pendingResponseBytes` as `OS_dispatch_data` and `_dataTaskCompletion` as a block. This proves the private callback/buffer surface exists on the exact current task class; the method-table snapshot alone does not prove invocation order.

Target `0df178903e95` again performs authoritative Conversation Detail GET polling; after relaunch intervals are `12.031 / 10.034 / 11.662 / 10.951s`. Native Detail polling remains Runtime Positive. `http.conversation_detail.async_status` remains absent because v0.6 did not yet hook the newly evidenced dispatch-data path; async-status semantics remain Unverified.

Probe v0.7 changes research tooling only. It hooks exactly `_task_onqueue_didReceiveDispatchData:completionHandler:` on NSURLSession task subclasses, gates scanning to authoritative Conversation Detail, feeds dispatch-data regions into the existing exact `conversation_async_status` scanner, and passes the original callback arguments through unchanged. It initiates no request/poll/timer/retry/resume and logs no response content/auth. Product remains b95; b96 remains unallocated.

Evidence ladder: **v0.6 Human Runtime analyzed / callback surface Runtime Positive / exact private callback invocation still Unverified / Native Detail polling Runtime Positive again / v0.7 research code written / dedicated CI pending / product b95 unchanged / b96 unallocated / Stable-Frozen Send No.**

**Next exact action:** dedicated research CI/package exact v0.7, then Human Runtime. Decisive evidence is same-target `http.conversation_detail.async_status` from the dispatch-data observer, ideally `is_streaming -> complete` or another actually observed safe enum. Do not allocate b96 before that result.

## Official iOS Probe v0.5 Runtime / v0.6 callback-surface gate — 2026-09-04

Exact user-exported Probe v0.5 JSONL `sha256:26e8646945831764bf6317c99213ff8a9621d09942e642a19b4f15aa24c892ba` is clean Human Runtime evidence: 47,648 bytes / 146 valid events / zero parse errors / all `probeVersion=0.5`, beginning from a clean-log test window. Native task-level observation is Runtime Positive again.

For target conversation hash `0df178903e95`, exact `__NSCFLocalDataTask` GET Detail requests occur at `20:57:28.958`, `20:57:56.962`, `20:58:07.117`, `20:58:16.235`, `20:58:25.668`, `20:58:35.051`, `20:58:44.323`, and `20:58:53.546Z`. After the first reacquisition gap, the repeated intervals are approximately `10.155 / 9.118 / 9.433 / 9.383 / 9.272 / 9.223s` (median `9.328s`). This independently reconfirms official Native authoritative Conversation Detail polling on the current account.

There are **zero** `http.conversation_detail.async_status` events despite the target Detail tasks. This is not evidence that `conversation_async_status` is absent. Probe v0.5's public `URLSession:dataTask:didReceiveData:` observer is therefore **Runtime Negative as coverage for this Swift-async Detail response path**; the field/value and official active/terminal contract remain Unverified.

Probe v0.6 is research-only and changes no ChatGPTClient product file. It keeps v0.5 observation but, on the first target Detail task only, records a bounded structural snapshot of the actual task class hierarchy: callback-relevant Objective-C selector names, argument counts/type encodings, plus callback/session/delegate-related ivar names/type encodings. It reads no ivar values, installs no guessed private callback hook, initiates no request, and logs no auth/content. The purpose is to identify one evidenced Swift-async response-delivery callback before any deeper observer.
