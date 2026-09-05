# DEV-send-stream b80 — Build / CI / Artifact Evidence

Date: 2026-09-01

## Identity

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b80`
- Version / Build: `0.1.0 (80)`
- Formal exact product/config source: `b0f51041c2d7b645f152752ea6196526b2e4e0f6`
- PR: #29
- Runtime/manual/real-device: **Pending**
- Stable/Frozen Send: **No**

## Exact formal product scope

Commit `b0f51041c2d7b645f152752ea6196526b2e4e0f6` changes exactly four product/config paths relative to its checkpoint parent `81e322c7e626a63048a1b303891a0c3efd87e83b`:

1. `.github/workflows/ios-foundation.yml`
2. `ChatGPTClient.xcodeproj/project.pbxproj`
3. `ChatGPTClient/Conversation/ConversationFeature.swift`
4. `ChatGPTClient/RootViewController.swift`

The workflow change is identity-only: the two b79 Candidate/artifact labels become b80. The three non-workflow blobs are the exact blobs previously validated by the guarded assembly path.

## Assembly / static / Simulator evidence

Guarded assembly run `33506668882`:

- exact b80 patch applied: **Passed**
- exact-scope / prohibited-pattern / static guard: **Passed**
- Xcode 16.4 Simulator build: **Passed**
- validated non-workflow product blobs persisted on tooling commit `e3f03f7349b71287fc528c41169af4b9090d03d8`

The earlier workflow-push permission failure was a GitHub Actions token permission limitation, not a product-source or Xcode failure.

## Formal CI

Exact formal source `b0f51041c2d7b645f152752ea6196526b2e4e0f6`:

- Push workflow run `33511327452`: **success**
- PR workflow run `33511332786`: **success**

CI success is not Runtime proof.

## Canonical Artifact

Canonical source: successful Push run `33511327452`.

- Artifact ID: `9801761448`
- Artifact name: `ChatGPTClient-DEV-send-stream-0.1.0-b80`
- Artifact ZIP SHA-256: `0d6a5ddfa3c05d956708e43fb91acd6bb19988198a5a3cf34e6b72e289091db9`
- IPA: `ChatGPTClient-0.1.0-b80-dev-send-stream.ipa`
- IPA SHA-256: `87c360175a4adc4fa476383b395cffe74c57c5e75db252dd49acdf42be39ce1f`

## Independent package verification

The downloaded canonical Push artifact was independently unpacked and inspected.

Built `Info.plist`:

- `CFBundleShortVersionString = 0.1.0`
- `CFBundleVersion = 80`
- `DiagnosticsCandidate = DEV-send-stream-0.1.0-b80`
- `DiagnosticsSourceCommit = b0f51041c2d7`
- `DiagnosticsBuildConfiguration = Release`
- `DiagnosticsDeploymentTarget = 14.0`
- `MinimumOSVersion = 14.0`

Executable identity:

- Mach-O 64-bit
- arm64

The artifact sidecar independently agrees with IPA SHA-256 `87c360175a4adc4fa476383b395cffe74c57c5e75db252dd49acdf42be39ce1f`.

## Evidence classification

- Code written: **Yes**
- Static/exact-scope checks: **Passed**
- Xcode Simulator build: **Passed**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced: **Yes**
- Package identity independently verified: **Yes**
- Runtime/manual/real-device: **Not yet tested**
- Stable/Frozen: **No**

## Human Runtime gate

Test this exact b80 IPA only. Verify:

1. final tool/timeline -> reasoning-divider spacing is symmetric/acceptable;
2. a normal remote response that reaches page `COMPLETE` before final materialization no longer terminalizes/releases early and later final text appears without requiring another manual Sync;
3. b79-positive external stopped-thinking behavior remains preserved;
4. b79-positive manual-Sync external re-arm remains preserved.

Progressive external final token streaming remains an open protocol gap and is not claimed fixed by b80.
