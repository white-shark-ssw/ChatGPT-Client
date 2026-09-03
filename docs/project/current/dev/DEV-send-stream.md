# DEV-send-stream

## Official iOS Probe v0.2 Runtime / v0.3 research gate — 2026-09-04

User-exported Probe v0.2 JSONL `sha256:f4f7e6f897e73262473a296ecbccc012477c5e1b44bdfe5ca7e3a43006148513` parsed cleanly: 392,033 events / 76,447,285 bytes / zero parse errors. `probe.log_cleared` is the first event, proving the new clear-log control works; opaque user-socket path redaction and direct presence-state logging also work.

This sample is **not a clean negative late-join result**. After `NSPOSIXErrorDomain/53` on the existing user WebSocket, the official app repeatedly invoked receive on the failed task and the Probe recorded 195,999 identical receive errors plus 196,002 receive-arm events. Two error storms span ~50.4 s and ~22.3 s, inflating the file to ~76 MB and materially perturbing observation. Source inspection shows the Probe logs/forwards the callback but does not itself schedule another receive, so causality of the official receive loop remains Unverified; regardless, per-arm/per-error logging must be removed/deduplicated before another decisive Runtime.

Across the entire file there are zero `conversationHash` events, zero conversation/per-turn WebSocket events and zero conversation HTTP/SSE events; the only `http.*` event is completion of the failed WebSocket task itself. Overall cross-platform late-join therefore remains **Inconclusive**, not Rejected. The JSONL does not encode whether the official iOS UI visibly joined the remote answer.

Static inspection of the exact supplied official framework independently exposes native `WebSocketConversationEventsService`, `stream_handoff`, `resume_conversation_token`, `turn_exchange_id`, `topic`, `resume_sse_endpoint`, and `ConversationResumeFetchRecovery.swift` strings including inline stream-status polling/fetch recovery. This proves official Native recovery machinery exists but does not prove which branch owns cross-platform late-join. The same binary exposes both `dataTaskWithRequest:` and `dataTaskWithURL:` forms; Probe v0.2 hooks only request forms.

**v0.3 research-only scope:** retain the working `清空`/privacy-safe structure; stop logging `ws.receive.arm`; log only the first repeated receive error per failed socket until a real message arrives; add wrappers for `dataTaskWithURL:` and `dataTaskWithURL:completionHandler:`; do not yet add a global task-resume hook. No ChatGPTClient product change, no polling implementation, and no b96 allocation.

Batch recovery: current feature head before this checkpoint workflow is the evidence commit `17cc302c40530067ed01be84547b8e2c2e81cc63`; PR #29 remains open/unmerged; `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`; b95 product/package remain `ac5e621aa69f5f27ef3167b4a951812be8b8e2c2` / `a10320e589acd551a8dc53f56aaf28a0a08f5b4a`; b96 unallocated. After this checkpoint commit, change only research Probe source/README, run dedicated research CI, package against official ZIP `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`, verify exact research IPA diff/hash, update durable docs/PR, then delete temporary v0.2/v0.3 apply/finalize tooling.

**Next exact action:** apply the minimal Probe v0.3 observation delta above. Product/config files must not change.

## Official iOS Probe v0.1 Runtime / v0.2 research gate — 2026-09-04

Human Runtime JSONL `sha256:c74a66702bd670f81a393afea1c306d2a0cce415961c9fe11be15589eeb83093` parsed cleanly: 29 events / 7,166 bytes. Probe v0.1 was genuinely active and captured the official `ws.chatgpt.com` user WebSocket. The observed socket sent `connect` plus only three base subscriptions (`app_notifications`, `calpico-chatgpt`, `push_auth_challenge`). After `NSPOSIXErrorDomain/53` it recreated the socket and repeated the same base subscriptions. No conversation/per-turn subscribe, target conversation hash, conversation-update, add-messages, async-status, catchup or live target frame appears.

This is **negative for the simple direct-user-WebSocket late-join hypothesis in this sample, but overall late-join remains Inconclusive** because Probe v0.1 filtered out ordinary conversation HTTP/Detail/stream-status/resume/SSE and did not observe delegate-based streaming response lifecycle. v0.1 also exposed an opaque user-specific WebSocket path segment; v0.2 must redact opaque path parts.

Research-only v0.2 is authorized: privacy-safe HTTP conversation/realtime path observation, response status/MIME/structural key metadata, delegate response/completion hooks, direct presence-state logging, raw-path redaction, and a confirmed `清空` log control. No prompt/body/auth/signed-query capture. No ChatGPTClient product change and no b96 allocation.

Batch recovery point: exact b95 product/package remain `ac5e621aa69f5f27ef3167b4a951812be8b8e2c2` / `a10320e589acd551a8dc53f56aaf28a0a08f5b4a`; `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`; PR #29 open. Temporary tooling commits beginning at `14bef4584efc1eb82375491d273f83f6da7d4548` have not modified product. This apply batch may modify only the three research Probe sources plus this checkpoint, PROJECT_STATE, and the new Runtime-evidence file. After source commit, require dedicated research Probe CI, independently package against exact `ChatGPT_Decrypted.zip` SHA `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`, verify research IPA identity/diff, then remove temporary tooling. Product/config files must not change.

**Next exact action:** build/package Probe v0.2, then run one clean cross-platform late-join test after pressing `清空` immediately before the remote turn. Analyze the earliest target-correlated HTTP/SSE/WebSocket acquisition event before any b96 decision.

## Status

**Active — exact b95 hard Reload is Runtime Positive as a deliberate recovery path, but automatic external terminal/final convergence remains insufficient. Latest user priority is cross-platform late-join continuation first: official iOS is explicitly reported able to continue a response initiated on another platform, so the immediate gate is to observe and reproduce the official native late-join realtime registration/topic/update path. Client-owned Web->Native handoff remains recorded but is secondary until this cross-platform path is resolved. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b89 Candidate: `DEV-send-stream-0.1.0-b89` permanently reserved; Runtime interactivity-sufficient Rejected
- b90 Candidate / Build: `DEV-send-stream-0.1.0-b90` / `0.1.0 (90)` permanently reserved
- Exact b90 product commit: `5e9d735ddb2f7a2c46dbc43de2525980c86a1c1e`
- Exact b90 product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`
- b91 Candidate / Build: `DEV-send-stream-0.1.0-b91` / `0.1.0 (91)` permanently reserved
- Exact b91 product commit: `cdab4e091683dc179753ed114c9ab5993a6c2d24`
- Exact b91 product/config package source: `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`
- b91 Push CI: `33746881658 / 100621278207` — success
- b91 PR CI: `33746886896 / 100621297087` — success
- b91 canonical Push Artifact: `9890000591`
- b91 IPA SHA-256: `abbd27370665fb97dd1ee5edd239c0a5fa1ea0694cbb329a81c32ee86867c140`
- b92 Candidate / Build: `DEV-send-stream-0.1.0-b92` / `0.1.0 (92)` permanently reserved
- b92 allocation checkpoint: `296de318c20ccc32bfea1cb93246bd9d824d3403`
- Exact b92 product commit: `96ea3e3d8c5cabf67ff33331d40c9dcc6c9f0850`
- Exact b92 product/config package source: `54b5803a74a123431f0a2a8e662a1a2fe874b3ca`
- b92 Push CI: `33750585725 / 100632980237` — success
- b92 PR CI: `33750591494 / 100632998279` — success
- b92 canonical Push Artifact: `9891430379`
- b92 IPA SHA-256: `82d96d359767b72c623f367bf3cd2c5f3ae9d1d7411ad547c1ba3634341c3514`
- b92 Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b92-covered-overlap-focus-handoff-20260903.md`
- b93 Candidate / Build: `DEV-send-stream-0.1.0-b93` / `0.1.0 (93)` permanently reserved
- b93 allocation checkpoint: `b86c1a3ca94b215204b0cfb135fa0cd8b3603619`
- Exact b93 product commit: `556bd8886061f4126d11e4ac44f4e24ed580500c`
- Exact b93 product/config package source: `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0`
- b93 staging: `33754848709 / 100646690995` — success
- b93 Push CI: `33755063112 / 100647405265` — success
- b93 PR CI: `33755067202 / 100647418537` — success
- b93 canonical Push Artifact: `9893141097`
- b93 IPA SHA-256: `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d`
- b94 Candidate / Build: `DEV-send-stream-0.1.0-b94` / `0.1.0 (94)` permanently reserved
- b94 allocation checkpoint: `d957e29595e13fcb46da133d98eebaa716f93d25`
- Exact b94 product commit: `95f0f99921ad9f41a40b7919162498b00138d5a4`
- Exact b94 product/config package source: `59894bd9ca7c293211cd856ecf33579f19ce4d84`
- b94 staging: `33761087305 / 100667284502` — success
- b94 Push CI: `33761341528 / 100668157341` — success
- b94 PR CI: `33761346240 / 100668174308` — success
- b94 canonical Push Artifact: `9895660898`
- b94 Artifact digest: `sha256:65d29b08d10ef3c626f64a9fa16e574a53ab33aa0d7041fa53f9c094915b9b60`
- b94 IPA SHA-256: `a0d3de344f18f75e0286f26c27b9ea0c89548bed6a75bff4bb3369ee7bcfaffb`
- b95 Candidate / Build: `DEV-send-stream-0.1.0-b95` / `0.1.0 (95)` permanently reserved
- Exact b95 product commit: `ac5e621aa69f5f27ef3167b4a951812be8b8e2c2`
- Exact b95 product/config package source: `a10320e589acd551a8dc53f56aaf28a0a08f5b4a`
- b95 staging: `33775057479 / 100714562438` — success
- b95 Push CI: `33775521398 / 100716116912` — success
- b95 PR CI: `33775526525 / 100716136837` — success
- b95 canonical Push Artifact: `9901461763`
- b95 Artifact digest: `sha256:0378271690113e92849d87cec7bc32fa56d4ae8de4885e7003fc0ba69e26cb6a`
- b95 IPA SHA-256: `2fd213a1dd692202b496adabd393c4130080607384e3d6c0f84cd3f975a8840d`
- Stable/Frozen Send: No

## b89 Runtime conclusion

Exact b89 on iPhone/iOS17 proved `isUserInteractionEnabled=true` and first-responder/document focus, yet emitted zero page-owned continuation while the same remote response later advanced only after explicit Sync from timeline `5 -> 28`, tools `4 -> 25`, reasoning `1 -> 3`. Therefore interactivity is rejected as a sufficient continuation condition. Manual authoritative Detail projection remains Runtime Positive.

## b90 Runtime progression

The earlier Native auth `NSURLErrorDomain -1005` sample was transient/inconclusive. Later exact b90 Runtime restored `/api/auth/session`, accounts-check and conversation-list HTTP200; manual Sync then raised the executor from `visibleSiblingCountAbove=1` to `0`, loaded a visible complete page, and achieved `nativeFirstResponder=true` / `documentHasFocus=true`. Therefore the b90 frontmost mechanism itself is Runtime Positive.

That sample still showed no bridge-reported matching `stream_status`, `/resume`, external streaming or project snapshot. This absence is no longer valid evidence against official project-Web continuation because a stronger bridge identity defect is now proven below.

## Project-scoped route-parser root cause — 2026-09-03

User Runtime observation: ordinary non-project conversations do not show the same continuation failure, while the current project conversation does; visible official Web itself appears healthy.

Current source directly explains this split:

- every existing conversation is initially loaded through `https://chatgpt.com/c/{conversationID}`;
- bridge `currentConversationID()` matches only `^/c/([^/?#]+)`;
- known official project canonical form is `/g/{scope}/c/{conversation}`;
- after canonicalization, the current bridge therefore returns `null` for a valid project conversation and classifies that page as `route=other`;
- the bridge uses that parsed `pageConversationID` as a required equality gate for page-owned `stream_status`, `/resume`, plural conversation snapshots, WebSocket exact-target matching and composer conversation identity;
- consequently, correct official project-Web requests can occur while the Native bridge silently treats them as non-target and emits none of the expected external continuation events.

The latest b90 log is consistent with this exact transition: immediately after direct `/c/{id}` reload page diagnostics report `route=conversation`, while later page activation events report `route=other` although the visible official Web remains healthy.

Qualification: **project scoped-route identity parsing is now the strongest evidenced blocker. The b90 no-event interval cannot decide z-order sufficiency for project conversations because the observer can become blind after project canonicalization.**

## b91 exact minimum A/B

Allocate b91 only for the bridge identity parser:

- preserve b90 transport, protected Send ownership, Repository ownership, observation protocol and diagnostic frontmost behavior for causal isolation;
- change `currentConversationID()` so it recognizes both ordinary `/c/{conversation}` and exact evidenced project scoped `/g/{scope}/c/{conversation}`;
- `pageRouteShape`, stream-status matching, resume matching, plural snapshot matching, WebSocket target matching and composer conversation identity then automatically consume the corrected identity through their existing shared helper;
- do not add new route guesses, retry/fallback/timer/watchdog/polling, Native status/resume synthesis, duplicate Send, WebSocket-body authority or second response store.

## b91 package / validation state

The exact minimum parser change was committed as `cdab4e091683dc179753ed114c9ab5993a6c2d24`. Guarded staging `33746622538 / 100620460993` passed ancestry, exact replacement, exact two-product-file scope and Simulator compile. Formal Push CI `33746881658 / 100621278207` and PR CI `33746886896 / 100621297087` both passed on exact package source `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`.

Canonical Push Artifact `9890000591` has backend digest `sha256:6062b02f9f1332744816d01a58e13c1a8c82017ee50828051f014ef79b943350`. Independent unpacking verified IPA `ChatGPTClient-0.1.0-b91-dev-send-stream.ipa`, SHA `abbd27370665fb97dd1ee5edd239c0a5fa1ea0694cbb329a81c32ee86867c140` matching sidecar, built `0.1.0 (91)`, Candidate b91, source `c5985f1e2e5d`, MinimumOS 14.0, iPhone/iPad family `[1,2]` and arm64.

Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

## b91 Human Runtime gate

After b91 package verification, run the same project-conversation test while a remote response is clearly active. Decisive evidence is no longer z-order itself; it is whether, after project canonicalization, the bridge continues to identify the target and reports the official page-owned path:

- page remains classified as conversation after scoped canonicalization;
- matching `coveredExecutor.externalStreamStatusRequest/Response` and/or `externalResumeRequest/Response` appears when official Web issues them;
- `externalStreamingObserved` / page-owned snapshot can advance the existing Repository external generation without another manual Sync.

If b91 makes project continuation observable/functional, route parsing is Runtime Positive; then a later separate candidate may remove the b90 frontmost diagnostic to prove the final covered production form. If b91 still has no page-owned requests while the project page is correctly recognized and the remote response demonstrably advances, continue from that new evidence without speculative protocol work.

## b91 Human Runtime result — 2026-09-03

Exact b91 Runtime is decisive for live continuation. Metadata matches Candidate b91 / Build 91 / source `c5985f1e2e5d`. After one explicit Sync established response generation 1, the official project page remained `route=conversation`, issued matching page-owned `stream_status`, repeatedly returned HTTP200 `IS_STREAMING`, emitted `externalStreamingObserved`, and continued after its own `/resume` offset 0 returned HTTP404 through the already-observed page-owned `stream_status` + plural conversation read path.

Native live state advanced automatically without another Sync: service messages/tools `6 / 2 -> 47 / 14`, reasoning characters `194 -> 909`, with repeated `externalSnapshot`, `liveResponse.externalSnapshot` and `liveResponse.presentationApplied`. Therefore the scoped-route parser and existing page-owned live continuation path are Runtime Positive.

The user could not return from the visible official Web because b91 intentionally retains b90's `hostView.bringSubviewToFront(webView)` diagnostic. That line changes z-order and has no balancing send-to-back in the rearm path; it is now a confirmed diagnostic presentation artifact.

The run does **not** validate automatic terminal/final convergence: the last pre-exit status was still `IS_STREAMING`, last snapshot had `finalCharacters=0`, then the app was force-quit/relaunched.

## b92 covered-form package / validation state

b92 removes only the b90 frontmost z-order mutation. The executor remains inserted at index 0 and manual rearm now records `manual_sync_covered` without changing z-order; b91 scoped route identity and page-owned continuation logic are unchanged.

Two early staging attempts (`33749925741`, `33750233706`) failed in guard-only tooling before product application. Successful staging `33750363774 / 100632281401` passed exact b91-state guard, exact two-product-file scope audit, and Simulator compile, then emitted product `96ea3e3d8c5cabf67ff33331d40c9dcc6c9f0850`.

Exact product/config package source `54b5803a74a123431f0a2a8e662a1a2fe874b3ca` passed Push CI `33750585725 / 100632980237` and PR CI `33750591494 / 100632998279`. Canonical Push Artifact `9891430379` has digest `sha256:f3cb6291fabcb2cf48729750d23a4403607e8ac81dc4354749974e287412e970`. Independent unpacking verified IPA SHA `82d96d359767b72c623f367bf3cd2c5f3ae9d1d7411ad547c1ba3634341c3514` matching sidecar, Release `0.1.0 (92)`, Candidate b92, source `54b5803a74a1`, MinimumOS 14.0, device family `[1,2]`, iphoneos and Mach-O arm64.

Evidence ladder before Runtime: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Stable-Frozen No.**

## b92 Human Runtime result — 2026-09-03

Exact diagnostics match Candidate b92 / Build 92 / source `54b5803a74a1` on iPhone / iOS 17.0.

The first project conversation (`sha256:0df178903e95`) proves the covered production form can continue externally after one explicit Sync: `manual_sync_covered` remained `subviewIndex=0` with `visibleSiblingCountAbove=1`, route remained `conversation`, page-owned `stream_status` repeatedly returned HTTP200 `IS_STREAMING`, and Native external snapshots advanced without another Sync to service messages/tools `54 / 18` and reasoning 781 characters. Therefore b90/b91 frontmost presentation is not required once the corrected project route identity is present.

A second conversation (`sha256:6f429823a988`) was then used for client-owned protected Send while the first external response remained active. The second executor produced HTTP200 `text/event-stream`, streamed reasoning/tools/final to `finalCharacters=6073`, reasoning 708, timeline 18/tools 14, emitted `terminal`, and automatically completed authoritative reconcile (`visible 15 -> 17`, `liveResponse.reconciled`, `liveSnapshotCleared=true`). Client-owned Send/SSE/natural terminal/final is Runtime Positive.

The overlap exposes a narrower failure. `activeExecutorCount` reached 2. The first external conversation continued after the second executor was created, reaching service messages/tools `54/18` at 11:58:27Z. The second client-owned Send began at 11:58:29Z; a Web `blur` event followed around the handoff. There were no further external status responses after 11:58:25Z and no further first-conversation snapshots after 11:58:27Z. Selecting the first conversation again at 12:01:45Z produced only `composer_ready`; its live response stayed frozen at reasoning 781 / timeline 21 / tools 18 / final 0 through 12:05:52Z. Explicit Sync at 12:05:55Z fetched authoritative visible messages 25 with no trailing reasoning/tool timeline and added the final assistant; `liveResponse.externalDetailReconciled` then cleared the stale external live row.

Source correlation is direct but not yet final proof of focus causality: executors are per-conversation; active external executors are deliberately retained by `releaseIdleExecutors`; protected Send focuses the second page composer; reselection of an already-active external executor with matching `currentConversationID` only probes the composer and does not restore first-responder/document focus. Bridge events do not currently include executor identity, so the observed `blur` cannot be conclusively assigned. **Strongest evidenced next differential: selection-time focus reacquisition for an already-active external response.**

Current Runtime classification: **covered single-conversation page-owned continuation Runtime Positive; client-owned protected Send/SSE terminal+authoritative reconcile Runtime Positive; overlapping external continuation/reselection recovery Runtime Negative; automatic external terminal/final under overlap Unverified/Rejected for current behavior; Stable-Frozen No.**

## b93 exact minimum A/B — allocated

Next candidate, if allocated, must change only selection-time reacquisition for an already-active external response:

- when the user selects a conversation whose live snapshot is active and `promptText` is empty, reuse its existing executor;
- reacquire that executor's Native/Web document focus without page reload;
- log a distinct selection focus-rearm stage/result;
- retain b92 covered z-order, b91 scoped route parser, page-owned continuation transport, protected Send transport and Repository ownership;
- do not add background polling, retry/watchdog/timer, Native `stream_status`/`resume`, guessed offset, duplicate Send, WebSocket-body authority or a second response store.

Decisive Runtime test: external project response -> one Sync -> switch to another conversation -> complete one client-owned Send -> select the original external-live conversation again **without manual Sync**. If page-owned `stream_status`/external snapshots resume and naturally materialize/reconcile the final assistant, selection-time focus reacquisition is Runtime Positive. If not, reject it as sufficient.

## b93 package / validation state

b93 changes only reselection behavior for an already-active external live response. `reactivateExternalObservationFocus()` keeps the existing covered WebView and route, calls `becomeFirstResponder()`, samples `document.hasFocus()`, and logs `selection_external_focus_rearm` / `selectionFocusActivationAttempt` / `selectionFocusActivationResult`. No page reload, manual Sync, status/resume synthesis, timer, retry, polling, duplicate Send or response-store change was added.

Allocation checkpoint `b86c1a3ca94b215204b0cfb135fa0cd8b3603619` precedes product `556bd8886061f4126d11e4ac44f4e24ed580500c`. Guarded staging `33754848709 / 100646690995` passed the exact b92 state guard, exact two-product-file audit and Simulator compile. Exact product/config package source `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0` passed Push CI `33755063112 / 100647405265` and PR CI `33755067202 / 100647418537`.

Canonical Push Artifact `9893141097` has backend digest `sha256:5a07512a1bf3becac3a8d2a7655c3d3f09caa150c1162b95327e40b3c8ed2ad5`. Independent unpacking verified `ChatGPTClient-0.1.0-b93-dev-send-stream.ipa`, SHA `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d` matching sidecar, Release `0.1.0 (93)`, Candidate b93, source `2d2cde58a7fb`, MinimumOS 14.0, device family `[1,2]`, `iphoneos`, and Mach-O arm64.

Evidence ladder: **Code written / guarded exact two-file scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

## b93 Human Runtime gate

1. Start a long response in a project conversation on another official client.
2. In b93 select the same conversation and press `同步最新消息` exactly once; confirm covered external snapshots begin.
3. Switch to a second conversation and send one message from ChatGPTClient; allow its local SSE response to finish naturally.
4. Return to the original external-live conversation **without pressing Sync**.
5. Diagnostics must show `selection_external_focus_rearm`, `selectionFocusActivationAttempt`, and `selectionFocusActivationResult`; the decisive focus result is `documentHasFocus=true`.
6. After reselection, page-owned `externalStreamStatusRequest/Response` and external snapshots must resume for the original response without reload/Sync.
7. Let the remote response finish naturally and verify the final assistant materializes/reconciles automatically. Export diagnostics after completion.

If focus is reacquired and continuation resumes, selection-time focus reacquisition is Runtime Positive. If focus is reacquired but continuation remains frozen while the remote answer advances, reject focus reacquisition as sufficient and continue from that evidence without speculative protocol work.

## b93 Human Runtime result — 2026-09-03

The user supplied exact b92 and b93 logs that materially revise the earlier focus hypothesis. Full evidence is in `docs/project/runtime-evidence/DEV-send-stream-b92-b93-page-loop-interruption-20260903.md`.

Exact b92 (`54b5803a74a1`) reproduces the terminal freeze with a single external conversation and a single executor. Page-owned status/snapshot progression reached `service 88 / tools 33`; the last `stream_status` request/HTTP200 `IS_STREAMING` and last snapshot coincide with entry to background at `12:13:30-12:13:31Z`. After later foreground returns the page becomes visible and the user WebSocket can reconnect, but no further page-owned `stream_status` or external snapshot is emitted. Explicit Sync at `12:19:46Z` then materializes the completed assistant and clears the stale live response. Therefore a second executor is not necessary for the failure.

Exact b93 (`2d2cde58a7fb`) proves the added focus mechanism itself: reselection repeatedly obtains `nativeFirstResponder=true` and `documentHasFocus=true`. At `13:07:31Z` that rearm is followed by another page-owned HTTP200 `IS_STREAMING` and snapshot `80 / 19`. After switching away at `13:07:38Z` and returning at `13:07:42Z`, focus rearm again succeeds (and repeats at `13:07:47Z`) but page-owned status requests never restart. Explicit Sync at `13:10:24Z` later adds the completed assistant (`visible 26 -> 27`) and performs `liveResponse.externalDetailReconciled`.

Classification: **b93 focus reacquisition mechanism Runtime Positive; focus reacquisition as a sufficient restart condition Rejected.** The common failure is now the lifetime of the official page-owned continuation acquisition loop itself.

## b94 exact minimum A/B — allocated

The next candidate, if allocated, must test the clean single-executor lifecycle case first. Keep b93 transport/ownership/route behavior, but when ChatGPTClient becomes active again and the selected Repository snapshot is still an active external response (`promptText` empty), rebootstrap that same existing official conversation page without a Native Detail Sync. Add a distinct foreground-rebootstrap diagnostic stage.

This is an official-page lifecycle A/B only. Do not add Native `stream_status`, `/resume`, guessed offset, polling/cadence reproduction, retry/watchdog/timer, duplicate Send, WebSocket-body authority, or a second response store.

Runtime gate: one external conversation/executor, one initial Sync to acquire continuation, background while the remote answer remains active, return foreground without Sync, then require page-owned status/snapshots to resume and the final assistant to reconcile naturally. Selection-triggered page rebootstrap remains a separate later A/B.

## b94 package / validation state

b94 changes only foreground lifecycle recovery for the selected already-active external response. On `UIApplication.willEnterForegroundNotification`, if the selected Repository live snapshot is active/external (`promptText` empty), the existing covered executor reloads the same official conversation page and logs `foreground_external_page_rebootstrap` / `coveredExecutor.foregroundPageRebootstrap`. It does not perform Native Detail Sync and does not synthesize `stream_status` or `/resume`.

Allocation checkpoint `d957e29595e13fcb46da133d98eebaa716f93d25`; product `95f0f99921ad9f41a40b7919162498b00138d5a4`; exact product/config package source `59894bd9ca7c293211cd856ecf33579f19ce4d84`. Staging `33761087305 / 100667284502` passed exact two-file scope and Simulator compile. Push CI `33761341528 / 100668157341` and PR CI `33761346240 / 100668174308` passed. Canonical Push Artifact `9895660898` has digest `sha256:65d29b08d10ef3c626f64a9fa16e574a53ab33aa0d7041fa53f9c094915b9b60`. Independent unpacking verified IPA SHA `a0d3de344f18f75e0286f26c27b9ea0c89548bed6a75bff4bb3369ee7bcfaffb` matching sidecar, `0.1.0 (94)`, Candidate b94, source `59894bd9ca7c`, MinimumOS 14.0, device family `[1,2]`, `iphoneos`, arm64.

Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

## b94 Human Runtime gate

Use one project conversation/executor only. Start a deliberately long remote response, press `同步最新消息` once to establish advancing page-owned external snapshots, keep that same conversation selected, background ChatGPTClient while the remote response is still active, then return foreground **without pressing Sync**. Require `foregroundExternalRebootstrap.requested`, activation stage `foreground_external_page_rebootstrap`, `coveredExecutor.foregroundPageRebootstrap`, a completed official page load, then renewed matching `externalStreamStatusRequest/Response` and external snapshots. Let the remote response finish naturally and require final materialization/reconcile without Sync.

If the remote answer is already terminal before foreground rebootstrap, classify the sample Inconclusive and reuse exact b94; do not allocate a new candidate. Selection-triggered page rebootstrap remains outside b94.

## b94 Human Runtime result — 2026-09-03

Exact b94 diagnostics match Candidate `DEV-send-stream-0.1.0-b94`, Build 94, source `59894bd9ca7c`, iPhone / iOS 17.0. Full evidence is recorded in `docs/project/runtime-evidence/DEV-send-stream-b94-foreground-rebootstrap-web-process-terminated-20260903.md`.

The foreground-rebootstrap mechanism itself is Runtime Positive. After background at `14:25:44-14:25:46Z`, foreground at `14:25:52Z` emitted the b94 rebootstrap diagnostics, reloaded the same official conversation page, and page-owned HTTP200 `IS_STREAMING` plus external snapshots resumed without another Sync. The live projection advanced through `11/4`, `13/4`, `15/5` service/tool counts. A later foreground rebootstrap at `14:27:25Z` again restored the loop and snapshots advanced through `34/12`, `36/13`, `37/14`, `39/14`. Therefore full official-page rebootstrap is sufficient to restart at least these interrupted page-owned continuation loops; b93 focus-only recovery remains rejected as sufficient.

The same exact run also exposes a new reliability failure. After several foreground/background transitions and repeated full conversation-page rebootstrap actions, foreground at `14:35:12Z` loaded the page, then at `14:35:17Z emitted `coveredExecutor.webProcess state=terminated` followed by `coveredExecutor.failed reason=web_process_terminated`; external generation 1 failed and the executor was released. This is direct Runtime evidence of WKWebView WebContent-process termination. The cause is Unverified: current diagnostics do not capture WebContent memory or jetsam reason, so do not call this proven OOM.

The conversation is now very large. Late authoritative Detail is `5,491,909` bytes, mapping `1535`, recipient-message count `397`, visible-message count `28`; the successful late Syncs take about `4.77s` and `5.44s`. This makes the earlier Web Rule Lab timeout/resource concern a material hypothesis, not a proven root cause.

Both late user Sync actions succeeded at the authoritative transport layer. At `14:36:15Z` and again `14:38:19Z`, HTTP200 Detail still contained trailing reasoning/timeline/tool counts `3 / 33 / 30` and no new visible final assistant. Repository therefore correctly rebuilt external generation 2, after which official `stream_status` continued returning `IS_STREAMING` and snapshots stayed around `service=109 / tools=30 / finalCharacters=0` through export. The final Sync did not fail; authoritative server state itself remained unfinished/stuck at export.

Current UI intentionally disables `重载当前会话` whenever the selected live snapshot phase is active. Therefore after the authoritative Sync rebuilt an active external live response, Reload being grey is expected current policy, not an in-flight-operation leak. In combination with an indefinitely active external response, this creates a real user recovery dead-end.

Classification: **foreground page rebootstrap mechanism Runtime Positive; repeated/heavy full-page covered-Web reliability Runtime Negative / not production-stable in this run; WebContent termination root cause Unverified; manual late Sync transport Runtime Positive; external terminal/final convergence Unverified/not achieved; manual Reload recovery blocked by current active-live UI policy; Stable/Frozen No.**

Do not allocate a new candidate merely to add polling/retry/timers. Next work must first isolate a minimum event-driven response to the now-proven WebContent termination / repeated heavy reload problem and a deliberate user recovery path, while preserving official-page transport ownership and Repository content ownership.

## Validation / identity state

b90 package remains exact and unchanged: canonical Artifact `9882770072`, exact package source `99f1aa15...`, IPA SHA `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`.

b91/b92 exact package identities remain permanently reserved. Exact b93 product `556bd8886061f4126d11e4ac44f4e24ed580500c` and package source `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0` are fixed; later docs/tooling commits do not redefine that package identity.

## Batch recovery state

**Closed at exact b94 Human Runtime gate. Next exact action:** install exact canonical b94 and run the single-executor foreground lifecycle test above. Do not modify product/config or allocate another candidate before Runtime evidence. Selection-triggered page rebootstrap remains separate.

## Preserved boundaries

Official page owns continuation transport; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling/cadence reproduction, retry/watchdog, duplicate Send, WebSocket-body authority, hidden-thought presentation or second response store.

## Session round counter

This user turn is **round 60**.

## b95 allocation — always-available hard Reload

Latest explicit user requirement restores an original product invariant and outranks the older preflight allowance to disable Reload while a response is active:

- `重载当前会话` is an exceptional recovery action and must never be disabled while a current conversation exists.
- Reload means: invalidate the current conversation's covered executor/observation, reset its Repository live-response state, clear the current page presentation/resident Detail, then issue one fresh authoritative server Detail load.
- Reload never resends/regenerates the prompt and does not claim to Stop the server generation.
- If the new authoritative Detail still contains a trailing active response timeline, rebuild the external live projection from that server data and attach one fresh covered observer.
- Repeated Reload while Sync/Reload is already in flight is allowed; existing `replacingCurrentRequest: true` generation ownership must supersede the older Detail operation rather than disabling the recovery action.
- Keep response generation counters monotonic when clearing a snapshot so stale callbacks cannot revive the old generation.
- No polling, retry, timer, watchdog, Native `stream_status`/`resume`, guessed offsets, duplicate Send, WebSocket-body authority, automatic server Stop, or second response store.

Candidate / Build: `DEV-send-stream-0.1.0-b95` / `0.1.0 (95)` — allocated and reserved.

### Intended minimum product scope

- `ChatGPTClient/RootViewController.swift`: add conversation hard-reset orchestration, always keep the detail recovery menu reachable, release the selected conversation executor before Reload, and re-observe only after authoritative Reload applies.
- `ChatGPTClient/Conversation/ConversationFeature.swift`: remove active/in-flight Reload disable/guards; keep the current page clear + replacement Detail load behavior; adopt authoritative trailing timeline after Reload success.
- `ChatGPTClient.xcodeproj/project.pbxproj`: bump Build/Candidate only.
- `.github/workflows/ios-foundation.yml`: bind exact b95 package identity only after guarded product compile passes.

### Batch recovery point

Known pre-allocation feature head: `b2cd6365c90decbc7f7e33958ef171076b52f8c4`; PR #29 open/unmerged; `main` `94f0c5777dad262cd1fb22be49082dbd92c962f2`; exact b94 package source remains `59894bd9ca7c293211cd856ecf33579f19ce4d84`.

Confirmed before product writes: b95 absent from Build/Test Index and commit search; no second Active feature checkpoint/branch conflict; current Xcode Build/Candidate is b94; permanent package workflow is still b94.

Write batches planned:

1. record this checkpoint and remove the temporary checkpoint workflow;
2. guarded staging applies only the b95 product files and runs Simulator compile without emitting an IPA;
3. create exact product commit plus package-binding commit objects and advance the feature branch once so no intermediate b94/b95 identity can emit;
4. require Push/PR CI, canonical Artifact and independent package inspection;
5. update durable docs/PR and hand exact IPA to Human Runtime.

Next exact action after checkpoint cleanup: run guarded b95 staging for the minimum hard-Reload patch. Do not modify b94 Runtime evidence or allocate b96 during recovery.


## b95 package / validation state

Exact b95 implements only the restored hard-Reload invariant. Product `ac5e621aa69f5f27ef3167b4a951812be8b8e2c2`; exact product/config package source `a10320e589acd551a8dc53f56aaf28a0a08f5b4a`. Isolated staging `33775057479 / 100714562438` passed exact three-product-file scope and Simulator compile. Formal Push CI `33775521398 / 100716116912` and PR CI `33775526525 / 100716136837` both passed. Canonical Push Artifact `9901461763` has digest `sha256:0378271690113e92849d87cec7bc32fa56d4ae8de4885e7003fc0ba69e26cb6a`. Independent unpacking verified `ChatGPTClient-0.1.0-b95-dev-send-stream.ipa`, SHA `2fd213a1dd692202b496adabd393c4130080607384e3d6c0f84cd3f975a8840d` matching sidecar, `0.1.0 (95)`, Candidate b95, source `a10320e589ac`, MinimumOS 14.0, device family `[1,2]`, `iphoneos`, arm64.

Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

### b95 Human Runtime gate

Use b95 primarily to validate recovery semantics while collecting a fresh exact log for the still-primary automatic-disconnect defect:

1. Start a deliberately long project response remotely and use one explicit Sync to establish page-owned external progression.
2. Let b95 advance automatically for several status/snapshot rounds.
3. Trigger one already-proven interruption boundary (background/foreground, or switch away and reselect) and confirm whether page-owned `externalStreamStatusResponse` / `externalSnapshot` stops while the remote answer remains active.
4. While the selected conversation is still active/stuck, verify `重载当前会话` remains enabled and invoke it once.
5. Require `manualReload.hardReset`, old executor release/live snapshot reset, one replacement authoritative Detail load, then a fresh external observation only if authoritative trailing timeline is still active.
6. Export diagnostics after observing whether automatic continuation resumes.

Reload Runtime success is a recovery feature only; it must not be classified as solving automatic continuation interruption.

## Automatic-disconnect source conclusion after b95 package

Current source plus b92-b94 Runtime narrows the primary defect to the lifetime of the official page-owned continuation acquisition loop. The covered bridge does not create Native polling: it only observes the official page's matching `stream_status`, `/resume`, and plural-conversation reads. When that page loop stops after background or browsing-context handoff, Repository progression therefore stops even though the remote server can keep generating. b93 proves restoring first-responder/document focus alone does not reliably restart the loop. b94 proves reloading the same official conversation page can restart it, but repeated/heavy full-page rebootstrap later terminated the WebContent process.

No b96 is allocated before b95 Human Runtime, per the artifact-to-runtime gate. Investigation may continue, but the next product candidate must remain event-driven and must not add polling, timers, retry/watchdog, Native `stream_status`/`resume`, guessed offsets, duplicate Send, WebSocket-body authority, or a second response store. The next change must reduce or replace repeated heavy page rebootstrap using evidence from an exact b95 interruption sample; do not simply add more reload triggers.

**Next exact action:** keep b95 product fixed and perform a privacy-safe transport-handoff research gate. For one client-owned protected Send, prove or reject server-issued continuation identity (`resume_conversation_token`, `stream_handoff`, `turn_exchange_id`, `topic_id` or equivalent) and whether a Native continuation channel can be established before Web becomes disposable. Separately prove whether an already-active cross-device turn exposes an official realtime subscription/update path. Do not allocate production b96 from guessed transport or reproduce page polling cadence.


## b95 Human Runtime result — 2026-09-04

Exact b95 diagnostics match Candidate `DEV-send-stream-0.1.0-b95`, Build 95, source `a10320e589ac`, iPhone / iOS 17.0. Full evidence: `docs/project/runtime-evidence/DEV-send-stream-b95-hard-reload-and-handoff-hypothesis-20260904.md`.

One explicit Sync exposed an active external tail and page-owned continuation then advanced automatically through repeated HTTP200 `IS_STREAMING` + plural snapshots. Before the first background, service/tools progressed `6/2 -> 14/6`; after foreground full-page rebootstrap the same response resumed, and a later rebootstrap caught up to phase `final`, reasoning `757`, service `103`, tools `30`, final characters `0`. Five foreground rebootstrap requests occurred in this run. Unlike b94, b95 emitted no `coveredExecutor.webProcess state=terminated` and no `coveredExecutor.failed`; therefore WebContent termination is not reproduced, but prior b94 still makes repeated/heavy full-page reliability non-stable and its cause remains Unverified.

At `17:09:33Z` the user invoked `重载当前会话` while the Repository live snapshot remained active/stuck in final phase. b95 released the old executor, reset the live snapshot (`manualReload.hardReset executorReleased=true / liveSnapshotCleared=true`), and issued one replacement authoritative Detail load. HTTP200 Reload returned `6,235,224` bytes, mapping `1737`, visible messages `33`, with zero trailing reasoning/timeline/tools; `conversationReload.end` reported visible `32 -> 33`. The completed assistant was therefore already authoritative and Hard Reload materialized it successfully. **Hard Reload recovery is Runtime Positive.**

The run still does not prove natural external terminal/final convergence: before manual Reload the official page kept reporting `IS_STREAMING` with static service `103` / tools `30` / final `0`, and there is no page-owned COMPLETE / natural terminal / automatic authoritative reconcile before Reload. Classification: **b95 Hard Reload Runtime Positive; full-page rebootstrap restart mechanism Runtime Positive again; WebContent termination not reproduced / cause Unverified; automatic external terminal/final convergence not achieved; Stable-Frozen No.**

A narrower b95 orchestration mismatch is also proven: after authoritative Reload returned no active trailing timeline, Root still created a fresh covered executor/`mode=selection` observer. This conflicts with b95's intended post-Reload rule to re-observe only if authoritative Detail remains active. Record as a secondary cleanup item; do not let it displace the primary automatic-disconnect architecture.

### Web -> Native transport handoff hypothesis

User proposes making covered Web only the protected Send/bootstrap executor, then letting Native own continuation once a matching Native channel is confirmed, so later WebContent death becomes irrelevant. This is a coherent next research direction only as a **server-supported transport handoff**, not by attempting to inherit the exact JavaScript `ReadableStream` after WebContent dies. Existing historical first-party probes already observed early `resume_conversation_token` on our own protected Send; external comparison research reports current self-submitted-turn paths that can expose `stream_handoff` / `turn_exchange_id` / `topic_id` and then subscribe to shared realtime transport.

For client-owned Send, the next research gate is therefore to prove those server-issued identities and an actual Native continuation subscription before releasing Web. For a cross-device already-active response, Sync/Detail alone does not prove possession of the original turn's handoff token/topic; that case requires separate first-party realtime evidence. Copying the official page's `stream_status` + plural-read cadence into Native remains rejected polling, not handoff.

No production ownership rule changes yet. Until the research gate is positive, official page owns continuation transport, `ConversationRepository` owns Native response/content, and Native must not guess topic/offset/resume, duplicate Send, add polling/timers/retry/watchdog, or create a second response store.


## Cross-platform late-join priority override — 2026-09-04

Latest explicit user direction prioritizes the existing cross-platform automatic-disconnect defect over client-owned handoff research. Treat the user's current observation that official ChatGPT iOS can join/continue another platform's active response as the highest-priority Runtime fact. This proves a late-join capability exists somewhere in the official service/client stack; it does not yet identify its transport or authorize guessing it.

Reuse the already-built privacy-safe official-iOS realtime Probe instead of modifying ChatGPTClient product code. The decisive observer and TrollStore packaging path already exist and statically match official native realtime types (`WebSocketConversationEventsService`, `WebSocketConversationObserver`, `WebSocketRegisterResponse.websocketURL`, `WebSocketTopic`, `SubscribePayload`, conversation-update/add-messages/async-status events).

Re-materialized research package identity is recorded in `docs/project/runtime-evidence/DEV-send-stream-cross-platform-late-join-priority-20260904.md`: official source ZIP `sha256:bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`; chained Probe dylib `sha256:0d20cf4761a982612fab995ed8766a887064005a561726c603edceea6072285e`; research IPA `ChatGPT-Official-RealtimeProbe-TrollStore-20260904.ipa`, `sha256:dd40dd092853f1e4dd4e52c560df0f1b24df18ebd47ca44015065442864ba555`. This is research tooling, not a product Candidate; b96 remains unallocated.

**Next exact action:** install/run the re-materialized official iOS realtime Probe, start a deliberately long response from another platform in the target project conversation, export `ChatGPTRealtimeProbe.jsonl`, and identify the first target-matching registration/subscribe/topic/update/catchup/live event before terminal. Analyze that evidence before allocating b96 or changing ChatGPTClient product code. No guessed topic/offset/resume, fixed polling, retry/watchdog/timer, duplicate Send, WebSocket-body authority or second response store.
