# Project-Specific Rules

This file contains rules specific to this repository/product. Do not copy assumptions from another project into this file.

Populate/change these rules only from explicit user requirements, verified product/runtime constraints, real source architecture, accepted test results, confirmed compatibility/deployment requirements, or durable technical decisions.

## Product contracts

- The current product goal is an **iOS native ChatGPT client**.
- The previous-project history pack is reference material only. It is not current product source, current protocol documentation, or proof that a historical implementation should be reused.
- The durable ordered implementation roadmap lives in `docs/project/DEVELOPMENT_PLAN.md`.
- `DEV-app-foundation-0.1.0-b1` is the accepted Stable foundation baseline after CI/artifact validation and successful TrollStore real-device testing on iPhone / iOS 17.0. Stable does not mean Frozen; lower-iOS/iPad runtime remains unverified.

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

- Structured diagnostics/logging is required from the **first executable product build** and is now implemented/accepted as part of the Stable foundation baseline.
- Important app lifecycle, authentication, session/account, network, protocol, conversation selection/state, streaming, rendering/performance, attachment and persistence operations must emit correlated diagnostic events sufficient to reconstruct the operation path.
- Include timing/count/size/status/error metadata where useful, while keeping the event schema stable enough to compare different test candidates.
- Maintain a bounded persistent local diagnostic history suitable for TrollStore-installed real-device debugging away from Xcode. Logs must not grow without limit. The accepted foundation uses a 2 MiB current JSONL file plus up to three rotated archives.
- Provide user-triggered redacted diagnostic export. The accepted foundation exposes this from Settings and real-device validation confirmed export plus persistence across relaunch.
- By default, do **not** log passwords, OAuth codes, tokens, Cookie values, full `Authorization`/`Cookie` headers, complete chat-message text, full user-content request/response bodies, or attachment contents.
- Prefer safe metadata such as method/path category, HTTP status, elapsed time, byte count, MIME/type, node/item count and terminal reason.
- Identifiers required to diagnose state ownership may be kept inside the app's private local diagnostics when justified, but exported diagnostics must redact/hash sensitive identifiers and must never export auth secrets.
- Remote analytics/telemetry or automatic log upload is **not** implied by the logging requirement; add it only if explicitly required later.
- Future tasks must extend the existing diagnostics authority rather than create an unrelated competing log store without concrete evidence that the current owner is insufficient.

## Compatibility / deployment constraints

- Platform direction: iOS native application.
- Distribution/install form: IPA installed through TrollStore.
- Intended user-device OS versions do not exceed iOS 17.0. Do not introduce a required API, dependency, framework setting, or deployment configuration that makes iOS > 17.0 mandatory unless the user explicitly changes this requirement.
- iOS 17.0 is an environment ceiling, **not** the minimum deployment target.
- Current accepted minimum deployment target is iOS 14.0 for the Swift/UIKit dependency-free foundation. Do not raise it without a concrete required API/dependency/runtime reason and corresponding documentation update.
- `DEV-app-foundation-0.1.0-b1` is real-device validated through TrollStore on iPhone / iOS 17.0. Do not claim runtime compatibility for iOS 14.x–16.x or iPad until separately evidenced.

## Critical invariants

- Historical WebView code must not become the new source baseline merely because it existed in the previous project.
- Any future WebView use, including login/bootstrap use, must be justified by the current task and current evidence; no chat-WebView architecture is inherited automatically.
- A future build/config change that raises the minimum supported iOS version must be treated as a compatibility change and justified against this project's “lower is better” requirement.
- Future conversation/session/account/stream/upload identities must have explicit state owners; UI text/titles are consumers and must not become competing identity authorities.
- CI/artifact success must never be described as runtime proof; candidate/runtime evidence stays associated with the exact build identity recorded in `BUILD_TEST_INDEX.md`.

## Frozen business or architecture rules

None recorded yet. Foundation modules are Stable, not Frozen.

## Code style / naming constraints

Follow existing repository style until explicit project-specific constraints are verified.

## Prohibited routes / known dangerous regressions

- Do not revive old WebView compensation mechanisms such as speculative timers, watchdogs, DOM scans, Shadow WebView recovery, or fallback chains without a current concrete failure mode and evidence.
- Do not use UI text or title matching as a substitute for a verified conversation identity/state owner when the native implementation is introduced.
- Do not raise the current iOS 14.0 minimum merely because the user's highest target OS is iOS 17.0 or CI uses a newer SDK.
- Do not add silent auth/network/protocol recovery that hides the original failure from diagnostics.
- Do not add a second diagnostics persistence/export authority beside the accepted foundation without evidence that the current owner cannot satisfy a concrete requirement.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for distilled previous-project lessons. That document is advisory evidence, not a current implementation contract.

## Rule maintenance

Rules work may update this file proactively when a durable project-specific constraint is confirmed. Development work may update it when a current product task establishes a new explicit durable contract from user requirements or verified evidence. Never turn a temporary hypothesis or historical suggestion into a permanent current rule.
