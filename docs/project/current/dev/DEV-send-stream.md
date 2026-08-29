# DEV-send-stream

## Status

**Active — exact b45 active-response background survival captured; no official reconnect transport observed; forced transport-interruption evidence is the next human gate**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open/mergeable; do not merge as accepted Send UX.
- **Stable native predecessor**: b38.
- **Original branch base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; main advanced by 3 commits only in root `AGENTS.md`. No Swift/Xcode/workflow/product/state-owner overlap was found. Branch is not yet synchronized to that rules-only base advance.
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

## b45 Runtime evidence

### Capture A/B — uninterrupted response

- `POST /backend-api/f/conversation` -> HTTP200 `text/event-stream`.
- Original SSE emitted `resume_conversation_token` at event 2, then conversation/request/message identity structure.
- Official page opened `GET /backend-api/conversation/{id}/stream_status`; response was HTTP200 JSON `{status:string}` only.
- No separate EventSource/WebSocket/turn-stream/handoff/resume/subscribe response stream appeared while uninterrupted answers were active.
- Original Send SSE stayed the answer transport through `message_stream_complete` and `[DONE]`.
- One previous sample contained `conversation_mode.gizmo_id`; it remains excluded as a clean default-primary sample.

### Capture C — clean default-primary new-chat active background / lock

User explicitly reports this was a new conversation. The observed Send body had no top-level `conversation_id` and no `conversation_mode.gizmo_id`.

- Send began `2026-08-29T12:45:20Z` through `POST /backend-api/f/conversation`, HTTP200 SSE.
- Original SSE again emitted `resume_conversation_token` at event 2.
- Active-response background intervals were approximately **35s**, **34s**, and **126s**; ~195s / 3m15s cumulative.
- Send-to-terminal elapsed time was ~227s / 3m47s.
- At final foreground return (`12:49:07Z`), the **same original `conversation_send` / `fetch` stream** delivered `server_ste_metadata -> message_stream_complete -> conversation_detail_metadata -> [DONE]`.
- No second Send, no new SSE, no resume/handoff/turn-stream/subscription connection, and no manual refresh/resend were observed.

### Interpretation

Exact b45 now gives positive evidence that the tested WebKit/original-fetch response path can survive or buffer across repeated ordinary background/lock intervals, including one ~126s interval.

It does not prove continuous event delivery while suspended, 5/15-minute behavior, real network-loss recovery, WebContent termination recovery, or Native same-response handoff.

Because the original transport survived, official Web again had no reason to reveal a reconnect API. `resume_conversation_token` remains an observed field, not an authorized Native continuation contract.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## Next evidence strategy

Natural short background is now a poor mechanism for discovering an official reconnect path on this device.

Reuse exact b45 and **force a real transport break without resending**:

1. Use an existing long conversation / default primary assistant.
2. Start a response expected to remain active long enough to observe recovery.
3. While visibly streaming, remove connectivity for about 10–15 seconds, then restore it; preferred controlled test is Airplane Mode / both Wi-Fi and cellular unavailable, with Wi-Fi -> cellular as a secondary variant after a stable Wi-Fi baseline.
4. Do not refresh, resend, Stop, switch GPT or navigate away.
5. Let official Web recover or fail naturally, then export diagnostics.

Evidence question: after a genuine transport break, does official Web open a new official status/resume/handoff/turn-stream/subscription connection that continues the same response without a second Send?

If a real reconnect route appears, only that exact observed structure may justify a later b46 Native no-resend parity experiment. If no reconnect appears, record negative architecture evidence; do not guess from `resume_conversation_token`.

## Completed Runtime docs batch

Updated with Capture C:

- `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`;
- `PROJECT_STATE.md`;
- `MODULE_STATUS.md`;
- `PROJECT_PROFILE.md`;
- `DEVELOPMENT_PLAN.md`;
- `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`;
- `TECHNICAL_DECISIONS.md` / TD-026 / TD-027;
- complete `BUILD_TEST_INDEX.md`.

**Batch recovery state:** docs writes above are confirmed. PR #29 metadata update and final exact-source drift audit remain pending. Do not replay completed docs writes during recovery.

Do **not** touch Swift/Xcode/workflow/build scripts, exact b45 product source, Candidate/Artifact identity, or merge PR #29.

## Next exact action

Update PR #29 to the forced-transport-interruption gate, then audit exact b45 product source `accd7bdf...` -> final branch head for docs-only drift.

After that, the human-only gate is one forced connectivity interruption on exact b45 in an existing long default-primary conversation, without refresh/resend/Stop/navigation. Export diagnostics after the official page naturally recovers or fails.

Do not allocate b46, rebuild b45, or merge PR #29 until that evidence is interpreted.