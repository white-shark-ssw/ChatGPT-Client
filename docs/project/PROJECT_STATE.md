# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

The first product foundation is merged into `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`. The accepted Stable foundation runtime candidate is `DEV-app-foundation-0.1.0-b1`, built from product/workflow source `89b29434e4d81486d395b8ddb093a031f6f919a7` and real-device tested through TrollStore on iPhone / iOS 17.0.

Authentication work remains on `dev/auth-bootstrap-20260826` / draft PR #6, but its current acceptance gate is now met by `DEV-auth-bootstrap-0.1.0-b6`. Embedded Google login, persistent WebKit authentication, direct native `/api/auth/session`, bearer-authenticated accounts-check, and ordered account-context parsing have all reached real-device success on iPhone / iOS 17.0. The task is ready for integration/merge; private conversation protocol work remains a separate future task.

The product goal remains an **iOS native ChatGPT client** distributed as a TrollStore IPA. Intended user OS does not exceed iOS 17.0; lower compatibility remains preferred where practical.

## Accepted foundation baseline

`DEV-app-foundation-0.1.0-b1` establishes Swift 5 + UIKit, iOS 14.0 deployment target, no third-party dependencies, application shell/settings, build/runtime identity, structured bounded local diagnostics/redacted export, reproducible unsigned IPA packaging and GitHub Actions build/artifact production. Foundation modules are Stable, not Frozen.

## Authentication evidence

### b2 — embedded web login and persistence

- Continue with Google succeeded in embedded `WKWebView` on iPhone / iOS 17.0.
- Force-close/relaunch retained login. Default persistent `WKWebsiteDataStore` remains the evidenced persistent auth-secret authority.

### b3 / b4 — native `/auth/login` is not a durable gate

- b3 showed native ephemeral `/auth/login` HTTP 200 under one tested condition.
- b4 later showed WebKit could pass a Cloudflare challenge and remain authenticated while a separate native `/auth/login` returned HTTP 403.
- Durable conclusion: browser-oriented `/auth/login` is route-specific evidence only and must not be an account-context prerequisite.

### b5 — direct session/accounts transport evidenced

- One direct `/api/auth/session` request returned HTTP 403 after an observed Cloudflare challenge.
- A later direct b5 run returned `/api/auth/session` HTTP 200, parsed the required user id/transient bearer, and then accounts-check HTTP 200.
- b5 then failed only because source required obsolete `payload.accounts.default.account.id`.

### b6 — account/workspace context accepted on device

- Candidate `DEV-auth-bootstrap-0.1.0-b6`, version `0.1.0 (6)`, exact product/workflow source `19c0cd22923d8c6f4c96e676258b31814d02a942`.
- Authoritative push run `32934821144` passed Xcode 16.4 build/inspect/upload; artifact ID `9594474567`; IPA `ChatGPTClient-0.1.0-b6-dev-auth-bootstrap.ipa`; IPA SHA-256 `c7109f691c1de675ef55da1a08695c10663b62030853453ee2fafd01fb070c8b`; ZIP digest `sha256:68c7cfc6667c362c79900be1cf46154a76aa3a363649b1995ff02a5d83b88d85`.
- User export `ChatGPTClient-Diagnostics-20260826-055035.json` matches b6/build 6/source `19c0cd22923d`, Release, iPhone / iOS 17.0.
- First b6 attempt: 48 total / 29 matched WebKit cookies; `/api/auth/session` HTTP 403; `stage=session`; `session.accountState=notAvailable`.
- User explicitly pressed `重新开始`. Second attempt: 49 total / 30 matched cookies; `/api/auth/session` HTTP 200; accounts-check HTTP 200; parser observed `accountCount=2`, `accountOrderingCount=1`, selected a `plus` / `personal` account, set `session.accountState=verified`, and ended `accountContextProbe` with `status=ok` in 1289.71 ms.
- User screenshot title reads `登录会话 · 账户上下文通过`.
- Therefore current account/workspace context is **Runtime/manual/real-device tested and accepted** for the b6 path on iPhone / iOS 17.0. The initial 403 remains route/timing evidence; the successful second attempt was user-triggered, not an automatic retry.

## Diagnostics state

Diagnostics/logging remains a Stable foundation capability: structured OSLog events, trace/span timing, bounded persistent JSONL history, secret-field filtering, redacted export and exact candidate/runtime metadata. b6 also provides user-triggered clearing of current/rotated local diagnostic files through the same owner without affecting WebKit authentication state. The supplied b6 export contains only the fresh 05:50 test cycle and no older b1-b5 events, consistent with the requested clean-log workflow.

## Current architecture

- `AppDelegate` owns foundation lifecycle/root setup.
- `AppBuildInfo` owns build/runtime identity presentation.
- `DiagnosticsLogger` / `DiagnosticsStore` / `DiagnosticsExporter` own diagnostics state/export/clear.
- `AuthWebViewController` owns login UI/navigation lifecycle and uses default persistent `WKWebsiteDataStore`.
- WebKit default data store remains the sole persistent auth-secret authority.
- `AuthSessionStore` is the accepted in-memory owner for current auth/account context; copied cookies and `/api/auth/session` bearer remain transient and are not persisted.
- Native `/auth/login` is historical diagnostic evidence, not a current state authority or account-context gate.

## Durable development plan

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Acceptance achieved on b6; pending PR #6 integration/merge.
3. `DEV-protocol-read` — may begin only as a separate task after auth integration; establish current conversation-list/detail protocol evidence before production models depend on it.
4. `DEV-native-read-path`.
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
- A direct `/api/auth/session` request can return HTTP 403 immediately after a Cloudflare challenge; current code intentionally has no speculative automatic retry.
- Workspace semantics beyond the selected account and all private conversation-list/detail/streaming protocol remain Unknown / Unverified.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
