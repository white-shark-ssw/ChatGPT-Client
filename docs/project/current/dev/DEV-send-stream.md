# DEV-send-stream

## Status

**Active — exact b92 proves the covered project page-owned continuation path and client-owned protected Send/SSE terminal path on iPhone/iOS17. A narrower overlap regression remains: after switching away from an externally streaming conversation and starting a client-owned Send in another executor, the first external page-owned loop stops advancing and does not reacquire automatically on reselection; final assistant materializes only after explicit Sync. Stable/Frozen Send remains No.**

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

## b93 exact minimum A/B — not yet allocated

Next candidate, if allocated, must change only selection-time reacquisition for an already-active external response:

- when the user selects a conversation whose live snapshot is active and `promptText` is empty, reuse its existing executor;
- reacquire that executor's Native/Web document focus without page reload;
- log a distinct selection focus-rearm stage/result;
- retain b92 covered z-order, b91 scoped route parser, page-owned continuation transport, protected Send transport and Repository ownership;
- do not add background polling, retry/watchdog/timer, Native `stream_status`/`resume`, guessed offset, duplicate Send, WebSocket-body authority or a second response store.

Decisive Runtime test: external project response -> one Sync -> switch to another conversation -> complete one client-owned Send -> select the original external-live conversation again **without manual Sync**. If page-owned `stream_status`/external snapshots resume and naturally materialize/reconcile the final assistant, selection-time focus reacquisition is Runtime Positive. If not, reject it as sufficient.

## Validation / identity state

b90 package remains exact and unchanged: canonical Artifact `9882770072`, exact package source `99f1aa15...`, IPA SHA `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`.

b91/b92 exact package identities remain permanently reserved. b93 has not been allocated in this Runtime-recording checkpoint.

## Batch recovery state

**Closed for b92 Runtime classification. Next exact action:** perform a fresh resume/conflict guard, then allocate b93 only for the selection-time external-focus reacquisition A/B above. Do not modify continuation protocol or add speculative recovery logic.

## Preserved boundaries

Official page owns continuation transport; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling/cadence reproduction, retry/watchdog, duplicate Send, WebSocket-body authority, hidden-thought presentation or second response store.

## Session round counter

This user turn is **round 60**.