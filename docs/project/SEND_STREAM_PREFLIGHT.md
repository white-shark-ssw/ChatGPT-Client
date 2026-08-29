# DEV-send-stream — Evidence / Ownership Preflight

_Last revalidated: 2026-08-29 against Stable merged b38 and `DEV-send-stream` activation._

## Purpose

This file is the durable evidence/ownership gate for Phase 9 text Send, new conversation creation, streaming answer, Stop, user-visible reasoning and follow-tail.

Current real source, the selected `DEV-send-stream` checkpoint, exact Runtime evidence and the user's latest explicit requirement outrank stale details here. Historical/private protocol names are clues only until current evidence confirms them.

## Activation state

The old serialized dependency is satisfied:

- user explicitly activated `DEV-send-stream` as a new Development task;
- predecessor `DEV-conversation-round-count` is merged Stable b38; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`;
- current development base is `main@34811877896ca88c6656be6676f5466a19931ce6`;
- no other Active development checkpoint or open PR existed at activation;
- dedicated branch is `dev/send-stream-20260829`;
- b24-b38 identities are permanently reserved; the first Send/Stream Candidate must allocate a later unique identity only when a testable evidence/implementation milestone is ready.

## Accepted architecture before Send

- `ConversationRepository` remains the sole production conversation/list/read/recovery authority and is the future response owner.
- Repository mutable authority remains on its explicit main-thread execution domain.
- Existing resident identity is verified account scope + authoritative conversation ID.
- `AuthSessionStore` remains sole verified auth/account-context owner.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- native reads use transient ephemeral WebKit-derived cookies + transient bearer; copied secrets are not persisted.
- foreground selection is presentation state only; hiding A must not cancel valid A work.
- same-target obsolete Detail operations use target generation + cancellation-before-replacement; equivalent loads may coalesce.
- accepted Detail keeps authoritative `current_node` as `ConversationDetail.currentNodeID`.
- `ConversationDetailViewController` owns per-conversation viewport/scroll presentation, not server conversation state.
- b38 Stable presentation uses bounded long-message chunks, deterministic row heights/prefix offsets and one derived round projection. Send/Stream must extend this architecture rather than replace it.
- `同步最新消息` and `重载当前会话` remain explicit recovery actions and never resend/regenerate prompts.
- current accepted private protocol Runtime evidence covers read only. Send/new-chat/stream/Stop/reasoning remain unaccepted until this Work establishes exact evidence.

## Current transport and protocol evidence boundary

`AuthTransientSession` currently exposes only completion-handler `URLSessionDataTask`, which buffers full data and is not an incremental stream transport.

Recent 2026 public captures/implementations consistently indicate that current ChatGPT Web generation commonly uses `POST /backend-api/f/conversation`, with Sentinel chat-requirements and `/f/conversation/prepare` in the normal browser flow, and that naive direct replay without valid browser-generated requirements/proof can return HTTP403. Recent structural SSE evidence commonly shows `data:` frames containing a protocol marker such as `"v1"`, patch/event objects and `[DONE]`.

These external observations are useful evidence for what must be measured, but they are **not accepted account/runtime proof** and do not authorize copying a third-party replay stack.

Rules:

- do not implement Sentinel/PoW/Turnstile bypass or replay captured proof credentials;
- do not synthesize browser/device proof headers or add speculative browser fingerprints;
- do not create another persistent credential store;
- do not create a hidden/shadow WebView as production Send transport;
- do not choose a production parser/request body merely from historical or third-party examples;
- if current evidence later proves a long-lived SSE/chunked response for this account, add incremental delivery inside the existing transient-auth boundary rather than a second stream authority.

## Evidence acquisition path

Before production Send is authoritative, collect current structural evidence for both:

1. one existing-conversation Send;
2. the first Send of a new conversation.

The initial evidence path is a **visible diagnostic-only Web protocol probe** using the existing default WebKit data store. The official `chatgpt.com` page performs its own normal browser requirements flow. Diagnostic instrumentation may observe only privacy-safe structural metadata and must never become production chat transport.

Allowed diagnostic facts include:

- method + route classification;
- HTTP status and content-type classification where observable;
- request header **names only**, never values;
- JSON top-level/nested key names and structural types, never prompt/text/token values;
- whether existing/new Send use the same route;
- presence/type of conversation/message/parent/model/mode/client-state fields;
- stream event type names, patch operation/path names, structural key sets, counts and timing;
- presence/timing of authoritative conversation ID and message/response ID, recorded only as presence or irreversible short hash when native correlation genuinely needs it;
- terminal marker/event shape;
- title-generation event presence;
- server Stop network operation if naturally observable from the official page.

Never log/export:

- prompt or response text;
- reasoning text;
- raw request/response body;
- Authorization/Cookie values;
- Sentinel/proof/Turnstile/requirements/conduit token values;
- raw account/user/conversation/message/response IDs;
- complete titles or attachment contents.

## Request evidence gate

Before production Send code, establish for existing and new conversation:

- exact method + route;
- response status/content type;
- whether both paths use the same endpoint;
- currently required non-secret header names beyond the accepted auth/cookie boundary;
- whether account/workspace identity requires any additional field/header;
- exact request JSON field names and structural types;
- user message identity source;
- parent/current-node identity requirements;
- existing conversation ID representation and new-chat absence/creation representation;
- actual model/mode/feature fields required for plain text;
- request-level operation/response identity, if any;
- real anti-dup/idempotency identity, if any.

Anything not observed remains `Unknown / Unverified`.

## Stream evidence gate

Establish from current traffic/runtime:

- actual framing: SSE/chunked JSON/JSON-lines/multipart/WebSocket/other;
- first byte and first usable event behavior;
- delta vs accumulated snapshot semantics;
- authoritative assistant message/response identity source;
- authoritative new conversation ID source/timing;
- authoritative current-node/branch-tip source/timing;
- terminal success marker and whether connection close alone is sufficient;
- terminal error event/HTTP behavior;
- explicit user-visible reasoning/status/detail events, if any;
- reasoning→final transition if explicitly represented;
- title/list metadata events for new conversation;
- whether a final Detail synchronization is needed after stream terminal.

Unknown event types must remain observable and must not trigger guessed state transitions.

## Stop evidence gate

Before implementing server Stop, establish:

- exact route/method/body or other mechanism, if any;
- target identity required;
- server acknowledgement and terminal stream behavior;
- whether local transport cancellation also stops server work or only disconnects;
- whether stopped partial content is authoritative server state;
- whether an explicit later Sync is needed.

**Local `URLSessionTask.cancel()` is never proof that server generation stopped.**

## Response state ownership

Conceptual authoritative ownership:

`verified account scope + authoritative conversation identity + exact response/message identity -> response lifecycle`

Do not create:

- one repository per screen;
- global `isStreaming` authority;
- VC/cell-owned response lifecycle;
- second stream/message store;
- UI text/title-derived identity.

Until stronger evidence exists, permit at most one active response per conversation as an ownership guard. This is not a claim that the server forbids overlap. Cross-conversation A/B simultaneous generation remains `Unknown / Unverified`; do not globally serialize unrelated conversations merely because same-conversation overlap is constrained.

Every active response operation must bind account scope, authoritative conversation identity or one repository-owned pending-new-chat token, operation/generation identity, required user request/message identity, server response/assistant identity once known, transport ownership, lifecycle phase/terminal reason and deterministic observers/completions. Late obsolete scope/operation callbacks cannot mutate current state.

## Pending -> authoritative new-chat identity

Use a local pending target only if actual protocol/UI timing requires an identity before the server supplies the authoritative conversation ID. If server identity arrives early enough, do not invent pending identity.

If pending identity is needed:

1. Repository owns one opaque pending token scoped to one verified account + one Send operation.
2. It is explicitly not a server conversation ID and is never persisted into server-ID cache/routes.
3. Composer/optimistic presentation may consume it but does not own identity.
4. First validated server conversation ID causes one atomic adoption/re-key into normal authoritative resident identity.
5. The same response lifecycle continues across adoption; do not start a second response.
6. Selection/presentation hands off exactly once without list flash or navigate-away/re-enter.
7. Pending identity stops owning resident/response/draft state after adoption.
8. A conflicting later server conversation ID is an identity error.
9. Obsolete account/operation callbacks cannot re-adopt it.
10. List/cache persist only authoritative server identity; no fake pending row.

Temporary `新对话` is presentation only and never identity authority.

## Response lifecycle

Concrete Swift names are not frozen, but the owner must semantically distinguish as evidence supports:

- Send requested/local pending;
- request accepted / response identity known;
- active receiving;
- explicit user-visible reasoning active, if evidenced;
- final-answer receiving;
- completed;
- user-stopped;
- failed/interrupted;
- invalidated/superseded.

One lifecycle reaches one deterministic terminal state. Repeated terminal callbacks cannot double-commit, double-notify or double-haptic. Navigation neither creates nor terminates a response. Hidden valid updates remain attached to the owner. Active response residents are protected from memory-warning eviction. Network/background expiration/Stop/Sync/Reload never automatically resend the prompt.

## Reasoning boundary

Only explicitly user-visible reasoning/status/detail supplied by the current service may be shown. Never expose hidden chain-of-thought or infer it from tool/internal nodes.

If a real reasoning→final transition is evidenced, record it exactly once and fire the user-required two short haptic pulses exactly once from that authoritative transition, not from cell redraw/reload. If no explicit user-visible reasoning is evidenced, do not fabricate reasoning UI; text Send/stream may still ship with reasoning as an explicit unverified boundary.

## Follow-tail and b38 history intent

Response activity comes from `ConversationRepository`; viewport intent remains in `ConversationDetailViewController`.

- A selected response at/near latest may follow its current tail.
- deliberate user upward scrolling exits follow-tail and establishes historical-reading intent;
- hidden A growth never mutates B viewport;
- returning A that stayed follow-tail eligible shows the **current** latest bottom;
- returning A after historical-reading intent restores its semantic anchor;
- programmatic scroll callbacks are not user drag;
- b38 quick navigation is explicit user navigation. Jumping to an older round establishes history-browsing intent rather than passive follow-tail.

Do not replace b38 deterministic geometry/round-navigation with raw offsets, self-sizing giant rows, `scrollToRow` geometry discovery, pre-jump teleport or correction snaps.

Exact near-bottom threshold remains a Runtime tuning value, not a preflight guess.

## Sync / Reload while active response

Existing contract remains: Sync one conversation and never sends; Reload one conversation and never sends/regenerates; navigation invokes neither.

Exact interaction with an active response must follow evidence. Do not prechoose automatic Stop-before-Sync/Reload, active-response destruction, duplicate stream recovery or timer-deferred retry. If necessary, a future Candidate may temporarily disable an unsafe recovery action while a response is active, but only from explicit ownership evidence.

## New-chat navigation

`RootViewController` remains the single compact navigation owner.

- new-chat presentation may exist without authoritative server conversation ID;
- no fake server ID exists solely to satisfy current selection assumptions;
- composer is visible on new-chat surface;
- first Send remains on the same visible surface through pending→authoritative handoff;
- authoritative adoption transitions to normal resident/selection exactly once;
- existing sidebar selection still uses the same native navigation owner;
- starting a fresh local new chat does not create a server conversation before real Send;
- hidden authoritative response continues regardless of visible screen;
- compact collapse behavior must be retested because b38 currently collapses to primary whenever `selectedConversationID == nil`.

## Expected modification surface

High confidence after protocol evidence:

- `ChatGPTClient/Conversation/ConversationFeature.swift` — response operations/lifecycle, streamed authoritative mutation, pending adoption, composer/detail presentation, Stop/reasoning/follow-tail integration.
- `ChatGPTClient/RootViewController.swift` — new-chat presentation/navigation and authoritative adoption handoff.
- `ChatGPTClient/Authentication/AuthSessionStore.swift` — only if accepted stream evidence requires incremental delivery through the same transient authenticated boundary.

Evidence stage may additionally use one cohesive protocol diagnostic file and Settings entry. Build project/workflow/version files change only at a uniquely identified Candidate milestone.

## Diagnostics contract

Use existing `DiagnosticsLogger`. Prefer semantic transitions + terminal aggregates over token/chunk flood.

Useful events include Send requested/transport start, HTTP accepted/rejected, first byte/event/visible update timings, pending created, authoritative conversation adopted, response identity adopted, phase transition, visible model commit count, Stop requested/server response/local cancellation, terminal reason, follow-tail enter/exit/return, account invalidation/stale callback discard and unknown parser event summary.

Safe fields: irreversible short hashes only when necessary, opaque local correlation, generation, existing/new flag, selected/hidden, HTTP status, symbolic route, framing/content-type class, byte/event/update counts, timings, phase/terminal reason, owner-derived active response count, non-secret viewport geometry/reason.

## First daily-chat Runtime gate

The earliest production daily-chat Candidate should prove, on exact identified iPhone/iOS17 artifact:

- exactly one existing-chat Send and one new-chat first Send;
- incremental assistant response without duplicate user/assistant messages;
- one authoritative pending→conversation handoff if pending is actually needed;
- no navigation/list flash or duplicate conversation;
- exact response-scoped Stop behavior;
- A hidden/B visible ownership isolation;
- follow-tail vs deliberate history intent;
- Sync/Reload never resend;
- b38 round/timestamp/Copy/geometry behavior remains intact;
- diagnostics contain no prompt/body/raw IDs/auth/proof/token values.

Reasoning, cross-conversation simultaneous generation, iPad, lower-iOS and non-personal workspace may remain explicit `Unknown / Unverified` when current evidence does not support them; do not fabricate unsupported behavior merely to close the matrix.