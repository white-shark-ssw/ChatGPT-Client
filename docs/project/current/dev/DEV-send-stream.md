# DEV-send-stream

## Status

**Active — exact b76 is fully assembled through Code/static/Simulator/Push+PR CI/Artifact/package verification and is now at the Human real-device Runtime gate. Exact product/config source is `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71`, Candidate `DEV-send-stream-0.1.0-b76`, Build 76. Canonical Artifact `9775920927` and IPA identity are independently verified. Current formal branch head after docs-only synchronization is `406ad21637b2fe1feb19ff850d4d54d3a1d4a10c`; this does not redefine the tested product source. Runtime/manual/device remains Unverified, so external adoption, 30/21/21 visual spacing, worst-case Back behavior and Stable/Frozen status are not accepted yet. PR #29 stays open/unmerged and is titled `DEV-send-stream: b76 page-owned live snapshot Runtime gate`.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b76 product/config source: `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)`
- Clean b76 product commit: `60bebc9e5b2296f6426ad264d7b57979781360b7`
- Clean product parent/checkpoint: `dd18b5beca16af34b075295dc3fc0782c714f26b`
- Assembly validation: `33439797547 / 99644929642` — guarded patch + `git diff --check` + exact scope + Xcode 16.4 Simulator build passed
- Push CI: `33440101178 / 99645927061` — success
- PR CI: `33440098527 / 99645917529` — success
- Canonical Push Artifact: `9775920927`
- ZIP SHA: `52f94ed7dbfbe311e37656fcce9a60bb5f8cc9c6b2af29434f7020d47729e944`
- IPA: `ChatGPTClient-0.1.0-b76-dev-send-stream.ipa`
- IPA SHA: `b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd`
- Package independently verified: Release `0.1.0 (76)`, Candidate b76, source marker `0da5a7577f2c`, MinimumOSVersion 14.0, arm64, iPhone+iPad family
- b39-b76 permanently reserved
- Runtime/manual/real-device b76: **Unverified**
- Stable/Frozen Send: No

## Identity / conflict guard

Before allocation, PR #29 remained open, mergeable and unmerged; PR base and actual `main` both remained `d323b9eed2dda75b9986fc06e14014d3e9b365fb`; no competing Active task/candidate conflict was found; b76 was unused. The formal product/config event head was exact `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71` with that same base; all later formal descendants through current `406ad21637b2fe1feb19ff850d4d54d3a1d4a10c` are docs-only and do not redefine b76. PR #29 remains open/mergeable/unmerged and its metadata is synchronized to the b76 Runtime gate.

The first temporary assembly run `33439592705 / 99644262927` stopped at an exact patch-match assertion before scope audit/build/commit and therefore produced no candidate. The corrected guarded assembly `33439797547 / 99644929642` passed patch application, exact scope audit and Xcode 16.4 Simulator build, then produced clean product commit `60bebc9e...` from parent `dd18b5...`. GitHub compare independently verified exactly three product files changed there. Workflow-only child `0da5a757...` gives the b76 Artifact identity, making it the exact product/config source.

## Retained accepted boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned read transport only, never a second conversation/message/response store.
- b67 local Native Send -> one protected `/backend-api/f/conversation` -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile remains Runtime accepted.
- b72 tested A-generating + B-send/generate simultaneous-generation remains Runtime positive.
- `assistant:thoughts` and inline COT remain non-presentational.
- No Native polling, Native resume/offset construction, WebSocket body authority, duplicate Send, retry/timer/watchdog, guessed fallback, compatibility shim or second state owner.

## Evidence that closed the protocol gate

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b75-visible-web-reprobe.md`
- `docs/project/runtime-evidence/DEV-send-stream-b75-visible-web-polling-structure.md`
- `docs/project/runtime-evidence/DEV-send-stream-b75-plural-message-semantics.md`

Current visible official Web itself can reproduce page-owned matching `/resume` HTTP404 JSON, then continue following the same externally active response through its own already-issued `stream_status` + plural `/backend-api/conversations/{conversation}` reads. `stream_status` moves `IS_STREAMING -> COMPLETE`; the plural response is a rolling/paged `messages[]` window, not singular Detail `mapping` and not a monotonic-count cursor.

The final structure probe proves entries after the latest user service message carry the already-evidenced service-message family needed for visible thinking preambles, assistant/non-all tool invocations, exact-parent tool results, hidden thoughts/inline COT, reasoning recap/end and final assistant text. While streaming, final assistant may be `status=in_progress`; after `COMPLETE`, the final service message is `finished_successfully`, `end_turn=true`, with completed body.

## Exact b76 code scope

GitHub compare from `dd18b5...` to clean product commit `60bebc9e...` is exactly:

- `ChatGPTClient/RootViewController.swift`
- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`

Exact source `0da5a757...` adds only `.github/workflows/ios-foundation.yml` to identify the b76 Artifact.

### Covered page observation

- Observes only the page's already-issued matching `GET /backend-api/conversation/{id}/stream_status` and `GET /backend-api/conversations/{id}` responses; no Native request/cadence is created.
- On page-owned `IS_STREAMING`, starts one Repository external live-response generation.
- On matching plural response, validates conversation identity, finds the latest user entry and forwards only following service messages as the current-response segment.
- Each received page-owned snapshot is projected atomically into the existing Repository live runtime rather than appended as duplicate deltas.
- Existing exact-parent tool association and GitHub tool-detail rule are retained; thoughts/inline COT stay hidden.
- Page-owned `/resume` remains strictly accepted only when HTTP200 `text/event-stream`; current external 404 is informational and lets the evidenced page-owned read path continue.
- WebSocket bodies remain unused.
- After page-owned `COMPLETE`, the next matching plural snapshot is projected, then terminal/reconcile occurs once.

### Typography

- Tool line height changes `26 -> 30`.
- Existing compact relationship remains `toolLineHeight * 0.70`, so reasoning/final fixed line height becomes `21.0`.
- Reasoning/final measurement and rendering continue to use the same paragraph style.
- This is a **candidate visual correction only**; it is not Runtime accepted until the user tests b76.

## Evidence classification

- Code written: **Yes — exact b76 source `0da5a757...`**
- Static/exact-scope checks: **Passed**
- Xcode 16.4 Simulator build: **Passed in assembly run `33439797547 / 99644929642`**
- Formal Push CI: **Passed — `33440101178 / 99645927061`**
- Formal PR CI: **Passed — `33440098527 / 99645917529`**
- Artifact produced: **Yes — canonical Push Artifact `9775920927`**
- Package identity verified: **Yes — ZIP/IPA SHA and built Info.plist independently checked**
- Runtime/manual/real-device: **No / Unverified**
- Stable/Frozen Send: **No**

## Exact next action

AI-owned build/CI/package/documentation work is complete. Next exact action is the Human b76 device gate using the canonical IPA; record Runtime evidence before any further product candidate.

Next Human Gate: exact b76 iPhone/iOS17 Runtime. It must test cross-platform active-response adoption, local b67 Send regression, b72-style concurrent ownership regression, visual line spacing, and—if reproduced—worst-case left-edge Back responsiveness. CI/Artifact success must not be described as Runtime success.
