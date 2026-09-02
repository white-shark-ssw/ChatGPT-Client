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

## Exact post-navigation route check

A follow-up boolean-only comparison used the internally saved scope/conversation and returned:

- `currentKind = EXACT_SCOPED_CANONICAL`;
- `currentIsExactScopedCanonical = true`;
- `currentIsExactUnscoped = false`;
- `currentIsProjectShape = true`;
- `currentConversationMatchesSaved = true`.

Therefore, in this **warm visible-Web session that had already visited the project conversation**, requesting `/c/{conversation}` ended with official Web at the exact scoped canonical `/g/{scope}/c/{conversation}` location.

This is direct Runtime evidence that official Web has a canonicalization mechanism. It is **not** yet evidence that a fresh/root covered-Web document which has never entered this project route has enough state to perform the same canonicalization. The existing b88 project failures remain incompatible with assuming warm-session canonicalization always occurs in production covered execution.

## Interpretation

1. The official visible Web possesses the project/GPT scoped canonical conversation route in an anchor href before successful target entry.
2. A successful project SPA transition can immediately issue page-owned `stream_status` using that canonical route without first fetching a project Detail payload that exposes the scope.
3. In a warm visible-Web session, even a deliberate unscoped `/c/{conversation}` navigation is canonicalized back to exact `/g/{scope}/c/{conversation}`.
4. `gizmo_id` remains external corroboration only, not a Runtime-confirmed route contract for ChatGPTClient.
5. The prior Control B remains decisive: a fresh full navigation to the exact official `/g/{scope}/c/{conversation}` route with transient user activation false starts genuine official page-owned continuation.
6. Before b89, reproduce the production covered-Web starting condition more closely: start from a fresh root document and then navigate directly to the unscoped project conversation while an external response is active. This will distinguish warm official canonicalization from a canonical-route defect that only exists in the covered cold/root path.

## Preserved boundary

This evidence does not authorize Native construction of `stream_status`, `/resume`, offsets or cadence. It does not authorize polling, timer/retry/watchdog, router emulation, WebSocket-body authority, duplicate Send or a second response store. The official page remains the continuation executor and `ConversationRepository` remains the Native response/content authority.
