# DEV-send-stream

## Status

**Active — exact b81 is now the Human Runtime candidate for externally initiated cross-platform acquisition evidence. Account-wide notification discovery remains deferred. b80 spacing and external stopped-thinking semantics remain Frozen. b81 changes only privacy-safe at-document-start WebSocket structural diagnostics plus Build/Artifact identity; socket bodies remain non-authoritative. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged at product gate
- Exact b81 product/config source: `d1d4d197cc5d2a5022a28b332afebe485b216ea1`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b81` / `0.1.0 (81)`
- Guarded assembly: `33529062319 / 99927255152` — success
- Formal Push CI: `33529489996 / 99928687280` — success
- Formal PR CI: `33529494465` — success
- Canonical Push Artifact: `9809150111`
- Artifact ZIP SHA-256: `b02224911a3443e1a79b6c8d5fbabee0d6811f6c80bf50df8f76f6d603843469`
- IPA: `ChatGPTClient-0.1.0-b81-dev-send-stream.ipa`
- IPA SHA-256: `d48d2398dc5a7ef16b9983021a9173d87ba3b852f4a45c9431dff2ebcf057038`
- Actual `main` at Artifact gate: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b39-b81 permanently reserved
- b81 Runtime/manual/real-device: **Pending / Unverified**
- Stable/Frozen Send: **No**

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b80-device-runtime-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b81-allocation-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b81-build-artifact-20260901.md`

## User scope decision — round 17

The user explicitly defers official account-wide notification/haptic discovery. Do not block `DEV-send-stream` on the official A-page/B-conversation notification bubble.

Current required scope:

1. preserve accepted client-owned protected Send and response ownership;
2. improve externally initiated cross-platform acquisition/streaming;
3. progressive external final-body streaming remains an evidence problem — do not fake it;
4. account-wide auto-notification/Sync for conversations the client neither started nor adopted is later work.

Future completion notification for **client-owned** Sends can consume the existing Repository-owned active-response set/terminal transition; it does not require the official account-wide transport.

## Frozen / accepted b80 boundaries

- final tool/timeline -> reasoning-divider spacing: **Accepted / Frozen**;
- external stopped-thinking semantics: **Accepted / Frozen**;
- adopted external final materialization gate: **Positive / preserve**;
- explicit manual-Sync re-arm: **Positive / preserve**;
- b67 client-owned protected Send Runtime and b72 tested A/B simultaneous ownership: **preserve**.

## Remaining cross-platform defect

Externally initiated response acquisition is intermittent before Repository adoption. A selected covered target can load without the official page emitting matching `stream_status == IS_STREAMING`; explicit Sync/re-arm can later cause that page-owned signal and adoption then starts. Native must not manufacture `stream_status`, polling, retry loops or duplicate Sync.

Historical official-Web evidence already proves a user-level `wss://ws.chatgpt.com/...` exists during cross-device active-response continuation, but `WEB_SEND_ADAPTER.md` correctly keeps it structural-only/non-authoritative for reasoning/final bodies. The latest Lab account probe was inconclusive because it was installed after page startup and could not observe a socket already created.

The production covered bridge is injected at document start, so b81 captures socket **structure** from creation onward without changing response authority.

## Exact b81 product scope

Formal source `d1d4d197cc5d2a5022a28b332afebe485b216ea1` differs from its predecessor in exactly three product/config files:

1. `ChatGPTClient/RootViewController.swift`
   - privacy-safe at-document-start WebSocket lifecycle/message structural diagnostics;
   - sanitized host/path, frame transport type/length, JSON key names, safe short `type/event/kind/action/topic/name` tokens, presence of conversation-id-shaped keys, and boolean exact target-conversation match;
   - no raw frame data/IDs/prompt/answer/reasoning/tool bodies exported;
   - no socket frame mutates `ConversationRepository` in b81.
2. `ChatGPTClient.xcodeproj/project.pbxproj`
   - Build 81 / Candidate b81 identity only.
3. `.github/workflows/ios-foundation.yml`
   - b81 Artifact identity only.

Explicitly excluded: account-wide notification/haptic code, Native `stream_status`, timer/poll/retry/watchdog, repeated automatic Sync/reload, DOM body authority, WebSocket body authority, fake progressive final/typewriter, duplicate Send/resend, second response owner, Frozen spacing/stopped-thinking changes.

## Validation / Artifact evidence

Guarded tooling assembly `33529062319 / 99927255152` passed:

- formal-head guard;
- exact patch and exact product scope;
- `git diff --check`;
- prohibited-pattern guard;
- Xcode 16.4 generic iOS Simulator build;
- validated product blob commit.

Formal exact source `d1d4d197...` then passed Push `33529489996` and PR `33529494465`. Canonical Push Artifact `9809150111` was independently downloaded and verified:

- GitHub ZIP digest == local ZIP SHA `b02224911a3443e1a79b6c8d5fbabee0d6811f6c80bf50df8f76f6d603843469`;
- IPA SHA `d48d2398dc5a7ef16b9983021a9173d87ba3b852f4a45c9431dff2ebcf057038`, matching sidecar;
- package `0.1.0 (81)`;
- Candidate `DEV-send-stream-0.1.0-b81`;
- source marker `d1d4d197cc5d`;
- MinimumOSVersion 14.0;
- UIDeviceFamily `[1,2]`;
- Mach-O 64-bit arm64.

CI/Artifact/package evidence does not establish Runtime success.

## Human Runtime gate — exact next action

Install exact b81 and test the externally-started acquisition boundary:

1. Open conversation A in b81 and leave it selected until the covered page is loaded.
2. On another platform, start a sufficiently long new turn in the **same A conversation**.
3. Do **not** press Sync initially.
4. Record whether Native automatically acquires reasoning/tools and later final materialization.
5. Wait for completion and export Diagnostics whether success or failure.
6. Only if automatic acquisition failed, press Sync once **after** the failure is established; export again if useful.
7. If practical, also run one normal client-owned Send as a regression check, but do not block the structural experiment on that optional check.

Required correlation:

- socket created/open before the remote turn;
- structural frames around remote start/reasoning/completion;
- stable `type/event/kind/action/topic/name` / key shapes and target-match booleans;
- ordering relative to page-owned `stream_status`, `externalStreamingObserved` and plural snapshots;
- difference, if any, between automatically successful and failed acquisition runs.

Only a proven stable event may authorize the next minimal acquisition change. WebSocket frame bodies remain non-authoritative unless separately evidenced.

## Target/base / conflict state

At the b81 Artifact gate:

- PR #29 remained open / mergeable / unmerged;
- actual `main` remained `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- the known `main` movement relative to the PR's older recorded base modifies only `docs/project/COMPOSER_PARITY_PLAN.md`, so no Send product/state-owner conflict was found;
- only one Active development checkpoint exists;
- no b82 is allocated.

## Evidence classification

- b81 Code written: **Yes**
- b81 static/exact scope: **Passed**
- b81 Xcode Simulator: **Passed**
- b81 Push CI: **Passed**
- b81 PR CI: **Passed**
- b81 Artifact/package: **Produced / independently verified**
- b81 Runtime/manual/real-device: **Pending / Unverified**
- b80 spacing: **Frozen**
- b80 external stopped-thinking semantics: **Frozen**
- Stable/Frozen Send as a whole: **No**

## Session round counter

Current work is round 17. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Human installs the exact b81 IPA and returns one success/failure observation plus Diagnostics from the no-Sync external-turn test. Do not allocate b82 before classifying that Runtime evidence.
