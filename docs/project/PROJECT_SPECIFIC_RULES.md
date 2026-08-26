# Project-Specific Rules

This file contains repository/product rules backed by explicit requirements, current source, accepted tests or durable technical decisions.

## Product contracts

- Product goal: **iOS native ChatGPT client**.
- Previous-project history is reference-only, not current protocol authority.
- Durable roadmap: `docs/project/DEVELOPMENT_PLAN.md`.
- Durable UI/interaction baseline: `docs/project/UI_INTERACTION_BASELINE.md`.
- Product delivery priority: **reach a genuinely usable TrollStore client as early as possible, then iterate in real-device candidates instead of waiting for the whole roadmap to finish**.
- Accepted foundation baseline: `DEV-app-foundation-0.1.0-b1`.
- Accepted auth/account baseline: `DEV-auth-bootstrap-0.1.0-b6`, merged through PR #6.
- Accepted diagnostic conversation-read baseline: `DEV-protocol-read-0.1.0-b7` for the tested Plus/personal list + one-detail path on iPhone / iOS 17.0, merged through PR #7 at `6208102eb3df79a1916b356cc95ff7916ff8f593`.
- Accepted production native-read baseline: `DEV-native-read-path-0.1.0-b9` for the tested Plus/personal native shell/list/two-detail/current-visible-branch scope on iPhone / iOS 17.0, merged through PR #9 at `467ea885d120fa59809c95c914b1ac670d76ee05`. Stable for tested scope, not Frozen.

## UI / interaction contract

- The **official ChatGPT iOS interaction model is the default baseline** where the user considers it acceptable. Do not invent a separate UI language merely to be different.
- This is an interaction/behavior baseline, not a pixel-perfect copying requirement. Prefer native UIKit/system behavior compatible with the current deployment target.
- The user's recordings are visual reference for sidebar/navigation, conversation layout, composer, send/stop state, assistant message layout/actions, menus/sheets, project-style navigation patterns, and reasoning presentation.
- `导出 Markdown` visible in the user's recording is **not an official-App feature**; it came from the user's injected dylib. Treat Markdown export as our enhancement, not official interaction evidence.
- Preserve the official-style reasoning interaction when current protocol supplies user-visible reasoning status/detail: subdued gray active state with shimmer/flowing-light treatment; tappable expand/collapse detail; completed static summary such as `思考了 Xs` when duration is available; final answer below.
- Only display reasoning summary/detail/tool-status explicitly returned for user display. Never manufacture, infer or expose hidden chain-of-thought.
- The user explicitly requires the official-style **two short haptic pulses** at the real-time reasoning -> final-answer transition. Exact intensity/spacing must be real-device tuned; trigger from response lifecycle state, not cell redraw, and do not replay merely because completed content is reloaded.
- Keep ordinary conversation actions inside official-style overflow/context menus rather than crowding the main navigation bar.
- UI text/title remains a consumer, never an identity authority.

## Fast usable candidate contract

- Do not hold usable functionality until all roadmap phases are complete.
- As soon as a coherent minimal user loop reaches its real artifact/test gate, produce a uniquely identified TrollStore candidate and let real-device evidence guide subsequent work.
- First planned usability milestones are:
  - **V0.1 read-use**: official-style native shell + conversation list/detail/message rendering + manual sync/reload.
  - **V0.2 chat-use**: V0.1 + text send/new conversation + streaming + stop + user-visible reasoning interaction + reasoning-to-final haptics + manual recovery integration.
  - **V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments and daily-use conversation features.
- Candidate labels must still obey `BUILD_TEST_INDEX.md` uniqueness and evidence separation; speed does not justify mixing identities or calling CI/artifact success runtime proof.

## Manual recovery contract

### `同步最新消息`

- This is an explicit user-triggered recovery tool for when server state may be ahead of local stream/thinking state, including the observed class where the server has completed and a completion notification may have arrived while the client still shows thinking/streaming.
- Use the current authoritative conversation identity to fetch current server detail and reconcile through the production conversation owner.
- It must not resend the user's prompt, regenerate, create a new conversation or enter an automatic retry loop.
- If server detail shows completion, stale local thinking/streaming UI should be replaced by the current server-backed completed state.

### `重载当前会话`

- This is a user-triggered recovery tool for current-conversation load failure, timeout, blank/spinning state or otherwise unusable local conversation state.
- Re-request current conversation detail and rebuild that conversation through the authoritative conversation owner.
- Provide a direct `重新加载` action in terminal load-error UI; a manual conversation-menu entry may also exist for loaded-but-broken/stale state.
- Preserve unsent composer draft when practical; never resend existing messages.
- Do not turn reload into an automatic retry/watchdog chain.

### Recovery diagnostics

- Log safe start/end/status/timing/count/diff/state-transition evidence sufficient to distinguish server-state, local merge/store and UI-render failures.
- Never log message bodies, raw payloads or auth secrets.

## Markdown export contract

- `导出 Markdown` is a project enhancement historically useful to the user through an injected dylib, not an official ChatGPT iOS feature.
- Export from the authoritative conversation model/current user-visible branch, never from mounted UI cells.
- Preserve useful Markdown structure/code blocks and supported visible attachment references.
- Do not export hidden/internal reasoning/tool content that is not user-visible.
- Place the action naturally in the official-style conversation menu and use normal iOS share/file presentation.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every new work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/artifact/runtime/architecture/status changes require same-cycle checkpoint and durable-doc updates.

## Protocol evidence contract

- Do not implement private/internal Web API behavior from historical names, shapes or memory alone.
- Establish current evidence for path/method/auth/account context/headers/body/response/stream/state/failure behavior as applicable before making a protocol capability authoritative.
- Current real-device evidence outranks history and CI-only evidence.
- **Accepted b7 personal-account diagnostic read path**: transient native transport with copied ephemeral WebKit cookies + transient bearer; `GET /backend-api/conversations?offset=0&limit=28&order=updated`; then `GET /backend-api/conversation/{conversation_id}` for a returned ID.
- In the accepted b7 Plus/personal run, no `chatgpt-account-id` or extra browser-only header set was required. This is a tested-scope fact, not a universal rule for other workspace structures.
- Accepted b7 list result: HTTP 200, 28 items / total 29, response limit 28, offset 0.
- Accepted b7 first-detail result: HTTP 200, 13,152,411 bytes, mapping 2068 / message nodes 2067; current node present+mapped; returned conversation identity present+matching. Role counts summed exactly to all message nodes.
- **Accepted b9 production native-read path**: `ConversationRepository` is the production owner for summaries, selected identity, loaded detail and current visible branch. It reuses the same transient auth owner/path and list/detail routes rather than `ProtocolReadProbe` state.
- Accepted b9 runtime result on iPhone/iOS 17.0 after explicit login verification: production list HTTP 200, 28/29. Two distinct selected conversations both completed detail/current-branch/render: position 1 = 1,529,866 bytes / mapping 337 / visible messages 154 / 5,668.41 ms; position 13 = 7,503,328 bytes / mapping 2023 / visible messages 843 / 20,742.89 ms. The user confirmed both were fully readable.
- b9's privacy-safe `conversationHash` + 1-based `listPosition` is an accepted correlation mechanism for production conversation diagnostics. Never log raw conversation IDs, full titles, message bodies/parts or payload dumps.
- b7/b9 read success does **not** establish send/streaming/attachments, non-personal workspace behavior, iPad or lower-iOS runtime.
- Terminal detail `重新加载` exists in b9 but was not exercised because both b9 details succeeded; its failure-path runtime behavior remains Unverified and must not be described as real-device proven.
- `ProtocolReadProbe` remains diagnostic-only. Do not turn it into the production repository by convenience.

## Authentication contract

- Tested login entry remains embedded `WKWebView` at `https://chatgpt.com/auth/login`.
- Continue with Google succeeds in the tested iPhone / iOS 17.0 environment.
- Default persistent `WKWebsiteDataStore` is the sole persistent authentication-secret authority.
- Do not create a second persistent Cookie/token/session authority.
- `AuthSessionStore` may copy matching WebKit cookies transiently into an **ephemeral `URLSession`** for evidence-backed requests; copied values must not be persisted.
- Native `/auth/login` is not an account-context prerequisite.
- Account sequencing: authenticated WebKit -> ephemeral current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- Preserve challenge sensitivity: b5, b6 and b7 each showed a direct `/api/auth/session` HTTP 403 in at least one attempt followed by a later user-triggered successful verification. Current code intentionally has no speculative automatic retry.
- b9 additionally showed a fresh app launch with 0 total / 0 matched WebKit cookies and missing required session fields; after explicit login verification, 48/29 then 49/30 total/matched cookies and Plus/personal account context succeeded. Therefore install/update authentication persistence remains Unknown / Unverified; do not silently add recovery until its state owner/failure mode is proven.
- Accepted account parser uses non-empty `account_ordering`, keyed `accounts`, first ordered accessible entry, and nested `account.account_id`.
- If future session/account requests fail, record exact stage/status/reason first. Do not immediately add retries, UA spoofing, Cloudflare bypass, alternate endpoints, browser-script token extraction or speculative parser fallbacks.
- Never log/export passwords, OAuth codes, access/refresh/session tokens, Cookie values, full Cookie/Authorization headers or equivalent secrets.

## Diagnostics / logging contract

- Use the accepted `DiagnosticsLogger`/store/export authority for lifecycle/auth/network/protocol/conversation/stream/render/upload/persistence evidence.
- Maintain bounded local history and redacted user-triggered export.
- Repeated testing uses the existing **clear local diagnostics** control; clearing must not affect WebKit/authentication state.
- Prefer method/path category, HTTP status, elapsed time, byte/item counts, pagination, MIME/type and terminal reason over payload contents.
- Safe cookie diagnostics may record total/matched counts only, not Cookie names/values.
- Production conversation diagnostics may use the accepted short irreversible `conversationHash` plus 1-based `listPosition`; raw conversation IDs remain prohibited.
- Do not create competing diagnostics persistence/export/clear authority without concrete evidence.

## Compatibility / deployment constraints

- Native iOS; TrollStore IPA.
- Intended device OS does not exceed iOS 17.0; this is a ceiling, not a minimum.
- Current build deployment target remains iOS 14.0; do not raise without concrete API/dependency/runtime need.
- Runtime evidence currently covers iPhone / iOS 17.0 only; do not infer iOS 14–16 or iPad runtime compatibility.

## Critical invariants

- Historical WebView chat code is not the native product baseline.
- WebView use remains limited to the evidence-backed authentication/bootstrap role; native chat remains the product direction.
- UI text/titles are consumers, not identity authorities.
- `ConversationRepository` is the accepted production conversation read owner for the b9 tested scope; `ProtocolReadProbe` stays diagnostic-only.
- CI/artifact success is not runtime proof.
- Auth route results remain tied to their tested route/time conditions.
- b7 first account HTTP 403 must not erase the accepted explicit-restart success; b7 success must not erase challenge sensitivity.
- b9 two-detail success means the earlier b8 one-off HTTP 500 is not proof of a systematic current native-read implementation failure; its exact cause remains unproven.
- b7/b9 list/detail success must not be generalized to send/streaming/attachments or non-personal workspaces.
- The observed 13.57 s b7 diagnostic total and 20.74 s b9 7.50 MB production detail are end-to-end only. Do not label network, parsing or rendering as the bottleneck without phase-specific timing evidence.
- The observed 13.15 MB / 2068-node b7 detail and 7.50 MB / 2023-node b9 production detail are real-world inputs. Do not assume tiny conversations or naive all-view materialization.
- Manual sync/reload must operate through the production conversation state owner rather than creating competing stores or identities.
- Response transition haptics must be tied to lifecycle state transitions rather than rendering callbacks.

## Frozen business or architecture rules

None recorded yet. Foundation, auth/account context, diagnostics, tested protocol-read diagnostic scope, and b9 production native-read scope are Stable for their accepted scope, not Frozen. Send/streaming remain Unverified.

## Code style / naming constraints

Follow existing repository style until explicit project-specific constraints are verified.

## Prohibited routes / known dangerous regressions

- No speculative timers, watchdogs, DOM scans, shadow WebViews, retry loops or auth fallback chains without concrete current failure evidence.
- No system-browser auth fallback while the accepted embedded route works.
- Do not persist copied Cookie/token values outside the accepted WebKit authority.
- Do not use UI title/text matching as production identity authority.
- Do not raise iOS 14.0 minimum merely because CI uses newer SDK.
- Do not add silent auth/network/protocol recovery that hides original failures.
- Do not reintroduce `accounts.default.account.id` without new evidence.
- Do not preemptively add `chatgpt-account-id`, duplicate browser headers, fallback conversation endpoints or compatibility shims to the accepted personal-account read path.
- Do not turn the diagnostic `ProtocolReadProbe` into the production conversation repository by convenience.
- Do not treat the injected Markdown menu shown in the reference recording as official-App behavior.
- Do not block the first usable client on Projects, Voice, attachments, advanced search or broad future feature completeness.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for advisory previous-project lessons.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses stay in an active task checkpoint.
