# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b44 integrated-hybrid Runtime rejection and TD-025 architecture gate._

## Purpose

Durable implementation sequence for the native iOS ChatGPT client. Current real source, exact CI/Artifact evidence, real-device evidence and the user's latest explicit requirements outrank stale plan wording.

Core constraints: UIKit native shell/read client, TrollStore IPA, primary tested runtime iPhone 15 Pro Max / iOS17.0, deployment target iOS14, and private/internal ChatGPT behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns where architecture permits.
4. Do not add speculative retry/fallback/timer/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency daily-use interactions such as Copy and attachments outrank low-value polish once dependencies exist.
7. Optimize only evidenced bottlenecks, especially for long conversations.
8. ChatGPT-account browser Send, when used, must remain explicitly user-visible; never convert Web into hidden challenge/Send transport controlled by Native DOM automation.

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

## Phase 9 — `DEV-send-stream` — Blocked at architecture gate

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

b43 therefore validates **visible-Web feasibility/smoothness**, not the final interaction.

### b44 — integrated full-page hybrid trial

Exact b44:

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.
- Product/config source `f1503cf7121512a84e5c55a3642181c17324d791`.
- Push Run / Job `33245105815` / `99081114295`, success.
- PR Run `33245107290`, success.
- Artifact `9712583513`; ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.

Trial flow:

`native detail -> 发送消息… -> visible Web /c/<conversation-id> -> Send -> 返回并同步 -> native detail`

Runtime conclusions:

- tested Native A/B IDs mapped to the corresponding Web conversations;
- immediate `返回并同步` could expose the newly sent user message while assistant output already visible in Web remained absent from Native;
- repeating immediate Web-return Sync and Native manual Sync still could miss the assistant output; a later Sync after waiting could expose it;
- no stable readiness signal/delay was evidenced;
- Native has already loaded the conversation, then Web loads/renders it again to become the Send surface;
- A -> B repeats Web-side conversation navigation/loading;
- the user explicitly rejected the interaction as too Web-driven and duplicative.

**Decision: b44 full-page hybrid form is product-rejected. Do not fix it with arbitrary delay, polling or repeated automatic Sync.**

Detailed Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b44-runtime.md`.

### TD-025 architecture gate

No b45 is allocated until one direction is explicitly chosen.

#### A — keep existing ChatGPT-account continuity

Native list/history/read/navigation remain primary. The next allowed experiment is an **explicitly visible embedded official-Web composer/live-response panel** inside the native detail rather than a separate full-page Web chat.

Requirements:

- actual official Web composer/live-response area remains visibly exposed and directly user-operated;
- no Native text field secretly driving a hidden Web DOM/contenteditable;
- no hidden synthetic Send click;
- no DOM answer/reasoning scraping to manufacture Native response authority;
- Web live response remains the immediate truth while active; Native reconciliation happens only when real read availability supports it;
- no automatic poll/retry loop absent a real readiness signal.

This preserves current ChatGPT-account/session/history continuity as far as current evidence permits, but **Send/stream remains Web-owned while active**.

#### B — truly Native Send/stream

Use an officially supported API product with separate API authentication/billing, then implement Native composer, incremental response lifecycle, attachments and follow-tail natively.

Before implementation, re-verify current official API auth/model/stream/files documentation. ChatGPT subscription and API billing are separate; do not claim API conversations are automatically the same existing ChatGPT-account history/session.

#### C — defer ChatGPT-account Send

Keep the Stable native read client and wait for a supported ChatGPT-account transport that does not require browser-owned challenge output.

### Explicitly rejected fourth route

A fully covered/hidden official WebView plus a Native composer that forwards text into Web is not an accepted compromise. Under current evidence that requires DOM/JS/input automation of a hidden protected browser Send flow and violates TD-023/TD-024/TD-025.

## Phase 10 — `DEV-attachments` — high priority but transport-dependent

Attachment daily-use priority remains high, but Send architecture must be resolved first.

Known requirements/evidence:

- composer `+` must react immediately; b43 Web `+` ~100–200 ms was acceptable in tested scope;
- iOS17 Web Photos chooser filtered video assets;
- public `WKUIDelegate` file-open-panel replacement is iOS18.4+, not iOS17;
- do not use private WebKit or DOM/file-input injection to fake video support;
- for iOS17, proper photo+video selection requires an evidenced native upload/handoff path;
- generic file sending and assistant file tap-download-share remain in `ATTACHMENT_TRANSFER_PLAN.md`;
- no automatic transfer retry/watchdog/timer loops.

If Phase 9 chooses API path B, attachment architecture can be native against supported API file semantics after current official documentation is verified. If Phase 9 stays on account-compatible path A, native attachment handoff must still be separately evidenced.

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

Isolated Work IDs for download manager, pagination, background completion, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

Background completion remains dependent on an accepted authoritative response lifecycle; visible Web Send alone does not establish native background response ownership.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities only with current protocol/UI evidence.

## Current next action

**Human architecture gate:** explicitly choose TD-025 A, B or C before any new Send product code or Candidate allocation.

- Choose **A** if retaining current ChatGPT account/history is the priority and an explicitly visible embedded Web composer/live-response panel is acceptable.
- Choose **B** if truly Native composer/stream/attachment UX is more important than using the existing ChatGPT subscription/history path.
- Choose **C** if neither compromise is acceptable and ChatGPT-account Send should wait.

Preserve b39-b44 identities, rejected Artifact `9710515489`, exact b44 Runtime evidence and Stable b38 native baseline. **No b45 currently exists.**
