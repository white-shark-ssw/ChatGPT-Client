# DEV-send-stream

## Status

**Active — exact b45 Native realtime handoff evidence Candidate ready for primary-device Runtime**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open/mergeable; do not merge as accepted Send UX.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor remains b38.
- **Resume guard before b45**: branch `d2a8fb7aa07fcac1ca57b1ebde54dc34f2aac51d`; PR #29 open/mergeable; main unchanged; only this Active dev checkpoint; no peer conflict.
- **Exact b45 product/config source**: `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- **Candidate**: `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`; permanently reserved because an Artifact now exists.
- **Push Run / Job**: `33248952646` / `99091176390` — success.
- **PR Run / Job**: `33248954018` / `99091179731` — success.
- **Push Artifact**: `9713774868`; Artifact ZIP digest `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- **IPA**: `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`; SHA-256 `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.
- **Package inspection**: `0.1.0 (45)`, Candidate b45, source marker `accd7bdf29e4`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, arm64.
- **Evidence classification**: Code / CI / Artifact / package identity passed. Runtime handoff capability **Unknown / Unverified**. Stable/Frozen Send: No.

## Security / transport boundary retained

Exact b42 proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native account Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured challenge/proof replay, guessed alternate Send endpoints, hidden challenge-harvesting WebViews, DOM answer/reasoning scraping, Native composer injection into a covered/hidden Web composer, synthetic hidden Send clicks, or private file-input injection.

The user's proposed visual idea of fully hiding Web and hooking its Send button is **not** an accepted implementation path. It would turn the protected browser Send path into hidden/shadow transport. b45 instead tests whether Web can be reduced to a user-visible legal Send initiator while Native legitimately attaches to the same already-started response.

## Accepted b40-b44 evidence retained

- b40: existing/new official Web Send uses `POST /backend-api/f/conversation`, HTTP200 SSE; normal `v1` + structural patch events + `[DONE]`; early `resume_conversation_token` observed; new-chat authoritative identity appears early.
- b41: server Stop `POST /backend-api/stop_conversation`; prepare/Sentinel precursor structure evidenced.
- b42: browser-owned PoW/Turnstile/`so` challenge output required before successful Send.
- b43: visible Web feasibility/smoothness largely accepted; Web `+` ~100–200ms; Web Photos filtered videos on iOS17.
- b44: `/c/<id>` A/B mapping worked, but immediate Native reconciliation could lag Web assistant output; full-page Native->Web->Native UX rejected.

## Current target architecture

The user explicitly rejects the separate API product route and selected this target **if current protocol evidence supports it**:

`Native composer/history/presentation -> user-visible official Web performs legal Send -> Native attaches/resumes/subscribes to that same in-progress response without resending prompt -> Native owns reasoning/final streaming presentation -> Native response lifecycle later owns background continuation.`

This is intentionally different from the b43/b44 hybrid forms. Web should not remain the realtime-response UI owner merely because it can Send.

## b45 implementation scope

b45 adds an observation-only `ProtocolHandoffProbeViewController` and Settings entry `实时接管协议探测（诊断）`.

It structurally observes:

1. original `/backend-api/f/conversation` Send SSE;
2. first presence/shape of `resume_conversation_token`, response/turn/conversation/message/async-task identity fields;
3. official-page follow-up same-origin fetch/XHR/EventSource/WebSocket connections after Send;
4. route classes for stream-status / turn-stream / handoff / resume / subscribe / continuation candidates;
5. response status/content type, header **names only**, query **names only**, structural JSON shape and identity-value shape only;
6. whether a later official-page connection naturally receives continuation-like events without another Send.

b45 does **not** replay a resume token, guess a continuation endpoint, create a second Send, inject prompts, click hidden Web controls, scrape answer/reasoning text or capture protected values.

Never record/export prompt/answer/reasoning text, raw conversation/message/response/resume IDs, Cookie/Authorization values, Sentinel/Turnstile/PoW/conduit values, or raw payloads.

## Background ordering

TD-026 background resilience remains a hard product requirement, but implementation is now deferred behind realtime-handoff feasibility.

- If Native handoff is proven, background work should preserve the Native-owned response lifecycle rather than WebKit.
- Only if Native handoff is disproven does WebKit true-background remain relevant to the fallback visible-Web architecture.
- Do not spend a new Candidate on Web background/UI polish before interpreting b45 Runtime evidence.

## Exact b45 Runtime procedure

Primary authority: iPhone 15 Pro Max / iOS17.0 TrollStore runtime.

1. Install exact b45 IPA above.
2. In Settings, preferably `清理诊断日志` first.
3. Open `实时接管协议探测（诊断）`.
4. Use default ChatGPT / primary assistant, not a custom GPT/Gizmo.
5. Start a **new chat** and send one prompt long enough to produce noticeable reasoning/streaming; let it run normally without manual refresh.
6. If practical, open an **existing chat** in the same probe and send one more prompt; again let it run normally.
7. Return to Settings and export the diagnostics JSON.
8. Upload that JSON for evidence analysis.

The probe is accepted only as a diagnostic instrument when it captures the intended structural traffic safely. Native realtime handoff itself is accepted only if evidence shows an actual continuation mechanism suitable for a no-resend Native connection.

## Docs-only handoff batch

After exact b45 product source, update durable docs with:

- b45 exact Candidate/CI/Artifact/package identity;
- Web-Send-only + Native-realtime-handoff target architecture;
- background/UI work ordered after handoff feasibility;
- hidden/shadow Web button-hook route remains rejected;
- PR #29 remains Runtime-gated and unmerged.

No Swift/Xcode/workflow/product mutation is permitted after `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` under b45 identity. Any corrected product code after this Artifact requires b46+.

## Next exact action

**Human-only Runtime gate:** install exact b45, run the new-chat + existing-chat realtime handoff capture, export diagnostics JSON, and analyze whether official Web demonstrates a real same-response continuation path.

- If yes: allocate b46 only after a fresh guard and implement the smallest **Native no-resend continuation parity** experiment against the exact observed route/structure.
- If no: do not guess a resume endpoint. Record the negative evidence and reassess the architecture ceiling.
- Do not proceed to hidden Web automation, polished hybrid UI, or TrollStore background implementation before this evidence is interpreted.
