# Project State

_Last updated: 2026-08-29 through exact b45 first handoff Runtime capture; targeted active-stream interruption evidence remains pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the current Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen; current native conversation modules remain Frozen No.

## Current Phase 9 — DEV-send-stream

### Security boundary retained

Exact b42 proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output: PoW, Turnstile and `so` required; non-empty PoW + Turnstile were finalized before Send.

Therefore pure-native/transient-auth ChatGPT-account Send remains blocked. Prohibited routes remain solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoint, hidden/shadow challenge WebView, challenge harvesting, DOM answer/reasoning scraping, covered-Web Native composer injection, synthetic hidden Send clicks and hidden file-input injection.

### Visible-Web product evidence retained

- b43 accepted visible-Web feasibility/smoothness for the recorded iPhone/iOS17 sequence; Web `+` latency ~100–200 ms; Web Photos filtered video assets; standalone Web-chat form not accepted as final UX.
- b44 accepted `/c/<id>` A/B route mapping and eventual native read observations, but the full-page Native -> Web -> Native interaction is product-rejected. Immediate Native Sync can lag assistant output already visible in Web; no stable readiness delay/signal was established. Do not patch with timer/poll/retry.

## Current product target — Web legal Send only, Native realtime response if provable

The user explicitly rejects the separate API product route.

Current target:

`Native composer/history/presentation -> user-visible official Web performs the legal protected Send -> Native attaches/resumes/subscribes to the same already-started response without resending prompt -> Native owns user-visible reasoning/final streaming and later background lifecycle.`

This remains conditional. Fully hiding Web and hooking/injecting the Web Send control is not accepted because it would turn the protected browser Send path into hidden/shadow transport.

## Exact b45 identity

- Candidate `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`.
- Exact product/config source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- Push Run / Job `33248952646` / `99091176390` — success.
- PR Run / Job `33248954018` / `99091179731` — success.
- Push Artifact `9713774868`.
- Artifact ZIP digest `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- IPA `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`; SHA `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.
- Package identity independently verified as Release, `0.1.0 (45)`, Candidate b45, source `accd7bdf29e4`, iOS14 minimum, `[1,2]`, arm64.

## b45 first Runtime result

Exact-device export metadata matched b45 / iPhone / iOS17.0.

### Captured normal active-response behavior

- Existing-conversation-classified Send: `POST /backend-api/f/conversation`, HTTP200 `text/event-stream`, original `fetch` SSE remained live through `message_stream_complete` and `[DONE]` for ~32 seconds.
- Very early original SSE event 2 was `resume_conversation_token`; conversation identity was structurally present and the token value remained redacted.
- Later original-stream structure exposed `conversation_id`, `request_id`, and message identity markers.
- The official page opened `GET /backend-api/conversation/{id}/stream_status` during the first active response. In this capture it returned HTTP200 `application/json` with only a structural `{status: string}` payload. It was **not** an answer-event continuation stream.
- No EventSource/WebSocket/turn-stream/handoff/resume/subscribe secondary response stream was observed while either answer remained active.
- The second captured Send also stayed on the original SSE through completion, but its request structure contained `conversation_mode.gizmo_id`; it is therefore not accepted as a clean default-primary new-chat sample.

### Interpretation boundary

This is **not** a No-go result for continuation. During uninterrupted operation the official page has no reason to abandon its original Send SSE, so absence of a second stream does not prove no reconnect mechanism exists.

The missing evidence is an interruption while the original response is still active. In the uploaded export every background/foreground interval happened before a Send or after the corresponding SSE had already completed.

Therefore:

- `resume_conversation_token` existence alone does not authorize Native use/replay;
- `stream_status` must not be reinterpreted as a stream endpoint;
- Native same-response handoff remains Unknown / Unverified;
- no b46 Native continuation implementation is justified yet.

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## Next Runtime gate — reuse exact b45

No product change is required for the next evidence step because b45 already observes fetch/XHR/EventSource/WebSocket and continuation-like routes.

On the primary iPhone/iOS17 runtime:

1. clear diagnostics;
2. use default ChatGPT / primary assistant only, not a custom GPT/Gizmo;
3. start a response that will stream well beyond 30 seconds;
4. while output is visibly still streaming, background or lock the device for roughly 20–30 seconds;
5. return before the response would normally finish; do not manually refresh/resend/Stop/switch GPT;
6. let official Web recover/continue/finish naturally and export diagnostics.

Evidence question: after return, does official Web continue the same original transport, or open a status/resume/handoff/turn-stream/subscription connection that receives the same response without another Send?

## Background ordering

Background resilience remains a hard requirement. Implementation remains downstream of realtime ownership evidence:

- if Native handoff is eventually proven, background work should protect Native response lifecycle rather than WebKit;
- if Native handoff is disproven, WebKit true-background remains relevant only to the fallback visible-Web architecture.

## Candidate / PR state

- b39-b45 identities are permanently reserved.
- Any corrected product code after b45 Artifact emission requires b46+.
- PR #29 remains open/mergeable as an evidence branch and must not be merged as accepted production Send UX.
- Product source authority for b45 remains `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`; later docs-only commits do not redefine it.

## Authority / evidence rule

- `ConversationRepository` remains sole native conversation/list/read/recovery authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Native Sync/Reload never resend/regenerate.
- No second Send may be created merely to obtain a response stream.
- CI/Artifact success is not Runtime proof.
- b45 Runtime proves only the exact structural observations above; Native handoff, native reasoning/follow-tail/background ownership, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown/Unverified where not explicitly tested.
