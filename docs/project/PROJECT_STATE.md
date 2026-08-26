# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

The first product foundation is merged into `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`. The accepted Stable foundation runtime candidate is `DEV-app-foundation-0.1.0-b1`, built from product/workflow source `89b29434e4d81486d395b8ddb093a031f6f919a7` and real-device tested through TrollStore on iPhone / iOS 17.0.

Authentication work remains Active on `dev/auth-bootstrap-20260826` / draft PR #6. Embedded Google login and persistent WebKit authentication are accepted. Native `/auth/login` is route-specific historical evidence only. b5 real-device evidence now establishes a more important boundary: on its second direct probe, `/api/auth/session` returned HTTP 200 and the bearer-authenticated accounts-check also returned HTTP 200; the remaining observed failure was the b5 response parser expecting `accounts.default.account.id`. b6 is the current CI-built candidate and updates parsing to the currently evidenced ordered-account response shape while also adding the requested local-diagnostics clear control.

The product goal remains an **iOS native ChatGPT client** distributed as a TrollStore IPA. Intended user OS does not exceed iOS 17.0; lower compatibility remains preferred where practical.

## Accepted foundation baseline

`DEV-app-foundation-0.1.0-b1` establishes Swift 5 + UIKit, iOS 14.0 deployment target, no third-party dependencies, application shell/settings, build/runtime identity, structured bounded local diagnostics/redacted export, reproducible unsigned IPA packaging and GitHub Actions build/artifact production. Foundation modules are Stable, not Frozen.

## Authentication evidence

### b2 — embedded web login and persistence

- Candidate `DEV-auth-bootstrap-0.1.0-b2`, source `809fa03e673afded87cb47fb755c998ab1b58e12`.
- Continue with Google succeeded in embedded `WKWebView` on iPhone / iOS 17.0.
- Force-close/relaunch retained login. Default persistent `WKWebsiteDataStore` remains the evidenced persistent auth-secret authority.

### b3 / b4 — native `/auth/login` is not a durable gate

- b3 exact source `0fcf040012c0698d0e3ce1628fec9865237eba3b` showed native ephemeral `/auth/login` HTTP 200 under its tested conditions.
- b4 exact source `33ea1b96f755bdf21fdd7691a9f1084a6d624908` later showed WebKit could pass a Cloudflare challenge and reach authenticated ChatGPT while a separate native `/auth/login` returned HTTP 403.
- b4 account probing never ran. The durable conclusion is that browser-oriented `/auth/login` must not be the account-context prerequisite.

### b5 — direct session/accounts transport evidenced on device

- Exact runtime identity: `DEV-auth-bootstrap-0.1.0-b5`, app `0.1.0 (5)`, source `c09f981171b0`, Release, iPhone / iOS 17.0.
- First direct probe after a WebKit Cloudflare challenge: 46 total / 27 matched cookies; `/api/auth/session` HTTP 403; `stage=session`, `session.accountState=notAvailable`.
- Second direct probe: WebKit reached non-`/auth` `chatgpt.com` HTTP 200; 49 total / 30 matched cookies; `/api/auth/session` HTTP 200; required user id and transient bearer were parsed; accounts-check HTTP 200.
- b5 then ended `stage=accounts`, `reason=missing_default_account`. Source inspection shows b5 required `payload.accounts.default.account.id`.
- Therefore the second b5 run is **Runtime/manual/real-device evidence that the current ephemeral native transport can perform both account/session HTTP requests**. The remaining observed failure was parsing the returned accounts shape, not authentication transport.

### b6 — current ordered-account parser candidate

- `AuthSessionStore` now parses the current evidenced shape: non-empty `account_ordering`, keyed `accounts`, first ordered entry not explicitly blocked by `can_access_with_session`, nested `account.account_id`; optional `plan_type` and `structure` remain consumers only.
- Safe failure diagnostics record structural counts/reason only. No response bodies, Cookie values, bearer values or Authorization values are logged or persisted.
- `DiagnosticsStore` now supports clearing the current JSONL and all configured rotated archives on its existing serial queue. Settings exposes this as `清理诊断日志`. This operation does not clear WebKit authentication state or create another diagnostics authority.
- Candidate `DEV-auth-bootstrap-0.1.0-b6`, version `0.1.0 (6)`, exact product/workflow source `19c0cd22923d8c6f4c96e676258b31814d02a942`.
- Authoritative push run `32934821144` passed Xcode 16.4 build/inspect/upload; artifact ID `9594474567`; artifact `ChatGPTClient-DEV-auth-bootstrap-0.1.0-b6`; IPA `ChatGPTClient-0.1.0-b6-dev-auth-bootstrap.ipa`; IPA SHA-256 `c7109f691c1de675ef55da1a08695c10663b62030853453ee2fafd01fb070c8b`; artifact ZIP digest `sha256:68c7cfc6667c362c79900be1cf46154a76aa3a363649b1995ff02a5d83b88d85`.
- Downloaded artifact was locally extracted and its embedded `0.1.0 (6)`, candidate b6, source `19c0cd22923d`, Release, minimum OS 14.0 and IPA checksum were rechecked.
- b6 is **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested**. Account/workspace context remains Candidate until b6 succeeds on-device.

## Durable development plan

The ordered roadmap remains:

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Active; web login/persistence accepted; native session/accounts transport reached HTTP 200 on b5; current b6 ordered-account parsing awaits real-device validation.
3. `DEV-protocol-read` — only after the current account/workspace context required by native requests is runtime-evidenced.
4. `DEV-native-read-path`.
5. `DEV-send-stream`.
6. `DEV-long-conversation`.
7. `DEV-attachments`.
8. Daily-use conversation features as separate Work IDs.
9. Advanced capabilities after the core client is stable.

The strongly dependent core remains serialized.

## Diagnostics state

Diagnostics/logging remains a Stable foundation capability: structured OSLog events, trace/span timing, bounded persistent JSONL history, secret-field filtering, redacted export and exact candidate/runtime metadata. The same owner now also provides explicit user-triggered clearing of its current/rotated local files for repeated test cycles. Clearing is not a second logging authority and does not affect WebKit authentication state.

## Current architecture

- `AppDelegate` owns foundation lifecycle/root setup.
- `AppBuildInfo` owns build/runtime identity presentation.
- `DiagnosticsLogger` / `DiagnosticsStore` / `DiagnosticsExporter` own diagnostics state/export/clear.
- `AuthWebViewController` owns login UI/navigation lifecycle and uses default persistent `WKWebsiteDataStore`.
- WebKit default data store remains the persistent auth-secret authority.
- `AuthSessionStore` owns safe auth evidence and the Candidate in-memory account context; it retains no copied persistent auth secrets.
- Native `/auth/login` is historical diagnostic evidence, not a current state authority or account-context gate.

## Compatibility direction

Current deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Runtime evidence currently covers iPhone / iOS 17.0 only. Lower iOS versions and iPad runtime remain unverified.

## Known issues / constraints

- Bundle ID is accepted but not Frozen as a permanent signing identity.
- No unit/UI test target yet; automated validation is Release compile, app validation, IPA packaging/inspection and artifact upload.
- b6 ordered-account parsing is not runtime proven yet.
- A direct `/api/auth/session` request can return 403 immediately after a Cloudflare challenge, as b5's first direct probe showed. No speculative retry is currently justified.
- Workspace semantics beyond the selected account and the private conversation protocol remain Unknown / Unverified.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
