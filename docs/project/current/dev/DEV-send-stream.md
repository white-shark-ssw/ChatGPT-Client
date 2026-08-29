# DEV-send-stream

## Status

**Active — exact b45 ordinary active-response background/lock survival is positive; Native continuation remains Unverified; forced transport-interruption Runtime is the next human gate.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; title `DEV-send-stream: b45 short-background survives; forced reconnect evidence gate`.
- **Stable native predecessor**: b38.
- **Original feature base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; main advanced only in root `AGENTS.md`; no product/state-owner overlap. Final synchronization remains required before any merge.
- **Exact b45 product/config source**: `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- **Candidate**: `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`; permanently reserved.
- **Push Run / Job**: `33248952646` / `99091176390` — success.
- **PR Run / Job**: `33248954018` / `99091179731` — success.
- **Artifact**: `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- **IPA**: `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`; SHA-256 `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.
- **Package inspection**: Release, source `accd7bdf29e4`, iOS14 minimum, UIDeviceFamily `[1,2]`, arm64.
- **Evidence**: Code / CI / Artifact / package identity passed. Two exact-device Runtime captures accepted. Native same-response handoff: **Unknown / Unverified**. Stable/Frozen Send: No.

## Security / product boundary

Exact b42 proved tested successful ChatGPT-account Send requires browser anti-abuse challenge output. Pure-native account Send remains blocked.

Permitted target only if evidence supports it:

`Native history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes/subscribes to the same already-started response without a second Send -> Native owns visible realtime response/background lifecycle.`

Still prohibited: challenge solver/bypass/replay, hidden/shadow protected Web transport, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping, guessed continuation endpoints and private file-input injection.

## b45 Runtime 1 — uninterrupted path

- `POST /backend-api/f/conversation` -> HTTP200 `text/event-stream`.
- `resume_conversation_token` appears at original SSE event 2.
- Later original-stream structure exposes conversation/request/message identity.
- `GET /backend-api/conversation/{id}/stream_status` returned HTTP200 JSON `{status:string}` only.
- Original Send `fetch` stayed response transport through `message_stream_complete` / `[DONE]`.
- No secondary EventSource/WebSocket/turn-stream/handoff/resume/subscribe response stream appeared.

Conclusion: token existence/name alone is not a Native continuation contract.

## b45 Runtime 2 — clean primary new-chat repeated background / lock

User explicitly identified the capture as a new conversation. The observed Send body had no top-level `conversation_id` and no `conversation_mode.gizmo_id`, so this is accepted as a clean default-primary new-chat sample.

Send began `2026-08-29T12:45:20Z`.

While the original Send SSE remained active, the app was backgrounded/locked for approximately:

- 35 seconds;
- 34 seconds;
- 126 seconds.

Cumulative active-response background time: ~195 seconds / 3m15s.
Send-to-terminal: ~227 seconds / 3m47s.

On final foreground return at `12:49:07Z`, the **same original `conversation_send` / `fetch` stream** immediately delivered:

`server_ste_metadata -> message_stream_complete -> conversation_detail_metadata -> [DONE]`.

No second Send, new SSE, resume/handoff/turn-stream/subscription connection, manual refresh or prompt resend was observed.

### Accepted conclusion

On exact b45 / primary iPhone / iOS17.0, the tested official-Web/WebKit response path can **survive or buffer across repeated ordinary background/lock intervals**, including one ~126-second interval, and still complete normally.

Do not overclaim:

- continuous event delivery while suspended is Unverified;
- 5/15-minute survival is Unverified;
- WebContent termination recovery is Unverified;
- network-loss recovery is Unverified;
- battery/thermal is Unverified;
- Native same-response handoff is Unverified.

Because the original transport survived, official Web again had no need to expose an interruption-only reconnect API.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## Current evidence strategy

Natural short background is now a poor way to discover reconnect behavior on this device. Reuse exact b45 and force one genuine connectivity interruption while a response is active.

### Next exact Runtime procedure

1. Clear diagnostics.
2. Use **default ChatGPT / primary assistant** in an **existing long conversation**.
3. Start a response long enough to remain actively streaming.
4. While visibly streaming, remove connectivity for about **10–15 seconds**, then restore it. Preferred deterministic variant: Airplane Mode / both Wi-Fi and cellular unavailable; a Wi-Fi -> cellular transition is a useful secondary variant after a stable Wi-Fi baseline.
5. Do not refresh, resend, Stop, switch GPT or navigate away.
6. Let official Web recover or fail naturally.
7. Export diagnostics JSON.

Evidence question: after a genuine transport break, does official Web create an official status/resume/handoff/turn-stream/subscription connection that continues the same already-started response without a second Send?

- If yes: fresh guard, then b46 may test only the smallest Native no-resend parity against that exact observed structure.
- If no: record negative Runtime and reassess the architecture ceiling; do not guess from `resume_conversation_token`.
- If the original connection somehow remains viable: refine the interruption experiment from evidence rather than inventing Native behavior.

## Documentation / PR state

Updated for Runtime 2:

- `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`
- `PROJECT_STATE.md`
- `MODULE_STATUS.md`
- `PROJECT_PROFILE.md`
- `DEVELOPMENT_PLAN.md`
- `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`
- `TECHNICAL_DECISIONS.md` / TD-026 / TD-027
- `BUILD_TEST_INDEX.md`
- PR #29 title/body

## Product-source drift audit

Audit from exact b45 product source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` to pre-final-checkpoint branch head `962b7a8873efb71fcdf3b6b716319b39831ba615`:

- status: ahead only, no divergence;
- all changed files are under `docs/project/**`;
- no Swift, Xcode project, workflow, build script, asset or product/config file changed after exact b45 source.

Therefore exact b45 product/Artifact authority remains unchanged. This checkpoint commit is docs-only and does not redefine the Candidate.

## Next exact action

**Human-only Runtime gate:** reuse exact b45 and perform the forced 10–15-second connectivity-loss test above in an existing long default-primary conversation. Upload the resulting diagnostics JSON.

Do not allocate b46, rebuild b45 or merge PR #29 before that evidence is interpreted.