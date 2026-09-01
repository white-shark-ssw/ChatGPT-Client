# DEV-send-stream

## Status

**Active — exact b79 Runtime is partial-positive / partial-rejected. `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)` is now allocated for the two evidence-backed corrections below; product assembly is in progress. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b79 product/config source: `a3d307b05d70e95568672bc29b0c939b7f3b8141`
- Allocated next Candidate / Version-Build: `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)`
- b39-b80 permanently reserved
- Runtime/manual/real-device b79: **Partial / rejected**
- Runtime/manual/real-device b80: **Not yet produced**
- Stable/Frozen Send: **No**

Durable b79 evidence: `docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md`.

## Resume / identity / conflict guard

Immediately before b80 allocation:

- formal feature branch `dev/send-stream-20260829` was at `412ed03c7519649bd65ec90e1d061e23ecfd820b`;
- PR #29 remained open / mergeable / unmerged, head branch `dev/send-stream-20260829`, base `main`;
- PR/base `main` remained `d323b9eed2dda75b9986fc06e14014d3e9b365fb`, so no target/base drift was observed;
- exact repository search returned no `DEV-send-stream-0.1.0-b80` before allocation;
- the stale temporary b79 assembly marker was removed; `docs/project/current/dev/` has no second Active Work checkpoint;
- no parallel Active branch/candidate conflict was found.

Therefore b80 is allocated exactly once here. Do not allocate b81 until b80 Runtime is classified.

## Exact b79 Runtime classification

### Tool presentation

**Partial positive / rejected.** The stronger special tool-operation presentation remains visible, but the final tool row still has asymmetric space above/below. b79 neutralized only inter-item attributed-string transitions. The terminal timeline -> horizontal reasoning-divider boundary is still separately owned by cell geometry, so the last tool row and divider do not share one spacing owner.

### Manual-Sync external re-arm

**Positive.** An explicit Sync that discovers a changed latest user turn re-arms/reloads the same covered official page once. The supplied diagnostics then show `manual_sync_rearm`, page load, external response start, `/resume` 404 JSON page-owned fallback, and adopted reasoning/tool snapshots before completion.

### External stopped-thinking semantics

**Positive.** External terminal-without-final now preserves reasoning/tools instead of promoting reasoning into normal final body text.

### Cross-platform streaming boundary

**Reasoning/tools remain only page-snapshot granular.** Tool count and service-message structure advance in coarse page-owned snapshots; this is not token/SSE-delta reasoning streaming.

**Progressive final remains unavailable.** Final characters remain zero through the observed final phase. No fake typewriter, Native polling/cadence, DOM-body authority or WebSocket-body authority is justified.

### New exact b79 defect — COMPLETE/final materialization race

**Rejected; root cause localized.** In the latest run, page-owned snapshots enter final phase with reasoning ended and five tools but `finalCharacters=0`. The page later reports `complete=true` while the final body is still absent. Current b79 immediately terminalizes/releases the covered executor and performs one authoritative Detail reconcile; that Detail still has no new assistant message. With the observation owner already released, the later materialized final is missed until a manual Sync about a minute later.

Current bridge/source explains the race:

- page `COMPLETE` sets `completePending`;
- the first following plural conversation read posts `complete=true` and immediately clears external streaming state;
- Swift unconditionally terminalizes/releases on that `complete` flag even when normal reasoning has ended but `finalText` is still empty.

For a normal external response, `COMPLETE` is therefore not sufficient terminal evidence when `reasoningEnded == true && finalText.isEmpty`.

### Large-conversation manual Sync latency

One supplied Detail Sync transferred roughly 2.2 MB and took about 10.27 seconds. This explains a separate short-lived `正在同步最新消息…` delay but not the later missing-final case above.

## Official-app completion haptic / automatic Sync boundary

The user reports that official ChatGPT iOS gives a two-stage haptic when any account conversation completes even if another screen/conversation is visible. Treat that as user Runtime evidence that **the official app has an account-wide completion signal**, but the transport is **Unknown / Unverified** for this client.

- For responses already owned by this client's `ConversationRepository`, a completion haptic is straightforward to trigger from the accepted terminal transition.
- Account-wide haptic/automatic Sync for conversations this client is not currently observing requires a proven account-level event source.
- If a privacy-safe account-level completion/new-turn event is later evidenced, one deduplicated event may drive both a haptic and one bounded authoritative Sync/list refresh.
- Do not infer APNs, WebSocket, service-worker or another mechanism from haptic behavior alone.
- Do not implement fixed polling/timers/watchdogs to imitate it.

## Exact b80 product scope

Only these product changes are authorized:

1. **Final timeline/tool -> reasoning-divider spacing:** the final expanded timeline boundary must use the same neutral separator representation as inter-item transitions. Remove the separate pre-divider spacing owner so the last tool/reasoning item and the divider share one deterministic rhythm. Do not increase the 36-point tool line height.
2. **Normal external COMPLETE materialization gate:** after consuming page-owned `complete=true`, if the external snapshot has `reasoningEnded == true` but `finalText` is still empty, do not terminalize/release. Keep the same covered page observation alive for its own subsequent page-owned plural reads. Terminal normally when a real final body is present. Preserve the b79-positive stopped-thinking terminal case where reasoning did not end and no final exists.
3. **Bridge ownership correction:** do not clear the page-owned external observation state merely because the first COMPLETE-associated plural snapshot was posted; native release remains the terminal owner.
4. **Identity-only changes:** Xcode Build 80/Candidate b80 and workflow artifact identity.

Explicitly excluded from b80:

- automatic Sync / account-wide haptic implementation;
- timer/poll/retry/watchdog;
- duplicate Sync/Send;
- fake progressive final/typewriter;
- DOM-body or WebSocket-body authority;
- Native resume/offset synthesis;
- second response owner or unrelated refactor.

Expected exact product/config scope: `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`, `ChatGPTClient.xcodeproj/project.pbxproj`, `.github/workflows/ios-foundation.yml`.

## Retained architecture / protocol boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response owner.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned observation transport only, not a second message store.
- b67 local protected Send and b72 tested simultaneous ownership remain accepted predecessors.
- b79 manual-Sync re-arm and stopped-thinking semantics are positive predecessors to preserve.
- `assistant:thoughts` / hidden COT remain non-presentational.
- No Native polling/cadence, Native resume/offset synthesis, duplicate Send, retry/timer/watchdog, guessed fallback, fake final streaming, DOM-body authority or WebSocket-body authority.

## Evidence classification

- b79 Code/static/Simulator/Push+PR CI/Artifact/package: **Verified**
- b79 Runtime/manual/real-device: **Partial / rejected**
- b80 Candidate allocation: **Done**
- b80 Code/static/CI/Artifact/Runtime: **Pending**
- Stable/Frozen Send: **No**

## Next exact action

1. Assemble the four-file b80 scope from formal head `412ed03c...` plus this allocation checkpoint.
2. Validate exact source substitutions, no prohibited retry/poll/timer/watchdog patterns, `git diff --check`, and Xcode 16.4 Simulator build.
3. If validation passes, transplant only the four product/config files to the formal feature branch, run Push + PR CI, produce and independently verify the canonical b80 IPA, then update checkpoint/durable state/PR in the same round.
4. Human Runtime gate: verify the last tool row has symmetric divider spacing; a normal remote response no longer terminalizes before its final body materializes; stopped-thinking and manual-Sync re-arm remain positive; note that progressive final token streaming remains an open protocol gap.

Do not claim CI/Artifact success as Runtime success.
