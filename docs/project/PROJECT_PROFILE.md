# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-29 through exact b46 Native resume parity Runtime.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS. Stable product value remains the native shell/read/navigation experience.
- **Primary distribution**: TrollStore IPA.
- **Primary tested runtime**: iPhone 15 Pro Max / iOS17.0; lower iOS compatibility preferred where practical.
- **Current Send constraint**: pure-native ChatGPT-account protected Send is blocked by exact b42 browser-challenge evidence. The user rejects the separately billed/supported API-product architecture.
- **Current Send target**: user-visible official Web performs the protected Send; Native may own the already-started response only if no-resend continuation parity is directly evidenced. Hidden/shadow Web automation remains prohibited.

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
- **Visible Web owner**: `Authentication/AuthWebViewController.swift` and diagnostic visible-Web controllers. Hidden/shadow protected Web Send remains prohibited.
- **Production native conversation/list/read/recovery/future accepted response authority**: one `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only.
- **Settings owner**: `AppPreferences`; persisted display/interaction booleans only. Protocol diagnostics are surfaced from Settings.
- **Conversation presentation owner**: `ConversationDetailViewController`.
- **Message presentation geometry**: `ConversationMessagePresentationProjection` + `ConversationMessageCell`; Stable b37/b38 deterministic bounded geometry.
- **Diagnostics**: `DiagnosticsLogger`; privacy-safe structural evidence only.
- **Official continuation observation owner**: `ProtocolHandoffProbeViewController`; diagnostic-only.
- **Native continuation parity diagnostic owner**: `NativeResumeParityProbeViewController`; diagnostic-only and must not mutate production `ConversationRepository` until parity is accepted.
- **Background planning owner**: `BACKGROUND_EXECUTION_PLAN.md`; response-owner dependent.
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

## Current repository-governance source

Latest repository-wide governance is current `main@1ac202c972f2dee6945fe8d0688df8e10f5d462c` root `AGENTS.md` plus `docs/project/START_HERE.md`. The current feature branch originated before three rules-only `main` commits, so final synchronization remains required before merge. Those target-only commits have no product/state-owner overlap with current Send diagnostics.

Current rules include autonomous continuation, rolling checkpoints, batched non-atomic GitHub recovery, same-conversation identity reuse and Full/Light Resume Guards.

## Stable / accepted merged baselines

- Foundation b1 Stable/merged.
- Auth/account b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic read b7 accepted/merged.
- Production native read b9 Stable/merged.
- Recovery b15 Stable/merged.
- Multi-conversation read state b21 Stable/merged; Frozen No.
- Conversation-list cache core b23 Stable/merged; Frozen No.
- **Conversation metadata/settings/round navigation b38 Stable/merged; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

## Stable Phase 8 identity

- Candidate `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- Exact tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Accepted architecture: bounded long-message chunks + deterministic row geometry/manual cell layout + continuous O(1)-target round animation.

## Phase 9 security / product evidence

### b42 protected-Send boundary

- Exact source `e8946e48a0b5ad86b402faf5eabba627e3393adf`; legitimate Artifact `9709824510`.
- Runtime: PoW, Turnstile and `so` required, with non-empty PoW + Turnstile finalize submissions before successful Send.
- Pure-native/transient-auth ChatGPT-account protected Send remains blocked.

### b43/b44 visible-Web product evidence

- b43 exact source `f602d68...`, Artifact `9711364573`: visible Web entry/re-entry, typing, Send and stream scrolling broadly smooth in tested scope; Web `+` ~100–200ms; photo chooser filtered videos. Standalone Web-chat form not accepted.
- b44 exact source `f1503cf...`, Artifact `9712583513`: tested `/c/<id>` mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; full-page Native -> Web -> Native form product-rejected. No timer/poll/retry patch is accepted.

### b45 official no-resend continuation

- Candidate `DEV-send-stream-0.1.0-b45`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868`.
- Uninterrupted Send uses original `/backend-api/f/conversation` SSE through terminal.
- Clean default-primary new-chat response survived/buffered repeated active-response background/lock intervals including ~126s continuous without resend/refresh.
- Forced interruption proved official `POST /backend-api/f/conversation/resume` with JSON body `{conversation_id: string, offset: number}` and HTTP200 `text/event-stream` continuation that can reach `[DONE]` without a second Send.
- Official resume header-name evidence included normal auth/client headers and `x-conduit-token`, but no Sentinel/Turnstile/PoW header names; header-name presence alone does not establish requirement.

### b46 Native duplicated resume parity

- Candidate `DEV-send-stream-0.1.0-b46`, exact source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`, legitimate Artifact `9715903443`, IPA SHA `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`.
- Official `/resume` with `offset=18` returned HTTP200 SSE after connectivity recovered.
- b46 then used the same in-memory conversation identity + offset exactly once through WebKit-derived transient cookie + bearer, without copied Conduit/OAI/browser/challenge header values.
- Auth/account context verified successfully, but Native `/resume` returned **HTTP404 `application/json`, 116 bytes, 0 SSE frames**.
- Later official Web successfully resumed the same response again at progressed `offset=54` with HTTP200 SSE.
- Accepted classification: official no-resend resume Runtime Confirmed; Native cookie+bearer-only **duplicated-after-official-success** resume Runtime Rejected for this exact attempt. Missing request context vs cursor/consumer ownership remains Unknown / Unverified.

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`.

## Current next Candidate boundary

Any changed product code after emitted b46 Artifact requires `DEV-send-stream-0.1.0-b47`, `0.1.0 (47)` or later.

Authorized b47 scope is diagnostic-only:

- safe Native HTTP404 JSON structure/error-code classification;
- Native response header names;
- triggering official successful resume request/response header names;
- Native request header names actually set;
- one Native parity attempt only;
- no copied browser header values, no first-consumer takeover yet, no production repository mutation.

## Attachment boundary

- b43 Web `+` latency ~100–200ms accepted.
- Web photo chooser filtered videos.
- Public WebKit upload-panel replacement is iOS18.4+, not primary iOS17.
- Native iOS17 photo+video selection/upload requires separately evidenced native attachment upload/handoff; do not use private WebKit or DOM/file-input injection.

## Runtime / evidence boundaries

- b38 Runtime remains Stable/merged for recorded scope.
- b42 remains security/transport evidence, not native Send acceptance.
- b45 official no-resend resume is Runtime Confirmed.
- b46 Native duplicated cookie+bearer-only resume is Runtime Rejected with HTTP404 JSON for the exact recorded attempt.
- Native first/exclusive resume, required browser/client header subset, incremental Native streaming/reasoning/follow-tail/background ownership, 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified where not explicitly tested.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.