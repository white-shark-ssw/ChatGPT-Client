# DEV-send-stream

## Status

**Active — exact b60 Runtime passes the tested thinking-state, reasoning-segmentation, text-completeness and invocation→result parent-association gate. Across two consecutive iPhone/iOS17 turns, initial/post-tool `正在思考` behavior and paragraph separation were visually correct with no obvious truncation. Exact result `parent_id` matched an observed invocation identity for 20/20 completed tool results; author-name/recipient equality was not reliable. Raw tool bodies and `assistant:thoughts` remain non-presentational. b61 is now available only for a bounded parent-paired tool lifecycle plus structure-only investigation of official user-visible detail fields. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged; PR #29 stays evidence-only / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Current target main verified: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Other Active development checkpoints: none
- Stable native predecessor: b38
- Stable/Frozen Send: No

## Exact b60 identity

- Candidate: `DEV-send-stream-0.1.0-b60`
- Version/build: `0.1.0 (60)`
- Exact product/config source: `8ca445f3c17233ac36832f46417a8e53a138499e`
- Product tree: `1f0b612cc233d4541336cc43177d8384ef5072bd`
- Push Run / Job: `33309296932 / 99251320370` — success
- PR Run / Job: `33309298759 / 99251325144` — success
- Artifact: `9731477362`
- ZIP digest: `sha256:167d32071f33639f1afe006aefd6b73900805f611f653ca24d908dfe1fdef17a`
- IPA SHA: `7cae323231b6b9d1aa837b03506450daa99f457fd8b4025deedb368dc008cd42`
- Package: Release / `0.1.0 (60)` / Candidate b60 / source `8ca445f3c172` / iOS14 / UIDeviceFamily `[1,2]` / arm64
- b60 permanently reserved.

## Exact b60 Runtime

User export `ChatGPTClient-Diagnostics-20260830-122917.json` exactly matches Release / build60 / Candidate b60 / source `8ca445f3c172` / iPhone / iOS17.0. Two consecutive tool-active turns were tested.

### Turn 1

- HTTP200 SSE / terminal true / frameCount 88
- Native reasoning `14 / 209 chars`; final `17 / 462 chars`
- thinking preambles `2 / 10 chars`
- service reasoning-active signals 2
- Native thinking presentations 3
- service / Native reasoning segment breaks `1 / 1`
- exact reasoning-end marker 1; fallback false; inactive value-string count 0
- completed invocation presentations 13; invocation identities 15
- tool results 15; parent present/matched/unmatched/missing = `15 / 15 / 0 / 0`
- author-name == invocation recipient only 14/15

### Turn 2

- HTTP200 SSE / terminal true / frameCount 101
- Native reasoning `17 / 221 chars`; final `54 / 922 chars`
- thinking preambles `2 / 32 chars`
- service reasoning-active signals 3
- Native thinking presentations 3
- service / Native reasoning segment breaks `1 / 1`
- exact reasoning-end marker 1; fallback false; inactive value-string count 0
- invocation identities / completed invocations / results = `5 / 5 / 5`
- parent present/matched/unmatched/missing = `5 / 5 / 0 / 0`
- author-name == invocation recipient only 3/5

Direct user result for both turns: Send后先出现 `正在思考`; then reasoning streamed; visible line/paragraph break present; no obvious truncation.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b60-runtime.md`.

Classification: **b60 Runtime pass for the tested presentation + parent association scope. Phase 9 remains Active because verified expandable tool-detail semantics and accepted production response ownership are pending.**

## Accepted parent-association rule

For the tested traffic, a completed tool result belongs to the invocation whose exact service message ID equals the result metadata `parent_id`.

- This rule is established only inside the response stream where both identities are observed.
- Raw IDs remain transient in Web diagnostic memory and must not be logged or persisted.
- Do not pair by adjacency, counts or author/tool name.
- Turn 1 proves completed-presentation count is not identity count: 13 presented invocations, 15 identities, 15 matched results.
- Author-name/recipient equality is only an optional structural signal, not the association authority.

## b61 bounded gate

Pre-allocation evidence:

- `main` remains `1ac202c...`;
- PR #29 remains the dedicated open/unmerged evidence PR;
- current dev checkpoint directory contains only `DEV-send-stream.md` plus README;
- commit/PR searches returned no b61 identity;
- build index currently ends at b60.

Therefore build/Candidate 61 is available. b61 may only:

1. preserve all b60 Send/text/reasoning/thinking/terminal behavior;
2. use the now-Runtime-proven `parent_id` association in transient diagnostic presentation so a tool result can update the correct invocation entry, without passing/logging raw service IDs to Native;
3. allow a paired result `reasoning_title` to refine a generic invocation label, because title presentation is already an accepted bounded user-visible field;
4. inspect only **shape/type/count/direct-key metadata** for already observed detail candidates such as `connector_tool_payload`, `reasoning_titles`, `tool_icons`, `invoked_plugin`, `invoked_resource`, and `inline_cot_expandable_content`;
5. never log/display the values or bodies of those candidates, never expose arbitrary tool result/request text, and never expose `assistant:thoughts` body;
6. avoid DOM scraping, timers, retries, fallback transports, production repository changes, auth/resume changes, attachments or unrelated UI refactors.

This b61 gate is diagnostic/presentation evidence only. It does **not** yet authorize expandable raw request/result detail.

## Batch O recovery point

Confirmed complete:

1. exact b60 Code / Push CI / PR CI / Artifact / package identity passed;
2. exact b60 two-turn Runtime accepted for thinking state, segment breaks and visible text completeness;
3. exact `parent_id` invocation→result association accepted for tested 20/20 results;
4. raw tool body and hidden thoughts remain prohibited;
5. runtime evidence file created;
6. b61 uniqueness guard passed; no b61 source or Artifact has been emitted yet at this checkpoint.

## Next exact action

Allocate exact `DEV-send-stream-0.1.0-b61` / build61 atomically from the current docs head. Keep b61 limited to parent-paired tool presentation state plus privacy-safe field-shape diagnostics. Verify diff, Push + PR CI, Artifact/package identity, then request one tool-active Runtime turn. Do not expose raw tool detail until b61 identifies a verified user-visible field boundary.
