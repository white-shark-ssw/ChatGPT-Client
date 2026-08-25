# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

Default-branch planning/governance baseline at `DEV-app-foundation` start: `main@bd9727e7a20c48c88944eff8a0f5fd0d23925ff6`.

The product goal is an **iOS native ChatGPT client** distributed as an IPA for TrollStore. The intended user-device environment does not exceed iOS 17.0, while compatibility with lower iOS versions is preferred where practical.

The first real product implementation now exists on active branch `dev/app-foundation-20260826`; it is not yet an accepted runtime baseline because real-device installation/launch/export validation remains pending.

## Active foundation candidate

`DEV-app-foundation-0.1.0-b1` currently establishes:

- Swift 5 + UIKit application shell with no third-party dependencies;
- iOS 14.0 deployment target;
- repository-derived bundle ID `com.whitesharkssw.chatgptclient` (not Frozen as a permanent product/signing identity);
- in-app version/build/candidate/source-commit/runtime metadata;
- structured OSLog diagnostics plus bounded persistent JSONL history;
- trace/span correlation and safe error/status metadata;
- local secret-field filtering and exported identifier hashing/redaction;
- user-triggered diagnostic JSON export from Settings;
- reproducible `scripts/build_ipa.sh` packaging path;
- GitHub Actions macOS build/IPA artifact workflow.

GitHub Actions run `32876352123` passed on Xcode 16.4 for product/workflow head `89b29434e4d81486d395b8ddb093a031f6f919a7` and produced artifact ID `9574034381` for this candidate. This is **CI passed + Artifact produced**, not runtime proof.

## Durable development plan

The ordered implementation roadmap is recorded in `docs/project/DEVELOPMENT_PLAN.md`.

Current intended sequence:

1. `DEV-app-foundation` — **Active candidate**; create the real Xcode/iOS baseline, TrollStore-installable IPA path, build identity and safe diagnostics/logging foundation.
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

The user reports that a previous Web-based IPA successfully used ChatGPT web login and that their account uses **Continue with Google**. This remains historical evidence only. `DEV-app-foundation` intentionally does not implement authentication/session/protocol behavior.

Current Google OAuth guidance warns that authorization endpoints shown in embedded user-agents such as `WKWebView` can be rejected with `disallowed_useragent`. Therefore `DEV-auth-bootstrap` must reproduce current behavior on-device first and only choose an alternate supported browser/auth handoff if current evidence requires it.

## Diagnostics state

Diagnostics/logging is now implemented at Candidate level rather than only planned:

- app lifecycle and UI/settings actions can emit structured local events;
- async operations can use trace IDs and timing spans;
- persistent history is size/count bounded (2 MiB current file plus up to three rotated files);
- secret-like field names are redacted before local persistence;
- exported account/conversation/message/session/user/workspace identifiers are SHA-256 shortened hashes;
- Settings exposes sample-event generation and user-triggered JSON export;
- build/device/runtime metadata is included in exports.

Runtime/manual validation of persistence across launches, Settings interaction, share sheet export and actual redaction contents is still pending.

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
- any future dependency/API/build change that raises iOS 14.0 must be justified and documented;
- TrollStore install/launch is still a real-device gate, not inferred from IPA production.

## Known issues / constraints

- Real-device TrollStore installation, launch and diagnostics export for `DEV-app-foundation-0.1.0-b1` are not yet validated.
- Current IPA packaging disables Xcode code signing; actual TrollStore resign/install behavior must be verified on the user's device before declaring the packaging path Stable.
- Bundle ID is a foundation identity but not yet Frozen as a permanent long-lived installation identity.
- There is no unit/UI test target yet; current validation is Xcode Release compilation, app bundle validation, IPA packaging/inspection and artifact upload.
- Authentication, account/session ownership and ChatGPT protocol remain unimplemented/unverified.
- ChatGPT private/internal protocol details can change and must be established from current evidence before implementation.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Historical experience is lower authority than the user's latest requirement, current source, and current runtime/protocol evidence.
