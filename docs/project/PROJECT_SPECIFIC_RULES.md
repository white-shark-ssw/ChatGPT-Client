## Phase 9 active-response navigation/reload closeout — b114 test candidate 2026-09-06

- While a conversation has an active Repository live response, leaving it at the current physical bottom preserves follow-tail by keeping no historical anchor; returning uses the existing latest-message path. Deliberate upward reading continues to save/restore the existing semantic message/chunk anchor. No parallel follow-tail dictionary or global streaming flag is allowed.
- Manual Reload is unavailable while any response is active because current Reload releases covered execution and clears live state, while server Stop is not yet proven. Local client-owned active Sync remains blocked; external-active manual Sync remains permitted as the already-evidenced authoritative recovery action.
- Completed color diagnostics are test instrumentation, not a permanent rendering dependency. Once b112/b113 Runtime is accepted, remove the b109-b111 per-chunk rendered-pixel probes without weakening the separate user/assistant reuse-pool invariant.
- Static official-app strings identifying `/stop_conversation` are not sufficient authorization to issue that request. Stop still requires current method/body/target/ack/terminal Runtime evidence.

## Stacked tested-Candidate integration ownership — b113 2026-09-06

- When an already-tested stacked task is integrated into its owning dependency branch, keep the original Candidate/Build ownership. For the current integration, Build113 / `DEV-message-rendering-0.1.0-b113` remains a `DEV-message-rendering` identity even though `dev/send-stream-20260829` now carries those product bits.
- Do not allocate or rename a new `DEV-send-stream` Candidate solely to represent an ownership-preserving merge. The last Send-owned Candidate remains b112 until new Send/Stream product evidence justifies a fresh unique Candidate.
- Existing Runtime evidence may be inherited across the merge only when source comparison proves the tested product paths are unchanged. CI on an integration commit is not a substitute for Human Runtime evidence.
- This rule does not change Send/SSE/Repository ownership: one protected Send remains one Send, `ConversationRepository` remains Native response/content authority, and the inherited b107 accepted clean-EOF gate stays separate until exercised.

## Native message rich-text presentation — Runtime accepted b113 2026-09-06

- The tested Runtime contract is now accepted for b113: ordinary user prose remains normal `.label`; only the actual HTTP(S) URL display span is system blue, including when Chinese/non-ASCII prose follows immediately with no whitespace.
- Preserve b112 user/assistant role-isolated reuse. Exact b113 Runtime `sha256:334a2f88d284e04936f0226c3cb6bdbad0710f1af5ead9c8168301fc5581af55` covers all five assistant chunks with zero cross-role user reuse, zero prior-link reuse and zero captured blue-dominant assistant output.
- Render authoritative/terminal assistant rich text before bounded attributed chunking; preserve raw Repository text as content/Copy authority. Do not introduce a second message store or reparsing timer/state machine.
- `filecite`/`cite` may remain readable non-interactive labels. Do not invent source navigation from opaque IDs until authoritative resource annotations are retained and evidenced.
- This rule is presentation-only. It does not alter protected Send/SSE/recovery ownership or prove unrelated Runtime gates.

## Native message rich-text presentation — b113 2026-09-06

- User body color semantics: ordinary text uses normal `.label`; only actual HTTP(S) URL/link display spans are system blue. A bare URL immediately followed by Chinese/non-ASCII prose must stop before that prose. Do not color the whole remainder of the user bubble blue.
- Preserve the b112 message-role reuse invariant: user and assistant cells remain in separate reuse pools. Visual link coloring must not be used as a reason to re-merge those pools.
- Assistant authoritative/terminal visible text may render native headings, emphasis, lists, inline/fenced code and pipe tables. Render the full message first, then bounded attributed chunks; raw Repository content and full-message Copy remain unchanged.
- Exact `filecite`/`cite` controls may be presented as readable citation labels. Until authoritative annotation/resource data is retained and evidenced, citation labels are non-interactive and opaque token IDs must not be guessed into URLs or file navigation.
- Do not expose hidden reasoning/tool/system content through the renderer. Do not add recurring parsing timers, streaming retry/state machinery or a second message-content authority for rich text.

## Message-cell role reuse isolation — Runtime accepted b112 2026-09-06

- User and assistant rows may share the `ConversationMessageCell` implementation class, but they must not share the same UITableView reuse identifier while user rows can render system-blue Markdown links. b111 proved user-link rendering can persist as UILabel layer/cache color across cross-role reuse; b112 Runtime `sha256:36fd01529ee522fd0646f7bdf6e6f409dca3f55a4b17ff21c88e4e19d16e23b2` proves role-isolated pools remove that contamination on the tested path.
- Assistant cells must therefore be dequeued from the assistant reuse pool and user cells from the user reuse pool. Preserve normal same-role reuse.
- Do not substitute repeated `textColor`/`tintColor`/highlight resets for this ownership invariant without new contrary Runtime evidence.
- This rule governs message presentation only. It does not create response/content authority and does not change user-link color semantics.

## New-chat first Send authoritative identity — b105 package rule 2026-09-05

- A Native New Chat draft has no server conversation identity and must not synthesize, persist or route on a fake ID.
- The first protected Send remains page-owned. Before the official `/backend-api/f/conversation` fetch is allowed to proceed for a new-chat Send, the official page itself must expose a concrete conversation ID through the already-evidenced conversation route parser (`/c/{id}` or scoped `/g/{scope}/c/{id}`).
- If the official identity is absent at that protected-fetch boundary, block that fetch and fail visibly with the symbolic `new_conversation_identity_missing`; do not send first and recover/guess identity later.
- Once the official ID is observed, re-key the same covered executor exactly once and create exactly one `ConversationRepository` live response generation for the real ID. Do not start a second protected Send or second response owner during handoff.
- If the user left the draft before identity adoption, the new server turn may continue hidden under its real ID; do not force visible selection back. A successful terminal authoritative Detail may trigger one conversation-list refresh to reconcile the real server conversation into the sidebar.
- Existing accepted-client hard-Web no-resend recovery applies after explicit HTTP200 SSE acceptance. No polling, timer/watchdog, guessed Native resume/status, challenge replay, duplicate Send/regenerate or second response/content store is authorized.
- Stop remains evidence-gated and is not part of b105.

## Accepted client Send hard-Web recovery — Runtime accepted / b104 normal rule 2026-09-05

- b103 Human Runtime `sha256:99049f500c129571d33aa628720f7d23ce5cf6d183e887938cd7fa621a3bbc51` supersedes the earlier test-pending wording: for the tested foreground iPhone/iOS17 path, a protected Send that has already returned HTTP200 `text/event-stream` may survive hard covered-WebContent death and must retain the same prompt-owned `ConversationRepository` generation rather than being marked failed solely because the transport process died.
- On that exact post-acceptance hard termination signal, release only the dead executor transport and attach one fresh covered observer to the same conversation/generation while active; if inactive, do not start background network work and defer the fresh observer to foreground. Never resend/replay/regenerate the prompt.
- Before explicit Send acceptance, hard WebContent death remains failure/no-resend. Generic navigation failure, silence, elapsed time, missing snapshots, route state and focus state are not equivalent hard-disconnect evidence.
- The b102/b103 deterministic 120-second kill probe is retired after this Runtime proof. Normal candidates from b104 forward must not contain its timer, JavaScript swizzle or `_killWebContentProcessAndResetState` test SPI unless a future explicitly scoped diagnostic experiment is separately justified and allocated.
- `ConversationRepository` remains the sole response/content authority; this rule authorizes no polling, heartbeat, retry loop, challenge replay, guessed Native resume, duplicate Send, second live-response store or claim of true background execution.

## Accepted client Send hard-Web recovery — b103 test candidate 2026-09-05

- b102 Runtime proved that a client-owned protected Send with explicit HTTP200 `text/event-stream` acceptance can survive hard `WKWebView` WebContent death server-side and later be reacquired through the already-evidenced covered observation + authoritative Detail chain without a second Send.
- b103 may treat hard WebContent death as a recoverable receive-transport interruption **only after** exact client Send acceptance has been observed. Before explicit acceptance, existing failure semantics remain mandatory and the prompt must never be replayed/resubmitted automatically.
- Accepted-client recovery must preserve the same `ConversationRepository` generation and prompt-owned live snapshot. Recovery may attach one fresh covered observer for the same conversation and feed evidenced external snapshot/resume/live events into that same generation; it must not create a second response/content authority.
- If the app is inactive when WebContent dies, do not start background network work. Leave the accepted client generation active and reattach one fresh covered observer on the next foreground lifecycle.
- The one-shot 120-second forced kill may be Candidate-gated to exact b103 solely as deterministic Human Runtime instrumentation because the b102 trigger itself is Runtime proven. It is not a response timeout, watchdog, keepalive or production scheduler and must not survive into a later normal/Stable candidate.
- Navigation failure, silence, missing snapshots, route/focus state and elapsed time are not generalized disconnect signals. b103 adds no polling, heartbeat, retry loop, duplicate Send, regenerate, challenge replay or guessed Native resume.

## Deterministic covered-Web kill probe — b102 test-only 2026-09-05

- The b102 120-second `WKWebView` kill is allowed **only** as Candidate-gated Human Runtime instrumentation for the explicit client-owned WebContent-death test. Never carry this timer into a later normal product candidate or treat elapsed time as disconnect evidence.
- Arm once from the existing covered protected-Send submit marker; do not read/log prompt or script body. Kill only the exact observed `WKWebView`, only through `_killWebContentProcessAndResetState` when `responds(to:)` succeeds.
- The probe must not call protected Send, resume, status, Sync, Reload, retry, regenerate or any response API. Current client-owned death failure semantics remain unchanged during b102 so Runtime evidence is causal.
- A qualifying run requires the client-owned response still active when `coveredExecutor.killProbe state=firing` occurs. If the answer already completed, an idle Web kill is not evidence for active-response death recovery.

## Native read transport loss recovery — b101 2026-09-05

- The only automatic Native transport retry authorized by b101 is for the first exact `NSURLErrorDomain / NSURLErrorNetworkConnectionLost (-1005)` from an idempotent conversation-list or Conversation Detail GET using the current account-scoped cached transient session.
- Recovery must retire only the matching cached transient session, reacquire one fresh transient session through the existing default-WebKit-auth path, preserve the existing account scope and operation generation, then retry the same read once. There must be no third attempt.
- A second `-1005`, any other network error, auth/HTTP failure, supersession or account change terminates normally. Do not generalize b101 into a retry framework, timer, watchdog, reachability monitor, polling loop or background keepalive.
- Protected covered-Web Send is excluded. Never resend/replay/regenerate a prompt because Native list/Detail transport was renewed. `ConversationRepository` remains content/response authority; `AuthSessionStore` remains account authority.

## Foreground dormant cross-platform discovery — b100 2026-09-05

- Foreground recovery must not require a pre-existing external live snapshot. With a selected conversation, no client-owned active response and no Detail operation, one lifecycle transition may issue exactly one existing authoritative `ConversationRepository.syncLatestMessages`.
- If final assistant is already materialized, use Detail directly. Rearm the existing covered observer only for a newly discovered unfinished remote user turn or active external projection.
- Never turn this into polling, retry, timer, keepalive, resend/regenerate, guessed resume, or a second response store.
- TD-029 protected Send ownership, b99 UI coalescing, b98 WebContent recovery, b97 active-external reconcile and Sync/Reload semantics remain unchanged.

## Live-response presentation coalescing — b99 2026-09-04

- Repository live-response events must remain lossless and ordered. Do not reduce transport/state event granularity to fix UIKit performance.
- The selected `ConversationDetailViewController` may coalesce multiple pending Repository change notifications into one main-queue presentation rebuild using the latest snapshot. The coalescing state is UI-only and must not become response authority.
- Do not add a timer, display cadence, retry, watchdog, polling loop, background heartbeat, resend/regenerate path or second response cache for this optimization.
- On execution, re-check displayed/selected conversation identity and preserve the existing authoritative-Detail replacement path when the live projection has already disappeared.
- b98 hard WebContent termination recovery and b97 foreground Detail reconcile remain unchanged and separately gated by their own Runtime evidence.

# Project-Specific Rules

## Accepted client SSE clean-EOF recovery — b107 2026-09-05

- Exact b106 Runtime proves an HTTP200 `text/event-stream` protected Send may finish server-side even when the covered filtered response ends without observing exact `[DONE]`; therefore exact `stream_ended_without_done` after explicit acceptance is a receive-transport interruption, not sufficient evidence to mark the Repository response failed.
- For that exact condition only, preserve the same prompt-owned Repository generation and reuse the existing accepted-client covered-observer recovery path. Never replay/resend/regenerate the prompt.
- A successful authoritative manual Sync may clear an already non-active client live projection only through the existing `clearLiveResponseAfterAuthoritativeReconcile` count/baseline guard. This prevents authoritative + stale-live duplication without creating another content authority.
- Do not generalize this rule to pre-acceptance failure, arbitrary navigation failure, silence, timeouts or unknown stream errors. No polling, retry loop, timer/watchdog, guessed resume/status or second response store is authorized.
- Assistant blue-text corruption remains separately evidence-gated; do not add speculative color fixes under this recovery rule.


## Hard covered-Web process recovery for external observation — b98 2026-09-04

- `webViewWebContentProcessDidTerminate` is the only new automatic recovery trigger authorized by b98. Do not use silence duration, lack of snapshots, focus state, route state or generic navigation failure as a substitute disconnect detector.
- When the executor is observing an external/cross-platform response, hard WebContent termination must preserve the current conversation identity, external observation callback and `ConversationRepository` live-response projection. It must not emit response `.failed` solely because WebContent died.
- If the app is active, issue exactly one existing full-page external-observation rebootstrap for that termination event. If inactive/background, do not start background network work; the existing foreground path owns later one-shot authoritative Detail reconcile and Web rebootstrap.
- Client-owned protected Send is excluded from this recovery rule: WebContent death remains failure and must never automatically resend, replay or regenerate the user prompt.
- b98 adds no recurring retry, timer, watchdog, Native status/resume synthesis, challenge replay, background heartbeat or second response store. TD-029 and the b97 foreground authoritative reconcile rule remain in force.

## Foreground external-response authoritative reconcile — b97 2026-09-04

- This section **supersedes** the earlier b96 `Native cross-platform Detail continuation exception` below. Do not use the b96 10-second `DispatchWorkItem`/async-status-driven Native polling path; Human Runtime showed ordinary authoritative Detail may omit `conversation_async_status` entirely.
- When `UIApplication.willEnterForegroundNotification` fires and the currently selected conversation already has an active external live response (`phase.isActive` with empty Native prompt), Root may issue exactly one existing `ConversationRepository.syncLatestMessages` request if no Detail operation is already in flight.
- This is lifecycle-triggered authoritative reconciliation, not polling. There is no recurring schedule, retry, fallback or background keepalive. Covered-Web foreground rebootstrap may still run for the same external response if authoritative Detail has not materialized terminal state.
- If the one-shot Detail contains a newly materialized final assistant, existing Repository reconciliation must remain the sole owner that removes the external live projection; Root may then release the idle covered executor. TD-029 protected Send ownership is unchanged.
- Do not describe b97 as true background completion. iOS suspension behavior remains authoritative; b97 validates convergence after return to foreground.

## Native cross-platform Detail continuation exception — b96 2026-09-04

- The prior general prohibition on Native polling remains in force except for this evidence-scoped b96 path: an authoritative `GET /backend-api/conversation/{id}` response that itself reports exact `conversation_async_status=IS_STREAMING` may schedule the next request of that same already-existing Detail route under the sole `ConversationRepository` authority.
- Missing/unknown status must not start the loop. Any authoritative non-`IS_STREAMING` result stops it; exact `COMPLETE` is the expected evidenced terminal token. Client-owned response authority and account-scope reset terminate external Native continuation.
- The current 10-second cadence is a test-candidate approximation, not a frozen service constant. Do not generalize it to idle/global polling, `/stream_status`, `/resume`, retries, watchdogs or fallback loops.
- This exception is cross-platform/read continuation only. TD-029 covered official-Web protected Send/challenge ownership is unchanged.

## Hard Reload recovery invariant — 2026-09-04

- `重载当前会话` is an exceptional recovery control and must remain enabled whenever a current conversation is selected. Active local/external response, stuck external state, or an in-flight Sync/Reload must not disable this action.
- Reload semantics are a conversation hard reset: invalidate/release the current covered executor/observation, clear the current Repository live-response projection without rolling its generation counter backward, clear current page presentation/resident Detail, and start one replacement authoritative Detail load. Existing detail-operation replacement ownership supersedes the older request.
- Reload is not Send, regenerate, retry, polling, watchdog, or server Stop. It must never duplicate the prompt or claim that remote generation was cancelled.
- After authoritative Reload succeeds, only the returned server Detail may decide whether an external live projection is rebuilt and a fresh covered observer is attached.
- This recovery invariant does not relax the Send/continuation architecture boundary: official page owns continuation transport; `ConversationRepository` remains the sole Native response/content owner.

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

## b89 current package rule — 2026-09-03

- Exact b89 is emitted and permanently reserved: `DEV-send-stream-0.1.0-b89`, Build89, product commit `f39bc9387575028d431b85409780a2f3670b3259`, exact package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676`, canonical Push Artifact `9881665748`, IPA SHA `c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`.
- b89 may change only covered Web interactivity plus privacy-safe automatic user-activation diagnostics relative to b88; it does not authorize route synthesis, Native status/resume/offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or another response owner.
- CI/Artifact/package success is not Runtime proof. Retain b89 only if a clean long-response real-device A/B supports the interactivity differential; otherwise reject it as sufficient and return to SPA/router-entry evidence.
## b82 current Runtime override — 2026-09-02

- Exact b82 is permanently reserved: source `c7a274786dfd175e8f476fc15c4964840e112a1d`, Artifact `9811406038`, IPA SHA `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`.
- Automatic no-manual-Sync final acquisition is Runtime positive, but live timing is rejected: the target-matching user-socket event arrived when authoritative Detail already added the remote user+assistant pair, and there was no earlier observed live acquisition event.
- Treat the current exact target-match socket event as completion/update discovery only. Do not label it request-start or live-stream authority.
- The current requirement is prompt remote-user visibility plus real progressive response. No fake typewriter, synthetic optimistic remote user row, duplicate Send, speculative retry/watchdog, silent polling/timer or second response owner.
- b83 is not allocated until an earlier source is evidenced or a deliberate new monitoring architecture is explicitly authorized from evidence.

## b76 current candidate override — 2026-09-01

- Exact b76 is allocated and permanently reserved: `DEV-send-stream-0.1.0-b76`, Build76, exact product/config source `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71`, Artifact `9775920927`, IPA SHA `b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd`.
- Current official-page external continuation is not `/resume`-SSE-only. A page-owned resume still requires exact HTTP200 SSE before SSE adoption; current evidence also allows official page-owned resume 404 followed by its own status/plural read path.
- Production may observe only the page's already-issued matching status/plural responses. It must not construct/schedule Native polling, copy cadence, construct resume/offset, parse WebSocket bodies, resend, add retry/watchdog behavior or create a second conversation/message/response store.
- Plural `messages[]` is rolling/paged; raw count is not a cursor. Bound the active segment by the latest user service message, validate target identity and project snapshots atomically into the sole `ConversationRepository` response owner.
- `assistant:thoughts` / inline COT remain non-presentational; exact-parent tool association and narrow GitHub detail mapping remain unchanged.
- b76 tool/reasoning/final line heights are candidate 30/21/21. Runtime visual acceptance pending.
- Code/static/Simulator/Push+PR CI/Artifact/package are passed; real-device Runtime and Stable/Frozen remain **No / Unverified**.

## b75 current Runtime override — 2026-09-01

- Exact b75 package is permanently reserved: source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, IPA SHA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`.
- A page-owned matching `/resume` request is structural observation only. Exact b75 covered-production Runtime returned HTTP404 JSON for all three observed matching resume attempts while the external response was active; current external stream adoption is therefore **not Runtime accepted**.
- Do not bypass this with Native resume/offset construction, `stream_status` polling, retry/timer/watchdog, guessed route fallback, duplicate Send or WebSocket body parsing. Use Web Rule Lab to establish the current page-owned transport first.
- b75 `26 / 18.2 / 18.2` tool/reasoning/final line-height output is visually rejected as too tight. Those numbers are not an accepted presentation baseline.
- b76 may be allocated only after the continuation probe defines a minimal current transport correction and the larger visual-spacing correction is coherent; until then b76 remains unallocated.

This file contains durable repository/product rules backed by explicit requirements, current source, accepted tests or technical decisions. Detailed historical evidence belongs in `BUILD_TEST_INDEX.md`, runtime-evidence files and Git history. Current rules below take precedence over stale historical wording.

## Product and architecture contracts

- Product is a native Swift/UIKit iOS ChatGPT client distributed primarily as a TrollStore IPA.
- Stable merged native baselines remain b9 read, b15 recovery, b21 multi-conversation state, b23 list-cache core and b38 conversation metadata/settings/round navigation for their recorded scopes. Stable does not mean Frozen.
- Exact Stable Phase 8 tested source remains `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Pure-native/transient-auth ChatGPT-account protected Send remains blocked by exact b42 browser-challenge evidence.
- The separately billed API-product route remains rejected unless that explicit product decision changes. Primary-account Sub2API/Codex-subscription route remains blocked by the account-safety decision.
- **TD-029 is current production Send architecture.** Native composer/history/reasoning/tool/final UI is the product surface. One process-resident covered official ChatGPT Web execution surface may use the existing default persistent `WKWebsiteDataStore` to let the official page perform browser challenge + exactly one protected Send for each Native Send action.
- Covered Web is transport/challenge execution only. It is not a conversation, message, response, list, draft or scroll-state authority.
- `ConversationRepository` is the sole native production conversation/list/detail/recovery/**response lifecycle** authority.
- `AuthSessionStore` remains sole native auth/account-context authority.
- `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority; no second Cookie/token/challenge store.
- TD-025/TD-028 still reject the b44 full-page Native->Web->Native product form and full mobile-Web conversation rendering as the daily-chat dependency.
- Final Composer hierarchy/drafts/attachment staging belong future serialized `DEV-composer-parity`; `DEV-send-stream` may retain only a minimal validation trigger until Send/Stop/response semantics are accepted.

## Web Send adapter contract

`docs/project/WEB_SEND_ADAPTER.md` is the durable authority for current evidenced official composer/protected-Send/SSE/reasoning/tool rules and Web rule-update workflow.

Core production invariants:

- Native Send must trigger exactly **one** official page-owned protected Send; no second Send merely to obtain a stream.
- The official page owns Sentinel/PoW/Turnstile/conduit/challenge generation. Native code must never solve, synthesize, copy for replay, persist or expose those values.
- Accepted composer authority is `#prompt-textarea` or explicit `[contenteditable="true"][role="textbox"]`; generic textarea remains rejected.
- A JavaScript `submitted` return is not success proof. Real `sendObserved` + HTTP/SSE lifecycle is required.
- Current tested protected route is official page-owned `POST /backend-api/f/conversation` -> HTTP200 `text/event-stream`.
- Current cross-device continuation evidence additionally authorizes **observation only** of the official page's own matching `POST /backend-api/f/conversation/resume` `{conversation_id, offset}` -> HTTP200 SSE. Native must not construct resume/offset, poll `stream_status`, replay browser headers, use the user WebSocket as response-body authority, or issue a second Send.
- Unknown/new Web/SSE shapes stay observable and must not trigger guessed state transitions.
- Do not accumulate speculative selector fallbacks, retry loops, timers, polling or watchdogs. When Web changes, probe the current page and replace/update the rule from evidence.
- A local production orchestration bug is **not** a Web-rule change merely because the page request fails. b66 proves this distinction: the service accepted the Send while duplicate Swift->JS submit orchestration caused the production wrapper to lose its Response before `sendResponse`.

## Covered executor operation gate

Exact b66 Runtime established a durable one-Send orchestration rule in addition to the Web adapter rule:

- one Repository response operation owns one `activeEvents` executor lifetime from accepted local request until terminal/failure;
- `pendingSend` is only the not-yet-issued JS submission payload, not the whole response lifetime;
- once the one JS `submit(...)` evaluation is issued, consume/clear that `pendingSend` immediately;
- repeated composer-ready callbacks after issuance must not schedule the same prompt again;
- executor busy state must remain true through the existing active response operation, not reopen merely because the pending payload was consumed;
- do not solve duplicate-submit races with debounce, timer, retry, resend, delayed submit, polling or a second state flag when the existing operation owner can enforce the invariant.

Exact b67 implements this by using existing `activeEvents != nil` for `isBusy` and clearing `pendingSend` immediately before the one JS submit evaluation. Exact b67 production transport Runtime is accepted for the recorded existing-conversation scope.

## Web Rule Lab contract

The app retains a development-only **Web Rule Lab** for future ChatGPT Web changes.

- reachable from Settings;
- uses the same `WKWebsiteDataStore.default()` login/session state as production Web execution;
- visibly presents a normal `WKWebView` while probing;
- user explicitly pastes/edits JavaScript and taps `执行`;
- no script auto-runs on page load or app launch;
- script text and returned body are temporary UI state only;
- allow copy/share of temporary result;
- do not persist Lab script/result bodies into `DiagnosticsLogger`, `UserDefaults`, files or another database;
- diagnostics may record only safe execution lifecycle/result type/length;
- the Lab is never a production Send/response owner.

Future Web update process:

`reproduce exact failure -> AI provides one small JS probe -> user runs it in Web Rule Lab -> collect structural evidence -> update WEB_SEND_ADAPTER rule -> one minimal product change -> one coherent Candidate/Artifact -> exact Runtime validation`.

Do not return to speculative IPA builds for selector/event discovery when the Lab can answer the structural question directly.

## Send / stream parser and presentation rules

Current accepted b48-b65 parser/presentation rules remain unchanged by b66/b67:

- compact assistant text continuation includes evidenced `o/p/v` + contextual continuation grammar and b51 continuation across exact `title_generation`;
- do not generalize arbitrary `v:string`, arbitrary nested values or arbitrary initial assistant parts into visible text;
- exact service-marked thinking preamble (`metadata.is_thinking_preamble_message=true`) is user-visible reasoning text;
- exact `reasoning_status=is_reasoning` may drive state only and never authorizes `assistant:thoughts` body;
- exact `reasoning_ended` is current reasoning->final phase authority;
- accepted visible text before that marker belongs to `思考过程`; accepted text after it belongs to final answer;
- `assistant:thoughts` is always non-presentational;
- initial/repeated `正在思考` must be event/response-state driven, never timer driven;
- if a terminal non-reasoning turn has no exact reasoning-end marker, deterministic promotion of already-accepted provisional text to final is permitted; this is classification, not retry/fallback.

Official-like target flow remains:

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次正在思考/思考流 -> reasoning_ended -> 自动折叠思考 -> 完整最终回答`.

Not every response requires reasoning or tools; UI follows actual service events.

## Tool activity / detail rules

- invocation->result association is response-local exact `result.metadata.parent_id == invocation service message ID` only.
- never pair by order, adjacency, count alignment, title/name or recipient equality.
- unmatched results remain unmatched and never force-complete a Native tool row.
- local tool slots are response presentation bookkeeping only, never a second message/repository authority.
- GitHub connector raw input/output mapping remains authorized only for the b63-b65 evidenced exact-parent GitHub shape.
- authorized GitHub input = invocation `metadata.connector_tool_payload`.
- authorized GitHub output = exact-parent matched completed result `message.content`; current b72+ product requirement deliberately does **not** present tool output in the normal tool-list sheet. Retaining authorized source data for response association does not require showing it.
- main inline reasoning is semantic: show only meaningful service-authored tool-purpose titles; omit fallback `工具调用` rows from the main surface without deleting the ordered tool list; never synthesize/merge titles by guess.
- clicking a concrete main tool row opens the current assistant turn's ordered tools-only list; authorized input is shown directly without a `工具输入` disclosure/title; no reasoning prose and no tool-output UI.
- do not generalize raw connector detail to another connector family until separately evidenced.
- `assistant:thoughts`, unmatched result bodies and unrelated unverified connector payloads remain prohibited from Native presentation.

## Production response ownership

Conceptual owner:

`verified account scope + authoritative conversation identity (or one Repository-owned pending new-chat token) + response operation identity -> response lifecycle`.

Rules:

- no global `isStreaming` state owner;
- no VC/cell-owned response lifecycle;
- no second stream/message store;
- no Web DOM/text-derived conversation authority;
- navigation never Stops an active response merely because it becomes hidden;
- at most one active response per conversation until stronger evidence supports overlap; do not globally serialize unrelated conversations by guess;
- one lifecycle reaches one deterministic terminal state; duplicate terminal callbacks cannot double-commit/double-haptic/double-notify;
- active response residents are protected from normal memory-warning eviction;
- response state must survive A hidden while B is selected.

b66 memory-warning evidence occurred only after its response had already failed; `resident.evictionSkipped` confirmed the tested protected resident was not evicted, but this is not full background/memory-warning acceptance.

## External active-response adoption

- Entering a conversation may expose an active response started by another platform only when the covered official page itself issues a `/backend-api/f/conversation/resume` whose request `conversation_id` exactly matches the executor's authoritative target.
- The page remains continuation-transport authority; Native observes a cloned SSE response and feeds accepted events into one existing `ConversationRepository` response generation.
- External adoption does not invent an optimistic prompt/user bubble; authoritative user history remains Repository Detail data.
- Native never chooses/derives offset, constructs the resume request, polls `stream_status`, replays browser/session headers, resends the prompt, or treats WebSocket frames as message-body authority without separate evidence.
- b74 was the first packaged candidate for this boundary; exact b75 Runtime now rejects the covered-production adoption path because matching page-owned resume responses were HTTP404 JSON. Re-probe before another product implementation.

## New-chat identity handoff

Use a local pending target only if actual server timing requires identity before authoritative conversation ID arrives.

If used:

- one Repository-owned opaque pending token per verified scope + one Send operation;
- never pretend it is a server conversation ID;
- never persist it into list/cache/server routes;
- first validated authoritative ID performs one atomic re-key/adoption;
- same response lifecycle continues; no second response/Send;
- UI selection/list handoff occurs once without duplicate conversation or navigate-away/re-enter;
- conflicting later server identity is an error;
- obsolete account/operation callbacks cannot re-adopt old pending state.

`新对话` is presentation only, never identity authority.

## Stop contract

Do not claim server Stop until exact current evidence establishes route/mechanism, target identity, acknowledgement and terminal semantics.

- local Web/URL task cancellation is not proof server generation stopped;
- do not ship a fake Stop that only hides UI while presenting it as server Stop;
- no automatic resend/regenerate after Stop/interruption;
- partial-content authority and whether later explicit Sync is needed must come from Runtime evidence.

## Follow-tail / multi-conversation contract

- `ConversationRepository` owns response activity; `ConversationDetailViewController` owns viewport intent.
- if A is at/near latest and owns an active response, A may follow its tail;
- deliberate upward user scrolling exits follow-tail and establishes historical-reading intent;
- hidden A growth never mutates B viewport;
- return to eligible A shows current latest bottom;
- return after history intent restores A's semantic anchor;
- b38 quick navigation to older rounds establishes history intent;
- programmatic scroll callbacks are not user drag.

Exact near-bottom threshold is Runtime tuning, not a preflight constant to guess.

## Native UI / message geometry contracts

- Official ChatGPT iOS interaction is the default baseline where acceptable; implement natively where architecture permits.
- `UISplitViewController`/native navigation remains compact navigation owner.
- UI text/title is a consumer, never identity authority.
- `ConversationRoundProjection` remains the single semantic round projection.
- each authoritative visible user message starts a round; hidden/internal nodes do not.
- `AppPreferences` remains the single persisted native settings owner.
- timestamps use authoritative historical time when available; omit rather than fabricate.
- Copy uses full authoritative visible message text and never issues network requests.
- Stable b37/b38 bounded display chunks + deterministic row geometry/manual layout remain message-presentation baseline.
- Stable b38 quick navigation uses derived O(1) geometry and one cancellable `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)`; no pre-jump teleport, `scrollToRow` geometry discovery, correction snap or debounce.
- rapid retargeting starts from current visual position; real finger drag immediately retakes ownership.
- per-conversation scroll state is semantic presentation state, not Repository message state.

## Manual recovery contract

- `同步最新消息` and `重载当前会话` are explicit authoritative Repository recovery actions and never resend/regenerate prompts.
- preserve an already loaded detail on Sync failure where applicable.
- newer explicit same-target Sync/Reload may cancel/replace only older same-target detail/recovery ownership; freshness rejects obsolete callbacks.
- no automatic retry/watchdog/timer/resend/regenerate chain.
- while response-active reconciliation semantics are not accepted, unsafe Sync/Reload may be explicitly disabled rather than guessed.
- terminal authoritative reconciliation may invoke one existing Sync after a true response terminal; it must not become a readiness polling loop or resend path.

## Cold-start auth / list-cache contracts

- default persistent WebKit store remains sole persistent auth-secret authority.
- Native `/auth/login` is not account-context authority. Accepted sequence remains WebKit context -> `/api/auth/session` -> transient auth -> accounts-check.
- `ConversationRepository` remains sole list/conversation authority; `ConversationListCacheStore` is storage only.
- persist only small versioned account-scoped list summary snapshot + privacy-safe bookkeeping, never Detail bodies or copied auth secrets.
- provisional cached rows cannot authorize Detail/Send until current account scope is verified.
- temporary auth/network failure may retain valid provisional rows without becoming logout or automatic retry.
- accepted rapid-relaunch freshness/manual-refresh/authoritative-total list-cache rules remain unchanged.

## Diagnostics / privacy contract

Use existing `DiagnosticsLogger` authority.

Never persist/export through normal diagnostics:

- prompt/assistant/reasoning bodies;
- tool title/body/raw input/output;
- `assistant:thoughts`;
- raw account/conversation/message/response IDs;
- Cookie/Authorization values;
- Sentinel/PoW/Turnstile/conduit/challenge values;
- Web local/session storage;
- Web Rule Lab script/result bodies.

Permitted diagnostics are bounded structural/aggregate facts such as route class, HTTP status, safe event/key/type shape, counts, character lengths, phase/terminal reason, local generation/slot, safe result type/length and non-secret viewport geometry.

## Candidate / identity contract

- every testable Candidate has unique version/build/Candidate/Artifact identity;
- Code / static / CI / Artifact / Runtime / Stable are separate evidence levels;
- once an Artifact identity is emitted, corrected product code never reuses it;
- built `Info.plist` version/build/Candidate/source marker + IPA SHA are package identity authority;
- `scripts/build_ipa.sh` must fail on identity mismatch;
- b24-b75 emitted identities are permanently reserved;
- exact b66 package authority remains `0.1.0 (66)`, source `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`, Artifact `9739572172`, IPA `7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`; Runtime rejected its first production bridge but does not invalidate package identity;
- exact b67 package authority is `0.1.0 (67)`, source `52ab38f16fe914ef8316bb1dc712b77c2c87a271`, Artifact `9739891865`, IPA `3712dec92cddfe64e84fc797e1506d83231cd878633b932b9acf0e7381795497`; production transport Runtime accepted for the recorded scope;
- exact b73 package authority is `0.1.0 (73)`, source `4edda892a04a1a07f4a07e74b135b969ea82193e`, Artifact `9764247402`, IPA `8285ba9d5f63207feb2eaf722ec722a886f3ee88956236a89a716ad58b884113`; Runtime presentation pending;
- exact b74 package authority is `0.1.0 (74)`, source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`, Artifact `9768668727`, ZIP `6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`, IPA `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`; permanently reserved;
- exact b75 package authority is `0.1.0 (75)`, source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, ZIP `6c4c4ec9de54264846376bdf7df4679daaaf33168481831698c884093b6209ad`, IPA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`; Runtime partial/rejected and permanently reserved;
- do not allocate b76 before the current Web Rule Lab continuation re-probe resolves the covered-production 404 behavior.

## Message rendering / attachment boundary

- ordinary native message body remains plain string until future `DEV-message-rendering`; Markdown/code/table/link/citation rendering remains a separate Work.
- reasoning/tool-card lifecycle semantics remain `DEV-send-stream`.
- final Composer/drafts/attachment staging remain future `DEV-composer-parity` and must consume accepted Send/Stop APIs rather than own them.
- attachments remain high priority but Send-boundary dependent.
- no private WebKit/DOM/file-input injection for iOS17 attachment support without separately evidenced public/engine-compatible path.

## Background / compatibility

- background continuation follows `BACKGROUND_EXECUTION_PLAN.md`; no automatic prompt resend and no second response store/stream.
- public `beginBackgroundTask` is a finite baseline only, never a long-duration guarantee.
- main-app process survival is not WebKit-stream survival proof.
- b45 positive short-background evidence remains valid; full background acceptance waits for successful production Repository response ownership and its own Runtime matrix.
- Native iOS/TrollStore primary runtime remains iOS17; build minimum remains iOS14 unless concrete evidence changes it.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/Artifact/Runtime/architecture/status changes update checkpoint + durable docs in the same cycle.
- final merge reconciles actual target branch state without overwriting parallel work.
- non-atomic GitHub write chains use the selected checkpoint recovery point and never blindly replay confirmed writes.
- tooling-only assembly commits/refs are never Work/Candidate authority.

## Critical invariants / prohibited routes

- full existing-conversation Web rendering is not accepted merely because it is hidden/display-trimmed;
- covered official Web under TD-029 is only evidenced Send/challenge executor, never a second state owner;
- no challenge bypass/replay;
- no duplicate Send to obtain stream/recovery;
- no speculative timer/watchdog/retry/polling/compatibility-shim chain;
- no arbitrary alternate private endpoints;
- no unrelated refactor for safety theatre;
- CI/Artifact success is never Runtime proof;
- Stable does not mean Frozen; no Frozen business/architecture modules are currently recorded.

## Code style / naming constraints

Follow existing repository style and established APIs/names. Do not rename interfaces or variables without source-backed need. Keep concise statements on one line where natural.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses belong to an Active checkpoint. Web-specific current rules and update procedure live in `WEB_SEND_ADAPTER.md`; detailed Candidate history lives in `BUILD_TEST_INDEX.md` and runtime-evidence files.