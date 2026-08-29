# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b51 Runtime and exact b52 Code/CI/Artifact/package verification.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS. Stable product value remains the native shell/read/navigation experience.
- **Primary distribution**: TrollStore IPA.
- **Primary tested runtime**: iPhone 15 Pro Max / iOS17.0; lower iOS compatibility preferred where practical.
- **Current Send constraint**: pure-native ChatGPT-account protected Send is blocked by exact b42 browser-challenge evidence. The user rejects the separately billed/supported API-product architecture and does not want primary-account Sub2API/Codex-subscription Runtime because of account-safety risk.
- **Current Send product gate**: full mobile-Web conversation rendering is not accepted as a daily-chat production dependency after exact-device long-conversation composer failure. b48-b52 are isolated diagnostic experiments for a Native surface over a Web protected-Send engine; their existence does not change the durable hidden/shadow-Web production boundary.

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
- **Visible Web owner**: `Authentication/AuthWebViewController.swift` and diagnostic Web controllers.
- **Native Web Send-engine diagnostic owner**: `NativeWebSendEngineProbeViewController`; diagnostic-only, does not mutate production `ConversationRepository`, and remains outside durable production acceptance.
- **Production native conversation/list/read/recovery/future accepted response authority**: one `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only.
- **Settings owner**: `AppPreferences`; persisted display/interaction booleans only. Protocol diagnostics are surfaced from Settings.
- **Conversation presentation owner**: `ConversationDetailViewController`.
- **Message presentation geometry**: `ConversationMessagePresentationProjection` + `ConversationMessageCell`; Stable b37/b38 deterministic bounded geometry.
- **Diagnostics**: `DiagnosticsLogger`; privacy-safe structural/aggregate evidence only.
- **Official continuation observation owner**: `ProtocolHandoffProbeViewController`; diagnostic-only.
- **Native continuation parity diagnostic owner**: `NativeResumeParityProbeViewController`; diagnostic-only.
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

Latest repository-wide governance is current `main@1ac202c972f2dee6945fe8d0688df8e10f5d462c` root `AGENTS.md` plus `docs/project/START_HERE.md`. The feature branch originated before rules-only `main` commits; final synchronization remains required before merge. No current product/state-owner conflict with those target-only rule commits is established.

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

- b43 exact source `f602d68...`, Artifact `9711364573`: visible Web entry/re-entry, typing, Send and stream scrolling broadly smooth in tested shorter scope; Web `+` ~100–200ms; photo chooser filtered videos. Standalone Web-chat form not accepted.
- b44 exact source `f1503cf...`, Artifact `9712583513`: tested `/c/<id>` mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; full-page Native -> Web -> Native form product-rejected. No timer/poll/retry patch is accepted.
- b47 exact-device user Runtime narrows b43: an older conversation with only about three rounds but long answers repeatedly froze when trying to bring up/use the mobile-Web composer. The user had to switch to a new conversation for protocol testing. Internal freeze cause remains Unknown.

### b45 official no-resend continuation

- Candidate `DEV-send-stream-0.1.0-b45`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868`.
- Uninterrupted Send uses original `/backend-api/f/conversation` SSE through terminal.
- Clean default-primary new-chat response survived/buffered repeated active-response background/lock including ~126s continuous without resend/refresh.
- Forced interruption proved official `POST /backend-api/f/conversation/resume` with JSON body `{conversation_id: string, offset: number}` and HTTP200 `text/event-stream` continuation that can continue the same response to `[DONE]` without a second Send.

### b46/b47 Native duplicated resume parity

- b46 exact source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`, legitimate Artifact `9715903443`: official offset 18 resume 200 SSE; one Native same-body Cookie+Bearer-only duplicate 404 JSON/116 bytes/0 SSE; later official offset 54 200 SSE.
- b47 exact source `21028bbff7982abeb42f130c56fcb21e6ef44d7a`, legitimate Artifact `9716878034`: official offset 23 200 SSE; one Native duplicate 404 JSON, ~707ms, 116 bytes, 0 SSE; rejection shape `{detail:{code:string,message:string}}`; later official offset 74 200 SSE.
- Accepted classification: official no-resend resume Runtime Confirmed; Native Cookie+Bearer-only **duplicated-after-official-success** resume Runtime Rejected. Missing browser context vs second-consumer/cursor ownership remains Unknown / Unverified.

### b48-b50 Native-composer/Web-Send-engine diagnostic evidence

- b48 exact source `6ccba03cefaa32a1186f1f468c3e696ed9457699`, Artifact `9718885751`: Native composer successfully drove official protected Send for two sequential turns. Parser used wrong long-form patch field names and captured zero assistant text to Native; Runtime completed/superseded.
- b49 exact source `20fb8f3f400200965acb868aeb8a7504b9bfb91f`, Artifact `9719418761`: real incremental Native delivery confirmed, but only two short explicit compact `o/p/v` text fragments per turn were captured; complete-response interception rejected.
- b50 exact source `837d5feeff05d198785f884ccf9cc4c1f71412ec`, Artifact `9719942650`: three sequential Native submissions all reached official protected Send and terminal. Turn 2 captured 191 Native characters across 10 deltas; turn 3 captured 671 characters across 31 deltas; user reported both complete and visibly incremental/effectively character-by-character. Web assistant text remained 45 characters in terminal metrics. Fresh new-chat turn 1 captured only 35 Native characters and lost a middle section, so b50 is a partial Runtime pass rather than complete parser acceptance.

Detailed b50 evidence: `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`.

### b51 exact Runtime result

- Candidate `DEV-send-stream-0.1.0-b51`, `0.1.0 (51)`.
- Exact product/config source `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`.
- Push Run / Job `33271794573` / `99151433241`; PR Run / Job `33271796259` / `99151437702` — success.
- Artifact `9720327648`; IPA SHA `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`.
- Fresh first long response: 11,618 Native chars / 284 deltas / `titleGenerationWhileContinuationCount=1`, terminal true, Web assistant text 0; user visually judged it complete.
- Second long response was also visually complete.
- Third GitHub/project-progress response reached terminal but user observed a small **leading truncation**; title-generation count was 0.
- Accepted: b51 Runtime confirms the narrow `title_generation` continuation-preserve rule fixes the b50 fresh-new-chat missing-middle defect. Complete parser coverage remains unaccepted because the separate tool-style leading gap remains.
- Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b51-runtime.md`.

### b52 current exact Candidate

- Candidate `DEV-send-stream-0.1.0-b52`, `0.1.0 (52)`.
- Exact product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`.
- Push Run / Job `33276080936` / `99162937523` — success.
- PR Run / Job `33276082767` / `99162942750` — success.
- Artifact `9721532867`; ZIP digest `sha256:2ffd7e46e80019d3c4e8d6cbfa5c91dffa2a5f88222a30d5c4d5fb1e4fd752fc`.
- IPA SHA `a3de5c6eb4f7b790764fcd0adc4c98108fb550e7cedb3d6b02b931d266946b23`.
- Package: Release / `0.1.0 (52)` / Candidate b52 / source `5c0690ce062e` / iOS14 / `[1,2]` / arm64.
- b52 keeps b51 parser/output semantics and adds only structural aggregate counters for exact/non-exact/nested assistant text patches, inactive value-only strings, continuation resets and first inactive-gap context.
- Runtime/manual: Pending. b52 is permanently reserved after Artifact emission.

## Current next Candidate boundary

b39-b52 emitted identities are permanently reserved. Any product-code correction after b52 requires `DEV-send-stream-0.1.0-b53`, `0.1.0 (53)` or later.

Do not allocate b53 unless exact b52 Runtime identifies a concrete structural gap class. The next gate is one focused GitHub/tool-style b52 reproduction with diagnostics export; b52 itself must remain behavior-neutral.

## Attachment boundary

- b43 Web `+` latency ~100–200ms accepted for its tested scope.
- Web photo chooser filtered videos.
- Public WebKit upload-panel replacement is iOS18.4+, not primary iOS17.
- Native iOS17 photo+video selection/upload requires separately evidenced native attachment upload/handoff; do not use private WebKit or DOM/file-input injection.

## Runtime / evidence boundaries

- b38 Runtime remains Stable/merged for recorded scope.
- b42 remains security/transport evidence, not native Send acceptance.
- b45 official no-resend resume is Runtime Confirmed.
- b46/b47 Native duplicated Cookie+Bearer-only resume are Runtime Rejected for their exact attempts.
- b50 materially confirms the diagnostic Native composer -> official Web Send -> pre-React SSE interception -> Native incremental text path on established turns.
- b51 Runtime confirms the fresh-new-chat title-generation fix but exposes a separate tool/GitHub-style leading truncation, so complete parser coverage is not accepted.
- b52 is Code/CI/Artifact/package verified, behavior-neutral, and Runtime pending.
- Full-Web long-conversation composer viability failed on the primary device/workload reported at b47.
- Native production response ownership/reasoning/follow-tail/background lifecycle, existing-conversation pre-React history virtualization, 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified where not explicitly tested.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.