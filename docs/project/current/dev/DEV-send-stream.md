# DEV-send-stream

## Status

**Active — exact b88 real-device Runtime is Partial/Diagnostic Positive: covered first-responder activation works and `document.hasFocus=true` is proven, but this sample entered at the final tool phase and authoritative active evidence preceded focus by only ~1 second. Focus causality remains Inconclusive, not Rejected. Automatic final convergence remained absent and required a later explicit Sync. Reuse exact b88 for one clean early/mid-generation A/B; do not allocate b89 yet. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged; title/body synced to b88 Runtime gate
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Durable b88 Runtime docs head before this checkpoint close: `a90844be98d3c1ebe564674e3c66903cc353f778`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 Push CI: `33636383827 / 100268195218` — passed
- b88 PR CI: `33636390081 / 100268217481` — passed
- b88 canonical Artifact: `9848999246`
- b88 Artifact ZIP digest: `sha256:7ae1c816a9300825fc2d0c726a822278abbe1af20735f1310f0f27328617baa7`
- b88 IPA: `ChatGPTClient-0.1.0-b88-dev-send-stream.ipa`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- built metadata: Release `0.1.0 (88)` / Candidate b88 / `DiagnosticsSourceCommit=378811691ccb` / iOS14 minimum / arm64
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Known-good visible official Web differential

Using Web Rule Lab with the same `WKWebsiteDataStore.default()` session authority, the user visibly entered a newly active cross-platform conversation and immediately observed live continuation with the composer already in Stop state. Probe state was `visibilityState=visible`, `hidden=false`, `readyState=complete`, `document.hasFocus=true`.

The same visible page returned coarse `route=other` despite visibly being inside the active conversation, so the existing route-shape probe is diagnostic-only and is not conversation-state authority.

This contrasts with b87 covered production, which was visible/loaded/attached but stayed `document.hasFocus=false` and produced zero page-owned continuation during about 161 seconds foreground. Focus was still only correlation because the visible sample also included genuine user-driven SPA/router conversation entry.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-visible-web-focus-sse-ab-20260902.md`.

## b88 implementation boundary

b88 varies one thing only after explicit manual-Sync rearm: after the existing programmatic target page load finishes, covered WKWebView calls `becomeFirstResponder()` once and directly evaluates `document.hasFocus()`.

Preserved:

- programmatic conversation load unchanged;
- Web interaction remains disabled;
- no Native `stream_status`, `/resume`, offset, polling, timers, retries, watchdogs, duplicate Send, router workaround, WebSocket-body authority or second response store;
- client-owned protected-Send SSE and Repository ownership unchanged.

## Exact b88 Runtime sample — 2026-09-02 22:44 local

Uploaded diagnostics: `ChatGPTClient-Diagnostics-20260902-144605.json` on exact Release b88 / iPhone / iOS17.0.

- Selection page loaded visible/complete but initially `hasFocus=false`.
- `14:44:25Z` Detail: visible `10`, mapping `450`, trailing timeline/tools `24/24`.
- Explicit Sync returned `14:44:36Z`: visible still `10`, mapping `452`, trailing timeline/tools `25/25`. The active turn had advanced by one tool and no final assistant had materialized at that authoritative fetch.
- Existing Detail projection started response generation `1` with 25 tool/timeline items.
- Manual-Sync rearm completed at `14:44:37Z`.
- `coveredExecutor.focusActivationAttempt`: `nativeFirstResponder=true`.
- Page emitted a `focus` event with `hasFocus=true`.
- `coveredExecutor.focusActivationResult`: `documentHasFocus=true`, evaluation succeeded.
- From focus acquisition until the user's second explicit Sync at `14:46:00Z` (~83 seconds), zero matching `stream_status`, `/resume`, resume-response, external-streaming or external-snapshot events were recorded; user-socket messages remained `targetMatch=false`.
- Memory warning did not evict the protected resident; no WebContent-process termination was recorded.
- Second explicit Sync returned at `14:46:02Z`: visible `10 -> 11`, mapping `465`, trailing timeline/tools `0/0`; `externalDetailReconciled(reason=authoritative_assistant_materialized)` correctly cleared the live row.

### Runtime classification

- first-responder activation: **Runtime Positive**
- covered `document.hasFocus=true`: **Runtime Positive**
- page-owned continuation after focus: **Not observed in this run**
- automatic final convergence: **Rejected in this run**; later explicit Sync was required
- focus causality: **Inconclusive**
- SPA/router causality: **Unverified**

Reason for Inconclusive: the user reports the target was already at the final tool call, and the last authoritative proof of active generation at `14:44:36Z` preceded focus acquisition at `14:44:37Z` by only ~1 second. The response may have completed in that narrow interval, so this is not clean enough to reject focus as sufficient.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md`.

## Next exact action — reuse exact b88

Do **not** allocate b89 and do not change product code.

Repeat exact canonical b88 with a deliberately long remote response and enter while it is clearly early or mid-generation:

1. Start a long response on another official client.
2. Enter/select the target conversation while remote reasoning/tool work is visibly still far from completion.
3. Press `同步最新消息` exactly once.
4. Keep ChatGPTClient foregrounded for 30–60 seconds without a second Sync, ideally while the remote side visibly continues advancing.
5. Export diagnostics before manually syncing again if possible.

A decisive focus-negative sample requires `documentHasFocus=true` **and** independent evidence that the same remote generation remains active after focus acquisition while covered Web still produces zero continuation traffic. If so, reject focus as sufficient and investigate genuine official SPA/router conversation-entry transition. If official continuation starts, focus/activation is causal.

## Durable docs / PR sync completed this round

- Runtime checkpoint classification: committed.
- Visible-Web A/B evidence: committed.
- b88 Runtime evidence: committed.
- `BUILD_TEST_INDEX.md`: b88 row added with Runtime Partial/Inconclusive classification.
- `MODULE_STATUS.md`: b88 focus Runtime override added.
- `TECHNICAL_DECISIONS.md`: b88 focus Runtime qualification added.
- `WEB_SEND_ADAPTER.md`: b88 focus activation qualification added.
- Docs-only recovery workflow `33645264795 / 100298240665`: passed and pushed durable docs at `a90844be98d3c1ebe564674e3c66903cc353f778`.
- PR #29 metadata synced to `DEV-send-stream: b88 focus activation works — clean early-runtime A/B next`; PR remains open / mergeable / unmerged.
- b88 product source/package/Artifact identities were not changed by docs recovery.

## Session round counter

This user turn is **round 27**.
