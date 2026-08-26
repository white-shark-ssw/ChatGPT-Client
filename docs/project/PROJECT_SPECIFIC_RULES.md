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
- On compact iPhone, the sidebar/navigation affordance must be usable immediately once the native shell is configured; revealing the sidebar must not be what starts the initial list request.
- `导出 Markdown` is our enhancement, not official-App evidence.
- Preserve user-required reasoning interaction/haptics only when current protocol supplies explicit user-visible material; never expose hidden chain-of-thought.

## Fast usable candidate contract

- Do not hold usable functionality until all roadmap phases complete.
- Every testable candidate has a unique build/candidate/artifact identity and keeps Code / CI / Artifact / Runtime / Stable evidence separate.

## Manual recovery contract

### `同步最新消息`

- Explicit user-triggered recovery through the authoritative `ConversationRepository` for stale/incomplete local state.
- Uses current authoritative conversation identity and current server detail; never resends/regenerates/creates another conversation.
- Preserve an already loaded detail on sync failure when applicable.
- **Keep this action available while the ordinary initial detail request is still loading.** A stuck ordinary load is itself a valid reason for one explicit manual recovery attempt.
- b12 accepted feedback: centered `正在同步最新消息…`; then centered `已是最新` or `已同步最新消息` for about 2 seconds.

### `重载当前会话`

- Explicit user-triggered recovery for failed, timed-out, blank/spinning, stale or otherwise unusable current conversation.
- Terminal load-error UI provides direct `重新加载`.
- **Keep overflow `重载当前会话` available during the ordinary initial detail-loading state**, not only after successful load.
- Reload clears/rebuilds the selected authoritative detail from one fresh server request; never resends existing messages.
- If a newer manual sync/reload starts while an older ordinary selected-detail request is in flight, the production owner must reject the older completion as obsolete so it cannot overwrite the newer recovery result.
- Duplicate manual recovery taps may be disabled while the manual action itself is active.

### Recovery diagnostics / prohibited behavior

- Log safe timing/count/diff/state/freshness evidence only; no raw IDs, message bodies, payloads or auth secrets.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- A request-generation/freshness guard is allowed as part of the authoritative owner; it is not a second data store and does not initiate requests by itself.

## Cold-start authentication contract

- Tested login entry remains embedded `WKWebView`; default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority.
- Do not persist copied cookies/tokens/session values outside WebKit; transient native copies remain ephemeral.
- Native `/auth/login` is not an account-context prerequisite. Current sequencing remains current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- b12 real-device evidence on iPhone/iOS17 proves one public `WKWebsiteDataStore.default()` warm-up can hydrate usable persisted auth: cookie visibility moved from 0/0 to 41/22 and the later single normal account/list probe succeeded without opening Login.
- This tested-scope result does not justify retry loops or hidden/shadow WebViews and does not prove all install/update/session states.
- After warm-up, initial conversation-list loading must begin independently of whether the compact-iPhone primary/sidebar view has been manually revealed.

## Protocol evidence contract

- Do not implement private/internal Web API behavior from history/memory alone.
- Accepted tested read path remains transient bearer + ephemeral WebKit cookies with conversation list/detail routes documented in current project evidence.
- Do not preemptively add `chatgpt-account-id`, duplicate browser headers, alternate endpoints or compatibility shims without a concrete current failure.
- `ProtocolReadProbe` remains diagnostic-only; `ConversationRepository` remains production conversation owner.

## Diagnostics / logging contract

- Use existing `DiagnosticsLogger`/store/export authority.
- Never log/export passwords, OAuth codes, access/refresh/session tokens, Cookie/Authorization values, raw conversation IDs, full titles, message bodies/parts or raw payloads.
- Safe auth diagnostics may record cookie total/matched counts only.
- Safe production conversation diagnostics may use short irreversible conversation hash + list position and operation-generation/discard reason.

## Multi-conversation / state-owner direction

- Current b13 freshness generation is intentionally scoped to the current single-selected conversation model.
- `DEV-multi-conversation-state` is the next serialized owner-level Work after recovery; it will establish account-scoped per-conversation resident state/freshness before production send/stream.
- Do not create a separate repository per screen or use retained UIKit hierarchy/navigation stack as conversation-state authority.

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
- Intended environment ceiling iOS17; current build minimum iOS14.0.
- Current runtime evidence covers iPhone/iOS17 only unless explicitly stated otherwise.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/artifact/runtime/architecture/status changes update the current checkpoint and durable docs in the same work cycle.

## Critical invariants / prohibited routes

- Historical WebView chat code is not the native product baseline; WebView remains authentication/bootstrap only.
- `ConversationRepository` is the production conversation read/recovery owner; UI titles/text are never identity.
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