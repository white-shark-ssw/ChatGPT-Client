# DEV-send-stream — b94 foreground rebootstrap + WebContent termination Runtime evidence — 2026-09-03

## Exact candidate identity

- Candidate: `DEV-send-stream-0.1.0-b94`
- Build: `0.1.0 (94)`
- Diagnostics source marker: `59894bd9ca7c`
- Exact product/config package source: `59894bd9ca7c293211cd856ecf33579f19ce4d84`
- Device / OS: iPhone / iOS 17.0
- User-supplied diagnostics export: `ChatGPTClient-Diagnostics-20260903-143853.json`, exported at `2026-09-03T14:38:53Z`

## What b94 proves

The isolated foreground page-rebootstrap mechanism is Runtime Positive as a mechanism.

After one explicit Sync established page-owned external continuation, the selected project conversation progressed normally. When the app entered background at `14:25:44-14:25:46Z` and returned foreground at `14:25:52Z`, exact b94 emitted:

- `foregroundExternalRebootstrap.requested`
- `coveredExecutor.webViewActivation stage=foreground_external_page_rebootstrap`
- `coveredExecutor.foregroundPageRebootstrap`
- official page load completion
- renewed page-owned `externalStreamStatusRequest/Response` with HTTP 200 / `IS_STREAMING`
- renewed external snapshots without another manual Sync

The renewed snapshots advanced from the pre-background `serviceMessageCount=7 / toolCount=2` through `11/4`, `13/4`, and `15/5`.

A later foreground rebootstrap at `14:27:25Z` again restored the official page-owned loop. After page load and renewed `IS_STREAMING`, Native external snapshots advanced to `34/12`, `36/13`, `37/14`, and then `39/14`.

Therefore exact b94 proves that full official-page rebootstrap on foreground can restart a continuation acquisition loop that otherwise dies across lifecycle transitions. This is stronger than b93 focus-only recovery, which was already rejected as sufficient.

## New reliability failure: WebContent process termination

The same exact run also contains a new decisive runtime failure.

After several foreground/background transitions and repeated full conversation-page rebootstrap actions, the app returned foreground at `14:35:12Z`. The page completed loading at `14:35:15Z`, then at `14:35:17Z diagnostics recorded:

- `coveredExecutor.webProcess state=terminated`
- `coveredExecutor.failed reason=web_process_terminated`
- the external live generation transitioned to `failed`
- the executor was released (`activeExecutorCount=0`)

This is direct evidence that the covered `WKWebView` WebContent process can terminate during this long-running project-conversation scenario.

The termination reason is **Unverified**. The current diagnostics do not capture WebContent-process memory or an OS jetsam reason, so this evidence must not be described as proven OOM. Resource pressure / Web page complexity / repeated heavy full-page reloads are now strong hypotheses, not established root cause.

## Conversation-size / request-cost context

This project conversation is very large and has continued growing across the development session. In this b94 export:

- initial Detail response: `5,179,662` bytes, mapping `1427`, recipient-message count `367`, visible messages `27`; because the app entered background almost immediately after the request, its `41.65s` duration is not a clean network/performance benchmark
- first explicit Sync: `5,180,455` bytes, mapping `1428`, recipient-message count `367`, visible messages `28`, duration `4.46s`
- later authoritative Syncs: `5,491,909` bytes, mapping `1535`, recipient-message count `397`, visible messages `28`, durations `4.77s` and `5.44s`

Historical exact Runtime logs on the same conversation show progressive growth from roughly `3.88 MB / mapping 1031` (b90-era sample), `4.23 MB / 1158`, `4.52 MB / 1238`, `4.82 MB / 1307`, to the current `5.49 MB / 1535`.

This size growth makes the user's earlier Web Rule Lab timeout/resource concern materially relevant. It still does not by itself prove the WebContent termination cause.

## What happened after WebContent termination

At `14:36:11Z` the user manually invoked `同步最新消息`.

That Sync **succeeded at the transport / authoritative Detail layer**:

- HTTP 200
- Detail `5,491,909` bytes
- mapping `1535`
- visible messages remained `28`
- authoritative trailing response remained active: reasoning items `3`, timeline items `33`, tool items `30`
- request duration `4.77s`

Repository correctly cleared the terminal/failed external generation and started a new external live generation (`responseGeneration=2`) from authoritative trailing Detail.

A fresh covered executor then reacquired page-owned continuation. `stream_status` repeatedly returned HTTP 200 / `IS_STREAMING`, and snapshots reported `serviceMessageCount=109`, `toolCount=30`, reasoning characters `902`, `finalCharacters=0`.

The user invoked Sync again at `14:38:14Z`. This final Sync also **succeeded**:

- HTTP 200
- same `5,491,909` byte authoritative Detail
- same mapping `1535`
- same visible message count `28`
- same trailing reasoning/timeline/tool counts `3 / 33 / 30`
- duration `5.44s`

After this successful Sync and manual page rearm, official `stream_status` continued to report `IS_STREAMING` through the end of the export. Repeated snapshots remained at `serviceMessageCount=109 / toolCount=30 / finalCharacters=0`.

Therefore the user's observation that the last Sync 'did not sync out the answer' is not a failed Sync request. The authoritative server data itself still represented an unfinished/stuck response at export time. This log cannot distinguish a genuinely still-running remote response from a server-side generation stuck in `IS_STREAMING`; no terminal/final assistant exists in the authoritative Detail before export.

## Grey '重载当前会话' behavior

Current product code intentionally disables `重载当前会话` whenever `liveSnapshot.phase.isActive == true`, while `同步最新消息` remains available for an external live response (`promptText` empty).

After the successful authoritative Sync rebuilt external generation 2 from the 33-item trailing response, its phase remained active, so the menu correctly rendered `重载当前会话` disabled. This matches the user's grey-button observation; it is not evidence of a detail operation remaining in flight.

The combination exposes a recovery dead-end: if authoritative Detail and official `stream_status` remain indefinitely active after a WebContent termination, the user can Sync but cannot manually choose full conversation reload under the current menu policy.

## Runtime classification

- project scoped-route identity: Runtime Positive (preserved from b91)
- covered page-owned external continuation: Runtime Positive (preserved from b92)
- foreground official-page rebootstrap mechanism: **Runtime Positive**; it demonstrably restarts page-owned continuation after lifecycle interruption
- focus-only recovery as sufficient: Rejected (preserved from b93)
- repeated full-page rebootstrap / long-running covered Web reliability: **Runtime Negative / not production-stable in this exact run** because `webViewWebContentProcessDidTerminate` occurred
- WebContent termination caused by memory/OOM: **Unverified**
- final external terminal/final convergence: **Unverified / not achieved**; authoritative Detail and `stream_status` still report active unfinished response at export
- final manual Sync transport: **Runtime Positive**; both late Sync calls returned HTTP 200 authoritative Detail
- current manual reload recovery UX while external live stays active: **blocked by intentional UI policy**
- Stable/Frozen Send: **No**

## Next evidence target

Do not treat b94 as a production-stable final recovery strategy, and do not add speculative polling/retry/timers/watchdogs.

Before allocating another candidate, inspect the minimum event-driven recovery needed for two now-proven conditions:

1. avoid repeated heavy full-page rebootstrap storms when foreground transitions happen close together / while a prior navigation is still being established;
2. provide a deliberate user recovery path after WebContent termination or indefinitely active external state without violating the official-page-owns-transport / Repository-owns-content boundary.

Any next candidate must be a separately justified minimum A/B. Do not claim OOM without WebContent/OS evidence, and do not replace official page-owned continuation with Native `stream_status`, `/resume`, guessed offsets, cadence polling, WebSocket-body authority, or a second response store.
