# Project-Specific Rules

This file contains rules specific to this repository/product. Populate/change these rules only from explicit user requirements, verified runtime constraints, current source, accepted test results or durable technical decisions.

## Product contracts

- The current product goal is an **iOS native ChatGPT client**.
- The previous-project history pack is reference material only; it is not current source or current protocol documentation.
- The durable ordered implementation roadmap lives in `docs/project/DEVELOPMENT_PLAN.md`.
- `DEV-app-foundation-0.1.0-b1` is the accepted Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b2` proves the tested embedded ChatGPT Continue with Google route and WebKit login persistence across force-close/relaunch on iPhone / iOS 17.0.
- `DEV-auth-bootstrap-0.1.0-b3` is the current native-session-consumption test candidate. CI/artifact success does not prove its runtime result.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority for AI-assisted work.
- Every new work session reads root `AGENTS.md`, then `docs/project/START_HERE.md` before substantive work.
- Material source/CI/artifact/runtime/architecture/status changes require same-cycle checkpoint and durable-doc updates.

## Protocol evidence contract

- Do not implement ChatGPT private/internal Web API behavior from historical endpoint names, old shapes or memory alone.
- Before implementing a protocol capability, establish current evidence for URL/path, method, authentication/account context, headers, body, response/stream shape, IDs/state semantics and failure behavior as applicable.
- Current evidence wins over historical notes.
- Production private-protocol work must not begin until authenticated session/account context actually usable by the native request path is evidenced.

## Authentication contract

- Current tested login entry is the embedded `WKWebView` route at `https://chatgpt.com/auth/login`.
- Continue with Google succeeds on the tested b2 iPhone / iOS 17.0 candidate.
- The default persistent `WKWebsiteDataStore` retained authenticated state across force-close/relaunch on b2 and is the current **persistent authentication-secret authority**.
- Do **not** add a system-browser/auth-session fallback while the tested embedded route works; a fallback requires a concrete current failure.
- Do **not** create a second persistent Cookie/token/session authority. If native transport must consume WebKit state, copy only what current evidence requires and keep the copy transient/in-memory unless a later verified requirement justifies a different secure owner.
- Current b3 evidence probe may transiently copy ChatGPT/OpenAI WebKit cookies into an **ephemeral `URLSession`** to test server acceptance. This is a diagnostic/session-consumption probe, not proof of production native authentication until real-device tested.
- `AuthSessionStore` owns safe web/native auth evidence state, not persistent credentials.
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
- Successful WebKit login/persistence must not be described as proof that native `URLSession` or private-protocol calls are authenticated.
- b3 runtime evidence must be tied to the **push artifact** built from product source `0fcf040012c0698d0e3ce1628fec9865237eba3b`, not the separate temporary PR-merge artifact.

## Frozen business or architecture rules

None recorded yet. Foundation modules are Stable, not Frozen. Embedded web login/persistence is accepted Stable on the tested environment, not Frozen. Native session bridge remains Candidate.

## Code style / naming constraints

Follow existing repository style until explicit project-specific constraints are verified.

## Prohibited routes / known dangerous regressions

- Do not add speculative timers, watchdogs, DOM scans, shadow WebViews, retry loops or authentication fallback chains without a concrete current failure mode.
- Do not add a system-browser authentication fallback while the tested embedded route works.
- Do not persist b3's copied Cookie values outside WebKit.
- Do not use UI text/title matching as a production identity authority.
- Do not raise the iOS 14.0 minimum merely because CI uses a newer SDK.
- Do not add silent auth/network/protocol recovery that hides original failure evidence.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for advisory previous-project lessons.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses remain in the active checkpoint, not here.
