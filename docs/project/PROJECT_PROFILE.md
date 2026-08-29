# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-29 through exact b45 first realtime-handoff Runtime capture.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS. Stable product value remains the native shell/read/navigation experience.
- **Primary distribution**: TrollStore IPA.
- **Primary tested runtime**: iPhone 15 Pro Max / iOS17.0; lower iOS compatibility preferred where practical.
- **Current Send constraint**: pure-native ChatGPT-account Send is blocked by exact b42 browser-challenge evidence. The user rejects a separately billed/supported API-product architecture. User-visible official Web may perform the protected Send, but hidden/shadow Web automation remains prohibited.
- **Current Send target**: if current protocol supports it, reduce Web responsibility to user-visible legal Send initiation and let Native attach/resume/subscribe to the same already-started response without a second Send. Exact b45 first Runtime did not yet prove that continuation path.

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
- **Visible Web owner**: `Authentication/AuthWebViewController.swift` owns login fallback / permitted visible official-Web surfaces. Hidden/shadow Web transport remains prohibited.
- **Production native conversation/list/read/recovery authority**: one `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only.
- **Settings owner**: `AppPreferences`; persisted display/interaction booleans only. Protocol diagnostic entries are also surfaced from Settings.
- **Conversation presentation owner**: `ConversationDetailViewController` for viewport/history/round presentation.
- **Message presentation geometry**: `ConversationMessagePresentationProjection` + `ConversationMessageCell`; ephemeral deterministic bounded-chunk geometry accepted in b37/b38.
- **Diagnostics**: `DiagnosticsLogger`; privacy-safe structural evidence only.
- **Realtime handoff diagnostic owner**: `ProtocolHandoffProbeViewController`; observation-only, not production transport.
- **Background gate owner**: `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md` supplements `BACKGROUND_EXECUTION_PLAN.md`. If Native response ownership is proven, later background work should protect Native response lifecycle rather than WebKit.
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

## Stable Phase 8 identity

- Candidate `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- Exact tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Accepted architecture: bounded long-message chunks + deterministic row geometry/manual cell layout + continuous O(1)-target round animation.

## Phase 9 security / product evidence

### b42 security boundary

- Exact source `e8946e48a0b5ad86b402faf5eabba627e3393adf`; legitimate Artifact `9709824510`.
- Runtime: PoW, Turnstile and `so` required, with non-empty PoW + Turnstile finalize submissions before successful Send.
- Pure-native/transient-auth ChatGPT-account Send remains blocked.

### b43 visible-Web feasibility

- Exact source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`; Artifact `9711364573`; IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.
- Entry/re-entry, typing, visible Send, stream/rapid scrolling and native return were accepted as broadly smooth for the tested sequence.
- Web `+` -> picker ~100–200 ms was acceptable; Web photo chooser filtered videos.
- Standalone Web-chat form was not accepted as final product UX.

### b44 full-page hybrid ceiling

- Exact source `f1503cf7121512a84e5c55a3642181c17324d791`; Artifact `9712583513`; IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- Tested `/c/<id>` A/B mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; later Sync could expose it.
- No stable readiness signal/delay was established. The full-page Native -> Web -> Native interaction is product-rejected; do not patch it with polling/timer/retry.

### b45 realtime-handoff diagnostic

- Candidate `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`.
- Exact product/config source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- Push Run / Job `33248952646` / `99091176390`; PR Run / Job `33248954018` / `99091179731`; all successful.
- Artifact `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- IPA SHA `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.
- First exact-device Runtime captured early `resume_conversation_token`, original `/backend-api/f/conversation` fetch SSE ownership through `message_stream_complete` / `[DONE]`, and one `GET /conversation/{id}/stream_status` JSON `{status:string}` follow-up.
- No secondary response stream was observed during uninterrupted active responses. This does **not** prove no reconnect mechanism exists because the original stream was never interrupted while active.
- The second captured Send carried `conversation_mode.gizmo_id`; it is not a clean default-primary new-chat sample.
- Next evidence reuses exact b45 and intentionally backgrounds/locks while output is still streaming, then observes official-page reconnect behavior without refresh/resend.

## Attachment boundary

- b43 Web `+` latency ~100–200 ms was acceptable in tested scope.
- Web photo chooser filtered videos.
- Public WebKit upload-panel replacement is iOS18.4+, not primary iOS17.
- Native iOS17 photo+video selection/upload requires separately evidenced native attachment upload/handoff; do not use private WebKit or DOM/file-input injection.

## Runtime / evidence boundaries

- b38 Runtime remains Stable/merged for recorded scope.
- b42 remains security/transport evidence, not native Send acceptance.
- b43 is visible-Web feasibility evidence; b44 is accepted only for its exact mapping/eventual-read observations and its product form is rejected.
- b45 is accepted as a diagnostic instrument for the first captured structural path, but Native same-response continuation remains Unknown/Unverified.
- `resume_conversation_token` existence alone is not a Native API contract; `stream_status` is not a continuation stream in the captured path.
- main-app process survival does not prove WebKit/WebContent/network stream survival.
- iOS17 does not prove lower iOS or iPad; non-personal workspace/account switch and native attachment handoff remain conditional/Unverified.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
