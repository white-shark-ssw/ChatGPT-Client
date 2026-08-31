# DEV-send-stream

## Status

**Active — b67 protected-Send transport remains Runtime accepted; exact b72 Runtime positively supports the tested A-generating + B-send simultaneous-generation path. Exact b73 Runtime exposed three concrete b74 needs: long resident re-entry geometry cost, insufficient main tool-row spacing, and no Native adoption of externally initiated active responses. Exact b74 is now Code/scope/Simulator/Push+PR CI/Artifact/package verified and permanently reserved. Real-device Runtime remains pending. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b74 product/config source: `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`
- Candidate: `DEV-send-stream-0.1.0-b74`
- Version / Build: `0.1.0 (74)`
- Final clean-reassembly run/job: `33420128454 / 99580192017` — success
- Push CI run/job: `33420408779 / 99581104920` — success
- PR CI run/job: `33420412792 / 99581117817` — success
- Canonical Push Artifact: `9768668727`
- Artifact ZIP digest: `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`
- IPA: `ChatGPTClient-0.1.0-b74-dev-send-stream.ipa`
- IPA SHA: `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`
- Built source marker: `50dd61b8b31c`
- b39-b74 permanently reserved.
- Stable/Frozen Send: No.

## Retained accepted boundaries

- b67: one local Send -> one protected official-page Send -> HTTP200 same-response SSE -> Repository updates -> terminal/reconcile is Runtime accepted.
- b72: tested A-generating + B-send simultaneous-generation is Runtime positive; do not regress the per-conversation covered executor.
- `ConversationRepository` remains sole conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole account authority; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/continuation transport only; full Web conversation rendering stays rejected.
- b69 chronological reasoning/tool timeline + exact-parent association remain retained.
- b38 deterministic long-message geometry/manual layout + quick navigation remain accepted; b74 only reuses already-derived geometry when presentation identity is unchanged.
- `assistant:thoughts` and `inline_cot_expandable_content` remain non-presentational.
- No retry/polling/timer/watchdog/fallback/compatibility shim/second message or response store.

## Exact b73 Runtime evidence motivating b74 — 2026-09-01

User supplied `RPReplay_Final1788192013.mp4` and `ChatGPTClient-Diagnostics-20260831-160234.json` from exact Build73 use.

### Long resident re-entry stall

The recording visibly showed repeated taps into a long resident conversation where list selection changed immediately but the detail transition waited roughly 1–1.5 seconds. Diagnostics localized the delay to historical presentation geometry, not network: a 32-authoritative-message / 68-presentation-row resident repeatedly showed `messagePresentation.rebuilt` around `1373–1427ms`, geometry around `1348–1393ms`, and `resident.firstVisible` around `1375–1429ms`; short resident entries were around `120–140ms`. Resident-hit reproductions did not issue a new Detail request before the stall.

b74 therefore adds bounded in-process reuse of derived b38 presentation geometry only when authoritative presentation identity is unchanged. It does not cache message bodies or create a second conversation store.

### Tool rhythm

User explicitly requested more vertical spacing above and below visible main tool calls. b74 changes only tool-line vertical rhythm; ordering, semantic filtering, titles, parser and response ownership are unchanged.

### External active-response lifecycle gap

User reported that a question sent from another platform could be actively thinking in official clients while entering the same conversation in this Native client showed no `正在思考` or ongoing reasoning.

A current Web Rule Lab capture then established the official cross-device continuation path:

- official Web enters the target conversation and requests `GET /backend-api/conversation/{id}/stream_status` -> HTTP200 JSON;
- while the response is active, the page itself issues `POST /backend-api/f/conversation/resume`;
- observed request JSON keys are exactly `conversation_id` + `offset`;
- response is HTTP200 `text/event-stream`;
- a user-level `wss://ws.chatgpt.com/...` socket exists, but the capture did not prove it carries reasoning/final body data.

Current production rule: Native may observe/parse only the page-owned matching `/resume` SSE. Native must not construct `/resume`, choose/derive offset, poll `stream_status`, replay browser headers or issue a second Send. WebSocket remains structural evidence only.

## Exact b74 implementation

1. `ConversationFeature.swift` keeps the b38 deterministic/manual geometry model but adds bounded in-process derived-geometry reuse for unchanged resident presentation identity. Key/invalidation includes authoritative current node, layout width, timestamp preference and historical reasoning expansion state; cached data is projection/metrics/offsets/content-height/answer rows only.
2. Main meaningful tool rows receive increased vertical rhythm.
3. `CoveredWebSendExecutor` can observe a selected existing conversation without sending.
4. The page bridge observes page-owned `/backend-api/f/conversation/resume`, parses only the request body's `conversation_id` for target equality, invokes the original fetch unchanged and returns the original response to official Web.
5. For a matching resume, a `response.clone()` is consumed through the already accepted SSE/parser grammar; Native does not construct the request or offset.
6. On first matching resume observation, the existing Repository response runtime creates one external live generation with an empty optimistic prompt and `thinking` phase; no second response store is added.
7. reasoning/tool/final/terminal events reuse `consumeLiveResponseEvent`; terminal reuses the existing authoritative reconciliation path.
8. External live presentation omits a synthetic user bubble because the authoritative external user message belongs to Detail/Repository history.
9. Existing local Send `/backend-api/f/conversation`, accepted composer selectors, b72 per-conversation executor concurrency and hidden-response ownership are retained.
10. User-level WebSocket is not parsed as response content.

## b74 assembly / source evidence

The first audited integrated product tree was `17bc52281e38fe3eca76777fd280256d1e5acc2b`, built from earlier evidence head `c10b295e...`. A later docs-only checkpoint made that tree no longer fast-forwardable, so it was not promoted directly.

A recovery checkpoint was written and final clean reassembly was performed from formal docs head `6d72d3e24c34d2594ac8466167c4c01749a91374`:

- tooling branch `assembly/dev-send-stream-b74-final-20260901`;
- workflow/run/job `b74 final clean reassembly` / `33420128454 / 99580192017` — success;
- workflow replayed exactly the four product files from the already-audited `c10b295e...17bc5228` delta;
- `git diff --check` passed;
- exact changed-file scope passed;
- `git diff --exit-code 17bc5228 -- <four product files>` passed, proving final file contents match the prior audited product tree;
- local-Send route, matching `/resume`, verified composer selector, Build74 identity and no resume timer/retry/poll invariants passed;
- Xcode 16.4 iOS Simulator build passed;
- clean final product source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d` has direct parent `6d72d3e...` and changes exactly:
  - `.github/workflows/ios-foundation.yml`
  - `ChatGPTClient.xcodeproj/project.pbxproj`
  - `ChatGPTClient/Conversation/ConversationFeature.swift`
  - `ChatGPTClient/RootViewController.swift`

Final promotion Guard verified formal head/PR/main/current checkpoint unchanged, then formal branch was non-force fast-forwarded to exact source `50dd61b8...`.

## Exact b74 CI / Artifact / package evidence

### CI

- Push: `33420408779 / 99581104920` — success on exact source `50dd61b8...`.
- PR: `33420412792 / 99581117817` — success on the same exact source.
- Toolchain: macOS15, Xcode 16.4, iPhoneOS18.5 SDK.
- Release iphoneos build succeeded; target arm64 / iOS14.0.

### Canonical Artifact

Push Artifact `9768668727`, name `ChatGPTClient-DEV-send-stream-0.1.0-b74`:

- API/upload ZIP digest `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`;
- build log IPA SHA `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`;
- build log Candidate `DEV-send-stream-0.1.0-b74`;
- build log source `50dd61b8b31c`.

The Artifact was independently downloaded and unpacked after CI. Independent verification found:

- local ZIP SHA exactly `6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`;
- archive contains only the expected IPA + SHA sidecar;
- local IPA SHA exactly `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`;
- built `Info.plist`: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=74`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b74`, `DiagnosticsSourceCommit=50dd61b8b31c`, `DiagnosticsBuildConfiguration=Release`, `MinimumOSVersion=14.0`, bundle ID `com.whitesharkssw.chatgptclient`;
- executable independently identified as Mach-O 64-bit arm64;
- device family remains iPhone + iPad.

Because a valid b74 Artifact now exists, b74 is permanently reserved. Any product correction after new Runtime evidence must use the earliest unique next Candidate (currently b75), never rewrite b74.

Evidence ladder: **Code written / exact scope audited / Simulator compile passed / Push CI passed / PR CI passed / Artifact produced / package independently verified / Runtime pending / Stable-Frozen No.**

## Batch recovery point — post-b74 package docs sync

Known immutable product identity:

- exact b74 product/config source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`;
- Candidate `DEV-send-stream-0.1.0-b74`, Version/Build `0.1.0 (74)`;
- Push `33420408779 / 99581104920`, PR `33420412792 / 99581117817` — success;
- canonical Artifact `9768668727`;
- ZIP digest `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`;
- IPA SHA `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`;
- actual main `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- PR #29 remains open/unmerged.

Completed product batches: Runtime evidence classification, Web Rule Lab `/resume` evidence, adapter rule update, UI/external-adoption implementation, clean reassembly, scope/compile audit, non-force promotion, exact-head Push+PR CI, canonical Artifact and independent package verification.

Remaining docs-only batches:

1. after this checkpoint write, read its resulting formal docs-only head;
2. update durable project documents to make b74 the current exact Runtime candidate while preserving b67/b72 accepted predecessors and b73 Runtime defect evidence;
3. record page-owned matching `/resume` observation/adoption as a durable TD/rule extension without authorizing Native resume construction;
4. update `BUILD_TEST_INDEX` with exact b74 source/CI/Artifact/digests and Runtime pending;
5. audit docs-only diff and non-force fast-forward formal branch if an isolated docs assembly branch is used;
6. update PR #29 title/body to exact b74 Runtime gate, keep open/unmerged;
7. hand exact b74 IPA to the user for the human iPhone/iOS17 Runtime gate.

Docs-only commits after `50dd61b8...` must never be described as the b74 product source.

## Exact human Runtime gate — b74

On the primary iPhone/iOS17 device using exact Build74:

1. Confirm Candidate `DEV-send-stream-0.1.0-b74` and source marker `50dd61b8b31c`.
2. Repeatedly enter/re-enter the previously slow long resident conversation. Verify the prior roughly 1.4-second resident geometry rebuild stall is materially removed while message geometry/scroll/quick-navigation remain correct. Export diagnostics after the reproduction.
3. Run a response with meaningful tool calls and confirm the main tool rows have visibly larger top/bottom spacing while chronological reasoning/tool order remains correct.
4. From another platform, start a sufficiently long reasoning/tool response; while it is still active, enter the same conversation in Build74. Native should adopt the page-owned matching `/resume` stream and show `正在思考` / ongoing visible reasoning/tools/final without a duplicate Send or synthetic user bubble; terminal should reconcile authoritative history once.
5. Regression-test one normal Native local Send: one protected `/backend-api/f/conversation` -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile.
6. Regression-test b72 A-generating + B-send/generate simultaneous ownership.
7. Confirm `assistant:thoughts`/hidden thought content remains absent and b38 quick navigation/Copy/geometry semantics do not regress.

Do not allocate b75 unless exact b74 Runtime supplies a concrete defect or new evidence-backed requirement.

## Exact next action

Synchronize durable project docs and PR #29 as docs-only state, then hand the independently verified exact b74 IPA to the user. The next evidence gate after handoff is human iPhone/iOS17 Runtime only; CI/Artifact do not prove the three Runtime issues are solved.
