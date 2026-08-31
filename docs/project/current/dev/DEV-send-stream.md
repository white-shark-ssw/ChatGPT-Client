# DEV-send-stream

## Status

**Active — exact b67 production existing-conversation Send/stream Runtime passed on the primary iPhone/iOS17 device. One local Send produced one submitted event, one real protected Send, HTTP200 SSE, Native Repository-owned tool/final updates, terminal and one authoritative reconciliation. The remaining concrete product defect is Native presentation: live response currently appears in a temporary floating validation overlay instead of the conversation timeline, and authoritative historical Detail does not expose the service-marked reasoning recap as a collapsible section. b68 is now authorized for this presentation-only integration. Stable/Frozen Send remains No. PR #29 remains open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — keep open / evidence-only / unmerged
- Current actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal branch head before this checkpoint update: `face020b6ba2de0c9a9a45f7949a7d0fae3db2f7`
- Stable merged predecessor: b38
- Latest probe Runtime pass: b65
- Latest production Runtime pass: b67
- b39-b67 emitted identities are permanently reserved.
- Future serialized `DEV-composer-parity` still owns final Composer hierarchy/drafts/attachment staging; this Work keeps only the validation send trigger while integrating response/reasoning presentation.

## Exact b67 identity

- Candidate: `DEV-send-stream-0.1.0-b67`
- Version / Build: `0.1.0 (67)`
- Exact product/config source: `52ab38f16fe914ef8316bb1dc712b77c2c87a271`
- Product tree: `dcd492d142bf0035208b8466ff02b6ae7209193c`
- Push Run / Job: `33338865423 / 99330666394` — success
- PR Run / Job: `33338868896 / 99330678769` — success
- Push Artifact: `9739891865`
- Artifact ZIP digest: `sha256:7e41508c76556466ab180009a30f36b5c12cbc731197d4213387698ed54d78c2`
- IPA SHA: `3712dec92cddfe64e84fc797e1506d83231cd878633b932b9acf0e7381795497`
- Runtime export: `ChatGPTClient-Diagnostics-20260831-052810.json`
- Device: iPhone / iOS17.0

b67 package identity is valid and permanently reserved.

## Exact b67 Runtime — accepted production existing-conversation transport gate

Generation 1:

`liveResponse.started -> composer_ready x2 -> submit_result=submitted x1 -> send_observed x1 -> HTTP200 text/event-stream -> accepted visible text -> terminal -> authoritative Sync 14→16 -> live snapshot cleared`

Generation 2, tool-active:

`liveResponse.started -> composer_ready x1 -> submit_result=submitted x1 -> send_observed x1 -> HTTP200 text/event-stream -> tool activity -> thinking_active -> exact reasoning_ended -> final deltas -> terminal -> authoritative Sync 16→18 -> live snapshot cleared`

Important evidence:

1. b66 duplicate-submit defect is closed for the tested production path: repeated ready callbacks did not create a second submitted event.
2. no `send_transport_error` occurred.
3. same-response SSE reached true terminal and the existing one-shot authoritative reconciliation succeeded.
4. generation 2 briefly crossed resign-active / become-active while still completing the same response. This is positive short-interval evidence only, not the later 5/15-minute background gate.
5. user visually confirmed Send, incremental response and final synchronization worked.

Classification: **Runtime passed for the current existing-conversation production Send/stream/terminal/reconcile gate; not Stable/Frozen and not yet a complete daily-chat UI.**

## User-confirmed presentation defect after b67

The temporary `ConversationLiveResponseOverlayView` visibly floats over the conversation. The user explicitly requires:

1. active assistant output must stream inline at the bottom of the current Native conversation, not in a floating popup/overlay;
2. historical assistant messages should expose a collapsible/expandable reasoning section where authoritative service data supports it.

This is within `DEV-send-stream` because it is response/reasoning lifecycle presentation, not final Composer work or general Markdown rendering.

## b68 evidence-backed presentation boundary

Transport remains exactly b67. Do not touch the covered-Web route/selectors/SSE grammar merely to change UI.

### Live response

- `ConversationRepository.liveResponse(for:)` remains the sole response state owner.
- `ConversationDetailViewController` may derive inline presentation rows/cells from that snapshot; it must not own/copy a second response lifecycle.
- remove the Root floating response overlay.
- keep b38 deterministic message geometry/quick-navigation semantics intact.
- live final text should incrementally grow in the conversation timeline; reasoning/tool/status are Native presentation derived from the same Repository snapshot.
- do not invent a timer/debounce/poll loop.

### Historical reasoning

Authoritative Detail currently walks the full current branch but only projects ordinary user/assistant visible text. b68 may add one separate historical reasoning-summary field only when the branch contains the already-evidenced service-marked completed recap shape:

- assistant recipient `all`;
- `content.content_type == reasoning_recap`;
- non-empty `content.content`;
- `metadata.reasoning_status == reasoning_ended`;
- `metadata.reasoning_recap_type == collapse`.

Attach that recap to the next visible assistant final message for presentation. **Never expose `assistant:thoughts` or `inline_cot_expandable_content` as historical reasoning.** The historical expandable body is the authoritative recap/status, not hidden chain-of-thought.

## TD-029 production authority retained

`Native send action -> ConversationRepository response operation -> covered official Web verified composer/page-owned protected Send -> same-response SSE -> Repository incremental response state -> Native conversation presentation`.

- official page owns browser challenge + protected request execution;
- `ConversationRepository` is sole production conversation/response owner;
- `AuthSessionStore` remains auth/account owner;
- `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority;
- full Web conversation rendering remains rejected;
- Sync/Reload never resend;
- `WEB_SEND_ADAPTER.md` remains the Web-rule maintenance authority;
- `assistant:thoughts` remains non-presentational.

## Batch recovery point — b68

Known baseline before product assembly:

- formal branch head: re-fetch after this checkpoint commit;
- exact accepted product predecessor: b67 source `52ab38f16fe914ef8316bb1dc712b77c2c87a271`;
- actual main: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- PR #29 open/mergeable/unmerged;
- only Active development checkpoint is this Work.

Intended coherent write batches:

1. create a tooling-only b68 assembly ref from the new formal checkpoint head;
2. modify only the minimum Native response/history presentation surfaces justified above, plus Xcode/workflow b68 identity;
3. audit exact diff against the checkpoint head; no transport/Web Rule Lab/auth/parser grammar changes except the narrow authoritative historical `reasoning_recap` extraction;
4. re-check main/PR/conflicts, then move the formal branch once to the coherent b68 source;
5. continue through Push + PR CI, Artifact/package identity verification;
6. update runtime evidence/index/state/module/profile/plan/rules/checkpoint/PR and stop only at exact b68 iPhone/iOS17 Runtime gate.

Do not touch final Composer, attachments, auth ownership/default WebKit store, b38 quick-navigation algorithm, Web selector rules, challenge logic, or b39-b67 identities.

## Next exact action

Inspect all real `ConversationMessage` construction/comparison call sites, then assemble b68 with inline Repository-owned live response presentation + safe historical reasoning-recap disclosure. No user confirmation is required before normal CI/Artifact progression.