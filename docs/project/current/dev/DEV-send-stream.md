# DEV-send-stream

## Status

**Active — b67 protected-Send transport remains Runtime accepted. Exact b72 Runtime positively supports the tested A-generating + B-send simultaneous-generation path. Exact b73 is a valid/reserved package and current iPhone/iOS17 Runtime is partial: the semantic reasoning/tool direction is retained, but three concrete next gates now exist — long-conversation entry stalls on full historical geometry rebuild, main tool-row vertical spacing is still too tight, and externally initiated generation is not adopted into the Native Repository live-response lifecycle. b74 is allocated for the evidence-backed corrections/investigation below. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal head before this checkpoint write: `993e3afc54bc8096ef123f0a3c8b330665074816` — docs-only after b73.
- Exact b73 product/config source: `4edda892a04a1a07f4a07e74b135b969ea82193e`
- b73 Candidate: `DEV-send-stream-0.1.0-b73`
- b73 Version / Build: `0.1.0 (73)`
- b73 Push CI: `33408695143 / 99542593642` — success
- b73 PR CI: `33408698697 / 99542605699` — success
- b73 Artifact: `9764247402`
- b73 Artifact ZIP digest: `sha256:718c2f4fd0fe3521f7469f5996f6944960ffdaa3b2829c0c17e340ebd41dd206`
- b73 IPA SHA: `8285ba9d5f63207feb2eaf722ec722a886f3ee88956236a89a716ad58b884113`
- b39-b73 permanently reserved.
- **Allocated next Candidate: `DEV-send-stream-0.1.0-b74` / `0.1.0 (74)`; no product source / CI / Artifact exists yet.**
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

The diagnostics localize the delay to historical presentation geometry, not a network load:

- long resident conversation, 32 authoritative messages / 68 presentation rows: repeated `messagePresentation.rebuilt` durations approximately `1373–1427ms`, of which `geometryDurationMs` is approximately `1348–1393ms`; `resident.firstVisible` is approximately `1375–1429ms`;
- the same run's short resident conversation is approximately `120–140ms` first-visible;
- resident-hit reproductions do not issue a new Detail request before the stall.

Current source confirms `apply(_:) -> rebuildRoundProjection() -> rebuildPresentationGeometry(...)` clears/recomputes every historical row metric/offset on every resident re-entry. The expensive path calls `ConversationMessageCell.metrics(...)` / `boundingRect` across all display chunks even when the same resident content, layout width and relevant presentation state are unchanged.

Exact b38 used the same deterministic full-rebuild design; therefore this is not evidence to revert b38 geometry. It is new Runtime evidence justifying a minimal **in-process derived-geometry reuse** for unchanged resident presentation state. It must cache only derived presentation metrics/offsets/content-height, never authoritative message bodies or a second message store, and invalidate deterministically on content/projection change, layout width, timestamp preference or historical reasoning-expansion state that changes row heights.

### 2. Tool-row rhythm remains too tight

User explicitly requests more vertical spacing above and below every visible tool call. Current b73 main timeline uses `toolParagraph.minimumLineHeight = 30` and `paragraphSpacing = 9`; this remains visually insufficient in the supplied recording. b74 may increase only the tool-line vertical rhythm; do not change tool ordering, semantic filtering, titles, inputs, parser or response ownership for this adjustment.

### 3. External-platform active generation is a real lifecycle gap and is the priority gate

User reports: send a question from another platform, then enter that conversation in this client. Official iOS/Web can show the active thinking state, but this Native client shows neither `正在思考` nor the ongoing reasoning process.

Current source explains the gap:

- Repository `beginLiveResponse(conversationID:promptText:)` is entered only for a local Native Send;
- `CoveredWebSendExecutor` installs the browser parser, but its fetch wrapper currently parses `/backend-api/f/conversation` only while page-local `activeSend == true` for this client's own submit: `if (!isSend || !activeSend) return originalFetch(...)`;
- without a local Send there is no `activeEvents` callback and no Repository live snapshot to own external response events.

This is not a missing-label bug. The missing feature is **adopting an already-active externally initiated response into the existing Repository response lifecycle when the user enters that conversation**.

Historical b45 Runtime proves the official browser has a no-resend continuation route `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` returning HTTP200 SSE and normal terminal grammar after an interrupted response. It does **not** prove that current cross-device live adoption uses `/resume`, what the current offset is, or whether Web now uses WebSocket/another page-owned transport for this case. The user's current observation proves official Web can receive the state, but not the exact transport shape.

Therefore b74 must not guess `/resume`, add polling, or synthesize a fake `正在思考`. Before external-adoption product code, use the existing Web Rule Lab/current official page to capture the smallest structural evidence identifying the actual page-owned cross-device continuation mechanism. Once identified, the intended ownership remains:

`page-owned external active-response transport observed -> Repository creates/adopts one external live response operation for the authoritative conversation -> existing reasoning/tool/final parser -> Native presentation -> deterministic terminal authoritative reconciliation`.

No optimistic prompt is invented for an external response; the authoritative user message remains Detail/Repository data. No second Send is issued.

## b74 planned minimal scope

Evidence-backed product changes allowed before/alongside the external-transport probe:

1. `ConversationFeature.swift`: add bounded in-process historical presentation-geometry reuse for unchanged resident conversation presentation, with deterministic invalidation and no second message authority.
2. `ConversationFeature.swift`: increase main tool-row top/bottom rhythm only.
3. External active-response adoption: **probe first**. Product source changes only after the current official browser transport shape is evidenced. Likely integration surfaces are `RootViewController.swift` covered executor + existing Repository response runtime, but no route/mechanism is authorized yet.
4. Xcode/workflow identity only after the complete coherent b74 product candidate is ready for CI/Artifact.

## Batch recovery point — b74

Known baseline:

- formal branch head entering b74 work: `993e3afc54bc8096ef123f0a3c8b330665074816`;
- PR #29 open / mergeable / unmerged;
- actual main `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- exact b73 product source/Artifact remain fixed as recorded above;
- no other Active development checkpoint exists;
- repository search found no existing `DEV-send-stream-0.1.0-b74` identity before allocation.

Allocated identity:

- Candidate `DEV-send-stream-0.1.0-b74`;
- Version / Build `0.1.0 (74)`;
- Artifact/product source: not yet emitted.

Write batches:

1. **Confirmed complete:** current b73 Runtime classification and b74 allocation in this checkpoint.
2. **Next:** implement and statically audit only the evidence-backed geometry reuse + tool-spacing changes on a tooling assembly branch from this checkpoint head.
3. **Then:** obtain current official-Web structural evidence for externally initiated active-response continuation using Web Rule Lab; update `WEB_SEND_ADAPTER.md` rule only if evidence supports a specific mechanism.
4. **Then:** implement the smallest Repository-owned external-adoption bridge, run scope/diff/compile checks, promote one clean b74 product/config source, Push+PR CI, Artifact/package verification.
5. **Then:** iPhone/iOS17 Runtime gate covering repeated long-conversation switching, tool spacing, local Send regression, external-platform active generation adoption, hidden-thought exclusion and b72 simultaneous-generation regression.

Recovery must not touch b73 product identity, must not regress b67/b72 transport/concurrency, must not invent `/resume` semantics, and must not produce a b74 Artifact before the external-adoption mechanism is evidenced and the coherent candidate is complete.

## Exact next action

Implement the deterministic geometry-reuse + tool-spacing patch and prepare the smallest Web Rule Lab probe for the external-platform active-generation reproduction. If the probe identifies the official continuation transport, implement that exact mechanism in b74; otherwise stop at the genuine human probe evidence gate rather than guessing.
