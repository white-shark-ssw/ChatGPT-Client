# DEV-send-stream b76 Candidate Evidence

_Date: 2026-09-01_

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b76`
- Version/build: `0.1.0 (76)`
- Exact product/config source: `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71`
- Clean product commit: `60bebc9e5b2296f6426ad264d7b57979781360b7`, parent exact checkpoint `dd18b5beca16af34b075295dc3fc0782c714f26b`
- Guarded assembly: `33439797547 / 99644929642` — patch, `git diff --check`, exact three-product-file scope and Xcode 16.4 Simulator build passed
- Push CI: `33440101178 / 99645927061` — success
- PR CI: `33440098527 / 99645917529` — success
- Canonical Push Artifact: `9775920927`
- Artifact ZIP SHA-256: `52f94ed7dbfbe311e37656fcce9a60bb5f8cc9c6b2af29434f7020d47729e944`
- IPA: `ChatGPTClient-0.1.0-b76-dev-send-stream.ipa`
- IPA SHA-256: `b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd`
- Independent package inspection: Release 0.1.0 (76), Candidate b76, source marker `0da5a7577f2c`, MinimumOSVersion 14.0, iPhone+iPad family, Mach-O arm64

## Code scope / boundary

Clean product compare changes exactly `ChatGPTClient/RootViewController.swift`, `ChatGPTClient/Conversation/ConversationFeature.swift`, and `ChatGPTClient.xcodeproj/project.pbxproj`; exact source adds `.github/workflows/ios-foundation.yml` only for b76 Artifact identity.

The covered executor observes only official page-owned matching status/plural responses when external observation is active. The plural rolling window is bounded after the latest user service message and projected atomically into the existing Repository live-response runtime. No Native polling/cadence, Native resume/offset construction, WebSocket response-body parsing or duplicate Send is added. Strict actual HTTP200-SSE page-owned resume support remains. Typography candidate changes 26/18.2/18.2 -> 30/21/21.

## Evidence classification

- Code written: Yes
- Static/exact scope: Passed
- Xcode 16.4 Simulator: Passed
- Push CI: Passed
- PR CI: Passed
- Artifact produced: Yes
- Package identity: Independently verified
- Runtime/manual/real-device: **No / Pending**
- Stable/Frozen Send: **No**

## Human gate

Install exact b76 IPA and test cross-platform live adoption, terminal once, b67 local Send regression, b72-style concurrent ownership regression, 30/21/21 visual spacing, and the prior extreme Back stall if reproducible. Diagnostics must remain privacy-safe.
