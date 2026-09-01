# DEV-send-stream

## Status

**Active — b81 automatic external acquisition is Runtime-rejected, while its at-document-start WebSocket structural probe is Runtime-positive and supplies an evidence-backed one-shot acquisition trigger. `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)` is allocated to convert that exact target-conversation event into one bounded authoritative Sync + one covered-page re-arm. Account-wide notification remains deferred. b80 spacing and external stopped-thinking semantics remain Frozen. Stable/Frozen Send as a whole remains No.**

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

## b81 Runtime finding

Exact b81 diagnostics show the covered `ws.chatgpt.com` socket created/open before the remote turn, then two JSON-array frames with exact current-conversation `targetMatch=true` at 16:22:20Z and 16:24:24Z while Native still had no `externalStreamingObserved`, no external snapshot and no Repository external response. Manual Sync at 16:24:59Z returned authoritative Detail with visible messages 4 -> 8 and four added messages, then invoked the already-positive `manual_sync_rearm` path.

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

1. the first b81 structural WebSocket `message` with `targetMatch=true` during an external observation cycle emits one external-acquisition hint only if no response has yet been acquired;
2. that hint triggers exactly one `ConversationRepository.syncLatestMessages(id:)` for the currently selected conversation;
3. after that one Sync completes, if the same conversation is still selected and no response was acquired naturally meanwhile, perform exactly one covered-page re-arm/reload;
4. existing page-owned `stream_status / plural-read` remains the reasoning/tool/final content source;
5. the second target-matching frame in the same observation cycle must not cause duplicate automatic Sync.

No timer, polling cadence, retry/watchdog, repeated auto-Sync loop, WebSocket body authority, Native status/body synthesis, duplicate Send, fake progressive final, account-wide notification work, or Frozen presentation change is authorized.

If the one automatic Sync fails, record it and stop; manual Sync remains recovery.

## b82 Runtime gate

Open A in b82, start a long turn in the same A from another platform, and do not press Sync. Expected sequence: target-matching WebSocket hint -> exactly one automatic authoritative Sync -> exactly one covered-page re-arm -> page-owned reasoning/tools acquisition. Repeat at least twice and export Diagnostics. Progressive final token streaming is not claimed solved by b82.

## Session round counter

Current work is round 19. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Assemble/validate the three-file b82 candidate in an isolated tooling branch, then formal Push+PR CI, canonical Artifact, independent IPA verification and Human Runtime handoff. Do not allocate b83 before b82 Runtime classification.
