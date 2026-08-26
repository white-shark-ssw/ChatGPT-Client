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
- **Decision**: Important async/auth/network/protocol/state operations use the accepted structured local diagnostics authority with bounded persistence and redacted export. The same authority provides explicit user-triggered clearing for repeated device-testing cycles; clearing operates on its own files and must not affect authentication/session state.
- **Evidence**: Foundation diagnostics real-device validation; user request for clearing accumulated logs; b6 implementation clears current JSONL + configured rotated archives through `DiagnosticsStore`'s serial queue. The supplied b6 export contains only the fresh 05:50 cycle and no earlier b1-b5 events, consistent with the clean-log workflow.
- **Rejected / do-not-repeat**: Do not log passwords, OAuth codes, access/session tokens, Cookie values, Authorization headers, full chat bodies or attachment contents; do not add implicit remote telemetry or a competing log store merely to support clearing.
- **Affected modules**: Whole product; `Diagnostics.swift`; Settings diagnostics UI.
- **Validation level**: Core diagnostics Code + CI + Artifact + real-device foundation validation; b6 clear path Code + CI + Artifact with fresh-log runtime evidence consistent with successful use.
- **Supersedes**: None.

### TD-005 — WebKit is the persistent login authority; tested native consumption is transient and route-specific

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Authentication sequencing / session authority / native bridge
- **Decision**: Use embedded `WKWebView` at `https://chatgpt.com/auth/login` for current authentication bootstrap. Default persistent `WKWebsiteDataStore` remains the only persistent auth-secret authority. Native transport may copy current ChatGPT/OpenAI WebKit cookies only transiently into an ephemeral `URLSession` for evidence-backed requests; do not create a second persistent credential store. Any success/failure conclusion remains route-specific.
- **Evidence**: b2 established Continue with Google + persistence. b3 once showed native `/auth/login` HTTP 200. b4 later showed authenticated WebKit while native `/auth/login` returned HTTP 403.
- **Rejected / do-not-repeat**: Do not create a second persistent auth-secret authority. Do not log/persist copied secrets. Do not generalize b3 or b4 beyond their exact tested routes.
- **Affected modules**: `AuthWebViewController`, `AuthSessionStore`, future account/session/network transport.
- **Validation level**: Embedded login/persistence and b3/b4 route behavior are Runtime/manual/real-device tested on iPhone / iOS 17.0.
- **Supersedes**: Earlier broad assumption that native `/auth/login` success could be treated as a durable prerequisite.

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
- **Decision**: Account-context verification is not gated by a separate native request to browser-oriented `/auth/login`. Once WebKit finishes at authenticated ChatGPT, the diagnostic path directly tests ephemeral current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- **Evidence**: b4 isolated native `/auth/login` as the wrong gate. b5 then showed one direct session 403 and a later direct session/accounts HTTP 200 path. b6 repeated the same pattern: first session request 403, then after user-triggered `重新开始`, session HTTP 200 + accounts-check HTTP 200 + verified account context.
- **Rejected / do-not-repeat**: No speculative automatic retry, User-Agent spoof, Cloudflare bypass, parallel duplicate gate or endpoint fallback. Preserve exact stage/status when a direct request fails.
- **Affected modules**: `AuthWebViewController`, `AuthSessionStore`, auth diagnostics and account-context identity.
- **Validation level**: Runtime/manual/real-device tested on iPhone / iOS 17.0.
- **Supersedes**: b4 controller sequencing that required native `/auth/login` before account probing.

### TD-008 — Parse accounts-check by ordered account identity, not `accounts.default`

- **Status**: **Confirmed**
- **Date**: 2026-08-26
- **Scope**: Account-context response parsing
- **Decision**: `payload.accounts.default.account.id` is superseded. Parse the evidenced response as non-empty `account_ordering` plus keyed `accounts`; choose the first ordered entry not explicitly denied by `can_access_with_session`; read nested `account.account_id`. Optional `plan_type` / `structure` remain non-authoritative metadata.
- **Evidence**: b5 accounts-check HTTP 200 contradicted the old required shape with `missing_default_account`. b6 exact runtime then returned session HTTP 200 + accounts-check HTTP 200, observed `accountCount=2`, `accountOrderingCount=1`, selected a `plus` / `personal` account, set `session.accountState=verified`, and ended `accountContextProbe status=ok` in 1289.71 ms. Screenshot title also showed `登录会话 · 账户上下文通过`.
- **Alternatives considered**: Keep probing `accounts.default`; guess multiple fallback shapes; log the response body; add alternate endpoints.
- **Rejected / do-not-repeat**: Do not restore `accounts.default.account.id` as current authority without new current evidence. Do not add speculative multi-shape fallback chains or log response bodies/auth secrets merely to discover structure.
- **Affected modules**: `AuthSessionStore` account-context parser and diagnostics.
- **Validation level**: Code + CI + Artifact + Runtime/manual/real-device tested on iPhone / iOS 17.0.
- **Supersedes**: b5 `accounts.default.account.id` parser assumption.

### TD-009 — Auth bootstrap gate is satisfied by b6 account-context evidence

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Roadmap / task boundary
- **Decision**: `DEV-auth-bootstrap` has met its runtime authentication/account-context gate with b6. The next core task may investigate current conversation-list/detail protocol only after auth changes are integrated; conversation/private protocol remains a separate evidence task and must not be inferred from auth success.
- **Evidence**: b2 Google login + persistence, b5 direct transport evidence, b6 verified ordered account context and user-visible success title.
- **Rejected / do-not-repeat**: Do not treat auth success as proof of conversation protocol shapes or start protocol implementation inside the auth checkpoint.
- **Affected modules**: Roadmap, auth, future protocol/network work.
- **Validation level**: Real-device auth/account-context evidence accepted; protocol remains Unverified.
- **Supersedes**: Phase-2 pending-account-context status.

## Rule

Do not write speculation here as fact. A historical plan or CI artifact is not runtime proof.
