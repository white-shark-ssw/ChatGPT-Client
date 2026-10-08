from pathlib import Path

FILES = {
    "checkpoint": Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md"),
    "state": Path("docs/project/PROJECT_STATE.md"),
    "preflight": Path("docs/project/SEND_STREAM_PREFLIGHT.md"),
}


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker not in text:
        path.write_text(section.rstrip() + "\n\n" + text)


checkpoint = '''## Web Rule Lab post-Stop Detail synthetic-read auth boundary — 2026-09-08

Latest user-run post-Stop Detail inspection using a manually reconstructed request to the previously observed official plural Detail URL returned HTTP401 JSON with only top-level `detail`. This result is **Inconclusive for Stop semantics** and must not be treated as a stopped-response failure.

What it proves:

- the prior 404 was a probe endpoint mistake and is superseded;
- reusing the official plural Detail URL with only a synthetic `fetch(..., {credentials:"include"})` is insufficient to reproduce the official Web request authorization/context;
- earlier official Web traffic already proved that the page itself can request `/backend-api/conversations/<opaque>` successfully with HTTP200, so the correct next evidence path is to observe the official page's own next Detail fetch rather than synthesize headers/challenge context.

What remains unchanged:

- Stop contract is still Runtime Positive: `POST /backend-api/stop_conversation`, body `conversation_id` matching current route + empty `exclude_async_types`, HTTP200 JSON `status="ok"`, observed `last_message_id=null`;
- authoritative post-Stop terminal/partial-content semantics remain Unverified;
- product remains b115, b116 remains unallocated.

**Next exact action:** install a read-only fetch observer that matches the official page's own `GET /backend-api/conversations/<current-id>` request and summarizes only the cloned HTTP200 response structure. Trigger that official read by normal Web navigation away from and back to the stopped conversation. Do not replay a synthetic Detail request and do not guess authorization headers.
'''
prepend_once(FILES["checkpoint"], "## Web Rule Lab post-Stop Detail synthetic-read auth boundary", checkpoint)

state = '''## DEV-send-stream post-Stop Detail synthetic-read auth boundary — 2026-09-08

- Manual replay of the observed official plural Detail URL with only browser credentials returned HTTP401; classify this as probe authorization/context insufficiency, not Stop failure.
- Next evidence must come from observing the official page's own successful Detail request/response after ordinary navigation, preserving official request construction. Stop request/ack contract remains Runtime Positive; terminal/partial semantics remain Unverified. Product stays b115; b116 unallocated.
'''
prepend_once(FILES["state"], "## DEV-send-stream post-Stop Detail synthetic-read auth boundary", state)

preflight = '''## Current Stop evidence gate — official Detail observation required 2026-09-08

- Synthetic post-Stop Detail replay is rejected as an evidence method after HTTP401 despite reusing an officially observed plural Detail URL. Cookies/`credentials: include` alone do not reproduce the official page's complete request context.
- Observe the official page's own `GET /backend-api/conversations/<id>` and clone its response instead. Do not guess authorization/challenge headers.
- Stop request/ack contract remains proven; authoritative terminal/partial-answer semantics remain the only Stop evidence gate before product implementation.
'''
prepend_once(FILES["preflight"], "## Current Stop evidence gate — official Detail observation required", preflight)
