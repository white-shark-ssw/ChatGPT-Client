# DEV-send-stream

## Status

**Active — exact b88 real-device Runtime is Partial/Diagnostic Positive: the focus-only A/B successfully made the covered WKWebView first responder and `document.hasFocus=true`, but the target response was already at its final tool phase and authoritative active evidence preceded focus by only ~1 second. Focus causality is therefore Inconclusive, not Rejected. Automatic final convergence remained absent and required a later explicit Sync. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged; metadata still needs b88 sync
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Branch head before this Runtime-doc batch: `f8d536e71c72174e719d17693934997d88686c04`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 Push CI: `33636383827 / 100268195218` — passed
- b88 PR CI: `33636390081 / 100268217481` — passed
- b88 canonical Artifact: `9848999246`
- b88 Artifact ZIP digest: `sha256:7ae1c816a9300825fc2d0c726a822278abbe1af20735f1310f0f27328617baa7`
- b88 IPA: `ChatGPTClient-0.1.0-b88-dev-send-stream.ipa`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b88 built metadata: `0.1.0 (88)` / Candidate b88 / `DiagnosticsSourceCommit=378811691ccb` / iOS14 minimum / arm64
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Known-good visible Web A/B — 2026-09-02

Web Rule Lab using the same `WKWebsiteDataStore.default()` visibly entered a newly active cross-platform conversation and immediately showed live continuation plus the active-response Stop control. Probe state was `visibilityState=visible`, `hidden=false`, `readyState=complete`, `document.hasFocus=true`. The coarse probe returned `route=other` despite visibly being inside the target conversation, so that route classifier is diagnostic-only.

This supplies a known-good differential against b87 covered production (`hasFocus=false` + no continuation), but focus was not yet causal because the visible sample also included a real user-driven SPA/router conversation-entry transition.

## b88 implementation — focus-only causal A/B

Exact product source `31d24e8b9ab4676effd757a793162abbdb0d7012` changes only `ChatGPTClient/RootViewController.swift` plus build/Candidate identity in `project.pbxproj`.

- Existing programmatic target-conversation load is unchanged.
- Only explicit manual-Sync re-arm arms one one-shot focus probe.
- After the re-armed target page finishes, the covered WKWebView calls `becomeFirstResponder()` once and directly evaluates `document.hasFocus()`.
- Web interaction remains disabled.
- No Native `stream_status`, `/resume`, offset, polling, timers, retries, watchdogs, duplicate Send, router workaround, WebSocket-body authority or second response store is added.

## b88 exact real-device Runtime sample — 2026-09-02 22:44 local

Uploaded diagnostics: `ChatGPTClient-Diagnostics-20260902-144605.json`.

Exact package metadata matches canonical b88: Release `0.1.0 (88)`, Candidate `DEV-send-stream-0.1.0-b88`, source `378811691ccb`, iPhone / iOS17.0.

Timeline:

1. Selection load started at `14:44:23Z`; initial covered page loaded route `conversation`, visible, complete, but `hasFocus=false`.
2. Authoritative Detail at `14:44:25Z` was still active: visible messages `10`, mapping `450`, trailing timeline `24`, all `24` tools, no trailing reasoning/final materialization.
3. User explicitly Sync'd at `14:44:34Z`; Detail returned at `14:44:36Z` with visible messages still `10`, mapping `452`, trailing timeline/tools `25 -> 25`. This proves the active remote turn had advanced by one additional tool and still had no materialized final assistant at that authoritative fetch.
4. Existing b85 Detail projection correctly created response generation `1` with `timelineItemCount=25`, `toolCount=25`.
5. Manual-Sync re-arm loaded the covered target page. At `14:44:37Z`, `coveredExecutor.focusActivationAttempt` reported `nativeFirstResponder=true`; a page `focus` event immediately reported `hasFocus=true`; `coveredExecutor.focusActivationResult` reported `documentHasFocus=true`, evaluation succeeded.
6. From focus acquisition at `14:44:37Z` until the user's second Sync at `14:46:00Z` (~83 seconds), there were zero matching `externalStreamStatusRequest/Response`, `externalResumeRequest`, `resumeResponse`, `externalStreamingObserved` or `externalSnapshot` events. User-socket frames remained `targetMatch=false`.
7. A memory warning at `14:44:47Z` did not evict the protected resident; no WebContent-process termination was recorded.
8. The later explicit Sync at `14:46:00Z` returned at `14:46:02Z` with visible messages `10 -> 11`, mapping `465`, trailing timeline/tools `0`, proving the final assistant had materialized by then. Existing `externalDetailReconciled(reason=authoritative_assistant_materialized)` correctly cleared the live row.

### Runtime classification

- b88 first-responder activation mechanism: **Runtime Positive**.
- covered `document.hasFocus=true`: **Runtime Positive**.
- automatic page-owned continuation after focus: **Not observed in this run**.
- automatic final convergence: **Rejected in this run**; final required another explicit Sync.
- focus causality: **Inconclusive**, because the user reports the conversation was already at the final tool call and the last authoritative proof of active generation (`14:44:36Z`) preceded actual focus acquisition (`14:44:37Z`) by only about one second. The response may have completed in that narrow interval, so this sample is not clean enough to reject focus as sufficient.
- router-entry causality: **Unverified**; do not infer it from this near-terminal sample alone.

## Next exact Runtime action — reuse exact b88

Do **not** allocate b89 and do not change product code yet.

Repeat exact canonical b88 with a remote response that is clearly early or mid-generation:

1. Start a deliberately long response on another official client.
2. Enter/select the target conversation while it is clearly still reasoning or several tools away from completion.
3. Press `同步最新消息` exactly once.
4. Keep ChatGPTClient foregrounded for at least 30–60 seconds without a second Sync, ideally while the remote side visibly continues advancing.
5. Export diagnostics before manually syncing again if possible.

A decisive focus-negative sample requires both:

- `focusActivationResult documentHasFocus=true`; and
- independent evidence that the same remote generation remains active **after** focus acquisition (for example later authoritative Detail growth from a separately triggered evidence point or prolonged remote-side visible generation), while covered official page still produces zero `stream_status`/`resume`/SSE.

If that clean sample still has focus true and no official continuation, focus is rejected as sufficient and the next target becomes the genuine official SPA/router conversation-entry transition. If continuation starts, focus/activation is causal.

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

## Batch recovery point — b88 Runtime docs

Known baseline before this chain: feature head `f8d536e71c72174e719d17693934997d88686c04`; b88 product/package identities above remain immutable.

Intended docs-only batches:

1. this checkpoint with exact Runtime classification — **current write**;
2. durable b88 Runtime evidence plus pending visible-Web A/B docs recovery;
3. `BUILD_TEST_INDEX.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `WEB_SEND_ADAPTER.md`;
4. PR #29 title/body metadata sync.

Do not touch b88 product source, Xcode build/Candidate identity, canonical Artifact/IPA identity, or allocate b89 during recovery.

## Session round counter

This user turn is **round 27**.
