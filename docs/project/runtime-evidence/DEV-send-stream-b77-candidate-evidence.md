# DEV-send-stream b77 candidate evidence

## Identity

- Work: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Base `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Candidate: `DEV-send-stream-0.1.0-b77`
- Version / Build: `0.1.0 (77)`
- Clean product parent: `81dbe729b0ad50bf63300bb6b5bd9b23cb20b87b`
- Clean product commit: `4c88a7dc5bb2b09dafa616e82cd75ee13eff9c4d`
- Exact product/config source: `c0266e83a5a27d2e39751ecb84a25e0072fb01f4`
- b39-b77 permanently reserved.

## Exact product scope

Guarded assembly first ran on isolated branch `tooling/dev-send-stream-b77-assembly-20260901` and then the validated product blobs were transplanted into the clean formal product commit. GitHub compare from `81dbe729...` to `4c88a7dc...` contains exactly:

- `ChatGPTClient.xcodeproj/project.pbxproj`
- `ChatGPTClient/Authentication/AuthSessionStore.swift`
- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient/RootViewController.swift`

Workflow-only child `c0266e83...` updates `.github/workflows/ios-foundation.yml` to b77 identity and is therefore the exact product/config source used for formal package production.

## Build / CI / Artifact evidence

- Guarded assembly run/job: `33443341526 / 99656536553` — exact patch application passed; exact four-file scope passed; `git diff --check` passed; Xcode 16.4 Simulator build passed.
- Formal Push CI: `33443626427 / 99657452954` — success.
- Formal PR CI: `33443630320 / 99657464938` — success.
- Canonical Push Artifact: `9777216066`.
- Artifact ZIP SHA-256: `ce26379ad43e338afc64bbe51e2fbbbad0063eb85923ba736504ff59f092a2d8`.
- IPA: `ChatGPTClient-0.1.0-b77-dev-send-stream.ipa`.
- IPA SHA-256: `651f5cfe05e862a74153e22479f2df649baf3412c10e583242d0a24b139e531b`.
- Sidecar checksum matches the independently computed IPA SHA.
- Built Info.plist independently inspected: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=77`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b77`, `DiagnosticsSourceCommit=c0266e83a5a2`, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`.
- Executable independently inspected as Mach-O 64-bit arm64.

## Intended b77 change

### Presentation

- tool fixed line height `30 -> 36` (+20%);
- shared reasoning/final fixed line height `21 -> 25.2` via retained `0.70` relationship;
- tool paragraph upper/lower spacing becomes symmetric `12 / 12` instead of `5 / 12`;
- font sizes unchanged.

### Secure transport / auth semantics

- do not demote an already verified in-memory account merely because a new account-context probe begins;
- if a subsequent temporary failed probe occurs while verified context is retained, preserve the verified account state while still failing the current operation;
- normalize direct native list/detail `NSURLErrorSecureConnectionFailed` (`-1200`) to explicit secure-connection-unavailable presentation;
- no retry/timer/watchdog/fallback was added; no claim is made that an external TLS outage itself is repaired.

### Progressive-final evidence only

- while an external response is active, record only the latest official-page assistant DOM node count and text-character count as privacy-safe structure evidence;
- no assistant DOM text is transferred into Repository state;
- DOM is not adopted as response authority;
- WebSocket bodies remain unused;
- no fake typewriter/synthetic final streaming is implemented.

## Evidence classification

- Code written: Yes
- Exact/static checks: Passed
- Simulator build: Passed
- Push CI: Passed
- PR CI: Passed
- Artifact produced: Yes
- Package identity verified: Yes
- Runtime/manual/real-device: **Pending / Unverified**
- Stable/Frozen Send: **No**

## Human gate

Install exact b77 and return screenshot + diagnostics after:

1. visual check of tool/reasoning/final vertical rhythm;
2. cross-platform active response through final completion;
3. enough final-phase duration to observe `coveredExecutor.externalDOMStructure` before terminal;
4. local Send regression where practical;
5. export diagnostics if `-1200`, 401, 403 or actual not-authenticated behavior occurs.

Do not infer true progressive final body support until Runtime evidence shows an official page-owned body source changing before completion.
