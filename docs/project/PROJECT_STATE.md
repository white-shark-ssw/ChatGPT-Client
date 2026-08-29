# Project State

_Last updated: 2026-08-29 through exact b45 official-resume Runtime evidence and exact b46 CI/Artifact packaging; b46 Native resume parity Runtime pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen.

## Current target/base status

`DEV-send-stream` was activated from `main@34811877896ca88c6656be6676f5466a19931ce6`. Current `main` is `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; the intervening target change is root `AGENTS.md` only and has no product/state-owner overlap. Final synchronization remains required before merge.

## Phase 9 security/product boundary

Exact b42 proved successful ChatGPT-account **Send** requires browser anti-abuse challenge output: PoW, Turnstile and `so`; non-empty PoW + Turnstile were finalized before successful Send. Pure-native/transient-auth Send therefore remains blocked.

The user explicitly rejects the separate API-product route.

Permitted target remains:

`Native history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes to the same already-started response without a second Send -> Native eventually owns visible realtime response/background lifecycle.`

Still prohibited: challenge solver/bypass/replay, copied proof/token values, guessed Send/continuation endpoints, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping and hidden file-input injection.

## Accepted visible-Web evidence

- b43: visible official-Web interaction sufficiently smooth for tested iPhone/iOS17 sequence; Web `+` ~100–200ms; Photos chooser filtered videos; standalone Web-chat product form not accepted.
- b44: tested `/c/<id>` A/B mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; full-page Native -> Web -> Native product form rejected.

## Exact b45 identity

- Candidate `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`.
- Exact product/config source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- Push Run / Job `33248952646` / `99091176390`; PR Run / Job `33248954018` / `99091179731`; success.
- Legitimate Artifact `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- IPA SHA `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.

## b45 Runtime progression

### Uninterrupted path

- `POST /backend-api/f/conversation` -> HTTP200 SSE.
- `resume_conversation_token` appeared very early.
- Original Send fetch remained response transport to terminal when intact.
- `/conversation/{id}/stream_status` was status-only JSON `{status:string}`.

### Ordinary background/lock

Clean default-primary new-chat response survived/buffered across ~35s, ~34s and ~126s active-response background intervals, cumulative ~195s, and completed on the same original fetch with no resend/refresh.

### Official no-resend resume transport — Runtime Confirmed

Exact b45 Capture D finally forced the original transport to fail. The captured Send was existing/Gizmo-associated and therefore is not a clean default-primary parity sample, but it directly established the generic official continuation mechanism:

- official Web opens `POST /backend-api/f/conversation/resume`;
- exact captured JSON body shape is `{conversation_id: string, offset: number}`;
- offline attempts may end in transport errors;
- after connectivity returns, `/resume` returns HTTP200 `text/event-stream`;
- the continuation carries conversation/request/message identity structure and can reach `server_ste_metadata -> message_stream_complete -> conversation_detail_metadata -> [DONE]`;
- multiple successful resumes occurred across repeated interruptions;
- no second `conversation_send` was observed.

Resume request header-name evidence included normal auth/client headers and `x-conduit-token`, but no Sentinel proof/Turnstile/PoW header names. Header-name presence does not prove every browser header is required. No header values were captured.

This endpoint is a post-Send continuation/read path and does **not** change the b42 protected Send boundary.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## Exact b46 Native resume parity Candidate

b46 is the smallest diagnostic parity experiment authorized by b45 Runtime; it does not modify production response ownership.

- Candidate `DEV-send-stream-0.1.0-b46`, `0.1.0 (46)`.
- Exact product/config source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`.
- Push Run / Job `33256273567` / `99110448112` — success.
- PR Run / Job `33256275218` / `99110452786` — success.
- Legitimate Push Artifact `9715903443`; ZIP digest `sha256:4747df63cc1eb0069fbb8e1d5204941e0df4cd15edd475313f464ccfc133d35c`.
- IPA `ChatGPTClient-0.1.0-b46-dev-send-stream.ipa`; SHA-256 `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`.
- Independent package inspection: `0.1.0 (46)`, Candidate b46, source `4ab9be3ef280`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, arm64.

### b46 scope

`NativeResumeParityProbeViewController` keeps the official Web visible and user-operated for protected Send. After official Web itself obtains a successful HTTP200 SSE `/resume`, it transiently bridges only the actual `conversation_id + offset` into Native memory and issues exactly **one** Native POST to the same `/resume` through the existing WebKit-derived transient cookie + bearer session.

Native does not copy `x-conduit-token`, OAI browser client/session headers or Sentinel/Turnstile/PoW/challenge values. It sets only ordinary JSON/SSE content negotiation plus the existing transient Authorization/cookie boundary. No retry/timer/watchdog. No second Send. No production `ConversationRepository`, message, reasoning, follow-tail or response-state mutation.

Current `AuthTransientSession` still buffers full response; b46 uses that deliberately for a first binary parity question: can Native receive this official continuation endpoint at all? Incremental stream ownership is a later Candidate only if b46 Runtime succeeds.

## Identity-invalid intermediate artifacts

During the non-atomic b46 identity transition, GitHub Actions emitted newer-code artifacts under stale b45 workflow/container identity. These are permanently rejected and must never be installed/cited as b45 or b46 Runtime candidates:

- Run `33256130472`, Artifact `9715858402`, stale container `ChatGPTClient-DEV-send-stream-0.1.0-b45`, head `7604d75...`.
- PR Run `33256131950`, Artifact `9715857814`, stale container b45, head `7604d75...`.
- Push Run `33256258691`, Artifact `9715907420`, stale container b45 over build-46 product config, head `aed59ba...`.
- PR Run `33256260467`, Artifact `9715902353`, stale container b45 over build-46 product config, head `aed59ba...`.

The legitimate b45 Artifact remains only `9713774868`. The legitimate b46 Runtime candidate starts at exact source `4ab9be3...` / Artifact `9715903443`.

## Current Runtime gate

Install exact b46 and test the new Settings entry `Native 续流接管探测（b46诊断）`.

Preferred parity matrix:

1. clear diagnostics;
2. use default ChatGPT / primary assistant in an existing long conversation;
3. send a response expected to stream long enough;
4. while streaming, Airplane Mode for ~10–15s, then restore connectivity;
5. do not refresh/resend/Stop/navigate/switch GPT;
6. official Web should attempt `/resume`; after one official HTTP200 SSE resume, b46 automatically issues one Native parity request;
7. wait for Native parity status/result and the official answer to finish;
8. export diagnostics.

Acceptance for this diagnostic milestone requires a `nativeResumeParityProbe.nativeResult` showing Native HTTP2xx `text/event-stream` with nonzero SSE structure; terminal `[DONE]` is especially strong evidence but is not required if the duplicated parity starts at an offset whose available window closes before terminal. Failure must be analyzed before adding any browser-specific headers; no speculative header copying.

## Authority/evidence boundary

- `ConversationRepository` remains sole native conversation/list/read/recovery/future response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- b46 Code/CI/Artifact/package identity: **passed**.
- b46 Runtime/manual/real-device Native parity: **Pending**.
- Native incremental response ownership/reasoning/follow-tail/background lifecycle: **Unknown / Unverified**.
- Phase 9 Stable/Frozen Send: **No**.
- PR #29 remains open and must not be merged as accepted Send UX before the Runtime gate is resolved.