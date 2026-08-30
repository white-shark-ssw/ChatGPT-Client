# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b60 Runtime and b61 Code / CI / Artifact / package verification._

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client without replacing accepted native ownership merely to accommodate private Web behavior. Current real source, exact CI/Artifact evidence, real-device evidence and latest explicit requirements outrank stale plan wording.

Core rules: one authority per state domain; no speculative retry/fallback/timer/watchdog/duplicate state; distinguish Code / CI / Artifact / Runtime / Stable; optimize only evidenced bottlenecks; private protocol behavior must be measured rather than guessed. b48-b61 remain isolated diagnostic exceptions and do not silently alter production hidden/shadow-Web restrictions.

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
- b60 Runtime passed the tested ordered presentation gate and established the exact parent association for tool results.

### b60 — thinking / segmentation / parent association Runtime passed

Exact b60:

- Candidate `DEV-send-stream-0.1.0-b60`, source `8ca445f3c17233ac36832f46417a8e53a138499e`.
- Artifact `9731477362`; IPA SHA `7cae323231b6b9d1aa837b03506450daa99f457fd8b4025deedb368dc008cd42`.
- Exact iPhone/iOS17 export: `ChatGPTClient-Diagnostics-20260830-122917.json`.

Two consecutive tool-active turns both returned HTTP200 SSE and terminal true. Each showed initial event-driven `正在思考`, visible reasoning streaming, one preserved Native paragraph break at the later thinking preamble, exact reasoning end, final answer and no obvious user-observed truncation.

Tool association evidence:

- Turn 1: 15 result `parent_id` values present; all 15 matched observed invocation IDs; 0 unmatched / 0 missing. Completed invocation presentations were only 13 while invocation identities/results were 15, proving presentation/count adjacency is insufficient.
- Turn 2: 5/5 parent matches; 0 unmatched / 0 missing.
- Author-name==invocation-recipient was 14/15 then 3/5, so it is not association authority.

Accepted tested rule: result metadata `parent_id` identifies the invocation service message ID inside the same response stream. Raw IDs remain transient/unlogged; adjacency/count/tool-name association is rejected.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b60-runtime.md`.

### Official-like response lifecycle target

The eventual Native interaction remains:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考过程 -> 只突出完整最终回答`.

This entire reasoning/tool/phase-transition interaction remains within `DEV-send-stream`; it is not a separate feature Work. General Markdown/code/table/link/citation rendering of ordinary message bodies remains later `DEV-message-rendering`.

### b61 — exact current Runtime gate

Exact b61 identity:

- Candidate `DEV-send-stream-0.1.0-b61`, `0.1.0 (61)`.
- Exact product/config source `2386872af03e0684eee8deca87f636dc265114ec`; tree `a687500c88cffabf3a8496652fd5e0b633264836`.
- Push `33312809061 / 99260781131` — success.
- PR `33312811455 / 99260788483` — success.
- Artifact `9732514781`; ZIP `sha256:66976ecb53ac8fc2b116dcbce753fdf05499cea88dd29f0ae4223ab8baa5bf28`.
- IPA SHA `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`.
- Package Release / `0.1.0 (61)` / source marker `2386872af03e` / iOS14 / `[1,2]` / arm64.

b61 must remain bounded:

1. preserve b60 protected Send, text grammar, thinking preambles, event-driven `正在思考`, reasoning/final split, exact `reasoning_ended`, terminal fallback and final answer behavior;
2. assign transient local slots to observed invocation identities and use only exact matched result `parent_id` to update the correct Native row to `已完成`;
3. never send/log raw service IDs to Native or diagnostics;
4. allow a matched result's already-authorized bounded `reasoning_title` to refine a generic tool label, but do not expose request/result body;
5. inspect only bounded **shape/type/count/direct-key/string-length** evidence for candidate fields such as `connector_tool_payload`, `inline_cot_expandable_content`, `reasoning_titles`, `tool_icons`, `invoked_plugin`, and `invoked_resource`;
6. keep candidate values/bodies, raw connector/tool payloads and `assistant:thoughts` non-presentational.

Evidence ladder: **Code / Push CI / PR CI / Artifact / package Passed; Runtime/manual pending; Stable/Frozen No.**

Only after exact b61 Runtime proves correct row lifecycle and identifies a bounded service field that is demonstrably user-visible may a later Candidate implement expandable tool details. Do not guess from field names alone.

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

Install exact b61 on the primary iPhone/iOS17 target and run one naturally tool-active repository/GitHub turn. Observe every visible tool row for `调用中 -> 已完成`, duplicate/missing rows, thinking/reasoning/final completeness, then export diagnostics after terminal. Do not allocate b62 until that exact Runtime evidence is classified.
