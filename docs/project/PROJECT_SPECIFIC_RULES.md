# Project-Specific Rules

This file contains rules specific to this repository/product. Populate/change these rules only from explicit user requirements, verified runtime constraints, current source, accepted test results or durable technical decisions.

## Product contracts

- The current product goal is an **iOS native ChatGPT client**.
- The previous-project history pack is reference material only; it is not current source or current protocol documentation.
- The durable ordered implementation roadmap lives in `docs/project/DEVELOPMENT_PLAN.md`.
- `DEV-app-foundation-0.1.0-b1` is the accepted Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b2` proves the tested embedded ChatGPT Continue with Google route and WebKit login persistence across force-close/relaunch on iPhone / iOS 17.0.
- `DEV-auth-bootstrap-0.1.0-b3` proves the tested transient native session bridge can consume the current authenticated WebKit context for `https://chatgpt.com/auth/login` on the intended iPhone / iOS 17.0 environment.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority for AI-assisted work.
- Every new work session reads root `AGENTS.md`, then `docs/project/START_HERE.md` before substantive work.
- Material source/CI/artifact/runtime/architecture/status changes require same-cycle checkpoint and durable-doc updates.

## Protocol evidence contract

- Do not implement ChatGPT private/internal Web API behavior from historical endpoint names, old shapes or memory alone.
- Before implementing a protocol capability, establish current evidence for URL/path, method, authentication/account context, headers, body, response/stream shape, IDs/state semantics and failure behavior as applicable.
- Current evidence wins over historical notes.
- `DEV-protocol-read` must not begin until the current account/workspace context actually required by the native request path is evidenced and assigned one explicit owner.
- b3 native-session success on `/auth/login` is authentication transport evidence only; it is not proof of current conversation-list/detail endpoints or their required headers/context.

## Authentication contract

- Current tested login entry is embedded `WKWebView` at `https://chatgpt.com/auth/login`.
- Continue with Google succeeds on the tested iPhone / iOS 17.0 environment.
- Default persistent `WKWebsiteDataStore` retains authenticated state across force-close/relaunch and remains the current **persistent authentication-secret authority**.
- Do **not** add a system-browser/auth-session fallback while the tested embedded route works; a fallback requires a concrete current failure.
- Do **not** create a second persistent Cookie/token/session authority.
- Current b3 runtime evidence accepts this narrow native consumption mechanism: read current WebKit cookies, filter ChatGPT/OpenAI domains, copy matching cookies transiently into an **ephemeral `URLSession`**, then perform the evidenced native request. The copy must not be persisted by `AuthSessionStore`.
- `AuthSessionStore` owns safe web/native auth evidence state and the tested transient bridge; it does not own persistent credentials.
- b3 real-device acceptance requires exact candidate identity and is satisfied on the tested device: screenshot `网页登录成功 · 原生会话通过`; diagnostics `session.nativeState=verified`; final `chatgpt.com` HTTP 200.
- Account/workspace context remains a separate evidence target and must receive one explicit owner before protocol-read implementation depends on it.
- Never log or export passwords, OAuth authorization codes, access/refresh/session tokens, Cookie values, full Cookie/Authorization headers or equivalent authentication secrets.

## Diagnostics / logging contract

- Structured diagnostics/logging is required from the first executable product build and uses the accepted `DiagnosticsLogger`/store/export authority.
- Important lifecycle/auth/session/network/protocol/conversation/stream/render/upload/persistence operations must emit correlated safe metadata sufficient to reconstruct the operation path.
- Maintain bounded persistent local history; the accepted foundation uses a 2 MiB current JSONL file plus up to three rotated archives.
- User-triggered diagnostic export must remain redacted/privacy-safe.
- Prefer method/path category, HTTP status, elapsed time, byte/item counts, MIME/type and terminal reason over payload contents.
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
- b3 runtime evidence must be tied to the authoritative push artifact from product source `0fcf040012c0698d0e3ce1628fec9865237eba3b`, not a temporary PR-merge artifact.
- Native `/auth/login` success must not be generalized into private conversation-protocol success.

## Frozen business or architecture rules

None recorded yet. Foundation modules, embedded web login/persistence and the tested transient native auth bridge are Stable for their accepted scope, not Frozen. Account/workspace context remains Unknown / Unverified.

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

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for advisory previous-project lessons.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses remain in the active checkpoint, not here.
