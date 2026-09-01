# DEV-send-stream

## Status

**Active — exact b83 is Runtime Rejected for the narrowed Send MVP. Repeated explicit manual Sync calls did execute `manual_sync_rearm`, but no external live reasoning/snapshot was acquired; the response only appeared after final authoritative synchronization. The former `latestUserChanged` gate was a real defect but not the final root cause. Client-owned Send remains true SSE. Cross-platform block/page-snapshot progressive reasoning remains the MVP target; automatic discovery and cross-platform token-level SSE remain deferred. A separate later requirement remains recorded: entering/selecting a conversation should make one latest-message sync attempt. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main` verified: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Branch head before this checkpoint update: `dc34c1808fc507a0ba32319cdfcdeab8d38de2fd`
- Exact b83 product/config source: `12e3c27138ebc81cbbae6236347122f79e03bf08`
- Clean b83 CI/package head: `3771ddccc8d0847ce28f72acbbe311aaf30b7482`
- Candidate: `DEV-send-stream-0.1.0-b83`
- Version / Build: `0.1.0 (83)`
- Push `33556857625 / 100019684027` — success
- PR `33556862137` — success
- Canonical Artifact: `9819681774`
- Artifact ZIP: `sha256:b76c71493b01c88c6dfc60f9ef886e9e1c862d15a6e93ee00794ae6740a42682`
- IPA SHA-256: `46f06106c3d47b3845a584665666fb6cb6d39cd66c0c9415412702e81795be97`
- b39-b83 permanently reserved
- b84: not yet emitted at this checkpoint; intended next scope is structural Detail-projection diagnostics only
- Stable/Frozen Send: No

## Send MVP contract

### Client-owned Send

Keep the existing true SSE response stream. Do not downgrade it.

### Cross-platform Send

For MVP, genuine block/page-snapshot progressive reasoning/tool updates are acceptable instead of token-level SSE. Explicit manual Sync is the acquisition boundary: it must converge to newest authoritative Detail and then acquire an active reasoning path whose later genuine blocks can continue without another Sync for every block. Final completion keeps the b80 final-materialization boundary.

Deferred until broader product completion:

- automatic remote-turn discovery/acquisition;
- cross-platform token-level reasoning SSE parity;
- cross-platform progressive final-answer token streaming;
- production integration of the official iOS native realtime/WebSocket path.

## b83 Runtime rejection — 2026-09-02

Exact uploaded diagnostics identify `0.1.0 (83)`, Candidate `DEV-send-stream-0.1.0-b83`, source `3771ddccc8d0`, iOS 17.0.

Observed on conversation `sha256:d597360f6d29`:

- repeated user Syncs returned authoritative Detail HTTP200 and repeatedly emitted `coveredExecutor.observing mode=manual_sync_rearm`;
- several re-arms reached `coveredExecutor.page state=loaded`, proving the b83 callback correction executed;
- two navigations also produced isolated `NSURLErrorDomain -999 / navigation_failed`, and one later background interval terminated the Web process; these are real noise but cannot be the sole root cause because clean page loads also failed to acquire reasoning;
- no `external_page_owned`, live-response adoption, reasoning snapshot, or live presentation was observed; `livePresentationRowCount` stayed 0;
- the user-socket structural frames remained `targetMatch=false` in this export;
- during generation the authoritative Detail payload visibly evolved even while `visibleMessageCount` stayed 22: `mappingCount` advanced `1020 -> 1027 -> 1033 -> 1038 -> 1043`, and `filteredRecipientMessageCount` advanced `427 -> 430 -> 433 -> 434 -> 436`;
- only later did authoritative visible count advance to 23 and the completed reasoning become historical content.

Conclusion: b83 proves the explicit re-arm gate is no longer skipped, but covered-page re-arm is not a deterministic active-reasoning acquisition mechanism. b83 is **Runtime Rejected** for the manual cross-platform block-stream MVP.

## Current source-backed investigation

`ConversationRepository.parseCurrentBranch` builds a `pendingTimeline` from already-authorized presentational sources such as service/tool events, collapsed reasoning recap, and `is_thinking_preamble_message`. That timeline is attached only when a visible assistant message is appended. If parsing ends while the response is still active, the current function returns only `messages` plus `filteredRecipientMessageCount`; any trailing `pendingTimeline` is not surfaced. The same parser explicitly skips `assistant` content types `thoughts` and `inline_cot_expandable_content`.

Do **not** infer that the skipped raw thoughts types are user-visible or authorized for presentation. The next diagnostic must record structure/counts only and must not export prompt, reasoning body, final body, tool body, auth/query/challenge data, or raw hidden chain-of-thought.

## Recorded later requirement — one sync attempt on conversation entry

After the current reasoning-acquisition problem is resolved, entering/selecting a conversation should automatically request one latest-message synchronization attempt. It must reuse the authoritative Detail/`ConversationRepository` operation path, avoid duplicate concurrent Detail work, and remain a one-shot entry refresh rather than polling/timer/watchdog/retry machinery. The user's observation that the official app makes an entry refresh attempt is Runtime/behavior reference evidence; its exact endpoint/cadence/state machine remain Unverified.

## Evidence ladder

- b82 manual external Sync stability: **Runtime Rejected**
- b83 Code written: **Yes**
- b83 Push CI / PR CI: **Passed**
- b83 Artifact/package identity: **Verified**
- b83 real-device Runtime: **Rejected**
- b83 former `latestUserChanged` defect: **Fixed but insufficient**
- Detail payload changes during active generation: **Runtime Confirmed**
- trailing pending presentational timeline during active Detail: **Unknown / next diagnostic target**
- raw `thoughts` / `inline_cot_expandable_content` presentational authorization: **No / do not surface without separate evidence**
- conversation-entry one-shot sync: **Requirement recorded / code not written**
- Stable/Frozen Send: **No**

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b83-manual-sync-determinism-20260902.md`
- next evidence file should record the b83 rejection chronology and any b84 structural Detail-projection result.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- no duplicate Send/resend, fake stream, speculative retry/watchdog/fallback, second response owner, or raw hidden-thought presentation.

## Batch recovery point — b83 rejection to b84 diagnostic

Baseline: branch `dev/send-stream-20260829`, PR #29, head `dc34c1808fc507a0ba32319cdfcdeab8d38de2fd`, b83 permanently reserved and Runtime Rejected.

Confirmed complete:

- user Runtime result received;
- uploaded b83 diagnostics inspected;
- b83 re-arm execution and failure chronology localized;
- source parser inspection identified trailing `pendingTimeline` as the next exact unknown.

Pending deterministic writes/actions:

1. durable b83 rejection evidence and BUILD_TEST_INDEX status update;
2. update PR #29 to b83 rejected / b84 structural diagnostic next;
3. verify b84 identity is unused, then allocate `DEV-send-stream-0.1.0-b84` only for privacy-safe structural Detail-projection diagnostics;
4. instrument counts/structural classifications only, build/CI/package, then hand exact b84 to human Runtime.

Do not touch client-owned SSE, automatic discovery, cross-platform token SSE, entry-one-shot Sync behavior, or the official realtime research probe during this batch.

## Session round counter

This user turn is **round 13**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Complete the durable b83 Runtime rejection record, then allocate b84 after identity/conflict verification. b84 must answer one question only: during active cross-platform generation, does authoritative Detail parsing end with a non-empty already-authorized presentational `pendingTimeline` (reasoning/tool/thinking-preamble) that the current projection drops before a visible assistant message exists? If yes, use that evidence for the next minimal acquisition design. If no, stop and reassess the data source; do not expose skipped raw thoughts and do not add speculative polling.