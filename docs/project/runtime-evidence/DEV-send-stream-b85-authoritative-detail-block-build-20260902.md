# DEV-send-stream b85 authoritative Detail block build — 2026-09-02

## Purpose

b85 is the minimal product correction authorized by exact b84 Runtime: explicit manual Sync can receive an already-approved trailing reasoning/tool timeline from authoritative Detail during active cross-platform generation even when covered Web never acquires the live response. b85 exposes that timeline through the existing `ConversationRepository` response runtime instead of dropping it before a visible assistant row exists.

## Identity

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29
- Candidate: `DEV-send-stream-0.1.0-b85`
- Version / Build: `0.1.0 (85)`
- Exact product/config source: `ec64dd170a6386612af8cb68b394045ce3c85313`
- Clean Push CI/workflow head: `6be1e8a8bafa80ef09c6fcebff014006de264e0f`
- Current branch after temporary staging-script cleanup: `6a2ae623a812742528083fb650cb559b6a4c2ac0`
- Push run/job: `33564141168 / 100043319389` — success
- PR run/job: `33564179303 / 100043444613` — success
- Canonical Push Artifact: `9822441595`
- Artifact ZIP digest: `sha256:0e32a52f91cb8580b91451d97d37696073fb4ee57c5df3918897aab69700ba48`
- IPA: `ChatGPTClient-0.1.0-b85-dev-send-stream.ipa`
- IPA SHA-256: `f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`
- Package metadata: `0.1.0 (85)` / Candidate b85 / `DiagnosticsSourceCommit=6be1e8a8bafa` / minimum iOS14.0 / arm64

## Exact product diff

The b85 product commit changes only:

- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient/RootViewController.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`

Compared with the staging parent, exact stats are:

- project file: 4 additions / 4 deletions (Debug+Release build/Candidate identity only);
- `ConversationFeature.swift`: 20 additions / 8 deletions;
- `RootViewController.swift`: 69 additions / 4 deletions.

The temporary guarded staging script was deleted after the product commit and is not part of the runtime package.

## Behavior change

- `ConversationDetail` now carries the actual already-presentational trailing response timeline and trailing reasoning duration from `parseCurrentBranch`.
- Explicit manual Sync adopts/updates that timeline through the existing per-conversation response runtime.
- A Detail-backed external response uses `promptText.isEmpty` and the same response-generation authority as page-owned external responses.
- If page-owned continuation later attaches, it reuses the same external generation rather than creating a competing response owner.
- Manual `同步最新消息` remains available during an active external response so a later explicit Sync can refresh a newer authoritative block.
- `重载当前会话` remains disabled during any active response; client-owned local Send still blocks recovery actions.
- When a later authoritative manual Sync materializes a new visible assistant beyond the external snapshot baseline and no trailing timeline remains, the Detail-backed external live snapshot is reconciled/cleared.
- Raw `thoughts` and `inline_cot_expandable_content` remain non-presentational.

No polling, timer, retry loop, watchdog, duplicate Send/resend, automatic discovery, conversation-entry one-shot Sync or cross-platform token-SSE change was added.

## Validation classification

- b84 source Runtime diagnosis: **Positive**
- b85 Code written: **Yes**
- guarded exact-match staging / `git diff --check`: **Passed**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced: **Yes**
- package identity / SHA / architecture: **Verified**
- Runtime/manual/real-device: **Pending**
- Stable/Frozen Send: **No**

## Human Runtime gate

Use exact b85 on a cross-platform response, especially the previously problematic long conversation class.

1. While the remote response is active, press `同步最新消息` once.
2. If authoritative Detail has a non-empty trailing presentational timeline, the reasoning/tool block should appear immediately from the Sync result without waiting for `external_page_owned`.
3. If page continuation attaches later, subsequent block updates should continue on the same live response.
4. If page continuation does not attach, press Sync again later; the displayed block should advance to the newer authoritative Detail timeline.
5. When the completed assistant message materializes, a later Sync should reconcile to historical completed content and clear the live snapshot.

Export diagnostics whether successful or failing. Key b85 events include `liveResponse.started source=external_authoritative_detail`, `liveResponse.externalDetailSnapshot`, optional page-owned external snapshots on the same generation, and `liveResponse.externalDetailReconciled` at authoritative completion.
