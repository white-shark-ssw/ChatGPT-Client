# DEV-send-stream

## Status

**Active — exact b89 real-device Runtime rejects covered-Web interactivity as sufficient for automatic cross-platform continuation. The next evidence-backed single-variable A/B is frontmost presentation/occlusion: b90 will keep b89 route, focus, interactivity, page-owned continuation and Repository ownership unchanged, but after explicit manual-Sync rearm will bring the same executor WKWebView above the Native sibling so it is genuinely frontmost. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Pre-runtime feature head: `f9ea8da29dcd1f808f4533ed05fa97f1fb4eeb2b`
- b89 Candidate / Build: `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)` permanently reserved
- b89 product commit: `f39bc9387575028d431b85409780a2f3670b3259`
- b89 exact package source: `fe45aeadf7ae03bf09aff66a8a05aa2542959676`
- b89 Artifact: `9881665748`
- b89 IPA SHA-256: `c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`
- Stable/Frozen Send: No

## Exact b89 Runtime result — 2026-09-03

User tested exact `DEV-send-stream-0.1.0-b89` / source marker `fe45aeadf7ae` on iPhone / iOS17 and reported that the project conversation still did not continue automatically; explicit `同步最新消息` remained necessary.

Diagnostics make this a decisive negative rather than an ambiguous near-terminal sample:

- initial authoritative Detail at `07:08:04Z`: timeline `4`, tools `3`, reasoning `1`;
- first explicit Sync completed at `07:08:09Z`: timeline `5`, tools `4`, reasoning `1`; one external Repository response generation started from authoritative Detail;
- rearmed target page completed with `userInteractionEnabled=true`, non-empty/intersecting bounds, key-window attachment and `visibleSiblingCountAbove=1`;
- first-responder activation succeeded: `nativeFirstResponder=true`, `documentHasFocus=true`;
- fresh target page user activation remained available but transient/sticky booleans were false at the focus sample;
- after rearm there were zero matching page-owned `externalStreamStatus*`, `externalResume*`, `externalStreamingObserved` or external snapshot events;
- observed user WebSocket frames remained structural and `targetMatch=false`;
- second explicit Sync at `07:10:06Z` returned at `07:10:07Z` with the same response generation now exposing timeline `28`, tools `25`, reasoning `3`, mapping `64`;
- therefore the same remote response advanced by at least `5 -> 28` timeline items / `4 -> 25` tools while the covered executor emitted no automatic continuation path. The newer content appeared only through explicit authoritative Detail Sync.

Classification:

- b89 package identity: verified;
- `isUserInteractionEnabled=true`: Runtime exercised;
- first-responder / `document.hasFocus=true`: Runtime Positive;
- authoritative manual Detail block projection: Runtime Positive;
- automatic page-owned continuation after interactivity+focus: Runtime Negative;
- interactivity as a sufficient condition: **Rejected**;
- automatic final convergence: still Rejected / Unverified for reliability;
- Stable/Frozen Send: No.

Do not infer that user activation itself is universally required or impossible: the successful visible-Web fresh-root control already continued from unscoped full navigation with transient activation false, while the later manual Lab sticky-activation read was contaminated by the Execute action.

## Causal state after b89

Already rejected as sufficient or sole explanation:

- hidden/detached/unready document state;
- focus alone;
- `WKWebView.isUserInteractionEnabled` alone;
- transient activation at navigation;
- trusted target click;
- same-document SPA transition;
- initial unscoped `/c/{conversation}` route alone, because visible official Web can canonicalize that route to `/g/{scope}/c/{conversation}` and begin continuation.

The remaining evidenced covered-vs-visible presentation difference is z-order/occlusion. Source attaches the production executor with `hostView.insertSubview(webView, at: 0)`; exact b89 Runtime reports `subviewIndex=0`, `visibleSiblingCountAbove=1`. The known-positive Web Rule Lab is genuinely frontmost/visible. This makes frontmost presentation the next smallest single-variable experiment.

## b90 intended A/B

Candidate identity is reserved only by the batch below after final guard: `DEV-send-stream-0.1.0-b90` / `0.1.0 (90)`.

Planned behavior delta relative to b89:

- only on explicit manual-Sync rearm, bring the existing executor `WKWebView` to the front of its current Root host before loading the same target conversation;
- retain `isUserInteractionEnabled=true`;
- retain b88/b89 first-responder focus activation;
- retain the same unscoped target load and all existing page-owned status/resume/snapshot observation;
- retain client-owned protected Send path and sole `ConversationRepository` response ownership;
- add only privacy-safe z-order diagnostics needed to prove `visibleSiblingCountAbove=0` after the A/B activation.

This is diagnostic Runtime scope only and does not reverse the product decision rejecting full official-Web conversation rendering as the daily-chat UI.

## Batch recovery state

**Active recovery point — b89 Runtime sync + b90 frontmost A/B preparation.**

Known baseline before the batch:

- branch head before this checkpoint update: `f9ea8da29dcd1f808f4533ed05fa97f1fb4eeb2b`;
- `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- PR #29 only open development PR identified for this Work;
- b90 commit search: no result;
- branch scan: no b90 branch/candidate identity found;
- BUILD_TEST_INDEX current top identity before allocation: b89.

Intended write batches:

1. **Completed by this checkpoint commit:** persist decisive b89 Runtime result and b90 exact intended single-variable scope.
2. **Pending:** create exact b90 product/config/workflow change on the same feature branch: Root frontmost-on-manual-rearm A/B + Build/Candidate 90 + `ios-foundation.yml` b90 identity.
3. **Pending:** run deterministic static/Simulator validation, then Push/PR CI and canonical package generation.
4. **Pending:** record b89 Runtime and b90 Code/CI/Artifact/package evidence in `runtime-evidence`, `BUILD_TEST_INDEX.md`, `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, `WEB_SEND_ADAPTER.md`, PR metadata and this checkpoint.
5. **Human Gate after package verification:** exact b90 real-device long-response A/B.

Recovery rule: after any interruption, re-read this checkpoint and actual branch/PR/head/Candidate state, then perform only missing deterministic writes. Never replay b89, never reuse b89 identity, and never allocate another Candidate if b90 has already been emitted.

## Next exact action

Apply the b90 single-variable z-order patch, bump exact Candidate/Build to 90, update the permanent CI Artifact identity, run static/Simulator validation, Push/PR CI, verify the canonical IPA identity, synchronize durable docs/PR, then hand exact b90 to the user for Runtime.

Runtime decision for b90:

- `visibleSiblingCountAbove=0` followed by genuine page-owned `stream_status` / `/resume` / snapshot continuation while the remote answer remains active -> frontmost/occlusion differential Runtime Positive; retain only the minimum necessary consequence and then redesign the final covered production form without full-Web daily UI;
- frontmost established but still zero page-owned continuation while remote generation demonstrably advances -> reject z-order/occlusion as sufficient and continue to the next evidenced WKWebView browsing-context differential;
- remote answer terminal before frontmost activation -> Inconclusive; reuse exact b90, do not allocate b91.

## Preserved boundaries

Official page owns continuation transport; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, cadence reproduction, retry/watchdog, duplicate Send, WebSocket-body authority, hidden-thought presentation or second response store.

## Session round counter

This user turn is **round 56**.
