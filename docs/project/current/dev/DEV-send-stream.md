# DEV-send-stream

## Status

**Active — MVP scope narrowed to reliable manual acquisition. Exact b82 remains the latest product Candidate. Automatic early cross-platform acquisition and token-level external streaming are no longer required for the minimum product gate. The minimum requirement is: while a remote turn is active, one explicit Sync must reliably acquire the newest authoritative turn state, re-arm the existing covered observation, and expose the latest available reasoning/tool snapshot; if the response remains active, the existing page-owned observation may continue to refresh later snapshots. b83 remains unallocated until the current b82 manual path is re-validated against this narrowed gate. Stable/Frozen Send as a whole remains No.**

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

## Latest product minimum

The minimum acceptable external-response behavior is now manual rather than automatic:

1. User keeps or opens the target conversation in ChatGPTClient.
2. A remote platform starts or is already generating a response for that conversation.
3. User taps Sync once.
4. Native performs the authoritative latest-message sync.
5. If the authoritative latest-user/turn state changed, the covered target page is re-armed exactly once.
6. The existing page-owned external-response path adopts the latest available reasoning/tool snapshot.
7. If the response is still active, later page-owned snapshots may continue updating without another synthetic response owner.
8. If the response is already complete, Sync must converge to the latest completed authoritative state.

This requirement does **not** require automatic request-start discovery, token-by-token external reasoning, token-by-token external final text, hidden polling, timers, retry loops, duplicate Send, WebSocket-body content authority or fake typewriter animation.

The phrase `latest reasoning stream` for this MVP means **latest cumulative reasoning/tool snapshot(s)**. It is not a claim of token-level streaming.

## Evidence supporting this scope

### b79 manual Sync — Runtime Positive

`docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md` proves the explicit manual path on real device:

- explicit Sync started;
- authoritative Detail advanced `45 -> 46`;
- covered observation entered `mode=manual_sync_rearm`;
- an `external_page_owned` live response started;
- reasoning/tool snapshots were subsequently adopted.

The same evidence also proves external reasoning/tools are page-snapshot granular, not token-streaming.

### b80 preservation/fix

`docs/project/runtime-evidence/DEV-send-stream-b80-device-runtime-20260901.md` preserves the manual-Sync re-arm path and fixes the later COMPLETE/final-materialization race. Stopped-thinking semantics and the final-materialization gate remain preserved.

### b81/b82 automatic acquisition

- b81 found a target-correlated socket signal but did not automatically acquire the external response.
- b82 automatically acquired the completed turn, but the signal arrived too late for live UX.

These automatic-acquisition results no longer block the narrowed MVP because automatic early discovery is now optional follow-up work rather than a release gate.

## Current answer to the MVP question

**Architecture/evidence: Yes, the manual path is already evidence-backed and likely already present in b82.**

**Stable/Frozen: Not yet.** The exact narrowed requirement has not yet been re-run as a focused b82 Human Runtime gate across repeated active-turn cases. Do not describe it as Stable until that gate passes.

A very large conversation may make the authoritative Sync itself slow; b79 recorded a roughly 2.2 MB Detail response taking about 10 seconds. That is latency, not a failure to acquire reasoning.

## Official native realtime research

The official iOS realtime Probe/research package remains useful future evidence, but it is no longer on the critical path for the MVP. Do not spend a product Candidate on native WebSocket integration unless the user later restores automatic acquisition as a requirement.

Research artifacts/evidence remain preserved under:

- `docs/project/runtime-evidence/DEV-send-stream-official-ios-runtime-hook-plan-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-build-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-export-ui-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-trollstore-package-20260902.md`

The official package remains an evidence oracle, not a ChatGPTClient product dependency.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- no duplicate Send/resend, fake streaming, speculative retry/watchdog/fallback, hidden fixed polling or second response store.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 8**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

**Do not allocate b83 yet. Do not continue the official realtime Probe as the critical path.**

Use exact b82 first for a focused manual-MVP Human Runtime gate:

- start a sufficiently long remote response while the target conversation is selected;
- during active reasoning, press Sync once;
- verify the latest remote user turn is acquired and the latest cumulative reasoning/tool snapshot appears;
- leave the response active and verify whether subsequent page-owned snapshots continue updating;
- repeat on at least one second conversation/turn;
- after completion, press Sync once and verify convergence to the latest final state.

If b82 passes this focused gate repeatedly, freeze manual external acquisition as the MVP and remove automatic early acquisition/native WebSocket research from the Send release blocker. If b82 fails, allocate b83 only for the smallest evidence-backed manual-Sync determinism fix.