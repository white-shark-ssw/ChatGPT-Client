# DEV-send-stream

## Status

**Active — b67 local protected-Send transport remains Runtime accepted; b72 tested A-generating + B-send simultaneous ownership remains Runtime positive. Exact b75 remains valid/permanently reserved but Runtime partial/rejected. Current visible official Web now independently proves the active external-response fallback shape: `stream_status = IS_STREAMING`, page-owned matching `/resume` returns HTTP404 JSON, then the page continues repeated page-owned `stream_status` + plural `/backend-api/conversations/{conversation}` reads whose `messages` count grows during generation and stops at terminal `COMPLETE`. This is current evidence that the official page can follow the response without a successful resume SSE, but the plural `messages[]` entry schema is not yet evidenced. One final structure-only `messages[]` probe is required before b76 product code. b76 remains unallocated. b75 typography 26/18.2/18.2 remains visually rejected as too tight. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Routing aliases / keywords: Send, stream, reasoning, tool, external resume, cross-platform response, continuation, 行高
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal branch head after this checkpoint write: current docs-only descendant of `c8363d1bdb6116b015d8b72578fa0898eb11eba5`
- Exact b75 product/config source: `b77303b8870dc25851dbffbf38ffc153a47bbcb2`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b75` / `0.1.0 (75)`
- Canonical b75 Artifact: `9772079468`
- IPA SHA: `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`
- b39-b75 permanently reserved
- b76: not allocated; earliest possible identity remains `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` after final allocation guard
- Stable/Frozen Send: No

## Resume / identity guard

This conversation resumed the existing Work and revalidated branch/PR/base/candidate identity before product edits.

- formal branch and PR #29 matched the checkpoint;
- PR #29 was open, mergeable and unmerged;
- `main` remained `d323b9eed2dda75b9986fc06e14014d3e9b365fb` at the guard;
- no competing Active development checkpoint/candidate conflict was found;
- b76 remained globally unused;
- takeover and all Web Rule Lab evidence commits are docs-only; b75 product/config source remains `b77303b8870dc25851dbffbf38ffc153a47bbcb2`.

## Retained accepted boundaries

- `ConversationRepository` is the sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` is sole verified auth/account owner; `WKWebsiteDataStore.default()` is sole persistent auth-secret authority.
- Covered official Web is browser challenge/protected-Send/page-owned continuation transport only, never conversation/message/response authority.
- b67 local Native Send -> one protected `/backend-api/f/conversation` -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile remains accepted.
- b72 tested A-generating + B-send/generate simultaneous-generation remains positive.
- b38 deterministic bounded message geometry, Copy, semantic rounds and O(1) quick-navigation remain accepted semantics.
- `assistant:thoughts` and `inline_cot_expandable_content` remain non-presentational.
- No speculative retry, Native polling, timer, watchdog, fallback, compatibility shim, duplicate Send, second message store or second response store.

## Exact b75 Runtime classification

- b75 fixed the b74 false Native failure: matching page-owned `/resume` is not accepted until exact HTTP200 `text/event-stream` validation.
- Exact iPhone/iOS17 covered-production Runtime observed three matching page-owned `/resume` responses as HTTP404 JSON while another platform's response was still active; no external Native live generation was created.
- Cooperative history geometry code ran; the supplied b75 export did not reproduce the former worst-case Back stall, so that sub-gate remains unclosed.
- b75 tool/reasoning/final line-height values `26 / 18.2 / 18.2` were visually rejected as too tight. The eventual b76 correction must increase visible vertical rhythm while keeping reasoning/final measurement/rendering consistent.

## Visible Web Rule Lab evidence — current continuation behavior

### Probe 1 — current visible Web reproduces `/resume` 404

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b75-visible-web-reprobe.md`.

Current visible official Web independently reproduced:

`stream_status 200 JSON -> page-owned matching {conversation_id, offset} /resume -> 404 JSON -> repeated page-owned stream_status + plural conversation GETs`

No later `/resume`, second Send or HTTP200 SSE continuation appeared in the captured window. This supersedes the earlier same-day HTTP200-SSE `/resume` run as the current continuation rule while preserving it as historical evidence.

### Probe 2 — page-owned polling carries incremental conversation state

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b75-visible-web-polling-structure.md`.

The second structure-only capture establishes:

- `stream_status` response shape is exactly `{status}` in this run;
- status remains `IS_STREAMING` during generation and later transitions to `COMPLETE`;
- plural `/backend-api/conversations/{conversation}` is a different schema from singular Detail: top-level `messages` array + `current_node`, not `mapping + current_node`;
- while status remains `IS_STREAMING`, page-owned plural snapshots changed `messages.__count` **113 -> 116 -> 120 -> 125**, with `update_time` advancing;
- later snapshots remained at 125, then status transitioned to `COMPLETE` and the terminal plural snapshot remained 125;
- WebSocket JSON arrays occurred alongside this cycle, but their bodies were intentionally not captured and they are not response-body authority.

**Conclusion:** current official Web can follow an external active response after `/resume` 404 using its own already-existing status/conversation read activity. This does not authorize Native to reproduce the polling cadence. The remaining unknown is the exact `messages[]` entry structure and whether the growing entries map to evidenced reasoning/tool/final service-message semantics.

## Source correlation

- Current `CoveredWebSendExecutor` correctly rejects resume 404 and therefore must not be weakened to accept a non-SSE response.
- Current `ConversationRepository` parses the accepted singular Detail `mapping + current_node` current branch and already owns the evidenced reasoning/tool/user-visible filtering semantics.
- The plural page-owned response is not that schema. Do not guess a transformation.
- If the final probe proves plural `messages[]` entries are the same service message objects or a narrow safely transformable subset, the preferred b76 direction is observation-only interception of page-owned responses already issued by official Web, feeding an evidenced transformation into the existing Repository response lifecycle. Native must not initiate the six-second polling.

## b76 allocation rule

b76 is permitted by concrete b75 defects but is **not allocated yet**. Allocate it only after the final `messages[]` structure probe defines one minimal current transport/observation rule and after the larger reasoning/tool/final vertical-rhythm correction is defined as the same coherent candidate scope.

Do not use b76 for guessed WebSocket parsing, Native `stream_status` polling, Native resume/offset construction, retry/timer machinery, or a second response store.

## Exact next action

**Human-only final Web Rule Lab structure gate:** on a fresh externally active response, inspect only the page-owned plural `/backend-api/conversations/{conversation}` JSON response's bounded `messages[]` structure. Record per-entry root keys, role/status/recipient/content type, body character counts only, metadata key names and safe reasoning/tool enums/booleans; compare the last bounded entries across repeated snapshots while `stream_status` remains `IS_STREAMING`. Never export text, tool bodies, raw IDs, auth/challenge values or Web storage.

After that evidence arrives: update `WEB_SEND_ADAPTER.md` and durable project state, run a light/final identity guard, define or reject the observation-only plural-message bridge, allocate b76 once if justified, implement the minimal transport correction plus larger vertical rhythm, then compile/CI/package one coherent Runtime candidate.
