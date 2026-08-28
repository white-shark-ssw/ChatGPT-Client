# DEV-send-stream — Evidence / Ownership Preflight

_Last prepared: 2026-08-28. This is a Rules-session planning document, not an activated Development checkpoint._

## Purpose

Prepare the next serialized development task, `DEV-send-stream`, for **text Send / new conversation / streaming answer / Stop / user-visible reasoning / follow-tail**, without guessing current ChatGPT private protocol behavior and without activating the Work before its predecessor is merged.

This document is authoritative only for the evidence/ownership gates below. Current real source, the latest explicit user requirement, current protocol/runtime evidence and the future selected Development checkpoint outrank stale details here.

## Hard activation gate

`DEV-send-stream` is **not Active** and owns no development branch, PR, Candidate, build number or Artifact.

At preparation time:

- live `main` = `e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`;
- `DEV-conversation-round-count` is Active on `dev/conversation-round-count-20260828`;
- PR #27 is open;
- its checkpoint records b30 Runtime partial/failing and b31 correction in progress;
- it directly modifies `ChatGPTClient/Conversation/ConversationFeature.swift` and therefore overlaps the primary expected Send/Stream state/presentation surface.

Therefore the two Works are **not safe independent parallel product-development tasks**. Do not activate Send/Stream while the predecessor remains unmerged.

Before actual development, all of the following are required:

1. user explicitly says `当前为开发会话，新任务：DEV-send-stream`;
2. `DEV-conversation-round-count` is merged/closed to its accepted state, or the user explicitly changes the dependency model;
3. re-read `AGENTS.md`, `START_HERE.md`, current project docs, this file, and the latest merged predecessor evidence;
4. resolve latest real `main` branch/head and inspect the merged source rather than using the preflight baseline above;
5. verify no other Active checkpoint overlaps the same files/state owners/shared core;
6. inspect `BUILD_TEST_INDEX.md`, project version/build source, live branches/Artifacts, then allocate a fresh unique Candidate only after the Development Work is actually activated.

The future Candidate/build number is **Unknown / Unverified** until that gate runs. Do not assume it will be b32 merely because the predecessor is currently working toward b31.

## Current accepted facts before Send

The following are established by current source and accepted project evidence:

- `ConversationRepository` is the sole production conversation/list/read/recovery authority.
- Repository mutable conversation/resident/operation state is confined to its explicit main-thread execution domain.
- Existing resident identity is `verified account scope + authoritative conversation ID`.
- `AuthSessionStore` is the sole verified auth/account-context owner.
- default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority.
- native transport uses a transient ephemeral session with WebKit-derived cookies plus transient bearer; copied auth secrets are not persisted.
- foreground selection is presentation state only; changing visible conversation does not cancel valid hidden-conversation work.
- same-conversation obsolete Detail operations use generation ownership and cancellation-before-replacement; equivalent loads may coalesce.
- current Detail evidence retains authoritative `current_node` and parses the visible active branch from the server mapping.
- `ConversationDetailViewController` owns per-conversation scroll presentation metadata; it is not conversation-data authority.
- historical semantic scroll anchors exist; future active-response follow-tail must consume real response lifecycle state rather than a UI-invented streaming flag.
- `同步最新消息` and `重载当前会话` are explicit recovery operations and never resend/regenerate a prompt.
- accepted private protocol evidence currently covers conversation **read** only. It does not prove current Send, new-chat creation, streaming, Stop or reasoning protocol.

## Current transport gap

`AuthTransientSession` currently exposes a completion-handler `URLSessionDataTask` API. That path buffers a response until its completion callback and is sufficient for the accepted list/detail reads.

It is **not evidence of incremental stream transport capability**.

If current Send evidence proves a long-lived/chunked/SSE-like response, the implementation will need an incremental data-delivery path while preserving the same transient authentication/session boundary. Exact `URLSession` delegate design remains implementation-level until the real response framing is known.

Rules:

- do not create another persistent credential store;
- do not create a second authenticated stream authority merely because the existing wrapper is completion-based;
- do not retain raw stream bodies after parsing without an evidenced need;
- do not choose SSE/JSON-lines/multipart/WebSocket semantics before current evidence proves the actual framing.

## Protocol evidence gate

Before production Send logic is treated as authoritative, capture current evidence for **both an existing conversation Send and the first message of a new conversation**. Historical endpoint names/body shapes are clues only.

### Request evidence required

Record safe structural facts only:

- HTTP method and route;
- response status and response content type;
- whether existing-conversation and new-conversation Send use the same route;
- which currently required request headers exist beyond the already accepted transient auth/cookie path;
- whether account/workspace identity requires any additional current header or body field;
- exact request body field names and structural types required by the current service;
- how the user message identity is supplied/created;
- how parent/current-node identity is supplied, if required;
- whether existing conversation ID is sent and how new-conversation absence is represented;
- model/mode/feature fields actually required by the observed current request;
- content shape for a plain text user message;
- whether a request-level response/operation identity is supplied by client or server;
- any current anti-duplication/idempotency identity actually present.

Do **not** log or persist the actual prompt/body, Authorization/Cookie values, raw account/user/conversation IDs or raw payload.

All specific field names above remain **Unknown / Unverified** until observed.

### Stream response evidence required

Establish from current traffic/runtime:

- actual framing/protocol: SSE, chunked JSON, JSON lines, multipart, WebSocket or another format;
- first-byte and first-usable-event behavior;
- whether content events are deltas or repeated accumulated snapshots;
- authoritative response/assistant-message identity source;
- authoritative conversation ID source/timing for a new chat;
- authoritative branch/current-node identity source/timing;
- terminal success marker and whether normal connection close alone is sufficient;
- terminal error event/HTTP behavior;
- current user-visible reasoning/status/detail events, if any;
- transition from reasoning to final answer, if explicitly represented;
- title/list metadata events for a newly created conversation, if any;
- whether final server state needs a subsequent Detail read or is complete from the stream itself.

Unknown event types must be observable diagnostically and ignored/rejected according to evidenced safety; they must not trigger guessed state transitions.

### Stop evidence required

Establish current behavior before implementing a server Stop contract:

- exact route/method/body, if a Stop request exists;
- identity required to target the exact response/conversation;
- server response/acknowledgement and terminal stream behavior;
- whether cancelling only the local transport also stops server generation or merely disconnects the client;
- whether the final/stopped partial answer remains authoritative server state;
- whether a later explicit Sync is needed for reconciliation.

**Local `URLSessionTask.cancel()` is not proof that server generation stopped.**

### Error/concurrency evidence required

Capture naturally occurring or safely reproducible behavior for:

- auth rejection / expired session;
- ordinary network disconnect;
- server 4xx/5xx including rate limiting if encountered;
- malformed/unknown stream event handling;
- exact behavior when another conversation is selected while one response remains active;
- simultaneous responses in A and B only if current protocol/runtime naturally supports and proves them.

Do not manufacture a global concurrency limiter, retry loop or fallback endpoint from absence of evidence.

## State ownership target

### One conversation authority

`ConversationRepository` remains the authoritative owner for server-backed conversation/resident state and response operations.

Conceptually, response ownership is:

`verified account scope + authoritative conversation identity + exact response/message identity -> response lifecycle`

Do not create:

- one repository per screen;
- a global `isStreaming` Boolean as response authority;
- response state owned by a cell/view controller;
- a second stream/message store beside `ConversationRepository`;
- UI-title/text-derived identity.

Selection stays presentation-only. A response belonging to A continues when B becomes visible unless the user explicitly stops A or a real terminal condition occurs.

### Initial active-response cardinality

Until current protocol/runtime proves otherwise, allow at most **one active response per conversation**. This is an ownership guard, not a claim that the server forbids more.

Cross-conversation simultaneous A/B responses are **Unknown / Unverified** until exact Runtime evidence exists. Do not globally serialize A and B merely because per-conversation overlap is initially constrained.

### Response operation identity

The concrete Swift type/name is not frozen before implementation, but every active response operation must bind at least:

- verified account scope;
- authoritative conversation identity, or one repository-owned pending-new-chat token before authoritative identity exists;
- operation/generation identity;
- exact user-message/request identity required by current protocol;
- exact response/assistant-message identity once provided by the server;
- transport task/session ownership;
- lifecycle phase/terminal reason;
- deterministic observers/completions.

Late callbacks must be rejected when account scope or operation identity is obsolete.

## Pending -> authoritative new-conversation identity handoff

The first Send of a new chat is the highest identity-risk path.

### Evidence-first rule

A local pending conversation token is allowed **only if the actual protocol/UI timing requires a state identity before the server supplies an authoritative conversation ID**. If the server supplies authoritative identity synchronously/early enough that no pending conversation identity is needed, do not invent one.

### Required handoff invariant

If a pending identity is needed:

1. `ConversationRepository` creates/owns one opaque local pending token scoped to the verified account and one Send operation.
2. The token is explicitly **not** a server conversation ID and is never written into server-ID caches/routes.
3. Composer/user optimistic presentation may consume the pending operation state, but must not become identity authority.
4. On the first validated authoritative server conversation ID, Repository performs one atomic adoption/re-key operation into the normal authoritative resident key.
5. The same response lifecycle continues across adoption; do not create a second response simply because identity changed.
6. Selection/presentation is handed from pending target to authoritative target exactly once without navigating away/re-entering the chat.
7. The old pending token ceases to own resident/response/draft state after successful adoption.
8. A later conflicting second server conversation ID for the same operation is an identity error, not a second conversation owner.
9. Late callbacks from an obsolete account scope or replaced operation cannot re-adopt the old pending token.
10. List/cache integration may only use authoritative server identity. A pending fake row must not be persisted as a real conversation.

### Title/list handoff

Whether the server stream supplies authoritative title/list metadata or whether the normal list later supplies it is **Unknown / Unverified**.

A temporary visible `新对话` label is presentation only. It must never be used to decide conversation identity.

Do not trigger hidden Detail/list refreshes merely to manufacture a title unless current evidence creates a concrete requirement.

## Per-conversation response lifecycle

Exact enum names/states are implementation details, but the owner must distinguish at least these semantic stages when current protocol supports them:

- Send requested / local pending;
- request accepted / response identity known when applicable;
- active response receiving;
- user-visible reasoning active, if explicitly evidenced;
- final-answer content receiving;
- completed;
- user-stopped;
- failed/interrupted;
- invalidated/superseded by account or ownership change.

Important invariants:

- one lifecycle reaches one deterministic terminal state;
- repeated terminal callbacks cannot commit/notify/haptic twice;
- response updates mutate the owning resident/conversation model, then presentation observes that state;
- navigation never creates or terminates a lifecycle;
- hidden valid updates are retained for the owning conversation;
- an active response protects its resident from memory-warning trimming;
- no automatic prompt resend/regenerate on network failure, app background expiration, Stop or Sync/Reload;
- active response count is derived from real owned lifecycles, not a manually maintained global Boolean.

The exact authoritative mutation strategy for the streamed visible branch depends on actual event semantics and is **Unknown / Unverified** until stream evidence exists.

## Stop ownership

Stop is a user action against one exact owned response.

Rules:

- visible Stop affordance is enabled only when the selected conversation/new-chat pending target owns a stoppable active response;
- Stop never targets all conversations globally;
- selecting B while A streams does not Stop A;
- Stop records the requested response/conversation identity at the owner before transport changes;
- server Stop request and local transport cancellation are separate facts in diagnostics;
- terminal state is committed once from evidenced server/transport semantics;
- Stop never retries/resends the prompt;
- if concurrent A/B responses become evidenced, stopping A must not alter B.

Exact Stop endpoint/ack/final-state semantics are **Unknown / Unverified**.

## Reasoning / final transition

Only explicitly user-visible reasoning/status/detail supplied by the current service may be shown.

Do not expose hidden chain-of-thought or infer reasoning text from internal/tool nodes.

If current evidence supplies a real reasoning -> final transition:

- Repository/response owner records the lifecycle transition exactly once;
- Detail presentation may show subdued active reasoning/status and evidenced expandable user-visible detail;
- completion summary/duration is shown only if actually supplied/derivable from accepted public lifecycle data;
- the user-required two short haptic pulses fire once from the real reasoning -> final transition, not from cell redraw/reload;
- hidden/background-conversation haptic policy is not assumed from the visible-conversation rule and remains **Unknown / Unverified** unless explicitly accepted.

If no current user-visible reasoning event can be evidenced, do not fabricate a reasoning UI merely to complete the checklist. Basic text Send/stream can still become the earliest daily-chat Candidate with reasoning compatibility recorded as an explicit boundary.

## Follow-tail and historical reading

Response activity comes from `ConversationRepository`; viewport intent remains presentation state in `ConversationDetailViewController`.

The existing historical semantic-anchor owner must be extended, not replaced by a repository scroll flag.

Required behavior:

1. If A is at/near latest and owns an active response, A may enter per-conversation follow-tail presentation mode.
2. While A remains selected and follow-tail is active, authoritative visible growth keeps A at the current latest edge without broad full-history reload behavior where practical.
3. If the user deliberately scrolls upward, follow-tail exits and A gains/preserves historical-reading intent.
4. If A is hidden while still follow-tail eligible, hidden growth/completion does not mutate B's scroll state.
5. Returning to hidden A that stayed follow-tail eligible shows A at its **current** latest bottom.
6. Returning to A after the user established historical-reading intent restores A's semantic anchor instead of stealing the viewport to bottom.
7. Programmatic scroll callbacks are not user-drag intent.
8. The predecessor's quick-answer navigation semantics must be re-read after merge. A user explicitly jumping to an older answer is expected to establish history-browsing intent, but the exact integration must be implemented against the merged source rather than guessed from this preflight.

Exact near-bottom threshold/geometry is **Unknown / Unverified** and requires real-device tuning. Do not freeze an arbitrary point value in this document.

## Sync / Reload while a response is active

Current accepted rules remain:

- Sync targets one conversation and never sends a message;
- Reload targets one conversation and never sends/regenerates a message;
- navigation alone does not invoke either.

Their exact interaction with a future active response is **Unknown / Unverified** until the Send/Stream protocol/lifecycle is evidenced.

Do not silently choose any of these pre-Send:

- automatically Stop before Sync;
- automatically Stop before Reload;
- let Reload destroy an active response owner;
- start a duplicate stream after recovery;
- defer/retry recovery with a timer.

The future development task must make an explicit evidence-backed decision, potentially including temporarily disabling an unsafe action while a response is active if the real lifecycle requires it.

## New-chat navigation / shell transition

`RootViewController` remains the compact navigation owner.

Current read-stage behavior starts at the conversation list when no authoritative conversation is selected. Phase 9 intentionally changes that **once new-chat creation is genuinely usable** toward an official-style new-chat main surface with history/sidebar as navigation.

Expected invariants for that transition:

- a new-chat presentation may exist with no authoritative conversation ID;
- no fake server conversation ID is created to satisfy current `selectedConversationID` assumptions;
- the composer can be visible for the new-chat presentation;
- first Send remains on the same visible chat surface through pending -> authoritative adoption;
- once authoritative identity is adopted, the normal resident/selection identity becomes that server conversation without a duplicate navigation round trip;
- opening an existing sidebar conversation still uses the one native navigation owner;
- returning to/new-chat action deliberately creates a fresh local new-chat presentation, not a server conversation until Send evidence says one exists;
- a hidden authoritative response continues independent of which screen is currently selected;
- startup/collapse behavior must be retested because current `UISplitViewController` collapse choice depends on `selectedConversationID == nil`.

Exact location/icon/menu treatment follows the latest merged `UI_INTERACTION_BASELINE.md` and real-device official-App comparison; it is not frozen here.

## Expected modification surface after predecessor merge

This is a forecast for conflict planning, not permission to edit now.

### High-confidence expected files

- `ChatGPTClient/Conversation/ConversationFeature.swift`
  - authoritative response operations/lifecycle;
  - streamed conversation/message mutation;
  - pending-authoritative handoff;
  - composer/detail presentation integration;
  - Stop/reasoning/follow-tail integration points.
- `ChatGPTClient/RootViewController.swift`
  - explicit new-chat presentation/navigation;
  - pending -> authoritative selection handoff;
  - compact startup/collapse transition.
- `ChatGPTClient/Authentication/AuthSessionStore.swift`
  - only if current protocol proves incremental streaming requires extending `AuthTransientSession` beyond completion-handler data tasks while retaining the same auth boundary.

### Candidate/build files — only after development activation

- `ChatGPTClient.xcodeproj/project.pbxproj`;
- `.github/workflows/ios-foundation.yml`;
- build/diagnostics identity sources required by the existing Candidate scheme.

These must not be touched in this preflight Rules Work.

### Possible but not pre-authorized

- a cohesive new conversation-stream transport/parser source file if the merged source and actual protocol make that the smallest clear ownership boundary;
- deterministic parser test support if the real event grammar justifies project/test-target churn;
- `Diagnostics/Diagnostics.swift` only if existing logger capabilities are insufficient; ordinary new diagnostic call sites alone do not justify changing the logger authority.

Do not split files, add abstractions or add a test target solely because `ConversationFeature.swift` is large.

### Expected non-scope

- attachment upload/download protocol;
- Markdown renderer overhaul;
- background notification/true-background mechanisms;
- Projects/workspace inference;
- edit/regenerate/branch switching;
- speculative model selector;
- persistent conversation-body cache.

## Conflict with `DEV-conversation-round-count`

Direct overlap is proven, not hypothetical:

- predecessor PR #27 modifies `ConversationFeature.swift` by hundreds of lines;
- it changes Detail presentation, timestamps, Copy, answer-jump scrolling, first-entry latest placement and list presentation;
- it introduces/owns centralized `AppPreferences` in `SettingsViewController.swift`;
- it modifies Candidate build/workflow identity and multiple durable project docs;
- its current checkpoint records an unresolved b31 correction to answer landing and Copy visual.

Send/Stream also needs the same Detail table/scroll presentation and Repository core, so creating an independent Send branch now would base the response lifecycle on stale pre-b31 UI/state code and create both source and state-owner conflict.

Serial rule: **wait for the predecessor merge, then base Send on the resulting latest main and re-audit all expected files.**

## Diagnostics plan

Use existing `DiagnosticsLogger` authority. Never log prompt/answer/reasoning text, raw payload, raw titles, raw conversation/message/response/account/user IDs, Cookie/Authorization values or copied credentials.

### Safe lifecycle events

Recommended semantic event families; exact names may follow current source style:

- Send requested / transport request started;
- request HTTP accepted/rejected;
- first stream byte / first parsed event / first visible update timing;
- pending new-chat token created;
- authoritative conversation identity adopted;
- response identity adopted;
- response phase transition;
- visible-message/model commit count;
- Stop requested / server Stop response / local transport cancellation;
- response terminal reason;
- follow-tail enter/exit/hidden-return restore;
- account invalidation / stale callback discarded;
- stream parser unknown-event/error summary.

### Safe fields

Use only non-secret structural/correlation values, for example:

- short irreversible hashes for authoritative conversation/response/message identity;
- hashed/opaque pending token correlation;
- operation generation;
- existing/new-chat flag;
- selected vs hidden visibility;
- HTTP status;
- symbolic route name rather than secret URL query/body;
- response content type/framing classification;
- request/received byte counts;
- parsed event/chunk counts;
- visible update count;
- elapsed/TTFB/first-visible/terminal timing;
- phase/terminal reason;
- active response count derived from owner;
- follow-tail reason and safe row/offset geometry.

Do not log every streamed token/chunk as a full event if it creates high-volume diagnostics. Prefer semantic transitions plus terminal aggregate counts; no heartbeat timer is needed.

### Required diagnostic distinctions

Never collapse these into one generic `cancelled` state:

- user Stop requested;
- Stop server-acknowledged;
- local transport task cancelled;
- account invalidated;
- operation superseded;
- natural network interruption;
- successful server terminal completion.

This distinction is required to diagnose whether the server kept generating after local disconnect and to prevent duplicate lifecycle completion.

## Real-device acceptance matrix

Primary acceptance remains exact Candidate on the user's tested Plus/personal iPhone/iOS17 environment. Lower iOS, iPad and non-personal workspace remain explicit boundaries until separately tested.

### A. Existing-conversation Send / stream

1. Open a loaded existing conversation at latest; send one plain-text message; exactly one request is owned; optimistic/user presentation does not duplicate after authoritative events; assistant answer updates incrementally and completes once.
2. Send a response long enough to observe multiple stream updates; UI remains responsive and no broad wrong-conversation redraw/state leak occurs.
3. Hide A by opening B while A responds; A continues; B shows no A content/state; return A and observe its current valid stream/final state with no duplicate request.
4. Navigate away/back repeatedly while A responds; navigation itself never calls Stop and never creates a second response lifecycle.
5. Natural network/server failure if encountered: visible terminal failure/interruption, no automatic resend/regenerate/retry; later explicit Sync remains recovery.

### B. New conversation / identity handoff

6. Enter new-chat surface with no authoritative server conversation ID; no fake persistent list/resident identity exists.
7. First text Send creates one pending operation only if required; when server ID arrives, diagnostics show exactly one pending -> authoritative handoff.
8. UI remains on the same chat during handoff; no flash to list, duplicate conversation, duplicate user message or second stream.
9. After handoff, the conversation is addressable through normal authoritative selection/resident identity; returning from another conversation restores the same conversation.
10. New-conversation list/cache integration eventually contains at most one authoritative row for the conversation. No pending fake row is persisted.
11. Server title timing/updates follow the evidenced authoritative source; temporary `新对话` presentation never controls identity.

### C. Stop

12. Stop an active selected response during ordinary final-text streaming; only that response stops according to the evidenced server contract; no resend.
13. If explicit user-visible reasoning can be evidenced, Stop during reasoning and verify the same exact-response targeting.
14. Navigate from A to B while A is active without pressing Stop; verify A is not stopped.
15. If simultaneous A/B responses become explicitly evidenced, Stop A while B remains active; B is unaffected. Until then this case is `Unknown / Unverified`, not a forced test.

### D. Reasoning / haptic

16. If the current protocol exposes explicit user-visible reasoning, verify only allowed visible reasoning/status/detail is presented; no hidden chain-of-thought appears.
17. Verify exactly one lifecycle transition from reasoning -> final and exactly two short haptic pulses for the accepted visible real-time transition.
18. Cell reuse/reload, switching away/back, Sync/Reload after completion and final redraw do not replay the reasoning->final haptic.
19. If no current user-visible reasoning event is available, record this submatrix `Unknown / Unverified` rather than manufacturing content.

### E. Follow-tail / historical reading

20. A active while viewport at/near latest: stream growth remains attached to latest without visible repeated snap/jump behavior.
21. A active at latest -> open B -> A grows/completes hidden -> return A: A appears at its current latest bottom.
22. A active -> user deliberately drags upward -> open B -> return A: restore A's historical-reading anchor; hidden growth does not steal viewport to bottom.
23. After predecessor merge, exercise quick-answer navigation during an active response: an explicit user jump into older history must not be mistaken for passive follow-tail. Exact control integration follows merged b31+ behavior.
24. B scrolling/jumping never mutates A follow-tail/history state.

### F. Recovery interaction

25. After completed response, `同步最新消息` and `重载当前会话` continue to work and never resend the sent prompt.
26. Active-response Sync/Reload behavior is tested only after the implementation makes an explicit evidence-backed ownership decision; verify no duplicate stream/resend/cross-conversation mutation.
27. Interrupted stream -> explicit Sync reconciles server state without automatically resending the prompt.

### G. Multi-conversation/account ownership

28. A loaded/active, B loaded, rapid A/B switching: every stream/update is committed only to its owner.
29. Resident return does not force a Detail reload merely because a response completed hidden, unless actual stream evidence requires reconciliation.
30. If a real supported account-context change is naturally available, active/pending old-scope responses are invalidated and late callbacks rejected; no old content appears under new scope. Otherwise keep this `Unknown / Unverified`.
31. Non-personal workspace response isolation remains `Unknown / Unverified` until current service identity evidence establishes the necessary scope.

### H. UI / composer

32. Composer is multiline, keyboard-safe and uses the official-style baseline; empty/whitespace-only Send is not actionable.
33. Send affordance transitions to exact-response Stop only while the selected target owns an active stoppable response.
34. New-chat startup/navigation shell remains native and has one navigation owner; existing sidebar conversation opening/back/re-entry remains usable.
35. Predecessor functionality regresses neither round count, timestamps, Copy, answer navigation nor accepted first-entry/historical-scroll semantics.

### I. Identity/privacy/package evidence

36. Exact Candidate metadata, version/build/source marker, Artifact SHA and arm64/iOS minimum are independently verified before Runtime claims.
37. Diagnostics export contains no raw auth secrets, prompts, answers, reasoning text, raw IDs or raw stream payloads.
38. CI/Artifact success is reported separately from Runtime/manual acceptance.
39. Earliest daily-chat Candidate may be issued as soon as exact existing/new text Send + streaming + required ownership/navigation/Stop gates work on-device; unsupported reasoning/concurrency/lower-iOS/iPad/non-personal conditions remain clearly labeled rather than delaying usability through speculation.

## Development first-actions after activation

Once the hard activation gate is satisfied, the future Development session should proceed in this order:

1. re-read latest merged source and predecessor checkpoint/history;
2. create its own `DEV-send-stream` checkpoint and unique branch only then;
3. resolve branch/PR/head/version/build/candidate identity guard;
4. collect current protocol evidence before hard-coding private Send/stream/Stop behavior;
5. write the smallest parser/transport/state-owner changes supported by that evidence;
6. establish pending->authoritative identity only if the observed protocol timing requires it;
7. integrate composer/new-chat/response presentation with repository ownership;
8. run static/source checks and exact CI/Artifact identity checks;
9. perform the real-device matrix above, distinguishing conditional `Unknown / Unverified` cases;
10. only after Runtime acceptance update Stable/durable project docs and consider the earliest daily-chat Candidate complete.

## Prohibited shortcuts

- No protocol implementation from historical memory alone.
- No global `isStreaming` response authority.
- No UI/cell-owned response lifecycle.
- No fake server conversation ID for new chat.
- No pending/server identities left as parallel owners after adoption.
- No navigation-driven Stop.
- No local task cancellation described as proven server Stop.
- No automatic prompt resend/regenerate/retry/watchdog/timer/fallback endpoint.
- No second persistent auth store or copied persistent bearer/cookies.
- No hidden chain-of-thought exposure.
- No token-by-token diagnostics payload logging.
- No arbitrary follow-tail threshold frozen before real-device tuning.
- No independent Send branch/Candidate while the overlapping predecessor remains unmerged.
