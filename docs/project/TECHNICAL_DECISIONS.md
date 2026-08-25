# Technical Decisions

This file records durable, evidence-backed technical decisions and rejected routes.

## Decision template

### TD-XXX — <title>

- **Status**: Proposed / Confirmed / Rejected / Frozen / Superseded
- **Date**:
- **Scope**:
- **Decision**:
- **Evidence**:
- **Alternatives considered**:
- **Rejected / do-not-repeat**:
- **Affected modules**:
- **Validation level**:
- **Supersedes**:
- **Notes**:

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Product direction / architecture baseline
- **Decision**: The current repository will be developed as an iOS native ChatGPT client. Product code should start from a new native-client baseline rather than treating the previous WebView client as the source to convert.
- **Evidence**: User explicit requirement in the current conversation; repository purpose already identifies a ChatGPT third-party custom client.
- **Alternatives considered**: Continue the previous WebView client as the primary chat runtime.
- **Rejected / do-not-repeat**: Do not inherit the old WebView chat implementation as the new source baseline by default.
- **Affected modules**: Future application architecture; concrete modules not yet created.
- **Validation level**: User-confirmed product requirement; no product code exists yet.
- **Supersedes**: None.
- **Notes**: This decision does not yet select UIKit vs SwiftUI, language/package stack, minimum iOS version, or login implementation.

### TD-002 — Previous-project history is reference-only evidence

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Historical evidence / protocol research / architecture reuse
- **Decision**: `ChatGPT_iOS_Native_Client_History_Pack_2026-08-25.zip` is retained conceptually as prior-project experience. Historical endpoint names, request/response shapes, WebView workarounds, diagnoses, and architecture suggestions must be revalidated before becoming current implementation facts or contracts.
- **Evidence**: User explicitly described the attachment as experience from the previous project and allowed it to be used as reference; the pack itself repeatedly marks old ChatGPT private API details as historical clues only.
- **Alternatives considered**: Treat the old pack as current API/specification or import old WebView implementation as the new baseline.
- **Rejected / do-not-repeat**: Do not implement private ChatGPT protocol behavior from old names or memory alone; do not confuse historical CI/artifact success with current runtime validation.
- **Affected modules**: Future protocol/network layer, authentication, conversation state, attachments, export, performance work.
- **Validation level**: User-confirmed evidence classification; no current protocol implementation exists yet.
- **Supersedes**: None.
- **Notes**: Distilled reference lessons are stored in `HISTORICAL_REFERENCE.md`.

### TD-003 — TrollStore IPA distribution with iOS 17.0 ceiling and lowest-practical deployment target

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Runtime compatibility / deployment / artifact distribution
- **Decision**: The client is distributed as an IPA for installation through TrollStore. The intended user-device OS environment does not exceed iOS 17.0. The future Xcode deployment target should be set as low as practical while still supporting the real required features, APIs, dependencies, and stable runtime behavior.
- **Evidence**: User explicit requirement in the current conversation: TrollStore-installed IPA; iOS systems at most 17.0; lower compatibility is preferred.
- **Alternatives considered**: Set the minimum deployment target to iOS 17.0 by default; optimize only for the newest target OS.
- **Rejected / do-not-repeat**: Do not interpret the iOS 17.0 environment ceiling as `IPHONEOS_DEPLOYMENT_TARGET = 17.0`. Do not choose a numeric minimum before actual source/toolchain/API constraints can be verified.
- **Affected modules**: Future Xcode project/build settings, dependency choices, API availability guards, packaging/signing pipeline, runtime compatibility testing.
- **Validation level**: User-confirmed deployment/compatibility requirement; no product build or runtime validation exists yet.
- **Supersedes**: None.
- **Notes**: The exact minimum iOS version remains Unknown / Unverified until implementation exists. Any future change that raises it must be treated as a compatibility-impacting decision and documented with evidence.

### TD-004 — Diagnostics/logging is part of the application foundation

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Observability / debugging / performance evidence
- **Decision**: Structured local diagnostics must be present from the first executable product build. Important auth, network, protocol, conversation, streaming, rendering, attachment and lifecycle operations must be traceable with correlated events and timing. The app must maintain bounded persistent diagnostic history suitable for real-device investigation and provide a redacted user-triggered diagnostic export path.
- **Evidence**: User explicitly requested logging/instrumentation to make future problem diagnosis easier; historical work showed many important failures were runtime-only and could not be proven by CI/artifact results.
- **Alternatives considered**: Add logs only after specific bugs appear; rely only on Xcode console output; add remote analytics immediately.
- **Rejected / do-not-repeat**: Do not postpone observability until the client becomes complex. Do not log passwords, OAuth codes, access/session tokens, Cookie values, full auth headers, full chat bodies or attachment contents by default. Do not introduce remote telemetry/upload as an implicit requirement.
- **Affected modules**: Future app foundation, auth/session, networking, protocol, conversation state, streaming, rendering/performance, attachments, diagnostics UI/export.
- **Validation level**: User-confirmed product requirement; implementation/runtime validation pending `DEV-app-foundation`.
- **Supersedes**: None.
- **Notes**: Exact logger type/function names are intentionally not frozen before source exists. The durable contract is described in `DEVELOPMENT_PLAN.md` and `PROJECT_SPECIFIC_RULES.md`.

### TD-005 — Current Google-based authentication must be revalidated before protocol implementation

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Authentication sequencing / historical evidence boundary
- **Decision**: Authentication is a dedicated verification stage before native private-protocol work. The first auth implementation should reproduce the user's actual Google-based ChatGPT sign-in on a real device, beginning from the simplest current web-login bootstrap. Historical Web IPA success is evidence that the route worked previously, but it is not a current contract. If embedded login is blocked today, capture the current failure/redirect evidence before choosing the smallest supported system-browser/auth handoff; do not prebuild multiple fallback schemes.
- **Evidence**: User reports the previous Web IPA successfully logged into ChatGPT through web login and that their account uses Google. Current Google OAuth documentation warns embedded user-agents such as `WKWebView` may be rejected with `disallowed_useragent`; current OpenAI help documents continue to support Google social sign-in.
- **Alternatives considered**: Assume the old embedded-WebView Google path still works; design a custom token/login system without reproducing current behavior; build several speculative fallback routes at once.
- **Rejected / do-not-repeat**: Do not assume WebKit cookies, system browser auth state and native `URLSession` state are interchangeable. Do not store or log login credentials/secrets. Do not implement ChatGPT private API clients before authenticated-session evidence exists.
- **Affected modules**: Future authentication bootstrap, session store, account context, network transport, protocol evidence work.
- **Validation level**: Sequencing/evidence rule confirmed; current real-device login behavior remains untested.
- **Supersedes**: None.
- **Notes**: The exact login mechanism remains intentionally unselected until `DEV-auth-bootstrap` produces current runtime evidence.

## Rule

Do not write speculation here as fact. A historical plan is not proof of implementation.
