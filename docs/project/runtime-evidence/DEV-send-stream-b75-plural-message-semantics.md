# DEV-send-stream b75 Plural Live-Message Semantics

_Date: 2026-09-01_

## Scope

This is the final privacy-safe Web Rule Lab structure probe for the current cross-platform active-response path. It follows the prior evidence that visible official Web itself gets page-owned `/resume` HTTP404 JSON, then continues page-owned `stream_status` plus plural `/backend-api/conversations/{conversation}` reads.

No Cookie/Authorization/challenge values, raw IDs, prompt/answer/reasoning bodies, tool bodies or Web storage were captured.

## Exact Runtime observations

- `GET /backend-api/conversation/{conversation}/stream_status` remained HTTP200 with `status=IS_STREAMING` during generation and later changed to `COMPLETE`.
- The page-owned plural response uses top-level `messages[]`, not singular Detail `mapping`.
- `messages[]` is a paged/rolling current-branch window; observed counts changed 125 -> 110 -> 116 -> 120 -> 124 and therefore **message count is not a monotonic lifecycle cursor or total**.
- Each `messages[]` entry is the same service-message object family already evidenced by the singular Detail parser: `author`, `content`, `metadata`, `recipient`, `status`, `id`, timestamps and related fields.

During `IS_STREAMING`, the current-response tail exposed all required response semantics structurally:

1. thinking preamble: assistant / recipient `all` / content `text` / `metadata.is_thinking_preamble_message=true`; observed visible character counts changed as new reasoning segments appeared;
2. tool invocation: assistant / recipient not `all` / content `code` / finished / `metadata.is_complete=true`, with `connector_tool_payload`, `parent_id`, `reasoning_title` and tool-icon metadata present;
3. tool result: role `tool` / recipient `all`, with exact-parent `metadata.parent_id` and invoked-resource metadata, matching the already accepted tool association rule;
4. non-presentational thoughts: assistant / recipient `all` / content `thoughts`, with `reasoning_status=is_reasoning` and sometimes `inline_cot_expandable_content=true`; these remain hidden;
5. reasoning end: assistant / recipient `all` / content `reasoning_recap`, with `reasoning_status=reasoning_ended` and `reasoning_recap_type=collapse`;
6. final answer while still streaming: assistant / recipient `all` / content `text` / `status=in_progress`, initially with an empty text part in the captured snapshot;
7. after `stream_status=COMPLETE`, the terminal plural snapshot contains the same final-answer service shape as `status=finished_successfully`, `end_turn=true`, with the completed answer body present.

The latest user service message is present immediately before the active response segment in the linear window. Therefore the current active-response segment can be deterministically bounded as the service messages after the latest user entry in the page-owned snapshot; raw message count must not be used as the response identity.

## Current rule established

The protocol-discovery gate is closed for this defect. Current official Web can follow a cross-platform active response after `/resume` 404 through **its own existing** `stream_status` + plural-conversation fetch activity, and the plural response already carries the service-message structures required to reconstruct thinking/tool/reasoning-end/final state.

This authorizes one narrow b76 production experiment:

- observe only the official page's already-issued matching `stream_status` and plural-conversation responses;
- never construct those requests natively and never reproduce their cadence;
- validate target conversation identity;
- derive only the service messages after the latest user entry;
- project those snapshots into the existing `ConversationRepository` live-response runtime, replacing derived snapshot state deterministically rather than appending duplicate deltas;
- keep `assistant:thoughts` / inline COT non-presentational;
- retain exact-parent tool association and existing GitHub detail rules;
- terminal only after page-owned `COMPLETE` plus the corresponding final plural snapshot;
- keep WebSocket structural-only and unused as response-body authority;
- preserve the historical `/resume` HTTP200-SSE path if the page actually returns it again, but do not weaken its HTTP200/SSE validation.

## Candidate boundary

This evidence itself changes no product/config source. Exact b75 remains the tested package and remains Runtime partial/rejected. b76 may now be allocated after the final identity uniqueness guard, with the plural-snapshot observation correction and the already-required larger reasoning/tool/final vertical rhythm as one coherent product candidate.
