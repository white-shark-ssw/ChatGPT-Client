from pathlib import Path

FILES = {
    "checkpoint": Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md"),
    "state": Path("docs/project/PROJECT_STATE.md"),
    "module": Path("docs/project/MODULE_STATUS.md"),
    "preflight": Path("docs/project/SEND_STREAM_PREFLIGHT.md"),
    "decisions": Path("docs/project/TECHNICAL_DECISIONS.md"),
}


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker not in text:
        path.write_text(section.rstrip() + "\n\n" + text)


checkpoint = '''## Web Rule Lab Stop request/ack contract Runtime Positive — 2026-09-08

Latest user-run targeted Web Rule Lab probe captures the exact official-Web Stop request and immediate acknowledgement. This supersedes the prior request-body/response-structure Unverified state.

Runtime-proven contract on one official Web Stop while a response was active:

- endpoint/method: `POST /backend-api/stop_conversation`, same-origin ChatGPT Web, no query items;
- request JSON is an object with exactly the observed top-level keys `conversation_id` and `exclude_async_types`;
- `conversation_id` is a 36-character string and the probe proved it exactly matches the currently routed conversation identity;
- `exclude_async_types` is an empty array in the observed official Stop request;
- server acknowledgement is HTTP200 `application/json`;
- response JSON is an object with top-level keys `last_message_id` and `status`;
- `status` is exact safe token `ok`;
- `last_message_id` is `null` in this observed acknowledgement. Do **not** infer from this field alone that partial assistant content is absent, deleted, or non-authoritative.

Evidence classification now:

- route: **Runtime Positive** (`/backend-api/stop_conversation`)
- method: **Runtime Positive** (`POST`)
- target identity: **Runtime Positive** (`conversation_id` equals current routed conversation)
- request structure: **Runtime Positive** (`conversation_id`, empty `exclude_async_types`)
- immediate server acknowledgement: **Runtime Positive** (HTTP200 JSON, `status=ok`, `last_message_id=null` in this sample)
- authoritative post-Stop terminal/partial-answer state: **still Unverified**
- whether product Stop should perform an immediate authoritative Detail reconciliation after the `ok` acknowledgement: **still Unverified**

Product remains exact canonical b115 and **b116 remains unallocated**. The deferred top-right live-menu persistence defect is still queued for the next independently justified product Candidate; it does not independently authorize a build.

**Next exact action:** on the same stopped conversation, perform one read-only authoritative Conversation Detail inspection using the already-installed Web Rule Lab helper. Record `conversation_async_status`, current-node/tail structure, assistant message status/end-turn/content length and whether the stopped partial response remains in Detail. No new Send or Stop is required. If that evidence establishes stopped terminal/partial-content semantics, the Server Stop protocol gate is sufficient to decide the next product Candidate.
'''
prepend_once(FILES["checkpoint"], "## Web Rule Lab Stop request/ack contract Runtime Positive", checkpoint)

state = '''## DEV-send-stream Web Stop contract Runtime Positive — 2026-09-08

- Official Web Runtime now proves `POST /backend-api/stop_conversation` with JSON keys `conversation_id` + `exclude_async_types`; `conversation_id` equals the currently routed conversation and `exclude_async_types` is empty in the observed request.
- Server returns HTTP200 JSON `{status: "ok", last_message_id: null}` structurally. `last_message_id:null` is not interpreted as evidence about partial-content persistence.
- Remaining Stop gate is one read-only authoritative post-Stop Detail inspection to establish terminal/async status and stopped partial-answer authority. Product remains b115; b116 is unallocated.
'''
prepend_once(FILES["state"], "## DEV-send-stream Web Stop contract Runtime Positive", state)

module = '''## Send / Stream — Web Stop request contract proven 2026-09-08

- Runtime-proven Web Stop: `POST /backend-api/stop_conversation`, body `conversation_id` matching current routed conversation plus empty `exclude_async_types`, HTTP200 JSON `status=ok`; observed `last_message_id` is null.
- Do not infer partial-answer deletion/absence from the null acknowledgement field. Authoritative post-Stop Detail remains the final semantic gate before product Stop implementation.
- No product Candidate is allocated from protocol research alone; current product remains b115.
'''
prepend_once(FILES["module"], "## Send / Stream — Web Stop request contract proven", module)

preflight = '''## Current Stop evidence gate — Web request/ack contract proven 2026-09-08

Runtime authority for the tested official Web Stop is now:

- `POST /backend-api/stop_conversation`
- request JSON: `conversation_id` equal to current routed conversation + empty `exclude_async_types`
- HTTP200 `application/json`
- response JSON: `status = "ok"`, `last_message_id = null` in the observed sample

The remaining required evidence is authoritative post-Stop Detail/terminal behavior and partial-response persistence. Do not infer these semantics from `last_message_id:null`, and do not allocate/implement product Stop until the final read-only Detail inspection is captured.
'''
prepend_once(FILES["preflight"], "## Current Stop evidence gate — Web request/ack contract proven", preflight)

decision = '''## 2026-09-08 — Web Stop target is conversation-scoped and exact request shape is evidenced

Decision update: official Web Runtime proves server Stop is conversation-scoped through `POST /backend-api/stop_conversation` with body fields `conversation_id` and `exclude_async_types`; the observed conversation ID equals the currently routed conversation and `exclude_async_types` is empty. HTTP200 JSON `status=ok` is the immediate acknowledgement. The observed `last_message_id:null` is not sufficient to decide partial-answer authority. Product implementation remains gated only on one authoritative post-Stop Detail semantic capture; do not reintroduce the rejected path-scoped `/conversation/<id>/stop_conversation` hypothesis.
'''
prepend_once(FILES["decisions"], "## 2026-09-08 — Web Stop target is conversation-scoped and exact request shape is evidenced", decision)
