# Project-Specific Rules

This file contains repository/product rules backed by explicit requirements, current source, accepted tests or durable technical decisions.

## Product contracts

- Product goal: **iOS native ChatGPT client**.
- Previous-project history is reference-only, not current protocol authority.
- Durable roadmap: `docs/project/DEVELOPMENT_PLAN.md`.
- Accepted foundation baseline: `DEV-app-foundation-0.1.0-b1`.
- Accepted auth/account baseline: `DEV-auth-bootstrap-0.1.0-b6`, merged through PR #6.
- Accepted current conversation-read baseline: `DEV-protocol-read-0.1.0-b7` for the tested Plus/personal list + one-detail path on iPhone / iOS 17.0, merged through PR #7 at `6208102eb3df79a1916b356cc95ff7916ff8f593`.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every new work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/artifact/runtime/architecture/status changes require same-cycle checkpoint and durable-doc updates.

## Protocol evidence contract

- Do not implement private/internal Web API behavior from historical names, shapes or memory alone.
- Establish current evidence for path/method/auth/account context/headers/body/response/stream/state/failure behavior as applicable before making a protocol capability authoritative.
- Current real-device evidence outranks history and CI-only evidence.
- **Accepted b7 personal-account read path**: transient native transport with copied ephemeral WebKit cookies + transient bearer; `GET /backend-api/conversations?offset=0&limit=28&order=updated`; then `GET /backend-api/conversation/{conversation_id}` for a returned ID.
- In the accepted b7 Plus/personal run, no `chatgpt-account-id` or extra browser-only header set was required. This is a tested-scope fact, not a universal rule for other workspace structures.
- Accepted b7 list result: HTTP 200, 28 items / total 29, response limit 28, offset 0.
- Accepted b7 first-detail result: HTTP 200, 13,152,411 bytes, mapping 2068 / message nodes 2067; current node present+mapped; returned conversation identity present+matching. Role counts summed exactly to all message nodes.
- b7 read success does **not** establish send/streaming/attachments, non-personal workspace behavior, iPad or lower-iOS runtime.
- `ProtocolReadProbe` remains diagnostic-only. Production repository/selected-conversation/message-tree identity must have explicit owners in `DEV-native-read-path`.
- Protocol diagnostics must not log/export full titles, message bodies/parts, payload dumps, raw conversation/message IDs or auth secrets. Prefer structural counts/status/pagination/timing and hashed IDs when needed.

## Authentication contract

- Tested login entry remains embedded `WKWebView` at `https://chatgpt.com/auth/login`.
- Continue with Google succeeds in the tested iPhone / iOS 17.0 environment.
- Default persistent `WKWebsiteDataStore` is the sole persistent authentication-secret authority.
- Do not create a second persistent Cookie/token/session authority.
- `AuthSessionStore` may copy matching WebKit cookies transiently into an **ephemeral `URLSession`** for evidence-backed requests; copied values must not be persisted.
- Native `/auth/login` is not an account-context prerequisite.
- Account sequencing: authenticated WebKit -> ephemeral current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- Preserve challenge sensitivity: b5, b6 and b7 each showed a direct `/api/auth/session` HTTP 403 in at least one attempt followed by a later user-triggered successful verification. Current code intentionally has no speculative automatic retry.
- b7 specifically: first account attempt used 46 total / 27 matched cookies and session HTTP 403; after explicit user `重新开始`, second attempt used 49 / 30 cookies, session/accounts HTTP 200, plus/personal verified.
- Accepted account parser uses non-empty `account_ordering`, keyed `accounts`, first ordered accessible entry, and nested `account.account_id`.
- If future session/account requests fail, record exact stage/status/reason first. Do not immediately add retries, UA spoofing, Cloudflare bypass, alternate endpoints, browser-script token extraction or speculative parser fallbacks.
- Never log/export passwords, OAuth codes, access/refresh/session tokens, Cookie values, full Cookie/Authorization headers or equivalent secrets.

## Diagnostics / logging contract

- Use the accepted `DiagnosticsLogger`/store/export authority for lifecycle/auth/network/protocol/conversation/stream/render/upload/persistence evidence.
- Maintain bounded local history and redacted user-triggered export.
- Repeated testing uses the existing **clear local diagnostics** control; clearing must not affect WebKit/authentication state.
- Prefer method/path category, HTTP status, elapsed time, byte/item counts, pagination, MIME/type and terminal reason over payload contents.
- Safe cookie diagnostics may record total/matched counts only, not Cookie names/values.
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
- CI/artifact success is not runtime proof.
- Auth route results remain tied to their tested route/time conditions.
- b7 first account HTTP 403 must not erase the accepted explicit-restart success; b7 success must not erase challenge sensitivity.
- b7 list/detail success must not be generalized to send/streaming/attachments or non-personal workspaces.
- The observed 13.57 s protocol-probe total is end-to-end only. Do not label network, parsing or rendering as the bottleneck without phase-specific timing evidence.
- The observed 13.15 MB / 2068-node detail is a current real-world input. `DEV-native-read-path` must not assume tiny conversations or naive all-view materialization.

## Frozen business or architecture rules

None recorded yet. Foundation, auth/account context, diagnostics and tested protocol-read diagnostic scope are Stable for their accepted scope, not Frozen. Production native conversation state and send/streaming remain Unverified.

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

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for advisory previous-project lessons.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses stay in an active task checkpoint.
