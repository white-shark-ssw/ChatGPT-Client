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
- **Implementation boundary**: `AuthTransientSession.dataTask` exposes only the same already-created/resumed transient `URLSessionDataTask`; auth/header/cookie/endpoint semantics are unchanged. Task cancellation remains request-lifecycle ownership inside the existing repository, not automatic retry and not a second state authority.
- **Runtime evidence**: b13 proved freshness rejection alone prevented stale mutation but concurrent replacement requests could return HTTP429. Exact b15 then proved two replacement sequences: generations 1/3 were cancelled, generations 2/4 returned HTTP200 with 168/591 visible messages, and no HTTP429 appeared. User reported no issues. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

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
- **Scope**: Cold-start authentication sequencing / merged recovery baseline
- **Decision**: Before first native conversation-list/account probe, initialize existing default persistent `WKWebsiteDataStore` with public APIs. Do not add hidden/shadow WebView or second persistent auth store merely to hydrate cookies.
- **Evidence**: Exact b12 iPhone/iOS17 export began at 0/0 total/matched cookies; warm-up completed in 194.97 ms with 41/22 cookies and 7 data records. The later unchanged normal account probe succeeded and conversation list returned HTTP200 28/29 without opening visible Login. b13 repeated warm-up success and immediate list start.
- **Boundary**: This proves hydration for tested persisted sessions only. It does not prove every install/update/session state and does not remove visible Login as explicit fallback after genuine failure evidence.
- **Rejected / do-not-repeat**: no hidden WebView, persisted copied secrets, automatic retry/watchdog loop, speculative auth endpoint/header fallback.

### TD-018 — Compact read-mode startup uses native primary/list root and one navigation owner
- **Status**: Confirmed for tested b14+ iPhone/iOS17 scope
- **Date**: 2026-08-27
- **Decision**: With no selected conversation, compact startup uses `.primary` conversation list as the useful root. UISplitViewController/native navigation is the sole compact list/detail navigation owner; do not layer a duplicate custom sidebar button on top.
- **Evidence**: b13 recording showed blank `新对话` startup, duplicate sidebar icons and unreliable custom reveal. Exact b14 removed the custom owner and user reported the stated compact startup/navigation gate had no issues. b15 preserved this behavior.

## Rule

Do not write speculation here as fact. Historical plans, CI and Artifacts are not runtime proof.
