# Project State

_Last updated: 2026-08-30 through exact b57 Runtime and exact b58 Code/CI/Artifact/package verification; b58 Runtime remains pending._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / target

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Current target `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c` at the latest guard; final target synchronization is still required before any future merge.

The exact current testable Candidate is **`DEV-send-stream-0.1.0-b58` / `0.1.0 (58)`**, exact product/config source `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`, Artifact `9729864129`, IPA SHA `0d5988caf21300bfb29e81b3f1f8bbf6eaa69a84f09efeda601e6d6f9b7b8875`.

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- The separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- TD-024/TD-025/TD-028 remain unchanged. Full existing-conversation mobile-Web rendering is not an accepted daily-chat dependency after the b47 long-answer composer failure.
- b48-b58 are **diagnostic exceptions only**. Their success does not approve hidden/shadow Web as production architecture and does not transfer production response ownership away from `ConversationRepository`.
- `ConversationRepository` remains sole native production conversation/list/detail/recovery/future accepted response authority; `AuthSessionStore` remains auth/account authority; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate; no second Send may be created merely to obtain a stream.

## Current Send/stream evidence progression

- b45 Runtime Confirmed official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` -> HTTP200 SSE; b46/b47 Native duplicated Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.
- b48-b50 established Native composer -> official protected Send and compact incremental text grammar; b51 fixed fresh-new-chat continuation across `title_generation`.
- b52 kept final answer complete while visible reasoning beginning truncated.
- b53 identified `assistant:reasoning_recap`, separate `assistant:thoughts`, assistant-code and tool message classes.
- b54 identified assistant invocation -> tool-result grammar but generic observation saturated; b55 special observation passed and captured explicit `reasoning_ended` / `collapse` structure.
- b56 corrected the recap interpretation: recap text was only a short status/description in the tested turn, not the real visible reasoning body. The exact recap event remained useful as a reasoning-end marker.

## Exact b57 Runtime — phase separation passed

Exact b57 identity: Candidate `DEV-send-stream-0.1.0-b57`, source `7074b1f85a0f239a5fd615f52196e1e28145523c`, Artifact `9729360247`, IPA SHA `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`.

User export `ChatGPTClient-Diagnostics-20260830-090524.json` matched Release / build57 / source `7074b1f85a0f` / iPhone iOS17.0. One protected Send returned HTTP200 SSE and terminal true.

- Native total `16 deltas / 348 chars`
- reasoning `4 / 61 chars`
- final answer `12 / 287 chars`
- exact reasoning-end marker `1`
- fallback promotion false
- assistant text before/after marker `1/1`
- phase structures `2/overflow0`; special structures `8/overflow0`

Direct user result: visible reasoning streamed only in independent `思考过程`, final answer remained separate, and the previous leading truncation did not reproduce. The first before-marker assistant text message had `parts:1:string:chars6` and `is_thinking_preamble_message:true`; b57 did not consume that message body, so there is no evidence-backed reason to broaden the parser.

The same turn exposed multiple completed assistant-code invocations followed by completed tool results while Native displayed no tool activity. Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b57-runtime.md`.

Classification: **b57 Runtime passed for reasoning -> final phase separation.** Missing-prefix extraction is not currently justified.

## Exact b58 Candidate — bounded tool activity

- Candidate: `DEV-send-stream-0.1.0-b58`
- Version/build: `0.1.0 (58)`
- Exact product/config source: `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`
- Product tree: `ddb396aa942c48222e69671eaf3610127d9797e9`
- Push Run / Job: `33303998650 / 99237187408` — success
- PR Run / Job: `33304001877 / 99237195550` — success
- Artifact: `9729864129`
- ZIP digest: `sha256:3a907e6bb5f1cbd7f57d54b01e64805196247e612e2de961dac99d92df2060ac`
- IPA SHA: `0d5988caf21300bfb29e81b3f1f8bbf6eaa69a84f09efeda601e6d6f9b7b8875`
- Package: Release / `0.1.0 (58)` / Candidate b58 / source marker `d9dbf208625e` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64.

b58 preserves b57 protected-Send, text acceptance, reasoning/final split, collapse behavior and terminal fallback. It adds only a separate compact Native `工具调用` region for exact completed assistant-code invocations with non-empty non-`all` recipient and `metadata.is_complete=true`.

A non-empty service `metadata.reasoning_title` may be used only for transient display; diagnostics record title character count, never title text. Without a title, the local generic `工具调用` label is shown. Completed tool results contribute aggregate counts only. Raw `content.text`, `content.parts`, arguments, results, connector payloads, IDs and `assistant:thoughts` remain excluded.

New aggregate signals: `toolInvocationCount`, `toolInvocationWithTitleCount`, `toolResultCount`, `toolResultWithTitleCount`, `nativeToolPresentationCount`.

Classification: **b58 Code/CI/Artifact/package passed; Runtime pending.** b58 is permanently reserved.

## Current Runtime gate

One focused b58 iPhone/iOS17 turn that naturally invokes tools:

1. confirm b57 reasoning/final separation remains intact and no leading truncation appears;
2. confirm a separate `工具调用` region appears during real tool activity;
3. note whether entries use coherent service-provided titles or generic `工具调用` fallback;
4. confirm no raw tool args/results/connector payloads or `assistant:thoughts` are shown;
5. wait for terminal and export diagnostics.

Do not allocate b59 until exact b58 Runtime supplies concrete next evidence. Phase 9 Stable/Frozen Send: No.

## Remaining Unknown / Unverified

Native first/exclusive resume, accepted production incremental-response ownership, exact production tool-card semantics/result presentation, existing-conversation pre-React history virtualization, full 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified where not explicitly tested. CI/Artifact success is never Runtime proof.
