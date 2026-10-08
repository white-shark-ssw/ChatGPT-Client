# DEV-send-stream b54 Runtime Evidence

Date: 2026-08-30

## Candidate identity

- Candidate: `DEV-send-stream-0.1.0-b54`
- Version/build: `0.1.0 (54)`
- Exact product/config source: `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`
- Artifact: `9727636043`
- Artifact ZIP digest: `sha256:28d07c99634a1b4f917561e95cf04a4e95666106985cb03bca09798b0dc7065c`
- IPA SHA-256: `d4b85cffe4db499252d0bc9a2c7c8ea582acf2b88f3d28eeb60e366ee471153b`
- Package: Release / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64

User-exported diagnostics metadata matched exactly:

- `appVersion=0.1.0`
- `buildNumber=54`
- `candidate=DEV-send-stream-0.1.0-b54`
- `sourceCommit=6a6903c7ad56`
- `buildConfiguration=Release`
- device class iPhone / iOS 17.0

## Runtime transport result

One Native submission reached the official protected Send path and returned HTTP200 `text/event-stream`; terminal was true.

Aggregate stream metrics:

- `frameCount=73`
- `nativeDeltaCount=22`
- `nativeCharacters=412`
- `removedTextPatchCount=22`
- `removedTextCharacters=412`
- `explicitTextPatchCount=7`
- `exactTopLevelTextPatchCount=4`
- `rootNonExactTextPatchCount=0`
- `nestedTextPatchCount=3`
- `contextualValueStringCount=15`
- `contextualValueStringCharacters=312`
- `inactiveValueStringCount=0`
- `inactiveValueStringCharacters=0`
- `continuationResetWhileActiveCount=4`
- `firstInactiveValueContext=none`
- `titleGenerationWhileContinuationCount=0`
- `structureSignatureCount=32`
- `structureSignatureOverflowCount=13`
- `webMessageNodes=2`
- `webAssistantTextCharacters=0`
- terminal `true`

The user did not provide a new explicit b54 visual completeness classification with this export, so this evidence record does not upgrade or replace the prior b53 visual result. b54 was intentionally behavior-neutral.

## Tool invocation/result structure

b54 materially completed the tool-structure half of its objective.

Observed assistant invocation messages:

- `assistant / code / in_progress` with recipient `api_tool.list_resources`, content fields `content_type,language,response_format_name,text`.
- multiple `assistant / code / finished_successfully` messages with recipient `api_tool.call_tool`.
- completed assistant-code metadata includes `is_complete:true`, `connector_tool_payload`, `tool_icons`, and normal model/reasoning bookkeeping keys.

Observed tool-result messages:

- `tool / text / finished_successfully`, author name `api_tool`, recipient `all`, content `parts` array.
- `tool / code / finished_successfully`, author name `api_tool.call_tool`, recipient `all`, direct `text` content.
- `tool / multimodal_text / finished_successfully`, author name `api_tool.call_tool`, recipient `all`, `parts` arrays.
- tool-result metadata includes `invoked_plugin` / `invoked_resource` where present.

This is direct protocol evidence that the stream contains distinct assistant tool invocation messages and subsequent tool result messages, and that they can be paired using role/content type plus recipient/author metadata.

It does **not** establish that raw tool arguments, raw tool output, or every internal tool node is user-visible. Production presentation still requires an explicitly user-visible summary/status boundary.

## Reasoning structure

Observed:

- `assistant / thoughts / finished_successfully`
- recipient `all`
- content keys `content_type,source_analysis_msg_id,thoughts`
- `thoughts` is an array with one object item whose keys are `chunks,content,finished,summary`
- metadata boolean `can_save:false`
- metadata enum `reasoning_status:is_reasoning`
- metadata enum `tool_summary_type:github`
- structural metadata keys also include `inline_cot_expandable_content`, `tool_icons`, `reasoning_start_time`, `reasoning_title`-related state and normal turn/model bookkeeping.

Safety/presentation interpretation:

- raw `thoughts`, `chunks`, internal reasoning content and hidden chain-of-thought are not authorized presentation data;
- the presence of `summary`, `inline_cot_expandable_content`, `reasoning_status` and `tool_summary_type` suggests that user-visible summary state may be represented within this message family, but b54 did not log enough nested shape to prove the exact authorized text field;
- b54 therefore does not authorize rendering raw `thoughts` content.

## Observer-cap defect

The intended b54 target also included `assistant:reasoning_recap`. b53 had directly observed that content type on the preceding exact Runtime.

In b54, the generic unique-structure set reached its hard cap of 32, and `structureSignatureOverflowCount=13`. The `assistant:thoughts` event was the 32nd emitted unique signature. Later unique structures were suppressed by the observer.

Therefore the absence of a logged b54 `reasoning_recap` cannot be interpreted as protocol absence. The current diagnostic cannot distinguish:

1. this turn emitted no recap; or
2. recap occurred after the generic structure set saturated and was dropped from diagnostics.

This is a diagnostic-observer limitation, not evidence for parser broadening or a production UI decision.

## Accepted b54 conclusion

- Protected Send / SSE / terminal: Runtime confirmed for this turn.
- Existing b54 response text behavior: not changed by b54; no new visual classification supplied.
- Tool invocation/result grammar: materially identified.
- Reasoning special-message grammar: partially identified (`thoughts` shape and presentation-related metadata), but exact authorized reasoning-recap/display container remains unresolved.
- b54 objective: **partial Runtime pass** because the shared 32-signature cap prevented deterministic completion of the reasoning-recap gate.

## Next evidence action

The smallest justified correction is a new Candidate that preserves all b54 Send/filter/output rules and all existing generic structure diagnostics, but gives only `assistant:reasoning_recap`, `assistant:thoughts`, `assistant:code`, and `tool:*` a separate small bounded dedupe channel. That channel must remain text-free and must report its own count/overflow metrics.

No reasoning UI, tool UI, hidden-thought extraction, retry, timer, fallback, watchdog, or production-ownership change is justified by b54 alone.
