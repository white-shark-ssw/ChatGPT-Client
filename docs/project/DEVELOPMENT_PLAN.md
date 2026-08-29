# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b45 repeated active-response background/lock Runtime._

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
8. ChatGPT-account browser Send, when used, must remain explicitly user-visible; never convert Web into hidden protected transport controlled by Native DOM automation.
9. A token/event name is not an implementation contract by itself. Native parity requires an observed official request/response structure or other direct Runtime evidence.

## Accepted merged foundation

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for recorded scope.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic read evidence.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is native conversation authority.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21 for recorded read-state scope; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23; Frozen No.
- **Phase 8 `DEV-conversation-round-count`: merged Stable b38; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

## Stable Phase 8 native baseline

Exact b38: Candidate `DEV-conversation-round-count-0.1.0-b38`, source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Runtime Artifact `9708425762`, IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.

Retain native list/detail/recovery ownership, per-conversation resident state, Copy/timestamps/preferences/round count, bounded long-message chunks, deterministic row geometry/manual cell layout, and continuous O(1)-target round navigation. Do not replace this baseline merely to accommodate Web Send.

## Phase 9 — `DEV-send-stream` — Active forced-reconnect evidence gate

### Accepted security/product evidence

- b40-b41 established the current official-Web Send SSE shape and server Stop structure.
- Exact b42 proved PoW, Turnstile and `so` are required before successful ChatGPT-account Send. Pure-native/transient-auth account Send remains blocked.
- b43 proved visible official Web can be sufficiently smooth for legal Send interaction on the tested iPhone/iOS17 path; Web `+` ~100–200 ms; Web Photos filtered videos.
- b44 proved tested `/c/<id>` mapping but also exposed the full-page Native -> Web -> Native architecture ceiling: immediate native reconciliation can lag Web output, no stable readiness signal/delay was established, and the user rejected duplicated full-page Web interaction.
- The user explicitly rejects the separately authenticated/billed API-product architecture.

### Current target architecture

Only if current Runtime evidence supports it:

`Native composer/history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes/subscribes to the same already-started response without resending prompt -> Native owns user-visible realtime response + later background lifecycle.`

Fully hidden Web + Native DOM/button injection remains rejected.

### Exact b45 diagnostic Candidate

- Candidate `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`.
- Product/config source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- Push Run / Job `33248952646` / `99091176390`, success.
- PR Run / Job `33248954018` / `99091179731`, success.
- Artifact `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- IPA SHA `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.

b45 observes original Send SSE and official-page post-Send fetch/XHR/EventSource/WebSocket continuation candidates, structurally only. It never replays tokens, guesses routes, issues a second Send, scrapes answer/reasoning text or captures protected values.

### b45 first Runtime — uninterrupted path

- `POST /backend-api/f/conversation` returned HTTP200 `text/event-stream`.
- `resume_conversation_token` appeared at original SSE event 2.
- original-stream structure later included conversation identity, `request_id` and message identity markers.
- official page opened `GET /backend-api/conversation/{id}/stream_status`; observed response was HTTP200 JSON `{status:string}` only.
- original Send `fetch` SSE stayed the response transport through `message_stream_complete` and `[DONE]`.
- no secondary EventSource/WebSocket/turn-stream/handoff/resume/subscribe response stream was observed while uninterrupted responses were active.

This did not prove or disprove an interruption-only reconnect path.

### b45 second Runtime — clean new-chat active background / lock

The user explicitly identifies the later capture as a new conversation. The observed Send body had neither top-level `conversation_id` nor `conversation_mode.gizmo_id`, so this is accepted as the clean default-primary new-chat sample.

While the original Send SSE remained active, the app was backgrounded/locked for approximately:

- 35 seconds;
- 34 seconds;
- 126 seconds.

Cumulative active-response background time was ~195 seconds / 3m15s; Send-to-terminal elapsed time was ~227 seconds / 3m47s.

At the end of the final ~126-second interval, the **same original `conversation_send` / `fetch` stream** delivered `server_ste_metadata -> message_stream_complete -> conversation_detail_metadata -> [DONE]` immediately on foreground return.

No second Send, no new SSE response, no resume/handoff/turn-stream/subscription stream and no manual refresh/resend were observed.

Interpretation:

- positive exact-device evidence that the tested WebKit/original-fetch response path can survive or buffer through repeated ordinary short background/lock;
- not proof of continuous event delivery while suspended;
- not proof of 5/15-minute background behavior;
- not proof of Native handoff;
- ordinary short background is now a poor mechanism for discovering a reconnect route because the original transport survives.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

### Current exact next step — reuse b45, force a real transport break

Do **not** allocate b46 yet. Reuse exact b45 in an existing long default-primary conversation:

1. clear diagnostics;
2. start a response expected to remain active long enough to observe recovery;
3. while visibly streaming, deliberately remove connectivity for about 10–15 seconds, then restore it;
4. preferred deterministic test: Airplane Mode / both Wi-Fi and cellular unavailable, then restore; Wi-Fi -> cellular is also useful after a stable Wi-Fi baseline;
5. do not refresh, resend, Stop, switch GPT or navigate away;
6. let official Web recover or fail naturally;
7. export diagnostics.

Evidence question: after a genuine transport break, does official Web open an official status/resume/handoff/turn-stream/subscription connection that continues the same already-started response without a second Send?

Only positive observed reconnect structure can justify a later b46 Native no-resend parity experiment. If no reconnect mechanism appears after a real transport failure, record that negative evidence and reassess the account-compatible architecture ceiling rather than guessing from `resume_conversation_token`.

### Background ordering

Background resilience remains P0. Exact b45 now provides a positive short-background signal, but full product acceptance still requires longer/process/network evidence.

- if Native handoff is proven, background work should protect Native response lifecycle;
- if handoff is disproven, WebKit true-background is relevant only to fallback visible-Web architecture;
- 5-minute, 15-minute, WebContent/process termination, network transition and battery/thermal remain separate gates.

### Candidate sequencing

- b39-b45 are permanently reserved.
- Do not modify b45 product/config source after Artifact emission.
- Do not allocate b46 merely because b45 Runtime exists; allocate it only when exact official reconnect traffic justifies a concrete Native parity experiment or another evidenced product change requires it.

## Phase 10 — `DEV-attachments` — high priority but Send-owner dependent

Attachment daily-use priority remains high. Known current boundaries:

- Web `+` ~100–200 ms was acceptable in b43;
- iOS17 Web Photos chooser filtered videos;
- public `WKUIDelegate` upload-panel replacement is iOS18.4+, not iOS17;
- do not use private WebKit or DOM/file-input injection;
- native iOS17 photo+video support requires an evidenced upload/handoff path;
- assistant file tap-download-share remains a core target before a full download manager.

## Phase 11 — `DEV-message-rendering`

Implement native Markdown/code/table/link/citation presentation only from authoritative user-visible content. Never expose hidden reasoning/tool/system content.

## Phase 12 — `DEV-conversation-list-preview`

Reuse the accepted list-cache owner/store. Do not issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export the authoritative current native user-visible branch; never scrape hybrid Web DOM.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve Stable b38 deterministic geometry unless new exact Runtime evidence justifies change.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities only with current protocol/UI evidence.

## Current next action

**Human Runtime gate on the same exact b45 IPA:** use an existing long default-primary conversation and deliberately break connectivity for ~10–15 seconds while the response is visibly streaming, then restore connectivity and let official Web recover or fail naturally. Do not refresh/resend/Stop/switch GPT/navigate away. Export diagnostics afterward.

After that evidence is interpreted, either:

- observed official reconnect/continuation structure -> fresh guard -> allocate b46 for the smallest Native no-resend parity experiment;
- no reconnect route after genuine transport failure -> record negative Runtime and reassess the architecture ceiling;
- response survives despite the intended break -> refine the interruption method from exact evidence rather than guessing a Native API.