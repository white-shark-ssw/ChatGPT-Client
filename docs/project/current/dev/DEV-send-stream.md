# DEV-send-stream

## Status

**Active — exact b47 Runtime confirms official resume again, Native duplicated resume still HTTP404 JSON, and the current full-Web-conversation Send dependency is now blocked by a long-conversation composer viability gate.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged.
- **Stable native predecessor**: b38.
- **Original feature base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; target-only delta remains repository-governance `AGENTS.md`, with no product/state-owner overlap.
- **Exact b47 product/config source**: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`.
- **Current branch head before this checkpoint update**: `f4172cc9f93f5b1ce3a83d5eb90195036f0191db`.
- **Stable/Frozen Send**: No.

## Governance / resume guard

Latest `main` `AGENTS.md` and `docs/project/START_HERE.md` were reread for this continuation. Because the previous turn ended during a documentation write chain, Full Resume Guard was rerun.

Verified:

- feature branch existed and was at `f731cbd05338f4dc8dd5da538c18a454d5b42233` before the new b47 evidence write;
- PR #29 remained open / mergeable / not merged;
- `21028bb... -> f731cbd...` was one checkpoint-only docs commit; exact b47 product source had not drifted;
- current `main` remained `1ac202c...`;
- exactly one Active development checkpoint exists (`DEV-send-stream`);
- exact b47 Candidate/Artifact identity remained unique and consistent.

Guard success is not a Human Gate; work continued automatically.

## Security / product boundary retained

Exact b42 still blocks pure-native ChatGPT-account **protected Send** because successful Send requires browser anti-abuse challenge output. The separate API-product route remains explicitly rejected by the user.

Still prohibited:

- Sentinel/Turnstile/PoW solver/bypass/replay;
- copied challenge/proof values;
- hidden/shadow protected Web Send;
- Native injection into a covered Web composer;
- synthetic hidden Send clicks;
- DOM answer/reasoning scraping;
- guessed continuation endpoints;
- hidden file-input injection.

`/backend-api/f/conversation/resume` remains a **post-Send continuation/read path**, not a protected-Send bypass.

## Accepted b45 official resume evidence

Exact b45 Candidate `DEV-send-stream-0.1.0-b45`, source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868` is permanently reserved.

Accepted:

1. uninterrupted original `/backend-api/f/conversation` SSE owns the response through terminal when intact;
2. clean default-primary new-chat response survived/buffered repeated active-response background/lock including ~126s continuous without resend/refresh;
3. forced interruption exposed official `POST /backend-api/f/conversation/resume` with JSON body `{conversation_id: string, offset: number}`;
4. official `/resume` can return HTTP200 `text/event-stream`, repeatedly continue the same response without a second Send, and reach terminal `[DONE]`.

## Exact b46 result

- Candidate `DEV-send-stream-0.1.0-b46`, source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`, legitimate Artifact `9715903443`.
- Official offset 18 resume returned HTTP200 SSE.
- Native same-body Cookie+Bearer-only duplicated attempt returned HTTP404 `application/json`, 116 bytes, 0 SSE frames.
- Later official offset 54 resume returned HTTP200 SSE.

Accepted: official resume Runtime Confirmed; Native duplicated-after-official-success Cookie+Bearer-only parity Runtime Rejected. Missing request context vs cursor/consumer ownership remained unresolved.

## Exact b47 identity

- Candidate: `DEV-send-stream-0.1.0-b47`
- Version/build: `0.1.0 (47)`
- Exact product/config source: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`
- Push Run / Job: `33259640112` / `99119258573` — success
- PR Run / Job: `33259642459` / `99119264902` — success
- Legitimate Push Artifact: `9716878034`
- Artifact ZIP digest: `sha256:a6915d0a2c48877e8d4d5b7eea966118ad84b321bc1462dafe55c593796e10fc`
- IPA: `ChatGPTClient-0.1.0-b47-dev-send-stream.ipa`
- IPA SHA-256: `49d1bd4886310f7761883784f73fc5532fe1a9532773619f0796cd7aab816909`
- Package identity: Release / `0.1.0 (47)` / source `21028bbff798` / iOS14 minimum / UIDeviceFamily `[1,2]` / arm64.

## b47 exact-device Runtime

Uploaded diagnostics metadata exactly matched b47 / Release / iPhone / iOS17.0 / source `21028bbff798`.

Protocol sequence:

- official Web Send observed;
- official `/resume` with offset 23 first hit a transport error while connectivity was unavailable;
- immediate official retry at the same offset 23 returned HTTP200 `text/event-stream`;
- b47 issued exactly one Native parity request with the same in-memory conversation identity + offset 23;
- transient WebKit-derived cookie/bearer account verification succeeded;
- Native `/resume` returned **HTTP404 `application/json` after ~707 ms, 116 bytes, 0 SSE frames**;
- rejection JSON structure was `{"detail":{"code":"string","message":"string"}}` only; response text was not captured;
- later official Web successfully resumed again at progressed offset 74 with HTTP200 SSE;
- no second Native parity attempt occurred.

Official successful resume request header names:

`accept, authorization, content-type, oai-client-build-number, oai-client-version, oai-device-id, oai-echo-logs, oai-language, oai-session-id, x-conduit-token, x-oai-is-client-observation, x-oai-is-pending-updates, x-oai-turn-trace-id, x-openai-target-path, x-openai-target-route`

Native request explicitly set only `accept, content-type`, plus the established transient bearer injection and WebKit-derived ephemeral cookies.

Accepted: the structural context difference is large, but b47 still does **not** identify which header(s), if any, are required. Do not copy browser values based only on name presence.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b47-runtime.md`.

## b47 diagnostics defect

`safeErrorTokens` was exported as `<redacted>` because current `DiagnosticsSanitizer.secretFragments` redacts every field key containing `token`. Therefore b47 failed to preserve the intended safe code/type/status token values even though the JSON body shape was captured.

This is a deterministic diagnostic naming defect. Since b47 Artifact identity is emitted/reserved, correcting it would require b48+. No b48 is allocated yet.

## New P0 product viability evidence — long Web conversation composer freeze

The user could not use the intended older long conversation for the b47 test. The conversation had only about three rounds, but the answers were long. On the target iPhone/iOS17 environment, repeatedly trying to bring up/use the mobile-Web composer caused the page to freeze and made the conversation unusable for the test. The user therefore used a new conversation.

Evidence classification:

- **Runtime/manual exact-device usability failure: Yes.**
- Internal root cause: **Unknown / Unverified** because the exported b47 diagnostics were captured from the replacement new-conversation run and do not contain the failed long-conversation Web attempt.
- Product impact: **P0 architecture viability risk.** A flow that requires entering/rendering the real full Web conversation before each protected Send can fail before Send initiation. Native post-Send handoff cannot repair a Web composer that never becomes usable enough to send.

This materially weakens the prior b43 conclusion that visible Web was smooth enough: b43 remains valid only for its tested shorter-sequence scope, not as proof of long-conversation daily-use viability.

## Current architecture gate

The previous target was:

`Native history/presentation -> user-visible official full Web conversation performs protected Send -> Native attaches/resumes to the same already-started response.`

After the new long-conversation Runtime result, **do not continue this form into production integration or allocate b48 merely to chase resume headers.** The Send surface itself now has a demonstrated exact-device failure mode before the Native handoff point.

Potential next directions remain Unknown / unselected and must not be guessed:

1. determine whether an official supported **lightweight visible send-only** Web surface exists that does not render the full conversation history;
2. determine whether another legitimate account-compatible protected-Send boundary can avoid full mobile-Web conversation rendering without hidden Web/DOM automation or challenge bypass;
3. if neither exists, treat the visible-Web architecture as a diagnostic/fallback ceiling rather than the production daily-chat architecture.

Choosing between these product directions is now a real Human Architecture Gate.

## Evidence ladder

- b47 Code written: Yes
- b47 CI passed: Yes
- b47 Artifact produced: Yes
- b47 package identity verified: Yes
- b47 Runtime/manual/real-device: **Yes**
- b47 Native duplicated resume parity: **Rejected — HTTP404 JSON**
- b47 long-conversation visible-Web composer viability: **Failed on exact target device for the reported long-conversation workload**
- Native first/exclusive resume: Unknown / Unverified
- Required browser/client header subset: Unknown / Unverified
- Lightweight supported visible-Web send-only route: Unknown / Unverified
- Native incremental response ownership/reasoning/follow-tail/background lifecycle: Unknown / Unverified
- Phase 9 Stable/Frozen: No

## Non-atomic recovery point

Current reusable product identity remains exact b47 source `21028bbff7982abeb42f130c56fcb21e6ef44d7a`; do not rebuild or modify b47 product code.

Completed this turn:

- latest governance reread;
- Full Resume Guard;
- exact b47 diagnostics interpretation;
- new `runtime-evidence/DEV-send-stream-b47-runtime.md`;
- architecture viability conclusion established.

Pending docs-only maintenance:

- refresh `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md`, `BUILD_TEST_INDEX.md` and PR #29 to the b47/architecture-gate truth.

Recovery must perform only missing docs/PR writes and must not touch b47 product identity.

## Next exact action

Finish the docs/PR evidence batch. Then stop product-code advancement at the Human Architecture Gate: do not allocate b48 until the product Send boundary is deliberately selected from evidence. If the current visible-full-Web path is retained only as fallback/diagnostic, record that explicitly before any later Candidate.