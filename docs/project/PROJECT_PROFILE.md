# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-30 through exact b63 Code/CI/Artifact/package verification.**

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
- b48-b63 are isolated diagnostic Native-over-Web-Send exceptions and do not modify production hidden/shadow-Web restrictions or native response ownership.

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
- b62 removed only that false-ready generic-textarea authority and passed the tested focused verified-composer Runtime gate.
- b63 preserves exact b62 response behavior and adds only bounded expandable-detail structure diagnostics; Runtime is pending.

### Exact b62 tested predecessor

- Candidate `DEV-send-stream-0.1.0-b62`, `0.1.0 (62)`.
- Exact product/config source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`; Artifact `9733577825`; IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`.
- Exact iPhone/iOS17 export showed `prompt_textarea -> submitted -> sendObserved -> HTTP200 SSE -> terminal`, reasoning `34/497`, final `93/2878`, result parent matches `20/20`, Native tool presentations/completion updates `20/20`.
- User reported the tested round looked normal.

Classification: **b62 focused Runtime pass for the tested verified-composer Send-entry + preserved reasoning/final + exact-parent tool lifecycle scope.** One positive run is not a universal proof that the intermittent b61 official-page race can never recur.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

### Exact b63 current diagnostic Candidate

- Candidate `DEV-send-stream-0.1.0-b63`, `0.1.0 (63)`.
- Exact product/config source `0c2e2b870e51c363c7734182d49618c438839cc2`; tree `cae7f27e2800fe48f8d492bfd364c91755935c67`.
- Push Run / Job `33321982009 / 99285436158` — success.
- PR Run / Job `33321983658 / 99285440962` — success.
- Artifact `9735145598`; ZIP `sha256:645cba67a91387f79d386931b5d0f4ead2502408b15c7f339013505e3f0ec7da`.
- IPA SHA `b347d1e41ca5a4e1355a9cc713574ea96247e11918ccfb1f5ff621a0f9f6ff36`.
- Package: Release / `0.1.0 (63)` / Candidate b63 / source marker `0c2e2b870e51` / iOS14 / `[1,2]` / arm64.
- b63 is permanently reserved because an Artifact exists.
- Evidence ladder: Code written / diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / **Runtime pending**.

b63 diagnostic scope is deliberately narrow:

- string-shaped `connector_tool_payload` is parsed only to produce a capped JSON parse/top-level key/type/direct length fingerprint;
- `inline_cot_expandable_content.source_message_ids` contributes only aggregate response-local reference/match counts against existing transient tool identities;
- no raw IDs, connector/tool payload values, nested bodies or `assistant:thoughts` are exported;
- no Native expandable body is presented yet;
- composer, protected Send, text parser, reasoning/final split and tool row lifecycle remain b62 behavior.

## Current product interaction target

For `DEV-send-stream`, eventual Native behavior should follow the official response lifecycle as closely as verified service data permits:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.

The tested state ordering, reasoning/final split and parent-paired tool lifecycle have positive Runtime evidence. Exact cross-tool **user-visible expandable-detail schema** and accepted production response ownership remain Unknown / Unverified.

## Current next Candidate boundary

b39-b63 are permanently reserved. **Do not allocate b64 from b63 field names alone.** The next product-code Candidate requires exact b63 iPhone/iOS17 Runtime evidence. If same-run diagnostics plus official-Web expanded-detail screenshot prove one safe user-visible mapping, a b64 implementation may use only that proven minimum. If b63 evidence rejects or fails to resolve the mapping, do not broaden by guess; use the smallest next evidence action instead.

## Remaining Unknown / Unverified

Accepted production Native response ownership/tool-card expandable detail semantics, Native first/exclusive resume, existing-conversation pre-React virtualization, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switch and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.
