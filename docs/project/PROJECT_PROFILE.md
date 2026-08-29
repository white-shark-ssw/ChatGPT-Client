# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-29 through b43 exact-device hybrid feasibility Runtime and valid b44 integrated-send CI/Artifact.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS. ChatGPT-account Send uses TD-024's explicit **user-visible official-Web Send surface** because exact b42 proved the pure-native/transient-auth account-session path requires browser anti-abuse challenge output.
- **Primary distribution**: TrollStore IPA.
- **Primary tested runtime**: iPhone 15 Pro Max / iOS17.0; lower iOS compatibility preferred where practical.

## Technology stack

- Swift 5 + UIKit.
- Foundation, WebKit, OSLog, CryptoKit.
- No third-party dependencies.
- Deployment target iOS14.0; Artifact architecture arm64.
- Important config: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared Xcode scheme, `.github/workflows/ios-foundation.yml`.

## State owners / major modules

- **App lifecycle / native navigation owner**: `AppDelegate.swift`, `RootViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore` only.
- **Auth/account authority**: `Authentication/AuthSessionStore.swift`; native copied cookies/session bearer are transient only.
- **Visible Web owner**: `Authentication/AuthWebViewController.swift` owns login fallback and TD-024 visible `hybridChat` Send surface. Hidden/shadow Web transport remains prohibited.
- **Production native conversation/list/read/recovery authority**: one `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only.
- **Settings owner**: `AppPreferences`; persisted display/interaction booleans only. The b43 ordinary standalone hybrid-chat Settings entry was removed in b44; protocol diagnostics remain.
- **Conversation presentation owner**: `ConversationDetailViewController` for viewport/history/round presentation.
- **Message presentation geometry**: `ConversationMessagePresentationProjection` + `ConversationMessageCell`; ephemeral deterministic bounded-chunk geometry accepted in b37/b38.
- **Diagnostics**: `DiagnosticsLogger`; hybrid fields are privacy-safe route class / targetMatch / timing only.
- **Test roots**: no XCTest/UI-test target yet.

## Build / CI / package identity

- Packaging: `bash scripts/build_ipa.sh`.
- Build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- CI: GitHub Actions macOS15.
- Artifact scheme: `build/artifacts/ChatGPTClient-<version>-b<build>-dev-<work-slug>.ipa` + SHA-256 sidecar.
- Marketing version source: `MARKETING_VERSION`.
- Build source: `CURRENT_PROJECT_VERSION`.
- Candidate scheme: `DEV-<work-slug>-<marketing-version>-b<build>`.
- Expanded built `Info.plist` is package identity authority for version/build/Candidate/source marker.
- Once an Artifact identity is emitted it is permanently reserved; corrected product code must use a new Candidate/build.

## Stable / accepted merged baselines

- Foundation b1 Stable/merged.
- Auth/account b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic read b7 accepted/merged.
- Production native read b9 Stable/merged.
- Recovery b15 Stable/merged; PR #10.
- Multi-conversation read state b21 Stable/merged; PR #23; Frozen No.
- Conversation-list cache core b23 Stable/merged; PR #24; Frozen No.
- **Conversation metadata/settings/round navigation b38 Stable/merged; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

## Stable Phase 8 product identity

- Candidate `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- Exact tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- User exact-device result: **“没问题了”**.
- Accepted architecture: bounded long-message chunks + deterministic row geometry/manual cell layout + continuous O(1)-target round animation.

## Phase 9 security / architecture evidence

- Exact b42 source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`.
- Runtime: PoW, Turnstile and `so` required, with non-empty PoW + Turnstile finalize submissions before successful Send.
- Pure-native/transient-auth ChatGPT-account Send therefore remains blocked.
- TD-024 allows a **visible** official ChatGPT Web Send surface while retaining the native shell; no solver/bypass/replay/hidden challenge WebView.

## b43 Runtime feasibility result

- Candidate `DEV-send-stream-0.1.0-b43`, source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.
- User ran requested iPhone/iOS17 sequence and reported **“基本上没什么问题”** for Web entry/re-entry, typing, visible Send, stream/rapid scrolling and native return.
- Web `+` -> picker observed ~100–200 ms and was not rejected as excessive.
- Web photo chooser filtered video assets. Public WKUIDelegate file-panel replacement is iOS18.4+, so iOS17 cannot fix this through that public WebKit hook; b44 does not claim otherwise.

## Current Phase 9 test Candidate — b44

- **Candidate**: `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.
- **Exact product/config source**: `f1503cf7121512a84e5c55a3642181c17324d791`.
- **Push Run / Job**: `33245105815` / `99081114295`, success.
- **PR Run**: `33245107290`, success.
- **Artifact**: `9712583513`; ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- **IPA**: `ChatGPTClient-0.1.0-b44-dev-send-stream.ipa`; SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- **Independent package inspection**: Candidate b44, `0.1.0 (44)`, source `f1503cf71215`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.
- **Evidence level**: Code/CI/Artifact valid and identity-verified; exact-device Runtime pending; Stable/Frozen No.

## Current hybrid Send product boundary

- Native detail is primary and exposes Root-owned `发送消息…`.
- b44 visible Web trial is scoped to selected conversation using `https://chatgpt.com/c/<conversation-id>`; exact mapping requires Runtime acceptance before becoming durable contract.
- `返回并同步` invokes one existing Repository Sync; ordinary Back does not auto-Sync.
- No DOM mirroring, prompt injection, answer scraping, challenge/proof/token capture or native replay.
- `ConversationFeature.swift` and Stable b38 message geometry are unchanged by b44.
- Native iOS17 video attachment upload/handoff remains Unknown/Unverified and belongs evidence-backed attachment work.

## Runtime / evidence boundaries

- Exact b38 Runtime remains Stable/merged for its recorded scope.
- b42 remains security/transport evidence, not native Send acceptance.
- b43 is accepted only as visible-Web feasibility/smoothness evidence with the recorded video-picker limitation.
- b44 is currently Code/CI/Artifact evidence; integrated Runtime pending.
- iOS17 does not prove lower iOS or iPad; non-personal workspace/account switch and native attachment handoff remain conditional/Unverified.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
