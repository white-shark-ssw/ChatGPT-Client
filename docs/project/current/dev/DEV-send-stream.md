# DEV-send-stream

## Status

**Active — b87 covered-page continuation is Rejected; visible official Web A/B on 2026-09-02 is Runtime Positive and shows a known-good cross-platform active conversation immediately continuing with official SSE while `document.hasFocus=true`. b88 is allocated as a focus-only causal A/B. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Branch / PR head before b88 allocation: `47ec5ce1f9ed8058d543b018c72072e02def5779`
- b87 Candidate / Build: `DEV-send-stream-0.1.0-b87` / `0.1.0 (87)` — permanently reserved
- b87 canonical Artifact: `9837745187`
- b87 IPA SHA-256: `02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`
- **b88 allocated Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`**
- b39-b88 permanently reserved once b88 source lands
- Stable/Frozen Send: No

## b87 exact Runtime boundary

- One explicit Sync correctly projected active authoritative Detail into the existing external response generation.
- Covered target page was `visibilityState=visible`, `hidden=false`, `readyState=complete`, attached to the key window with valid geometry, but every recorded page activation had `document.hasFocus=false`.
- Approximately 161 seconds clean foreground produced zero page-owned `stream_status`, `/resume`, snapshot, DOM continuation or SSE events.
- Final assistant materialized only after a later explicit Sync; reconciliation itself worked once authoritative Detail was fetched.
- Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b87-visible-unfocused-no-continuation-20260902.md`.

## Visible official Web A/B — 2026-09-02

User opened Web Rule Lab using the same default persistent WebKit store, visibly entered a newly active cross-platform conversation, and observed immediately that:

- the already-running remote response was continuing live in the official Web UI;
- the composer Send control was already the active-response **Stop** control, proving the official page had acquired the response lifecycle state;
- the page probe returned `visibilityState=visible`, `hidden=false`, `readyState=complete`, `document.hasFocus=true`;
- the coarse probe returned `route=other`, but the screenshot/user observation proves the Web UI was visibly inside the target conversation, so the existing `/^\/c\//` route classifier is too narrow for this visible-page case and must not be treated as conversation-state authority.

This is a known-good continuation sample and creates a direct differential against b87 covered production: visible official Web `hasFocus=true` + live continuation versus covered Web `hasFocus=false` + no continuation.

**Causality is not yet proven.** A genuine user-driven SPA/router entry transition also occurred in the known-good sample. The next candidate must change only focus/activation while keeping the covered programmatic conversation load unchanged, so one Runtime run can distinguish focus from router-entry causality.

## b88 scope — focus-only causal A/B

Evidence-backed minimal experiment:

1. Keep the existing `observeExistingConversation` programmatic conversation URL load unchanged.
2. Only for explicit manual-Sync re-arm, after the target page finishes loading, attempt to make the covered `WKWebView` first responder.
3. Do **not** synthesize/call `stream_status`, `/resume`, offset, WebSocket bodies, polling, timers, retries, watchdogs or duplicate Send.
4. Do **not** add another response/content store or change `ConversationRepository` authority.
5. Keep client-owned protected-Send behavior unchanged.
6. Log whether the Native first-responder activation attempt succeeded, then use the existing b87 page-activation diagnostics to observe whether `document.hasFocus` changes and the existing b86 continuation diagnostics to observe whether official page traffic starts.
7. Do not add a SPA/router workaround in b88; router remains the alternate hypothesis if focus activation succeeds but continuation still does not start.

## b88 Runtime decision gate

During another-platform long response:

- press `同步最新消息` once;
- keep ChatGPTClient foregrounded;
- do not press a second Sync before evidence is collected.

Interpretation:

- activation succeeds -> `document.hasFocus=true` -> page starts `stream_status`/`resume`/SSE: focus/activation is causal and continuation path is Runtime Positive;
- activation succeeds -> `document.hasFocus=true` but still zero continuation traffic: focus is rejected as sufficient; investigate genuine SPA/router conversation-entry transition next;
- activation attempt reports failure or `document.hasFocus` stays false: b88 is inconclusive for focus causality; do not infer router causality from that alone.

## Preserved boundaries

- client-owned Send true same-response SSE preserved;
- `ConversationRepository` sole Native response/content authority;
- `AuthSessionStore` sole Native auth/account authority;
- `WKWebsiteDataStore.default()` sole persistent auth-secret authority;
- no polling/timer/watchdog/retry/fallback/duplicate Send;
- no guessed Native resume offset;
- hidden thoughts non-presentational;
- b80 presentation/final boundaries preserved;
- conversation-entry one-shot authoritative Sync remains later freshness scope, not a continuation substitute.

## Evidence state

- b87 Code/CI/Artifact/package: **Verified**
- b87 covered page visible/loaded: **Runtime Positive**
- b87 covered page focus: **false throughout Runtime**
- b87 automatic continuation/final convergence: **Rejected**
- visible Web Rule Lab known-good cross-platform continuation: **Runtime Positive user observation**
- visible Web `document.hasFocus=true`: **Runtime Positive observation**
- focus causality: **Evidence-backed A/B required; not yet proven**
- b88 Candidate: **Allocated; code not yet landed at this checkpoint**
- Stable/Frozen Send: **No**

## Next exact action

Land the guarded b88 focus-only A/B against exact branch head derived from `47ec5ce1f9ed8058d543b018c72072e02def5779`, update build/Candidate identity to 88, run `git diff --check` and Xcode/CI, produce one canonical feature-head IPA, then stop at the real-device Runtime gate above.

## Session round counter

This user turn is **round 26**.
