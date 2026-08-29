# Technical Decisions

This file records durable, evidence-backed technical decisions and rejected routes. Detailed historical evidence remains available in Git history and `BUILD_TEST_INDEX.md`; current decisions below are the active durable contracts.

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client
- **Status**: Confirmed; qualified by TD-024/TD-025/TD-026 for ChatGPT-account Send
- **Decision**: Develop a native Swift/UIKit ChatGPT client as the product shell and native read/navigation baseline. Historical hidden-WebView chat architecture is not the product source baseline. TD-024 allows a user-visible official-Web Send surface because current account-session native Send is security-boundary blocked; TD-025 records that b44's full-page hybrid form is not acceptable product UX; TD-026 makes background resilience a prerequisite for any remaining existing-account hybrid direction.

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
- **Decision**: Use official interaction patterns where acceptable, implemented natively where the architecture permits. Any TD-024 Web Send surface must still be wrapped/integrated with native UIKit and meet the user's explicit smoothness/product-coherence gates.

### TD-012 — Ship small usable candidates before roadmap completeness
- **Status**: Confirmed
- **Decision**: Produce unique TrollStore candidates whenever a coherent milestone becomes testable; CI/Artifact never substitutes for Runtime proof.

### TD-013 — Manual sync/reload are explicit recovery actions, not automatic retry machinery
- **Status**: Confirmed / Runtime accepted for recorded recovery scope
- **Decision**: `同步最新消息`, `重载当前会话` and terminal `重新加载` operate through authoritative `ConversationRepository` and never resend/regenerate or form retry/watchdog chains. Newer same-target recovery cancels/replaces the older active request before replacement ownership proceeds; generation/freshness rejects obsolete completions.
- **Evidence**: b15/b21 recorded cancellation/rejoin behavior; PR #10 merged.
- **Phase 9 extension**: b44 proved that an immediate Sync after Web Send may expose the user message while assistant output already visible in Web is still absent from native Detail; a later Sync can expose it. This does not authorize automatic polling/timer retry because no readiness signal or stable delay was evidenced.

### TD-014 — Reasoning UI includes expandable user-visible detail and two-pulse transition haptic
- **Status**: Confirmed requirement; native implementation remains future/evidence-dependent
- **Decision**: When an accepted native response owner receives explicitly user-visible reasoning detail/status, use subdued active reasoning/shimmer, explicit expand/collapse visible detail and two short haptic pulses on real-time reasoning→final transition. Never expose hidden chain-of-thought. Visible-Web Send does not scrape or mirror Web reasoning into native state.

### TD-015 — Production detail diagnostics use privacy-safe hashed identity + list position
- **Status**: Confirmed
- **Decision**: Use short irreversible SHA-256-derived conversation marker + 1-based list position for correlation; never raw ID/title/body.

### TD-016 — Background completion uses public baseline then isolated TrollStore experiment
- **Status**: Confirmed plan; hybrid-Web feasibility now split by TD-026
- **Decision**: For native-owned response lifecycles, first use normal iOS background-task time + local completion notification; any TrollStore true-background experiment remains isolated. A visible-Web page being capable of Send does not itself establish native response ownership/background-completion semantics. TD-026 separately governs whether a visible official-Web response can survive or deterministically recover across background/lock.

### TD-017 — Public default-WebKit data-store warm-up is accepted for tested cold-start auth hydration
- **Status**: Confirmed for recorded scope
- **Decision**: Before first native list/account probe, initialize the existing default persistent `WKWebsiteDataStore` using public APIs. Do not add hidden/shadow WebView or second persistent auth store merely to hydrate cookies.

### TD-018 — Compact read-mode startup uses native primary/list root and one navigation owner
- **Status**: Confirmed for tested iPhone/iOS17 scope
- **Decision**: With no selected conversation, compact startup uses `.primary` conversation list as the useful root. `UISplitViewController`/native navigation remains the native shell navigation owner.

### TD-019 — Multi-conversation data remains one account-scoped repository authority
- **Status**: Confirmed / merged Stable for recorded read-state scope; Frozen No
- **Decision**: One `ConversationRepository` owns native production conversation state scoped by verified account context and keyed per authoritative conversation identity. Foreground selection is presentation only; selecting B does not delete A or cancel valid hidden A work. Do not retain raw graph payloads or UIKit hierarchies as cache. No arbitrary normal LRU capacity; memory-warning trimming remains evidence-backed policy. A visible Web surface is not another native repository.

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

### TD-024 — ChatGPT-account Send may use an explicit user-visible official-Web surface while native read/navigation remain authoritative
- **Status**: Architecture permission retained; b43 visible-Web feasibility largely accepted; b44 full-page integrated form rejected; Stable/Frozen No
- **Date**: 2026-08-29
- **User decision**: After TD-023/b42 Path B, the user selected Option 2: keep the native shell/read/navigation and use a **user-visible official ChatGPT Web surface** for ChatGPT-account Send.
- **Decision**: A visible Web surface may execute the official page's normal browser Send/challenge behavior using the existing default persistent `WKWebsiteDataStore`. It must be visibly presented to the user and integrated with native UIKit. It is not pure-native Send and must never be described as such.
- **b43 evidence**: one process-resident shared `AuthWebViewController.hybridChat` was smooth/resident enough in the tested sequence; Web `+` latency was ~100–200ms. The standalone Settings Web-chat form was not accepted as final UX; Web Photos filtered video on iOS17.
- **b44 evidence**: native detail -> visible `/c/<id>` Web -> explicit `返回并同步` worked structurally, and tested A/B native IDs mapped to the corresponding Web conversations. However immediate Native reconciliation could expose the user message while assistant output already visible in Web remained unreadable until a later Sync. The same conversation was loaded by Native and then again by Web. User rejected this full-page interaction as making Native lose its purpose.
- **Rejected**: hidden/shadow WebView challenge harvesting, continuous DOM observation/state mirroring, prompt/answer scraping, native replay of captured challenge outputs, Native composer injection into a covered/hidden Web composer, synthetic hidden Web Send clicks, and programmatic file-input injection without a supported/evidenced path.
- **Authority boundary**: `ConversationRepository` remains sole native conversation/list/detail/recovery authority; `AuthSessionStore` remains native auth/account authority; default persistent WebKit store remains persistent auth-secret authority. A visible Web surface owns only its own Web session/Send interaction while presented.
- **Identity incident**: Artifact `9710515489` from Run `33238065644` carried b42 identity over newer hybrid code and is permanently rejected; legitimate b42 remains Artifact `9709824510`.

### TD-025 — b44 proves a product-architecture ceiling for existing-account hybrid Send
- **Status**: Confirmed by exact b44 Runtime; API option later rejected by user; account-compatible path now conditioned by TD-026
- **Date**: 2026-08-29
- **Exact evidence**: b44 `DEV-send-stream-0.1.0-b44`, source `f1503cf7121512a84e5c55a3642181c17324d791`, Artifact `9712583513`, IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`; detailed Runtime record `docs/project/runtime-evidence/DEV-send-stream-b44-runtime.md`.
- **Runtime conclusion**: Web Send can succeed and `/c/<id>` mapping can be correct while immediate Native Detail reconciliation still lacks assistant output already visible in Web. Later Sync can expose it. No stable completion/readiness delay or signal was established. A/B switching also causes Web to reload/render the conversation separately from the already-loaded Native Detail.
- **Decision**: Do not patch the b44 architecture with arbitrary delay, automatic polling/retry or repeated Sync. Treat the full-page Native->Web->Native form as product-rejected.
- **Native-over-hidden-Web proposal**: A Native composer that forwards text into a fully covered/hidden official Web composer would require programmatic DOM/JS/input automation of the protected browser Send flow under current evidence. This is not accepted; it would turn Web into hidden/shadow transport rather than the explicitly visible user interaction permitted by TD-024.
- **Current route**: the user explicitly rejected the supported-API product option. The only active Send direction under evaluation is existing ChatGPT-account continuity through an explicitly visible Web-assisted surface; if that direction fails TD-026, defer account Send.
- **Candidate rule**: b39-b44 remain permanently reserved. No b45 is allocated until the background-resilience gate is explicitly authorized for experiment and its normal preflight completes.

### TD-026 — Existing-account visible-Web Send must survive background/lock or transparently recover without manual refresh
- **Status**: Confirmed product requirement; feasibility Unverified; blocks next Send UI Candidate
- **Date**: 2026-08-29
- **User decision**: The user explicitly rejects the API-product route and identifies background reasoning/stream interruption as unacceptable. During long reasoning or streamed reasoning/final output, backgrounding/locking the app for a while must not routinely lead to timeout/disconnect that requires manual refresh on return.
- **Public iOS boundary**: Apple's public background-task APIs provide finite extra runtime and do not guarantee long-running foreground-equivalent execution. `beginBackgroundTask` may be used as a short-duration baseline only; do not encode fixed-duration guarantees, keepalive timers or unrelated background-mode abuse.
- **TrollStore decision**: because the product is TrollStore-installed, evaluate a narrowly scoped true-background mechanism before polishing the embedded-Web UI. The experiment must prove the relevant **WebKit WebContent/network execution and official ChatGPT response stream**, not merely that the main app PID remains alive.
- **Activation boundary**: Native currently has no authoritative Web response terminal signal without prohibited DOM/stream observation. An initial experiment may conservatively preserve the process for the whole background interval when the visible Web Send/live-response surface was active at background entry, then release on foreground return. Do not create a fake `isWebStreaming` authority from UI text, timers or DOM scraping.
- **Foreground recovery**: if a **known** preservation loss or WebKit lifecycle failure occurs, one same-conversation recovery/reload on foreground is allowed provided it does not resend/regenerate the prompt. No timer/poll/retry chain and no repeated automatic Native Sync. If preservation remained valid, resume the existing live Web page without forced reload.
- **Unknowns**: WebContent survival, WebKit network-process survival, stream continuity, silent-stall detection, lock behavior, network transition and battery/thermal cost remain Unverified until exact-device Runtime.
- **Go/No-go**: Go only if the visible Web response reliably survives the user's normal background/lock habit or a known interruption recovers automatically without resend/manual refresh. No-go if routine use still needs manual refresh, WebKit cannot be preserved reliably, recovery requires hidden DOM automation, or battery/thermal cost is unacceptable.
- **Product consequence**: with API explicitly rejected, a TD-026 No-go means defer ChatGPT-account Send rather than hide a fragile Web transport behind Native UI.
- **Durable plan**: `docs/project/HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`.

## Rule

Do not write speculation here as fact. Historical plans, CI and Artifacts are not Runtime proof. Stable does not mean Frozen.