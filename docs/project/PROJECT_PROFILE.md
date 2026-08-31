# Project Profile

## Initialization

**Initialized — 2026-08-25; refreshed 2026-08-31 through accepted b67 production transport Runtime, positive b72 tested cross-conversation simultaneous-generation Runtime, b72 presentation rejection, and exact b73 Code/scope/Simulator/Push+PR CI/Artifact/package verification.**

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
- Production native conversation/list/read/recovery/**response lifecycle** authority: one `ConversationRepository` in `Conversation/ConversationFeature.swift`; optimistic user/live assistant state, ordered reasoning/tools and per-conversation response snapshots remain Repository-owned. b73 changes presentation state only and does not add a second response owner.
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
- b67 accepted the existing-conversation production protected-Send transport: one Send -> HTTP200 SSE -> Repository updates -> terminal/reconcile.
- b69 established the ordered response-timeline direction but exact iPhone/iOS17 Runtime exposed keyboard, optimistic-user-row, GitHub detail/icon/spacing/divider and transient Native 403 lifecycle defects.
- b70 is the exact correction Candidate: source `fb83be9163838f78abfa47903e67f27b6f66ec52`, Push+PR CI passed, Artifact `9752289536`, package independently verified; Runtime pending.

## Exact b66 production Runtime

b66 implemented the first existing-conversation TD-029 production bridge + Repository live response + Web Rule Lab.

- Candidate `DEV-send-stream-0.1.0-b66`, source `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`, Artifact `9739572172`, IPA `7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`.
- Build/CI/package identity passed.
- Exact iPhone/iOS17 Runtime **failed production same-response ownership**: each reproduction showed `composer_ready x2`, `submit_result=submitted x2`, one real `send_observed`, then `send_transport_error`; no `sendResponse`, no Native response characters.
- User independently confirmed the official ChatGPT app had already received the assistant reply. Therefore the protected Send reached/completed server-side, while the Native production wrapper lost the request before obtaining HTTP Response.
- Source correlation identified a local Swift->JS duplicate-submit race, not an official Web selector/SSE rule change. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b66-runtime.md`.

## Exact b73 current Candidate

Build73 is the presentation-only correction after b72 Runtime accepted the tested A-generating + B-send simultaneous-generation path but rejected main reasoning/tool density and default live disclosure behavior. b73 preserves the b72 per-conversation covered executor implementation and b67 protected-Send/SSE path.

Identity: Candidate `DEV-send-stream-0.1.0-b73`, `0.1.0 (73)`, exact source `4edda892a04a1a07f4a07e74b135b969ea82193e`; product code commit `0e3eb6cad4cc56e8c2bcb946724d7cf1d4d55701`; assembly `33408291419` success after one tooling-only assertion failure; Push `33408695143/99542593642`; PR `33408698697/99542605699`; Artifact `9764247402`; ZIP `sha256:718c2f4fd0fe3521f7469f5996f6944960ffdaa3b2829c0c17e340ebd41dd206`; IPA `8285ba9d5f63207feb2eaf722ec722a886f3ee88956236a89a716ad58b884113`; package source marker `4edda892a04a`, Release, iOS14 minimum, arm64. Evidence: Code/scope/Simulator/Push+PR CI/Artifact/package verified; **Runtime pending**; Stable-Frozen No.

Build73 main inline reasoning shows body-scale primary reasoning prose and only meaningful service-authored tool titles with looser tool row rhythm, while the tools-only sheet retains the ordered call list. Live reasoning auto-opens once when visible reasoning/tool content first arrives and auto-collapses once on exact `reasoning_ended`; later user disclosure state remains user-owned.

## Current product interaction target

Native response behavior should follow verified service events:

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次思考/思考流 -> reasoning_ended -> 折叠思考 -> 完整最终回答`.

Tool phases remain optional. `assistant:thoughts` is never presented. General Markdown/code/table/link/citation rendering remains future `DEV-message-rendering`; final Composer hierarchy/dynamic input/drafts/attachment staging remain future `DEV-composer-parity`.

## Current next Candidate boundary

Build73 is the current exact real-device presentation Runtime candidate. b39-b73 are permanently reserved. Do not allocate b74 before exact b73 Runtime supplies a concrete defect/next evidence need. The gate must verify live default-expanded reasoning, one automatic collapse at exact reasoning end, user-owned disclosure after that transition, concise meaningful main tool rows with looser spacing/body-scale reasoning prose, tools-only/input-only sheet preservation, and no regression to the b72 tested cross-conversation simultaneous-generation path.

## Remaining Unknown / Unverified

Exact b73 presentation Runtime, new-chat authoritative identity timing, server Stop mechanism, broader cross-conversation/service concurrency beyond the exact b72 A/B test, connector detail beyond the evidenced GitHub mapping, Native first/exclusive resume, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.