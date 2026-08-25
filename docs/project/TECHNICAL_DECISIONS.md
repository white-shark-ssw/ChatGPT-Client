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
- **Decision**: The current repository will be developed as an iOS native ChatGPT client. Product code starts from a new native-client baseline rather than treating the previous WebView client as the source to convert.
- **Evidence**: User explicit requirement; repository purpose; accepted `DEV-app-foundation-0.1.0-b1` provides a real native Swift/UIKit baseline and was installed/launched successfully through TrollStore on iPhone / iOS 17.0.
- **Alternatives considered**: Continue the previous WebView client as the primary chat runtime.
- **Rejected / do-not-repeat**: Do not inherit the old WebView chat implementation as the new source baseline by default.
- **Affected modules**: Application architecture and all future product modules.
- **Validation level**: User-confirmed product requirement + Code written + CI passed + Artifact produced + Runtime/manual/real-device tested for the foundation baseline.
- **Supersedes**: None.
- **Notes**: Concrete foundation framework/deployment choices are recorded in TD-006. Authentication remains a later evidence-driven task.

### TD-002 — Previous-project history is reference-only evidence

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Historical evidence / protocol research / architecture reuse
- **Decision**: `ChatGPT_iOS_Native_Client_History_Pack_2026-08-25.zip` is retained conceptually as prior-project experience. Historical endpoint names, request/response shapes, WebView workarounds, diagnoses, and architecture suggestions must be revalidated before becoming current implementation facts or contracts.
- **Evidence**: User explicitly described the attachment as experience from the previous project and allowed it to be used as reference; the pack itself repeatedly marks old ChatGPT private API details as historical clues only.
- **Alternatives considered**: Treat the old pack as current API/specification or import old WebView implementation as the new baseline.
- **Rejected / do-not-repeat**: Do not implement private ChatGPT protocol behavior from old names or memory alone; do not confuse historical CI/artifact success with current runtime validation.
- **Affected modules**: Future protocol/network layer, authentication, conversation state, attachments, export, performance work.
- **Validation level**: User-confirmed evidence classification.
- **Supersedes**: None.
- **Notes**: Distilled reference lessons are stored in `HISTORICAL_REFERENCE.md`.

### TD-003 — TrollStore IPA distribution with iOS 17.0 ceiling and lowest-practical deployment target

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Runtime compatibility / deployment / artifact distribution
- **Decision**: The client is distributed as an IPA for installation through TrollStore. The intended user-device OS environment does not exceed iOS 17.0. The deployment target should remain as low as practical while still supporting real required features, APIs, dependencies, and stable runtime behavior.
- **Evidence**: User explicit requirement; `DEV-app-foundation` builds with iOS 14.0 as the verified minimum for the dependency-free foundation. CI compiled `arm64-apple-ios14.0`, generated IPA metadata reports `MinimumOSVersion=14.0`, and the accepted candidate installed/launched successfully through TrollStore on iPhone / iOS 17.0.
- **Alternatives considered**: Set the minimum deployment target to iOS 17.0 by default; optimize only for the newest target OS.
- **Rejected / do-not-repeat**: Do not interpret the iOS 17.0 environment ceiling as a 17.0 minimum. Do not raise the current 14.0 target merely because CI uses a newer Xcode/SDK.
- **Affected modules**: Xcode project/build settings, dependency choices, API availability, packaging/signing pipeline, runtime compatibility testing.
- **Validation level**: iOS 14.0 is verified at source/build/artifact level; TrollStore install/launch is runtime-validated on iPhone / iOS 17.0. Runtime compatibility on lower iOS versions and iPad remains unverified.
- **Supersedes**: None.
- **Notes**: Any future minimum-OS increase is compatibility-impacting and must be documented with concrete evidence.

### TD-004 — Diagnostics/logging is part of the application foundation

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Observability / debugging / performance evidence
- **Decision**: Structured local diagnostics are present from the first executable product candidate. Important auth, network, protocol, conversation, streaming, rendering, attachment and lifecycle operations must be traceable with correlated events and timing as those modules are introduced. The app maintains bounded persistent diagnostic history and provides a redacted user-triggered diagnostic export path.
- **Evidence**: User explicitly requested logging/instrumentation for future diagnosis; `Diagnostics.swift` implements OSLog events, rolling JSONL persistence, trace/span timing, secret filtering and redacted export; Settings exposes sample-event and export actions; CI compiles/packages the implementation. User real-device testing of `DEV-app-foundation-0.1.0-b1` reported no problems and confirmed data persisted after restart. The supplied export records two launch sequences, successful sample/export operations, pre-restart events after relaunch, correct candidate/runtime metadata and no observed password/token/Cookie/Authorization/OAuth secret fields.
- **Alternatives considered**: Add logs only after specific bugs appear; rely only on Xcode console output; add remote analytics immediately.
- **Rejected / do-not-repeat**: Do not postpone observability. Do not log passwords, OAuth codes, access/session tokens, Cookie values, full auth headers, full chat bodies or attachment contents by default. Do not introduce remote telemetry/upload implicitly.
- **Affected modules**: App foundation and all future async/network/state/render/upload modules.
- **Validation level**: Code written + CI passed + Artifact produced + Runtime/manual/real-device tested on iPhone / iOS 17.0; diagnostics foundation accepted Stable, not Frozen.
- **Supersedes**: None.
- **Notes**: Future modules should extend this same diagnostics authority rather than create competing log stores.

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
- **Notes**: `DEV-app-foundation` intentionally contains no auth/session/private-protocol implementation. `DEV-auth-bootstrap` is the next serial phase after foundation merge.

### TD-006 — Foundation baseline is Swift/UIKit with iOS 14.0 minimum

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: App foundation / UI framework / dependency / deployment baseline
- **Decision**: The native product baseline uses Swift 5 + UIKit, Foundation, OSLog and CryptoKit with no third-party dependencies, and sets `IPHONEOS_DEPLOYMENT_TARGET=14.0`. This is the current compatibility baseline for subsequent work unless a real required API/dependency/runtime constraint justifies changing it.
- **Evidence**: Xcode source/project configuration; Apple's iOS 14 logging API availability for structured `Logger`; TrollStore support range includes iOS 14 through the project's iOS 17.0 ceiling; GitHub Actions Xcode 16.4 compiled `arm64-apple-ios14.0`; generated IPA reports `MinimumOSVersion=14.0`; accepted `DEV-app-foundation-0.1.0-b1` installed/launched and exercised diagnostics successfully through TrollStore on iPhone / iOS 17.0.
- **Alternatives considered**: SwiftUI-first foundation; setting iOS 17.0 as minimum; adding third-party logging/project scaffolding before a concrete need exists.
- **Rejected / do-not-repeat**: Do not raise the minimum OS for convenience, CI SDK age or speculative future features. Do not add a third-party framework merely to replace sufficient system APIs in the current foundation.
- **Affected modules**: Xcode project, application shell, diagnostics, build/CI packaging, future feature availability decisions.
- **Validation level**: Code written + CI passed + Artifact produced + Runtime/manual/real-device tested on iPhone / iOS 17.0. Foundation is Stable, not Frozen; lower iOS runtime remains unverified.
- **Supersedes**: None.
- **Notes**: The current bundle ID is accepted for the foundation but is not Frozen as a permanent signing/product identity.

## Rule

Do not write speculation here as fact. A historical plan is not proof of implementation.
