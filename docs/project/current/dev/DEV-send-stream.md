# DEV-send-stream

## Status

**Active — b81 automatic external acquisition is Runtime-rejected, while its target-conversation WebSocket structural trigger is Runtime-positive. The user confirmed the two b81 `targetMatch=true` frames corresponded to two separate remote Sends, so b82 implements a bounded acquisition attempt per eligible target-match event rather than a one-shot observation-cycle latch. Exact b82 is now the Human Runtime candidate. Account-wide notification remains deferred. b80 spacing and external stopped-thinking semantics remain Frozen. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29
- Actual main at b82 gate: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b82 product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- Guarded assembly attempt 2: `33534965707 / 99946924531` — success after attempt 1 compile caught a missing exhaustive event case
- Formal Push CI: `33535342383 / 99948156535` — success
- Formal PR CI: `33535347654 / 99948174293` — success
- Canonical Push Artifact: `9811406038`
- Artifact ZIP SHA-256: `bcb9c65f7cee7680580acd6238d3dd9f03f30b3c5f9024cd251b31690ac13681`
- IPA: `ChatGPTClient-0.1.0-b82-dev-send-stream.ipa`
- IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- b39-b82 permanently reserved
- b81 Runtime: automatic acquisition rejected / structural trigger positive
- b82 Runtime: Pending / Unverified
- Stable/Frozen Send: No

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b81-device-runtime-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b82-allocation-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b82-build-artifact-20260902.md`

## Corrected b81 Runtime finding

Exact b81 diagnostics show the covered `ws.chatgpt.com` socket created/open before remote activity, then two JSON-array frames with exact current-conversation `targetMatch=true` at 16:22:20Z and 16:24:24Z while Native still had no `externalStreamingObserved`, no external snapshot and no Repository external response. The user confirms two separate messages were sent remotely during this test. Therefore the two target-matching frames are correlated with two separate remote Sends/new turns rather than duplicate noise from one response.

Manual Sync later returned authoritative Detail with visible messages 4 -> 8 and four added visible messages, consistent with two new user/assistant turns. The socket event is therefore authorized as an acquisition/discovery trigger only; WebSocket content remains non-authoritative.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- explicit manual-Sync re-arm: preserve as recovery.
- b67 client-owned Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole response/content owner.
- account-wide notification/haptic discovery is deferred.
- progressive external final token streaming remains unresolved and must not be faked.

## Exact b82 product behavior

Exact product/config diff from parent `9183daa...` to source `c7a27478...` is exactly:

1. `ChatGPTClient/RootViewController.swift`
2. `ChatGPTClient.xcodeproj/project.pbxproj`
3. `.github/workflows/ios-foundation.yml`

Runtime design:

1. while observing the currently selected existing conversation, each WebSocket structural `message` with exact `targetMatch=true` may emit `.externalAcquisitionHint` only while page-owned response events have not already taken ownership;
2. Root accepts the hint only if the conversation is still selected, Repository has no active live response, no auto-acquisition Sync for that conversation is in flight, and no Detail operation is already in flight;
3. one accepted hint triggers exactly one `ConversationRepository.syncLatestMessages(id:)` operation;
4. it compares authoritative latest-user message identity before/after the Sync;
5. only when latest user changed, the conversation is still selected, no natural live response was acquired meanwhile, and the same covered executor is still current, Root performs one forced covered-page re-arm/reload;
6. no-change and failure terminate the attempt without automatic retry/reload;
7. once the attempt is finished, a later distinct target-match frame may trigger another bounded attempt, matching the two-distinct-Send b81 evidence.

No timer, polling cadence, retry/watchdog, repeated automatic loop, WebSocket body authority, Native status/body synthesis, duplicate Send, fake progressive final, account-wide notification work, or Frozen presentation change is present.

## Validation / Artifact

Guarded assembly attempt 1 `33534672784 / 99945951282` passed the exact patch/scope/static checks but Xcode correctly rejected a missing exhaustive `.externalAcquisitionHint` Repository event case. No validated product commit was produced from attempt 1 and nothing from that failed attempt entered the formal product branch.

Attempt 2 `33534965707 / 99946924531` added the missing non-authoritative event-name case, passed exact scope, `git diff --check`, prohibited-pattern checks and Xcode 16.4 Release generic iOS Simulator build. Validated tooling product commit: `71559f5a216adf49d7b14f58e159b249e658f48c`.

Formal source `c7a274786dfd175e8f476fc15c4964840e112a1d` then passed Push and PR CI. Canonical Artifact `9811406038` independently verifies:

- ZIP SHA `bcb9c65f7cee7680580acd6238d3dd9f03f30b3c5f9024cd251b31690ac13681`;
- IPA SHA `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`;
- `0.1.0 (82)`;
- Candidate `DEV-send-stream-0.1.0-b82`;
- source marker `c7a274786dfd`;
- minimum iOS 14.0;
- UIDeviceFamily `[1,2]`;
- Mach-O arm64.

CI/Artifact/package evidence does not establish Runtime success.

## b82 Human Runtime gate

1. Install the exact b82 IPA.
2. Open conversation A and leave A selected until the covered page is loaded.
3. From another platform send a sufficiently long new turn in the same A.
4. Do **not** press Sync.
5. Expected acquisition sequence in Diagnostics: `coveredExecutor.webSocketStructure targetMatch=true` -> `coveredExecutor.externalAcquisitionHint` -> `externalAcquisitionSync.started` -> authoritative Detail Sync -> `externalAcquisitionSync.completed latestUserChanged=true` -> one page re-arm -> page-owned `externalStreamingObserved` / snapshots.
6. Verify reasoning/tools begin appearing without manual Sync; final materialization should still follow the b80 gate. Progressive final token streaming is **not** claimed solved.
7. After the first remote response is complete, send a second separate remote turn in the same selected conversation and verify it can independently trigger another bounded acquisition attempt without manual Sync.
8. Export Diagnostics after the two tests whether positive or negative.
9. Optional regression: one client-owned Send; preserve b67/b72 behavior.

Do not allocate b83 before b82 Runtime is classified.

## Evidence classification

- b81 Runtime automatic external acquisition: Rejected
- b81 target-conversation structural trigger: Positive
- b82 Code written: Yes
- b82 exact/static checks: Passed
- b82 Xcode Simulator: Passed on guarded attempt 2
- b82 Push CI: Passed
- b82 PR CI: Passed
- b82 Artifact/package: Produced / independently verified
- b82 Runtime/manual/real-device: Pending / Unverified
- b80 spacing: Frozen
- b80 external stopped-thinking semantics: Frozen
- Stable/Frozen Send as a whole: No

## Session round counter

Current work is round 20. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Human installs exact b82 and runs two distinct remote Sends in the same selected conversation without manual Sync, then returns the Runtime result and Diagnostics. Do not allocate b83 before classifying b82 Runtime.
