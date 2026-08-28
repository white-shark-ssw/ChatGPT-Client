# Project-Specific Rules

This file contains repository/product rules backed by explicit requirements, current source, accepted tests or durable technical decisions.

## Product contracts

- Product goal: **iOS native ChatGPT client**.
- Previous-project history is reference-only, not current protocol authority.
- Durable roadmap: `docs/project/DEVELOPMENT_PLAN.md`.
- Durable UI/interaction baseline: `docs/project/UI_INTERACTION_BASELINE.md`.
- Product delivery priority: reach a genuinely usable TrollStore client early, then iterate with exact real-device candidates.
- Stable merged read baselines remain b9 native read, b15 recovery, b21 multi-conversation read state and b23 conversation-list cache core for their recorded scopes. Stable does not mean Frozen.
- `DEV-conversation-round-count-0.1.0-b29` is the current identity-valid metadata Runtime Candidate. b28 is real-device partial/failing and superseded. b29 is not Stable until exact real-device Runtime passes.

## UI / interaction contract

- Official ChatGPT iOS interaction is the default baseline where acceptable; use native UIKit/system behavior rather than inventing a second UI language.
- UI text/title is a consumer, never identity authority.
- Ordinary conversation actions live in official-style overflow/context surfaces.
- On compact iPhone with no selected conversation, initial useful surface is the conversation list; revealing navigation must not start the initial list request.
- UISplitViewController/native navigation remains the sole compact list/detail navigation owner for the accepted shell.
- Conversation-list right-top refresh and pull-to-refresh are distinct presentation sources over the same repository manual-refresh request path. Right-top refresh must never begin/resize/mutate `UIRefreshControl`; genuine pull uses native spinner + `endRefreshing()` only.
- **Do not use `navigationItem.prompt` for ordinary conversation-list refresh/cache status.** b28 Runtime reproduced the blank top region after refresh-control attributed-title removal, and current source still used prompt status. Because prompt changes navigation-bar height, it changes adjusted top inset. Current fixed-height title/status presentation may be used instead.
- Do not assign attributed/text titles to `UIRefreshControl`, and do not reintroduce b27 contentOffset/top-normalization compensation. The former is unnecessary; Runtime disproved stranded overscroll as the root cause.
- `导出 Markdown` remains an enhancement, not official-App evidence.

## Conversation metadata / Preferences contract

- Round count and previous/next answer navigation consume one `ConversationRoundProjection` derived from the authoritative visible active branch. Do not maintain a second mutable round counter or semantic answer index.
- Each visible authoritative user message starts one round. The first following visible assistant message before the next visible user message is that round's answer anchor. Missing answers are not fabricated; hidden tool/reasoning/system nodes do not create rounds.
- Recompute the lightweight projection when authoritative visible messages change; scroll callbacks consume the derived answer rows and must not rescan all messages every frame.
- `AppPreferences` is the single persisted settings owner. Current defaults remain: `显示会话轮数` On, `显示消息时间` On, `显示回答快速跳转` On.
- Message timestamps use authoritative historical `createTime`; if absent, omit rather than fabricate. Formatting uses current locale/time zone.
- Copy reads only authoritative user-visible message text, uses system pasteboard, does not mutate message state and does not issue network requests. Hidden reasoning/tool/system content is never copied.
- Assistant Copy follows the official compact quick-action visual: small `doc.on.doc`-style outline glyph, clear background, subdued dynamic tint and compact response action row. Current implementation uses 14pt glyph in a 28×28 layout slot; function/time/preferences have prior Runtime acceptance, while final visual scale remains part of the current Work's acceptance.
- Quick answer navigation uses one adaptive floating control and real user-drag direction. Programmatic scrolling is not user intent; no timer-stepped animation or auto-hide watchdog.
- Rapid taps advance from the last requested derived answer target. This transient cursor points into the existing derived answer projection and is not a second semantic authority.
- b28 Runtime on a 1577-visible-message conversation rejected fixed estimated-row geometry for long-distance answer targets: completion errors grew to thousands of points while self-sizing rows resolved. b29 disables the fixed `estimatedRowHeight=96`, lays out before target-offset resolution, and retains the existing interruptible native content-offset animation.
- While a programmatic answer cursor exists and both previous/next remain valid, keep the current clicked direction. Only a **real user drag** or a boundary may change it. b28 Runtime directly rejected falling back to stale `lastUserDragDirection` during continuous programmatic taps.
- No debounce, timer, watchdog or speculative row-height cache may be added without new evidence. Disabling an evidenced-wrong fixed estimate is not authorization for a new height-cache subsystem.
- Current source has no evidenced authoritative Chat/Work conversation-type owner. Ordinary supported detail may present `聊天`; do not infer `工作` from title/presentation text.

## Per-conversation scroll presentation contract

- Scroll presentation belongs to the detail presentation owner, not `ConversationRepository` and not a retained UIKit hierarchy cache.
- Historical reading uses semantic message anchor + relative offset where practical; one global raw offset is prohibited.
- A/B anchors are independent. Account-scope reset clears presentation anchors.
- **First visible presentation with no valid saved reading anchor must show latest/bottom of the current visible branch without visibly animating through history.** Loading/empty placeholder offsets are not reading anchors. b28 Runtime proved this contract was not implemented; b29 adds nonanimated latest placement.
- Sync/Reload may preserve an established anchor only when the same anchored message remains; otherwise discard explicitly rather than invent cross-message fallback.
- Exact b18 accepts the tested historical-anchor matrix. Missing-anchor-message discard remains Runtime-unexercised.
- Future follow-tail belongs to authoritative Send/Stream response lifecycle; do not invent UI streaming flags/timers before that owner exists.

## Fast usable candidate contract

- Do not hold usable functionality until the entire roadmap is complete.
- Every testable candidate has a unique build/Candidate/Artifact identity and keeps Code / Static / CI / Artifact / Runtime / Stable evidence separate.
- Once a Candidate/Artifact identity has been produced, do not rebuild corrected product code under that same identity.
- Files defining one product Candidate's source, version/build, workflow and package identity must be committed atomically enough that one intended Candidate maps to one intended source/config tree.
- Workflow Artifact container naming is not identity proof. Verify built `CFBundleShortVersionString`, `CFBundleVersion`, `DiagnosticsCandidate`, source marker and IPA filename/SHA before Runtime.
- `scripts/build_ipa.sh` must derive identity from built app metadata and fail on Candidate/version/build mismatch; it must not override Candidate with stale per-Work defaults.
- A package-identity failure permanently rejects/reserves that build even when compilation/upload succeed. b24 is the concrete example.

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

## Conversation-list persistent cache contract

- b23 is the Stable merged cache-core baseline for the recorded Plus/personal iPhone/iOS17 scope; PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`. Frozen No.
- `ConversationRepository` remains the sole authoritative list/conversation owner; `ConversationListCacheStore` is storage only.
- Persist only a small versioned account-scoped summary snapshot plus privacy-safe namespace bookkeeping; never Detail/full-body data or copied auth secrets.
- Automatic cold start may provisionally publish last-successfully-verified cached **titles only** before current network verification. Provisional rows cannot authorize Detail until current scope is verified.
- Temporary auth transport failure may retain valid provisional rows without converting it into logout or automatic retry.
- Exact b23 accepts the current 60-second rapid-relaunch freshness window. Manual refresh bypasses suppression and issues exactly one user-requested list refresh.
- Page-1 absence is not deletion evidence. b23 proved `28 + 1 -> 29`; b26 later real-device accepted the authoritative-total cap for stale excess cached rows (`30 -> 29`, repeated `29/29`). b29 does not change that reconciliation.
- Never add timer/polling/watchdog/retry, alternate list/auth endpoints, per-row Detail prefetch or another list/account authority solely for cache behavior.

## Protocol evidence contract

- Do not implement private/internal Web API behavior from history/memory alone.
- Accepted read path remains transient WebKit-derived auth + current list/detail routes documented in project evidence.
- Do not preemptively add account headers, duplicate browser headers, alternate endpoints or compatibility shims without concrete current failure.
- `ProtocolReadProbe` remains diagnostic-only; `ConversationRepository` remains production authority.

## Diagnostics / logging contract

- Use existing `DiagnosticsLogger` authority.
- Never log/export passwords, OAuth codes, tokens, Cookie/Authorization values, raw conversation IDs, full titles, message bodies/parts or raw payloads.
- Multi-conversation correlation uses privacy-safe hashes/counts/generations.
- Cache diagnostics may record schema/hit/age/count/duration/scope hash/decision only.
- Scroll/answer diagnostics may record non-secret row indices, content offsets and landing error, never message identity/body.
- Approximate visible-text bytes are correlation only, not memory-pressure proof.

## Multi-conversation / state-owner contract

- b21 remains the Stable merged multi-conversation read-state baseline for recorded tested scope. One `ConversationRepository` remains production conversation authority.
- Foreground selection is presentation only. Selecting B does not destroy/cancel valid A work merely because A becomes hidden.
- Same-target obsolete operations are rejected by per-target generation/freshness ownership; equivalent loads may coalesce.
- Account scope comes only from accepted auth owner; stale operation context may never re-adopt an older scope.
- Current personal scope uses `userID + accountID`; non-personal workspace isolation remains Unknown/Unverified until evidenced.
- Retain minimum current-node identity only; do not persist raw multi-megabyte graph payloads or invent future send state.
- No arbitrary normal LRU capacity: b19 evidence through 8 residents does not justify one. Memory warnings may trim eligible inactive terminal residents.

## Markdown export / background / compatibility

- Markdown export reads authoritative current user-visible branch, never mounted cells or hidden internal content.
- Background continuation follows `BACKGROUND_EXECUTION_PLAN.md`: response-scoped, no automatic resend or second stream/store; TrollStore privileged background remains isolated future experiment.
- Native iOS / TrollStore IPA; intended ceiling iOS17; current build minimum iOS14; current real-device evidence primarily iPhone/iOS17.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/Artifact/Runtime/architecture/status changes update the current checkpoint and corresponding durable docs in the same work cycle.
- Current main may advance independently; exact Candidate evidence remains tied to its tested product source, and final merge must reconcile target-branch state without overwriting parallel work.

## Critical invariants / prohibited routes

- Historical WebView chat code is not native product baseline; WebView remains authentication/bootstrap only.
- UI text/titles are never identity authority.
- CI/Artifact success is never Runtime proof.
- Manual Sync/Reload/list refresh never create competing state stores or automatic retry machinery.
- No speculative timers, watchdogs, retry loops, shadow WebViews, persisted copied auth secrets, UA spoofing, Cloudflare bypass, fallback conversation endpoints or speculative parser/header compatibility.
- Do not raise iOS14 minimum without concrete need.
- Stable does not mean Frozen; no Frozen business/architecture rules are currently recorded.

## Code style / naming constraints

Follow existing repository style and established APIs/names. Do not rename interfaces or variables without source-backed need. Keep concise statements on one line where natural.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses remain in the Active checkpoint.
