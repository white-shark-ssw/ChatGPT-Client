# Conversation List Cache / Preview Plan

_Last updated: 2026-08-28._

## Purpose

This document defines the durable conversation-list persistence baseline and the later preview-row enhancement. The work remains intentionally split:

- **`DEV-conversation-list-cache-core`** — persistent summary snapshot + rapid-relaunch suppression. Exact b23 is merged Stable for the recorded Plus/personal iPhone/iOS17 matrix via PR #24.
- **`DEV-conversation-list-preview`** — later clipped message-preview enhancement built on the same accepted store and repository owner.

## Ownership model

`ConversationRepository` remains the authoritative in-memory product owner. `ConversationListCacheStore` is storage only; sidebar cells never read/write cache files directly.

Current persistent cache may contain:

- schema version;
- authoritative conversation ID;
- title;
- last known server `update_time` and ordering;
- last successful authoritative list reconciliation time;
- privacy-safe cache bookkeeping, including the accepted last-successfully-verified scope namespace hint;
- later optional bounded preview metadata owned by `DEV-conversation-list-preview`.

Do **not** persist access tokens, cookies, bearer values, raw account/user IDs for cache routing, Detail mappings, hidden reasoning/tool content or full message bodies.

## Storage baseline

Accepted b23 uses app-private Application Support storage, iOS Data Protection, atomic writes and a versioned Codable JSON snapshot. Cache filenames use a stable SHA-256-derived account-scope namespace rather than raw identifiers.

A protected `last-verified-scope.txt` stores only that 64-hex SHA-256 namespace. It is cache bookkeeping, not account/auth authority and contains no credential material.

Corrupt/incompatible snapshots may be deliberately discarded without crash, retry loop, polling or watchdog. Exact corrupt/schema-rejection Runtime remains conditional Unverified until naturally exercised or separately tested with a safe dedicated fixture.

# Part A — `DEV-conversation-list-cache-core`

## Accepted goal

Make list rows available immediately on warm process relaunch, preserve a useful list during temporary offline auth-transport failure, and reduce repeated automatic list requests during rapid relaunches without creating a second list/account authority.

## Accepted cold-start sequence

The original plan required verified scope before showing any cache. b22 real-device evidence showed that ordering left the list blank for ~4.4–5.0 seconds and made offline cold start bypass an otherwise valid cache. Exact b23 replaced that rule with the following accepted boundary:

1. Existing default-WebKit warm-up still begins normally.
2. On **automatic cold start only**, if there is a valid last-successfully-verified scope namespace hint, load that snapshot immediately and provisionally publish **list titles only**.
3. Start normal account verification through the existing `AuthSessionStore` path; the cache hint never establishes account or transport authority.
4. While the list is provisional/offline, rows must not start Detail. A tap may explain that current account verification is required.
5. If verification succeeds for the same scope, keep the published rows and apply normal freshness logic.
6. If a different scope verifies, reject/clear the provisional old-scope presentation before applying the verified scope.
7. If auth is confirmed unavailable/unauthenticated, reject provisional rows and normal Login/account-verification UI may appear.
8. If account verification fails only because of temporary network transport failure, retain the valid provisional rows as offline list presentation; do not retry automatically.
9. When refresh is needed, perform one normal list request through `ConversationRepository`, reconcile into the same repository state and persist atomically.
10. A failed refresh never clears already-valid cached rows.

This provisional presentation exception is intentionally narrow: it improves list availability but cannot authorize Detail/send/other account-bound operations.

## Rapid-relaunch freshness suppression

Accepted semantics:

- no valid cache -> normal automatic list refresh after usable verified context;
- stale cache -> show cache immediately, then one automatic list refresh;
- recently reconciled cache -> show cache and skip that launch's automatic list refresh;
- explicit pull-to-refresh/refresh button always bypasses suppression and performs one requested refresh;
- successful refresh persists the new reconciliation timestamp;
- one launch-time timestamp comparison only; no timer/polling/retry/watchdog.

### Freshness interval

Exact b22/b23 uses **60 seconds**. Real-device evidence accepts that value for the current rapid-relaunch development/use case: b23 rapid relaunch at ~18–23 seconds selected `recent_skip`, while stale-cache paths perform one refresh. It remains a small implementation baseline rather than a promise that the value can never change if later product evidence justifies adjustment.

## Incremental reconciliation

For each returned authoritative summary:

- insert unknown IDs;
- update title/update time for known IDs;
- place returned page ordering first;
- retain older cached IDs absent from the returned first page;
- persist the reconciled ordered result.

### First-page safety — Runtime accepted

Current list request remains `GET /backend-api/conversations?offset=0&limit=28&order=updated`. Absence from page 1 is **not** deletion/archive evidence.

Exact b23 real-device diagnostics exercise this path with a genuine off-page cached row: server returns `pageCount=28`, `totalCount=29`; reconciliation records `preservedOffPageCount=1` and `resultCount=29`, then writes the 29-entry cache. Two later manual refreshes repeat the same preservation. This rule is Runtime accepted for the recorded tested scope.

Only complete pagination or explicit authoritative rename/archive/delete evidence may later justify pruning specific entries.

## Manual refresh UI contract

Manual refresh is user-owned and bypasses freshness suppression. Accepted b23 presentation:

- active: `正在刷新会话列表…`;
- success: `已刷新 · N 条`;
- failure while cached rows remain: `刷新失败 · 当前显示缓存`;
- confirmed unauthenticated state may still expose Login/account verification;
- temporary network failure with cached rows must not cover the list with misleading Login controls.

The prompt is the centered navigation-bar text above the `ChatGPT` title. b23 screenshot directly confirms the offline failure presentation.

## Core diagnostics

Privacy-safe accepted events include:

- `listCache.provisional.started/completed`;
- `listCache.load.started/completed`;
- `listCache.autoRefreshDecision` with `missing` / `stale` / `recent_skip` / `manual_bypass` / `offline_cache`;
- `listCache.scopeRejected`;
- `listCache.reconcile`;
- `listCache.write`.

Never log raw conversation IDs, titles, cached text, auth secrets or raw payloads.

## b22 → b23 Runtime evidence

### b22 — partial/failing predecessor

b22 proved disk snapshot write/read, 60-second recent suppression, stale one-refresh and manual bypass. It failed the visible product acceptance because cache reading occurred only after slow account verification, offline auth transport failure prevented cache use, and manual refresh had no explicit terminal feedback.

### b23 — accepted merged baseline

Exact Candidate `DEV-conversation-list-cache-core-0.1.0-b23`, source `d2af0fc157f6e2d037636c55f963c18071a332d5`, Runtime Run `33101116431`, Artifact `9658508764`.

User-supplied iPhone/iOS17 diagnostics show:

- provisional 29-row cache load in `4.09 ms` before ~4521 ms matching account verification, followed by `recent_skip` and no automatic list request;
- offline process relaunch loads 29 rows in `4.30 ms`; natural `NSURLErrorDomain -1005` auth failure selects `offline_cache`, and list load completes from cache in `31.58 ms`;
- screenshot confirms rows remain visible with `刷新失败 · 当前显示缓存` after offline manual refresh;
- online manual refresh uses `manual_bypass`, performs exactly one list request and writes reconciled cache;
- first-page safety preserves one true off-page item (`28 + 1 -> 29`);
- user reports the tested b23 behavior appears problem-free.

PR #24 merge-view Run `33103769517` / Job `98628067286` checked out merge view `26297ff0683966c2c82fd7a8a95f53f1ad51d3d6`, compiled/package-tested successfully and produced Artifact `9659600955`. PR #24 then merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`. The merge-view Artifact is CI evidence only and does not replace the exact real-device Runtime Artifact.

## Core accepted / conditional matrix

Accepted on exact b23 for tested Plus/personal iPhone/iOS17:

1. warm relaunch cached rows appear before slow current account verification completes;
2. rapid relaunch inside 60 seconds suppresses automatic list request;
3. stale cache performs one refresh;
4. temporary offline auth transport failure retains cached rows with no automatic retry;
5. manual refresh bypasses suppression;
6. offline manual refresh preserves rows and shows explicit failure/cache feedback;
7. first-page absence preserves real off-page cached rows;
8. observed cache I/O is small (provisional reads around 4 ms; scoped reads/writes around low milliseconds to ~20 ms in supplied run).

Still conditional Unknown / Unverified:

- supported real account switch / verified-scope mismatch Runtime path;
- provisional-row tap/Detail-block Runtime path (source/CI-defined);
- corrupt/schema-incompatible cache rejection Runtime;
- iPad, runtime below iOS17 and non-personal workspace identity.

Do not manufacture fake account transitions, destructive user-data corruption or unsupported flows merely to fill those cells.

## Core non-goals / rejected routes

- No `ConversationDetail` or full message-body disk cache.
- No offline claim for all conversation Detail content.
- No per-row Detail fan-out.
- No preview scraping in cache core.
- No timer/polling refresh or automatic retry chain.
- No alternate speculative list/auth endpoint.
- No second repository/list/account authority.
- No persisted copied auth secrets.
- No raw account/user identity in cache filenames or scope hint.
- No deletion merely because an item is absent from newest 28.

# Part B — `DEV-conversation-list-preview`

## Goal

Add a one-line clipped preview under each conversation title, reusing the merged cache-core snapshot/store and repository list owner.

## Preview source priority

### Priority 1 — same list response, only if proven

At implementation start inspect list-item **key/type presence only**. Never log preview values or full list objects. If the current list response contains a confirmed user-visible preview/snippet field, use it from that same list request.

### Priority 2 — already-loaded Detail

If the list route has no usable preview field, whenever the client already receives a Conversation Detail through normal activity (open, Sync, Reload), derive a bounded preview from the latest visible user/assistant message in the current branch.

Rules:

- exclude system/tool/hidden reasoning content;
- collapse whitespace/newlines;
- persist only a bounded clipped prefix, not full body;
- omit preview if no user-visible text exists;
- never trigger a Detail solely to fill preview.

### Priority 3 — future Send/Stream

After production Send/Stream exists, authoritative locally-created user messages and terminal assistant results update the same preview entry. Do not persist every streamed token; durable writes occur only on meaningful transitions.

## Preview freshness / UI

If a list refresh reports newer `update_time` but has no current preview content, cached subtitle is only the last locally known preview. Do not hide that uncertainty behind automatic Detail prefetching.

Compact row direction remains title + subdued one-line secondary preview, Dynamic-Type-friendly, with authoritative conversation ID as row identity.

A future `显示会话消息预览` preference changes presentation only; it does not delete cache data or trigger network requests.

## Preview acceptance

- Opening A once creates/updates A preview, and later relaunch can show it without reopening A.
- Many rows cause no automatic Detail fan-out.
- Potentially stale preview never causes hidden Detail request.
- Preview survives cache-core reconciliation when list response supplies no newer preview.
- Preview Off hides subtitle without deleting snapshot state or changing requests.

## Relationship to resident state

- resident Detail: fast A/B/A switching while process lives;
- persistent list snapshot: fast process cold-start/offline list availability;
- preview: bounded derived list metadata.

Memory-warning eviction of resident Detail does not delete the small persistent list snapshot.

## Development sequencing

`DEV-conversation-list-cache-core` is complete and merged. The next serialized route is:

`DEV-conversation-round-count -> DEV-send-stream -> earliest daily-chat Candidate -> DEV-attachments -> DEV-message-rendering -> DEV-conversation-list-preview`

## Remaining Unknown / Unverified for preview

- Exact list-item preview/snippet field availability.
- Exact large-account snapshot size/entry count; measure before inventing arbitrary disk caps.
- Full deletion/archive reconciliation until pagination/actions provide authoritative evidence.