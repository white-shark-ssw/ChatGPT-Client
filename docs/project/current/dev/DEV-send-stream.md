# DEV-send-stream

## Status

**Active — exact b70 product/config source is assembled, audited, Push+PR CI passed, Artifact/package identity independently verified, and real-device Runtime is now the only acceptance gate. b67 remains the accepted existing-conversation protected-Send transport predecessor. b69 Runtime defects justify b70 but are not themselves proof that b70 is fixed. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged at the b70 product gate
- Actual `main` at product promotion guard: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Clean b70 checkpoint parent: `5c379b3d994b28cb0ba5a3c793e4efa193a003a1`
- Exact b70 product/config source: `fb83be9163838f78abfa47903e67f27b6f66ec52`
- Candidate: `DEV-send-stream-0.1.0-b70`
- Version / Build: `0.1.0 (70)`
- b39-b70 permanently reserved; do not reuse b70 even if Runtime fails
- Stable/Frozen Send: No

## Why b70 exists

Exact b69 iPhone/iOS17 Runtime retained the b67 production transport success and validated the ordered response-timeline direction, but was Partial/Rejected for current daily-chat parity because the same test cycle exposed six concrete defects:

1. covered Web programmatic composer injection could raise the iOS keyboard after Native validation UI dismissed;
2. the current user prompt did not appear in live Native rows until terminal authoritative Sync;
3. expanded reasoning/tool presentation had excessive spacing and no reasoning/final divider;
4. production b69 dropped b65 Runtime-accepted GitHub nested `工具输入` / `工具输出` disclosures;
5. tool rows lacked bounded leading icons;
6. Native list/detail auth could become sticky after a transient 403 even while browser authentication later proved valid for the same account.

b67 remains the accepted existing-conversation protected-Send predecessor: one local Send -> one protected `/backend-api/f/conversation` -> HTTP200 `text/event-stream` -> Repository reasoning/tool/final updates -> terminal -> one authoritative reconcile.

## Exact b70 implementation boundary

Only the minimum source-backed corrections were made:

- `CoveredWebSendExecutor` keeps the verified composer selector/submit/protected-Send/SSE mechanism but suppresses the covered Web virtual keyboard during programmatic focus and blurs after injection;
- `ConversationRepository.beginLiveResponse` receives the actual trimmed prompt and stores it only in the response-local live snapshot so one optimistic user row appears immediately before the live assistant row; authoritative Detail replaces it at successful reconcile;
- b65 GitHub exact-parent detail authorization is restored inside the ordered b69 timeline: invocation `metadata.connector_tool_payload` + exact-parent GitHub result `message.content`, nested `工具输入` / `工具输出` collapsed independently, readable hierarchical output, and no raw tool body diagnostics;
- timeline items carry only response-local detail strings plus a bounded local tool icon kind; spacing and the reasoning/final separator stay inside the existing deterministic/manual message geometry;
- exact session/accounts HTTP403 is a temporary probe failure rather than persistent account absence by itself; last verified account identity is preserved while no fresh transient transport is returned from the failed probe;
- exact 401 retains unavailable/not-authenticated semantics;
- list/detail 401/403 invalidates the currently copied transient transport once and the current operation still fails visibly; the next explicit/normal read probes fresh WebKit credentials. No automatic replay/retry/poll/timer/watchdog was added;
- returning from a user-opened login flow may issue one explicit list refresh. This is a new navigation operation, not hidden retry.

State owners remain unchanged: `ConversationRepository` is the sole production conversation/response authority; `AuthSessionStore` is sole account authority; `WKWebsiteDataStore.default()` is sole persistent auth-secret authority; covered Web is challenge/protected-Send execution only.

## Exact source/scope evidence

Tooling-only assembly rebuilt b70 from clean checkpoint `5c379b3d...` with exact anchors.

- Assembly Run / Job: `33373254877 / 99428895016` — success.
- `git diff --check` passed.
- Authorized-scope audit passed and changed exactly five product/config files:
  - `.github/workflows/ios-foundation.yml`
  - `ChatGPTClient.xcodeproj/project.pbxproj`
  - `ChatGPTClient/Authentication/AuthSessionStore.swift`
  - `ChatGPTClient/Conversation/ConversationFeature.swift`
  - `ChatGPTClient/RootViewController.swift`
- Scope stat: `394 insertions / 93 deletions`; no tooling file is part of exact product commit.
- Xcode 16.4 iOS Simulator compile passed in assembly CI.
- Clean product commit `fb83be9163838f78abfa47903e67f27b6f66ec52` is exactly one commit ahead of `5c379b3d...`, direct parent `5c379b3d...`, tree `fff3ed3861ce9bad7dc848ba12a1f8b086d353de`.
- Xcode identity is `CURRENT_PROJECT_VERSION = 70`, `MARKETING_VERSION = 0.1.0`, `DIAGNOSTICS_CANDIDATE = DEV-send-stream-0.1.0-b70` in Debug and Release.

## Formal CI / Artifact evidence

Exact product head `fb83be9163838f78abfa47903e67f27b6f66ec52` was fast-forwarded to the formal Work branch without force.

- Push Run / Job: `33377045570 / 99440767755` — success.
- PR Run / Job: `33377049590 / 99440781050` — success.
- Push Artifact: `9752289536` (`ChatGPTClient-DEV-send-stream-0.1.0-b70`).
- Artifact ZIP digest: `sha256:bdf09b246ff259ee80d46acfad675713c1a0b51aee3b44f7ea9f0a7e67eafde0`.
- IPA: `ChatGPTClient-0.1.0-b70-dev-send-stream.ipa`.
- IPA SHA: `8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a`.
- Build log source marker: `fb83be916383`.
- Independently downloaded/unpacked Push Artifact agrees with GitHub digest and sidecar SHA.
- Built `Info.plist` independently verified: Release `0.1.0`, Build `70`, Candidate `DEV-send-stream-0.1.0-b70`, `DiagnosticsSourceCommit=fb83be916383`, minimum iOS `14.0`, arm64/iPhone+iPad family.

Artifact production and package verification do **not** prove the b69 Runtime defects are fixed.

## Evidence ladder

- Code written: Yes — exact product source `fb83be9163838f78abfa47903e67f27b6f66ec52`.
- Static / source-scope / `git diff --check`: Passed.
- Assembly iOS Simulator compile: Passed.
- Push CI: Passed.
- PR CI: Passed.
- Artifact produced: Yes — `9752289536`.
- Package identity independently verified: Yes.
- Runtime/manual/real-device: **Pending b70 gate**.
- Stable/Frozen: **No**.

## Conflict / recovery guard

Before formal promotion, PR #29 remained open/mergeable/unmerged at head `5c379b3d...`, `main` remained `d323b9ee...`, and no foreign formal-branch commit intervened. The formal ref was advanced only by a non-force fast-forward to exact b70 product source.

Earlier tooling/recovery placeholder commits are not part of the formal lineage and must never be replayed. Tooling assembly/product-base refs are evidence utilities only and never Candidate authority.

## Exact b70 real-device gate

Install exact Artifact `9752289536` / IPA SHA `8084e2ac...a44a` on the primary iPhone/iOS17 device, verify Build70/Candidate/source marker, clear diagnostics, then exercise normal daily-chat behavior. Required evidence:

1. covered Web never leaves a visible iOS keyboard after the Native Send/validation transition;
2. one local Send immediately inserts exactly one optimistic user row before the live assistant row; terminal reconcile must not duplicate it;
3. reasoning/tools remain chronological (`reasoning -> tool -> reasoning -> tool -> final`) and tool completion updates the existing row in place;
4. expanded GitHub tool rows again expose independently collapsed `工具输入` / `工具输出` with readable hierarchy and bounded leading icons;
5. expanded reasoning/tool spacing is compact and a deterministic divider separates reasoning/tool content from a real final answer;
6. navigating away/back during an active response preserves the Repository-owned live response without introducing a second owner or floating overlay;
7. if Native list/detail hits transient 403 while Web auth remains valid, the current operation may fail visibly, stale transient transport is discarded, and the next explicit/normal read can recover from current WebKit credentials without automatic replay/retry;
8. hidden `assistant:thoughts` / `inline_cot_expandable_content` never appears;
9. accepted b38 long-message geometry/quick navigation and accepted b67 one-Send transport do not regress;
10. export diagnostics after the tested terminal/recovery sequence.

If any item fails, keep b70 reserved, record the exact defect/evidence, and allocate a new candidate only from that evidence. Do not patch speculatively.

## Next exact action

Hand exact b70 Artifact `9752289536` to the user for the real-device gate above. Keep PR #29 open/unmerged. Do not allocate b71 and do not begin unrelated Composer/attachment/Stop/background work before exact b70 Runtime evidence is recorded.
