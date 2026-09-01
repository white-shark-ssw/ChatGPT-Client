# DEV-send-stream

## Status

**Active — Send MVP scope is now explicitly split by ownership. Exact b82 remains the latest product Candidate. Client-owned requests must retain the existing real SSE streaming path. Cross-platform/external responses may use genuine coarse/page-snapshot streaming rather than token-level SSE, but one explicit Sync must reliably converge the selected conversation to the newest authoritative turn and, when that remote turn is still active, re-arm the existing covered observation so later real reasoning/tool blocks continue to arrive. Automatic remote-turn discovery and cross-platform token-level SSE are deferred until after the broader product is completed. b83 remains unallocated pending focused b82 qualification of the manual external-sync contract. Stable/Frozen Send as a whole remains No.**

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

## Send MVP contract

### A. Client-owned request path

When the user sends from ChatGPTClient itself, the current protected-Send response path must keep its accepted **real SSE streaming** behavior. Do not downgrade this path to snapshots, polling, fake typewriter animation or final-only materialization.

### B. Cross-platform / externally-started response path

The MVP allows **real block-level / page-snapshot progressive streaming** instead of token-level SSE parity.

Minimum accepted behavior:

1. A remote platform starts or has already started a turn for the selected conversation.
2. User taps Sync once.
3. Native performs the authoritative latest-message sync and must reliably converge to the newest available user/message state.
4. If that remote turn is still active and the authoritative turn changed, the covered target page is re-armed once.
5. The existing page-owned external-response path adopts the latest available reasoning/tool state.
6. While the turn remains active, later genuine page-owned reasoning/tool snapshots may continue to update without requiring the user to press Sync for every block.
7. Completion must converge to the latest final state using the preserved b80 final-materialization boundary.

A one-shot-only stale refresh or a Sync that sometimes misses the newest remote turn is **not acceptable**. Cross-platform token-by-token SSE is **not required for this MVP**.

### C. Explicitly deferred work

The following are postponed until after the broader product is completed and the user chooses to return to Send research:

- automatic detection/acquisition of a remotely-started turn;
- official-iOS native realtime/WebSocket integration as a product dependency/path;
- cross-platform token-level reasoning SSE parity;
- cross-platform progressive final-answer token streaming.

Existing official-Web/iOS realtime research artifacts and evidence remain preserved for that later phase. They are no longer a current release blocker.

## Existing Runtime evidence

### b78 proves genuine external progressive blocks exist

`docs/project/runtime-evidence/DEV-send-stream-b78-device-runtime-20260901.md` records an active external response where Native received changing page-owned snapshots while reasoning/tools were active. Reasoning characters progressed `131 -> 260` while tool count progressed `2 -> 8` before completion. This is genuine progressive update behavior, but at page-snapshot granularity rather than token/SSE granularity.

The same b78 evidence shows the previous defect: a newly-started external turn in an already-open conversation could require manual Sync/re-arm before that progressive path starts.

### b79 proves manual Sync can enter the external progressive path

`docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md` proves on real device:

- explicit Sync starts;
- authoritative Detail advances;
- covered observation enters `mode=manual_sync_rearm`;
- an `external_page_owned` live response starts;
- subsequent reasoning/tool snapshots are adopted.

This is the direct evidence-backed basis for the external MVP contract.

### b80 preserves terminal correctness

`docs/project/runtime-evidence/DEV-send-stream-b80-device-runtime-20260901.md` preserves manual-Sync re-arm and fixes the COMPLETE-before-final-materialization race. External stopped-thinking semantics and the final-materialization gate remain preserved.

### b81/b82 automatic acquisition

Automatic early acquisition remains unresolved/late and is no longer an MVP blocker. b82's automatic completion acquisition may remain as bonus behavior but cannot substitute for stable explicit manual Sync.

## Current qualification

**Architecture/evidence: the requested split MVP is technically supported by existing Runtime evidence.**

- client-owned Send SSE: existing accepted product direction, preserve;
- cross-platform block-level reasoning/tool updates: Runtime evidenced;
- manual Sync -> re-arm -> external progressive path: Runtime evidenced in predecessor candidates;
- exact b82 repeated stability against this narrowed combined contract: **still needs focused Human Runtime qualification**.

Do not claim Stable/Frozen until exact b82 repeatedly proves that manual Sync reliably reaches the newest remote turn and enters/continues the block-level external path when the response is active.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- no duplicate Send/resend, fake streaming, speculative retry/watchdog/fallback, hidden fixed polling or second response store.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 10**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

**Do not allocate b83 yet. Do not continue official native realtime research on the MVP critical path.**

First qualify exact b82 against the final external MVP contract:

- start a sufficiently long remote turn for the selected conversation;
- during the active turn, press Sync once;
- verify the newest remote user message/turn is acquired reliably;
- verify the latest reasoning/tool block appears;
- without pressing Sync again, verify at least one later real reasoning/tool block arrives while the turn is still active;
- repeat on at least one second turn/conversation;
- after completion, verify one Sync converges to the newest final state.

If b82 passes repeatedly, freeze this split Send MVP and proceed to the next product phase. If b82 fails, allocate b83 only for the smallest evidence-backed fix required to make **manual external Sync deterministic**; do not spend b83 on automatic discovery or cross-platform SSE research.