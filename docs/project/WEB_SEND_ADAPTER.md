# Web Send Adapter / Rule Update Playbook

## DEV-send-stream b107 accepted protected-Send SSE clean EOF — package-ready override 2026-09-05

- Exact b106 Runtime retained the correct first top-level protected-Send SSE `conversation_id` handoff but showed that a successfully accepted HTTP200 SSE can end without the bridge observing exact `[DONE]` while the authoritative server conversation is already complete.
- b107 keeps the Web adapter grammar and New Chat identity logic unchanged. Native Root handles the exact post-acceptance `stream_ended_without_done` transport result by preserving the same Repository generation and reattaching one covered observer; it never performs a second protected Send.
- Product `113fa19d7264b953949770d2e44cb500ded2da6b` / package `4bd3501a3092dfe7aad7ea836ba0cb8e42b0d65f`; staging `33960451799/101291316464`, Push `33960627676/101291785599`, PR `33960629168/101291789461` passed; canonical Artifact `9967821935`, ZIP `d2036ed0372b16c7690c9d3b324d680db6a522fd5ace26d27afa8733a95a9585`, IPA `7195d89cb9837efc3386c5dd7e030e7f11f10233689416e59c86d1ae4cf055cd` verified.
- Human Runtime pending. No new Stop behavior is authorized; exact Stop route/target/ack evidence remains required.


## DEV-send-stream b105 authoritative new-chat first Send — package-ready override 2026-09-05

- Historical b62 Runtime is the identity evidence: an official root/new-chat page transitioned to an existing-conversation route before the first protected `/backend-api/f/conversation` fetch and then returned HTTP200 `text/event-stream`. b105 consumes that official route identity; Native does not invent one.
- Exact product `6ef4e874d7c2c5f144ab7e784f7a81755d1b2f59`; canonical package source `93ab92a9a4a7b8a020ac209f6a82088dc77acbce`; corrected staging `33923512745/101186860450`, Push `33923732331/101187538891`, PR `33923735651/101187548902` all passed. Canonical Artifact `9956018294`, ZIP `ba53bc8e50e1b89056565e3a557e196ef6b9c5db76e3b40dd28a0536e81d6921`, IPA `d162a7132ff830d3a2f6eb85a2b4a5b4ebc2d9f84531b01418912c99109e5095`; Build105/Candidate b105/source `93ab92a9a4a7`/Release/iOS14+/arm64 independently verified.
- New-chat bridge rule: when `submit(text, newConversation=true)` reaches the protected fetch interception, `currentConversationID()` must already resolve from the official route. If absent, clear the local submit marker, emit only symbolic `new_conversation_identity_missing`, throw before `originalFetch`, and never create an untracked protected turn.
- When present, emit `send_observed` with that official conversation ID before forwarding the one real protected fetch. Native `.conversationCreated(realID)` re-keys the same executor and starts one Repository generation; normal protected-Send SSE filtering and b103/b104 post-acceptance hard-Web recovery remain unchanged.
- Do not infer new-chat identity from title text, DOM message text, list position, generated UUID, guessed route, WebSocket body, elapsed time or a second request. No retry/poll/watchdog/resend/challenge replay.
- Human Runtime pending; Stop is outside this override and remains evidence-gated.

## DEV-send-stream b93 external reselection focus A/B — 2026-09-03

- Exact b92 Runtime is Partial: covered external continuation works and client-owned protected Send/SSE natural terminal reconciliation works, but when an external live executor overlaps a second client-owned Send, the first stream can stop advancing and does not recover merely by reselection; explicit Sync later materialized the already-completed assistant.
- Exact b93 tests one evidence-backed variable only: when reselecting an already-active external response, reuse the existing covered executor and restore WKWebView first-responder/document focus without reload or Sync.
- b93 identity: allocation `b86c1a3ca94b215204b0cfb135fa0cd8b3603619`, product `556bd8886061f4126d11e4ac44f4e24ed580500c`, package source `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0`, Push `33755063112/100647405265`, PR `33755067202/100647418537`, Artifact `9893141097`, IPA SHA `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d`.
- b93 package inspection: `0.1.0 (93)`, Candidate `DEV-send-stream-0.1.0-b93`, source `2d2cde58a7fb`, iOS14+, `[1,2]`, iphoneos, arm64. Human Runtime pending; Stable/Frozen Send No.
- Preserved boundary: official page owns continuation transport, Repository owns Native content. No polling/retry/watchdog/timer, Native status/resume synthesis, guessed offset, duplicate Send, WebSocket-body authority, or second response store.
- On external-live reselection b93 calls only `becomeFirstResponder()` plus `document.hasFocus()` diagnostics on the existing executor. It does not reload the page or initiate a Native continuation request.

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

## b89 covered interactivity A/B package qualification — 2026-09-03

Fresh-root visible-Web evidence now proves that official Web can canonicalize an unscoped `/c/{conversation}` navigation to the exact scoped `/g/{scope}/c/{conversation}` route and start genuine page-owned continuation even when transient activation at navigation is false. Therefore project/GPT scope recovery and transient activation alone do not explain the b88 covered-page failure.

b89 changes only covered `WKWebView.isUserInteractionEnabled` from false to true and automatically records privacy-safe `navigator.userActivation` availability / `isActive` / `hasBeenActive` on the existing page-activation diagnostic path. b88 one-shot first-responder focus after explicit Sync rearm remains unchanged. No route construction, page-owned status/resume/snapshot observation, Send, Repository ownership, cadence or fallback behavior changes.

Exact b89 package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676` passed guarded Simulator plus Push/PR CI; canonical Push Artifact `9881665748` and IPA `sha256:c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55` are package-verified. Runtime is Pending. A clean test must keep the remote generation active after covered load/focus/interactivity and then determine whether official page-owned `stream_status` / `/resume` / snapshots appear. A negative clean run rejects interactivity as sufficient and returns the evidence target to genuine official SPA/router conversation-entry state.
## b88 decisive focus-negative continuation qualification — 2026-09-02

The second exact b88 real-device sample resolves the earlier near-terminal ambiguity. Manual-Sync rearm successfully made the covered WKWebView first responder and direct `document.hasFocus()` returned true. The same remote generation then visibly continued through multiple additional tool rounds on PC, but the covered page issued no matching `stream_status`, `/resume`, external SSE or page-owned snapshot and ChatGPTClient remained on the six-tool authoritative Detail snapshot.

Therefore **focus is rejected as a sufficient activation condition** for the current covered executor's direct full conversation navigation. This does not establish that focus is irrelevant to the known-good visible Web path; it only removes focus-alone as the missing variable.

The next maintenance target is the remaining differential: a genuine user-driven official SPA/router conversation-entry transition versus programmatic full `/c/<conversation>` load. Do not implement a router workaround until a privacy-safe experiment identifies the exact official transition behavior. The existing prohibitions on Native status/resume synthesis, offset guessing, polling, timers, retries/watchdogs, duplicate Send, WebSocket-body authority and second response stores remain in force.

## b88 focus activation Runtime qualification — 2026-09-02

A known-good visible Web Rule Lab sample on the same `WKWebsiteDataStore.default()` authority immediately acquired/live-continued a newly active cross-platform response and showed the active Stop control while `document.hasFocus=true`. Its coarse `route=other` result confirms route shape is diagnostic-only.

Exact b88 then changed only first-responder activation after manual-Sync rearm. Real-device Runtime produced `nativeFirstResponder=true` and direct `document.hasFocus=true`, proving the covered page can obtain focus without enabling Web interaction or changing the programmatic target load.

No page-owned `stream_status`, `/resume`, external streaming or snapshot followed in that run; final authoritative materialization required another explicit Sync. Do **not** yet conclude that focus is insufficient: the target was already at its final tool call, and the last authoritative proof that the generation was active preceded focus by only ~1 second. Repeat exact b88 earlier in a long generation before moving to SPA/router entry work.

This evidence still does not authorize Native protocol synthesis, guessed offsets, polling, timers, retries/watchdogs, duplicate Send, WebSocket-body authority or a second response store.

## b82 completion-time acquisition qualification — 2026-09-02

Exact b82 Runtime changes the external-discovery interpretation. The covered user WebSocket was injected/observed from document start and produced no incoming frame during the long remote generation interval; the first exact-conversation `targetMatch=true` frame arrived only when an automatic authoritative Detail Sync already returned two added visible messages (remote user + assistant) and the user reports the answer was complete. The subsequent one-time page re-arm produced no `externalStreamingObserved` or external snapshot.

**Current rule:** the tested generic user-socket exact-conversation notification may trigger one bounded authoritative completion/update Sync, but it is not an evidenced request-start/live-stream signal. The existing page-owned `stream_status` / plural-read machinery remains content authority only when the official page actually enters that path. Do not increase observation frequency when no event exists, do not parse the generic socket as message-body authority, and do not introduce hidden polling/timers merely to mask this timing gap.

Next maintenance gate: with visible official Web already open on the same target conversation before a remote Send, determine whether the page itself begins live acquisition before completion. A positive result must identify the concrete browser/network behavior to reproduce; a negative result means a separate real-time subscription or deliberately authorized bounded status-monitor design must be evidenced before product code.

_Last established: 2026-09-01 through b67 accepted local transport, b72 tested concurrent ownership, b75 visible-Web continuation probes, and exact b76 Code/CI/Artifact/package verification; b76 Runtime remains pending._


## Current b76 external-response read rule — 2026-09-01

Fresh visible official-Web evidence supersedes the older same-day assumption that cross-device adoption must receive a successful `/backend-api/f/conversation/resume` SSE. Current official-page behavior can be:

`page-owned stream_status=IS_STREAMING -> page-owned /resume -> HTTP404 JSON -> repeated page-owned stream_status + plural /backend-api/conversations/{conversation} JSON -> stream_status=COMPLETE -> final plural snapshot`

The plural response is a rolling/paged top-level `messages[]` window. Its raw count is not monotonic and is not a response cursor. Entries are the same service-message family already evidenced by the native parser. While streaming, the active segment can contain visible thinking preambles, assistant/non-all tool invocations, exact-parent tool results, hidden thoughts/inline COT, reasoning recap/end and an assistant final message with `status=in_progress`; after `COMPLETE`, the final assistant is `finished_successfully`, `end_turn=true` with completed body.

**Current b76 production rule:** observe only page-owned matching requests/responses already issued by official Web; never construct or schedule Native status/plural reads and never reproduce cadence. Validate returned conversation identity, find the latest user service message, project only following entries atomically into the existing `ConversationRepository` live-response runtime, preserve existing reasoning/tool/final semantics, and terminal/reconcile once after page-owned COMPLETE plus the following plural snapshot. Historical page-owned `/resume` remains supported only when that exact response is HTTP200 `text/event-stream`. User-level WebSocket remains structural-only and is not a response-body source.

Exact b76 has passed guarded scope/Simulator, Push+PR CI, Artifact and package identity checks. Those checks do not prove Runtime behavior; real-device adoption remains the Human Gate.
## Purpose

This document is the durable maintenance contract for the ChatGPT-account protected-Send bridge used by the native iOS client.

The product remains a Native Swift/UIKit chat client. The official ChatGPT Web page is used only where the browser security boundary is required to perform the official protected Send/challenge flow. The goal is to keep that Web dependency small, explicit, replaceable from fresh evidence, and easy to re-probe when ChatGPT Web changes.

This file is the first document to read when any of these regress:

- Native Send button no longer causes a real protected Send;
- the official composer selector/submit behavior changes;
- `/backend-api/f/conversation` interception stops matching;
- SSE framing/event grammar changes;
- reasoning/final/tool state stops classifying correctly;
- official Web adds/removes model/mode/composer controls that the adapter must drive;
- a future ChatGPT Web deployment breaks the current covered-Web executor.

Current source/runtime evidence and the latest exact real-device reproduction outrank this document if the service changes.

## Production authority split

### Native owns

`ConversationRepository` is the sole production authority for:

- conversation residents;
- authoritative visible message projection;
- active response lifecycle;
- pending->authoritative new-chat handoff when required;
- reasoning/final/tool presentation state derived from accepted service events;
- response terminal state;
- response-scoped Stop once evidenced;
- active-response protection and future follow-tail/background integration.

`ConversationDetailViewController` owns viewport/presentation intent only.

`AuthSessionStore` remains the sole native auth/account-context authority.

### Web owns only protected browser execution

One process-resident official ChatGPT Web execution surface may be covered/not user-visible in normal production chat while it:

- uses the existing default persistent `WKWebsiteDataStore`;
- lets the official page create/refresh browser-required challenge/session context;
- receives text from the Native composer through the currently evidenced composer path;
- invokes the page's own normal Send behavior;
- performs exactly one official protected Send for the user's one Send action.

It is a **transport/challenge executor**, not a conversation repository, message cache, response owner or UI authority.

The adapter must never synthesize, solve, persist, copy for replay, or expose Sentinel/PoW/Turnstile/conduit/challenge values.

## Current accepted Send entry rule

Accepted from b61/b62 Runtime:

1. composer authority is `#prompt-textarea`, or
2. explicit `[contenteditable="true"][role="textbox"]` when that is the evidenced official composer.

Rejected:

- generic `textarea:not([disabled])`;
- guessing from placeholder text alone;
- delayed retry/timer/watchdog loops searching for another composer;
- alternate hidden fallback selectors added without a fresh real reproduction.

A Native Send is not accepted merely because JavaScript returns `submitted`. The adapter must observe the real protected-Send lifecycle (`sendObserved` plus the actual response stream/HTTP evidence).

## Current accepted protected Send / stream boundary

Current tested route:

- official page owns the browser request;
- protected Send observed on `POST /backend-api/f/conversation`;
- successful tested responses are HTTP200 `text/event-stream`;
- Native/Repository must consume the **same response**; do not issue a second Send merely to obtain streaming data.

Pure-native/transient-auth protected Send remains blocked by b42 browser-challenge evidence.

Official no-resend `/backend-api/f/conversation/resume` remains a separate b45-b47 continuation/recovery evidence surface. It is not a substitute for the first protected Send and its native parity remains unverified.

### Cross-device active-response continuation — 2026-09-01 Runtime evidence

A current Web Rule Lab capture now confirms the official page behavior when another platform has already started a response and the user enters the same conversation in official Web:

- the page opens a user-level `wss://ws.chatgpt.com/...` socket and receives short string frames; this capture does **not** establish that socket as the reasoning/final body transport;
- on entering the target conversation, the page issues the normal conversation/detail bootstrap plus `GET /backend-api/conversation/{conversation_id}/stream_status` -> HTTP200 JSON;
- when the response is still active, the page itself issues `POST /backend-api/f/conversation/resume`;
- the observed request JSON shape is exactly `{ conversation_id, offset }`;
- the resume response is HTTP200 `text/event-stream`;
- no second `/backend-api/f/conversation` Send is required for this adoption path.

**Current production rule:** external active-response adoption may observe and parse the official page's own `/backend-api/f/conversation/resume` SSE for the currently targeted conversation. Native code must not construct the resume request, choose/synthesize `offset`, replay browser/session headers, or poll `stream_status`. The page remains transport authority; `ConversationRepository` becomes/retains the sole Native response lifecycle owner once that page-owned resume is observed. Only a resume whose request `conversation_id` matches the executor's authoritative target may be adopted. The user-level WebSocket remains structural evidence only and is not authorized as a Native response-body source from this capture.

### b75 covered-production qualification — 2026-09-01

The visible Web Rule Lab HTTP200-SSE capture above remains historical evidence for that exact visible-Web run, but exact Build75 production Runtime rejects treating it as proof that the covered executor will currently receive the same stream. In three separate covered-production attempts while the external response was still active, the page itself issued a matching `/backend-api/f/conversation/resume`, but the response was HTTP404 `application/json`; Native therefore had no validated SSE to adopt and correctly created no external live-response generation.

Current rule until re-probed: keep the b75 validation gate (request observation alone is never response authority), but **do not claim covered-production external adoption is working** and do not add Native-constructed resume/offset, polling, retry, delayed resend, WebSocket-body parsing or guessed alternate routes. Use Web Rule Lab to capture current page-owned `stream_status` status/order, all matching resume attempts/statuses, and whether a later page-owned HTTP/SSE transport follows an initial 404. Only that fresh evidence may define the next production continuation rule.

## Current accepted SSE/text grammar

The adapter/parser may rely only on shapes already backed by exact Runtime evidence.

### Ordinary assistant text

Accepted compact text behavior includes:

- exact top-level assistant append patch with `o/p/v`;
- contextual value-only continuation while a previously accepted text continuation is active;
- preserving active continuation across exact `title_generation` (b51);
- deterministic terminal promotion only when a turn ends without an explicit reasoning-end marker and the already-accepted pre-marker text must become the non-reasoning final answer.

Do not generalize arbitrary `v:string`, arbitrary nested values or arbitrary structural frames into visible assistant text.

### Reasoning

Accepted user-visible reasoning rules:

- exact service-marked `assistant:text:in_progress` part with `metadata.is_thinking_preamble_message=true` is visible reasoning text;
- exact `reasoning_status=is_reasoning` may drive state only, not expose `assistant:thoughts`;
- exact completed reasoning recap with `reasoning_status=reasoning_ended` / `reasoning_recap_type=collapse` is an accepted reasoning-phase end marker;
- visible accepted text before that marker belongs to `思考过程`;
- accepted text after it belongs to final answer;
- a later exact thinking preamble may start another visible reasoning segment;
- `assistant:thoughts` is always non-presentational.

Official-like target presentation remains:

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次正在思考/思考流 -> reasoning_ended -> 折叠思考 -> 完整最终回答`.

Not every answer requires tools or visible reasoning; state must follow actual service events.

### Tools

Accepted association rule:

`completed result.metadata.parent_id == same-response invocation service message ID`.

Only exact response-local parent equality associates a result with an invocation.

Never associate by:

- order;
- adjacency;
- count alignment;
- tool title/name equality;
- recipient equality.

Unmatched results remain unmatched and are never force-paired.

For the GitHub connector family only, b63/b64/b65 currently authorize:

- visible tool input = invocation `metadata.connector_tool_payload`;
- visible tool output = exact-parent matched completed result `message.content`;
- result must identify the invoked resource as GitHub in the already-evidenced shape;
- nested input/output disclosure and decoded hierarchical output are presentation only.

Do not generalize this visible-detail rule to another connector family without fresh evidence.

## Web Rule Lab

The project includes/maintains a development-only **Web Rule Lab** reachable from Settings.

Its role is to make future Web-rule changes cheap to investigate without rebuilding an IPA for every selector/event hypothesis.

### Lab invariants

- uses `WKWebsiteDataStore.default()` so it sees the same current ChatGPT Web login/session state;
- Web page is visibly presented while probing;
- user explicitly pastes/edits JavaScript and taps `执行`;
- no automatic probe runs on launch;
- script text and returned body are response-local UI state only;
- script/result body is not written to `DiagnosticsLogger`, `UserDefaults`, files or another database;
- result can be copied/shared manually by the user;
- safe diagnostics may record only execution success/failure, result JavaScript type/class and result character/byte length;
- Lab never becomes a production response owner and never automatically mutates production Repository state.

### Normal future update workflow

When official Web changes:

1. **Reproduce first** on the current exact production/test IPA; record the visible symptom.
2. **Do not guess a fallback.** Open Web Rule Lab using the same logged-in account/page state.
3. AI provides one small purpose-built JS probe. The user pastes and executes it in the Lab.
4. Probe returns bounded structural evidence needed for the current question: selectors, element attributes, event key/type shapes, safe counts/types, or other non-secret structure.
5. User sends the Lab result/screenshot back.
6. Update this document's `Current accepted ...` rule only after evidence is sufficient.
7. Modify the production adapter minimally. Remove/reject obsolete selector/event logic rather than accumulating compatibility shims unless two live official variants are simultaneously evidenced.
8. Run static/CI/Artifact identity checks.
9. Run one exact real-device Runtime gate proving real protected Send + response lifecycle.
10. Update checkpoint, BUILD_TEST_INDEX/runtime evidence and this document in the same cycle.

This is intentionally a **probe -> understand -> one product rebuild** workflow rather than `guess -> build IPA -> install -> guess again`.

## Probe snippet contract

A probe snippet supplied to the user should normally:

- be self-contained JavaScript;
- return one JSON-serializable object/string rather than dumping the full page;
- inspect the smallest relevant DOM/network/runtime surface;
- prefer key names, tag/type/role/attribute names, counts and booleans over text bodies;
- omit Cookie, Authorization, local/session storage secrets, challenge values and full prompt/answer content;
- not click Send or mutate chat state unless that mutation is the explicit test goal;
- clearly mark any action that will send a real message before the user runs it.

Example shape for a **non-sending composer discovery** probe (illustrative only; current rule still comes from Runtime evidence):

```javascript
(() => {
  const nodes = [...document.querySelectorAll('textarea,[contenteditable="true"],[role="textbox"]')];
  return nodes.map((el, index) => ({
    index,
    tag: el.tagName,
    id: el.id || null,
    role: el.getAttribute('role'),
    contenteditable: el.getAttribute('contenteditable'),
    disabled: 'disabled' in el ? !!el.disabled : null,
    ariaDisabled: el.getAttribute('aria-disabled')
  }));
})()
```

Do not treat this example as a fallback selector list. It is only a Lab discovery pattern.

## Rule-change classification

When a Web update breaks the adapter, classify before editing:

### A. Composer/submit-only change

Examples: `#prompt-textarea` moved, contenteditable wrapper changed, submit button semantics changed.

Action: Lab DOM probe -> one minimal selector/action update -> exact protected-Send Runtime gate.

### B. Protected request interception change

Examples: route/path changes, fetch/XHR ownership changes, response wrapping changes.

Action: Lab/runtime structural probe -> confirm exact method/route/framing -> update interceptor only. Do not replay browser challenge values natively.

### C. Stream grammar change

Examples: new patch shape, reasoning marker moved, tool/result structure changed.

Action: capture privacy-safe structural evidence; update parser at the narrowest evidenced shape; preserve unknown-event observability.

### D. Official account/security boundary change

Examples: new browser challenge mechanism, page no longer permits the established Send path, Web process/session requirements materially change.

Action: treat as an architecture/security gate. Do not bypass or emulate challenge machinery. Reassess TD before product code.

## Production adapter versioning

The adapter does not need a separate marketing version. Its exact behavior is identified by the normal app Candidate/source commit and this document's last-evidence update.

When a Web rule changes materially, record in the current Work/checkpoint:

- old exact Candidate/source;
- exact visible failure;
- Lab/probe evidence identity or screenshot/export;
- old rule rejected/superseded;
- new minimal rule;
- product Candidate/source/Artifact used for Runtime verification.

Do not keep speculative compatibility branches merely because the service may someday revert.

## Privacy/security red lines

Never persist/export through normal diagnostics:

- prompt/answer/reasoning bodies;
- `assistant:thoughts`;
- raw tool request/result bodies;
- Cookie/Authorization values;
- Sentinel/PoW/Turnstile/conduit/challenge values;
- raw account/conversation/message/response IDs;
- arbitrary Web local/session storage.

The Lab may temporarily display explicitly requested page/probe results to the user because it is an interactive developer tool, but those values remain user-controlled transient UI data and are not silently captured by app diagnostics.

## Product non-goals preserved

Option B does **not** authorize:

- full official Web conversation rendering as the daily-chat UI;
- b44 `Native -> full Web conversation -> return + Sync` product flow;
- a second Web/DOM message store;
- continuous DOM mirroring as response authority;
- browser challenge solving/replay outside the official page;
- duplicate Send/resend to recover stream state;
- speculative retry/timer/watchdog/fallback selectors;
- programmatic file-input injection without a separately evidenced attachment path.

## Current next integration boundary

Exact b74 is the first packaged product candidate for cross-device active-response adoption under this rule. Its human Runtime gate must prove:

1. another platform starts a still-active response in an existing conversation;
2. entering that conversation in b74 lets official Web perform its own continuation behavior;
3. only a matching page-owned `/backend-api/f/conversation/resume` is adopted;
4. `ConversationRepository` owns one Native live-response generation and chronological reasoning/tool/final state;
5. no duplicate Send, Native resume request, offset synthesis, stream-status polling, synthetic user bubble or WebSocket-body assumption occurs;
6. terminal authoritative history reconciles once;
7. the b67 local Send path and b72 tested A/B simultaneous-generation path remain intact;
8. diagnostics remain privacy-safe.

CI/Artifact/package verification does not prove this Runtime gate. Any code correction after the emitted b74 Artifact requires a new Candidate identity.

## 2026-09-03 — b92/b93 page-owned continuation loop interruption

Exact b92 single-executor Runtime proves that a background lifecycle transition can stop the official page-owned `stream_status`/snapshot loop even without another executor. Exact b93 proves successful first-responder/document-focus reacquisition does not necessarily restart a stopped loop. The next isolated candidate is foreground official-page rebootstrap without Native Detail Sync; selection rebootstrap remains separate. Stable/Frozen Send remains No.

## b94 Runtime reliability finding — 2026-09-03

Exact b94 proves foreground reload of the same official conversation page can restart page-owned continuation after lifecycle interruption. It also proves this cannot yet be treated as production-stable: after repeated foreground/background transitions and repeated full-page rebootstrap of a very large project conversation, `webViewWebContentProcessDidTerminate` fired and the executor failed. The cause is Unverified; do not label it OOM without WebContent/OS evidence.

Late authoritative Detail had grown to about 5.49 MB / mapping 1535. Two late manual Syncs still returned HTTP200, but authoritative trailing response remained active (`reasoning/timeline/tools = 3/33/30`) and official `stream_status` remained `IS_STREAMING` with no final assistant before export. Current Reload UI is intentionally disabled while any live response phase is active, creating a manual recovery dead-end if the external response stays active indefinitely.

Do not answer this with Native `stream_status`, Native `/resume`, guessed offsets, cadence polling, retry/watchdog timers, WebSocket-body authority, duplicate Send, or a second response store. Any next candidate must isolate an event-driven WebContent/rebootstrap reliability change or explicit user recovery path.
