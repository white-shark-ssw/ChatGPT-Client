# DEV-send-stream

## Status

**Active — exact b84 diagnostic Runtime proved manual Sync already receives approved trailing reasoning/tool timeline during active cross-platform generation, while current Native projection dropped it. Exact b85 implements the minimal correction by adopting that authoritative Detail timeline into the existing per-conversation response runtime. Push+PR CI and canonical IPA/package identity are verified. Runtime/manual/real-device remains Pending. Client-owned Send remains true SSE; cross-platform block-level reasoning/tool snapshots remain the MVP. Automatic discovery, cross-platform token SSE, progressive external final-token streaming and official-native realtime product integration remain deferred. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Final current branch head before Human Runtime: `144a6e5af2d79339556e30f2e7b9f52c9192de63` (b85 product unchanged since clean package head; later changes are evidence/docs/tool cleanup)
- b84 exact product/config source: `626c3ad4d4d592618d794c4cb8854324f719f4a4`
- b84 Candidate: `DEV-send-stream-0.1.0-b84` / `0.1.0 (84)` — diagnostic Runtime Positive, product acquisition still unstable
- b85 exact product/config source: `ec64dd170a6386612af8cb68b394045ce3c85313`
- b85 clean Push CI/package head: `6be1e8a8bafa80ef09c6fcebff014006de264e0f`
- b85 Candidate: `DEV-send-stream-0.1.0-b85`
- Version / Build: `0.1.0 (85)`
- Push run/job: `33564141168 / 100043319389` — success
- PR run/job: `33564179303 / 100043444613` — success
- Canonical b85 Artifact: `9822441595`
- Artifact ZIP digest: `sha256:0e32a52f91cb8580b91451d97d37696073fb4ee57c5df3918897aab69700ba48`
- IPA: `ChatGPTClient-0.1.0-b85-dev-send-stream.ipa`
- IPA SHA-256: `f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`
- Package identity: `0.1.0 (85)` / Candidate b85 / source `6be1e8a8bafa` / iOS14 minimum / arm64
- b39-b85 permanently reserved
- Stable/Frozen Send: No

## Send MVP contract

### Client-owned Send

Keep the existing true SSE response stream. Do not downgrade it.

### Cross-platform Send

For MVP, genuine block/page-snapshot progressive reasoning/tool updates are acceptable instead of token-level SSE. Explicit manual Sync must reliably converge to newest authoritative messages and expose the newest approved reasoning/tool block available from authoritative Detail/page-owned sources. Page-owned continuation may keep updating the same response generation when it attaches; another explicit Sync remains allowed for an active external response when page continuation does not attach.

Deferred until broader product completion:

- automatic remote-turn discovery/acquisition;
- cross-platform token-level reasoning SSE parity;
- cross-platform progressive final-answer token streaming;
- production integration of the official iOS native realtime/WebSocket path.

## b84 decisive Runtime

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b84-active-detail-trailing-timeline-20260902.md`.

Exact problematic target on b84/iOS17 produced active authoritative Detail samples while no page-owned live response existed:

- `21:28:16`: visible `25 -> 26`, mapping 1297, trailing timeline **1 = reasoning 1**;
- `21:28:37`: visible 26, mapping 1303, trailing timeline **4 = reasoning 1 + tools 3**;
- `21:28:49`: visible 26, mapping 1305, trailing timeline **5 = reasoning 1 + tools 4**;
- `21:28:56`: visible 26, mapping 1307, trailing timeline **6 = reasoning 1 + tools 5**.

`livePresentationRowCount` stayed 0 and covered Web did not acquire `external_page_owned`. Therefore `parseCurrentBranch` already had user-visible thinking/tool structure, but the ordinary Detail projection discarded the trailing `pendingTimeline` before a visible assistant row existed.

Raw `thoughts` / `inline_cot_expandable_content` remained skipped and are not authorized for presentation.

## b85 implemented correction

Durable build evidence: `docs/project/runtime-evidence/DEV-send-stream-b85-authoritative-detail-block-build-20260902.md`.

Exact product commit `ec64dd17...` changes only:

- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient/RootViewController.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`

Behavior:

1. `ConversationDetail` carries the actual already-approved trailing response timeline and reasoning duration returned by `parseCurrentBranch`.
2. Explicit manual Sync adopts/updates it through the existing `ConversationRepository` per-conversation `responseRuntime`; no second response store.
3. A Detail-backed external response and a later page-owned external continuation reuse the same response generation.
4. `同步最新消息` remains available while an external response is active, allowing another explicit authoritative block refresh if page continuation does not attach.
5. `重载当前会话` remains disabled during any active response; client-owned local Send continues to block recovery actions.
6. A later manual Sync with a materialized authoritative assistant beyond the external baseline and no trailing timeline reconciles/clears the Detail-backed live snapshot.
7. Client-owned SSE and all hidden-thought boundaries remain unchanged.

No polling, timer, retry, watchdog, duplicate Send/resend, automatic discovery, conversation-entry Sync or cross-platform token SSE was added.

## Durable architecture/status updates

- `BUILD_TEST_INDEX.md`: b84 promoted to Diagnostic Runtime Positive; b85 added as Code/CI/Artifact verified, Runtime Pending.
- `MODULE_STATUS.md`: b85 Active override records authoritative Detail as an accepted block-source architecture with Runtime pending.
- `TECHNICAL_DECISIONS.md`: TD-023 records explicit manual Sync adoption of approved trailing Detail timeline through the existing response owner; b85 product Runtime remains pending.
- Temporary staging/docs workflows and staging script have been removed from the current branch.

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
- b84 active authoritative trailing presentational timeline: **Runtime Positive**
- b84 active timeline growth without visible assistant: **Runtime Positive (`1 -> 4 -> 5 -> 6`)**
- b85 Code written: **Yes**
- b85 guarded exact-match staging / `git diff --check`: **Passed**
- b85 Push CI: **Passed**
- b85 PR CI: **Passed**
- b85 Artifact/package identity: **Verified**
- b85 Runtime/manual/real-device: **Pending**
- Stable/Frozen Send: **No**

## Next exact action — Human Runtime gate

Install exact b85. On a long cross-platform turn, press `同步最新消息` while it is active.

Expected decisive behavior:

1. if authoritative Detail has a non-empty trailing timeline, the current reasoning/tool block appears immediately from that Sync result without requiring covered Web acquisition;
2. if page-owned continuation later attaches, newer blocks continue on the same live response;
3. if it does not attach, a later explicit Sync advances the displayed block from newer Detail;
4. when the completed assistant materializes, a later Sync reconciles to completed historical content and clears the live snapshot.

Export b85 diagnostics either way. Key events: `liveResponse.started source=external_authoritative_detail`, `liveResponse.externalDetailSnapshot`, optional page-owned snapshot on the same generation, and `liveResponse.externalDetailReconciled`.

Do not modify product code or allocate b86 before this Runtime result unless a deterministic packaging/source defect is discovered.

## Session round counter

This user turn is **round 15**.
