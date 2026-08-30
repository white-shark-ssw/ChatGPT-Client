# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b57 Runtime and exact b58 Code/CI/Artifact/package verification.**

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
- `NativeWebSendEngineProbeViewController` is diagnostic-only and does not mutate production `ConversationRepository`.

## Durable Send/security/product boundary

- Exact b42 proves successful ChatGPT-account protected Send depends on browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- Separately billed API-product architecture remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by account-safety policy.
- TD-024 permits an explicitly visible official-Web Send surface as a security permission only; TD-025 rejects b44 full-page hybrid product form; TD-028 records the b47 long-answer mobile-Web composer viability ceiling.
- Full existing-conversation mobile-Web rendering is not an accepted daily-chat production dependency.
- b48-b58 are isolated diagnostic Native-over-Web-Send exceptions and do not modify production hidden/shadow-Web restrictions or native response ownership.

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
- b52 kept final answer complete while visible reasoning beginning was incomplete.
- b53-b55 identified explicit reasoning/tool classes and exact `reasoning_ended` marker while keeping raw `assistant:thoughts` non-presentational.
- b56 showed recap text itself is not the real reasoning body in the tested turn; the recap event remains a valid reasoning-end marker.

### b57 Runtime

Exact b57: Candidate `DEV-send-stream-0.1.0-b57`, source `7074b1f85a0f239a5fd615f52196e1e28145523c`, Artifact `9729360247`, IPA SHA `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`.

Exact iPhone/iOS17 Runtime passed the reasoning/final phase gate: reasoning `4 deltas / 61 chars` streamed only in `思考过程`, final answer `12 / 287 chars` stayed separate, exact reasoning-end marker count was 1, and the prior leading truncation did not reproduce. A six-character `is_thinking_preamble_message` existed but was not consumed, so no prefix parser change is justified.

The same turn contained multiple assistant-code -> tool-result structures while Native showed no tool activity. Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b57-runtime.md`.

### Exact current b58 Candidate

- Candidate `DEV-send-stream-0.1.0-b58`, `0.1.0 (58)`.
- Exact product/config source `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`; tree `ddb396aa942c48222e69671eaf3610127d9797e9`.
- Push Run / Job `33303998650 / 99237187408` — success.
- PR Run / Job `33304001877 / 99237195550` — success.
- Artifact `9729864129`; ZIP `sha256:3a907e6bb5f1cbd7f57d54b01e64805196247e612e2de961dac99d92df2060ac`.
- IPA SHA `0d5988caf21300bfb29e81b3f1f8bbf6eaa69a84f09efeda601e6d6f9b7b8875`.
- Package: Release / `0.1.0 (58)` / Candidate b58 / source `d9dbf208625e` / iOS14 / `[1,2]` / arm64.
- b58 preserves b57 text/reasoning behavior and adds only a separate compact diagnostic `工具调用` region for exact completed assistant-code invocations. Service `reasoning_title` is transient UI only if present; generic local fallback otherwise. Tool result body, raw args/results, connector payloads and `assistant:thoughts` remain excluded.
- Runtime/manual: Pending. b58 permanently reserved.

## Current next Candidate boundary

b39-b58 are permanently reserved. Do not allocate b59 until exact b58 Runtime supplies a concrete smallest next change.

Current b58 human gate: one tool-active reasoning turn confirming b57 phase split remains correct, the compact tool region appears, titles/fallback are understandable, raw tool payloads remain absent, and terminal diagnostics are exported.

## Remaining Unknown / Unverified

Accepted production Native response ownership/tool-card semantics, Native first/exclusive resume, existing-conversation pre-React virtualization, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
