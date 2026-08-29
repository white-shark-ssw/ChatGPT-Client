# DEV-send-stream

## Status

**Active — b45 first Runtime captured; uninterrupted Web traffic did not expose a separate continuation stream; exact-b45 active-stream interruption capture is the human gate**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open/mergeable; title `DEV-send-stream: b45 realtime handoff reconnect evidence gate`; do not merge as accepted Send UX.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor remains b38.
- **Exact b45 product/config source**: `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- **Candidate**: `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`; permanently reserved.
- **Push Run / Job**: `33248952646` / `99091176390` — success.
- **PR Run / Job**: `33248954018` / `99091179731` — success.
- **Push Artifact**: `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- **IPA**: `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`; SHA-256 `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.
- **Package inspection**: `0.1.0 (45)`, Candidate b45, source `accd7bdf29e4`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, arm64.
- **Evidence classification**: Code / CI / Artifact / package identity passed. First Runtime structural capture accepted. Native same-response handoff remains **Unknown / Unverified**. Stable/Frozen Send: No.

## Security / transport boundary retained

Exact b42 proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native account Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured challenge/proof replay, guessed alternate Send endpoints, hidden challenge-harvesting WebViews, DOM answer/reasoning scraping, Native composer injection into a covered/hidden Web composer, synthetic hidden Send clicks, or private file-input injection.

The user's proposed fully hidden Web + hooked Send button remains rejected because it would turn the protected browser Send path into hidden/shadow transport. The permitted target remains user-visible official Web legal Send initiation followed by Native same-response continuation only if current evidence proves a legitimate no-resend continuation path.

## b45 first Runtime capture — exact observations

Uploaded diagnostic metadata matches exact b45: `0.1.0 (45)`, Candidate `DEV-send-stream-0.1.0-b45`, source marker `accd7bdf29e4`, Release, iPhone, iOS17.0.

### Sequence A — page classified `existing_conversation`

- Send at `11:17:15Z`: `POST /backend-api/f/conversation`, `fetch`.
- Response at `11:17:16Z`: HTTP200 `text/event-stream`.
- Original SSE event 1: `v1`; event 2: `resume_conversation_token` with conversation identity structurally present and token value redacted.
- Later original-stream identity includes `conversation_id`, then `conversation_id + request_id`, and later a message identity marker.
- Official page opened `GET /backend-api/conversation/{id}/stream_status` at `11:17:16Z`; HTTP200 `application/json`; observed payload shape only `{status: string}`.
- No separate EventSource/WebSocket/turn-stream/handoff/resume/subscribe response stream was observed while the answer remained active.
- Original Send SSE stayed the answer transport through `message_stream_complete` and `[DONE]` around `11:17:47Z` (~32s after Send).

### Sequence B — page classified `new_or_other`

- Send at `11:19:39Z`: again `POST /backend-api/f/conversation`, HTTP200 SSE.
- Original SSE again emitted `resume_conversation_token` at event 2 and later conversation/request/message identity structure.
- Request structure contained both top-level `conversation_id` and `conversation_mode.gizmo_id`; therefore this sequence is **not accepted as a clean default-primary new-chat sample**.
- No follow-up continuation transport was observed during its active ~32s stream; original Send SSE reached `message_stream_complete` and `[DONE]` around `11:20:11Z`.

### Interpretation boundary

- `resume_conversation_token` is real and arrives very early, but this capture does **not** show official Web using it to open a second stream.
- `stream_status` is status JSON in this capture, not a response-event continuation channel.
- No response/turn ID was observed by the probe; `request_id`, conversation ID and message ID structure were observed on the original stream.
- All recorded background/foreground intervals occurred before a Send or after the active Send SSE had already completed. The official page never needed to demonstrate active-response reconnect behavior.
- Absence of a secondary stream during an uninterrupted response does **not** prove no reconnect mechanism exists. It proves only that the normal page continues consuming the original Send SSE when that transport remains intact.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## Exact next Runtime procedure — reuse b45

1. Keep exact b45 installed; clear diagnostics first.
2. Open `实时接管协议探测（诊断）` and use **default ChatGPT / primary assistant only**; avoid custom GPT/Gizmo.
3. Start a prompt that will keep the answer streaming comfortably longer than 30 seconds.
4. As soon as visible output is actively streaming, background or lock the device for roughly 20–30 seconds, then return **before the answer would normally have finished**.
5. Do not manually refresh, resend, Stop, or switch GPT during this capture.
6. Let official Web recover/continue/finish naturally, then export diagnostics JSON.
7. If the response completes before the intended interruption, repeat with a longer prompt rather than interpreting it as reconnect evidence.

Evidence question: after foreground return, does official Web keep consuming the same original stream, or open a new status/resume/handoff/turn-stream/subscription connection that continues the same response without a second Send?

## Completed b45 first-Runtime documentation chain

- `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md` records the exact capture and evidence boundary.
- `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md`, `PROJECT_SPECIFIC_RULES.md`, `TECHNICAL_DECISIONS.md` (TD-027), and the complete `BUILD_TEST_INDEX.md` are aligned to this Runtime result.
- An intermediate docs-only Build Index narrowing was detected immediately and repaired from the pre-write full blob; final `BUILD_TEST_INDEX.md` retains the complete historical Candidate table and the updated b45 row.
- PR #29 metadata is updated to the b45 reconnect evidence gate and remains open/mergeable/not merged.

## Final product-source drift audit

Audit performed from exact b45 product/config source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` to docs head `0503faf7592919bd2e067444a26c7f5787072465` before this final checkpoint commit:

- compare status: ahead only, no divergence;
- changed paths were **only under `docs/project/**`**;
- no Swift, Xcode project, workflow, build script, asset or product/config file changed after the exact b45 source;
- therefore exact b45 Runtime product authority remains `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` and Artifact `9713774868`; later docs-only commits do not redefine it.

## Next exact action

**Human-only Runtime gate:** reuse the exact installed b45 IPA and perform one default-primary response with a deliberate 20–30 second background/lock interval while the original response is visibly still streaming. Return before expected completion, do not refresh/resend/Stop/switch GPT, let official Web recover/finish, then export and upload the diagnostics JSON.

After that evidence:

- official reconnect/continuation traffic observed -> re-run full guard and consider b46 for the smallest Native no-resend parity experiment;
- same original stream simply survives -> record WebKit survival evidence, Native handoff remains Unverified;
- response is lost and no official continuation appears -> record negative evidence and reassess the existing-account architecture ceiling.

Do not allocate b46, rebuild b45 or merge PR #29 before that evidence is interpreted.
