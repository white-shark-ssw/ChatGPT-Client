# DEV-send-stream — official project canonical anchor evidence — 2026-09-03

## Runtime setup

Privacy-safe Web Rule Lab probes were run on visible official Web project/GPT-scoped conversation state. The probes returned only sanitized route/path shapes and structural counts/booleans. They did not return raw conversation IDs, project/scope IDs, titles, message bodies, Cookie, token or auth material.

## Ordinary conversation comparison

A trusted transition from the project conversation to an ordinary non-project conversation emitted:

- trusted click target `/c/{id}`;
- `history.pushState` to `/c/{id}`;
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

## Deliberate unscoped-route DOM probe

From the same project conversation, a later probe saved the current project scope/conversation internally and deliberately requested a full navigation toward the unscoped form `/c/{conversation}`. After load, without exposing the raw IDs, DOM inspection found:

- `sameConversationLinkCount = 1`;
- `scopedConversationLinkCount = 1`;
- `exactCanonicalLinkCount = 1`;
- `exactCanonicalVisibleCount = 1`;
- `sameProjectScopeLinkCount = 1`.

Therefore the rendered official page state possessed exactly one visible anchor for that same selected conversation using the exact expected canonical `/g/{scope}/c/{conversation}` href, even though the navigation had been deliberately initiated through the unscoped form.

The probe's coarse current-route classifier returned `other` because it only labeled an exact `/c/{id}` path and did not classify the actual post-navigation path. This sample therefore does **not yet** prove whether official Web automatically canonicalized the browser location itself back to `/g/{scope}/c/{conversation}` or stayed on another route while exposing the canonical href. A one-step boolean route comparison is the next evidence action.

## Interpretation

1. The official visible Web possesses the project/GPT scoped canonical conversation route in an anchor href before successful target entry.
2. A successful project SPA transition can immediately issue page-owned `stream_status` using that canonical route without first fetching a project Detail payload that exposes the scope.
3. Even after deliberately requesting the same project conversation through `/c/{conversation}`, the rendered page state exposes the exact scoped canonical anchor for that conversation in this visible-Web session.
4. `gizmo_id` remains external corroboration only, not a Runtime-confirmed route contract for ChatGPTClient.
5. The prior Control B remains decisive: a fresh full navigation to the exact official `/g/{scope}/c/{conversation}` route with transient user activation false starts genuine official page-owned continuation.
6. Before b89, resolve whether the wrong-route navigation itself was automatically canonicalized. If not, then verify that exact canonical-anchor resolution is deterministic in the covered production-like page state without manual sidebar/project expansion.

## Preserved boundary

This evidence does not authorize Native construction of `stream_status`, `/resume`, offsets or cadence. It does not authorize polling, timer/retry/watchdog, router emulation, WebSocket-body authority, duplicate Send or a second response store. The official page remains the continuation executor and `ConversationRepository` remains the Native response/content authority.
