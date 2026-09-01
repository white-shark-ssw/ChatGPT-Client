# DEV-send-stream

## Status

**Active — account-wide notification discovery is deferred by explicit user decision. Current priority is client-owned Send/stream correctness plus reliable externally initiated cross-platform acquisition/streaming. b80 spacing and external stopped-thinking semantics are Frozen. `DEV-send-stream-0.1.0-b81` / `0.1.0 (81)` is allocated as a focused at-document-start WebSocket structural-probe candidate; WebSocket bodies remain non-authoritative. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Exact b80 product/config source: `b0f51041c2d7b645f152752ea6196526b2e4e0f6`
- b80 Candidate / Version-Build: `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)`
- b80 canonical Artifact: `9801761448`
- b80 IPA SHA-256: `87c360175a4adc4fa476383b395cffe74c57c5e75db252dd49acdf42be39ce1f`
- Allocated b81 Candidate / Version-Build: `DEV-send-stream-0.1.0-b81` / `0.1.0 (81)`
- b39-b81 permanently reserved
- b81 Runtime: Pending

Durable allocation evidence: `docs/project/runtime-evidence/DEV-send-stream-b81-allocation-20260901.md`.

## User scope decision — round 17

The user explicitly defers official account-wide notification/haptic discovery. Do not block `DEV-send-stream` on the official A-page/B-conversation notification bubble.

Current required scope:

1. preserve accepted client-owned protected Send and response ownership;
2. improve externally initiated cross-platform acquisition/streaming;
3. progressive external final-body streaming remains an evidence problem — do not fake it;
4. account-wide auto-notification/Sync for conversations the client neither started nor adopted is later work.

Client-owned completion notification can later use the existing Repository-owned active-response set and terminal transitions; it does not require official account-wide transport.

## Frozen / accepted b80 boundaries

- final tool/timeline -> reasoning-divider spacing: **Accepted / Frozen**;
- external stopped-thinking semantics: **Accepted / Frozen**;
- adopted external final materialization gate: **Positive / preserve**;
- explicit manual-Sync re-arm: **Positive / preserve**;
- b67 client-owned protected Send Runtime and b72 tested A/B simultaneous ownership: **preserve**.

## Remaining cross-platform defect

Externally initiated response acquisition is intermittent before Repository adoption. A selected covered target can load without the official page emitting matching `stream_status == IS_STREAMING`; explicit Sync/re-arm can later cause that page-owned signal and adoption then starts. Native must not manufacture `stream_status`, polling, retry loops or duplicate Sync.

Historical official-Web evidence already proves a user-level `wss://ws.chatgpt.com/...` exists during cross-device active-response continuation, but `WEB_SEND_ADAPTER.md` correctly keeps it structural-only/non-authoritative for reasoning/final bodies. The latest Lab account probe was inconclusive because it was installed after page startup and could not observe a socket already created.

The production covered bridge is injected at document start, so b81 can capture socket **structure** from creation onward without changing response authority.

## Exact b81 product scope

Authorized product/config paths:

1. `ChatGPTClient/RootViewController.swift`
   - add privacy-safe at-document-start WebSocket lifecycle/message structural diagnostics only;
   - record sanitized host/path, frame transport type/length, JSON key names, safe short `type/event/kind/action/topic/name` tokens, presence of conversation-id-shaped keys, and a boolean exact match against the current page conversation ID;
   - do not export raw frame data, IDs, prompts, answers, reasoning or tool bodies;
   - do not feed socket frames into `ConversationRepository` in b81.
2. `ChatGPTClient.xcodeproj/project.pbxproj` — Build 81 / Candidate b81 identity only.
3. `.github/workflows/ios-foundation.yml` — b81 Artifact identity only.

Explicitly excluded: account-wide notification/haptic code, Native `stream_status`, timer/poll/retry/watchdog, repeated automatic Sync/reload, DOM body authority, WebSocket body authority, fake progressive final/typewriter, duplicate Send/resend, second response owner, Frozen spacing/stopped-thinking changes.

## b81 Runtime gate

1. Open conversation A in the exact b81 client and leave it selected until the covered page has loaded.
2. Start a sufficiently long new turn in the same A from another platform.
3. Do not press Sync initially.
4. Observe whether Native automatically acquires reasoning/tools/final materialization.
5. Export Diagnostics after the response whether success or failure.
6. Only if acquisition failed, press Sync once after the failure is established and export again if useful.

Need to correlate socket creation/frames with remote start/reasoning/completion and with page-owned `stream_status`/plural reads. Only a proven stable event may authorize a later bounded trigger. Socket frame bodies remain non-authoritative unless separately evidenced.

## Batch recovery point — b81 assembly

Latest formal feature head after the b81 allocation evidence write: `9e49c966d6f776e59e7300bd387b5eda7fcea165`.

Guard facts:

- PR #29 open / mergeable / unmerged;
- actual `main` `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- main delta from the PR's older recorded base modifies only `docs/project/COMPOSER_PARITY_PLAN.md`, so no Send product/state-owner conflict was found;
- exact b81 repository search was unused before allocation;
- `docs/project/current/dev/` contains only this Active Work checkpoint plus README;
- b81 must never be reused.

Pending coherent batches:

1. create isolated tooling branch from `9e49c966...`;
2. apply only RootViewController structural probe + b81 Xcode identity;
3. run exact-scope/prohibited-pattern/`git diff --check` + Xcode 16.4 Simulator validation;
4. validate b81 workflow identity separately;
5. transplant the three validated product/config blobs to formal branch in one Git-data commit;
6. run formal Push + PR CI, canonical Artifact and independent IPA identity/hash verification;
7. update checkpoint/Build-Test/PR and hand the exact b81 IPA to the user.

Do not touch account-wide notification product code, Frozen spacing, stopped-thinking semantics, or another task checkpoint during recovery.

## Evidence classification

- b80 Code/static/Simulator/Push+PR CI/Artifact/package: Verified
- b80 Runtime: Partial-positive / partial-rejected
- b80 spacing: Frozen
- b80 external stopped-thinking semantics: Frozen
- b81 allocation: Done
- b81 Code/static/CI/Artifact/Runtime: Pending
- Stable/Frozen Send as a whole: No

## Session round counter

Current work is round 17. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Create isolated b81 tooling branch from `9e49c966...` and continue through canonical IPA production unless a real identity/evidence/CI blocker occurs.
