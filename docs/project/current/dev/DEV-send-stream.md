# DEV-send-stream

## Status

**Active — b81 automatic external acquisition is Runtime-rejected, while its at-document-start WebSocket structural probe is Runtime-positive. The user confirms the two observed `targetMatch=true` frames corresponded to two separate remote Sends, so the prior “first frame only per observation cycle” interpretation is withdrawn. `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)` remains allocated to convert each eligible target-conversation event into one bounded authoritative Sync, with one re-arm only when authoritative latest-user identity actually changes. Account-wide notification remains deferred. b80 spacing and external stopped-thinking semantics remain Frozen. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29
- Actual main at allocation: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b81 product/config source: `d1d4d197cc5d2a5022a28b332afebe485b216ea1`
- b81: `DEV-send-stream-0.1.0-b81` / `0.1.0 (81)` / Artifact `9809150111`
- b81 IPA SHA-256: `d48d2398dc5a7ef16b9983021a9173d87ba3b852f4a45c9431dff2ebcf057038`
- Allocated b82: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- b39-b82 permanently reserved
- b81 Runtime: automatic acquisition rejected / structural trigger positive
- b82 Runtime: not yet produced
- Stable/Frozen Send: No

Durable b81 Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b81-device-runtime-20260901.md`.
Durable b82 allocation evidence: `docs/project/runtime-evidence/DEV-send-stream-b82-allocation-20260901.md`.

## Corrected b81 Runtime finding

Exact b81 diagnostics show the covered `ws.chatgpt.com` socket created/open before the remote activity, then two JSON-array frames with exact current-conversation `targetMatch=true` at 16:22:20Z and 16:24:24Z while Native still had no `externalStreamingObserved`, no external snapshot and no Repository external response. The user confirms **two separate messages were sent remotely** during this test. Therefore the two target-matching frames are not duplicate noise from one response; they are correlated with two separate remote Sends/new turns.

Manual Sync at 16:24:59Z returned authoritative Detail with visible messages 4 -> 8 and four added visible messages, consistent with two new user/assistant turns, then invoked the already-positive `manual_sync_rearm` path.

Therefore a target-conversation-correlated socket event reaches the covered page before the currently unreliable page-owned `stream_status` acquisition path. The event is authorized only as a discovery trigger; WebSocket content remains non-authoritative.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- explicit manual-Sync re-arm: preserve as recovery.
- b67 client-owned Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole response/content owner.
- account-wide notification/haptic discovery is deferred.
- progressive external final token streaming remains unresolved and must not be faked.

## Exact b82 scope

Only `ChatGPTClient/RootViewController.swift`, `ChatGPTClient.xcodeproj/project.pbxproj`, and `.github/workflows/ios-foundation.yml` are authorized.

Root behavior:

1. each b81 structural WebSocket `message` with `targetMatch=true` may emit a bounded external-acquisition hint when the executor is observing the currently selected existing conversation, no Repository live response is active, and no automatic acquisition Sync for that conversation is currently in flight;
2. one accepted hint triggers at most one `ConversationRepository.syncLatestMessages(id:)`;
3. capture authoritative latest-user identity before/after Sync;
4. after Sync succeeds, only when latest-user identity changed, the same conversation remains selected, and no response was acquired naturally meanwhile, perform exactly one covered-page re-arm/reload;
5. if Sync reports no latest-user change, log `no_change` and stop without reload;
6. if Sync fails, log and stop; manual Sync remains recovery;
7. after the previous auto Sync finishes, a later distinct target-matching frame may trigger another bounded acquisition attempt. This preserves the two-distinct-Send behavior proven by b81.

No timer, polling cadence, retry/watchdog, repeated automatic loop, WebSocket body authority, Native status/body synthesis, duplicate Send, fake progressive final, account-wide notification work, or Frozen presentation change is authorized.

## b82 Runtime gate

Open A in b82, start a long turn in the same A from another platform, and do not press Sync. Expected sequence: target-matching WebSocket hint -> one automatic authoritative Sync -> if latest user changed, one covered-page re-arm -> page-owned reasoning/tools acquisition. Run at least two separate remote Sends in the same selected conversation and verify both can independently trigger acquisition without manual Sync. Export Diagnostics. Progressive final token streaming is not claimed solved by b82.

## Session round counter

Current work is round 20. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Clean the temporary b82 assembly residue created during connector orchestration, then assemble/validate the corrected three-file b82 candidate in an isolated tooling branch; proceed through formal Push+PR CI, canonical Artifact, independent IPA verification and Human Runtime handoff. Do not allocate b83 before b82 Runtime classification.
