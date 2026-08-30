# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-31 through exact b66 Runtime failure and exact b67 Code/CI/Artifact/package verification._

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client while preserving one authority per state domain. Current real source, exact CI/Artifact evidence, exact-device Runtime evidence and latest explicit requirements outrank stale plans.

Core rules: no speculative retry/fallback/timer/watchdog/polling/duplicate state; distinguish Code / CI / Artifact / Runtime / Stable; private Web behavior must be measured rather than guessed; full Web conversation rendering remains rejected as the daily-chat dependency.

## Accepted merged foundation

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for recorded scope.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic evidence.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is native conversation authority.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23; Frozen No.
- Phase 8 `DEV-conversation-round-count`: merged Stable b38; exact source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; PR #27 merged `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.

Retain b38 bounded long-message chunks, deterministic geometry/manual layout and continuous O(1)-target round navigation.

## Phase 9 — `DEV-send-stream` — Active production integration

### Durable Send boundary

- b42 proves ChatGPT-account protected Send requires browser anti-abuse challenge output; pure-native/transient-auth protected Send remains blocked.
- Separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription route remains blocked by account-safety policy.
- TD-025/TD-028 continue to reject the full-page hybrid product form and full existing-conversation Web rendering.
- **TD-029 is the current production architecture:** Native send action -> `ConversationRepository` response operation -> covered official page performs exactly one protected Send -> same-response SSE -> Repository incremental response state -> Native consumers.
- Covered Web is transport/challenge execution only and uses the existing `WKWebsiteDataStore.default()`; it never becomes a second conversation/message/response/draft/auth-secret authority.
- Final Composer UI belongs future serialized `DEV-composer-parity`. Current Work keeps only a validation text trigger needed to accept Send/Stop/response semantics first.

### Accepted diagnostic/protocol progression

- b45 Runtime Confirmed official no-resend resume; b46/b47 duplicated Native Cookie+Bearer-only resume rejected.
- b48-b51 established Native composer -> official protected Send and complete compact response text, including exact `title_generation` continuation.
- b52-b56 identified reasoning/tool grammar and exact `reasoning_ended`; `assistant:thoughts` remains non-presentational.
- b57-b59 established Native reasoning/final split and service-marked thinking-preamble inclusion.
- b60 passed thinking/segmentation/text-completeness and exact result-parent association.
- b61 exposed generic-textarea false readiness; b62 removed that authority and passed the verified-composer path.
- b63 same-run Runtime plus official-Web expanded detail authorized the minimal GitHub input/output mapping only.
- b64 passed protected Send/reasoning/final/exact-parent detail lifecycle; formatting/density only rejected.
- b65 fixed only nested disclosure/readable output and passed focused iPhone/iOS17 Runtime. It is the accepted diagnostic predecessor for the production bridge.

### Web Rule Lab / maintenance foundation

`WEB_SEND_ADAPTER.md` owns current Web composer/protected-Send/SSE/reasoning/tool rules and future update procedure.

The current branch implements the development-only Web Rule Lab:

- Settings-reachable visible `WKWebView` using `.default()` store;
- explicit user-pasted/edited JS + explicit execute;
- temporary result + copy/share;
- no auto-run;
- no persistence/logging of script/result bodies;
- never production response owner.

b66 diagnostics already observed Lab open and page load. Future official-Web changes should use `reproduce -> Lab probe -> evidence -> one minimal adapter update -> one Candidate`, not speculative selector/fallback IPA loops.

### Exact b66 — first production existing-conversation bridge

Identity:

- Candidate `DEV-send-stream-0.1.0-b66`, `0.1.0 (66)`;
- source `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`; tree `31ef29457273a44dd202a63a96560563154e8823`;
- Push `33337771534 / 99327694040` — success;
- PR `33337774136 / 99327701256` — success;
- Push Artifact `9739572172`;
- ZIP `sha256:6c6d8e165ed070e88a27abafc57973dc847937826e40c552bf9f0d29bb91bb45`;
- IPA `sha256:7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`.

Product scope:

- process-resident covered executor exact-targets existing `/c/<conversationID>`;
- accepted composer selectors only;
- same-response SSE filter/parser preserves b65 grammar;
- Repository owns response generation/snapshot/phase/tool lifecycle;
- terminal requests existing authoritative Sync;
- active selected response disables unsafe Sync/Reload;
- validation-only Send trigger; b38 message geometry unchanged.

Exact iPhone/iOS17 Runtime **failed this first production bridge**. Two generations reproduced:

`composer_ready x2 -> submit_result=submitted x2 -> one send_observed -> send_transport_error`

No `coveredExecutor.sendResponse` occurred and Native response text stayed empty. The user verified the official ChatGPT app already contained the assistant reply, proving protected Send reached the service while Native lost the same-response request before receiving the HTTP Response object.

Source correlation established a local Swift->JS duplicate-submit race: `pendingSend` remained available until later `send_observed`, allowing repeated composer-ready callbacks to schedule the same asynchronous JS submit twice. This is not evidence of a new Web selector/SSE rule. Detailed Runtime record: `docs/project/runtime-evidence/DEV-send-stream-b66-runtime.md`.

### Exact b67 — current correction Candidate

b67 changes only the operation gate:

1. `CoveredWebSendExecutor.isBusy` now follows existing `activeEvents != nil` lifetime.
2. `pendingSend` is consumed immediately before issuing the one JS submit evaluation.
3. Duplicate composer-ready callbacks can no longer schedule the same pending operation again.
4. `activeEvents` keeps executor busy through terminal/failure, so consuming `pendingSend` does not open a second user-Send window.
5. Web selectors, protected route, parser/filter grammar, Repository owner, Web Rule Lab and diagnostics privacy are unchanged.
6. No retry, resend, timer, polling, watchdog, fallback or compatibility shim was added.

Exact Root change is `+2/-1`; assembly audit showed only Root + b67 Xcode/workflow identity files changed relative to the b66 Runtime checkpoint.

Identity:

- Candidate `DEV-send-stream-0.1.0-b67`, `0.1.0 (67)`;
- exact product/config source `52ab38f16fe914ef8316bb1dc712b77c2c87a271`; tree `dcd492d142bf0035208b8466ff02b6ae7209193c`;
- Push `33338865423 / 99330666394` — success;
- PR `33338868896 / 99330678769` — success;
- Push Artifact `9739891865`;
- ZIP `sha256:7e41508c76556466ab180009a30f36b5c12cbc731197d4213387698ed54d78c2`;
- IPA `sha256:3712dec92cddfe64e84fc797e1506d83231cd878633b932b9acf0e7381795497`;
- Release / source marker `52ab38f16fe9` / iOS14 / `[1,2]` / arm64.

Evidence ladder: **Code / diff audit / Push CI / PR CI / Artifact / package identity passed; Runtime pending; Stable-Frozen No.**

### Current Phase 9 human Runtime gate

Install exact b67 on the primary iPhone/iOS17 device, clear diagnostics and run **one clean existing-conversation validation Send**.

Required first-pass evidence:

- only one `submit_result=submitted` for the response generation;
- only one real `sendObserved`;
- `coveredExecutor.sendResponse` appears with HTTP200 `text/event-stream`;
- Native moves beyond preparing into actual response updates with nonzero reasoning/final where service emits them;
- no immediate `send_transport_error`;
- real terminal occurs;
- terminal authoritative Sync reconciles without an automatic resend/poll loop.

Export diagnostics after terminal. One clean run is sufficient initially. Do not add A/B/background/new-chat complexity to this first retry gate.

**Do not allocate b68 before exact b67 Runtime yields a concrete next need.** If b67 still fails with only one submit, discard the duplicate-submit diagnosis as sufficient explanation and investigate the new exact evidence rather than adding retries.

### Shortest remaining Phase 9 sequence after b67 gate

1. accept/fix existing-conversation production Repository-owned Send/stream;
2. new-chat first Send and pending->authoritative handoff only if actual timing requires it;
3. exact server Stop evidence + response-scoped Stop implementation;
4. A/B hidden-response ownership + follow-tail/history intent;
5. Sync/Reload active-response safety + b38 geometry/round/time/Copy regression;
6. final daily-chat Runtime matrix, target-main sync, Stable/merge decision.

### Official-like response lifecycle target

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次正在思考/思考流 -> reasoning_ended -> 自动折叠思考 -> 完整最终回答`.

Tool phases remain optional and must follow actual service events. General Markdown/code/table/link/citation rendering remains future `DEV-message-rendering`.

### Background ordering

Background resilience remains P0 but follows accepted production response ownership. b45 positive short-background evidence remains valid; b66's post-failure memory warning is not a background-completion acceptance test. 5/15-minute, WebContent termination, network transitions and battery/thermal remain later Runtime gates.

## Future serialized `DEV-composer-parity`

After current Send/Stream lifecycle acceptance, implement final official-like Composer hierarchy: bounded multiline auto-growth/full-screen editor, keyboard/layout behavior, per-conversation drafts, photo/video/file staging/preview, mode/reasoning controls, final Send/Stop button presentation. Do not move Send/response authority out of `ConversationRepository`.

## Phase 10 — `DEV-attachments`

High priority but Send-boundary dependent. Preserve iOS17 requirements; do not use private WebKit or DOM/file-input injection. Native photo+video upload/handoff needs separate current evidence.

## Phase 11 — `DEV-message-rendering`

Implement native Markdown/code/table/link/citation presentation only from authoritative user-visible content; never expose hidden reasoning/tool/system content.

## Later phases

Conversation-list preview, Markdown export, long-conversation profiling beyond accepted b38 geometry, download manager, pagination, production background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement and later advanced capabilities remain isolated Works.

## Current next action

Hand exact b67 Artifact `9739891865` / IPA SHA `3712dec92cddfe64e84fc797e1506d83231cd878633b932b9acf0e7381795497` to the user for the focused one-submit existing-conversation Runtime gate. Keep PR #29 open/unmerged and do not allocate b68 before that evidence.