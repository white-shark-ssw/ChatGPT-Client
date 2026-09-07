# DEV-send-stream b46 Runtime Evidence

_Date: 2026-08-29_

## Exact Candidate

- Candidate: `DEV-send-stream-0.1.0-b46`
- Version/build: `0.1.0 (46)`
- Exact product/config source: `4ab9be3ef2809204e88fcb0d44884e35b43726b1`
- Push Run / Job: `33256273567` / `99110448112` — success
- PR Run / Job: `33256275218` / `99110452786` — success
- Legitimate Artifact: `9715903443`
- Artifact ZIP digest: `sha256:4747df63cc1eb0069fbb8e1d5204941e0df4cd15edd475313f464ccfc133d35c`
- IPA SHA-256: `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`
- Package identity: Release; source marker `4ab9be3ef280`; deployment target iOS14.0; UIDeviceFamily `[1,2]`; arm64.

Identity-invalid intermediate artifacts from the non-atomic b46 identity transition remain permanently rejected: `9715858402`, `9715857814`, `9715907420`, `9715902353`.

## Device / export identity

Uploaded diagnostics reported:

- Candidate `DEV-send-stream-0.1.0-b46`
- app `0.1.0`, build `46`
- source `4ab9be3ef280`
- Release
- iPhone / iOS17.0

The export is accepted as exact-b46 real-device evidence.

## Test design

b46 preserved visible user-operated official ChatGPT Web for the protected Send. It waited until official Web itself obtained a successful HTTP200 `text/event-stream` response from:

`POST /backend-api/f/conversation/resume`

Then, once only, Native used that same in-memory `conversation_id + offset` through the existing WebKit-derived transient cookie + bearer boundary and issued the same route/body. Native deliberately did **not** copy `x-conduit-token`, OAI browser/client/session headers, Sentinel/Turnstile/PoW/challenge values or other browser header values. No retry/timer/watchdog and no second Send were permitted.

## Exact Runtime sequence

- `14:30:01Z`: official Web Send observed in an existing conversation.
- During a connectivity interruption, official Web opened `/backend-api/f/conversation/resume` repeatedly with valid body and `offset=18`; attempts at `14:30:32Z`, `14:30:33Z` and `14:30:35Z` ended in transport errors while connectivity was unavailable.
- `14:30:37Z`: official Web opened `/resume` again with `offset=18`.
- `14:30:38Z`: official `/resume` returned **HTTP200 `text/event-stream`**.
- In the same second b46 started exactly one Native parity request using the same transient conversation identity and `offset=18`.
- Native auth/account re-verification completed successfully: `/api/auth/session` HTTP200; account check HTTP200; Plus/personal account context verified.
- `14:30:40Z`: Native `/resume` returned **HTTP404 `application/json`**, `116` bytes, `frameCount=0`, `jsonFrameCount=0`, `terminal=false`; diagnostic status `http_rejected`.
- b46 did not issue a second Native parity attempt.
- Later official Web again attempted resume with a progressed `offset=54`; after temporary transport errors, `14:31:31Z` official `/resume` again returned **HTTP200 `text/event-stream`**.

## What this proves

1. The official no-resend continuation route remains healthy in the same response while the Native parity attempt fails; the Native 404 is not explained by a dead conversation or global server failure.
2. Existing WebKit-derived transient cookies + bearer + `{conversation_id, offset}` + ordinary `Accept: text/event-stream` / `Content-Type: application/json` are **insufficient for the tested duplicated-after-official-success Native attempt**.
3. The Native request definitely executed after successful auth/account verification; this is not a missing-request observation.
4. The one-attempt/no-retry constraint was preserved.
5. Observed official cursor progression `18 -> 54` supports a cursor-like offset that advances with response progress, but exact offset units/semantics remain Unknown / Unverified.

## What this does not prove

- It does **not** prove Native resume is impossible.
- It does **not** prove `x-conduit-token` or any specific OAI/browser header is required. b45 recorded their header-name presence only.
- It does **not** distinguish missing browser/session/route context from stream/cursor/consumer ownership semantics.
- It does **not** test Native as the first/exclusive `/resume` consumer. b46 intentionally waited for official Web to obtain HTTP200 SSE first, then duplicated the same offset.
- It does **not** establish default-primary parity; this capture is an existing-conversation Runtime sample.
- It does **not** establish incremental Native streaming because the current transient URLSession completion path buffers the full response.

## Architecture consequence

The official Web no-resend resume mechanism remains Runtime Confirmed, but Native cookie+bearer-only duplicated parity is Runtime Rejected for this exact attempt.

Two evidence-backed hypotheses remain open:

1. **Required request context**: one or more non-challenge browser/client/session/route headers may be required beyond cookie+bearer.
2. **Consumer/cursor ownership**: the official successful resume may claim the cursor/continuation, so a second consumer using the same offset may be rejected even if otherwise authenticated.

Do not copy browser header values or suppress official resume merely from these hypotheses.

## Next exact experiment — b47 diagnostic clarification

Allocate a new Candidate because b46 Artifact identity is permanently reserved.

b47 remains diagnostic-only:

- preserve visible official Web protected Send;
- preserve one Native parity attempt only;
- log Native HTTP rejection JSON **structure only**: top-level/nested keys + primitive types and only safe enum/error-code tokens where explicitly present;
- log Native response header **names only**;
- log the triggering official successful `/resume` request header names and response header names only;
- log Native request header names actually set before dispatch;
- never capture/copy header values, raw IDs, prompt/answer/reasoning text or auth/challenge values;
- do not add browser headers, retry, timer, watchdog, second Send or production repository mutation;
- do not yet test first/exclusive consumer ownership until the 404 itself has been structurally classified.

## Evidence classification

- Code written: Yes
- CI passed: Yes
- Artifact produced: Yes
- Package identity verified: Yes
- Runtime/manual/real-device: **Yes — Native duplicated resume rejected with HTTP404 JSON while official resume remains HTTP200 SSE**
- Official no-resend resume: **Runtime Confirmed**
- Native cookie+bearer-only duplicated resume: **Runtime Rejected for exact b46 attempt**
- Native first/exclusive resume: **Unknown / Unverified**
- Required browser/client header subset: **Unknown / Unverified**
- Incremental Native response ownership/reasoning/follow-tail/background lifecycle: **Unknown / Unverified**
- Stable/Frozen Send: **No**