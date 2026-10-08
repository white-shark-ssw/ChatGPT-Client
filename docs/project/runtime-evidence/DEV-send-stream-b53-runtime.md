# DEV-send-stream b53 Runtime evidence

- Candidate: `DEV-send-stream-0.1.0-b53`
- Version/build: `0.1.0 (53)`
- Exact product/config source: `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`
- Push Run / Job: `33294541342` / `99211838094`
- PR Run / Job: `33294542985` / `99211842336`
- Artifact: `9726996570`
- Artifact ZIP digest: `sha256:8831bbae1c5cad9c9cd7f0ad9fbcf4846d709b27ae950b0391d436e20749b38c`
- IPA SHA-256: `d5eee722ea01dc2c1b419a803574aec8ad2199299a3d0bbb51de4bae574f25dc`
- Runtime: iPhone / iOS 17.0
- Diagnostics exported: `2026-08-30T06:02:47Z`
- Evidence class: exact-device diagnostic Runtime; not production Send acceptance.

## User-visible result

The user reported for the focused reasoning/tool-style turn:

- the beginning of the visible reasoning/thinking portion was still truncated;
- the final/real answer was complete;
- no tool-call presentation was visible in the Native diagnostic UI.

This is consistent with b53 being behavior-neutral: it adds structural observation only and does not implement reasoning/tool presentation.

## Stream / terminal metrics

One Native submission reached official protected Send HTTP 200 `text/event-stream` and completed normally.

- `frameCount=71`
- `removedTextPatchCount=21`
- `removedTextCharacters=476`
- `explicitTextPatchCount=10`
- `exactTopLevelTextPatchCount=4`
- `rootNonExactTextPatchCount=0`
- `nestedTextPatchCount=6`
- `contextualValueStringCount=11`
- `contextualValueStringCharacters=196`
- `inactiveValueStringCount=0`
- `inactiveValueStringCharacters=0`
- `continuationResetWhileActiveCount=4`
- `firstInactiveValueContext=none`
- `titleGenerationWhileContinuationCount=0`
- `nativeDeltaCount=21`
- `nativeCharacters=476`
- `webAssistantTextCharacters=0`
- `structureSignatureCount=32`
- `structureSignatureOverflowCount=1`
- terminal true.

The b52 conclusion remains intact: this reasoning-leading gap is not explained by a root non-exact text patch followed by inactive value-only continuation.

## Newly evidenced message/content grammar

b53 captured explicit structure signatures without recording message text or raw IDs.

Important observed sequence/classes:

- event 14: `assistant / text / in_progress`;
- event 15: exact top-level `append /message/content/parts/0`;
- event 16: contextual value-string continuation;
- event 19: patch batch containing `append /message/content/parts/0` plus status/end-turn/metadata changes;
- event 20: `assistant / code / in_progress`;
- event 21: patch batch containing `append /message/content/text` plus status/end-turn/metadata changes;
- event 22: `tool / text / finished_successfully`;
- event 24: `assistant / code / finished_successfully`;
- event 25: `tool / code / finished_successfully`;
- event 27: `tool / multimodal_text / finished_successfully`;
- event 31: `tool / text / finished_successfully`;
- event 45: `assistant / thoughts / finished_successfully`;
- event 46: `assistant / reasoning_recap / finished_successfully`;
- events 52/53/54/58/59: citation/content-reference-rich nested patches involving `append /message/content/parts/0`;
- event 69: `message_stream_complete`.

## Accepted conclusions

1. **Explicit `assistant:reasoning_recap` is now Runtime evidenced.** This is the first direct service-visible reasoning-named content type in the current exact account/runtime evidence.
2. `assistant:thoughts` is also present, but it must remain non-presentational unless separate evidence proves it is explicitly user-visible. Do not expose it as chain-of-thought.
3. Tool execution is structurally real in this turn: `assistant:code` and multiple `tool` content types were emitted. The absence of Native tool UI is a presentation/parser gap, not absence of service-side tool activity.
4. b53 does **not** prove which `tool`/`assistant:code` nodes are intended for user-visible presentation. Role/content type alone is insufficient because internal tool execution nodes must remain hidden.
5. b53 also does not yet prove the concrete content container for `reasoning_recap` (for example parts/text/other) or the visibility metadata attached to tool/code messages. Therefore implementing reasoning text extraction or tool-detail UI directly from role/content type would still be a guess.
6. Final-answer capture passes this exact reproduction; complete reasoning capture remains Runtime rejected/partial.

## Required next evidence

A minimal b54 structure refinement is justified. It should preserve b53 output/filtering and record only privacy-safe structure for `assistant:reasoning_recap`, `assistant:thoughts`, `assistant:code`, and `tool:*` messages:

- message/author/content/metadata key names;
- content array/string field counts and character counts, never text;
- direct metadata boolean fields and safe structural enum fields relevant to visibility/presentation;
- recipient/author-name safe protocol token where structurally present;
- existing role/content-type/status/end-turn information.

The objective is to identify the actual `reasoning_recap` content container and distinguish service-visible tool presentation from internal-only execution nodes. Do not implement reasoning collapse/expand, tool sheet/popover, reasoning haptics or expose `thoughts` until that evidence is available.
