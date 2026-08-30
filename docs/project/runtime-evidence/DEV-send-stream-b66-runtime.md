# DEV-send-stream b66 Runtime Evidence

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b66`
- Version / Build: `0.1.0 (66)`
- Exact product/config source: `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`
- Product tree: `31ef29457273a44dd202a63a96560563154e8823`
- Push Run / Job: `33337771534 / 99327694040` — success
- PR Run / Job: `33337774136 / 99327701256` — success
- Push Artifact: `9739572172`
- Artifact digest: `sha256:6c6d8e165ed070e88a27abafc57973dc847937826e40c552bf9f0d29bb91bb45`
- IPA SHA: `7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`
- Primary Runtime: iPhone / iOS17.0
- Diagnostics export: `ChatGPTClient-Diagnostics-20260830-220515.json`

## User-visible result

The Native validation Send visibly submitted the message, but the live-response overlay changed to `本轮失败 / send_transport_error`. The user independently verified in the official ChatGPT app that the same conversation had already received the assistant reply. Therefore protected Send reached the service, but b66 failed to retain/consume the same-response stream in Native.

## Diagnostics result

The export matches exact build66/source `9ce228ad880e`.

Two attempted response generations reproduced the same sequence:

`liveResponse.started -> coveredExecutor.requested -> page loaded -> composer_ready x2 -> submit_result=submitted x2 -> send_observed -> composer_ready -> send_transport_error -> liveResponse.failed`

Generation 1 timestamps:

- `22:03:46` live response / covered executor requested
- `22:04:04` `composer_ready` twice
- `22:04:07` `submit_result=submitted` twice
- `22:04:07` real `send_observed`
- `22:04:08` `send_transport_error`

Generation 2 reproduced the same duplicate-ready / duplicate-submit shape before failure. A brief resign-active interval occurred during generation 2, but generation 1 failed identically while foreground, so backgrounding is not required for the defect.

No `coveredExecutor.sendResponse` event was emitted in either run. Native reasoning/final/tool character counts remained zero. This places failure before the production wrapper received an HTTP Response object; it is not an SSE text-parser failure.

A memory warning occurred after generation 1 had already failed. Repository diagnostics reported `resident.evictionSkipped` with one protected resident, so the warning is not the failure trigger and active-resident protection behaved as intended in that observation.

## Source correlation / accepted diagnosis

b66 keeps `pendingSend` until `send_observed`. `composer_state` calls `submitPendingSendIfReady()` whenever a ready composer for the current conversation is reported. Because JavaScript evaluation is asynchronous, two ready messages can arrive before the first JS submit sets page-local `activeSend`; both Swift callbacks therefore schedule `submit(...)` for the same pending operation. The exact Runtime evidence shows this occurred: two `composer_ready` events and two `submitted` results for one response generation.

This duplicate submit race is new production orchestration behavior; b65's manually triggered diagnostic submit did not have the same Swift pending-send callback race. The observed real Send can reach the server while the page-side fetch becomes rejected immediately afterward, explaining why the official app later shows the assistant reply while Native reports `send_transport_error`.

## Minimal correction boundary

For b67:

1. Consume/clear the Repository executor's `pendingSend` immediately when its one JS `submit(...)` evaluation is issued, not only after later `send_observed`.
2. Keep the whole response operation busy using the already-existing `activeEvents` lifetime, so clearing `pendingSend` does not open a second Send window before `sendObserved`.
3. Preserve all b66 selectors, official page-owned protected Send, SSE filtering/parser grammar, Repository response ownership, Web Rule Lab, diagnostics privacy and terminal reconciliation.
4. Add no retry, resend, polling, timer, watchdog, selector fallback or second response owner.

## Evidence classification

- Code/CI/Artifact/package: passed for exact b66.
- Runtime: **failed production existing-conversation response bridge**.
- Protected Send itself: reached service in the tested run, supported by user observation plus `send_observed`.
- Same-response Native stream ownership: failed before HTTP Response acceptance.
- Stable/Frozen Send: No.

b66 is permanently reserved because a valid Artifact exists. Corrected product code must use b67 or later.