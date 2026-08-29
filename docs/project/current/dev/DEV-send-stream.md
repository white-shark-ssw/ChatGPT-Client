# DEV-send-stream

## Status

**Active — exact b45 now proves the official Web no-resend resume transport; b46 Native resume parity Candidate is authorized and in progress.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged.
- **Stable native predecessor**: b38.
- **Original feature base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; target advance is root-`AGENTS.md` only and has no product/state-owner overlap.
- **Pre-Runtime-3 branch head**: `eafe65cf46b405335adcb70efec90c9667a38e08`.
- **Exact b45 product/config source**: `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- **b45 Candidate**: `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`; permanently reserved.
- **b45 Artifact**: `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`; IPA SHA-256 `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.
- **b45 validation**: Code / CI / Artifact / package identity passed. Three exact-device Runtime evidence sets now accepted.
- **Stable/Frozen Send**: No.

## Security / product boundary retained

Exact b42 still blocks pure-native ChatGPT-account **Send** because the successful Send path requires browser anti-abuse challenge output. The API-product route remains explicitly rejected by the user.

Permitted target remains:

`Native history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes to that already-started response without a second Send -> Native eventually owns visible realtime response/background lifecycle.`

Still prohibited: Sentinel/Turnstile/PoW solver/bypass/replay, copied challenge/proof values, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping, guessed continuation endpoints and hidden file-input injection.

The newly evidenced `/backend-api/f/conversation/resume` route is a **post-Send continuation read**, not a Send bypass.

## b45 Runtime 1 — uninterrupted path

- `POST /backend-api/f/conversation` -> HTTP200 `text/event-stream`.
- `resume_conversation_token` appears very early.
- Original Send `fetch` remains the response transport to terminal when uninterrupted.
- `GET /backend-api/conversation/{id}/stream_status` was status-only JSON `{status:string}`.
- No secondary continuation stream was needed on the uninterrupted path.

## b45 Runtime 2 — ordinary background/lock survival

Clean default-primary new-chat capture: original Send SSE survived/buffered across active-response background intervals of about 35s, 34s and 126s; cumulative ~195s. Same original fetch produced terminal events on foreground return with no resend/refresh.

Accepted only as short-background survival/buffering evidence; not proof of 5/15-minute behavior or Native continuation.

## b45 Runtime 3 — official resume transport confirmed

Uploaded exact-b45 diagnostics metadata: `0.1.0 (45)`, Candidate `DEV-send-stream-0.1.0-b45`, source `accd7bdf29e4`, Release, iPhone, iOS17.0.

This sample's Send request is an existing/Gizmo-associated conversation (`conversation_id` and `conversation_mode.gizmo_id` structurally present), so it is **not** a clean default-primary sample. It is accepted for the generic official resume transport structure only.

### Observed sequence

- Original `POST /backend-api/f/conversation` Send request at `13:28:44Z`.
- Original Send response became HTTP200 `text/event-stream` at `13:28:56Z` and emitted early `resume_conversation_token`, conversation/request identity and a message marker through original event 11 by `13:29:08Z`.
- After the original transport was disrupted, official Web opened `POST /backend-api/f/conversation/resume` with JSON body structure exactly `{conversation_id: string, offset: number}`.
- Official resume request header-name set included normal browser/auth/client headers, but no Sentinel proof/Turnstile/PoW header names. Diagnostics recorded names only; no values were captured.
- `13:29:23Z` through `13:29:46Z`: repeated official `/resume` attempts failed with transport errors while connectivity was unavailable.
- `13:29:53Z`: official `/resume` returned HTTP200 `text/event-stream`; continuation event 1 carried conversation + request identity structure.
- A later interruption caused another resume attempt; `13:32:10Z` returned HTTP200 `text/event-stream` with the same structural continuation identity class.
- After a later background interval, `13:35:00Z` official Web opened `/resume` again; `13:35:02Z` returned HTTP200 `text/event-stream`.
- That final continuation stream emitted `message_marker`, then `server_ste_metadata`, `message_stream_complete`, `conversation_detail_metadata`, and `[DONE]` at `13:35:03Z`.
- No second `conversation_send` was observed for these recoveries.

### Accepted conclusion

The current official Web has a concrete no-resend same-response continuation transport:

`POST /backend-api/f/conversation/resume`

with JSON body structural contract:

`{ conversation_id: string, offset: number }`

and HTTP200 `text/event-stream` response carrying the ongoing response through normal terminal events.

This upgrades official reconnect existence/route/method/body-shape/framing from Unknown to **Runtime Confirmed** for the captured existing/Gizmo-associated response.

Important remaining unknowns:

- exact `offset` value semantics and relationship to original stream cursor are not yet recorded;
- which non-secret browser client headers, if any, are required beyond the already accepted transient cookie + bearer boundary is Unverified;
- Native access to this route is Unverified;
- default-primary Native parity is Unverified;
- incremental Native delivery remains Unverified because existing `AuthTransientSession.dataTask` buffers full response.

## b46 scope — smallest Native no-resend parity experiment

Allocate `DEV-send-stream-0.1.0-b46`, `0.1.0 (46)` only for a diagnostic parity experiment; b45 remains immutable.

Design:

1. Keep official ChatGPT Web visibly user-operated for protected Send.
2. Observe an **official successful** `/backend-api/f/conversation/resume` request in the visible page.
3. Transiently bridge that exact request's raw `conversation_id` + numeric `offset` into Native memory only; never persist or export the raw ID.
4. After the official resume itself returns HTTP200 SSE, issue exactly one Native `POST /backend-api/f/conversation/resume` using the same body values through the existing WebKit-derived transient cookie + bearer session.
5. Native parity request sets only ordinary `Accept: text/event-stream` + `Content-Type: application/json`; it does **not** copy `x-conduit-token`, browser client/session headers, Sentinel/Turnstile/PoW/challenge values or any raw browser header values.
6. No retry/timer/watchdog. One diagnostic attempt only.
7. Existing completion-handler transport may buffer the parity SSE to terminal for this first proof. Record only status/content-type/byte+frame counts/terminal + structural event/identity presence; never message/reasoning text or raw IDs.
8. Do not mutate `ConversationRepository`, native message state, follow-tail or production response ownership in b46. If Native parity succeeds, a later Candidate may add incremental `URLSessionDataDelegate` transport inside the existing auth/repository ownership boundary.

## Batch recovery point

Known starting branch head before this checkpoint: `eafe65cf46b405335adcb70efec90c9667a38e08`.

Planned coherent batches:

1. **Runtime-3 durable evidence batch** — update `runtime-evidence/DEV-send-stream-b45-runtime.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md`, `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`, `BUILD_TEST_INDEX.md`, and PR #29 to record the confirmed official resume transport and b46 authorization.
2. **b46 product/config batch** — add one dedicated Native resume parity diagnostic controller, wire Settings to it, add the source file to the Xcode project, advance build/Candidate to 46, and update workflow Candidate/artifact identity. Do not touch production `ConversationRepository`/Root response ownership.
3. **Validation/artifact batch** — run CI through normal GitHub Actions, produce/inspect unique b46 Artifact/IPA, then update exact evidence identities.
4. **Final handoff docs batch** — checkpoint and durable docs to the b46 exact-device Runtime gate.

Confirmed completed at checkpoint creation: Runtime-3 evidence interpreted; resume route/method/body-shape/framing conclusion established; b46 minimal scope selected.

Pending: all batches above after this checkpoint.

Recovery must never modify/rebuild b45 identity or Artifact `9713774868`; any b46 product correction after an emitted b46 Artifact requires b47+.

## Next exact action

Update Runtime-3 durable evidence, then implement the isolated b46 Native resume parity probe and continue autonomously through CI/Artifact/package-identity verification. Human gate is the resulting exact b46 real-device parity test.