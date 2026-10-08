# DEV-send-stream b85 manual block / automatic continuation Runtime — 2026-09-02

## Identity

- Candidate: `DEV-send-stream-0.1.0-b85`
- App: `0.1.0 (85)` Release
- Runtime source marker: `6be1e8a8bafa`
- Product/config source: `ec64dd170a6386612af8cb68b394045ce3c85313`
- Canonical Artifact: `9822441595`
- IPA SHA-256: `f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`
- Device: iPhone / iOS17.0
- Target conversation marker: `sha256:d597360f6d29`
- User observation: each press of `同步最新消息` immediately revealed another portion of the reasoning/tool timeline, but the response did not continue updating automatically between Sync actions.

## Exact Runtime chronology

### First explicit Sync

- `22:17:29Z` `conversation.latestSync.requested`.
- `22:17:34Z` authoritative Detail HTTP200: visible messages `29 -> 30`, mapping `1622`, trailing timeline `1`, reasoning `1`, tools `0`.
- `22:17:34Z` `liveResponse.started`, source `external_authoritative_detail`, generation `1`.
- Same time `liveResponse.externalDetailSnapshot`: generation `1`, timeline `1`, reasoning `1`, tools `0`.
- Live presentation row appears.
- `manual_sync_rearm` then covered page `loaded` at `22:17:35Z`.

### Second explicit Sync

- `22:18:23Z` requested.
- `22:18:29Z` Detail HTTP200: visible still `30`, mapping `1630`, trailing timeline `5`, reasoning `1`, tools `4`.
- Same existing `responseGeneration=1` receives `externalDetailSnapshot timeline=5`.
- `manual_sync_rearm`; covered page `loaded` at `22:18:30Z`.

### Third explicit Sync

- `22:19:35Z` requested.
- `22:19:39Z` Detail HTTP200: visible still `30`, mapping `1637`, trailing timeline `7`, reasoning `2`, tools `5`.
- Same existing generation `1` receives `externalDetailSnapshot timeline=7`.
- `manual_sync_rearm`; covered page `loaded` at `22:19:42Z`.

### Completion reconcile

- `22:20:34Z` requested.
- `22:20:38Z` Detail HTTP200: visible `31`, trailing timeline `0`.
- `liveResponse.externalDetailReconciled`, generation `1`, reason `authoritative_assistant_materialized`.
- Live presentation row clears and completed historical content becomes authoritative.

## Automatic continuation evidence

Across the uploaded export there are no events for:

- `coveredExecutor.externalStreamingObserved`;
- `coveredExecutor.externalSnapshot`;
- `liveResponse.externalSnapshot`;
- `coveredExecutor.externalResumeObserved`;
- `coveredExecutor.resumeResponse`.

Yet each manual re-arm reports covered page `state=loaded`.

Therefore b85's authoritative Detail projection and same-generation response ownership work on device, but the official page did not enter the currently observed external continuation transport during this sample. No page-owned reasoning/SSE/plural snapshot updated the response between explicit Syncs.

## Lifecycle qualification

The app moved between foreground/background several times during the run; covered user-WebSocket structure later reported error/close. Several page-rearm foreground windows were only a few seconds. This means the export is sufficient to reject *reliable* automatic continuation for the current MVP, but it does not prove a permanently foreground page could never attach later.

Prior b83/b84 samples already show repeated clean page loads can also fail to acquire, so background transitions are not accepted as the sole explanation.

## Source interpretation

Current bridge source only emits `external_streaming` after a matching page-owned `stream_status` response parses as `IS_STREAMING`. It logs `resumeResponse` only when a matching page-owned resume request is observed. Because neither event family appears here, existing diagnostics cannot distinguish:

1. no matching `stream_status` request happened, or
2. it happened but returned a non-200/non-`IS_STREAMING` state that the bridge currently does not log.

The b85 Native response owner is not the blocker: repeated authoritative Detail updates stayed on generation `1`, and current observer code explicitly permits page continuation to reuse an active external generation whose prompt text is empty.

## Classification

- b85 manual authoritative block acquisition: **Runtime Positive**.
- b85 repeated explicit Sync progression: **Runtime Positive** (`1 -> 5 -> 7` timeline items on one response generation).
- b85 final authoritative materialization/reconcile: **Runtime Positive**.
- b85 automatic page-owned continuation after one Sync: **Runtime Rejected for reliability in this sample**.
- b85 true cross-platform SSE continuation: **Not acquired**.
- Stable/Frozen Send: **No**.

## Next evidence

Do not add polling, timers, retries, guessed Native `/resume`, guessed `offset`, duplicate Send/resend, or a second response store.

The smallest missing evidence is page-owned network structure after re-arm:

- whether matching `stream_status` was requested;
- HTTP status and parsed status token (`IS_STREAMING`, `COMPLETE`, other/invalid), without content bodies;
- whether a matching `/resume` request occurred;
- whether its request shape contains an offset and the offset's primitive type/number, without headers/auth/challenge values;
- resume HTTP status/content-type.

A diagnostics-only next candidate is justified if the current bridge cannot emit those facts.
