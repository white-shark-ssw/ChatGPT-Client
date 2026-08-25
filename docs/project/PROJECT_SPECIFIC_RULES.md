# Project-Specific Rules

This file contains rules specific to this repository/product. Do not copy assumptions from another project into this file.

Populate/change these rules only from explicit user requirements, verified product/runtime constraints, real source architecture, accepted test results, confirmed compatibility/deployment requirements, or durable technical decisions.

## Product contracts

- The current product goal is an **iOS native ChatGPT client**.
- The previous-project history pack is reference material only. It is not current product source, current protocol documentation, or proof that a historical implementation should be reused.
- The durable ordered implementation roadmap lives in `docs/project/DEVELOPMENT_PLAN.md`.
- `DEV-app-foundation-0.1.0-b1` is the accepted Stable foundation baseline after CI/artifact validation and successful TrollStore real-device testing on iPhone / iOS 17.0. Stable does not mean Frozen; lower-iOS/iPad runtime remains unverified.
- `DEV-auth-bootstrap-0.1.0-b2` has current real-device evidence that the embedded ChatGPT web-login route can complete Continue with Google on the tested iPhone / iOS 17.0 device. This validates that route only; broader session/account/native-auth behavior remains unverified.

## Repository governance contract

- The repository uses the AI Governance Rules as the dynamic authority for AI-assisted work.
- Every new work session must read root `AGENTS.md` first and then `docs/project/START_HERE.md` before substantive work.
- When repository evidence changes materially, the corresponding checkpoint and durable `docs/project/` records must be refreshed in the same work cycle.

## Protocol evidence contract

- Do not implement ChatGPT private/internal Web API behavior from historical endpoint names, old request shapes, or memory alone.
- Before implementing a protocol capability, establish current evidence for the relevant URL/path, method, authentication/account context, headers, request body, response/stream shape, IDs/state semantics, and failure behavior as applicable.
- If current evidence contradicts historical notes, current evidence wins and durable docs must be corrected.
- Successful WebView login alone is not sufficient evidence to begin production native private-protocol implementation. First establish how authenticated/session/account context required by native requests is owned and consumed.

## Authentication contract

- Historical Web-based IPA login success is reference-only; current authentication decisions use current candidate/runtime evidence.
- Current `DEV-auth-bootstrap-0.1.0-b2` real-device evidence shows that the embedded `WKWebView` flow at the current ChatGPT login path can successfully complete Continue with Google on the tested iPhone / iOS 17.0 device.
- Do **not** add a system-browser/auth-session fallback merely because embedded Google OAuth can fail in other contexts. The tested embedded route currently works; a fallback requires a concrete current failure.
- Next authentication evidence must cover session persistence/re-entry, an authoritative authenticated-vs-unauthenticated state signal, account/workspace context ownership, and the mechanism by which later native requests consume authenticated context.
- Do not assume WebKit cookies, system-browser cookies/session state and native `URLSession` authentication state are interchangeable.
- Do not duplicate authentication/session authority. Establish one explicit production owner when the evidence supports it.
- Never persist or log user passwords, OAuth authorization codes, access/refresh/session tokens, Cookie values or equivalent authentication secrets outside the real secure/session mechanism required by the implemented path.

## Diagnostics / logging contract

- Structured diagnostics/logging is required from the **first executable product build** and is implemented/accepted as part of the Stable foundation baseline.
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
- `DEV-app-foundation-0.1.0-b1` is real-device validated through TrollStore on iPhone / iOS 17.0. `DEV-auth-bootstrap-0.1.0-b2` also has real-device web-login validation on that environment. Do not claim runtime compatibility for iOS 14.x–16.x or iPad until separately evidenced.

## Critical invariants

- Historical WebView code must not become the new source baseline merely because it existed in the previous project.
- Current WebView use is limited to the evidence-backed login/bootstrap role; no chat-WebView architecture is inherited automatically.
- A future build/config change that raises the minimum supported iOS version must be treated as a compatibility change and justified against this project's “lower is better” requirement.
- Future conversation/session/account/stream/upload identities must have explicit state owners; UI text/titles are consumers and must not become competing identity authorities.
- CI/artifact success must never be described as runtime proof; candidate/runtime evidence stays associated with the exact build identity recorded in `BUILD_TEST_INDEX.md`.
- Current successful embedded login must not be described as proof that native `URLSession` or future private-protocol calls are authenticated.

## Frozen business or architecture rules

None recorded yet. Foundation modules are Stable, not Frozen. Embedded web login is a runtime-validated Candidate, not Frozen.

## Code style / naming constraints

Follow existing repository style until explicit project-specific constraints are verified.

## Prohibited routes / known dangerous regressions

- Do not revive old WebView compensation mechanisms such as speculative timers, watchdogs, DOM scans, Shadow WebView recovery, or fallback chains without a current concrete failure mode and evidence.
- Do not add a system-browser authentication fallback while the current embedded login route works unless a new concrete runtime failure justifies it.
- Do not use UI text or title matching as a substitute for a verified conversation identity/state owner when the native implementation is introduced.
- Do not raise the current iOS 14.0 minimum merely because the user's highest target OS is iOS 17.0 or CI uses a newer SDK.
- Do not add silent auth/network/protocol recovery that hides the original failure from diagnostics.
- Do not add a second diagnostics persistence/export authority beside the accepted foundation without evidence that the current owner cannot satisfy a concrete requirement.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for distilled previous-project lessons. That document is advisory evidence, not a current implementation contract.

## Rule maintenance

Rules work may update this file proactively when a durable project-specific constraint is confirmed. Development work may update it when a current product task establishes a new explicit durable contract from user requirements or verified evidence. Never turn a temporary hypothesis or historical suggestion into a permanent current rule.
