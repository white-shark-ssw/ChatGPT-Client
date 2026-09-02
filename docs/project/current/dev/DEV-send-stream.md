# DEV-send-stream

## Status

**Active — exact b88 real-device Runtime now cleanly rejects focus as a sufficient condition for covered official-Web cross-platform continuation. The focus mechanism itself remains Runtime Positive (`nativeFirstResponder=true`, `document.hasFocus=true`), but a second early/mid-generation sample stayed stale while the user directly observed multiple additional PC tool rounds after focus. No covered `stream_status`, `/resume`, external SSE or page-owned snapshot appeared, and the completed assistant still required a final explicit Sync. Next evidence target is genuine official SPA/router conversation-entry behavior; router causality remains Unverified. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged; metadata synced to decisive b88 focus-negative state
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Durable decisive b88 Runtime docs head before this checkpoint close: `31bf478917697a6228cf5deded4f4fd5277962e9`
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

Web Rule Lab on the same `WKWebsiteDataStore.default()` authority visibly entered a newly active cross-platform conversation and immediately showed live continuation plus the active Stop control while `document.hasFocus=true`. The coarse probe returned `route=other` despite visibly being inside the active conversation, so route shape is diagnostic-only.

Exact b87 covered production was visible/loaded/attached but `document.hasFocus=false` and produced no continuation. b88 therefore isolated focus first; the first b88 sample proved the focus mechanism works but was near-terminal and inconclusive.

Durable visible-Web evidence: `docs/project/runtime-evidence/DEV-send-stream-visible-web-focus-sse-ab-20260902.md`.

## b88 implementation boundary

b88 changes only explicit manual-Sync rearm focus activation after the existing programmatic target page load:

- `WKWebView.becomeFirstResponder()` once after re-armed load;
- direct `document.hasFocus()` probe;
- existing programmatic `/c/<conversation>` load unchanged;
- Web interaction remains disabled;
- no Native `stream_status`, `/resume`, offset, polling, timers, retries, watchdogs, duplicate Send, router workaround, WebSocket-body authority or second response store.

## First b88 Runtime sample — near-terminal / inconclusive

`ChatGPTClient-Diagnostics-20260902-144605.json` proved `nativeFirstResponder=true` and `document.hasFocus=true`, but the last authoritative ACTIVE Detail was only ~1 second before focus and the user reported the turn was already on its final tool call. No continuation followed and final required explicit Sync, but focus sufficiency could not yet be rejected from that sample alone.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md`.

## Second b88 Runtime sample — decisive focus-negative

Uploaded diagnostics:

- `ChatGPTClient-Diagnostics-20260902-150016.json` — mid-run before final manual Sync.
- `ChatGPTClient-Diagnostics-20260902-150109.json` — after final manual Sync materialized the completed assistant.

Exact package metadata again matches canonical b88: Release `0.1.0 (88)`, Candidate `DEV-send-stream-0.1.0-b88`, source `378811691ccb`, iPhone / iOS17.0.

Target conversation hash: `sha256:38ede68b30d8`.

### Timeline

1. `14:58:06Z` initial authoritative Detail: visible `12`, mapping `479`, trailing timeline/tools `5/5`.
2. Explicit Sync at `14:58:14Z`; Detail returned `14:58:16Z`: visible still `12`, mapping `481`, trailing timeline/tools `6/6`. Existing authoritative-Detail projection started response generation `1` with six tool items.
3. Manual-Sync rearm succeeded: `14:58:17Z nativeFirstResponder=true`; `14:58:18Z documentHasFocus=true`, page visible/complete.
4. From focus acquisition until first background at `14:59:10Z`, covered Web had about **52 seconds clean foreground with focus true**. No matching `externalStreamStatusRequest/Response`, `externalResumeRequest`, resume response, `externalStreamingObserved` or `externalSnapshot` occurred.
5. The user directly observed on PC that the same remote response produced **multiple additional tool rounds after focus acquisition**, while ChatGPTClient remained on the six-tool authoritative snapshot and did not continue. This supplies the independent post-focus ACTIVE/progress evidence missing from the first sample.
6. User-socket frames remained structural-only with `targetMatch=false`; no automatic acquisition trigger fired.
7. Mid-run export at `15:00:16Z` still contained no page-owned continuation/SSE events. Returning to the target conversation restored the resident live row rather than newer remote blocks; no authoritative Detail refresh had occurred.
8. Final explicit Sync at `15:01:04Z` returned `15:01:06Z` with visible `12 -> 13`, mapping `507`, trailing timeline/tools `0/0`; `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)` cleared response generation `1` and exposed the completed assistant.
9. The final rearm again produced `nativeFirstResponder=true` / `documentHasFocus=true` at `15:01:07Z`, after final materialization; it was not the completion acquisition source.

### Runtime classification

- b88 first-responder activation mechanism: **Runtime Positive**.
- covered `document.hasFocus=true`: **Runtime Positive**.
- focus as a sufficient condition for official cross-platform continuation: **Rejected**.
- page-owned continuation after focus: **Rejected in the decisive sample**.
- automatic final convergence: **Rejected again**; completed assistant required final explicit Sync.
- genuine official SPA/router conversation-entry transition: **next evidence target / causality Unverified**.
- visible official Web server capability: still **Runtime Positive**.

Important wording: this does **not** prove focus is irrelevant or unnecessary in every Web path. It proves focus alone, with the current programmatic full conversation load, is not sufficient.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b88-focus-sufficient-rejected-20260902.md`.

## Next exact action

Do not change protocol ownership and do not guess `/resume` offsets. Focus has completed its causal A/B.

Next investigate the remaining known-good differential: **genuine official SPA/router conversation entry** versus the covered executor's programmatic full `/c/<id>` load. Before product code, establish the smallest privacy-safe evidence needed to distinguish the official user-driven SPA transition from direct full navigation. Do not combine router investigation with polling, timers, retries, Native protocol synthesis, WebSocket body authority or a second response store.

A future b89 may be allocated only after the router-entry experiment has one exact evidence-backed variable to test. Do not reuse b88 for a different product behavior.

## Durable docs / PR sync completed this round

- Decisive Runtime checkpoint classification: committed.
- Durable evidence `DEV-send-stream-b88-focus-sufficient-rejected-20260902.md`: committed.
- `BUILD_TEST_INDEX.md`: b88 upgraded from focus-Inconclusive to focus-alone Rejected as sufficient.
- `MODULE_STATUS.md`: decisive b88 focus-negative override added.
- `TECHNICAL_DECISIONS.md`: decisive b88 qualification added.
- `WEB_SEND_ADAPTER.md`: focus-alone continuation qualification added.
- Docs-only sync workflow `33649704051 / 100313298289`: passed and pushed durable docs at `31bf478917697a6228cf5deded4f4fd5277962e9`.
- PR #29 title/body synced to `DEV-send-stream: b88 focus alone rejected — SPA/router entry evidence next`; PR remains open / mergeable / unmerged.
- b88 product source/package/Artifact identities were not changed.

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

## Session round counter

This user turn is **round 28**.
