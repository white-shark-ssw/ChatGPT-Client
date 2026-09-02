# DEV-send-stream — official project canonical anchor evidence — 2026-09-03

## Runtime setup

A privacy-safe Web Rule Lab observer was installed on the visible official Web while already on a project/GPT-scoped conversation route. The user then:

1. clicked an ordinary non-project conversation;
2. waited for that ordinary route to load;
3. clicked back to the target project conversation.

The observer recorded only sanitized route/path shapes, HTTP methods/status/content-types, query-key names, safe request-body structure, and scoped-field booleans/types. It did not return raw conversation IDs, project/scope IDs, titles, message bodies, Cookie, token or auth material.

## Ordinary conversation transition

The official visible Web emitted:

- trusted click target `/c/{id}`;
- `history.pushState` from `/g/{scope}/c/{conversation}` to `/c/{id}`;
- `GET /backend-api/conversations/{id}` with query keys `include_has_versions` and `num_turns`;
- `POST /backend-api/conversation/init`;
- ordinary Detail response HTTP 200 JSON;
- scoped-key scan of that ordinary Detail showed:
  - `gizmo_id = null`;
  - `gizmo_type = null`;
  - `memory_scope` non-empty but not equal to the project route scope;
  - `context_scopes` empty;
- page-owned `GET /backend-api/conversation/{id}/stream_status` -> HTTP 200 JSON.

This ordinary-conversation structure is not a source for the target project's scope.

## Project conversation re-entry

Before navigation, the trusted click already targeted the exact official project conversation anchor shape:

`/g/{scope}/c/{conversation}`

The official visible Web then emitted:

- `history.pushState` from `/c/{id}` to `/g/{scope}/c/{conversation}`;
- `POST /backend-api/conversation/init`;
- `GET /backend-api/conversation/{conversation}/stream_status`;
- sentinel `chat-requirements/prepare` and `chat-requirements/finalize` POSTs;
- project `stream_status` -> HTTP 200 JSON;
- init -> HTTP 200 JSON.

No project `GET /backend-api/conversations/{conversation}` response was required in this captured successful transition, so this sample does not support claiming that any project Detail field supplied the route scope at entry time.

## Interpretation

1. The official visible Web already possesses the project/GPT scoped canonical conversation route in the sidebar anchor href before target entry.
2. A successful project SPA transition can immediately issue page-owned `stream_status` using that canonical route without first fetching a project Detail payload that exposes the scope.
3. Therefore `gizmo_id` remains only external corroboration, not a Runtime-confirmed service contract for ChatGPTClient.
4. The prior Control B remains decisive: a fresh full navigation to the exact official `/g/{scope}/c/{conversation}` route with transient user activation false starts genuine official page-owned continuation.
5. The product defect remains that current covered-Web code hard-loads `/c/<conversationID>` and has no persisted scoped canonical route identity.
6. The next implementation-evidence question is whether covered official Web can deterministically resolve the canonical href for a Native-selected conversation without manual sidebar/project expansion. Prefer an already-present official canonical href/page-state source over guessing an API field.

## Preserved boundary

This evidence does not authorize Native construction of `stream_status`, `/resume`, offsets or cadence. It does not authorize polling, timer/retry/watchdog, router emulation, WebSocket-body authority, duplicate Send or a second response store. The official page remains the continuation executor and `ConversationRepository` remains the Native response/content authority.
