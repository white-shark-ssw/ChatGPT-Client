# DEV-send-stream

## Status

**Active — b83 is Runtime Rejected for manual cross-platform reasoning acquisition. b84 is a diagnostic-only Candidate now built and packaged to determine whether authoritative Detail already contains a trailing, already-presentational reasoning/tool timeline during active generation that current Native projection drops before a visible assistant row exists. Client-owned Send remains true SSE. Cross-platform block/page-snapshot reasoning remains the MVP target. Automatic discovery, cross-platform token-level SSE, progressive external final-token streaming, and official-native realtime production integration remain deferred. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main` verified this round: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Branch head before this checkpoint update: `6d4db9f0317191ffb9c8e910726032c22ac0fcae`
- b83 exact product/config source: `12e3c27138ebc81cbbae6236347122f79e03bf08`
- b83 Candidate: `DEV-send-stream-0.1.0-b83` / `0.1.0 (83)` — Runtime Rejected
- b84 exact product/config source: `626c3ad4d4d592618d794c4cb8854324f719f4a4`
- b84 clean CI/package head: `c7398eea6b20788f0e13a18f98e79d3c81ebfc21`
- b84 Candidate: `DEV-send-stream-0.1.0-b84`
- Version / Build: `0.1.0 (84)`
- Push run/job: `33559649854 / 100028790782` — success
- PR run/job: `33559655688 / 100028812048` — success
- Canonical b84 Artifact: `9820763662`
- Artifact ZIP digest: `sha256:65ff52ddc7b6c4ad1e85e0c084a4f55799da06baad602dff3693edd12a814e9f`
- IPA: `ChatGPTClient-0.1.0-b84-dev-send-stream.ipa`
- IPA SHA-256: `1a276fbfc46efeb75566989892d8811561563d6c43a664b1bb7b30799468be38`
- Package identity: `0.1.0 (84)` / `DEV-send-stream-0.1.0-b84` / source `c7398eea6b20` / iOS14 minimum / arm64
- b39-b84 permanently reserved
- Stable/Frozen Send: No

## Send MVP contract

### Client-owned Send

Keep the existing true SSE response stream. Do not downgrade it.

### Cross-platform Send

For MVP, genuine block/page-snapshot progressive reasoning/tool updates are acceptable instead of token-level SSE. Explicit manual Sync remains the current acquisition boundary: it must converge to newest authoritative Detail and eventually acquire an active reasoning path whose later genuine blocks can continue without another Sync for every block. Final completion keeps the b80 final-materialization boundary.

Deferred until broader product completion:

- automatic remote-turn discovery/acquisition;
- cross-platform token-level reasoning SSE parity;
- cross-platform progressive final-answer token streaming;
- production integration of the official iOS native realtime/WebSocket path.

## b83 Runtime rejection — 2026-09-02

Exact b83 diagnostics from the user prove repeated successful manual Sync calls executed `manual_sync_rearm`; several covered-page re-arms also reached `page state=loaded`, yet no external live reasoning/snapshot was acquired and `livePresentationRowCount` stayed 0. The response only became available later as historical content after authoritative Detail advanced to the completed assistant message.

During the active response, authoritative Detail changed materially while visible message count stayed fixed: `mappingCount` advanced `1020 -> 1027 -> 1033 -> 1038 -> 1043` and `filteredRecipientMessageCount` advanced `427 -> 430 -> 433 -> 434 -> 436`. Therefore active server-side Detail is evolving before current Native visible projection exposes the assistant row.

The former `latestUserChanged` re-arm gate was a real defect and b83 fixed it, but that correction is insufficient. `NSURLErrorDomain -999` and one Web-process termination occurred, but cannot be the sole root cause because clean page loads also failed. Covered-page re-arm is not accepted as a deterministic active-reasoning acquisition mechanism.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b83-manual-sync-determinism-20260902.md`.

## b84 exact diagnostic scope

Current source inspection shows `ConversationRepository.parseCurrentBranch` can accumulate an already-presentational `pendingTimeline` from recognized reasoning recap/thinking-preamble/tool events and attaches it only when a visible assistant message is appended. Historically, if parsing ended while the response remained active, any trailing `pendingTimeline` was not surfaced by the return value.

b84 changes no acquisition behavior. It adds integer-only structural fields to `detail.response`:

- `trailingTimelineItemCount`
- `trailingReasoningItemCount`
- `trailingToolItemCount`
- `thinkingPreambleMessageCount`
- `ignoredThoughtsMessageCount`
- `ignoredInlineCotMessageCount`

The last two fields count skipped internal message types only. Raw `thoughts` and `inline_cot_expandable_content` remain explicitly non-presentational. b84 does not export prompt text, reasoning text, final text, tool bodies, auth/session/challenge values, signed query values, or hidden chain-of-thought.

Exact product source `626c3ad4...` changes only `ConversationFeature.swift` plus build/Candidate identity. Normal Push and PR CI both pass; canonical Artifact/package identity is verified. Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b84-detail-projection-diagnostics-20260902.md`.

## Recorded later requirement — one Sync attempt on conversation entry

After the current reasoning-acquisition problem is resolved, entering/selecting a conversation should automatically request exactly one latest-message synchronization attempt. It must reuse the authoritative Detail/`ConversationRepository` path, avoid duplicate concurrent Detail work, and remain a one-shot entry refresh rather than polling/timer/watchdog/retry machinery.

The user's observation that the official app makes a network refresh attempt on conversation entry is Runtime/behavior reference evidence. Exact official endpoint/cadence/state machine remain Unverified. This requirement is **not implemented in b84**.

## Evidence ladder

- b82 manual external Sync stability: **Runtime Rejected**
- b83 Code / CI / Artifact: **Verified**
- b83 real-device Runtime: **Rejected**
- b83 former `latestUserChanged` defect: **Fixed but insufficient**
- active authoritative Detail graph evolution: **Runtime Confirmed**
- b84 Code written: **Yes**
- b84 Push CI: **Passed**
- b84 PR CI: **Passed**
- b84 Artifact/package identity: **Verified**
- b84 Runtime/manual/real-device: **Pending**
- trailing already-presentational pending timeline during active Detail: **Unknown / b84 Runtime target**
- raw `thoughts` / `inline_cot_expandable_content` presentational authorization: **No**
- conversation-entry one-shot Sync: **Requirement recorded / not implemented**
- Stable/Frozen Send: **No**

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- no duplicate Send/resend, fake stream, speculative retry/watchdog/fallback, polling, second response owner, or raw hidden-thought presentation.

## Batch recovery point — b84 Runtime handoff

Baseline: branch `dev/send-stream-20260829`, PR #29, b83 permanently reserved/Runtime Rejected, b84 product source `626c3ad4...`, clean CI/package head `c7398eea...`.

Confirmed complete:

- b83 user Runtime result and diagnostics analyzed;
- durable b83 Runtime rejection evidence written;
- b84 identity verified unused and allocated;
- privacy-safe b84 structural diagnostic source committed;
- Push and PR CI passed;
- canonical b84 Artifact downloaded and package identity verified;
- b84 durable evidence written.

Pending deterministic docs/actions:

1. update `BUILD_TEST_INDEX.md` b83 status and add b84 row;
2. update PR #29 to b83 rejected / b84 Runtime diagnostic next;
3. hand exact b84 IPA to user for real-device structural diagnostic.

Do not touch client-owned SSE, automatic discovery, cross-platform token SSE, conversation-entry one-shot Sync behavior, or official realtime probe while b84 Runtime is pending.

## Session round counter

This user turn is **round 13**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action — Human Runtime gate

Install exact b84. Start a deliberately long cross-platform response. While it is still generating, press manual Sync two or three times at separated points; b84 is not expected to fix the UI. Export diagnostics while the response is still active if possible and provide the JSON.

Decisive result:

- any active `detail.response` with `trailingTimelineItemCount > 0` proves an already-authorized presentational trailing timeline exists in authoritative Detail and is being dropped by the current projection; next work may be a minimal Native projection fix;
- if active samples consistently show `trailingTimelineItemCount == 0`, reject that hypothesis and reassess the data source. Do not expose raw skipped thoughts and do not add speculative polling.
