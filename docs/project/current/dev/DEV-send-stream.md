# DEV-send-stream

## Status

**Active — b45 probe validated; uninterrupted Web traffic did not expose a separate response continuation stream; targeted mid-stream interruption capture required**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open/mergeable; do not merge as accepted Send UX.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor remains b38.
- **Resume guard before interpreting uploaded b45 diagnostics**: branch head `1a61298fa829b45ead2bfc0e28a2cddf869e7db3`; PR #29 open/mergeable with matching head; main unchanged; only this Active dev checkpoint; no peer conflict.
- **Exact b45 product/config source**: `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- **Candidate**: `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`; permanently reserved.
- **Push Run / Job**: `33248952646` / `99091176390` — success.
- **PR Run / Job**: `33248954018` / `99091179731` — success.
- **Push Artifact**: `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- **IPA**: `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`; SHA-256 `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.
- **Package inspection**: `0.1.0 (45)`, Candidate b45, source `accd7bdf29e4`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, arm64.
- **Evidence classification**: Code / CI / Artifact / package identity passed. First Runtime capture analyzed. Native same-response handoff remains **Unknown / Unverified**. Stable/Frozen Send: No.

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

## Current architecture interpretation

Desired target remains conditional:

`Native composer/history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes/subscribes to the same already-started response without resending prompt -> Native owns user-visible reasoning/final streaming and background lifecycle.`

b45 first Runtime is **not sufficient to implement Native parity**. Do not guess a resume route from the token name or reinterpret `stream_status` as a stream endpoint.

The next highest-value evidence is to reuse exact b45 and deliberately interrupt the original response while it is still active, then observe official-page behavior on return. No b46 is needed merely to collect this traffic because b45 already instruments fetch/XHR/EventSource/WebSocket and continuation-like routes.

## Exact next Runtime procedure — reuse b45

1. Keep exact b45 installed; clear diagnostics first.
2. Open `实时接管协议探测（诊断）` and use **default ChatGPT / primary assistant only**; avoid custom GPT/Gizmo.
3. Start a prompt that will keep the answer streaming comfortably longer than 30 seconds.
4. As soon as visible output is actively streaming, background or lock the device for roughly 20–30 seconds, then return **before the answer would normally have finished**.
5. Do not manually refresh, resend, Stop, or switch GPT during this capture.
6. Let official Web recover/continue/finish naturally, then export diagnostics JSON.
7. If the response completes before the intended interruption, repeat with a longer prompt rather than interpreting it as reconnect evidence.

Evidence question: after foreground return, does official Web keep consuming the same original stream, or open a new status/resume/handoff/turn-stream/subscription connection that continues the same response without a second Send?

## Batch recovery point — b45 Runtime documentation chain

Known baseline before docs-only Runtime writes: branch `dev/send-stream-20260829@1a61298fa829b45ead2bfc0e28a2cddf869e7db3`; PR #29 open/mergeable at the same head; `main@34811877896ca88c6656be6676f5466a19931ce6`; exact b45 product source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` must not be mutated.

Confirmed complete in this chain:

- b45 diagnostic JSON parsed and first Runtime conclusion established.
- runtime evidence file created.
- `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md`, `PROJECT_SPECIFIC_RULES.md`, and `TECHNICAL_DECISIONS.md` updated to current b45 Runtime truth.
- `BUILD_TEST_INDEX.md` reviewed: its b45 row already states `Runtime handoff Unverified`, which remains the exact capability classification after this first insufficient/negative-normal-path capture; no identity/status rewrite is required until handoff evidence changes.

Still pending:

1. update PR #29 title/body from stale pre-b45 wording to the b45 active-stream reconnect evidence gate;
2. verify final branch diff from exact b45 product source contains no post-b45 product/config mutation;
3. refresh this checkpoint with final docs-only head and exact next action.

Recovery must **not** modify Swift/Xcode/workflow product/config files or allocate b46. If interrupted, re-read this checkpoint and actual branch/PR state, then perform only missing docs/PR writes.

## Next exact action

Update PR #29 metadata, verify the final docs-only delta from `accd7bdf...`, then hand the user the targeted exact-b45 mid-stream background/lock capture procedure. Do not allocate b46 until official-page reconnect evidence justifies a concrete Native parity experiment.
