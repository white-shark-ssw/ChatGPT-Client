# Technical Decisions

## DEV-send-stream b96 Native authoritative Detail continuation decision — 2026-09-04

- Retire further private response-callback swizzling inside the official iOS app for the current late-join gate; repeated injected-package crashes make that research method observably destabilizing.
- Accept one narrow Native continuation experiment in `ConversationRepository`: only an already-authoritative Conversation Detail response with exact `conversation_async_status=IS_STREAMING` may start/continue refresh of that same existing Detail route. Exact `COMPLETE` or any non-`IS_STREAMING` authoritative result terminates; missing/unknown does not start.
- The 10-second b96 interval is a Runtime-backed candidate approximation from repeated official ~9-12s Detail requests plus static `default_interval` / `model_slug_intervals`; it is not asserted as the exact compiled official value and remains subject to Human Runtime validation.
- This decision does not authorize idle/global polling, Native `/resume`, guessed offsets, retry/watchdog/fallback, duplicate Send, WebSocket-body authority, challenge replay, or a second response store. TD-029 protected Send remains unchanged.

## DEV-send-stream Probe v0.3 observation decision — 2026-09-04

- Treat the v0.2 76 MB / 195,999-error sample as **observationally perturbed and overall Inconclusive**, not as evidence that official iOS late-join has no conversation transport.
- The next research delta is deliberately narrow: remove per-receive-arm logging, deduplicate repeated receive errors on one failed WebSocket task, and add the two URL-form `NSURLSession` data-task constructors that the exact official binary exposes but Probe v0.2 did not hook.
- Do **not** add a global task-resume hook yet. Escalate to that broader observer only if exact v0.3 visually confirms official iOS late-join while still recording no target-correlated HTTP/SSE/WebSocket acquisition event.
- Static official-iOS strings for `stream_handoff`, `resume_conversation_token`, `turn_exchange_id`, `topic`, `resume_sse_endpoint`, `ConversationResumeFetchRecovery`, and inline stream-status/fetch recovery prove native continuation/recovery machinery exists, but do not prove the active late-join branch and do not authorize product polling/cadence reproduction.
- This is research tooling only. Product ownership and b95 identity remain unchanged; b96 remains unallocated.

## DEV-send-stream b93 selection-focus A/B decision — 2026-09-03

- Exact b92 Runtime is Partial: covered external continuation works and client-owned protected Send/SSE natural terminal reconciliation works, but when an external live executor overlaps a second client-owned Send, the first stream can stop advancing and does not recover merely by reselection; explicit Sync later materialized the already-completed assistant.
- Exact b93 tests one evidence-backed variable only: when reselecting an already-active external response, reuse the existing covered executor and restore WKWebView first-responder/document focus without reload or Sync.
- b93 identity: allocation `b86c1a3ca94b215204b0cfb135fa0cd8b3603619`, product `556bd8886061f4126d11e4ac44f4e24ed580500c`, package source `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0`, Push `33755063112/100647405265`, PR `33755067202/100647418537`, Artifact `9893141097`, IPA SHA `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d`.
- b93 package inspection: `0.1.0 (93)`, Candidate `DEV-send-stream-0.1.0-b93`, source `2d2cde58a7fb`, iOS14+, `[1,2]`, iphoneos, arm64. Human Runtime pending; Stable/Frozen Send No.
- Preserved boundary: official page owns continuation transport, Repository owns Native content. No polling/retry/watchdog/timer, Native status/resume synthesis, guessed offset, duplicate Send, WebSocket-body authority, or second response store.
- This is an A/B, not a declared root-cause fix: b92 blur events lacked executor identity, so focus handoff remains the strongest evidenced differential, not proven causality.

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

## b89 interactivity A/B package qualification — 2026-09-03

- Fresh-root visible official Web already proved unscoped `/c/{conversation}` can canonicalize to exact scoped `/g/{scope}/c/{conversation}` and start page-owned continuation with transient user activation false, so scoped-route identity alone is no longer the remaining b88 explanation.
- b89 therefore tests one remaining covered-WKWebView differential only: `isUserInteractionEnabled=true` instead of false, retaining the already-proven b88 first-responder focus/rearm behavior. Existing page-activation diagnostics additionally record privacy-safe `navigator.userActivation.isActive` / `hasBeenActive`; no user-triggered Web Rule Lab probe is needed.
- b89 is Code/Simulator/Push+PR CI/Artifact/package verified but Runtime Pending. Do not treat interactivity or user activation as causal until a clean early/mid-generation real-device run observes page-owned `stream_status`/resume/snapshot continuation while the remote generation demonstrably remains active.
- Existing prohibitions remain: no Native status/resume/offset synthesis, polling/timers/retries/watchdogs, router emulation, duplicate Send, WebSocket-body authority or second response store.
## b88 decisive focus-negative qualification — 2026-09-02

- The clean second b88 Runtime sample closes the focus A/B. Covered first-responder activation and `document.hasFocus=true` are Runtime Positive, but focus alone is **not sufficient** for official cross-platform continuation with the current programmatic full `/c/<conversation>` load.
- Evidence: authoritative Detail advanced to six tool items before focus; after focus the user directly observed multiple additional PC tool rounds from the same remote generation, while covered Web produced zero page-owned `stream_status`, `/resume`, external SSE or snapshot and Native remained on the six-tool live snapshot.
- Final materialization again required explicit Sync. Therefore neither focus nor the current generic user-socket structural frames provide reliable continuation/final convergence for this path.
- The remaining known-good differential is genuine official SPA/router conversation entry versus direct full navigation. Treat router causality as **Unverified** until a privacy-safe causal A/B identifies one exact variable. Do not jump directly to a router workaround from correlation alone.
- Existing boundaries remain: no Native protocol synthesis or guessed offsets, no polling/timers/retries/watchdogs, no duplicate Send, no WebSocket body authority, no second response store.

## b88 focus Runtime qualification — 2026-09-02

- b88 real-device Runtime proves covered first-responder activation is technically effective: manual-Sync rearm produced `nativeFirstResponder=true`, a page focus event, and direct `document.hasFocus=true`.
- The same run produced no official page-owned continuation traffic and final materialization still required a later explicit Sync. This is not yet sufficient to reject focus because the user entered at the final tool call and authoritative active Detail at `14:44:36Z` preceded focus at `14:44:37Z` by only about one second.
- Therefore focus causality remains **Inconclusive**. Do not promote SPA/router entry as causal yet and do not allocate b89. Repeat exact b88 earlier in a long remote generation.
- The visible-Web known-good sample remains valid: current official Web can acquire/live-continue cross-platform active responses under the same persistent WebKit session authority. The remaining problem is covered-page activation/entry behavior, not server capability or Repository response ownership.
- Existing prohibitions remain: no Native `stream_status`/`resume`/offset construction, polling, timers, retries/watchdogs, duplicate Send, WebSocket body authority or second response store.

## b85 Runtime / b86 continuation diagnostics qualification — 2026-09-02

- **Authoritative block path:** b85 real-device Runtime confirms explicit `同步最新消息` may project the already-approved active Detail trailing reasoning/tool timeline through the existing per-conversation Repository response owner. Repeated Sync updated one response generation (`1 -> 5 -> 7` timeline items) and final authoritative materialization reconciled it correctly.
- **Continuation qualification:** this does not establish one-Sync automatic continuation. In the supplied b85 run the covered page re-armed and loaded, but no page-owned streaming/snapshot/resume event appeared; each newer block required another explicit Sync. The remaining problem is page-owned continuation activation, not Native response ownership.
- **Diagnostic decision:** b86 may log only matching page-owned `stream_status` request/HTTP/status token and matching resume offset structure/response. It must not issue new requests, construct Native resume/offset, poll, retry, resend or create another state owner.
- **SSE research boundary:** historical exact Runtime already proves official Web can perform cross-device `/resume {conversation_id, offset}` -> HTTP200 `text/event-stream`; b86 exists only to determine whether/when the current covered page enters that official path after the new authoritative active-Detail anchor is known.

## Send MVP / b83 qualification — 2026-09-02

- **TD-029 current MVP qualification:** client-owned Send continues to require the existing real SSE stream. For cross-platform/external turns, genuine block/page-snapshot progressive reasoning/tool updates are acceptable for the current MVP; token-level external SSE parity is deferred.
- **Explicit recovery contract:** manual `同步最新消息` is a hard reliability boundary. After a successful explicit Sync, if the same conversation remains selected and `ConversationRepository` does not already own an active live response, the covered target page may be force re-armed exactly once even when the latest user ID did not change. b83 implements only this source-backed correction.
- **Deferred:** automatic remote-turn discovery/acquisition, cross-platform token-level reasoning SSE, progressive external final-token streaming, and production integration of the official iOS native realtime/WebSocket path are postponed until the broader product is completed.
- This qualification supersedes the earlier requirement that automatic prompt receipt/live acquisition block the current Send MVP. It does not revoke b80 stopped-thinking/final-materialization boundaries, b67 client-owned protected Send, b72 tested simultaneous ownership, or `ConversationRepository` response ownership.

## b82 Runtime qualification — 2026-09-02

- **TD-029 external-acquisition qualification:** exact b82 proves the current at-document-start user-socket exact-conversation `targetMatch=true` event is sufficient to trigger an automatic authoritative Sync/re-arm, but in the tested long remote turn it arrived only after authoritative Detail already contained the added user+assistant pair (8 -> 10). No earlier incoming socket frame, page-owned active-response signal, external snapshot or Repository live response was observed. Therefore this event is authorized as a completion/update trigger only, not as a request-start/live-stream trigger.
- The user's current requirement is explicit: a long cross-platform turn must show prompt request receipt and real progressive response state. Do not satisfy that requirement with synthetic text, duplicate Send or an unevidenced timer/polling loop.
- Before changing production behavior again, compare an already-open visible official Web page on the same conversation. If visible Web has an earlier live path, reproduce the exact evidenced browser behavior; if it also waits until completion, separately evidence a real-time subscription/status design before implementation. b83 remains unallocated.

## b76 qualification — 2026-09-01

- **TD-029 current external-continuation rule:** a page-owned matching `/backend-api/f/conversation/resume` is accepted only on exact HTTP200 `text/event-stream`. Current visible-Web evidence also proves official Web can receive resume HTTP404 JSON and then follow the same active response through its own already-issued `stream_status` and plural `/backend-api/conversations/{conversation}` responses. Native must not reproduce either request or cadence. b76 may observe matching page-owned responses, validate target identity, derive service messages after the latest user, and atomically project them into the sole Repository response runtime. WebSocket remains non-authoritative. Raw plural message count is not a cursor because the response is rolling/paged.
- **TD-014 presentation qualification:** b75 26/18.2/18.2 remains rejected. b76 tests 30/21/21 while preserving the 0.70 relationship and shared reasoning/final measurement/rendering behavior; visual acceptance is Runtime-only.
- b67 local protected-Send Runtime and b72 tested concurrent ownership remain accepted predecessors. b76 CI/Artifact success does not establish Runtime success.

## b75 Runtime qualification — 2026-09-01

- **TD-014 presentation qualification:** Build75 proves the numeric `26 / 18.2 / 18.2` tool/reasoning/final line-height implementation is not the accepted visual target; the latest exact screenshot rejects it as too tight. Future correction must increase the visible vertical rhythm while keeping reasoning/final measurement and rendering consistent and preserving chronological reasoning/tool semantics.
- **TD-029 external-continuation qualification:** request observation alone remains non-authoritative. Exact b75 covered-production Runtime saw three matching official-page-owned `/backend-api/f/conversation/resume` responses return HTTP404 JSON while the external response was still active. Therefore covered-production external adoption is not Runtime accepted. Do not add Native resume/offset construction, polling, retry, guessed alternate routes or WebSocket body authority. Re-probe current official page behavior in Web Rule Lab first.
- b67 local protected-Send transport and b72 exact tested cross-conversation simultaneous ownership remain accepted predecessors; b75 does not revoke them.

This file records durable, evidence-backed technical decisions and rejected routes. Detailed historical evidence remains available in Git history and `BUILD_TEST_INDEX.md`; current decisions below are the active durable contracts.

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client
- **Status**: Confirmed; qualified by TD-024/TD-025/TD-026/TD-027/TD-028/TD-029 for ChatGPT-account Send
- **Decision**: Develop a native Swift/UIKit ChatGPT client as the product shell and native read/navigation baseline. Historical hidden-WebView chat architecture is not the product source baseline. TD-024 records the earlier visible-Web security permission; TD-025 rejects b44's full-page hybrid form; TD-026 retains background resilience as a hard product requirement; TD-027 records the confirmed official resume / rejected Native duplicated parity boundary; TD-028 records the exact-device long-conversation full-Web composer viability ceiling; TD-029 is the current production Send decision and explicitly authorizes a covered official-Web **transport/challenge executor** behind Native UI while keeping `ConversationRepository` as the sole production response/conversation owner.

### TD-002 — Previous-project history is reference-only evidence
- **Status**: Confirmed
- **Decision**: Historical endpoint names/shapes/workarounds require current revalidation before becoming contracts.

### TD-003 — TrollStore IPA distribution with iOS17 primary tested ceiling and iOS14 build minimum
- **Status**: Confirmed
- **Decision**: TrollStore IPA; primary real-device evidence is iPhone/iOS17. Keep build minimum iOS14.0 until concrete need.

### TD-004 — Diagnostics/logging is application foundation
- **Status**: Confirmed
- **Decision**: Important async/auth/network/protocol/state operations use the accepted structured local diagnostics authority with bounded/redacted export.
- **Rejected**: passwords, OAuth codes, tokens, Cookie/Authorization values, raw conversation IDs, full titles/chat bodies or attachment contents.

### TD-005 — WebKit is persistent login authority; native consumption is transient
- **Status**: Confirmed; production Send execution qualified by TD-029
- **Decision**: Default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority. Native read transport may transiently copy current WebKit cookies/token into ephemeral `URLSession`; no second persistent credential store. TD-029 permits a process-resident official Web execution surface to use this same default store for page-owned protected Send/challenge execution without becoming a second auth or conversation authority.

### TD-006 — Foundation baseline is Swift/UIKit with iOS14 minimum
- **Status**: Confirmed
- **Decision**: Swift5 + UIKit/Foundation/WebKit/OSLog/CryptoKit, no third-party dependencies, deployment target iOS14.0 until concrete need.

### TD-007 — Probe actual account/session path after usable WebKit context
- **Status**: Confirmed
- **Decision**: Account verification is not gated by native browser-oriented `/auth/login`. Accepted sequencing is WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- **Rejected**: speculative automatic retry, UA spoof, Cloudflare bypass, duplicate gates/fallback endpoint.

### TD-008 — Parse accounts-check by ordered account identity
- **Status**: Confirmed
- **Decision**: Parse `account_ordering` + keyed `accounts`; choose first ordered entry not explicitly denied and use nested `account.account_id`.

### TD-009 — Auth bootstrap gate is satisfied for tested Plus/personal scope
- **Status**: Confirmed
- **Decision**: Authentication/account-context gate is satisfied for the recorded scope; this does not prove later private protocol surfaces.

### TD-010 — Current personal-account conversation list/detail read path is accepted
- **Status**: Confirmed
- **Decision**: For tested Plus/personal iPhone/iOS17 scope, accepted read path is transient WebKit-derived native auth, `GET /backend-api/conversations?offset=0&limit=28&order=updated`, then `GET /backend-api/conversation/{conversation_id}`. No extra account/browser headers were needed in accepted evidence.

### TD-011 — Official ChatGPT iOS interaction is default UI baseline
- **Status**: Confirmed; production Send qualified by TD-029
- **Decision**: Use official interaction patterns where acceptable, implemented natively where the architecture permits. TD-029 keeps the user-facing composer/history/reasoning/tool/final experience Native while allowing the official page to execute only the browser-required protected Send behind that Native surface.

### TD-012 — Ship small usable candidates before roadmap completeness
- **Status**: Confirmed
- **Decision**: Produce unique TrollStore candidates whenever a coherent milestone becomes testable; CI/Artifact never substitutes for Runtime proof.

### TD-013 — Manual sync/reload are explicit recovery actions, not automatic retry machinery
- **Status**: Confirmed / Runtime accepted for recorded recovery scope
- **Decision**: `同步最新消息`, `重载当前会话` and terminal `重新加载` operate through authoritative `ConversationRepository` and never resend/regenerate or form retry/watchdog chains. Newer same-target recovery cancels/replaces the older active request before replacement ownership proceeds; generation/freshness rejects obsolete completions.
- **Evidence**: b15/b21 recorded cancellation/rejoin behavior; PR #10 merged.
- **Phase 9 extension**: b44 proved that an immediate Sync after Web Send may expose the user message while assistant output already visible in Web is still absent from native Detail; a later Sync can expose it. This does not authorize automatic polling/timer retry because no readiness signal or stable delay was evidenced.

### TD-014 — Reasoning UI includes expandable user-visible detail and two-pulse transition haptic
- **Status**: Confirmed requirement; local production transport Runtime accepted b67; tested A/B simultaneous generation positive b72; exact b74 package verified with external-adoption/tool-rhythm/geometry-reuse Runtime pending
- **Decision**: When `ConversationRepository` receives explicitly user-visible reasoning/tool events, preserve chronological order inside one assistant turn (`reasoning -> tool -> reasoning -> tool -> ... -> final`). Tool completion updates the existing tool segment in place; later reasoning remains below the preceding tool. The main conversation should remain semantic rather than a raw engineering log: show meaningful service-authored tool-purpose titles, omit fallback generic `工具调用` rows from the main inline surface without destroying the ordered tool list, and never synthesize/merge titles by guess. Visible reasoning prose uses ordinary body-scale primary presentation while tool rows/summary remain secondary with official-like vertical rhythm. During a live generation the first visible reasoning/tool timeline auto-expands once; exact `reasoning_ended` auto-collapses it once; subsequent manual disclosure state remains user-owned. Historical completed reasoning defaults collapsed. Never expose hidden chain-of-thought; `assistant:thoughts` / `inline_cot_expandable_content` remain non-presentational.

### TD-015 — Production detail diagnostics use privacy-safe hashed identity + list position
- **Status**: Confirmed
- **Decision**: Use short irreversible SHA-256-derived conversation marker + 1-based list position for correlation; never raw ID/title/body.

### TD-016 — Background completion uses public baseline then isolated TrollStore experiment
- **Status**: Confirmed plan; response-owner ordering qualified by TD-026/TD-027/TD-028/TD-029
- **Decision**: For Repository-owned response lifecycles, first use normal iOS background-task time + local completion notification; any TrollStore true-background experiment remains isolated. TD-029 establishes the intended production response owner: covered official Web may execute protected Send, but background completion state belongs to the Repository response lifecycle, not Web DOM/UI state.

### TD-017 — Public default-WebKit data-store warm-up is accepted for tested cold-start auth hydration
- **Status**: Confirmed; TD-029 adds one explicit production-use exception
- **Decision**: Before first native list/account probe, initialize the existing default persistent `WKWebsiteDataStore` using public APIs. Do not add a second persistent auth store. TD-029 additionally permits one process-resident official Web execution surface using that same store for protected Send/challenge execution; this does not create another persistent credential authority.

### TD-018 — Compact read-mode startup uses native primary/list root and one navigation owner
- **Status**: Confirmed for tested iPhone/iOS17 scope
- **Decision**: With no selected conversation, compact startup uses `.primary` conversation list as the useful root. `UISplitViewController`/native navigation remains the native shell navigation owner.

### TD-019 — Multi-conversation data remains one account-scoped repository authority
- **Status**: Confirmed / merged Stable for recorded read-state scope; Frozen No
- **Decision**: One `ConversationRepository` owns native production conversation state scoped by verified account context and keyed per authoritative conversation identity. Foreground selection is presentation only; selecting B does not delete A or cancel valid hidden A work. Do not retain raw graph payloads or UIKit hierarchies as cache. No arbitrary normal LRU capacity; memory-warning trimming remains evidence-backed policy. Covered Web Send execution under TD-029 is not another repository.

### TD-020 — Per-conversation scroll presentation is semantic anchor or follow-tail, not one raw offset
- **Status**: Historical-reading anchor Runtime accepted; native active-response follow-tail pending production response-owner integration
- **Decision**: Each native conversation owns lightweight scroll presentation semantics independently of conversation data. Historical reading preserves an authoritative message anchor plus display position/relative offset where practical. Follow-tail must consume Repository-owned active-response state; do not derive it from Web DOM observation.

### TD-021 — Conversation-list cache may provisionally present last verified titles before current verification, but never authorize account-bound operations
- **Status**: Confirmed / merged Stable for recorded cache-core scope; Frozen No
- **Decision**: `ConversationListCacheStore` is storage only behind `ConversationRepository`. Automatic cold start may provisionally publish cached titles using a privacy-safe last-verified scope namespace hint, but this never establishes verified account/transport/Detail/send authority. Current 60-second rapid-relaunch window, offline retained list behavior, manual refresh bypass and first-page `28 + 1 -> 29` preservation are accepted.
- **Phase 8 extension**: authoritative `total=29` caps stale excess cached rows (`30 -> 29`, repeated `29/29`) without creating a second list owner; right-top refresh must not create persistent blank top inset.

### TD-022 — Long-conversation presentation uses deterministic derived geometry; round navigation consumes it
- **Status**: Confirmed / Runtime accepted / merged Stable on exact b38 recorded iPhone/iOS17 scope; Frozen No
- **Date**: 2026-08-29
- **Problem evidence**: Exact b36 retained severe long-conversation stutter in quick navigation and ordinary right-side scroll-indicator dragging. 47 direct-position samples had median ~187ms, P90 ~780ms and max ~3952ms. One 161-visible-message table initially reported ~13.8k points of bottom geometry and later ~154.6k points as giant estimated/self-sized message rows became realized.
- **Decision**: Keep authoritative native messages solely in `ConversationRepository`; derive an ephemeral `ConversationMessagePresentationProjection` that splits very long plain-text messages into bounded display chunks, computes deterministic row heights/prefix offsets for the current layout width, maps authoritative messages to first display rows, and drives `ConversationMessageCell` with deterministic manual frame layout. This projection is presentation-only and is rebuilt when authoritative messages/layout width require it; it is not a persistent second message/row-height store.
- **Copy/semantics boundary**: Copy reads the complete authoritative message; round count/semantic targets still come from one `ConversationRoundProjection`; each visible authoritative user message starts a round. Display chunking never creates semantic turns.
- **Navigation decision**: Stable b38 uses the already-derived O(1) target offset and one cancellable `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)` from the current viewport to the target. Short/long distances use one method. Rapid taps retarget from current visual position; real drag immediately retakes ownership. No pre-jump teleport, `scrollToRow` geometry discovery or end correction snap is part of the accepted path.
- **Runtime evidence**: Exact b37 user feedback **“这次确实不卡了”** accepted the deterministic geometry/performance direction. Exact b38 then restored genuine continuous full-distance animation while preserving that geometry; user feedback **“没问题了”** accepted the combined result.
- **Exact accepted identity**: b38 tested product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Runtime Artifact `9708425762`, IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- **Merge evidence**: PR #27 final head `57b3efe576dbf187171439a68d6d2dfe2fba0ebc`; tested product->final head delta was docs-only; PR merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- **Rejected without new evidence**: reverting to one giant whole-message self-sizing UILabel with unstable estimated geometry; persistent cross-detail row-height cache; pre-jump direct teleport; `scrollToRow` as target-geometry discovery; final correction snap; debounce/timer/watchdog/retry; alternate semantic index or second repository.

### TD-023 — Current ChatGPT-account pure-native Send is blocked by required browser anti-abuse challenges
- **Status**: Confirmed by exact b42 protocol Runtime for recorded Plus/personal iPhone/iOS17 scope; qualified by TD-029
- **Date**: 2026-08-29
- **Evidence**: Exact b42 `DEV-send-stream-0.1.0-b42`, product source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, Artifact `9709824510`, used a default `primary_assistant` new conversation. Sentinel prepare returned `proofOfWorkRequired=true`, `turnstileRequired=true`, and `soRequired=true`; Sentinel finalize submitted non-empty PoW and Turnstile values before successful `POST /backend-api/f/conversation` SSE Send.
- **Decision**: Under pure-native/transient-WebKit-auth request construction, do not implement ChatGPT-account Send because the successful path requires browser-generated anti-abuse challenge output that the native auth boundary does not legitimately own. TD-029 does not reverse that evidence; it keeps challenge execution inside the official page.
- **Rejected**: PoW/Turnstile/Sentinel solver or bypass, browser-fingerprint emulation/replay, captured proof/token replay, guessed alternate/fallback endpoints, or presenting CI/Artifact/protocol-probe success as pure-native Send success.

### TD-024 — Earlier user-visible official-Web Send permission
- **Status**: Historical security permission; production visibility requirement superseded by TD-029
- **Date**: 2026-08-29
- **User decision**: After TD-023/b42, the user initially selected a user-visible official ChatGPT Web Send surface while retaining Native shell/read/navigation.
- **Evidence**: b43/b44 established that the official page can perform protected Send with the default WebKit store, but the full-page hybrid interaction duplicated conversation rendering and immediate Native reconciliation could lag the Web answer.
- **b47 qualification**: a long-answer mobile-Web conversation could make the composer unusable before Send on the primary device.
- **Authority boundary retained**: `ConversationRepository` remains native conversation authority; `AuthSessionStore` remains auth authority; default WebKit store remains persistent auth-secret authority.
- **Supersession**: TD-029 explicitly supersedes only TD-024's requirement that the official Send surface remain user-visible and its rejection of a covered official-page executor. The challenge-bypass prohibition and state-owner boundaries remain in force.
- **Identity incident**: Artifact `9710515489` from Run `33238065644` carried b42 identity over newer hybrid code and is permanently rejected; legitimate b42 remains Artifact `9709824510`.

### TD-025 — b44 full-page existing-account hybrid Send is rejected
- **Status**: Confirmed by exact b44 Runtime; full-page form remains rejected; covered transport executor later authorized by TD-029
- **Date**: 2026-08-29
- **Exact evidence**: b44 `DEV-send-stream-0.1.0-b44`, source `f1503cf7121512a84e5c55a3642181c17324d791`, Artifact `9712583513`, IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`; detailed Runtime record `docs/project/runtime-evidence/DEV-send-stream-b44-runtime.md`.
- **Runtime conclusion**: Web Send can succeed and `/c/<id>` mapping can be correct while immediate Native Detail reconciliation still lacks assistant output already visible in Web. Later Sync can expose it. No stable completion/readiness delay or signal was established. A/B switching also causes Web to reload/render the conversation separately from already-loaded Native Detail.
- **Decision retained**: do not ship the b44 `Native -> full Web conversation -> return + Sync` form and do not patch it with arbitrary delay, polling/retry or repeated Sync.
- **Supersession**: the earlier rejection of any Native-composer -> covered official-Web composer execution is superseded by TD-029 because b48-b65 subsequently produced extensive exact Runtime evidence for that narrower transport shape. Full-Web conversation rendering remains rejected.
- **Candidate rule**: emitted b39-b47 identities are permanently reserved.

### TD-026 — Background/lock resilience remains a hard product requirement, but implementation follows the Repository response owner
- **Status**: Confirmed product requirement; exact b45 gives positive short-background evidence; full feasibility still Unverified
- **Date**: 2026-08-29
- **User decision**: During long reasoning or streamed reasoning/final output, backgrounding/locking the app for a while must not routinely lead to timeout/disconnect that requires manual refresh on return.
- **Public iOS boundary**: Apple's public background-task APIs provide finite extra runtime and do not guarantee long-running foreground-equivalent execution. `beginBackgroundTask` may be used as a short-duration baseline only; do not encode fixed-duration guarantees, keepalive timers or unrelated background-mode abuse.
- **Exact b45 evidence**: on iPhone/iOS17.0, one clean default-primary new-chat response remained on the same original `/backend-api/f/conversation` fetch while the app was backgrounded approximately 35s, 34s and 126s during the active response (~195s cumulative). On final foreground return the same original stream delivered `message_stream_complete` and `[DONE]`; no manual refresh/resend or secondary reconnect transport was observed.
- **Evidence boundary**: this proves the tested path can survive or buffer across those ordinary background/lock intervals. It does not prove continuous background event delivery, 5/15-minute survival, WebContent termination recovery, network-loss recovery or battery/thermal cost.
- **Ordering decision**: TD-029 establishes the planned production response owner: the Web surface may remain necessary to execute the protected browser request, but active-response/background state belongs to `ConversationRepository`. Background work must preserve/recover that one response lifecycle without duplicate Send.
- **Rejected**: manual-refresh-as-normal-use, DOM-state authority, timer/poll/retry chains, permanent idle process immortality, or claiming main-app survival equals WebKit-stream survival.
- **Durable plan**: `docs/project/HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`.

### TD-027 — Official no-resend resume is Runtime Confirmed; Native duplicated Cookie+Bearer-only parity remains rejected
- **Status**: Confirmed through exact b45-b47 Runtime; Native first/exclusive continuation remains Unverified
- **Date**: 2026-08-29
- **Exact evidence**: b45 source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` / Artifact `9713774868`; b46 source `4ab9be3ef2809204e88fcb0d44884e35b43726b1` / Artifact `9715903443`; b47 source `21028bbff7982abeb42f130c56fcb21e6ef44d7a` / Artifact `9716878034`. Detailed records: `DEV-send-stream-b45-runtime.md`, `DEV-send-stream-b46-runtime.md`, `DEV-send-stream-b47-runtime.md`.
- **Official transport conclusion**: current official Web uses `POST /backend-api/f/conversation/resume` with body `{conversation_id: string, offset: number}` as a post-Send continuation read. After real transport interruption it can return HTTP200 `text/event-stream`, repeatedly continue the same already-started response without another Send and reach terminal events.
- **b46 Native parity**: after official offset 18 resume succeeded, one Native same-body Cookie+Bearer-only duplicate returned HTTP404 JSON; later official offset 54 succeeded.
- **b47 Native parity**: after official offset 23 resume succeeded, one Native same-body Cookie+Bearer-only duplicate again returned HTTP404 JSON (~707ms, 116 bytes, 0 SSE frames); later official offset 74 succeeded. Rejection shape was `{"detail":{"code":"string","message":"string"}}`.
- **Request-context evidence**: successful official resume exposed header names `accept, authorization, content-type, oai-client-build-number, oai-client-version, oai-device-id, oai-echo-logs, oai-language, oai-session-id, x-conduit-token, x-oai-is-client-observation, x-oai-is-pending-updates, x-oai-turn-trace-id, x-openai-target-path, x-openai-target-route`. Native explicitly set only `accept, content-type`, plus the established transient bearer injection and WebKit-derived ephemeral cookies.
- **Decision**: this structural difference does not authorize copying browser header values. Missing non-challenge request context vs second-consumer/cursor ownership remains unresolved. Native first/exclusive resume is Unknown / Unverified.
- **Rejected**: guessing required browser headers, copying `x-conduit-token`/OAI browser values without evidence, retry loops, duplicate Send, or treating HTTP404 as proof that Native continuation is universally impossible.

### TD-028 — Full mobile-Web conversation is not an accepted production Send dependency after exact long-conversation composer failure
- **Status**: Confirmed product architecture gate; narrowed by TD-029
- **Date**: 2026-08-29
- **Evidence**: while preparing exact b47 testing, the user attempted to use an older conversation containing only about three rounds but long answers. On the primary iPhone/iOS17 environment, repeatedly trying to bring up/use the mobile-Web composer froze the page badly enough that the conversation could not be used for the test; the user switched to a new conversation. The exported b47 diagnostics cover the replacement run and therefore do not establish the freeze's internal owner.
- **Decision retained**: do not render/use the full mobile-Web conversation as the daily-chat product dependency. The Native product must own history/presentation.
- **Supersession**: the old shortcut rejection of a covered official Web Send executor is superseded by TD-029 after b48-b65 proved a narrower page-owned Send/SSE path under Native presentation. TD-029 does not require full Web history rendering and therefore does not reverse the b47 long-conversation failure evidence.
- **Evidence boundary**: b43's earlier smooth visible-Web result remains valid only for its shorter tested sequence; root cause of the long full-page freeze remains Unknown / Unverified.

### TD-029 — Production Send uses Native UI + covered official-Web protected-Send executor + Repository response ownership
- **Status**: Confirmed product architecture decision; existing-conversation local protected-Send transport Runtime accepted b67; external page-owned matching-resume adoption exact b74 Code/CI/Artifact/package verified, Runtime pending
- **Date**: 2026-08-31
- **User decision**: after b65 focused Runtime passed and the remaining blocker was the earlier visibility prohibition, the user explicitly selected Option B: authorize the already-tested Native composer -> covered official Web page-owned protected Send mechanism for production and prioritize finishing `DEV-send-stream` quickly.
- **Evidence basis**: b42 proves pure-native ChatGPT-account Send is blocked by browser challenge output. b48-b65 then prove on the primary iPhone/iOS17 scope that a Native-controlled composer can drive the official page's verified composer, observe one real protected `/backend-api/f/conversation` HTTP200 SSE response, classify complete-looking reasoning/final text, preserve `title_generation` continuation, honor exact `reasoning_ended`, present event-driven thinking state, exact-parent tool lifecycle and the bounded GitHub detail mapping. b65 closes the tested tool-detail formatting defect.
- **Decision**: the production user-facing composer/history/reasoning/tool/final UI is Native. One process-resident official ChatGPT Web execution surface may be covered/not user-visible while using `WKWebsiteDataStore.default()` to let the official page execute the browser challenge and exactly one protected Send for each user Send action. The same response stream is consumed into a Repository-owned response lifecycle.
- **State ownership**: `ConversationRepository` remains the sole production conversation/resident/response authority. Covered Web owns no durable message/conversation/response state and no production UI semantics. `AuthSessionStore` remains auth/account authority; default WebKit store remains persistent auth-secret authority.
- **Security boundary retained**: no challenge solver/bypass, no copying/replaying PoW/Turnstile/Sentinel/conduit values, no second persistent credential store, no duplicate Send to obtain a stream, no arbitrary fallback selectors/retry/timer/watchdog chain.
- **Product boundary retained**: b44 full-page Web chat remains rejected; TD-028 full-Web long-conversation dependency remains rejected; continuous DOM message mirroring remains rejected. Only the evidenced composer/protected-Send/SSE executor is promoted.
- **Maintenance decision**: add and retain an in-app development **Web Rule Lab** using the same default WebKit store. It visibly opens ChatGPT Web, accepts user-pasted temporary JS probes, displays/copies/shares the temporary result, and never persists probe code/result bodies in diagnostics or app storage. Future Web changes should follow `reproduce -> Lab probe -> evidence -> one minimal adapter update -> one coherent product build`, not repeated speculative IPA builds.
- **Durable adapter authority**: `docs/project/WEB_SEND_ADAPTER.md` owns current evidenced selectors/SSE/reasoning/tool rules and the Web Rule Lab update playbook. `SEND_STREAM_PREFLIGHT.md` owns Repository/new-chat/Stop/follow-tail state invariants.
- **Implementation order**: Web Rule Lab foundation -> existing-conversation Repository-owned production Send/stream -> new-chat identity handoff -> exact Stop -> A/B/follow-tail -> Sync/Reload/b38 regression -> final daily-chat Runtime/merge decision.
- **Evidence ladder**: architecture decision confirmed; b67 production existing-conversation transport Runtime accepted; exact b70 Code/scope/Push+PR CI/Artifact/package verified; b70 real-device daily-chat parity/auth-lifecycle Runtime remains pending.
- **b74 external continuation extension**: 2026-09-01 Web Rule Lab Runtime evidence shows that when another platform already owns an active response and official Web enters that conversation, official Web may request `stream_status` and then issue its own `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` receiving HTTP200 SSE. Production Native may observe/clone/parse only that page-owned resume when its `conversation_id` exactly matches the executor target, then create/adopt one response generation in the existing `ConversationRepository` runtime. Native must not construct the resume request, select/derive `offset`, poll `stream_status`, replay browser headers, treat the user WebSocket as response-body authority, or issue a second Send. Exact b74 package implements this boundary; real-device adoption behavior remains pending.

### TD-030 — Transient Native read HTTP403 is not persistent logout by itself; stale copied transport is discarded without automatic replay
- **Status**: Confirmed state-lifecycle decision; exact b70 Runtime pending
- **Date**: 2026-08-31
- **Evidence**: exact b69 diagnostics/source correlation showed the same browser-authenticated account could pass session/accounts, later receive Native list/detail or account-probe HTTP403, and later succeed again. b69 also cached one copied `AuthTransientSession` indefinitely for an unchanged account scope. Therefore one 403 does not prove logout/account replacement, and retaining the failed copied transport can make Native reads sticky.
- **Decision**: exact HTTP403 at session/accounts probe stages is a temporary probe failure that preserves the last verified account identity while returning no fresh transient transport from that failed probe. Exact 401 retains unavailable/not-authenticated semantics.
- **Repository behavior**: current list/detail 401/403 invalidates/discards the copied transient transport once; that operation still fails visibly. A later explicit/normal read follows the existing account-context probe and materializes current WebKit credentials. The framework does not replay the failed operation.
- **User-navigation behavior**: returning from a user-opened login screen may issue one explicit list refresh; this is a new navigation operation, not hidden retry.
- **Ownership/security retained**: `AuthSessionStore` remains sole account authority; `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority; `ConversationRepository` remains sole read/response lifecycle authority. No second credential store, retry loop, polling, timer, watchdog, compatibility shim or challenge copying is authorized.
- **Evidence boundary**: b70 Code/CI/Artifact/package success proves only implementation/package identity. Recovery from a real transient 403 remains a real-device Runtime gate.

### TD-023 — Explicit cross-platform Sync may adopt approved trailing Detail timeline into the existing response owner
- **Status**: Confirmed architecture from b84 Runtime; b85 product Runtime pending
- **Date**: 2026-09-02
- **Evidence**: Exact b84 real-device samples on the previously problematic conversation showed authoritative Detail trailing presentational timeline growth `1 -> 4 -> 5 -> 6` while visible assistant count stayed fixed and covered Web never acquired a live response. Parser sources were already-authorized thinking preambles/reasoning recap/tools; raw `thoughts` and `inline_cot_expandable_content` remained skipped.
- **Decision**: Explicit manual `同步最新消息` may project that already-approved trailing Detail timeline through the existing per-conversation `ConversationRepository` response runtime. If page-owned continuation later attaches it updates the same external response generation. Another explicit Sync may refresh a newer block while the external response remains active.
- **Rejected**: covered-page re-arm as the sole deterministic manual acquisition mechanism; polling/timer/retry/watchdog loops; duplicate Send/resend; WebSocket body authority; raw hidden-thought presentation.

## Rule

Do not write speculation here as fact. Historical plans, CI and Artifacts are not Runtime proof. Stable does not mean Frozen. A newer explicit TD may supersede only the clauses it names; all unaffected evidence and boundaries remain active.

## 2026-09-03 — b92/b93 page-owned continuation loop interruption

Exact b92 single-executor Runtime proves that a background lifecycle transition can stop the official page-owned `stream_status`/snapshot loop even without another executor. Exact b93 proves successful first-responder/document-focus reacquisition does not necessarily restart a stopped loop. The next isolated candidate is foreground official-page rebootstrap without Native Detail Sync; selection rebootstrap remains separate. Stable/Frozen Send remains No.
