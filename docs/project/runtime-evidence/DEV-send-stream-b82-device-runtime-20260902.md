# DEV-send-stream b82 device Runtime — 2026-09-02

## Candidate under test

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b82`
- Version / Build: `0.1.0 (82)`
- Exact product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Canonical Push Artifact: `9811406038`
- IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- Supplied diagnostics: `ChatGPTClient-Diagnostics-20260901-175030.json`
- Diagnostics metadata: Release 0.1.0, Build82, Candidate b82, source marker `c7a274786dfd`, iPhone / iOS17.0.

## User-visible Runtime result

The user confirms b82 **did automatically update without pressing Sync**, but the update was too late for live conversation UX:

- the remotely sent user message did not appear promptly;
- the assistant response did not appear progressively;
- both appeared only when the long assistant answer had apparently already fully generated.

User requirement after this test: a long cross-platform turn must show promptly that the request was received and must expose real progressive response state instead of leaving Native unchanged until completion.

Runtime classification: **Partial — automatic final acquisition positive; live-acquisition timing rejected.**

## Exact event sequence

### Covered page and user socket ready before the remote turn

- 17:48:33Z: selected conversation begins covered observation in `mode=selection`.
- 17:48:34Z: authoritative Detail is loaded with 8 visible messages.
- 17:48:37Z: `wss://ws.chatgpt.com/p24/ws/user/{id}` structurally observed as `created`.
- 17:48:38Z: socket `open`.
- 17:48:39Z: initial JSON-array message, 371 chars, `targetMatch=false`.

The WebSocket probe is injected at document start. The current source records every interesting incoming socket message up to a 200-message budget and reports string/JSON/ArrayBuffer/typed-array/Blob shape, so an unlogged ordinary incoming frame during this short reproduction is not explained by late attachment.

### No early acquisition signal was observed

Between the initial socket frame and the eventual target-match frame, the export contains no:

- additional `coveredExecutor.webSocketStructure` message;
- `coveredExecutor.externalStreamingObserved`;
- `coveredExecutor.externalSnapshot`;
- Repository `liveResponse.started` for an external response;
- Repository external snapshot update.

Therefore b82 had no evidenced event from which to show the remote user turn or start Native response presentation during the actual generation interval.

### The one target-match event arrived when authoritative Detail was already two visible messages ahead

At 17:49:56Z:

- user socket JSON-array message length 180 arrives with exact `targetMatch=true`;
- b82 emits `coveredExecutor.externalAcquisitionHint`;
- `externalAcquisitionSync.started` and authoritative `latestSync.start` begin immediately from previous visible count 8.

At 17:49:57Z:

- authoritative Detail HTTP200 returns 10 visible messages;
- `latestSync.end` reports `8 -> 10`, `addedVisibleMessageCount=2`, `changedVisibleMessageCount=2`;
- `externalAcquisitionSync.completed` reports `latestUserChanged=true`;
- Native applies 10 authoritative messages;
- b82 performs the one forced covered-page re-arm.

The user reports that this is when both the remote user message and assistant answer became visible, and that the answer had already finished generating. The +2 authoritative visible messages are consistent with the newly completed user/assistant turn.

### Re-arm did not acquire an active response

- 17:49:58Z: re-armed covered page finishes loading.
- 17:50:00Z/01Z: new user socket created/opened; initial 371-char JSON-array frame again has `targetMatch=false`.
- no `externalStreamingObserved`, no external snapshot and no Repository live response follow before the diagnostics export.

This is consistent with the target-match event/re-arm occurring after the server response was already complete, not during an active turn.

## Architectural conclusion

b82 proves the current exact-conversation user-socket notification is useful as a **completion/update trigger** but is too late to be the desired cross-platform request-start/live-stream trigger in this reproduction.

The already-authorized page-owned `stream_status` + plural-conversation path remains capable of following an active external response **once the official page itself enters that path**. The b82 export shows that an already-open covered page did not autonomously enter that path before the completion notification.

Therefore simply making b82's existing observation more frequent cannot solve the delay: there was no earlier observed event to consume.

## Next evidence gate before new product behavior

Determine whether an **already-open visible official ChatGPT Web page** on the same conversation behaves differently when another platform starts the turn:

1. if visible Web itself immediately sees the remote user turn / begins active-response requests, capture the concrete visibility/focus/network behavior and reproduce only that evidenced browser behavior in the covered executor;
2. if visible Web also remains unchanged until completion, then current official-page passive behavior supplies no early trigger. The project must then separately evidence a subscribable real-time turn signal or explicitly authorize a bounded selected-conversation status-monitoring design.

Do not silently introduce polling/timers, duplicate Send, WebSocket body message authority, synthetic user bubbles or fake progressive text to mask the missing early source.

Public/third-party observations that `ws.chatgpt.com` supports conversation updates/notifications and that current clients may subscribe to generic/per-turn WebSocket topics are useful hypotheses only. They are not product authority until reproduced on the exact current account/page flow.

## Evidence classification

- Code/static/Simulator/Push+PR CI/Artifact/package for b82: **Verified**.
- Automatic no-manual-Sync final refresh: **Runtime Positive**.
- Remote user message shown promptly: **Runtime Rejected**.
- External active response acquired before completion: **Runtime Rejected for timing**.
- Progressive reasoning/final stream in this run: **Not acquired**.
- Current `targetMatch=true` as completion/update notification: **Positive**.
- Current `targetMatch=true` as start/live trigger: **Rejected by this reproduction**.
- Stable/Frozen Send as a whole: **No**.