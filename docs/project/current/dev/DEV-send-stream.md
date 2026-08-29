# DEV-send-stream

## Status

**Active — exact b45 active-response background survival captured; no official reconnect transport observed; forced transport-interruption evidence is the next human gate**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open/mergeable; do not merge as accepted Send UX.
- **Stable native predecessor**: b38.
- **Original branch base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; main advanced by 3 commits only in root `AGENTS.md`. No Swift/Xcode/workflow/product/state-owner overlap was found. Branch is not yet synchronized to that docs/rules-only base advance.
- **Exact b45 product/config source**: `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- **Candidate**: `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`; permanently reserved.
- **Push Run / Job**: `33248952646` / `99091176390` — success.
- **PR Run / Job**: `33248954018` / `99091179731` — success.
- **Push Artifact**: `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- **IPA**: `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`; SHA-256 `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.
- **Package inspection**: `0.1.0 (45)`, Candidate b45, source `accd7bdf29e4`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, arm64.
- **Evidence classification**: Code / CI / Artifact / package identity passed. Two exact-device Runtime captures accepted as protocol/background evidence. Native same-response handoff remains **Unknown / Unverified**. Stable/Frozen Send: No.

## Security / transport boundary retained

Exact b42 proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native account Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured challenge/proof replay, guessed alternate Send endpoints, hidden challenge-harvesting WebViews, DOM answer/reasoning scraping, Native composer injection into a covered/hidden Web composer, synthetic hidden Send clicks, or private file-input injection.

The user's proposed fully hidden Web + hooked Send button remains rejected because it would turn the protected browser Send path into hidden/shadow transport. The permitted target remains user-visible official Web legal Send initiation followed by Native same-response continuation only if current evidence proves a legitimate no-resend continuation path.

## b45 first Runtime capture — uninterrupted response

Uploaded diagnostic metadata matched exact b45: `0.1.0 (45)`, Candidate `DEV-send-stream-0.1.0-b45`, source marker `accd7bdf29e4`, Release, iPhone, iOS17.0.

- `POST /backend-api/f/conversation` -> HTTP200 `text/event-stream`.
- Original SSE emitted `resume_conversation_token` at event 2, then conversation/request/message identity structure.
- Official page opened `GET /backend-api/conversation/{id}/stream_status`; response was HTTP200 JSON with structural `{status:string}` only.
- No separate EventSource/WebSocket/turn-stream/handoff/resume/subscribe response stream appeared while the uninterrupted answer was active.
- Original Send SSE stayed the answer transport through `message_stream_complete` and `[DONE]`.
- One previous sample contained `conversation_mode.gizmo_id`; it remains excluded as a clean default-primary sample.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## b45 second Runtime capture — active-response background / lock survival

User explicitly reports this was a new conversation and performed several suspend/lock cycles because a new conversation was less likely to disconnect.

Uploaded export again matches exact b45 / Release / iPhone / iOS17.0 / source `accd7bdf29e4`.

### Request / identity structure

- Probe page initially loaded as `new_or_other`.
- Send began `2026-08-29T12:45:20Z` through `POST /backend-api/f/conversation`, HTTP200 `text/event-stream`.
- The Send request body did **not** contain top-level `conversation_id` and did **not** contain `conversation_mode.gizmo_id`; together with the user's explicit Runtime statement, treat this as the clean default-primary new-chat sample despite the probe's later `pageKind=existing_conversation` classification at request time.
- Original stream event 2 again carried `resume_conversation_token`; later events exposed conversation identity, request identity and message identity structure.
- `stream_status` again returned only HTTP200 JSON `{status:string}` and was not a response-event stream.

### Active-response lifecycle

- Before Send there was one unrelated ~64s background interval.
- While the original Send SSE was active, the app entered background for approximately **35s**, **34s**, then **126s**.
- Total active-response background time observed: approximately **195s / 3m15s**.
- Send-to-terminal elapsed time: approximately **227s / 3m47s**.
- Immediately when the final ~126s background interval ended at `12:49:07Z`, the **same original `conversation_send` / `fetch` stream** delivered event 464 `server_ste_metadata`, event 465 `message_stream_complete`, event 466 `conversation_detail_metadata`, then event 467 `[DONE]`.
- No second `conversation_send`, no second stream response, and no post-background resume/handoff/turn-stream/subscribe/EventSource/WebSocket connection was observed.

### Interpretation

This is positive exact-device evidence that the tested WebKit/original-fetch response path can survive or buffer across multiple ordinary background/lock intervals, including one ~126s interval, and still complete without manual refresh or prompt resend.

It does **not** prove that WebKit processed/delivered every stream event continuously while suspended; the probe cannot distinguish live background delivery from WebKit/network/server continuation plus buffered delivery on foreground.

It also does **not** prove Native same-response handoff. In fact, because the original transport survived, official Web again had no need to reveal any separate reconnect API. `resume_conversation_token` remains an observed field, not an authorized Native continuation contract.

This capture therefore advances TD-026 short-background evidence but does not close its 5/15-minute or forced-interruption matrix and does not justify guessing a b46 Native resume endpoint.

## Architecture consequence / next evidence strategy

Natural short background is now a poor mechanism for discovering an official reconnect path on this device because the original WebKit fetch survived all three active-response intervals.

The next highest-value Runtime experiment reuses exact b45 and **forces a real transport break without resending**:

1. Use an existing long conversation / default primary assistant.
2. Start a response expected to run long enough to observe recovery.
3. While the response is visibly streaming, briefly break connectivity (preferred controlled test: disable Wi-Fi and cellular / Airplane Mode for about 10–15s, then restore; alternatively Wi-Fi -> cellular transition after a stable Wi-Fi baseline).
4. Do not refresh, resend, Stop, switch GPT or navigate away.
5. Let official Web recover or fail naturally, then export diagnostics.

Evidence question: after a genuine transport break, does official Web open a new official status/resume/handoff/turn-stream/subscription connection that continues the same response without a second Send, or does it only surface a failure / later history refresh path?

If a real reconnect route appears, only that exact observed structure may justify a later b46 Native no-resend parity experiment. If no reconnect appears, record the negative architecture evidence; do not guess from `resume_conversation_token`.

## Batch recovery point — Runtime docs chain

Known head before this docs batch: `77f2fc6eef92ca61e5c08ff31a4d9251905ee9bf`.

This checkpoint update is the first confirmed write of the batch. Remaining deterministic docs-only writes:

- append this second exact b45 Runtime capture to `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`;
- update `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md`, `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`, `TECHNICAL_DECISIONS.md`/TD-027, `BUILD_TEST_INDEX.md`, and PR #29 body/title where needed;
- final compare from exact b45 product source `accd7bdf...` to branch head must still show docs-only changes.

Do **not** touch Swift/Xcode/workflow/build scripts, exact b45 product source, Candidate/Artifact identity, or merge PR #29 during recovery.

## Next exact action

Complete the docs-only Runtime evidence batch above. Then the human-only gate is one **forced transport interruption** on exact b45 in an existing long default-primary conversation, without refresh/resend/Stop. Export diagnostics after the official page naturally recovers or fails.

Do not allocate b46, rebuild b45, or merge PR #29 until that evidence is interpreted.