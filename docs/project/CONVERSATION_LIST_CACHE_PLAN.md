# Conversation List Cache / Preview Plan

_Last planned: 2026-08-27._

## Purpose

This document defines the durable plan for persistent conversation-list startup, network-efficient reconciliation and later clipped message previews.

The user has raised persistence priority because the current client has no conversation-list data after process death until the network list request finishes, and frequent development/test relaunches can repeatedly hit the list route.

The work is now intentionally split:

- **`DEV-conversation-list-cache-core`** — early persistent list snapshot + rapid-relaunch request suppression; runs immediately after multi-conversation state becomes Stable/merged.
- **`DEV-conversation-list-preview`** — later preview-row enhancement built on the same accepted cache store; no second cache/list owner.

## Current evidence baseline

Current multi-conversation source establishes:

- `ConversationSummary` currently stores `id`, `title`, `updateTime`.
- `ConversationRepository.conversations` is in-memory only.
- cold process startup has no disk-backed list rows to render.
- current list request is `GET /backend-api/conversations?offset=0&limit=28&order=updated`.
- current parser consumes list-item `id`, `title`, `update_time`.
- accepted evidence has shown `total` can exceed the returned first page.
- account-scoped repository state is being established by `DEV-multi-conversation-state`; persistent cache work must build on that accepted owner rather than create a second account/list authority.

**Unknown / Unverified:** whether the current list payload itself contains a safe user-visible preview/snippet field.

## Shared ownership model

`ConversationRepository` remains the authoritative in-memory product owner.

Add one small durable storage component conceptually similar to `ConversationListCacheStore`. It is storage only; the sidebar never reads/writes a cache file directly.

Conceptual ownership:

`verified account/workspace scope -> ConversationRepository -> persistent list snapshot store`

The snapshot may contain:

- schema version;
- authoritative conversation ID;
- title;
- last known server `update_time` and ordering metadata;
- last successful authoritative list reconciliation time;
- later optional bounded preview text/source metadata;
- any small cache bookkeeping needed for schema/freshness.

Do **not** persist access tokens, cookies, bearer values, raw Detail mappings, hidden reasoning/tool content or full message bodies in this cache.

## Storage direction

Use app-private normal sandbox/Application Support storage with iOS Data Protection and atomic writes. A small versioned Codable JSON/property-list snapshot is preferred before adding a database dependency.

Use a stable account-scope-derived namespace; do not expose raw account identifiers in cache filenames or diagnostics when a stable hash suffices.

Schema versioning is required. Corrupt/incompatible snapshots may be discarded deliberately without crashing or starting retry loops.

# Part A — `DEV-conversation-list-cache-core`

## Goal

Make cold-start list presentation immediate after verified account scope and reduce needless repeated automatic list requests during rapid process relaunches.

This Work is intentionally **before** metadata/settings and Send/Stream so the many later development/test cycles benefit from it.

## Core cold-start sequence

1. Existing WebKit warm-up/account verification establishes the current verified scope.
2. Before a verified scope exists, never show a previous account's cached titles.
3. Once verified, load that scope's persistent snapshot and publish valid rows immediately.
4. Decide whether an automatic network list refresh is needed using the persisted last-successful-reconciliation time.
5. If refresh is needed, start one normal list request through `ConversationRepository`.
6. Incrementally reconcile returned summaries into the same repository/list state.
7. Persist the reconciled snapshot atomically.
8. If refresh fails, keep valid cached rows visible and surface the failure non-destructively; no retry loop.

Disk I/O may run off-main when appropriate, but account-scope validation and published repository/UI mutation remain deterministic.

## Rapid-relaunch freshness suppression

A cache that always triggers a list request on every launch solves blank UI but does **not** solve request pressure. Therefore cache core adds one persisted freshness decision.

Required semantics:

- no valid cache -> perform the normal automatic list refresh;
- cache exists but is older than the accepted freshness interval -> render cache immediately, then perform one automatic list refresh;
- cache was successfully reconciled very recently -> render cache and **skip that launch's automatic list refresh**;
- explicit pull-to-refresh / refresh-button action always bypasses the freshness suppression and performs one user-requested list refresh;
- after an explicit successful refresh, persist the new reconciliation timestamp;
- this is a single launch-time timestamp comparison, not a scheduled timer, polling loop, retry or watchdog.

### Freshness interval

Planning intentionally does not freeze an arbitrary long value. The implementation Work must choose/document a **small conservative rapid-relaunch window** and validate it on real device against two goals:

1. repeated build/install/relaunch cycles do not each generate an unnecessary list request;
2. ordinary users do not remain unexpectedly stale for a long interval, and manual refresh always remains available.

If later evidence proves current list responses support useful validators such as ETag/Last-Modified, conditional refresh may be evaluated. Do not assume those semantics now.

## Incremental reconciliation

"Incremental" means client-side diff/merge of the normal list response unless a current service delta API is explicitly evidenced.

For each returned authoritative summary:

- insert unknown IDs;
- update title/update time for known IDs when changed;
- reorder using current authoritative list ordering/update time;
- preserve later preview metadata if this response does not supply newer preview content;
- update changed UI rows rather than blanking the entire list where practical.

### First-page safety rule

The current request is limited to 28 rows while accepted evidence shows the server total may be larger.

Therefore **absence from refreshed page 1 is not deletion/archive evidence**. Do not remove an older cached conversation merely because it is not among the newest 28.

Only complete pagination or an explicit authoritative rename/archive/delete result may later justify pruning specific entries.

## Core non-goals

- No `ConversationDetail` or full message-body disk cache.
- No attempt to make all conversations available offline.
- No per-row Detail request fan-out.
- No preview scraping requirement for the first cache-core Candidate.
- No timer/polling refresh.
- No automatic retry chain.
- No alternate speculative list endpoint.

## Core diagnostics

Privacy-safe events may include:

- `listCache.load.started/completed` — hit/miss, entry count, schema, age;
- `listCache.autoRefreshDecision` — `missing` / `stale` / `recent_skip` / `manual_bypass`;
- `listCache.scopeRejected` — safe hashed scope/reason;
- `listCache.reconcile` — inserted/updated/moved/unchanged counts;
- `listCache.write` — entry count, bytes, duration.

Never log raw conversation IDs, titles, cached text, auth secrets or raw payloads.

## Core runtime acceptance

Exact iPhone/iOS17 candidate should cover:

1. Warm-cache cold start shows cached rows immediately after account verification and before a slow network refresh would finish.
2. Multiple rapid process relaunches inside the accepted freshness window do **not** each produce an automatic list request.
3. Manual refresh during that same window still produces exactly one requested list refresh.
4. Relaunch after the freshness window shows cache immediately and performs one normal refresh.
5. Refresh merge does not blank/flicker the list.
6. Network failure keeps valid cache visible and does not automatically retry.
7. Account A cache never appears under verified account B.
8. First-page-28 reconciliation does not delete older cached rows just because they fall below page 1.
9. Corrupt/schema-incompatible cache is rejected safely and normal network loading still works.
10. Cache read/write remains small enough not to materially block main-thread startup interaction.

# Part B — `DEV-conversation-list-preview`

## Goal

Add the one-line clipped preview under each conversation title **after cache core already exists**, reusing the exact same snapshot/store and repository list owner.

## Preview source priority

### Priority 1 — same list response, only if proven

At implementation start inspect list item **key/type presence only**. Never log preview values or full list objects.

If the current list response contains a confirmed user-visible preview/snippet field, use it from that same list request.

### Priority 2 — already-loaded Detail

If the list route has no usable preview field, whenever the client already receives a Conversation Detail through normal user activity (open, Sync, Reload), derive a bounded preview from the latest visible user/assistant message in the current branch.

Rules:

- exclude system/tool/hidden reasoning content;
- collapse whitespace/newlines;
- persist only a bounded clipped prefix, not the full body;
- omit preview if no user-visible text exists;
- never trigger a Detail solely to fill a preview.

### Priority 3 — future Send/Stream

After production Send/Stream exists, authoritative locally-created user messages and terminal assistant results update the same preview entry.

Do not persist every streamed token. Durable writes occur only on meaningful state transitions.

## Preview freshness

If a list refresh reports a newer server `update_time` but the response has no current preview content, a locally cached subtitle is only the **last locally known preview**.

Do not hide this uncertainty behind automatic Detail prefetching.

It becomes current again when the conversation is normally opened/synced/reloaded, local Send/Stream updates it, or a proven list preview field supplies new content.

## Preview UI

Compact iPhone row direction:

- title: primary one-line/tail-truncated label;
- preview: subdued one-line `.secondaryLabel` with tail truncation;
- Dynamic Type may increase row height;
- row identity/tap behavior remains authoritative conversation ID.

`显示会话消息预览` uses the centralized Preferences owner created in metadata/settings work. Toggle changes presentation only; it does not delete cache data or trigger network requests.

## Preview acceptance

- Opening A once creates/updates A preview, and a later relaunch can show it without reopening A.
- Many list rows cause no automatic Detail fan-out.
- Potentially stale preview never causes a hidden Detail request.
- Preview survives normal cache-core reconciliation when the list response has no newer preview field.
- Preview Off hides the subtitle without deleting snapshot state or changing request behavior.

## Relationship to resident multi-conversation state

Persistent list cache and resident Conversation Detail solve different problems:

- resident state: fast A/B/A switching while the process lives;
- persistent list snapshot: fast process cold-start list availability;
- preview: bounded derived list metadata.

Memory-warning eviction of a resident Detail does not delete the small persistent list snapshot.

## Account / privacy boundaries

- Never show cached list/preview before verified account/workspace scope.
- Separate cache namespace per verified scope.
- Account change removes the old scope from current presentation before another scope is applied.
- Late cache/network callbacks from an obsolete scope are rejected.
- Explicit logout deletion behavior follows the future real logout owner; until then old-scope cache may remain on disk but must be inaccessible to a different verified scope.
- No title/preview/body/auth-secret logging.

## Development sequencing

Current serialized route is:

`DEV-multi-conversation-state -> DEV-conversation-list-cache-core -> DEV-conversation-round-count -> DEV-send-stream -> earliest daily-chat Candidate -> DEV-attachments -> DEV-message-rendering -> DEV-conversation-list-preview`

The cache core is moved early because it protects the repeated development/test lifecycle itself. Preview remains later because it depends naturally on the centralized preference owner and benefits from Send/Stream data, while it is not required to solve blank cold starts or rapid-relaunch request pressure.

## Rejected routes

- Delay all persistence until the end of the roadmap.
- Treat cache-first UI as sufficient while still automatically requesting the list on every rapid relaunch.
- Fetch Detail for every visible list row.
- Prefetch all conversations in the background merely to fill previews.
- Persist full conversation JSON/full message bodies for list-cache needs.
- Present last-account cache before current scope verification.
- Delete cached rows merely because they are absent from the newest 28.
- Let cells directly read/write cache files.
- Timer/polling/retry-based refresh machinery.

## Unknown / Unverified

- Exact list-item preview/snippet field availability.
- Exact initial rapid-relaunch freshness interval until the cache-core Work starts and documents it.
- Exact large-account snapshot size/entry count; measure before inventing arbitrary disk caps.
- Full deletion/archive reconciliation until pagination/actions provide authoritative evidence.
