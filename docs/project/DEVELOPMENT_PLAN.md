# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-31 through exact b64 Runtime and exact b65 Code/CI/Artifact/package verification._

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client without replacing accepted native ownership merely to accommodate private Web behavior. Current real source, exact CI/Artifact evidence, real-device evidence and latest explicit requirements outrank stale plan wording.

Core rules: one authority per state domain; no speculative retry/fallback/timer/watchdog/duplicate state; distinguish Code / CI / Artifact / Runtime / Stable; optimize only evidenced bottlenecks; private protocol behavior must be measured rather than guessed. b48-b65 remain isolated diagnostic exceptions and do not silently alter production hidden/shadow-Web restrictions.

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
- b57-b59 established Native reasoning/final split and exact service-marked thinking-preamble inclusion.
- b60 passed the tested thinking/segmentation gate and exact result-parent association.
- b61 exposed generic-textarea false readiness; b62 removed only that exact fallback and passed the focused verified-composer normal path.
- b63 captured bounded expandable-detail structure evidence. Same-run Runtime plus official-Web expanded-detail evidence authorized one minimal GitHub mapping: invocation connector payload -> visible tool input; exact parent-paired GitHub result `message.content` -> visible tool output.
- b64 implemented that mapping. Exact iPhone/iOS17 Runtime passed real protected Send, reasoning/final completeness, exact-parent row completion and detail expand/collapse; only output formatting/density was rejected.
- b65 is the presentation-only correction: tool row opens to independently collapsed `工具输入` / `工具输出`; output outer JSON is decoded and displayed hierarchically so nested strings are shown as actual text rather than a second-layer escape wall.

### Exact b64 Runtime — lifecycle/detail mapping passed, formatting partial

User export `ChatGPTClient-Diagnostics-20260830-174329.json` matched exact build64/source on iPhone/iOS17.0.

Observed Send path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 SSE -> terminal`.

Terminal evidence included reasoning `27/440`, final `215/6716`, exact reasoning end `1`, parent matches `30`, unmatched `5`, missing `0`, Native tool presentations/completion updates `30/30`, detail-capable rows `26`, and multiple successful expand/collapse events. The user reported no apparent truncation.

Classification: **Runtime partial-pass — verified composer / protected Send / reasoning-final / exact-parent GitHub detail lifecycle passed; current detail formatting/density rejected only.**

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b64-runtime.md`.

### Exact b65 — structured detail presentation Candidate

Identity:

- Candidate `DEV-send-stream-0.1.0-b65`, `0.1.0 (65)`.
- Exact product/config source `44138db766d00e62cfda7f20182f6d20f1ec3352`; tree `fb02dfa7512e9c8428c4b0e9b7184a56d602f688`.
- Push `33328232044 / 99302071335` — success.
- PR `33328233842 / 99302076369` — success.
- Push Artifact `9736876465`; PR Artifact `9736874445`.
- Push ZIP `sha256:d9a52ecb0cd7d5131e22fc399bc5db0d573a9de3e5d80838f3a8d2b3164ceb7a`.
- IPA SHA `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`.
- Package Release / `0.1.0 (65)` / source marker `44138db766d0` / iOS14 / `[1,2]` / arm64.
- b65 permanently reserved; Runtime pending.

b65 implementation boundary:

1. preserve b64 verified composer, protected Send, SSE text grammar, reasoning/final split, exact `reasoning_ended`, transient invocation map, exact result `parent_id` pairing and GitHub-only detail authorization;
2. preserve diagnostics privacy: no raw prompt/answer/reasoning/tool input/output/IDs/auth/proof in exported logs;
3. keep the tool row as the first disclosure;
4. after row expansion, show `工具输入` and `工具输出` as independent collapsed second-level disclosures;
5. input remains readable pretty JSON;
6. output decodes b64's outer `message.content` JSON and recursively presents dictionaries/arrays; actual string values are shown as actual text, and complete JSON object/array strings may be decoded one structural layer;
7. no arbitrary character truncation, retry, polling, timer, watchdog, fallback, compatibility shim, second response owner or production repository mutation.

Evidence ladder: **Code written / detached diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**

### Current Phase 9 human Runtime gate

Install exact b65 on the primary iPhone/iOS17 device, clear diagnostics, and run one GitHub/repository request that naturally creates multiple tool rows. Verify:

- verified composer becomes ready and `submitted` is followed by real `sendObserved`;
- HTTP200 SSE reaches terminal;
- reasoning/final still appear complete;
- exact-parent completed GitHub tool rows still expand/collapse;
- opening one row initially shows only collapsed second-level `工具输入` and `工具输出`;
- each child expands/collapses independently;
- output is readable hierarchy/text without b64's escaped `\"` / `\\` wall;
- no expected paired tool/result content is silently truncated.

Export diagnostics after terminal. **Do not allocate b66 before this exact b65 Runtime evidence.** If b65 passes, close the formatting defect without another Candidate. If it fails, b66 may address only the smallest evidenced product defect.

### Official-like response lifecycle target

The eventual Native interaction remains:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考过程 -> 只突出完整最终回答`.

Tool phases remain optional and must follow actual service events. No-tool answers must never fabricate a tool stage. This reasoning/tool/phase-transition interaction remains within `DEV-send-stream`; general Markdown/code/table/link/citation rendering of ordinary message bodies remains later `DEV-message-rendering`.

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

Hand exact b65 Artifact `9736876465` / IPA SHA `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16` to the user for the focused iPhone/iOS17 structured-detail Runtime gate. Keep PR #29 open/unmerged and do not allocate b66 unless b65 Runtime supplies a concrete need.
