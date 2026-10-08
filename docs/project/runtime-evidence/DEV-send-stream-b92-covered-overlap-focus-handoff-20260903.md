# DEV-send-stream b92 covered overlap Runtime — 2026-09-03

## Identity

- Candidate: `DEV-send-stream-0.1.0-b92`
- Build: `0.1.0 (92)`
- Diagnostics source marker: `54b5803a74a1`
- Exact package source: `54b5803a74a123431f0a2a8e662a1a2fe874b3ca`
- Device: iPhone / iOS 17.0

## Runtime result

This run contains two overlapping conversations and separates three outcomes.

### 1. Covered external continuation is Runtime Positive

The first project conversation (`sha256:0df178903e95`) was manually synchronized once and rearmed with `manual_sync_covered`, `subviewIndex=0`, `visibleSiblingCountAbove=1`; Native UI remained frontmost. The project page remained `route=conversation`. Page-owned `stream_status` repeatedly returned HTTP200 `IS_STREAMING`, and external snapshots advanced without a second Sync from service messages/tools `5/2` through `54/18`; reasoning advanced to 781 characters. This proves b92 no longer needs the b90/b91 frontmost Web presentation for the already-established page-owned continuation path.

### 2. Client-owned protected Send/SSE terminal path is Runtime Positive

A second conversation (`sha256:6f429823a988`) was selected while the first external response remained active. `activeExecutorCount` became 2. The client-owned Send submitted successfully, received HTTP200 `text/event-stream`, streamed reasoning/tools/final, reached `finalCharacters=6073`, `reasoningCharacters=708`, timeline 18/tools 14, then emitted `terminal` at 12:01:34Z. The executor was released, authoritative reconcile ran automatically, Detail advanced visible messages 15 -> 17, `liveResponse.reconciled` fired, and `authoritativeReconcile.completed` reported `liveSnapshotCleared=true`. The local protected Send + SSE + natural terminal/final reconcile path is therefore Runtime Positive.

### 3. Overlap/reselection recovery is Runtime Negative

The first external conversation continued after the second executor was initially created, reaching service messages/tools `54/18` at 11:58:27Z. The second client-owned Send began at 11:58:29Z. Around that handoff the Web bridge recorded a `blur` event; after 11:58:25Z there were no further `externalStreamStatusResponse` events and after 11:58:27Z there were no further external snapshots for the first conversation. Returning to the first conversation at 12:01:45Z produced only `composer_ready`; its live snapshot remained frozen at reasoning 781 / timeline 21 / tools 18 / final 0 through 12:05:52Z.

A manual `同步最新消息` at 12:05:55Z then fetched authoritative Detail with visible messages 25, trailing reasoning/timeline/tool counts all zero, added one visible assistant message, and `liveResponse.externalDetailReconciled` cleared the stale external live presentation because the authoritative assistant had materialized.

Therefore b92 does not prove automatic external terminal/final convergence under overlapping executor activity. The failure is narrower than the original continuation bug: single selected covered continuation works; the stale state appears after focus/context handoff to another executor and is not automatically reacquired when the user selects the external-live conversation again.

## Source correlation

Current source keeps one `CoveredWebSendExecutor` per conversation. `releaseIdleExecutors(except:)` deliberately retains an executor whose external response is active because `isBusy` is `activeEvents != nil`. Starting a Send in another executor focuses that page's composer (`element.focus(...)`) before submit. When the user later reselects an already-active external conversation, `observeExistingConversation(..., forceReload: false)` only probes the composer when `currentConversationID` already matches; it does not restore `WKWebView` first-responder/document focus.

The exact executor identity of the bridge `blur` event is not logged, so focus handoff is not yet declared a final root cause. It is the strongest evidence-backed single-variable differential for the next A/B.

## Next exact action

Allocate the next candidate only to test selection-time focus reacquisition for an already-active external live response:

- on selecting a conversation whose Repository snapshot is active and `promptText` is empty, reuse its existing executor;
- reacquire Native/Web document focus without page reload and without changing route, continuation transport, Send transport, Repository ownership, status/resume protocol, cadence, or persistence;
- log a distinct selection-focus-rearm stage/result;
- repeat the same overlap test: external response -> switch conversation -> client-owned Send -> return to external conversation, with no manual Sync after returning.

Success requires page-owned `stream_status` / external snapshots to resume after reselection and eventually natural authoritative final reconciliation. Failure rejects focus reacquisition as sufficient. No polling, retry/watchdog, Native `stream_status`/`resume`, guessed offset, duplicate Send, WebSocket-body authority, or second response store is permitted.
