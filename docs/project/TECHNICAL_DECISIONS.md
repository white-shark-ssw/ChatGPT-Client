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

### TD-019 — Multi-conversation data remains one account-scoped repository authority
- **Status**: Confirmed architectural direction; b17 core Runtime accepted + b18 historical-scroll Runtime accepted for tested scope / Work Active
- **Date**: 2026-08-27
- **Decision**: Production conversation state is owned by one `ConversationRepository` scoped by the currently verified account context and keyed per authoritative conversation identity. Foreground selection is presentation state only. Selecting B must not delete A, cancel A merely because A became hidden, or make navigation itself a reload trigger. Same-target async freshness/cancellation remains per-conversation ownership inside this repository.
- **Account boundary**: `AuthSessionStore` remains the sole auth/account-context owner. Repository operation contexts may be checked against current verified account scope but must never become authority that can restore an older scope after a newer account transition. Persistent auth secrets remain solely in default WebKit storage.
- **Resident model boundary**: retain only current evidence-backed conversation data/metadata, including current branch-tip identity when available. Do not retain raw multi-megabyte payloads, use UIKit hierarchy as cache, or create one repository per screen/conversation.
- **Memory boundary**: normal resident capacity must become bounded from real-device evidence; no arbitrary capacity is frozen from source/CI or approximate text-byte metrics alone. Memory-warning trimming is distinct from ordinary LRU capacity.
- **Runtime evidence**: b17 accepts resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid overlap for the tested iPhone/iOS17 run. Exact b18 keeps Repository/protocol ownership unchanged and accepts historical-scroll isolation/preservation plus resident/coalescing regression paths on iPhone/iOS17. Remaining Work gates are natural failure residency, supported account-switch isolation, normal process/system-memory/LRU evidence and one isolated same-target Reload replacement-under-load spot-check.
- **Rejected**: stale operation context re-adopting account scope; selection-driven cancellation; separate screen repositories; retained VC/cell cache; navigation-triggered reload; speculative retry/timer/watchdog/global rate limiter; persistent chat-body cache without a separate contract.

### TD-020 — Per-conversation scroll presentation is semantic anchor or follow-tail, not one raw offset
- **Status**: User-confirmed product requirement; **historical-reading anchor Runtime accepted on exact b18 for tested iPhone/iOS17 matrix**; active-response follow-tail Runtime pending Send/Stream
- **Date**: 2026-08-27
- **Decision**: Each conversation owns lightweight scroll presentation semantics independently of conversation data. When the user is reading history away from the bottom, preserve a semantic message anchor plus relative visual offset where practical. When the user is at/near the bottom and that conversation has an authoritative active response, use `follow-tail` semantics instead of freezing the old anchor.
- **Historical-anchor Runtime evidence**: exact b18 user test reported no issue. Diagnostics identify b18/build18/source `f30c13b4ac2c` on iPhone/iOS17 and show repeated independent A/B save/restore pairs, first-time third-conversation isolation, Sync/Reload anchor preservation when the message remains, resident return without navigation-only refetch, and same-target Sync coalescing. The export contains 21 anchor saves, 19 restores, all 17 recorded HTTP statuses 200, no error/HTTP429/anchor discard.
- **Conditional boundary**: anchored-message disappearance did not occur naturally, so `scrollAnchor.discarded -> top` is source/CI-defined but not claimed as real-device tested.
- **Hidden-response rule**: if A is in `follow-tail`, the user switches to B, and A continues reasoning/generating/completes while hidden, returning to A must show A's **current latest bottom**. It must not restore the stale position that existed before the hidden answer grew.
- **User-intent rule**: intentionally scrolling upward in A while A is generating exits `follow-tail` and establishes historical-reading intent. Later A->B->A must restore that reading anchor rather than force-scroll to the newest bottom.
- **Isolation**: B's scrolling never changes A's anchor/follow-tail state; hidden A growth never changes B's scroll state. This remains presentation metadata, not a second conversation/response authority, and does not justify retaining one UIKit hierarchy per conversation.
- **Response-owner boundary**: whether a response is active/terminal must come from the future authoritative per-conversation Send/Stream response owner. Do not invent a separate UI `isStreaming` authority merely to implement follow-tail early.
- **Future Runtime gates**: Send/Stream must separately prove (1) A active at bottom -> B -> A completes hidden -> return A at latest bottom, and (2) A active -> user scrolls upward -> B -> return A at preserved reading anchor.
- **Rejected**: one global raw `contentOffset`; copying B's offset into A; always restoring the pre-switch location even when A was following an active response tail; always forcing bottom despite explicit upward reading intent.

## Rule

Do not write speculation here as fact. Historical plans, CI and Artifacts are not runtime proof.
