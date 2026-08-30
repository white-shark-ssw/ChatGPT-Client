# Project State

_Last updated: 2026-08-30 through exact b59 Runtime. b59 text/preamble completeness passed; official-equivalent ordered reasoning/tool presentation remains Active._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / target

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Current target `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; final target synchronization is still required before any future merge.

The exact current tested Candidate is **`DEV-send-stream-0.1.0-b59` / `0.1.0 (59)`**, exact product/config source `138c09a5d11121945bc45f1d866c449aa0f7611e`, Artifact `9730376958`, IPA SHA `5758cf40b287c7d9c5cef2f13163d5c8239834ee617468692c56b4bdb0349252`.

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- The separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- TD-024/TD-025/TD-028 remain unchanged. Full existing-conversation mobile-Web rendering is not an accepted daily-chat dependency after the b47 long-answer composer failure.
- b48-b59 are **diagnostic exceptions only**. Their success does not approve hidden/shadow Web as production architecture and does not transfer production response ownership away from `ConversationRepository`.
- `ConversationRepository` remains sole native production conversation/list/detail/recovery/future accepted response authority; `AuthSessionStore` remains auth/account authority; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate; no second Send may be created merely to obtain a stream.

## Current Send/stream evidence progression

- b45 Runtime Confirmed official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` -> HTTP200 SSE; b46/b47 Native duplicated Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.
- b48-b50 established Native composer -> official protected Send and compact incremental text grammar; b51 fixed fresh-new-chat continuation across `title_generation`.
- b52-b56 isolated reasoning/tool grammar and established exact completed `reasoning_recap` with `reasoning_status=reasoning_ended` / `reasoning_recap_type=collapse` as the reasoning-end marker while keeping `assistant:thoughts` non-presentational.
- b57 proved already-accepted text can be split around `reasoning_ended` into Native reasoning vs final answer.
- b58 passed bounded compact tool-activity presentation but reproduced a leading reasoning gap exactly matching one service-marked `is_thinking_preamble_message` string part.
- b59 consumed only that exact service-marked preamble path and now proves the service may emit **multiple** thinking preambles within one reasoning phase.

## Exact b59 Runtime

Exact identity: Candidate `DEV-send-stream-0.1.0-b59`, source `138c09a5d11121945bc45f1d866c449aa0f7611e`, Artifact `9730376958`, ZIP `sha256:4c13fc5941786b6db1797d72b8938f763cdaec2b76b8d15998fd4d6f235763ef`, IPA SHA `5758cf40b287c7d9c5cef2f13163d5c8239834ee617468692c56b4bdb0349252`.

User export `ChatGPTClient-Diagnostics-20260830-103539.json` matched Release / build59 / source `138c09a5d111` / iPhone iOS17.0. Protected Send returned HTTP200 SSE, `frameCount=83`, terminal true.

- Native total `30 deltas / 564 chars`
- reasoning `12 / 207 chars`
- final answer `18 / 357 chars`
- exact reasoning-end marker 1; fallback false
- thinking preambles `2 / 13 chars`
- tool invocations 12; tool results 13; Native compact tool presentations 12

Direct user result: reasoning, compact tool activity and final answer all appeared complete; the previous leading truncation did not reproduce.

New defect/requirement: Native reasoning does not preserve official visible segment/paragraph breaks because separate reasoning messages are flattened into one text view. Official Web also exposes expandable tool request/result details while b59 intentionally does not. The user explicitly wants the eventual response interaction to follow the official sequence:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.

The same b59 traffic contains an explicit safe `reasoning_status=is_reasoning` signal after tool activity followed by the second thinking preamble, so return-to-reasoning state is now evidenced without presenting `assistant:thoughts` body.

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b59-runtime.md`.

Classification: **b59 Runtime passes the tested reasoning-preamble/text/final completeness correction. Phase 9 remains Active for ordered official-like presentation, exact tool-detail association/field semantics and eventual production response ownership.**

## Next evidence gate

A next Candidate may:

1. fix Native-only paragraph separation at later exact thinking-preamble segment boundaries without changing service character metrics;
2. represent initial waiting as response-lifecycle `正在思考` without timers and observe explicit later service `reasoning_status=is_reasoning` transitions;
3. add privacy-safe in-memory invocation/result association diagnostics because 12 invocations vs 13 results proves adjacency pairing is unsafe;
4. collect only bounded structural evidence for which fields map to the official expandable user-visible tool request/reply card.

Do not expose arbitrary raw tool bodies, `connector_tool_payload`, `assistant:thoughts`, prompt/reasoning/final bodies in diagnostics, or allocate a later detailed-card implementation before exact pairing/field evidence.

## Remaining Unknown / Unverified

Accepted production incremental-response ownership, exact initial service-side reasoning-start signal, exact cross-tool user-visible detail schema and pairing, Native first/exclusive resume, existing-conversation pre-React history virtualization, full 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified where not explicitly tested. CI/Artifact success is never Runtime proof.
