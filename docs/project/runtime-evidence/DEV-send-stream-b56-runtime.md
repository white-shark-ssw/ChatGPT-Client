# DEV-send-stream b56 Runtime Evidence

## Candidate identity

- Candidate: `DEV-send-stream-0.1.0-b56`
- Version/build: `0.1.0 (56)`
- Exact product/config source: `cec921030fd1af9f3853f35af52b661586b3a8ab`
- Artifact: `9728937100`
- IPA SHA-256: `da62776200ce94fef95326abaea3b980f65a5698df5dfe481bd34046e0f8dbe6`
- Runtime export: `ChatGPTClient-Diagnostics-20260830-083244.json`
- Runtime package metadata matched: Release / Candidate b56 / build 56 / source marker `cec921030fd1` / iPhone / iOS17.0.

## User-visible Runtime result

User supplied screenshots and direct observation:

- the beginning of the real visible reasoning/thinking text is still truncated;
- `思考摘要` appears and expands/collapses successfully;
- the recap itself contains only a short reasoning-status/description string (`思考了 40s` in this reproduction), not the actual visible reasoning body;
- the actual visible reasoning text remains concatenated in the same Native body as the final answer;
- therefore b56 does not yet provide the requested reasoning-body/final-answer separation.

User direct visual observation is authoritative over aggregate counters for presentation correctness.

## Transport / aggregate evidence

One official protected Send completed successfully:

- HTTP status `200`;
- content type `text/event-stream`;
- terminal `true`;
- `frameCount=75`;
- `nativeDeltaCount=26`;
- `nativeCharacters=504`;
- `removedTextPatchCount=26` / `removedTextCharacters=504`;
- `explicitTextPatchCount=12`;
- `exactTopLevelTextPatchCount=4`;
- `nestedTextPatchCount=8`;
- `rootNonExactTextPatchCount=0`;
- `contextualValueStringCount=14` / `299` chars;
- `inactiveValueStringCount=0`;
- `continuationResetWhileActiveCount=4`;
- generic structures `32`, overflow `16`;
- special structures `8`, overflow `0`;
- `reasoningRecapCharacters=7`.

## Exact reasoning recap evidence

At event index 45 the service emitted:

- role `assistant`;
- content type `reasoning_recap`;
- status `finished_successfully`;
- recipient `all`;
- content keys `content,content_type`;
- `reasoning_status=reasoning_ended`;
- `reasoning_recap_type=collapse`;
- exact-turn recap text length `7`.

Native received exactly 7 recap characters and the user repeatedly expanded/collapsed the region. This confirms the b56 recap presentation code works as implemented, but falsifies the stronger assumption that this recap string is the real visible reasoning body. In this Runtime sample it is only a short user-facing status/description.

`assistant:thoughts` remains a separate message at event 44 and is still non-presentational. Raw `thoughts`, chunks and hidden/internal reasoning remain prohibited.

## New phase-separation evidence

The stream shows an important ordering around the visible text path:

1. event 14: `assistant:text:in_progress`;
2. event 15: exact `append /message/content/parts/0`;
3. event 16: contextual value-string continuation;
4. later assistant code/tool activity;
5. event 44: `assistant:thoughts / finished_successfully`;
6. event 45: exact `assistant:reasoning_recap`, with `reasoning_status=reasoning_ended`;
7. terminal at event count 75.

The existing b56 parser sends all accepted `/message/content/parts/0` and contextual value-string text to one Native body. User observation confirms that this combines visible reasoning and final answer.

Accepted new boundary: exact `assistant:reasoning_recap` with `reasoning_status=reasoning_ended` is an evidenced reasoning-phase end marker. A following Candidate may use that event to split already-accepted assistant text into a pre-marker reasoning presentation and a post-marker final-answer presentation without exposing `assistant:thoughts`.

## Remaining leading-truncation hypothesis

The persistent leading truncation now has a stronger source-backed hypothesis: event 14 `assistant:text:in_progress` occurs immediately before the first accepted append at event 15, while the current parser only forwards explicit `/message/content/parts/0` append patches and contextual `{v:string}` continuations. The b56 diagnostic did not record the direct content field shape of ordinary `assistant:text` messages, so it does **not** yet prove where any initial characters are stored.

Therefore do not guess `parts[0]`, `text`, or another field. The next Candidate may add bounded text-free structure/count evidence for ordinary `assistant:text` message starts before/after the reasoning-end marker while implementing only the already-proven phase split.

## Classification

**b56 Runtime partial pass / presentation defect confirmed.**

Passed:

- exact recap detection;
- default collapse and explicit expand/collapse UI;
- no raw thoughts/tool payload exposure;
- protected Send transport and terminal completion.

Rejected / incomplete:

- recap string as the real reasoning body;
- reasoning-body/final-answer separation;
- leading visible-reasoning completeness.

b56 is permanently reserved. Any product-code change requires b57+.
