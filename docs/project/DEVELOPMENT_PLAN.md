# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b44 integrated-hybrid Runtime rejection, API-product rejection, and hybrid-Web background-resilience gate._

## Purpose

Durable implementation sequence for the native iOS ChatGPT client. Current real source, exact CI/Artifact evidence, real-device evidence and the user's latest explicit requirements outrank stale plan wording.

Core constraints: UIKit native shell/read client, TrollStore IPA, primary tested runtime iPhone 15 Pro Max / iOS17.0, deployment target iOS14, and private/internal ChatGPT behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns where architecture permits.
4. Do not add speculative retry/fallback/timer/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency daily-use interactions such as Copy, attachments and reliable background reasoning/stream continuation outrank low-value polish once dependencies exist.
7. Optimize only evidenced bottlenecks, especially for long conversations.
8. ChatGPT-account browser Send, when used, must remain explicitly user-visible; never convert Web into hidden challenge/Send transport controlled by Native DOM automation.
9. For the TrollStore product, background resilience is measured on the exact device/runtime; main-app process survival alone is not proof that WebKit response streaming survives.

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

Retain:

- native list/detail/recovery ownership;
- per-conversation resident state and semantic reading anchors;
- Copy/timestamps/preferences/round count;
- bounded long-message display chunks;
- deterministic row heights/prefix offsets/manual message-cell layout;
- continuous O(1)-target 0.35s `.easeInOut` round navigation.

Do not replace this baseline merely to accommodate Web Send.

## Phase 9 — `DEV-send-stream` — Blocked at existing-account background gate

### Accepted protocol/security evidence

b40-b42 established current ChatGPT Web Send structure and the security boundary:

- existing/new Web Send uses `POST /backend-api/f/conversation`;
- normal response is HTTP 200 SSE with `v1`, message/patch lifecycle and `[DONE]`;
- official server Stop is `POST /backend-api/stop_conversation`;
- exact b42 default-primary-assistant Runtime proved PoW, Turnstile and `so` are required, with non-empty PoW + Turnstile finalize input before successful Send.

Therefore TD-023 remains in force: **pure-native/transient-auth ChatGPT-account Send is blocked under current architecture**. Do not implement solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints or hidden challenge WebViews.

### b43 — visible-Web feasibility

Exact b43 source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

Exact-device result:

- visible Web first/re-entry, keyboard/typing, Send, stream scrolling and rapid scrolling had no material reported issue;
- Web `+` -> picker ~100–200 ms, not rejected as excessive;
- Web Photos path filtered video assets;
- standalone Settings Web-chat form was not accepted as final product UX.

b43 validates **visible-Web feasibility/smoothness**, not final interaction.

### b44 — integrated full-page hybrid trial

Exact b44:

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.
- Product/config source `f1503cf7121512a84e5c55a3642181c17324d791`.
- Push Run / Job `33245105815` / `99081114295`, success.
- PR Run `33245107290`, success.
- Artifact `9712583513`; ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.

Runtime conclusions:

- tested Native A/B IDs mapped to corresponding Web conversations;
- immediate `返回并同步` could expose the newly sent user message while assistant output already visible in Web remained absent from Native;
- repeated immediate Web-return Sync and Native manual Sync still could miss the assistant output; a later Sync after waiting could expose it;
- no stable readiness signal/delay was evidenced;
- Native has already loaded the conversation, then Web loads/renders it again to become the Send surface;
- A -> B repeats Web-side conversation navigation/loading;
- the user explicitly rejected the interaction as too Web-driven and duplicative.

**Decision: b44 full-page hybrid form is product-rejected. Do not fix it with arbitrary delay, polling or repeated automatic Sync.**

Detailed Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b44-runtime.md`.

### Product route after b44

The user explicitly rejects the separately billed/supported API-product architecture. It is not an active Phase-9 option unless the user later reverses that decision.

The only active Send direction under evaluation is:

**Native list/history/read/navigation + an explicitly visible official-Web composer/live-response surface for the existing ChatGPT account/history.**

A hidden/covered WebView driven by a Native composer remains prohibited.

### New P0 product gate — background reasoning/stream resilience

The user reports an unacceptable recurring behavior in Web-style clients: during long reasoning/streaming, backgrounding or locking the app for a while can lead to timeout/disconnect and force manual refresh on return.

This is now a **P0 architecture gate before any polished embedded-Web b45 UI**.

Public iOS facts:

- ordinary apps may be suspended shortly after entering background;
- `beginBackgroundTask` gives finite extra runtime only;
- therefore public UIKit background time is a short-duration baseline, not a long-reasoning guarantee.

Because this product is TrollStore-installed, the next useful feasibility step is to prove whether a narrowly scoped true-background mechanism can preserve the relevant WebKit page/process/network execution or support deterministic one-shot foreground recovery after a known lifecycle interruption.

Durable plan: `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`.

Important evidence split:

- main app process alive;
- WebContent process alive;
- WebKit network/process alive;
- official Web response stream alive;
- foreground return resumed without reload;
- known interruption auto-recovered without resend/manual refresh.

These are separate claims.

### Background go/no-go before UI work

Minimum exact-device matrix on iPhone 15 Pro Max / iOS17.0 / TrollStore:

- long visible-Web reasoning/stream -> short background -> return;
- same with device lock;
- repeat around 5 minutes and 15 minutes when workload permits;
- extend longer only when a controlled test can meaningfully remain active;
- verify whether the same live official-Web response resumes without manual refresh;
- exercise public background-task expiration;
- exercise observed WebContent/process failure and one-shot foreground recovery;
- verify no prompt resend/duplicate response;
- stable Wi-Fi first, then network transition only after baseline works;
- observe battery/thermal cost sufficiently to reject harmful always-on behavior.

**Go:** normal user background habit keeps the visible Web response alive, or a known lifecycle interruption recovers automatically on foreground without resend/manual refresh.

**No-go:** Web generation routinely disconnects/stalls and needs manual refresh, WebKit execution cannot be preserved reliably, recovery would require hidden DOM automation, or battery/thermal behavior is unacceptable.

With API explicitly rejected, a No-go means **defer ChatGPT-account Send** rather than ship a fragile Web facade.

### Candidate sequencing

- b39-b44 remain permanently reserved.
- No b45 currently exists.
- Do **not** allocate a polished embedded-Web composer b45 first.
- If the user explicitly authorizes the background feasibility experiment, create the appropriately isolated/stacked background Work per `BACKGROUND_EXECUTION_PLAN.md` and `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`, then allocate the next unique Candidate only after branch/state-owner/conflict preflight.
- Only after background Go evidence should a later Candidate implement the polished embedded visible composer/live-response UI.

## Phase 10 — `DEV-attachments` — high priority but Send/background-dependent

Attachment daily-use priority remains high, but the existing-account Send architecture and background gate must pass first.

Known requirements/evidence:

- composer `+` must react immediately; b43 Web `+` ~100–200 ms was acceptable in tested scope;
- iOS17 Web Photos chooser filtered video assets;
- public `WKUIDelegate` file-open-panel replacement is iOS18.4+, not iOS17;
- do not use private WebKit or DOM/file-input injection to fake video support;
- for iOS17, proper photo+video selection requires an evidenced native upload/handoff path;
- generic file sending and assistant file tap-download-share remain in `ATTACHMENT_TRANSFER_PLAN.md`;
- no automatic transfer retry/watchdog/timer loops.

## Phase 11 — `DEV-message-rendering`

Implement native rich message presentation for Markdown paragraphs/headings/lists/links, emphasis, inline/fenced code, code-block Copy and tables as needed. Investigate current user-visible citation/annotation markers from real protocol content. Preserve authoritative visible text and never expose hidden reasoning/tool/system content.

This work is independent enough to be reprioritized while Send remains architecture-blocked if the user explicitly requests it.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted cache owner/store. Prefer list-response preview only when evidenced; otherwise bounded preview comes from Detail/Sync/Reload activity. Never issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current user-visible native branch; never scrape mounted cells or hybrid Web DOM.

## Phase 14 — `DEV-long-conversation`

Measure native network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve Stable b38 deterministic geometry unless new evidence justifies change.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

The generic background plan remains response-owner-based. For the current hybrid account path, `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md` is the prerequisite feasibility gate before later notification/polish work.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities only with current protocol/UI evidence.

## Current next action

**Human gate:** decide whether to run the existing-account Web background-resilience feasibility experiment.

- If yes: create the isolated/stacked experiment Work, re-run branch/PR/base/state-owner/candidate conflict preflight, and build the smallest Candidate that measures public-background + TrollStore/WebKit survival/recovery. Do not start with UI polish.
- If no: leave ChatGPT-account Send deferred.

The API product route is not active. Preserve b39-b44 identities, rejected Artifact `9710515489`, exact b44 Runtime evidence and Stable b38 native baseline.
