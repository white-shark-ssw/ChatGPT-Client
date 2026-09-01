# DEV-send-stream

## Status

**Active — exact b79 Runtime is partial-positive / partial-rejected. The next evidence-backed product candidate is b80, but b80 is not allocated until the fresh pre-allocation identity guard below is completed. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b79 product/config source: `a3d307b05d70e95568672bc29b0c939b7f3b8141`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)`
- Guarded staging validation: `33488975445 / 99795672696` — exact scope + `git diff --check` + Xcode 16.4 Simulator passed
- Formal Push CI: `33489654106 / 99797864816` — success
- Formal PR CI: `33489658656 / 99797878467` — success
- Canonical Push Artifact: `9793240789`
- Artifact ZIP SHA: `2016508002ae7ff43d803c90fcbb92ba01c45906c885be6f6e50a1e43e1e87fc`
- IPA SHA: `39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`
- b39-b79 permanently reserved
- Runtime/manual/real-device b79: **Partial / rejected**
- Stable/Frozen Send: **No**

Durable b79 evidence: `docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md`.

## Resume / identity / conflict guard

The selected Work remains `DEV-send-stream`. Before this Runtime evidence sync:

- formal feature head was `608d7d77f2d65c786eab5ac5a0b04095f02d608a`;
- PR #29 remained open / mergeable / unmerged and based on `main`;
- `main` remained `d323b9eed2dda75b9986fc06e14014d3e9b365fb`, so no target/base drift was observed;
- exact search found no `DEV-send-stream-0.1.0-b80` before this evidence sync;
- `docs/project/current/dev/` still had a stale temporary b79 scope marker in addition to this checkpoint and README; it is assembly residue, not a separate Active Work, and must be removed now that b79 is classified.

Re-run the branch/PR/main/b80 non-use guard immediately before allocating b80.

## Exact b79 Runtime classification

### Tool presentation

**Partial positive / rejected.** The stronger special tool-operation presentation remains visible, but the final tool row still has asymmetric space above/below. b79 neutralized only inter-item attributed-string transitions. The terminal timeline -> horizontal reasoning-divider boundary is still separately owned by cell geometry, so the last tool row and divider do not share one spacing owner.

### Manual-Sync external re-arm

**Positive.** An explicit Sync that discovers a changed latest user turn re-arms/reloads the same covered official page once. The supplied diagnostics then show `manual_sync_rearm`, page load, external response start, `/resume` 404 JSON page-owned fallback, and adopted reasoning/tool snapshots before completion.

### External stopped-thinking semantics

**Positive.** External terminal-without-final now preserves reasoning/tools instead of promoting reasoning into normal final body text. The tested stopped-thinking case retains reasoning and tools with final characters remaining zero.

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

## Evidence-backed b80 scope — not yet allocated at this checkpoint

Only these product changes are authorized by b79 Runtime:

1. **Final timeline/tool -> reasoning-divider spacing:** make the last visible reasoning/tool item use the same deterministic neutral vertical-rhythm owner as other timeline transitions; do not blindly increase line height.
2. **Normal external COMPLETE materialization gate:** after consuming a page-owned `complete=true` snapshot, if this is a normal response with `reasoningEnded == true` but `finalText` is still empty, do not terminalize/release yet. Keep the same covered page observation alive for its own subsequent page-owned reads. Terminal normally when a real final body is observed. Preserve the already-positive stopped-thinking path where reasoning did not end and no final exists.
3. **No automatic Sync/haptic implementation in b80.** The official-app completion signal observation is a future protocol-evidence gate, not authorization for polling.
4. **No progressive-final invention.** No timer/poll/retry/watchdog, duplicate Sync/Send, fake typewriter, DOM-body authority, WebSocket-body authority, second response owner or compatibility shim.

Expected minimum product scope after exact call-site inspection: `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`, plus identity-only Xcode/workflow changes if b80 is allocated.

## Retained architecture / protocol boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response owner.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned observation transport only, not a second message store.
- b67 local protected Send and b72 tested simultaneous ownership remain accepted predecessors.
- `assistant:thoughts` / hidden COT remain non-presentational.
- No Native polling/cadence, Native resume/offset synthesis, duplicate Send, retry/timer/watchdog, guessed fallback, fake final streaming, DOM-body authority or WebSocket-body authority.

## Evidence classification

- b79 Code/static/Simulator/Push+PR CI/Artifact/package: **Verified**
- b79 Runtime/manual/real-device: **Partial / rejected**
- Tool prominence: **Positive**
- Tool terminal-boundary spacing symmetry: **Rejected**
- Manual-Sync external re-arm: **Positive**
- External stopped-thinking semantics: **Positive**
- External reasoning/tool adoption: **Positive at page-snapshot granularity only**
- External progressive final: **Rejected / no authorized progressive source**
- COMPLETE/final-materialization handling: **Rejected; premature terminal/release localized**
- Official-app account-wide completion haptic mechanism for this client: **Unknown / Unverified**
- Stable/Frozen Send: **No**

## Next exact action

1. Remove the stale temporary b79 assembly scope marker.
2. Re-check formal branch / PR / main base and exact b80 non-use.
3. If still clean, allocate `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)` once.
4. Implement only the two evidence-backed product corrections above.
5. Run exact-scope/static checks and Xcode 16.4 Simulator build through the guarded assembly path; then formal Push + PR CI, canonical IPA production and independent package verification.
6. Human Runtime gate: verify the last tool row has symmetric divider spacing; a normal remote response no longer terminalizes before its final body materializes; stopped-thinking and manual-Sync re-arm remain positive; note that progressive final token streaming remains an open protocol gap.

Do not claim CI/Artifact success as Runtime success.
