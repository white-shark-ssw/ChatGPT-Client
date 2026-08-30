# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b63 Code/CI/Artifact/package verification._

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client without replacing accepted native ownership merely to accommodate private Web behavior. Current real source, exact CI/Artifact evidence, real-device evidence and latest explicit requirements outrank stale plan wording.

Core rules: one authority per state domain; no speculative retry/fallback/timer/watchdog/duplicate state; distinguish Code / CI / Artifact / Runtime / Stable; optimize only evidenced bottlenecks; private protocol behavior must be measured rather than guessed. b48-b63 remain isolated diagnostic exceptions and do not silently alter production hidden/shadow-Web restrictions.

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
- b52-b56 identified reasoning/tool message grammar, separated raw internal `assistant:thoughts`, and established exact `reasoning_ended` semantics.
- b57-b59 established Native reasoning/final split and exact service-marked thinking-preamble inclusion without the earlier leading gap.
- b60 passed the tested thinking/segmentation gate and exact result-parent association.
- b61 successful tool-active Runtime passed transient parent-paired row completion, but a separate cold/new-page run exposed generic-textarea false readiness before protected Send.
- b62 removed only that exact generic-textarea fallback and passed the tested verified-composer normal path while retaining reasoning/final and exact-parent tool lifecycle.
- b63 preserves b62 behavior and adds only bounded structure evidence for the unresolved expandable-detail schema.

### b62 — focused Runtime passed

Exact b62 user Runtime export matched Candidate/source and showed:

`ready=false / none -> ready=true / prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 SSE -> thinking/reasoning/tools/final -> terminal`.

Response evidence included reasoning `34/497`, exact reasoning end `1`, final `93/2878`, tool result parent matches `20/20`, Native tool presentations/completion updates `20/20`; user reported the tested round looked normal.

Classification: **focused Runtime pass for the tested verified-composer Send-entry + reasoning/final + exact-parent tool lifecycle scope.** It does not prove every future official-page state is race-free.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

### b63 — bounded expandable-detail structure diagnostic

Exact b63 identity:

- Candidate `DEV-send-stream-0.1.0-b63`, `0.1.0 (63)`.
- Exact product/config source `0c2e2b870e51c363c7734182d49618c438839cc2`; tree `cae7f27e2800fe48f8d492bfd364c91755935c67`.
- Push `33321982009 / 99285436158` — success.
- PR `33321983658 / 99285440962` — success.
- Artifact `9735145598`; ZIP `sha256:645cba67a91387f79d386931b5d0f4ead2502408b15c7f339013505e3f0ec7da`.
- IPA SHA `b347d1e41ca5a4e1355a9cc713574ea96247e11918ccfb1f5ff621a0f9f6ff36`.
- Package Release / `0.1.0 (63)` / source marker `0c2e2b870e51` / iOS14 / `[1,2]` / arm64.
- b63 permanently reserved; Runtime pending.

b63 is justified by exact b62 shape evidence rather than a guessed presentation mapping:

- string-shaped `metadata.connector_tool_payload` repeatedly appears on completed assistant tool-invocation messages;
- object-shaped `metadata.inline_cot_expandable_content` can appear on completed assistant `thoughts` structures and expose `source_message_ids` references;
- existing exact parent association already owns one response-local transient invocation-ID Map.

b63 records only:

1. `connectorToolPayloadJSONShape`: capped JSON parse/top-level key/type/direct string-or-array length fingerprint; no values or nested bodies;
2. aggregate inline-expandable message/source-reference counts and matches against existing response-local invocation/tool-activity identities;
3. existing b62 exact-parent, reasoning/final, composer and terminal metrics unchanged.

b63 does **not** display expandable Native request/result bodies. Raw connector/tool payload values, service IDs, nested bodies and raw `assistant:thoughts` remain non-presentational.

Evidence ladder: **Code written / diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**

### Official-like response lifecycle target

The eventual Native interaction remains:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考过程 -> 只突出完整最终回答`.

Tool phases remain optional and must follow actual service events. No-tool answers must never fabricate a tool stage.

This entire reasoning/tool/phase-transition interaction remains within `DEV-send-stream`; it is not a separate feature Work. General Markdown/code/table/link/citation rendering of ordinary message bodies remains later `DEV-message-rendering`.

### Current Phase 9 human Runtime gate

Install exact b63 on the primary iPhone/iOS17 device and run one focused tool-active response. The test must:

- verify exact build63/Candidate/source marker;
- clear diagnostics before the run;
- use Native composer and wait for real protected Send + terminal;
- verify reasoning/final still appear complete and Native tool rows complete;
- open the same response in the visible official Web surface and, if the official UI offers tool-detail expansion, capture at least one expanded representative row;
- export diagnostics after terminal.

Interpret `connectorToolPayloadJSONShape`, inline-expandable aggregate source-reference metrics, existing exact-parent counts and the same-run official-Web screenshot together. A Web screenshot is the higher-priority presentation reference. Do not infer a user-visible body from field names alone.

**Do not allocate b64 before exact b63 Runtime evidence.** If the same-run evidence proves one safe minimal user-visible mapping, b64 may implement only that mapping. If it rejects or fails to resolve the mapping, use the smallest next evidence action instead of broadening payload capture.

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

Hand exact b63 Artifact `9735145598` to the user for the focused iPhone/iOS17 expandable-detail structure Runtime gate. Keep PR #29 open/unmerged. Do not allocate b64 or implement Native expandable bodies until same-run b63 evidence justifies the exact minimum mapping.
