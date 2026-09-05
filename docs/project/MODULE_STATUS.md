## DEV-send-stream b109 chunk-color diagnostic package qualification — 2026-09-06

- UI behavior is unchanged from b108; b109 only exposes privacy-safe final color state for each chunked assistant cell at `willDisplay` so blue/normal authoritative chunks can be compared with their actual UILabel/attributed/highlight/tint/selection state.
- `ConversationRepository`, covered Send executor, New Chat authoritative handoff, b107 accepted-client recovery, row geometry and message content authority are unchanged.
- Exact product `11e7ec536b986c45811dc449cd2c4f6e442c28df` / package `8c6ea43677f2a0f39c08d6b9ca695c9c2e4a5267` passed corrected staging and same-source Push + PR packaging; canonical Artifact `9974791883` / IPA `6c37dfb8496c533ce2d5e4878f22a5b265f7c55e87e9cbfbb9189155fa30096a` is verified.
- Diagnostic Human Runtime remains Pending; module remains Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b108 chunk-row color Runtime Negative / b109 probe — 2026-09-06

- Repository/Send/recovery owners remain unchanged. b108 normal New Chat transport, terminal, and authoritative reconcile are Runtime Positive in `sha256:c26f5ed8712ca63c8dae037e58330d5fa4b2f7cb47b8b0dafc078e920b4c813c`; accepted clean-EOF recovery remains Unexercised.
- UI evidence is now chunk-row-specific: completed authoritative state has 6 presentation rows / 0 live rows, and video `sha256:6cecee7a5f249529c72c53ee08620740e9d8480b080d8914476f697ad0efdc73` shows one assistant message alternating blue/normal between long-message chunks. b108's final UILabel `textColor=.label` assignment is insufficient.
- b109 is diagnostic-only and will audit each chunk cell's resolved UILabel/attributed/highlight/tint state from `willDisplay`; rendering behavior itself must remain unchanged.
- Module remains Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b108 package qualification — 2026-09-06

- UI delta is confined to `ConversationMessageCell.messageLabel`: assistant body attributed text is assigned first, then UILabel `textColor=.label` becomes the final uniform body-color owner. Separate `reasoningTextView`, user links and response timeline styles are unchanged.
- `ConversationRepository`, covered Send executor, New Chat authoritative handoff and b107 accepted-client recovery owners are unchanged.
- Exact product `eb0de74460b0bd06a6d977bf915b5e06a5c946db` / package `d34ff4534ca76ee03e2c8a3eeddb29eca011319f` passed guarded Simulator staging and same-source Push + PR packaging; canonical Artifact `9973988017` / IPA `a2639b5793316077c0f203bfd4dffdecd8cef74c361a4995bc8bfba05f657dbd` is verified. Runtime color correction remains Pending.
- Module remains Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b107 UI-owner Runtime update / b108 allocation — 2026-09-06

- `ConversationRepository` / covered Send transport remain unchanged by the new defect evidence. b107 normal New Chat Send/terminal/authoritative convergence is Runtime Positive in `sha256:8e3e10b44e8e627f60e7a831d48f11c7fa9fff4bc4b0446b71588fbc38ade7da`, but its exact accepted `stream_ended_without_done` recovery branch remains Unexercised.
- UI ownership is now narrower: assistant placeholder/final body uses `ConversationMessageCell.messageLabel` (`UILabel`), while reasoning SSE text uses `reasoningTextView` (`UITextView`). User Runtime reports body blue / reasoning normal and supplied screenshots reproduce final body blue. b106's pre-assignment `messageLabel` reset did not fix it.
- b108 is reserved for the smallest body-rendering correction: reassert assistant `messageLabel.textColor = .label` after its attributed body assignment; do not change reasoning, user-link coloring, row geometry, Repository, SSE, or recovery ownership.
- Module remains Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b105 new-chat authoritative identity handoff — 2026-09-05

- `ConversationRepository` remains sole Native conversation/response/content authority; `CoveredWebSendExecutor` remains official-page protected-Send transport. b105 adds no second store and no fake persisted conversation identity.
- New Chat draft starts with no selected server ID. The official root page may submit only after its own route yields the real conversation ID; then the same executor is re-keyed and exactly one Repository live generation is created for that real ID. Successful terminal Detail triggers one authoritative list refresh so the server-created conversation enters the sidebar.
- Exact product/package `6ef4e874d7c2c5f144ab7e784f7a81755d1b2f59` / `93ab92a9a4a7b8a020ac209f6a82088dc77acbce`; staging + Push + PR CI passed; Artifact `9956018294`; IPA `sha256:d162a7132ff830d3a2f6eb85a2b4a5b4ebc2d9f84531b01418912c99109e5095` independently verified. Human Runtime pending; module remains Active / Runtime Partial overall / Stable-Frozen No.

## DEV-send-stream b104 ordinary/background-return Runtime Positive — 2026-09-05

- `ConversationRepository` remains the sole Native response/content/reconciliation authority. Exact b104 Runtime `sha256:3789dc478c0bdf46c0f2ca2f572ebc618b4f53299e39fe68086e6dc936387216` has one accepted protected Send, no test kill instrumentation, no duplicate Send, and one generation through terminal + authoritative Detail `21 -> 23` reconciliation.
- After ~96s background, queued covered-response events were delivered on foreground and the completed live answer appeared before the one-shot authoritative sync completed. The subsequent loading indication is consistent with that automatic reconciliation, not a second generation or resend.
- Background execution itself is not proven: there is a long interval with no response events while suspended. Module remains Active / Runtime Partial overall / Stable-Frozen No because separate background-execution and b101 `-1005` evidence boundaries remain open.

## DEV-send-stream b104 no-probe accepted-client recovery — 2026-09-05

- `ConversationRepository` remains sole Native response/content/lifecycle authority. b103 Runtime `sha256:99049f500c129571d33aa628720f7d23ce5cf6d183e887938cd7fa621a3bbc51` proves the accepted-client hard-Web handoff keeps one prompt-owned generation through death, fresh covered observation, resume/live terminal and authoritative reconcile with no second protected Send.
- b104 keeps that recovery implementation unchanged and removes the deterministic kill instrumentation completely. No test timer/private WebKit kill SPI ships in this normal candidate.
- Exact product/package `4aebb546f3be6b71de0a67f466e6557a357dbfdc` / `08fab73ab9a6fb83f6aa97702d2d4cd358b6ec43`; staging + Push + PR CI passed; Artifact `9953695815`; IPA `sha256:9c35141e9877621d3a7e39245982cba6722acbb17a19f5ebabd8734d2b94df04`; package identity independently verified. b104 ordinary Runtime pending; module remains Active / Runtime Partial overall / Stable-Frozen No because separate background/silent-stall and other open gates are not collapsed into this result.

## DEV-send-stream b103 accepted-client hard-Web recovery — 2026-09-05

- `ConversationRepository` remains sole Native response/content/lifecycle authority. b103 does not create a second response object when the covered WebContent process dies after Send acceptance; the existing prompt-owned generation remains active and receives the fresh covered observer's already-evidenced external continuation events.
- `CoveredWebSendExecutor` now distinguishes explicit accepted-client transport death from pre-acceptance failure. Accepted-client death emits `acceptedClientWebProcessInterrupted`, clears only the dead executor transport state, and Root replaces it with one observer for the same conversation/generation. No protected Send is repeated.
- b102 Runtime proves the server-turn survival/no-second-Send premise. b103 exact product/package `d514e9a5bde01bf3243d81016bf8cbda533fd5bf` / `e1cca160e9c466ab98a2aeffc038e94f58335cab`; staging + Push + PR CI passed; Artifact `9952548424`; IPA `sha256:f41c81a89552027fb4c42152eb3864c1732494465230ffd4787c6bba56d746c3`; package identity verified. Recovery Runtime pending; module remains Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b102 deterministic client-owned WebContent-death probe — 2026-09-05

- `ConversationRepository` remains sole Native response/content owner and `CoveredWebSendExecutor` remains the protected-Send Web transport. b102 adds no recovery owner or alternate transport.
- Exact b102 installs one Candidate-gated diagnostic probe: first covered submit arms one 120-second main-queue action and then requests WebKit to kill/reset only that covered WebContent process. Current `webViewWebContentProcessDidTerminate` handling is intentionally unchanged: external observation may rebootstrap under b98, while client-owned Send still fails and is never replayed.
- Push+PR CI passed; canonical Artifact `9951331101`; IPA `sha256:53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`; Human Runtime pending. Module remains Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b101 Runtime qualification update — 2026-09-05

- `ConversationRepository` remains sole Native conversation/list/detail/recovery/response-lifecycle authority. Exact b101 Runtime `sha256:f7209546f3f2d1dd8ad08458b0dea8adbef522af100deb2f5de90cbe26180b9d` keeps the new `-1005` transport-renewal branch Unexercised because every authoritative Detail in the sample returned HTTP200 and no transport-recovery diagnostic occurred.
- The same sample closes two external-flow module gates as Runtime Positive: no-active unfinished remote discovery (`13 -> 14`, `rearmDiscoveredRemoteTurn=true`, covered `IS_STREAMING` + reasoning/tool snapshot) and known-active foreground final reconcile (`14 -> 15`, `authoritative_assistant_materialized`). A later ~17m35s dormant discovery also converged `15 -> 17` automatically.
- User WebSocket `close(1006)` occurred twice, but no `webViewWebContentProcessDidTerminate` signal occurred. Hard WebContent recovery and client-owned accepted-Send transport-death recovery remain separate Unverified gates; this sample contains no client-owned Send.
- Module remains Active / Runtime Partial / Stable-Frozen No. No b102 or product delta is authorized from this evidence alone.

## DEV-send-stream b101 Native read transport recovery override — 2026-09-05

- `ConversationRepository` remains sole Native conversation/list/detail/recovery/response-lifecycle authority. `AuthSessionStore` remains account authority and default persistent WebKit storage remains persistent auth-secret authority.
- Exact b100 Runtime proves the cached transient Native transport can remain stale after long suspension and repeatedly return `NSURLErrorNetworkConnectionLost (-1005)` even while covered Web networking reconnects. b101 fixes this at the transport owner rather than adding a second reader or lifecycle store.
- For conversation-list and Detail GET only, first exact `-1005` may retire the matching cached `AuthTransientSession`, reacquire one transient session through the existing auth path, and retry the same read once after scope/generation freshness checks. Any second error/failure terminates normally. Client-owned protected Send is untouched and never automatically replayed.
- Product/package `54a9fa52...` / `da103452...`; staging + Push + PR CI passed; Artifact `9948780963`; IPA `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`; Human Runtime pending; module not Stable/Frozen.

## DEV-send-stream b100 dormant foreground discovery Runtime Positive — 2026-09-05

- `ConversationRepository.syncLatestMessages` remains the sole authoritative foreground discovery primitive. Exact b100 Human Runtime `sha256:f0f3619ea61f30f9bcbaadbb577f3a99839a032dfcd95503e22b4a7bdb984696` proves the no-active-snapshot lifecycle path after ~19m31s background: one automatic Detail changed visible messages `8 -> 10` with no manual Sync/Reload and no second response authority.
- Completed remote state did not rearm Covered Web (`rearmDiscoveredRemoteTurn=false`). A later no-change foreground cycle also issued one Detail and remained `10 -> 10`.
- A user WebSocket `error/close(1006)` occurred on foreground and later reopened; the authoritative Detail path still converged first. No hard WebContent-process termination event occurred, so b98 hard-process recovery remains Unverified.
- Runtime acceptance is scoped to dormant foreground discovery. Unfinished remote-turn rearm, exact-b100 known-active reconcile regression and b99 backlog-coalescing stress remain Unverified; module is not Stable/Frozen.

## DEV-send-stream b100 foreground dormant-discovery override — 2026-09-05

- b99 Runtime: known-active external response auto-reconciled authoritative Detail `5->6` after ~7m32s background. After that response/executor was released, a later ~12m54s background interval had no automatic foreground discovery; manual Sync recovered `6->8`. b99 is Runtime Partial; its backlog-coalescing stress is Inconclusive in this sample; hard WebContent-death recovery remains Unverified.
- b100 changes only foreground discovery: selected conversation + no client-owned active response + no Detail operation => exactly one existing `ConversationRepository.syncLatestMessages`, even without a pre-existing external snapshot. Completed server state materializes directly; a newly discovered unfinished remote user turn may rearm the existing covered observer once.
- No polling/timer/retry/watchdog/background heartbeat/resend/guessed resume/second response authority.
- Exact product `70c7dc052865ef80ca7bdec083d7621c1a297eab`; package source `e88a50ad9c2098449b43fb0fce2c441a50cd20ac`; staging `33895020559/101095508915`, Push `33895244146/101096229135`, PR `33895249810/101096247432` passed; Artifact `9945483725`; IPA `sha256:5629deedca665b7a5cfa7e36b4996b7b1e4b7a160ca5cb35a465abfbd97fbc69`; Human Runtime pending; Stable-Frozen No.

## DEV-send-stream b99 backlog-presentation stability override — 2026-09-04

- b98 Human Runtime exact diagnostics `sha256:e0a0bd2c42168d0c3f8a6dd681bbad1bb571d4061b0f2958131cae5f8e059105`: no hard WebContent termination event occurred, so that new b98 branch remains Unverified. The included foreground authoritative Detail reconcile is Runtime Positive, but a later client-owned response replayed 170 buffered live events after ~5m background and drove 169 synchronous full presentation applications; user observed freeze/crash and a fresh `launch.start` followed 3s after the last live event.
- b99 is the evidence-scoped stability correction: preserve every Repository event/state transition, but coalesce only the expensive selected Detail UIKit presentation onto one pending main-queue application using the latest Repository snapshot. No timer, retry, watchdog, polling, transport mutation, Send replay or second response authority.
- b99 exact product `ec05c284010cb0f2de066bd1cfc3968e07730779`; package source `313c4c3bf2ac0dc729d4793198fe462ada5a14eb`; staging `33890678564/101081289220`; Push `33890809275/101081720750`; PR `33890812345/101081730258`; Artifact `9943798885`; IPA `sha256:68b7f99eac8fd1d3ab14c6085abd4a084f2b4759dc630f94044017c9a4aecf02`; Human Runtime pending; Stable/Frozen No.

# Module Status

## Send / Stream — b107 package-ready update 2026-09-05

- `DEV-send-stream` remains Active / Stable-Frozen No.
- b106 proved New Chat protected-Send SSE authoritative identity but exposed accepted clean-EOF false failure and stale-live double presentation.
- b107 is package-qualified for the narrow same-generation no-resend EOF recovery + authoritative stale-live cleanup gate. Blue assistant text remains a separate unresolved presentation defect and is not changed by b107.


## DEV-send-stream b98 hard WebContent recovery package-ready override — 2026-09-04

- `ConversationRepository` remains sole Native conversation/content/response-lifecycle authority. b98 does not create another response owner or Native continuation protocol.
- Covered Web now distinguishes a hard WebContent-process death during external observation from client-owned Send failure. External observation preserves its callbacks/current conversation/Repository live projection and reboots the same existing page once when active; inactive/background termination is deferred to existing foreground b97 Detail reconcile + page rebootstrap.
- Client-owned protected Send still fails on WebContent termination; no automatic resend/replay. Navigation failure semantics are unchanged. No silence timer/watchdog/retry loop was added.
- Exact product `2edd55febe2005071722ddcb9989151b427165d8`; package `17c65a390f2724a55cd29d466e01eaab988dcbfe`; staging `33886277311/101066715850` + Push `33886537405/101067576599` + PR `33886540813/101067587985` passed; Artifact `9942092070`; IPA `sha256:b1dc76dbe28e77ceac3468e8cfd3ca0ded41601bd02db6b228bd391a1d697b67`; Human Runtime Pending; Stable/Frozen No.

## DEV-send-stream b97 foreground reconcile package-ready override — 2026-09-04

- `ConversationRepository` remains sole Native conversation/content/response-lifecycle authority. b97 removes the b96 recurring Native Detail scheduler; the only new lifecycle action is one existing `syncLatestMessages` request when returning foreground with a selected active external live response and no Detail operation already in flight.
- Covered Web retains its foreground rebootstrap role if the one-shot authoritative Detail does not yet contain the final assistant. Existing Repository terminal reconciliation owns final projection removal; no second response store or Send path was added.
- Exact product `12fc1d1f5020d76d1892c25a0ced94323d5a0142`; package source `5e43c398b52a62de9f9a6e6546de7312ba5eb1df`; guarded staging/Simulator + Push+PR CI passed; Artifact `9940228423`; IPA `sha256:49f8d9a8ef425409923bf904a3134265ddfa6d90597d72e04a1e976a5a8a90c7`; Human Runtime Pending; Stable/Frozen No.
- True background execution/notification remains separate future scope; b97 only targets foreground-return convergence.

## DEV-send-stream b96 Native continuation package-ready override — 2026-09-04

- `ConversationRepository` remains sole Native conversation/content/response lifecycle authority. b96 adds one evidence-scoped external continuation loop only after authoritative Detail reports exact `IS_STREAMING`; exact `COMPLETE`/non-streaming terminates it, account reset cancels it, and client-owned response authority wins.
- Exact product `9e50943de39dc304ab31904cbad8596d4ffddc14`; package source `cd6268540e4f5a815829f26a713b10e8d1957239`; Push+PR CI passed; Artifact `9938422716`; IPA `sha256:a635903898324bdf0e59cf8712a2ebd5924def0da591d555fb25d2f62dabc361`; Human Runtime Pending; Stable/Frozen No.
- Official-App private callback Probe ladder is retired for this gate because injected packages are Runtime unstable; terminal re-entry recovery in official app is Runtime Positive.

## DEV-send-stream b93 selection-focus package-ready override — 2026-09-03

- Exact b92 Runtime is Partial: covered external continuation works and client-owned protected Send/SSE natural terminal reconciliation works, but when an external live executor overlaps a second client-owned Send, the first stream can stop advancing and does not recover merely by reselection; explicit Sync later materialized the already-completed assistant.
- Exact b93 tests one evidence-backed variable only: when reselecting an already-active external response, reuse the existing covered executor and restore WKWebView first-responder/document focus without reload or Sync.
- b93 identity: allocation `b86c1a3ca94b215204b0cfb135fa0cd8b3603619`, product `556bd8886061f4126d11e4ac44f4e24ed580500c`, package source `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0`, Push `33755063112/100647405265`, PR `33755067202/100647418537`, Artifact `9893141097`, IPA SHA `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d`.
- b93 package inspection: `0.1.0 (93)`, Candidate `DEV-send-stream-0.1.0-b93`, source `2d2cde58a7fb`, iOS14+, `[1,2]`, iphoneos, arm64. Human Runtime pending; Stable/Frozen Send No.
- Preserved boundary: official page owns continuation transport, Repository owns Native content. No polling/retry/watchdog/timer, Native status/resume synthesis, guessed offset, duplicate Send, WebSocket-body authority, or second response store.

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

## DEV-send-stream b89 package-ready override — 2026-09-03

- Build/runtime metadata: exact b89 product `f39bc9387575028d431b85409780a2f3670b3259`, package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676`, Candidate/Build `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)`.
- Guarded staging `33722656297/100544857329`, Push `33725042383/100552047445`, and PR `33725044367/100552051932` all passed. Canonical Push Artifact `9881665748`; ZIP `2e383a63...3988f`; IPA `c8ad5dce...21a55`; package independently verified as Release/source `fe45aeadf7ae`/iOS14/arm64.
- Covered official-Web continuation: b89 enables only `WKWebView.isUserInteractionEnabled` and records automatic user-activation booleans while preserving b88 focus/rearm and all page-owned continuation rules. Runtime continuation remains Unverified.
- Evidence ladder: Code/guarded Simulator/Push+PR CI/Artifact/package verified; Runtime Pending; Stable/Frozen Send No.
## DEV-send-stream b88 decisive focus-negative override — 2026-09-02

- Exact b88 identity remains unchanged: product `31d24e8b9ab4676effd757a793162abbdb0d7012`, clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`, Candidate/Build `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`, Artifact `9848999246`, IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`.
- Second real-device b88 sample is decisive: manual-Sync rearm produced `nativeFirstResponder=true` and `documentHasFocus=true`; the user then observed multiple additional PC tool rounds from the same remote generation while ChatGPTClient stayed on the six-tool snapshot and covered Web emitted zero `stream_status`, `/resume`, external SSE or page-owned snapshot.
- Focus is therefore rejected as a **sufficient** condition for continuation under the current direct full conversation navigation. This does not prove focus is universally irrelevant.
- Completed assistant still required explicit Sync (`visible 12 -> 13`, mapping `507`, trailing `0/0`, `authoritative_assistant_materialized`). Automatic final convergence remains rejected.
- Next evidence target is genuine official SPA/router conversation-entry behavior; causality remains Unverified. No b89 until one exact router-entry variable is evidenced. Stable/Frozen Send remains No.

## DEV-send-stream b88 focus Runtime override — 2026-09-02

- Known-good visible official Web can immediately acquire/live-continue a newly active cross-platform response and shows Stop while `document.hasFocus=true`; the coarse route probe is not conversation-state authority.
- b88 identity: exact product source `31d24e8b9ab4676effd757a793162abbdb0d7012`; clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`; Candidate/Build `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`; Push+PR CI passed; Artifact `9848999246`; IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`.
- Exact b88 Runtime proves the one-shot focus mechanism works: `nativeFirstResponder=true` and direct `documentHasFocus=true` after manual-Sync rearm.
- No `stream_status`, `/resume`, external streaming or snapshot followed in the supplied run, and final materialization still required another explicit Sync. However the response was already at the final tool phase; the last authoritative active Detail proof preceded focus by only ~1 second, so focus causality remains Inconclusive rather than Rejected.
- Reuse exact b88 for one earlier/mid-generation A/B. No b89/product change yet. Stable/Frozen Send remains No.

## DEV-send-stream b86 diagnostics / b85 Runtime override — 2026-09-02

- b85 identity: exact product source `ec64dd170a6386612af8cb68b394045ce3c85313`; Push/PR CI passed; Artifact `9822441595`; IPA `sha256:f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`.
- b85 real-device Runtime: explicit Sync reliably projected active authoritative Detail reasoning/tool timeline `1 -> 5 -> 7` on the same external response generation and final authoritative assistant materialization reconciled/cleared it. Manual block acquisition is Runtime Positive.
- b85 automatic continuation: Rejected for reliability. Covered page re-armed/loaded after Sync but no external streaming/snapshot/resume event appeared; each newer block required another explicit Sync.
- b86 identity: exact diagnostics product source `dc77a94be5b2f7eecd822480f759358ad6a0ad25`; Push `33566939415/100052171917` and PR `33566968066/100052259409` passed; canonical Artifact `9823485856`; IPA `sha256:25d483ac31473b124e6ad555b79c488e78da91ec1761ee8a40076b6e978bee6f`.
- b86 is diagnostics-only: matching page-owned `stream_status` request/HTTP/state and matching resume offset structure are logged without issuing any new request or changing acquisition behavior. Runtime pending.
- Client-owned Send remains true SSE; no Native guessed resume/offset, polling, timer, retry/watchdog, duplicate Send or hidden-thought presentation. Stable/Frozen Send remains No; b39-b86 reserved.

## DEV-send-stream b82 Runtime override — 2026-09-02

- Build/runtime metadata: exact b82 source `c7a274786dfd175e8f476fc15c4964840e112a1d`; Push/PR CI passed; Artifact `9811406038`; IPA `3ca16867...d6d2`; exact iPhone/iOS17 Runtime Partial.
- Covered external acquisition: b82 automatic Sync/re-arm fires without manual Sync, but only after the current user-socket target notification; the supplied run had authoritative visible messages 8 -> 10 at that point and no earlier live event. Treat this signal as completion/update only for the tested flow.
- Live cross-platform request acknowledgement/reasoning/final: still rejected/open. Do not fake progress or silently add polling/timers.
- b80 spacing and external stopped-thinking semantics remain Frozen. Stable/Frozen Send remains No; b39-b82 are reserved.

## DEV-send-stream b79 candidate override — 2026-09-01

- Build/runtime metadata: exact b79 source `a3d307b05d70e95568672bc29b0c939b7f3b8141`; guarded staging `33488975445 / 99795672696` passed exact scope + `git diff --check` + Xcode 16.4 Simulator; formal Push `33489654106 / 99797864816` and PR `33489658656 / 99797878467` passed; canonical Artifact `9793240789`; ZIP `20165080...e87fc`; IPA `39f64dd9...34fb4`; package independently verified as Release 0.1.0 (79), Candidate b79, source `a3d307b05d70`, iOS14 minimum, arm64. Runtime pending.
- Tool activity presentation: inter-item spacing now has one neutral separator owner instead of preceding reasoning/tool paragraph ownership; real-device symmetry remains the acceptance gate.
- Covered external continuation: explicit Sync detecting a changed latest user may reload/re-arm the already-current covered official page once, preserving the page-owned observation model and adding no polling/automatic Sync.
- External stop semantics: external terminal-without-final preserves reasoning/tools and uses stopped-thinking presentation; local protected-Send terminal fallback remains unchanged.
- External progressive final remains unavailable from the currently authorized source; b79 adds no fake stream, DOM body, WebSocket body, retry, timer, watchdog or second state owner.
- Stable/Frozen Send remains No; b39-b79 are permanently reserved.

## DEV-send-stream b78 candidate override — 2026-09-01

- Build/runtime metadata: exact b78 product/config source `031b1a1f2c1d01900c2ab79ff14b1f2fb6c7e809`; clean product commit `180065e0faf947292a9f21b56c4ea366a5c322fe`; final Xcode validation `33482721335 / 99775722851`; Push `33482983693 / 99776545604` and PR `33482987997 / 99776557269` success; canonical Artifact `9790836559`; ZIP `7b5900a9...b081f`; IPA `726e3c09...8620e`; package independently verified as Release 0.1.0 (78), Candidate b78, source `031b1a1f2c1d`, iOS14 minimum, arm64. Runtime pending.
- Conversation read/recovery: b77 diagnostics prove list HTTP403 cancelled the shared transient session and the selected Detail, then the cancelled Detail operation remained coalescible forever. b78 retires the transport without cancelling in-flight work and terminalizes current Detail cancellation; no retry/fallback/state-owner duplication.
- User-message presentation: b78 renders and measures from the same attributed representation, uses character wrapping, and supports inline-only Markdown semantics on supported OS versions; this targets the exact official-Web parity/truncation defect reported on b77.
- Tool activity presentation: b78 removes mixed paragraph-style ownership at reasoning/tool boundaries and treats tool icon/text/separator as one distinct tool paragraph presentation; visual prominence remains a real-device gate.
- External continuation: b76/b77 reasoning/tool adoption remains the accepted positive boundary. b77 DOM-structure evidence did not reveal final text before plural completion, so progressive final-body authority remains unresolved and no fake stream is added.
- Stable/Frozen Send remains No; b39-b78 are permanently reserved.

## DEV-send-stream b76 candidate override — 2026-09-01

- Build/runtime metadata: exact b76 source `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71`; Push `33440101178 / 99645927061` and PR `33440098527 / 99645917529` success; Artifact `9775920927`; IPA `sha256:b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd`; package independently verified as Release 0.1.0 (76), Candidate b76, source `0da5a7577f2c`, iOS14 minimum, arm64. Runtime pending.
- Covered external continuation: current official page may `/resume` -> 404, then use its own `stream_status` + plural conversation reads. b76 observes only that existing page traffic and atomically projects the latest-user-bounded service segment into `ConversationRepository`; no Native polling/resume construction/WebSocket body path.
- User-visible reasoning/tool/final: current probe evidence contains thinking preambles, exact-parent tools/results, reasoning recap/end and final in-progress/completed message structures. b76 Code/CI/Artifact is verified but device presentation remains unverified.
- Typography: b76 candidate increases 26/18.2/18.2 -> 30/21/21 while preserving the 0.70 relationship and shared measurement/rendering style.
- Geometry: b75 cooperative path evidence remains; worst-case Back responsiveness is still an open real-device gate if reproduced.

## DEV-send-stream b75 Runtime override — 2026-09-01

- Build/runtime metadata: exact b75 package verified; Runtime partial/rejected; b39-b75 reserved; Stable/Frozen Send No.
- Covered external continuation: b75 pre-accept validation works, but covered production page-owned matching `/resume` returned HTTP404 JSON in three observed active-response attempts. HTTP200 SSE adoption is therefore not a current production-proven path; Web Rule Lab re-probe is required before product changes.
- User-visible reasoning/tool/final: no external live rows were created in the supplied b75 run. Local b67 transport and b72 tested simultaneous A/B ownership remain accepted predecessors.
- Typography: b75 26/18.2/18.2 is visually rejected as too tight; next correction must increase visible vertical rhythm rather than merely assert those numeric values.
- Geometry: cooperative cache-miss path and resident reuse observed; worst-case Back responsiveness remains Runtime-unverified in this export.

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/START_HERE.md` | Checkpoint/evidence/conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline; Phase 9 integrated validation surface** | `AppDelegate.swift`, `RootViewController.swift` | Native shell/read/navigation remains product UI. Current branch adds TD-029 covered-Send orchestration + validation-only trigger without changing b38 message geometry. Final Composer remains future `DEV-composer-parity`. |
| Build/runtime metadata | **b74 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (74)`, exact source `50dd61b8...`, Artifact `9768668727`; b39-b74 reserved. |
| Diagnostics / logging | **Stable privacy contract** | `DiagnosticsLogger` | Prompt/answer/reasoning/tool bodies/raw IDs/auth/challenge values remain excluded. b66 Runtime evidence used only bounded lifecycle/count/state facts. |
| IPA build / CI packaging | **Stable capability; b74 Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33420408779/99581104920`, PR `33420412792/99581117817`, Artifact `9768668727`, ZIP `6ac4cc97...95cb3`, IPA `07c999fd...285da`; package independently verified as b74/source `50dd61b8b31c`/Release/iOS14/arm64. |
| Embedded Web login / persistent browser state | Stable authority | `AuthWebViewController.swift` + `WKWebsiteDataStore.default()` | Default persistent WebKit store remains sole persistent auth-secret authority. TD-029 covered executor and Web Rule Lab reuse it; no second store. |
| Authentication/account context | **Stable owner; b70 transient-403 behavior Runtime pending** | `AuthSessionStore.swift` | Sole native auth/account owner. Exact probe 403 preserves last verified identity while returning no fresh transport; 401 remains unavailable semantics. |
| Protocol-read transport | Stable read scope | transient auth + probes | Native read transport is not protected-Send executor and not incremental-response owner. |
| Official same-response resume | **Runtime Confirmed official-page continuation; b74 external adoption candidate** | official Web `/backend-api/f/conversation/resume` | b45/b47 proved no-resend continuation; 2026-09-01 Web Rule Lab additionally proves page-owned matching `{conversation_id, offset}` -> HTTP200 SSE on cross-device active-conversation entry. Native construction remains Unverified/rejected for current product path. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| Covered official-Web protected Send executor | **b67 local Send Runtime accepted; b74 page-owned resume observation packaged** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b67 passed protected Send -> HTTP200 SSE -> terminal/reconcile. b74 retains that path and adds observation of only the official page's matching `/resume` SSE for external active-response adoption; Runtime pending. |
| Full official-Web conversation UI | **Rejected as daily-chat product dependency** | TD-025/TD-028 | b44 full-page hybrid UX rejected; b47 long-conversation Web composer failure retained. TD-029 does not restore full-Web rendering. |
| Web Rule Lab | **Implemented / Runtime page-load observed b66** | Settings + visible `WKWebView` using `.default()` store | b66 diagnostics recorded Lab open/page loaded. Explicit execute only; temporary script/result; copy/share; no persisted body/log body; not a production owner. |
| Native Web Send-engine diagnostic | **b65 focused Runtime passed** | `NativeWebSendEngineProbeViewController` | Verified composer/protected Send/reasoning/final/tool-detail probe baseline remains accepted; diagnostic only. |
| Native conversation read/recovery | **Stable merged baseline + b74 response/adoption candidate** | `ConversationRepository` | Sole production conversation/list/detail/recovery/response lifecycle authority. b74 external continuation creates one response generation in the existing Repository runtime; no second response store. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38 semantics; b74 reuse optimization Runtime pending** | presentation projection + message cell | b38 deterministic bounded geometry/quick navigation remain authoritative. b74 caches only derived presentation geometry for unchanged resident identity to avoid repeated full rebuild; no message-body cache. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation remains separate; response lifecycle/tool-card semantics stay `DEV-send-stream`. |
| Streaming / Send | **Active — b67 transport accepted; b72 A/B positive; b74 exact Runtime candidate** | `DEV-send-stream`; PR #29; TD-029 | b74 exact source/Push+PR CI/Artifact/package verified; external page-owned resume adoption + geometry reuse/tool spacing Runtime pending. |
| User-visible reasoning | **Production local stream passed b67; b74 external-adoption Runtime pending** | `ConversationRepository` + `DEV-send-stream` | Ordered reasoning/tool segments retained; external matching resume feeds the same Repository timeline; hidden thoughts prohibited. |
| Tool activity presentation | **b74 Code/CI/Artifact/package verified; Runtime pending** | `DEV-send-stream` | b73 semantic filtering retained; b74 increases main meaningful tool-row vertical rhythm only. Ordered tools-only/input-only sheet remains. |
| Expandable GitHub tool detail | **b65 Runtime mapping accepted; b70 production restoration Runtime pending** | `DEV-send-stream` | b70 restores nested input/output disclosures + decoded hierarchy only for the evidenced exact-parent GitHub shape; no cross-connector generalization. |
| Background completion | **Hard requirement; follows accepted production response owner** | `BACKGROUND_EXECUTION_PLAN.md` | b45 positive short-background evidence retained. b66 memory warning occurred after failure and protected resident was not evicted; full 5/15-minute/WebContent gates remain later. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video handoff still needs evidence; no unsupported WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains b38.
- b67 production existing-conversation transport Runtime is accepted.
- Exact b72 Runtime positively supports the tested A-generating + B-send/generate simultaneous-generation path.
- Exact b73 Runtime is the evidence predecessor that exposed long resident geometry rebuild cost, insufficient tool rhythm and the external-active-response lifecycle gap.
- Exact b74 source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`, Push/PR CI, canonical Artifact `9768668727`, ZIP `6ac4cc97...95cb3` and IPA `07c999fd...285da` are verified; package identity independently unpacked.
- b74 observes only the official page-owned matching `/backend-api/f/conversation/resume` SSE for external adoption; it does not construct resume/offset/polling and does not change `ConversationRepository` authority.
- b39-b74 are reserved. Phase 9 Stable/Frozen: No. Runtime remains pending.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, Runtime behavior, Web-adapter rule or stability changes.

## 2026-09-03 — b92/b93 page-owned continuation loop interruption

Exact b92 single-executor Runtime proves that a background lifecycle transition can stop the official page-owned `stream_status`/snapshot loop even without another executor. Exact b93 proves successful first-responder/document-focus reacquisition does not necessarily restart a stopped loop. The next isolated candidate is foreground official-page rebootstrap without Native Detail Sync; selection rebootstrap remains separate. Stable/Frozen Send remains No.
