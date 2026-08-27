# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-27._

## Purpose

This is the durable implementation sequence for the iOS-native ChatGPT client. Current source, CI/artifact evidence, real-device evidence, explicit user requirements and specialized plans under `docs/project/` take priority over stale historical wording.

Current constraints: native UIKit iOS client; TrollStore IPA; primary tested runtime iPhone/iOS17; deployment target iOS14; current ChatGPT private/internal behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns unless an explicit requirement says otherwise.
4. Do not add speculative retry/fallback/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency operations such as Copy and image/file transfer outrank lower-frequency polish once their dependencies exist.
7. Persistent list caching is now an early infrastructure/performance task because repeated cold starts otherwise begin with no list data and may cause unnecessary repeated list requests during development/testing.

## Usability milestones

- **V0.1 read-use**: native shell + list/detail + manual recovery + accepted cold-start auth warm-up.
- **V0.1 cache-use increment**: V0.1 + account-scoped persistent conversation-list snapshot so cold start can show known rows immediately and rapid relaunches can avoid needless automatic list refreshes when the cache was just synchronized.
- **V0.2 chat-use**: stable multi-conversation ownership + metadata/preferences + message Copy + answer navigation + text send/new conversation + stream/stop/reasoning/haptics.
- **V0.2 attachment-use increment**: image/file sending + assistant-file tap-download-share.
- **V0.3 refinement**: Markdown/code rendering, conversation-list previews, Markdown export, long-conversation tuning, pagination/search/download manager and remaining daily-use features.

## Completed foundations

### Phase 1 — `DEV-app-foundation`
Completed / merged / Stable.

### Phase 2 — `DEV-auth-bootstrap`
Completed / merged / Stable for tested scope. Default persistent `WKWebsiteDataStore` remains the sole persistent auth-secret authority.

### Phase 3 — `DEV-protocol-read`
Completed / merged / Stable for accepted diagnostic read scope.

### Phase 4 — `DEV-native-read-path`
Completed / merged / Stable for tested b9 scope. `ConversationRepository` is the production conversation owner.

### Phase 5 — `DEV-conversation-recovery`
Completed / merged / Stable for recorded Plus/personal iPhone/iOS17 scope. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`; exact evidence remains in `BUILD_TEST_INDEX.md`.

### Phase 6 — `DEV-multi-conversation-state`

**Completed / merged / Stable for the recorded Plus/personal iPhone/iOS17 read-state scope.** PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`; final Runtime Candidate is `DEV-multi-conversation-state-0.1.0-b21` with exact product/config source `6b50ead167bfde305d2ad58dd16fee6edaabf597`. Frozen remains No.

Accepted scope includes account-scoped per-conversation resident state, stale-operation protection, same-target coalescing/replacement ownership, minimum current-node identity, independent historical scroll presentation, measured 0→8 resident process footprint, selected-title lifecycle ordering, and same-target Reload replacement-under-load/hidden-rejoin behavior.

Evidence boundaries retained after closure: natural failed-resident navigation, supported account-switch purge, non-personal workspace identity and missing-anchor-message discard remain Unknown / Unverified where applicable; normal LRU capacity remains unfrozen because current real-device evidence does not justify one. Future active-response follow-tail belongs to Send/Stream.

### Conversation-entry scroll semantics

- First visible presentation with **no valid saved reading anchor** defaults to the latest message / bottom of the current branch.
- This first placement does not visibly animate from the top through a long conversation.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A rather than forcing bottom.
- Sync/Reload preserve an established reading anchor through the existing presentation owner.
- Future Send/Stream follow-tail applies only while the user remains at/near the latest edge; deliberate history browsing must not be pulled back to bottom.

## Phase 7 — `DEV-conversation-list-cache-core`

### Why this is moved earlier

This is the **first task after the now-Stable/merged multi-conversation baseline**, before metadata/settings and before Send/Stream.

The previous plan delayed list persistence until after the first chat loop. That leaves every development/test cold start with no local list data and still causes an automatic list request per relaunch. The user explicitly wants this risk reduced earlier.

Durable design: `docs/project/CONVERSATION_LIST_CACHE_PLAN.md`.

### Core scope

- Add one account/workspace-scoped persistent list snapshot behind `ConversationRepository`.
- Persist bounded list metadata only: schema version, conversation ID, title, update time/order metadata, last successful reconciliation time, and fields required for future bounded preview integration.
- After the current account scope is verified, load the matching snapshot and publish cached rows before waiting for network.
- Never display another account's cache before scope verification.
- No full `ConversationDetail`, raw mapping JSON or full message-body disk cache in this Work.
- No per-row Detail prefetch and no automatic polling/retry loop.
- Current first-page `limit=28` absence never proves deletion; preserve older cached rows unless later complete pagination or an explicit authoritative action proves removal.

### Rapid-relaunch request suppression

Cache-first rendering alone is insufficient to reduce frequent restart traffic, so the core Work must persist the time of the last successful authoritative list reconciliation and apply a **short freshness window** on launch:

- valid cache missing/invalid -> perform the normal list request;
- valid cache older than the accepted freshness window -> show cache immediately, then perform one normal list request;
- valid cache that was successfully synchronized very recently -> show it and **skip that launch's automatic list request**;
- explicit pull-to-refresh / refresh-button action always bypasses this suppression and performs one user-requested list refresh;
- this is a one-time timestamp comparison, not a timer, polling loop, retry or watchdog.

The exact initial freshness interval is intentionally not frozen by planning. The implementation Work must choose/document a small conservative value and validate it on device; do not silently invent a long stale interval. If current response evidence later proves usable ETag/validator semantics, conditional refresh may be evaluated but is not assumed.

### Acceptance focus

- Warm-cache cold start shows known rows immediately after verified scope.
- Several rapid process relaunches inside the accepted freshness window do not each emit an automatic list request.
- Manual refresh still performs a request immediately.
- Once cache ages beyond the window, one normal refresh occurs and reconciles without blanking/flicker.
- Network failure leaves valid cached rows visible; no automatic retry.
- Account A cache never appears under verified account B.

## Phase 8 — `DEV-conversation-round-count`

### User-facing bundle

Implement after cache core and before Send/Stream:

- `聊天 · N轮` / `工作 · N轮` derived from authoritative visible user turns;
- per-user/per-assistant message timestamps from authoritative `createTime` when available;
- adaptive `上一轮回答` / `下一轮回答` floating navigation with native animated scrolling;
- basic one-tap Copy for visible user and assistant message text;
- first centralized Preferences owner for these toggles and later settings.

### Shared derivation / behavior

- Round count and answer navigation share one derived active-branch round projection, not parallel mutable counters.
- A visible user message starts a round; the first visible assistant reply before the next user message is that round's answer anchor.
- Tool/reasoning/system nodes do not create rounds.
- Recompute answer anchors only when authoritative visible messages change, not on every scroll callback.
- Quick-jump animation is native scroll-container animation, not timer-stepped fake scrolling.
- Copy never includes hidden reasoning/tool/system material and never triggers network requests.

## Phase 9 — `DEV-send-stream`

Evidence the current text Send/new-conversation/stream/stop protocol, then implement composer, pending-to-authoritative identity handoff, per-conversation response lifecycle, incremental stream presentation, Stop, user-visible reasoning interaction and required reasoning-to-final haptic behavior.

- No global response owner.
- A hidden conversation may continue responding while another is visible.
- Sync/Reload never resend messages.
- If user is at/near latest, stream may follow tail; once user intentionally browses history, stream must not steal the viewport.

**As soon as exact real-device text chat/stream works, issue the earliest practical daily-chat Candidate.**

## Phase 10 — `DEV-attachments`

High-priority immediately after accepted text Send/Stream. Durable design: `ATTACHMENT_TRANSFER_PLAN.md`.

Core first Candidate:

- native photo/image picker;
- native document/file picker;
- per-conversation pending attachment cards/thumbnails and removal before Send;
- evidence current upload/asset/message attachment protocol before implementation;
- assistant user-visible file cards;
- tap file -> explicit file-backed download -> app-private local file -> immediate `UIActivityViewController` share sheet;
- visible transfer failure, explicit user retry only; no automatic retry loop;
- full custom download manager does not block this phase.

## Phase 11 — `DEV-message-rendering`

Improve development-chat readability:

- Markdown paragraphs/headings/lists/links;
- inline/fenced code;
- code-block one-tap Copy while retaining whole-message Copy;
- tables when needed;
- no full-conversation reparse/reload on every streamed token.

## Phase 12 — `DEV-conversation-list-preview`

This is now the **preview/UI enhancement built on the already-accepted cache core**, rather than the first introduction of persistence.

- Reuse the same persistent list snapshot/store and repository owner from `DEV-conversation-list-cache-core`.
- First verify whether the current list response itself exposes a safe user-visible preview/snippet field.
- If not, populate bounded previews only from Detail/Sync/Reload already obtained through normal user activity and from later authoritative Send/Stream events.
- Never issue one Detail request per row solely to manufacture previews.
- Show one clipped secondary preview line and use the centralized `显示会话消息预览` preference.
- Streaming must not write preview data to disk token-by-token.

Do not create a second list/cache store for this phase.

## Phase 13 — `DEV-markdown-export`

Export the authoritative current user-visible branch to Markdown; never scrape mounted cells or expose hidden/internal reasoning/tool content.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / Markdown-layout timing and optimize only evidenced bottlenecks.

## Phase 15 — remaining daily-use features

Split into isolated Work IDs as dependencies stabilize:

- `DEV-download-manager` — persistent download history/progress/re-share/storage controls;
- conversation pagination/load-more using the same list-cache/reconciliation owner;
- background wait/completion notification and later TrollStore true-background experiment;
- search;
- rename/archive/delete;
- edit/regenerate/branch switching;
- model selection/temporary chat;
- settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other current capabilities, each only with current protocol/UI evidence.

## Current next action

The multi-conversation phase is complete. The serialized near-term route is:

`DEV-conversation-list-cache-core -> DEV-conversation-round-count -> DEV-send-stream -> earliest daily-chat Candidate -> DEV-attachments -> DEV-message-rendering -> DEV-conversation-list-preview`

This document records priority only. It does not activate `DEV-conversation-list-cache-core`; that Work must establish its own checkpoint/branch/candidate identity in the development session that owns it.
