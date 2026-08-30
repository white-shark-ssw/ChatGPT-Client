# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b57 Runtime and exact b58 Code/CI/Artifact/package verification._

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client without replacing accepted native ownership merely to accommodate private Web behavior. Current real source, exact CI/Artifact evidence, real-device evidence and latest explicit requirements outrank stale plan wording.

Core rules: one authority per state domain; no speculative retry/fallback/timer/watchdog/duplicate state; distinguish Code / CI / Artifact / Runtime / Stable; optimize only evidenced bottlenecks; private protocol behavior must be measured rather than guessed. b48-b58 remain isolated diagnostic exceptions and do not silently alter production hidden/shadow-Web restrictions.

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
- b52 kept final answer complete while visible reasoning beginning was truncated.
- b53-b55 identified reasoning/tool message grammar and exact `reasoning_ended` semantics while keeping raw `assistant:thoughts` non-presentational.
- b56 corrected the recap-body assumption: recap text itself was only a short status/description in the tested turn; the recap event remains the explicit reasoning-end marker.

### b57 — reasoning/final separation Runtime passed

Exact b57: Candidate `DEV-send-stream-0.1.0-b57`, source `7074b1f85a0f239a5fd615f52196e1e28145523c`, Artifact `9729360247`, IPA SHA `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`.

Exact iPhone/iOS17 Runtime:

- HTTP200 SSE / terminal true;
- Native `16 deltas / 348 chars`;
- reasoning `4 / 61 chars`, answer `12 / 287 chars`;
- exact reasoning-end marker 1, fallback false;
- user confirmed reasoning streamed only in `思考过程`, final answer stayed separate, and the previous leading truncation did not reproduce.

The first before-marker assistant-text message carried `parts:1:string:chars6` and `is_thinking_preamble_message:true`, but b57 did not consume that body and the output was visually complete. Therefore no missing-prefix parser expansion is justified.

The same turn exposed multiple completed assistant-code invocations followed by completed tool results, while b57 showed no tool activity. Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b57-runtime.md`.

### b58 — current Runtime Candidate: bounded tool activity

Exact identity:

- Candidate `DEV-send-stream-0.1.0-b58`, `0.1.0 (58)`.
- Exact source `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`; tree `ddb396aa942c48222e69671eaf3610127d9797e9`.
- Push `33303998650 / 99237187408` — success.
- PR `33304001877 / 99237195550` — success.
- Artifact `9729864129`; ZIP `sha256:3a907e6bb5f1cbd7f57d54b01e64805196247e612e2de961dac99d92df2060ac`.
- IPA SHA `0d5988caf21300bfb29e81b3f1f8bbf6eaa69a84f09efeda601e6d6f9b7b8875`.
- Package Release / `0.1.0 (58)` / source marker `d9dbf208625e` / iOS14 / `[1,2]` / arm64.

b58 preserves every b57 protected-Send/text/reasoning rule. It adds one compact diagnostic `工具调用` region for exact completed assistant-code invocations with `metadata.is_complete=true` and non-empty non-`all` recipient.

Presentation contract:

- one line per unique invocation, deduped in memory by service message ID; ID never logged/exported;
- use non-empty service `metadata.reasoning_title` only as transient display; diagnostics record only title length;
- otherwise show local generic `工具调用`;
- completed tool results are count/evidence only, never body presentation;
- no raw args/results, connector payloads, internal thoughts, IDs, auth/proof/header values.

b58 Code/CI/Artifact/package passed; Runtime pending. b58 is permanently reserved.

### Current b58 human Runtime gate

One focused reasoning/tool-active turn is sufficient:

1. verify b57 reasoning/final separation still works and leading truncation does not regress;
2. verify `工具调用` appears during real tool activity;
3. note whether displayed entries are coherent service titles or generic fallback;
4. confirm no raw tool arguments/results/connector payloads or `assistant:thoughts` appear;
5. wait for terminal and export diagnostics.

Decision signals: `toolInvocationCount`, `toolInvocationWithTitleCount`, `toolResultCount`, `toolResultWithTitleCount`, `nativeToolPresentationCount`, plus the b57 reasoning/answer metrics.

Do not allocate b59 before exact b58 Runtime. Do not merge PR #29 or promote diagnostic Web Send ownership to production from CI/Artifact success alone.

### Background ordering

Background resilience remains P0 but production implementation follows eventual response ownership. b45/b49 are positive short-background evidence only; 5/15-minute, process termination, network transitions and battery/thermal remain separate Runtime gates.

## Phase 10 — `DEV-attachments`

High priority but Send-boundary dependent. Preserve iOS17 requirements; do not use private WebKit or DOM/file-input injection. Native photo+video upload/handoff needs separate current evidence.

## Phase 11 — `DEV-message-rendering`

Implement native Markdown/code/table/link/citation presentation only from authoritative user-visible content; never expose hidden reasoning/tool/system content.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted list-cache ownership; do not issue one Detail per row to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current native visible branch; never scrape hybrid Web DOM.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve Stable b38 deterministic geometry unless new Runtime evidence justifies change.

## Later phases

Isolated Work IDs for download manager, pagination, production background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement, and later advanced capabilities.

## Current next action

**Human Runtime Gate on exact b58.** Validate one tool-active reasoning turn, bounded tool activity presentation, b57 reasoning/final regression, privacy boundary and terminal diagnostics. b59 remains unallocated.
