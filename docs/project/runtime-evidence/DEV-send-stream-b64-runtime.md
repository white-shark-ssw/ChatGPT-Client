# DEV-send-stream b64 Runtime evidence

## Identity

- Candidate: `DEV-send-stream-0.1.0-b64`
- Version / Build: `0.1.0 (64)`
- Exact product/config source: `6ce1fbd242c903d85930b0e8a8d2aadc29669cc1`
- Push Run / Job: `33325292890 / 99294233652` — success
- PR Run / Job: `33325295457 / 99294240336` — success
- Artifact: `9736051023`
- ZIP SHA-256: `5a4ba89298f6bdd467ed66294133b0a38bae58f30c90d3b104d1ea3954db856a`
- IPA SHA-256: `49b5e8021ca78da3e87f67721682edf306b300995be3566a391a6c35d573c6fc`
- Package: Release / source marker `6ce1fbd242c9` / minimum iOS14 / device family `[1,2]` / arm64
- Runtime device/export: iPhone / iOS17.0 / `ChatGPTClient-Diagnostics-20260830-174329.json`

## User-visible result

The user reported that the tested response appeared complete with no obvious reasoning/final-answer truncation. Native tool rows advanced through the expected invocation/completion lifecycle. Parent-paired GitHub tool detail could be expanded and collapsed, and both `工具输入` and `工具输出` were visible.

The remaining visible defect is presentation-only: `工具输出` is dumped as a very large JSON block with escaped nested strings, visually much denser than the official Web tree. The user specifically observed that output looked unformatted, all piled together, and apparently showed substantially more at once than the official Web presentation.

## Send / reasoning / final evidence

Observed verified-composer path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 text/event-stream -> terminal`

Terminal metrics:

- `frameCount=344`
- `terminal=true`
- exact reasoning-end marker `1`
- fallback promoted `false`
- Native reasoning `27 deltas / 440 chars`
- Native final answer `215 deltas / 6716 chars`
- Native total `242 deltas / 7156 chars`
- thinking preambles `3 / 33 chars`
- reasoning-active signals `7`
- Native thinking presentations `4`
- service/native reasoning segment breaks `2/2`
- inactive value strings `0`
- root-nonexact text patches `0`

Classification for text/reasoning: **tested behavior retained / no obvious user-observed truncation**.

## Tool lifecycle/detail evidence

Terminal metrics:

- invocation identities `30`
- completed invocation messages `27`
- tool results `35`
- parent present `35`
- exact parent matches `30`
- unmatched `5`
- missing `0`
- Native presentations/completion updates `30/30`
- paired presentations `30`
- Native rows with detail available `26`
- pre-terminal detail-expansion metric `7`

The unmatched results remained unpresented instead of being force-paired. Exact `parent_id` remains the row authority.

Across the complete exported interaction, the user exercised multiple detail expand/collapse operations successfully. This confirms the b64 disclosure interaction itself works.

## Root cause of the remaining formatting defect

b64 intentionally retains the exact paired result `message.content` in response-local presentation state. The Web-side bridge currently serializes that entire content object with `JSON.stringify(content)`. Native then parses/pretty-prints only that outer JSON layer.

For `multimodal_text`, service evidence includes shapes such as `parts:3:string:chars13504`; b64 then reports a serialized `detailOutputCharacters=15151`. Similar examples include `11895 -> 13249`. The extra visual density comes from the outer JSON envelope plus escaping of strings inside `parts`/`text` (`\"`, `\\`, escaped newlines, etc.), not from a parent-association error.

Official Web screenshots from the preceding b63 same-response comparison showed a hierarchical disclosure model: the tool row can open, then `工具输入` / `工具输出` expose structured object/array content rather than immediately flattening the entire nested result into one text block.

## Accepted b65 correction boundary

b65 may correct presentation only:

1. preserve exact b64 composer / protected Send / SSE parser / reasoning-final split / reasoning-end / parent pairing and GitHub-only detail authorization;
2. after a tool row is opened, present `工具输入` and `工具输出` as independent disclosure sections, default collapsed;
3. `工具输入` may pretty-print the already-authorized `connector_tool_payload` JSON;
4. `工具输出` may parse the already-authorized paired `message.content` outer JSON and render its structure without re-escaping string values; for known top-level `content_type`, `parts`, `language`, `response_format_name`, and `text`, show readable labels/array counts and raw string content rather than a second JSON-string layer;
5. do **not** invent an arbitrary truncation limit merely to imitate Web density; the first fix is hierarchy + decoding of the outer serialization layer;
6. do not expose `assistant:thoughts`, service IDs, unmatched results, or unrelated connector families;
7. do not log/export raw input/output values;
8. add no retry/timer/watchdog/fallback/second response authority.

## Runtime classification

**b64 Runtime Partial / presentation behavior proven, formatting rejected.**

Accepted from b64:

- verified Send path retained;
- reasoning/final looked complete in the tested response;
- exact-parent tool lifecycle remained correct;
- authorized GitHub input/output detail can be expanded/collapsed.

Rejected / next correction:

- one-level flattened JSON output presentation is not acceptable because nested string content remains escaped and a large output is dumped all at once.

Stable/Frozen Send remains No. b64 is permanently reserved because a valid Artifact exists.
