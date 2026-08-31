# DEV-send-stream

## Status

**Active — b76 Runtime is now partial-positive / partial-rejected, and exact b77 has completed Code/static/Simulator/Push+PR CI/Artifact/package verification. b77 is now at the Human real-device Runtime gate. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b77 product/config source: `c0266e83a5a27d2e39751ecb84a25e0072fb01f4`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b77` / `0.1.0 (77)`
- Clean b77 product commit: `4c88a7dc5bb2b09dafa616e82cd75ee13eff9c4d`
- Clean product parent/checkpoint: `81dbe729b0ad50bf63300bb6b5bd9b23cb20b87b`
- Guarded assembly: `33443341526 / 99656536553` — exact patch application + exact scope + `git diff --check` + Xcode 16.4 Simulator build passed
- Formal Push CI: `33443626427 / 99657452954` — success
- Formal PR CI: `33443630320 / 99657464938` — success
- Canonical Push Artifact: `9777216066`
- Artifact ZIP SHA: `ce26379ad43e338afc64bbe51e2fbbbad0063eb85923ba736504ff59f092a2d8`
- IPA: `ChatGPTClient-0.1.0-b77-dev-send-stream.ipa`
- IPA SHA: `651f5cfe05e862a74153e22479f2df649baf3412c10e583242d0a24b139e531b`
- Independent package inspection: Release `0.1.0 (77)`, Candidate `DEV-send-stream-0.1.0-b77`, source marker `c0266e83a5a2`, MinimumOSVersion 14.0, iPhone+iPad family, Mach-O arm64
- b39-b77 permanently reserved
- Runtime/manual/real-device b77: **Pending / Unverified**
- Stable/Frozen Send: **No**

## Resume / identity / conflict guard

Before b77 allocation, the formal feature branch was `81dbe729...`, PR #29 remained open/mergeable/unmerged, PR base and actual `main` were both `d323b9ee...`, and no exact `DEV-send-stream-0.1.0-b77` repository use was found. The b77 patch was first assembled on isolated tooling branch `tooling/dev-send-stream-b77-assembly-20260901`; guarded run `33443341526 / 99656536553` passed exact patch/scope/diff and Xcode 16.4 Simulator build. The resulting product blobs were transplanted into one clean formal product commit `4c88a7dc...` directly on parent `81dbe729...`; compare verifies exactly four product files changed. Workflow-only child `c0266e83...` identifies the b77 candidate/artifact and is the exact product/config source. Any later documentation-only descendants do not redefine b77.

## b76 Runtime evidence now accepted

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b76-device-runtime-20260831.md`.

User real-device evidence establishes:

- **Cross-platform thinking/reasoning/tools adoption: positive.** An externally-started response now starts one Repository-owned `external_page_owned` live generation and updates reasoning/tool state while the official page-owned `/resume` returns HTTP404 JSON and the page continues via its own read path.
- **Cross-platform final body progression: rejected.** During final phase the observed plural snapshots remained `finalCharacters=0` and then jumped directly to the complete final body (`6718` characters in the captured run) at terminal. Therefore the currently evidenced plural response path does not provide incremental final body bytes.
- **Refresh/login complaint: secure-transport failure, not proven login loss.** The failure window is `NSURLErrorDomain/-1200`; WebKit persistent auth data remains present and there is no 401/403/not-authenticated evidence in the supplied run.
- **b76 typography: rejected.** The b76 `30 / 21 / 21` line-height candidate still looked too tight, and the tool paragraph additionally retained asymmetric `paragraphSpacingBefore=5` vs `paragraphSpacing=12`.

b76 remains permanently reserved and is not Stable/Frozen.

## Retained architecture / protocol boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned observation transport only; it is not a second conversation/message store.
- b67 local Native Send -> one protected official Web Send -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile remains Runtime accepted.
- b72 exact tested A-generating + B-send/generate ownership path remains Runtime positive.
- `assistant:thoughts` / inline COT remain non-presentational.
- No Native polling/cadence, Native resume/offset synthesis, duplicate Send, retry/timer/watchdog, guessed fallback, compatibility shim, second response owner, or WebSocket-body authority.

## Exact b77 product scope

GitHub compare from `81dbe729...` to clean product commit `4c88a7dc...` is exactly:

- `ChatGPTClient.xcodeproj/project.pbxproj`
- `ChatGPTClient/Authentication/AuthSessionStore.swift`
- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient/RootViewController.swift`

Exact source `c0266e83...` adds only the b77 identity update in `.github/workflows/ios-foundation.yml` after that clean product commit.

### Typography correction

- Tool fixed line height: `30 -> 36` (+20%).
- Existing shared ratio remains `toolLineHeight * 0.70`, therefore reasoning/final fixed line height becomes `25.2` (+20% from 21).
- Tool paragraph upper/lower spacing is now symmetric: `paragraphSpacingBefore=12`, `paragraphSpacing=12` instead of `5 / 12`.
- Font sizes are unchanged. This is still a Runtime visual candidate until the user accepts it on-device.

### Secure-transport / auth-state semantics

- A previously verified in-memory account context is no longer demoted to `.probing` merely because another account-context probe starts.
- If that subsequent probe returns the existing temporary `.failed` state while a verified context is still present, the verified account state is preserved and a privacy-safe `session.accountStatePreserved` diagnostic is emitted; the current operation still receives failure and no retry is created.
- Direct native list/detail `NSURLErrorSecureConnectionFailed` (`-1200`) is normalized to an explicit `secureConnectionUnavailable` error instead of being presented as authentication invalidation.
- This does **not** claim to fix an underlying TLS/network outage, and a cold launch that cannot establish any verified native context still cannot synthesize one.

### Final-body evidence probe

b77 does **not** fake final streaming and does **not** adopt a guessed body source. While an external page-owned response is active, the covered official page now emits only a privacy-safe structural diagnostic for the latest assistant DOM node: assistant-node count + text-character count. No DOM body text is copied into Repository state. This evidence is used only to decide whether the official page itself has progressive final text before the plural API exposes the completed body. WebSocket bodies remain unused.

## Evidence classification

- Code written: **Yes — clean product commit `4c88a7dc...`; exact product/config source `c0266e83...`**
- Exact-scope / `git diff --check`: **Passed**
- Xcode 16.4 Simulator build: **Passed — assembly `33443341526 / 99656536553`**
- Formal Push CI: **Passed — `33443626427 / 99657452954`**
- Formal PR CI: **Passed — `33443630320 / 99657464938`**
- Artifact produced: **Yes — canonical Push Artifact `9777216066`**
- Package identity verified: **Yes — ZIP/IPA hashes, Info.plist and arm64 Mach-O independently inspected**
- Runtime/manual/real-device b77: **Pending / Unverified**
- Stable/Frozen Send: **No**

## Exact next action

Human b77 device gate using the canonical IPA.

Required evidence in one real-device pass:

1. Verify the tool row now has visibly symmetric vertical rhythm and the `36 / 25.2 / 25.2` tool/reasoning/final spacing is acceptable or reject it with screenshot.
2. Start a sufficiently long response on another platform, enter the same conversation in Native, and confirm b76's positive thinking/reasoning/tool continuation still works.
3. During the final phase, keep the app open until completion, then export diagnostics. Inspect `coveredExecutor.externalDOMStructure` timestamps/character counts against `liveResponse.externalSnapshot finalCharacters=0` and terminal to decide whether a true progressive page-owned final-body source exists.
4. If refresh/secure-connection failure recurs, export diagnostics; distinguish `-1200` transport failure from actual 401/403/not-authenticated evidence. Do not interpret cached/verified state preservation as proof that TLS is repaired.
5. Regression-check local protected Send (b67 boundary) and, when practical, b72-style concurrent ownership.

Do not allocate another product candidate until b77 Runtime evidence is classified. CI/Artifact/package success must not be described as Runtime success.
