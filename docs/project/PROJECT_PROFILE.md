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
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore`, accepted from b2/b4 real-device evidence.
- **Safe auth evidence/account-context owner**: `ChatGPTClient/Authentication/AuthSessionStore.swift`; copied WebKit auth context is transient only. The b3 native `/auth/login` probe remains historical route-specific evidence and is not a current account-context gate.
- **Account/workspace context owner**: b5 Candidate in-memory context in `AuthSessionStore`; direct `/api/auth/session` runtime result pending.
- **Test roots**: None yet.

## Build and validation

- **Primary packaging command**: `bash scripts/build_ipa.sh` on macOS with Xcode.
- **Underlying build**: `xcodebuild -project ChatGPTClient.xcodeproj -scheme ChatGPTClient -configuration Release -sdk iphoneos ... build` with signing disabled for TrollStore candidate packaging.
- **Lint/static checks**: No separate lint tool configured.
- **CI workflow**: `.github/workflows/ios-foundation.yml` on GitHub-hosted `macos-15`; current b5 push run uses Xcode 16.4 / iPhoneOS 18.5 SDK and compiles for `arm64-apple-ios14.0`.
- **Artifact/package output**: `build/artifacts/ChatGPTClient-<version>-b<build>-<work-slug>.ipa` plus `.sha256`.
- **Current validation level**: foundation and embedded login/persistence are runtime accepted on iPhone / iOS 17.0. b3/b4 provide route-specific native `/auth/login` evidence showing both HTTP 200 and later Cloudflare HTTP 403 conditions. b5 direct account-context path is Code written + CI passed + Artifact produced, runtime pending. Conversation/private protocol remains Unknown / Unverified.

## Versioning and candidate identity

- **Version source**: `MARKETING_VERSION` in `ChatGPTClient.xcodeproj/project.pbxproj`.
- **Build number source**: `CURRENT_PROJECT_VERSION` in the same Xcode target settings.
- **Merged main foundation version/build**: `0.1.0 (1)` / `DEV-app-foundation-0.1.0-b1`.
- **Accepted web-login/persistence runtime evidence**: b2.
- **Historical native `/auth/login` success evidence**: b3.
- **Failed native `/auth/login` gate evidence**: b4, exact source `33ea1b96f755bdf21fdd7691a9f1084a6d624908`.
- **Current active account-context test candidate**: `0.1.0 (5)` / `DEV-auth-bootstrap-0.1.0-b5`, exact source `c09f981171b02dc8a4f0d8ada4624bd779c68c2f`.
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
- b3 runtime source `0fcf040012c0698d0e3ce1628fec9865237eba3b` established one successful native `/auth/login` result.
- b4 runtime source `33ea1b96f755bdf21fdd7691a9f1084a6d624908`, artifact ID `9579720453`, showed authenticated WebKit but native `/auth/login` Cloudflare HTTP 403; account-context probe was not reached.
- b5 exact product/workflow source `c09f981171b02dc8a4f0d8ada4624bd779c68c2f`; authoritative push run `32932389742`; artifact ID `9593649485`; IPA `ChatGPTClient-0.1.0-b5-dev-auth-bootstrap.ipa`; IPA SHA-256 `d9a22635cc6ac05d2ba09a0a627eaa74d38d1a690b5e9affe2f318d2aa204f15`; artifact ZIP digest `sha256:4ad6e95d4e30981aa63bb8bd401c0d4cd9acdddabbf83fab27b1f6fe54307066`.
- Downloaded b5 artifact was locally extracted and its embedded version/build/candidate/source/deployment identity and IPA SHA-256 were rechecked successfully.

## Historical reference material

The previous-project history pack is experience/reference only. It is not the current source baseline and does not make historical endpoint names, request shapes, workarounds, diagnoses or framework choices current facts. See `docs/project/HISTORICAL_REFERENCE.md`.

## Evidence notes

- Runtime success on iOS 17.0 does not prove runtime compatibility on all systems down to the compiled iOS 14.0 minimum.
- b3 native `/auth/login` acceptance does not prove durable behavior; b4 demonstrates Cloudflare can change the result while WebKit remains authenticated.
- b4 did not execute `/api/auth/session`; it must not be labeled an account-context endpoint failure.
- b5 CI/artifact success does not prove direct account/session runtime behavior; exact b5 device evidence is required.
- Current protocol/account requests must be established from current evidence before implementation.

## Auto-refresh rule

Update this file proactively when project purpose, language/framework, build/test commands, version scheme, deployment/runtime, repository structure, major state ownership or accepted baseline changes.
