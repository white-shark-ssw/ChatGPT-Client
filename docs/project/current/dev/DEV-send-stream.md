# DEV-send-stream

## Status

**Active — exact b85 real-device Runtime is now Partial Positive / MVP continuation Rejected. Manual `同步最新消息` reliably adopts the authoritative Detail trailing reasoning/tool timeline into the existing response owner and updates the UI, but the covered official-Web continuation does not automatically attach in this sample: every newer block required another explicit Sync. Client-owned Send remains true SSE. Cross-platform block-level reasoning is available through explicit Sync, but the current MVP requirement that one Sync can re-arm later genuine block continuation without pressing Sync for every block is not met. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Branch head before this Runtime checkpoint update: `1c54a40d01ad50545c82cc8bc25435e421e3e6ef`
- b85 exact product/config source: `ec64dd170a6386612af8cb68b394045ce3c85313`
- b85 clean Push CI/package head: `6be1e8a8bafa80ef09c6fcebff014006de264e0f`
- Candidate: `DEV-send-stream-0.1.0-b85`
- Version / Build: `0.1.0 (85)`
- Push run/job: `33564141168 / 100043319389` — success
- PR run/job: `33564179303 / 100043444613` — success
- Canonical Artifact: `9822441595`
- IPA SHA-256: `f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`
- Uploaded Runtime package metadata: `0.1.0 (85)` / Candidate b85 / source `6be1e8a8bafa` / iOS17.0
- b39-b85 permanently reserved
- b86: **not allocated**
- Stable/Frozen Send: No

## Send MVP contract

### Client-owned Send

Keep the existing true SSE response stream. Do not downgrade it.

### Cross-platform Send

For MVP, genuine block/page-snapshot progressive reasoning/tool updates are acceptable instead of token-level SSE, but explicit manual Sync must be a stable acquisition/re-arm boundary: one Sync should expose the newest authoritative block and, when the external response remains active, the covered page should be able to continue newer genuine blocks without requiring another Sync for every block. Final completion keeps the b80 materialization boundary.

Deferred unless explicitly reopened by current user work:

- automatic remote-turn discovery/acquisition;
- cross-platform token-level reasoning SSE parity;
- progressive external final-answer token streaming;
- production official-native realtime/WebSocket integration.

The user has now explicitly reopened the narrower question of whether the newly proven authoritative active-Detail anchor can help establish true page-owned cross-platform SSE continuation. Do not interpret that as authorization for polling or guessed Native resume requests.

## b84 decisive Runtime

Exact b84 proved active authoritative Detail can expose an already-presentational trailing timeline before a visible assistant row exists. On the previously problematic conversation it grew `1 -> 4 -> 5 -> 6` while covered Web never acquired the live response. Raw `assistant:thoughts` / `inline_cot_expandable_content` remained skipped.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b84-active-detail-trailing-timeline-20260902.md`.

## b85 implementation

b85 carries the approved trailing timeline in `ConversationDetail`, adopts it into the existing per-conversation `responseRuntime` on explicit Sync, permits repeated Sync while the active response is external, and lets a later page-owned continuation reuse the same response generation. No second response store, polling, retry loop, timer, watchdog, duplicate Send/resend, automatic discovery, conversation-entry Sync or cross-platform token SSE was added.

Durable build evidence: `docs/project/runtime-evidence/DEV-send-stream-b85-authoritative-detail-block-build-20260902.md`.

## b85 real-device Runtime — 2026-09-02

Uploaded diagnostics identify exact b85 on iOS17.0 and target conversation marker `sha256:d597360f6d29`.

### Manual authoritative block path — Runtime Positive

The same live response generation (`responseGeneration=1`) advances only when the user explicitly presses Sync:

- `22:17:29` Sync requested -> `22:17:34` Detail: visible `29 -> 30`, mapping `1622`, trailing timeline **1 = reasoning 1** -> `liveResponse.started source=external_authoritative_detail` -> `externalDetailSnapshot timeline=1` -> live row shown.
- `22:18:23` Sync requested -> `22:18:29` Detail: visible still `30`, mapping `1630`, trailing timeline **5 = reasoning 1 + tools 4** -> same `responseGeneration=1` updated to timeline 5.
- `22:19:35` Sync requested -> `22:19:39` Detail: visible still `30`, mapping `1637`, trailing timeline **7 = reasoning 2 + tools 5** -> same generation updated to timeline 7.
- `22:20:34` Sync requested -> `22:20:38` Detail: visible `31`, trailing timeline 0 -> `liveResponse.externalDetailReconciled reason=authoritative_assistant_materialized` and live row cleared.

This proves b85's Native Detail projection/reconciliation and single response-owner design work on real device.

### Automatic continuation after Sync — Runtime Rejected in this sample

After each active Sync, `manual_sync_rearm` occurs and the covered page reports `state=loaded`, but the export contains:

- zero `coveredExecutor.externalStreamingObserved`;
- zero `coveredExecutor.externalSnapshot`;
- zero `liveResponse.externalSnapshot`;
- zero `coveredExecutor.externalResumeObserved`;
- zero `coveredExecutor.resumeResponse`.

Therefore no page-owned continuation transport was acquired at all. This is not a failure of the b85 timeline parser or generation reuse; the official page never entered the currently observed `stream_status` / resume / plural-read path during these windows.

User observation exactly matches the log: each explicit Sync reveals a newer portion of reasoning, but no automatic continuation occurs between Sync actions.

### Lifecycle qualification

The app entered background shortly after several page re-arms, and the covered user WebSocket produced error/close events. The longest clean foreground windows after page load in this export are only several seconds. Therefore this export proves current behavior is not stable enough for the MVP, but by itself does **not** prove that a fully foreground page could never attach later. Previous b83/b84 failures with clean page loads still show this is a real reliability problem rather than only a background artifact.

### Current technical conclusion

The remaining bottleneck is **page-owned continuation activation**, not Native authoritative block acquisition. The bridge is already able to consume page-owned `stream_status`, `/resume` SSE, and plural snapshots when the official page actually issues those requests. Current b85 logs cannot distinguish:

1. page never requested `stream_status`, versus
2. page requested it but received a state/status that did not trigger `externalStreamingObserved`.

Do not guess `offset`, construct Native `/resume`, add Detail polling, or add refresh/retry loops. The next evidence must instrument the existing page-owned network interception just enough to distinguish those cases.

## Narrow SSE research direction

Existing exact historical Runtime proves official Web can perform cross-device continuation as:

`stream_status -> POST /backend-api/f/conversation/resume {conversation_id, offset} -> HTTP200 text/event-stream`

and other current runs can fall back to page-owned plural snapshots after resume 404. b84/b85 now provide a reliable authoritative active-response anchor and immediate UI snapshot, but they do not themselves create SSE.

The next question is not whether SSE exists. It is: **what official page state causes the target conversation to issue `stream_status` and then a valid resume/read continuation after an explicit authoritative Sync/re-entry?**

## Recorded later requirement — one Sync on conversation entry

Entering/selecting a conversation should eventually perform exactly one latest-message Sync attempt through the authoritative Detail/Repository path. This one-shot refresh does not solve automatic continuation by itself and remains unimplemented in b85.

## Evidence ladder

- b83 manual acquisition: **Runtime Rejected**
- b84 active authoritative trailing timeline: **Runtime Positive**
- b85 Code / Push+PR CI / Artifact/package: **Verified**
- b85 explicit manual Detail block projection: **Runtime Positive**
- b85 repeated Sync updates same external response generation: **Runtime Positive**
- b85 final authoritative reconciliation: **Runtime Positive**
- b85 automatic page-owned continuation after one Sync: **Runtime Rejected in uploaded sample**
- b85 true cross-platform SSE continuation: **Not acquired**
- Stable/Frozen Send: **No**

## Batch recovery point — b85 Runtime documentation + next diagnostic decision

Baseline/head before this checkpoint write: `1c54a40d01ad50545c82cc8bc25435e421e3e6ef` on `dev/send-stream-20260829`; PR #29 open/mergeable; b85 product identity remains fixed at source `ec64dd17...`, package head `6be1e8a8...`, Artifact `9822441595`.

Small write batches:

1. **Completed by this checkpoint write:** record uploaded b85 Runtime and classify manual block path Positive / auto continuation Rejected.
2. **Pending:** create durable b85 Runtime evidence file from the uploaded diagnostics.
3. **Pending:** update `BUILD_TEST_INDEX.md` b85 Runtime status and `MODULE_STATUS.md` Send override; TD-023 needs only status qualification, not a new architecture rule.
4. **Pending:** refresh PR #29 stale b84 title/body to b85 Runtime truth.
5. **Pending decision after durable docs:** do not allocate b86 unless exact source inspection confirms a privacy-safe diagnostic gap that cannot be answered from existing logs. If allocated, b86 must be diagnostics-only around page-owned `stream_status` / resume request structure and must not change acquisition behavior.

Do not touch b85 product source, canonical Artifact identity, client-owned SSE, b80 Frozen presentation/final boundaries, or raw hidden-thought rules during recovery.

## Next exact action

Complete the pending durable Runtime documentation above, then inspect the current covered bridge's `stream_status`/resume interception. If current diagnostics do not log non-IS_STREAMING `stream_status` responses or whether a matching resume request carried an offset, allocate a single diagnostics-only b86 candidate to expose only those structural facts. Otherwise use b85 for one foreground-held targeted Runtime probe. No behavior change before that evidence.

## Session round counter

This user turn is **round 17**.
