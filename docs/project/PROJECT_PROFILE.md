# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b60 Runtime and b61 Code / CI / Artifact / package verification.**

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
- b48-b61 are isolated diagnostic Native-over-Web-Send exceptions and do not modify production hidden/shadow-Web restrictions or native response ownership.

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
- b60 Runtime passed the tested official-like thinking-state / reasoning-segmentation / text-completeness gate and established exact result `parent_id` association.

### Exact b60 Runtime

- Candidate `DEV-send-stream-0.1.0-b60`, exact source `8ca445f3c17233ac36832f46417a8e53a138499e`, Artifact `9731477362`, IPA SHA `7cae323231b6b9d1aa837b03506450daa99f457fd8b4025deedb368dc008cd42`.
- Two consecutive iPhone/iOS17 tool-active turns: HTTP200 SSE / terminal; both showed initial `正在思考`, reasoning streaming and a Native paragraph break with no obvious truncation.
- Turn 1 parent association `15/15` results matched, 0 unmatched/missing; Turn 2 `5/5`, 0 unmatched/missing.
- Author-name==recipient was only 14/15 then 3/5; therefore it is not association authority.
- Accepted tested rule: result metadata `parent_id` matches the invocation service message ID observed in the same stream. Raw IDs remain transient/unlogged; chronology/count/name pairing is rejected.
- Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b60-runtime.md`.

### Exact current b61 Candidate

- Candidate `DEV-send-stream-0.1.0-b61`, `0.1.0 (61)`.
- Exact product/config source `2386872af03e0684eee8deca87f636dc265114ec`; tree `a687500c88cffabf3a8496652fd5e0b633264836`.
- Push Run / Job `33312809061 / 99260781131` — success.
- PR Run / Job `33312811455 / 99260788483` — success.
- Artifact `9732514781`; ZIP `sha256:66976ecb53ac8fc2b116dcbce753fdf05499cea88dd29f0ae4223ab8baa5bf28`.
- IPA SHA `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`.
- Package: Release / `0.1.0 (61)` / Candidate b61 / source `2386872af03e` / iOS14 / `[1,2]` / arm64.
- b61 is permanently reserved. Code / Push CI / PR CI / Artifact / package identity passed; Runtime/manual pending.
- b61 preserves b60 Send/text/reasoning/thinking behavior, uses the accepted `parent_id` association to update the correct transient Native tool row, and logs only bounded type/key/count/string-length shape for candidate detail metadata.
- Raw tool request/result bodies, connector payload values and `assistant:thoughts` remain non-presentational.

## Current product interaction target

For `DEV-send-stream`, eventual Native behavior should follow the official response lifecycle as closely as verified service data permits:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.

Current evidence supports the tested state ordering and parent pairing. Exact cross-tool **user-visible detail field schema** and accepted production response ownership remain Unknown / Unverified.

## Current next Candidate boundary

b39-b61 are permanently reserved. **Do not allocate b62 until exact b61 Runtime** proves correct parent-paired row completion behavior and identifies a bounded field that can be demonstrated as user-visible rather than internal connector data.

## Remaining Unknown / Unverified

Accepted production Native response ownership/tool-card detail semantics, Native first/exclusive resume, existing-conversation pre-React virtualization, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
