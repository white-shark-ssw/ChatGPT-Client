# DEV-send-stream b91 project live-continuation Runtime — 2026-09-03

## Identity

- Candidate / Build: `DEV-send-stream-0.1.0-b91` / `0.1.0 (91)`.
- Diagnostics source marker: `c5985f1e2e5d`, matching exact package source `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`.
- Device Runtime: iPhone / iOS 17.0.

## Decisive Runtime sequence

- One explicit `同步最新消息` at `11:10:43Z` fetched authoritative Detail and started external response generation 1 at `11:10:47Z` with one reasoning/timeline item.
- The retained b90 diagnostic then moved the executor WebView frontmost: `manual_sync_frontmost_ab`, `subviewIndex=1`, `visibleSiblingCountAbove=0` at `11:10:48Z`; focus subsequently reached `nativeFirstResponder=true` and `documentHasFocus=true`.
- Every recorded page-activation sample in this run remained `route=conversation`; the prior project canonicalization failure to `route=other` did not recur.
- At `11:10:55Z` the official page issued a matching `externalStreamStatusRequest`; `11:10:56Z` returned HTTP200 `IS_STREAMING` and emitted `externalStreamingObserved`.
- The official page then issued its own `/resume` with numeric offset 0; it returned HTTP404 JSON. The existing page-owned fallback path continued through repeated matching `stream_status` plus plural conversation snapshots; no Native resume/status request was synthesized.
- Native Repository live state advanced automatically without another manual Sync: service messages/tools progressed from `6 / 2` at `11:11:02Z` through `47 / 14` at `11:13:47Z`; reasoning characters progressed `194 -> 909`. Corresponding `coveredExecutor.externalSnapshot`, `liveResponse.externalSnapshot`, and `liveResponse.presentationApplied` events were emitted throughout.
- The user reported that the visible official Web was receiving the live data but could not return to the Native screen. Source explains this presentation issue: b91 intentionally retains the b90 diagnostic `hostView.bringSubviewToFront(webView)` and contains no balancing send-to-back operation in that rearm path. This is a diagnostic UI artifact, not a failure of Web -> bridge -> Repository live continuation.
- The app was force-quit/relaunched while the response was still active: the last pre-exit stream status remained `IS_STREAMING`, and the last snapshot had `finalCharacters=0`. Therefore this run does not validate automatic terminal/final convergence.

## Classification

- Project-scoped route identity parser: **Runtime Positive**.
- Existing official page-owned live continuation (`stream_status` + plural conversation snapshots after page-owned resume 404): **Runtime Positive**.
- Web -> bridge -> `ConversationRepository` progressive live projection: **Runtime Positive**.
- b90 frontmost diagnostic as a presentation mechanism: **Runtime Positive but not acceptable as final product UI**, because it leaves the WebView in front of Native UI.
- Automatic terminal/final convergence: **Unverified in this run** because the app was force-quit while `IS_STREAMING`.
- Stable/Frozen Send: **No**.

## Next exact action

Do not change transport ownership or add retry/polling/timer/watchdog/resume synthesis. The next product candidate must isolate only the presentation cleanup: retain the b91 scoped-route identity parser and existing page-owned continuation observation, remove the b90 `bringSubviewToFront(webView)` diagnostic so the executor remains covered, and keep all other variables unchanged. Then run a project-conversation Human Runtime test through both live progression and natural terminal/final completion without a second manual Sync.
