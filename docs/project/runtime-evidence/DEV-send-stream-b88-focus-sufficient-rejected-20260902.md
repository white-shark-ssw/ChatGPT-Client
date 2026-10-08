# DEV-send-stream b88 focus-sufficient rejected Runtime — 2026-09-02

## Identity

- Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- Exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- Clean package head / diagnostics source: `378811691ccbd6f44b232d8cc5564628e9b021e1` / `378811691ccb`
- Canonical Artifact: `9848999246`
- IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- Device: iPhone / iOS17.0
- Mid-run diagnostics: `ChatGPTClient-Diagnostics-20260902-150016.json`
- Final diagnostics: `ChatGPTClient-Diagnostics-20260902-150109.json`
- Target conversation hash: `sha256:38ede68b30d8`

## Runtime timeline

- `14:58:06Z` initial authoritative Detail: visible `12`, mapping `479`, trailing timeline/tools `5/5`.
- Explicit Sync at `14:58:14Z`; Detail returned `14:58:16Z`: visible still `12`, mapping `481`, trailing timeline/tools `6/6`. Existing authoritative-Detail projection started external response generation `1` with six tool items.
- Manual-Sync rearm loaded the target page. `14:58:17Z` `becomeFirstResponder()` returned true; `14:58:18Z` direct probe returned `documentHasFocus=true` with the page visible and complete.
- From focus acquisition until first background at `14:59:10Z` there were about 52 seconds of clean foreground. No matching page-owned `stream_status`, `/resume`, resume response, external streaming or external snapshot event occurred.
- The user directly observed the same remote generation on PC continue through multiple additional tool rounds after focus acquisition. ChatGPTClient remained on the six-tool snapshot and did not advance. This is the independent post-focus active/progress evidence missing from the earlier near-terminal b88 sample.
- User-socket frames remained `targetMatch=false` and provided no automatic acquisition trigger.
- Mid-run export at `15:00:16Z` still had no page-owned continuation/SSE event. Returning to the target conversation restored the resident live row; no newer authoritative Detail had been fetched.
- Final explicit Sync at `15:01:04Z` returned at `15:01:06Z` with visible `12 -> 13`, mapping `507`, trailing timeline/tools `0/0`. `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)` then cleared response generation `1` and exposed the completed assistant.
- A later rearm again produced `nativeFirstResponder=true` / `documentHasFocus=true` at `15:01:07Z`, after final materialization; it was not the source of completion acquisition.

## Classification

- First-responder activation: **Runtime Positive**.
- Covered `document.hasFocus=true`: **Runtime Positive**.
- Focus as a sufficient condition for official cross-platform continuation under the current programmatic full conversation load: **Rejected**.
- Page-owned continuation in this decisive sample: **Rejected**; remote tool progress continued while covered Web emitted zero status/resume/SSE/snapshot events.
- Automatic final convergence: **Rejected again**; the completed assistant required explicit Sync.
- Genuine official SPA/router conversation-entry transition: **next evidence target / causality Unverified**.
- Visible official Web server capability remains **Runtime Positive** from the separate known-good Web Rule Lab sample.

This result does not prove focus is universally irrelevant or unnecessary. It proves focus alone is not sufficient with the current covered executor's direct full `/c/<conversation>` navigation.

## Next evidence target

Investigate the smallest privacy-safe difference between a genuine user-driven official SPA/router conversation entry and the covered executor's programmatic full navigation. Do not synthesize Native `stream_status`/`resume` requests, guess offsets, poll, add timers/retries/watchdogs, use WebSocket bodies as content authority, duplicate Send, or create a second response store.
