# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

The first product foundation is merged into `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`. The accepted Stable foundation runtime candidate is `DEV-app-foundation-0.1.0-b1`, built from product/workflow source `89b29434e4d81486d395b8ddb093a031f6f919a7` and real-device tested through TrollStore on iPhone / iOS 17.0.

Authentication work remains Active on `dev/auth-bootstrap-20260826` / draft PR #6. b2 established embedded Continue with Google and persistent WebKit login across force-close/relaunch. b3 established real-device native-session consumption for the tested authentication route: current ChatGPT/OpenAI WebKit cookies copied transiently into an ephemeral `URLSession` were accepted by `https://chatgpt.com/auth/login` and resolved to authenticated `chatgpt.com` HTTP 200. b4 now provides an identity-correct **CI-built account-context test candidate**, but its account/workspace result remains runtime-unverified.

The product goal remains an **iOS native ChatGPT client** distributed as a TrollStore IPA. Intended user OS does not exceed iOS 17.0; lower compatibility remains preferred where practical.

## Accepted foundation baseline

`DEV-app-foundation-0.1.0-b1` establishes Swift 5 + UIKit, iOS 14.0 deployment target, no third-party dependencies, application shell/settings, build/runtime identity, structured bounded local diagnostics/redacted export, reproducible unsigned IPA packaging and GitHub Actions build/artifact production. Foundation modules are Stable, not Frozen.

## Authentication evidence

### b2 — embedded web login and persistence

- Candidate `DEV-auth-bootstrap-0.1.0-b2`, product source `809fa03e673afded87cb47fb755c998ab1b58e12`.
- CI run `32886019320` passed; artifact ID `9577612707`; IPA SHA-256 `426c5f9b6b5e71a41c3ca571abdc73951835a55dc902691d75030a781ee61465`.
- User completed Continue with Google successfully in embedded `WKWebView` on iPhone / iOS 17.0.
- Force-close/relaunch retained login; diagnostics corroborated direct `/auth/login` -> logged-in `chatgpt.com` HTTP 200 without Google navigation.
- Default persistent `WKWebsiteDataStore` is the current evidenced persistent auth-secret authority. No system-browser fallback is justified.

### b3 — native session consumption accepted

- Candidate `DEV-auth-bootstrap-0.1.0-b3`, exact runtime product source `0fcf040012c0698d0e3ce1628fec9865237eba3b`.
- Authoritative push run `32889095904` passed on Xcode 16.4 and produced artifact ID `9578766019`, IPA `ChatGPTClient-0.1.0-b3-dev-auth-bootstrap.ipa`, SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`.
- On the intended iPhone / iOS 17.0 device, the user observed `网页登录成功 · 原生会话通过`.
- Supplied b3 diagnostics identify `DEV-auth-bootstrap-0.1.0-b3`, build `3`, source `0fcf040012c0`, iPhone / iOS 17.0 and record `session.webState=authenticated`, 54 WebKit cookies with 35 matching ChatGPT/OpenAI domains for the transient probe, `session.nativeState=verified`, and `nativeSessionProbe.end` at `chatgpt.com` / destination `chatgpt`, HTTP 200, `status=ok`, duration `1203.68 ms`.
- The copied Cookie values are not persisted by `AuthSessionStore`; the supplied probe diagnostics expose counts/state/status rather than authentication-secret values.

This is **Runtime/manual/real-device evidence that an ephemeral native `URLSession` can consume the current authenticated WebKit context for the tested `/auth/login` route**. It is not evidence that conversation/private endpoints require only those cookies.

### b4 — account-context candidate

- `AuthSessionStore` now contains the explicit in-memory account-context candidate owner and one narrow probe: ephemeral current WebKit auth context -> `/api/auth/session` -> transient bearer -> `/backend-api/accounts/check/v4-2023-04-27` -> required default account context only.
- Authentication secrets and response bodies are not logged or persisted; exported `userID` / `accountID` fields are handled by the existing identifier hashing path.
- The first b4 artifact from run `32891478482` is rejected because its filename/artifact identity said b4 while job logs showed an embedded b3 candidate due a stale build-script default. Artifact ID `9579620441` must not be used for runtime testing.
- Commit `33ea1b96f755bdf21fdd7691a9f1084a6d624908` fixes only that concrete identity mismatch.
- Corrected authoritative push run `32891798350` passed Xcode 16.4 build/inspect/upload and explicitly embedded `SOURCE_COMMIT=33ea1b96f755` and `DIAGNOSTICS_CANDIDATE=DEV-auth-bootstrap-0.1.0-b4`.
- Valid artifact ID `9579720453`; artifact `ChatGPTClient-DEV-auth-bootstrap-0.1.0-b4`; IPA `ChatGPTClient-0.1.0-b4-dev-auth-bootstrap.ipa`; IPA SHA-256 `f918b1f5762458e55e89a1f0d23e5c2bf46be11d7f4599c692627a07043dab03`; artifact ZIP digest `sha256:a11819f7473472ec074fc09ee7c0bed4101d3288d92edd9fbe2880d9e666c001`.
- Local extraction of the downloaded artifact rechecked the IPA SHA-256 to the same value.
- b4 is **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested**. Account/workspace context remains Candidate/Unverified until device evidence passes.

## Durable development plan

The ordered roadmap remains:

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Active; web login, persistence and tested native-session bridge passed; valid b4 account-context candidate awaiting real-device test.
3. `DEV-protocol-read` — only after current native-authenticated account/workspace context is runtime-evidenced.
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
- `AuthSessionStore` owns safe web/native auth evidence state, the accepted transient native bridge, and the b4 in-memory candidate account context; it does not own persistent authentication secrets.
- WebKit default data store remains the persistent auth-secret authority.
- Account/workspace context is Candidate/Unverified until b4 runtime testing establishes the current response/owner behavior.

## Compatibility direction

Current deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Runtime evidence currently covers iPhone / iOS 17.0 only. Lower iOS versions and iPad runtime remain unverified.

## Known issues / constraints

- Bundle ID is accepted but not Frozen as a permanent signing identity.
- No unit/UI test target yet; automated validation is Release compile, app validation, IPA packaging/inspection and artifact upload.
- b4 account/workspace context is not runtime proven yet; private/internal conversation protocol remains Unknown / Unverified.
- b3 proves native consumption only for the tested authentication route and environment; do not generalize it to conversation protocol behavior without current evidence.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
