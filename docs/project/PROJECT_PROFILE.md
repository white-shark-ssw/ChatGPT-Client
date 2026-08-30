# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b59 Runtime.**

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
- b48-b59 are isolated diagnostic Native-over-Web-Send exceptions and do not modify production hidden/shadow-Web restrictions or native response ownership.

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
- b57 split already-accepted visible text into Native reasoning/final around exact reasoning end.
- b58 Runtime passed compact tool activity but proved an omitted reasoning prefix exactly matched a service-marked thinking-preamble part.

### Exact current b59 Candidate / Runtime

- Candidate `DEV-send-stream-0.1.0-b59`, `0.1.0 (59)`.
- Exact product/config source `138c09a5d11121945bc45f1d866c449aa0f7611e`; tree `c28eb92616e494a15aa2e370e2fd5150986b2452`.
- Push Run / Job `33305680998 / 99241706079` — success.
- PR Run / Job `33305683021 / 99241711695` — success.
- Artifact `9730376958`; ZIP `sha256:4c13fc5941786b6db1797d72b8938f763cdaec2b76b8d15998fd4d6f235763ef`.
- IPA SHA `5758cf40b287c7d9c5cef2f13163d5c8239834ee617468692c56b4bdb0349252`.
- Package: Release / `0.1.0 (59)` / Candidate b59 / source `138c09a5d111` / iOS14 / `[1,2]` / arm64.
- Exact iPhone/iOS17 Runtime: HTTP200 SSE / terminal; Native reasoning `12 deltas / 207 chars`, final `18 / 357`; thinking preambles `2 / 13 chars`; tool invocations/results `12/13`; Native compact tool presentations 12.
- User confirmed reasoning, compact tool activity and final answer were complete; prior leading truncation did not reproduce.
- Remaining reasoning presentation defect: separate reasoning segments are flattened without official-style paragraph breaks.
- Current tool-detail boundary: official Web exposes expandable request/result detail; Native does not yet. Exact pairing must be proven because 12 invocations vs 13 results makes adjacency unsafe.
- Explicit safe `metadata.reasoning_status=is_reasoning` was observed after tool activity and before the second thinking preamble, proving a return-to-reasoning state signal while `assistant:thoughts` body remains non-presentational.
- Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b59-runtime.md`.

## Current product interaction target

For `DEV-send-stream`, the user explicitly wants eventual Native behavior to follow the official response lifecycle as closely as verified service data permits:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.

Current evidence supports most state boundaries. Exact initial service-side reasoning-start signal, cross-tool user-visible card schema/pairing and accepted production response ownership remain Unknown / Unverified.

## Current next Candidate boundary

b39-b59 are permanently reserved. A b60 candidate may be allocated only after confirming the identity/artifact name is unused. Its bounded evidence scope is reasoning segment presentation, lifecycle/explicit reasoning-active status, and privacy-safe tool invocation/result association diagnostics. It must not expose raw tool bodies or restructure production `ConversationRepository`.

## Remaining Unknown / Unverified

Accepted production Native response ownership/tool-card semantics, Native first/exclusive resume, exact initial service reasoning-start event, existing-conversation pre-React virtualization, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
