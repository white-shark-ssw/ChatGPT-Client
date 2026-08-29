# DEV-send-stream

## Status

**Active — Phase 9 is at a Human Architecture Gate. Official no-resend `/resume` is Runtime Confirmed; b46/b47 Native duplicated parity remains HTTP404; full existing-conversation Web is not accepted as a production Send dependency. External Sub2API source research has opened a distinct subscription-backed Codex OAuth/Responses route that now requires deliberate feasibility selection.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream / Codex OAuth / sub2api`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Stable native predecessor**: b38.
- **Original feature base**: `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; target-only delta is repository governance, with no current product/state-owner conflict established.
- **Exact b47 product/config source**: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`.
- **Stable/Frozen Send**: No.

## Governance / identity

Latest repository `AGENTS.md` and `docs/project/START_HERE.md` were reread before the current architecture research. The most recent Full Resume Guard verified branch / PR / b47 Candidate / Artifact / target main / Active-task uniqueness. Later work in this conversation is docs/evidence-only and has not altered exact b47 product source.

No b48 Candidate is allocated.

## Security boundary retained

Exact b42 still proves ordinary ChatGPT consumer protected Send through `/backend-api/f/conversation` requires browser anti-abuse challenge output on the tested path. The separate supported/billed OpenAI API-key product route remains explicitly rejected by the user.

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

## External architecture research — Sub2API / Codex OAuth

Source-code research inspected `Wei-Shaw/sub2api` at upstream `main@b5827cfd54d58c248a9480b800444d0b40f0c6ea`.

Evidence class: **external third-party source evidence only; not ChatGPT Client Runtime proof and not yet a selected product architecture.**

Key findings:

1. Sub2API uses the official Codex CLI OAuth client flow against `auth.openai.com`, including PKCE, refresh tokens and ChatGPT account/plan claims such as `chatgpt_account_id` and `chatgpt_plan_type`.
2. For OpenAI OAuth-like accounts, its Responses upstream is `https://chatgpt.com/backend-api/codex/responses`, not ordinary consumer-chat `/backend-api/f/conversation` and not the separately billed `api.openai.com` API-key route.
3. Its quota service reads ChatGPT/Codex subscription usage from `/backend-api/wham/usage`, strongly indicating subscription/Codex entitlement rather than separate API-key billing.
4. Current source recognizes GPT-5.6 Codex-family models including `gpt-5.6-sol`, `gpt-5.6-terra` and `gpt-5.6-luna`; tests exercise OAuth streaming Responses and GPT-5.6 reasoning effort.
5. The source does **not** establish continuity with ordinary ChatGPT consumer `/c/<id>` history. Repository search did not reveal ordinary `/backend-api/conversations` integration. Treat consumer-history mapping as Unknown / Unverified.
6. The gateway contains substantial Codex client-identity logic: canonical User-Agent/originator/version enforcement, session/conversation isolation, optional installation/session/thread/turn/window fingerprint convergence and observed minimum-version behavior. Therefore this is valuable protocol evidence, but it is **not** proof of a clean officially supported arbitrary third-party native contract.

Potential architecture now worth evaluating, but not selected:

`Native UI -> Codex OAuth account authorization -> subscription-backed /backend-api/codex/responses -> Native Responses stream`

If independently validated on the user's account, this could avoid full mobile ChatGPT Web rendering and could permit native composer/stream ownership. It is materially different from the separately billed API-key route the user already rejected.

Unresolved P0 questions:

- does the user's exact subscription/account have the required Codex entitlement;
- can a minimal single-user native client use the transport without unjustified identity spoofing/fingerprint mimicry;
- what exact auth/account/session headers are genuinely required;
- whether Codex Responses sessions map to ordinary ChatGPT consumer history;
- whether a split product (existing consumer history read-only, new native Codex conversations separate) would be acceptable if the histories are not unified;
- exact-device reasoning/attachments/background semantics.

Detailed research: `docs/project/SUB2API_CODEX_OAUTH_RESEARCH.md`.

## Current architecture conclusion

The following is no longer an accepted production target:

`Native history -> full official Web existing conversation for every Send -> Native post-Send resume`

Also rejected as a performance fix:

`load the same full Web conversation -> userscript/CSS hides most history -> use its composer`

A future Web `lightweight visible send-only` direction is worth pursuing only if it is **structurally lightweight before existing-conversation rendering**, not the same full ChatGPT page with most history hidden after load.

Separately, Sub2API source research introduces a non-full-Web candidate boundary based on Codex OAuth + `/backend-api/codex/responses`. This candidate must not be conflated with ordinary ChatGPT `/f/conversation`, normal consumer history, or separately billed OpenAI API-key usage.

## Human Architecture Gate

Product-code advancement is paused. **No b48 Candidate is allocated.**

Evidence-backed choices/questions that now remain:

1. investigate whether an official supported visible send-only surface can continue an existing ordinary ChatGPT conversation without loading full Web application state;
2. investigate the distinct Codex OAuth/subscription-backed Responses path evidenced by Sub2API, beginning with entitlement and minimal single-user transport feasibility rather than copying its multi-user fingerprint machinery;
3. if neither path can preserve acceptable product semantics, classify visible full Web as diagnostic/fallback only and explicitly record the remaining product constraint.

The user's prior experiment already rejects “full page + DOM pruning” as option 1's implementation shortcut.

## Evidence ladder

- b47 Code written: Yes
- b47 CI: Passed
- b47 Artifact: Produced
- b47 package identity: Verified
- b47 Runtime/manual: Completed
- official ordinary-chat no-resend resume: Runtime Confirmed
- Native duplicated ordinary-chat resume: Runtime Rejected with HTTP404 JSON
- full existing-conversation Web composer viability: Failed for the reported exact-device long-answer workload
- full-Web userscript/DOM-pruning mitigation: Prior user experiment rejected for UX / `+` lag
- Codex OAuth `/backend-api/codex/responses` subscription-backed route: **External source evidence only**
- Codex OAuth exact-account Runtime: Unknown / Unverified
- ordinary ChatGPT history ↔ Codex Responses mapping: Unknown / Unverified
- Native first/exclusive ordinary-chat resume: Unknown / Unverified
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

Additional architecture research now recorded in `docs/project/SUB2API_CODEX_OAUTH_RESEARCH.md`. Exact b47 product source remains immutable.

## Next exact action

Do **not** start b48 automatically. Present the Sub2API/Codex OAuth findings as a new architecture option at the Human Gate. If the user selects it for feasibility work, perform a fresh Candidate preflight and design the smallest diagnostic experiment: validate the user's own Codex OAuth entitlement and one safe Responses request/stream without integrating production conversation state or importing Sub2API fingerprint-convergence behavior. If the user instead requires ordinary ChatGPT `/c/<id>` history continuity as a hard condition, research that mapping first and do not assume Codex Responses provides it.
