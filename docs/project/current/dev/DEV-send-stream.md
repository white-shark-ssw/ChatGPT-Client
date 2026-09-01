# DEV-send-stream

## Status

**Active — b85 real-device Runtime is Partial Positive / MVP continuation Rejected. Explicit Sync reliably projects authoritative trailing reasoning/tool blocks and reconciles final materialization, but each newer block required another Sync; no page-owned continuation/SSE/plural snapshot attached. Exact source inspection proves current diagnostics cannot tell whether the official page never requested `stream_status` or requested it and received a non-`IS_STREAMING` result. b86 is now allocated as diagnostics-only to expose that structural gap. No acquisition behavior changes are authorized. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Branch head before b86 allocation checkpoint: `5ba29671c2949ed82b587884861b8837637548d8`
- b85 product/config source: `ec64dd170a6386612af8cb68b394045ce3c85313`
- b85 package head: `6be1e8a8bafa80ef09c6fcebff014006de264e0f`
- b85 Candidate / Build: `DEV-send-stream-0.1.0-b85` / `0.1.0 (85)`
- b85 canonical Artifact: `9822441595`
- b85 IPA SHA-256: `f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`
- b85 Runtime upload: exact Candidate b85 / source `6be1e8a8bafa` / iOS17.0
- b86 Candidate: **allocated** `DEV-send-stream-0.1.0-b86` / `0.1.0 (86)`
- b86 scope: **diagnostics only**; no product acquisition/state behavior change
- b39-b86 permanently reserved once b86 source is committed
- Stable/Frozen Send: No

## Send MVP contract

### Client-owned Send

Preserve the existing true SSE response stream.

### Cross-platform Send

Block/page-snapshot progressive reasoning/tool updates are acceptable for MVP, but one explicit Sync must be a stable acquisition/re-arm boundary: it should expose the newest authoritative block, then later genuine blocks should be able to continue without pressing Sync for every block when the external response remains active. No fake typewriter, duplicate Send, polling/timer/watchdog/retry loop, second response store or raw hidden-thought presentation.

The user has explicitly reopened the narrower investigation of whether the newly proven authoritative active-Detail anchor can help establish true page-owned cross-platform SSE continuation. This does not authorize guessed Native `/resume` or offset construction.

## b84/b85 Runtime facts

b84 proved authoritative Detail can expose a presentational trailing timeline during active generation before a visible assistant row exists.

b85 then proved on real device that the same external `responseGeneration=1` advances via explicit Sync:

- `22:17:34`: timeline **1 = reasoning 1**;
- `22:18:29`: timeline **5 = reasoning 1 + tools 4**;
- `22:19:39`: timeline **7 = reasoning 2 + tools 5**;
- `22:20:38`: visible assistant materialized, trailing timeline 0, `externalDetailReconciled` cleared the live row.

So b85 Native Detail projection, repeated same-owner updates and final reconciliation are Runtime Positive.

But after each active Sync, `manual_sync_rearm` and covered page `state=loaded` occurred with **zero**:

- `coveredExecutor.externalStreamingObserved`;
- `coveredExecutor.externalSnapshot` / `liveResponse.externalSnapshot`;
- `coveredExecutor.externalResumeObserved`;
- `coveredExecutor.resumeResponse`.

User observation matches: every Sync exposed another part of reasoning, with no automatic continuation between presses.

Durable Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b85-manual-block-no-auto-continuation-20260902.md`.

### Lifecycle qualification

The app moved between foreground/background several times and the covered user WebSocket later errored/closed. Some post-rearm foreground windows were only several seconds. This is enough to reject *reliable* one-Sync continuation for the MVP, but not enough to prove a permanently foreground page can never attach. Previous clean-load failures show backgrounding is not the sole explanation.

## Current source finding

`CoveredWebSendExecutor` already allows a page-owned continuation to reuse an active external generation whose `promptText` is empty, so b85 response ownership is not blocking continuation.

The bridge currently:

- intercepts matching page-owned `stream_status`;
- emits `external_streaming` only if HTTP200 JSON parses to `status == IS_STREAMING`;
- emits no diagnostic event for a matching non-200/non-`IS_STREAMING` `stream_status` response;
- observes matching `/resume` and logs its HTTP status/content type, but does not export offset structure/value;
- can consume page-owned `/resume` HTTP200 SSE or page-owned plural snapshots when those requests actually happen.

Therefore the next missing evidence is page-owned continuation **activation**, not another Native projection fix.

## b86 diagnostics-only scope

b86 may change only `CoveredWebSendExecutor` diagnostics plus build/Candidate identity:

1. log that a matching page-owned `stream_status` request occurred;
2. log its HTTP status and bounded status token (`IS_STREAMING`, `COMPLETE`, other/empty), never body text;
3. when a matching page-owned `/resume` occurs, log only whether `offset` exists, its primitive type, and a safe integer offset value when present;
4. keep existing resume HTTP status/content-type logging;
5. do not issue any new network request, reload, timer, poll, retry, resume or Send;
6. do not persist/export auth headers, cookies, challenge values, message/reasoning bodies or raw IDs.

If b86 shows no matching `stream_status` request after a foreground-held re-arm, the next research target is the official page state/action that starts continuation. If `stream_status=IS_STREAMING` occurs and `/resume` follows, compare the page-owned offset/request sequence with historical HTTP200-SSE evidence. If resume is HTTP200 SSE, validate existing parser/owner continuation before any new product change.

## Recorded later requirement

Entering/selecting a conversation should eventually perform exactly one authoritative latest-message Sync attempt. This one-shot entry refresh does not itself create continuation and remains separate from b86.

## Evidence ladder

- b83 manual covered-page acquisition: **Runtime Rejected**
- b84 active authoritative trailing timeline: **Runtime Positive**
- b85 Code/CI/Artifact: **Verified**
- b85 explicit manual Detail block projection: **Runtime Positive**
- b85 repeated Sync same response generation: **Runtime Positive**
- b85 final reconcile: **Runtime Positive**
- b85 automatic continuation after one Sync: **Runtime Rejected for reliability**
- b85 true cross-platform SSE: **Not acquired**
- b86 Code/CI/Artifact: **Pending**
- Stable/Frozen Send: **No**

## Batch recovery point — b86 diagnostics candidate

Verified before allocation:

- branch/PR: `dev/send-stream-20260829`, PR #29 open/mergeable;
- actual branch before this checkpoint: `5ba29671c2949ed82b587884861b8837637548d8`;
- base/main remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- current product identity is b85; project Debug+Release both `CURRENT_PROJECT_VERSION=85` / Candidate b85;
- `BUILD_TEST_INDEX.md` contains no exact `DEV-send-stream-0.1.0-b86` identity;
- current `docs/project/current/dev/` contains only this active Send task plus its historical round7 addendum, so no parallel Active checkpoint/candidate conflict is visible.

Planned small write batches:

1. **Completed:** b85 Runtime checkpoint + durable b85 Runtime evidence file.
2. **Current:** stage exact b86 diagnostics-only source + `0.1.0 (86)` identity; verify exact diff.
3. Restore normal b86 build workflow, run Push+PR CI, verify canonical IPA identity.
4. Update `BUILD_TEST_INDEX.md`, `MODULE_STATUS.md`, checkpoint and PR #29 with b85 Runtime + b86 diagnostic identity.
5. Human gate: install exact b86 and keep the client foreground after one Sync/re-arm long enough to capture page-owned `stream_status` / resume structure.

Recovery must not modify b85 product source/history, client-owned SSE, b80 Frozen presentation/final boundaries, automatic-discovery scope, or hidden-thought rules.

## Session round counter

This user turn is **round 17**.
