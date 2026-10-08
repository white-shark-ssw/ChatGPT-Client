# DEV-send-stream b75 Visible-Web Continuation Re-probe

_Date: 2026-09-01_

## Purpose

Record the current privacy-safe Web Rule Lab evidence obtained after exact b75 covered-production Runtime showed page-owned matching `/backend-api/f/conversation/resume` returning HTTP404 JSON during an externally active response.

This evidence is structural only. It does not authorize Native polling, Native-constructed resume/offset, WebSocket body parsing, duplicate Send, retry/timer/watchdog behavior, or a second conversation/response authority.

## Capture method

The user opened Settings -> Web Rule Lab using the same default persistent `WKWebsiteDataStore`, installed a read-only network-structure probe before entering the target conversation, started/kept a response active from another platform, then entered the same conversation in visible official Web.

The probe recorded only:

- request method/host/sanitized route;
- request JSON key names only;
- HTTP status/content-type;
- WebSocket host/sanitized route, frame data type and byte/character length.

It did not capture Cookie/Authorization/challenge values, raw IDs, prompt/answer/reasoning/tool bodies or Web storage.

## Observed sequence

Relative times are from the supplied probe dump.

1. A user-level `wss://ws.chatgpt.com/.../ws/user/{user}` connection was present. The capture observed a 375-character string frame plus later 54-character string frames. Their bodies were intentionally not captured, so no message-body authority is established.
2. Target conversation entry began around `t=76.084s` with normal page bootstrap requests.
3. `GET /backend-api/conversation/{conversation}/stream_status` started at `t=77.869s` and returned HTTP200 `application/json` at `t=78.748s`.
4. The page itself then issued `POST /backend-api/f/conversation/resume` at `t=78.810s`. Its JSON key set was exactly `conversation_id,offset`.
5. That page-owned resume returned **HTTP404 `application/json`** at `t=79.366s`.
6. Immediately after the resume 404, the page issued another `stream_status` plus `GET /backend-api/conversations/{conversation}`. Both returned HTTP200 JSON.
7. The same page-owned `stream_status` + plural conversation GET pattern repeated at roughly six-second intervals in the captured window.
8. Short 54-character WebSocket frames occurred during this repeated status/detail cycle.
9. No later matching `/resume`, no second `/backend-api/f/conversation` Send, and no later HTTP200 `text/event-stream` continuation were observed through the dump at `t=97.898s`, about 18.5 seconds after the resume 404.

## Current conclusion

The exact b75 production 404 is not merely a covered/hidden WebView anomaly. Current **visible official Web** independently reproduces:

`stream_status 200 JSON -> page-owned matching {conversation_id, offset} resume -> 404 JSON -> repeated page-owned stream_status + /backend-api/conversations/{conversation} JSON fetches`

Therefore the earlier same-day visible-Web HTTP200-SSE `/resume` capture remains valid historical evidence for that exact run, but it is superseded as the current external-continuation rule.

The official page clearly continues doing work after the failed resume. The currently evidenced follow-on mechanism is repeated page-owned status/detail fetching, with short WebSocket frames occurring alongside it. This capture does **not** yet prove whether:

- `stream_status` contains only lifecycle state or also transport identity needed by the page;
- the plural conversation response contains incremental in-progress reasoning/tool/final structures;
- the 54-character WebSocket frames merely trigger page refresh/status checks or carry independently authoritative response information.

## Source correlation

Current `CoveredWebSendExecutor` only adopts a matching page-owned resume after exact HTTP200 `text/event-stream` validation. That validation remains correct and prevented false Native live-response creation on b75.

Current `ConversationRepository` already parses the standard singular Detail response from `mapping + current_node` into one authoritative current branch, including current visible user/assistant projection and evidenced reasoning/tool structures. The newly observed page polling route is plural `/backend-api/conversations/{conversation}` and must not be assumed to share the same schema without direct evidence.

## Next exact evidence gate

Run one narrower read-only Web Rule Lab capture on a fresh externally active response:

1. clone only the official page's own `stream_status` and `/backend-api/conversations/{conversation}` JSON responses;
2. export root keys and safe status/state/type/boolean/number fields only for `stream_status`;
3. for conversation responses export mapping/message counts and a bounded current-branch/tail structural summary only: role, status, content type, character counts, metadata key names and safe reasoning/tool booleans/enums — never text or raw IDs;
4. if a new WebSocket is created, export only top-level JSON key/type/event/status structure or, when non-JSON, data type/length;
5. compare repeated page-owned snapshots while the external response is still active.

If the page-owned conversation snapshots are proven to contain incremental user-visible reasoning/tool/final structure, evaluate the smallest observation-only bridge that reuses `ConversationRepository` authority without Native polling. If they do not, do not manufacture live reasoning from terminal/history reconciliation.

## Candidate / status boundary

- Exact tested product remains b75 source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`.
- b39-b75 remain permanently reserved.
- b76 remains unallocated.
- No product/config code was changed by this evidence capture.
- Stable/Frozen Send remains No.
