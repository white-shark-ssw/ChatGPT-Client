# DEV-send-stream b81 build / Artifact evidence — 2026-09-01

## Scope decision

The user explicitly deferred account-wide notification discovery. b81 is a focused structural acquisition probe for externally initiated cross-platform responses while preserving the already-accepted client-owned Send path. It does not make WebSocket frame bodies authoritative.

## Exact candidate identity

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b81`
- Version / Build: `0.1.0 (81)`
- Exact formal product/config source: `d1d4d197cc5d2a5022a28b332afebe485b216ea1`
- Formal product diff from predecessor docs head `fef9d91b9a91bb9e446566cb53321a8c37498ef5` is exactly:
  - `.github/workflows/ios-foundation.yml`
  - `ChatGPTClient.xcodeproj/project.pbxproj`
  - `ChatGPTClient/RootViewController.swift`
- No `ConversationFeature.swift`, Frozen spacing, stopped-thinking semantic, notification, polling or second-owner change is included.

## Guarded assembly evidence

Isolated tooling branch: `tooling/dev-send-stream-b81-assembly-20260901`.

- Assembly run: `33529062319`
- Job: `99927255152`
- Result: **success**
- Passed:
  - formal-head guard;
  - exact b81 patch application;
  - exact product scope check;
  - `git diff --check`;
  - prohibited timer/poll/retry/watchdog pattern check;
  - Xcode 16.4 generic iOS Simulator build;
  - validated product-blob commit.
- Validated tooling product commit: `cbf430d07c15f5e14de9c5624931eb911dab368c`
- Tooling workflow identity was then moved to b81 and only the three validated product/config blobs were transplanted to the formal branch.

## Exact b81 behavior change

`CoveredWebSendExecutor.bridgeScript` is already injected using `WKUserScript(... injectionTime: .atDocumentStart)`. b81 adds privacy-safe WebSocket **structure-only** observation from page startup:

- sanitized socket host/path;
- created/open/message/close/error lifecycle;
- frame transport type and length;
- JSON top-level/nested key names when a bounded string frame parses as JSON;
- safe short `type/event/kind/action/topic/name` tokens;
- booleans for conversation-key presence and exact match to the currently selected page conversation ID.

Swift records these only as `coveredExecutor.webSocketStructure` diagnostics while external observation is active.

It does **not**:

- send raw frame data to diagnostics;
- expose raw conversation IDs;
- use socket payload text as reasoning/final/tool content;
- begin/advance/terminalize a Repository response from WebSocket data;
- issue Native `stream_status`, resume or plural conversation requests;
- add polling/timer/retry/watchdog/automatic Sync loops;
- duplicate Send/resend;
- change the b80 Frozen spacing or stopped-thinking semantics.

## Formal CI

Exact source `d1d4d197cc5d2a5022a28b332afebe485b216ea1`:

- Push run `33529489996` — **success**
- Push job `99928687280` — **success**
- PR run `33529494465` — **success**

## Canonical Artifact / package evidence

Canonical source is the successful Push run.

- Artifact ID: `9809150111`
- Artifact name: `ChatGPTClient-DEV-send-stream-0.1.0-b81`
- GitHub Artifact ZIP digest: `sha256:b02224911a3443e1a79b6c8d5fbabee0d6811f6c80bf50df8f76f6d603843469`
- Independently downloaded ZIP SHA-256: `b02224911a3443e1a79b6c8d5fbabee0d6811f6c80bf50df8f76f6d603843469`
- IPA: `ChatGPTClient-0.1.0-b81-dev-send-stream.ipa`
- IPA SHA-256: `d48d2398dc5a7ef16b9983021a9173d87ba3b852f4a45c9431dff2ebcf057038`
- Artifact sidecar matches the independently calculated IPA SHA.

Independent unpacking verifies:

- `CFBundleShortVersionString = 0.1.0`
- `CFBundleVersion = 81`
- `DiagnosticsCandidate = DEV-send-stream-0.1.0-b81`
- `DiagnosticsSourceCommit = d1d4d197cc5d`
- `MinimumOSVersion = 14.0`
- `UIDeviceFamily = [1, 2]`
- executable is Mach-O 64-bit arm64.

The build workflow uses the existing Release IPA packaging path; package identity agrees with the exact formal source and candidate.

## Target/base state at Artifact gate

- PR #29 remains open / mergeable / unmerged.
- PR head at the product gate: `d1d4d197cc5d2a5022a28b332afebe485b216ea1`.
- Actual `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- The previously observed `main` movement relative to the PR's older recorded base touches only `docs/project/COMPOSER_PARITY_PLAN.md`, so no Send product/state-owner conflict was found.

## Human Runtime gate

b81 is **not** a claim that cross-platform streaming is fixed. It is a diagnostic candidate to identify the missing externally-started acquisition signal without changing response authority.

Test:

1. Open conversation A in b81 and leave it selected until the covered page has loaded.
2. On another platform, start a sufficiently long response in the same A.
3. Do not press Sync initially.
4. Record whether reasoning/tools are automatically acquired.
5. Wait for completion and export Diagnostics whether success or failure.
6. Only if acquisition failed, press Sync once after the failure is established and optionally export again.

Needed evidence is the ordering/correlation of `coveredExecutor.webSocketStructure` with page-owned `stream_status`, external adoption and plural snapshots. WebSocket bodies remain non-authoritative until separate Runtime evidence proves an exact safe use.

## Evidence classification

- Code written: **Yes**
- Exact scope/static checks: **Passed**
- Xcode 16.4 Simulator build: **Passed**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced: **Yes**
- Package identity independently verified: **Yes**
- Runtime/manual/real-device tested: **No / Pending**
- Stable/Frozen Send as a whole: **No**
