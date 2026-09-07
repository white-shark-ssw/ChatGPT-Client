# DEV-send-stream b90 — Runtime blocked before frontmost A/B — 2026-09-03

## Exact tested identity

- Candidate: `DEV-send-stream-0.1.0-b90`
- Version / Build: `0.1.0 (90)`
- Exact product commit: `5e9d735ddb2f7a2c46dbc43de2525980c86a1c1e`
- Exact product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`
- Canonical Push Artifact: `9882770072`
- IPA SHA-256: `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`
- Runtime metadata exported from the device: Release, iPhone, iOS 17.0, source marker `99f1aa15ce49`.

## User-visible result

The user reported that the conversation list kept failing to refresh, preventing the intended b90 cross-platform continuation test from reaching the target conversation / manual-Sync frontmost A/B.

## Diagnostic sequence

The exported diagnostics show that this run failed in the Native auth prerequisite before any real conversation-list request or covered-Web A/B occurred:

1. At `07:39:28Z` the default WebKit data-store warmup began. It completed successfully at `07:39:29Z`, changing from `0` cookies / `0` matched auth cookies before warmup to `42` cookies / `24` matched auth cookies after warmup, with `7` website-data records.
2. Automatic list load generation 1 began at `07:39:29Z`. The provisional durable list cache loaded successfully with `29` entries (`ageSeconds=1888.03`).
3. `accountContextProbe` then started with `42` cookies / `24` matched auth cookies, but at `07:39:34Z` `/api/auth/session` failed with `NSURLErrorDomain` code `-1005`. The account probe ended `failed` after about `5049 ms`.
4. Because this was an automatic load and a provisional cache existed, `ConversationRepository` selected `offline_cache` and completed generation 1 from the existing 29-entry cache with `auth=temporarily_unavailable`.
5. The user then requested a manual list refresh at `07:39:37Z`. Manual generation 2 again started `accountContextProbe` with `42` cookies / `24` matched auth cookies and again failed at `07:39:42Z` with `NSURLErrorDomain -1005` after about `5036 ms`.
6. Manual generation 2 ended `status=failed`, `stage=auth`. No `conversation list` network request was emitted after the failed probe.
7. The earlier pre-relaunch portion of the same export shows the same pattern at `07:39:09Z`, `07:39:17Z` and `07:39:25Z`: repeated `accountContextProbe.sessionFailed` with `NSURLErrorDomain -1005`; manual list loads ended at `stage=auth`.

## Qualification

This run does **not** test the b90 frontmost / z-order hypothesis:

- no target conversation was successfully entered through a fresh authenticated list flow;
- no explicit target-conversation `同步最新消息` reached the covered executor;
- no `coveredExecutor.webViewActivation stage=manual_sync_frontmost_ab` event exists;
- no `visibleSiblingCountAbove=0` frontmost proof exists;
- no matching page-owned `stream_status`, `/resume`, snapshot or SSE continuation opportunity was reached.

Therefore b90 is **Runtime Inconclusive / prerequisite blocked**, not Runtime Positive and not Runtime Rejected for the frontmost hypothesis.

## Source correlation / decision

The exact b90 product change is the already-recorded `RootViewController` frontmost diagnostic A/B plus Build/Candidate 89 -> 90. The auth/list path is not part of the b90 product delta. The current failure is a Native auth transport prerequisite failure observed at `/api/auth/session`, not evidence that the b90 frontmost change broke conversation-list parsing or that the z-order hypothesis failed.

Do not add automatic retry, fallback, timer, watchdog or a second auth authority from this sample. Do not allocate b91. Reuse the exact b90 package after the normal auth/list prerequisite succeeds, then execute the existing frontmost A/B Human Runtime gate unchanged.
