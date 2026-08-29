# Project-Specific Rules

This file contains repository/product rules backed by explicit requirements, current source, accepted tests or durable technical decisions.

## Product contracts

- Product goal remains an **iOS native ChatGPT client shell/read experience**.
- Exact b42 Runtime proves the pure-native/transient-auth ChatGPT-account protected Send path depends on browser anti-abuse challenge output. The separately supported/billed API-product route remains explicitly rejected by the user unless that decision changes later.
- TD-024 permits a **user-visible official ChatGPT Web surface** to perform protected Send, but this is a security permission only; it is not proof that full mobile-Web conversation rendering is an acceptable daily-chat product surface.
- TD-025 rejects b44's full-page Native -> Web -> Native product form.
- TD-027 records the current continuation boundary: official `/backend-api/f/conversation/resume` is Runtime Confirmed, while b46/b47 Native duplicated Cookie+Bearer-only resume attempts returned HTTP404 JSON.
- TD-028 adds the current P0 product ceiling: the user reported an exact target-device long-answer conversation (~3 rounds) where the mobile-Web composer repeatedly froze badly enough that the conversation could not be used for b47 testing. The internal freeze cause is Unknown, but **full Web conversation rendering before every protected Send is no longer an accepted production dependency**.
- Do not allocate b48 merely to chase resume headers or fix a diagnostic field name while TD-028's production Send boundary remains unresolved.
- Previous-project history is reference-only, not current protocol authority.
- Durable roadmap: `docs/project/DEVELOPMENT_PLAN.md`.
- Durable UI/interaction baseline: `docs/project/UI_INTERACTION_BASELINE.md`.
- Durable existing-account Web background plan: `docs/project/HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`.
- Product delivery priority: reach a genuinely usable TrollStore client early, then iterate with exact real-device Candidates.
- Stable merged baselines include b9 native read, b15 recovery, b21 multi-conversation read state, b23 conversation-list cache core, and **b38 Phase 8 conversation metadata/settings/round navigation** for their recorded scopes. Stable does not mean Frozen.
- Exact Phase 8 accepted Candidate is `DEV-conversation-round-count-0.1.0-b38`, exact tested product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.

## UI / interaction contract

- Official ChatGPT iOS interaction is the default baseline where acceptable; use native UIKit/system behavior rather than inventing a second UI language.
- UI text/title is a consumer, never identity authority.
- Ordinary native conversation actions live in official-style overflow/context surfaces.
- On compact iPhone with no selected conversation, initial useful surface is the native conversation list; revealing navigation must not start the initial list request.
- `UISplitViewController`/native navigation remains the native shell's compact list/detail navigation owner.
- Conversation-list right-top refresh and pull-to-refresh are distinct presentation sources over the same repository manual-refresh request path. Right-top refresh must never begin/resize/mutate `UIRefreshControl`; genuine pull uses native spinner + `endRefreshing()` only.
- Do not use `navigationItem.prompt` for ordinary conversation-list refresh/cache status. b29 Runtime accepts removal of the prompt-induced blank/top-inset growth for the tested right-top refresh path.
- Do not assign attributed/text titles to `UIRefreshControl`, and do not reintroduce b27 contentOffset/top-normalization compensation.

## User-visible hybrid Web Send / realtime handoff contract

- Visible official Web may legally perform protected Send because b42 blocks pure-native/transient-auth Send, but the surface must remain genuinely visible and user-operated.
- The Web surface must never become a hidden/shadow WebView used only to execute browser anti-abuse challenge + Send under a Native facade.
- Use the existing default persistent `WKWebsiteDataStore`; do not add another persistent credential/challenge store.
- `ConversationRepository` remains sole native conversation/list/detail/recovery/future accepted response authority. `AuthSessionStore` remains native auth/account authority. A visible Web surface owns only its own official Web session/Send interaction while presented and does not become a second native repository.
- b43 established only a **shorter-sequence** smoothness/residency baseline: entry/re-entry, keyboard/typing, Send/stream scrolling and rapid scrolling had no material reported problem; Web `+` -> picker was roughly 100–200 ms. b43 is not long-conversation viability proof.
- b44 established tested `/c/<conversation-id>` A/B mapping and explicit Native reconciliation, but the full-page Native -> Web -> Native flow is **product-rejected**. Immediate Native Sync could expose the user message while assistant output already visible in Web remained absent until a later Sync. No stable readiness signal/delay was established.
- Do not patch b44 with arbitrary delay, timer, polling or automatic repeated Sync.
- b45 later proved official Web has a real no-resend post-Send continuation transport: `POST /backend-api/f/conversation/resume`, JSON body `{conversation_id: string, offset: number}`, HTTP200 `text/event-stream` on successful recovery.
- b46 and b47 each issued exactly one Native same-body duplicated resume only after an official successful resume; both Native requests returned HTTP404 `application/json` while later official resume remained healthy. Native first/exclusive resume remains Unknown / Unverified.
- b47 successful official resume request exposed header names `accept, authorization, content-type, oai-client-build-number, oai-client-version, oai-device-id, oai-echo-logs, oai-language, oai-session-id, x-conduit-token, x-oai-is-client-observation, x-oai-is-pending-updates, x-oai-turn-trace-id, x-openai-target-path, x-openai-target-route`; Native explicitly set only `accept, content-type` plus the established transient bearer injection and WebKit-derived ephemeral cookies. Header-name presence does **not** authorize copying browser header values.
- b47 Native rejection JSON shape was `{"detail":{"code":"string","message":"string"}}`. The intended safe code/type/status export field was named `safeErrorTokens`; current diagnostics sanitization redacts keys containing `token`, so those safe values were lost. Correcting it requires b48+ and is not currently prioritized over the architecture gate.
- Exact target-device b47 preparation exposed a stronger pre-Send problem: an older conversation with only about three rounds but long answers repeatedly froze when trying to bring up/use the mobile-Web composer. The user had to test with a new conversation.
- Therefore **do not continue production integration of `Native history -> full official Web conversation for every protected Send -> Native resume`**. A post-Send Native handoff cannot repair a Web composer that becomes unusable before Send.
- The internal owner of the composer freeze remains Unknown / Unverified because the exported b47 diagnostics cover the replacement new-conversation run, not the failed long-conversation attempt.
- Evidence-backed next architecture questions are limited to: whether an official supported lightweight **visible send-only** surface exists without full conversation-history rendering; whether another legitimate account-compatible protected-Send boundary can avoid the full mobile-Web conversation without hidden DOM automation/challenge bypass; otherwise whether visible Web is diagnostic/fallback only.
- Choosing the production Send boundary is a **Human Architecture Gate**. No b48 product code is allocated until that gate is deliberately resolved.
- Do not continuously observe the DOM, scrape prompt/answer/reasoning text, mirror Web message state into native state, capture challenge/token values, or replay browser proof output.
- Do not implement a Native composer that secretly injects text into a fully covered/hidden Web DOM/contenteditable and triggers synthetic hidden Send clicks.
- Do not guess a resume/handoff/turn-stream endpoint or required browser header values.
- Background resilience remains a hard gate, but response ownership and Send-surface viability must be settled before production background work.
- `beginBackgroundTask` is a finite public baseline only. It must not be presented as a long-duration guarantee.
- Main-app process survival is not sufficient proof; distinguish WebContent process, WebKit network/process and actual official-Web stream survival.
- Do not create a fake `isWebStreaming` authority from UI text, timer inference or DOM scraping.
- Attachment `+` remains a hard UX gate. Exact b43 Web `+` latency ~100–200 ms was not rejected, but the Web Photos chooser filtered videos.
- Public WebKit upload-panel replacement via `WKUIDelegate.runOpenPanelWith...` is iOS18.4+, not the primary iOS17 target. Do not use private WebKit or DOM/file-input injection to fake a photo+video picker fix. iOS17 video attachment support requires separately evidenced native attachment upload/handoff.

## Conversation metadata / Preferences contract

- Round count and previous/next round navigation consume one `ConversationRoundProjection` derived from the authoritative visible active branch. Do not maintain a second mutable round counter or semantic navigation index.
- Each visible authoritative user message starts one round. The accepted physical quick-navigation target is the **round-start user message**. Hidden tool/reasoning/system/internal-recipient nodes do not create ordinary rounds.
- Recipient/internal filtering remains upstream of ordinary visible chat-row projection. b32 Runtime accepted filtering of tool/internal recipient rows before round/message presentation.
- `AppPreferences` is the single persisted native settings owner. Current defaults remain: `显示会话轮数` On, `显示消息时间` On, `显示轮次快速跳转` On.
- Message timestamps use authoritative historical `createTime`; if absent, omit rather than fabricate. Formatting uses current locale/time zone.
- Copy reads only authoritative user-visible message text, uses system pasteboard, does not mutate message state and does not issue network requests. Hidden reasoning/tool/system content is never copied.
- Assistant Copy remains a compact official-style quick action with clear background and subdued dynamic tint. User context Copy remains native.

## Long-conversation presentation geometry contract

- b36 exact Runtime proved the dominant **native** stutter owner was deferred giant-row/table geometry, not quick-navigation animation alone: direct positioning reached ~3952ms in the tested trace and ordinary right-side scroll-indicator dragging also severely stuttered.
- The Stable b37/b38 native presentation baseline uses `ConversationMessagePresentationProjection` as **ephemeral derived presentation state only**. It is not conversation authority and must never become a persistent second message store.
- Very long plain-text messages are split into bounded display chunks for native presentation virtualization. Concatenated authoritative message content is unchanged; Copy always reads the full authoritative message.
- Presentation derives deterministic row heights and prefix offsets for the current detail/layout width before interaction. Round targets and scroll anchors consume this geometry rather than asking UITableView to discover giant self-sized rows while scrolling.
- `ConversationMessageCell` uses deterministic manual frame layout for one bounded display chunk. Do not restore one unbounded whole-message multiline UILabel + deferred automatic estimated geometry without new exact Runtime evidence.
- Width/presentation changes may rebuild this ephemeral geometry. Do not persist row heights across unrelated details/layout widths as a new durable cache owner.
- b37 exact-device feedback accepted this geometry/performance direction; b38 preserved it and the merged Phase 8 baseline is Stable, Frozen No.
- The b47 mobile-Web composer freeze is a **separate Web-surface failure** and is not evidence that the Stable native b38 geometry regressed.

## Round-navigation contract

- Use one adaptive floating control. Real user drag owns user intent; programmatic presentation is not user intent.
- Rapid taps advance from the last requested derived round target via one transient presentation cursor; this is not a second semantic authority. A real user drag clears/replaces programmatic intent.
- Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll. At physical bottom, when a previous round exists, overscroll must not flip the control to `下一轮` merely because drag delta reverses. b33 Runtime accepts this tested path.
- Short and long quick-navigation distances use **one unified method**.
- Stable b38 programmatic presentation contract: resolve the semantic target through the already-derived O(1) deterministic prefix geometry, then continuously animate from the **current viewport offset** to the final target offset using one cancellable `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)`.
- Do not perform a nonanimated pre-jump teleport/120pt lead step in the accepted path.
- Do not call `scrollToRow` merely to discover target geometry during round navigation. The target offset is derived from presentation geometry.
- Rapid retargeting stops the active animator at its current visual position and immediately starts toward the next semantic target. No debounce/wait gate.
- Real finger drag cancels the programmatic animator and clears programmatic target ownership immediately.
- Do **not** reintroduce b33/b34 final correction snaps or stale-completion correction ownership unless new exact Runtime evidence requires a different accuracy strategy.
- Privacy-safe diagnostics may record presentation mode, row index/role, offsets, travel distance, retargeting and landing error; never message identity/body.
- No debounce, retry, timer, watchdog, alternate semantic index, duplicate repository/state owner or speculative compatibility shim may be added without new evidence.

## Per-conversation scroll presentation contract

- Native scroll presentation belongs to the detail presentation owner, not `ConversationRepository` and not a retained UIKit hierarchy cache.
- Historical reading uses semantic authoritative-message anchor plus display-chunk position/relative offset where practical; one global raw offset is prohibited.
- A/B anchors are independent. Account-scope reset clears presentation anchors.
- First visible presentation with no valid saved reading anchor shows latest/bottom of the current visible branch without visibly animating through history. Loading/empty placeholder offsets are not reading anchors.
- Sync/Reload may preserve an established anchor only when the same anchored authoritative message remains; otherwise discard explicitly rather than invent cross-message fallback.
- Native follow-tail still belongs to an authoritative native Send/Stream response lifecycle; do not derive it by observing the hybrid Web DOM.

## Message rendering scope contract

- Current native message body remains plain string content. Markdown headings/lists/links/emphasis/code/tables and rich citation/annotation rendering belong to future `DEV-message-rendering`.
- Supplied real-device comparison showed raw Markdown and raw `filecite`-adjacent boxed glyphs in the current client. Do not strip/rewrite those markers without authoritative rich-content/annotation evidence.
- If later evidence shows file citations map to attachment/file-card ownership, coordinate with attachment rendering rather than inventing a second representation.

## Fast usable Candidate contract

- Do not hold usable functionality until the entire roadmap is complete.
- Every testable Candidate has a unique build/Candidate/Artifact identity and keeps Code / Static / CI / Artifact / Runtime / Stable evidence separate.
- Once a Candidate/Artifact identity has been produced, do not rebuild corrected product code under that same identity.
- Workflow Artifact container naming is not identity proof. Verify built `CFBundleShortVersionString`, `CFBundleVersion`, `DiagnosticsCandidate`, source marker and IPA filename/SHA before Runtime.
- `scripts/build_ipa.sh` must derive identity from built app metadata and fail on Candidate/version/build mismatch.
- Exact b24-b47 identities and emitted artifacts are permanently reserved. The accidental newer-code Artifact `9710515489` carrying b42 identity is permanently rejected and must never be installed; legitimate b42 remains Artifact `9709824510`.
- Exact b47 product/config source remains `21028bbff7982abeb42f130c56fcb21e6ef44d7a`; later docs-only commits do not redefine it.
- **No b48 is currently allocated.** Correcting b47 product code would require b48+, but TD-028 architecture selection precedes any such allocation.

## Manual recovery contract

### `同步最新消息`

- Explicit user recovery through authoritative `ConversationRepository`; current target only, never resend/regenerate.
- Preserve an already loaded detail on sync failure where applicable.
- Keep available during ordinary initial Detail loading.
- Accepted feedback remains centered `正在同步最新消息…`, then `已是最新` or `已同步最新消息` for about 2 seconds.
- b44 adds an important boundary: an immediate Sync after visible-Web Send may still lack assistant output already visible in Web. A later explicit Sync can expose it. Do not convert this into automatic polling/retry without a real server readiness signal.

### `重载当前会话`

- Explicit recovery for unusable current conversation; terminal failure provides direct `重新加载`.
- Clears/rebuilds only selected authoritative detail from one fresh server request; never resends existing messages.
- Keep overflow Reload available during ordinary initial load.

### Replacement request lifecycle

- A newer explicit same-target Sync/Reload cancels/replaces the older target network task before replacement request ownership proceeds, while generation/freshness rejection protects against late callbacks.
- This remains request lifecycle ownership inside the same repository, not a second store or retry chain.
- b15/b21 real-device evidence accepts the recorded cancellation/rejoin/coalescing behavior.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.

## Cold-start authentication contract

- Default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority; copied cookies/tokens are transient only.
- Native `/auth/login` is not an account-context prerequisite. Accepted sequence remains WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- b12 accepted public WebKit data-store warm-up for the tested persisted cold-start path.
- Do not add hidden/shadow WebViews, persistent copied secrets or retry loops.
- Cache namespace hint is cache bookkeeping only and never establishes verified account/transport/Detail authority.
- TD-024's explicit visible Web Send permission does not authorize hidden Web hydration/challenge harvesting.

## Conversation-list persistent cache contract

- b23 is the Stable merged cache-core baseline for recorded Plus/personal iPhone/iOS17 scope; PR #24 merged. Frozen No.
- `ConversationRepository` remains sole authoritative list/conversation owner; `ConversationListCacheStore` is storage only.
- Persist only a small versioned account-scoped summary snapshot plus privacy-safe namespace bookkeeping; never Detail/full-body data or copied auth secrets.
- Automatic cold start may provisionally publish last-successfully-verified cached **titles only** before current network verification. Provisional rows cannot authorize Detail until current scope is verified.
- Temporary auth transport failure may retain valid provisional rows without converting it into logout or automatic retry.
- Exact b23 accepts the current 60-second rapid-relaunch window. Manual refresh bypasses suppression and issues exactly one user-requested list refresh.
- Page-1 absence is not deletion evidence. b23 proved `28 + 1 -> 29`; merged Phase 8 b26 behavior accepts the authoritative-total cap for stale excess rows (`30 -> 29`, repeated `29/29`). Preserve that bound.
- b29 Runtime accepts the tested right-top list refresh presentation with no persistent blank band above the first conversation.
- Never add timer/polling/watchdog/retry, alternate list/auth endpoints, per-row Detail prefetch or another list/account authority solely for cache behavior.

## Protocol evidence contract

- Do not implement private/internal Web API behavior from history/memory alone.
- Accepted native read path remains transient WebKit-derived auth + current list/detail routes documented in project evidence.
- Do not preemptively add account headers, duplicate browser headers, alternate endpoints or compatibility shims without concrete current failure.
- `ProtocolReadProbe` remains diagnostic-only; `ConversationRepository` remains native production authority.
- b40-b42 private Send observations remain protocol evidence and do not authorize native replay around browser protections.
- b45 proves the official no-resend resume route/method/body/framing after real transport interruption.
- b46/b47 prove only that a **duplicated-after-official-success** Native Cookie+Bearer-only resume receives HTTP404 JSON; they do not prove Native first/exclusive resume impossible.
- b47 proves a large official-vs-Native request-header-name structural difference, but no browser header value is authorized for copying from name presence alone.
- Do not continue resume-parity experiments while the production Send surface is under TD-028's Human Architecture Gate unless the later selected architecture makes that evidence relevant again.

## Diagnostics / logging contract

- Use existing `DiagnosticsLogger` authority.
- Never log/export passwords, OAuth codes, tokens, Cookie/Authorization values, raw conversation IDs, full titles, message bodies/parts, raw payloads, Sentinel/Turnstile/PoW values or Web prompt/answer text.
- Hybrid/hand-off diagnostics may record safe route/transport/status/header-name/query-name/structural identity presence/timing only; proof/challenge/header values remain redacted.
- Current sanitizer redacts any field key containing `token`; therefore diagnostic field names intended to carry safe enum/error-code summaries must avoid `token` in the **field key** if such evidence is needed in a future Candidate.
- Background diagnostics may record app lifecycle, public background-task begin/end/expiration, safe Web process/navigation failure class and foreground recovery reason. No heartbeat timer merely to manufacture activity.
- Multi-conversation correlation uses privacy-safe hashes/counts/generations.
- Cache diagnostics may record schema/hit/age/count/duration/scope hash/decision only.
- Scroll/round diagnostics may record non-secret row indices, content offsets, geometry/presentation durations where applicable, travel distance and landing error, never message identity/body.

## Multi-conversation / state-owner contract

- b21 remains the Stable merged multi-conversation read-state baseline for recorded tested scope. One `ConversationRepository` remains native production conversation authority.
- Foreground selection is presentation only. Selecting B does not destroy/cancel valid A work merely because A becomes hidden.
- Same-target obsolete operations are rejected by per-target generation/freshness ownership; equivalent loads may coalesce.
- Account scope comes only from accepted auth owner; stale operation context may never re-adopt an older scope.
- No arbitrary normal LRU capacity: b19 evidence through 8 residents does not justify one. Memory warnings may trim eligible inactive terminal residents.
- Do not treat a Web page's visible conversation state as a second native resident/message authority.

## Background / compatibility

- Generic background continuation follows `BACKGROUND_EXECUTION_PLAN.md`: no automatic prompt resend and no second stream/store; TrollStore privileged background remains an isolated experiment.
- Public `beginBackgroundTask` is a finite short-duration baseline only; do not promise long foreground-equivalent execution from it.
- A visible Web surface does not establish a native response owner, and main-app process survival does not prove WebKit WebContent/network/stream survival.
- b45 exact-device evidence establishes positive short-background/original-stream survival and official recovery after forced interruption, but full background acceptance still requires its own matrix after a viable production response owner is selected.
- TD-028 means production background work must not optimize a full-Web Send architecture whose composer can fail before Send on long conversations.
- Native iOS / TrollStore IPA; intended ceiling iOS17; current build minimum iOS14; current real-device evidence primarily iPhone/iOS17.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/Artifact/Runtime/architecture/status changes update the current checkpoint and corresponding durable docs in the same work cycle.
- Current main may advance independently; exact Candidate evidence remains tied to its tested product source, and final merge must reconcile target-branch state without overwriting parallel work.
- Non-atomic GitHub write chains use the selected checkpoint's batch recovery point and never replay already-confirmed Candidate writes blindly.
- Tooling-only temporary assembly/unpublished commits are never Work/Candidate authority. Exact Stable Phase 8 product authority remains b38 source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; exact b47 product authority is `21028bbff7982abeb42f130c56fcb21e6ef44d7a`, and later docs-only commits do not redefine it.

## Critical invariants / prohibited routes

- Historical hidden WebView chat code is not the native product baseline.
- TD-024 permits only an **explicit user-visible official-Web protected Send surface**; TD-025 rejects the b44 full-page integrated form; TD-028 rejects making the full mobile-Web conversation a required production Send surface after its exact-device long-conversation composer failure.
- Hiding the same slow Web conversation under Native UI is not a performance fix and would violate the protected-Send visibility/security boundary if Native DOM/input automation drives it.
- UI text/titles are never identity authority.
- CI/Artifact success is never Runtime proof.
- Main-app background survival is never WebKit-stream survival proof.
- Manual Sync/Reload/list refresh never create competing state stores or automatic retry machinery.
- No speculative timers, watchdogs, retry loops, shadow WebViews, persisted copied auth/challenge secrets, UA spoofing, Cloudflare/Sentinel bypass, fallback conversation endpoints, DOM mirroring/scraping or speculative parser/header compatibility.
- Do not raise iOS14 minimum without concrete need.
- Stable does not mean Frozen; no Frozen business/architecture rules are currently recorded.

## Code style / naming constraints

Follow existing repository style and established APIs/names. Do not rename interfaces or variables without source-backed need. Keep concise statements on one line where natural.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses belong to an Active checkpoint; completed Work keeps durable conclusions here and history in Git/index.
