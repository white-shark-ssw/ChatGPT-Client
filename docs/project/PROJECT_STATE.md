# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

The first product foundation is merged into `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`. The accepted Stable foundation runtime candidate is `DEV-app-foundation-0.1.0-b1`, built from product/workflow source `89b29434e4d81486d395b8ddb093a031f6f919a7` and real-device tested through TrollStore on iPhone / iOS 17.0.

Authentication work remains Active on `dev/auth-bootstrap-20260826` / draft PR #6. b2 established embedded Continue with Google and persistent WebKit login. b3 established that a transient cookie-copy native `URLSession` could consume `/auth/login` under its tested conditions. b4 real-device evidence now shows that same browser-oriented `/auth/login` route can be Cloudflare-challenged and return native HTTP 403 even after WebKit itself reaches authenticated `chatgpt.com`. Therefore native `/auth/login` is no longer used as a prerequisite gate for account-context verification. b5 is the current identity-correct CI-built candidate and directly probes the actual account/session path after authenticated WebKit navigation.

The product goal remains an **iOS native ChatGPT client** distributed as a TrollStore IPA. Intended user OS does not exceed iOS 17.0; lower compatibility remains preferred where practical.

## Accepted foundation baseline

`DEV-app-foundation-0.1.0-b1` establishes Swift 5 + UIKit, iOS 14.0 deployment target, no third-party dependencies, application shell/settings, build/runtime identity, structured bounded local diagnostics/redacted export, reproducible unsigned IPA packaging and GitHub Actions build/artifact production. Foundation modules are Stable, not Frozen.

## Authentication evidence

### b2 — embedded web login and persistence

- Candidate `DEV-auth-bootstrap-0.1.0-b2`, product source `809fa03e673afded87cb47fb755c998ab1b58e12`.
- CI run `32886019320` passed; artifact ID `9577612707`; IPA SHA-256 `426c5f9b6b5e71a41c3ca571abdc73951835a55dc902691d75030a781ee61465`.
- User completed Continue with Google successfully in embedded `WKWebView` on iPhone / iOS 17.0.
- Force-close/relaunch retained login; diagnostics corroborated direct `/auth/login` -> logged-in `chatgpt.com` HTTP 200 without Google navigation.
- Default persistent `WKWebsiteDataStore` remains the evidenced persistent auth-secret authority.

### b3 — native `/auth/login` consumption evidence

- Candidate `DEV-auth-bootstrap-0.1.0-b3`, exact runtime product source `0fcf040012c0698d0e3ce1628fec9865237eba3b`.
- Authoritative push run `32889095904`; artifact ID `9578766019`; IPA SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`.
- On iPhone / iOS 17.0, copied current ChatGPT/OpenAI WebKit cookies in an ephemeral `URLSession` resolved `/auth/login` to authenticated `chatgpt.com` HTTP 200.
- This remains valid evidence for that tested route/time. It is not a durable guarantee that `/auth/login` will remain challenge-free or a required gate for later private requests.

### b4 — Cloudflare-gated native auth route

- Exact tested candidate: `DEV-auth-bootstrap-0.1.0-b4`, version `0.1.0 (4)`, source `33ea1b96f755bdf21fdd7691a9f1084a6d624908`, artifact ID `9579720453`, IPA SHA-256 `f918b1f5762458e55e89a1f0d23e5c2bf46be11d7f4599c692627a07043dab03`.
- User screenshot showed `网页登录成功 · 原生会话未通过`.
- Supplied diagnostic export identifies iPhone / iOS 17.0 and records WebKit `/auth/login` HTTP 403, then `challenges.cloudflare.com` HTTP 200, then non-auth `chatgpt.com` HTTP 200 with `session.webState=authenticated`.
- The native `/auth/login` probe copied 46 total WebKit cookies / 27 ChatGPT/OpenAI matches into ephemeral `URLSession`, but returned HTTP 403 in 536.82 ms and set `session.nativeState=notAuthenticated`.
- `accountContextProbe` never started because the controller only called it after native `/auth/login` verification. Thus b4 is evidence of a **failed prerequisite design**, not evidence that account/session acquisition failed.

### b5 — direct account-context candidate

- `AuthWebViewController` now starts account-context verification directly once WebKit finishes at authenticated non-`/auth` `chatgpt.com`; it no longer requires native `/auth/login` success first.
- `AuthSessionStore.probeAccountContext` remains the one narrow candidate path: current WebKit auth context copied transiently into ephemeral `URLSession` -> `/api/auth/session` -> transient bearer -> `/backend-api/accounts/check/v4-2023-04-27` -> required default account context only.
- b5 adds safe `accountContextProbe.webData` cookie counts so direct native session probing has enough evidence without exposing Cookie values.
- Candidate `DEV-auth-bootstrap-0.1.0-b5`, version `0.1.0 (5)`, exact product/workflow source `c09f981171b02dc8a4f0d8ada4624bd779c68c2f`.
- Authoritative push run `32932389742` passed Xcode 16.4 build/inspect/upload; artifact ID `9593649485`; artifact `ChatGPTClient-DEV-auth-bootstrap-0.1.0-b5`; IPA `ChatGPTClient-0.1.0-b5-dev-auth-bootstrap.ipa`; IPA SHA-256 `d9a22635cc6ac05d2ba09a0a627eaa74d38d1a690b5e9affe2f318d2aa204f15`; artifact ZIP digest `sha256:4ad6e95d4e30981aa63bb8bd401c0d4cd9acdddabbf83fab27b1f6fe54307066`.
- Downloaded artifact was locally extracted and verified: embedded app version/build `0.1.0 (5)`, candidate b5, source `c09f981171b0`, deployment target 14.0; local IPA SHA-256 equals CI sidecar.
- b5 is **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested**.

## Durable development plan

The ordered roadmap remains:

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Active; web login/persistence accepted, current direct account/session probe candidate b5 awaiting real-device test.
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
- WebKit default data store remains the persistent auth-secret authority.
- `AuthSessionStore` owns safe auth evidence and the Candidate in-memory account context. It retains no copied persistent auth secrets.
- Native `/auth/login` is historical diagnostic evidence, not a current state authority or account-context gate.

## Compatibility direction

Current deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Runtime evidence currently covers iPhone / iOS 17.0 only. Lower iOS versions and iPad runtime remain unverified.

## Known issues / constraints

- Bundle ID is accepted but not Frozen as a permanent signing identity.
- No unit/UI test target yet; automated validation is Release compile, app validation, IPA packaging/inspection and artifact upload.
- Direct `/api/auth/session` behavior from the current ephemeral native transport remains runtime-unverified until b5 device testing.
- Accounts-check bearer acceptance/default-account response shape and private conversation protocol remain Unknown / Unverified.
- Do not add Cloudflare bypass, User-Agent spoofing, retry/fallback chains or a second credential authority unless a concrete later result justifies a specific change.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
