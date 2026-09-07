# DEV-send-stream b89 — Interactivity Sufficient Rejected — 2026-09-03

## Exact tested identity

- Candidate: `DEV-send-stream-0.1.0-b89`
- Version / Build: `0.1.0 (89)`
- Product commit: `f39bc9387575028d431b85409780a2f3670b3259`
- Exact product/config package source: `fe45aeadf7ae03bf09aff66a8a05aa2542959676`
- Canonical Push Artifact: `9881665748`
- IPA SHA-256: `c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`
- Runtime: iPhone / iOS17.0 / Release.

## User-visible result

The user reported that this same project conversation still did not continue automatically and required pressing `同步最新消息`.

## Decisive diagnostic sequence

- `07:08:04Z` initial authoritative Detail: timeline `4`, tools `3`, reasoning `1`.
- First explicit Sync at `07:08:08Z` completed at `07:08:09Z`: timeline `5`, tools `4`, reasoning `1`; one Repository external response generation started from authoritative Detail.
- Rearmed executor page completed with `isUserInteractionEnabled=true`, non-empty/intersecting bounds in the key window, while remaining at `subviewIndex=0` with `visibleSiblingCountAbove=1`.
- First-responder activation succeeded: `nativeFirstResponder=true`, `documentHasFocus=true`.
- Fresh target page reported `navigator.userActivation` available, with `isActive=false` / `hasBeenActive=false` at the focus sample.
- No matching page-owned `stream_status`, `/resume`, external SSE or page-owned snapshot continuation appeared after the rearm/focus/interactivity state. Observed user WebSocket frames remained structural and `targetMatch=false`.
- A second explicit Sync at `07:10:06Z` returned at `07:10:07Z` with the same response generation at timeline `28`, tools `25`, reasoning `3`, mapping `64`.

Therefore the remote response advanced substantially (`5 -> 28` timeline, `4 -> 25` tools) while the covered executor produced no automatic continuation path; newer material appeared only through authoritative manual Detail Sync.

## Qualification

- Interactivity=true: Runtime exercised.
- First-responder / document focus: Runtime Positive.
- Manual authoritative Detail block projection: Runtime Positive.
- Automatic page-owned continuation after interactivity+focus: Runtime Negative.
- **Interactivity as a sufficient condition: Rejected.**
- Stable/Frozen Send: No.

This does not prove user activation universally irrelevant or impossible. The known-positive visible-Web fresh-root control had already continued from unscoped full navigation with transient activation false, while a later manual Lab activation read was contaminated by its explicit Execute gesture.

## Next evidence target

The remaining directly evidenced covered-vs-visible presentation differential is z-order/occlusion: production source inserts the executor at Root index 0, and b89 logged one visible sibling above it. Exact b90 therefore tests only frontmost presentation after explicit Sync/rearm. No Native status/resume/offset, polling, timer/retry/watchdog, duplicate Send, WebSocket-body authority or second response store is authorized.
