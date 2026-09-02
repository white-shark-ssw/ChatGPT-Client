# DEV-send-stream

## Status

**Active — exact b87 real-device Runtime is Diagnostic Positive: covered page is structurally visible/loaded but never focused and never starts official continuation. b85 authoritative Detail projection remains Runtime Positive; automatic continuation and automatic final convergence remain Rejected. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b87 product source: `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a`
- b87 clean package source: `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`
- Candidate / Build: `DEV-send-stream-0.1.0-b87` / `0.1.0 (87)`
- canonical Artifact: `9837745187`
- IPA SHA-256: `02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`
- Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b87-visible-unfocused-no-continuation-20260902.md`
- b39-b87 permanently reserved
- Stable/Frozen Send: No

## b87 exact Runtime

Exact canonical b87 / iPhone / iOS17.0.

- Active authoritative Detail evolved `mapping 168 -> 170`, trailing timeline/tools `66 -> 67`; one explicit Sync correctly created the existing external response generation.
- Manual-rearm official page reached route `conversation`, `readyState=complete`, `visibilityState=visible`, `document.hidden=false`.
- Native WKWebView was attached to key window, not hidden, non-empty and intersecting the window.
- It remained non-interactive, under one visible Native sibling, and every recorded page event had `document.hasFocus=false`.
- After re-arm page load, approximately **161 seconds** of clean foreground produced zero `stream_status`, `/resume`, page-owned snapshot, DOM continuation or SSE events.
- User WebSocket frames remained `targetMatch=false`.
- Final assistant materialized only after a later explicit Sync; `externalDetailReconciled(authoritative_assistant_materialized)` worked once authoritative Detail was fetched.

## Current conclusion

Rejected as primary blockers: Page Visibility hidden state, detached/off-window WebView, incomplete readiness, wrong conversation route, or insufficient foreground wait.

Remaining evidence fork:

1. focus/interactivity/Native occlusion is causally required; or
2. genuine visible official SPA/router conversation-entry transition is the trigger rather than programmatic full `/c/<id>` load.

`document.hasFocus=false` is a strong observed differential, **not yet a proven cause**. `/resume` offset remains downstream and must not be guessed before page-owned `stream_status` begins.

Automatic final convergence remains absent because no reliable acquisition/completion trigger fetched authoritative Detail after completion.

## Next exact action — visible Web Rule Lab A/B

No b88 and no new IPA yet.

While another official client is generating a long response:

1. open Settings -> Web Rule Lab;
2. visibly enter/tap the same active conversation in official Web UI;
3. return only these privacy-safe fields from that visible active page:
   - `document.visibilityState`
   - `document.hidden`
   - `document.hasFocus()`
   - `document.readyState`
   - route shape `conversation/root/other`.

If known-good visible Web has `hasFocus=true` while continuation starts, focus/activation A/B is evidence-backed. If visible Web also has `hasFocus=false` while continuation starts, reject focus and investigate SPA/router entry transition.

## Preserved boundaries

- client-owned Send true same-response SSE preserved;
- `ConversationRepository` remains sole Native response/content authority;
- no polling/timer/watchdog/retry/fallback/duplicate Send;
- no guessed Native resume offset;
- hidden thoughts non-presentational;
- b80 presentation/final boundaries preserved;
- conversation-entry one-shot Sync remains later freshness scope, not continuation.

## Evidence state

- b87 Code/CI/Artifact/package: **Verified**
- b87 Runtime diagnostics: **Diagnostic Positive**
- automatic continuation: **Rejected in exact run**
- automatic final convergence: **Rejected in exact run**
- focus causality: **Unverified**
- Stable/Frozen Send: **No**

Durable Runtime evidence and `BUILD_TEST_INDEX.md` are updated; temporary docs tooling is removed. PR #29 metadata is maintained separately and does not alter branch/product identity.

## Session round counter

This user turn is **round 22**.
