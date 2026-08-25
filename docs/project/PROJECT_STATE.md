# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

The first real product foundation is merged into `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`.

The accepted Stable foundation runtime candidate is `DEV-app-foundation-0.1.0-b1`, built from product/workflow source `89b29434e4d81486d395b8ddb093a031f6f919a7`. It was installed and launched successfully through TrollStore on an iPhone running iOS 17.0, and its diagnostics/settings/persistence path was manually validated.

Authentication work is active on `dev/auth-bootstrap-20260826` / draft PR #6. Candidate `DEV-auth-bootstrap-0.1.0-b2`, product/build-input source `809fa03e673afded87cb47fb755c998ab1b58e12`, passed CI and produced a test artifact. The user then successfully completed the current ChatGPT Continue with Google login in the embedded `WKWebView` flow on the intended real device. This validates the embedded web-login route for that candidate/device, but not native session consumption.

The product goal remains an **iOS native ChatGPT client** distributed as an IPA for TrollStore. The intended user-device environment does not exceed iOS 17.0, while compatibility with lower iOS versions is preferred where practical.

## Accepted foundation baseline

`DEV-app-foundation-0.1.0-b1` establishes:

- Swift 5 + UIKit application shell with no third-party dependencies;
- iOS 14.0 deployment target;
- repository-derived bundle ID `com.whitesharkssw.chatgptclient` (accepted for the foundation, not Frozen as a permanent signing identity);
- in-app version/build/candidate/source-commit/runtime metadata;
- structured OSLog diagnostics plus bounded persistent JSONL history;
- trace/span correlation and safe error/status metadata;
- local secret-field filtering and exported identifier hashing/redaction;
- user-triggered diagnostic JSON export from Settings;
- reproducible `scripts/build_ipa.sh` packaging path;
- GitHub Actions macOS build/IPA artifact workflow.

Automated foundation evidence:

- GitHub Actions run `32876352123` passed on Xcode 16.4 and produced artifact ID `9574034381`.
- Final material PR head `aa3233de...` passed run `32877096378`.
- Final PR completion head `c3a9437c...` passed run `32878347358` before merge.
- Accepted IPA SHA-256: `dcdefac9e508c5fd55c3c418fc0ea497c736f54fadc3b5e946300c5c1c032760`.

Runtime foundation evidence confirms TrollStore install/launch, Settings/sample/export, persistent diagnostics across relaunch and privacy-safe exported logs on iPhone / iOS 17.0.

## Active authentication evidence

`DEV-auth-bootstrap-0.1.0-b2` currently establishes:

- minimal embedded `WKWebView` login bootstrap at `https://chatgpt.com/auth/login`;
- Continue with Google can complete successfully on the tested iPhone / iOS 17.0 candidate;
- privacy-safe navigation diagnostics reuse the Stable diagnostics authority and do not record password/OAuth-code/token/Cookie/Authorization values;
- user-supplied app icon is included through a deterministic checksum-verified reconstruction/build path;
- CI run `32886019320` passed on Xcode 16.4;
- GitHub artifact ID `9577612707`, artifact `ChatGPTClient-DEV-auth-bootstrap-0.1.0-b2`;
- IPA `ChatGPTClient-0.1.0-b2-dev-auth-bootstrap.ipa`, SHA-256 `426c5f9b6b5e71a41c3ca571abdc73951835a55dc902691d75030a781ee61465`.

The current runtime result rejects the need to add a system-browser fallback merely because embedded Google OAuth can fail in other contexts. Current evidence says this tested route works. A fallback requires a concrete future failure.

Still unverified within authentication/session:

- whether the authenticated WebKit session persists across force-close/relaunch;
- an authoritative authenticated-vs-unauthenticated state signal;
- account/workspace context ownership;
- whether and how the WebKit-authenticated state can be used by native `URLSession` requests without creating a second auth authority.

A successful WebView login must not be described as proof that native ChatGPT private/internal requests are authenticated.

## Durable development plan

The ordered implementation roadmap is recorded in `docs/project/DEVELOPMENT_PLAN.md`.

Current intended sequence:

1. `DEV-app-foundation` — **Completed / merged / Stable foundation**.
2. `DEV-auth-bootstrap` — **Active**; embedded Google web login runtime-validated, session persistence/authenticated-state/account-context/native consumption still pending.
3. `DEV-protocol-read` — establish current conversation-list/detail/account-context protocol evidence only after the auth/session evidence gate is satisfied.
4. `DEV-native-read-path` — build native conversation navigation, authoritative conversation state and native message rendering.
5. `DEV-send-stream` — send text and process streaming replies with correct conversation/message ownership.
6. `DEV-long-conversation` — dedicated real-device long-conversation performance/stability work.
7. `DEV-attachments` — native files/photos/videos upload and attachment state.
8. Split daily-use conversation features into separate Work IDs as dependencies become stable.
9. Add advanced ChatGPT capabilities only after core chat is stable and current protocol evidence exists.

The strongly dependent core (`app foundation -> auth -> protocol read -> native read -> send/stream`) should normally be serialized rather than developed as independent parallel branches.

## Diagnostics state

Diagnostics/logging is an accepted Stable foundation capability:

- app lifecycle and UI/settings actions emit structured local events;
- async operations can use trace IDs and timing spans;
- persistent history is size/count bounded (2 MiB current file plus up to three rotated files);
- secret-like field names are redacted before local persistence;
- exported account/conversation/message/session/user/workspace identifiers are SHA-256 shortened hashes;
- Settings exposes sample-event generation and user-triggered JSON export;
- build/device/runtime metadata is included in exports;
- real-device validation confirmed export and persistence across app relaunch on iPhone / iOS 17.0;
- auth bootstrap extends the same authority with safe web-navigation destination/host/status/error metadata.

## Current architecture

Accepted architecture-level direction:

- native Swift/UIKit app baseline;
- `AppDelegate` owns foundation lifecycle/root setup;
- `AppBuildInfo` owns build/runtime identity presentation;
- `DiagnosticsLogger` / `DiagnosticsStore` / `DiagnosticsExporter` own diagnostics state and export;
- `AuthWebViewController` currently owns only the embedded login UI/navigation lifecycle and uses the default persistent `WKWebsiteDataStore`;
- production authentication/session/account ownership remains to be established from evidence;
- future conversation/session/account/message-stream identities require explicit state owners;
- historical WebView/private-protocol details remain reference-only until revalidated.

## Compatibility direction

- current deployment target: iOS 14.0;
- build artifact is arm64 and declares iPhone+iPad device families;
- intended environment ceiling remains iOS 17.0;
- TrollStore installation/launch is verified on iPhone / iOS 17.0 for the foundation and auth b2 test candidates;
- lower iOS runtime compatibility (14.x–16.x) and iPad runtime remain unverified and must not be inferred from the deployment target alone;
- any future dependency/API/build change that raises iOS 14.0 must be justified and documented.

## Known issues / constraints

- Bundle ID is accepted for the foundation but not yet Frozen as a permanent long-lived installation identity.
- There is no unit/UI test target yet; current automated validation is Xcode Release compilation, app bundle validation, IPA packaging/inspection and artifact upload.
- Runtime validation currently covers iPhone / iOS 17.0; lower OS versions and iPad are not yet tested.
- Embedded Google web login is verified for b2, but authenticated session persistence, account/session ownership and native session consumption remain unverified.
- ChatGPT private/internal protocol details can change and must be established from current evidence before implementation.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Historical experience is lower authority than the user's latest requirement, current source, and current runtime/protocol evidence.
