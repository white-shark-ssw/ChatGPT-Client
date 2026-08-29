# Technical Decisions

This file records durable, evidence-backed technical decisions and rejected routes. Detailed historical evidence remains available in Git history and `BUILD_TEST_INDEX.md`; current decisions below are the active durable contracts.

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client
- **Status**: Confirmed; qualified by TD-024 for ChatGPT-account Send
- **Decision**: Develop a native Swift/UIKit ChatGPT client as the product shell and native read/navigation baseline. Historical hidden-WebView chat architecture is not the product source baseline. TD-024 explicitly allows one user-visible official-Web Send surface because current account-session native Send is security-boundary blocked.

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
- **Decision**: Default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority. Native transport may transiently copy current WebKit cookies/token into ephemeral `URLSession`; no second persistent credential store. TD-024's visible Web Send surface uses this same default store and does not add another credential owner.

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
- **Decision**: Use official interaction patterns where acceptable, implemented natively where the architecture permits. TD-024's user-visible official Web surface must still be wrapped in native UIKit navigation and must meet the user's explicit smoothness gate.

### TD-012 — Ship small usable candidates before roadmap completeness
- **Status**: Confirmed
- **Decision**: Produce unique TrollStore candidates whenever a coherent milestone becomes testable; CI/Artifact never substitutes for Runtime proof.

### TD-013 — Manual sync/reload are explicit recovery actions, not automatic retry machinery
- **Status**: Confirmed / Runtime accepted for recorded recovery scope
- **Decision**: `同步最新消息`, `重载当前会话` and terminal `重新加载` operate through authoritative `ConversationRepository` and never resend/regenerate or form retry/watchdog chains. Newer same-target recovery cancels/replaces the older active request before replacement ownership proceeds; generation/freshness rejects obsolete completions.
- **Evidence**: b15/b21 recorded cancellation/rejoin behavior; PR #10 merged.

### TD-014 — Reasoning UI includes expandable user-visible detail and two-pulse transition haptic
- **Status**: Confirmed requirement; native implementation remains future/evidence-dependent
- **Decision**: When an accepted native response owner receives explicitly user-visible reasoning detail/status, use subdued active reasoning/shimmer, explicit expand/collapse visible detail and two short haptic pulses on real-time reasoning→final transition. Never expose hidden chain-of-thought. b43 visible-Web Send does not scrape or mirror Web reasoning into native state.

### TD-015 — Production detail diagnostics use privacy-safe hashed identity + list position
- **Status**: Confirmed
- **Decision**: Use short irreversible SHA-256-derived conversation marker + 1-based list position for correlation; never raw ID/title/body.

### TD-016 — Background completion uses public baseline then isolated TrollStore experiment
- **Status**: Confirmed plan; dependency still requires an accepted response lifecycle
- **Decision**: After an accepted owned streaming lifecycle exists, first use normal iOS background-task time + local completion notification; any TrollStore true-background experiment remains isolated. A visible-Web page being capable of Send does not by itself establish native response ownership/background completion semantics.

### TD-017 — Public default-WebKit data-store warm-up is accepted for tested cold-start auth hydration
- **Status**: Confirmed for recorded scope
- **Decision**: Before first native list/account probe, initialize the existing default persistent `WKWebsiteDataStore` using public APIs. Do not add hidden/shadow WebView or second persistent auth store merely to hydrate cookies.

### TD-018 — Compact read-mode startup uses native primary/list root and one navigation owner
- **Status**: Confirmed for tested iPhone/iOS17 scope
- **Decision**: With no selected conversation, compact startup uses `.primary` conversation list as the useful root. `UISplitViewController`/native navigation remains the native shell navigation owner. The b43 hybrid surface is entered explicitly through native navigation rather than replacing startup.

### TD-019 — Multi-conversation data remains one account-scoped repository authority
- **Status**: Confirmed / merged Stable for recorded read-state scope; Frozen No
- **Decision**: One `ConversationRepository` owns native production conversation state scoped by verified account context and keyed per authoritative conversation identity. Foreground selection is presentation only; selecting B does not delete A or cancel valid hidden A work. Do not retain raw graph payloads or UIKit hierarchies as cache. No arbitrary normal LRU capacity; memory-warning trimming remains evidence-backed policy. The visible Web surface is not another native repository.

### TD-020 — Per-conversation scroll presentation is semantic anchor or follow-tail, not one raw offset
- **Status**: Historical-reading anchor Runtime accepted; native active-response follow-tail still pending an accepted native response owner
- **Decision**: Each native conversation owns lightweight scroll presentation semantics independently of conversation data. Historical reading preserves an authoritative message anchor plus display position/relative offset where practical. Do not fabricate native follow-tail from visible-Web DOM observation.

### TD-021 — Conversation-list cache may provisionally present last verified titles before current verification, but never authorize account-bound operations
- **Status**: Confirmed / merged Stable for recorded cache-core scope; Frozen No
- **Decision**: `ConversationListCacheStore` is storage only behind `ConversationRepository`. Automatic cold start may provisionally publish cached titles using a privacy-safe last-verified scope namespace hint, but this never establishes verified account/transport/Detail/send authority. Current 60-second rapid-relaunch window, offline retained list behavior, manual refresh bypass and first-page `28 + 1 -> 29` preservation are accepted.
- **Phase 8 extension**: authoritative `total=29` caps stale excess cached rows (`30 -> 29`, repeated `29/29`) without creating a second list owner; right-top refresh must not create persistent blank top inset.

### TD-022 — Long-conversation presentation uses deterministic derived geometry; round navigation consumes it
- **Status**: Confirmed / Runtime accepted / merged Stable on exact b38 recorded iPhone/iOS17 scope; Frozen No
- **Date**: 2026-08-29
- **Problem evidence**: Exact b36 retained severe long-conversation stutter in quick navigation and ordinary right-side scroll-indicator dragging. 47 direct-position samples had median ~187ms, P90 ~780ms and max ~3952ms. One 161-visible-message table initially reported ~13.8k points of bottom geometry and later ~154.6k points as giant estimated/self-sized message rows became realized.
- **Decision**: Keep authoritative native messages solely in `ConversationRepository`; derive an ephemeral `ConversationMessagePresentationProjection` that splits very long plain-text messages into bounded display chunks, computes deterministic row heights/prefix offsets for the current layout width, maps authoritative messages to first display rows, and drives `ConversationMessageCell` with deterministic manual frame layout. This projection is presentation-only and is rebuilt when authoritative messages/layout width require it; it is not a persistent second message/row-height store.
- **Copy/semantics boundary**: Copy reads the complete authoritative message; round count/semantic targets still come from one `ConversationRoundProjection`; each visible authoritative user message starts a round. Display chunking never creates semantic turns.
- **Navigation decision**: Stable b38 uses the already-derived O(1) target offset and one cancellable `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)` from the current viewport to the target. Short/long distances use one method. Rapid taps retarget from current visual position; real drag immediately retakes ownership. No pre-jump teleport, `scrollToRow` geometry discovery or end correction snap is part of the accepted path.
- **Runtime evidence**: Exact b37 user feedback **“这次确实不卡了”** accepted the deterministic geometry/performance direction. Exact b38 then restored genuine continuous full-distance animation while preserving that geometry; user feedback **“没问题了”** accepted the combined result.
- **Exact accepted identity**: b38 tested product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Runtime Artifact `9708425762`, IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- **Merge evidence**: PR #27 final head `57b3efe576dbf187171439a68d6d2dfe2fba0ebc`; tested product→final head delta was docs-only; PR merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- **Rejected without new evidence**: reverting to one giant whole-message self-sizing UILabel with unstable estimated geometry; persistent cross-detail row-height cache; pre-jump direct teleport; `scrollToRow` as target-geometry discovery; final correction snap; debounce/timer/watchdog/retry; alternate semantic index or second repository.

### TD-023 — Current ChatGPT-account native Send is blocked by required browser anti-abuse challenges
- **Status**: Confirmed by exact b42 protocol Runtime for recorded Plus/personal iPhone/iOS17 scope; pure-native production Send not implemented; Stable/Frozen No
- **Date**: 2026-08-29
- **Evidence**: Exact b42 `DEV-send-stream-0.1.0-b42`, product source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, Artifact `9709824510`, used a default `primary_assistant` new conversation. Sentinel prepare returned `proofOfWorkRequired=true`, `turnstileRequired=true`, and `soRequired=true`; Sentinel finalize submitted non-empty PoW and Turnstile values before successful `POST /backend-api/f/conversation` SSE Send.
- **Decision**: Under the pure-native/transient-WebKit-auth architecture, do not implement production ChatGPT-account Send because the successful path requires browser-generated anti-abuse challenge output that the native auth boundary does not legitimately own.
- **Rejected**: PoW/Turnstile/Sentinel solver or bypass, browser-fingerprint emulation/replay, captured proof/token replay, guessed alternate/fallback endpoints, hidden production WebView transport, or presenting CI/Artifact/protocol-probe success as native Send success.
- **Allowed path selected later**: TD-024 records the user's explicit selection of a user-visible official-Web Send surface.

### TD-024 — ChatGPT-account Send uses an explicit user-visible official-Web surface while native read/navigation remain authoritative
- **Status**: Architecture selected; exact b43 Code/CI/Artifact valid; Runtime acceptance pending; Stable/Frozen No
- **Date**: 2026-08-29
- **User decision**: After TD-023/b42 Path B, the user explicitly selected Option 2: keep the native shell/read/navigation and use a **user-visible official ChatGPT Web surface** for ChatGPT-account Send.
- **Decision**: The visible Web surface may execute the official page's normal browser Send/challenge behavior using the existing default persistent `WKWebsiteDataStore`. It must be visibly presented to the user and wrapped in native UIKit navigation. It is not pure-native Send and must never be described as such.
- **b43 implementation**: one process-resident shared `AuthWebViewController.hybridChat` loads `https://chatgpt.com/` on first visible presentation and reuses the same controller/WebView on ordinary return/re-entry without automatic reload. Settings exposes the explicit entry. No Root or `ConversationFeature.swift` product change.
- **Exact b43 evidence**: source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`; push Run/Job `33241032864` / `99070294478`; Artifact `9711364573`; IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`; PR Run/Job `33241035013` / `99070299776`; independent package identity `0.1.0 (43)`, Candidate b43, source marker `f602d68ae95d`, iOS14 minimum, arm64. **This is not Runtime acceptance.**
- **Hard Runtime gates**: first-entry responsiveness, resident re-entry/no avoidable reload, keyboard/typing, visible Web Send/stream scrolling, rapid scroll, native Back/return and attachment `+` responsiveness must be acceptable on exact iPhone/iOS17. Functional Send alone is insufficient.
- **Rejected**: hidden/shadow WebView challenge harvesting, continuous DOM observation/state mirroring, prompt/answer scraping, native replay of captured challenge outputs, guessed current-conversation deep links, or programmatic file-input injection without evidence.
- **Authority boundary**: `ConversationRepository` remains sole native conversation/list/detail/recovery authority; `AuthSessionStore` remains native auth/account authority; default persistent WebKit store remains persistent auth-secret authority. The visible Web surface owns only its own Web session/Send interaction while presented.
- **Identity incident**: Artifact `9710515489` from Run `33238065644` carried b42 identity over newer hybrid code and is permanently rejected; it does not redefine legitimate b42 Artifact `9709824510`.

## Rule

Do not write speculation here as fact. Historical plans, CI and Artifacts are not Runtime proof. Stable does not mean Frozen.
