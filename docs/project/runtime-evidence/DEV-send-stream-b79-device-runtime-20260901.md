# DEV-send-stream b79 device Runtime — 2026-09-01

## Candidate under test

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b79`
- Version / Build: `0.1.0 (79)`
- Exact product/config source: `a3d307b05d70e95568672bc29b0c939b7f3b8141`
- Canonical Artifact: `9793240789`
- IPA SHA-256: `39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`
- Supplied diagnostics metadata reports Release `0.1.0`, Build `79`, Candidate `DEV-send-stream-0.1.0-b79`, source marker `a3d307b05d70`, iPhone / iOS 17.0.

## User Runtime findings

### 1. Tool operation prominence remains positive, but the last tool -> reasoning-divider boundary is still asymmetric

The supplied screenshot confirms the distinct tool-operation presentation remains active, but the vertical gap above and below the final tool operation is still visibly uneven.

The b79 neutral 12-point attributed separator only owns transitions **between timeline items**. Current cell geometry separately owns the terminal timeline-to-divider boundary: after the expanded reasoning body, `metrics(...)` adds 12 points before the horizontal reasoning divider and another 12 points after it. Therefore b79 removed previous-item ownership inside the timeline but did not unify the last timeline item -> divider transition with the same spacing owner.

Runtime result: **Partial positive / terminal-boundary spacing rejected.** The next correction should unify the final timeline boundary with the same neutral rhythm rather than increasing tool line height again.

### 2. Explicit manual-Sync re-arm is Runtime positive

The exported run proves the b79 event-driven re-arm works when Native is already displaying the conversation:

- 11:06:47Z explicit `conversation.latestSync.requested` starts;
- Detail HTTP200 completes at 11:06:57Z and increases visible messages 45 -> 46;
- 11:06:59Z `coveredExecutor.observing` reports `mode=manual_sync_rearm`;
- the covered page loads at 11:07:00Z;
- by 11:07:06Z an `external_page_owned` live response starts;
- page-owned `/resume` returns HTTP404 JSON and the current page-owned read fallback continues;
- reasoning/tool snapshots are adopted at 11:07:09Z and 11:07:15Z.

Runtime result: **Positive for the tested explicit-manual-Sync re-arm path.** This is not automatic Sync and does not authorize polling.

### 3. External stopped-thinking semantics are Runtime positive

In the first re-armed external run, terminal occurs with `finalCharacters=0`, `reasoningCharacters=134` and three tool rows. b79 preserves the reasoning/tool state instead of promoting it into final body text, matching the user's confirmation that the previous “思考变正文” defect is fixed.

Runtime result: **Positive for the tested external terminal-without-final stopped-thinking behavior.** The b67 local protected-Send fallback remains a separate accepted predecessor.

### 4. Cross-platform reasoning/tools remain page-snapshot granular; progressive final remains unavailable

The second external response advances through page-owned snapshots rather than token/SSE deltas:

- 11:07:52Z: reasoning 146 chars / 1 tool / 6 service messages;
- 11:07:58Z: reasoning 146 / 2 tools / 8 messages;
- 11:08:06Z: reasoning 146 / 3 tools / 10 messages;
- 11:08:13Z: reasoning 146 / 4 tools / 11 messages;
- 11:08:19Z: reasoning 146 / 4 tools / 12 messages;
- 11:08:26Z: phase final / reasoning 146 / 5 tools / 17 messages / `finalCharacters=0`.

The visible reasoning text itself can stay unchanged while tool state progresses, so this is not token-level reasoning streaming. Final body remains zero characters throughout the observed final phase.

Runtime result: **Reasoning/tool adoption positive only at coarse page-owned snapshot granularity; progressive external final remains rejected/unavailable from the current authorized source.** No fake typewriter, Native polling/cadence, DOM-body authority or WebSocket-body authority is justified.

### 5. New exact defect: COMPLETE can precede final-message materialization, causing premature terminal/release

The final b79 run localizes the user's “很久无法刷新出最新消息” report to a terminal/materialization race rather than a generic refresh failure.

Sequence:

1. At 11:08:26Z the external snapshot enters `phase=final` with `reasoningCharacters=146`, five tools and `finalCharacters=0`.
2. Additional page-owned snapshots at 11:08:32Z and 11:08:39Z still have `finalCharacters=0`.
3. At 11:08:46Z the page reports `complete=true`, but the projected Native snapshot still has `finalCharacters=0`.
4. Current b79 immediately marks the Repository response terminal, releases the covered executor, and starts authoritative reconciliation.
5. That immediate Detail reconciliation returns HTTP200 at 11:08:48Z but still has 47 visible messages — no new final assistant message — so `liveSnapshotCleared=false`.
6. Because the observation owner has already been released, no later page-owned update is adopted.
7. Only the user's later manual Sync at 11:09:50Z obtains Detail HTTP200 at 11:09:52Z with visible messages 47 -> 48, after which the terminal live snapshot can finally be cleared.

Current source explains the race: the bridge marks the first plural read after page `COMPLETE` as `complete=true` and clears its external-streaming state immediately; Swift unconditionally terminalizes/releases on that `complete` flag even when the projected response has ended reasoning but still has no real final body.

Runtime result: **Rejected; root cause identified.** `COMPLETE` is not sufficient terminal evidence for a normal external response when `reasoningEnded=true` but `finalText` is still empty. The observation owner must remain alive until a real final body materializes, while the already-evidenced stopped-thinking case (`reasoningEnded=false`, no final) must still be allowed to terminalize.

This correction can remain event-driven: keep observing the official page's own later reads; do not add timers, polling, retries or duplicate Sync.

### 6. One explicit Sync can itself be slow on a very large conversation

The 11:06:47Z manual Detail Sync transferred about 2.2 MB and took `10266.94ms`. This separately explains why the `正在同步最新消息…` presentation can remain visible for around ten seconds on this long conversation. It does not explain the later one-minute missing-final case, which is the terminal/materialization race above.

### 7. Official-app account-wide completion haptic observation

The user reports that the official ChatGPT iOS app produces a two-stage haptic when any account conversation completes, even while the app is on another screen/conversation. Treat this as **user Runtime evidence of an account-wide completion signal in the official app**, but the transport/mechanism is **Unknown / Unverified**. The observation alone does not prove whether the source is APNs/push, an account-level realtime connection, or another private service mechanism.

For this client, a response already owned by `ConversationRepository` can trivially drive one completion haptic from its accepted terminal transition. Account-wide haptic / automatic Sync for conversations that this client is not currently observing requires a proven account-level completion/new-turn event source. If such a signal is later evidenced, the same event can drive both a deduplicated haptic and one bounded authoritative Sync without polling. Until then, no fixed timer/poll/watchdog implementation is authorized.

## Evidence-backed next-candidate boundary

The next product candidate may contain only:

1. **Unify the final timeline/tool -> reasoning-divider spacing boundary** so the last tool row uses the same deterministic neutral rhythm as other timeline transitions.
2. **Defer normal external terminal while final is not materialized:** when page-owned `complete=true` arrives after reasoning has ended but `finalText` is still empty, keep the existing covered observation alive instead of terminalizing/releasing. Terminal normally when a real final body is observed; retain the external stopped-thinking terminal behavior when reasoning never ended and no final exists.
3. **Keep page-owned observation event-driven.** Do not add timer/poll/retry/watchdog/automatic Sync/fake final streaming/DOM-body/WebSocket-body authority.
4. **Do not add account-wide haptic/automatic Sync in this candidate.** The official-app observation becomes a future evidence gate for discovering a real account-level event source.

## Evidence classification

- b79 Code/static/Simulator/Push+PR CI/Artifact/package: **Verified**.
- b79 Runtime/manual/real-device: **Partial / rejected**.
- Tool prominence: **Positive**.
- Tool terminal-boundary spacing symmetry: **Rejected**.
- Manual-Sync external re-arm: **Positive**.
- External stopped-thinking semantics: **Positive**.
- External reasoning/tool adoption: **Positive only at page-snapshot granularity; not token-streaming**.
- External progressive final: **Rejected / no authorized progressive source**.
- External COMPLETE/final-materialization handling: **Rejected; premature terminal/release root cause identified**.
- Account-wide completion haptic mechanism: **Unknown / Unverified for this client**.
- Stable/Frozen Send: **No**.
