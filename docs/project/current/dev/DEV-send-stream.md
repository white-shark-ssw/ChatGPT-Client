# DEV-send-stream

## Status

**Active — b67 protected-Send transport remains Runtime accepted. Exact b72 Runtime positively supports the tested A-generating + B-send simultaneous-generation path. Exact b73 is a valid/reserved package and current iPhone/iOS17 Runtime is partial: the semantic reasoning/tool direction is retained, but three concrete next gates now exist — long-conversation entry stalls on full historical geometry rebuild, main tool-row vertical spacing is still too tight, and externally initiated generation is not adopted into the Native Repository live-response lifecycle. b74 is allocated for the evidence-backed corrections below. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal evidence head before the earlier b74 product assembly: `c10b295e28a4075c8b10ee33e928f92cebe82dd0`.
- Formal head at 2026-09-01 session resume before this checkpoint write: `d3398ccae6b3764ef3ae7f9ab4daec960a2fe0e6` — docs-only direct child of `c10b295e...`.
- Exact b73 product/config source: `4edda892a04a1a07f4a07e74b135b969ea82193e`
- b73 Artifact: `9764247402`
- b73 IPA SHA: `8285ba9d5f63207feb2eaf722ec722a886f3ee88956236a89a716ad58b884113`
- b39-b73 permanently reserved.
- **Allocated next Candidate: `DEV-send-stream-0.1.0-b74` / `0.1.0 (74)`.**
- **Previously assembled/compiled b74 product/config tree source: `17bc52281e38fe3eca76777fd280256d1e5acc2b`; no Artifact exists. Because it descends from `c10b295e...` while formal now descends through docs-only `d3398cca...`, it is compile/diff evidence and must be cleanly reassembled onto the latest formal docs head before promotion.**
- Stable/Frozen Send: No.

## Retained accepted boundaries

- b67: one local Send -> one protected official-page Send -> HTTP200 same-response SSE -> Repository updates -> terminal/reconcile is Runtime accepted.
- b72: tested A-generating + B-send simultaneous-generation is Runtime positive; do not regress the per-conversation covered executor.
- `ConversationRepository` remains sole conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole account authority; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/continuation transport only; full Web conversation rendering stays rejected.
- b69 chronological reasoning/tool timeline + exact-parent association remain retained.
- b38 deterministic long-message geometry/manual layout + quick navigation remain accepted; any performance correction must preserve the same derived geometry semantics.
- `assistant:thoughts` and `inline_cot_expandable_content` remain non-presentational.
- No retry/polling/timer/watchdog/fallback/compatibility shim/second message or response store.

## Exact b73 Runtime evidence — 2026-09-01 user recording + diagnostics

User supplied `RPReplay_Final1788192013.mp4` and `ChatGPTClient-Diagnostics-20260831-160234.json` from exact Build73 use.

### 1. Conversation-entry stall is confirmed and localized

The recording visibly shows repeated taps into a long resident conversation where the list selection/highlight changes immediately but the detail transition waits roughly 1–1.5 seconds.

Diagnostics localize the delay to historical presentation geometry, not network:

- long resident conversation, 32 authoritative messages / 68 presentation rows: repeated `messagePresentation.rebuilt` durations approximately `1373–1427ms`, of which `geometryDurationMs` is approximately `1348–1393ms`; `resident.firstVisible` approximately `1375–1429ms`;
- same run short resident approximately `120–140ms` first-visible;
- resident-hit reproductions do not issue a new Detail request before the stall.

Current source confirms `apply(_:) -> rebuildRoundProjection() -> rebuildPresentationGeometry(...)` clears/recomputes every historical row metric/offset on resident re-entry. Exact b38 used deterministic full rebuild, so b74 does not replace b38 geometry; it adds bounded in-process **derived geometry reuse** for unchanged resident presentation. Cache contains only projection/metrics/offsets/content-height/answer rows and is keyed/invalidation-bound by authoritative current node, width, timestamp preference and historical reasoning expansion state. No message body or second conversation store is cached.

### 2. Tool-row rhythm remains too tight

User explicitly requests more vertical spacing above and below each visible tool call. b74 raises only the main tool-line vertical rhythm; it does not change tool ordering, semantic filtering, titles, inputs, parser or response ownership.

### 3. External-platform active generation lifecycle gap

User reports: send on another platform, then enter that conversation in this client. Official iOS/Web shows active thinking, but this Native client previously showed neither `正在思考` nor ongoing reasoning.

Current source explained the gap: local Repository live response was created only for local Native Send, and the covered fetch wrapper parsed `/backend-api/f/conversation` only while page-local `activeSend == true`.

The 2026-09-01 Web Rule Lab capture closes the current transport-shape gap. After another platform started the response and official Web entered the same conversation, the page:

- opened its normal user-level WebSocket (short string frames observed, not proven as reasoning/final body transport);
- loaded conversation/bootstrap state;
- requested `GET /backend-api/conversation/{id}/stream_status` -> HTTP200 JSON;
- issued **page-owned** `POST /backend-api/f/conversation/resume` with JSON keys exactly `conversation_id` + `offset`;
- received HTTP200 `text/event-stream`.

Current production rule: external adoption may observe and parse only the official page's own matching `/resume` SSE. Native must not construct the request, derive/guess `offset`, poll `stream_status`, replay browser headers, or issue a second Send. WebSocket remains structural evidence only.

## Exact b74 assembled implementation / compile evidence

UI-only patch precursor:

- tooling run `33414597158 / 99562115400` succeeded;
- scope `ConversationFeature.swift` only;
- `git diff --check` passed;
- Xcode 16.4 iOS Simulator build succeeded;
- temporary clean code commit `894eea1` is compile evidence only, not product identity.

Integrated external-adoption assembly:

- first integrated run `33417148467 / 99570443019` failed tooling-only before scope/compile because the patcher expected obsolete synthetic user ID `live-user-*`; no product branch/Artifact emitted;
- corrected integrated run `33417444152 / 99571391754` succeeded completely: patch application, exact scope/invariant audit, `git diff --check`, Xcode 16.4 Simulator build, clean product-code branch output;
- clean product-code commit `07c3c81231745361a629225c39a21729c887a6c3`, direct parent `c10b295e28a4075c8b10ee33e928f92cebe82dd0`;
- final workflow identity commit produced assembled source `17bc52281e38fe3eca76777fd280256d1e5acc2b`;
- detached compare `c10b295e...17bc5228` changes exactly:
  - `.github/workflows/ios-foundation.yml`
  - `ChatGPTClient.xcodeproj/project.pbxproj`
  - `ChatGPTClient/Conversation/ConversationFeature.swift`
  - `ChatGPTClient/RootViewController.swift`
- no tooling/docs files are in that product range.

Implemented behavior:

1. Historical resident geometry reuse preserves b38-derived row geometry and reuses it only for unchanged resident presentation identity; deterministic invalidation remains.
2. Main tool-line vertical rhythm is enlarged above/below.
3. `CoveredWebSendExecutor` can observe a selected existing conversation without sending.
4. Its bridge watches **page-owned** `/backend-api/f/conversation/resume`, verifies body `conversation_id` equals the page/current authoritative target, performs the original fetch unchanged, returns the original response to official Web, and reads a `response.clone()` through the already accepted parser grammar.
5. No Native `/resume` request/offset/header construction and no stream-status polling is added.
6. On first matching page-owned resume observation, the existing `ConversationRepository` response runtime creates one external live generation with empty optimistic prompt and phase thinking; no second response store exists.
7. Subsequent reasoning/tool/final/terminal events use the existing `consumeLiveResponseEvent` path; terminal uses existing authoritative reconciliation.
8. External live presentation omits a synthetic user bubble because the authoritative external prompt is already Detail/Repository state.
9. Local Send `/backend-api/f/conversation`, accepted composer selectors and b72 per-conversation busy-response executors remain present.
10. User-level WebSocket is not parsed as response content.

Evidence ladder at this checkpoint: **Code written / exact scope audited / Simulator compile passed on the previously assembled product tree / Push CI pending / PR CI pending / Artifact not yet produced / Runtime pending / Stable-Frozen No.**

## Batch recovery point — b74 clean reassembly

Known baseline/identity at session resume:

- formal branch head before this checkpoint write: `d3398ccae6b3764ef3ae7f9ab4daec960a2fe0e6` — docs-only direct child of `c10b295e...`;
- previously assembled product source `17bc52281e38fe3eca76777fd280256d1e5acc2b` is a sibling descendant of `c10b295e...`, not a fast-forward of `d3398cca...`;
- PR #29 open / mergeable / unmerged;
- actual main `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- current `docs/project/current/dev/` contains only `DEV-send-stream.md` plus README;
- Candidate `DEV-send-stream-0.1.0-b74`; Version/Build `0.1.0 (74)`;
- no b74 Artifact emitted; b74 remains allocated but not permanently artifact-reserved.

Completed batches:

1. b73 Runtime classification + b74 allocation.
2. current Web Rule Lab cross-device `/resume` evidence + `WEB_SEND_ADAPTER.md` rule update.
3. UI geometry reuse/tool-spacing compile proof.
4. integrated external-adoption assembly + exact four-file product tree `17bc5228...` compile proof.
5. docs-only checkpoint commit `d3398cca...` landed after that assembly, creating the current topology mismatch before product promotion.

Remaining deterministic batches:

1. verify the exact formal head produced by **this checkpoint write** and use that commit as the sole clean reassembly base;
2. create an isolated tooling/assembly branch from that exact formal docs head;
3. replay exactly the four-file detached product diff represented by `c10b295e...17bc5228`, run `git diff --check`, assert exact four-file scope and retained local-Send/composer/resume/no-retry invariants, then run Xcode 16.4 iOS Simulator build;
4. emit one clean b74 product/config commit/branch whose direct parent is the latest formal docs head; audit parent + exact four-file diff before promotion;
5. final Guard branch/PR/main/current checkpoint; non-force fast-forward formal branch to that exact source only if unchanged;
6. lock exact-head Push + PR CI without inserting docs commits;
7. if both succeed, use Push Artifact as canonical b74 package, independently verify ZIP/IPA identity and permanently reserve b74;
8. then sync checkpoint/durable docs/PR as docs-only commits;
9. human iPhone/iOS17 Runtime: repeated long resident re-entry, tool spacing, external active response adoption, local Send regression, simultaneous A/B regression, hidden-thought exclusion and b38 quick-navigation.

Recovery must not rewrite b73 identity; must not change the already-audited b74 product semantics while repairing topology; must not construct Native resume/offset/polling; must not create a second response/message authority; and must not produce a b74 Artifact until the clean direct-parent source passes the exact compile/scope checks above.

## Exact next action

After this checkpoint write, re-read the formal branch to obtain its exact new docs-only head. Reassemble the already-audited `c10b295e...17bc5228` four-file product delta directly on that head, compile/audit it, and only then promote by non-force fast-forward for exact-head Push/PR CI. Runtime remains pending until the exact Build74 IPA is installed and tested.
