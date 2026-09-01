# DEV-send-stream

## Status

**Active — b85 real-device Runtime is Partial Positive / MVP continuation Rejected. Explicit Sync reliably projects authoritative active reasoning/tool blocks and final reconciliation works, but every newer block required another explicit Sync; no page-owned continuation/SSE/plural snapshot attached. Exact b86 is diagnostics-only and is now Code/Push+PR CI/Artifact/package verified, Runtime Pending. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Current branch before this checkpoint write: `ffb30477e7f30f0448a3e5f9b4e35c1002b1899f`
- b85 exact product/config source: `ec64dd170a6386612af8cb68b394045ce3c85313`
- b85 canonical Artifact: `9822441595`
- b85 IPA SHA-256: `f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`
- b85 Runtime: **manual block Positive / automatic continuation Rejected for reliability**
- b86 exact diagnostics product source: `dc77a94be5b2f7eecd822480f759358ad6a0ad25`
- b86 clean Push package head: `f90caca0419f13254567485171fac7d970aa8c95`
- b86 Candidate / Build: `DEV-send-stream-0.1.0-b86` / `0.1.0 (86)`
- b86 Push run/job: `33566939415 / 100052171917` — success
- b86 PR run/job: `33566968066 / 100052259409` — success
- b86 canonical Artifact: `9823485856`
- b86 ZIP digest: `sha256:cdccdcd034964b99e98e62c2e79a9bece96c190138c774e6f1590896d54fbacb`
- b86 IPA SHA-256: `25d483ac31473b124e6ad555b79c488e78da91ec1761ee8a40076b6e978bee6f`
- b86 package: `0.1.0 (86)` / Candidate b86 / source `f90caca0419f` / iOS14 minimum / arm64
- b39-b86 permanently reserved
- Stable/Frozen Send: No

## Send MVP contract

### Client-owned Send

Preserve the existing true same-response SSE. Do not downgrade it.

### Cross-platform Send

Real block/page-snapshot reasoning/tool progression is acceptable for MVP, but explicit `同步最新消息` must be a stable acquisition/re-arm boundary: one Sync should expose the newest authoritative block and, if the external response remains active, later genuine blocks should continue without pressing Sync for every block when the page-owned continuation path attaches.

Do not satisfy this with fake typewriter, polling, timer, watchdog, speculative retry/fallback, duplicate Send/resend, a second response store, guessed Native resume/offset, WebSocket-body authority, or raw hidden-thought presentation.

The user has explicitly reopened only the narrower research question of whether the newly proven authoritative active-Detail anchor can help establish true page-owned cross-platform SSE continuation. Automatic remote-turn discovery, progressive external final-token streaming, and official-native realtime production integration remain separate/deferred.

## b84/b85 decisive Runtime

b84 proved authoritative Detail can expose already-presentational active trailing reasoning/tool timeline before a visible assistant row exists.

Exact b85 real-device diagnostics then proved one external `responseGeneration=1` advances only on explicit Sync:

- `22:17:34`: trailing timeline **1 = reasoning 1**;
- `22:18:29`: timeline **5 = reasoning 1 + tools 4**;
- `22:19:39`: timeline **7 = reasoning 2 + tools 5**;
- `22:20:38`: visible assistant materialized, trailing timeline 0, `externalDetailReconciled` cleared the live row.

Therefore b85 Native Detail projection, repeated same-owner updates and final materialization/reconciliation are Runtime Positive.

But after each active Sync, `manual_sync_rearm` and covered page `state=loaded` occurred with zero:

- `coveredExecutor.externalStreamingObserved`;
- `coveredExecutor.externalSnapshot` / `liveResponse.externalSnapshot`;
- `coveredExecutor.externalResumeObserved`;
- `coveredExecutor.resumeResponse`.

The user observation exactly matches the export: each Sync reveals another part of reasoning, with no automatic continuation between Sync actions.

Durable Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b85-manual-block-no-auto-continuation-20260902.md`.

### Lifecycle qualification

The b85 sample entered background several times shortly after re-arm and covered WebSocket later errored/closed; some foreground windows were only about 3–6 seconds. Therefore this sample rejects *reliable* automatic continuation for MVP but does not prove a permanently foreground page can never attach. Earlier b83/b84 clean-load failures show backgrounding is not the sole explanation.

## Remaining bottleneck

Current b85 source already permits a page-owned continuation to reuse an active external response whose prompt text is empty, so the Detail-backed response owner is not blocking continuation.

The remaining bottleneck is **official page continuation activation**:

- Does the re-armed official page actually issue matching `stream_status`?
- If yes, what HTTP/status token does it receive?
- Does it issue matching `/resume`?
- If yes, what page-owned offset does it use and what response does it receive?

Historical exact Runtime already proves official Web can perform cross-device:

`stream_status -> POST /backend-api/f/conversation/resume {conversation_id, offset} -> HTTP200 text/event-stream`

and other runs can use resume 404 followed by page-owned plural snapshots. Native must not synthesize either path.

## b86 diagnostics-only implementation

Exact b86 product commit changes only `RootViewController.swift` diagnostics/bridge structure and build/Candidate identity. It adds:

- `coveredExecutor.externalStreamStatusRequest`;
- `coveredExecutor.externalStreamStatusResponse` with HTTP status + bounded `streamState` token;
- `coveredExecutor.externalResumeRequest` with only `hasOffset`, primitive `offsetType`, and safe integer `offsetValue` when present;
- existing resume observed/response diagnostics remain.

No new request, reload cadence, polling, retry, timer, watchdog, resume, offset choice, Send or response owner was added. Prompt/answer/reasoning/tool bodies, Cookie/Authorization/challenge values and raw conversation IDs remain excluded.

Durable build evidence: `docs/project/runtime-evidence/DEV-send-stream-b86-continuation-diagnostics-build-20260902.md`.

## Durable docs synchronized

- `BUILD_TEST_INDEX.md`: b85 Runtime updated to manual-block Positive / auto-continuation Rejected; b86 exact identity added as Runtime Pending.
- `MODULE_STATUS.md`: top Send override now records b85 Runtime and b86 diagnostics-only scope.
- `TECHNICAL_DECISIONS.md`: b85 Runtime / b86 continuation diagnostics qualification added.
- PR #29 title/body updated to the b86 gate.
- Temporary b86 staging and docs-maintenance scripts/workflows have been removed from the current branch.

## Recorded later requirement — one Sync on conversation entry

Entering/selecting a conversation should eventually perform exactly one authoritative latest-message Sync attempt through `ConversationRepository`. This one-shot entry refresh remains separate from b86 and does not itself solve continuation.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- default persistent WebKit store remains sole persistent auth-secret authority.
- no raw hidden-thought presentation.

## Evidence ladder

- b83 covered-page manual acquisition: **Runtime Rejected**
- b84 active authoritative trailing timeline: **Runtime Positive**
- b85 explicit manual Detail block projection: **Runtime Positive**
- b85 repeated Sync same response generation: **Runtime Positive**
- b85 final authoritative reconcile: **Runtime Positive**
- b85 automatic page-owned continuation after one Sync: **Runtime Rejected for reliability**
- b85 true cross-platform SSE continuation: **Not acquired**
- b86 Code written: **Yes**
- b86 guarded staging / `git diff --check`: **Passed**
- b86 Push CI: **Passed**
- b86 PR CI: **Passed**
- b86 Artifact/package identity: **Verified**
- b86 Runtime/manual/real-device: **Pending**
- Stable/Frozen Send: **No**

## Next exact action — Human Runtime gate

Install exact b86 and use a sufficiently long external response.

1. While the remote response is active, press `同步最新消息` exactly once.
2. After covered page load/re-arm, keep ChatGPTClient foreground; do not switch away immediately.
3. Leave it foreground long enough for the official page continuation logic to settle.
4. Export diagnostics whether automatic reasoning continuation happens or not.

Decision tree:

- **No `externalStreamStatusRequest`** -> the official page never activated continuation; next research target is the exact official page state/action that starts it.
- **Request exists, state != `IS_STREAMING`** -> compare page status/timing with authoritative Detail that already proves active reasoning.
- **`IS_STREAMING` + `externalResumeRequest`** -> inspect offset/request ordering and resume response.
- **resume HTTP200 `text/event-stream`** -> validate existing SSE parser and same-generation response-owner continuation before any new behavior change.
- **resume 404 + page-owned plural snapshots** -> accept the genuine page-owned block continuation evidence; do not synthesize SSE.

Do not modify b86 behavior or allocate b87 before this Runtime evidence unless a deterministic packaging/source defect is found.

## Session round counter

This user turn is **round 17**.
