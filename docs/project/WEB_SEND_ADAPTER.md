# Web Send Adapter / Rule Update Playbook

_Last established: 2026-09-01 through DEV-send-stream b67 accepted local transport, b72 tested concurrent ownership, and current cross-device page-owned `/resume` evidence used by exact b74._

## Purpose

This document is the durable maintenance contract for the ChatGPT-account protected-Send bridge used by the native iOS client.

The product remains a Native Swift/UIKit chat client. The official ChatGPT Web page is used only where the browser security boundary is required to perform the official protected Send/challenge flow. The goal is to keep that Web dependency small, explicit, replaceable from fresh evidence, and easy to re-probe when ChatGPT Web changes.

This file is the first document to read when any of these regress:

- Native Send button no longer causes a real protected Send;
- the official composer selector/submit behavior changes;
- `/backend-api/f/conversation` interception stops matching;
- SSE framing/event grammar changes;
- reasoning/final/tool state stops classifying correctly;
- official Web adds/removes model/mode/composer controls that the adapter must drive;
- a future ChatGPT Web deployment breaks the current covered-Web executor.

Current source/runtime evidence and the latest exact real-device reproduction outrank this document if the service changes.

## Production authority split

### Native owns

`ConversationRepository` is the sole production authority for:

- conversation residents;
- authoritative visible message projection;
- active response lifecycle;
- pending->authoritative new-chat handoff when required;
- reasoning/final/tool presentation state derived from accepted service events;
- response terminal state;
- response-scoped Stop once evidenced;
- active-response protection and future follow-tail/background integration.

`ConversationDetailViewController` owns viewport/presentation intent only.

`AuthSessionStore` remains the sole native auth/account-context authority.

### Web owns only protected browser execution

One process-resident official ChatGPT Web execution surface may be covered/not user-visible in normal production chat while it:

- uses the existing default persistent `WKWebsiteDataStore`;
- lets the official page create/refresh browser-required challenge/session context;
- receives text from the Native composer through the currently evidenced composer path;
- invokes the page's own normal Send behavior;
- performs exactly one official protected Send for the user's one Send action.

It is a **transport/challenge executor**, not a conversation repository, message cache, response owner or UI authority.

The adapter must never synthesize, solve, persist, copy for replay, or expose Sentinel/PoW/Turnstile/conduit/challenge values.

## Current accepted Send entry rule

Accepted from b61/b62 Runtime:

1. composer authority is `#prompt-textarea`, or
2. explicit `[contenteditable="true"][role="textbox"]` when that is the evidenced official composer.

Rejected:

- generic `textarea:not([disabled])`;
- guessing from placeholder text alone;
- delayed retry/timer/watchdog loops searching for another composer;
- alternate hidden fallback selectors added without a fresh real reproduction.

A Native Send is not accepted merely because JavaScript returns `submitted`. The adapter must observe the real protected-Send lifecycle (`sendObserved` plus the actual response stream/HTTP evidence).

## Current accepted protected Send / stream boundary

Current tested route:

- official page owns the browser request;
- protected Send observed on `POST /backend-api/f/conversation`;
- successful tested responses are HTTP200 `text/event-stream`;
- Native/Repository must consume the **same response**; do not issue a second Send merely to obtain streaming data.

Pure-native/transient-auth protected Send remains blocked by b42 browser-challenge evidence.

Official no-resend `/backend-api/f/conversation/resume` remains a separate b45-b47 continuation/recovery evidence surface. It is not a substitute for the first protected Send and its native parity remains unverified.

### Cross-device active-response continuation — 2026-09-01 Runtime evidence

A current Web Rule Lab capture now confirms the official page behavior when another platform has already started a response and the user enters the same conversation in official Web:

- the page opens a user-level `wss://ws.chatgpt.com/...` socket and receives short string frames; this capture does **not** establish that socket as the reasoning/final body transport;
- on entering the target conversation, the page issues the normal conversation/detail bootstrap plus `GET /backend-api/conversation/{conversation_id}/stream_status` -> HTTP200 JSON;
- when the response is still active, the page itself issues `POST /backend-api/f/conversation/resume`;
- the observed request JSON shape is exactly `{ conversation_id, offset }`;
- the resume response is HTTP200 `text/event-stream`;
- no second `/backend-api/f/conversation` Send is required for this adoption path.

**Current production rule:** external active-response adoption may observe and parse the official page's own `/backend-api/f/conversation/resume` SSE for the currently targeted conversation. Native code must not construct the resume request, choose/synthesize `offset`, replay browser/session headers, or poll `stream_status`. The page remains transport authority; `ConversationRepository` becomes/retains the sole Native response lifecycle owner once that page-owned resume is observed. Only a resume whose request `conversation_id` matches the executor's authoritative target may be adopted. The user-level WebSocket remains structural evidence only and is not authorized as a Native response-body source from this capture.

## Current accepted SSE/text grammar

The adapter/parser may rely only on shapes already backed by exact Runtime evidence.

### Ordinary assistant text

Accepted compact text behavior includes:

- exact top-level assistant append patch with `o/p/v`;
- contextual value-only continuation while a previously accepted text continuation is active;
- preserving active continuation across exact `title_generation` (b51);
- deterministic terminal promotion only when a turn ends without an explicit reasoning-end marker and the already-accepted pre-marker text must become the non-reasoning final answer.

Do not generalize arbitrary `v:string`, arbitrary nested values or arbitrary structural frames into visible assistant text.

### Reasoning

Accepted user-visible reasoning rules:

- exact service-marked `assistant:text:in_progress` part with `metadata.is_thinking_preamble_message=true` is visible reasoning text;
- exact `reasoning_status=is_reasoning` may drive state only, not expose `assistant:thoughts`;
- exact completed reasoning recap with `reasoning_status=reasoning_ended` / `reasoning_recap_type=collapse` is an accepted reasoning-phase end marker;
- visible accepted text before that marker belongs to `思考过程`;
- accepted text after it belongs to final answer;
- a later exact thinking preamble may start another visible reasoning segment;
- `assistant:thoughts` is always non-presentational.

Official-like target presentation remains:

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次正在思考/思考流 -> reasoning_ended -> 折叠思考 -> 完整最终回答`.

Not every answer requires tools or visible reasoning; state must follow actual service events.

### Tools

Accepted association rule:

`completed result.metadata.parent_id == same-response invocation service message ID`.

Only exact response-local parent equality associates a result with an invocation.

Never associate by:

- order;
- adjacency;
- count alignment;
- tool title/name equality;
- recipient equality.

Unmatched results remain unmatched and are never force-paired.

For the GitHub connector family only, b63/b64/b65 currently authorize:

- visible tool input = invocation `metadata.connector_tool_payload`;
- visible tool output = exact-parent matched completed result `message.content`;
- result must identify the invoked resource as GitHub in the already-evidenced shape;
- nested input/output disclosure and decoded hierarchical output are presentation only.

Do not generalize this visible-detail rule to another connector family without fresh evidence.

## Web Rule Lab

The project includes/maintains a development-only **Web Rule Lab** reachable from Settings.

Its role is to make future Web-rule changes cheap to investigate without rebuilding an IPA for every selector/event hypothesis.

### Lab invariants

- uses `WKWebsiteDataStore.default()` so it sees the same current ChatGPT Web login/session state;
- Web page is visibly presented while probing;
- user explicitly pastes/edits JavaScript and taps `执行`;
- no automatic probe runs on launch;
- script text and returned body are response-local UI state only;
- script/result body is not written to `DiagnosticsLogger`, `UserDefaults`, files or another database;
- result can be copied/shared manually by the user;
- safe diagnostics may record only execution success/failure, result JavaScript type/class and result character/byte length;
- Lab never becomes a production response owner and never automatically mutates production Repository state.

### Normal future update workflow

When official Web changes:

1. **Reproduce first** on the current exact production/test IPA; record the visible symptom.
2. **Do not guess a fallback.** Open Web Rule Lab using the same logged-in account/page state.
3. AI provides one small purpose-built JS probe. The user pastes and executes it in the Lab.
4. Probe returns bounded structural evidence needed for the current question: selectors, element attributes, event key/type shapes, safe counts/types, or other non-secret structure.
5. User sends the Lab result/screenshot back.
6. Update this document's `Current accepted ...` rule only after evidence is sufficient.
7. Modify the production adapter minimally. Remove/reject obsolete selector/event logic rather than accumulating compatibility shims unless two live official variants are simultaneously evidenced.
8. Run static/CI/Artifact identity checks.
9. Run one exact real-device Runtime gate proving real protected Send + response lifecycle.
10. Update checkpoint, BUILD_TEST_INDEX/runtime evidence and this document in the same cycle.

This is intentionally a **probe -> understand -> one product rebuild** workflow rather than `guess -> build IPA -> install -> guess again`.

## Probe snippet contract

A probe snippet supplied to the user should normally:

- be self-contained JavaScript;
- return one JSON-serializable object/string rather than dumping the full page;
- inspect the smallest relevant DOM/network/runtime surface;
- prefer key names, tag/type/role/attribute names, counts and booleans over text bodies;
- omit Cookie, Authorization, local/session storage secrets, challenge values and full prompt/answer content;
- not click Send or mutate chat state unless that mutation is the explicit test goal;
- clearly mark any action that will send a real message before the user runs it.

Example shape for a **non-sending composer discovery** probe (illustrative only; current rule still comes from Runtime evidence):

```javascript
(() => {
  const nodes = [...document.querySelectorAll('textarea,[contenteditable="true"],[role="textbox"]')];
  return nodes.map((el, index) => ({
    index,
    tag: el.tagName,
    id: el.id || null,
    role: el.getAttribute('role'),
    contenteditable: el.getAttribute('contenteditable'),
    disabled: 'disabled' in el ? !!el.disabled : null,
    ariaDisabled: el.getAttribute('aria-disabled')
  }));
})()
```

Do not treat this example as a fallback selector list. It is only a Lab discovery pattern.

## Rule-change classification

When a Web update breaks the adapter, classify before editing:

### A. Composer/submit-only change

Examples: `#prompt-textarea` moved, contenteditable wrapper changed, submit button semantics changed.

Action: Lab DOM probe -> one minimal selector/action update -> exact protected-Send Runtime gate.

### B. Protected request interception change

Examples: route/path changes, fetch/XHR ownership changes, response wrapping changes.

Action: Lab/runtime structural probe -> confirm exact method/route/framing -> update interceptor only. Do not replay browser challenge values natively.

### C. Stream grammar change

Examples: new patch shape, reasoning marker moved, tool/result structure changed.

Action: capture privacy-safe structural evidence; update parser at the narrowest evidenced shape; preserve unknown-event observability.

### D. Official account/security boundary change

Examples: new browser challenge mechanism, page no longer permits the established Send path, Web process/session requirements materially change.

Action: treat as an architecture/security gate. Do not bypass or emulate challenge machinery. Reassess TD before product code.

## Production adapter versioning

The adapter does not need a separate marketing version. Its exact behavior is identified by the normal app Candidate/source commit and this document's last-evidence update.

When a Web rule changes materially, record in the current Work/checkpoint:

- old exact Candidate/source;
- exact visible failure;
- Lab/probe evidence identity or screenshot/export;
- old rule rejected/superseded;
- new minimal rule;
- product Candidate/source/Artifact used for Runtime verification.

Do not keep speculative compatibility branches merely because the service may someday revert.

## Privacy/security red lines

Never persist/export through normal diagnostics:

- prompt/answer/reasoning bodies;
- `assistant:thoughts`;
- raw tool request/result bodies;
- Cookie/Authorization values;
- Sentinel/PoW/Turnstile/conduit/challenge values;
- raw account/conversation/message/response IDs;
- arbitrary Web local/session storage.

The Lab may temporarily display explicitly requested page/probe results to the user because it is an interactive developer tool, but those values remain user-controlled transient UI data and are not silently captured by app diagnostics.

## Product non-goals preserved

Option B does **not** authorize:

- full official Web conversation rendering as the daily-chat UI;
- b44 `Native -> full Web conversation -> return + Sync` product flow;
- a second Web/DOM message store;
- continuous DOM mirroring as response authority;
- browser challenge solving/replay outside the official page;
- duplicate Send/resend to recover stream state;
- speculative retry/timer/watchdog/fallback selectors;
- programmatic file-input injection without a separately evidenced attachment path.

## Current next integration boundary

Exact b74 is the first packaged product candidate for cross-device active-response adoption under this rule. Its human Runtime gate must prove:

1. another platform starts a still-active response in an existing conversation;
2. entering that conversation in b74 lets official Web perform its own continuation behavior;
3. only a matching page-owned `/backend-api/f/conversation/resume` is adopted;
4. `ConversationRepository` owns one Native live-response generation and chronological reasoning/tool/final state;
5. no duplicate Send, Native resume request, offset synthesis, stream-status polling, synthetic user bubble or WebSocket-body assumption occurs;
6. terminal authoritative history reconciles once;
7. the b67 local Send path and b72 tested A/B simultaneous-generation path remain intact;
8. diagnostics remain privacy-safe.

CI/Artifact/package verification does not prove this Runtime gate. Any code correction after the emitted b74 Artifact requires a new Candidate identity.