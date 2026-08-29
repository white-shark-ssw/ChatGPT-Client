# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-29 through exact b44 integrated-hybrid Runtime rejection and reopened Send architecture gate.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS. Stable product value remains the native shell/read/navigation experience. ChatGPT-account Send is constrained by TD-023/TD-024/TD-025: pure-native account-session Send is browser-challenge blocked; a user-visible official-Web Send surface is permitted, but b44 proved the full-page Native -> Web -> Native form is not acceptable final UX.
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
- **Visible Web owner**: `Authentication/AuthWebViewController.swift` owns login fallback and experimental TD-024 visible `hybridChat` Send surfaces. Hidden/shadow Web transport remains prohibited.
- **Production native conversation/list/read/recovery authority**: one `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only.
- **Settings owner**: `AppPreferences`; persisted display/interaction booleans only. Protocol diagnostics remain in Settings; b43's ordinary standalone hybrid-chat entry was removed in b44.
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

## Phase 9 security / transport evidence

- Exact b42 source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`.
- Runtime: PoW, Turnstile and `so` required, with non-empty PoW + Turnstile finalize submissions before successful Send.
- Pure-native/transient-auth ChatGPT-account Send therefore remains blocked.
- TD-024 permits a **visible** official ChatGPT Web Send surface while retaining the native shell; no solver/bypass/replay/hidden challenge WebView.

## b43 Runtime feasibility result

- Candidate `DEV-send-stream-0.1.0-b43`, source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.
- User ran requested iPhone/iOS17 sequence and reported **“基本上没什么问题”** for Web entry/re-entry, typing, visible Send, stream/rapid scrolling and native return.
- Web `+` -> picker observed ~100–200 ms and was not rejected as excessive.
- Web photo chooser filtered video assets. Public WKUIDelegate file-panel replacement is iOS18.4+, so iOS17 cannot fix this through that public WebKit hook.
- b43 established visible-Web feasibility/smoothness, not acceptable final standalone-Web product UX.

## b44 integrated hybrid trial — exact identity and Runtime

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.
- Exact product/config source `f1503cf7121512a84e5c55a3642181c17324d791`.
- Push Run / Job `33245105815` / `99081114295`, success.
- PR Run `33245107290`, success.
- Artifact `9712583513`; ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- IPA `ChatGPTClient-0.1.0-b44-dev-send-stream.ipa`; SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- Independent package inspection: Candidate b44, `0.1.0 (44)`, source `f1503cf71215`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.
- Product flow trial: Native detail -> `发送消息…` -> visible Web `/c/<conversation-id>` -> Send -> explicit `返回并同步` -> Native detail.
- Exact-device Runtime proved tested A/B native IDs mapped to corresponding Web conversations.
- Immediate `返回并同步`/Native Sync could show the just-sent user message while assistant output already visible in Web remained absent from Native; a later Sync after waiting could expose the answer.
- No stable readiness signal/delay was established. Do not add automatic polling/timer/retry to guess readiness.
- User explicitly rejected the b44 full-page Native -> Web -> Native UX because it duplicates conversation loading and leaves actual interaction fundamentally Web-driven.
- **b44 classification**: Code/CI/Artifact/package identity passed; route/mapping/reconciliation Runtime observations accepted; integrated full-page product UX rejected; Stable/Frozen No.

## Current Send architecture gate — TD-025

No b45 is allocated. `DEV-send-stream` is blocked pending an explicit product architecture choice:

1. **Existing-account compromise**: Native list/history/read/navigation + an **explicitly visible embedded official-Web composer/live-response panel** directly operated by the user. This may remove b44's full-page browser-like transition but does not make Send/stream fully Native.
2. **Truly Native supported API product**: separate officially supported API authentication/billing, then Native composer/stream/attachments. Do not claim this is the same ChatGPT subscription/session/history without explicit supported evidence.
3. **Defer ChatGPT-account Send** until a supported account transport exists that does not require browser-owned challenge output.

The user's proposed fully covered Web + Native text field forwarding into Web is not currently accepted: under current evidence it requires DOM/JS/input automation of a hidden/covered protected Web Send surface, which violates TD-023/TD-024/TD-025.

## Attachment boundary

- b43 Web `+` latency ~100–200 ms was acceptable in tested scope.
- Web photo chooser filtered videos.
- Public WebKit upload-panel replacement is iOS18.4+, not primary iOS17.
- Native iOS17 photo+video selection/upload requires separately evidenced native attachment upload/handoff; do not use private WebKit or DOM/file-input injection.

## Runtime / evidence boundaries

- Exact b38 Runtime remains Stable/merged for its recorded scope.
- b42 remains security/transport evidence, not native Send acceptance.
- b43 is visible-Web feasibility/smoothness evidence with recorded video-picker limitation.
- b44 is accepted only for its exact Runtime observations; its integrated product form is rejected.
- iOS17 does not prove lower iOS or iPad; non-personal workspace/account switch and native attachment handoff remain conditional/Unverified.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
