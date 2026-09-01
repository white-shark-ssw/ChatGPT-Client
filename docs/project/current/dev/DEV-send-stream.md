# DEV-send-stream

## Status

**Active — exact b78 has completed Code/static/Simulator/Push+PR CI/Artifact/package verification and is now at the Human real-device Runtime gate. b77 Runtime is partial/rejected. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal branch head after durable b78 docs sync: `cdf30f26e827193edc9b2c7d31dc832cd1266386`
- Clean b78 product commit: `180065e0faf947292a9f21b56c4ea366a5c322fe`
- Exact b78 product/config source: `031b1a1f2c1d01900c2ab79ff14b1f2fb6c7e809`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b78` / `0.1.0 (78)`
- Final tooling Xcode validation: `33482721335 / 99775722851` — exact final presentation patch + exact scope + `git diff --check` + Xcode 16.4 Simulator build passed on the complete b78 tooling state
- Formal Push CI: `33482983693 / 99776545604` — success
- Formal PR CI: `33482987997 / 99776557269` — success
- Canonical Push Artifact: `9790836559`
- Artifact ZIP SHA: `7b5900a960ef680cce34642ca6cef232f201a260b182d6b640266e81982b081f`
- IPA: `ChatGPTClient-0.1.0-b78-dev-send-stream.ipa`
- IPA SHA: `726e3c09bcac4eb8a40a8ecb79b8abb0f145d89e41481083bc51941a7978620e`
- Independent package inspection: Release `0.1.0 (78)`, Candidate `DEV-send-stream-0.1.0-b78`, source marker `031b1a1f2c1d`, MinimumOSVersion 14.0, Mach-O arm64
- b39-b78 permanently reserved
- Runtime/manual/real-device b78: **Pending / Unverified**
- Stable/Frozen Send: **No**

## Resume / identity / final-artifact guard

This is the same continuously selected Work. Final artifact synchronization was re-checked before handoff:

- PR #29 remains open / mergeable / unmerged.
- PR base remains `main` at `d323b9eed2dda75b9986fc06e14014d3e9b365fb`; no target/base drift occurred during b78 assembly/packaging.
- PR head exact product/config source for the canonical b78 Push Artifact is `031b1a1f2c1d01900c2ab79ff14b1f2fb6c7e809`; later descendants are docs-only and do not redefine the tested product.
- Clean compare from b78 parent/checkpoint to product commit changes exactly `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift`.
- `DEV-send-stream-0.1.0-b78` is reserved and recorded in `BUILD_TEST_INDEX.md`; no later candidate is allocated.

## b77 Runtime evidence — partial/rejected

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b77-device-runtime-20260901.md`.

The user-supplied iPhone screenshots and exact b77 diagnostics establish:

1. **Inline tool presentation rejected.** Tool/GitHub operation rows still had visibly wrong vertical rhythm and insufficient prominence as a special message type. Source inspection found the transition separator/newline still inherited reasoning paragraph style while tool text/icon used a different style, so changing only numeric line height/spacing could not make boundaries deterministic.
2. **User-message parity/integrity rejected.** Native rendered user messages as plain `UILabel.text` while measuring through a separate `NSString.boundingRect` path. A long Markdown/link-bearing message visibly differed from official Web and the Native bubble truncated mid-message.
3. **Relaunch/history read rejected; root cause identified.** On relaunch, account/session probes were HTTP200 and state `verified`. The conversation-list request alone returned HTTP403; current source then called `invalidateAndCancel()` on the shared transient session, cancelling the selected Detail request. The Detail cancellation branch returned without finishing/removing its current operation. Later Detail requests coalesced onto that zombie operation, so authoritative history/user rows remained absent while external live reasoning/tool state could still render and the UI stayed on `正在读取会话…`.
4. **Progressive final-body source remains unresolved.** b77 structure-only DOM evidence changed only after the plural page-owned response had already exposed the full final body. No evidence authorizes DOM text, WebSocket bodies, fake typewriter streaming, Native polling, resume synthesis, timer, retry or watchdog.

b77 remains permanently reserved and is not Stable/Frozen.

## Exact b78 correction scope

### Tool-operation presentation

- Tool text uses medium weight and primary label color so tool operations remain visually distinct from ordinary reasoning.
- Tool `paragraphSpacingBefore` is removed as a second directional spacing source.
- The icon attachment, tool text and separator/newline are assigned the tool paragraph style instead of allowing reasoning paragraph style to own the transition boundary.
- Existing tool/reasoning/final line-height relationship is retained from b77; b78 changes deterministic ownership/prominence rather than blindly increasing the numbers again.

### User-message official-like representation / truncation

- User messages now render through `userBodyAttributedText(...)` instead of plain `UILabel.text`.
- The same attributed representation is used for both rendering and `boundingRect` measurement.
- Explicit character wrapping is used.
- On supported OS versions, inline-only Markdown preserving whitespace is parsed; links receive system link color. If parsing is unavailable/fails, exact plain text is preserved.
- Privacy-safe `latestUserCharacters` is emitted on Detail response to distinguish service/projection loss from UI clipping if Runtime still fails.

### Relaunch/history Detail lifecycle

- Route-level 401/403 invalidation retires the shared transient `URLSession` with `finishTasksAndInvalidate()` instead of `invalidateAndCancel()`, so already-running Detail requests are not killed merely because another route rejected the copied transport.
- If a current Detail request is cancelled for another legitimate reason, the cancellation branch now calls `finishDetailOperation(...)` so the operation cannot remain forever coalescible.
- No retry, timer, watchdog, polling, fallback, duplicate Send or second state owner was added.

## Retained architecture / protocol boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned observation transport only; it is not a second conversation/message store.
- b67 local Native Send -> one protected official Web Send -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile remains Runtime accepted.
- b72 tested A-generating + B-send/generate ownership remains Runtime positive.
- b76/b77 cross-platform thinking/reasoning/tool adoption remains positive even when official page-owned `/resume` returns HTTP404 JSON and the page follows its own read path.
- `assistant:thoughts` / inline COT remain non-presentational.
- No Native polling/cadence, Native resume/offset synthesis, duplicate Send, retry/timer/watchdog, guessed fallback, compatibility shim, second response owner, fake final streaming, DOM-body authority or WebSocket-body authority.

## Evidence classification

- Code written: **Yes — clean product commit `180065e0...`; exact product/config source `031b1a1f...`**
- Exact-scope / `git diff --check`: **Passed**
- Xcode 16.4 Simulator build: **Passed — final validation `33482721335 / 99775722851`**
- Formal Push CI: **Passed — `33482983693 / 99776545604`**
- Formal PR CI: **Passed — `33482987997 / 99776557269`**
- Artifact produced: **Yes — canonical Push Artifact `9790836559`**
- Package identity verified: **Yes — artifact ZIP digest, IPA sidecar/hash, built Info.plist and arm64 Mach-O independently inspected**
- Runtime/manual/real-device b78: **Pending / Unverified**
- Stable/Frozen Send: **No**

## Exact next action

Human b78 real-device gate using the canonical Push IPA.

Test in this order so one pass covers the three user-reported defects plus retained response behavior:

1. **Tool presentation:** expand a response with multiple GitHub/tool operations. Confirm tool rows are clearly more prominent than normal reasoning and that the vertical rhythm above/below each tool operation is visually consistent. Screenshot any rejection.
2. **User message parity/integrity:** open the same round that contains a long link/Markdown-bearing user message. Confirm the user bubble renders the full message without mid-text clipping and that inline link presentation is substantially consistent with official Web. Screenshot any mismatch.
3. **Relaunch during external active response:** on another platform start a sufficiently long response in an existing conversation; while it is still reasoning/generating, kill Native and relaunch into that conversation. Confirm authoritative history **including the latest user message** appears, `正在读取会话…` terminates normally, and external reasoning/tools can still be adopted.
4. After step 3, export diagnostics even if it passes. The decisive b78 evidence is: account/list/Detail statuses, presence/absence of `authTransport.retired`, a terminal Detail operation, no permanent `detail.coalesced` zombie, `latestUserCharacters`, and retained `externalSnapshot` reasoning/tool lifecycle.
5. Regression-check local protected Send and b72-style concurrent ownership when practical.

Do not allocate b79 until b78 Runtime evidence is classified. CI/Artifact/package success is not Runtime success.