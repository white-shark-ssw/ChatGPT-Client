# DEV-send-stream

## Status

**Active — b45 official no-resend resume Runtime Confirmed; b46 Native duplicated cookie+bearer-only resume Runtime Rejected with HTTP404 JSON; exact b47 rejection-classification Candidate is built and waiting for real-device Runtime.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged.
- **Stable native predecessor**: b38.
- **Original feature base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; target-only delta is governance `AGENTS.md`, no product/state-owner overlap found.
- **Exact b47 product/config source**: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`.
- **Stable/Frozen Send**: No.

## Current governance / identity guard

Latest repository `main` `AGENTS.md` + `docs/project/START_HERE.md` were reloaded this session at the user's explicit request. Current rules include autonomous continuation, rolling checkpoints, non-atomic batch recovery, same-conversation verified identity reuse, and Full/Light Resume Guards.

Initial Full Resume Guard passed. Continuous-session Light Guard before b47 publication confirmed the real feature branch had not advanced unexpectedly. b47 was assembled on non-CI `tooling/send-stream-b47-assembly-20260829`, audited against the real branch, then published by one non-force fast-forward. The assembly delta was exactly four files:

- `.github/workflows/ios-foundation.yml`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `ChatGPTClient/Protocol/NativeResumeParityProbe.swift`
- `ChatGPTClient/SettingsViewController.swift`

No `AuthSessionStore`, `ConversationRepository`, `ConversationFeature`, Root, scripts or other product owner changed.

## Security / product boundary retained

Exact b42 still blocks pure-native ChatGPT-account **protected Send** because successful Send requires browser anti-abuse challenge output. The user explicitly rejects the separate API-product route.

Permitted target remains:

`Native history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes to the same already-started response without a second Send -> Native eventually owns visible realtime response/background lifecycle.`

Still prohibited: Sentinel/Turnstile/PoW solver/bypass/replay, copied challenge/proof values, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping, guessed continuation endpoints and hidden file-input injection.

The evidenced `/backend-api/f/conversation/resume` route is a **post-Send continuation/read path**, not a protected-Send bypass.

## Accepted b45 official resume evidence

Exact b45 Candidate `DEV-send-stream-0.1.0-b45`, source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868` remains permanently reserved.

Accepted evidence:

- uninterrupted original `/backend-api/f/conversation` SSE owns the response through terminal when intact;
- clean default-primary new-chat response survived/buffered repeated active-response background/lock including ~126s continuous without resend/refresh;
- forced interruption exposed official `POST /backend-api/f/conversation/resume` body `{conversation_id: string, offset: number}`;
- official `/resume` can return HTTP200 `text/event-stream`, repeatedly continue the same response without a second Send, and reach `message_stream_complete -> conversation_detail_metadata -> [DONE]`;
- official resume request header-name evidence included ordinary auth/client/session/route names plus `x-conduit-token`, but no Sentinel/Turnstile/PoW header names. Header-name presence does not establish a required value/header subset.

## Exact b46 identity / Runtime result

- Candidate `DEV-send-stream-0.1.0-b46`, `0.1.0 (46)`.
- Exact product/config source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`.
- Push Run / Job `33256273567` / `99110448112` — success.
- PR Run / Job `33256275218` / `99110452786` — success.
- Legitimate Artifact `9715903443`; ZIP `sha256:4747df63cc1eb0069fbb8e1d5204941e0df4cd15edd475313f464ccfc133d35c`.
- IPA SHA `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`.

Runtime:

- official `/resume` offset 18 returned HTTP200 SSE after connectivity returned;
- b46 then issued exactly one Native same-body request using WebKit-derived transient Cookie + Bearer only;
- account/session verification succeeded;
- Native `/resume` returned **HTTP404 `application/json`, 116 bytes, 0 SSE frames**;
- no Native retry occurred;
- later official Web successfully resumed the same response at progressed offset 54.

Accepted: official resume remains Runtime Confirmed; Native cookie+bearer-only **duplicated-after-official-success** resume is Runtime Rejected for this exact b46 attempt. Missing browser/client/session/route context vs cursor/consumer ownership remains unresolved. Offset `18 -> 54` is cursor-like evidence only; exact semantics remain Unknown / Unverified.

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`.

Identity-invalid b46-transition Artifacts remain permanently rejected: `9715858402`, `9715857814`, `9715907420`, `9715902353`.

## Exact b47 Candidate

- Candidate: `DEV-send-stream-0.1.0-b47`
- Version/build: `0.1.0 (47)`
- Exact product/config source: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`
- Push Run / Job: `33259640112` / `99119258573` — success
- PR Run / Job: `33259642459` / `99119264902` — success
- Legitimate Push Artifact: `9716878034`
- Artifact ZIP digest: `sha256:a6915d0a2c48877e8d4d5b7eea966118ad84b321bc1462dafe55c593796e10fc`
- IPA: `ChatGPTClient-0.1.0-b47-dev-send-stream.ipa`
- IPA SHA-256: `49d1bd4886310f7761883784f73fc5532fe1a9532773619f0796cd7aab816909`
- Independent package inspection: Release; `0.1.0 (47)`; Candidate b47; source marker `21028bbff798`; iOS14 minimum; UIDeviceFamily `[1,2]`; arm64.

## b47 implementation scope

b47 is **diagnostic-only**. It does not modify production `ConversationRepository`, response ownership or protected Send.

It preserves:

- visible user-operated official Web protected Send;
- official Web owns its normal resume behavior;
- exactly one Native duplicated parity attempt after an official HTTP200 SSE resume;
- no retry/timer/watchdog/second Send.

New structural diagnostics:

1. official `/resume` request header **names only**;
2. official `/resume` response header names only;
3. Native request context: explicit request header names + the known transient Authorization injection marker + ephemeral WebKit-cookie source marker;
4. Native response header names only;
5. Native rejected JSON **shape only** — keys + primitive types, not response text;
6. only safe tokens under explicit code/type/status-style fields may be exported (`code`, `error_code`, `type`, `error_type`, `status`).

Still not captured/copied: header values, raw conversation IDs, prompt/answer/reasoning content, Cookie/Authorization values, Conduit values, OAI browser header values, Sentinel/Turnstile/PoW/challenge values.

b47 does **not** add `x-conduit-token`, OAI browser/client/session values or any browser header value. It does **not** suppress official resume or test Native first/exclusive consumer ownership yet.

## Evidence ladder

- b47 Code written: Yes
- b47 CI passed: Yes — Push + PR
- b47 Artifact produced: Yes
- b47 package identity independently verified: Yes
- b47 Runtime/manual/real-device: **Pending**
- Native first/exclusive resume: Unknown / Unverified
- Required browser/client header subset: Unknown / Unverified
- Native incremental SSE owner/reasoning/follow-tail/background lifecycle: Unknown / Unverified
- Phase 9 Stable/Frozen: No

## Remaining durable-doc batch

Already current this session:

- rolling checkpoint
- `runtime-evidence/DEV-send-stream-b46-runtime.md`
- `PROJECT_STATE.md`
- `MODULE_STATUS.md`
- `PROJECT_PROFILE.md`

Still pending after this checkpoint roll:

- `TECHNICAL_DECISIONS.md`
- `PROJECT_SPECIFIC_RULES.md`
- `DEVELOPMENT_PLAN.md`
- `BUILD_TEST_INDEX.md`
- PR #29 title/body

These are docs/PR metadata only and must not alter exact b47 product source.

## Next exact action

Finish the remaining durable-doc/PR batch, audit that exact b47 product source -> final handoff head is docs-only, then hand exact b47 IPA to the user for the real-device rejection-classification Runtime test. After a legitimate b47 Artifact exists, any corrected product code requires b48+.