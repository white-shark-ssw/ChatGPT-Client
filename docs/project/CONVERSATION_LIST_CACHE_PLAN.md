# Conversation List Cache / Preview Plan

_Last planned: 2026-08-27._

## Purpose

This document defines the durable plan for a fast cold-start conversation list, clipped message previews, persistent list metadata and network-efficient incremental reconciliation.

The primary product requirement is: **show useful cached conversation rows quickly after the current account scope is verified, then reconcile with one normal list refresh without issuing one Conversation Detail request per row.**

Planned Work ID: `DEV-conversation-list-cache-preview`.

## Current evidence baseline

Current multi-conversation branch source establishes:

- `ConversationSummary` currently stores only `id`, `title`, `updateTime`.
- `ConversationRepository.conversations` is in-memory only.
- `ConversationSidebarViewController.viewDidLoad()` immediately calls `loadConversations()`; a cold process has no disk-backed list to render while the request is pending.
- Current list request is one `GET /backend-api/conversations?offset=0&limit=28&order=updated`.
- Current parser consumes only list-item `id`, `title`, and `update_time`.
- Current repository has real account-scoped state work in progress; the persistent cache must build on the accepted account-scope owner after `DEV-multi-conversation-state` is merged/stable.

**Unknown / Unverified:** whether the current list payload already carries a safe user-visible snippet/preview field. Do not assume one exists and do not infer it from historical/private API memory.

## Goals

1. After current account verification succeeds, render the last known list snapshot without waiting for the list network request to finish.
2. Immediately perform the normal current list refresh and merge changed rows into the cached presentation.
3. Add one clipped message-preview line below the conversation title when preview data is locally available or is proven to arrive in the same list response.
4. Never fan out `N` Conversation Detail requests merely to populate `N` preview rows.
5. Persist only the minimum metadata needed for this experience; do not turn this feature into full chat-body/offline caching.
6. Keep all cache data strictly scoped to the verified account/workspace context and never flash another account's cached list before scope verification.
7. Integrate later with pagination, Send/Stream, rename/archive/delete and account switching without creating a second conversation authority.

## Non-goals

- No full `ConversationDetail` / raw mapping JSON persistence in this Work.
- No automatic background polling, timer refresh or watchdog.
- No server-request retry chain.
- No speculative alternate list/preview endpoint.
- No loading every conversation once at startup to manufacture previews.
- No claim that cached preview text is server-current when another client may have changed the conversation since the preview was captured.

## Ownership model

`ConversationRepository` remains the authoritative in-memory product owner.

Add one small durable snapshot component conceptually similar to `ConversationListCacheStore`. It is storage, not a second repository. UI never reads the cache file directly; the repository loads/reconciles the snapshot and publishes one list state.

Conceptual ownership:

`verified account/workspace scope -> ConversationRepository -> persistent list snapshot`

The persistent snapshot may contain:

- schema version;
- authoritative conversation ID required for later selection;
- title;
- last known server `update_time`;
- last known list ordering metadata needed for stable presentation;
- optional bounded preview text;
- optional preview role/source metadata;
- optional preview source message/create time and/or source list update time for freshness reasoning;
- last successful list reconciliation timestamp.

Do not persist access tokens, cookies, bearer values, raw Detail payloads, hidden reasoning/tool content or full message bodies for this feature.

## Storage direction

Use app-private Application Support / normal sandbox storage with iOS Data Protection and atomic writes. Prefer a simple versioned Codable/JSON or property-list snapshot before introducing a database dependency; list metadata + clipped previews are small enough that a database is not currently evidenced as necessary.

Use a stable account-scope-derived cache namespace. Do not expose raw account identifiers in diagnostics or cache filenames when a stable hash can provide the namespace.

Schema versioning is required so incompatible future fields can be discarded/migrated deliberately rather than decoded as ambiguous state.

## Cold-start sequence

The cold-start sequence remains auth-safe:

1. Existing WebKit warm-up/account verification runs through the accepted auth owner.
2. Before a verified account/workspace scope exists, do **not** present a previous account's conversation cache.
3. Once the current scope is verified, load that scope's persistent list snapshot and publish it immediately if valid.
4. The sidebar renders cached title/preview rows without waiting for the network list response.
5. Start exactly one normal current list request through `ConversationRepository`.
6. Reconcile the returned page into the cached list.
7. Persist the reconciled snapshot atomically.
8. If the list refresh fails, keep the valid cached rows visible and surface refresh failure non-destructively; do not blank the list and do not enter automatic retry.

Disk load may be performed off-main when useful, but cache application to repository/UI state remains deterministic and account-scoped.

## Incremental reconciliation semantics

"Incremental" initially means **client-side merge/diff of one normal list response**, not an assumed undocumented delta endpoint.

For each returned authoritative summary:

- insert an unknown conversation ID;
- update title/update time for an existing ID when changed;
- preserve the existing preview when the list response does not supply a newer preview;
- reorder according to current authoritative ordering/update time;
- update only changed presentation rows where practical instead of clearing/replacing the whole visible list.

### Important first-page rule

The current list route returns only the first 28 items while accepted evidence already shows `total` can exceed 28.

Therefore **absence from the refreshed first page does not prove deletion/archive**. Do not delete a cached older conversation solely because it is missing from page 1; it may simply have fallen below the first-page boundary.

Later `DEV-conversation-pagination` can extend this same store. Only when the client has authoritative evidence for the complete current server set, or an explicit rename/archive/delete action succeeds, may it safely prune a specific cached entry for those reasons.

If a future current response proves stable ETag/validator or delta semantics, that may be evaluated then; it is not assumed in this plan.

## Message preview source priority

### Priority 1 — same list response, only if currently proven

At implementation start, inspect **key names/type presence only** for the current list item schema in a privacy-safe diagnostic/development probe. Never log the preview value or full item payload.

If the current list response contains a user-visible preview/snippet field and real-device evidence confirms its semantics, use it. This is ideal because all visible rows receive preview data from the same one list request.

If no usable field is proven, do not add another network route and do not fan out Detail requests.

### Priority 2 — locally known authoritative visible messages

Whenever the client already obtains a Conversation Detail through normal user activity (open, Sync, Reload), derive a preview from that conversation's current visible branch and update the persistent list snapshot.

Initial text-only rule:

- use the latest visible user/assistant message in the current branch;
- never use system/tool/hidden reasoning content;
- collapse whitespace/newlines for list presentation;
- persist only a bounded clipped prefix (for example implementation-level ~120–160 user-visible characters, tuned without storing the full body);
- if no visible text exists, omit preview rather than manufacture content.

### Priority 3 — future local Send/Stream events

After production Send/Stream exists, locally created/received authoritative messages should update the same preview entry without waiting for a full list refresh.

Do not persist every streamed token. Update the preview presentation in memory as appropriate, but durable writes should occur at meaningful message/response state changes (for example an authoritative user message insertion or terminal assistant result), not token-by-token.

## Preview freshness

When a list refresh reports a newer `update_time` than the source associated with a locally cached preview and the list response itself does not provide preview content, that preview is only the **last locally known preview**.

Do not issue an automatic Detail request merely to refresh it.

The preview becomes fresh again when:

- the user opens the conversation and normal Detail loads;
- the user explicitly Syncs/Reloads it;
- future local Send/Stream updates the conversation;
- or a future proven list preview field supplies current content.

Whether a potentially stale preview remains visible or is visually suppressed is an implementation/UI tuning choice, but the product must never claim stale cached text is guaranteed server-current.

## Sidebar UI design

Recommended compact iPhone row:

- title: primary label, normally one concise line with tail truncation for dense scanning;
- preview: one secondary line below, `.secondaryLabel` style, tail truncation;
- selected state continues to use the existing list/navigation owner;
- Dynamic Type may expand row height when needed; do not hard-code a tiny fixed row that clips accessibility text.

The preview is presentation metadata only; tapping the row still selects by authoritative conversation ID.

A future setting `显示会话消息预览` should use the centralized preference owner created by `DEV-conversation-round-count`. Toggling it changes only row presentation and does not delete cached data or trigger network requests. Recommended initial product direction is On, but the implementation Work records the final default if the user gives a newer preference.

## Relationship to existing multi-conversation state

This persistent list cache is different from resident Conversation Detail state:

- resident Detail state optimizes A/B/A in-process switching;
- persistent list snapshot optimizes process cold-start/sidebar availability;
- preview cache stores only bounded list metadata, not the full resident Detail model.

Do not make the disk snapshot a competing current Conversation Detail authority.

A/B resident state may populate/update previews, but memory warning eviction of a resident Detail does not require deleting the small persistent title/preview snapshot.

## Account / privacy boundaries

- Never present a cached list before current account/workspace scope verification.
- Cache namespaces are per verified scope.
- Account change invalidates the currently published scope's list presentation before another scope is applied.
- Late network/cache callbacks from an old scope must be rejected by the same account-scope freshness principle used elsewhere.
- Explicit logout cache-deletion semantics should follow the real logout owner when that feature exists; until then, an old scope cache may remain on disk but must be unreachable from another verified scope.
- Diagnostics may record cache hit/miss/count/age/schema/version and hashed scope identity, never title, preview text or raw conversation ID.

## Diagnostics

Safe events may include:

- `listCache.load.started/completed` — hit/miss, entry count, cache age, schema;
- `listCache.scopeRejected` — hashed scope/reason only;
- `listCache.reconcile` — inserted/updated/moved/unchanged counts;
- `listCache.write` — entry count, bytes, duration;
- `listPreview.source` — `list_field` / `detail` / `send_stream`, count only;
- `listPreview.staleKnown` — count only;
- network list request/response continues using the existing diagnostics owner.

Never log cached preview/title contents.

## Runtime acceptance matrix

At minimum test exact candidate on iPhone/iOS17:

1. **Warm-cache cold start**: after account verification, cached list appears before network list completion.
2. **Cold-start refresh**: one normal list request reconciles without clearing/flickering the cached list.
3. **Offline/network failure**: cached list remains usable for navigation attempts; refresh failure is visible but non-destructive; no retry loop.
4. **No preview fan-out**: a screen with many rows produces no automatic Detail requests solely for preview population.
5. **Preview from opened Detail**: opening A once creates/updates A's clipped preview; relaunch shows it from cache without reopening A.
6. **Potentially stale remote change**: newer list update time does not trigger hidden Detail fetch.
7. **A/B account isolation**: no cached title/preview from A is shown under verified B.
8. **First-page merge**: cached older rows are not incorrectly deleted merely because refreshed page 1 contains only 28 recent rows.
9. **Large list cache**: disk read/write and UI reconciliation remain fast and do not materially block main-thread interaction.
10. **Schema corruption/version mismatch**: reject/discard only the unusable cache snapshot and continue normal network list flow; no crash/retry loop.

Later pagination/Send tests extend this matrix rather than creating another cache owner.

## Development sequencing

Default serialized route:

`DEV-multi-conversation-state -> DEV-conversation-round-count -> DEV-send-stream -> DEV-conversation-list-cache-preview`

Reason: the project priority remains the earliest daily-chat Send/Stream candidate. Persistent list caching is high-value daily-use performance work but must not delay the first proven chat loop. It also touches `ConversationRepository` / sidebar list ownership, so it should not run as an unsafe parallel task against an active unmerged Send/Stream owner.

After `DEV-send-stream` is Stable/merged, perform a normal file/state-owner conflict scan and start `DEV-conversation-list-cache-preview` before broader daily-use refinements such as Markdown export/long-conversation tuning.

If future source modularization proves the list-cache owner no longer overlaps an active task, parallelization may be reconsidered through the normal governance preflight; do not assume it now.

## Rejected routes

- Fetch Detail for every visible list row at cold start.
- Prefetch all conversations in the background merely to fill previews.
- Timer/polling-based list refresh.
- Persist full conversation JSON or full message bodies for a one-line preview requirement.
- Present last-account cache before current account verification.
- Delete cached rows merely because they are absent from the first 28-item page.
- Let cells read/write cache files directly.

## Unknown / Unverified

- Exact current server list-item preview/snippet field availability.
- Exact preview default setting until implementation/user confirmation.
- Exact cache file size/entry count in large accounts; measure before adding arbitrary disk caps.
- Full deletion/archive reconciliation until those product actions and/or complete pagination are implemented.
