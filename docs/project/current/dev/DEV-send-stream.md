# DEV-send-stream

## Status

**Active — exact b66 production existing-conversation bridge failed focused iPhone/iOS17 Runtime after the real protected Send was observed. The official service completed the answer, but Native emitted `send_transport_error` before receiving an HTTP Response object. Exact evidence isolates a duplicate Swift→JS submit race: one response generation produced `composer_ready x2` and `submit_result=submitted x2` before one `send_observed`. b67 is now the next correction Candidate. Stable/Frozen Send remains No. PR #29 remains open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — keep open / evidence-only / unmerged
- Current actual `main` last verified in this session: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Stable merged predecessor: b38
- Latest probe Runtime pass: b65
- Latest production Candidate: b66 — Runtime failed
- b39-b66 emitted identities are permanently reserved.
- Future serialized `DEV-composer-parity` owns final Composer UI; this Work keeps only a validation text trigger.

## Exact b66 identity / evidence

- Candidate: `DEV-send-stream-0.1.0-b66`
- Version / Build: `0.1.0 (66)`
- Exact product/config source: `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`
- Product tree: `31ef29457273a44dd202a63a96560563154e8823`
- Push Run / Job: `33337771534 / 99327694040` — success
- PR Run / Job: `33337774136 / 99327701256` — success
- Push Artifact: `9739572172`
- Artifact ZIP digest: `sha256:6c6d8e165ed070e88a27abafc57973dc847937826e40c552bf9f0d29bb91bb45`
- IPA SHA: `7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`
- Runtime export: `ChatGPTClient-Diagnostics-20260830-220515.json`
- Detailed Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b66-runtime.md`

b66 package identity is valid and therefore permanently reserved. CI/Artifact success did not prove Runtime; exact-device Runtime rejected the first production bridge.

## b66 Runtime failure

Two response generations reproduced the same shape:

`liveResponse.started -> coveredExecutor.requested -> page loaded -> composer_ready x2 -> submit_result=submitted x2 -> send_observed -> composer_ready -> send_transport_error -> liveResponse.failed`

Important facts:

1. user verified the official ChatGPT app already contained the assistant reply, so protected Send reached the service;
2. no `coveredExecutor.sendResponse` event occurred; failure is before the wrapper receives an HTTP Response, not in SSE parser text classification;
3. Native reasoning/final/tool characters remained zero;
4. generation 1 failed while foreground; generation 2 also failed after a short resign-active interval, so backgrounding is not required for reproduction;
5. a memory warning occurred after generation 1 had already failed and Repository logged `resident.evictionSkipped`, so it is not the trigger.

## Accepted diagnosis

b66 `pendingSend` remains populated until later `send_observed`. `composer_state` immediately calls `submitPendingSendIfReady()`. JavaScript evaluation is asynchronous, so two ready messages can arrive before the first evaluated `submit()` sets JS `activeSend`; Swift therefore schedules the same pending text twice. Runtime proves that exact race with duplicate ready + duplicate submitted events.

This duplicate production-orchestration race was not present in the manually triggered b65 probe path. A server-accepted first request plus subsequent page-side request cancellation/rejection is consistent with the user seeing a completed official reply while Native reports `send_transport_error`.

## b67 minimal correction

Only change the executor operation gate:

1. `isBusy` uses the already-existing `activeEvents != nil` lifetime, which spans request through terminal/failure.
2. `submitPendingSendIfReady()` consumes/clears `pendingSend` immediately before issuing the one `evaluateJavaScript(submit(...))` call.
3. Later duplicate composer-ready messages therefore cannot schedule another submit for the same operation.
4. `activeEvents` keeps the executor busy until real terminal/failure, so clearing `pendingSend` does not open a second user Send window.
5. Preserve b66 Web selectors, exact-target navigation, one page-owned protected Send, same-response fetch interception, SSE parser/filtering, Repository response owner, Web Rule Lab and privacy diagnostics unchanged.
6. No retry, resend, polling, timer, watchdog, fallback, compatibility shim or second state owner.

## TD-029 production authority retained

`Native send action -> ConversationRepository response operation -> covered official Web verified composer/page-owned protected Send -> same-response SSE -> Repository incremental response state -> Native consumers`.

- official page owns browser challenge + protected request execution;
- `ConversationRepository` is sole production conversation/response owner;
- `AuthSessionStore` remains auth/account owner;
- `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority;
- full Web conversation rendering remains rejected;
- Sync/Reload never resend;
- `WEB_SEND_ADAPTER.md` remains the Web-rule maintenance authority;
- `assistant:thoughts` remains non-presentational.

## Tooling notes

`tmp-b66-assembly-20260831` is tooling-only and has no Work/Candidate/Artifact authority. Historical accidental empty-file create/delete commits are tooling-only and never product authority; do not replay them.

## Batch recovery point — b67

Current formal branch after this checkpoint must be re-fetched before product writes.

Next coherent write chain:

1. create one tooling-only `tmp-b67-assembly-20260831` branch from the new formal docs/checkpoint head;
2. modify only `ChatGPTClient/RootViewController.swift` for the two-line semantic correction above;
3. set Xcode Debug+Release `CURRENT_PROJECT_VERSION=67` and `DIAGNOSTICS_CANDIDATE=DEV-send-stream-0.1.0-b67`;
4. set workflow Candidate/Artifact name to b67;
5. compare-audit assembly against the formal docs head: expected exactly Root + pbxproj + workflow;
6. re-check real `main`, PR and candidate conflicts;
7. move formal branch once to the exact coherent b67 commit/tree;
8. continue autonomously through Push+PR CI, Artifact download and independent package identity verification;
9. update `BUILD_TEST_INDEX.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md`, `PROJECT_SPECIFIC_RULES.md`, this checkpoint and PR #29 in the same cycle;
10. stop only at exact iPhone/iOS17 b67 Runtime gate.

Do not touch final Composer, attachments, b38 conversation geometry, auth ownership/default WebKit store, parser grammar or b39-b66 identities.