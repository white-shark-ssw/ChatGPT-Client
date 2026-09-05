# DEV-send-stream b57 Runtime Evidence

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b57`
- Version/build: `0.1.0 (57)`
- Exact product/config source: `7074b1f85a0f239a5fd615f52196e1e28145523c`
- Artifact: `9729360247`
- IPA SHA-256: `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`
- Runtime export: `ChatGPTClient-Diagnostics-20260830-090524.json`
- Export metadata: Release / Candidate b57 / source marker `7074b1f85a0f` / iPhone / iOS17.0 / deployment target iOS14.0.

## Direct user-visible result

The user reported for the exact b57 reproduction:

- visible reasoning streamed only inside the Native `思考过程` region;
- reasoning no longer appeared concatenated with the final-answer body;
- the previously reported leading reasoning truncation did **not** reproduce;
- final answer appeared in the ordinary answer region after reasoning ended;
- tool calls still had no Native presentation.

The screenshot is consistent with the separated presentation: completed reasoning remains available in the independent reasoning region and the final answer is below it.

## Transport / aggregate evidence

One official protected Send completed with HTTP200 `text/event-stream` and terminal true.

- `frameCount=52`
- `nativeDeltaCount=16`
- `nativeCharacters=348`
- `nativeReasoningDeltaCount=4`
- `nativeReasoningCharacters=61`
- `nativeAnswerDeltaCount=12`
- `nativeAnswerCharacters=287`
- `reasoningEndMarkerCount=1`
- `reasoningFallbackPromoted=false`
- exact top-level text patches `3`
- nested text patches `4`
- contextual value strings `9 / 189 chars`
- inactive value strings `0`
- continuation resets `3`
- ordinary assistant-text messages `2`: before reasoning end `1`, after reasoning end `1`
- phase-text structure signatures `2 / overflow0`
- special structures `8 / overflow0`
- generic structures `32 / overflow1`

## Reasoning phase evidence

The first ordinary assistant text message was event 14:

- `assistant:text:in_progress`
- phase `before_reasoning_end`
- recipient `all`
- content keys `content_type,parts`
- `parts:1:string:chars6`
- metadata includes `is_thinking_preamble_message:true`

b57 intentionally did not extract that message body. Despite that, the user directly observed no leading truncation in this exact run. Therefore the previous missing-prefix defect is not reproduced here and there is no evidence-backed reason to broaden the text parser or start consuming the six-character preamble message.

Event 32 was the exact completed `assistant:reasoning_recap` with `reasoning_status=reasoning_ended`; b57 used it only as the phase-end marker. Event 33 then exposed a separate `assistant:text:in_progress` in phase `after_reasoning_end` with `parts:1:string:chars0`, after which accepted text entered the final-answer region.

Accepted Runtime conclusion: **b57 reasoning→final phase separation passes this exact-device gate.** The prior leading-prefix defect did not reproduce and no missing-prefix parser change is justified from this run.

## Tool activity evidence

The same turn contained multiple explicit tool invocation/result structures while Native displayed none:

- event 19: completed `assistant:code`, `recipient=api_tool.list_resources`, `is_complete:true`;
- event 20: completed `tool:text`, author `api_tool`, recipient `all`;
- event 22: completed `assistant:code`, `recipient=api_tool.call_tool`, metadata includes `connector_tool_payload`, `reasoning_title`, `reasoning_titles`, `tool_icons`;
- event 23: completed `tool:code`, author `api_tool.call_tool`, recipient `all`, metadata includes `invoked_plugin`, `invoked_resource`, `reasoning_title`;
- later events repeat the same assistant invocation -> tool result grammar, including a `tool:multimodal_text` result.

This is sufficient to establish **tool activity occurrence and ordering** for a narrow diagnostic presentation. It does not authorize exposing `content.text`, `content.parts`, raw parameters, raw results, connector payloads, internal thoughts, IDs or auth/proof material.

A later diagnostic Candidate may show one compact Native tool-activity entry for each exact completed assistant-code invocation with a non-`all` recipient and `is_complete:true`. If `metadata.reasoning_title` is a non-empty string at Runtime, that service-provided title may be displayed transiently but must not be persisted in diagnostics. Otherwise the UI may use a local generic `工具调用` label. Tool result messages remain evidence/status only; their body is not presentation data.

## Classification

- Code: Passed before Runtime
- CI: Passed before Runtime
- Artifact/package: Passed before Runtime
- Runtime/manual: **Passed for reasoning/final phase separation; tool activity remains visibly unimplemented**
- Stable/Frozen: No

TD-024/TD-025/TD-028 and production response ownership remain unchanged. b57 remains a diagnostic exception only.
