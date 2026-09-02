# DEV-send-stream

## Status

**Active — exact b87 real-device Runtime is Diagnostic Positive: covered page is structurally visible/loaded but never focused and never starts official continuation. b85 authoritative Detail projection remains Runtime Positive; automatic continuation and automatic final convergence remain Rejected. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b87 Runtime docs/index head before checkpoint-only close: `1874a6651036d7b8e13a93e01cf26412f64e6125`
- checkpoint-only close commit: `bd682c121b0c381d2f5c608e7ada51dfb513f8f4`
- b87 exact diagnostics product source: `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a`
- b87 clean feature/package source: `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`
- b87 Candidate / Build: `DEV-send-stream-0.1.0-b87` / `0.1.0 (87)`
- b87 clean-head PR CI: `33607517120 / 100174803981` — passed
- b87 exact feature-head package: `33607783508 / 100175624048` — passed
- b87 canonical Artifact: `9837745187`
- b87 ZIP: `sha256:5cf72023fdd7b309213da8d31e28e59907fae6e46b3c816230d93386b003dc3b`
- b87 IPA: `sha256:02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`
- b87 built metadata: `0.1.0 (87)` / Candidate b87 / `DiagnosticsSourceCommit=49cf74f5f97e` / iOS17.0 real-device export
- b39-b87 permanently reserved
- Stable/Frozen Send: No

## Send MVP contract

Client-owned Send preserves true same-response SSE. Cross-platform MVP may use genuine page/Detail blocks, but one explicit Sync should become a stable acquisition boundary and later genuine blocks should continue without requiring Sync for every block when an official continuation attaches.

Do not satisfy this with fake typewriter, periodic polling, timers, watchdogs, speculative retry/fallback, duplicate Send/resend, guessed Native `/resume` offsets, a second response store, WebSocket-body authority, or raw hidden-thought presentation.

## b87 exact Runtime — 2026-09-02

Runtime export metadata is exact canonical b87: `0.1.0 (87)`, Candidate `DEV-send-stream-0.1.0-b87`, source `49cf74f5f97e`, iPhone / iOS17.0. Target privacy-safe conversation hash is `sha256:e1e56d1afe93`.

### Authoritative response activity was real

- `09:40:35` user selected target conversation.
- `09:40:36` initial authoritative Detail returned visible `1`, mapping `168`, trailing timeline `66`, tools `66`.
- `09:40:43` user pressed `同步最新消息` once during active generation.
- `09:40:44` authoritative Detail returned visible `1`, mapping `170`, trailing timeline `67`, tools `67`; this started `responseGeneration=1` from `external_authoritative_detail` and rendered one live row.
- Therefore the server-side response was actively evolving while the covered page was being observed; lack of continuation cannot be explained by an inactive/finished response.

### Covered page was not hidden/off-window

After manual re-arm:

- `09:40:45` page reached route `conversation`, `readyState=complete`, `visibilityState=visible`, `document.hidden=false`.
- Native `WKWebView` at `did_finish`: `windowAttached=true`, `windowIsKey=true`, `hidden=false`, `alphaZero=false`, `boundsEmpty=false`, `intersectsWindow=true`.
- The WebView remained at `subviewIndex=0`, had one visible sibling above it, and `userInteractionEnabled=false`.
- Across every recorded `pageActivation` event, `document.hasFocus()` remained `false`.

This rejects the earlier broad hypothesis that continuation failed simply because WebKit considered the page hidden, detached, zero-sized, off-window, incomplete, or on the wrong route.

### Continuation still never activated

- `09:40:45` manual-rearm page load completed.
- Until the first app `willResignActive` at `09:43:26`, there was an approximately **161-second clean foreground window**.
- During that window there were zero matching `externalStreamStatusRequest/Response`, `externalResumeRequest`, `resumeResponse`, `externalStreamingObserved`, page-owned external snapshots, or DOM continuation events.
- Therefore waiting longer in foreground does not make this exact covered page enter the known official continuation path.

### Automatic final convergence also failed

- User WebSocket structural messages remained `hasConversationKey=false`, `targetMatch=false`; the current exact-target acquisition hint did not fire.
- The app later moved foreground/background several times; socket reconnects/messages still did not match the target.
- `09:45:21` the user pressed Sync again.
- `09:45:22` Detail returned visible `2`, mapping `197`, trailing `0`; `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)` then cleared the live row and materialized the completed assistant.
- So final reconciliation logic still works **when authoritative Detail is fetched**; what is absent is an automatic trigger/source that fetches it.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b87-visible-unfocused-no-continuation-20260902.md`.

## Current conclusion

b87 narrows the continuation blocker substantially:

1. **Rejected as primary blocker:** Page Visibility hidden state, WebView detachment, empty/off-window geometry after load, incomplete document readiness, wrong `/c/...` route, or simply insufficient foreground wait.
2. **Observed differential:** covered page is `visible` but continuously `document.hasFocus=false`; the underlying WKWebView is non-interactive and covered by one visible Native sibling.
3. **Still Unverified:** whether focus/interactivity/occlusion is causally required, or whether the decisive difference is the official SPA/router transition created when a user visibly enters the conversation rather than a programmatic full `/c/<id>` load.
4. `/resume` offset remains downstream and should not be investigated until the page actually begins `stream_status`.
5. b82 exact-target user-socket completion hint remains opportunistic and is not reliable final convergence.

## Next exact action — visible Web Rule Lab A/B, no new IPA yet

Use the existing **visible Web Rule Lab** with the same default persistent WebKit store to get the missing A/B without allocating b88:

1. From another official client, start a sufficiently long response in a target conversation.
2. In ChatGPTClient, open Settings -> Web Rule Lab so the official Web page is visibly presented.
3. Visibly enter/tap the same active conversation in the official Web UI.
4. While that official visible page is in the active conversation, run a privacy-safe JS probe returning only:
   - `document.visibilityState`
   - `document.hidden`
   - `document.hasFocus()`
   - `document.readyState`
   - route shape `conversation/root/other`
5. Return the probe result. Do not expose IDs, message bodies, cookies, storage or auth/challenge values.

Decision gate:

- If known-good visible official Web is `hasFocus=true` while entering the active conversation and the covered page remains `hasFocus=false`, an activation/focus A/B becomes evidence-backed for the next Candidate.
- If visible official Web also has `hasFocus=false` while it successfully starts `stream_status`, focus is rejected as causal and the next investigation targets genuine SPA/router conversation-entry transition instead.

Do **not** allocate b88 or change product continuation behavior before this A/B result unless a new deterministic source defect is found.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- default persistent WebKit store remains sole persistent auth-secret authority.
- no raw hidden-thought presentation.
- conversation-entry one-shot authoritative Sync remains a later freshness requirement, not a continuation substitute.

## Evidence ladder

- b84 active authoritative trailing timeline: **Runtime Positive**
- b85 explicit manual Detail projection/repeated same-generation Sync/final reconcile after fetch: **Runtime Positive**
- b85 automatic continuation: **Rejected**
- b86 continuation activation: **Absent**
- b86 automatic final convergence: **Absent**
- b87 Code/PR CI/Artifact/package: **Verified**
- b87 Page Visibility / Native attachment diagnostics: **Runtime Positive**
- b87 covered page visible/loaded but `hasFocus=false`: **Runtime Positive observation; causality Unverified**
- b87 page-owned continuation: **Absent despite ~161s clean foreground**
- b87 automatic final convergence: **Absent; final materialized only after later explicit Sync**
- true cross-platform SSE continuation: **Not acquired**
- Stable/Frozen Send: **No**

## Documentation state

- Runtime evidence file: written.
- `BUILD_TEST_INDEX.md` b87 row: updated to Diagnostic Runtime Positive / continuation rejected.
- Temporary b87 Runtime docsync script/workflow: removed from staging branch after successful target write.
- PR #29 metadata update: pending as the next exact action in this same round; PR metadata does not alter branch source.

## Session round counter

This user turn is **round 22**.
