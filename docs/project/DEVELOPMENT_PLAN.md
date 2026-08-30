# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b59 Runtime._

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client without replacing accepted native ownership merely to accommodate private Web behavior. Current real source, exact CI/Artifact evidence, real-device evidence and latest explicit requirements outrank stale plan wording.

Core rules: one authority per state domain; no speculative retry/fallback/timer/watchdog/duplicate state; distinguish Code / CI / Artifact / Runtime / Stable; optimize only evidenced bottlenecks; private protocol behavior must be measured rather than guessed. b48-b59 remain isolated diagnostic exceptions and do not silently alter production hidden/shadow-Web restrictions.

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
- b57 split already-accepted visible text into Native reasoning/final around exact reasoning end.
- b58 passed bounded compact tool-activity display but side-by-side Web evidence proved the remaining leading gap exactly matched a service-marked thinking-preamble string.

### b59 — thinking preamble completeness Runtime passed

Exact b59:

- Candidate `DEV-send-stream-0.1.0-b59`, `0.1.0 (59)`.
- Exact source `138c09a5d11121945bc45f1d866c449aa0f7611e`; tree `c28eb92616e494a15aa2e370e2fd5150986b2452`.
- Push `33305680998 / 99241706079` — success.
- PR `33305683021 / 99241711695` — success.
- Artifact `9730376958`; ZIP `sha256:4c13fc5941786b6db1797d72b8938f763cdaec2b76b8d15998fd4d6f235763ef`.
- IPA SHA `5758cf40b287c7d9c5cef2f13163d5c8239834ee617468692c56b4bdb0349252`.
- Package Release / `0.1.0 (59)` / source marker `138c09a5d111` / iOS14 / `[1,2]` / arm64.

Exact iPhone/iOS17 Runtime `ChatGPTClient-Diagnostics-20260830-103539.json`:

- HTTP200 SSE / terminal true / frameCount 83;
- Native reasoning `12 deltas / 207 chars`;
- final answer `18 / 357 chars`;
- exact reasoning-end marker 1 / fallback false;
- thinking preambles `2 / 13 chars`;
- tool invocations/results `12/13`; Native compact tool presentations 12.

User confirmed reasoning, tool activity and final answer were complete; the b58 leading truncation did not reproduce. b59 therefore passes the exact preamble/text-completeness correction.

The same run also supplies the next evidence:

- two separate service-marked thinking preambles occur before the one reasoning-end marker, proving reasoning can resume after tools within the same turn;
- a safe explicit `metadata.reasoning_status=is_reasoning` appears after tool activity and before the second preamble; its `assistant:thoughts` body remains non-presentational;
- Native currently flattens separate reasoning segments into one `UITextView`, so official paragraph/segment boundaries are visually lost;
- 12 accepted invocation messages vs 13 tool results proves adjacency/count-only result pairing is unsafe;
- official Web exposes expandable tool request/result cards; b59 intentionally exposes only bounded activity titles/fallbacks.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b59-runtime.md`.

### Official-like response lifecycle target

The user explicitly requires this eventual Native interaction, as close to official behavior as verified service data permits:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开用户可见的调用详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考过程 -> 只突出完整最终回答`.

This entire reasoning/tool/phase-transition interaction remains within `DEV-send-stream`; it is not a separate feature Work. General Markdown/code/table/link/citation rendering of ordinary message bodies remains later `DEV-message-rendering`.

### Next bounded candidate gate

Before exposing tool request/result detail, one candidate should first:

1. preserve b59 text grammar and correct Native-only paragraph separation at later exact thinking-preamble segment starts without changing service character metrics;
2. show initial response-active/no-visible-text state as deterministic `正在思考`, never timer-based;
3. observe explicit later service `reasoning_status=is_reasoning` and distinguish it from lifecycle-derived initial waiting;
4. compare invocation/result service identities only in memory and export match/missing counts, never raw IDs, to establish the exact association rule;
5. collect bounded structural shape/character-count evidence for the official user-visible tool card fields, without logging raw tool bodies or connector payloads.

Only after exact association/user-visible-field evidence may a later Candidate implement expandable tool request/result detail. Do not guess pairing from chronology.

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

Synchronize durable evidence through b59, then use the smallest next Candidate for reasoning segment breaks, deterministic thinking-state presentation and privacy-safe tool invocation/result association diagnostics. Do not expose detailed tool bodies until that Runtime gate proves exact pairing and user-visible fields.
