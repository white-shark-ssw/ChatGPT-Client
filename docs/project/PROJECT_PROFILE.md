## Latest DEV-send-stream candidate override — b101 2026-09-05

- Latest Human Runtime candidate: `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)`, permanently reserved. It addresses the exact b100 long-suspension Native read failure where Detail/list/manual Sync repeatedly returned `NSURLErrorDomain -1005` while WebKit networking reopened independently.
- b101 changes only Native idempotent conversation-list/Detail transport recovery: retire the matching cached transient session on the first exact `-1005`, reacquire through existing default-WebKit auth, retry the same read once, then terminate normally on any further failure. Protected Web Send and response/content authority are unchanged.
- Exact product `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; package source `da103452236e31e070eae68b9e7979a832662fc1`; Artifact `9948780963`; IPA `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`; package identity verified; Human Runtime pending; Stable/Frozen No.

## DEV-send-stream b100 foreground dormant-discovery override — 2026-09-05

- b99 Runtime: known-active external response auto-reconciled authoritative Detail `5->6` after ~7m32s background. After that response/executor was released, a later ~12m54s background interval had no automatic foreground discovery; manual Sync recovered `6->8`. b99 is Runtime Partial; its backlog-coalescing stress is Inconclusive in this sample; hard WebContent-death recovery remains Unverified.
- b100 changes only foreground discovery: selected conversation + no client-owned active response + no Detail operation => exactly one existing `ConversationRepository.syncLatestMessages`, even without a pre-existing external snapshot. Completed server state materializes directly; a newly discovered unfinished remote user turn may rearm the existing covered observer once.
- No polling/timer/retry/watchdog/background heartbeat/resend/guessed resume/second response authority.
- Exact product `70c7dc052865ef80ca7bdec083d7621c1a297eab`; package source `e88a50ad9c2098449b43fb0fce2c441a50cd20ac`; staging `33895020559/101095508915`, Push `33895244146/101096229135`, PR `33895249810/101096247432` passed; Artifact `9945483725`; IPA `sha256:5629deedca665b7a5cfa7e36b4996b7b1e4b7a160ca5cb35a465abfbd97fbc69`; Human Runtime pending; Stable-Frozen No.

## Latest DEV-send-stream candidate override — b99 2026-09-04

- b98 Human Runtime exact diagnostics `sha256:e0a0bd2c42168d0c3f8a6dd681bbad1bb571d4061b0f2958131cae5f8e059105`: no hard WebContent termination event occurred, so that new b98 branch remains Unverified. The included foreground authoritative Detail reconcile is Runtime Positive, but a later client-owned response replayed 170 buffered live events after ~5m background and drove 169 synchronous full presentation applications; user observed freeze/crash and a fresh `launch.start` followed 3s after the last live event.
- b99 is the evidence-scoped stability correction: preserve every Repository event/state transition, but coalesce only the expensive selected Detail UIKit presentation onto one pending main-queue application using the latest Repository snapshot. No timer, retry, watchdog, polling, transport mutation, Send replay or second response authority.
- b99 exact product `ec05c284010cb0f2de066bd1cfc3968e07730779`; package source `313c4c3bf2ac0dc729d4793198fe462ada5a14eb`; staging `33890678564/101081289220`; Push `33890809275/101081720750`; PR `33890812345/101081730258`; Artifact `9943798885`; IPA `sha256:68b7f99eac8fd1d3ab14c6085abd4a084f2b4759dc630f94044017c9a4aecf02`; Human Runtime pending; Stable/Frozen No.

# Project Profile

## Latest DEV-send-stream candidate override — b98 2026-09-04

- Latest test candidate: `DEV-send-stream-0.1.0-b98` / `0.1.0 (98)`; exact product `2edd55febe2005071722ddcb9989151b427165d8`; package source `17c65a390f2724a55cd29d466e01eaab988dcbfe`; canonical Artifact `9942092070`; IPA `sha256:b1dc76dbe28e77ceac3468e8cfd3ca0ded41601bd02db6b228bd391a1d697b67`; Human Runtime pending; Stable/Frozen No.
- b98 preserves b97 foreground authoritative Detail reconcile and adds only explicit hard `WKWebView` WebContent-process-death recovery for external observation. Protected Send remains TD-029 covered official-Web owned and is never automatically resent.
- b97 Human Runtime was not executed by user; its package identity remains permanently reserved.

## Latest DEV-send-stream candidate override — b97 2026-09-04

- Latest test candidate: `DEV-send-stream-0.1.0-b97` / `0.1.0 (97)`; exact product `12fc1d1f5020d76d1892c25a0ced94323d5a0142`; package source `5e43c398b52a62de9f9a6e6546de7312ba5eb1df`; canonical Artifact `9940228423`; IPA `sha256:49f8d9a8ef425409923bf904a3134265ddfa6d90597d72e04a1e976a5a8a90c7`; Human Runtime pending; Stable/Frozen No.
- b97 supersedes b96's rejected async-status/timer continuation experiment with one lifecycle-triggered authoritative Conversation Detail reconcile on foreground return for an already-active external response. Protected Send remains TD-029 covered official-Web owned.

## Latest DEV-send-stream candidate override — b96 2026-09-04

- Latest test candidate: `DEV-send-stream-0.1.0-b96` / `0.1.0 (96)`; exact product `9e50943de39dc304ab31904cbad8596d4ffddc14`; package source `cd6268540e4f5a815829f26a713b10e8d1957239`; canonical Artifact `9938422716`; IPA `sha256:a635903898324bdf0e59cf8712a2ebd5924def0da591d555fb25d2f62dabc361`; Human Runtime pending; Stable/Frozen No.
- b96 is the first Native cross-platform continuation candidate gated by authoritative Conversation Detail `conversation_async_status`; it does not replace TD-029 protected Web Send.

## Latest DEV-send-stream candidate override — 2026-09-03

- Latest test candidate: `DEV-send-stream-0.1.0-b93` / `0.1.0 (93)`; exact package source `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0`; canonical Artifact `9893141097`; Runtime pending; Stable/Frozen No.

## DEV-send-stream b91 project-scoped route identity package-ready override — 2026-09-03

- User Runtime distinction is now material: ordinary non-project conversations do not show the same continuation failure, while the tested project conversation does and its visible official Web appears healthy.
- Source inspection proves the injected bridge parsed conversation identity only from `/c/{conversation}`. Official project canonicalization uses the already-evidenced `/g/{scope}/c/{conversation}` form; after that transition the old parser returned `null`, classified the valid project page as `route=other`, and disabled the bridge's target-equality gates for page-owned `stream_status`, `/resume`, plural conversation snapshots, WebSocket target matching and composer identity.
- Exact b91 changes only that shared identity parser so both ordinary `/c/{conversation}` and the evidenced project `/g/{scope}/c/{conversation}` are recognized. It preserves b90 frontmost diagnostics for causal isolation and adds no retry, polling, timer, watchdog, Native status/resume synthesis, duplicate Send or response-store authority.
- Candidate / Build: `DEV-send-stream-0.1.0-b91` / `0.1.0 (91)`, permanently reserved.
- Exact b91 product commit: `cdab4e091683dc179753ed114c9ab5993a6c2d24`; exact product/config package source: `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`.
- Guarded staging `33746622538 / 100620460993` passed ancestry guard, exact replacement, exact two-product-file scope audit and Xcode Simulator compile. Earlier run `33746541830 / 100620201072` failed at an over-strict base guard before product application and emitted no product commit.
- Formal Push CI `33746881658 / 100621278207` and PR CI `33746886896 / 100621297087` both passed on exact package source `c5985f1e...`.
- Canonical Push Artifact `9890000591`; Artifact digest `sha256:6062b02f9f1332744816d01a58e13c1a8c82017ee50828051f014ef79b943350`; IPA `ChatGPTClient-0.1.0-b91-dev-send-stream.ipa`, independently recomputed SHA-256 `abbd27370665fb97dd1ee5edd239c0a5fa1ea0694cbb329a81c32ee86867c140`, matching its sidecar.
- Independent package inspection confirms Release `0.1.0 (91)`, Candidate b91, source `c5985f1e2e5d`, MinimumOSVersion 14.0, iPhone/iPad family `[1,2]`, `iphoneos`, Mach-O arm64.
- Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime Unverified / Stable-Frozen No.**
- Human Runtime gate is project-specific: after project canonicalization the bridge must continue reporting `route=conversation` and then prove or disprove the existing official page-owned continuation path. Non-project conversations are regression coverage, not the primary target.

## DEV-send-stream b90 frontmost-presentation package-ready override — 2026-09-03

- Candidate / Build: `DEV-send-stream-0.1.0-b90` / `0.1.0 (90)`, permanently reserved.
- Exact b90 product commit: `5e9d735ddb2f7a2c46dbc43de2525980c86a1c1e`; exact product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`.
- b90 changes only one Runtime A/B variable relative to b89: after explicit manual-Sync rearm, the existing executor `WKWebView` is brought to the front of its current Root host before loading the same target. Existing interactivity, focus rearm, route, page-owned continuation observation, protected Send and `ConversationRepository` ownership remain unchanged.
- Corrected guarded staging `33727956426 / 100561161422` passed exact patch, exact two-product-file scope audit and Xcode Simulator compile, then committed/pushed product `5e9d735...`. An earlier staging run `33727587238 / 100560009446` also passed patch/scope/Simulator but failed before remote product commit only because the Actions token could not modify a workflow file; it emitted no b90 product identity.
- Push CI `33728071476 / 100561518990` and PR CI `33728075476 / 100561530874` both passed on package source `99f1aa15...`.
- Canonical Push Artifact `9882770072`; ZIP `sha256:363c6fdbade5d476eacdee064eec26ed3480c0e7ba1da3b5dcf6b8537af46f6e`; IPA `ChatGPTClient-0.1.0-b90-dev-send-stream.ipa`, SHA `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`.
- Independent package inspection confirms Release `0.1.0 (90)`, Candidate b90, source `99f1aa15ce49`, MinimumOSVersion 14.0, iPhone/iPad family and Mach-O arm64; sidecar SHA matches.
- Evidence ladder: **Code written / guarded scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**
- Human Runtime gate: after one explicit Sync on a deliberately long externally active response, b90 must prove `manual_sync_frontmost_ab` with `visibleSiblingCountAbove=0`, then determine whether the official page itself begins matching `stream_status` / `/resume` / snapshot continuation without another Sync.

## DEV-send-stream b89 decisive interactivity-negative Runtime override — 2026-09-03

- Exact b89 identity remains `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)`, product `f39bc9387575028d431b85409780a2f3670b3259`, package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676`, Artifact `9881665748`, IPA SHA `c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`.
- Exact iPhone/iOS17 Runtime is decisive: after manual Sync/rearm, covered Web had `isUserInteractionEnabled=true`, non-empty/intersecting key-window bounds, then `nativeFirstResponder=true` and `documentHasFocus=true`, but emitted zero matching page-owned `stream_status`, `/resume`, SSE or external snapshot continuation.
- The same external response advanced only when manually re-Synced: authoritative live timeline `5 -> 28`, tools `4 -> 25`, reasoning `1 -> 3`. Therefore interactivity is rejected as a sufficient condition for automatic continuation. Manual authoritative Detail block projection remains Runtime Positive.
- b89 also recorded `subviewIndex=0` / `visibleSiblingCountAbove=1`; the next isolated causal A/B is genuine frontmost presentation/occlusion, not a route/status/resume/polling workaround.

## DEV-send-stream b89 package-ready override — 2026-09-03

- Exact Runtime candidate is now `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)`. Product commit `f39bc9387575028d431b85409780a2f3670b3259`; exact product/config package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676`.
- Guarded staging `33722656297 / 100544857329` passed exact patch, `git diff --check` and Xcode 16.4 Simulator compile. Formal Push `33725042383 / 100552047445` and PR `33725044367 / 100552051932` both passed.
- Canonical Push Artifact `9881665748`; Artifact ZIP `sha256:2e383a6328f801dd754d6858c3b9a8b71be5d5765a9a612d497b18c91b73988f`; IPA `sha256:c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`. Independent unpacking confirms Release `0.1.0 (89)`, Candidate b89, source `fe45aeadf7ae`, iOS14 minimum and Mach-O arm64.
- b89 changes only covered `WKWebView.isUserInteractionEnabled=false -> true` plus privacy-safe automatic `navigator.userActivation` booleans; b88 focus/rearm, route, continuation protocol, Send and Repository ownership are unchanged. Runtime/manual remains Pending; Stable/Frozen Send remains No.
## DEV-send-stream b82 current Runtime override — 2026-09-02

- Exact current tested package: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`, product/config source `c7a274786dfd175e8f476fc15c4964840e112a1d`, Artifact `9811406038`, IPA SHA `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`.
- iPhone/iOS17 Runtime is Partial: automatic final refresh works without manual Sync, but the remote user message and assistant answer remain absent until the current user-socket completion/update signal arrives; no active external response was acquired before completion.
- b80 spacing + external stopped-thinking semantics remain Frozen. Cross-platform request acknowledgement/progressive stream remains open. b39-b82 are permanently reserved; b83 is not allocated.

## DEV-send-stream b75 current Runtime override — 2026-09-01

- Exact current package remains `DEV-send-stream-0.1.0-b75` / `0.1.0 (75)`, product/config source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, IPA SHA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`.
- Exact iPhone/iOS17 Runtime is **partial/rejected**: pre-accept resume validation fixed the false Native failure, but three matching page-owned `/backend-api/f/conversation/resume` attempts returned HTTP404 JSON while the external response was still active, so no Native live reasoning/tool/final stream was adopted.
- b75 cooperative history geometry scheduling is executing; worst-case Back responsiveness remains unclosed by the supplied run.
- b75 tool/reasoning/final line-height values `26 / 18.2 / 18.2` are implemented but visually rejected as too tight by the latest Runtime screenshot.
- b39-b75 are permanently reserved. b76 is permitted by concrete b75 defects but **not allocated** before the current Web Rule Lab continuation re-probe resolves the transport rule.

## Initialization

**Initialized — 2026-08-25; refreshed 2026-09-01 through accepted b67 production transport Runtime, positive b72 tested cross-conversation simultaneous-generation Runtime, exact b73 Runtime defect evidence, and exact b74 Code/scope/Simulator/Push+PR CI/Artifact/package verification.**

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

- Native navigation shell / production covered-Send/continuation orchestration: `AppDelegate.swift`, `RootViewController.swift`.
- Persistent auth-secret authority: default persistent `WKWebsiteDataStore` only.
- Native auth/account authority: `Authentication/AuthSessionStore.swift`.
- Production native conversation/list/read/recovery/**response lifecycle** authority: one `ConversationRepository` in `Conversation/ConversationFeature.swift`; optimistic local-Send state and external page-resume adoption both feed the same per-conversation Repository response runtime. b74 adds only derived resident-geometry reuse and no second message/response authority.
- Conversation-list persistence: `ConversationListCacheStore`, storage-only behind Repository authority.
- Native conversation presentation: `ConversationDetailViewController`.
- Stable long-message geometry: `ConversationMessagePresentationProjection` + `ConversationMessageCell`, exact b38.
- Covered official Web executor: `CoveredWebSendExecutor`; browser challenge/protected-Send plus page-owned matching continuation observation only, never conversation/message/response authority. b74 may clone/parse the official page's own matching `/backend-api/f/conversation/resume` SSE but never constructs that request or offset.
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

## Exact b74 current Candidate

Build74 is the exact Runtime candidate produced from concrete b73 real-device defects plus the current Web Rule Lab cross-device continuation evidence.

Identity: Candidate `DEV-send-stream-0.1.0-b74`, `0.1.0 (74)`, exact product/config source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`; final clean-reassembly `33420128454 / 99580192017` success; Push `33420408779 / 99581104920`; PR `33420412792 / 99581117817`; canonical Artifact `9768668727`; ZIP `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`; IPA `sha256:07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`; independently unpacked package source marker `50dd61b8b31c`, Release, iOS14 minimum, arm64, iPhone/iPad family. Evidence: Code/scope/Simulator/Push+PR CI/Artifact/package verified; **Runtime pending**; Stable-Frozen No.

b74 preserves b38 deterministic geometry semantics while reusing already-derived historical geometry only for unchanged resident presentation identity, increases main tool-row vertical rhythm, and adds external active-response adoption by observing only the official page's own matching `/backend-api/f/conversation/resume` SSE. Native does not create the resume request, offset, stream-status polling or a second response store.

## Current product interaction target

Native response behavior should follow verified service events:

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次思考/思考流 -> reasoning_ended -> 折叠思考 -> 完整最终回答`.

Tool phases remain optional. `assistant:thoughts` is never presented. General Markdown/code/table/link/citation rendering remains future `DEV-message-rendering`; final Composer hierarchy/dynamic input/drafts/attachment staging remain future `DEV-composer-parity`.

## Current next Candidate boundary

Build75 is the latest exact real-device Runtime package and is partial/rejected for the evidence above. b39-b75 are permanently reserved. The current human-only gate is a Web Rule Lab structural re-probe of page-owned `stream_status` / matching `/resume` ordering and statuses while another platform owns an active response. Do not allocate b76 until that transport evidence is captured and the larger reasoning/tool/final vertical-rhythm correction is one coherent scope.

## Remaining Unknown / Unverified

Exact b74 Runtime for resident-geometry reuse, external active-response adoption and tool spacing; new-chat authoritative identity timing, server Stop mechanism, broader cross-conversation/service concurrency beyond the exact b72 A/B test, connector detail beyond the evidenced GitHub mapping, Native-constructed first/exclusive resume, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, Candidate identity, deployment/runtime, state ownership, accepted baseline or validation evidence changes.