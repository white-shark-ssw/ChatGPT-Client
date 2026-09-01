# DEV-send-stream

## Status

**Active — b82 manual external Sync is Runtime rejected for stability. The current user report is that manual Sync sometimes fails to acquire the active external reasoning stream. b83 is now allocated only for a bounded manual-Sync determinism correction. Client-owned requests keep real SSE. Cross-platform responses may remain block/page-snapshot progressive. Automatic discovery, cross-platform token-level SSE and progressive external final-token streaming remain deferred. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Resume/pre-change head: `1bfb7a1ff87de9ab8242f4a1e55843efc1e8cd0c`
- Actual `main` verified this round: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Latest tested Candidate: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- b82 exact product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- b82 canonical Artifact: `9811406038`
- b82 IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- b39-b82 permanently reserved
- **b83 allocated: `DEV-send-stream-0.1.0-b83` / `0.1.0 (83)`**
- b83 product source: Pending until the minimal code/config write is committed
- b83 Artifact: Pending
- Stable/Frozen Send: No

## Final Send MVP contract

### Client-owned Send

Keep the existing real SSE response stream. Do not downgrade this path to page snapshots, polling or synthetic typewriter behavior.

### Cross-platform / externally-started Send

The MVP accepts genuine block/page-snapshot progressive reasoning/tool updates rather than token-level SSE parity, but explicit manual Sync is a hard reliability requirement:

1. a remote turn may already be active;
2. user taps `同步最新消息` once;
3. authoritative Detail must converge to the newest available remote state;
4. if Repository does not already own an active live response, the selected covered page must be re-armed exactly once by that explicit recovery action;
5. when an active remote response exists, the external page-owned path may then produce the latest reasoning/tool block and later genuine blocks without repeated Sync for each block;
6. completion must converge through the preserved b80 final-materialization boundary.

Automatic remote-turn discovery, official-iOS native realtime product integration, cross-platform token-level reasoning SSE and progressive external final-token streaming are explicitly deferred until the broader product is completed.

## Latest user Runtime evidence

The user reports that **manual Sync sometimes does not acquire the reasoning stream and is not stable**. This rejects b82 for the final manual-sync MVP gate. The failure is specifically about external reasoning acquisition after explicit Sync; client-owned SSE is not rejected by this report.

## Current source-backed defect

Current `ConversationDetailViewController.syncLatestMessages()` computes `latestUserChanged`, then invokes `onManualLatestSyncApplied(id, latestUserChanged)` only after authoritative Sync/apply succeeds.

Current `RootViewController` handles that callback with a guard requiring `latestUserChanged == true` before calling `observeExternalResponseIfNeeded(conversationID:forcePageReload:true)`.

Therefore this valid state can occur:

- newest remote user message is already present locally;
- Repository has no active external live response because the reasoning path was not acquired;
- user explicitly taps Sync again;
- authoritative Sync succeeds but latest user ID is unchanged;
- current code skips the only manual force-reload/re-arm action;
- reasoning stream remains unattached.

This logic is narrower than the accepted MVP contract and directly matches the reported intermittent symptom. The fix does not require a timer, retry loop, WebSocket content authority or automatic discovery.

## b83 exact scope

Make only the minimum ownership-preserving correction:

- after a successful **explicit manual Sync** callback, if the conversation is still selected and Repository has no active live response, force one covered-page re-arm regardless of `latestUserChanged`;
- preserve `latestUserChanged` diagnostics if useful, but do not use it as the gate for the explicit re-arm;
- leave automatic acquisition logic unchanged;
- leave client-owned SSE unchanged;
- no polling/timer/watchdog/retry loop/duplicate Send/fake stream/second response owner.

## Evidence ladder

- b82 code/CI/Artifact: previously verified
- b82 manual external Sync stability: **Runtime Rejected by latest user report**
- b83 Candidate identity: Allocated
- b83 code: Pending
- b83 static/local checks: Pending
- b83 CI: Pending
- b83 Artifact: Pending
- b83 real-device Runtime: Pending
- Stable/Frozen Send: No

## Batch recovery point

Known baseline before b83 writes:

- branch `dev/send-stream-20260829`
- PR #29
- head `1bfb7a1ff87de9ab8242f4a1e55843efc1e8cd0c`
- actual main `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- project config currently `0.1.0 (82)` / `DEV-send-stream-0.1.0-b82`
- no separate competing Active development checkpoint is present under `docs/project/current/dev/`; the only task checkpoint is this Send work (the round7 addendum is supplemental, not another Work ID)
- b83 was not present in `BUILD_TEST_INDEX.md` or repository code search before allocation

Confirmed completed in this write chain:

- PR #29 title/body updated to record b82 manual-Sync instability and b83 scope.
- this checkpoint allocated b83 and records the recovery point.

Still pending, in order:

1. change only the manual-Sync callback gate in `RootViewController.swift`;
2. bump Debug+Release product config from build 82/b82 to build 83/b83;
3. record b83 allocation/source in `BUILD_TEST_INDEX.md` and Runtime evidence;
4. run the normal CI/artifact path and verify exact package identity;
5. hand b83 to the user for focused real-device Runtime.

Recovery must not touch automatic discovery/native realtime research or other deferred product areas.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 11**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Apply the minimal b83 source/config change, then validate/package it. Human Runtime focus after Artifact: run at least two active remote turns; during each, press Sync once while reasoning is active; verify the current reasoning block appears and at least one later real reasoning/tool block arrives without another Sync. Also reproduce the important edge case where the latest remote user message is already visible before pressing Sync; b83 must still re-arm and acquire the active reasoning path.