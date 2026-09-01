# DEV-send-stream

## Status

**Active — b83 remains Runtime Rejected for deterministic manual cross-platform reasoning acquisition. Exact b84 is now Runtime Partial Positive: one different-conversation real-device sample proves manual Sync re-arm can enter `external_page_owned` and acquire a genuine live reasoning/tool snapshot within seconds, while a later post-terminal authoritative Detail reconcile also proves a non-empty approved presentational trailing timeline can exist before a visible assistant row materializes. The original active-generation trailing-timeline hypothesis is not yet fully proven because the non-zero b84 Detail sample occurred after the page-owned live response had already emitted terminal/completed. The user is simultaneously testing the current conversation on the same exact b84 build to obtain a same-build A/B comparison. Client-owned Send remains true SSE. Cross-platform block/page-snapshot reasoning remains the MVP target. Automatic discovery, cross-platform token-level SSE, progressive external final-token streaming, and official-native realtime production integration remain deferred. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main` last verified: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Branch head before this checkpoint update: `176e24cb17967399dc03186c1a8ad734b0e0b852`
- b83 exact product/config source: `12e3c27138ebc81cbbae6236347122f79e03bf08`
- b83 Candidate: `DEV-send-stream-0.1.0-b83` / `0.1.0 (83)` — **Runtime Rejected**
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
- b85: **not allocated**
- Stable/Frozen Send: No

## Send MVP contract

### Client-owned Send

Keep the existing true SSE response stream. Do not downgrade it.

### Cross-platform Send

For MVP, genuine block/page-snapshot progressive reasoning/tool updates are acceptable instead of token-level SSE. Explicit manual Sync remains the current acquisition boundary: it must converge to newest authoritative Detail and acquire an active reasoning path whose later genuine blocks can continue without another Sync for every block. Final completion keeps the b80 final-materialization boundary.

Deferred until broader product completion:

- automatic remote-turn discovery/acquisition;
- cross-platform token-level reasoning SSE parity;
- cross-platform progressive final-answer token streaming;
- production integration of the official iOS native realtime/WebSocket path.

## b83 Runtime rejection — 2026-09-02

Exact b83 diagnostics prove repeated successful manual Sync calls executed `manual_sync_rearm`; several covered-page re-arms reached `page state=loaded`, yet no external live reasoning/snapshot was acquired and `livePresentationRowCount` stayed 0. The response only became available later as historical content after authoritative Detail advanced to the completed assistant message.

During the active response, authoritative Detail changed materially while visible message count stayed fixed: `mappingCount` advanced `1020 -> 1027 -> 1033 -> 1038 -> 1043` and `filteredRecipientMessageCount` advanced `427 -> 430 -> 433 -> 434 -> 436`. Therefore active server-side Detail is evolving before current Native visible projection exposes a new assistant message.

The former `latestUserChanged` re-arm gate was a real defect and b83 fixed it, but that correction is insufficient. `NSURLErrorDomain -999` and one Web-process termination occurred, but cannot be the sole root cause because clean page loads also failed. Covered-page re-arm is not accepted as a deterministic active-reasoning acquisition mechanism.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b83-manual-sync-determinism-20260902.md`.

## b84 diagnostic scope

`ConversationRepository.parseCurrentBranch` can accumulate an already-presentational `pendingTimeline` from recognized reasoning recap/thinking-preamble/tool events and attaches it only when a visible assistant message is appended. If parsing ends first, a trailing pending timeline is not represented by the ordinary visible-message projection.

b84 changes no acquisition behavior. It adds integer-only structural fields to `detail.response`:

- `trailingTimelineItemCount`
- `trailingReasoningItemCount`
- `trailingToolItemCount`
- `thinkingPreambleMessageCount`
- `ignoredThoughtsMessageCount`
- `ignoredInlineCotMessageCount`

The last two fields count skipped internal message types only. Raw `thoughts` and `inline_cot_expandable_content` remain explicitly non-presentational. b84 does not export prompt text, reasoning text, final text, tool bodies, auth/session/challenge values, signed query values, or hidden chain-of-thought.

Exact product source `626c3ad4...` changes only `ConversationFeature.swift` plus build/Candidate identity. Push and PR CI both pass; canonical Artifact/package identity is verified.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b84-detail-projection-diagnostics-20260902.md`.

## First b84 Runtime sample — successful live acquisition

Exact uploaded b84 diagnostics identify `0.1.0 (84)`, Candidate `DEV-send-stream-0.1.0-b84`, source `c7398eea6b20`, iOS17.0. Target marker: `sha256:6f429823a988`.

User observation: in this different conversation, pressing Sync made the reasoning block attach immediately. Log chronology supports that:

- initial selected Detail `21:24:33`: visible 13, mapping 134, trailing timeline 0;
- manual/latest Sync begins `21:25:00`; Detail returns `21:25:01`, visible `13 -> 14`, mapping `134 -> 135`, still trailing timeline 0;
- `manual_sync_rearm` at `21:25:01`;
- covered page loaded at `21:25:02`;
- `liveResponse.started source=external_page_owned` at `21:25:06`;
- same second: external streaming observed and page DOM structure reports `assistantNodeCount=4`, `textCharacters=1326`;
- page-owned resume returned HTTP404 JSON, then existing `page_owned_read_path` supplied the snapshot;
- `21:25:07`: live external snapshot `phase=reasoning`, `reasoningCharacters=258`, `serviceMessageCount=9`, `toolCount=3`;
- `21:25:13`: later snapshot service count 11, then page-owned live response terminal/completed;
- `21:25:14`: authoritative reconcile still visible 14 but now `trailingTimelineItemCount=6`, `trailingReasoningItemCount=2`, `trailingToolItemCount=4`.

### Exact conclusions from this sample

Runtime confirmed:

1. manual Sync re-arm can successfully acquire a covered-page external live response on exact b84;
2. successful acquisition can happen within seconds after a clean page load;
3. page-owned resume HTTP404 does not prevent the existing page-owned read path from producing genuine reasoning/tool snapshots;
4. a non-empty approved presentational trailing timeline can exist in authoritative Detail before a new visible assistant row materializes.

Timing qualification:

- the non-zero trailing-timeline Detail is **post-terminal** (`terminal/completed` at 21:25:13, Detail at 21:25:14), so active-generation `trailingTimelineItemCount > 0` before terminal remains Unverified;
- this result therefore does not yet authorize a b85 Native projection fix.

Strong current hypothesis only:

- the user observes that conversations which begin producing visible reasoning text quickly seem to attach, while conversations with a long initial no-visible-reasoning interval do not;
- the successful b84 sample is consistent with that: within seconds of page load it entered `external_page_owned` and had presentational reasoning/tool service content;
- the b83 failed sample had repeated clean page loads but never entered `external_page_owned` during its active interval.

Do not yet promote first-visible-reasoning timing to a production rule. The user's current-conversation test on the same b84 build is the next A/B evidence.

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
- b84 covered-page manual Sync live reasoning acquisition: **Runtime Positive in one exact sample**
- b84 post-terminal/pre-visible-assistant trailing presentational timeline: **Runtime Positive**
- b84 active-generation trailing presentational timeline before terminal: **Unverified**
- deterministic acquisition across conversations/response shapes: **Unproven / prior samples rejected**
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

## Session round counter

This user turn is **round 14**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action — same-build A/B Runtime gate

Keep exact b84. **Do not allocate b85 yet.**

Analyze the user's current-conversation test performed while this turn is being generated. Export and provide the b84 diagnostics regardless of whether the reasoning block attached.

For the same build, compare:

1. manual Sync authoritative Detail result;
2. `manual_sync_rearm` timing;
3. clean/failed page load;
4. whether and when `external_page_owned` begins;
5. whether page/service presentational reasoning/tool structure appears before acquisition;
6. first `liveResponse.externalSnapshot` timing and counts;
7. any pre-terminal `trailingTimelineItemCount` sample.

If current conversation fails while the successful conversation above acquires within seconds, treat first-presentational-content timing/page state as the leading hypothesis and instrument/inspect that exact boundary next. Do not add more refreshes/retries. If current conversation also succeeds, collect the second positive sample before deciding whether any code change is justified.
