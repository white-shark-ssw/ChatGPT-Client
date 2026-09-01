# DEV-send-stream

## Status

**Active — exact b84 diagnostic Runtime is now decisive: explicit manual Sync can receive an already-authorized trailing reasoning/tool timeline from authoritative Detail during active cross-platform generation even when covered Web never acquires `external_page_owned`. Current Native Detail projection drops that trailing timeline before a visible assistant row exists. b85 is allocated for the minimal projection/response-owner correction only. Client-owned Send remains true SSE; cross-platform block-level reasoning/tool snapshots remain the MVP. Automatic discovery, cross-platform token SSE, progressive external final-token streaming and official-native realtime production integration remain deferred. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Branch head before b85 product edit: `1f3da37246063e0bef7d415bbb2ae64ac0bbbf93`
- b84 exact product/config source: `626c3ad4d4d592618d794c4cb8854324f719f4a4`
- b84 clean CI/package head: `c7398eea6b20788f0e13a18f98e79d3c81ebfc21`
- b84 Candidate: `DEV-send-stream-0.1.0-b84` / `0.1.0 (84)`
- b84 canonical Artifact: `9820763662`
- b84 IPA SHA-256: `1a276fbfc46efeb75566989892d8811561563d6c43a664b1bb7b30799468be38`
- b84 Runtime: **Diagnostic Positive / product acquisition still unstable**
- b85 Candidate: **allocated** `DEV-send-stream-0.1.0-b85` / `0.1.0 (85)`
- b39-b85 permanently reserved
- Stable/Frozen Send: No

## Send MVP contract

### Client-owned Send

Keep the existing true SSE response stream. Do not downgrade it.

### Cross-platform Send

For MVP, genuine block/page-snapshot progressive reasoning/tool updates are acceptable instead of token-level SSE. Explicit manual Sync must reliably converge to newest authoritative messages and expose the newest approved reasoning/tool block available from the authoritative Detail/page-owned sources. Page-owned continuation may keep updating the same response generation when it attaches; another explicit Sync remains allowed for an active external response when page continuation does not attach.

Deferred until broader product completion:

- automatic remote-turn discovery/acquisition;
- cross-platform token-level reasoning SSE parity;
- cross-platform progressive final-answer token streaming;
- production integration of the official iOS native realtime/WebSocket path.

## b83 rejection retained

b83 fixed the real `latestUserChanged` manual re-arm gate but repeated explicit Sync + clean page loads still failed to acquire live reasoning in the problematic conversation. Active Detail graph nevertheless evolved. Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b83-manual-sync-determinism-20260902.md`.

## b84 decisive Runtime — active Detail timeline

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b84-active-detail-trailing-timeline-20260902.md`.

Exact b84 target `sha256:d597360f6d29`, iOS17.0:

- initial Detail `21:25:56`: visible 25, mapping 1293, trailing timeline 0;
- manual Sync Detail `21:28:16`: visible `25 -> 26`, mapping 1297, **trailing timeline 1 = reasoning 1**;
- re-arm/page load succeeded but no `external_page_owned`, no external live snapshot, live rows remained 0;
- second manual Sync Detail `21:28:37`: visible still 26, mapping 1303, **trailing timeline 4 = reasoning 1 + tools 3**;
- after relaunch Detail `21:28:49`: visible 26, mapping 1305, **trailing timeline 5 = reasoning 1 + tools 4**;
- explicit Reload Detail `21:28:56`: visible 26, mapping 1307, **trailing timeline 6 = reasoning 1 + tools 5**.

This is active/pre-final evidence. Therefore the b84 diagnostic hypothesis is accepted: `parseCurrentBranch` already recognizes presentational thinking preambles / reasoning recap / approved tools into `pendingTimeline`, while raw `thoughts` and `inline_cot_expandable_content` remain skipped; the current ordinary Detail projection loses that trailing timeline when no visible assistant message follows.

A separate b84 conversation also proved the covered page can acquire page-owned reasoning within seconds after re-arm. That path remains a useful continuation source but is not deterministic enough to be the sole manual-Sync acquisition path.

## b85 exact scope

Only the following evidence-backed correction is authorized:

1. `ConversationDetail` carries the actual already-approved trailing response timeline and trailing reasoning duration returned by `parseCurrentBranch`.
2. Explicit manual Sync adopts/updates that trailing timeline through the **existing per-conversation `ConversationRepository` response runtime**; no second response store.
3. If page-owned external snapshots later attach, they reuse/update the same external response generation rather than creating a competing owner.
4. Explicit `同步最新消息` remains available while an **external** response is active, so the user can fetch a newer authoritative block when page continuation does not attach.
5. `重载当前会话` remains disabled during an active response; client-owned local Send still blocks recovery actions.
6. When a later authoritative manual Sync materializes a new visible assistant beyond the external snapshot baseline and no trailing timeline remains, reconcile/clear that external live snapshot.
7. Keep raw `thoughts` / `inline_cot_expandable_content` non-presentational.

Do **not** add polling, timer, watchdog, retry loop, duplicate Send/resend, automatic discovery, entry-one-shot Sync, cross-platform token SSE, new response authority or unrelated refactor.

Expected product files: `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`, `ChatGPTClient.xcodeproj/project.pbxproj` only.

## Recorded later requirement — one Sync on conversation entry

After the current reasoning-acquisition MVP is accepted, entering/selecting a conversation should automatically request exactly one latest-message synchronization attempt through the authoritative Detail/`ConversationRepository` path. It must avoid duplicate concurrent Detail work and remain one-shot, not polling/timer/watchdog/retry machinery. This is **not part of b85**.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- default persistent WebKit store remains sole persistent auth-secret authority.
- WebSocket bodies remain structural only without separate Runtime authorization.
- no raw hidden-thought presentation.

## Evidence ladder

- b83 manual acquisition: **Runtime Rejected**
- b84 Code / Push+PR CI / Artifact: **Verified**
- b84 page-owned acquisition: **Runtime Positive in one conversation, non-deterministic overall**
- b84 active authoritative trailing presentational timeline: **Runtime Positive**
- b84 active timeline growth while visible assistant absent: **Runtime Positive (`1 -> 4 -> 5 -> 6`)**
- b85 identity: **Allocated; code not yet written at this checkpoint**
- Stable/Frozen Send: **No**

## Batch recovery point — b85 projection correction

Known baseline: branch `dev/send-stream-20260829` at `1f3da37246063e0bef7d415bbb2ae64ac0bbbf93`; main `94f0c577...`; PR #29 open/mergeable; b85 identity newly allocated and must not be reused if an Artifact is emitted.

Intended product batch: only `ConversationFeature.swift`, `RootViewController.swift`, and `project.pbxproj`; then normal b85 workflow/CI/package validation. No other feature scope.

If interrupted, re-read this checkpoint and actual branch head, then perform only missing deterministic writes. Do not replay an already-landed b85 product commit or reuse an emitted Artifact identity.

## Next exact action

Implement the minimal b85 authoritative-Detail trailing-timeline adoption into the existing response runtime, preserve page-owned continuation on the same generation, allow manual Sync for external active responses, build/package exact b85, then stop at real-device Runtime gate.

## Session round counter

This user turn is **round 15**.
