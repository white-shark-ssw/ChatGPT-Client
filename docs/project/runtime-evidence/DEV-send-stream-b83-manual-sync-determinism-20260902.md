# DEV-send-stream b83 manual Sync determinism — 2026-09-02

## Candidate

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b83`
- Version / Build: `0.1.0 (83)`
- Exact product/config source: `12e3c27138ebc81cbbae6236347122f79e03bf08`
- Clean CI/package head: `3771ddccc8d0847ce28f72acbbe311aaf30b7482`
- PR: #29

## User Runtime evidence that triggered b83

The latest user result for b82 is that explicit manual `同步最新消息` sometimes fails to acquire the active cross-platform reasoning stream. This rejects b82 for the final manual-sync MVP stability gate.

The accepted MVP boundary remains:

- client-owned Send keeps the existing true SSE stream;
- cross-platform responses may be genuine block/page-snapshot progressive reasoning/tool updates;
- explicit manual Sync must be reliable;
- automatic remote-turn discovery, cross-platform token-level SSE parity and progressive external final-token streaming are deferred.

## Source-backed defect

Before b83, the successful manual-Sync callback reached the covered-page force-rearm path only when `latestUserChanged == true`.

That made this state unrecoverable by a second explicit Sync:

1. the latest remote user message is already present locally;
2. Repository has no active external live response because the reasoning path was not acquired;
3. user explicitly presses Sync;
4. authoritative Detail succeeds but latest user ID is unchanged;
5. b82 skips the force reload/re-arm;
6. the active external reasoning path remains unattached.

This directly matches the reported intermittent behavior and is narrower than the accepted explicit-recovery contract.

## b83 minimal correction

Exact product diff in `12e3c27138ebc81cbbae6236347122f79e03bf08`:

- `RootViewController` no longer requires `latestUserChanged` in `onManualLatestSyncApplied` before a force re-arm;
- the re-arm still requires the same conversation to remain selected and Repository to have no active live response;
- the action remains one bounded force reload caused by the user's explicit successful Sync;
- Debug and Release build identity moved from b82/build82 to b83/build83.

No automatic acquisition logic, client-owned SSE, response ownership, polling, timer, retry loop, watchdog, duplicate Send, fake stream or WebSocket body authority was changed.

## CI / Artifact evidence

Clean normal workflow head: `3771ddccc8d0847ce28f72acbbe311aaf30b7482`.

- Push workflow run: `33556857625` — **success**
- Push job: `100019684027` — build / inspect / upload all **success**
- PR workflow run: `33556862137` — **success**
- Artifact ID: `9819681774`
- Artifact name: `ChatGPTClient-DEV-send-stream-0.1.0-b83`
- Artifact ZIP digest: `sha256:b76c71493b01c88c6dfc60f9ef886e9e1c862d15a6e93ee00794ae6740a42682`
- IPA: `ChatGPTClient-0.1.0-b83-dev-send-stream.ipa`
- IPA SHA-256: `46f06106c3d47b3845a584665666fb6cb6d39cd66c0c9415412702e81795be97`

Local extraction of the downloaded Artifact verified:

- `CFBundleShortVersionString = 0.1.0`
- `CFBundleVersion = 83`
- `DiagnosticsCandidate = DEV-send-stream-0.1.0-b83`
- `DiagnosticsSourceCommit = 3771ddccc8d0`
- `MinimumOSVersion = 14.0`
- executable is Mach-O arm64.

The clean CI head differs from the exact product/config source only by the finalized normal b83 workflow definition; the product/config change itself is the two-file commit above.

## Evidence classification

- User b82 manual-Sync stability: **Runtime Rejected**
- b83 root cause: **Source-backed**
- b83 code written: **Yes**
- b83 build/candidate identity: **Verified**
- b83 Push CI: **Passed**
- b83 PR CI: **Passed**
- b83 Artifact produced/package identity: **Verified**
- b83 real-device manual-Sync stability: **Pending Human Runtime**
- Stable/Frozen Send: **No**

## Human Runtime gate

Use b83 for repeated active cross-platform turns.

For each test:

1. keep/select the target conversation;
2. start a sufficiently long response from another platform;
3. while reasoning is active, press Sync once;
4. verify the newest available remote state appears;
5. verify a reasoning/tool block is acquired;
6. do not press Sync again and verify at least one later genuine reasoning/tool block arrives while the response remains active;
7. verify final completion converges correctly.

At least one reproduction must cover the specific b83 edge case: the remote user message is already visible locally before pressing Sync, but no reasoning stream is active. Pressing Sync must still force one re-arm and acquire the active reasoning path.

Passing CI or producing the IPA does not prove this Runtime requirement.