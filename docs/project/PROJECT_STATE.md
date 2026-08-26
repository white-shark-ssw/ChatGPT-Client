# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

The first product foundation is merged into `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`. The accepted Stable foundation runtime candidate is `DEV-app-foundation-0.1.0-b1`, built from product/workflow source `89b29434e4d81486d395b8ddb093a031f6f919a7` and real-device tested through TrollStore on iPhone / iOS 17.0.

Authentication bootstrap is merged into `main` by PR #6 at merge commit `78f42a06e6254088e3b495cb4529e549a1d4717f`. Its accepted runtime candidate is `DEV-auth-bootstrap-0.1.0-b6`. Embedded Google login, persistent WebKit authentication, direct native `/api/auth/session`, bearer-authenticated accounts-check, ordered account-context parsing, and diagnostics clearing have accepted real-device evidence on iPhone / iOS 17.0.

`DEV-protocol-read` is now Active on `dev/protocol-read-20260826` / draft PR #7. Candidate `DEV-protocol-read-0.1.0-b7`, version `0.1.0 (7)`, has reached **Code written + CI passed + Artifact produced**. Exact product source is `44a137b973e29e2a313e9114fdacb7727dccefb9`; authoritative push run `32938912018`; artifact ID `9595827498`; IPA `ChatGPTClient-0.1.0-b7-dev-protocol-read.ipa`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`; ZIP digest `sha256:c1d851dc949a43587f94fffd34b35c233ff5f35a2c8eef3399d2e722a9f7833f`. Current conversation-list/detail runtime behavior remains **Unknown / Unverified** until the device test is performed.

The product goal remains an **iOS native ChatGPT client** distributed as a TrollStore IPA. Intended user OS does not exceed iOS 17.0; lower compatibility remains preferred where practical.

## Accepted foundation baseline

`DEV-app-foundation-0.1.0-b1` establishes Swift 5 + UIKit, iOS 14.0 deployment target, no third-party dependencies, application shell/settings, build/runtime identity, structured bounded local diagnostics/redacted export, reproducible unsigned IPA packaging and GitHub Actions build/artifact production. Foundation modules are Stable, not Frozen.

## Authentication evidence

- b2 established Continue with Google and persistent authenticated `WKWebsiteDataStore` state across force-close/relaunch.
- b3/b4 established that native browser-oriented `/auth/login` is route-specific evidence only, not an account-context gate.
- b5 established one successful direct `/api/auth/session` + accounts-check path and exposed the obsolete account parser.
- b6 established ordered account selection (`account_ordering` + keyed `accounts` + `account.account_id`) on-device. One b6 attempt returned session HTTP 403; after explicit user restart, a later attempt returned session HTTP 200 + accounts-check HTTP 200 and verified the selected plus/personal account. No automatic retry was added.
- Default persistent `WKWebsiteDataStore` remains the sole persistent auth-secret authority. `AuthSessionStore` owns accepted in-memory account context; copied cookies and bearer remain transient only.

## Protocol-read b7 state

- `AuthSessionStore` can create a private short-lived `AuthTransientSession` only after accepted account verification. It uses ephemeral native transport and injects the transient bearer internally; no token accessor or persistent second credential store exists.
- `ProtocolReadProbe` is a diagnostic-only owner. It attempts one current conversation-list GET and one detail GET for the first returned conversation ID, then discards the payload.
- Diagnostics record only status/timing/byte/item/pagination/tree/role/content-type structural metadata. Full titles, message bodies/parts, payload dumps, raw conversation/message IDs, Cookie values, bearer values and Authorization headers are excluded.
- First b7 CI run `32938007843` and second run `32938132841` failed only on Swift compiler type-check complexity. The implementation was split without changing protocol behavior.
- Exact source `44a137b973e29e2a313e9114fdacb7727dccefb9` passed Xcode 16.4 Release build/package on push run `32938912018`, targeting `arm64-apple-ios14.0`. The downloaded artifact and sidecar hashes were independently rechecked.
- Commits after `44a137...` currently change only project documentation; the b7 product artifact therefore remains representative of current product/workflow code.
- CI/artifact success does **not** prove the conversation endpoints or response structures work on-device. The next gate is one clean iPhone run and diagnostics export.

## Diagnostics state

Diagnostics/logging remains a Stable foundation capability: structured OSLog events, trace/span timing, bounded persistent JSONL history, secret-field filtering, redacted export and exact candidate/runtime metadata. Settings provides user-triggered clearing of current/rotated local diagnostic files through the same owner without affecting WebKit authentication state.

## Current architecture

- `AppDelegate` owns foundation lifecycle/root setup.
- `AppBuildInfo` owns build/runtime identity presentation.
- `DiagnosticsLogger` / `DiagnosticsStore` / `DiagnosticsExporter` own diagnostics state/export/clear.
- `AuthWebViewController` owns login UI/navigation lifecycle and the explicit protocol-read test entry sequencing.
- WebKit default data store remains the sole persistent auth-secret authority.
- `AuthSessionStore` owns current in-memory auth/account context and creation of transient authorized native transport.
- `ProtocolReadProbe` owns only the active diagnostic list/detail probe and persists no production conversation state.
- Production conversation repository/selection/message-tree ownership remains deferred to `DEV-native-read-path` after protocol evidence is accepted.

## Durable development plan

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Completed / merged / Stable for the accepted iPhone / iOS 17.0 auth/account-context scope.
3. `DEV-protocol-read` — Active; b7 Code + CI + Artifact; runtime list/detail evidence pending.
4. `DEV-native-read-path` — blocked on accepted protocol-read evidence.
5. `DEV-send-stream`.
6. `DEV-long-conversation`.
7. `DEV-attachments`.
8. Daily-use conversation features as separate Work IDs.
9. Advanced capabilities after the core client is stable.

The strongly dependent core remains serialized.

## Compatibility direction

Current deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Runtime evidence currently covers iPhone / iOS 17.0 only. Lower iOS versions and iPad runtime remain unverified.

## Known issues / constraints

- Bundle ID is accepted but not Frozen as a permanent signing identity.
- No unit/UI test target yet; automated validation is Release compile, app validation, IPA packaging/inspection and artifact upload.
- A direct `/api/auth/session` request can return HTTP 403 under observed challenge-sensitive conditions; current code intentionally has no speculative automatic retry.
- Exact device-required conversation read headers, list/detail server behavior, non-personal workspace behavior, and all streaming/send protocol remain Unknown / Unverified until current runtime evidence exists.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
