# Project State

_Last updated: 2026-08-30 through exact b60 Runtime and exact b61 Code / CI / Artifact / package verification. Phase 9 remains Active; b61 Runtime/manual is pending._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / target

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Current target `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; final target synchronization is still required before any future merge.

Current exact test Candidate is **`DEV-send-stream-0.1.0-b61` / `0.1.0 (61)`**, exact product/config source `2386872af03e0684eee8deca87f636dc265114ec`, Artifact `9732514781`, IPA SHA `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`. Code / Push CI / PR CI / Artifact / package identity passed; Runtime/manual pending.

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- The separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- TD-024/TD-025/TD-028 remain unchanged. Full existing-conversation mobile-Web rendering is not an accepted daily-chat dependency after the b47 long-answer composer failure.
- b48-b61 are **diagnostic exceptions only**. Their success does not approve hidden/shadow Web as production architecture and does not transfer production response ownership away from `ConversationRepository`.
- `ConversationRepository` remains sole native production conversation/list/detail/recovery/future accepted response authority; `AuthSessionStore` remains auth/account authority; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate; no second Send may be created merely to obtain a stream.

## Current Send/stream evidence progression

- b45 Runtime Confirmed official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` -> HTTP200 SSE; b46/b47 duplicated Native Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.
- b48-b51 established Native composer -> official protected Send and compact incremental text grammar, including fresh-new-chat continuation across `title_generation`.
- b52-b56 isolated reasoning/tool grammar and exact `reasoning_ended`, while keeping `assistant:thoughts` non-presentational.
- b57-b59 established Native reasoning/final split and exact service-marked thinking-preamble inclusion without the earlier leading gap.
- b60 preserved later reasoning paragraph boundaries, presented event-driven `正在思考`, and proved the exact invocation→result parent association for the tested traffic.

## Exact b60 Runtime — accepted bounded gate

Exact b60 identity: Candidate `DEV-send-stream-0.1.0-b60`, source `8ca445f3c17233ac36832f46417a8e53a138499e`, Artifact `9731477362`, IPA SHA `7cae323231b6b9d1aa837b03506450daa99f457fd8b4025deedb368dc008cd42`.

User export `ChatGPTClient-Diagnostics-20260830-122917.json` matched Release / build60 / source `8ca445f3c172` / iPhone iOS17.0. Two consecutive tool-active turns returned HTTP200 SSE and terminal true.

- Turn 1: reasoning `14 / 209 chars`, final `17 / 462`, preambles `2 / 10`, Native thinking presentations 3, service/Native segment breaks `1/1`, exact reasoning-end 1, fallback false. Invocation identities 15, completed invocation presentations 13, results 15; parent present/matched/unmatched/missing `15/15/0/0`; author-name==recipient 14/15.
- Turn 2: reasoning `17 / 221 chars`, final `54 / 922`, preambles `2 / 32`, Native thinking presentations 3, service/Native segment breaks `1/1`, exact reasoning-end 1, fallback false. Identities/completed/results `5/5/5`; parent present/matched/unmatched/missing `5/5/0/0`; author-name==recipient 3/5.
- Direct user result: both turns showed `正在思考` before reasoning, streamed reasoning with visible line/paragraph separation, and no obvious truncation.

Accepted tested association rule: a completed tool result belongs to the invocation whose exact service message ID equals that result metadata `parent_id`, when both are observed in the same response stream. Raw IDs remain transient/unlogged. Adjacency/count/tool-name pairing is rejected; author-name/recipient equality is not authoritative.

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b60-runtime.md`.

Classification: **b60 Runtime pass for tested thinking-state / segmentation / text completeness / parent-association scope.**

## Exact b61 Candidate / validation

- Candidate `DEV-send-stream-0.1.0-b61`, `0.1.0 (61)`.
- Exact product/config source `2386872af03e0684eee8deca87f636dc265114ec`; tree `a687500c88cffabf3a8496652fd5e0b633264836`.
- Push Run / Job `33312809061 / 99260781131` — success.
- PR Run / Job `33312811455 / 99260788483` — success.
- Artifact `9732514781`; ZIP `sha256:66976ecb53ac8fc2b116dcbce753fdf05499cea88dd29f0ae4223ab8baa5bf28`.
- IPA SHA `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`.
- Package: Release / `0.1.0 (61)` / Candidate b61 / source `2386872af03e` / iOS14 / `[1,2]` / arm64.
- b61 is permanently reserved after Artifact emission.

b61 preserves b60 Send/text/reasoning/thinking behavior. It assigns transient local tool slots, uses only the accepted `parent_id` match to update the correct Native tool row from `调用中` to `已完成`, and records bounded shape descriptors for candidate detail fields such as `connector_tool_payload`, `inline_cot_expandable_content`, `reasoning_titles`, `tool_icons`, `invoked_plugin`, and `invoked_resource`. It does **not** display or log those values/bodies.

Evidence ladder: **Code written / Push CI passed / PR CI passed / Artifact produced / package identity independently verified; Runtime/manual pending; Stable/Frozen No.**

## Next evidence gate

Run exact b61 once on iPhone/iOS17 with a naturally tool-active repository/GitHub question. Observe whether all visible tool rows transition to `已完成` without duplicate/missing rows, and whether thinking/reasoning/final text remains complete. Export diagnostics after terminal.

Only after b61 Runtime identifies a bounded field that can be proven user-visible may a later Candidate implement expandable tool details. Do not expose arbitrary raw tool bodies, `connector_tool_payload` values, `assistant:thoughts`, prompt/reasoning/final bodies in diagnostics, or allocate b62 by guess.

## Remaining Unknown / Unverified

Accepted production incremental-response ownership, exact cross-tool user-visible detail schema, Native first/exclusive resume, existing-conversation pre-React history virtualization, full 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified where not explicitly tested. CI/Artifact success is never Runtime proof.
