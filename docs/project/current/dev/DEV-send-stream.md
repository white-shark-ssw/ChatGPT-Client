# DEV-send-stream

## Status

**Active — exact b87 real-device Runtime is Diagnostic Positive: covered page is structurally visible/loaded but never focused and never starts official continuation. b85 authoritative Detail projection remains Runtime Positive; automatic continuation and automatic final convergence remain Rejected. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b87 exact diagnostics product source: `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a`
- b87 clean feature/package source: `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`
- b87 Candidate / Build: `DEV-send-stream-0.1.0-b87` / `0.1.0 (87)`
- b87 clean-head PR CI: `33607517120 / 100174803981` — passed
- b87 exact feature-head package: `33607783508 / 100175624048` — passed
- b87 canonical Artifact: `9837745187`
- b87 ZIP: `sha256:5cf72023fdd7b309213da8d31e28e59907fae6e46b3c816230d93386b003dc3b`
- b87 IPA: `sha256:02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`
- b87 built metadata: `0.1.0 (87)` / Candidate b87 / `DiagnosticsSourceCommit=49cf74f5f97e` / iOS17.0 real-device export
- Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b87-visible-unfocused-no-continuation-20260902.md`
- b39-b87 permanently reserved
- Stable/Frozen Send: No

## Send MVP contract

Client-owned Send preserves true same-response SSE. Cross-platform MVP may use genuine page/Detail blocks, but one explicit Sync should become a stable acquisition boundary and later genuine blocks should continue without requiring Sync for every block when an official continuation attaches.

Do not satisfy this with fake typewriter, periodic polling, timers, watchdogs, speculative retry/fallback, duplicate Send/resend, guessed Native `/resume` offsets, a second response store, WebSocket-body authority, or raw hidden-thought presentation.

## b87 exact Runtime — 2026-09-02

Runtime export metadata is exact canonical b87: `0.1.0 (87)`, Candidate `DEV-send-stream-0.1.0-b87`, source `49cf74f5f97e`, iPhone / iOS17.0. Target privacy-safe conversation hash is `sha256:e1e56d1afe93`.

- `09:40:36` initial authoritative Detail: visible `1`, mapping `168`, trailing timeline/tools `66`.
- `09:40:44` one explicit Sync: visible `1`, mapping `170`, trailing timeline/tools `67`; Repository started `responseGeneration=1` from `external_authoritative_detail` and rendered one live row.
- The evolving `168 -> 170` mapping and `66 -> 67` tail prove the external response was active.
- After manual re-arm, target page reached route `conversation`, `readyState=complete`, `visibilityState=visible`, `document.hidden=false`.
- Native WebView at `did_finish`: `windowAttached=true`, `windowIsKey=true`, `hidden=false`, `alphaZero=false`, `boundsEmpty=false`, `intersectsWindow=true`.
- The WebView remained non-interactive, under one visible Native sibling, and every recorded page activation had `document.hasFocus=false`.
- From re-arm load completion `09:40:45` to first `willResignActive` `09:43:26`, approximately **161 seconds** foregrounded with zero matching `stream_status`, `/resume`, page-owned snapshot, DOM continuation, or SSE events.
- User WebSocket frames remained `hasConversationKey=false`, `targetMatch=false`.
- `09:45:21` later explicit Sync fetched final authoritative state; `09:45:22` visible messages became `2`, trailing `0`, and `externalDetailReconciled(reason=authoritative_assistant_materialized)` correctly cleared the live row.

## Current conclusion

1. **Rejected as primary blocker:** Page Visibility hidden state, WebView detachment, zero/off-window geometry after load, incomplete readiness, wrong conversation route, or insufficient foreground wait.
2. **Observed strong differential:** covered page is visible/ready but always `document.hasFocus=false`; underlying WKWebView is non-interactive and occluded by one visible Native sibling.
3. **Causality remains Unverified:** focus/interactivity/occlusion may matter, but the real trigger could instead be the genuine official SPA/router conversation-entry transition created by visible user navigation rather than programmatic full `/c/<id>` load.
4. `/resume` offset remains downstream; do not investigate/guess it until the page begins `stream_status`.
5. Automatic final reconcile works after authoritative Detail fetch; automatic trigger/discovery remains absent.

## Next exact action — visible Web Rule Lab A/B, no new IPA yet

Use the existing visible Web Rule Lab with the same default persistent WebKit store:

1. Start a long response from another official client.
2. Open Settings -> Web Rule Lab in ChatGPTClient.
3. Visibly tap/enter the same active conversation in official Web UI.
4. On the visible active page run only this privacy-safe state probe: `document.visibilityState`, `document.hidden`, `document.hasFocus()`, `document.readyState`, and coarse route shape `conversation/root/other`.
5. Return the probe result; do not expose IDs, messages, cookies, storage or auth/challenge values.

Decision gate:

- visible known-good official Web `hasFocus=true` while it begins continuation -> focus/activation A/B is evidence-backed for next Candidate;
- visible known-good official Web also `hasFocus=false` while it begins continuation -> reject focus as causal and investigate genuine SPA/router entry transition.

Do **not** allocate b88 or change continuation behavior before this A/B result unless a new deterministic source defect is found.

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
- b86 continuation activation / automatic final convergence: **Absent**
- b87 Code/PR CI/Artifact/package: **Verified**
- b87 visibility/attachment diagnostics: **Runtime Positive**
- b87 covered page visible/loaded but `hasFocus=false`: **Observed; causality Unverified**
- b87 page-owned continuation: **Absent despite ~161s clean foreground**
- b87 automatic final convergence: **Absent; final only after later explicit Sync**
- true cross-platform SSE continuation: **Not acquired**
- Stable/Frozen Send: **No**

## Documentation state

- Runtime evidence file and `BUILD_TEST_INDEX.md` b87 classification are updated.
- Temporary b87 Runtime docsync files were removed from staging.
- PR #29 metadata is maintained separately; PR metadata does not alter branch product identity.

## Session round counter

This user turn is **round 22**.
