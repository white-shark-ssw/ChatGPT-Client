# Project-Specific Rules

This file contains repository/product rules backed by explicit requirements, current source, accepted tests or durable technical decisions.

## Product contracts

- Product goal: **iOS native ChatGPT client**.
- Previous-project history is reference-only, not current protocol authority.
- Durable roadmap: `docs/project/DEVELOPMENT_PLAN.md`.
- Durable UI/interaction baseline: `docs/project/UI_INTERACTION_BASELINE.md`.
- Product delivery priority: reach a genuinely usable TrollStore client early, then iterate with exact real-device candidates.
- Accepted production native-read baseline remains `DEV-native-read-path-0.1.0-b9` for tested Plus/personal iPhone/iOS17 scope. Stable, not Frozen.
- Accepted merged multi-conversation read-state baseline is `DEV-multi-conversation-state-0.1.0-b21` for the recorded Plus/personal iPhone/iOS17 scope; PR #23 merged. Stable, not Frozen.
- Accepted merged conversation-list cache-core baseline is `DEV-conversation-list-cache-core-0.1.0-b23` for the recorded Plus/personal iPhone/iOS17 scope; PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`. Stable, not Frozen.

## UI / interaction contract

- Official ChatGPT iOS interaction is the default baseline where acceptable; use native UIKit/system behavior, not a second UI language.
- UI text/title is a consumer, never identity authority.
- Ordinary conversation actions live in official-style overflow/context menus.
- On compact iPhone with no selected conversation, initial product surface is the conversation list; opening/revealing a sidebar must not start the initial list request.
- UISplitViewController/native navigation is the sole compact list/detail navigation owner for accepted b14 shell; do not add a duplicate custom sidebar button.
- Conversation-list manual refresh feedback uses the centered navigation prompt above the `ChatGPT` title. Accepted b23 states are `正在刷新会话列表…`, `已刷新 · N 条`, and retained-cache failure `刷新失败 · 当前显示缓存`.
- `导出 Markdown` is our enhancement, not official-App evidence.
- Preserve user-required reasoning interaction/haptics only when current protocol supplies explicit user-visible material; never expose hidden chain-of-thought.

## Fast usable candidate contract

- Do not hold usable functionality until all roadmap phases complete.
- Every testable candidate has a unique build/candidate/artifact identity and keeps Code / CI / Artifact / Runtime / Stable evidence separate.
- Once a Candidate/Artifact identity has actually been produced, do not rebuild corrected product code under that same build/candidate identity.
- When CI runs on every product/config push, all files that define one Candidate's product source, version/build, workflow and packaging identity must be committed atomically enough that one intended Candidate maps to one intended source/config tree.

## Manual recovery contract

### `同步最新消息`

- Explicit user-triggered recovery through authoritative `ConversationRepository` for stale/incomplete local state.
- Uses current authoritative conversation identity and current server detail; never resends/regenerates/creates another conversation.
- Preserve an already loaded detail on sync failure when applicable.
- Keep this action available while ordinary initial detail request is still loading.
- b12 accepted feedback: centered `正在同步最新消息…`; then centered `已是最新` or `已同步最新消息` for about 2 seconds.

### `重载当前会话`

- Explicit user-triggered recovery for failed, timed-out, blank/spinning, stale or otherwise unusable current conversation.
- Terminal load-error UI provides direct `重新加载`.
- Keep overflow `重载当前会话` available during ordinary initial detail loading.
- Reload clears/rebuilds selected authoritative detail from one fresh server request; never resends existing messages.
- Duplicate manual recovery taps may be disabled while the manual action itself is active.

### Replacement request lifecycle

- If a newer explicit manual sync/reload replaces an older same-target detail request still in flight, `ConversationRepository` must cancel/replace the older target network task before starting the replacement request.
- Retain operation-generation/freshness rejection so late obsolete callbacks cannot mutate newer authoritative state.
- Cancellation/task handle is request-lifecycle ownership inside the same repository, not a second conversation authority.
- b13 runtime proved freshness rejection alone while overlapping replacement requests could HTTP429.
- b15 Runtime accepted deterministic cancellation-before-replacement for recorded selected-conversation scope: obsolete requests cancelled, replacements HTTP200, no HTTP429.
- Merged multi-conversation implementation preserves this same-target rule per conversation. Exact b21 diagnostics accept two same-target ordinary-load -> Reload replacement sequences: older generation cancelled; replacement generation HTTP200; unrelated conversation remained independent; returning to the target while Reload was active coalesced onto the same replacement rather than starting a duplicate request.

### Recovery diagnostics / prohibited behavior

- Log safe timing/count/diff/state/freshness evidence only; no raw conversation IDs, message bodies, payloads or auth secrets.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- Request-generation/freshness guards and target task cancellation are allowed at the authoritative owner; neither initiates automatic retries or creates a second store.

## Cold-start authentication contract

- Tested login entry remains embedded `WKWebView`; default persistent `WKWebsiteDataStore` is sole persistent auth-secret authority.
- Do not persist copied cookies/tokens/session values outside WebKit; transient native copies remain ephemeral.
- Native `/auth/login` is not an account-context prerequisite. Sequencing remains WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- b12 real-device evidence proves one public `WKWebsiteDataStore.default()` warm-up can hydrate usable persisted auth for tested iPhone/iOS17 cold start.
- This tested result does not justify retry loops or hidden/shadow WebViews and does not prove all install/update/session states.
- After warm-up, initial conversation-list loading begins independently of manual sidebar reveal.
- Cache-core does **not** change auth authority: a last-successfully-verified cache namespace hint may provisionally identify which cached list titles to present, but it can never establish verified account/transport state or authorize Detail.

## Conversation-list persistent cache contract

- `DEV-conversation-list-cache-core-0.1.0-b23` is the **Stable merged cache-core baseline** for the recorded Plus/personal iPhone/iOS17 scope. Exact Runtime source `d2af0fc157f6e2d037636c55f963c18071a332d5`; PR #24 merge-view Run `33103769517` / Job `98628067286` passed on `26297ff0683966c2c82fd7a8a95f53f1ad51d3d6`; PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`. Frozen remains No.
- `ConversationRepository` remains the single authoritative list/conversation owner; `ConversationListCacheStore` is storage only and the sidebar never becomes a second cache/list owner.
- Persist only a small versioned account-scoped summary snapshot plus privacy-safe bookkeeping. Do not persist Detail/full-body data for this feature.
- Cache namespace uses a SHA-256-derived scope value. b23 additionally persists only that 64-hex namespace in `last-verified-scope.txt`; never persist raw account/user IDs for routing.
- On automatic cold start, a valid last-successfully-verified scope snapshot may provisionally publish **list titles only** before current network account verification completes. This is the accepted correction to b22's visible blank/offline failure behavior.
- Provisional/offline cached rows must not start Detail until current account scope is actually verified. The list may explain `当前仅显示缓存，联网验证账户后可打开会话`.
- Matching verified scope keeps the provisional rows and applies normal freshness logic. A different newly verified scope or confirmed unauthenticated/unavailable result rejects the old provisional presentation.
- Temporary auth transport failure may retain valid provisional rows as offline list presentation. It must not be reinterpreted as confirmed logout and must not start an automatic retry chain.
- Exact b23 accepts a 60-second rapid-relaunch freshness window for the recorded current use case: recent cache may skip that launch's automatic list request; stale cache performs one refresh; manual refresh always bypasses suppression.
- Manual refresh emits one user-requested list request and provides visible terminal feedback. Failure with valid cached rows keeps rows visible.
- Page-1 absence is never deletion evidence. Exact b23 Runtime proves a returned page of 28 with server total 29 preserves one real off-page cached row (`preservedOffPageCount=1`, result 29) across automatic and manual reconciliation.
- Cache storage uses app-private Application Support, Data Protection and atomic writes; corrupt/schema-incompatible data may be discarded deliberately without retry loop.
- Never add timer/polling/watchdog/retry, alternate list/auth endpoint, speculative ETag behavior, per-row Detail prefetch or another list/account authority solely for cache-core.
- Runtime below iOS17, iPad, supported real account-switch mismatch, provisional-row Detail-block tap and corrupt/schema-rejection remain conditional Unknown / Unverified until evidenced.

## Protocol evidence contract

- Do not implement private/internal Web API behavior from history/memory alone.
- Accepted tested read path remains transient bearer + ephemeral WebKit cookies with current conversation list/detail routes documented in project evidence.
- Do not preemptively add `chatgpt-account-id`, duplicate browser headers, alternate endpoints or compatibility shims without concrete current failure.
- `ProtocolReadProbe` remains diagnostic-only; `ConversationRepository` remains production conversation owner.

## Diagnostics / logging contract

- Use existing `DiagnosticsLogger`/store/export authority.
- Never log/export passwords, OAuth codes, access/refresh/session tokens, Cookie/Authorization values, raw conversation IDs, full titles, message bodies/parts or raw payloads.
- Multi-conversation correlation uses privacy-safe irreversible conversation markers and non-secret counts/generations.
- Cache diagnostics may record schema, hit/miss, age, entry counts, duration, privacy-safe scope hash and decisions such as `recent_skip`, `stale`, `manual_bypass`, `offline_cache`; never cached titles/text or raw scope identities.
- Scroll-anchor diagnostics may record non-secret row indices/relative offset and save/restore/discard reason but never raw message identity/body.
- Approximate visible-text byte counts may be correlation data but are not actual memory-footprint evidence for LRU capacity.

## Multi-conversation / state-owner contract

- `DEV-multi-conversation-state-0.1.0-b21` is the **Stable merged multi-conversation read-state baseline** for the tested Plus/personal iPhone/iOS17 scope. PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`. Frozen remains No.
- One `ConversationRepository` remains production conversation authority. Do not create one repository per screen or use retained UIKit hierarchy/navigation stack as conversation-state authority.
- Foreground selection is presentation state only. Loading, Sync, Reload and future response work target authoritative conversation identity without changing selection as side effect.
- Selection change alone does not cancel another conversation's valid request/work and is not a reason to discard a valid hidden result.
- Same-conversation obsolete operations are rejected by target-specific freshness/generation ownership. Equivalent same-target missing-detail loads may coalesce, but every waiter has deterministic terminal contract.
- Account scope comes only from accepted auth owner. Delayed operation/transport context may never re-establish an older scope after newer verified context exists.
- Current source uses `userID + accountID` for personal-account scope. Do not claim non-personal workspace isolation until current service evidence establishes any additional identity.
- Retain minimum evidence-backed authoritative branch identity such as `current_node`; do not retain raw multi-megabyte mapping payloads or invent future send graph requirements.
- Resident terminal failures may remain in memory so navigation does not become implicit network retry. Explicit Reload remains user-owned retry/rebuild action.
- A loaded conversation may remain visible while explicit Sync is in flight; navigating away/back must not lose target terminal update.
- List/account presentation needs freshness protection so late old-scope/superseded completion cannot clear/overwrite newer presentation.
- Mutable resident/session/list/operation authority uses one explicit execution domain. Network transfer/pure parsing may be off-owner.
- b19 real task-VM evidence shows no immediate pressure through 8 residents; do not add or freeze an arbitrary normal LRU capacity. Memory warning may trim eligible inactive terminal residents.
- Supported account-switch purge remains Runtime-unverified until a real supported switch/logout route exists. Do not create fake account transition UI to prove it.
- Missing-anchor-message discard remains source/CI-defined and Runtime-unexercised; no current defect evidence justifies destructive branch mutation solely to exercise it.
- Stable is scoped to recorded tested behavior only: runtime below iOS17, iPad, non-personal workspaces and conditional paths remain Unknown / Unverified where applicable.

## Per-conversation scroll presentation contract

- Scroll presentation metadata belongs to the existing detail presentation owner, not `ConversationRepository` and not a retained UIKit hierarchy per conversation.
- Historical reading uses a semantic anchor tied to message identity plus relative visual offset where practical; one global raw `contentOffset` is prohibited.
- A/B scroll presentation is independent. Switching/scrolling B must not mutate A's saved anchor.
- A target with no saved anchor starts from its normal top instead of inheriting another conversation's offset.
- Account-scope reset clears presentation anchors.
- Visible Sync/Reload may preserve the historical anchor only if the same anchored message remains in the refreshed current branch. If it disappears, do not invent a cross-message fallback.
- Exact b18 iPhone/iOS17 Runtime accepts the tested historical-anchor behavior. Anchored-message disappearance remains Runtime-unexercised.
- Future active-response `follow-tail` behavior must consume the authoritative per-conversation Send/Stream response lifecycle. Do not invent UI `isStreaming`, timer, response flag or unused future state to fake follow-tail before Send/Stream exists.
- User-confirmed future rule: if A is at/near bottom with an active authoritative response and grows/completes while hidden, returning A shows A's current latest bottom; intentional upward scrolling exits follow-tail and establishes historical-reading intent.

## Markdown export contract

- Export authoritative current user-visible branch to Markdown, not mounted cells.
- Never export hidden/internal reasoning/tool content.

## Background execution contract

- Durable plan: `docs/project/BACKGROUND_EXECUTION_PLAN.md`.
- Background continuation is response-scoped; no automatic resend or second stream/store.
- Public iOS APIs do not guarantee user-selected 30m/1h execution windows.
- TrollStore true-background remains a later isolated experiment and must not grant broad private entitlements to the main authenticated app without evidence.

## Compatibility / deployment constraints

- Native iOS; TrollStore IPA.
- Intended environment ceiling iOS17; current build minimum iOS14.
- Current runtime evidence covers iPhone/iOS17 only unless explicitly stated otherwise.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/artifact/runtime/architecture/status changes update current checkpoint and durable docs in the same work cycle.
- Current `main` may advance through parallel docs/planning work; exact Candidate evidence remains tied to its tested product source, and final merge must synchronize target-branch docs without overwriting parallel planning.

## Critical invariants / prohibited routes

- Historical WebView chat code is not native product baseline; WebView remains authentication/bootstrap only.
- `ConversationRepository` is production conversation read/recovery/list-cache owner; UI titles/text are never identity.
- CI/artifact success is not runtime proof.
- Manual sync/reload/list refresh never create competing state stores or automatic retry machinery.
- No speculative timers, watchdogs, shadow WebViews, retry loops, auth fallback chains, persisted copied auth secrets, UA spoofing, Cloudflare bypass, fallback conversation endpoints or speculative parser/header compatibility.
- Do not raise iOS14 minimum without concrete need.
- Stable does not mean Frozen; no Frozen business/architecture rules are currently recorded.

## Code style / naming constraints

Follow existing repository style and established APIs/names. Do not rename interfaces or variables without source-backed need.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for advisory previous-project lessons.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses stay in active checkpoint.