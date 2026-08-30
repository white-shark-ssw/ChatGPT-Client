# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b61 Runtime classification and b62 Code / CI / Artifact / package verification.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity / purpose

- Project: `ChatGPT-Client` (`white-shark-ssw/ChatGPT-Client`).
- Purpose: native third-party ChatGPT client for iOS; stable product value is native shell/read/navigation with future accepted response ownership kept in native architecture.
- Distribution: TrollStore IPA.
- Primary tested runtime: iPhone 15 Pro Max / iOS17.0; build minimum iOS14.0.
- Current stable merged product baseline: Phase 8 b38; Frozen No.
- Current Active Work: `DEV-send-stream`, branch `dev/send-stream-20260829`, PR #29 open/evidence-only.

## Technology stack / build

- Swift 5 + UIKit, Foundation, WebKit, OSLog, CryptoKit; no third-party dependencies.
- Build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- Packaging: `bash scripts/build_ipa.sh`.
- CI: GitHub Actions macOS15.
- Candidate identity: `DEV-<work-slug>-<marketing-version>-b<build>`; built `Info.plist` is package identity authority.
- Once an Artifact identity is emitted it is permanently reserved; corrected code uses a new build/Candidate.

## State owners

- Native navigation shell: `AppDelegate.swift`, `RootViewController.swift`.
- Persistent auth-secret authority: default persistent `WKWebsiteDataStore` only.
- Native auth/account authority: `Authentication/AuthSessionStore.swift`.
- Production native conversation/list/read/recovery/future accepted response authority: one `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- Conversation-list persistence: `ConversationListCacheStore`, storage-only behind repository authority.
- Native conversation presentation: `ConversationDetailViewController`.
- Stable long-message geometry: `ConversationMessagePresentationProjection` + `ConversationMessageCell`, exact b38.
- Protocol diagnostics: `DiagnosticsLogger` + diagnostic controllers. Diagnostics may record privacy-safe structure/counts, never prompt/body/raw IDs/auth/proof/token values.
- `NativeWebSendEngineProbeViewController` remains diagnostic-only and does not mutate production `ConversationRepository`.

## Durable Send/security/product boundary

- Exact b42 proves successful ChatGPT-account protected Send depends on browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- Separately billed API-product architecture remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by account-safety policy.
- TD-024 permits an explicitly visible official-Web Send surface as a security permission only; TD-025 rejects b44 full-page hybrid product form; TD-028 records the b47 long-answer mobile-Web composer viability ceiling.
- Full existing-conversation mobile-Web rendering is not an accepted daily-chat production dependency.
- b48-b62 are isolated diagnostic Native-over-Web-Send exceptions and do not modify production hidden/shadow-Web restrictions or native response ownership.

## Stable accepted baselines

- Foundation b1 Stable/merged.
- Auth b6 Stable/merged for recorded Plus/personal scope.
- Protocol-read b7 accepted diagnostic evidence.
- Native read b9 Stable/merged.
- Recovery b15 Stable/merged.
- Multi-conversation b21 Stable/merged.
- List-cache b23 Stable/merged; Frozen No.
- Conversation metadata/settings/round navigation b38 Stable/merged; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; exact tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Artifact `9708425762`, IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.

## Phase 9 current evidence

- b45 official no-resend resume is Runtime Confirmed; b46/b47 duplicated Native Cookie+Bearer-only resume rejected with HTTP404 JSON; first/exclusive Native resume Unknown.
- b48-b51 established Native composer -> official protected Send and complete compact text continuation, including fresh-new-chat title-generation correction.
- b52-b56 identified reasoning/tool grammar and exact `reasoning_ended` while keeping raw `assistant:thoughts` non-presentational.
- b57-b59 established reasoning/final split and exact service-marked thinking-preamble inclusion.
- b60 passed tested thinking-state / reasoning-segmentation / text-completeness and exact result-parent association.
- b61 successful tool-active Runtime passed transient parent-paired row lifecycle; a separate cold/new-page run captured generic-textarea false-ready / false-submitted behavior before protected Send.
- b62 removes only that false-ready generic-textarea authority and otherwise preserves b61 behavior.

### Exact b61 Runtime

- Candidate `DEV-send-stream-0.1.0-b61`, source `2386872af03e0684eee8deca87f636dc265114ec`, Artifact `9732514781`, IPA SHA `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`.
- Failed run `ChatGPTClient-Diagnostics-20260830-134827.json`: page `new_or_other`; composer `strategy=textarea`; `nativeSubmit` + `submitResult=submitted`; no `sendObserved`, `sendResponse`, thinking or stream metrics. User observed no answer activity. Classified as a Send-entry false-ready defect.
- Successful run `ChatGPTClient-Diagnostics-20260830-135112.json`: HTTP200 SSE / terminal; reasoning `10/251`, final `68/2363`, reasoning segment breaks `1/1`, reasoning-end 1, fallback false; identities/results `14/14`, parent matches `14/14`, unmatched/missing `0/0`, Native presentations/completion updates `14/14`. User observed complete reasoning opening and tool rows progressing `调用中 -> 已完成`.
- Overall b61: **Runtime Partial** because successful response/tool lifecycle passed but the independent Send-entry defect remained.
- Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b61-runtime.md`.

### Exact current b62 Candidate

- Candidate `DEV-send-stream-0.1.0-b62`, `0.1.0 (62)`.
- Exact product/config source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`; tree `d3432dfe2e32cddcfac7a5a56d7880772dc6989d`.
- Push Run / Job `33316398081 / 99270535435` — success.
- PR Run / Job `33316399402 / 99270539763` — success.
- Artifact `9733577825`; ZIP `sha256:d53ddb88c5d2092294592416e10e5a0a752cb7afb0bbe0a39c2c137d021082d0`.
- IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`.
- Package: Release / `0.1.0 (62)` / Candidate b62 / source marker `e1b44f7ab6c4` / iOS14 / `[1,2]` / arm64.
- b62 is permanently reserved. Code / Push CI / PR CI / Artifact / package identity passed; Runtime/manual pending.
- Behavior change: remove unqualified `textarea:not([disabled])` from composer authority; retain `#prompt-textarea` and explicit `[contenteditable="true"][role="textbox"]`; add no retry/timer/watchdog/polling/fallback.

## Current product interaction target

For `DEV-send-stream`, eventual Native behavior should follow the official response lifecycle as closely as verified service data permits:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.

Current evidence supports the tested state ordering and parent pairing. Exact cross-tool **user-visible detail field schema** and accepted production response ownership remain Unknown / Unverified.

## Current next Candidate boundary

b39-b62 are permanently reserved. **Do not allocate b63 until exact b62 Runtime** classifies the verified-composer Send-entry gate and either accepts it for the tested scope or produces a concrete next defect/evidence need.

The b61 false-ready race is intermittent. b62 acceptance does not require reproducing it; one focused cold-launch run must instead prove that Native does not accept an unverified generic textarea and that any enabled Send which succeeds proceeds into the real protected-Send/SSE lifecycle. A second cold launch is useful but optional.

## Remaining Unknown / Unverified

Accepted production Native response ownership/tool-card detail semantics, Native first/exclusive resume, existing-conversation pre-React virtualization, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
