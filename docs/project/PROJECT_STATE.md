# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

Planning baseline: `main@5e346232cfef0bdb41bab5f6023e89bd8c18a17e`.

The product goal is an **iOS native ChatGPT client**. Distribution is intended as an IPA installed through TrollStore. The target user-device environment does not exceed iOS 17.0, while compatibility with lower iOS versions is preferred where practical.

No application/product source baseline has been added yet. Product implementation details and the exact minimum deployment target must be established from future source, toolchain/API requirements, artifacts and runtime evidence.

## Durable development plan

The ordered implementation roadmap is recorded in `docs/project/DEVELOPMENT_PLAN.md`.

Current intended sequence:

1. `DEV-app-foundation` — create the real Xcode/iOS baseline, TrollStore-installable IPA path, build identity and safe diagnostics/logging foundation.
2. `DEV-auth-bootstrap` — reproduce the user's current Google-based ChatGPT login on-device and establish real authenticated-session evidence.
3. `DEV-protocol-read` — establish current conversation-list/detail/account-context protocol evidence.
4. `DEV-native-read-path` — build native conversation navigation, authoritative conversation state and native message rendering.
5. `DEV-send-stream` — send text and process streaming replies with correct conversation/message ownership.
6. `DEV-long-conversation` — dedicated real-device long-conversation performance/stability work.
7. `DEV-attachments` — native files/photos/videos upload and attachment state.
8. Split daily-use conversation features into separate Work IDs as dependencies become stable.
9. Add advanced ChatGPT capabilities only after core chat is stable and current protocol evidence exists.

The strongly dependent core (`app foundation -> auth -> protocol read -> native read -> send/stream`) should normally be serialized rather than developed as independent parallel branches.

## Authentication evidence

The user reports that a previous Web-based IPA successfully used ChatGPT web login and that their account uses **Continue with Google**. This is valuable historical evidence, not proof that the same embedded login path still works today.

Current Google OAuth guidance warns that authorization endpoints shown in embedded user-agents such as `WKWebView` can be rejected with `disallowed_useragent`. Therefore `DEV-auth-bootstrap` must reproduce current behavior on-device first, log safe navigation/state evidence, and only choose an alternate supported browser/auth handoff if current evidence requires it. Do not assume WebKit cookies, system-browser state and native `URLSession` authentication state are interchangeable.

## Diagnostics direction

Structured diagnostics/logging is a first-class product requirement from the first executable build, not a later debugging patch. The durable contract is defined in `DEVELOPMENT_PLAN.md` and `PROJECT_SPECIFIC_RULES.md`.

Key requirements include bounded persistent local logs, correlation across async/network/stream/upload operations, performance spans, user-triggered redacted diagnostic export, and default exclusion of authentication secrets and full chat content.

## Current development candidates

No product-code candidate is allocated yet. The roadmap-planning Work produces documentation only and no IPA candidate.

## Current architecture

Product architecture is not implemented yet.

Accepted architecture-level direction:

- iOS native client rather than the previous WebView chat runtime;
- authentication/session establishment is separated conceptually from the native chat UI;
- conversation identity and future session/account/message-stream identities require explicit state owners;
- historical WebView/private-protocol details remain reference-only until revalidated.

Governance architecture: root `AGENTS.md` → `docs/project/START_HERE.md` → session router/checkpoints and durable project-state documents under `docs/project/`.

## Compatibility direction

- produce/install an IPA through TrollStore;
- do not require iOS newer than 17.0 for the intended environment;
- when the Xcode project and feature/API requirements are known, choose the lowest practical deployment target that can be built and validated reliably;
- do not confuse the iOS 17.0 environment ceiling with the minimum deployment target.

## Known issues / constraints

- Product language/framework, dependency, Xcode project structure, build/test, CI, version/build, exact minimum deployment target, signing/packaging pipeline, and module ownership are not yet verified.
- Current Google-based web login behavior in the future app has not yet been real-device validated.
- ChatGPT private/internal protocol details can change and must be established from current evidence before implementation.
- New libraries/framework choices must not silently raise the required OS above the accepted compatibility envelope.
- Historical WebView performance/lifecycle problems are useful design warnings, not proof of present native-client behavior.
- These fields must be refreshed automatically when real product files, protocol evidence, tests, artifacts, diagnostics or runtime results are added.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Historical experience is lower authority than the user's latest requirement, current source, and current runtime/protocol evidence.
