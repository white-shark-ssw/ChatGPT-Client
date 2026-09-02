# DEV-send-stream

## Status

**Active — b87 diagnostics-only package is now Code/PR-CI/Artifact verified and ready for real-device Runtime. b86 remains the decisive Runtime baseline: covered-page continuation activation was absent despite authoritative active reasoning. b87 changes diagnostics only; no continuation behavior fix is claimed. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b87 exact diagnostics product source: `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a`
- b87 clean feature/package head and PR #29 head before docs-only evidence sync: `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`
- b85 exact product/config source: `ec64dd170a6386612af8cb68b394045ce3c85313`
- b85 Runtime: **manual authoritative block projection Positive / automatic continuation Rejected**
- b86 exact diagnostics product source: `dc77a94be5b2f7eecd822480f759358ad6a0ad25`
- b86 clean package head: `f90caca0419f13254567485171fac7d970aa8c95`
- b86 Candidate / Build: `DEV-send-stream-0.1.0-b86` / `0.1.0 (86)`
- b86 Push: `33566939415 / 100052171917` — passed
- b86 PR: `33566968066 / 100052259409` — passed
- b86 Artifact: `9823485856`
- b86 ZIP: `sha256:cdccdcd034964b99e98e62c2e79a9bece96c190138c774e6f1590896d54fbacb`
- b86 IPA: `sha256:25d483ac31473b124e6ad555b79c488e78da91ec1761ee8a40076b6e978bee6f`
- b86 Runtime export: exact Candidate b86 / source `f90caca0419f` / iPhone / iOS17.0
- b87 Candidate / Build: `DEV-send-stream-0.1.0-b87` / `0.1.0 (87)`
- b87 clean-head PR CI: `33607517120 / 100174803981` — passed
- b87 exact feature-head packaging: `33607783508 / 100175624048` — passed
- b87 canonical Artifact: `9837745187`
- b87 ZIP: `sha256:5cf72023fdd7b309213da8d31e28e59907fae6e46b3c816230d93386b003dc3b`
- b87 IPA: `sha256:02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`
- b87 built metadata: `0.1.0 (87)` / Candidate `DEV-send-stream-0.1.0-b87` / `DiagnosticsSourceCommit=49cf74f5f97e` / minimum iOS14 / arm64
- b87 PR-triggered Artifact built from synthetic merge `93f1a827f938` is **non-canonical** and must not be used for Runtime evidence
- b39-b87 permanently reserved
- Stable/Frozen Send: No

## Send MVP contract

Client-owned Send keeps true same-response SSE. Cross-platform MVP may use real block/page snapshots, but one explicit Sync must be a stable acquisition boundary and later genuine blocks should continue without pressing Sync for every block when a real page-owned continuation attaches.

Do not satisfy this with fake typewriter, polling, timer, watchdog, speculative retry/fallback, duplicate Send/resend, a second response store, guessed Native resume/offset, WebSocket-body authority, or raw hidden-thought presentation.

## b86 decisive Runtime

Target privacy-safe conversation hash: `sha256:d597360f6d29`.

- `07:15:10` explicit Sync started.
- `07:15:20` authoritative Detail HTTP200 returned visible `34`, trailing timeline `6 = reasoning 1 + tools 5`.
- `responseGeneration=1` started from `external_authoritative_detail` and one live row rendered.
- `07:15:21` `manual_sync_rearm`; `07:15:22` covered page loaded.
- From that load until the next explicit Sync at `07:16:37` (~75 seconds), there were zero `externalStreamStatus*`, `externalResume*`, `externalStreamingObserved`, or page-owned/Repository snapshot events.
- User WebSocket emitted a structural message with `hasConversationKey=false`, `targetMatch=false`; current exact-target completion hint did not fire.
- `07:16:37` user pressed Sync again.
- `07:16:43` Detail returned visible `35`, trailing `0`; `externalDetailReconciled(reason=authoritative_assistant_materialized)` cleared the live row.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b86-no-continuation-no-final-auto-convergence-20260902.md`.

## Current conclusion

b86 resolves the prior fork: the covered page did **not** request `stream_status` at all during the clean observation window. The bottleneck is before resume/offset and before page-owned plural reads: **official page continuation activation itself**.

The lack of automatic final answer is separately explained by the current completion/update trigger also not firing: the user-socket structural frame did not match the target conversation. The b82 exact-target WebSocket hint is opportunistic, not reliable convergence.

Recorded visible Web Rule Lab evidence uses the same default persistent `WKWebsiteDataStore`. When the user visibly entered an externally active target conversation, official Web issued matching `stream_status` within roughly two seconds, then page-owned `/resume {conversation_id, offset}` and, after a 404, repeated page-owned `stream_status + /backend-api/conversations/{conversation}` reads.

Exact b86 covered programmatic `/c/<id>` load differs materially. This strengthens the working hypothesis that server capability is not the primary blocker; the likely differential is page activation/navigation/visibility/focus state, but the exact causal field/action remains Unverified.

## b87 diagnostics-only scope

Candidate availability was checked against the current candidate index, actual Xcode identity (`0.1.0 (86)`), active checkpoints, branch/PR identity and repository commit search; no existing b87 allocation/commit was found.

b87 may add only privacy-safe, event-driven diagnostics:

- JS page activation state: `document.visibilityState`, `document.hidden`, `document.hasFocus()`, `document.readyState`;
- route shape only (`conversation` / `root` / `other`), never raw IDs or full paths;
- event reason only for initial/readystatechange/visibilitychange/focus/blur/pageshow/pagehide/popstate;
- Native WKWebView structure at attach/load: window attachment, hidden state, alpha-zero boolean, empty bounds, coarse window intersection, sibling/subview position and interaction-enabled boolean.

b87 must **not** call `stream_status`, call `/resume`, choose/guess offset, add polling/timers/retries/watchdogs, front/focus/show the covered WebView, implement conversation-entry Sync, change response authority, or expose hidden reasoning.

## b87 canonical package evidence

The b87 product/config change is diagnostics-only. Exact product commit `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a` added page/WebView activation structure probes and build 87 identity. A later workflow-comment-only commit produced clean feature/package head `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`.

Normal PR CI for that clean head passed, but GitHub's `pull_request` checkout built synthetic merge source `93f1a827f938`; that Artifact is intentionally non-canonical for device evidence.

Canonical b87 was therefore packaged in isolated run `33607783508 / 100175624048` after an explicit exact-source assertion and checkout of `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`. The resulting Artifact `9837745187` has ZIP digest `sha256:5cf72023fdd7b309213da8d31e28e59907fae6e46b3c816230d93386b003dc3b`. Extracted IPA SHA is `02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`; its built Info.plist reports `0.1.0 (87)`, Candidate `DEV-send-stream-0.1.0-b87`, `DiagnosticsSourceCommit=49cf74f5f97e`, minimum iOS14.

Evidence classification: Code written / exact staging guard passed / PR CI passed / Artifact produced and identity verified. **Runtime/manual/real-device remains Pending.**

## Next exact action

Install the canonical b87 IPA on the primary iPhone/iOS17 device. Start a sufficiently long response from another official client while the same conversation is selected in ChatGPTClient. During active generation press `同步最新消息` exactly once, then keep ChatGPTClient foregrounded without a second Sync. Export diagnostics after additional reasoning/tool progress or completion.

Compare, in timestamp order:

- `coveredExecutor.pageActivation`: `visibilityState`, `hidden`, `hasFocus`, `readyState`, `route`, `reason`;
- `coveredExecutor.webViewActivation`: `windowAttached`, `windowIsKey`, `hidden`, `alphaZero`, `boundsEmpty`, `intersectsWindow`, `subviewIndex`, `siblingCount`, `visibleSiblingCountAbove`, `userInteractionEnabled`;
- whether `externalStreamStatusRequest/Response`, `externalResumeRequest`, `resumeResponse`, `externalStreamingObserved`, external snapshots or DOM structure begin afterward.

Do not allocate b88 or change continuation behavior until this b87 Runtime distinguishes page visibility/focus/attachment from router/navigation activation.

## Recorded later requirement

Entering/selecting a conversation should eventually perform exactly one authoritative latest-message Sync through `ConversationRepository`. This remains separate from continuation and does not keep an active external response current by itself.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- default persistent WebKit store remains sole persistent auth-secret authority.
- no raw hidden-thought presentation.

## Evidence ladder

- b83 covered-page manual acquisition: **Runtime Rejected**
- b84 active authoritative trailing timeline: **Runtime Positive**
- b85 explicit manual Detail block projection: **Runtime Positive**
- b85 repeated Sync same response generation: **Runtime Positive**
- b85 final reconcile when Detail is fetched: **Runtime Positive**
- b85 automatic continuation: **Runtime Rejected**
- b86 Code/Push+PR CI/Artifact/package: **Verified**
- b86 continuation-structure diagnostics: **Runtime Positive**
- b86 page-owned continuation activation: **Absent in exact run**
- b86 automatic final convergence: **Absent in exact run; final materialized only after manual Sync**
- b86 true cross-platform SSE: **Not acquired**
- b87 Code/PR CI/Artifact/package: **Verified**
- b87 Runtime/manual/real-device: **Pending**
- Stable/Frozen Send: **No**

## Session round counter

This user turn is **round 21**.
