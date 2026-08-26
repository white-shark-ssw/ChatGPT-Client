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

### TD-005 — WebKit is the persistent login authority; tested native consumption is transient and route-specific

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Authentication sequencing / session authority / native bridge
- **Decision**: Use embedded `WKWebView` at `https://chatgpt.com/auth/login` for current authentication bootstrap. Default persistent `WKWebsiteDataStore` remains the only persistent auth-secret authority. Native transport may copy current ChatGPT/OpenAI WebKit cookies only transiently into an ephemeral `URLSession` for evidence-backed requests; do not create a second persistent credential store. Any success/failure conclusion is route-specific and must not be generalized.
- **Evidence**: b2 established Continue with Google + persistence. b3 exact source `0fcf040012c0698d0e3ce1628fec9865237eba3b` / run `32889095904` showed native `/auth/login` HTTP 200 with 54 total / 35 matched cookies. b4 exact source `33ea1b96f755bdf21fdd7691a9f1084a6d624908` later showed WebKit could reach authenticated `chatgpt.com` after a Cloudflare challenge while native `/auth/login` returned HTTP 403 with 46 total / 27 matched cookies.
- **Alternatives considered**: Persist copied WebKit cookies/tokens in a native store; assume one successful route proves all private endpoints; treat a later `/auth/login` 403 as proof that WebKit login was lost.
- **Rejected / do-not-repeat**: Do not create a second persistent auth-secret authority. Do not log/persist copied secrets. Do not generalize b3 or b4 beyond their exact tested routes. Do not infer WebKit logout from a native Cloudflare 403 when WebKit itself is authenticated.
- **Affected modules**: `AuthWebViewController`, `AuthSessionStore`, future account/session/network transport.
- **Validation level**: Embedded login/persistence + b3/b4 route behavior are Runtime/manual/real-device tested on iPhone / iOS 17.0. Account/workspace/private protocol remain separately gated.
- **Supersedes**: Earlier broad assumption that native `/auth/login` success could be treated as a durable prerequisite for later account-context work.

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

### TD-007 — Probe the actual account/session path directly after authenticated WebKit navigation

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Authentication account-context sequencing
- **Decision**: Account-context verification must not be gated by a separate native request to browser-oriented `/auth/login`. Once WebKit finishes at authenticated non-`/auth` `chatgpt.com`, the diagnostic path should directly test the actual account/session request needed for the next phase. Current b5 therefore invokes `probeAccountContext` directly: ephemeral current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- **Evidence**: b4 runtime: WebKit `/auth/login` initially HTTP 403, Cloudflare challenge succeeded, WebKit reached authenticated `chatgpt.com` HTTP 200, but native `/auth/login` independently returned HTTP 403 and prevented account probe from running. This isolates the gate as the wrong prerequisite. b5 source `c09f981171b02dc8a4f0d8ada4624bd779c68c2f` implements the direct sequencing and passed CI/artifact production in run `32932389742`; runtime result is pending.
- **Alternatives considered**: Retry native `/auth/login`; spoof User-Agent; add Cloudflare bypass logic; run both probes concurrently; retain the failed gate and treat its result as account failure.
- **Rejected / do-not-repeat**: No speculative retry, User-Agent spoof, Cloudflare bypass, parallel duplicate gate or endpoint fallback. If `/api/auth/session` itself fails, record its exact stage/status first.
- **Affected modules**: `AuthWebViewController`, `AuthSessionStore`, auth diagnostics and account-context candidate identity.
- **Validation level**: Sequencing reason is backed by b4 real-device evidence. b5 implementation is Code written + CI passed + Artifact produced; runtime pending.
- **Supersedes**: b4 controller sequencing that required `probeNativeSession(/auth/login)` to verify before `probeAccountContext` could start.

## Rule

Do not write speculation here as fact. A historical plan or CI artifact is not runtime proof.
