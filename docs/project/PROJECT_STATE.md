# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

The first real product foundation is merged into `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`.

The accepted Stable foundation runtime candidate is `DEV-app-foundation-0.1.0-b1`, built from product/workflow source `89b29434e4d81486d395b8ddb093a031f6f919a7`. It was installed and launched successfully through TrollStore on an iPhone running iOS 17.0, and its diagnostics/settings/persistence path was manually validated.

Authentication work remains Active on `dev/auth-bootstrap-20260826` / draft PR #6. `DEV-auth-bootstrap-0.1.0-b2` validated the current embedded ChatGPT Continue with Google route and persistent WebKit login across force-close/relaunch on the intended iPhone / iOS 17.0 environment. `DEV-auth-bootstrap-0.1.0-b3` now adds the narrow native-session-consumption probe; its exact push candidate has passed CI and produced an IPA, but the native probe has not yet been runtime tested.

The product goal remains an **iOS native ChatGPT client** distributed as an IPA for TrollStore. The intended user-device environment does not exceed iOS 17.0, while compatibility with lower iOS versions is preferred where practical.

## Accepted foundation baseline

`DEV-app-foundation-0.1.0-b1` establishes Swift 5 + UIKit, iOS 14.0 deployment target, no third-party dependencies, application shell/settings, build/runtime identity, structured bounded local diagnostics/redacted export, reproducible unsigned IPA packaging and GitHub Actions build/artifact production. Foundation modules are Stable, not Frozen.

## Active authentication evidence

### b2 — embedded web login and persistence

- Candidate: `DEV-auth-bootstrap-0.1.0-b2`, product source `809fa03e673afded87cb47fb755c998ab1b58e12`.
- CI run `32886019320` passed; artifact ID `9577612707`; IPA SHA-256 `426c5f9b6b5e71a41c3ca571abdc73951835a55dc902691d75030a781ee61465`.
- User completed Continue with Google successfully in the embedded `WKWebView` on iPhone / iOS 17.0.
- After force-close/relaunch, the user remained signed in. The supplied b2 diagnostic export corroborates this: opening `/auth/login` redirected directly to non-auth `chatgpt.com` HTTP 200 with no Google navigation.
- Default persistent `WKWebsiteDataStore` is therefore the current evidenced persistent web-session authority on the tested environment.
- No system-browser fallback is currently justified.

### b3 — native session-consumption candidate

- Candidate: `DEV-auth-bootstrap-0.1.0-b3`, product source `0fcf040012c0698d0e3ce1628fec9865237eba3b`.
- Push run `32889095904` passed on Xcode 16.4 and produced artifact ID `9578766019` / `ChatGPTClient-DEV-auth-bootstrap-0.1.0-b3`.
- IPA: `ChatGPTClient-0.1.0-b3-dev-auth-bootstrap.ipa`; SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`.
- `AuthSessionStore` now owns safe auth evidence state only. WebKit remains the sole persistent secret authority.
- After authenticated WebView navigation, b3 transiently copies ChatGPT/OpenAI cookies into an **ephemeral** native `URLSession` and requests the already-verified `/auth/login` route. Only final safe destination/status/count/error metadata is logged; Cookie/token/Authorization values are not persisted or logged.
- **Runtime status: pending.** CI/artifact success does not prove native authentication acceptance.

Still unverified within authentication/session:

- whether the exact b3 native probe resolves as authenticated on the real device;
- current account/workspace context ownership;
- any additional current headers/context required by later native ChatGPT requests.

A successful WebView login and successful b3 build must not be described as proof that private/internal conversation requests are authenticated.

## Durable development plan

The ordered roadmap remains:

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Active; web login + persistence passed, native consumption runtime test and account/workspace context remain.
3. `DEV-protocol-read` — only after auth/session/account context needed by native requests is evidenced.
4. `DEV-native-read-path`.
5. `DEV-send-stream`.
6. `DEV-long-conversation`.
7. `DEV-attachments`.
8. Daily-use conversation features as separate Work IDs.
9. Advanced capabilities after the core client is stable.

The strongly dependent core remains serialized.

## Diagnostics state

Diagnostics/logging remains a Stable foundation capability: structured OSLog events, trace/span timing, bounded persistent JSONL history, secret-field filtering, redacted export and exact candidate/runtime metadata. Auth work extends the same authority rather than adding a competing log store.

## Current architecture

- `AppDelegate` owns foundation lifecycle/root setup.
- `AppBuildInfo` owns build/runtime identity presentation.
- `DiagnosticsLogger` / `DiagnosticsStore` / `DiagnosticsExporter` own diagnostics state/export.
- `AuthWebViewController` owns login UI/navigation lifecycle and uses default persistent `WKWebsiteDataStore`.
- `AuthSessionStore` owns only web/native auth **evidence state** and the transient native probe; it does not own persistent authentication secrets.
- WebKit default data store is the current persistent auth-secret authority until stronger current evidence justifies changing that contract.
- Account/workspace context owner remains Unknown / Unverified.

## Compatibility direction

Current deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Runtime evidence currently covers iPhone / iOS 17.0 only. Lower iOS versions and iPad runtime remain unverified.

## Known issues / constraints

- Bundle ID is accepted but not Frozen as a permanent signing identity.
- No unit/UI test target yet; automated validation is Release compile, app validation, IPA packaging/inspection and artifact upload.
- b3 native-session acceptance is not runtime-proven yet.
- Account/workspace context and private/internal protocol remain Unknown / Unverified.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
