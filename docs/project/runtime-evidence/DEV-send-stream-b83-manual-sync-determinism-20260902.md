# DEV-send-stream b83 manual Sync determinism — 2026-09-02

## Candidate

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b83`
- Version / Build: `0.1.0 (83)`
- Exact product/config source: `12e3c27138ebc81cbbae6236347122f79e03bf08`
- Clean CI/package head: `3771ddccc8d0847ce28f72acbbe311aaf30b7482`
- PR: #29
- Canonical Artifact: `9819681774`
- IPA SHA-256: `46f06106c3d47b3845a584665666fb6cb6d39cd66c0c9415412702e81795be97`

## MVP boundary

- client-owned Send keeps the existing true SSE stream;
- cross-platform responses may use genuine block/page-snapshot progressive reasoning/tool updates;
- explicit manual Sync must reliably acquire the active cross-platform reasoning path;
- automatic remote-turn discovery, cross-platform token-level SSE parity and progressive external final-token streaming are deferred.

## Source defect fixed by b83

Before b83, a successful manual Sync reached the covered-page force-rearm path only when `latestUserChanged == true`. This was a real source defect because a remote user row could already be present locally while the reasoning response was still unattached; another successful Sync would then skip the only explicit force re-arm.

b83 removed that gate while preserving the same-conversation and no-active-live-response guards. No client-owned SSE, polling, timer, retry loop, duplicate Send, response ownership or WebSocket-body authority changed.

## Exact b83 real-device result — Runtime Rejected

The uploaded diagnostic export identifies the tested package as:

- `appVersion = 0.1.0`
- `buildNumber = 83`
- `candidate = DEV-send-stream-0.1.0-b83`
- `sourceCommit = 3771ddccc8d0`
- `systemVersion = 17.0`

Target conversation hash in the export: `sha256:d597360f6d29`.

The user pressed manual Sync repeatedly while the remote turn was still active. The log proves the b83 callback correction executed: successful `latestSync` operations repeatedly emitted `coveredExecutor.observing mode=manual_sync_rearm`.

Representative chronology:

- `20:53:47 -> 20:53:50`: Sync HTTP200, visible `21 -> 21`, then `manual_sync_rearm`; page loaded at `20:53:51`.
- `20:53:54 -> 20:53:57`: Sync HTTP200, visible `21 -> 22`, `mappingCount=1020`; re-arm at `20:53:58`; page loaded at `20:54:01`.
- `20:54:12 -> 20:54:15`: Sync HTTP200, visible stays `22`, `mappingCount=1027`; re-arm emitted; one navigation reported `NSURLErrorDomain -999`, then a page still loaded at `20:54:20`.
- full Detail reload at `20:54:26 -> 20:54:29`: visible stays `22`, `mappingCount=1033`.
- `20:54:38 -> 20:54:41`: Sync HTTP200, visible stays `22`, `mappingCount=1038`; clean re-arm; page loaded at `20:54:42`.
- `20:54:58 -> 20:55:01`: Sync HTTP200, visible stays `22`, `mappingCount=1043`; another re-arm; one navigation reported `-999`.
- `20:55:08 -> 20:55:10`: Sync HTTP200, visible stays `22`, `mappingCount=1043`; re-arm; page loaded at `20:55:17`; a later background interval terminated that Web process at `20:55:27`.
- `20:55:32 -> 20:55:35`: Sync HTTP200 finally advances visible `22 -> 23`, `mappingCount=1049`; page loads again at `20:55:37`.
- at `20:55:47+`, reasoning disclosure interactions are explicitly logged on `surface=historical`.

Throughout the active period, `livePresentationRowCount` remained `0`. The export contains no accepted `external_page_owned` response acquisition, live reasoning snapshot adoption or live-response presentation. The observed user-socket structural frames in this export were `targetMatch=false`.

## Strong new Runtime clue

The authoritative Detail payload changed materially during generation even while the visible message count remained `22`:

- `mappingCount`: `1020 -> 1027 -> 1033 -> 1038 -> 1043`
- `filteredRecipientMessageCount`: `427 -> 430 -> 433 -> 434 -> 436`
- response byte count also grew on successive requests.

Only later did visible count become `23` and the completed reasoning appear as historical presentation.

Therefore the active server-side Detail graph is evolving before the current Native visible projection exposes a new assistant message.

## Rejection conclusion

- The former `latestUserChanged` gate was real and b83 fixed it.
- That correction is **insufficient**: repeated explicit Sync + force re-arm did not deterministically acquire the active reasoning stream.
- `NSURLErrorDomain -999` and one Web-process termination are real runtime noise, but they cannot be the sole root cause because several clean page loads also failed to acquire reasoning.
- Covered-page re-arm is therefore not accepted as a deterministic manual reasoning-acquisition mechanism.

b83 is **Runtime Rejected** for the current manual cross-platform block-stream MVP and remains permanently reserved.

## Current source-backed next question

`ConversationRepository.parseCurrentBranch` accumulates an already-presentational `pendingTimeline` from recognized reasoning recap/thinking-preamble/tool events and only attaches that timeline when a visible assistant message is appended. If parsing ends while an active response has a trailing pending timeline but no visible assistant body yet, the current return value drops that trailing timeline.

The same parser explicitly skips raw assistant content types `thoughts` and `inline_cot_expandable_content`. Those skipped raw types are **not authorized for presentation** and must remain non-presentational unless separate user-visible service evidence exists.

## b84 diagnostic gate

Allocate b84 only for privacy-safe structural Detail-projection diagnostics. It must record integer counts/classifications only, including whether parsing ends with a non-empty already-authorized pending timeline. It must not export prompt text, reasoning text, final text, tool bodies, auth/session/challenge data, signed query values, or raw hidden chain-of-thought.

If b84 proves a trailing presentational timeline exists during active manual Sync, use that evidence for the next minimal projection/acquisition design. If it is absent, reassess the data source rather than exposing skipped raw thoughts or adding speculative polling.

## Evidence classification

- b82 manual-Sync stability: **Runtime Rejected**
- b83 source defect: **Fixed**
- b83 Code written: **Yes**
- b83 Push/PR CI: **Passed**
- b83 Artifact/package identity: **Verified**
- b83 real-device Runtime: **Rejected**
- active authoritative Detail graph evolution: **Runtime Confirmed**
- trailing already-presentational pending timeline during active Detail: **Unknown / b84 target**
- Stable/Frozen Send: **No**
