# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b54 Runtime and exact b55 Code/CI/Artifact/package verification.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS. Stable product value remains the native shell/read/navigation experience.
- **Primary distribution**: TrollStore IPA.
- **Primary tested runtime**: iPhone 15 Pro Max / iOS17.0; lower iOS compatibility preferred where practical.
- **Current Send constraint**: pure-native ChatGPT-account protected Send is blocked by exact b42 browser-challenge evidence. The separately billed/supported API-product architecture remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- **Current Send product gate**: full mobile-Web conversation rendering is not accepted as a daily-chat production dependency after exact-device long-conversation composer failure. b48-b55 are isolated diagnostic experiments for a Native surface over a Web protected-Send engine and do not change the durable hidden/shadow-Web production boundary.
- **Current reasoning/tool gate**: b53 directly identifies `assistant:reasoning_recap`, separate non-presentational `assistant:thoughts`, assistant code and tool messages. b54 materially identifies assistant tool invocation→tool-result shape and thoughts summary/status metadata, but its generic structure observer saturated at 32/overflow13 before deterministic recap coverage. Exact b55 is the current behavior-neutral Runtime Candidate with a separate bounded special-structure channel.

## Technology stack

- Swift 5 + UIKit.
- Foundation, WebKit, OSLog, CryptoKit.
- No third-party dependencies.
- Deployment target iOS14.0; current Artifact architecture arm64.
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

### Protected Send / full-Web ceiling

- b42: PoW, Turnstile and `so` required before successful protected Send; pure-native/transient-auth account Send remains blocked.
- b43/b44: shorter visible-Web interaction can work, but full-page Native→Web→Native product form rejected and immediate Native reconciliation can lag Web-visible assistant output.
- b47: long-answer existing conversation could repeatedly freeze mobile-Web composer before Send. Full existing-conversation Web rendering is therefore not a daily production dependency.

### Official continuation / Native parity

- b45: official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` returns HTTP200 SSE and can continue the same already-started response. Short background/lock survival evidence positive.
- b46/b47: Native duplicated-after-official-success Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.

### Native composer / Web Send-engine progression

- b48: Native composer successfully drove sequential official protected Sends; parser used wrong long-form patch names.
- b49: real incremental compact `o/p/v` delivery confirmed but incomplete.
- b50: contextual value-only continuation made established turns complete; fresh first turn still lost a middle section.
- b51: preserving active continuation across exact `title_generation` fixes the fresh-new-chat missing-middle failure; exact fresh long answer delivered 11,618 Native chars / 284 deltas and was visually complete.
- b52: final answer complete while visible reasoning beginning slightly truncated; root-nonexact/inactive-value theory rejected for that reproduction.

### b53 Runtime

- Candidate `DEV-send-stream-0.1.0-b53`, exact source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`, Artifact `9726996570`.
- User: visible reasoning beginning still truncated; final answer complete; Native tool-call presentation absent.
- Service stream directly identified `assistant:reasoning_recap`, separate `assistant:thoughts`, `assistant:code`, and tool text/code/multimodal classes.
- Accepted: `reasoning_recap` is the direct candidate for explicitly user-visible reasoning; raw `thoughts` remains non-presentational; role/content type alone is insufficient for tool UI.

### b54 Runtime

- Candidate `DEV-send-stream-0.1.0-b54`, exact source `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`.
- Push `33296672444 / 99217423647`; PR `33296674388 / 99217428590` — success.
- Artifact `9727636043`; IPA SHA `d4b85cffe4db499252d0bc9a2c7c8ea582acf2b88f3d28eeb60e366ee471153b`.
- Exact Runtime matched build 54 / source `6a6903c7ad56` / Release / iPhone iOS17.0; HTTP200 SSE, terminal true.
- Tool invocation/result grammar materially identified: assistant code recipients `api_tool.*`, tool-result author names/recipient/content containers, plus `invoked_plugin` / `invoked_resource` where present.
- `assistant:thoughts` structure includes `chunks,content,finished,summary` object keys and metadata `can_save:false`, `reasoning_status:is_reasoning`, `tool_summary_type:github`, `inline_cot_expandable_content`, `tool_icons`.
- Generic structure set saturated at 32 with overflow13; absent `reasoning_recap` cannot be treated as protocol absence. b54 is a partial Runtime pass.
- Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b54-runtime.md`.

### Exact current b55 Candidate

- Candidate `DEV-send-stream-0.1.0-b55`, `0.1.0 (55)`.
- Exact product/config source `aae856069b461e12dc11ee7d2d450a40ca621d21`.
- Push Run / Job `33299965737 / 99226125826` — success.
- PR Run / Job `33299967033 / 99226129092` — success.
- Artifact `9728606514`; ZIP `sha256:fda8dfb16e3d734b9e0f0d55c4e49c0f6cd656e4ec228b13dab3cae108c0a7e3`.
- IPA SHA `f5106949814b44c6c97e2f519ff181498f6a75ff7b9bf9edf0dc0bb0bd299ad1`.
- Package: Release / `0.1.0 (55)` / Candidate b55 / source `aae856069b46` / iOS14 / `[1,2]` / arm64.
- b55 preserves all b54 response behavior and adds only an independent bounded special-message structure channel for reasoning_recap/thoughts/assistant-code/tool messages plus count/overflow metrics.
- Runtime/manual: Pending. b55 permanently reserved after Artifact emission.

## Current next Candidate boundary

b39-b55 emitted identities are permanently reserved. Any product-code correction after b55 requires b56+.

Do not allocate b56 unless exact b55 Runtime identifies a concrete display boundary or another specific smallest defect. The next gate is one focused b55 reasoning/tool reproduction with diagnostics export; b55 itself is behavior-neutral.

## Reasoning/tool presentation boundary

`DEV-send-stream` owns explicitly user-visible reasoning, reasoning→final transition and follow-tail per `SEND_STREAM_PREFLIGHT.md`. Requested reasoning collapse/expand and tap-driven tool-call detail presentation remain in current scope.

Only explicitly user-visible service reasoning/status/tool data may be shown. Hidden chain-of-thought/internal tool/system nodes, raw `assistant:thoughts`, raw tool arguments and raw tool output must never be exposed merely because structural diagnostics exist.

b55 Runtime is the current evidence gate before implementing these presentations.

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
- b51 Runtime confirms the fresh-new-chat title-generation fix.
- b52 Runtime confirms final-answer capture for the tested tool-style response while visible reasoning begins incompletely.
- b53 Runtime identifies explicit reasoning/tool message classes.
- b54 Runtime materially identifies tool call/result grammar but leaves recap display-container gate inconclusive due diagnostic saturation.
- b55 Code/CI/Artifact/package is verified and Runtime pending.
- Full-Web long-conversation composer viability failed on the primary device/workload reported at b47.
- Native production response ownership/reasoning/follow-tail/background lifecycle, existing-conversation pre-React history virtualization, 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified where not explicitly tested.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
