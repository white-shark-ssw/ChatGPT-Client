# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

Default-branch planning/governance baseline at `DEV-app-foundation` start: `main@bd9727e7a20c48c88944eff8a0f5fd0d23925ff6`.

The product goal is an **iOS native ChatGPT client** distributed as an IPA for TrollStore. The intended user-device environment does not exceed iOS 17.0, while compatibility with lower iOS versions is preferred where practical.

The first real product foundation is now runtime-accepted as `DEV-app-foundation-0.1.0-b1`. It was built from product/workflow source `89b29434e4d81486d395b8ddb093a031f6f919a7`, installed and launched successfully through TrollStore on an iPhone running iOS 17.0, and its diagnostics/settings/persistence path was manually validated. PR #5 contains this foundation plus documentation updates and is the merge vehicle for the accepted baseline.

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

GitHub Actions run `32876352123` passed on Xcode 16.4 and produced artifact ID `9574034381`; later final material PR head `aa3233de...` passed run `32877096378`. The accepted IPA SHA-256 is `dcdefac9e508c5fd55c3c418fc0ea497c736f54fadc3b5e946300c5c1c032760`.

Runtime evidence from the user and exported diagnostic JSON confirms:

- TrollStore install and app launch succeeded with no reported problem;
- runtime identity is version `0.1.0 (1)`, candidate `DEV-app-foundation-0.1.0-b1`, Release, iPhone / iOS 17.0, source `89b29434e4d8`;
- Settings opened and sample diagnostic events were written;
- diagnostic JSON export completed successfully;
- a sample event written before a restart remained present after a second launch, proving persistent log history across relaunch for this candidate;
- no password/token/Cookie/Authorization/OAuth secret fields were observed in the supplied export.

## Durable development plan

The ordered implementation roadmap is recorded in `docs/project/DEVELOPMENT_PLAN.md`.

Current intended sequence:

1. `DEV-app-foundation` — **Accepted / completing merge**; real Xcode/iOS baseline, TrollStore IPA path, build identity and safe diagnostics/logging foundation are implemented and runtime-tested on iPhone / iOS 17.0.
2. `DEV-auth-bootstrap` — next serial phase: reproduce the user's current Google-based ChatGPT login on-device and establish real authenticated-session evidence.
3. `DEV-protocol-read` — establish current conversation-list/detail/account-context protocol evidence.
4. `DEV-native-read-path` — build native conversation navigation, authoritative conversation state and native message rendering.
5. `DEV-send-stream` — send text and process streaming replies with correct conversation/message ownership.
6. `DEV-long-conversation` — dedicated real-device long-conversation performance/stability work.
7. `DEV-attachments` — native files/photos/videos upload and attachment state.
8. Split daily-use conversation features into separate Work IDs as dependencies become stable.
9. Add advanced ChatGPT capabilities only after core chat is stable and current protocol evidence exists.

The strongly dependent core (`app foundation -> auth -> protocol read -> native read -> send/stream`) should normally be serialized rather than developed as independent parallel branches.

## Authentication evidence

The user reports that a previous Web-based IPA successfully used ChatGPT web login and that their account uses **Continue with Google**. This remains historical evidence only. `DEV-app-foundation` intentionally does not implement authentication/session/protocol behavior.

Current Google OAuth guidance warns that authorization endpoints shown in embedded user-agents such as `WKWebView` can be rejected with `disallowed_useragent`. Therefore `DEV-auth-bootstrap` must reproduce current behavior on-device first and only choose an alternate supported browser/auth handoff if current evidence requires it.

## Diagnostics state

Diagnostics/logging is now an accepted Stable foundation capability:

- app lifecycle and UI/settings actions emit structured local events;
- async operations can use trace IDs and timing spans;
- persistent history is size/count bounded (2 MiB current file plus up to three rotated files);
- secret-like field names are redacted before local persistence;
- exported account/conversation/message/session/user/workspace identifiers are SHA-256 shortened hashes;
- Settings exposes sample-event generation and user-triggered JSON export;
- build/device/runtime metadata is included in exports;
- real-device validation confirmed export and persistence across app relaunch on iPhone / iOS 17.0.

## Current architecture

Accepted architecture-level direction:

- native Swift/UIKit app baseline;
- `AppDelegate` owns foundation lifecycle/root setup;
- `AppBuildInfo` owns build/runtime identity presentation;
- `DiagnosticsLogger` / `DiagnosticsStore` / `DiagnosticsExporter` own diagnostics state and export;
- authentication/session establishment remains separate from native chat UI and is not implemented yet;
- future conversation/session/account/message-stream identities require explicit state owners;
- historical WebView/private-protocol details remain reference-only until revalidated.

## Compatibility direction

- current deployment target: iOS 14.0;
- build artifact is arm64 and declares iPhone+iPad device families;
- intended environment ceiling remains iOS 17.0;
- TrollStore installation/launch is verified on iPhone / iOS 17.0 for the accepted foundation candidate;
- lower iOS runtime compatibility (14.x–16.x) and iPad runtime remain unverified and must not be inferred from the deployment target alone;
- any future dependency/API/build change that raises iOS 14.0 must be justified and documented.

## Known issues / constraints

- Bundle ID is accepted for the foundation but not yet Frozen as a permanent long-lived installation identity.
- There is no unit/UI test target yet; current automated validation is Xcode Release compilation, app bundle validation, IPA packaging/inspection and artifact upload.
- Runtime validation currently covers iPhone / iOS 17.0; lower OS versions and iPad are not yet tested.
- Authentication, account/session ownership and ChatGPT protocol remain unimplemented/unverified.
- ChatGPT private/internal protocol details can change and must be established from current evidence before implementation.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Historical experience is lower authority than the user's latest requirement, current source, and current runtime/protocol evidence.
