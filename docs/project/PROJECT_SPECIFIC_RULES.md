# Project-Specific Rules

This file contains repository/product rules backed by explicit requirements, current source, accepted tests or durable technical decisions.

## Product contracts

- Product goal: **iOS native ChatGPT client**.
- Previous-project history is reference-only, not current protocol authority.
- Durable roadmap: `docs/project/DEVELOPMENT_PLAN.md`.
- Durable UI/interaction baseline: `docs/project/UI_INTERACTION_BASELINE.md`.
- Product delivery priority: reach a genuinely usable TrollStore client early, then iterate with exact real-device candidates.
- Accepted production native-read baseline remains `DEV-native-read-path-0.1.0-b9` for tested Plus/personal iPhone/iOS17 scope. Stable, not Frozen.

## UI / interaction contract

- Official ChatGPT iOS interaction is the default baseline where acceptable; use native UIKit/system behavior, not a second UI language.
- UI text/title is a consumer, never identity authority.
- Ordinary conversation actions live in official-style overflow/context menus.
- On compact iPhone with no selected conversation, initial product surface is the conversation list; opening/revealing a sidebar must not start the initial list request.
- UISplitViewController/native navigation is the sole compact list/detail navigation owner for accepted b14 shell; do not add a duplicate custom sidebar button.
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
- Multi-conversation generalization preserves this same-target rule per conversation. Exact b18 did not naturally isolate an older in-flight Detail -> newer Reload replacement sequence, so that specific regression gate remains open rather than inferred from ordinary Reload success.

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

## Protocol evidence contract

- Do not implement private/internal Web API behavior from history/memory alone.
- Accepted tested read path remains transient bearer + ephemeral WebKit cookies with current conversation list/detail routes documented in project evidence.
- Do not preemptively add `chatgpt-account-id`, duplicate browser headers, alternate endpoints or compatibility shims without concrete current failure.
- `ProtocolReadProbe` remains diagnostic-only; `ConversationRepository` remains production conversation owner.

## Diagnostics / logging contract

- Use existing `DiagnosticsLogger`/store/export authority.
- Never log/export passwords, OAuth codes, access/refresh/session tokens, Cookie/Authorization values, raw conversation IDs, full titles, message bodies/parts or raw payloads.
- Multi-conversation correlation uses privacy-safe irreversible conversation markers and non-secret counts/generations.
- Scroll-anchor diagnostics may record non-secret row indices/relative offset and save/restore/discard reason but never raw message identity/body.
- Approximate visible-text byte counts may be correlation data but are not actual memory-footprint evidence for LRU capacity.

## Multi-conversation / state-owner contract

- `DEV-multi-conversation-state` is Active after merged recovery. b16 is historical/rejected before runtime; b17 has accepted core real-device evidence with reproduced historical-scroll defect; exact b18 source `f30c13b4ac2c40dcda829585682825ca906dceae` now has Code + source/static + CI + identity-valid Artifact + **real-device historical-scroll Runtime acceptance for the tested iPhone/iOS17 matrix**. Work remains not Stable/Frozen.
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
- Memory warning may trim eligible inactive terminal residents. Normal bounded LRU policy remains unfrozen until real **process/system memory** measurement; approximate text bytes alone are insufficient.
- Exact b18 Runtime evidence may close only the tested paths: independent historical anchors, first-time target isolation, Sync/Reload anchor preservation when the anchored message remains, resident return and active Sync coalescing. It does not automatically close natural failure residency, supported account-switch isolation, normal LRU policy or unexercised replacement paths.

## Per-conversation scroll presentation contract

- Scroll presentation metadata belongs to the existing detail presentation owner, not `ConversationRepository` and not a retained UIKit hierarchy per conversation.
- Historical reading uses a semantic anchor tied to message identity plus relative visual offset where practical; one global raw `contentOffset` is prohibited.
- A/B scroll presentation is independent. Switching/scrolling B must not mutate A's saved anchor.
- A target with no saved anchor starts from its normal top instead of inheriting another conversation's offset.
- Account-scope reset clears presentation anchors.
- Visible Sync/Reload may preserve the historical anchor only if the same anchored message remains in the refreshed current branch. If it disappears, do not invent a cross-message fallback.
- Exact b18 iPhone/iOS17 Runtime **accepts** the tested historical-anchor behavior: user reported no issue; diagnostics show repeated A/B saved/restored pairs, first-time third-conversation isolation, Sync/Reload preservation, resident hits and same-target Sync coalescing, with all recorded HTTP statuses 200 and no error/HTTP429.
- Anchored-message disappearance did not occur naturally in b18, so `scrollAnchor.discarded -> top` remains source/CI-defined and Runtime-unverified; do not manufacture destructive branch mutation solely to trigger it.
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
- `ConversationRepository` is production conversation read/recovery owner; UI titles/text are never identity.
- CI/artifact success is not runtime proof.
- Manual sync/reload never create competing state stores or automatic retry machinery.
- No speculative timers, watchdogs, shadow WebViews, retry loops, auth fallback chains, persisted copied auth secrets, UA spoofing, Cloudflare bypass, fallback conversation endpoints or speculative parser/header compatibility.
- Do not raise iOS14 minimum without concrete need.
- Stable does not mean Frozen; no Frozen business/architecture rules are currently recorded.

## Code style / naming constraints

Follow existing repository style and established APIs/names. Do not rename interfaces or variables without source-backed need.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for advisory previous-project lessons.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses stay in active checkpoint.
