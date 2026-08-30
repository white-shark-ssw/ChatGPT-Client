# Technical Decisions

This file records durable, evidence-backed technical decisions and rejected routes. Detailed historical evidence remains available in Git history and `BUILD_TEST_INDEX.md`; current decisions below are the active durable contracts.

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client
- **Status**: Confirmed; qualified by TD-024/TD-025/TD-026/TD-027/TD-028/TD-029 for ChatGPT-account Send
- **Decision**: Develop a native Swift/UIKit ChatGPT client as the product shell and native read/navigation baseline. Historical hidden-WebView chat architecture is not the product source baseline. TD-024 records the earlier visible-Web security permission; TD-025 rejects b44's full-page hybrid form; TD-026 retains background resilience as a hard product requirement; TD-027 records the confirmed official resume / rejected Native duplicated parity boundary; TD-028 records the exact-device long-conversation full-Web composer viability ceiling; TD-029 is the current production Send decision and explicitly authorizes a covered official-Web **transport/challenge executor** behind Native UI while keeping `ConversationRepository` as the sole production response/conversation owner.

### TD-002 — Previous-project history is reference-only evidence
- **Status**: Confirmed
- **Decision**: Historical endpoint names/shapes/workarounds require current revalidation before becoming contracts.

### TD-003 — TrollStore IPA distribution with iOS17 primary tested ceiling and iOS14 build minimum
- **Status**: Confirmed
- **Decision**: TrollStore IPA; primary real-device evidence is iPhone/iOS17. Keep build minimum iOS14.0 until concrete need.

### TD-004 — Diagnostics/logging is application foundation
- **Status**: Confirmed
- **Decision**: Important async/auth/network/protocol/state operations use the accepted structured local diagnostics authority with bounded/redacted export.
- **Rejected**: passwords, OAuth codes, tokens, Cookie/Authorization values, raw conversation IDs, full titles/chat bodies or attachment contents.

### TD-005 — WebKit is persistent login authority; native consumption is transient
- **Status**: Confirmed; production Send execution qualified by TD-029
- **Decision**: Default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority. Native read transport may transiently copy current WebKit cookies/token into ephemeral `URLSession`; no second persistent credential store. TD-029 permits a process-resident official Web execution surface to use this same default store for page-owned protected Send/challenge execution without becoming a second auth or conversation authority.

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
- **Status**: Confirmed; production Send qualified by TD-029
- **Decision**: Use official interaction patterns where acceptable, implemented natively where the architecture permits. TD-029 keeps the user-facing composer/history/reasoning/tool/final experience Native while allowing the official page to execute only the browser-required protected Send behind that Native surface.

### TD-012 — Ship small usable candidates before roadmap completeness
- **Status**: Confirmed
- **Decision**: Produce unique TrollStore candidates whenever a coherent milestone becomes testable; CI/Artifact never substitutes for Runtime proof.

### TD-013 — Manual sync/reload are explicit recovery actions, not automatic retry machinery
- **Status**: Confirmed / Runtime accepted for recorded recovery scope
- **Decision**: `同步最新消息`, `重载当前会话` and terminal `重新加载` operate through authoritative `ConversationRepository` and never resend/regenerate or form retry/watchdog chains. Newer same-target recovery cancels/replaces the older active request before replacement ownership proceeds; generation/freshness rejects obsolete completions.
- **Evidence**: b15/b21 recorded cancellation/rejoin behavior; PR #10 merged.
- **Phase 9 extension**: b44 proved that an immediate Sync after Web Send may expose the user message while assistant output already visible in Web is still absent from native Detail; a later Sync can expose it. This does not authorize automatic polling/timer retry because no readiness signal or stable delay was evidenced.

### TD-014 — Reasoning UI includes expandable user-visible detail and two-pulse transition haptic
- **Status**: Confirmed requirement; diagnostic reasoning lifecycle evidenced through b65; production owner integration pending
- **Decision**: When the production `ConversationRepository` response owner receives explicitly user-visible reasoning detail/status from the accepted same-response stream, use subdued active reasoning/shimmer, explicit expand/collapse visible detail and two short haptic pulses on real-time reasoning->final transition. Never expose hidden chain-of-thought. `assistant:thoughts` remains non-presentational.

### TD-015 — Production detail diagnostics use privacy-safe hashed identity + list position
- **Status**: Confirmed
- **Decision**: Use short irreversible SHA-256-derived conversation marker + 1-based list position for correlation; never raw ID/title/body.

### TD-016 — Background completion uses public baseline then isolated TrollStore experiment
- **Status**: Confirmed plan; response-owner ordering qualified by TD-026/TD-027/TD-028/TD-029
- **Decision**: For Repository-owned response lifecycles, first use normal iOS background-task time + local completion notification; any TrollStore true-background experiment remains isolated. TD-029 establishes the intended production response owner: covered official Web may execute protected Send, but background completion state belongs to the Repository response lifecycle, not Web DOM/UI state.

### TD-017 — Public default-WebKit data-store warm-up is accepted for tested cold-start auth hydration
- **Status**: Confirmed; TD-029 adds one explicit production-use exception
- **Decision**: Before first native list/account probe, initialize the existing default persistent `WKWebsiteDataStore` using public APIs. Do not add a second persistent auth store. TD-029 additionally permits one process-resident official Web execution surface using that same store for protected Send/challenge execution; this does not create another persistent credential authority.

### TD-018 — Compact read-mode startup uses native primary/list root and one navigation owner
- **Status**: Confirmed for tested iPhone/iOS17 scope
- **Decision**: With no selected conversation, compact startup uses `.primary` conversation list as the useful root. `UISplitViewController`/native navigation remains the native shell navigation owner.

### TD-019 — Multi-conversation data remains one account-scoped repository authority
- **Status**: Confirmed / merged Stable for recorded read-state scope; Frozen No
- **Decision**: One `ConversationRepository` owns native production conversation state scoped by verified account context and keyed per authoritative conversation identity. Foreground selection is presentation only; selecting B does not delete A or cancel valid hidden A work. Do not retain raw graph payloads or UIKit hierarchies as cache. No arbitrary normal LRU capacity; memory-warning trimming remains evidence-backed policy. Covered Web Send execution under TD-029 is not another repository.

### TD-020 — Per-conversation scroll presentation is semantic anchor or follow-tail, not one raw offset
- **Status**: Historical-reading anchor Runtime accepted; native active-response follow-tail pending production response-owner integration
- **Decision**: Each native conversation owns lightweight scroll presentation semantics independently of conversation data. Historical reading preserves an authoritative message anchor plus display position/relative offset where practical. Follow-tail must consume Repository-owned active-response state; do not derive it from Web DOM observation.

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
- **Merge evidence**: PR #27 final head `57b3efe576dbf187171439a68d6d2dfe2fba0ebc`; tested product->final head delta was docs-only; PR merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- **Rejected without new evidence**: reverting to one giant whole-message self-sizing UILabel with unstable estimated geometry; persistent cross-detail row-height cache; pre-jump direct teleport; `scrollToRow` as target-geometry discovery; final correction snap; debounce/timer/watchdog/retry; alternate semantic index or second repository.

### TD-023 — Current ChatGPT-account pure-native Send is blocked by required browser anti-abuse challenges
- **Status**: Confirmed by exact b42 protocol Runtime for recorded Plus/personal iPhone/iOS17 scope; qualified by TD-029
- **Date**: 2026-08-29
- **Evidence**: Exact b42 `DEV-send-stream-0.1.0-b42`, product source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, Artifact `9709824510`, used a default `primary_assistant` new conversation. Sentinel prepare returned `proofOfWorkRequired=true`, `turnstileRequired=true`, and `soRequired=true`; Sentinel finalize submitted non-empty PoW and Turnstile values before successful `POST /backend-api/f/conversation` SSE Send.
- **Decision**: Under pure-native/transient-WebKit-auth request construction, do not implement ChatGPT-account Send because the successful path requires browser-generated anti-abuse challenge output that the native auth boundary does not legitimately own. TD-029 does not reverse that evidence; it keeps challenge execution inside the official page.
- **Rejected**: PoW/Turnstile/Sentinel solver or bypass, browser-fingerprint emulation/replay, captured proof/token replay, guessed alternate/fallback endpoints, or presenting CI/Artifact/protocol-probe success as pure-native Send success.

### TD-024 — Earlier user-visible official-Web Send permission
- **Status**: Historical security permission; production visibility requirement superseded by TD-029
- **Date**: 2026-08-29
- **User decision**: After TD-023/b42, the user initially selected a user-visible official ChatGPT Web Send surface while retaining Native shell/read/navigation.
- **Evidence**: b43/b44 established that the official page can perform protected Send with the default WebKit store, but the full-page hybrid interaction duplicated conversation rendering and immediate Native reconciliation could lag the Web answer.
- **b47 qualification**: a long-answer mobile-Web conversation could make the composer unusable before Send on the primary device.
- **Authority boundary retained**: `ConversationRepository` remains native conversation authority; `AuthSessionStore` remains auth authority; default WebKit store remains persistent auth-secret authority.
- **Supersession**: TD-029 explicitly supersedes only TD-024's requirement that the official Send surface remain user-visible and its rejection of a covered official-page executor. The challenge-bypass prohibition and state-owner boundaries remain in force.
- **Identity incident**: Artifact `9710515489` from Run `33238065644` carried b42 identity over newer hybrid code and is permanently rejected; legitimate b42 remains Artifact `9709824510`.

### TD-025 — b44 full-page existing-account hybrid Send is rejected
- **Status**: Confirmed by exact b44 Runtime; full-page form remains rejected; covered transport executor later authorized by TD-029
- **Date**: 2026-08-29
- **Exact evidence**: b44 `DEV-send-stream-0.1.0-b44`, source `f1503cf7121512a84e5c55a3642181c17324d791`, Artifact `9712583513`, IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`; detailed Runtime record `docs/project/runtime-evidence/DEV-send-stream-b44-runtime.md`.
- **Runtime conclusion**: Web Send can succeed and `/c/<id>` mapping can be correct while immediate Native Detail reconciliation still lacks assistant output already visible in Web. Later Sync can expose it. No stable completion/readiness delay or signal was established. A/B switching also causes Web to reload/render the conversation separately from already-loaded Native Detail.
- **Decision retained**: do not ship the b44 `Native -> full Web conversation -> return + Sync` form and do not patch it with arbitrary delay, polling/retry or repeated Sync.
- **Supersession**: the earlier rejection of any Native-composer -> covered official-Web composer execution is superseded by TD-029 because b48-b65 subsequently produced extensive exact Runtime evidence for that narrower transport shape. Full-Web conversation rendering remains rejected.
- **Candidate rule**: emitted b39-b47 identities are permanently reserved.

### TD-026 — Background/lock resilience remains a hard product requirement, but implementation follows the Repository response owner
- **Status**: Confirmed product requirement; exact b45 gives positive short-background evidence; full feasibility still Unverified
- **Date**: 2026-08-29
- **User decision**: During long reasoning or streamed reasoning/final output, backgrounding/locking the app for a while must not routinely lead to timeout/disconnect that requires manual refresh on return.
- **Public iOS boundary**: Apple's public background-task APIs provide finite extra runtime and do not guarantee long-running foreground-equivalent execution. `beginBackgroundTask` may be used as a short-duration baseline only; do not encode fixed-duration guarantees, keepalive timers or unrelated background-mode abuse.
- **Exact b45 evidence**: on iPhone/iOS17.0, one clean default-primary new-chat response remained on the same original `/backend-api/f/conversation` fetch while the app was backgrounded approximately 35s, 34s and 126s during the active response (~195s cumulative). On final foreground return the same original stream delivered `message_stream_complete` and `[DONE]`; no manual refresh/resend or secondary reconnect transport was observed.
- **Evidence boundary**: this proves the tested path can survive or buffer across those ordinary background/lock intervals. It does not prove continuous background event delivery, 5/15-minute survival, WebContent termination recovery, network-loss recovery or battery/thermal cost.
- **Ordering decision**: TD-029 establishes the planned production response owner: the Web surface may remain necessary to execute the protected browser request, but active-response/background state belongs to `ConversationRepository`. Background work must preserve/recover that one response lifecycle without duplicate Send.
- **Rejected**: manual-refresh-as-normal-use, DOM-state authority, timer/poll/retry chains, permanent idle process immortality, or claiming main-app survival equals WebKit-stream survival.
- **Durable plan**: `docs/project/HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`.

### TD-027 — Official no-resend resume is Runtime Confirmed; Native duplicated Cookie+Bearer-only parity remains rejected
- **Status**: Confirmed through exact b45-b47 Runtime; Native first/exclusive continuation remains Unverified
- **Date**: 2026-08-29
- **Exact evidence**: b45 source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` / Artifact `9713774868`; b46 source `4ab9be3ef2809204e88fcb0d44884e35b43726b1` / Artifact `9715903443`; b47 source `21028bbff7982abeb42f130c56fcb21e6ef44d7a` / Artifact `9716878034`. Detailed records: `DEV-send-stream-b45-runtime.md`, `DEV-send-stream-b46-runtime.md`, `DEV-send-stream-b47-runtime.md`.
- **Official transport conclusion**: current official Web uses `POST /backend-api/f/conversation/resume` with body `{conversation_id: string, offset: number}` as a post-Send continuation read. After real transport interruption it can return HTTP200 `text/event-stream`, repeatedly continue the same already-started response without another Send and reach terminal events.
- **b46 Native parity**: after official offset 18 resume succeeded, one Native same-body Cookie+Bearer-only duplicate returned HTTP404 JSON; later official offset 54 succeeded.
- **b47 Native parity**: after official offset 23 resume succeeded, one Native same-body Cookie+Bearer-only duplicate again returned HTTP404 JSON (~707ms, 116 bytes, 0 SSE frames); later official offset 74 succeeded. Rejection shape was `{"detail":{"code":"string","message":"string"}}`.
- **Request-context evidence**: successful official resume exposed header names `accept, authorization, content-type, oai-client-build-number, oai-client-version, oai-device-id, oai-echo-logs, oai-language, oai-session-id, x-conduit-token, x-oai-is-client-observation, x-oai-is-pending-updates, x-oai-turn-trace-id, x-openai-target-path, x-openai-target-route`. Native explicitly set only `accept, content-type`, plus the established transient bearer injection and WebKit-derived ephemeral cookies.
- **Decision**: this structural difference does not authorize copying browser header values. Missing non-challenge request context vs second-consumer/cursor ownership remains unresolved. Native first/exclusive resume is Unknown / Unverified.
- **Rejected**: guessing required browser headers, copying `x-conduit-token`/OAI browser values without evidence, retry loops, duplicate Send, or treating HTTP404 as proof that Native continuation is universally impossible.

### TD-028 — Full mobile-Web conversation is not an accepted production Send dependency after exact long-conversation composer failure
- **Status**: Confirmed product architecture gate; narrowed by TD-029
- **Date**: 2026-08-29
- **Evidence**: while preparing exact b47 testing, the user attempted to use an older conversation containing only about three rounds but long answers. On the primary iPhone/iOS17 environment, repeatedly trying to bring up/use the mobile-Web composer froze the page badly enough that the conversation could not be used for the test; the user switched to a new conversation. The exported b47 diagnostics cover the replacement run and therefore do not establish the freeze's internal owner.
- **Decision retained**: do not render/use the full mobile-Web conversation as the daily-chat product dependency. The Native product must own history/presentation.
- **Supersession**: the old shortcut rejection of a covered official Web Send executor is superseded by TD-029 after b48-b65 proved a narrower page-owned Send/SSE path under Native presentation. TD-029 does not require full Web history rendering and therefore does not reverse the b47 long-conversation failure evidence.
- **Evidence boundary**: b43's earlier smooth visible-Web result remains valid only for its shorter tested sequence; root cause of the long full-page freeze remains Unknown / Unverified.

### TD-029 — Production Send uses Native UI + covered official-Web protected-Send executor + Repository response ownership
- **Status**: Confirmed product architecture decision; implementation/production Runtime still pending
- **Date**: 2026-08-31
- **User decision**: after b65 focused Runtime passed and the remaining blocker was the earlier visibility prohibition, the user explicitly selected Option B: authorize the already-tested Native composer -> covered official Web page-owned protected Send mechanism for production and prioritize finishing `DEV-send-stream` quickly.
- **Evidence basis**: b42 proves pure-native ChatGPT-account Send is blocked by browser challenge output. b48-b65 then prove on the primary iPhone/iOS17 scope that a Native-controlled composer can drive the official page's verified composer, observe one real protected `/backend-api/f/conversation` HTTP200 SSE response, classify complete-looking reasoning/final text, preserve `title_generation` continuation, honor exact `reasoning_ended`, present event-driven thinking state, exact-parent tool lifecycle and the bounded GitHub detail mapping. b65 closes the tested tool-detail formatting defect.
- **Decision**: the production user-facing composer/history/reasoning/tool/final UI is Native. One process-resident official ChatGPT Web execution surface may be covered/not user-visible while using `WKWebsiteDataStore.default()` to let the official page execute the browser challenge and exactly one protected Send for each user Send action. The same response stream is consumed into a Repository-owned response lifecycle.
- **State ownership**: `ConversationRepository` remains the sole production conversation/resident/response authority. Covered Web owns no durable message/conversation/response state and no production UI semantics. `AuthSessionStore` remains auth/account authority; default WebKit store remains persistent auth-secret authority.
- **Security boundary retained**: no challenge solver/bypass, no copying/replaying PoW/Turnstile/Sentinel/conduit values, no second persistent credential store, no duplicate Send to obtain a stream, no arbitrary fallback selectors/retry/timer/watchdog chain.
- **Product boundary retained**: b44 full-page Web chat remains rejected; TD-028 full-Web long-conversation dependency remains rejected; continuous DOM message mirroring remains rejected. Only the evidenced composer/protected-Send/SSE executor is promoted.
- **Maintenance decision**: add and retain an in-app development **Web Rule Lab** using the same default WebKit store. It visibly opens ChatGPT Web, accepts user-pasted temporary JS probes, displays/copies/shares the temporary result, and never persists probe code/result bodies in diagnostics or app storage. Future Web changes should follow `reproduce -> Lab probe -> evidence -> one minimal adapter update -> one coherent product build`, not repeated speculative IPA builds.
- **Durable adapter authority**: `docs/project/WEB_SEND_ADAPTER.md` owns current evidenced selectors/SSE/reasoning/tool rules and the Web Rule Lab update playbook. `SEND_STREAM_PREFLIGHT.md` owns Repository/new-chat/Stop/follow-tail state invariants.
- **Implementation order**: Web Rule Lab foundation -> existing-conversation Repository-owned production Send/stream -> new-chat identity handoff -> exact Stop -> A/B/follow-tail -> Sync/Reload/b38 regression -> final daily-chat Runtime/merge decision.
- **Evidence ladder**: architecture decision confirmed; production code/CI/Artifact/Runtime under this decision remain pending until a new unique Candidate is emitted and tested.

## Rule

Do not write speculation here as fact. Historical plans, CI and Artifacts are not Runtime proof. Stable does not mean Frozen. A newer explicit TD may supersede only the clauses it names; all unaffected evidence and boundaries remain active.