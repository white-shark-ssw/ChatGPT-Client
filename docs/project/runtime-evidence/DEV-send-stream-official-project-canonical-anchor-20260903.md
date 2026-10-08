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
- scoped-key scan of that ordinary Detail showed `gizmo_id=null`, `gizmo_type=null`, `memory_scope` non-empty but not equal to the project route scope, and `context_scopes` empty;
- page-owned `GET /backend-api/conversation/{id}/stream_status` -> HTTP 200 JSON.

This ordinary-conversation structure is not a source for the target project's scope.

## Project conversation re-entry

Before navigation, the trusted click already targeted the exact official project conversation anchor shape `/g/{scope}/c/{conversation}`. Official visible Web then emitted:

- `history.pushState` from `/c/{id}` to `/g/{scope}/c/{conversation}`;
- `POST /backend-api/conversation/init`;
- `GET /backend-api/conversation/{conversation}/stream_status`;
- sentinel `chat-requirements/prepare` and `chat-requirements/finalize` POSTs;
- project `stream_status` -> HTTP 200 JSON;
- init -> HTTP 200 JSON.

No project `GET /backend-api/conversations/{conversation}` response was required in this successful transition, so this sample does not support claiming that a project Detail field supplied the route scope at entry time.

## Deliberate unscoped-route DOM probe

From the same project conversation, a probe deliberately requested a full navigation toward `/c/{conversation}`. After load, DOM inspection found exactly one visible exact scoped canonical anchor for that same conversation:

- `sameConversationLinkCount=1`;
- `scopedConversationLinkCount=1`;
- `exactCanonicalLinkCount=1`;
- `exactCanonicalVisibleCount=1`;
- `sameProjectScopeLinkCount=1`.

A follow-up boolean route comparison proved the post-navigation location itself was exact scoped canonical:

- `currentKind=EXACT_SCOPED_CANONICAL`;
- `currentIsExactScopedCanonical=true`;
- `currentIsExactUnscoped=false`;
- `currentIsProjectShape=true`;
- `currentConversationMatchesSaved=true`.

This proved official Web can canonicalize an unscoped project conversation route in a warm visible-Web session.

## Fresh-root production-like unscoped control — Positive

A stronger control then reproduced the covered executor's route shape more closely:

1. save only the target scope/conversation for result comparison;
2. full-navigate the visible Web Rule Lab to a fresh `/` root document;
3. while the remote project response was active, wait until transient user activation was false;
4. from root, full-navigate directly to unscoped `/c/{conversation}`;
5. observe the resulting route and Resource Timing without manually entering the project route.

Exact user result:

- marker `phase=unscoped_full_navigation_started`;
- `activationAtNavigation=false`;
- elapsed since navigation request about 111.5s;
- page `readyState=complete`, `visibilityState=visible`, `hasFocus=true`;
- final `currentKind=EXACT_SCOPED_CANONICAL`;
- `currentIsExactScopedCanonical=true`;
- `currentIsExactUnscoped=false`;
- Resource Timing `totalResourceCount=4`, `possiblySaturated=false`;
- `plural_snapshot=1`;
- `stream_status=1`;
- `resume=0`;
- `canonicalizationObserved=true`;
- `continuationObserved=true`.

This is decisive against the single-cause hypothesis that production fails merely because it initially requests `/c/<project-conversationID>` instead of `/g/<scope>/c/<conversationID>`. In this tested visible-Web browsing context, official Web itself recovered the exact scoped canonical route and started genuine page-owned continuation from an unscoped full navigation with transient activation false.

The observed continuation was page-owned status/snapshot behavior, not resume-SSE in this sample, because no `/resume` resource was observed.

## Interpretation

1. Official Web possesses and can use exact project/GPT scoped canonical conversation identity without Native synthesizing it.
2. Exact scoped full navigation remains Runtime Positive for continuation.
3. Trusted click and same-document SPA entry are not required.
4. A fresh root document followed by direct unscoped `/c/{conversation}` navigation can also canonicalize and continue in the visible Web Rule Lab browsing context.
5. Therefore scoped-route identity alone no longer explains b88 covered-Web failure and must not drive a route-only b89 fix.
6. `gizmo_id` remains external corroboration only, not a Runtime-confirmed ChatGPTClient route contract.
7. The remaining investigation target is the covered-vs-visible WKWebView runtime/browsing-context differential. b87/b88 already ruled out hidden/detached/unready page state and b88 proves covered `document.hasFocus=true` is achievable; transient user activation at navigation is now also shown unnecessary in the successful visible path.
8. Next smallest evidence action is to read `navigator.userActivation.isActive/hasBeenActive` on the successful visible page. If sticky activation is absent, the next code-backed A/B should target the remaining WKWebView presentation/interactivity differential rather than route identity.

## Preserved boundary

This evidence does not authorize Native construction of `stream_status`, `/resume`, offsets or cadence. It does not authorize polling, timer/retry/watchdog, router emulation, WebSocket-body authority, duplicate Send or a second response store. The official page remains the continuation executor and `ConversationRepository` remains the Native response/content authority.
