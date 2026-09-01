# DEV-send-stream

## Status

**Active — exact b82 Runtime is now Partial: automatic cross-platform acquisition works, but the evidenced `targetMatch=true` trigger is completion-time rather than start-time. The user's remote user message and assistant answer appeared only after the long answer had already completed. Therefore b82 closes the manual-Sync requirement for final refresh, but it does not satisfy request-received visibility or live reasoning/final streaming. b80 spacing and external stopped-thinking semantics remain Frozen. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Current formal branch head at this Runtime classification: `5dc69b8ac8ac7d7f1acaf9e9a2d3b8703c042bb8`
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b82 product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- Guarded assembly attempt 2: `33534965707 / 99946924531` — success
- Formal Push CI: `33535342383 / 99948156535` — success
- Formal PR CI: `33535347654 / 99948174293` — success
- Canonical Push Artifact: `9811406038`
- Artifact ZIP SHA-256: `bcb9c65f7cee7680580acd6238d3dd9f03f30b3c5f9024cd251b31690ac13681`
- IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- b39-b82 permanently reserved
- b82 Runtime: **Partial — automatic final acquisition positive / live acquisition timing rejected**
- b83: **not allocated**
- Stable/Frozen Send: No

Durable predecessors:

- `docs/project/runtime-evidence/DEV-send-stream-b81-device-runtime-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b82-allocation-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b82-build-artifact-20260902.md`

## Exact b82 Runtime finding — 2026-09-02

User supplied exact b82 diagnostics `ChatGPTClient-Diagnostics-20260901-175030.json`; metadata confirms Release `0.1.0`, Build82, Candidate `DEV-send-stream-0.1.0-b82`, source marker `c7a274786dfd`, iPhone / iOS17.0.

Observed sequence:

1. 17:48:33Z A is selected and the covered executor begins observing the existing conversation.
2. 17:48:37Z/38Z the `ws.chatgpt.com` user socket is created/opened; 17:48:39Z initial JSON-array frame is `targetMatch=false`.
3. During the long remote turn there is no earlier `websocket_structure message`, no `externalStreamingObserved`, no `externalSnapshot`, and no Repository external live-response start.
4. 17:49:56Z one JSON-array socket frame arrives with exact `targetMatch=true`; b82 immediately starts `externalAcquisitionSync`.
5. 17:49:57Z authoritative Detail returns HTTP200 with visible messages **8 -> 10**, `addedVisibleMessageCount=2`, and `latestUserChanged=true`.
6. The user reports that at this point both the remotely sent user message and the assistant answer appeared, and the assistant answer had already completely generated.
7. b82 then performs its one re-arm. The covered page reloads by 17:49:58Z and opens a new user socket at 17:50:00Z/01Z, but no `externalStreamingObserved`, no external snapshot and no live Repository response follows. This is consistent with the response already being complete before the trigger/re-arm.

The current `CoveredWebSendExecutor` WebSocket probe is injected at document start and records every interesting incoming socket message up to a 200-message budget, including string/JSON/binary shape. Therefore the absence of another incoming frame in this reproduction is meaningful evidence: the current observed user-level `targetMatch=true` frame is not an early request-start signal for this flow.

## Runtime classification

- Automatic refresh without pressing Sync: **Positive**.
- Remote user-message visibility before answer completion: **Rejected**.
- Automatic acquisition of an active external response: **Rejected for timing**.
- External reasoning/tools/final live stream in this reproduction: **Not acquired**.
- `targetMatch=true` user-socket event as a completion/update trigger: **Positive**.
- `targetMatch=true` as request-start/live-stream trigger: **Rejected by this reproduction**.
- Fake typewriter/synthetic progressive final: **Still prohibited**.

The user's current requirement is explicit: for a long cross-platform response, Native must show promptly that the request was received and then expose real progressive response state rather than remaining unchanged until completion.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole response/content owner.
- `AuthSessionStore` remains sole native auth/account owner; default persistent WebKit store remains sole persistent auth-secret owner.
- WebSocket content is not promoted into Native user/reasoning/final body authority without separate exact evidence.
- no duplicate Send, resend, fake stream, speculative retry/watchdog/fallback or second response store.

## Current protocol boundary

b82 proves that waiting for the current generic user-socket exact-conversation notification is too late for the desired UX. The already-authorized page-owned `stream_status` / plural-read path can follow an active response once the official page decides to query it, but this reproduction shows the already-open covered page did not autonomously issue that active-response path before the completion notification.

A new product implementation therefore needs an **earlier evidence-backed discovery source**. Do not simply increase observation frequency: there was no earlier observed event to sample.

The next investigation should distinguish two cases before allocating b83 product behavior:

1. **Visible official Web already open on A does begin cross-device live acquisition** — then inspect the concrete visibility/focus/network difference and reproduce only that evidenced browser behavior in the covered executor.
2. **Visible official Web also waits until completion while already open on A** — then the current page does not provide a passive early trigger; the project must separately evidence either a subscribable real-time turn signal or explicitly decide on a bounded selected-conversation status-monitoring design. Do not smuggle polling in as a guessed fix.

Current public/third-party observations about `ws.chatgpt.com`, `celsius/ws/user`, generic `conversations` subscriptions or per-turn topics are hypothesis-level only until reproduced on the user's exact current official page/account flow.

## Batch recovery point — b82 Runtime documentation sync

Known source/head before durable sync: formal branch head `5dc69b8ac8ac7d7f1acaf9e9a2d3b8703c042bb8`; exact tested product source remains `c7a274786dfd175e8f476fc15c4964840e112a1d` and must not be redefined by docs-only descendants.

Intended docs batch:

1. create exact b82 device Runtime evidence;
2. update `BUILD_TEST_INDEX.md` with b80-b82/current classification if practical;
3. update current external-continuation rule docs (`WEB_SEND_ADAPTER.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_STATE.md`/`MODULE_STATUS.md` where necessary) so they no longer imply b82 is Runtime pending;
4. update PR #29 Runtime gate text;
5. finish this checkpoint with the next exact human/protocol action.

Confirmed completed in this batch so far: this checkpoint recovery point only.

Do not change product code or allocate b83 until the next evidence source is selected under the rule above.

## Session round counter

Current work is round 21. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Record the supplied b82 Runtime export durably, then use Web Rule Lab / visible official Web on the same conversation to determine whether an already-open visible official page itself receives the remote user turn and active response before completion. That human observation is the next evidence gate; it decides whether to reproduce a browser visibility/focus behavior or move to a separately authorized real-time-status design. Do not allocate b83 before this distinction is made.