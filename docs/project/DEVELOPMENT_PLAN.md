# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b61 Runtime classification and b62 Code / CI / Artifact / package verification._

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client without replacing accepted native ownership merely to accommodate private Web behavior. Current real source, exact CI/Artifact evidence, real-device evidence and latest explicit requirements outrank stale plan wording.

Core rules: one authority per state domain; no speculative retry/fallback/timer/watchdog/duplicate state; distinguish Code / CI / Artifact / Runtime / Stable; optimize only evidenced bottlenecks; private protocol behavior must be measured rather than guessed. b48-b62 remain isolated diagnostic exceptions and do not silently alter production hidden/shadow-Web restrictions.

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

## Phase 9 — `DEV-send-stream` — Active diagnostic architecture experiment

### Durable Send boundary

- b42 proves ChatGPT-account protected Send requires browser anti-abuse challenge output; pure-native/transient-auth account Send remains blocked.
- Separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by account-safety policy.
- TD-024 is a visible-Web security permission only; TD-025 rejects b44 full-page hybrid form; TD-028 records the b47 long-answer Web-composer ceiling.
- Full existing-conversation Web rendering is not an accepted daily-chat production dependency.
- `ConversationRepository` remains future accepted production response owner; diagnostic Web transport must not become a second production repository.

### Evidence progression

- b45 Runtime Confirmed official no-resend resume; b46/b47 duplicated Native Cookie+Bearer-only resume rejected.
- b48-b51 established Native composer -> official protected Send and complete compact response text, including fresh-new-chat title-generation continuation.
- b52-b56 identified reasoning/tool message grammar, separated internal `assistant:thoughts`, and established exact `reasoning_ended` semantics.
- b57-b59 established Native reasoning/final split and exact service-marked thinking-preamble inclusion without the earlier leading gap.
- b60 passed the tested thinking/segmentation gate and exact result-parent association.
- b61 successful tool-active Runtime passed transient parent-paired row completion, but a separate cold/new-page run exposed generic-textarea false readiness before protected Send.
- b62 is the bounded Send-entry correction for that exact defect only.

### b61 — Runtime Partial

Exact b61:

- Candidate `DEV-send-stream-0.1.0-b61`, source `2386872af03e0684eee8deca87f636dc265114ec`.
- Artifact `9732514781`; IPA SHA `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`.

Two runs must remain separately represented:

1. **False-ready Send-entry defect** — `ChatGPTClient-Diagnostics-20260830-134827.json`: `new_or_other`, composer strategy `textarea`, `nativeSubmit`, `submitResult=submitted`, then no `sendObserved`, `sendResponse`, thinking or stream metrics. User observed no answer activity.
2. **Successful tool-active lifecycle** — `ChatGPTClient-Diagnostics-20260830-135112.json`: HTTP200 SSE / terminal; reasoning `10/251`, final `68/2363`; segment break `1/1`; exact reasoning-end 1; invocation identities/results `14/14`; result parent matches `14/14`, 0 unmatched/missing; Native tool presentations/completion updates `14/14`. User observed complete reasoning opening and rows moving `调用中 -> 已完成`.

Therefore b61 is **Runtime Partial**, not failed wholesale and not fully passed. Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b61-runtime.md`.

### b62 — verified-composer Send gate

Exact b62 identity:

- Candidate `DEV-send-stream-0.1.0-b62`, `0.1.0 (62)`.
- Exact product/config source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`; tree `d3432dfe2e32cddcfac7a5a56d7880772dc6989d`.
- Push `33316398081 / 99270535435` — success.
- PR `33316399402 / 99270539763` — success.
- Artifact `9733577825`; ZIP `sha256:d53ddb88c5d2092294592416e10e5a0a752cb7afb0bbe0a39c2c137d021082d0`.
- IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`.
- Package Release / `0.1.0 (62)` / source marker `e1b44f7ab6c4` / iOS14 / `[1,2]` / arm64.

b62 remains bounded:

1. remove only unqualified `textarea:not([disabled])` from composer authority;
2. accept only `#prompt-textarea` or explicit `[contenteditable="true"][role="textbox"]` as evidenced composer identities;
3. add no retry, wait timer, watchdog, polling or speculative fallback;
4. preserve b61 protected Send, text grammar, thinking preambles, event-driven `正在思考`, reasoning/final split, exact `reasoning_ended`, terminal fallback, parent-paired tool lifecycle and safe detail-shape diagnostics;
5. keep raw service IDs, tool request/result bodies, connector payload values and `assistant:thoughts` non-presentational.

Evidence ladder: **Code / Push CI / PR CI / Artifact / package Passed; Runtime/manual pending; Stable/Frozen No.**

### b62 Runtime standard

The exact b61 false-ready race is intermittent. **Do not require it to reproduce.** The focused Runtime gate is:

- after force-quit/cold launch, while no evidenced official composer exists, Native Send must stay not-ready/disabled; an unrelated generic textarea must not authorize Send;
- once Send becomes enabled and a prompt is submitted, a successful turn must reach the real protected-Send lifecycle (`sendObserved`, then HTTP200 SSE when service success occurs) rather than stopping at `submitResult=submitted`;
- the successful response must retain b61's accepted thinking/reasoning/final presentation and tool lifecycle, with no obvious opening/middle truncation and no obvious duplicate/missing tool rows;
- tool-active rows should visibly progress `调用中 -> 已完成` when matched results arrive;
- if a run ever again reports submitted but never `sendObserved`, export immediately; that is a concrete b62 rejection signal.

One focused cold-launch tool-active turn is sufficient for the primary gate. One additional cold launch is a useful confidence check but optional. Do not burn time indefinitely trying to reproduce a low-frequency page race.

### Official-like response lifecycle target

The eventual Native interaction remains:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考过程 -> 只突出完整最终回答`.

This entire reasoning/tool/phase-transition interaction remains within `DEV-send-stream`; it is not a separate feature Work. General Markdown/code/table/link/citation rendering of ordinary message bodies remains later `DEV-message-rendering`.

Expandable tool detail still requires exact evidence that a bounded field is intended for user-visible presentation. b61's shape diagnostics do not authorize raw connector/tool payloads.

### Background ordering

Background resilience remains P0 but production implementation follows eventual response ownership. b45/b49 are positive short-background evidence only; 5/15-minute, process termination, network transitions and battery/thermal remain separate Runtime gates.

## Phase 10 — `DEV-attachments`

High priority but Send-boundary dependent. Preserve iOS17 requirements; do not use private WebKit or DOM/file-input injection. Native photo+video upload/handoff needs separate current evidence.

## Phase 11 — `DEV-message-rendering`

Implement native Markdown/code/table/link/citation presentation only from authoritative user-visible content; never expose hidden reasoning/tool/system content. This phase does not own reasoning/tool lifecycle semantics already scoped to `DEV-send-stream`.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted list-cache ownership; do not issue one Detail per row to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current native visible branch; never scrape hybrid Web DOM.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve Stable b38 deterministic geometry unless new Runtime evidence justifies change.

## Later phases

Isolated Work IDs for download manager, pagination, production background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement, and later advanced capabilities.

## Current next action

Install exact b62 on the primary iPhone/iOS17 target. Force-quit, reopen `Native 输入 / Web Send`, observe that Send does not become usable merely because an unrelated page textarea exists, then run one naturally tool-active repository/GitHub turn after Send becomes enabled. Wait for terminal and export diagnostics. Optional: repeat one additional cold launch. Do not require reproduction of b61's rare false-ready race and do not allocate b63 until b62 Runtime is classified.
