# DEV-send-stream

## Status

**Active — protocol discovery for the current b75 external-response defect is now complete. b67 local protected-Send Runtime and b72 tested A/B simultaneous ownership remain accepted. Exact b75 remains valid/permanently reserved but Runtime partial/rejected. Fresh visible-Web evidence proves current official Web may receive page-owned `/resume` HTTP404 JSON and then follow the still-active response through its own `stream_status` + plural `/backend-api/conversations/{conversation}` reads. The final structure probe proves that plural `messages[]` already carries the same service-message family needed for thinking preamble, tool invocation/result, reasoning recap and final-answer projection while `stream_status=IS_STREAMING`, then a finished final snapshot after `COMPLETE`. This closes the Human Web Rule Lab gate and authorizes one minimal b76 observation-only product experiment. b75 typography 26/18.2/18.2 remains visually rejected and will be increased in the same coherent candidate. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged at the final pre-allocation guard
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal branch head before the final evidence docs: `1e41131b85a4de042d57df0c4e197cb165379810`
- Exact b75 product/config source: `b77303b8870dc25851dbffbf38ffc153a47bbcb2`
- Exact b75 Candidate / Build: `DEV-send-stream-0.1.0-b75` / `0.1.0 (75)`
- Canonical b75 Artifact: `9772079468`
- b39-b75 permanently reserved
- Earliest next identity: `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` after one final uniqueness check
- Stable/Frozen Send: No

## Resume / identity guard

The existing Work was resumed from the supplied historical transcript and repeatedly reconciled against GitHub truth. Immediately before this gate closed:

- PR #29 remained open, mergeable and unmerged, base `main`, head `dev/send-stream-20260829`;
- PR base and actual `main` were both `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- head matched the current checkpoint lineage;
- no competing Active development checkpoint/candidate conflict was found;
- b76 remained unallocated in the current task/repository evidence;
- all takeover/probe commits remained docs-only; b75 product source was unchanged.

## Retained boundaries

- `ConversationRepository` is the sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` is sole native auth/account owner; `WKWebsiteDataStore.default()` is sole persistent auth-secret authority.
- Covered official Web is browser challenge/protected-Send/page-owned read transport only, never a second conversation/message/response store.
- b67 local Native Send -> one protected `/backend-api/f/conversation` -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile remains accepted.
- b72 tested A-generating + B-send/generate simultaneous-generation remains positive.
- `assistant:thoughts` and inline COT remain non-presentational.
- No Native polling, Native resume/offset construction, WebSocket body authority, duplicate Send, retry/timer/watchdog, fallback, compatibility shim or second state owner.

## Exact b75 Runtime classification

- Positive: b75 no longer creates a false Native failure merely because a matching page-owned `/resume` was observed; exact HTTP200 `text/event-stream` validation is retained.
- Rejected: three covered-production external-adoption attempts returned page-owned `/resume` HTTP404 JSON and produced no Native live reasoning/tool/final stream.
- Geometry: cooperative scheduling executed, but worst-case Back responsiveness remains open because the supplied run did not reproduce the former extreme case.
- Typography: tool/reasoning/final values `26 / 18.2 / 18.2` were visibly rejected as still too tight. The next candidate must increase visible vertical rhythm while keeping reasoning/final measurement and rendering identical and retaining the established reduced-height relationship.

## Current visible-Web evidence

### Probe 1 — `/resume` 404 is current official-page behavior

`docs/project/runtime-evidence/DEV-send-stream-b75-visible-web-reprobe.md`

Visible official Web independently reproduced:

`stream_status 200 -> matching page-owned {conversation_id,offset} /resume -> 404 JSON -> repeated page-owned stream_status + plural conversation GET`

No later HTTP200 SSE was observed in that capture.

### Probe 2 — page-owned plural snapshots advance while streaming

`docs/project/runtime-evidence/DEV-send-stream-b75-visible-web-polling-structure.md`

- `stream_status` is `{status}` and moves `IS_STREAMING -> COMPLETE`.
- plural conversation responses use top-level `messages[]`, not singular `mapping`.
- page-owned snapshots change while generation is active.
- WebSocket remains structural-only and unused.

### Probe 3 — plural `messages[]` semantics are sufficient

`docs/project/runtime-evidence/DEV-send-stream-b75-plural-message-semantics.md`

The final structure-only capture proves the plural linear entries are the same service-message family already understood by the current singular parser. During `IS_STREAMING` the active-response segment exposes:

- visible thinking preamble: assistant/all/text + `is_thinking_preamble_message=true`;
- tool invocation: assistant/non-all/code + completed invocation metadata including connector payload and parent identity;
- exact-parent tool result with invoked-resource metadata;
- hidden thoughts / inline COT that remain non-presentational;
- `reasoning_recap` with `reasoning_ended` + `collapse`;
- final assistant text with `status=in_progress` while active;
- after `COMPLETE`, the corresponding final assistant is `finished_successfully`, `end_turn=true`, with completed final text.

The plural response is a paged/rolling window: observed counts changed `125 -> 110 -> 116 -> 120 -> 124`; **message count is not a monotonic cursor or response identity**. The active segment must instead be bounded by the latest user service message and the following service messages.

## b76 authorized product rule

A single b76 experiment is now authorized, subject to the final uniqueness guard:

1. Extend the existing covered-page fetch observer to clone only the page's **already-issued** matching `stream_status` and plural-conversation responses.
2. Native must never initiate or schedule those requests.
3. Validate target conversation identity and derive only the service-message segment after the latest user entry.
4. Feed each page-owned snapshot into the existing Repository live-response runtime as an **atomic deterministic projection**, not append-only duplicate deltas and not a second message store.
5. Reuse the already accepted service-message rules for thinking preamble, exact-parent tools, hidden thoughts, reasoning recap and final text.
6. Keep current `/resume` HTTP200-SSE support if the page actually produces it; keep strict 200/SSE validation. A 404 during external observation is informational, not a Native response failure, because the page-owned plural read path is now current evidenced behavior.
7. When page-owned `stream_status` becomes `COMPLETE`, consume the following plural snapshot, then terminal/reconcile once.
8. Do not parse WebSocket body content.
9. In the same candidate, increase the rejected tool/reasoning/final vertical rhythm while preserving the reduced reasoning/final relationship and shared measurement/rendering paragraph style.

## Candidate allocation

Protocol evidence is sufficient; b76 may now be allocated once after the final exact uniqueness check. Exact identity, source SHA, CI, Artifact and package hash must be written here immediately after allocation/production.

## Exact next action

**AI-owned implementation gate:** final b76 uniqueness guard -> allocate `DEV-send-stream-0.1.0-b76` / Build 76 exactly once -> implement the observation-only plural snapshot bridge + vertical-rhythm correction -> `git diff --check` + Xcode 16.4 Simulator build -> CI/Artifact/package verification -> update durable project docs/checkpoint -> hand exact IPA to the user for the real-device Runtime gate.

The next Human Gate is the exact b76 device test. Do not claim external adoption, visual spacing, worst-case Back behavior or Stable/Frozen status before that Runtime evidence.
