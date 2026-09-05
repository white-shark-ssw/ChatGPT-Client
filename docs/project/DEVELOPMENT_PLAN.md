# Development Plan — Native iOS ChatGPT Client

## DEV-send-stream b93 selection-focus Runtime gate — 2026-09-03

- Exact b92 Runtime is Partial: covered external continuation works and client-owned protected Send/SSE natural terminal reconciliation works, but when an external live executor overlaps a second client-owned Send, the first stream can stop advancing and does not recover merely by reselection; explicit Sync later materialized the already-completed assistant.
- Exact b93 tests one evidence-backed variable only: when reselecting an already-active external response, reuse the existing covered executor and restore WKWebView first-responder/document focus without reload or Sync.
- b93 identity: allocation `b86c1a3ca94b215204b0cfb135fa0cd8b3603619`, product `556bd8886061f4126d11e4ac44f4e24ed580500c`, package source `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0`, Push `33755063112/100647405265`, PR `33755067202/100647418537`, Artifact `9893141097`, IPA SHA `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d`.
- b93 package inspection: `0.1.0 (93)`, Candidate `DEV-send-stream-0.1.0-b93`, source `2d2cde58a7fb`, iOS14+, `[1,2]`, iphoneos, arm64. Human Runtime pending; Stable/Frozen Send No.
- Preserved boundary: official page owns continuation transport, Repository owns Native content. No polling/retry/watchdog/timer, Native status/resume synthesis, guessed offset, duplicate Send, WebSocket-body authority, or second response store.
- Next exact action: install exact b93; reproduce external A -> local B Send -> reselect A without Sync; require selection focus rearm and resumed page-owned continuation through natural final.

## DEV-send-stream b92 covered-form package-ready override — 2026-09-03

- b91 project-scoped route identity and official page-owned live continuation are Runtime Positive; Native progressive projection works without a second Sync. Natural terminal/final remains Unverified because b91 was force-quit while still streaming.
- b92 is one isolated presentation cleanup only: it removes the b90 `bringSubviewToFront(webView)` z-order mutation and retains the b91 scoped-route parser, page-owned continuation observation, protected Send ownership, and `ConversationRepository` response authority. Manual Sync records `manual_sync_covered` but does not promote the WebView.
- Candidate / Build: `DEV-send-stream-0.1.0-b92` / `0.1.0 (92)`, permanently reserved. Allocation checkpoint `296de318c20ccc32bfea1cb93246bd9d824d3403`; exact product `96ea3e3d8c5cabf67ff33331d40c9dcc6c9f0850`; exact product/config package source `54b5803a74a123431f0a2a8e662a1a2fe874b3ca`.
- Two earlier staging runs `33749925741` and `33750233706` failed in guard-only tooling before checkpoint/product application. Successful guarded staging `33750363774 / 100632281401` passed exact b91-state guard, exact two-product-file scope audit and Xcode Simulator compile.
- Formal Push CI `33750585725 / 100632980237` and PR CI `33750591494 / 100632998279` both passed on the b92 package identity.
- Canonical Push Artifact `9891430379`; Artifact digest `sha256:f3cb6291fabcb2cf48729750d23a4403607e8ac81dc4354749974e287412e970`; IPA `ChatGPTClient-0.1.0-b92-dev-send-stream.ipa`, independently recomputed SHA-256 `82d96d359767b72c623f367bf3cd2c5f3ae9d1d7411ad547c1ba3634341c3514`, matching sidecar.
- Independent package inspection confirms Release `0.1.0 (92)`, Candidate b92, source `54b5803a74a1`, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, `iphoneos`, Mach-O 64-bit arm64.
- Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**
- Human Runtime must use a project conversation, one explicit Sync only, keep Native UI visible, prove covered `manual_sync_covered` + `route=conversation` + page-owned live continuation without a second Sync, then allow natural completion and verify terminal/final convergence before exporting diagnostics.

## DEV-send-stream b91 project live-continuation Runtime Positive override — 2026-09-03

- Exact b91 Runtime on iPhone / iOS 17.0 matches Candidate `DEV-send-stream-0.1.0-b91`, Build 91, source marker `c5985f1e2e5d`.
- Project route identity is Runtime Positive: every recorded `coveredExecutor.pageActivation` remained `route=conversation`; the prior scoped-project degradation to `route=other` did not recur.
- After one explicit Sync established the active authoritative response, the official page itself issued matching `stream_status`; HTTP200 repeatedly returned `IS_STREAMING`, `externalStreamingObserved` fired, and the page-owned `/resume` offset 0 returned HTTP404 JSON before the already-existing page-owned read path continued via `stream_status` plus plural conversation snapshots.
- Web -> bridge -> `ConversationRepository` live progression is Runtime Positive without a second manual Sync: external snapshots advanced from service messages/tools `6 / 2` to `47 / 14`, while reasoning characters advanced `194 -> 909`; Native live presentation was repeatedly applied.
- The user-visible inability to return from the official Web page is explained by the intentionally retained b90 diagnostic `bringSubviewToFront(webView)`. It is a presentation artifact, not a continuation failure; source has no balancing send-to-back in that diagnostic path.
- The app was force-quit/relaunched while the response still reported `IS_STREAMING` and `finalCharacters=0`, so automatic terminal/final convergence remains Unverified in this run.
- Evidence ladder: **Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; project route identity Runtime Positive; page-owned live continuation Runtime Positive; Native progressive projection Runtime Positive; terminal/final Unverified; Stable-Frozen No.**
- Next exact product action: retain b91 route parser and continuation observation, remove only the b90 frontmost diagnostic so the executor remains covered, then validate live progression plus natural terminal/final completion. Do not add retry/polling/timer/watchdog/Native resume or status synthesis.

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

_Last updated: 2026-09-01 through exact DEV-send-stream b79 Code/static/Simulator/Push+PR CI/Artifact/package verification; the next gate is b79 real-device Runtime._

## Current DEV-send-stream b79 gate — 2026-09-01

- Exact candidate `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)`; source `a3d307b05d70e95568672bc29b0c939b7f3b8141`; Push `33489654106 / 99797864816`; PR `33489658656 / 99797878467`; canonical Artifact `9793240789`; IPA SHA `39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`.
- b79 implements only the b78 Runtime-backed corrections: neutral reasoning/tool transition spacing, explicit-manual-Sync same-page re-arm after a changed latest user turn, and preservation of external stopped-thinking reasoning instead of synthesizing final body text.
- External reasoning/tool continuation remains page-snapshot granular. External progressive final still has no authorized progressive source; do not fake it. Automatic Sync remains future evidence work and must not be implemented as fixed polling.
- **Next gate is Human Runtime:** verify symmetric tool spacing, manual Sync adopts an already-open conversation's newly-started external response, stopped external reasoning displays as stopped reasoning rather than body text, and retained b67/b72 behavior where practical. Stable/Frozen remains No.

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client while preserving one authority per state domain. Current real source, exact CI/Artifact evidence, exact-device Runtime evidence and the latest explicit requirements outrank stale plans.

Core rules: no speculative retry/fallback/timer/watchdog/polling/duplicate state; distinguish Code / static-local / CI / Artifact / Runtime / Stable; private Web behavior must be measured rather than guessed; full Web conversation rendering remains rejected as the daily-chat dependency.

## Accepted merged foundation

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for recorded scope.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic evidence.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is native conversation authority.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23; Frozen No.
- Phase 8 `DEV-conversation-round-count`: merged Stable b38; exact tested product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.

Retain b38 bounded long-message chunks, deterministic geometry/manual layout, full-message Copy semantics, semantic rounds and continuous O(1)-target round navigation.

## Phase 9 — `DEV-send-stream` — Active production integration

### Current b76 candidate / next gate — 2026-09-01

- Exact candidate `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)`; source `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71`; Artifact `9775920927`; IPA SHA `b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd`.
- Guarded scope/Simulator passed; Push `33440101178 / 99645927061` and PR `33440098527 / 99645917529` passed; package identity independently verified.
- Current external-response design observes only page-owned status/plural reads after current resume 404, validates target identity and atomically projects the latest-user-bounded service segment into the Repository response owner. No Native polling/cadence/resume construction/WebSocket body path. Actual HTTP200-SSE page-owned resume remains supported under strict validation.
- b76 also tests 30/21/21 vertical rhythm.
- **Next gate is Human Runtime:** cross-platform active-response adoption, b67 local Send regression, b72 concurrent-ownership regression, visual spacing, and worst-case Back responsiveness if reproduced. Stable/Frozen remains No.

### Durable authority / transport boundary

- `ConversationRepository` remains the sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole native auth/account owner.
- `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority.
- b42 proves ChatGPT-account protected Send requires browser anti-abuse challenge output; pure-native/transient-auth protected Send remains blocked.
- TD-029 is the current production architecture: Native action -> Repository response operation -> covered official page performs exactly one protected Send/challenge flow -> same-response accepted SSE -> Repository incremental reasoning/tool/final state -> Native presentation.
- Covered official Web is transport/challenge execution only. It is not a conversation/message/response/list/draft/scroll-state authority.
- Native must not solve/synthesize/replay Sentinel/PoW/Turnstile/conduit/challenge values.
- Full official-Web conversation rendering and the b44 Native->Web->Native daily-chat form remain rejected.
- Final Composer hierarchy/drafts/attachment staging remain future serialized `DEV-composer-parity`; this Work retains only the minimum validation UI required to accept Send/response semantics.

### Accepted protocol / parser progression

- b45 Runtime Confirmed official no-resend continuation behavior; b46/b47 duplicated Native Cookie+Bearer-only resume remained rejected.
- b48-b51 established Native composer -> official protected Send and compact response text continuation, including exact `title_generation` preservation.
- b52-b60 established visible reasoning/final classification, exact `reasoning_ended`, service-marked thinking preambles and exact result-parent association. `assistant:thoughts` remains non-presentational.
- b61/b62 rejected generic textarea readiness and accepted only the evidenced composer path.
- b63-b65 authorized the narrow exact-parent GitHub tool-detail mapping and passed the focused diagnostic Runtime gate.
- b67 accepted the production existing-conversation TD-029 transport: one Native Send -> one official protected `/backend-api/f/conversation` -> HTTP200 `text/event-stream` -> Repository reasoning/tool/final -> terminal/reconcile.
- b72 exact Runtime positively supports the tested A-generating + B-send/generate simultaneous-generation ownership path. This is evidence for that exact matrix, not a claim about arbitrary overlap.

### b73-b75 daily-chat / external-continuation progression

- b73 retained successful local Send while exposing long resident geometry rebuild cost, insufficient tool vertical rhythm and the external-active-response lifecycle gap.
- b74 packaged first external active-response adoption based on historical visible-Web evidence that the official page can issue matching `/backend-api/f/conversation/resume` SSE. Its Runtime exposed false external failure before response validation and additional geometry/presentation defects.
- b75 added the required response-acceptance gate and cooperative presentation-geometry scheduling while preserving b67 local Send and b72 tested multi-conversation ownership.

### Exact b75 identity / evidence

- Candidate: `DEV-send-stream-0.1.0-b75`
- Version / Build: `0.1.0 (75)`
- Exact product/config source: `b77303b8870dc25851dbffbf38ffc153a47bbcb2`
- Assembly validation: `33429163152` — exact scope + `git diff --check` + Xcode 16.4 Simulator build passed
- Push CI: `33429597213 / 99611443839` — success
- PR CI: `33429599704 / 99611451360` — success
- Canonical Push Artifact: `9772079468`
- Artifact ZIP: `sha256:6c4c4ec9de54264846376bdf7df4679daaaf33168481831698c884093b6209ad`
- IPA: `ChatGPTClient-0.1.0-b75-dev-send-stream.ipa`
- IPA SHA: `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`
- Independent package inspection: Release `0.1.0 (75)`, Candidate b75, source marker `b77303b8870d`, minimum iOS14, arm64
- b39-b75 are permanently reserved.
- Evidence ladder: Code / exact static-local / Push CI / PR CI / Artifact / package identity passed; exact Runtime partial/rejected; Stable/Frozen Send No.

### Exact b75 iPhone/iOS17 Runtime qualification

Positive evidence:

1. **False external failure suppression passed.** A page-owned matching `/resume` request no longer creates a Repository external response before exact HTTP200 `text/event-stream` acceptance. The observed 404 cases therefore did not surface the former false Native `回答失败`.
2. **Cooperative geometry path is active.** Cache misses report `geometryMode=cooperative_main_queue`; resident reuse reports `geometryMode=resident_cache`, `geometryReused=true`. This run does not prove the former worst-case Back responsiveness because that extreme case was not reproduced.

Rejected / open evidence:

1. **Cross-platform active-response adoption failed in covered production.** While another platform's response was still actively reasoning, entering the same conversation in Native, Sync, Reload, background/foreground and process relaunch never produced Native live reasoning/tool/final rows. `livePresentationRowCount` remained 0.
2. In three separate covered-production attempts the official page itself issued a matching `/backend-api/f/conversation/resume`, but every observed response was HTTP404 `application/json` rather than an accepted SSE response.
3. Authoritative Detail later advanced visible messages, but server-backed reconciliation is not a substitute for live reasoning/tool SSE.
4. b75 typography values tool `26`, reasoning `18.2`, final `18.2` were implemented but visually rejected by the latest exact screenshot/feedback as too tight. Those numbers are not an accepted presentation baseline.

### Current Web Rule Lab evidence gate before b76

Historical visible-Web evidence showed `stream_status` HTTP200 and a page-owned `{conversation_id, offset}` resume returning HTTP200 SSE. Exact b75 covered production contradicts any assumption that this visible-Web behavior automatically applies to the covered executor.

Therefore the next step is evidence-only, using Settings -> Web Rule Lab on the same logged-in `.default()` WebKit store while another platform owns a still-active response. Capture only privacy-safe structural facts:

1. whether page-owned `GET /backend-api/conversation/{id}/stream_status` occurs and its status/content-type;
2. count/order of matching page-owned `/backend-api/f/conversation/resume` attempts;
3. resume request JSON key names only plus each response status/content-type;
4. whether any later page-owned HTTP/SSE transport follows an initial resume 404;
5. WebSocket remains structural-only unless separate exact evidence proves reasoning/final body authority.

Do not capture Cookie/Authorization/challenge values, raw account/conversation/message/response IDs, prompt/answer/reasoning bodies or tool bodies. Do not send a message from the Lab for this probe.

Until this evidence arrives, do not add Native resume/offset construction, `stream_status` polling, retry/timer/watchdog, guessed alternate route fallback, duplicate Send, delayed resend or WebSocket body parsing.

### b76 allocation rule

b76 is permitted by concrete b75 defects but remains **unallocated**. Allocate `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` only after:

- the Web Rule Lab evidence defines one minimal current continuation-transport correction;
- the rejected reasoning/tool/final vertical rhythm has one coherent visual correction;
- a fresh identity/conflict guard confirms b76 remains globally unused.

Then make one evidence-backed product change set, run static/local checks, Push/PR CI, independently verify package identity, and hand one exact b76 Artifact to the user for real-device Runtime. CI/Artifact success is not Runtime proof.

### Shortest remaining Phase 9 sequence

1. resolve the current external active-response continuation rule from Web Rule Lab evidence and, if justified, ship one b76 correction together with the already-evidenced visual-spacing correction;
2. re-accept local b67 Send and tested b72 A/B ownership regression paths on the coherent candidate as affected;
3. new-chat first Send and pending->authoritative handoff only if actual timing requires it;
4. establish exact server Stop evidence before implementing response-scoped Stop;
5. close A/B hidden-response ownership + follow-tail/history intent and Sync/Reload active-response safety;
6. run final b38 geometry/round/time/Copy regression plus daily-chat Runtime matrix;
7. final target-main synchronization, fresh CI/Artifact if tested code changes, Stable/merge decision for PR #29.

### Official-like response lifecycle target

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次正在思考/思考流 -> reasoning_ended -> 自动折叠思考 -> 完整最终回答`.

Tool phases remain optional and must follow actual service events. General Markdown/code/table/link/citation rendering remains future `DEV-message-rendering`.

### Background ordering

Background resilience remains a hard product requirement but follows accepted production response ownership. b45 positive short-background evidence remains historical support; full 5/15-minute, WebContent termination, network-transition and TrollStore true-background work remain later isolated Runtime gates. Do not create a second response owner merely for background continuation.

## Future serialized `DEV-composer-parity`

After current Send/Stream lifecycle acceptance, implement the final official-like Composer hierarchy: bounded multiline auto-growth/full-screen editor, keyboard/layout behavior, per-conversation drafts, photo/video/file staging/preview, mode/reasoning controls and final Send/Stop button presentation. Do not move Send/response authority out of `ConversationRepository`.

## Phase 10 — `DEV-attachments`

High priority but Send-boundary dependent. Preserve iOS17 native photo+video requirements; do not use unsupported private WebKit/DOM file-input injection. Native upload/handoff needs separate current evidence.

## Phase 11 — `DEV-message-rendering`

Implement native Markdown/code/table/link/citation presentation only from authoritative user-visible content; never expose hidden reasoning/tool/system content.

## Later phases

Conversation-list preview, Markdown export, long-conversation profiling beyond accepted b38 geometry, download manager, pagination, production background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement and later advanced capabilities remain isolated Works.

## Current next action

Keep PR #29 open/unmerged and exact b75 as the current rejected Runtime package. Perform the privacy-safe Web Rule Lab continuation re-probe described above. Do not allocate b76 and do not change production continuation code until that Human Gate returns current page-owned transport evidence.

## 2026-09-03 — b92/b93 page-owned continuation loop interruption

Exact b92 single-executor Runtime proves that a background lifecycle transition can stop the official page-owned `stream_status`/snapshot loop even without another executor. Exact b93 proves successful first-responder/document-focus reacquisition does not necessarily restart a stopped loop. The next isolated candidate is foreground official-page rebootstrap without Native Detail Sync; selection rebootstrap remains separate. Stable/Frozen Send remains No.
