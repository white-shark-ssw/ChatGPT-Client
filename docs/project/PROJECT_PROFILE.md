# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-31 through exact b64 Runtime and exact b65 Code/CI/Artifact/package verification.**

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
- b48-b65 are isolated diagnostic Native-over-Web-Send exceptions and do not modify production hidden/shadow-Web restrictions or native response ownership.

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
- b61 captured generic-textarea false readiness; b62 removed only that authority and passed the focused verified-composer path.
- b63 same-run Runtime plus official-Web expanded-detail evidence authorized one narrow GitHub mapping: invocation `connector_tool_payload` as user-visible tool input and exact parent-paired GitHub result `message.content` as user-visible output.
- b64 implemented that mapping. Exact iPhone/iOS17 Runtime reached real protected Send, HTTP200 SSE/terminal, reasoning `27/440`, final `215/6716`, Native tool presentations/completion updates `30/30`, 26 detail-capable rows and multiple successful expand/collapse interactions. The only rejected part was detail formatting/density.
- b65 preserves b64 transport/lifecycle/data authorization and changes Native detail presentation only: tool row -> independently collapsed `工具输入` / `工具输出`; output outer JSON is decoded into readable hierarchy so nested string text is no longer displayed as a second-layer escaped JSON wall.

### Exact b64 Runtime predecessor

- Candidate `DEV-send-stream-0.1.0-b64`, `0.1.0 (64)`.
- Exact product/config source `6ce1fbd242c903d85930b0e8a8d2aadc29669cc1`; Artifact `9736051023`; IPA SHA `49b5e8021ca78da3e87f67721682edf306b300995be3566a391a6c35d573c6fc`.
- User export matched exact build/source on iPhone/iOS17.0.
- Exact parent association remained authoritative: 30 matches, 5 unmatched, 0 missing; unmatched results were not force-paired.
- Classification: **Runtime partial-pass — Send/reasoning/final/exact-parent detail lifecycle passed; formatting/density defect only.**
- Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b64-runtime.md`.

### Exact b65 current Artifact Candidate

- Candidate `DEV-send-stream-0.1.0-b65`, `0.1.0 (65)`.
- Exact product/config source `44138db766d00e62cfda7f20182f6d20f1ec3352`; tree `fb02dfa7512e9c8428c4b0e9b7184a56d602f688`.
- Push Run / Job `33328232044 / 99302071335` — success.
- PR Run / Job `33328233842 / 99302076369` — success.
- Push Artifact `9736876465`; PR Artifact `9736874445`.
- Push ZIP `sha256:d9a52ecb0cd7d5131e22fc399bc5db0d573a9de3e5d80838f3a8d2b3164ceb7a`.
- IPA SHA `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`.
- Package: Release / `0.1.0 (65)` / Candidate b65 / source marker `44138db766d0` / iOS14 / `[1,2]` / arm64.
- b65 is permanently reserved because a valid Artifact exists.
- Evidence ladder: Code written / detached diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / **Runtime pending**.

## Current product interaction target

For `DEV-send-stream`, eventual Native behavior should follow the official response lifecycle as closely as verified service data permits:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.

The tested state ordering, reasoning/final split, exact-parent tool lifecycle and GitHub input/output mapping have positive Runtime evidence. Exact cross-tool expandable-detail schema and accepted production response ownership remain Unknown / Unverified.

## Current next Candidate boundary

b39-b65 are permanently reserved. **Do not allocate b66 before exact b65 iPhone/iOS17 Runtime evidence.** If b65's nested disclosure/readable-output gate passes, close the current formatting defect without another Candidate. If an exact product defect remains, b66 may implement only the smallest evidence-backed correction.

## Remaining Unknown / Unverified

Accepted production Native response ownership, expandable detail semantics for connectors/tool families beyond the currently evidenced GitHub mapping, Native first/exclusive resume, existing-conversation pre-React virtualization, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
