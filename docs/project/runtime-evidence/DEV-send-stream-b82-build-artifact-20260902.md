# DEV-send-stream b82 build / Artifact evidence — 2026-09-02

## Identity

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b82`
- Version / Build: `0.1.0 (82)`
- Exact formal product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Product parent: `9183daa299fac5ec28ebe53ab89bb919a991d6d2`
- PR: #29
- Actual `main` at gate: `94f0c5777dad262cd1fb22be49082dbd92c962f2`

Exact product/config diff parent -> source contains only:

1. `.github/workflows/ios-foundation.yml`
2. `ChatGPTClient.xcodeproj/project.pbxproj`
3. `ChatGPTClient/RootViewController.swift`

## Guarded assembly

Tooling branch: `tooling/dev-send-stream-b82-assembly-20260902`.

Attempt 1:

- run `33534672784` / job `99945951282`;
- formal-head guard passed;
- exact patch/scope/`git diff --check`/prohibited-pattern checks passed;
- Xcode 16.4 Simulator compile rejected the candidate because `CoveredWebSendEvent.externalAcquisitionHint` had not been added to the Repository event switch exhaustively;
- no validated product commit was produced and nothing from this failed attempt was transplanted to the formal branch.

Attempt 2:

- run `33534965707` / job `99946924531`;
- exact fix added the missing non-authoritative event-name case and retained the current-executor re-arm guard;
- formal-head guard passed;
- exact two-product-file tooling scope passed;
- `git diff --check` passed;
- prohibited timer/poll/retry/watchdog pattern guard passed;
- Xcode 16.4 Release generic iOS Simulator build passed;
- validated tooling product commit: `71559f5a216adf49d7b14f58e159b249e658f48c`.

Validated Root/PBX blobs were transplanted to the clean formal product parent and the b82 workflow identity was added through Git data, yielding exact formal source `c7a274786dfd175e8f476fc15c4964840e112a1d`.

## Formal CI

- Push run `33535342383` / job `99948156535`: **success**.
- PR run `33535347654` / job `99948174293`: **success**.

CI success is not Runtime proof.

## Canonical Artifact / package verification

- Canonical Push Artifact: `9811406038`
- Artifact name: `ChatGPTClient-DEV-send-stream-0.1.0-b82`
- GitHub Artifact digest / independently downloaded ZIP SHA-256: `bcb9c65f7cee7680580acd6238d3dd9f03f30b3c5f9024cd251b31690ac13681`
- IPA: `ChatGPTClient-0.1.0-b82-dev-send-stream.ipa`
- IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- Artifact sidecar carries the same IPA SHA.

Independent unpacking confirms:

- `CFBundleShortVersionString = 0.1.0`
- `CFBundleVersion = 82`
- `DiagnosticsCandidate = DEV-send-stream-0.1.0-b82`
- `DiagnosticsSourceCommit = c7a274786dfd`
- `MinimumOSVersion = 14.0`
- `UIDeviceFamily = [1, 2]`
- executable = Mach-O 64-bit arm64.

## b82 behavior under Runtime test

b82 uses the b81-evidenced exact target-conversation WebSocket structure only as an **acquisition hint**. It does not treat the socket body as conversation/reasoning/final content authority.

For each eligible target-match event while no same-conversation auto Sync/live response is active:

1. start at most one authoritative `ConversationRepository.syncLatestMessages`;
2. compare latest user identity before/after;
3. if latest user changed and the conversation is still selected and no response was naturally acquired, re-arm/reload the existing covered page once;
4. if there is no change or Sync fails, stop without retry;
5. a later distinct target-match event can trigger another bounded attempt after the previous one finishes.

This matches the corrected b81 evidence that the two observed target-match events came from two distinct remote Sends.

## Evidence classification

- Code written: **Yes**
- Exact/static checks: **Passed**
- Xcode Simulator: **Passed on attempt 2**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact/package: **Produced / independently verified**
- Runtime/manual/real-device: **Pending**
- b80 spacing: **Frozen**
- b80 external stopped-thinking semantics: **Frozen**
- Stable/Frozen Send as a whole: **No**
