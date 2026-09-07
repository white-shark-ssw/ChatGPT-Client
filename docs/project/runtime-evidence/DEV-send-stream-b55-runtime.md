# DEV-send-stream b55 Runtime Evidence

Date: 2026-08-30

## Exact identity

User-supplied diagnostics: `ChatGPTClient-Diagnostics-20260830-080229.json`.

Export metadata exactly matched the emitted b55 Candidate:

- app version `0.1.0`;
- build `55`;
- Candidate `DEV-send-stream-0.1.0-b55`;
- source marker `aae856069b46`;
- Release;
- iPhone / iOS 17.0;
- deployment target iOS14.0.

Exact product/config source remains `aae856069b461e12dc11ee7d2d450a40ca621d21`; Artifact `9728606514`; IPA SHA-256 `f5106949814b44c6c97e2f519ff181498f6a75ff7b9bf9edf0dc0bb0bd299ad1`.

## Transport / completion

One Native submission reached the official protected Send and returned HTTP200 `text/event-stream`. The intercepted response reached terminal `[DONE]`.

Aggregate metrics:

- `frameCount=69`;
- `nativeDeltaCount=24`;
- `nativeCharacters=481`;
- `removedTextPatchCount=24`, `removedTextCharacters=481`;
- `explicitTextPatchCount=12`;
- `exactTopLevelTextPatchCount=4`;
- `rootNonExactTextPatchCount=0`;
- `nestedTextPatchCount=8`;
- `contextualValueStringCount=12`, `contextualValueStringCharacters=236`;
- `inactiveValueStringCount=0`, `inactiveValueStringCharacters=0`;
- `continuationResetWhileActiveCount=4`;
- `firstInactiveValueContext=none`;
- `titleGenerationWhileContinuationCount=0`;
- generic `structureSignatureCount=32`, overflow `14`;
- special `specialStructureSignatureCount=7`, overflow `0`;
- `webAssistantTextCharacters=0`, `webMessageNodes=2`, `webElementCount=651`;
- `terminal=true`.

Accepted: the independent b55 special-structure channel works under the exact failure condition that defeated b54. The generic observer again saturated at 32 and overflowed, while the special channel retained its target structures with zero overflow.

## Exact reasoning boundary proved

b55 directly emitted a completed `assistant:reasoning_recap` message at event index 41 with:

- role `assistant`;
- content type `reasoning_recap`;
- status `finished_successfully`;
- recipient `all`;
- content keys `content,content_type`;
- content string shape `content_type:15,content:7` for this exact turn;
- metadata boolean `can_save:false`;
- metadata enums `reasoning_status:reasoning_ended` and `reasoning_recap_type:collapse`;
- metadata also carries timing/model/request/turn bookkeeping keys, but their values are not presentation authority.

This is the first exact Runtime evidence that identifies both the concrete recap text container (`message.content.content`) and service-provided presentation/lifecycle semantics (`reasoning_ended`, `collapse`).

Accepted presentation boundary: a following diagnostic Candidate may extract only this exact `assistant:reasoning_recap / finished_successfully / recipient=all` `content.content` string into a Native user-visible recap region, with default collapsed presentation matching `reasoning_recap_type=collapse`.

The recap string itself was not persisted by b55 diagnostics; only its field name and length were recorded.

## Raw thoughts remain excluded

Immediately before the recap, b55 emitted `assistant:thoughts / finished_successfully` at event index 40 with:

- recipient `all`;
- content keys `content_type,source_analysis_msg_id,thoughts`;
- `thoughts` array with object keys `chunks,content,finished,summary`;
- metadata `can_save:false`;
- `reasoning_status:is_reasoning`;
- `tool_summary_type:github`;
- structural keys including `inline_cot_expandable_content` and `tool_icons`.

This does not authorize display of `thoughts`, `chunks`, `content`, hidden chain-of-thought or internal reasoning. They remain explicitly non-presentational. Only `reasoning_recap` is authorized by this Runtime evidence.

## Tool structure retained

The special channel also continued to retain assistant code invocation and tool-result structure after ordinary signature pressure:

- assistant `code` messages targeted recipients including `api_tool.list_resources` and `api_tool.call_tool`;
- completed assistant code carried `is_complete:true`, `connector_tool_payload` and `tool_icons` structural metadata;
- tool results included author names `api_tool` / `api_tool.call_tool`, recipient `all`, and result content types including `text` and `multimodal_text`;
- tool metadata exposed structural `invoked_plugin` / `invoked_resource` where present.

Accepted: invocation/result pairing remains structurally real. Not accepted: showing raw arguments/results, connector payloads, or arbitrary internal tool nodes. b55 does not add a new explicit user-visibility marker for tool nodes, so tool-call UI remains separately evidence-gated.

## Runtime classification

**b55 Runtime pass for its intended gate.**

Specifically:

1. the special observer capacity defect from b54 is corrected;
2. exact `reasoning_recap` content-container and collapse/end lifecycle metadata are now Runtime proved;
3. raw `thoughts` remains separate and prohibited;
4. tool call/result structure remains captured, but exact user-visible tool presentation is not yet proven;
5. b55 itself made no response-output/UI behavior change, so it is not a Runtime acceptance of a reasoning UI.

## Smallest justified next change

A following Candidate may implement **only** Native recap extraction/presentation:

- exact message match: assistant + `reasoning_recap` + `finished_successfully` + recipient `all`;
- extract only `message.content.content` when it is a non-empty string;
- present it in a distinct Native reasoning-summary region;
- default collapsed because the exact Runtime message declares `reasoning_recap_type=collapse`;
- allow explicit user expand/collapse;
- never present `assistant:thoughts` or raw tool payloads;
- keep the existing b55 final/mixed text interception behavior unchanged until a separate Runtime proves the exact reasoning→final patch-phase boundary.

No tool-call UI, response-owner promotion, TD-024/TD-025 change, retry/fallback/timer/watchdog or production repository mutation is justified by this evidence alone.
