# DEV-send-stream b81 device Runtime — 2026-09-01

## Candidate under test

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b81`
- Version / Build: `0.1.0 (81)`
- Exact product/config source: `d1d4d197cc5d2a5022a28b332afebe485b216ea1`
- Canonical Artifact: `9809150111`
- IPA SHA-256: `d48d2398dc5a7ef16b9983021a9173d87ba3b852f4a45c9431dff2ebcf057038`
- Supplied diagnostics metadata confirms Release `0.1.0`, Build `81`, Candidate `DEV-send-stream-0.1.0-b81`, source marker `d1d4d197cc5d`, iPhone / iOS 17.0.

## User Runtime result

The user kept the target conversation selected and did **not** press Sync while a new turn was started from another platform. Native did not automatically acquire the remote reasoning/response. The user pressed Sync only after the failure was established.

Runtime classification: **b81 automatic external acquisition rejected, but the structural probe produced a positive acquisition trigger signal.**

## Exact event sequence

### Covered page / socket was ready before the remote turn

- 16:19:14Z: selected conversation begins observation in `mode=selection`.
- 16:19:15Z: authoritative Detail load returns HTTP200 with 4 visible messages; covered page finishes loading.
- 16:19:18Z: `wss://ws.chatgpt.com/p24/ws/user/{id}` is structurally observed as `created`.
- 16:19:19Z: socket is `open`; an initial JSON-array frame of 371 chars has `targetMatch=false`.

This proves b81 did observe the socket from creation time rather than attaching a late Lab hook.

### Two exact target-conversation socket frames arrive while Native remains unaware of the remote response

- 16:22:20Z: socket `message`, JSON array, length 180, `targetMatch=true`.
- 16:24:24Z: a second socket `message`, JSON array, length 180, `targetMatch=true`.

`targetMatch=true` in b81 means the parsed JSON frame contains an exact string value equal to the current covered-page conversation ID within the bounded structural traversal. Raw frame data and the ID itself are not exported.

Crucially, before the user's manual Sync there are **no** corresponding:

- `coveredExecutor.externalStreamingObserved`;
- `coveredExecutor.externalSnapshot`;
- Repository `liveResponse.started` for an external response;
- page-owned target `stream_status` adoption evidence.

Therefore the official user-level WebSocket delivered target-conversation-correlated activity while the current covered page failed to enter the existing page-owned `stream_status/plural-read` acquisition path.

### Manual Sync later proves the conversation really changed

- 16:24:59Z: user requests `conversation.latestSync`.
- 16:25:00Z: authoritative Detail returns HTTP200 with 307124 bytes, mapping 73, visible messages **4 -> 8**, latest user characters 107, and `addedVisibleMessageCount=4`.
- 16:25:00Z: existing b80/b81 manual path re-arms the covered page as `mode=manual_sync_rearm`.

This confirms the pre-Sync target-matching WebSocket frames were not harmless page-idle noise: by the time manual Sync was requested, the selected conversation had materially advanced by four visible messages.

## Evidence-backed architectural conclusion

The missing cross-platform acquisition problem no longer requires polling as the first choice.

b81 provides a privacy-safe, event-driven trigger candidate:

`user-level WebSocket frame with exact current-conversation match`
→ one bounded authoritative Sync for the currently selected conversation
→ one bounded covered-page re-arm
→ existing page-owned `stream_status / plural-read` response adoption remains the content authority.

The socket frame itself remains **non-authoritative** for user/reasoning/tool/final content and must not directly mutate `ConversationRepository` response content.

## Next-candidate boundary

The next product candidate may use only the **first** target-matching WebSocket message in an observation cycle as an acquisition hint when:

- the executor is observing an existing selected conversation;
- no Repository live response for that conversation has been acquired yet;
- the signal matches the exact current conversation structurally.

That hint may trigger exactly one bounded authoritative `syncLatestMessages` plus exactly one covered-page re-arm after the Sync result. It must not create a timer, polling cadence, retry loop, repeated Sync loop, WebSocket body authority, duplicate Send, second response owner, or fake progressive stream.

The hint must be one-shot for that observation cycle so the second target-matching frame in this run cannot trigger a duplicate automatic Sync. A later explicit new observation cycle / newly created executor may arm a fresh one-shot hint for the next response.

## Frozen / retained boundaries

- b80 tool/reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b79/b80 explicit manual-Sync re-arm: preserve as recovery.
- b67 client-owned protected Send and b72 simultaneous A/B ownership: preserve.
- progressive external final-body token streaming remains unresolved; do not fake it.
- account-wide notification/haptic discovery remains deferred.

## Evidence classification

- b81 Code/static/Simulator/Push+PR CI/Artifact/package: **Verified**.
- b81 Runtime automatic external acquisition: **Rejected**.
- b81 WebSocket structural probe: **Positive** — target-correlated event exists before manual Sync and without page-owned acquisition.
- WebSocket content authority: **Rejected / not authorized**.
- Event-driven one-shot acquisition trigger: **Evidence-backed for next candidate**.
- Stable/Frozen Send as a whole: **No**.
