# DEV-send-stream

## Status

**Active — exact b57 Runtime passes the reasoning→final phase-separation gate on the primary iPhone/iOS17 runtime. Visible reasoning streamed only in the Native `思考过程` region, final answer remained separate, and the previously reported leading reasoning truncation did not reproduce. Exact b57 also supplied concrete tool invocation/result evidence while Native still displayed no tool activity. The next smallest evidence-backed Candidate is b58: preserve b57 text/reasoning behavior and add a diagnostic-only compact tool-activity region for exact completed assistant-code invocations, without exposing raw arguments/results or `assistant:thoughts`. TD-024/TD-025/TD-028 and production response ownership remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence-only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c` at the latest light guard.
- **Current branch head / b58 assembly parent**: `d63a149f609a7c9b1fd9ebcdde44ecf2c3797f75` before this checkpoint refresh; the two immediately preceding temporary-file commits created and then removed a tooling marker and produced no lasting tree change.
- **Stable native predecessor**: b38.
- **Stable/Frozen Send**: No.
- Other Active development checkpoints: none.

## Exact b57 identity

- Candidate: `DEV-send-stream-0.1.0-b57`
- Version/build: `0.1.0 (57)`
- Exact product/config source: `7074b1f85a0f239a5fd615f52196e1e28145523c`
- Product tree: `c402ce522e244cf63aa44b80a6d165b84342104c`
- Push Run / Job: `33302357908 / 99232731468` — success
- PR Run / Job: `33302359351 / 99232735067` — success
- Artifact: `9729360247`
- Artifact ZIP digest: `sha256:ae5a5532e2c30624907e9a2d61966090df4b8cc9ffa57f1b5725db8b61a8d275`
- IPA SHA-256: `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`
- Package: Release / `0.1.0 (57)` / Candidate b57 / source `7074b1f85a0f` / iOS14 / `[1,2]` / arm64.
- b57 is permanently reserved.

## Exact b57 Runtime

User export `ChatGPTClient-Diagnostics-20260830-090524.json` exactly matched build 57 / Candidate b57 / source `7074b1f85a0f` / Release / iPhone / iOS17.0.

Direct user observation:

- reasoning streamed only inside `思考过程`;
- final answer no longer contained reasoning text;
- no visible leading truncation in this reproduction;
- tool calls still had no Native presentation.

Transport / metrics:

- official protected Send HTTP200 `text/event-stream`, terminal true;
- `frameCount=52`;
- Native total `16 deltas / 348 chars`;
- reasoning `4 deltas / 61 chars`;
- answer `12 deltas / 287 chars`;
- exact reasoning-end marker `1`;
- fallback promotion `false`;
- exact-root patches `3`, nested patches `4`, contextual values `9 / 189 chars`, inactive values `0`, resets `3`;
- ordinary assistant text messages `2`: one before marker and one after;
- phase-text structures `2 / overflow0`;
- special structures `8 / overflow0`;
- generic structures `32 / overflow1`.

First pre-reasoning-end `assistant:text:in_progress` had `content_type,parts`, `parts:1:string:chars6`, and `is_thinking_preamble_message:true`. b57 did not extract that six-character message body, yet the user saw no prefix defect. Therefore do not broaden the text parser from this run.

Durable Runtime record: `docs/project/runtime-evidence/DEV-send-stream-b57-runtime.md`.

Classification: **b57 Runtime passed for reasoning→final phase separation.** Leading-prefix extraction is not currently justified.

## Exact tool evidence from b57 Runtime

The same turn included multiple completed tool invocation/result structures:

- assistant `code` invocation with non-`all` recipients such as `api_tool.list_resources` and `api_tool.call_tool`;
- invocation messages had `status=finished_successfully`; observed calls had `metadata.is_complete=true`;
- several invocations/results exposed metadata keys `reasoning_title`, `reasoning_titles`, `tool_icons`, `connector_tool_payload`, `invoked_plugin`, `invoked_resource`;
- following tool results used role `tool`, `recipient=all`, with text/code/multimodal_text content types;
- Native b57 intentionally displayed none of this.

Raw `content.text`, `content.parts`, arguments, results, connector payloads, IDs and `assistant:thoughts` remain prohibited presentation/log data.

## b58 evidence-backed scope

b58 may be allocated because exact b57 Runtime supplied the required next evidence.

The change must remain diagnostic-only and minimal:

1. Preserve b57 protected-Send construction, text acceptance, reasoning-end split, reasoning collapse/expand and terminal fallback unchanged.
2. Detect only exact completed assistant-code messages where role=`assistant`, content type=`code`, status=`finished_successfully`, recipient is a non-empty string other than `all`, and metadata `is_complete === true`.
3. Deduplicate only in-memory by service message ID; never export/log that ID.
4. For each unique invocation, post one Native tool-activity event.
5. If `metadata.reasoning_title` is a non-empty string, bridge it only for transient display. Diagnostics record only title presence/character count, never title text.
6. If no service title exists, display only local generic `工具调用`; do not invent a tool name from raw arguments/results.
7. Add a distinct compact `工具调用` Native region; tool activity must not enter reasoning text or final-answer text.
8. Observe completed tool result messages only for bounded aggregate counts; do not display their body and do not guess invocation/result pairing.
9. Add terminal aggregate counts for invocation/result/title presence.
10. Do not expose `assistant:thoughts`, raw tool args/results, connector payload, auth/proof/header values or message/conversation IDs.

## Batch L recovery point

Confirmed complete:

1. b57 Runtime export identity and metrics classified;
2. user visual result accepted for reasoning/final split and no visible prefix truncation;
3. tool invocation/result structures classified;
4. `docs/project/runtime-evidence/DEV-send-stream-b57-runtime.md` created at commit `91217066f8213eec30c0ebdee76c9fb0437ca741`;
5. Resume guard confirmed only one Active task, PR #29 open/mergeable/unmerged, `main@1ac202c...`, and exact b57 product source unchanged;
6. accidental temporary marker/copy files were both removed immediately; no temporary file remains and no product/config source changed.

Pending deterministic writes:

1. allocate unique b58 identity only after this checkpoint;
2. atomically assemble exactly three Candidate files: `NativeWebSendEngineProbe.swift`, Xcode build identity, workflow Artifact identity;
3. move feature ref once to the exact b58 product commit;
4. run/verify Push and PR CI;
5. verify Artifact, ZIP digest, IPA SHA and built package identity;
6. update PR #29 and durable project docs through b57 Runtime / b58 Artifact;
7. hand exact b58 IPA to the user for one focused tool-active Runtime turn.

Do not modify `ConversationRepository`, auth ownership, Stable b38 modules, resume transport, attachment code or production architecture in this batch.

## Next exact action

Allocate `DEV-send-stream-0.1.0-b58` / build 58 and assemble the narrow tool-activity presentation Candidate above. Any interruption must resume from real branch/PR/head state and perform only missing writes. b59 must not be allocated unless exact b58 Runtime supplies concrete evidence.
