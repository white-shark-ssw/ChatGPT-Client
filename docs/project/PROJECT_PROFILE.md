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
- **Diagnostics owner**: `ChatGPTClient/Diagnostics/Diagnostics.swift` (`DiagnosticsLogger`, bounded store, sanitizer, exporter).
- **Embedded login UI/navigation owner**: `ChatGPTClient/Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore`, accepted from b2 real-device persistence evidence.
- **Safe auth evidence/native bridge owner**: `ChatGPTClient/Authentication/AuthSessionStore.swift`; b3 runtime evidence accepts its transient WebKit-cookie -> ephemeral `URLSession` bridge for the tested `/auth/login` route. It does not persist copied auth secrets.
- **Account/workspace context owner**: b4 Candidate implementation in `AuthSessionStore`; in-memory only and not yet runtime accepted.
- **Test roots**: None yet.

## Build and validation

- **Primary packaging command**: `bash scripts/build_ipa.sh` on macOS with Xcode.
- **Underlying build**: `xcodebuild -project ChatGPTClient.xcodeproj -scheme ChatGPTClient -configuration Release -sdk iphoneos ... build` with signing disabled for TrollStore candidate packaging.
- **Lint/static checks**: No separate lint tool configured.
- **CI workflow**: `.github/workflows/ios-foundation.yml` on GitHub-hosted `macos-15`; current valid b4 push run used Xcode 16.4 / iPhoneOS 18.5 SDK and compiled for `arm64-apple-ios14.0`.
- **Artifact/package output**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` plus `.sha256`.
- **Current validation level**: foundation, embedded login/persistence and b3 transient native auth bridge are runtime accepted on iPhone / iOS 17.0 for their documented scopes. b4 account context is Code written + CI passed + Artifact produced, runtime pending. Conversation/private protocol remains Unknown / Unverified.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in `ChatGPTClient.xcodeproj/project.pbxproj`.
- **Build number source**: `CURRENT_PROJECT_VERSION` in the same Xcode target settings.
- **Merged main foundation version/build**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted auth runtime evidence version/build**: `0.1.0 (3)` / `DEV-auth-bootstrap-0.1.0-b3`.
- **Current active account-context test candidate**: `0.1.0 (4)` / `DEV-auth-bootstrap-0.1.0-b4`, valid runtime-test source `33ea1b96f755bdf21fdd7691a9f1084a6d624908`.
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
- Foundation accepted runtime source `89b29434e4d81486d395b8ddb093a031f6f919a7`; artifact ID `9574034381`.
- Auth work is on `dev/auth-bootstrap-20260826` / draft PR #6.
- b2 runtime source `809fa03e673afded87cb47fb755c998ab1b58e12` established Google login + WebKit persistence.
- b3 exact runtime product source `0fcf040012c0698d0e3ce1628fec9865237eba3b`; authoritative push run `32889095904`; artifact ID `9578766019`; IPA SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`. Real-device diagnostics prove `session.nativeState=verified` with final `chatgpt.com` HTTP 200 for the transient native `/auth/login` probe.
- b4 valid runtime-test source `33ea1b96f755bdf21fdd7691a9f1084a6d624908`; authoritative push run `32891798350`; artifact ID `9579720453`; IPA `ChatGPTClient-0.1.0-b4-dev-auth-bootstrap.ipa`; IPA SHA-256 `f918b1f5762458e55e89a1f0d23e5c2bf46be11d7f4599c692627a07043dab03`. Runtime account-context result remains pending.
- Earlier b4 artifact ID `9579620441` is explicitly rejected because its embedded candidate identity remained b3 despite a b4 filename/artifact name.

## Historical reference material

The previous-project history pack is experience/reference only. It is not the current source baseline and does not make historical endpoint names, request shapes, workarounds, diagnoses or framework choices current facts. See `docs/project/HISTORICAL_REFERENCE.md`.

## Evidence notes

- Runtime success on iOS 17.0 does not prove runtime compatibility on all systems down to the compiled iOS 14.0 minimum.
- b3 native `/auth/login` acceptance does not prove current account/workspace or conversation private-protocol behavior.
- b4 account-context CI/artifact success does not prove account/workspace runtime behavior; exact b4 device evidence is required.
- Current protocol/account requests must be established from current evidence before implementation.

## Auto-refresh rule

Update this file proactively when project purpose, language/framework, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline changes.
