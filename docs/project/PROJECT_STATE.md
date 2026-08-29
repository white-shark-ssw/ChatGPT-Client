# Project State

_Last updated: 2026-08-29 through exact b45 repeated active-response background/lock Runtime; forced transport-interruption reconnect evidence remains pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the current Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen; current native conversation modules remain Frozen No.

## Current target/base status

`DEV-send-stream` was activated from `main@34811877896ca88c6656be6676f5466a19931ce6`.

Current `main` is `1ac202c972f2dee6945fe8d0688df8e10f5d462c`. The three intervening main commits modify only root `AGENTS.md`; current compare shows no Swift/Xcode/workflow/product/state-owner overlap with b45. The feature branch has not yet synchronized that rules-only main advance.

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

## b45 first Runtime result — uninterrupted traffic

- `POST /backend-api/f/conversation` returned HTTP200 `text/event-stream`.
- Original SSE emitted `resume_conversation_token` very early, then conversation/request/message identity structure.
- Official page opened `GET /backend-api/conversation/{id}/stream_status`; observed response was only HTTP200 JSON `{status:string}`.
- No EventSource/WebSocket/turn-stream/handoff/resume/subscribe secondary stream appeared while the uninterrupted response remained active.
- The original Send `fetch` SSE stayed the response transport through `message_stream_complete` and `[DONE]`.

That capture did not force reconnect and therefore did not establish Native continuation.

## b45 second Runtime result — repeated active background / lock

The user explicitly reports a **new conversation** and several suspend/lock cycles while the answer was still active. Export metadata again matches exact b45 / iPhone / iOS17.0.

### Clean default-primary new-chat structure

- Probe initially loaded `new_or_other`.
- Send at `12:45:20Z` used `POST /backend-api/f/conversation`, HTTP200 SSE.
- Request structure had **no top-level `conversation_id`** and **no `conversation_mode.gizmo_id`**.
- Together with the user's explicit Runtime statement, this is accepted as the clean default-primary new-chat sample despite the probe's later `pageKind=existing_conversation` label at Send time.
- Original SSE again emitted `resume_conversation_token` at event 2, then conversation/request/message identity structure.
- `stream_status` again returned only JSON `{status:string}`.

### Active-response background evidence

While that same original SSE remained active, the app entered background for approximately:

- 35 seconds;
- 34 seconds;
- 126 seconds.

Total active-response background time: approximately **195 seconds / 3m15s**.

Send-to-terminal elapsed time: approximately **227 seconds / 3m47s**.

At the end of the final ~126-second background interval, `willEnterForeground` and original-stream events 464–467 occurred in the same second. The **same original `conversation_send` / `fetch` stream** delivered `server_ste_metadata -> message_stream_complete -> conversation_detail_metadata -> [DONE]`.

No second Send, no new SSE response, and no resume/handoff/turn-stream/subscribe/EventSource/WebSocket connection appeared after any background interval. No manual refresh or resend was needed.

### Evidence boundary

This is positive exact-device evidence that the tested official-Web/WebKit response path can **survive or buffer** across repeated ordinary background/lock intervals, including one ~126-second interval, and still complete normally.

It does not prove continuous event delivery while suspended; delivery may have been buffered until foreground. It also does not prove 5/15-minute behavior, WebContent termination, network transition or Native continuation.

Because the original transport survived, official Web again had no reason to reveal a reconnect mechanism. `resume_conversation_token` remains an observed field, not an authorized Native API contract.

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## Updated Runtime gate — reuse exact b45, force transport failure

Natural short background is now a weak way to discover continuation because the original WebKit fetch survived three active-response intervals.

Next exact-device test:

1. clear diagnostics;
2. use default ChatGPT / primary assistant in an **existing long conversation**;
3. start a long response;
4. while visibly streaming, deliberately remove connectivity for about 10–15 seconds, then restore it; preferred controlled test is Airplane Mode / both Wi-Fi and cellular unavailable, or a Wi-Fi -> cellular transition after a stable Wi-Fi baseline;
5. do not refresh, resend, Stop, switch GPT or navigate away;
6. let official Web recover or fail naturally and export diagnostics.

Evidence question: after a genuine transport break, does official Web open an official status/resume/handoff/turn-stream/subscription connection that continues the same response without another Send?

Only exact observed reconnect structure may justify a later b46 Native no-resend parity experiment. If no reconnect path appears, record the negative evidence and reassess the architecture ceiling rather than guessing an endpoint.

## Background ordering

TD-026 remains a hard requirement, but Capture C gives a positive short-background signal:

- ordinary tested background/lock up to ~126 seconds continuous did not force manual refresh or prompt resend;
- 5-minute, 15-minute, process-termination, network-transition and battery/thermal matrix remains Unverified;
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
- Native same-response handoff, native reasoning/follow-tail/background ownership, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown/Unverified where not explicitly tested.