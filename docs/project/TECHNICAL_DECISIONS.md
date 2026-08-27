# Technical Decisions

This file records durable, evidence-backed technical decisions and rejected routes.

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client
- **Status**: Confirmed
- **Decision**: Develop a native Swift/UIKit ChatGPT client; historical WebView chat architecture is not the product source baseline.
- **Validation level**: User-confirmed + runtime-tested foundation.

### TD-002 — Previous-project history is reference-only evidence
- **Status**: Confirmed
- **Decision**: Historical endpoint names/shapes/workarounds require current revalidation before becoming contracts.

### TD-003 — TrollStore IPA distribution with iOS17 ceiling and low practical minimum
- **Status**: Confirmed
- **Decision**: TrollStore IPA; intended runtime ceiling iOS17.0; keep build minimum iOS14.0 until a real requirement changes it.

### TD-004 — Diagnostics/logging is application foundation
- **Status**: Confirmed
- **Decision**: Important async/auth/network/protocol/state operations use the accepted structured local diagnostics authority with bounded/redacted export.
- **Rejected**: passwords, OAuth codes, tokens, Cookie/Authorization values, raw conversation IDs, full chat bodies or attachment contents.

### TD-005 — WebKit is persistent login authority; native consumption is transient
- **Status**: Confirmed
- **Decision**: Default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority. Native transport may transiently copy current WebKit cookies/token into ephemeral `URLSession`; no second persistent credential store.

### TD-006 — Foundation baseline is Swift/UIKit with iOS14 minimum
- **Status**: Confirmed
- **Decision**: Swift5 + UIKit/Foundation/WebKit/OSLog/CryptoKit, no third-party dependencies, deployment target iOS14.0 until concrete need.

### TD-007 — Probe actual account/session path after usable WebKit context
- **Status**: Confirmed
- **Decision**: Account verification is not gated by native browser-oriented `/auth/login`. Current accepted sequencing is WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- **Rejected**: speculative automatic retry, UA spoof, Cloudflare bypass, duplicate gates/fallback endpoint.

### TD-008 — Parse accounts-check by ordered account identity
- **Status**: Confirmed
- **Decision**: Parse `account_ordering` + keyed `accounts`; choose first ordered entry not explicitly denied and use nested `account.account_id`.
- **Rejected**: obsolete `accounts.default.account.id` assumption.

### TD-009 — Auth bootstrap gate is satisfied for tested Plus/personal scope
- **Status**: Confirmed
- **Decision**: Authentication/account-context gate is satisfied; this does not prove conversation protocol/send/streaming.

### TD-010 — Current personal-account conversation list/detail read path is accepted
- **Status**: Confirmed
- **Decision**: For tested Plus/personal iPhone/iOS17 scope, accepted read path is transient WebKit-derived native auth, `GET /backend-api/conversations?offset=0&limit=28&order=updated`, then `GET /backend-api/conversation/{conversation_id}`. No extra `chatgpt-account-id`/browser headers were needed in accepted evidence.
- **Validation**: b7 diagnostic + b9 production real-device evidence.

### TD-011 — Official ChatGPT iOS interaction is default UI baseline
- **Status**: Confirmed
- **Decision**: Use official interaction patterns where acceptable, implemented natively rather than pixel-perfect copying.

### TD-012 — Ship small usable candidates before roadmap completeness
- **Status**: Confirmed
- **Decision**: Produce unique TrollStore candidates whenever a coherent milestone becomes testable; CI/artifact never substitutes for runtime proof.

### TD-013 — Manual sync/reload are explicit recovery actions, not automatic retry machinery
- **Status**: Confirmed / Runtime accepted for recorded recovery scope
- **Decision**: `同步最新消息`, `重载当前会话` and terminal `重新加载` operate through authoritative `ConversationRepository` and never resend/regenerate or form retry/watchdog chains.
- **Recovery-during-load**: actions remain available during ordinary selected-detail loading because a stuck load is itself a valid explicit recovery case.
- **Freshness**: a newer manual recovery supersedes the older selected-detail operation; operation generation rejects obsolete completions.
- **Request lifecycle**: if the older selected-detail network request is still active, the authoritative repository cancels/replaces that older task after the new generation takes ownership and before issuing the replacement detail request.
- **Runtime evidence**: b13 proved freshness rejection alone prevented stale mutation but concurrent replacement requests could HTTP429. Exact b15 then proved deterministic cancellation-before-replacement with no HTTP429. PR #10 merged.

### TD-014 — Reasoning UI includes expandable user-visible detail and two-pulse transition haptic
- **Status**: Confirmed
- **Decision**: When server provides user-visible reasoning detail/status, use subdued active reasoning/shimmer, expand/collapse explicit visible detail, static completed summary where supported, and two short haptic pulses on real-time reasoning->final transition. Never expose hidden chain-of-thought.

### TD-015 — Production detail diagnostics use privacy-safe hashed identity + list position
- **Status**: Confirmed
- **Decision**: Use short irreversible SHA-256-derived conversation marker + 1-based list position for correlation; never raw ID/title/body.

### TD-016 — Background completion uses public baseline then isolated TrollStore experiment
- **Status**: Confirmed
- **Decision**: After send/stream exists, first use normal iOS background-task time + local completion notification; a later isolated TrollStore true-background experiment may test minimal privileged lifetime control. No automatic resend or broad privilege grant to main authenticated app without evidence.

### TD-017 — Public default-WebKit data-store warm-up is accepted for the tested cold-start auth hydration step
- **Status**: Confirmed for tested scope
- **Date**: 2026-08-27
- **Decision**: Before first native conversation-list/account probe, initialize existing default persistent `WKWebsiteDataStore` with public APIs. Do not add hidden/shadow WebView or second persistent auth store merely to hydrate cookies.
- **Evidence**: Exact b12 iPhone/iOS17 export began at 0/0 total/matched cookies; warm-up completed with usable persisted auth and later account/list success without opening visible Login.
- **Boundary**: This proves hydration for tested persisted sessions only. It does not prove every install/update/session state and does not remove visible Login as explicit fallback after genuine failure evidence.
- **Rejected**: no hidden WebView, persisted copied secrets, automatic retry/watchdog loop, speculative auth endpoint/header fallback.

### TD-018 — Compact read-mode startup uses native primary/list root and one navigation owner
- **Status**: Confirmed for tested b14+ iPhone/iOS17 scope
- **Date**: 2026-08-27
- **Decision**: With no selected conversation, compact startup uses `.primary` conversation list as the useful root. UISplitViewController/native navigation is the sole compact list/detail navigation owner; do not layer a duplicate custom sidebar button on top.
- **Evidence**: b14 user Runtime accepted the compact startup/navigation gate; b15 preserved it.

### TD-019 — Multi-conversation data remains one account-scoped repository authority
- **Status**: Confirmed / merged Stable for the tested Plus/personal iPhone/iOS17 read-state scope; Frozen No
- **Date**: 2026-08-27
- **Decision**: Production conversation state is owned by one `ConversationRepository` scoped by the currently verified account context and keyed per authoritative conversation identity. Foreground selection is presentation state only. Selecting B must not delete A, cancel A merely because A becomes hidden, or make navigation itself a reload trigger.
- **Account boundary**: `AuthSessionStore` remains the sole auth/account-context owner. Repository operation contexts may be checked against current verified account scope but must never become authority that can restore an older scope after a newer account transition. Persistent auth secrets remain solely in default WebKit storage.
- **Resident model boundary**: retain only current evidence-backed conversation data/metadata; do not retain raw multi-megabyte payloads, use UIKit hierarchy as cache, or create one repository per screen/conversation.
- **Memory boundary**: b19 real-device evidence through 8 residents does not justify an arbitrary normal LRU capacity; memory-warning trimming remains the current evidence-backed policy.
- **Runtime/merge evidence**: b17-b21 established resident/coalescing/scroll/title/replacement behavior; PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`.
- **Conditional boundaries**: natural failed-resident navigation, supported account switch, non-personal workspace identity and missing-anchor-message discard remain Unknown / Unverified where applicable.
- **Rejected**: stale operation context re-adopting account scope; selection-driven cancellation; separate screen repositories; retained VC/cell cache; navigation-triggered reload; speculative retry/timer/watchdog/global rate limiter; arbitrary LRU capacity.

### TD-020 — Per-conversation scroll presentation is semantic anchor or follow-tail, not one raw offset
- **Status**: Historical-reading anchor Runtime accepted on exact b18 for tested iPhone/iOS17 matrix; active-response follow-tail pending Send/Stream
- **Date**: 2026-08-27
- **Decision**: Each conversation owns lightweight scroll presentation semantics independently of conversation data. Historical reading preserves a semantic message anchor plus relative visual offset where practical. Future active-response follow-tail must consume the authoritative per-conversation Send/Stream response owner rather than invent UI streaming authority.
- **Boundary**: anchored-message disappearance remains Runtime-unexercised; future hidden-response follow-tail has separate Send/Stream acceptance gates.

### TD-021 — Conversation-list cache may provisionally present the last verified scope's titles before current verification, but never authorize account-bound operations
- **Status**: Confirmed / exact b23 Runtime accepted for recorded Plus/personal iPhone/iOS17 cache-core scope; merge pending
- **Date**: 2026-08-28
- **Problem evidence**: Exact b22 persisted/loaded list snapshots correctly, but visible cache publication waited until account verification completed (~4.4–5.0 s). With network disabled, auth transport failed first (`NSURLErrorDomain -1005/-1004`), so cache was never presented and UI incorrectly fell back to Login/account verification. Manual refresh also lacked visible terminal feedback.
- **Decision**: Keep `ConversationRepository` as the sole authoritative list/conversation owner and `AuthSessionStore` as the sole verified account owner. A storage-only `ConversationListCacheStore` may persist a protected 64-hex SHA-256 last-successfully-verified scope namespace hint and, on **automatic cold start only**, use it to provisionally publish that scope's cached **list titles** before current network account verification completes.
- **Authority boundary**: The namespace hint is cache bookkeeping only. It cannot establish a verified account, transport, Detail authority or send authority. Provisional/offline rows must not start Detail until current scope is verified. A newly verified different scope or confirmed unauthenticated/unavailable result rejects the provisional presentation. Temporary auth transport failure may retain it as offline list presentation without automatic retry.
- **Freshness / refresh**: Exact b23 accepts the current 60-second rapid-relaunch window for this use case. Recent cache may skip that launch's automatic list request; stale cache performs one normal refresh; manual refresh always bypasses suppression and emits exactly one requested list refresh. UI feedback uses `正在刷新会话列表…`, `已刷新 · N 条`, or retained-cache failure `刷新失败 · 当前显示缓存`.
- **First-page rule**: Page-1 absence is not deletion evidence. Exact b23 Runtime proves a real server response of 28 with `total=29` preserves one off-page cached row (`preservedOffPageCount=1`, `resultCount=29`) across reconciliation.
- **Runtime evidence**: b23 rapid relaunch loads 29 provisional rows in ~4 ms before ~4.5 s matching account verification and then chooses `recent_skip`; offline relaunch loads 29 rows in ~4 ms, natural `-1005` auth failure chooses `offline_cache`, and list load succeeds from cache. Screenshot directly confirms the retained list plus centered `刷新失败 · 当前显示缓存` after offline manual refresh. User reports no new issue in the tested matrix.
- **Privacy/storage**: No raw account/user IDs, cookies, tokens, bearer values, Detail mappings or message bodies are persisted. Storage remains app-private Application Support with Data Protection, schema versioning and atomic writes.
- **Conditional boundaries**: supported real account-switch mismatch, provisional-row Detail-block tap, corrupt/schema rejection, iPad, runtime below iOS17 and non-personal workspace identity remain Unknown / Unverified.
- **Rejected**: persisted copied auth secrets; raw account identity scope hint; second list/account repository; per-row Detail prefetch; timer/polling/retry/watchdog; alternate list/auth endpoints; treating temporary transport failure as confirmed logout; allowing provisional cache to authorize Detail.

## Rule

Do not write speculation here as fact. Historical plans, CI and Artifacts are not runtime proof.