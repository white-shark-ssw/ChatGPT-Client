# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-31 through accepted b67 production transport Runtime, b69 daily-chat defect evidence, and exact b70 Code/scope/Push+PR CI/Artifact/package verification._

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

### b67 accepted transport predecessor / b69 daily-chat evidence

Exact b67 accepted the production existing-conversation TD-029 transport gate: one local Send -> one protected official Send -> HTTP200 `text/event-stream` -> Repository reasoning/tool/final updates -> terminal -> one authoritative reconcile. This remains the transport predecessor and b70 does not replace its route/selectors/challenge/SSE grammar.

b69 then implemented one Repository-owned chronological response timeline. Exact iPhone/iOS17 Runtime retained real Send success but exposed six concrete daily-chat defects: covered-Web keyboard pop, missing immediate user row, excessive reasoning/tool spacing/no divider, lost b65 GitHub nested details, missing tool icons, and sticky Native reads around temporary 403.

### Exact b70 — current correction Candidate

b70 makes only the evidence-backed corrections:

1. suppress covered-Web virtual keyboard during temporary programmatic composer focus and blur after injection;
2. keep the actual trimmed prompt only in the current Repository live-response snapshot and render exactly one optimistic user row before the assistant row;
3. restore b65 exact-parent GitHub `工具输入` / `工具输出` mapping inside the ordered timeline, with bounded local icons and compact deterministic spacing/divider;
4. preserve last verified account identity across exact probe 403, retain 401 unavailable semantics, and discard stale copied transient read transport on list/detail 401/403 while visibly failing the current operation;
5. next explicit/normal read probes current WebKit credentials; no automatic replay/retry/poll/timer/watchdog;
6. returning from user-opened login may perform one explicit list refresh;
7. `ConversationRepository`, `AuthSessionStore`, default WebKit auth store, b38 geometry, and accepted b67 one-Send transport remain their existing authorities.

Identity/evidence:

- Candidate `DEV-send-stream-0.1.0-b70`, `0.1.0 (70)`;
- exact product/config source `fb83be9163838f78abfa47903e67f27b6f66ec52`, direct parent clean checkpoint `5c379b3d994b28cb0ba5a3c793e4efa193a003a1`;
- assembly `33373254877 / 99428895016`: exact five-file scope audit, `git diff --check`, Xcode16.4 iOS Simulator compile passed;
- Push `33377045570 / 99440767755` and PR `33377049590 / 99440781050` — success;
- Artifact `9752289536`; ZIP `sha256:bdf09b246ff259ee80d46acfad675713c1a0b51aee3b44f7ea9f0a7e67eafde0`;
- IPA `sha256:8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a`;
- independently unpacked package `0.1.0 (70)` / Candidate b70 / source marker `fb83be916383` / iOS14 / arm64.

Evidence ladder: **Code / exact scope/static / Simulator compile / Push CI / PR CI / Artifact / package identity passed; Runtime pending; Stable-Frozen No.**

### Current Phase 9 human Runtime gate

Install exact b70 Artifact `9752289536` on the primary iPhone/iOS17 device and verify Build70/Candidate/source marker. Clear diagnostics, then test normal daily chat and one transient-read-auth recovery opportunity if reproducible.

Required evidence: no covered-Web keyboard pop; exactly one immediate optimistic user row with no terminal duplication; chronological reasoning/tool order and in-place tool completion; restored GitHub nested input/output, bounded icons, compact spacing and final divider; active response survives navigation; a transient Native 403 does not become sticky and can recover on the next explicit/normal read from current WebKit credentials without automatic replay/retry; hidden thoughts stay excluded; b38 geometry and b67 one-Send transport do not regress. Export diagnostics after terminal/recovery.

**Do not allocate b71 before exact b70 Runtime yields a concrete next need.** CI/Artifact/package success is not Runtime proof.

### Shortest remaining Phase 9 sequence after b70 gate

1. accept/fix this daily-chat existing-conversation parity/auth-lifecycle gate from exact Runtime evidence;
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

Hand exact b70 Artifact `9752289536` / IPA SHA `8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a` to the user for the focused b70 real-device daily-chat/auth-lifecycle gate. Keep PR #29 open/unmerged. Do not allocate b71 or begin unrelated Composer/attachments/Stop/background work before that Runtime evidence.
