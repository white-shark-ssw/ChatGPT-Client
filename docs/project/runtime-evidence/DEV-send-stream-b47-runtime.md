# DEV-send-stream b47 Runtime Evidence

_Date: 2026-08-29_

## Exact Candidate identity

- Candidate: `DEV-send-stream-0.1.0-b47`
- Version/build: `0.1.0 (47)`
- Exact product/config source: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`
- Runtime device metadata: iPhone / iOS17.0 / Release
- Legitimate Artifact: `9716878034`
- Artifact ZIP digest: `sha256:a6915d0a2c48877e8d4d5b7eea966118ad84b321bc1462dafe55c593796e10fc`
- IPA SHA-256: `49d1bd4886310f7761883784f73fc5532fe1a9532773619f0796cd7aab816909`

The uploaded diagnostics metadata exactly matched the Candidate/source above.

## Test-scope caveat

The intended older long conversation could not be used for this run. The user reported that the conversation contained only about three rounds of long answers, but the mobile Web surface became unusably slow: attempting to bring up/use the Web composer repeatedly froze the page. The user therefore completed the protocol test using a new conversation.

This direct exact-device usability result is accepted as a new product-architecture risk. The diagnostics file does not contain the failed long-conversation attempt itself, so it does **not** establish the internal freeze cause (Web page rendering, WKWebView process behavior, instrumentation overhead, memory pressure, or another owner remains Unverified). It does establish that a product architecture which requires the user to enter the real full Web conversation before every protected Send can fail before Send initiation on a realistic long-conversation workload.

## b47 protocol sequence

- `15:29:35Z`: official Web Send observed.
- After an active-response network/background interruption, official Web opened `POST /backend-api/f/conversation/resume` with a valid body and `offset=23`.
- First official offset-23 resume attempt hit a transport error while connectivity was unavailable.
- The immediately repeated official offset-23 resume request returned HTTP200 `text/event-stream` at `15:30:25Z`.
- b47 then issued exactly one Native parity request using the same in-memory conversation identity + offset 23.
- Transient account/session verification succeeded: `/api/auth/session` and accounts-check both returned HTTP200 for the recorded Plus/personal account context.
- Native request context intentionally contained only explicit `Accept` + `Content-Type`, plus the existing transient bearer injection and WebKit-derived ephemeral cookies. No browser header values were copied.
- Native `/resume` returned HTTP404 `application/json` after about 707 ms, 116 response bytes, 0 SSE frames.
- Rejection body structure was only `{"detail":{"code":"string","message":"string"}}`; response text was not recorded.
- Later, after another background interval, official Web opened `/resume` again at progressed `offset=74` and received HTTP200 `text/event-stream`.
- No second Native parity attempt occurred.

## Official vs Native request-header structure

The successful official resume request exposed these header names:

`accept, authorization, content-type, oai-client-build-number, oai-client-version, oai-device-id, oai-echo-logs, oai-language, oai-session-id, x-conduit-token, x-oai-is-client-observation, x-oai-is-pending-updates, x-oai-turn-trace-id, x-openai-target-path, x-openai-target-route`

The Native request explicitly set only:

`accept, content-type`

with existing transient Authorization injection + WebKit-derived ephemeral cookies.

This establishes a **large structural request-context difference**, but not which header(s), if any, are required. b47 does not authorize copying those browser values.

## Response-header observations

Official HTTP200 SSE responses included response-header names such as `x-oai-is-receipt`, `x-oai-is-update`, `x-oai-request-id`, `retry-after`, CORS headers and normal CDN/server headers.

The Native HTTP404 JSON response still included `x-build`, `x-oai-is-update`, `x-oai-request-id`, CDN/server headers and `set-cookie`, but not the successful official response's `x-oai-is-receipt` / CORS / `retry-after` set.

This proves only that Native reached a different response class. It does not distinguish missing browser context from cursor/consumer ownership.

## b47 diagnostics defect

The intended safe error-code field was exported as `<redacted>` because its field name was `safeErrorTokens`. Current `DiagnosticsSanitizer.secretFragments` redacts every key containing `token`, so the safe code/type/status values were lost before export.

This is a deterministic diagnostic naming defect. Correcting it would require a new Candidate because b47 Artifact identity is already emitted/reserved. It does not affect the accepted HTTP404/body-shape/header-name evidence above.

## Accepted conclusions

1. Official Web no-resend resume remains **Runtime Confirmed**.
2. Native Cookie+Bearer-only duplicated resume remains **Runtime Rejected** for the b47 offset-23 attempt with the same HTTP404 JSON class as b46.
3. b47 does **not** resolve missing browser/session/route context vs second-consumer/cursor ownership.
4. Official request-header context is substantially richer than Native, but no browser header value may be copied without additional evidence.
5. The user's exact-device long-conversation result creates a new P0 product risk: **visible full Web-conversation rendering/composer availability can fail before protected Send begins.** Native post-Send handoff cannot repair a Send surface that freezes before Send.
6. Therefore further production integration of the current `full Web conversation required for every Send -> Native resume afterward` architecture should pause at an architecture viability gate rather than continue automatically into b48 header/resume experiments.

## Remaining unknowns

- Root cause of the long-conversation Web composer freeze: Unknown / Unverified.
- Whether Safari outside the app behaves materially better than the embedded WKWebView: Unknown / Unverified.
- Whether a supported official Web route can expose a lightweight send-only surface without rendering full conversation history: Unknown / Unverified.
- Required browser/client/session/route context for Native `/resume`: Unknown / Unverified.
- Native first/exclusive resume ownership: Unknown / Unverified.
- Native incremental response ownership/reasoning/follow-tail/background lifecycle: Unknown / Unverified.
