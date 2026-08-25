# Project-Specific Rules

This file contains rules specific to this repository/product. Do not copy assumptions from another project into this file.

Populate/change these rules only from explicit user requirements, verified product/runtime constraints, real source architecture, accepted test results, confirmed compatibility/deployment requirements, or durable technical decisions.

## Product contracts

- The current product goal is an **iOS native ChatGPT client**.
- The current executable foundation is Swift 5 + UIKit with no third-party dependencies; framework or dependency changes must be justified by current feature/compatibility needs rather than historical preference.
- The previous-project history pack is reference material only. It is not current product source, current protocol documentation, or proof that a historical implementation should be reused.
- The durable ordered implementation roadmap lives in `docs/project/DEVELOPMENT_PLAN.md`.

## Repository governance contract

- The repository uses the AI Governance Rules as the dynamic authority for AI-assisted work.
- Every new work session must read root `AGENTS.md` first and then `docs/project/START_HERE.md` before substantive work.
- When repository evidence changes materially, the corresponding checkpoint and durable `docs/project/` records must be refreshed in the same work cycle.

## Protocol evidence contract

- Do not implement ChatGPT private/internal Web API behavior from historical endpoint names, old request shapes, or memory alone.
- Before implementing a protocol capability, establish current evidence for the relevant URL/path, method, authentication/account context, headers, request body, response/stream shape, IDs/state semantics, and failure behavior as applicable.
- If current evidence contradicts historical notes, current evidence wins and durable docs must be corrected.
- Do not begin native private-protocol implementation until a current authenticated ChatGPT session/context has been reproduced and evidenced on-device.

## Authentication contract

- The user's previous Web-based IPA successfully used ChatGPT web login, and their account uses Google sign-in. Treat this as historical success evidence only.
- The current app must revalidate the real Google-based login path on-device before adopting an authentication architecture.
- Start with the simplest current web-login bootstrap and capture safe navigation/auth-state evidence.
- If current Google OAuth rejects an embedded `WKWebView`/embedded user-agent, capture the actual current failure/redirect evidence first; then choose the smallest supported system-browser/auth handoff justified by that evidence.
- Do not prebuild speculative multi-route authentication fallback chains.
- Do not assume WebKit cookies, system-browser cookies/session state and native `URLSession` authentication state are interchangeable.
- Never persist or log user passwords, OAuth authorization codes, access/refresh/session tokens, Cookie values or equivalent authentication secrets outside the real secure/session mechanism required by the implemented path.

## Diagnostics / logging contract

- Structured diagnostics/logging is required from the **first executable product build**; it is not a later debugging enhancement.
- Important app lifecycle, authentication, session/account, network, protocol, conversation selection/state, streaming, rendering/performance, attachment and persistence operations must emit correlated diagnostic events sufficient to reconstruct the operation path.
- Include timing/count/size/status/error metadata where useful, while keeping the event schema stable enough to compare different test candidates.
- Maintain a bounded persistent local diagnostic history suitable for TrollStore-installed real-device debugging away from Xcode. Logs must not grow without limit.
- Provide a user-triggered redacted diagnostic export path once the first executable app foundation is built.
- By default, do **not** log passwords, OAuth codes, tokens, Cookie values, full `Authorization`/`Cookie` headers, complete chat-message text, full user-content request/response bodies, or attachment contents.
- Prefer safe metadata such as method/path category, HTTP status, elapsed time, byte count, MIME/type, node/item count and terminal reason.
- Identifiers required to diagnose state ownership may be kept inside the app's private local diagnostics when justified, but exported diagnostics must redact/hash sensitive identifiers and must never export auth secrets.
- Remote analytics/telemetry or automatic log upload is **not** implied by the logging requirement; add it only if explicitly required later.
- The current foundation implementation uses OSLog plus an app-private rolling JSONL store and user-triggered JSON export. This is Candidate behavior, not Stable/Frozen until real-device validation confirms persistence/export behavior.

## Compatibility / deployment constraints

- Platform direction: iOS native application.
- Distribution/install form: IPA installed through TrollStore.
- Intended user-device OS versions do not exceed iOS 17.0. Do not introduce a required API, dependency, framework setting, or deployment configuration that makes iOS > 17.0 mandatory unless the user explicitly changes this requirement.
- The current verified foundation deployment target is **iOS 14.0**, present in Xcode build settings and in the generated IPA `MinimumOSVersion`.
- iOS 14.0 is justified by the current dependency-free UIKit/Foundation/CryptoKit foundation and use of the structured `Logger` API introduced with iOS 14; it also aligns with TrollStore's currently documented supported range beginning at iOS 14.
- Any future change that raises the minimum deployment target above iOS 14.0 must be treated as a compatibility-impacting decision and justified by actual required APIs/dependencies/runtime evidence.
- Current build settings target iPhone + iPad device families, but real-device support claims remain limited to devices/OS versions actually tested.

## Critical invariants

- Historical WebView code must not become the new source baseline merely because it existed in the previous project.
- Any future WebView use, including login/bootstrap use, must be justified by the current task and current evidence; no chat-WebView architecture is inherited automatically.
- Do not raise the current iOS 14.0 deployment target merely for convenience or because a newer SDK/Xcode is used in CI.
- Future conversation/session/account/stream/upload identities must have explicit state owners; UI text/titles are consumers and must not become competing identity authorities.
- CI/artifact production must never be described as proof of TrollStore install/launch or in-app runtime behavior.

## Frozen business or architecture rules

None recorded yet.

## Code style / naming constraints

Follow existing repository/source style until explicit project-specific constraints are verified. Keep foundation APIs small and evidence-driven; do not add speculative retry, watchdog, fallback, duplicate state owners or future-only abstractions.

## Prohibited routes / known dangerous regressions

- Do not revive old WebView compensation mechanisms such as speculative timers, watchdogs, DOM scans, Shadow WebView recovery, or fallback chains without a current concrete failure mode and evidence.
- Do not use UI text or title matching as a substitute for a verified conversation identity/state owner when the native implementation is introduced.
- Do not raise the deployment target just because CI uses a newer iPhoneOS SDK.
- Do not add silent auth/network/protocol recovery that hides the original failure from diagnostics.
- Do not log/export authentication secrets or full user content merely to simplify debugging.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for distilled previous-project lessons. That document is advisory evidence, not a current implementation contract.

## Rule maintenance

Rules work may update this file proactively when a durable project-specific constraint is confirmed. Development work may update it when a current product task establishes a new explicit durable contract from user requirements or verified evidence. Never turn a temporary hypothesis or historical suggestion into a permanent current rule.
