# DEV-send-stream b88 focus-positive near-terminal Runtime — 2026-09-02

## Identity

- Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- Exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- Clean package head / diagnostics source: `378811691ccbd6f44b232d8cc5564628e9b021e1` / `378811691ccb`
- Canonical Artifact: `9848999246`
- IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- Device: iPhone / iOS17.0
- Uploaded diagnostics: `ChatGPTClient-Diagnostics-20260902-144605.json`

## Runtime timeline

- Selection covered page loaded visible/complete on the target conversation but initially had `document.hasFocus=false`.
- `14:44:25Z` authoritative Detail: visible `10`, mapping `450`, trailing timeline/tools `24/24`.
- Explicit Sync returned at `14:44:36Z`: visible still `10`, mapping `452`, trailing timeline/tools `25/25`. The remote turn had advanced one additional tool and no final assistant had materialized at that authoritative fetch.
- Existing Detail projection started response generation `1` with `25` timeline/tool items.
- Manual-Sync re-arm completed at `14:44:37Z`; `WKWebView.becomeFirstResponder()` returned true, page emitted a focus event with `hasFocus=true`, and direct evaluation returned `documentHasFocus=true`.
- From focus acquisition until the user's second explicit Sync at `14:46:00Z` (~83 seconds), no matching `stream_status`, `/resume`, resume response, external streaming or external snapshot event appeared. User-socket messages remained `targetMatch=false`.
- A memory warning did not evict the protected resident and no WebContent-process termination was recorded.
- Second explicit Sync returned at `14:46:02Z`: visible messages `10 -> 11`, mapping `465`, trailing timeline/tools `0/0`; `externalDetailReconciled(reason=authoritative_assistant_materialized)` correctly cleared the live row.

## Classification

- First-responder activation mechanism: **Runtime Positive**.
- Covered `document.hasFocus=true`: **Runtime Positive**.
- Automatic page-owned continuation after focus: **Not observed in this run**.
- Automatic final convergence: **Rejected in this run**; final materialization required another explicit Sync.
- Focus causality: **Inconclusive**, not Rejected. The user reports entering at the final tool call, and the last authoritative proof of active generation at `14:44:36Z` preceded actual focus acquisition at `14:44:37Z` by only about one second. The response may have completed in that narrow interval, so this sample cannot prove that focus is insufficient.
- SPA/router causality: **Unverified**.

## Next gate

Reuse the exact canonical b88 IPA. Start a deliberately long remote response and enter while it is clearly early or mid-generation. Press Sync once, keep ChatGPTClient foregrounded for 30–60 seconds without another Sync, then export diagnostics. Do not allocate b89 or change product code until that clean focus A/B is collected.
