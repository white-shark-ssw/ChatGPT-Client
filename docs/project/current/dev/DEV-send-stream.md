# DEV-send-stream

## Status

**Active — b83 is built and packaged for the narrowed Send MVP and is currently under real-device Runtime testing. b82 manual cross-platform Sync is Runtime Rejected for intermittent reasoning acquisition. b83 removes the source-backed `latestUserChanged` re-arm gate so every successful explicit manual Sync can perform one bounded covered-page re-arm when the selected conversation has no active Repository live response. Client-owned requests remain true SSE. Cross-platform block/page-snapshot progressive reasoning is acceptable for MVP. Automatic discovery and cross-platform token-level SSE remain deferred. A separate post-b83 requirement is now recorded: entering a conversation should automatically request one latest-message sync attempt. b83 Runtime result remains Pending; Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main` last verified this round: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Current branch head verified before this documentation update: `58d6d585eae1d5155334d737dad3ffda882bff4e`
- Exact b83 product/config source: `12e3c27138ebc81cbbae6236347122f79e03bf08`
- Clean b83 CI/package head: `3771ddccc8d0847ce28f72acbbe311aaf30b7482`
- Candidate: `DEV-send-stream-0.1.0-b83`
- Version / Build: `0.1.0 (83)`
- Push workflow run/job: `33556857625 / 100019684027` — success
- PR workflow run: `33556862137` — success
- Canonical b83 Artifact: `9819681774`
- Artifact ZIP digest: `sha256:b76c71493b01c88c6dfc60f9ef886e9e1c862d15a6e93ee00794ae6740a42682`
- IPA: `ChatGPTClient-0.1.0-b83-dev-send-stream.ipa`
- IPA SHA-256: `46f06106c3d47b3845a584665666fb6cb6d39cd66c0c9415412702e81795be97`
- b39-b83 permanently reserved
- Stable/Frozen Send: No

## Final Send MVP contract

### Client-owned Send

Keep the existing true SSE response stream. Do not downgrade this path.

### Cross-platform Send

For MVP, genuine block/page-snapshot progressive reasoning/tool updates are acceptable instead of token-level SSE, but explicit manual Sync is a hard reliability requirement:

1. user presses `同步最新消息` once;
2. authoritative Detail converges to the newest available remote state;
3. if the selected conversation has no active Repository live response, that successful explicit Sync performs one covered-page force re-arm;
4. if the remote response is active, the latest reasoning/tool block is acquired and later genuine blocks may continue without another Sync for every block;
5. final completion converges through the preserved b80 final-materialization boundary.

Deferred until broader product completion:

- automatic remote-turn discovery/acquisition;
- cross-platform token-level reasoning SSE parity;
- cross-platform progressive final-answer token streaming;
- production integration of the official iOS native realtime/WebSocket path.

## Recorded next requirement — one sync attempt when entering a conversation

User requirement recorded on 2026-09-02 while b83 Runtime testing is still in progress:

- when the user enters/selects a conversation, automatically request one latest-message synchronization attempt for that conversation;
- this should behave as a one-shot entry refresh, not a polling loop, timer, watchdog, repeated retry, or second state authority;
- `ConversationRepository` must remain the authoritative Detail/content owner;
- the current b83 Candidate must not be modified while its Runtime result is being qualified; implementation belongs to a later Candidate only after the current b83 result is known;
- user-observed reference behavior: the official ChatGPT app appears to make a network refresh attempt whenever entering a conversation, although the official app itself can still fail to visibly refresh under poor/network-changing conditions;
- evidence classification: the desired product behavior is an explicit user requirement; the observation that the official app issues an entry refresh is user Runtime/behavior evidence; the exact official endpoint, cadence, internal state machine, and failure handling remain **Unverified** and must not be guessed.

When implemented, prefer reusing the existing authoritative `syncLatestMessages`/Detail operation path rather than adding another refresh owner. Preserve existing operation coalescing/cancellation rules and avoid duplicate concurrent Detail operations.

## Latest Runtime evidence

The user reports b82 manual Sync sometimes fails to acquire the active external reasoning stream. Therefore b82 fails the final manual-Sync MVP reliability gate.

b83 is currently being exercised by the user in this same conversation. No pass/fail conclusion has been reported yet, so b83 Runtime remains Pending.

Previous accepted evidence remains:

- b78: real external reasoning/tool state can update multiple times at page-snapshot granularity;
- b79: explicit manual Sync can enter `manual_sync_rearm`, acquire `external_page_owned`, and adopt reasoning/tool snapshots;
- b80: stopped-thinking semantics and final-materialization boundary are preserved;
- b82: automatic completed-turn refresh works but is too late and is no longer an MVP blocker.

## b83 root cause and exact correction

Current source inspection identified that b82's `onManualLatestSyncApplied` callback required `latestUserChanged == true` before the only explicit force re-arm.

That fails when the latest remote user message is already present locally but the external live response was never acquired. A second explicit Sync succeeds, sees the same latest user ID, and b82 skips re-arm.

b83 exact source commit `12e3c27138ebc81cbbae6236347122f79e03bf08` changes only the manual callback gate plus build identity:

- callback ignores `latestUserChanged` as a re-arm gate;
- still requires same selected conversation;
- still refuses to re-arm while Repository already owns an active live response;
- still performs only one force reload per successful explicit manual Sync callback;
- build/candidate becomes 83/b83.

Automatic acquisition logic and client-owned SSE were not changed.

## Evidence ladder

- b82 manual external Sync stability: **Runtime Rejected**
- b83 source/root cause: **Verified from current source**
- b83 Code written: **Yes**
- b83 static diff/config identity: **Verified**
- b83 Push CI: **Passed**
- b83 PR CI: **Passed**
- b83 Artifact produced/package identity: **Verified**
- b83 Runtime/manual/real-device: **Testing in progress / result Pending**
- conversation-entry one-shot sync requirement: **Recorded only / Code not written / Candidate not allocated**
- Stable/Frozen Send: **No**

Durable Runtime evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b83-manual-sync-determinism-20260902.md`

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- no duplicate Send/resend, fake stream, polling, timer, speculative retry/watchdog/fallback or second response owner.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 12**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action — Human Runtime gate

Continue exact b83 real-device testing in the current conversation and wait for the user's Runtime result before modifying product code or allocating another Candidate.

For each b83 test, press Sync exactly once while reasoning is active. Verify the latest state and first reasoning/tool block appear, then do not press Sync again and verify at least one later genuine reasoning/tool block arrives before completion. Verify final convergence.

At least one test must cover the exact b83 edge case: the remote user message is already visible locally before Sync, but no reasoning stream is active. Pressing Sync must still re-arm and acquire the active reasoning path.

After the b83 result is classified, the recorded conversation-entry one-shot sync requirement may be scheduled as the next minimal product change. It must reuse the authoritative Detail/sync path and must not become polling or a second response owner.

If b83 passes repeated cases, freeze the manual cross-platform block-stream MVP before taking the entry-sync change as the next Candidate. If b83 still fails, first use b83 diagnostics to localize the exact page-owned acquisition failure; do not mix that diagnosis with the entry-sync requirement and do not reopen automatic discovery or cross-platform SSE research as part of this MVP fix.