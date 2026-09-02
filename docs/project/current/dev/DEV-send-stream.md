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
- b87 canonical Artifact: `9837745187`
- b87 IPA: `sha256:02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`
- Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b87-visible-unfocused-no-continuation-20260902.md`
- b39-b87 permanently reserved
- Stable/Frozen Send: No

## b87 exact Runtime — 2026-09-02

Exact canonical b87 export: `0.1.0 (87)`, Candidate `DEV-send-stream-0.1.0-b87`, source `49cf74f5f97e`, iPhone / iOS17.0.

- Initial Detail: visible `1`, mapping `168`, trailing timeline/tools `66`.
- One explicit Sync: mapping `170`, trailing timeline/tools `67`; existing response generation started from authoritative Detail.
- Manual-rearm page: `visibilityState=visible`, `document.hidden=false`, `readyState=complete`, route `conversation`.
- Native WebView: attached to key window, non-empty, intersecting window, not hidden, but non-interactive and under one visible sibling.
- Every recorded page activation: `document.hasFocus=false`.
- Approximately **161 seconds** clean foreground after load with zero `stream_status`, `/resume`, page-owned snapshot, DOM continuation or SSE.
- User WebSocket frames remained `targetMatch=false`.
- Final assistant materialized only after a later explicit Sync; final reconciliation itself worked correctly once authoritative Detail was fetched.

## Current conclusion

Rejected as primary blockers: page hidden state, detached/off-window WebView, incomplete readiness, wrong conversation route, insufficient wait.

Observed but not yet causal: visible covered page remains unfocused (`document.hasFocus=false`), non-interactive and Native-occluded. The remaining fork is **focus/activation vs genuine SPA/router conversation-entry transition**.

Do not investigate guessed `/resume` offset until page-owned `stream_status` actually starts. Automatic final convergence also remains absent because no reliable completion/acquisition trigger fired.

## Next exact action — visible Web Rule Lab A/B, no new IPA

Start a long response from another official client, open Settings -> Web Rule Lab, visibly enter the same active conversation in official Web UI, and return only this privacy-safe state set from the visible active page:

- `document.visibilityState`
- `document.hidden`
- `document.hasFocus()`
- `document.readyState`
- route shape `conversation/root/other`

If known-good visible Web is `hasFocus=true` when continuation starts, focus/activation A/B becomes evidence-backed for the next Candidate. If visible Web is also `hasFocus=false` while continuation starts, reject focus and target genuine SPA/router entry transition.

Do **not** allocate b88 or change continuation behavior before this A/B result unless a new deterministic source defect appears.

## Preserved boundaries

- client-owned Send remains true same-response SSE;
- `ConversationRepository` remains sole Native response/content authority;
- no polling/timer/watchdog/speculative retry/fallback;
- no guessed Native resume offsets or duplicate Send;
- hidden thoughts remain non-presentational;
- b80 presentation/final boundaries remain Frozen/preserved;
- conversation-entry one-shot authoritative Sync remains a later freshness requirement, not continuation.

## Evidence state

- b87 Code/CI/Artifact/package: **Verified**
- b87 Runtime activation diagnostics: **Diagnostic Positive**
- b87 page-owned continuation: **Rejected in exact run**
- b87 automatic final convergence: **Rejected in exact run**
- focus causality: **Unverified**
- Stable/Frozen Send: **No**

`BUILD_TEST_INDEX.md` and durable Runtime evidence are updated. Temporary docs tooling is removed. PR metadata is the only metadata-only external record remaining in this round; it does not alter branch/product identity.

## Session round counter

This user turn is **round 22**.
