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

### TD-005 — WebKit is the persistent login authority; tested native consumption uses a transient bridge

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Authentication sequencing / session authority / native bridge
- **Decision**: Use embedded `WKWebView` at `https://chatgpt.com/auth/login` for current authentication bootstrap. On the tested iPhone / iOS 17.0 environment, Continue with Google works and default persistent `WKWebsiteDataStore` preserves authenticated state across force-close/relaunch. WebKit remains the only persistent auth-secret authority. When native transport needs the current authenticated context, the accepted tested mechanism is to copy current ChatGPT/OpenAI WebKit cookies only transiently into an ephemeral `URLSession`; do not create a second persistent credential store. This bridge is accepted only for the exact runtime-tested `/auth/login` session-consumption scope; account/workspace context and private conversation requests require separate evidence.
- **Evidence**: b2 source `809fa03e...`, CI run `32886019320`, artifact `9577612707`, successful Google login and persisted relaunch diagnostics. b3 exact source `0fcf040012c0698d0e3ce1628fec9865237eba3b`, push run `32889095904`, artifact ID `9578766019`, IPA SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`. User real-device b3 screenshot shows `网页登录成功 · 原生会话通过`; supplied b3 diagnostics identify the exact candidate/source/device and record `session.webState=authenticated`, transient 54 total / 35 matched cookies, `session.nativeState=verified`, and final `chatgpt.com` HTTP 200 / `status=ok` in 1203.68 ms.
- **Alternatives considered**: Preemptively add system-browser fallback; persist copied WebKit cookies/tokens in a native store; assume WebKit success automatically proves every private endpoint.
- **Rejected / do-not-repeat**: Do not add browser fallback without a concrete new failure. Do not create a second persistent auth-secret authority. Do not log/persist copied secrets. Do not generalize the b3 `/auth/login` result to account/workspace or conversation protocol without current evidence.
- **Affected modules**: `AuthWebViewController`, `AuthSessionStore`, future account/session/network transport.
- **Validation level**: Embedded login + persistence: Code + CI + Artifact + Runtime/manual/real-device tested. Transient native bridge to `/auth/login`: Code + CI + Artifact + Runtime/manual/real-device tested on iPhone / iOS 17.0. Account/workspace/private protocol remain Unknown / Unverified.
- **Supersedes**: Earlier untested concerns that the embedded route might require a browser handoff, that WebKit state might not survive relaunch, or that the tested native `URLSession` bridge might fail to consume the current WebKit session.
- **Notes**: Account/workspace context is the remaining Phase 2 evidence gate before `DEV-protocol-read`.

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
