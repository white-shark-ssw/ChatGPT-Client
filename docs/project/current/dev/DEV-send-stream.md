# DEV-send-stream

## Status

**Active — b67 local protected-Send transport remains Runtime accepted; b72 tested A-generating + B-send simultaneous ownership remains Runtime positive. Exact b75 is a valid/permanently-reserved package and is now Runtime partial/rejected on iPhone/iOS17: pre-accept external resume 404 no longer creates a false Native `回答失败`, cooperative history geometry is active, but cross-platform active reasoning still is not adopted because every observed page-owned matching `/resume` returned HTTP404 JSON; the exact b75 26/18.2/18.2 typography also rendered too tight and is rejected by the user's latest screenshot/feedback. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Routing aliases / keywords: Send, stream, reasoning, tool, external resume, cross-platform response, continuation, 行高
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal head before this checkpoint write: `b77303b8870dc25851dbffbf38ffc153a47bbcb2`
- Exact b75 product/config source: `b77303b8870dc25851dbffbf38ffc153a47bbcb2`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b75` / `0.1.0 (75)`
- Assembly validation: `33429163152` — exact scope + `git diff --check` + Xcode 16.4 Simulator build passed
- Push CI: `33429597213 / 99611443839` — success
- PR CI: `33429599704 / 99611451360` — success
- Canonical Push Artifact: `9772079468`
- ZIP: `sha256:6c4c4ec9de54264846376bdf7df4679daaaf33168481831698c884093b6209ad`
- IPA SHA: `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`
- Package independently verified: `0.1.0 (75)`, Candidate b75, source marker `b77303b8870d`, Release, MinimumOSVersion 14.0, arm64
- b39-b75 permanently reserved
- Stable/Frozen Send: No

## Retained accepted boundaries

- `ConversationRepository` is the sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` is sole native account authority; `WKWebsiteDataStore.default()` is sole persistent auth-secret authority.
- Covered official Web is browser challenge/protected-Send/page-owned continuation transport only, never message/conversation/response authority.
- b67 local Native Send -> one protected `/backend-api/f/conversation` -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile remains accepted.
- b72 tested A-generating + B-send/generate simultaneous-generation remains positive.
- b38 deterministic bounded message geometry, Copy, semantic rounds and O(1) quick-navigation remain accepted semantics.
- `assistant:thoughts` and `inline_cot_expandable_content` remain non-presentational.
- No speculative retry, polling, timer, watchdog, fallback, compatibility shim, second message store or second response store.

## Exact b75 Runtime evidence — 2026-09-01

User supplied screenshot plus `ChatGPTClient-Diagnostics-20260831-193333.json`. Metadata proves exact `DEV-send-stream-0.1.0-b75`, Build75, source marker `b77303b8870d`, Release, iPhone, iOS17.0.

### 1. False failure suppression passed, but external active stream adoption failed

The user's exact reproduction: another platform starts a response and is visibly still reasoning; entering the same conversation in Native, then explicit Sync, Reload, background/foreground and full app relaunch still shows only the authoritative user message. Native never shows `正在思考`, reasoning, tools or incremental final.

Diagnostics prove the covered executor did reach the target official page and repeatedly observed the page's own matching resume request, but the page-owned response was not an SSE stream:

- `19:30:39` observing existing conversation -> page loaded `19:30:40` -> `externalResumeObserved` `19:30:46` -> `resumeResponse` `19:30:47` = **HTTP404 `application/json`** -> executor released.
- second resident entry: page loaded `19:31:12` -> matching resume observed `19:31:17` -> **HTTP404 JSON** `19:31:18` -> released.
- after process relaunch: page loaded `19:32:56` -> matching resume observed `19:33:02` -> **HTTP404 JSON** `19:33:03` -> released.
- throughout the export, every `messagePresentation.applied` has `livePresentationRowCount=0`; no Repository external live generation was created because b75 correctly waits for `.responseAccepted`.

Authoritative Detail does move while the external response proceeds, but not as a live reasoning stream: visible count stays 11 through several successful Sync/Reload calls while mapping/filtered-node counts change; later Sync increases visible count 11->12, then 12->13 as server-backed visible messages become authoritative. That cannot substitute for incremental reasoning/tool SSE.

**Conclusion:** b75 successfully fixes the b74 false-failure presentation, but the production assumption that the covered official page will yield a usable matching HTTP200 SSE `/resume` is rejected for this exact Runtime. Do not bypass the validation gate and do not fabricate Native polling/resume/offset. The next action is Web Rule Lab evidence on the same account/session to determine why official visible Web can resume while the covered production page gets 404, and whether there is a later page-owned request/transport after the first 404.

### 2. Cooperative geometry path is active in the supplied run

The export contains `geometryMode=cooperative_main_queue` on cache misses and `geometryMode=resident_cache`, `geometryReused=true` on resident reuse. Examples include roughly 95-281ms cooperative geometry builds and 0.01-0.02ms reused geometry in the supplied tested conversations. This proves the b75 scheduling code is executing; it does not by itself close the separate worst-case left-edge Back Runtime gate because this export did not reproduce the former 10s geometry case.

### 3. b75 typography values were applied but visually rejected

Exact source uses:

- tool line height `26`;
- reasoning fixed line height `18.2`;
- final assistant fixed line height `18.2`;
- final assistant measurement and rendering share the same attributed paragraph style.

The user's latest screenshot and explicit feedback reject the actual result: tool rows remain visually too short/tight, and reasoning plus final answer line height also remain too low. Therefore **26/18.2/18.2 is not an accepted visual baseline**, even though the code implements those numbers. The latest user Runtime feedback outranks the earlier numeric requirement. The next product correction must increase visible vertical rhythm; do not claim the old numbers are accepted merely because they were implemented.

## Current Web evidence gate before b76 product code

`WEB_SEND_ADAPTER.md` requires a probe-first workflow when the official page continuation behavior differs from the documented rule. The current defect is exactly such a case: production observed page-owned matching `/resume`, but it returned 404 JSON while the external response was still active.

Use the existing Settings -> Web Rule Lab on the same logged-in `.default()` WebKit store to capture only structural facts for the target active conversation:

1. whether page-owned `GET /backend-api/conversation/{id}/stream_status` occurs and its HTTP status/content-type;
2. how many page-owned matching `/backend-api/f/conversation/resume` requests occur after entering the conversation;
3. for each resume: request JSON key names only, response status/content-type, and relative ordering after stream-status;
4. whether a later page-owned HTTP/SSE transport appears after an initial resume 404;
5. WebSocket remains structural-only unless exact evidence proves reasoning/final body authority.

Do not capture/export Cookie, Authorization, challenge values, raw prompt/answer/reasoning bodies or raw conversation IDs.

## b76 allocation rule

b76 is **not allocated yet**. Exact b75 supplies a concrete defect, so b76 is now permitted, but do not emit/allocate it until the Web Rule Lab result resolves the continuation transport rule and the visual spacing correction is defined as one coherent product scope. Once allocated, earliest valid identity is `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` if still globally unused at final allocation guard.

## Completed documentation batch — b75 Runtime classification

- Exact b75 product source remains `b77303b8870dc25851dbffbf38ffc153a47bbcb2`; all later commits in this batch are docs-only and do not redefine the package.
- Checkpoint Runtime classification commit: `d07cde81277d5bbb1e57d2c3f85c8772a64745c7`.
- Durable b75 Runtime docs commit: `238b9e93b4e5f780aaf525106ec672de8ed8225b`, audited as exactly `BUILD_TEST_INDEX.md`, `MODULE_STATUS.md`, `PROJECT_STATE.md`, and `WEB_SEND_ADAPTER.md`.
- PR #29 metadata is synchronized to title `DEV-send-stream: b75 Runtime rejection -> Web continuation re-probe gate`; it remains open / mergeable / unmerged.
- This final docs-only batch synchronizes `PROJECT_PROFILE.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, and this checkpoint.
- Actual `main` remains `d323b9eed2dda75b9986fc06e14014d3e9b365fb` at the last guard. Stable/Frozen Send remains No.
- b76 remains unallocated.

## Exact next action

Human-only Web Rule Lab gate: while another platform owns a still-active response, instrument only page-owned fetch structure before entering that target conversation, then report `stream_status` / matching `/resume` ordering, response status/content-type, request JSON key names, and whether another page-owned HTTP/SSE transport follows an initial 404. Do not send from the Lab and do not capture secrets or message bodies. After that evidence arrives, rerun Resume Guard, define the current continuation rule, combine it with the clearly required larger reasoning/tool/final vertical rhythm, allocate b76 once, then compile/CI/package one coherent Runtime candidate.
