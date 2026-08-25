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
- **Decision**: Develop a native iOS ChatGPT client from the new Swift/UIKit baseline rather than converting the previous WebView chat implementation into the product source.
- **Evidence**: User requirement; accepted `DEV-app-foundation-0.1.0-b1` runtime baseline.
- **Rejected / do-not-repeat**: Do not inherit the historical WebView chat architecture as the new source baseline.
- **Affected modules**: Whole product.
- **Validation level**: User-confirmed requirement + runtime-tested foundation.
- **Supersedes**: None.

### TD-002 — Previous-project history is reference-only evidence

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Historical evidence / protocol research
- **Decision**: Historical endpoint names, shapes, workarounds and architecture suggestions must be revalidated before becoming current contracts.
- **Evidence**: User classification of the history pack and its own warnings.
- **Rejected / do-not-repeat**: Do not implement current ChatGPT private protocol from old names or memory alone.
- **Affected modules**: Authentication, protocol/network, conversation, streaming, attachments.
- **Validation level**: User-confirmed evidence classification.
- **Supersedes**: None.

### TD-003 — TrollStore IPA distribution with iOS 17.0 ceiling and lowest-practical deployment target

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Runtime compatibility / distribution
- **Decision**: Distribute as IPA for TrollStore. iOS 17.0 is the intended environment ceiling, not the minimum. Keep the minimum as low as practical when real requirements permit.
- **Evidence**: User requirement; current iOS 14.0 Swift/UIKit baseline builds in CI and runs on the intended iOS 17.0 device.
- **Rejected / do-not-repeat**: Do not raise the minimum merely because CI uses a newer SDK or because the user's highest OS is 17.0.
- **Affected modules**: Xcode/build/dependencies/runtime APIs.
- **Validation level**: Build/artifact iOS 14.0; runtime iPhone/iOS 17.0.
- **Supersedes**: None.

### TD-004 — Diagnostics/logging is part of the application foundation

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Observability / debugging / performance evidence
- **Decision**: Important async/auth/network/protocol/state operations use the accepted structured local diagnostics authority with bounded persistence and redacted export.
- **Evidence**: `Diagnostics.swift`, CI/artifact evidence and foundation real-device export/persistence validation.
- **Rejected / do-not-repeat**: Do not postpone observability; do not log passwords, OAuth codes, access/session tokens, Cookie values, Authorization headers, full chat bodies or attachment contents; do not add implicit remote telemetry.
- **Affected modules**: Whole product.
- **Validation level**: Code + CI + artifact + real-device foundation validation.
- **Supersedes**: None.

### TD-005 — WebKit is the current persistent login authority; native consumption must be proven separately

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Authentication sequencing / session authority / native bridge
- **Decision**: Use the simplest embedded `WKWebView` login at `https://chatgpt.com/auth/login` for current authentication bootstrap. On the tested iPhone / iOS 17.0 environment, Continue with Google works and the default persistent `WKWebsiteDataStore` preserves authenticated state across force-close/relaunch. Therefore no system-browser fallback is justified today. WebKit remains the only persistent auth-secret authority. Native transport authentication must be proven separately; the next minimal evidence step is a transient WebKit-cookie -> ephemeral `URLSession` probe of the same `/auth/login` route, not a second persistent credential store.
- **Evidence**: b2 product source `809fa03e...`; CI run `32886019320`; artifact `9577612707`; user completed Google login; user reported retained login after relaunch; supplied b2 diagnostics show the initial Google/OpenAI navigation and later direct `/auth/login` -> non-auth `chatgpt.com` HTTP 200 with no Google navigation. b3 source `0fcf040...` implements `AuthSessionStore` and the ephemeral native probe; push run `32889095904` passed and produced artifact ID `9578766019`, IPA SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`.
- **Alternatives considered**: Preemptively add system-browser fallback; persist copied WebKit cookies/tokens in a new native store; assume successful WebView login means native `URLSession` is authenticated.
- **Rejected / do-not-repeat**: Do not add browser fallback without a concrete new failure. Do not create a second persistent auth-secret authority. Do not log/persist copied secrets. Do not call b3 CI/artifact success proof of native authentication.
- **Affected modules**: `AuthWebViewController`, `AuthSessionStore`, future account/session/network transport.
- **Validation level**: Embedded login + WebKit persistence: Code + CI + Artifact + Runtime/manual/real-device tested. b3 native bridge: Code + CI + Artifact only; runtime pending.
- **Supersedes**: Earlier untested concerns that the embedded route might require a browser handoff or that WebKit state might not survive relaunch.
- **Notes**: The embedded web-login/persistence route is accepted for the tested environment, but broader authentication/session is not Stable until native consumption/account context is evidenced. If b3 runtime probe succeeds, account/workspace context is the next evidence gate before protocol-read work.

### TD-006 — Foundation baseline is Swift/UIKit with iOS 14.0 minimum

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: App foundation / UI / dependency / deployment
- **Decision**: Use Swift 5 + UIKit/Foundation/OSLog/CryptoKit with no third-party dependencies and `IPHONEOS_DEPLOYMENT_TARGET=14.0` until a real requirement justifies change.
- **Evidence**: Current Xcode project, CI compilation and real-device foundation testing.
- **Rejected / do-not-repeat**: Do not raise the minimum for convenience or add dependencies without a concrete need.
- **Affected modules**: Xcode project and future feature availability decisions.
- **Validation level**: Code + CI + artifact + real-device foundation test.
- **Supersedes**: None.

## Rule

Do not write speculation here as fact. A historical plan or CI artifact is not runtime proof.
