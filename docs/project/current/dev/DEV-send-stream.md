# DEV-send-stream

## Status

**Active — exact b57 Runtime passed reasoning→final phase separation on iPhone/iOS17: reasoning streamed only in `思考过程`, final answer stayed separate, and the prior leading truncation did not reproduce. The same turn contained multiple explicit assistant-code→tool-result chains while b57 showed no tool activity. Exact b58 product/config source is now emitted and preserves b57 text/reasoning behavior while adding only a bounded diagnostic Native tool-activity region. b58 CI/Artifact/Runtime are pending. TD-024/TD-025/TD-028 and production response ownership remain unchanged; PR #29 remains evidence-only.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Current target main: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Other Active development checkpoints: none
- Stable native predecessor: b38
- Stable/Frozen Send: No

## b57 Runtime — accepted

Exact identity: `DEV-send-stream-0.1.0-b57` / `0.1.0 (57)` / source `7074b1f85a0f239a5fd615f52196e1e28145523c` / Artifact `9729360247` / IPA SHA `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`.

User export `ChatGPTClient-Diagnostics-20260830-090524.json` matched exact b57 / Release / iPhone / iOS17.0. One official protected Send returned HTTP200 SSE and terminal true.

Key evidence:

- Native total `16 deltas / 348 chars`
- reasoning `4 / 61 chars`
- final answer `12 / 287 chars`
- exact `reasoningEndMarkerCount=1`
- fallback promotion false
- user: reasoning only in `思考过程`, final answer separate, no visible leading truncation
- first before-marker `assistant:text:in_progress` had `parts:1:string:chars6` and `is_thinking_preamble_message:true`; b57 did not consume it, so no prefix parser broadening is justified
- multiple completed assistant `code` invocations with non-`all` recipients followed by `tool` results; Native showed none

Durable record: `docs/project/runtime-evidence/DEV-send-stream-b57-runtime.md`.

Classification: **b57 Runtime passed for reasoning→final split.** Tool activity presentation remains missing.

## Exact b58 product/config identity

- Candidate: `DEV-send-stream-0.1.0-b58`
- Version/build: `0.1.0 (58)`
- Exact product/config source: `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`
- Product tree: `ddb396aa942c48222e69671eaf3610127d9797e9`
- Swift blob: `a1f67ace0415b898d8f8d62f22c141e9a8092006`
- Xcode config blob: `cbec2615008d71e68f76cd34af7ca71c00103547`
- Workflow blob: `c7d5150648dfc42da3440b848d348db05f908bef`
- CI: Pending
- Artifact/package: Pending
- Runtime/manual: Pending

Atomic assembly: tooling branch `tooling/b58-assembly-20260830` was created from checkpoint parent `3e3b5284c94d6c0dbdea818e6cc7144bb7980734`. Compare showed exactly three Candidate files changed: `.github/workflows/ios-foundation.yml`, `ChatGPTClient.xcodeproj/project.pbxproj`, and `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`. Final tree was attached directly to the checkpoint parent as exact product commit `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`; feature ref moved once. Tooling commits are not Candidate authority.

## Exact b58 scope

1. Preserve all b57 protected-Send, SSE text acceptance, reasoning-end split/collapse, and terminal fallback behavior.
2. Detect only completed assistant-code invocations with role `assistant`, `content_type=code`, `status=finished_successfully`, non-empty recipient other than `all`, and `metadata.is_complete=true`.
3. Deduplicate only in memory by service message ID; never log/export the ID.
4. Show one compact Native tool activity line per unique invocation in a separate `工具调用` region.
5. If service `metadata.reasoning_title` is a non-empty string, use it only for transient UI. Diagnostics log only title character count, never title text.
6. Without a title, use local generic `工具调用`; do not derive a tool name from raw arguments/results.
7. Completed tool-result messages contribute aggregate counts only; result body is never displayed and no guessed invocation/result pairing is introduced.
8. Terminal metrics add invocation/result/title-presence counts and Native tool-presentation count.
9. Never expose `assistant:thoughts`, raw tool args/results, connector payload, auth/proof/header values, or message/conversation IDs.

## Batch L recovery point

Completed:

- b57 Runtime classified and durable evidence written
- checkpoint and Resume guard updated
- unique b58/build58 allocated
- b58 three-file assembly completed and conflict-checked
- exact b58 product source `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb` emitted atomically and feature ref moved

Pending:

- verify Push + PR CI for exact b58 source
- verify exact Artifact, ZIP digest, IPA SHA and built package identity
- update PR #29 and durable docs through b57 Runtime / b58 Artifact
- hand exact b58 IPA to user for one focused tool-active Runtime turn

Do not modify `ConversationRepository`, auth ownership, Stable b38 modules, resume transport, attachments or production architecture in this batch. b59 must not be allocated until exact b58 Runtime supplies concrete evidence.

## Next exact action

Verify CI for exact source `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`; if both normal Push and PR checks pass, verify the b58 Artifact/package and then synchronize durable docs/PR before handoff.
