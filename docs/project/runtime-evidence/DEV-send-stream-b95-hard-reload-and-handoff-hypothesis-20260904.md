# DEV-send-stream b95 Runtime — hard Reload positive, transport handoff next hypothesis

Date: 2026-09-04
Work ID: `DEV-send-stream`
Candidate: `DEV-send-stream-0.1.0-b95`
Build: `0.1.0 (95)`
Source marker: `a10320e589ac`
Device: iPhone / iOS 17.0

## Evidence identity

User-exported diagnostics metadata matches the exact canonical b95 package: Release `0.1.0 (95)`, Candidate `DEV-send-stream-0.1.0-b95`, source `a10320e589ac`.

## Runtime progression

The tested project conversation is `sha256:0df178903e95`.

Initial authoritative Detail was already very large: `5,916,472` bytes, mapping `1634`, filtered-recipient messages `422`, visible messages `31`, with no active trailing timeline.

At `16:58:16Z` the user performed one explicit Sync. It completed HTTP200 at `16:58:20Z` with `5,919,249` bytes, visible messages `32`, and a trailing active reasoning/timeline item. Repository started external generation 1 from authoritative Detail.

The official covered page then acquired the external response through its own continuation path. Matching `stream_status` returned HTTP200 `IS_STREAMING`; the page-owned `/resume` offset 0 returned HTTP404 JSON and the existing page-owned status + plural-conversation read path continued. Native snapshots advanced without another Sync:

- `6` service / `2` tools / reasoning `202`
- `8 / 3 / 202`
- `10 / 4 / 202`
- `12 / 5 / 202`
- `14 / 6 / 202`

After background/foreground, full official-page rebootstrap again restarted continuation. A later foreground recovery caught the response up to phase `final`, reasoning `757`, service messages `103`, tools `30`, final characters `0`. Matching status/snapshot events then continued repeatedly while status remained `IS_STREAMING`.

Across this exact b95 run there were five `foregroundExternalRebootstrap.requested` / `foregroundPageRebootstrap` cycles. Unlike exact b94, there was no `coveredExecutor.webProcess state=terminated` and no `coveredExecutor.failed`. Therefore b94 WebContent termination is not reproduced by this sample; its cause remains Unverified and must not be called deterministic or proven OOM.

## Hard Reload result

At `17:09:33Z`, while Repository still held the external live response in phase `final` with reasoning `757`, timeline `33`, tools `30`, and final characters `0`, the user invoked `重载当前会话`.

b95 performed the intended hard-reset core:

- old covered executor released, active executor count reached 0;
- `liveResponse.reset reason=manual_reload` cleared external generation 1's live snapshot;
- `manualReload.hardReset` reported `executorReleased=true` and `liveSnapshotCleared=true`;
- one replacement authoritative Reload began as Detail operation generation 3.

At `17:09:38Z` Reload returned HTTP200 Detail `6,235,224` bytes, mapping `1737`, filtered-recipient messages `452`, visible messages `33`, with `trailingReasoningItemCount=0`, `trailingTimelineItemCount=0`, `trailingToolItemCount=0`. `conversationReload.end` reported visible messages `32 -> 33` and status `ok`.

This proves the completed assistant already existed authoritatively and the b95 hard Reload successfully materialized it. Hard Reload recovery is therefore **Runtime Positive** for this sample.

## Automatic convergence classification

This run does **not** prove automatic terminal/final convergence. Before the manual Reload, the page repeatedly reported HTTP200 `IS_STREAMING` while snapshots stayed at service `103`, tools `30`, final characters `0`. There is no page-owned COMPLETE / natural external terminal / authoritative automatic reconcile before the user Reload. The final assistant became visible through the authoritative hard Reload.

Classification:

- b95 hard Reload recovery: **Runtime Positive**.
- foreground full-page rebootstrap as a restart mechanism: **Runtime Positive again in this sample**.
- repeated/heavy covered-Web reliability: **not Stable** because exact b94 previously terminated WebContent; b95 does not reproduce that failure.
- WebContent termination cause: **Unverified**.
- automatic external terminal/final convergence: **not achieved in this sample / current behavior still insufficient**.
- Stable/Frozen Send: **No**.

## Newly exposed b95 scope mismatch

After the successful authoritative Reload returned no active trailing timeline, Root orchestration nevertheless created a fresh covered executor and started `coveredExecutor.observing mode=selection` around `17:09:40Z`.

This is narrower than the primary disconnect problem, but it conflicts with the documented b95 intent that a fresh external observer should be attached after Reload only when authoritative Detail still contains an active trailing response. Current Root orchestration calls `observeExternalResponseIfNeeded` unconditionally after manual Reload applies, and that helper can create an observer when no live snapshot exists.

Treat this as an evidence-backed cleanup item; do not confuse it with the primary automatic-continuation architecture.

## User-proposed Web -> Native transport handoff hypothesis

The user proposes reducing dependency on covered Web lifetime: use Web only to perform the official protected Send/bootstrap, then once Native has joined the response transport, let Native own continuation so later WebContent termination no longer affects the response.

This direction is technically coherent **only as an explicit transport handoff**, not as a direct transfer of the same Web fetch stream. A `ReadableStream` consumed by JavaScript belongs to the WKWebView/WebContent process; Native cannot inherit that exact in-flight reader after the process dies. Native needs a separately established server-supported continuation channel before Web becomes disposable.

Existing project evidence makes this worth investigating for client-owned turns:

- prior first-party protected Send probes observed early `resume_conversation_token` structure after HTTP200 SSE;
- external comparison research reports current implementations using a bootstrap sequence resembling `resume_conversation_token -> stream_handoff -> conversation_id / turn_exchange_id / topic_id -> shared WebSocket subscribe` for turns they themselves just submitted.

That evidence does not yet prove our production client can safely perform the handoff, and it does not prove the same mechanism exists for a response started on another device. For cross-device already-active responses, an authoritative Detail Sync exposes an active tail but not necessarily the original turn's handoff topic/token. Copying the official page's status/plural-read cadence into Native would merely recreate polling and remains rejected.

### Next research gate

Do not allocate a production b96 merely to replace Web continuation with guessed Native transport. First prove a server-issued handoff/realtime path with privacy-safe structural diagnostics:

1. **Client-owned Send:** capture whether the exact current protected-Send bootstrap exposes `resume_conversation_token`, `stream_handoff`, `turn_exchange_id`, `topic_id`, or equivalent server-issued continuation identity before terminal.
2. Determine whether Native can establish a matching continuation subscription/channel before the covered Web executor is released.
3. **Cross-device external response:** use first-party iOS/Web structural observation to determine whether an already-active external turn has an official realtime registration/topic/update path available without replaying or guessing the original Send state.
4. Web lifetime policy, if proven: `Web prepare -> one protected Send -> handoff candidate -> Native continuation confirmed -> Web releasable -> terminal`. If Web dies before handoff confirmation, fail/recover the existing operation without a duplicate Send. If Web dies after confirmed handoff, Web death should be irrelevant to continuation.

Until those gates are proven, existing ownership remains unchanged: official page owns continuation transport; `ConversationRepository` owns Native response/content; no Native polling, guessed resume/offset/topic, duplicate Send, retry/watchdog, or second response store.
