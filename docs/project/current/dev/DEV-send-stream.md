# DEV-send-stream

## Status

**Active — visible official Web A/B is Runtime Positive: a newly active cross-platform conversation immediately continued live and showed active Stop state while `document.hasFocus=true`. b88 focus-only causal A/B is Code/CI/Artifact/package verified; real-device Runtime remains Pending. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged before final PR metadata sync
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
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

**Causality is not yet proven.** A genuine user-driven SPA/router entry transition also occurred in the known-good sample.

## b88 implementation — focus-only causal A/B

Exact product source `31d24e8b9ab4676effd757a793162abbdb0d7012` changes only `ChatGPTClient/RootViewController.swift` plus build/Candidate identity in `project.pbxproj`.

Behavior:

1. Existing programmatic `observeExistingConversation` conversation URL load is unchanged.
2. Only explicit manual-Sync re-arm sets a one-shot `manualSyncFocusProbePending` flag.
3. After that target page finishes loading, covered `WKWebView` calls `becomeFirstResponder()` once.
4. The WebView remains `isUserInteractionEnabled=false`; b88 does not make it a visible/interactable product surface.
5. Logs `coveredExecutor.focusActivationAttempt` with Native result and `coveredExecutor.focusActivationResult` with direct `document.hasFocus()` result.
6. Pending focus probe is cleared on local Send, account reset, navigation failure and WebContent process termination.
7. No `stream_status`, `/resume`, offset, WebSocket body, polling, timer, retry, watchdog, duplicate Send, second response store or router workaround is added.
8. Client-owned protected-Send transport and Repository ownership remain unchanged.

Guarded staging run `33636270267` passed exact two-file product patch + `git diff --check`. Earlier staging run `33635988823` is intentionally non-product: the patch/checks passed but GitHub Actions correctly refused a workflow-file update without workflows permission; feature branch was unchanged by that failed push. Workflow identity was then updated separately through GitHub Contents API.

## Validation state

- Code written: **Yes**
- Exact guarded staging / `git diff --check`: **Passed**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced: **Yes**
- Canonical feature-head package metadata / IPA SHA / arm64 / iOS14 minimum: **Verified**
- Runtime/manual/real-device b88: **Pending**
- Stable/Frozen Send: **No**

## b88 Runtime decision gate

During another-platform long response:

1. Keep the target conversation selected in ChatGPTClient.
2. Press `同步最新消息` exactly once while response is still clearly active.
3. Keep ChatGPTClient foregrounded and do not press a second Sync before evidence is collected.
4. Export diagnostics after enough time for the remote reasoning/tool response to advance or finish.

Primary diagnostics:

- `coveredExecutor.focusActivationAttempt`
- `coveredExecutor.focusActivationResult`
- existing `coveredExecutor.pageActivation`
- `coveredExecutor.externalStreamStatusRequest/Response`
- `coveredExecutor.externalResumeRequest`
- `coveredExecutor.resumeResponse`
- `coveredExecutor.externalStreamingObserved`
- `coveredExecutor.externalSnapshot`

Interpretation:

- Native activation succeeds -> `document.hasFocus=true` -> page starts official continuation traffic/SSE: focus/activation is causal for this path.
- Native activation succeeds -> `document.hasFocus=true` but still zero continuation traffic: focus is rejected as sufficient; genuine SPA/router conversation-entry transition becomes the next evidence target.
- Native activation fails or `document.hasFocus` remains false: b88 is inconclusive for focus causality; do not infer router causality from that alone.

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

## Next exact action

Install exact canonical b88 IPA and run the single-Sync real-device gate above. Do not allocate b89 or add router/interactivity work until b88 Runtime shows whether first-responder activation actually changes `document.hasFocus` and official page continuation behavior.

## Session round counter

This user turn is **round 26**.
