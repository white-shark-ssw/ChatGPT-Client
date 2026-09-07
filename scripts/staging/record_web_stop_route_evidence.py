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

checkpoint = '''## Web Rule Lab Stop route/method/ack Runtime evidence — 2026-09-07

Latest user-run broad Web Rule Lab network probe supersedes the earlier assumed Web Stop route.

Proven on official ChatGPT Web in one active-response Stop action:

- Protected Send for the test turn used the already-evidenced `POST /backend-api/f/conversation` and returned HTTP200 `text/event-stream` before Stop.
- At probe-relative `t=40085`, clicking the official Web Stop control emitted **`POST /backend-api/stop_conversation`**, same origin `https://chatgpt.com`, with no query items.
- At `t=41690`, the same Stop request returned **HTTP200 `application/json`**. `PerformanceResourceTiming` independently observed the request as `fetch`, duration about 1599 ms, transfer size 356 bytes.
- The current broad probe could not yet inspect Stop request body: it recorded `request-body-pending`. Therefore request keys, target identity and any tracking field remain **Unverified**. Do not infer them from static symbol names.
- Immediately after Stop, Web emitted `POST /backend-api/f/conversation/<opaque>` returning HTTP200 JSON. Its purpose/body were not captured, so it is structural post-Stop traffic only; do not classify it as regeneration, acknowledgement or reconciliation without more evidence.

Evidence correction:

- The earlier assumed Web route `/backend-api/conversation/<opaque>/stop_conversation` is **rejected for the tested official Web Stop path**. Current Runtime authority is `/backend-api/stop_conversation`.
- Official-iOS Probe v0.8 remains research-only fallback/cross-validation, but its exact path classifier was based on the older static/iOS hypothesis and is not Web protocol authority. Do not require that IPA before continuing Web Stop research.

Current Stop gate classification:

- route: **Runtime Positive** (`/backend-api/stop_conversation`)
- method: **Runtime Positive** (`POST`)
- immediate server acknowledgement: **Runtime Positive** (HTTP200 JSON)
- request body / target identity: **Unverified**
- response JSON structure/body: **Unverified**
- authoritative post-Stop terminal/partial-answer state and whether an explicit Detail reconciliation is needed: **Unverified**

Product remains canonical b115 and b116 remains unallocated. The deferred top-right live-menu persistence defect remains queued for the next independently justified product Candidate.

**Next exact action:** use a targeted Web Rule Lab wrapper for the now-proven `/backend-api/stop_conversation` endpoint that reads a cloned Request body *before* forwarding the fetch and reads a cloned response body before returning it. Record only JSON key/value classes plus irreversible hashes/match flags for identifier-like strings. Then perform one official Web Stop and inspect the post-Stop authoritative conversation Detail. Do not implement product Stop until body target + terminal semantics are evidenced.
'''
prepend_once(FILES["checkpoint"], "## Web Rule Lab Stop route/method/ack Runtime evidence", checkpoint)

state = '''## DEV-send-stream Web Stop protocol partially proven — 2026-09-07

- Official Web Runtime now proves `POST /backend-api/stop_conversation` -> HTTP200 `application/json` for the user's real Stop action. This supersedes the earlier assumed Web path containing the conversation ID.
- Stop request body/target and response JSON structure are not yet captured; post-Stop authoritative terminal/partial-answer semantics remain unverified.
- Product stays b115; no b116 allocation. Next evidence action is targeted body/response capture in Web Rule Lab, followed by authoritative Detail inspection. Official-iOS Probe v0.8 is fallback/cross-validation rather than a prerequisite.
'''
prepend_once(FILES["state"], "## DEV-send-stream Web Stop protocol partially proven", state)

module = '''## Send / Stream — Web Stop route/method/ack Runtime Positive 2026-09-07

- Official Web Stop has now been observed as `POST /backend-api/stop_conversation` with HTTP200 JSON acknowledgement while a response is active.
- Body target identity, response payload structure and post-Stop authoritative terminal state are still unverified, so product Server Stop is not yet implemented.
- Earlier `/backend-api/conversation/<opaque>/stop_conversation` Web assumption is superseded by Runtime evidence. Keep b115 as product baseline and do not allocate b116 yet.
'''
prepend_once(FILES["module"], "## Send / Stream — Web Stop route/method/ack Runtime Positive", module)

preflight = '''## Current Stop evidence gate — Web route/method/ack proven 2026-09-07

Runtime evidence from official ChatGPT Web now proves:

- route `/backend-api/stop_conversation`;
- method `POST`;
- HTTP200 `application/json` server acknowledgement.

Still required before product implementation:

- exact request JSON keys/value classes and response/conversation target relationship;
- response JSON structure/ack meaning;
- authoritative post-Stop Detail/terminal behavior, including whether partial assistant content is retained and whether an explicit later Detail reconciliation is needed.

The older assumed Web route `/backend-api/conversation/<opaque>/stop_conversation` is superseded. A research IPA is no longer prerequisite; Web Rule Lab is the preferred evidence path. Local transport cancellation remains non-proof of Server Stop.
'''
prepend_once(FILES["preflight"], "## Current Stop evidence gate — Web route/method/ack proven", preflight)

decision = '''## 2026-09-07 — Prefer Web Rule Lab for proven Stop endpoint before product implementation

Decision: official Web Runtime has established `POST /backend-api/stop_conversation` with HTTP200 JSON acknowledgement. This outranks the earlier static/iOS-derived path assumption. Continue with targeted Web Rule Lab body/response/Detail structural evidence; keep official-iOS Probe v0.8 only as optional cross-validation. Do not allocate the next product Candidate until the Stop target and terminal semantics are proven. When a product Stop Candidate is justified, include the already-deferred stable top-right-menu-host correction in the same exact scope rather than creating a standalone menu build.
'''
prepend_once(FILES["decisions"], "## 2026-09-07 — Prefer Web Rule Lab for proven Stop endpoint", decision)
