# Project State

_Last updated: 2026-08-29 through exact b45 Native-realtime-handoff diagnostic Candidate; Runtime handoff evidence pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the current Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen; current native conversation modules remain Frozen No.

## Current Phase 9 — DEV-send-stream

### Security boundary retained

Exact b42 (`e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`) proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output: PoW, Turnstile and `so` required; non-empty PoW + Turnstile were finalized before Send.

Therefore pure-native/transient-auth ChatGPT-account Send remains blocked. Prohibited routes remain solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoint, hidden/shadow challenge WebView, challenge harvesting, DOM answer/reasoning scraping, covered-Web Native composer injection, synthetic hidden Send clicks and hidden file-input injection.

### b43 visible-Web feasibility baseline

Exact b43 source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

Primary-device Runtime:

- first/re-entry, keyboard/typing, visible Web Send, stream scrolling, rapid scrolling and native return had no material reported problem;
- Web `+` -> picker latency was roughly **100–200 ms**, not rejected as excessive;
- Web photo selection filtered video assets;
- standalone Settings Web-chat UX was not accepted as final product interaction.

Verified iOS17 boundary: public `WKUIDelegate.runOpenPanelWith...` replacement is iOS18.4+, so iOS17 cannot publicly replace the page's upload chooser with a custom PHPicker through that delegate. Proper iOS17 photo+video attachment support still requires separately evidenced native attachment upload/handoff.

### b44 integrated full-page hybrid trial — product form rejected

Exact b44:

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`;
- product/config source `f1503cf7121512a84e5c55a3642181c17324d791`;
- Push Run / Job `33245105815` / `99081114295` — success;
- PR Run `33245107290` — success;
- Artifact `9712583513`;
- ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`;
- IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.

Runtime established that Web Send and tested `/c/<id>` A/B mapping worked, but immediate Native Sync could expose the just-sent user message while assistant output already visible in Web remained absent until a later Sync. No stable readiness delay/signal was established. The same conversation also had to be loaded by Native and then Web. The full-page Native -> Web -> Native product form is rejected / superseded; do not patch it with arbitrary delay, polling or repeated automatic Sync.

## Current product decision — Web Send only if Native can own realtime response

The user explicitly rejects the separate API product route.

The user's preferred architecture is now:

`Native composer/history/presentation -> user-visible official Web performs the legal protected Send -> Native attaches/resumes/subscribes to the same already-started response without resending prompt -> Native owns user-visible reasoning/final streaming and later background lifecycle.`

This is the current **target**, not an accepted capability. The key unknown is whether the official ChatGPT account flow exposes a same-response continuation mechanism that Native can legitimately consume without issuing another Send.

The user's alternative suggestion of completely hiding Web and hooking/injecting the Web Send control is not an accepted route because it would make the protected browser Send flow a hidden/shadow transport under a Native facade.

## Exact b45 — Native realtime handoff diagnostic probe

Candidate identity:

- `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`;
- exact product/config source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`;
- Push Run / Job `33248952646` / `99091176390` — success;
- PR Run / Job `33248954018` / `99091179731` — success;
- Push Artifact `9713774868`;
- Artifact ZIP digest `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`;
- IPA `ChatGPTClient-0.1.0-b45-dev-send-stream.ipa`;
- IPA SHA `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`;
- package identity independently verified as `0.1.0 (45)`, Candidate b45, source marker `accd7bdf29e4`, Release, iOS14 minimum, `[1,2]`, arm64.

b45 adds an observation-only `ProtocolHandoffProbeViewController`, reached from Settings as `实时接管协议探测（诊断）`.

The probe structurally observes:

- original `/backend-api/f/conversation` SSE;
- presence/shape only for `resume_conversation_token`, response/turn/conversation/message/async-task identity fields;
- official-page post-Send same-origin fetch/XHR/EventSource/WebSocket connections;
- stream-status / turn-stream / handoff / resume / subscribe / continuation-like route classes;
- HTTP status/content type, header names, query names, structural JSON shape and identity-value shape only;
- whether a later official-page connection naturally receives continuation-like events without another Send.

It does **not** replay resume tokens, guess endpoints, resend prompts, inject into hidden Web controls, scrape answer/reasoning text or capture protected values.

**b45 classification: Code / CI / Artifact / package identity passed. Runtime handoff capability Unknown / Unverified. Stable/Frozen Send No.**

## Background ordering — still a hard requirement, now downstream of handoff feasibility

The user requires that long reasoning/streaming not routinely break after background/lock and force manual refresh.

TD-026 remains a hard product gate, but implementation order changed:

- if b45/b46 prove Native can own/resume the response stream, background work should protect that Native response lifecycle;
- only if Native handoff is disproven does WebKit true-background remain relevant to the fallback visible-Web architecture;
- do not spend a Candidate on Web background/UI polish before the handoff evidence is interpreted.

## Current Runtime gate

Primary authority: iPhone 15 Pro Max / iOS17.0 TrollStore runtime.

Exact b45 test:

1. Settings -> clear diagnostics if practical.
2. Open `实时接管协议探测（诊断）`.
3. Use default ChatGPT / primary assistant.
4. Send one sufficiently long new-chat prompt and let it run normally.
5. If practical, send one existing-chat prompt and let it run normally.
6. Do not manually refresh during capture.
7. Export diagnostics JSON and analyze for an official same-response continuation mechanism.

If positive evidence exists, the next Candidate may test Native no-resend continuation parity against the **exact observed** route/structure. If negative, do not guess a resume endpoint.

## Candidate / PR state

- b39-b45 identities are permanently reserved.
- b45 is the current Runtime diagnostic Candidate; any corrected product code after Artifact emission requires b46+.
- PR #29 remains open/mergeable as an evidence branch and must not be merged as accepted production Send UX.
- Product source authority for b45 remains `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`; later docs-only commits do not redefine it.

## Authority / evidence rule

- `ConversationRepository` remains sole native conversation/list/read/recovery authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- UI text/title is never identity authority.
- Native Sync/Reload never resend/regenerate.
- CI/Artifact success is not Runtime proof.
- no second Send may be created merely to obtain a response stream.
- iOS17 evidence does not prove lower iOS/iPad; non-personal workspace/account switch and native attachment handoff remain Unknown/Unverified where not explicitly tested.
