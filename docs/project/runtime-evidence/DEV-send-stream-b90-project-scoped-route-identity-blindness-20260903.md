# DEV-send-stream b90 — Project-Scoped Route Identity Blindness — 2026-09-03

## Exact observed Runtime identity

- Candidate: `DEV-send-stream-0.1.0-b90`
- Version / Build: `0.1.0 (90)`
- Exact product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`
- Device: iPhone / iOS17.0 / Release

## User observation

The user reports that ordinary non-project conversations do not have the same continuation problem, while the current project conversation does. In the same project test, the visible official Web page itself appeared healthy. This materially weakens z-order/occlusion as the primary explanation and points to project-specific conversation context.

## Runtime correlation

The exact b90 log first proves the earlier Native auth/list prerequisite recovered: `/api/auth/session`, accounts-check, and conversation-list requests returned HTTP200. A manual Sync then obtained an active authoritative Detail and the b90 frontmost mechanism executed successfully with `visibleSiblingCountAbove=0`, followed by `nativeFirstResponder=true` and `documentHasFocus=true`.

Immediately after the explicit direct `/c/{conversation}` reload, page diagnostics report `route=conversation`. Later activation events report `route=other` while the official Web remains visible/healthy. During that later interval the bridge emits no matching external stream-status/resume/snapshot continuation events.

## Source-level cause

Current `CoveredWebSendExecutor` initially loads every existing conversation through `https://chatgpt.com/c/{conversationID}`. Its document-start bridge derives identity only with:

```js
const currentConversationID = () => {
  const match = location.pathname.match(/^\/c\/([^/?#]+)/);
  return match ? decodeURIComponent(match[1]) : null;
};
```

Existing project evidence already establishes the official project-conversation canonical shape `/g/{scope}/c/{conversation}`. Once an unscoped project URL canonicalizes to that scoped route, the current parser returns `null` and `pageRouteShape()` reports `other`.

That parser is not cosmetic. The bridge uses `currentConversationID()` as the target identity gate for:

- matching `GET /backend-api/conversation/{id}/stream_status`;
- matching `POST /backend-api/f/conversation/resume` by request-body `conversation_id`;
- matching `GET /backend-api/conversations/{id}` snapshots;
- WebSocket exact-target structure detection;
- composer conversation identity.

Therefore the official project Web can be functioning correctly while the injected bridge becomes blind to the same project conversation after canonicalization. A zero-event interval after that point cannot be used to reject official page-owned continuation.

## Decision

This is stronger and more specific evidence than the b90 occlusion hypothesis. Allocate b91 as a minimum route-identity A/B only: recognize both ordinary `/c/{conversation}` and the exactly evidenced project `/g/{scope}/c/{conversation}` in the existing shared parser. Do not add retries, timers, polling, Native status/resume synthesis, guessed offsets, duplicate Send, new response ownership, or speculative route families.

b91 Runtime must prove whether project canonicalization remains target-recognized and whether the existing page-owned continuation events then become observable/functional. A later separate candidate is required before removing the b90 frontmost diagnostic; do not combine those variables in b91.
