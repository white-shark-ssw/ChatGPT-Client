# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b62 focused Runtime classification._

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
- b62 removed only that exact generic-textarea fallback and now passes the tested verified-composer normal path.

### b62 — focused Runtime passed

Exact b62 identity:

- Candidate `DEV-send-stream-0.1.0-b62`, `0.1.0 (62)`.
- Exact product/config source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`; tree `d3432dfe2e32cddcfac7a5a56d7880772dc6989d`.
- Push `33316398081 / 99270535435` — success.
- PR `33316399402 / 99270539763` — success.
- Artifact `9733577825`; ZIP `sha256:d53ddb88c5d2092294592416e10e5a0a752cb7afb0bbe0a39c2c137d021082d0`.
- IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`.
- Package Release / `0.1.0 (62)` / source marker `e1b44f7ab6c4` / iOS14 / `[1,2]` / arm64.

Exact Runtime export `ChatGPTClient-Diagnostics-20260830-151146.json` matched b62 and showed the required cold-launch ordering:

`ready=false / none -> ready=true / prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 SSE -> thinking/reasoning/tools/final -> terminal`.

Response evidence:

- reasoning `34 deltas / 497 chars`;
- preambles `3 / 20 chars`;
- reasoning segment breaks `2`;
- reasoning-active signals `3`;
- Native thinking presentations `4`;
- exact reasoning end `1`, fallback false;
- final answer `93 deltas / 2878 chars`;
- result parent present/matched/unmatched/missing `20/20/0/0`;
- Native tool presentations/completion updates `20/20`.

User reported the tested round looked normal and screenshot evidence showed populated reasoning, completed tool rows and complete-looking final text.

Classification: **focused Runtime pass for the tested verified-composer Send-entry + reasoning/final + exact-parent tool lifecycle scope.** It does not prove every future official-page state is race-free.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

### Official-like response lifecycle target

The eventual Native interaction remains:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考过程 -> 只突出完整最终回答`.

Tool phases remain optional and must follow actual service events. No-tool answers must never fabricate a tool stage.

This entire reasoning/tool/phase-transition interaction remains within `DEV-send-stream`; it is not a separate feature Work. General Markdown/code/table/link/citation rendering of ordinary message bodies remains later `DEV-message-rendering`.

### Next Phase 9 evidence target — expandable tool detail

The nearest unresolved current target is official-like expandable tool detail. b62 safe shape diagnostics observed candidates including:

- string-shaped `connector_tool_payload`;
- bounded `reasoning_titles` and `tool_icons` arrays;
- object-shaped `invoked_resource` on tool results;
- `inline_cot_expandable_content` on one `assistant:thoughts` structure.

Current evidence authorizes **shape only**, not raw values/bodies. `assistant:thoughts`, raw connector/tool request/result bodies and arbitrary invoked-resource fields remain non-presentational.

**Do not allocate b63 by guess.** First correlate existing official-Web expanded-tool screenshots with b62 structural evidence. If the mapping remains unproven, the next Candidate may be a bounded diagnostic-only b63 focused on one exact unresolved field, after a fresh uniqueness/conflict guard. It must not broaden into raw payload exposure.

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

Persist b62 Runtime as the accepted tested gate, keep PR #29 open/unmerged, and inspect existing b62 safe shape evidence against previously captured official-Web expanded-tool screenshots. Do not allocate b63 unless that comparison yields one concrete evidence question or implementation boundary.
