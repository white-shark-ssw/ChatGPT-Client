# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b45 Native-realtime-handoff diagnostic Candidate; Runtime evidence pending._

## Purpose

Durable implementation sequence for the native iOS ChatGPT client. Current real source, exact CI/Artifact evidence, real-device evidence and the user's latest explicit requirements outrank stale plan wording.

Core constraints: UIKit native shell/read client, TrollStore IPA, primary tested runtime iPhone 15 Pro Max / iOS17.0, deployment target iOS14, and private/internal ChatGPT behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns where architecture permits.
4. Do not add speculative retry/fallback/timer/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency daily-use interactions such as Copy, attachments and reliable long-response/background behavior outrank low-value polish once dependencies exist.
7. Optimize only evidenced bottlenecks, especially for long conversations.
8. ChatGPT-account protected Send may use only an explicitly user-visible official-Web surface; never convert Web into hidden challenge/Send transport controlled by Native DOM/button automation.
9. Web is not the desired realtime-response presentation owner. First prove whether Native can attach/resume/subscribe to the already-started response without a second Send.

## Accepted merged foundation

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for recorded scope; default persistent `WKWebsiteDataStore` is sole persistent auth-secret authority.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic read evidence.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is native conversation authority.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15; PR #10.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21 for recorded Plus/personal iPhone/iOS17 read-state scope; PR #23; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23; PR #24; Frozen No.
- **Phase 8 `DEV-conversation-round-count`: merged Stable b38; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

## Stable Phase 8 native baseline

Exact b38:

- Candidate `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- Product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- User exact-device result: **“没问题了”**.

Retain native list/detail/recovery ownership, per-conversation resident state and semantic anchors, Copy/timestamps/preferences/round count, bounded long-message chunks, deterministic row heights/prefix offsets/manual message-cell layout, and continuous O(1)-target 0.35s `.easeInOut` round navigation. Do not replace this baseline merely to accommodate Web Send.

## Phase 9 — `DEV-send-stream` — Active at Native realtime-handoff Runtime gate

### Accepted protocol/security evidence

b40-b42 established current ChatGPT Web Send structure and the security boundary:

- existing/new Web Send uses `POST /backend-api/f/conversation`;
- normal response is HTTP 200 SSE with `v1`, message/patch lifecycle and `[DONE]`;
- b40 observed early `resume_conversation_token` during the Send stream;
- official server Stop is `POST /backend-api/stop_conversation`;
- exact b42 default-primary-assistant Runtime proved PoW, Turnstile and `so` are required, with non-empty PoW + Turnstile finalize input before successful Send.

Therefore TD-023 remains in force: **pure-native/transient-auth ChatGPT-account Send is blocked**. Do not implement solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints or hidden challenge WebViews.

### b43 — visible-Web feasibility

Exact b43 source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

Exact-device result: visible Web first/re-entry, keyboard/typing, Send, stream scrolling and rapid scrolling had no material reported issue; Web `+` -> picker ~100–200ms; Web Photos filtered video assets. This validates visible-Web feasibility only, not final product interaction.

### b44 — full-page integrated hybrid rejected

Exact b44 source `f1503cf7121512a84e5c55a3642181c17324d791`, Artifact `9712583513`, IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.

Runtime established tested `/c/<id>` mapping, but immediate Native Sync could expose the newly sent user message while assistant output already visible in Web remained absent until later. No stable readiness signal/delay was evidenced. Native also loads the conversation before Web loads it again for Send. The user rejected this full-page Web-driven product form. Do not patch it with arbitrary delay, polling or repeated automatic Sync.

### Product direction after b44

The user explicitly rejects the separately billed/supported API-product route.

The desired architecture, if evidence permits, is now:

`Native composer/history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes/subscribes to the same in-progress response without resending prompt -> Native owns user-visible reasoning/final stream and later background lifecycle.`

This makes Web a minimal Send initiator rather than the realtime chat UI owner.

A fully covered/hidden WebView with Native text injection or a hooked/synthetic hidden Web Send button remains rejected: that would turn the protected browser path into hidden/shadow transport.

### b45 — Native realtime handoff evidence Candidate

Exact b45:

- Candidate `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`;
- exact product/config source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`;
- Push Run / Job `33248952646` / `99091176390` — success;
- PR Run / Job `33248954018` / `99091179731` — success;
- Push Artifact `9713774868`;
- Artifact ZIP digest `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`;
- IPA SHA `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`;
- package identity verified as b45 / `0.1.0 (45)` / source `accd7bdf29e4` / Release / iOS14 minimum / `[1,2]` / arm64.

b45 is **observation-only**. It adds a visible `实时接管协议探测（诊断）` surface which observes:

- original `/backend-api/f/conversation` SSE;
- structural presence/shape of resume/response/turn/conversation/message/async-task identities;
- post-Send same-origin fetch/XHR/EventSource/WebSocket traffic created naturally by official Web;
- stream-status / turn-stream / handoff / resume / subscribe / continuation-like route classes;
- HTTP/content-type/header-name/query-name/structural-payload evidence only.

It never replays a resume token, guesses a continuation route, issues a second Send, injects a hidden composer, clicks hidden Web controls, captures protected challenge values or scrapes answer/reasoning text.

**Current evidence level: Code/CI/Artifact/package identity passed; Runtime handoff capability Unknown/Unverified.**

Detailed probe record: `runtime-evidence/DEV-send-stream-b45-handoff-probe.md`.

### b45 Runtime decision gate

Primary-device test on iPhone 15 Pro Max / iOS17.0:

1. Clear diagnostics if practical.
2. Settings -> `实时接管协议探测（诊断）`.
3. Use default ChatGPT / primary assistant.
4. Send one new-chat prompt long enough to expose reasoning/stream behavior; do not manually refresh.
5. If practical, send one existing-chat prompt and let it run normally.
6. Export diagnostics JSON.

**Positive:** official Web naturally demonstrates a same-response continuation mechanism with enough route/identity structure to justify a later Native no-resend parity test.

**Negative:** ordinary ChatGPT keeps realtime response only on the original `/f/conversation` SSE or no supportable continuation mechanism is observed. Do not guess an endpoint from absence.

If positive, allocate b46 only after a fresh identity/conflict guard and implement the smallest Native continuation parity experiment against the exact observed behavior.

### Background ordering

Reliable background/lock behavior remains a hard product requirement, but it is now downstream of the realtime-handoff gate.

- If Native can own/resume the response stream, background work should preserve that Native lifecycle using `BACKGROUND_EXECUTION_PLAN.md`; this is the preferred architecture.
- Only if Native handoff is disproven does `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md` remain relevant to a fallback visible-Web response owner.
- Do not spend Candidate identity on Web background/UI polish before b45 evidence is interpreted.

## Phase 10 — `DEV-attachments` — high priority but Send-architecture-dependent

Known requirements/evidence:

- composer `+` must react immediately; b43 Web `+` ~100–200ms was acceptable;
- iOS17 Web Photos chooser filtered videos;
- public `WKUIDelegate` file-open-panel replacement is iOS18.4+, not iOS17;
- do not use private WebKit or DOM/file-input injection to fake video support;
- proper iOS17 photo+video support requires an evidenced native upload/handoff path;
- generic file sending and assistant file tap-download-share remain in `ATTACHMENT_TRANSFER_PLAN.md`;
- no automatic transfer retry/watchdog/timer loops.

## Phase 11 — `DEV-message-rendering`

Implement native rich message presentation for Markdown paragraphs/headings/lists/links, emphasis, inline/fenced code, code-block Copy and tables as needed. Investigate current user-visible citation/annotation markers from real protocol content. Preserve authoritative visible text and never expose hidden reasoning/tool/system content.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted cache owner/store. Prefer list-response preview only when evidenced; otherwise bounded preview comes from Detail/Sync/Reload activity. Never issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current user-visible native branch; never scrape mounted cells or hybrid Web DOM.

## Phase 14 — `DEV-long-conversation`

Measure native network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve Stable b38 deterministic geometry unless new evidence justifies change.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities only with current protocol/UI evidence.

## Current next action

**Human Runtime gate:** install exact b45 and export the new-chat + existing-chat realtime-handoff diagnostics.

- Positive official continuation evidence -> fresh guard -> b46 Native no-resend continuation parity experiment.
- Negative evidence -> record the architecture ceiling; do not invent/replay a resume route.
- Do not reactivate the API product route, hidden Web automation, polished Web UI or TrollStore background implementation before this evidence is interpreted.

Preserve b39-b45 identities, rejected Artifact `9710515489`, exact b44 Runtime evidence and Stable b38 native baseline.
