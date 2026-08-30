# DEV-send-stream — Production Send / Response Ownership Preflight

_Last revalidated: 2026-08-31 after b65 Runtime and the user's explicit Option B production decision._

## Purpose

This is the durable state/ownership gate for Phase 9 text Send, new-chat identity handoff, streaming response ownership, Stop, user-visible reasoning/tool lifecycle and follow-tail.

Web-specific selectors, official-page protected-Send execution rules, SSE grammar and future rule-update procedure live in `WEB_SEND_ADAPTER.md`. Read both files before changing production Send.

Current real source, exact Runtime evidence, the selected `DEV-send-stream` checkpoint and the user's latest explicit requirement outrank stale wording here.

## Current accepted architecture

- `ConversationRepository` is the sole production conversation/list/detail/recovery/**response lifecycle** authority.
- Repository mutable authority remains on its explicit main-thread execution domain.
- Resident identity is verified account scope + authoritative conversation ID.
- `AuthSessionStore` remains sole verified auth/account-context owner.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Native list/detail reads may continue using transient ephemeral WebKit-derived auth.
- ChatGPT-account protected Send is **not pure native**: b42 proved browser challenge output is required.
- User explicitly authorized the b48-b65 tested architecture for production: one process-resident official ChatGPT Web execution surface may be covered/not user-visible while it runs the page's own protected Send/challenge flow.
- That Web surface is a transport/challenge executor only. It does not own Native messages, conversation state, response lifecycle, reasoning/tool presentation or terminal state.
- Native code must not synthesize/replay Sentinel/PoW/Turnstile/conduit/challenge values.
- One user Send action must cause exactly one official protected Send. Do not create a second Send merely to obtain streaming data.
- foreground selection remains presentation state only; hiding A must not cancel valid A response work.
- `同步最新消息` and `重载当前会话` remain explicit recovery/reconciliation actions and never resend/regenerate.
- b38 bounded message geometry, one `ConversationRoundProjection`, Copy semantics and quick-navigation contracts remain prerequisites, not replaceable state.

## Current production Send boundary

The production bridge is:

`Native composer -> covered official Web composer/page-owned protected Send -> same-response SSE -> ConversationRepository response owner -> Native presentation`.

This decision supersedes only the former prohibition on covered/hidden official-Web Send execution. It does not authorize:

- full official Web conversation rendering as daily chat;
- b44 full-page Native->Web->Native UX;
- continuous DOM message mirroring;
- Web ownership of conversation/messages;
- browser challenge solving/replay outside the page;
- speculative alternate selectors/retries/timers/watchdogs;
- duplicate Send/resend recovery.

Exact selector/SSE/tool rules are maintained in `WEB_SEND_ADAPTER.md`.

## Evidence accepted from b42-b65

For the tested primary account/iPhone/iOS17 scope:

- successful ChatGPT-account Send requires browser anti-abuse challenge output;
- page-owned `POST /backend-api/f/conversation` protected Send can return HTTP200 `text/event-stream`;
- verified composer authority is `#prompt-textarea` or explicit contenteditable role=textbox; generic textarea is rejected;
- compact assistant text continuation, b51 `title_generation` preservation, exact service-marked reasoning preambles and exact `reasoning_ended` are Runtime-backed;
- `assistant:thoughts` remains non-presentational;
- event-driven `正在思考 -> reasoning -> optional tools -> reasoning/final` behavior is Runtime-backed;
- tool result association is response-local exact `parent_id` only;
- GitHub connector visible input/output mapping is authorized only for the evidenced exact-parent GitHub shape;
- b65 passed the focused structured-detail Runtime gate;
- no retry/timer/watchdog/polling fallback is required for the accepted path.

## Web rule maintenance / Web Rule Lab

When ChatGPT Web changes, do not immediately create a new IPA for each selector/event hypothesis.

Use the in-app development Web Rule Lab defined by `WEB_SEND_ADAPTER.md`:

1. reproduce the exact current failure;
2. run one small user-pasted JS probe in the visible Lab using the same default WebKit store;
3. return structural evidence only as far as practical;
4. update the adapter rule from that evidence;
5. build one coherent product Candidate;
6. Runtime-test the real protected Send/response lifecycle;
7. update adapter docs/checkpoint/runtime evidence in the same cycle.

The Lab is not a second transport owner and does not auto-run probe code.

## Response state ownership

Conceptual production ownership:

`verified account scope + authoritative conversation identity (or one Repository-owned pending new-chat token) + response operation identity -> response lifecycle`.

Do not create:

- one repository per screen;
- global `isStreaming` authority;
- VC/cell-owned response lifecycle;
- second stream/message store;
- UI text/title-derived response identity;
- Web DOM as conversation authority.

Until stronger evidence exists, permit at most one active response per conversation as an ownership guard. This is not a claim that the service forbids overlap. Unrelated conversations must not be globally serialized merely because same-conversation overlap is constrained.

Every active response operation must bind:

- verified account scope;
- authoritative conversation ID or Repository-owned pending token;
- local operation/generation identity;
- the one protected Web Send execution it initiated;
- server response/assistant identity when current events provide it;
- lifecycle phase and deterministic terminal reason;
- observers/completions owned by Repository consumers.

Late obsolete scope/operation callbacks cannot mutate current state.

## Existing-conversation Send acceptance

The first production slice should use an already-loaded authoritative conversation.

Required behavior:

1. Native composer submits one prompt to `ConversationRepository`.
2. Repository creates one active response operation for that conversation.
3. covered official Web execution is targeted to the same authoritative conversation and performs one real protected Send.
4. real `sendObserved` / HTTP/SSE acceptance is associated with that operation.
5. accepted reasoning/final/tool updates mutate only Repository-owned response presentation state.
6. Native detail updates incrementally without a second assistant message store.
7. navigating to B does not terminate hidden A.
8. one terminal transition removes/protects response ownership deterministically.
9. no post-Send automatic Sync/poll loop is used to manufacture streaming completeness.

If the covered page cannot prove the intended conversation target, fail visibly; do not silently send into another conversation.

## Pending -> authoritative new-chat identity

Use a local pending target only if actual protocol/UI timing requires an identity before the server supplies the authoritative conversation ID.

If pending identity is needed:

1. Repository owns one opaque pending token scoped to one verified account + one Send operation.
2. It is explicitly not a server conversation ID and is never persisted into server-ID cache/routes.
3. Native composer/optimistic presentation may consume it but does not own identity.
4. first validated server conversation ID causes one atomic adoption/re-key into normal resident identity.
5. the same response lifecycle continues across adoption; do not start a second response.
6. selection/presentation hands off exactly once without list flash or navigate-away/re-enter.
7. pending identity stops owning resident/response/draft state after adoption.
8. a conflicting later authoritative ID is an identity error.
9. obsolete account/operation callbacks cannot re-adopt it.
10. list/cache persist only authoritative server identity; no fake pending row.

Temporary `新对话` is presentation only and never identity authority.

## Response lifecycle

Concrete Swift names may evolve, but the Repository owner must semantically distinguish as evidence supports:

- local Send requested;
- protected Web Send preparing/accepted;
- active response / waiting for visible reasoning;
- user-visible reasoning receiving;
- optional tool activity;
- final-answer receiving;
- completed;
- user-stopped;
- failed/interrupted;
- invalidated/superseded.

One lifecycle reaches one deterministic terminal state. Repeated terminal callbacks cannot double-commit, double-notify or double-haptic. Navigation neither creates nor terminates a response. Hidden valid updates remain attached to the owner. Active response residents are protected from memory-warning eviction.

## Reasoning / tool presentation boundary

Only explicitly user-visible service data may enter Native presentation.

- `assistant:thoughts` is never shown.
- accepted service-marked thinking preambles enter Native reasoning.
- exact `reasoning_ended` is the current reasoning->final transition authority.
- two-pulse haptic fires at most once from the authoritative real-time transition, not cell redraw.
- tools may appear zero or more times depending on actual service events.
- exact-parent association remains mandatory.
- GitHub detail content is currently the only connector family with authorized expandable input/output mapping.

Unknown event/tool shapes remain observable and unpresented until evidenced.

## Follow-tail and b38 history intent

Response activity comes from `ConversationRepository`; viewport intent remains in `ConversationDetailViewController`.

- selected A at/near latest may follow its active response tail;
- deliberate upward user scrolling exits follow-tail and establishes historical-reading intent;
- hidden A growth never mutates B viewport;
- returning A that stayed follow-tail eligible shows the current latest bottom;
- returning A after historical-reading intent restores its semantic anchor;
- b38 quick-navigation to an older round establishes history-browsing intent;
- programmatic scroll callbacks are not user drag.

Do not replace b38 deterministic geometry with raw global offsets, giant self-sizing rows, pre-jump teleport or correction snaps.

Exact near-bottom threshold is a Runtime tuning value, not a preflight guess.

## Sync / Reload while response active

Existing contract remains: Sync one conversation and never sends; Reload one conversation and never sends/regenerates; navigation invokes neither.

Do not prechoose automatic Stop-before-Sync/Reload, duplicate stream recovery or timer-deferred retry.

For the first safe production Candidate, if the exact active-response reconciliation semantics are not yet proven, it is acceptable to disable an unsafe Sync/Reload action while that conversation owns an active response, provided this is explicit UI behavior and not a hidden retry/fallback.

## Stop evidence gate

Before claiming server Stop, establish:

- exact route/method/mechanism;
- exact response/conversation target identity required;
- server acknowledgement/terminal behavior;
- whether aborting the page/transport merely disconnects locally or actually stops server generation;
- whether partial content after Stop is authoritative;
- whether explicit later Sync is needed.

**Local Web/URL task cancellation is never proof that server generation stopped.**

Do not ship a fake Stop button that only hides the UI while server work continues unless it is clearly labeled as local disconnect and intentionally accepted as such.

## New-chat navigation

`RootViewController` remains the compact navigation owner.

- new-chat presentation may exist without authoritative server conversation ID;
- no fake server ID exists solely to satisfy current selection assumptions;
- Native composer is visible on the new-chat surface;
- first Send remains on the same visible surface through pending->authoritative handoff;
- authoritative adoption transitions to normal resident/selection exactly once;
- starting a fresh local new chat does not create a server conversation before real Send;
- hidden authoritative responses continue regardless of visible screen;
- compact collapse behavior must be retested because b38 currently collapses to primary whenever `selectedConversationID == nil`.

## Expected implementation surface

High confidence:

- `ChatGPTClient/Conversation/ConversationFeature.swift` — Repository response operation/lifecycle, streamed mutation, pending adoption, active-response APIs, composer/detail response presentation, Stop/follow-tail integration.
- `ChatGPTClient/RootViewController.swift` — native composer/new-chat navigation and adoption handoff; removal of the old full-page hybrid toolbar as the normal Send path.
- current Web probe/engine code — extract/reuse only the evidenced protected-Send executor/interceptor logic behind a production bridge; do not reuse Probe VC UI as state owner.
- `ChatGPTClient/SettingsViewController.swift` — Web Rule Lab entry.
- Web Rule Lab implementation — visible developer-only `WKWebView` + temporary JS/result UI using `.default()` data store.
- Xcode/workflow/version files only at a unique coherent Candidate milestone.

`AuthSessionStore.swift` changes only if actual production bridge integration needs an auth/account lifecycle hook; do not move Web auth-secret ownership into Repository.

## Diagnostics contract

Use existing `DiagnosticsLogger`.

Useful production events include:

- Send requested;
- protected Web executor ready/targeted;
- actual Send observed;
- HTTP/SSE accepted/rejected;
- first visible reasoning/final update timing;
- response phase transition;
- tool presentation/parent match aggregates;
- pending new-chat created/adopted;
- Stop requested/acknowledged/terminal;
- active response hidden/visible;
- follow-tail enter/exit/return;
- account invalidation/stale callback discard;
- unknown parser event summary.

Safe fields: irreversible short hashes only when genuinely needed, opaque local generation/slot, selected/hidden, HTTP status, symbolic route, framing class, counts, timings, phase/terminal reason, owner-derived active-response count and non-secret viewport geometry.

Never export prompt/answer/reasoning/tool bodies, raw account/conversation/message/response IDs, browser challenge values, Cookie/Authorization, Web local/session storage, or Lab script/result bodies.

## First production daily-chat Runtime gate

Earliest coherent production Candidate should prove on exact iPhone/iOS17 artifact:

- one existing-chat Native Send -> one real protected official-Web Send;
- incremental Native reasoning/final without duplicate user/assistant messages;
- Repository remains response owner when the conversation becomes hidden;
- no wrong-conversation Web Send;
- no duplicate Send/resend to get the stream;
- exact terminal ownership;
- diagnostics contain no message/challenge/auth secrets.

The next Candidates in the same Work then add/accept:

- one new-chat first Send + pending->authoritative handoff if needed;
- exact response-scoped Stop;
- A hidden/B visible response ownership;
- follow-tail vs deliberate history intent;
- Sync/Reload safety;
- b38 round/timestamp/Copy/geometry regression.

Cross-conversation simultaneous server generation, lower iOS/iPad and non-personal workspace may remain explicit Unknown/Unverified if current evidence does not support them; do not fabricate proof merely to close the matrix.
