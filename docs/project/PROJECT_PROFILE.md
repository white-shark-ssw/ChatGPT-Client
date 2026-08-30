# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b56 Runtime and exact b57 Code/CI/Artifact/package verification.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: native third-party ChatGPT client for iOS. Stable product value remains the native shell/read/navigation experience.
- **Primary distribution**: TrollStore IPA.
- **Primary tested runtime**: iPhone 15 Pro Max / iOS17.0; lower iOS compatibility preferred where practical.
- **Current Send constraint**: pure-native ChatGPT-account protected Send is blocked by exact b42 browser-challenge evidence. The separately billed/supported API-product architecture remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- **Current Send product gate**: full mobile-Web conversation rendering is not accepted as a daily-chat production dependency after exact-device long-conversation composer failure. b48-b57 are isolated diagnostic experiments for a Native surface over a Web protected-Send engine and do not change the durable hidden/shadow-Web production boundary.
- **Current reasoning gate**: b56 Runtime corrected the prior recap assumption. Exact `assistant:reasoning_recap` still provides a trustworthy `reasoning_status=reasoning_ended` phase marker, but its `content.content` was only a 7-character status/description in the tested turn and is **not** established as the real visible reasoning body. Raw `assistant:thoughts` remains separate/non-presentational. Exact b57 is the current testable Candidate: it splits the already-accepted visible assistant text stream before/after the exact reasoning-end marker and adds bounded text-free `assistant:text` start-shape diagnostics for the still-truncated reasoning prefix. Tool presentation remains separately evidence-gated.

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
- **Diagnostics**: `DiagnosticsLogger`; privacy-safe structural/aggregate evidence only. b57 records phase counts and direct ordinary-assistant-text field names/string lengths/array shapes/safe enums only; it does not persist the assistant text itself, prompt, raw reasoning, raw tool output, IDs, auth/proof/header values.
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
- b53: service stream directly identified `assistant:reasoning_recap`, separate `assistant:thoughts`, `assistant:code`, and tool text/code/multimodal classes. Raw `thoughts` remains non-presentational.
- b54: assistant tool invocation→tool-result grammar materially identified; generic structure observer saturated at 32/overflow13 before deterministic recap coverage.
- b55: independent special observer passed under saturation (generic 32/overflow14, special 7/overflow0) and deterministically captured exact `assistant:reasoning_recap / finished_successfully / recipient=all` with `reasoning_status=reasoning_ended`, `reasoning_recap_type=collapse`; separate `assistant:thoughts` remained non-presentational.

### b56 Runtime — recap presentation assumption corrected

- Candidate `DEV-send-stream-0.1.0-b56`, exact source `cec921030fd1af9f3853f35af52b661586b3a8ab`, Artifact `9728937100`, IPA SHA `da62776200ce94fef95326abaea3b980f65a5698df5dfe481bd34046e0f8dbe6`.
- Exact iPhone/iOS17 Runtime matched build 56 / source `cec921030fd1`; HTTP200 SSE / terminal true.
- Metrics: `frameCount=75`, Native 26 deltas / 504 chars, exact-root 4, nested 8, contextual strings 14 / 299 chars, inactive strings 0, generic 32/overflow16, special 8/overflow0, recap 7 chars.
- User-visible result: recap control worked, but expanded recap was only `思考了 40s` in this sample; the real visible reasoning body stayed mixed with the final answer and its beginning was still truncated.
- Accepted correction: exact recap **text is not established as the real reasoning body**. The exact recap event remains an explicit reasoning-end marker.
- Event ordering showed `assistant:text:in_progress` immediately before the first accepted `/message/content/parts/0` append, creating a concrete missing-prefix hypothesis; b56 did not log ordinary assistant-text content shape, so the initial field remains Unknown / Unverified and must not be guessed.
- Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b56-runtime.md`.

### Exact current b57 Candidate

- Candidate `DEV-send-stream-0.1.0-b57`, `0.1.0 (57)`.
- Exact product/config source `7074b1f85a0f239a5fd615f52196e1e28145523c`.
- Product tree `c402ce522e244cf63aa44b80a6d165b84342104c`.
- Push Run / Job `33302357908 / 99232731468` — success.
- PR Run / Job `33302359351 / 99232735067` — success.
- Artifact `9729360247`; ZIP `sha256:ae5a5532e2c30624907e9a2d61966090df4b8cc9ffa57f1b5725db8b61a8d275`.
- IPA SHA `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`.
- Package: Release / `0.1.0 (57)` / Candidate b57 / source `7074b1f85a0f` / iOS14 / `[1,2]` / arm64.
- b57 preserves prior accepted protected-Send and text-acceptance rules. Existing accepted text before exact reasoning-end marker is routed to a distinct Native `思考过程` region; accepted text after marker is routed to final answer. Exact recap text is not used as the reasoning body.
- If terminal arrives with no exact reasoning-end marker, provisional pre-marker text is promoted into the ordinary answer so non-reasoning turns are not permanently misclassified.
- b57 adds a separate bounded 12-entry ordinary `assistant:text` structure channel containing only direct field names, string lengths, array shapes/string-char counts, safe booleans/enums and before/after-marker phase. It deliberately does **not** extract an unproven initial text field.
- Runtime/manual: Pending. b57 permanently reserved after Artifact emission.

## Current next Candidate boundary

b39-b57 emitted identities are permanently reserved. Any product-code correction after b57 requires b58+.

Do not allocate b58 unless exact b57 Runtime identifies a concrete smallest next change. The current gate is one focused b57 reasoning/tool reproduction validating phase separation and exposing the first ordinary `assistant:text` content shape needed to classify the remaining leading-prefix defect.

## Reasoning/tool presentation boundary

`DEV-send-stream` owns explicitly user-visible reasoning, reasoning→final transition and follow-tail per `SEND_STREAM_PREFLIGHT.md`.

Only explicitly user-visible service reasoning/status/tool data may be shown. Hidden chain-of-thought/internal tool/system nodes, raw `assistant:thoughts`, raw tool arguments and raw tool output remain prohibited.

The b55/b56 evidence authorizes exact `reasoning_ended` as a phase marker; it does **not** authorize treating recap text as the reasoning body. b57 re-presents only the same already-accepted visible assistant text stream around that marker. Exact missing-prefix extraction and exact user-visible tool-node presentation remain Unknown / Unverified pending evidence.

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
- b54 Runtime materially identifies tool call/result grammar but leaves recap coverage inconclusive due generic diagnostic saturation.
- b55 Runtime passes the special-observer / exact recap-end-structure gate.
- b56 Runtime is a partial pass: recap UI works, recap-body assumption rejected, real reasoning/final remained mixed, leading reasoning still truncated.
- b57 Code/CI/Artifact/package is verified and Runtime pending.
- Full-Web long-conversation composer viability failed on the primary device/workload reported at b47.
- Native production response ownership/reasoning/follow-tail/background lifecycle, exact missing-prefix field, exact tool-node user visibility, existing-conversation pre-React history virtualization, 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified where not explicitly tested.
- CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
