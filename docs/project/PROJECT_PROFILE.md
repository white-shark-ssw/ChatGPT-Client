# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-31 through accepted b67 production transport Runtime, b68 superseded presentation Artifact, and exact b69 Code/CI/Artifact/package verification.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity / purpose

- Project: `ChatGPT-Client` (`white-shark-ssw/ChatGPT-Client`).
- Purpose: native third-party ChatGPT client for iOS; native shell/read/navigation/conversation state remain product authority while official Web is used only for the browser-required protected-Send execution boundary authorized by TD-029.
- Distribution: TrollStore IPA.
- Primary tested runtime: iPhone 15 Pro Max / iOS17.0; build minimum iOS14.0.
- Current stable merged product baseline: Phase 8 b38; Frozen No.
- Current Active Work: `DEV-send-stream`, branch `dev/send-stream-20260829`, PR #29 open/evidence-only.
- Future final Composer Work: serialized `DEV-composer-parity`; not an Active parallel branch/Candidate.

## Technology stack / build

- Swift 5 + UIKit, Foundation, WebKit, OSLog, CryptoKit; no third-party dependencies.
- Build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- Packaging: `bash scripts/build_ipa.sh`.
- CI: GitHub Actions macOS15.
- Candidate identity: `DEV-<work-slug>-<marketing-version>-b<build>`; built `Info.plist` is package identity authority.
- Once an Artifact identity is emitted it is permanently reserved; corrected product code uses a new build/Candidate.

## State owners

- Native navigation shell / production covered-Send orchestration: `AppDelegate.swift`, `RootViewController.swift`.
- Persistent auth-secret authority: default persistent `WKWebsiteDataStore` only.
- Native auth/account authority: `Authentication/AuthSessionStore.swift`.
- Production native conversation/list/read/recovery/**response lifecycle** authority: one `ConversationRepository` in `Conversation/ConversationFeature.swift`; current b69 ordered response runtime extension is still Repository-owned even though integration code presently lives with the first production bridge.
- Conversation-list persistence: `ConversationListCacheStore`, storage-only behind Repository authority.
- Native conversation presentation: `ConversationDetailViewController`.
- Stable long-message geometry: `ConversationMessagePresentationProjection` + `ConversationMessageCell`, exact b38.
- Covered official Web executor: `CoveredWebSendExecutor`; browser challenge/protected-request execution only, never conversation/message/response authority.
- Web Rule Lab: Settings-reachable visible development `WKWebView`, same `.default()` data store, explicit temporary JS/result only, never production owner.
- Protocol diagnostics: `DiagnosticsLogger` + diagnostic controllers. Normal exports may record privacy-safe structure/counts/state only, never prompt/body/raw IDs/auth/proof/token/tool-body values.
- `NativeWebSendEngineProbeViewController` remains diagnostic-only and does not own production Repository state.

## Durable Send/security/product boundary

- Exact b42 proves successful ChatGPT-account protected Send depends on browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- Separately billed API-product architecture remains rejected; primary-account Sub2API/Codex-subscription route remains blocked by account-safety policy.
- TD-025/TD-028 reject the full-page Native->Web->Native product form and full existing-conversation mobile-Web rendering as the daily-chat dependency.
- **TD-029 is current production Send architecture:** Native action -> Repository response operation -> one covered official-page protected Send -> same-response SSE -> Repository incremental response -> Native presentation.
- Covered Web uses `WKWebsiteDataStore.default()`, owns browser challenge + protected request execution only, and never becomes a second conversation/response/auth-secret store.
- Native code never solves/replays/persists Sentinel/PoW/Turnstile/conduit/challenge material.
- One user Send must produce exactly one protected Send; Sync/Reload never resend/regenerate.

## Stable accepted baselines

- Foundation b1 Stable/merged.
- Auth b6 Stable/merged for recorded Plus/personal scope.
- Protocol-read b7 accepted diagnostic evidence.
- Native read b9 Stable/merged.
- Recovery b15 Stable/merged.
- Multi-conversation b21 Stable/merged.
- List-cache b23 Stable/merged; Frozen No.
- Conversation metadata/settings/round navigation b38 Stable/merged; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; exact tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Artifact `9708425762`, IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.

## Phase 9 evidence progression

- b45 official no-resend resume Runtime Confirmed; b46/b47 duplicated Native Cookie+Bearer-only resume rejected; first/exclusive Native resume Unknown.
- b48-b51 established Native composer -> official protected Send and complete compact text continuation, including exact `title_generation` continuation.
- b52-b56 identified reasoning/tool grammar and exact `reasoning_ended`, keeping `assistant:thoughts` non-presentational.
- b57-b59 established reasoning/final split and service-marked thinking-preamble inclusion.
- b60 passed thinking/segmentation/text completeness and exact result-parent association.
- b61 captured generic-textarea false readiness; b62 removed only that authority and passed the verified-composer path.
- b63 same-run Runtime + official-Web evidence authorized one narrow GitHub detail mapping.
- b64 passed protected Send/reasoning/final/exact-parent detail lifecycle; formatting/density only rejected.
- b65 fixed only nested disclosure/readable output and passed focused iPhone/iOS17 Runtime. Exact predecessor source `44138db766d00e62cfda7f20182f6d20f1ec3352`, Artifact `9736876465`, IPA `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`.

## Exact b66 production Runtime

b66 implemented the first existing-conversation TD-029 production bridge + Repository live response + Web Rule Lab.

- Candidate `DEV-send-stream-0.1.0-b66`, source `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`, Artifact `9739572172`, IPA `7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`.
- Build/CI/package identity passed.
- Exact iPhone/iOS17 Runtime **failed production same-response ownership**: each reproduction showed `composer_ready x2`, `submit_result=submitted x2`, one real `send_observed`, then `send_transport_error`; no `sendResponse`, no Native response characters.
- User independently confirmed the official ChatGPT app had already received the assistant reply. Therefore the protected Send reached/completed server-side, while the Native production wrapper lost the request before obtaining HTTP Response.
- Source correlation identified a local Swift->JS duplicate-submit race, not an official Web selector/SSE rule change. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b66-runtime.md`.

## Exact b69 current Candidate

b69 implements the user-supplied official-app chronological requirement with one Repository-owned ordered response timeline. Reasoning/tool items keep event order; tool completion updates in place; reasoning after a tool becomes a new segment; exact `reasoning_ended` still transitions to separate incremental final; authoritative Detail preserves supported order; hidden thoughts remain prohibited; b38 deterministic/manual geometry is retained.

Identity: Candidate `DEV-send-stream-0.1.0-b69`, `0.1.0 (69)`, source `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`, Push `33366226539/99407331552`, PR `33366229125/99407340011`, Artifact `9748400171`, ZIP `b1d91179...232f1`, IPA `0c06256d...3b0aa`, package source marker `5e9c21834830`, iOS14 minimum. Evidence: Code/diff/Push+PR CI/Artifact/package verified; **Runtime pending**; Stable-Frozen No.

## Current product interaction target

Native response behavior should follow verified service events:

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次思考/思考流 -> reasoning_ended -> 折叠思考 -> 完整最终回答`.

Tool phases remain optional. `assistant:thoughts` is never presented. General Markdown/code/table/link/citation rendering remains future `DEV-message-rendering`; final Composer hierarchy/dynamic input/drafts/attachment staging remain future `DEV-composer-parity`.

## Current next Candidate boundary

b39-b69 are permanently reserved. **Do not allocate b70 before exact b69 iPhone/iOS17 Runtime evidence.** The gate must naturally exercise at least `reasoning -> tool -> reasoning -> tool -> final` and verify chronological live/history presentation without modifying accepted b67 transport unless concrete Runtime evidence demands it.

## Remaining Unknown / Unverified

Exact b69 ordered-timeline Runtime, new-chat authoritative identity timing, server Stop mechanism, simultaneous cross-conversation generation, connector detail beyond the evidenced GitHub mapping, Native first/exclusive resume, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.