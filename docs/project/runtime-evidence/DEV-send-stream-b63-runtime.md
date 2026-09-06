# DEV-send-stream b63 Runtime Evidence

Date: 2026-08-31 (user local time)

Candidate: `DEV-send-stream-0.1.0-b63`

Exact product/config source: `0c2e2b870e51c363c7734182d49618c438839cc2`

Artifact: `9735145598`

IPA SHA-256: `b347d1e41ca5a4e1355a9cc713574ea96247e11918ccfb1f5ff621a0f9f6ff36`

User export: `ChatGPTClient-Diagnostics-20260830-170359.json`

## Identity gate

The exported diagnostics matched the exact intended Runtime candidate:

- app version `0.1.0`;
- build `63`;
- Candidate `DEV-send-stream-0.1.0-b63`;
- source marker `0c2e2b870e51`;
- Release;
- iPhone;
- iOS `17.0`;
- deployment target `14.0`.

## Tested path

The user sent one GitHub/repository request through `Native 输入 / Web Send` that naturally generated many GitHub connector tool calls, waited for the response to complete, then switched to the official Web surface and expanded representative tool details.

Observed Send-entry order remained the accepted b62 path:

`ready=false / none -> page loaded -> ready=false / none -> ready=true / prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 text/event-stream -> terminal`.

No generic-textarea fallback, retry, timer, polling or watchdog was involved.

## Native reasoning / final presentation

Terminal metrics:

- frameCount `308`;
- terminal `true`;
- exact reasoning-end marker `1`;
- reasoning fallback promoted `false`;
- Native reasoning `23 deltas / 328 chars`;
- Native answer `200 deltas / 6345 chars`;
- Native total `223 deltas / 6673 chars`;
- thinking preambles `2 / 7 chars`;
- reasoning active signals `5`;
- Native thinking presentations `4`;
- service/native reasoning segment breaks `1 / 1`;
- title-generation while continuation active `1`.

The user directly reported that this run appeared untruncated. Screenshot evidence showed a populated Native reasoning section, completed tool rows and a long final answer with no obvious leading/middle truncation.

Classification for the tested response-text scope: **Runtime pass**. This remains scoped evidence for the tested iPhone/iOS17 path, not a universal proof for every future service shape.

## Exact parent-paired tool lifecycle

Terminal tool metrics:

- invocation count `21`;
- invocation identity count `24`;
- tool result count `25`;
- result parent present `25`;
- exact parent matches `24`;
- unmatched `1`;
- missing parent `0`;
- Native tool presentations `24`;
- Native tool completion updates `24`;
- paired presentation count `24`.

The user reported that visible Native tool rows first showed invocation state and then completed successfully.

The extra unmatched result was **not** force-paired by count/order. This strengthens the durable rule that invocation/result association remains exact `parent_id` matching only; adjacency, count alignment or order must not be used to manufacture a pair.

Classification for the tested Native tool-row lifecycle: **Runtime pass for 24 exact-parent visible pairs; one additional unmatched result correctly remained outside the forced-pair path.**

## Official Web expandable-detail evidence

The user captured multiple screenshots from the same response after switching to the official Web surface.

The official Web GitHub tool UI showed:

- a tool-call list with individually expandable rows such as `list_resources`, `fetch`, `search_commits`, `search`;
- a representative expanded `fetch` row with sections labelled `工具描述`, `工具输入`, and `工具输出`;
- `工具输入` displayed an object whose visible field/value was the request URL;
- `工具输出` displayed the returned structured result, including visible `content_type: "multimodal_text"` and `parts: Array(3)`; another screenshot expanded the result far enough to show the first `parts` entries and their returned textual content.

This same-run visual evidence is higher-priority than field-name inference and establishes that, for the tested GitHub connector path, invocation arguments and the matched tool result content are intentionally user-visible expandable detail in the official UI.

## b63 structural correlation

The structural diagnostics line up with the official Web screenshots:

### Invocation input

Completed assistant `code` invocation messages to `api_tool.call_tool` repeatedly carried `metadata.connector_tool_payload` as JSON strings. b63 safely fingerprinted concrete top-level parameter shapes including examples such as:

- `json_object:url:string49`;
- `json_object:url:string69`;
- `json_object:query:string0+repository_full_name:string30+topn:number+sort:string14+order:string4`;
- `json_object:query:string52+repository_name:string30+topn:number`;
- `json_object:owner:string15+repo_name:string14+query:string11+page_size:number`.

The official Web expanded `fetch` screenshot displayed the corresponding `url` argument under `工具输入`. Therefore the tested GitHub `connector_tool_payload` is now evidenced as the source of official user-visible tool input, not merely a string-shaped candidate field.

### Matched output

Parent-paired tool result messages in the same stream included tested visible content shapes such as:

- `messageRole=tool`, `messageContentType=multimodal_text`, `parts:3`;
- `messageRole=tool`, `messageContentType=code`, `text:<length>`;
- `messageRole=tool`, `messageContentType=text`.

The official Web expanded `fetch` screenshot displayed `content_type: "multimodal_text"` and `parts: Array(3)` under `工具输出`, directly matching the parent-paired tool-result `message.content` shape seen in the stream.

Therefore, for the tested GitHub connector path, the matched result `message.content` is evidenced as official user-visible expandable tool output.

### `inline_cot_expandable_content`

Aggregate b63 metrics:

- expandable messages `3`;
- source IDs `3`;
- source→invocation matches `3`;
- source→tool-activity matches `2`;
- unmatched `0`.

This proves the tested `source_message_ids` refer to tool invocation identities, but only three such references were observed while 24 Native tool rows were presented. It is therefore **not** accepted as the per-row association authority for all expandable tool details. Exact existing invocation/result `parent_id` association remains the row-level authority.

## Accepted mapping from this Runtime

The current evidence is sufficient for a minimal next implementation limited to the tested GitHub connector flow:

1. keep existing response-local invocation identity and exact result `parent_id` pairing as the only row association rule;
2. for a paired GitHub connector invocation, retain the invocation's `metadata.connector_tool_payload` only in response-local transient presentation state and make its parsed value available as expandable Native `工具输入`;
3. for the exact matched result, retain only the matched result `message.content` in the same transient presentation state and expose it as expandable Native `工具输出`;
4. do not use `assistant:thoughts` body as display content;
5. do not log/export raw tool input/output values or service message IDs;
6. do not invent `工具描述` until an exact service source for that description is evidenced;
7. do not broaden this Runtime evidence to unrelated connector/tool families without later evidence.

## Classification / next boundary

Exact b63 classification:

**Code written / Push CI passed / PR CI passed / Artifact produced / package identity verified / Runtime passed for tested verified-composer + complete-looking reasoning/final + exact-parent visible tool lifecycle + GitHub official expandable input/output mapping; Stable/Frozen No.**

b63 is permanently reserved.

The next evidence-backed product action is a minimal b64 diagnostic-UI implementation of expandable Native GitHub tool input/output using the accepted mapping above. b64 must preserve b63 Send/text/reasoning/tool lifecycle behavior, must not add retry/timer/watchdog/fallback, must not expose `assistant:thoughts`, and must keep raw tool values out of diagnostics.