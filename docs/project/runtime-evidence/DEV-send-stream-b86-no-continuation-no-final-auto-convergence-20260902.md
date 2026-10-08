# DEV-send-stream b86 Runtime — no page continuation and no automatic final convergence

_Date: 2026-09-02_

## Identity

- Candidate: `DEV-send-stream-0.1.0-b86`
- Version / Build: `0.1.0 (86)`
- Package source marker: `f90caca0419f`
- Exact diagnostics product source: `dc77a94be5b2f7eecd822480f759358ad6a0ad25`
- Canonical Artifact: `9823485856`
- IPA SHA-256: `25d483ac31473b124e6ad555b79c488e78da91ec1761ee8a40076b6e978bee6f`
- Device: iPhone / iOS 17.0

## Runtime result

**Diagnostic Runtime Positive / continuation activation absent. Automatic final convergence also absent in this exact run.**

The supplied diagnostics export proves the b86 structural instrumentation worked as intended and that the covered official page did **not** enter the current page-owned continuation flow.

## Decisive timeline

Target conversation hash in the privacy-safe log: `sha256:d597360f6d29`.

1. `07:15:10` explicit `同步最新消息` started.
2. `07:15:20` authoritative Detail returned HTTP200 with an active presentational tail:
   - visible messages `34`;
   - `trailingTimelineItemCount=6`;
   - reasoning `1`;
   - tools `5`.
3. The same authoritative tail created `responseGeneration=1` via `external_authoritative_detail`; one live row was rendered.
4. `07:15:21` covered executor re-armed in `manual_sync_rearm` mode.
5. `07:15:22` target page reported `state=loaded`.
6. From that clean page load until the next explicit Sync at `07:16:37` — about **75 seconds** — the diagnostics contain **zero**:
   - `coveredExecutor.externalStreamStatusRequest`;
   - `coveredExecutor.externalStreamStatusResponse`;
   - `coveredExecutor.externalResumeRequest`;
   - `coveredExecutor.externalResumeObserved`;
   - `coveredExecutor.resumeResponse`;
   - `coveredExecutor.externalStreamingObserved`;
   - page-owned `externalSnapshot` / Repository `externalSnapshot`.
7. A user WebSocket was created/opened and produced a 371-byte JSON-array message, but its structural classification was `hasConversationKey=false` and `targetMatch=false`. Therefore the current exact-conversation `externalAcquisitionHint` path did not fire.
8. `07:16:37` the user explicitly pressed Sync again.
9. `07:16:43` authoritative Detail returned visible messages `35`, trailing timeline `0`; `liveResponse.externalDetailReconciled` recorded `authoritative_assistant_materialized` and cleared the live row.

Therefore the complete assistant answer was available through authoritative Detail by the final manual Sync, but this exact run had **no automatic completion/update trigger** that caused the client to fetch it before that manual action.

## Comparison with visible official Web evidence

Previously recorded visible-Web Rule Lab evidence used the same default persistent `WKWebsiteDataStore`. After the user visibly entered an externally active target conversation, the page itself issued:

`stream_status -> resume {conversation_id, offset}`

within roughly two seconds of target-conversation entry; in that recorded run resume returned 404 and the visible page then continued with repeated page-owned `stream_status + /backend-api/conversations/{conversation}` reads.

Exact b86 is materially different: the covered programmatic `/c/<id>` load completed while authoritative Detail independently proved active reasoning existed, yet the page issued **no matching `stream_status` at all** for at least 75 seconds.

This strengthens the current working hypothesis that the remaining differential is **official page activation/navigation/visibility/focus state**, not server inability to provide continuation. It does not prove which page-state field or user action is causal.

## Architectural consequence

- b85 authoritative Detail block projection remains Runtime Positive.
- b86 proves the next bottleneck is *before* resume/offset: covered page continuation activation did not start.
- Do not spend the next change guessing `/resume` offset; no resume request existed in this run.
- Do not add polling/timers/retries/watchdogs or a second state authority to compensate.
- The b82 user-socket exact-target signal remains opportunistic only; `targetMatch=false` in this run demonstrates it is not a reliable completion convergence source.
- The recorded future one-shot Sync-on-conversation-entry requirement remains useful for freshness on navigation but does not solve post-entry continuation/completion by itself.

## Next evidence target

Compare the covered page's activation state against the known-good visible Web entry path, focusing on privacy-safe structure only:

- `document.visibilityState` / `document.hidden`;
- `document.hasFocus()`;
- page route/readiness at and shortly after `didFinish`;
- Native WebView window attachment / hidden / alpha / bounds state;
- whether a user-visible entry/activation transition is the event that causes official Web to issue `stream_status`.

No behavior change is authorized solely from this b86 result.
