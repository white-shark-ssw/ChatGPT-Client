# Project-Specific Rules

This file contains rules specific to this repository/product. Populate/change these rules only from explicit user requirements, verified runtime constraints, current source, accepted test results or durable technical decisions.

## Product contracts

- The current product goal is an **iOS native ChatGPT client**.
- The previous-project history pack is reference material only; it is not current source or current protocol documentation.
- The durable ordered implementation roadmap lives in `docs/project/DEVELOPMENT_PLAN.md`.
- `DEV-app-foundation-0.1.0-b1` is the accepted Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6` is the accepted current authentication/account-context runtime candidate for iPhone / iOS 17.0, pending PR #6 integration.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority for AI-assisted work.
- Every new work session reads root `AGENTS.md`, then `docs/project/START_HERE.md` before substantive work.
- Material source/CI/artifact/runtime/architecture/status changes require same-cycle checkpoint and durable-doc updates.

## Protocol evidence contract

- Do not implement ChatGPT private/internal Web API behavior from historical endpoint names, old shapes or memory alone.
- Before implementing a protocol capability, establish current evidence for URL/path, method, authentication/account context, headers, body, response/stream shape, IDs/state semantics and failure behavior as applicable.
- Current evidence wins over historical notes.
- The auth/account-context entry gate for future `DEV-protocol-read` is satisfied by accepted b6 evidence, but conversation-list/detail/streaming protocol remains Unknown / Unverified until separately tested.
- Native `/auth/login` success/failure is authentication-route evidence only; it is not proof of conversation-list/detail endpoints or their required context.

## Authentication contract

- Current tested login entry is embedded `WKWebView` at `https://chatgpt.com/auth/login`.
- Continue with Google succeeds on the tested iPhone / iOS 17.0 environment.
- Default persistent `WKWebsiteDataStore` retains authenticated state and remains the current **persistent authentication-secret authority**.
- Do **not** add a system-browser/auth-session fallback while the tested embedded route works; a fallback requires a concrete current failure.
- Do **not** create a second persistent Cookie/token/session authority.
- `AuthSessionStore` may read current WebKit cookies and copy matching ChatGPT/OpenAI cookies transiently into an **ephemeral `URLSession`** for a specifically evidenced request. The copy must not be persisted.
- Native `/auth/login` is **not** a current account-context prerequisite or authentication state authority.
- Current account-context sequencing begins after WebKit reaches authenticated ChatGPT: ephemeral current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- Preserve challenge sensitivity as an observed fact: b5 and b6 both had a direct `/api/auth/session` HTTP 403 in one attempt, followed by a later user-triggered verification attempt that returned HTTP 200. Current app code intentionally does not add a speculative automatic retry for this.
- The accepted accounts-check parser uses non-empty `account_ordering`, keyed `accounts`, the first ordered entry not explicitly inaccessible with session, and nested `account.account_id`. Optional `plan_type` / `structure` are metadata only.
- b6 real-device evidence: second user-triggered attempt returned `/api/auth/session` HTTP 200 + accounts-check HTTP 200, observed accountCount=2/orderCount=1, selected plus/personal account context, set `session.accountState=verified`, and ended `status=ok`. This is the accepted current account-context contract for the tested environment.
- If a direct session/account request fails in later work, record the exact stage/status/reason first. Do not immediately add retries, User-Agent spoofing, Cloudflare bypass logic, alternate endpoints, browser-script token extraction or speculative multi-shape parser fallbacks.
- Never log or export passwords, OAuth authorization codes, access/refresh/session tokens, Cookie values, full Cookie/Authorization headers or equivalent authentication secrets.

## Diagnostics / logging contract

- Structured diagnostics/logging is required from the first executable product build and uses the accepted `DiagnosticsLogger`/store/export authority.
- Important lifecycle/auth/session/network/protocol/conversation/stream/render/upload/persistence operations must emit correlated safe metadata sufficient to reconstruct the operation path.
- Maintain bounded persistent local history; the accepted foundation uses a 2 MiB current JSONL file plus up to three rotated archives.
- User-triggered diagnostic export must remain redacted/privacy-safe.
- Prefer method/path category, HTTP status, elapsed time, byte/item counts, MIME/type and terminal reason over payload contents.
- Safe cookie diagnostics may record only total/matched counts, never Cookie names/values when names themselves could reveal security mechanisms unnecessarily.
- Repeated device testing provides an explicit **clear local diagnostics** control through the existing diagnostics authority. Clearing removes the store's current JSONL and configured rotated archives; it must not create another store or clear WebKit/authentication state.
- Do not create a competing diagnostics persistence/export/clear authority without evidence that the current owner is insufficient.

## Compatibility / deployment constraints

- Platform: iOS native app; distribution: TrollStore IPA.
- Intended user-device OS does not exceed iOS 17.0. This is a ceiling, not a minimum.
- Current accepted minimum deployment target remains iOS 14.0; do not raise it without a concrete required API/dependency/runtime reason.
- Runtime evidence currently covers iPhone / iOS 17.0; do not infer iOS 14.x–16.x or iPad runtime compatibility from build settings alone.

## Critical invariants

- Historical WebView chat code does not become the new source baseline merely because it existed.
- Current WebView use is limited to the evidence-backed login/bootstrap role; native chat architecture remains the product direction.
- Future session/account/conversation/message-stream/upload identities must have explicit state owners; UI text/titles are consumers, not authorities.
- CI/artifact success must never be described as runtime proof.
- b3/b4/b5/b6 route behavior remains tied to exact runtime evidence; do not generalize auth results into private conversation protocol behavior.
- b4 must not be labeled an account-context endpoint failure because its account probe never ran.
- b5 second-run accounts HTTP 200 must not be labeled an auth failure; its terminal failure was the old response parser.
- b6 first HTTP 403 must not erase the accepted second-attempt success, and b6 success must not erase the observed challenge sensitivity.

## Frozen business or architecture rules

None recorded yet. Foundation modules, embedded web login/persistence, diagnostics, and current account-context ownership are Stable for their accepted scope, not Frozen. Conversation/private protocol remains Unverified.

## Code style / naming constraints

Follow existing repository style until explicit project-specific constraints are verified.

## Prohibited routes / known dangerous regressions

- Do not add speculative timers, watchdogs, DOM scans, shadow WebViews, retry loops or authentication fallback chains without a concrete current failure mode.
- Do not add a system-browser authentication fallback while the tested embedded route works.
- Do not persist copied Cookie values outside WebKit.
- Do not use UI text/title matching as a production identity authority.
- Do not raise the iOS 14.0 minimum merely because CI uses a newer SDK.
- Do not add silent auth/network/protocol recovery that hides original failure evidence.
- Do not guess conversation endpoints from historical notes; establish current evidence first.
- Do not treat native `/auth/login` as a mandatory gate for actual account/session requests.
- Do not restore `accounts.default.account.id` as current authority without new current evidence.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for advisory previous-project lessons.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses remain in the active checkpoint, not here.
