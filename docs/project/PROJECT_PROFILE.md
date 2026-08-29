# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-29 through exact b47 Runtime and the long-conversation full-Web composer viability failure.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS. Stable product value remains the native shell/read/navigation experience.
- **Primary distribution**: TrollStore IPA.
- **Primary tested runtime**: iPhone 15 Pro Max / iOS17.0; lower iOS compatibility preferred where practical.
- **Current Send constraint**: pure-native ChatGPT-account protected Send is blocked by exact b42 browser-challenge evidence. The user rejects the separately billed/supported API-product architecture.
- **Current Send product gate**: visible official Web is security-permitted for protected Send, but exact b47 user Runtime now proves that requiring the real full mobile-Web conversation can become unusable on a long-answer conversation before Send occurs. The previous full-Web-conversation-per-Send architecture is therefore not accepted for further production integration without a new architecture decision.

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

- b43 exact source `f602d68...`, Artifact `9711364573`: visible Web entry/re-entry, typing, Send and stream scrolling broadly smooth in tested shorter scope; Web `+` ~100–200ms; photo chooser filtered videos. Standalone Web-chat form not accepted.
- b44 exact source `f1503cf...`, Artifact `9712583513`: tested `/c/<id>` mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; full-page Native -> Web -> Native form product-rejected. No timer/poll/retry patch is accepted.
- b47 exact-device user Runtime narrows b43: an older conversation with only about three rounds but long answers repeatedly froze when trying to bring up/use the mobile-Web composer. The user had to switch to a new conversation for the b47 protocol test. Internal freeze cause is Unknown because the exported diagnostics cover the replacement run, not the failed long-conversation attempt.

### b45 official no-resend continuation

- Candidate `DEV-send-stream-0.1.0-b45`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868`.
- Uninterrupted Send uses original `/backend-api/f/conversation` SSE through terminal.
- Clean default-primary new-chat response survived/buffered repeated active-response background/lock including ~126s continuous without resend/refresh.
- Forced interruption proved official `POST /backend-api/f/conversation/resume` with JSON body `{conversation_id: string, offset: number}` and HTTP200 `text/event-stream` continuation that can continue the same response to `[DONE]` without a second Send.

### b46 Native duplicated resume parity

- Candidate `DEV-send-stream-0.1.0-b46`, exact source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`, legitimate Artifact `9715903443`, IPA SHA `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`.
- Official offset 18 resume returned HTTP200 SSE.
- Native same-body request using only WebKit-derived transient cookie + bearer returned **HTTP404 `application/json`, 116 bytes, 0 SSE frames**.
- Later official offset 54 resume again returned HTTP200 SSE.
- Accepted classification: official no-resend resume Runtime Confirmed; Native Cookie+Bearer-only **duplicated-after-official-success** resume Runtime Rejected. Missing request context vs cursor/consumer ownership remains Unknown / Unverified.

### b47 rejection classification / product viability

- Candidate `DEV-send-stream-0.1.0-b47`, exact source `21028bbff7982abeb42f130c56fcb21e6ef44d7a`, legitimate Artifact `9716878034`, IPA SHA `49d1bd4886310f7761883784f73fc5532fe1a9532773619f0796cd7aab816909`.
- Push/PR CI passed; package identity verified as Release / `0.1.0 (47)` / iOS14 / arm64.
- Official offset 23 resume returned HTTP200 SSE after a transport-error retry; Native same-body duplicated request again returned HTTP404 JSON, ~707ms, 116 bytes, 0 SSE frames.
- Rejection JSON structure: `{"detail":{"code":"string","message":"string"}}`.
- Later official offset 74 resume returned HTTP200 SSE.
- Successful official request header-name set was much richer than Native: ordinary auth plus multiple `oai-*`, `x-oai-*`, `x-openai-*` and `x-conduit-token` names. This proves a structural difference only; it does not identify required values/headers.
- `safeErrorTokens` was redacted by the generic diagnostics sanitizer because the field key contains `token`, so safe code/type/status values were not preserved in export.
- Exact-device long-conversation visible-Web composer viability failed before Send, creating a P0 architecture gate.

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b47-runtime.md`.

## Current next Candidate boundary

b39-b47 emitted identities are permanently reserved. Any changed product code requires `DEV-send-stream-0.1.0-b48`, `0.1.0 (48)` or later.

**No b48 is currently allocated.** Do not allocate it merely to rename the diagnostic field or chase resume headers while the full-Web conversation Send dependency itself is under a Human Architecture Gate.

Evidence-backed architecture questions now precede further product code:

- whether an official supported lightweight visible send-only Web surface exists without full conversation-history rendering;
- whether another legitimate account-compatible protected-Send boundary can avoid the full mobile-Web conversation without hidden/shadow DOM automation or challenge bypass;
- otherwise whether visible Web must remain diagnostic/fallback only.

## Attachment boundary

- b43 Web `+` latency ~100–200ms accepted for its tested scope.
- Web photo chooser filtered videos.
- Public WebKit upload-panel replacement is iOS18.4+, not primary iOS17.
- Native iOS17 photo+video selection/upload requires separately evidenced native attachment upload/handoff; do not use private WebKit or DOM/file-input injection.

## Runtime / evidence boundaries

- b38 Runtime remains Stable/merged for recorded scope.
- b42 remains security/transport evidence, not native Send acceptance.
- b45 official no-resend resume is Runtime Confirmed.
- b46 and b47 Native duplicated Cookie+Bearer-only resume are Runtime Rejected with HTTP404 JSON for their exact recorded attempts.
- full-Web long-conversation composer viability failed on the primary exact device/workload reported at b47.
- Native first/exclusive resume, required browser/client header subset, lightweight official send-only Web surface, incremental Native streaming/reasoning/follow-tail/background ownership, 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified where not explicitly tested.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.