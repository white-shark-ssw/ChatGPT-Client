# DEV-send-stream

## Status

**Active — b45 official no-resend resume is Runtime Confirmed; exact b46 Native cookie+bearer-only duplicated resume is Runtime Rejected with HTTP404 JSON; b47 diagnostic clarification is authorized.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged.
- **Stable native predecessor**: b38.
- **Original feature base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; current main-only delta from original base is repository-governance `AGENTS.md` changes. No product/state-owner overlap found.
- **Pre-this-checkpoint branch head**: `c6d70eb662848bf70b2754df3f8e9b8371090313`.
- **Stable/Frozen Send**: No.

## Current governance / resume guard

Latest repository `main` `AGENTS.md` + `docs/project/START_HERE.md` were reloaded on 2026-08-29 at the user's explicit request. Current rules include autonomous continuation, rolling checkpoints, batched non-atomic GitHub recovery, same-conversation identity reuse, and Full/Light Resume Guards.

Full Resume Guard for this continuation:

- branch exists and current head is `c6d70eb662848bf70b2754df3f8e9b8371090313` before this checkpoint write;
- PR #29 open / mergeable / not merged;
- exact b46 product/config source remains `4ab9be3ef2809204e88fcb0d44884e35b43726b1`;
- `4ab9be3... -> c6d70e...` is docs-only (`PROJECT_STATE.md`); no product drift;
- Xcode config is `0.1.0 (46)` / `DEV-send-stream-0.1.0-b46`;
- workflow identity is b46;
- legitimate b46 Artifact remains `9715903443`, digest `sha256:4747df63cc1eb0069fbb8e1d5204941e0df4cd15edd475313f464ccfc133d35c`;
- no peer Active development checkpoint exists on current feature/main routing state, so no branch/Candidate/state-owner conflict is present;
- current `main` is 3 governance commits ahead of the original feature base; final synchronization is still required before merge, but it does not block this isolated diagnostic work.

## Security / product boundary retained

Exact b42 still blocks pure-native ChatGPT-account **Send** because successful protected Send requires browser anti-abuse challenge output. The API-product route remains explicitly rejected by the user.

Permitted target remains:

`Native history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes to the same already-started response without a second Send -> Native eventually owns visible realtime response/background lifecycle.`

Still prohibited: Sentinel/Turnstile/PoW solver/bypass/replay, copied challenge/proof values, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping, guessed continuation endpoints and hidden file-input injection.

The evidenced `/backend-api/f/conversation/resume` route is a **post-Send continuation read**, not a protected-Send bypass.

## Accepted b45 Runtime evidence

Exact b45 Candidate `DEV-send-stream-0.1.0-b45`, source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868` is permanently reserved.

Accepted evidence:

1. uninterrupted `/backend-api/f/conversation` Send remains the SSE owner through terminal when intact;
2. clean default-primary new chat survived/buffered repeated active-response background/lock intervals including ~126s continuous without resend/refresh;
3. forced transport failure exposed official `POST /backend-api/f/conversation/resume` with body `{conversation_id: string, offset: number}`;
4. official `/resume` can return HTTP200 `text/event-stream`, repeatedly continue the same response without a second Send, and reach `message_stream_complete -> conversation_detail_metadata -> [DONE]`;
5. official resume request header-name evidence included normal auth/client headers and `x-conduit-token`, but no Sentinel proof/Turnstile/PoW header names. Header-name presence does not prove every browser header is required.

## Exact b46 identity

- Candidate: `DEV-send-stream-0.1.0-b46`
- Version/build: `0.1.0 (46)`
- Exact product/config source: `4ab9be3ef2809204e88fcb0d44884e35b43726b1`
- Push Run / Job: `33256273567` / `99110448112` — success
- PR Run / Job: `33256275218` / `99110452786` — success
- Legitimate Artifact: `9715903443`
- Artifact ZIP digest: `sha256:4747df63cc1eb0069fbb8e1d5204941e0df4cd15edd475313f464ccfc133d35c`
- IPA SHA-256: `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`
- Package identity: Release, source marker `4ab9be3ef280`, iOS14 minimum, UIDeviceFamily `[1,2]`, arm64.

Identity-invalid intermediate artifacts remain permanently rejected: `9715858402`, `9715857814`, `9715907420`, `9715902353`.

## b46 exact-device Runtime result — Native duplicated resume rejected

Uploaded diagnostics metadata exactly matches b46 / Release / iPhone / iOS17.0 / source `4ab9be3ef280`.

Observed sequence:

- official Web Send observed at `14:30:01Z`;
- after connectivity interruption, official `/resume` repeatedly attempted `offset=18` and initially hit transport errors;
- `14:30:38Z`: official `/resume` returned HTTP200 `text/event-stream` for offset 18;
- b46 then started exactly one Native parity request using the same in-memory `conversation_id + offset=18`;
- transient account/cookie/bearer context re-verification succeeded (`/api/auth/session` + accounts-check HTTP200; Plus/personal);
- `14:30:40Z`: Native `/resume` returned **HTTP404 `application/json`, 116 bytes, 0 SSE frames**;
- later official Web continued recovering the same response and successfully opened another HTTP200 SSE `/resume` at `offset=54`;
- no second Native parity attempt was made, preserving the one-attempt/no-retry design.

### Accepted conclusion

- Official no-resend resume transport remains **Runtime Confirmed**.
- Native parity using only WebKit-derived transient Cookie + Bearer + JSON body + ordinary Accept/Content-Type is **Runtime Rejected for this duplicated-after-official-success attempt**.
- This does **not** yet prove Native resume is impossible.
- Two unresolved explanations remain evidence-backed:
  1. one or more official browser/session/route headers may be required beyond cookie+bearer;
  2. `/resume` may have cursor/consumer ownership semantics, and b46 tested a second consumer only **after** official Web had already claimed offset 18.
- Observed offset progression `18 -> 54` supports cursor-like progression, but exact units/semantics remain Unknown / Unverified.

## b47 minimal scope

Any product/config correction after emitted b46 Artifact requires a new Candidate; b47 is the next available identity.

b47 remains **diagnostic-only** and must not modify `ConversationRepository` or production response ownership.

Evidence-backed scope:

1. preserve visible user-operated official Web protected Send;
2. preserve one Native parity attempt only; no retry/timer/watchdog/second Send;
3. on Native non-SSE/HTTP rejection, log only privacy-safe **response JSON structural keys/types** and safe enumerated/error-code tokens where present — never full error/body text, raw IDs, auth values or message content;
4. log Native response header **names only**;
5. for the exact successful official `/resume` that triggers Native parity, log official request header **names only** and response header names only;
6. log the Native request header names actually set/visible before dispatch so official-vs-Native structural header differences can be compared;
7. do **not** copy `x-conduit-token`, OAI browser/client/session values or any other browser header values in b47;
8. do not yet suppress official resume or attempt first/exclusive-consumer takeover; first identify whether the 404 itself supplies direct evidence before changing ownership order.

If b47 reveals a concrete missing-context error or another explicit server signal, only that evidence may justify a later minimal parity change. If b47 only reports not-found/cursor ownership style rejection, a later Candidate may investigate first/exclusive resume ordering without guessing browser headers.

## Non-atomic GitHub batch recovery point

Known reusable baseline before b47 writes: branch head after this checkpoint write; exact b46 product source remains immutable `4ab9be3ef2809204e88fcb0d44884e35b43726b1` and legitimate Artifact `9715903443`.

Planned batches:

1. **b46 Runtime durable-evidence batch** — update b46 Runtime evidence + `PROJECT_STATE`/`MODULE_STATUS`/`PROJECT_PROFILE`/`TECHNICAL_DECISIONS`/`PROJECT_SPECIFIC_RULES`/`DEVELOPMENT_PLAN`/`BUILD_TEST_INDEX` and PR #29 so current truth is no longer b45/b46-pending stale.
2. **b47 product/config identity batch** — minimally extend `NativeResumeParityProbe.swift` diagnostics, update Settings label only if needed, advance Xcode build/Candidate to 47, update workflow b47 identity. Because GitHub Contents writes are non-atomic and branch CI triggers per product write, any intermediate stale-identity Artifact must be permanently rejected and recorded; never install it.
3. **b47 validation/artifact batch** — verify exact final source, run normal push/PR CI, accept only Artifact whose built package identity matches b47 exact source; independently inspect package identity/SHA.
4. **final handoff batch** — roll checkpoint and durable docs to the exact b47 real-device Runtime gate.

Recovery must never rewrite/rebuild b45 or b46 identities. After a legitimate b47 Artifact exists, any corrected product code requires b48+.

## Completed

- Latest repository governance reloaded.
- Full Resume Guard completed.
- b45 official resume transport confirmed.
- b46 Code / CI / Artifact / package identity passed.
- b46 exact-device Native duplicated resume produced deterministic HTTP404 JSON rejection while official Web resume remained healthy.

## Validation

- b46 Runtime/manual/real-device: **Yes — Native duplicated resume rejected with HTTP404 JSON**.
- Native first/exclusive `/resume`: **Unknown / Unverified**.
- Required browser/client header subset for `/resume`: **Unknown / Unverified**.
- Native incremental SSE owner/reasoning/follow-tail/background lifecycle: **Unknown / Unverified**.
- Phase 9 Stable/Frozen: **No**.

## Pending

- Durable docs/PR still need b46 Runtime 404 update.
- b47 diagnostic clarification not yet implemented at this checkpoint.

## Next exact action

Complete the b46 Runtime durable-evidence batch, then implement b47 privacy-safe 404/header-structure diagnostics and continue autonomously through exact b47 CI/Artifact/package-identity verification to the next human real-device Runtime gate.