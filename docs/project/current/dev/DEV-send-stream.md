# DEV-send-stream

## Status

**Active — user explicitly defers the account-wide notification requirement. Current priority remains: (1) client-owned protected Send/stream stays correct; (2) externally initiated cross-platform responses should be acquired and streamed as reliably as current official-Web evidence permits. b80 spacing and external stopped-thinking semantics remain Frozen. `DEV-send-stream-0.1.0-b81` / `0.1.0 (81)` is now allocated as a focused structural acquisition probe candidate; it does not make WebSocket body data authoritative. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Formal branch head at b81 allocation guard: `2198fa2059e4104259ce49647ec057177bb9e932`
- Actual `main` at allocation guard: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- `main` delta from the PR's older recorded base modifies only `docs/project/COMPOSER_PARITY_PLAN.md`; no Send product/state-owner overlap was found.
- Exact b80 product/config source: `b0f51041c2d7b645f152752ea6196526b2e4e0f6`
- b80 Candidate / Version-Build: `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)`
- b80 canonical Artifact: `9801761448`
- b80 IPA SHA-256: `87c360175a4adc4fa476383b395cffe74c57c5e75db252dd49acdf42be39ce1f`
- Allocated b81 Candidate / Version-Build: `DEV-send-stream-0.1.0-b81` / `0.1.0 (81)`
- Exact repository search found no pre-existing `DEV-send-stream-0.1.0-b81` before allocation.
- `docs/project/current/dev/` contains only this Active Work checkpoint plus its README; no parallel Active branch/candidate conflict exists.
- b39-b81 permanently reserved.

## User scope decision — round 17

The user explicitly chose to **defer account-wide notification discovery**. Do not block `DEV-send-stream` on the official A-page/B-conversation notification bubble or official iOS account-wide haptic transport.

Current required Send scope:

1. preserve the already-accepted client-owned protected Send lifecycle and its reasoning/tool/final behavior;
2. make externally initiated cross-platform response acquisition/streaming reliable enough for normal use;
3. keep progressive external final-body token streaming as an evidence problem — do not fake it;
4. account-wide completion notification/automatic Sync for conversations the client neither started nor adopted is later work.

For future client-owned completion notifications, the existing Repository-owned active-response set/terminal transitions remain sufficient; no account-wide official signal is required.

## b80 Runtime retained

### Frozen / preserve

- final tool/timeline -> reasoning-divider spacing: **Accepted / Frozen**;
- external stopped-thinking semantics: **Accepted / Frozen**;
- adopted external final materialization gate: **Positive**;
- explicit manual-Sync re-arm: **Positive / preserve**;
- client-owned protected Send predecessor (b67) and tested A/B concurrent ownership predecessor (b72): **preserve**.

### Still open

- externally initiated response acquisition is intermittent: a selected covered target can load yet fail to emit the target `stream_status == IS_STREAMING`; explicit Sync/re-arm can then make the page emit the signal and adoption starts;
- external reasoning/tools are only page-snapshot granular on the currently authorized plural-read path;
- progressive external final body is still unavailable from an authorized progressive source.

## Why b81 is a structural probe candidate

Current source begins external adoption only after the official page itself emits either:

- matching page-owned `GET /backend-api/conversation/{conversation}/stream_status` with `status == IS_STREAMING`, or
- a validated matching page-owned `/backend-api/f/conversation/resume` HTTP200 SSE.

The client does not issue those requests. b80 Runtime proves some target pages never emit the status signal until a re-arm/reload, so the missing trigger occurs **before** Repository adoption.

Historical official-Web evidence already proves a user-level `wss://ws.chatgpt.com/...` connection exists during cross-device active-response continuation, but that socket is explicitly non-authoritative for message/reasoning/final bodies. The latest Web Rule Lab account probe was inconclusive partly because it was installed after page startup and could not observe a socket that already existed.

`CoveredWebSendExecutor.bridgeScript` is injected at `WKUserScript(..., injectionTime: .atDocumentStart)`, so b81 can observe **structural WebSocket metadata from creation onward** without treating frame bodies as response authority.

## Exact b81 product scope

Only these changes are authorized:

1. `ChatGPTClient/RootViewController.swift`
   - add privacy-safe at-document-start WebSocket structural observation in the existing covered bridge;
   - capture only host/path, lifecycle, frame transport type/length, JSON top-level/nested key names, safe short event/type/kind/action tokens, and booleans such as whether the structure contains a conversation-id field / whether any exact string value equals the currently selected page conversation ID;
   - send those facts through the existing script-message bridge and record them in `DiagnosticsLogger`;
   - **do not** feed WebSocket payload/body text into `ConversationRepository`; do not use WebSocket frames to start/advance/terminalize a response in b81.
2. `ChatGPTClient.xcodeproj/project.pbxproj`
   - Build 81 / Candidate b81 identity only.
3. `.github/workflows/ios-foundation.yml`
   - b81 Artifact identity only.

No `ConversationFeature.swift` product change is authorized for b81 unless the structural probe itself requires a compile-only signature adjustment (not currently expected).

Explicitly excluded:

- account-wide notification/haptic implementation;
- Native `stream_status` construction;
- polling/timer/retry/watchdog;
- automatic repeated Sync/reload loops;
- DOM text authority;
- WebSocket body/reasoning/final authority;
- fake typewriter/progressive final;
- duplicate Send/resend;
- second conversation/response owner;
- changes to the b80 Frozen spacing or stopped-thinking semantics.

## b81 Runtime gate

Use the exact b81 IPA on iPhone/iOS17:

1. open conversation A in the client and leave it selected;
2. on another platform, send a sufficiently long new turn in the **same A conversation** after the covered page is already loaded;
3. do **not** press Sync initially;
4. record whether Native automatically acquires reasoning/tools;
5. after the remote response finishes, export Diagnostics regardless of success;
6. if automatic acquisition failed, press Sync once only after the initial failure is established, then export again if needed.

Required evidence from b81 diagnostics:

- whether a covered-page WebSocket already exists before the remote turn;
- whether structural frames arrive near remote start/reasoning/completion;
- whether any frame has a stable event/type/key shape and target-conversation match boolean that precedes the page-owned `stream_status`/plural reads;
- whether the successful and failing acquisitions differ structurally.

Only if that exact event source is proven may the next candidate use it as a bounded trigger for one page-owned re-arm/status discovery. Frame bodies themselves remain non-authoritative unless separately evidenced.

## Batch recovery point — b81 assembly

Known baseline before product assembly:

- formal feature head: `2198fa2059e4104259ce49647ec057177bb9e932`;
- PR #29: open / mergeable / unmerged;
- actual main: `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- b81 allocated here and must never be reused;
- b80 exact product source remains `b0f51041c2d7b645f152752ea6196526b2e4e0f6`.

Planned coherent batches:

1. create isolated tooling branch from this checkpointed formal head;
2. apply only RootViewController structural probe + b81 Xcode/workflow identity;
3. run exact-scope / prohibited-pattern / `git diff --check` + Xcode 16.4 Simulator build;
4. if validation passes, transplant only the validated three product/config blobs onto the formal branch in one Git-data commit;
5. run formal Push + PR CI and produce canonical b81 IPA;
6. independently verify Build/Candidate/source/Release/iOS14/arm64 + hashes;
7. update checkpoint/Build-Test/PR and hand the exact IPA to the user for the Runtime gate.

Do not touch account-wide notification product code, Frozen spacing, stopped-thinking semantics, or another task checkpoint during recovery.

## Evidence classification

- b80 Code/static/Simulator/Push+PR CI/Artifact/package: **Verified**
- b80 Runtime: **Partial-positive / partial-rejected**
- b80 spacing: **Frozen**
- b80 external stopped-thinking semantics: **Frozen**
- b81 allocation: **Done**
- b81 Code/static/CI/Artifact/Runtime: **Pending**
- Stable/Frozen Send as a whole: **No**

## Session round counter

This checkpoint update occurs during round 17. Continue displaying the current round count at the end of each user-facing response in this conversation.

## Next exact action

Create the isolated b81 tooling branch and validate the three-file structural-probe candidate. Continue autonomously through canonical IPA production unless a real evidence/CI/identity blocker occurs.
