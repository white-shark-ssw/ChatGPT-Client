# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b62 focused Runtime classification.**

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
- b62 removed only that false-ready generic-textarea authority and now passes the tested focused verified-composer Runtime gate.

### Exact b62 current tested Candidate

- Candidate `DEV-send-stream-0.1.0-b62`, `0.1.0 (62)`.
- Exact product/config source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`; tree `d3432dfe2e32cddcfac7a5a56d7880772dc6989d`.
- Push Run / Job `33316398081 / 99270535435` — success.
- PR Run / Job `33316399402 / 99270539763` — success.
- Artifact `9733577825`; ZIP `sha256:d53ddb88c5d2092294592416e10e5a0a752cb7afb0bbe0a39c2c137d021082d0`.
- IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`.
- Package: Release / `0.1.0 (62)` / Candidate b62 / source marker `e1b44f7ab6c4` / iOS14 / `[1,2]` / arm64.
- b62 is permanently reserved.

Exact user Runtime export `ChatGPTClient-Diagnostics-20260830-151146.json` matched the package identity and showed:

- startup composer `ready=false / none` until official `prompt_textarea` appeared;
- submit-time strategy `prompt_textarea`;
- `submitted` followed immediately by real `sendObserved`;
- HTTP200 SSE, terminal true;
- reasoning `34 deltas / 497 chars`, preambles `3/20`, reasoning segment breaks `2`, exact reasoning end `1`, fallback false;
- final answer `93 deltas / 2878 chars`;
- result parent present/matched/unmatched/missing `20/20/0/0`;
- Native tool presentations/completion updates `20/20`.

User reported the tested round looked normal and the screenshot showed complete-looking reasoning, tool completion state and final answer.

Classification: **b62 focused Runtime pass for the tested verified-composer Send-entry + preserved reasoning/final + exact-parent tool lifecycle scope.** One positive run is not a universal proof that the intermittent b61 official-page race can never recur.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

## Current product interaction target

For `DEV-send-stream`, eventual Native behavior should follow the official response lifecycle as closely as verified service data permits:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.

The tested state ordering, reasoning/final split and parent-paired tool lifecycle now have positive evidence. Exact cross-tool **user-visible expandable-detail schema** and accepted production response ownership remain Unknown / Unverified.

## Current next Candidate boundary

b39-b62 are permanently reserved. **Do not allocate b63 by field-name guess.** b62 safe shape evidence includes `connector_tool_payload`, `reasoning_titles`, `tool_icons`, `invoked_resource` and `inline_cot_expandable_content`, but current evidence does not authorize their raw values/bodies as user-visible tool detail.

A b63 Candidate requires a concrete current evidence need plus a fresh uniqueness/conflict guard. If existing official-Web screenshots and b62 shape evidence cannot prove the user-visible detail mapping, the next candidate should be bounded diagnostic-only rather than a speculative detail implementation.

## Remaining Unknown / Unverified

Accepted production Native response ownership/tool-card expandable detail semantics, Native first/exclusive resume, existing-conversation pre-React virtualization, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
