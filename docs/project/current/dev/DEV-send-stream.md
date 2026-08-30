# DEV-send-stream

## Status

**Active — exact b54 Runtime materially proves the tool invocation/result structure but does not complete the reasoning-recap evidence gate because the shared 32-signature observer saturated before later unique structures. b54 remains behavior-neutral; final text parser/output was not changed. The next smallest justified correction is b55: give only special reasoning/tool structures their own bounded dedupe channel so they cannot be displaced by ordinary protocol signatures. No reasoning/tool UI is authorized yet. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged at the b54 Runtime light guard.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; unchanged.
- **Other Active development checkpoints**: none known for this Work guard.
- **Stable native predecessor**: b38.
- **Stable/Frozen Send**: No.

## Exact b53

- Candidate `DEV-send-stream-0.1.0-b53`, `0.1.0 (53)`.
- Exact product/config source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`.
- Artifact `9726996570`; IPA SHA `d5eee722ea01dc2c1b419a803574aec8ad2199299a3d0bbb51de4bae574f25dc`.
- Runtime: visible reasoning beginning still truncated, final answer complete, no Native tool-call presentation.
- Runtime structurally identified `assistant:reasoning_recap`, `assistant:thoughts`, `assistant:code`, and `tool:*`.
- Durable record: `docs/project/runtime-evidence/DEV-send-stream-b53-runtime.md`.

## Exact b54 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b54`
- Version/build: `0.1.0 (54)`
- Exact product/config source: `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`
- Push Run / Job: `33296672444 / 99217423647` — success
- PR Run / Job: `33296674388 / 99217428590` — success
- Artifact: `9727636043`
- ZIP digest: `sha256:28d07c99634a1b4f917561e95cf04a4e95666106985cb03bca09798b0dc7065c`
- IPA SHA-256: `d4b85cffe4db499252d0bc9a2c7c8ea582acf2b88f3d28eeb60e366ee471153b`
- Package: Release / `0.1.0 (54)` / source marker `6a6903c7ad56` / iOS14 / UIDeviceFamily `[1,2]` / arm64.
- b54 is permanently reserved.

## Exact b54 Runtime — 2026-08-30

User supplied diagnostics `ChatGPTClient-Diagnostics-20260830-073425.json`. Metadata exactly matches b54: build 54, Candidate b54, source `6a6903c7ad56`, Release, iPhone/iOS17.0.

One Native submission reached official protected Send HTTP200 `text/event-stream` and terminal true.

Aggregate metrics:

- `frameCount=73`;
- `nativeDeltaCount=22`, `nativeCharacters=412`;
- `explicitTextPatchCount=7`, `exactTopLevelTextPatchCount=4`, `nestedTextPatchCount=3`, `rootNonExactTextPatchCount=0`;
- `contextualValueStringCount=15`, `contextualValueStringCharacters=312`;
- `inactiveValueStringCount=0`, `firstInactiveValueContext=none`;
- `continuationResetWhileActiveCount=4`;
- `structureSignatureCount=32`, **overflow=13**;
- terminal true.

### Tool structure accepted from b54

b54 directly captured concrete call/result pairs:

- assistant `code` messages target recipients such as `api_tool.list_resources` / `api_tool.call_tool`;
- completed assistant `code` carries `is_complete:true` and metadata keys including `connector_tool_payload` and `tool_icons`;
- tool results identify author names such as `api_tool` / `api_tool.call_tool`, `recipient=all`, and content types `text`, `code`, or `multimodal_text`;
- tool result metadata includes `invoked_plugin` / `invoked_resource` where present;
- tool payload content containers are now structurally known (`parts` arrays for text/multimodal results; `text` for code results).

This proves the service stream contains explicit tool invocation and tool-result messages that can be paired structurally. It still does **not** prove that every internal tool/result node should be shown verbatim or that raw tool payloads are user-visible.

### Reasoning structure accepted / remaining gap

b54 captured `assistant:thoughts / finished_successfully` with:

- content keys `content_type,source_analysis_msg_id,thoughts`;
- `thoughts` = one object item with keys `chunks,content,finished,summary`;
- metadata `can_save:false`;
- metadata includes `reasoning_status:is_reasoning`, `tool_summary_type:github`, plus structural keys `inline_cot_expandable_content`, `tool_icons`, `reasoning_start_time`, etc.

Do not expose raw `thoughts`, `chunks`, or internal reasoning content. These structures may contain user-visible summary metadata, but b54 does not yet prove which nested field is the authorized display surface.

The intended `assistant:reasoning_recap` special structure was **not observed in the emitted diagnostics**. Because the generic observer was already at its hard 32-signature limit and reports 13 overflowed unique signatures, b54 cannot distinguish “no recap in this turn” from “recap occurred after saturation and was suppressed by the observer”. Therefore b54 does not complete the recap content-container gate.

Durable record to create: `docs/project/runtime-evidence/DEV-send-stream-b54-runtime.md`.

## b55 allocation decision

Repository search found no existing `DEV-send-stream-0.1.0-b55`; b39-b54 are already reserved. b55 is justified only for the observer-cap defect exposed by exact b54 Runtime.

Planned identity:

- Candidate `DEV-send-stream-0.1.0-b55`
- Version/build `0.1.0 (55)`

### Exact b55 scope

Preserve every b54 Send/filter/output behavior and all existing generic 32-signature diagnostics.

Only change structure observation:

1. classify a summary as special when it is `assistant:reasoning_recap`, `assistant:thoughts`, `assistant:code`, or `tool:*`;
2. maintain a separate bounded `specialStructureSeen` set (small fixed cap) for these messages;
3. emit a special structure signature even if the generic 32-signature set is already full;
4. keep ordinary signatures under the existing 32 cap;
5. add special-signature count/overflow metrics so the next Runtime can prove coverage;
6. do not log any new raw text, IDs, tool payload values, prompts, answers, reasoning content, auth/proof values or headers.

No reasoning collapse/expand, tool-call presentation, haptics or production ownership change in b55.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b55 are diagnostic exceptions only. TD-024/TD-025 remain unchanged. No diagnostic result alone promotes hidden/shadow Web to production.

Only explicitly user-visible service reasoning/status/tool information may be shown. Hidden chain-of-thought/internal tool/system data remains prohibited.

## Batch I recovery point

Verified before b55 writes:

- feature head before this checkpoint: `d4a74cd8104f24f0efaa34c5e0c4d3ae3d3ca458`;
- `main` still `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- PR #29 open / mergeable / not merged and head matched the feature branch;
- exact b54 diagnostics identity matched the emitted Artifact;
- no b55 identity found.

Planned batches:

1. write exact b54 Runtime evidence;
2. atomically emit b55 Swift + build/Candidate + workflow Artifact identity;
3. verify b55 Push/PR CI and Artifact/package identity;
4. synchronize PR and durable docs;
5. hand exact b55 IPA for one focused reasoning/tool turn.

Recovery rule: if interrupted, re-read this checkpoint and actual branch/PR state; continue only missing deterministic writes. Never alter/rebuild b54. Once any b55 Artifact exists, b55 is permanently reserved.

## Next exact action

Create `DEV-send-stream-b54-runtime.md`, then implement the b55 separate special-structure observer without changing response text behavior. Continue through exact CI/Artifact/package verification before asking for another Runtime test.
