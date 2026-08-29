# Project State

_Last updated: 2026-08-29 through exact b46 Native resume parity Runtime; b47 diagnostic clarification authorized._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen.

## Current target/base status

`DEV-send-stream` was activated from `main@34811877896ca88c6656be6676f5466a19931ce6`.

Current `main` is `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; the three target-only commits are repository-governance `AGENTS.md` changes and have no product/state-owner overlap. Feature branch final synchronization remains required before merge, but does not block the current isolated diagnostic work.

Current feature branch: `dev/send-stream-20260829`; PR #29 remains open / mergeable / not merged.

## Phase 9 security/product boundary

Exact b42 proved successful ChatGPT-account **Send** requires browser anti-abuse challenge output: PoW, Turnstile and `so`; non-empty PoW + Turnstile were finalized before successful Send. Pure-native/transient-auth protected Send remains blocked.

The user explicitly rejects the separate API-product route.

Permitted target remains:

`Native history/presentation -> user-visible official Web performs legal protected Send -> Native attaches/resumes to the same already-started response without a second Send -> Native eventually owns visible realtime response/background lifecycle.`

Still prohibited: challenge solver/bypass/replay, copied proof/token values, guessed Send/continuation endpoints, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping and hidden file-input injection.

The current `/backend-api/f/conversation/resume` work is a **post-Send continuation/read path** and does not weaken the b42 protected-Send boundary.

## Accepted visible-Web evidence

- b43: visible official-Web interaction sufficiently smooth for tested iPhone/iOS17 sequence; Web `+` ~100–200ms; Photos chooser filtered videos; standalone Web-chat product form not accepted.
- b44: tested `/c/<id>` A/B mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; full-page Native -> Web -> Native product form rejected. No arbitrary timer/poll/retry workaround is accepted.

## Exact b45 identity / accepted Runtime

- Candidate `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`.
- Exact product/config source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`.
- Push Run / Job `33248952646` / `99091176390`; PR Run / Job `33248954018` / `99091179731`; success.
- Legitimate Artifact `9713774868`; ZIP `sha256:17843765c861e44e0e93e66e373ba3f2acbd6a772f3ffd43fab572766ca7626d`.
- IPA SHA `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`.

Accepted b45 progression:

1. uninterrupted original `/backend-api/f/conversation` SSE remains response transport through terminal when intact;
2. clean default-primary new-chat original fetch survived/buffered repeated active-response background/lock intervals including ~126s continuous without resend/refresh;
3. forced interruption exposed official `POST /backend-api/f/conversation/resume` with JSON body `{conversation_id: string, offset: number}`;
4. official `/resume` can return HTTP200 `text/event-stream`, repeatedly continue the same already-started response without a second Send, and reach `message_stream_complete -> conversation_detail_metadata -> [DONE]`;
5. official resume request header-name evidence included normal auth/client headers and `x-conduit-token`, but no Sentinel proof/Turnstile/PoW header names. Presence does not prove any one header is required.

Detailed b45 evidence: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## Exact b46 Native resume parity Candidate

- Candidate `DEV-send-stream-0.1.0-b46`, `0.1.0 (46)`.
- Exact product/config source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`.
- Push Run / Job `33256273567` / `99110448112` — success.
- PR Run / Job `33256275218` / `99110452786` — success.
- Legitimate Artifact `9715903443`; ZIP digest `sha256:4747df63cc1eb0069fbb8e1d5204941e0df4cd15edd475313f464ccfc133d35c`.
- IPA SHA-256 `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`.
- Package identity independently verified as Release, source `4ab9be3ef280`, iOS14 minimum, `[1,2]`, arm64.

Identity-invalid intermediate b46-transition artifacts remain permanently rejected: `9715858402`, `9715857814`, `9715907420`, `9715902353`.

### b46 Runtime result — cookie+bearer-only duplicated resume rejected

Exact-device diagnostics match b46 / Release / iPhone / iOS17.0.

- official Web Send observed;
- official Web `/resume` attempts with `offset=18` failed while offline, then returned HTTP200 `text/event-stream` when connectivity returned;
- b46 immediately issued exactly one Native parity request using the same in-memory `conversation_id + offset=18`;
- Native WebKit-derived cookie/bearer account re-verification succeeded (`/api/auth/session` and accounts-check HTTP200; Plus/personal);
- Native `/resume` returned **HTTP404 `application/json`, 116 bytes, 0 SSE frames**;
- no Native retry occurred;
- later official Web successfully resumed the same response again with progressed `offset=54`, returning HTTP200 SSE.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`.

### Accepted b46 conclusion

- Official no-resend resume remains **Runtime Confirmed**.
- Native cookie+bearer-only duplicated `/resume`, issued **after official Web already successfully claimed the same offset**, is **Runtime Rejected for this exact b46 attempt**.
- This does not prove Native resume is impossible.
- Two evidence-backed possibilities remain unresolved:
  1. required non-challenge browser/client/session/route request context beyond cookie+bearer;
  2. cursor/consumer ownership semantics, because b46 tested a second consumer only after official success.
- Offset progression `18 -> 54` supports cursor-like advancement, but exact units remain Unknown / Unverified.

## b47 diagnostic clarification gate

Because b46 Artifact identity is emitted/reserved, any changed product code requires b47+.

b47 is authorized only as a diagnostic clarification Candidate:

- preserve visible user-operated official Web protected Send;
- preserve exactly one Native parity attempt; no retry/timer/watchdog/second Send;
- capture Native HTTP-rejection JSON **structure only** and safe error-code/enum tokens where present; never full response text;
- capture Native response header names only;
- capture the triggering official successful `/resume` request and response header names only;
- capture Native request header names actually set before dispatch;
- do not copy `x-conduit-token`, OAI browser/client/session values or any browser header values;
- do not suppress official resume or test first/exclusive consumer ownership yet;
- do not modify production `ConversationRepository`, native message state, reasoning/follow-tail or response ownership.

Only b47's direct error/header evidence may justify a later request-context change. If the rejection instead points to not-found/cursor/stream ownership, a later Candidate may test Native as first/exclusive resume consumer without speculative browser-header copying.

## Background ordering

Background resilience remains a hard product requirement. b45 already provides positive short-background survival/buffering evidence, but response ownership is still unresolved.

- if Native continuation becomes accepted, background work should protect the Native response lifecycle;
- if Native continuation is disproven, WebKit true-background remains relevant only to a visible-Web fallback;
- 5/15-minute, process termination, network transition and battery/thermal remain separate gates.

## Authority / evidence boundary

- `ConversationRepository` remains sole native conversation/list/read/recovery/future response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- no second Send may be created merely to obtain a stream.
- CI/Artifact is not Runtime proof.
- b46 Code/CI/Artifact/package identity: **passed**.
- b46 Runtime Native duplicated resume: **rejected with HTTP404 JSON**.
- Native first/exclusive resume: **Unknown / Unverified**.
- Required browser/client header subset: **Unknown / Unverified**.
- Native incremental response ownership/reasoning/follow-tail/background lifecycle: **Unknown / Unverified**.
- Phase 9 Stable/Frozen Send: **No**.
- PR #29 must not be merged as accepted production Send UX while this gate remains unresolved.