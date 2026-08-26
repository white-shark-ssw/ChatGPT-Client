# Project Profile

## Initialization

**Initialized — 2026-08-25; product baseline refreshed 2026-08-26**

Bootstrap inspection completed against real repository state. Unsupported compatibility/protocol details remain `Unknown / Unverified`.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Project purpose**: Develop an iOS native ChatGPT client.
- **Product type**: Native iOS third-party ChatGPT client application.
- **Primary users/runtime**: iOS users. Intended user-device environment does not exceed iOS 17.0; lower compatibility is preferred where practical.

## Technology stack

- **Primary language(s)**: Swift 5.
- **Primary UI framework**: UIKit.
- **System frameworks**: UIKit, Foundation, WebKit, OSLog, CryptoKit.
- **Package/dependency manager(s)**: None; current product has no third-party dependencies.
- **Important manifests/configs**: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared Xcode scheme, `.github/workflows/ios-foundation.yml`.

## Repository structure and state owners

- **Main source root**: `ChatGPTClient/`.
- **Application entry point**: `ChatGPTClient/AppDelegate.swift`.
- **Application shell**: `RootViewController.swift`, `SettingsViewController.swift`.
- **Build/runtime metadata owner**: `ChatGPTClient/Support/AppBuildInfo.swift` plus Xcode build settings/Info.plist expansion.
- **Diagnostics owner**: `ChatGPTClient/Diagnostics/Diagnostics.swift` (`DiagnosticsLogger`, bounded store, sanitizer, exporter, user-triggered clear operation). Clearing uses the existing store and removes its current + rotated local files only.
- **Embedded login UI/navigation owner**: `ChatGPTClient/Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore`, accepted from real-device evidence.
- **Safe auth evidence/account-context owner**: `ChatGPTClient/Authentication/AuthSessionStore.swift`; copied WebKit auth context and `/api/auth/session` bearer are transient only. Native `/auth/login` remains historical route-specific evidence and is not a current account-context gate.
- **Account/workspace context owner**: accepted b6 in-memory context in `AuthSessionStore`. Current parser uses `account_ordering` + keyed `accounts` + nested `account.account_id` and is real-device verified for the tested account.
- **Protocol-read diagnostic owner**: `ChatGPTClient/Protocol/ProtocolReadProbe.swift` in active `DEV-protocol-read`. It is diagnostic-only, persists no conversation payload/model/repository, and does not become the production conversation state owner.
- **Production conversation/private protocol owner**: Not established yet; current list/detail runtime evidence must be accepted before `DEV-native-read-path` introduces production conversation ownership.
- **Test roots**: None yet.

## Build and validation

- **Primary packaging command**: `bash scripts/build_ipa.sh` on macOS with Xcode.
- **Underlying build**: `xcodebuild -project ChatGPTClient.xcodeproj -scheme ChatGPTClient -configuration Release -sdk iphoneos ... build` with signing disabled for TrollStore candidate packaging.
- **Lint/static checks**: No separate lint tool configured.
- **CI workflow**: `.github/workflows/ios-foundation.yml` on GitHub-hosted `macos-15`. Current protocol-read candidate b7 passed an exact-branch push build with Xcode 16.4 / iPhoneOS 18.5 SDK and `arm64-apple-ios14.0`.
- **Artifact/package output**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` plus `.sha256`.
- **Current validation level**: Foundation/auth/account context are runtime accepted on iPhone / iOS 17.0 through b6. `DEV-protocol-read-0.1.0-b7` has **Code written + CI passed + Artifact produced** for the current minimal list/detail diagnostic harness, but conversation-list/detail runtime behavior remains Unknown / Unverified until device testing.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in `ChatGPTClient.xcodeproj/project.pbxproj`.
- **Build number source**: `CURRENT_PROJECT_VERSION` in the same Xcode target settings.
- **Merged foundation version/build**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted web-login/persistence runtime evidence**: b2.
- **Historical native `/auth/login` success/failure evidence**: b3/b4.
- **Direct native session/accounts transport evidence**: b5/b6.
- **Merged auth/account-context runtime baseline**: `0.1.0 (6)` / `DEV-auth-bootstrap-0.1.0-b6`, exact product/workflow source `19c0cd22923d8c6f4c96e676258b31814d02a942`; PR #6 merged at `78f42a06e6254088e3b495cb4529e549a1d4717f`.
- **Active protocol-read candidate**: `0.1.0 (7)` / `DEV-protocol-read-0.1.0-b7`, exact product source `44a137b973e29e2a313e9114fdacb7727dccefb9`; authoritative push run `32938912018`; artifact ID `9595827498`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`; runtime pending.
- **Parallel test-candidate scheme**: `DEV-<work-slug>-<marketing-version>-b<build>`; identities must remain unique across Active tasks.
- **Artifact naming rule**: `ChatGPTClient-<marketing-version>-b<build>-<work-slug>.ipa`.
- **Current bundle identifier**: `com.whitesharkssw.chatgptclient`; accepted but not Frozen as a permanent signing/product contract.

## Runtime / deployment

- **Platform**: Native iOS application.
- **Current minimum deployment target**: iOS 14.0, verified in Xcode build settings and generated IPA metadata.
- **Compatibility ceiling**: intended user environment does not exceed iOS 17.0.
- **Deployment / installation**: IPA through TrollStore.
- **Device family build setting**: iPhone + iPad (`UIDeviceFamily` 1,2). Real-device validation currently covers iPhone only; iPad and iOS versions below 17.0 remain unverified.
- **Architecture verified in artifact**: arm64 Mach-O.

## Current source/candidate baselines

- Foundation merged to `main` by PR #5 at merge commit `9e7a06801715b0002d3e9a720d57041e830b776e`.
- Auth bootstrap merged to `main` by PR #6 at merge commit `78f42a06e6254088e3b495cb4529e549a1d4717f`.
- b2 source `809fa03e673afded87cb47fb755c998ab1b58e12` established Google login + WebKit persistence.
- b3 source `0fcf040012c0698d0e3ce1628fec9865237eba3b` established one successful native `/auth/login` result; b4 source `33ea1b96f755bdf21fdd7691a9f1084a6d624908` later showed native Cloudflare HTTP 403 while WebKit remained authenticated.
- b5 source `c09f981171b02dc8a4f0d8ada4624bd779c68c2f` established a successful direct session/accounts HTTP 200 path and exposed the old parser.
- b6 exact product/workflow source `19c0cd22923d8c6f4c96e676258b31814d02a942`; run `32934821144`; artifact ID `9594474567`; IPA SHA-256 `c7109f691c1de675ef55da1a08695c10663b62030853453ee2fafd01fb070c8b`.
- b7 exact product source `44a137b973e29e2a313e9114fdacb7727dccefb9`; push run `32938912018`; artifact ID `9595827498`; IPA `ChatGPTClient-0.1.0-b7-dev-protocol-read.ipa`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`; artifact ZIP digest `sha256:c1d851dc949a43587f94fffd34b35c233ff5f35a2c8eef3399d2e722a9f7833f`. Downloaded ZIP and IPA hashes were independently rechecked. Commits after `44a137...` currently modify project docs only and do not change the tested product/workflow code.

## Historical reference material

The previous-project history pack is experience/reference only. It is not the current source baseline and does not make historical endpoint names, request shapes, workarounds, diagnoses or framework choices current facts. See `docs/project/HISTORICAL_REFERENCE.md`.

## Evidence notes

- Runtime success on iOS 17.0 does not prove runtime compatibility on all systems down to the compiled iOS 14.0 minimum.
- Native `/auth/login` results are route/time-specific and not a durable prerequisite contract.
- Direct `/api/auth/session` can return HTTP 403 under observed challenge conditions; current code intentionally has no speculative automatic retry.
- b6 auth/account success does not prove conversation-list/detail/streaming behavior.
- b7 CI/artifact success proves build/package identity only. Conversation-list/detail protocol must still be established from current real-device evidence before becoming a production contract.

## Auto-refresh rule

Update this file proactively when project purpose, language/framework, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline changes.
