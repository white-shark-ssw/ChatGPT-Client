# DEV-send-stream

## Status

**Active — b67 local protected-Send transport remains Runtime accepted; b72 tested A-generating + B-send simultaneous ownership remains Runtime positive. Exact b75 remains a valid/permanently-reserved but Runtime partial/rejected package. The current visible Web Rule Lab now independently reproduces the same external-continuation shape as covered production: page-owned `stream_status` -> matching `{conversation_id, offset}` `/resume` -> HTTP404 JSON, followed by repeated page-owned `stream_status` + conversation fetches and short WebSocket frames, with no later HTTP/SSE continuation observed in the captured window. Therefore the earlier visible-Web HTTP200-SSE `/resume` result is historical rather than the current rule. One narrower structural response-body probe is now required before any b76 product code; b76 remains unallocated. b75 typography 26/18.2/18.2 remains visually rejected as too tight. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Routing aliases / keywords: Send, stream, reasoning, tool, external resume, cross-platform response, continuation, 行高
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal head before this checkpoint write: `0c6d014788d75406eb8ec96390346659b04f527e` (docs-only takeover synchronization)
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
- b76: not allocated; current GitHub search/guard found no `DEV-send-stream-0.1.0-b76` identity
- Stable/Frozen Send: No

## Resume takeover guard — 2026-09-01

This conversation resumed the existing Work from the supplied historical transcript and then revalidated GitHub/source truth before any product edit.

- formal branch exists and was at `73e7f758c95f89bffaa61caa702f3160b84eed33` before the documentation synchronization in this takeover;
- PR #29 was verified open, mergeable and unmerged, with head matching that branch and base `main`;
- `main` remains exactly `d323b9eed2dda75b9986fc06e14014d3e9b365fb`, so the recorded target baseline has not materially advanced;
- the formal branch contains only this Active development checkpoint plus the checkpoint template under `docs/project/current/dev/`; no competing Active development checkpoint/candidate conflict was found on the branch;
- b76 remains globally unallocated by the current repository search guard;
- `DEVELOPMENT_PLAN.md` was found stale at b70 and was docs-only synchronized to the current b75 Runtime/Web Rule Lab gate in commit `105583cc6e367815397a95361d17dc08004a0f54`;
- the takeover checkpoint synchronization then advanced the docs-only branch head to `0c6d014788d75406eb8ec96390346659b04f527e`;
- no product/config source changed during this takeover; exact b75 tested product source remains `b77303b8870dc25851dbffbf38ffc153a47bbcb2`.

## Retained accepted boundaries

- `ConversationRepository` is the sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` is sole verified auth/account owner; default persistent `WKWebsiteDataStore` is sole persistent auth-secret authority.
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

**Conclusion:** b75 successfully fixes the b74 false-failure presentation, but the production assumption that the covered official page will yield a usable matching HTTP200 SSE `/resume` is rejected for this exact Runtime. Do not bypass the validation gate and do not fabricate Native polling/resume/offset.

### 2. Cooperative geometry path is active in the supplied run

The export contains `geometryMode=cooperative_main_queue` on cache misses and `geometryMode=resident_cache`, `geometryReused=true` on resident reuse. Examples include roughly 95-281ms cooperative geometry builds and 0.01-0.02ms reused geometry in the supplied tested conversations. This proves the b75 scheduling code is executing; it does not by itself close the separate worst-case left-edge Back Runtime gate because this export did not reproduce the former 10s geometry case.

### 3. b75 typography values were applied but visually rejected

Exact source uses:

- tool line height `26`;
- reasoning fixed line height `18.2`;
- final assistant fixed line height `18.2`;
- final assistant measurement and rendering share the same attributed paragraph style.

The user's latest screenshot and explicit feedback reject the actual result: tool rows remain visually too short/tight, and reasoning plus final answer line height also remain too low. Therefore **26/18.2/18.2 is not an accepted visual baseline**, even though the code implements those numbers. The latest user Runtime feedback outranks the earlier numeric requirement. The next product correction must increase visible vertical rhythm; do not claim the old numbers are accepted merely because they were implemented.

## Visible Web Rule Lab continuation re-probe — 2026-09-01

The user ran the requested privacy-safe network-structure probe in Settings -> Web Rule Lab before entering an externally active conversation and supplied the complete bounded JSON result.

Observed current official-page sequence:

1. a user-level `wss://ws.chatgpt.com/.../ws/user/{user}` connection is active; observed string frames were bounded by length only, including 375-byte and repeated 54-byte frames; no WebSocket body authority is established;
2. on target entry, the page performs its normal conversation bootstrap and then `GET /backend-api/conversation/{conversation}/stream_status` -> HTTP200 `application/json`;
3. immediately after that status response, the page itself issues `POST /backend-api/f/conversation/resume` with request JSON keys exactly `conversation_id,offset`;
4. that page-owned resume returns **HTTP404 `application/json`**;
5. immediately after the 404 the page issues another `stream_status` plus `GET /backend-api/conversations/{conversation}`; both return HTTP200 JSON;
6. the same page-owned `stream_status` + conversation GET pair repeats at roughly six-second intervals in the captured window;
7. no later `/resume`, no second `/backend-api/f/conversation` Send, and no later HTTP200 `text/event-stream` continuation were observed through the dump at 97.898s, approximately 18.5s after the resume 404;
8. short 54-byte WebSocket frames occur during the repeated status/detail cycle, but their structure/content was intentionally not captured, so they remain notification/transport-shape evidence only.

**Current evidence conclusion:** the b75 404 is not merely a hidden/covered executor anomaly. The current visible official Web itself reproduces `stream_status 200 -> matching resume 404`, then continues with page-owned repeated status/detail fetching. The earlier same-day visible-Web HTTP200-SSE `/resume` capture remains valid historical evidence for that exact run but is superseded as the current continuation rule. Do not Native-construct resume/offset or copy the page's polling cadence. The next probe must determine what the official page is learning from the already-observed page-owned status/detail responses and whether the short WebSocket frames are only triggers or carry independently authoritative response structure.

## Current Web evidence gate before b76 product code

One narrower read-only Web Rule Lab probe is required before product code:

1. clone only page-owned `stream_status` and `/backend-api/conversations/{conversation}` responses and emit privacy-safe structural summaries, not bodies;
2. for `stream_status`, record root keys and only safe status/state/type/boolean/number fields while redacting IDs/tokens/text;
3. for conversation snapshots, record root keys, mapping/message counts, current-node presence, role/content-type/status counts, and a bounded tail of message **structure only** (role, status, content type, part/text character counts, metadata key names), never message text or raw IDs;
4. parse WebSocket strings only to top-level key/type/event/status structure when JSON; otherwise record only length/type;
5. determine whether repeated page-owned conversation snapshots change incrementally while the external response is still generating and whether those changes contain user-visible reasoning/tool/final structural nodes.

Do not capture/export Cookie, Authorization, challenge values, raw prompt/answer/reasoning/tool bodies, raw IDs, or arbitrary Web storage. Do not Send from the Lab.

## b76 allocation rule

b76 is **not allocated yet**. Exact b75 supplies a concrete defect and the current visible-Web re-probe supplies a current transport direction, but the response-body semantics remain unresolved. Do not emit/allocate b76 until the narrow structural probe establishes whether a minimal page-owned status/detail observation rule can preserve the required reasoning/tool/final lifecycle without creating Native polling or a second conversation/response authority. The clearly required larger reasoning/tool/final vertical rhythm remains part of the eventual coherent correction. Earliest valid identity remains `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` if still globally unused at final allocation guard.

## Completed documentation batch — b75 Runtime classification

- Exact b75 product source remains `b77303b8870dc25851dbffbf38ffc153a47bbcb2`; all later commits in this batch are docs-only and do not redefine the package.
- Checkpoint Runtime classification commit: `d07cde81277d5bbb1e57d2c3f85c8772a64745c7`.
- Durable b75 Runtime docs commit: `238b9e93b4e5f780aaf525106ec672de8ed8225b`, audited as exactly `BUILD_TEST_INDEX.md`, `MODULE_STATUS.md`, `PROJECT_STATE.md`, and `WEB_SEND_ADAPTER.md`.
- Prior final docs-only handoff head: `73e7f758c95f89bffaa61caa702f3160b84eed33`.
- Current takeover docs-only plan/checkpoint synchronization reached `0c6d014788d75406eb8ec96390346659b04f527e` before this new visible-Web evidence checkpoint.
- PR #29 remains open / mergeable / unmerged; actual `main` remains `d323b9eed2dda75b9986fc06e14014d3e9b365fb` at the current guard.
- Stable/Frozen Send remains No; b76 remains unallocated.

## Exact next action

Human-only narrow Web Rule Lab gate: before entering a fresh externally active target conversation, install a response-structure probe that clones only the page's own `stream_status` and `/backend-api/conversations/{conversation}` JSON responses plus privacy-safe WebSocket frame structure. Confirm whether the repeated page-owned snapshots change during generation and whether their structural tail contains in-progress user-visible reasoning/tool/final nodes. Do not Send, do not log bodies/secrets/raw IDs, and do not Native-poll. After that evidence arrives, update `WEB_SEND_ADAPTER.md`/durable project state, define or reject a minimal current continuation transport rule, then and only then allocate b76 and combine the transport correction with the required larger vertical rhythm into one Runtime candidate.
