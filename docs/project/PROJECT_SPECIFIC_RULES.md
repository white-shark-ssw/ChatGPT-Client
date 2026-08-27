# Project-Specific Rules

This file contains repository/product rules backed by explicit requirements, current source, accepted tests or durable technical decisions.

## Product contracts

- Product goal: **iOS native ChatGPT client**.
- Previous-project history is reference-only, not current protocol authority.
- Durable roadmap: `docs/project/DEVELOPMENT_PLAN.md`.
- Durable UI/interaction baseline: `docs/project/UI_INTERACTION_BASELINE.md`.
- Product delivery priority: reach a genuinely usable TrollStore client early, then iterate with exact real-device candidates.
- Accepted production native-read baseline remains `DEV-native-read-path-0.1.0-b9` for the tested Plus/personal iPhone/iOS17 scope. Stable, not Frozen.

## UI / interaction contract

- Official ChatGPT iOS interaction is the default baseline where acceptable; use native UIKit/system behavior, not a second UI language.
- UI text/title is a consumer, never identity authority.
- Ordinary conversation actions live in official-style overflow/context menus.
- On compact iPhone with no selected conversation, initial product surface is the conversation list; opening/revealing a sidebar must not start the initial list request.
- UISplitViewController/native navigation is the sole compact list/detail navigation owner for the accepted b14 shell; do not add a duplicate custom sidebar button.
- `导出 Markdown` is our enhancement, not official-App evidence.
- Preserve user-required reasoning interaction/haptics only when current protocol supplies explicit user-visible material; never expose hidden chain-of-thought.

## Fast usable candidate contract

- Do not hold usable functionality until all roadmap phases complete.
- Every testable candidate has a unique build/candidate/artifact identity and keeps Code / CI / Artifact / Runtime / Stable evidence separate.
- Once a Candidate/Artifact identity has actually been produced, do not rebuild corrected product code under that same build/candidate identity.
- When CI runs on every product/config push, all files that define one Candidate's product source, version/build, workflow and packaging identity must be committed atomically enough that one intended Candidate maps to one intended source/config tree. Do not knowingly create multiple different product commits that all publish the same candidate/build identity.

## Manual recovery contract

### `同步最新消息`

- Explicit user-triggered recovery through authoritative `ConversationRepository` for stale/incomplete local state.
- Uses current authoritative conversation identity and current server detail; never resends/regenerates/creates another conversation.
- Preserve an already loaded detail on sync failure when applicable.
- Keep this action available while the ordinary initial detail request is still loading; a stuck ordinary load is itself a valid reason for one explicit manual recovery attempt.
- b12 accepted feedback: centered `正在同步最新消息…`; then centered `已是最新` or `已同步最新消息` for about 2 seconds.

### `重载当前会话`

- Explicit user-triggered recovery for failed, timed-out, blank/spinning, stale or otherwise unusable current conversation.
- Terminal load-error UI provides direct `重新加载`.
- Keep overflow `重载当前会话` available during ordinary initial detail loading, not only after successful load.
- Reload clears/rebuilds selected authoritative detail from one fresh server request; never resends existing messages.
- Duplicate manual recovery taps may be disabled while the manual action itself is active.

### Replacement request lifecycle

- If a newer explicit manual sync/reload replaces an older same-target detail request that is still in flight, `ConversationRepository` must **cancel/replace the older target network task before starting the replacement request**.
- Retain operation-generation/freshness rejection so a late callback from an obsolete task cannot mutate or surface stale state after the newer operation owns that target.
- This cancellation/task handle is request-lifecycle ownership inside the same authoritative repository; it must not become a second conversation-data authority.
- b13 runtime is the evidence for this rule: stale-generation rejection worked, while concurrently started replacement requests returned HTTP429.
- Exact b15 then Runtime-accepted the cancellation-before-replacement fix for the recorded selected-conversation scope: two obsolete generations were cancelled, both replacements returned HTTP200, no HTTP429 appeared, and the user reported no issue. PR #10 is merged.
- Multi-conversation generalization must preserve this same-target ordering per conversation. An implementation detail that leaves the old task handle temporarily unavailable after the old request is already resumed is not sufficient evidence of deterministic cancel-before-replace ownership.

### Recovery diagnostics / prohibited behavior

- Log safe timing/count/diff/state/freshness evidence only; no raw conversation IDs, message bodies, payloads or auth secrets.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- A request-generation/freshness guard and request-task cancellation are allowed at the authoritative owner; neither initiates automatic retries or creates a second store.

## Cold-start authentication contract

- Tested login entry remains embedded `WKWebView`; default persistent `WKWebsiteDataStore` is sole persistent auth-secret authority.
- Do not persist copied cookies/tokens/session values outside WebKit; transient native copies remain ephemeral.
- Native `/auth/login` is not an account-context prerequisite. Sequencing remains current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- b12 real-device evidence proves one public `WKWebsiteDataStore.default()` warm-up can hydrate usable persisted auth for the tested iPhone/iOS17 cold start.
- This tested-scope result does not justify retry loops or hidden/shadow WebViews and does not prove all install/update/session states.
- After warm-up, initial conversation-list loading must begin independently of any manual sidebar reveal.

## Protocol evidence contract

- Do not implement private/internal Web API behavior from history/memory alone.
- Accepted tested read path remains transient bearer + ephemeral WebKit cookies with current conversation list/detail routes documented in project evidence.
- Do not preemptively add `chatgpt-account-id`, duplicate browser headers, alternate endpoints or compatibility shims without concrete current failure.
- `ProtocolReadProbe` remains diagnostic-only; `ConversationRepository` remains production conversation owner.

## Diagnostics / logging contract

- Use existing `DiagnosticsLogger`/store/export authority.
- Never log/export passwords, OAuth codes, access/refresh/session tokens, Cookie/Authorization values, raw conversation IDs, full titles, message bodies/parts or raw payloads.
- New multi-conversation correlation should use privacy-safe irreversible conversation markers and non-secret counts/generations; old/new selection traces must not expose raw IDs.
- Approximate visible-text byte counts may be used as correlation data but are not a substitute for actual memory-footprint/runtime evidence when choosing resident capacity.

## Multi-conversation / state-owner contract

- `DEV-multi-conversation-state` is now Active after merged recovery. Current b16 source has Code + CI evidence only; its Artifact identity is rejected and multi-conversation runtime behavior is not accepted yet.
- One `ConversationRepository` remains production conversation authority. Evolve it to account-scoped per-conversation resident/operation entries; do not create one repository per screen or use retained UIKit hierarchy/navigation stack as conversation-state authority.
- Foreground selection is presentation state only. Loading, Sync, Reload and future response work target an authoritative conversation identity without changing selection as a side effect.
- Selection change alone does not cancel another conversation's valid request/work and is not a reason to discard a valid hidden-conversation result.
- Same-conversation obsolete operations are rejected by target-specific freshness/generation ownership. Equivalent same-target missing-detail loads may coalesce, but every collected waiter must have a deterministic terminal contract; do not silently abandon waiters on supersede/account reset as the final design.
- Account scope comes only from the accepted auth owner. A delayed conversation/list/detail operation context may never re-establish an older account scope after a newer verified context exists. Old-scope callbacks are rejected; they are not account authority.
- Current active source uses `userID + accountID` for personal-account scope. Do not claim this proves non-personal workspace isolation until current service evidence establishes whether another workspace identity is required.
- Retain minimum evidence-backed authoritative branch identity such as current `current_node`; do not retain raw multi-megabyte mapping payloads or invent future send graph requirements.
- Resident terminal failures may remain in memory so ordinary navigation does not become implicit network retry. Explicit Reload remains the user-owned retry/rebuild action.
- A loaded conversation may remain visible while explicit Sync is in flight, but navigating away/back must not lose the active target's terminal update. Recovery presentation may be lightweight/per-conversation, but must not become a second conversation-data authority.
- List/account presentation also needs freshness protection: late old-scope/superseded list completion must not clear/overwrite a newer list operation's UI state.
- Mutable resident/session/list/operation authority must use one explicit execution domain. Network transfer and JSON parsing may be off-main; mutable repository state and list-position/state reads may not race across URLSession and UI callbacks.
- Memory warning may trim eligible inactive resident terminal states through the repository owner. A normal-operation bounded LRU policy is not frozen until real-device measurement; approximate text bytes alone do not justify a capacity number.
- Semantic scroll-anchor restoration is P1 in the architecture gap review. It is useful within this Work but does not block the first valid core multi-conversation runtime Candidate unless a later explicit user requirement changes priority.

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

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses stay in the active checkpoint.
