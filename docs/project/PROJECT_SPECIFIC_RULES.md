# Project-Specific Rules

This file contains repository/product rules backed by explicit requirements, current source, accepted tests or durable technical decisions.

## Product contracts

- Product goal remains an **iOS native ChatGPT client shell/read experience**, with one explicit Phase 9 exception recorded by TD-024: ChatGPT-account Send may use a **user-visible official ChatGPT Web surface** because exact b42 Runtime proved the pure-native account-session Send path depends on browser anti-abuse challenge output.
- The hybrid Send surface is not pure-native Send and must never be described as such.
- Previous-project history is reference-only, not current protocol authority.
- Durable roadmap: `docs/project/DEVELOPMENT_PLAN.md`.
- Durable UI/interaction baseline: `docs/project/UI_INTERACTION_BASELINE.md`.
- Product delivery priority: reach a genuinely usable TrollStore client early, then iterate with exact real-device Candidates.
- Stable merged baselines include b9 native read, b15 recovery, b21 multi-conversation read state, b23 conversation-list cache core, and **b38 Phase 8 conversation metadata/settings/round navigation** for their recorded scopes. Stable does not mean Frozen.
- Exact Phase 8 accepted Candidate is `DEV-conversation-round-count-0.1.0-b38`, exact tested product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Phase 8 remains Stable / merged, Frozen No.

## UI / interaction contract

- Official ChatGPT iOS interaction is the default baseline where acceptable; use native UIKit/system behavior rather than inventing a second UI language.
- UI text/title is a consumer, never identity authority.
- Ordinary native conversation actions live in official-style overflow/context surfaces.
- On compact iPhone with no selected conversation, initial useful surface is the native conversation list; revealing navigation must not start the initial list request.
- `UISplitViewController`/native navigation remains the native shell's compact list/detail navigation owner.
- Conversation-list right-top refresh and pull-to-refresh are distinct presentation sources over the same repository manual-refresh request path. Right-top refresh must never begin/resize/mutate `UIRefreshControl`; genuine pull uses native spinner + `endRefreshing()` only.
- Do not use `navigationItem.prompt` for ordinary conversation-list refresh/cache status. b29 Runtime accepts removal of the prompt-induced blank/top-inset growth for the tested right-top refresh path.
- Do not assign attributed/text titles to `UIRefreshControl`, and do not reintroduce b27 contentOffset/top-normalization compensation.

## User-visible hybrid Web Send contract

- The user explicitly selected the Option-2 architecture after b42: native shell/read/navigation + **user-visible official ChatGPT Web Send**.
- The Web surface must be visibly presented as the user's active interaction surface. It must never become a hidden/shadow WebView used to harvest Sentinel/Turnstile/PoW output for a native replay path.
- Use the existing default persistent `WKWebsiteDataStore`; do not add another persistent credential/challenge store.
- `ConversationRepository` remains sole native conversation/list/detail/recovery authority. `AuthSessionStore` remains native auth/account authority. The visible Web surface owns only its own official Web session/Send interaction while presented and does not become a second native repository.
- The first accepted implementation direction is one process-resident shared visible Web controller/WebView so ordinary Back -> re-entry can reuse the loaded page instead of avoidable reconstruction/reload.
- Do not continuously observe the DOM, scrape prompt/answer/reasoning text, mirror Web message state into native state, capture challenge/token values, or replay browser proof output.
- Do not guess current-conversation Web deep links such as `/c/<id>` or programmatic Web file-input injection without current evidence.
- Functional Web Send alone is insufficient. Exact-device Runtime on the primary iPhone/iOS17 target must accept first-entry response, resident re-entry, keyboard/typing, Send/stream scrolling, rapid scrolling, native return and attachment `+` responsiveness.
- Attachment `+` is a hard UX gate: local selection UI must not be delayed by page navigation, network, Sentinel/Turnstile or upload preparation. The exact native-picker -> official-Web handoff remains Unknown/Unverified until separately evidenced.
- Exact b43 `DEV-send-stream-0.1.0-b43`, source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, is Code/CI/Artifact valid but **not Runtime accepted** until exact-device user testing passes.

## Conversation metadata / Preferences contract

- Round count and previous/next round navigation consume one `ConversationRoundProjection` derived from the authoritative visible active branch. Do not maintain a second mutable round counter or semantic navigation index.
- Each visible authoritative user message starts one round. The accepted physical quick-navigation target is the **round-start user message**. Hidden tool/reasoning/system/internal-recipient nodes do not create ordinary rounds.
- Recipient/internal filtering remains upstream of ordinary visible chat-row projection. b32 Runtime accepted filtering of tool/internal recipient rows before round/message presentation.
- `AppPreferences` is the single persisted native settings owner. Current defaults remain: `显示会话轮数` On, `显示消息时间` On, `显示轮次快速跳转` On.
- Message timestamps use authoritative historical `createTime`; if absent, omit rather than fabricate. Formatting uses current locale/time zone.
- Copy reads only authoritative user-visible message text, uses system pasteboard, does not mutate message state and does not issue network requests. Hidden reasoning/tool/system content is never copied.
- Assistant Copy remains a compact official-style quick action with clear background and subdued dynamic tint. User context Copy remains native.

## Long-conversation presentation geometry contract

- b36 exact Runtime proved the dominant stutter owner was deferred giant-row/table geometry, not quick-navigation animation alone: direct positioning reached ~3952ms in the tested trace and ordinary right-side scroll-indicator dragging also severely stuttered.
- The Stable b37/b38 native presentation baseline uses `ConversationMessagePresentationProjection` as **ephemeral derived presentation state only**. It is not conversation authority and must never become a persistent second message store.
- Very long plain-text messages are split into bounded display chunks for native presentation virtualization. Concatenated authoritative message content is unchanged; Copy always reads the full authoritative message.
- Presentation derives deterministic row heights and prefix offsets for the current detail/layout width before interaction. Round targets and scroll anchors consume this geometry rather than asking UITableView to discover giant self-sized rows while scrolling.
- `ConversationMessageCell` uses deterministic manual frame layout for one bounded display chunk. Do not restore one unbounded whole-message multiline UILabel + deferred automatic estimated geometry without new exact Runtime evidence.
- Width/presentation changes may rebuild this ephemeral geometry. Do not persist row heights across unrelated details/layout widths as a new durable cache owner.
- b37 exact-device feedback accepted this geometry/performance direction; b38 preserved it and the merged Phase 8 baseline is Stable, Frozen No.

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
- Exact b24-b43 identities and emitted artifacts are permanently reserved. The accidental newer-code Artifact `9710515489` carrying b42 identity is permanently rejected and must never be installed; legitimate b42 remains Artifact `9709824510`.

## Manual recovery contract

### `同步最新消息`

- Explicit user recovery through authoritative `ConversationRepository`; current target only, never resend/regenerate.
- Preserve an already loaded detail on sync failure where applicable.
- Keep available during ordinary initial Detail loading.
- Accepted feedback remains centered `正在同步最新消息…`, then `已是最新` or `已同步最新消息` for about 2 seconds.

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
- TD-024's explicit visible Web Send surface uses the same default data store; its existence does not authorize hidden Web hydration/challenge harvesting.

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

## Diagnostics / logging contract

- Use existing `DiagnosticsLogger` authority.
- Never log/export passwords, OAuth codes, tokens, Cookie/Authorization values, raw conversation IDs, full titles, message bodies/parts, raw payloads, Sentinel/Turnstile/PoW values or Web prompt/answer text.
- Hybrid `webSend` diagnostics may record safe presentation/reuse/navigation timing, destination class/host and failure class only.
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

- Background continuation follows `BACKGROUND_EXECUTION_PLAN.md`: response-scoped, no automatic resend or second stream/store; TrollStore privileged background remains isolated future experiment.
- The visible hybrid Web surface does not by itself establish a native response owner suitable for background-completion claims.
- Native iOS / TrollStore IPA; intended ceiling iOS17; current build minimum iOS14; current real-device evidence primarily iPhone/iOS17.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/Artifact/Runtime/architecture/status changes update the current checkpoint and corresponding durable docs in the same work cycle.
- Current main may advance independently; exact Candidate evidence remains tied to its tested product source, and final merge must reconcile target-branch state without overwriting parallel work.
- Non-atomic GitHub write chains use the selected checkpoint's batch recovery point and never replay already-confirmed Candidate writes blindly.
- Tooling-only temporary assembly/unpublished commits are never Work/Candidate authority. Exact Stable Phase 8 product authority remains b38 source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; exact b43 product/config authority is `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c` pending Runtime.

## Critical invariants / prohibited routes

- Historical hidden WebView chat code is not the native product baseline. The only current Send exception is TD-024's **explicit user-visible official-Web Send surface**; hidden/shadow Web transport remains prohibited.
- UI text/titles are never identity authority.
- CI/Artifact success is never Runtime proof.
- Manual Sync/Reload/list refresh never create competing state stores or automatic retry machinery.
- No speculative timers, watchdogs, retry loops, shadow WebViews, persisted copied auth/challenge secrets, UA spoofing, Cloudflare/Sentinel bypass, fallback conversation endpoints, DOM mirroring/scraping or speculative parser/header compatibility.
- Do not raise iOS14 minimum without concrete need.
- Stable does not mean Frozen; no Frozen business/architecture rules are currently recorded.

## Code style / naming constraints

Follow existing repository style and established APIs/names. Do not rename interfaces or variables without source-backed need. Keep concise statements on one line where natural.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses belong to an Active checkpoint; completed Work keeps durable conclusions here and history in Git/index.
