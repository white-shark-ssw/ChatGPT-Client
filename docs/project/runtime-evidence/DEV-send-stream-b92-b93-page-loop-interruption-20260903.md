# DEV-send-stream b92/b93 page-owned continuation interruption Runtime evidence — 2026-09-03

## Scope

This evidence compares two exact real-device diagnostic exports supplied by the user on iPhone / iOS 17.0.

- b92: Candidate `DEV-send-stream-0.1.0-b92`, Build `0.1.0 (92)`, source `54b5803a74a1`.
- b93: Candidate `DEV-send-stream-0.1.0-b93`, Build `0.1.0 (93)`, source `2d2cde58a7fb`.

The files are Runtime evidence. They do not by themselves authorize Native `stream_status`, `/resume`, polling/cadence reproduction, retry/watchdog, duplicate Send, WebSocket-body authority, or a second response store.

## b92 — single executor / foreground-background interruption

This run used only one selected external conversation and one covered executor (`activeExecutorCount=1`). There is no second conversation/executor handoff in the run.

After page-owned continuation acquired the remote response, the official page repeatedly issued matching `externalStreamStatusRequest` and received HTTP200 `IS_STREAMING`. Native external snapshots advanced automatically from service/tool `34/14` through `79/29`, then after the first foreground return to `86/32` and finally `88/33` at `12:13:31Z`.

The decisive interruption is lifecycle-bound:

- `12:13:29Z` — `willResignActive`.
- `12:13:30Z` — last `externalStreamStatusRequest`.
- `12:13:31Z` — last HTTP200 `IS_STREAMING` response, last external snapshot `serviceMessageCount=88 / toolCount=33`, and `didEnterBackground`.
- `12:15:18Z` — app returns foreground; page reports `visibilityState=visible`, WebSocket reports error/close and later recreates/reopens.
- Subsequent foreground periods continue to show page/DOM/WebSocket activity, but there is no further page-owned `externalStreamStatusRequest/Response` and no further external snapshot.
- `12:19:46Z` — explicit `同步最新消息` is finally requested.
- `12:19:48Z` — authoritative Detail adds the completed assistant (`visible 1 -> 2`) and `liveResponse.externalDetailReconciled` clears the stale external live response.

Classification: **single-executor covered continuation is Runtime Positive while the official page-owned acquisition loop remains alive; a real background lifecycle transition can terminate that loop; ordinary foreground visibility/WebSocket reconnection does not restart it.**

This rejects the earlier interpretation that a second executor/focus handoff is necessary to reproduce the terminal freeze.

## b93 — selection focus reacquisition is not sufficient

b93 exact package identity is confirmed by the diagnostic metadata.

The run proves the b93 mechanism itself works:

- when the external-live conversation is reselected at `13:05:31Z`, `selection_external_focus_rearm` runs;
- `nativeFirstResponder=true` and `documentHasFocus=true`;
- page-owned status/snapshot continuation continues afterward (`19/7 -> ... -> 78/18`).

Later the same external response reaches a decisive negative reselection sequence:

- `13:07:27Z` — status HTTP200 `IS_STREAMING`.
- `13:07:29Z` — external snapshot `serviceMessageCount=78 / toolCount=18`.
- `13:07:31Z` — reselect external conversation; focus rearm again succeeds with `documentHasFocus=true`.
- `13:07:34Z` / `13:07:35Z` — one more page-owned status request/HTTP200 `IS_STREAMING`.
- `13:07:37Z` — last external snapshot `serviceMessageCount=80 / toolCount=19`, final text still 0.
- `13:07:38Z` — switch away to the other conversation.
- `13:07:42Z` — return to the external-live conversation; `selection_external_focus_rearm` again reports `nativeFirstResponder=true` and `documentHasFocus=true`.
- `13:07:47Z` — another focus-rearm sample again reports both true.
- Despite successful focus reacquisition, there is no later page-owned `externalStreamStatusRequest/Response` and no later external snapshot through the stale-live interval.
- `13:10:24Z` — explicit Sync is requested.
- `13:10:28Z` — authoritative Detail adds the completed assistant (`visible 26 -> 27`) and `liveResponse.externalDetailReconciled` clears the stale external response.

Classification: **b93 first-responder/document-focus reacquisition is Runtime Positive as a mechanism, but Rejected as a sufficient recovery condition for a stopped official page-owned continuation loop.**

## Combined conclusion

The two runs narrow the failure substantially:

1. The Native `ConversationRepository` is not the origin of the stall; while page-owned snapshots arrive it projects them, and explicit authoritative Detail later materializes the completed assistant correctly.
2. The protected client-owned Send/SSE path remains separately proven by the prior b92 overlap run and is not contradicted here.
3. A second executor is not required for the external continuation loop to stop; b92 reproduces it with one executor after background lifecycle interruption.
4. `becomeFirstResponder()` / `document.hasFocus=true` is not sufficient to restart a loop that has already stopped; b93 proves this directly.
5. The strongest common differential is now the lifetime of the **official page-owned continuation acquisition loop** itself. Once that first-party page lifecycle stops issuing `stream_status`, Native receives no further authoritative page snapshots even though the remote response can later be present in Detail.
6. The only currently proven action that re-establishes page-owned acquisition after a stopped interval is the existing manual-Sync page rearm, which performs a real official conversation page load. This supports testing page lifecycle rebootstrap, not Native protocol synthesis.

## Next exact A/B

Allocate the next candidate only for the cleanest single-variable reproduction first: **foreground reactivation of an already-active external response**.

- Use exact b93 as the base behavior except for the new A/B.
- Keep one external conversation/executor only.
- After page-owned continuation is demonstrably advancing, background ChatGPTClient while the remote response remains active, then return foreground.
- On foreground, if the selected Repository snapshot is an active external response (`promptText` empty), rebootstrap the existing official executor page for that same conversation **without performing Native Detail Sync**.
- The rebootstrap must remain first-party page-owned: no Native `stream_status`, `/resume`, guessed offset, polling/cadence reproduction, retry/watchdog, duplicate Send, WebSocket-body authority, or second response store.
- Log a distinct foreground page-rebootstrap stage so Runtime can distinguish it from manual Sync and selection focus rearm.

Decisive Runtime Positive: after foreground rebootstrap, the official page again emits matching `externalStreamStatusRequest/Response`, external snapshots resume, and the remote assistant naturally reaches final/reconcile without pressing Sync.

If foreground page rebootstrap succeeds, selection-triggered page rebootstrap remains a separate later A/B for the b93 reselection failure. If it fails while exact page load completes and the remote response demonstrably advances, reject page reload as sufficient and continue from that evidence.