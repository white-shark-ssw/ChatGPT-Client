# DEV-send-stream

## Status

**Active — MVP scope is manual-triggered progressive reasoning. Exact b82 remains the latest product Candidate. Automatic early cross-platform acquisition is no longer required for the minimum gate, but progressive reasoning after one explicit Sync is required. The accepted minimum is: while a remote turn is active, one explicit Sync must reliably acquire the newest turn, re-arm the existing covered observation, and then continue presenting multiple real reasoning/tool updates while the turn remains active. Token-by-token SSE parity is not required unless separately requested, but one-shot-only reasoning refresh is insufficient. b83 remains unallocated until exact b82 is re-validated against this corrected gate. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main` last verified: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b82 product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Candidate: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- Canonical b82 Artifact: `9811406038`
- b82 IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- b39-b82 permanently reserved
- b83: **not allocated**
- Stable/Frozen Send: No

## Corrected MVP requirement

Minimum acceptable external-response behavior:

1. A remote platform starts or is already generating a response for the selected conversation.
2. User taps Sync once.
3. Native performs the authoritative latest-message sync.
4. If the latest turn changed, the covered target page is re-armed once.
5. The existing page-owned external-response path starts/adopts the active response.
6. While the remote turn remains active, Native must receive and display **multiple real cumulative reasoning/tool updates over time** without requiring another manual Sync for every update.
7. Completion must converge to the latest final state using the preserved b80 materialization boundary.

A single one-shot reasoning snapshot after Sync is **not sufficient**.

The MVP does not require automatic request-start detection. It also does not require token-by-token SSE/delta parity if the real page-owned source only exposes coarser progressive snapshots. No fake typewriter animation or synthetic deltas are allowed.

## Existing Runtime evidence

### b78 proves progressive reasoning snapshots exist

`docs/project/runtime-evidence/DEV-send-stream-b78-device-runtime-20260901.md` records an active external response where Native received changing page-owned snapshots while reasoning/tools were active. Reasoning characters progressed `131 -> 260` while tool count progressed `2 -> 8` before completion. This is genuine progressive update behavior, but at page-snapshot granularity rather than token/SSE granularity.

The same b78 evidence shows the previous defect: a newly-started external turn in an already-open conversation could require manual Sync/re-arm before that progressive path starts.

### b79 proves manual Sync can enter the progressive path

`docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md` proves on real device:

- explicit Sync starts;
- authoritative Detail advances;
- covered observation enters `mode=manual_sync_rearm`;
- an `external_page_owned` live response starts;
- subsequent reasoning/tool snapshots are adopted.

This is the direct evidence-backed basis for the corrected MVP.

### b80 preserves terminal correctness

`docs/project/runtime-evidence/DEV-send-stream-b80-device-runtime-20260901.md` preserves manual-Sync re-arm and fixes the COMPLETE-before-final-materialization race. External stopped-thinking semantics and the final-materialization gate remain preserved.

### b81/b82 automatic acquisition

Automatic early acquisition remains unresolved/late and is no longer an MVP blocker. b82's automatic completion acquisition can remain as a bonus behavior but cannot substitute for the required manual-triggered progressive reasoning path.

## Current answer

**Yes, this MVP is evidence-backed as technically achievable with the existing architecture.** We have separate real-device evidence that:

- manual Sync can re-arm and enter the external response path;
- once in that path, reasoning/tool state can update multiple times while the response is active.

**Not yet Stable/Frozen:** exact b82 has not yet been run as a focused repeated test of the combined requirement `one manual Sync -> progressive reasoning updates continue`. Do not claim the current b82 package already satisfies it until that Human Runtime gate passes.

## Progressive final text boundary

Current evidence does **not** show progressive external final-body text. b78 shows final text staying at zero and then jumping to the full body. Therefore the corrected MVP requirement is specifically progressive **reasoning/tool** updates plus correct final convergence, not progressive final-answer token streaming.

If the user later requires progressive final text too, that is a separate protocol/source problem.

## Official native realtime research

Official iOS realtime Probe work remains preserved as optional future research but is not on the critical path for this MVP. Do not allocate a product Candidate for native WebSocket integration unless needed after the manual-triggered progressive gate is evaluated.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- no duplicate Send/resend, fake streaming, speculative retry/watchdog/fallback, hidden fixed polling or second response store.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 9**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

**Do not allocate b83 yet.** First run exact b82 against the corrected focused Human Runtime gate:

- start a sufficiently long remote reasoning turn for the selected conversation;
- while reasoning is active, press Sync exactly once;
- verify the remote user turn appears;
- verify the first reasoning/tool snapshot appears;
- without pressing Sync again, verify at least one later reasoning/tool update arrives while the turn is still active;
- repeat on a second turn/conversation;
- verify final convergence after completion.

If b82 passes repeatedly, freeze manual-triggered progressive reasoning as the Send MVP. If b82 fails, allocate b83 only for the smallest evidence-backed fix needed to make `manual Sync -> re-arm -> continuing page-owned progressive snapshots` deterministic.