# DEV-send-stream

## Status

**Active — Phase 9 is at a Human Architecture Gate. Official no-resend `/resume` is Runtime Confirmed; b46/b47 Native duplicated parity remains HTTP404; full existing-conversation Web is not accepted as a production Send dependency.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Stable native predecessor**: b38.
- **Original feature base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; target-only delta is repository governance, with no current product/state-owner conflict established.
- **Exact b47 product/config source**: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`.
- **Latest docs/evidence head before this checkpoint write**: `2985c3af693a315d9048fe91d6cddad74e093ab0`.
- **Stable/Frozen Send**: No.

## Governance / identity

Latest repository `AGENTS.md` and `docs/project/START_HERE.md` were reread in the current continuous Work. The most recent Full Resume Guard verified branch / PR / b47 Candidate / Artifact / target main / Active-task uniqueness. Later work in this conversation is docs/evidence-only and has not altered exact b47 product source.

Continuous-session Light Guard confirmed the branch was at `a54a707d85f32a2ebe28633853269d984a23139e` before the newest evidence note; only docs/evidence changed afterward.

## Security boundary retained

Exact b42 still proves ChatGPT-account protected Send requires browser anti-abuse challenge output on the tested path. The separate supported/billed API-product route remains explicitly rejected by the user.

Still prohibited unless a later explicit rule change is made from evidence:

- Sentinel / Turnstile / PoW solver, bypass or captured-proof replay;
- guessed alternate protected-Send endpoints;
- hidden/shadow protected Web Send;
- Native text injection into a covered Web composer;
- synthetic hidden Web Send clicks;
- DOM answer/reasoning scraping;
- hidden file-input injection;
- copying `x-conduit-token` or OAI browser header values merely because their names were observed.

## Official no-resend continuation — accepted evidence

Exact b45 forced-interruption Runtime established official:

`POST /backend-api/f/conversation/resume`

with JSON body:

`{conversation_id: string, offset: number}`

A successful official resume returns HTTP200 `text/event-stream`, can repeatedly continue the same already-started response without a second Send, and can reach terminal `[DONE]`.

This is a post-Send continuation/read path, not a protected-Send bypass.

## b46 / b47 Native parity boundary

### b46

- Candidate `DEV-send-stream-0.1.0-b46`
- exact source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`
- legitimate Artifact `9715903443`
- official offset 18 resume -> HTTP200 SSE
- one Native same-body Cookie+Bearer-only duplicate -> HTTP404 JSON, 116 bytes, 0 SSE frames
- later official offset 54 resume -> HTTP200 SSE

### b47

- Candidate `DEV-send-stream-0.1.0-b47`, `0.1.0 (47)`
- exact product/config source `21028bbff7982abeb42f130c56fcb21e6ef44d7a`
- Push Run / Job `33259640112` / `99119258573` — success
- PR Run / Job `33259642459` / `99119264902` — success
- legitimate Push Artifact `9716878034`
- Artifact ZIP `sha256:a6915d0a2c48877e8d4d5b7eea966118ad84b321bc1462dafe55c593796e10fc`
- IPA SHA `49d1bd4886310f7761883784f73fc5532fe1a9532773619f0796cd7aab816909`
- package identity verified: Release / source `21028bbff798` / iOS14 minimum / `[1,2]` / arm64

Exact-device Runtime:

- official offset 23 resume first hit transport error while offline, then official retry at offset 23 returned HTTP200 SSE;
- b47 issued exactly one Native same-body duplicate;
- transient auth/account verification succeeded;
- Native `/resume` again returned HTTP404 `application/json`, ~707ms, 116 bytes, 0 SSE frames;
- rejection JSON shape: `{"detail":{"code":"string","message":"string"}}`;
- later official offset 74 resume returned HTTP200 SSE;
- no Native retry occurred.

Official successful resume request header names include `authorization`, OAI client/session/route names and `x-conduit-token`; Native explicitly set only `accept, content-type` plus the existing transient bearer injection and WebKit-derived ephemeral cookies. This proves a structural difference, not a required header subset.

Native first/exclusive resume remains Unknown / Unverified. Do not allocate b48 merely to copy headers or chase this 404 while the production Send surface is unresolved.

Detailed Runtime evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b47-runtime.md`

## b47 diagnostics defect

The intended safe code/type/status field was named `safeErrorTokens`; `DiagnosticsSanitizer` redacts every field key containing `token`, so these safe values were exported as `<redacted>`. Correcting this deterministic naming defect would require b48+ because b47 is reserved. It is not currently important enough to allocate b48 before the architecture gate is resolved.

## Full-Web Send-surface viability evidence

### Current exact-device b47 preparation

The intended older test conversation had only about three rounds but long answers. On the target iPhone/iOS17 device, repeatedly trying to bring up/use the mobile-Web composer froze the page badly enough that the user could not use that conversation for the protocol test and switched to a new conversation.

The b47 export covers the replacement new-conversation run, so the internal freeze owner remains Unknown / Unverified. Product impact is direct: a route that requires entering/rendering the real full Web conversation before every protected Send can fail **before Send initiation**, which Native post-Send handoff cannot repair.

### Prior user product experiment — DOM pruning does not rescue the full page

The user previously built another IPA that wrapped ChatGPT Web and injected a Tampermonkey-style userscript to reduce long-conversation cost. The script made older turns invisible and kept roughly only the latest two rounds visible.

User result:

- the full Web experience still felt poor;
- opening the `+` attachment entry still had noticeable lag;
- the approach was ultimately abandoned.

Evidence classification: prior-project real-device/product experience supplied explicitly by the user, **not** current b47 Candidate Runtime. It does not identify the internal performance owner, but it is sufficient to reject one concrete mitigation: **loading the full conversation and merely hiding/pruning old visible DOM is not an accepted production solution.**

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-full-web-pruning-history.md`.

## Current architecture conclusion

The following is no longer an accepted production target:

`Native history -> full official Web existing conversation for every Send -> Native post-Send resume`

Also rejected as a performance fix:

`load the same full Web conversation -> userscript/CSS hides most history -> use its composer`

A future `lightweight visible send-only` direction is worth pursuing only if it is **structurally lightweight before existing-conversation rendering**, not the same full ChatGPT page with most history hidden after load.

Current public research found no official documented existing-conversation lightweight send-only route. `chatgpt.com/?q=...`-style behavior can be observed around home/new-chat prompt prefill, but current official/public evidence does not establish it as a supported way to continue an existing `/c/<id>` thread. Do not promote it into production from third-party observations.

## Human Architecture Gate

Product-code advancement is paused. **No b48 Candidate is allocated.**

Evidence-backed choices that remain:

1. investigate whether OpenAI exposes an official supported visible send-only surface that can continue an existing conversation without loading the full conversation-history application state;
2. investigate another legitimate account-compatible protected-Send boundary that avoids full existing-conversation Web rendering without hidden DOM automation or challenge bypass;
3. if neither exists, classify visible full Web as diagnostic/fallback only and accept that current constraints do not yet provide a production ChatGPT-account Send path for existing conversations.

The user's latest evidence already rejects “full page + DOM pruning” as option 1.

## Evidence ladder

- b47 Code written: Yes
- b47 CI: Passed
- b47 Artifact: Produced
- b47 package identity: Verified
- b47 Runtime/manual: Completed
- official no-resend resume: Runtime Confirmed
- Native duplicated resume: Runtime Rejected with HTTP404 JSON
- full existing-conversation Web composer viability: Failed for the reported exact-device long-answer workload
- full-Web userscript/DOM-pruning mitigation: Prior user experiment rejected for UX / `+` lag
- Native first/exclusive resume: Unknown / Unverified
- required browser/client header subset: Unknown / Unverified
- official existing-thread lightweight visible Send surface: Unknown / Unverified
- Native incremental response ownership/reasoning/follow-tail/background lifecycle: Unknown / Unverified
- Phase 9 Stable/Frozen: No

## Completed durable-doc state

Current b47 Runtime / TD-028 architecture gate has already been propagated to:

- `PROJECT_STATE.md`
- `MODULE_STATUS.md`
- `PROJECT_PROFILE.md`
- `TECHNICAL_DECISIONS.md`
- `PROJECT_SPECIFIC_RULES.md`
- `DEVELOPMENT_PLAN.md`
- `BUILD_TEST_INDEX.md`
- PR #29
- b47 Runtime evidence

The newest prior DOM-pruning evidence is recorded separately in `runtime-evidence/DEV-send-stream-full-web-pruning-history.md`. Exact b47 product source remains immutable.

## Next exact action

Do **not** start b48 or resume-header product work. Continue evidence research only on the production protected-Send boundary, with the first question being whether a structurally lightweight **official, visible, existing-conversation** Send surface exists. If current evidence cannot establish one, report that constraint explicitly rather than manufacturing one from DOM injection, unsupported URL parameters or browser-header replay.
