# Project-Specific Rules

This file contains rules specific to this repository/product. Populate/change these rules only from explicit user requirements, verified runtime constraints, current source, accepted test results or durable technical decisions.

## Product contracts

- The current product goal is an **iOS native ChatGPT client**.
- The previous-project history pack is reference material only; it is not current source or current protocol documentation.
- The durable ordered implementation roadmap lives in `docs/project/DEVELOPMENT_PLAN.md`.
- `DEV-app-foundation-0.1.0-b1` is the accepted Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b2` proves the tested embedded ChatGPT Continue with Google route and WebKit login persistence across force-close/relaunch on iPhone / iOS 17.0.
- `DEV-auth-bootstrap-0.1.0-b3` proves that native `/auth/login` succeeded under its tested conditions; `DEV-auth-bootstrap-0.1.0-b4` proves the same route can later be Cloudflare-blocked while WebKit itself is authenticated. Treat these as route-specific evidence, not a durable prerequisite contract.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority for AI-assisted work.
- Every new work session reads root `AGENTS.md`, then `docs/project/START_HERE.md` before substantive work.
- Material source/CI/artifact/runtime/architecture/status changes require same-cycle checkpoint and durable-doc updates.

## Protocol evidence contract

- Do not implement ChatGPT private/internal Web API behavior from historical endpoint names, old shapes or memory alone.
- Before implementing a protocol capability, establish current evidence for URL/path, method, authentication/account context, headers, body, response/stream shape, IDs/state semantics and failure behavior as applicable.
- Current evidence wins over historical notes.
- `DEV-protocol-read` must not begin until the current account/workspace context actually required by the native request path is evidenced and assigned one explicit owner.
- Native `/auth/login` success/failure is authentication-route evidence only; it is not proof of current conversation-list/detail endpoints or their required context.

## Authentication contract

- Current tested login entry is embedded `WKWebView` at `https://chatgpt.com/auth/login`.
- Continue with Google succeeds on the tested iPhone / iOS 17.0 environment.
- Default persistent `WKWebsiteDataStore` retains authenticated state and remains the current **persistent authentication-secret authority**.
- Do **not** add a system-browser/auth-session fallback while the tested embedded route works; a fallback requires a concrete current failure.
- Do **not** create a second persistent Cookie/token/session authority.
- `AuthSessionStore` may read current WebKit cookies and copy matching ChatGPT/OpenAI cookies transiently into an **ephemeral `URLSession`** for a specifically evidenced diagnostic/request. The copy must not be persisted.
- b3 native `/auth/login` HTTP 200 remains valid for that tested time. b4 later showed WebKit `/auth/login` HTTP 403 -> Cloudflare challenge -> authenticated `chatgpt.com` HTTP 200, while a separate native `/auth/login` request returned HTTP 403. Therefore native `/auth/login` is **not** a current account-context prerequisite or authentication state authority.
- Current b5 account-context sequencing starts the actual account/session diagnostic directly after WebKit reaches authenticated non-`/auth` `chatgpt.com`: ephemeral current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check. This path remains Candidate until real-device b5 evidence passes.
- If direct `/api/auth/session` fails, record the exact stage/status first. Do not immediately add retries, User-Agent spoofing, Cloudflare bypass logic, alternate endpoints or browser-script token extraction without new concrete evidence.
- Never log or export passwords, OAuth authorization codes, access/refresh/session tokens, Cookie values, full Cookie/Authorization headers or equivalent authentication secrets.

## Diagnostics / logging contract

- Structured diagnostics/logging is required from the first executable product build and uses the accepted `DiagnosticsLogger`/store/export authority.
- Important lifecycle/auth/session/network/protocol/conversation/stream/render/upload/persistence operations must emit correlated safe metadata sufficient to reconstruct the operation path.
- Maintain bounded persistent local history; the accepted foundation uses a 2 MiB current JSONL file plus up to three rotated archives.
- User-triggered diagnostic export must remain redacted/privacy-safe.
- Prefer method/path category, HTTP status, elapsed time, byte/item counts, MIME/type and terminal reason over payload contents.
- Safe cookie diagnostics may record only total/matched counts, never Cookie names/values when names themselves could reveal security mechanisms unnecessarily.
- Do not create a competing diagnostics persistence/export authority without evidence that the current owner is insufficient.

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
- b3 and b4 route behavior must remain tied to their exact runtime candidates; neither result may be generalized into private protocol behavior.
- b4 must not be labeled an account-context endpoint failure because `accountContextProbe` never ran.

## Frozen business or architecture rules

None recorded yet. Foundation modules and embedded web login/persistence are Stable for their accepted scope, not Frozen. Native `/auth/login` behavior is route-specific evidence. Account/workspace context remains Candidate / Unverified.

## Code style / naming constraints

Follow existing repository style until explicit project-specific constraints are verified.

## Prohibited routes / known dangerous regressions

- Do not add speculative timers, watchdogs, DOM scans, shadow WebViews, retry loops or authentication fallback chains without a concrete current failure mode.
- Do not add a system-browser authentication fallback while the tested embedded route works.
- Do not persist copied Cookie values outside WebKit.
- Do not use UI text/title matching as a production identity authority.
- Do not raise the iOS 14.0 minimum merely because CI uses a newer SDK.
- Do not add silent auth/network/protocol recovery that hides original failure evidence.
- Do not guess account/workspace or conversation endpoints from historical notes; establish current evidence first.
- Do not treat native `/auth/login` as a mandatory gate for the actual account/session request.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for advisory previous-project lessons.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses remain in the active checkpoint, not here.
