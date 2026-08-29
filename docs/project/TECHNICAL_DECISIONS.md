# Technical Decisions

This file records durable, evidence-backed technical decisions and rejected routes. Detailed historical evidence remains available in Git history and `BUILD_TEST_INDEX.md`; current decisions below are the active durable contracts.

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client
- **Status**: Confirmed
- **Decision**: Develop a native Swift/UIKit ChatGPT client; historical WebView chat architecture is not the product source baseline.

### TD-002 — Previous-project history is reference-only evidence
- **Status**: Confirmed
- **Decision**: Historical endpoint names/shapes/workarounds require current revalidation before becoming contracts.

### TD-003 — TrollStore IPA distribution with iOS17 primary tested ceiling and iOS14 build minimum
- **Status**: Confirmed
- **Decision**: TrollStore IPA; primary real-device evidence is iPhone/iOS17. Keep build minimum iOS14.0 until concrete need changes it.

### TD-004 — Diagnostics/logging is application foundation
- **Status**: Confirmed
- **Decision**: Important async/auth/network/protocol/state operations use the accepted structured local diagnostics authority with bounded/redacted export.
- **Rejected**: passwords, OAuth codes, tokens, Cookie/Authorization values, raw conversation IDs, full titles/chat bodies or attachment contents.

### TD-005 — WebKit is persistent login authority; native consumption is transient
- **Status**: Confirmed
- **Decision**: Default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority. Native transport may transiently copy current WebKit cookies/token into ephemeral `URLSession`; no second persistent credential store.

### TD-006 — Foundation baseline is Swift/UIKit with iOS14 minimum
- **Status**: Confirmed
- **Decision**: Swift5 + UIKit/Foundation/WebKit/OSLog/CryptoKit, no third-party dependencies, deployment target iOS14.0 until concrete need.

### TD-007 — Probe actual account/session path after usable WebKit context
- **Status**: Confirmed
- **Decision**: Account verification is not gated by native browser-oriented `/auth/login`. Accepted sequencing is WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- **Rejected**: speculative automatic retry, UA spoof, Cloudflare bypass, duplicate gates/fallback endpoint.

### TD-008 — Parse accounts-check by ordered account identity
- **Status**: Confirmed
- **Decision**: Parse `account_ordering` + keyed `accounts`; choose first ordered entry not explicitly denied and use nested `account.account_id`.

### TD-009 — Auth bootstrap gate is satisfied for tested Plus/personal scope
- **Status**: Confirmed
- **Decision**: Authentication/account-context gate is satisfied for the recorded scope; this does not prove later private protocol surfaces.

### TD-010 — Current personal-account conversation list/detail read path is accepted
- **Status**: Confirmed
- **Decision**: For tested Plus/personal iPhone/iOS17 scope, accepted read path is transient WebKit-derived native auth, `GET /backend-api/conversations?offset=0&limit=28&order=updated`, then `GET /backend-api/conversation/{conversation_id}`. No extra account/browser headers were needed in accepted evidence.

### TD-011 — Official ChatGPT iOS interaction is default UI baseline
- **Status**: Confirmed
- **Decision**: Use official interaction patterns where acceptable, implemented natively rather than pixel-perfect copying.

### TD-012 — Ship small usable candidates before roadmap completeness
- **Status**: Confirmed
- **Decision**: Produce unique TrollStore candidates whenever a coherent milestone becomes testable; CI/Artifact never substitutes for Runtime proof.

### TD-013 — Manual sync/reload are explicit recovery actions, not automatic retry machinery
- **Status**: Confirmed / Runtime accepted for recorded recovery scope
- **Decision**: `同步最新消息`, `重载当前会话` and terminal `重新加载` operate through authoritative `ConversationRepository` and never resend/regenerate or form retry/watchdog chains. Newer same-target recovery cancels/replaces the older active request before replacement ownership proceeds; generation/freshness rejects obsolete completions.
- **Evidence**: b15/b21 recorded cancellation/rejoin behavior; PR #10 merged.

### TD-014 — Reasoning UI includes expandable user-visible detail and two-pulse transition haptic
- **Status**: Confirmed requirement; implementation belongs later send/stream work
- **Decision**: When server provides user-visible reasoning detail/status, use subdued active reasoning/shimmer, explicit expand/collapse visible detail and two short haptic pulses on real-time reasoning→final transition. Never expose hidden chain-of-thought.

### TD-015 — Production detail diagnostics use privacy-safe hashed identity + list position
- **Status**: Confirmed
- **Decision**: Use short irreversible SHA-256-derived conversation marker + 1-based list position for correlation; never raw ID/title/body.

### TD-016 — Background completion uses public baseline then isolated TrollStore experiment
- **Status**: Confirmed plan
- **Decision**: After send/stream exists, first use normal iOS background-task time + local completion notification; any TrollStore true-background experiment remains isolated. No automatic resend or broad privilege grant without evidence.

### TD-017 — Public default-WebKit data-store warm-up is accepted for tested cold-start auth hydration
- **Status**: Confirmed for recorded scope
- **Decision**: Before first native list/account probe, initialize the existing default persistent `WKWebsiteDataStore` using public APIs. Do not add hidden/shadow WebView or second persistent auth store merely to hydrate cookies.

### TD-018 — Compact read-mode startup uses native primary/list root and one navigation owner
- **Status**: Confirmed for tested iPhone/iOS17 scope
- **Decision**: With no selected conversation, compact startup uses `.primary` conversation list as the useful root. `UISplitViewController`/native navigation is the sole compact list/detail navigation owner.

### TD-019 — Multi-conversation data remains one account-scoped repository authority
- **Status**: Confirmed / merged Stable for recorded read-state scope; Frozen No
- **Decision**: One `ConversationRepository` owns production conversation state scoped by verified account context and keyed per authoritative conversation identity. Foreground selection is presentation only; selecting B does not delete A or cancel valid hidden A work. Do not retain raw graph payloads or UIKit hierarchies as cache. No arbitrary normal LRU capacity; memory-warning trimming remains evidence-backed policy.

### TD-020 — Per-conversation scroll presentation is semantic anchor or follow-tail, not one raw offset
- **Status**: Historical-reading anchor Runtime accepted; active-response follow-tail pending Send/Stream
- **Decision**: Each conversation owns lightweight scroll presentation semantics independently of conversation data. Historical reading preserves an authoritative message anchor plus display position/relative offset where practical. Future follow-tail must consume the authoritative per-conversation response owner.

### TD-021 — Conversation-list cache may provisionally present last verified titles before current verification, but never authorize account-bound operations
- **Status**: Confirmed / merged Stable for recorded cache-core scope; Frozen No
- **Decision**: `ConversationListCacheStore` is storage only behind `ConversationRepository`. Automatic cold start may provisionally publish cached titles using a privacy-safe last-verified scope namespace hint, but this never establishes verified account/transport/Detail/send authority. Current 60-second rapid-relaunch window, offline retained list behavior, manual refresh bypass and first-page `28 + 1 -> 29` preservation are accepted.
- **Phase 8 extension**: authoritative `total=29` caps stale excess cached rows (`30 -> 29`, repeated `29/29`) without creating a second list owner; right-top refresh must not create persistent blank top inset.

### TD-022 — Long-conversation presentation uses deterministic derived geometry; round navigation consumes it
- **Status**: Confirmed / Runtime accepted / merged Stable on exact b38 recorded iPhone/iOS17 scope; Frozen No
- **Date**: 2026-08-29
- **Problem evidence**: Exact b36 retained severe long-conversation stutter in quick navigation and ordinary right-side scroll-indicator dragging. 47 direct-position samples had median ~187ms, P90 ~780ms and max ~3952ms. One 161-visible-message table initially reported ~13.8k points of bottom geometry and later ~154.6k points as giant estimated/self-sized message rows became realized.
- **Decision**: Keep authoritative messages solely in `ConversationRepository`; derive an ephemeral `ConversationMessagePresentationProjection` that splits very long plain-text messages into bounded display chunks, computes deterministic row heights/prefix offsets for the current layout width, maps authoritative messages to first display rows, and drives `ConversationMessageCell` with deterministic manual frame layout. This projection is presentation-only and is rebuilt when authoritative messages/layout width require it; it is not a persistent second message/row-height store.
- **Copy/semantics boundary**: Copy reads the complete authoritative message; round count/semantic targets still come from one `ConversationRoundProjection`; each visible authoritative user message starts a round. Display chunking never creates semantic turns.
- **Navigation decision**: Stable b38 uses the already-derived O(1) target offset and one cancellable `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)` from the current viewport to the target. Short/long distances use one method. Rapid taps retarget from current visual position; real drag immediately retakes ownership. No pre-jump teleport, `scrollToRow` geometry discovery or end correction snap is part of the accepted path.
- **Runtime evidence**: Exact b37 user feedback **“这次确实不卡了”** accepted the deterministic geometry/performance direction. Exact b38 then restored genuine continuous full-distance animation while preserving that geometry; user feedback **“没问题了”** accepted the combined result.
- **Exact accepted identity**: b38 tested product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Runtime Artifact `9708425762`, IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- **Merge evidence**: PR #27 final head `57b3efe576dbf187171439a68d6d2dfe2fba0ebc`; tested product→final head delta was docs-only; PR merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- **Rejected without new evidence**: reverting to one giant whole-message self-sizing UILabel with unstable estimated geometry; persistent cross-detail row-height cache; pre-jump direct teleport; `scrollToRow` as target-geometry discovery; final correction snap; debounce/timer/watchdog/retry; alternate semantic index or second repository.

## Rule

Do not write speculation here as fact. Historical plans, CI and Artifacts are not Runtime proof. Stable does not mean Frozen.
