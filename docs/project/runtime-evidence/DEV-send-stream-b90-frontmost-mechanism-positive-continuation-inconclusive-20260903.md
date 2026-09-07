# DEV-send-stream b90 — Frontmost mechanism Positive / continuation Inconclusive — 2026-09-03

## Exact tested identity

- Candidate: `DEV-send-stream-0.1.0-b90`
- Version / Build: `0.1.0 (90)`
- Exact product commit: `5e9d735ddb2f7a2c46dbc43de2525980c86a1c1e`
- Exact product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`
- Canonical Push Artifact: `9882770072`
- IPA SHA-256: `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`
- Runtime: iPhone / iOS17.0 / Release.

## Auth/list prerequisite recovered

The earlier same-day b90 sample that failed `/api/auth/session` with `NSURLErrorDomain -1005` was transient. In this exact sample:

- `08:16:00Z` `accountContextProbe.session` returned HTTP200;
- accounts-check returned HTTP200 and verified Plus/personal context by `08:16:02Z`;
- `08:16:03Z` conversation list returned HTTP200, page items `28`, authoritative total `29`;
- a later relaunch repeated `/api/auth/session` HTTP200 at `08:21:21Z` and list HTTP200 at `08:21:23Z`.

No auth/list product correction is justified by this evidence.

## Manual authoritative acquisition

At `08:16:47Z` the user triggered one explicit Sync. At `08:16:55Z` authoritative Detail returned HTTP200 with:

- visible messages `20 -> 21`;
- mapping count `1035`;
- trailing timeline `2`;
- trailing reasoning `1`;
- trailing tools `1`.

`ConversationRepository` started external response generation 1 from this authoritative Detail and projected the available reasoning/tool snapshot.

## b90 frontmost A/B mechanism

Immediately after the successful Sync:

- before raise: `subviewIndex=0`, `visibleSiblingCountAbove=1`;
- `stage=manual_sync_frontmost_ab`: `subviewIndex=1`, `visibleSiblingCountAbove=0`;
- bounds were non-empty and intersected the key window;
- `userInteractionEnabled=true`;
- the target page loaded to `readyState=complete`, route `conversation`, `visibilityState=visible`;
- at `08:16:57Z`, `nativeFirstResponder=true` and `documentHasFocus=true`.

This proves the b90 frontmost-presentation mechanism executes correctly on the real device. **Mechanism Runtime Positive.** The user's observation that the frontmost official Web looked normal is consistent with this result.

## Continuation result

The log after frontmost activation contains:

- zero matching `coveredExecutor.externalStreamStatusRequest/Response`;
- zero matching `coveredExecutor.externalResumeRequest/Response`;
- zero `coveredExecutor.externalStreamingObserved`;
- zero page-owned external snapshot;
- only structural user-WebSocket activity with `targetMatch=false`.

The app began resigning active at `08:17:10Z`, about 13 seconds after focus success, and entered background at `08:17:11Z`. There is no later explicit Detail Sync in this sample proving how much the same remote response advanced after frontmost activation.

Therefore this sample **cannot yet reject or accept frontmost/occlusion as sufficient for automatic continuation**. It proves visibility/z-order/focus execution, but not page-owned continuation causality.

## Qualification / next gate

- Auth/list prerequisite: **Recovered / Runtime Positive**.
- Manual authoritative Detail projection: **Runtime Positive**.
- Frontmost z-order mechanism: **Runtime Positive**.
- Page-owned automatic continuation after frontmost: **Inconclusive**.
- Stable/Frozen Send: **No**.

Reuse exact b90. Do not allocate b91 or change product code. Next test must keep ChatGPTClient continuously foregrounded 30–60 seconds after frontmost activation while the other official client demonstrably continues the same long response. Export diagnostics before a second Sync; if Native still does not advance, a later second Sync may then establish authoritative remote progression without contaminating the first observation window.
