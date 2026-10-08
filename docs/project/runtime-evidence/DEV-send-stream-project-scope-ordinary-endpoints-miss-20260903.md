# DEV-send-stream — project scope ordinary-endpoint probe miss — 2026-09-03

## Runtime result

A privacy-safe Web Rule Lab probe was run while the visible official Web page was confirmed on a current project/GPT-scoped conversation route `/g/{scope}/c/{conversation}` with `readyState=complete`.

The probe intentionally returned no raw conversation ID, scope ID, title, body, Cookie, token, or auth material.

Observed result:

- current route shape: `/g/{x}/c/{x}`;
- direct ordinary `GET /backend-api/conversation/{conversation}`: HTTP 404;
- ordinary `GET /backend-api/conversations?offset=0&limit=28&order=updated`: HTTP 200;
- matching current project conversation in that ordinary list window: false;
- therefore no `gizmo_id`/project/scope/workspace field could be inspected from either attempted payload in this probe.

## Interpretation

This result does **not** prove that `gizmo_id` is absent from the current service model. It proves that the attempted ordinary conversation Detail/list surfaces are not a valid evidence source for this current scoped project conversation.

The prior decisive Control B remains unchanged: a fresh full document navigation to the exact official `/g/{scope}/c/{conversation}` route with transient user activation false started genuine official page-owned continuation (`stream_status + plural_snapshot`). The remaining pre-b89 evidence gap is now to identify the scoped route identity from the official project's own current page/request surfaces rather than guessing an ordinary conversation endpoint or importing an external implementation contract.

## Next exact evidence action

Use Web Rule Lab passively on the already loaded scoped project conversation to inventory only sanitized same-origin `/backend-api/` resource path shapes that the official page itself requested. Replace the known route scope and conversation ID with placeholders and omit query values/body/headers. If passive Resource Timing is insufficient, install a narrow privacy-safe fetch/XHR path-shape observer and perform one ordinary official scoped-page reload/entry. Do not synthesize or schedule any Native request.

No product source, version/build, Candidate, Artifact, or IPA identity changes are authorized by this evidence alone.
