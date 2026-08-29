# Project State

_Last updated: 2026-08-29 through exact b47 Runtime and the long-conversation visible-Web composer viability failure._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen.

## Current target/base status

`DEV-send-stream` was activated from `main@34811877896ca88c6656be6676f5466a19931ce6`.

Current `main` is `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; its target-only delta is repository-governance `AGENTS.md` work with no product/state-owner overlap. Final synchronization remains required before any future merge.

Current feature branch: `dev/send-stream-20260829`; PR #29 remains open / mergeable / not merged.

## Phase 9 security/product boundary

Exact b42 proved successful ChatGPT-account **protected Send** requires browser anti-abuse challenge output: PoW, Turnstile and `so`; non-empty PoW + Turnstile were finalized before successful Send. Pure-native/transient-auth protected Send remains blocked.

The user explicitly rejects the separate API-product route.

Still prohibited: challenge solver/bypass/replay, copied proof/token values, guessed Send/continuation endpoints, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Web Send clicks, DOM answer/reasoning scraping and hidden file-input injection.

`/backend-api/f/conversation/resume` is a **post-Send continuation/read path** and does not weaken the b42 protected-Send boundary.

## Visible-Web product evidence

- b43: visible official-Web interaction was sufficiently smooth for its tested shorter iPhone/iOS17 sequence; Web `+` ~100–200ms; Photos chooser filtered videos; standalone Web-chat product form not accepted.
- b44: tested `/c/<id>` A/B mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; full-page Native -> Web -> Native product form rejected. No timer/poll/retry workaround is accepted.
- **b47 exact-device long-conversation result materially narrows b43**: the user reported that an older conversation with only about three rounds but long answers repeatedly froze when trying to bring up/use the mobile-Web composer, making that conversation unusable for the protocol test. The test therefore had to be completed in a new conversation.

The b47 export does not contain the failed long-conversation attempt, so its internal root cause remains Unknown / Unverified. Product impact is nevertheless direct: an architecture requiring the real full Web conversation before every protected Send can fail **before Send initiation**, which Native post-Send handoff cannot repair.

## Exact b45 official no-resend continuation

- Candidate `DEV-send-stream-0.1.0-b45`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868`.
- Uninterrupted Send uses original `/backend-api/f/conversation` SSE through terminal.
- Clean default-primary new-chat response survived/buffered repeated active-response background/lock including ~126s continuous without resend/refresh.
- Forced interruption proved official `POST /backend-api/f/conversation/resume` body `{conversation_id: string, offset: number}` and HTTP200 `text/event-stream` continuation that can repeatedly continue the same response to `[DONE]` without a second Send.

Official resume request header-name evidence includes ordinary auth/client/session/route names and `x-conduit-token`; no Sentinel/Turnstile/PoW names were observed on resume. Header-name presence alone does not establish requirement.

## Exact b46 Native duplicated resume parity

- Candidate `DEV-send-stream-0.1.0-b46`, exact source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`, legitimate Artifact `9715903443`, IPA SHA `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`.
- Official offset 18 resume returned HTTP200 SSE.
- Native same-body request using only WebKit-derived transient cookie + bearer returned **HTTP404 `application/json`, 116 bytes, 0 SSE frames**.
- Later official offset 54 resume again returned HTTP200 SSE.

Accepted: official no-resend resume Runtime Confirmed; Native Cookie+Bearer-only **duplicated-after-official-success** resume Runtime Rejected. Missing request context vs cursor/consumer ownership remained unresolved.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`.

## Exact b47 Candidate / Runtime

- Candidate `DEV-send-stream-0.1.0-b47`, `0.1.0 (47)`.
- Exact product/config source `21028bbff7982abeb42f130c56fcb21e6ef44d7a`.
- Push Run / Job `33259640112` / `99119258573` — success.
- PR Run / Job `33259642459` / `99119264902` — success.
- Legitimate Push Artifact `9716878034`; ZIP digest `sha256:a6915d0a2c48877e8d4d5b7eea966118ad84b321bc1462dafe55c593796e10fc`.
- IPA SHA `49d1bd4886310f7761883784f73fc5532fe1a9532773619f0796cd7aab816909`.
- Package identity independently verified: Release, source `21028bbff798`, iOS14 minimum, `[1,2]`, arm64.

### b47 protocol Runtime

Uploaded metadata exactly matched b47 / Release / iPhone / iOS17.0.

- official `/resume` offset 23 first hit a transport error while connectivity was unavailable, then official Web retried the same offset and returned HTTP200 SSE;
- b47 issued exactly one Native same-body parity request;
- transient account/session verification succeeded;
- Native `/resume` returned **HTTP404 `application/json`, ~707ms, 116 bytes, 0 SSE frames**;
- rejection JSON shape was `{"detail":{"code":"string","message":"string"}}`;
- later official Web resumed again at progressed offset 74 with HTTP200 SSE;
- no Native retry occurred.

Successful official resume request header names were:

`accept, authorization, content-type, oai-client-build-number, oai-client-version, oai-device-id, oai-echo-logs, oai-language, oai-session-id, x-conduit-token, x-oai-is-client-observation, x-oai-is-pending-updates, x-oai-turn-trace-id, x-openai-target-path, x-openai-target-route`

Native explicitly set only `accept, content-type`, plus the established transient Authorization injection and WebKit-derived ephemeral cookies.

This proves a large request-context structural difference, but does **not** identify a required header subset and does not authorize copying browser values.

### b47 diagnostics defect

The intended safe error-code export field was named `safeErrorTokens`; current `DiagnosticsSanitizer` redacts every field key containing `token`, so the safe code/type/status values were exported as `<redacted>`. This is a deterministic diagnostic naming defect. Correcting product code would require b48+ because b47 is reserved.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b47-runtime.md`.

## Current architecture viability gate

Previous target:

`Native history/presentation -> user-visible official full Web conversation performs protected Send -> Native attaches/resumes to the same already-started response.`

After the long-conversation composer failure, this exact form is **not accepted for further production integration** without a deliberate architecture decision. The failure occurs before Native handoff can begin.

Do not allocate b48 merely to chase `/resume` headers while the Send surface itself has an exact-device P0 usability failure.

Evidence-backed next questions:

1. Does an official supported **lightweight visible send-only** surface exist that avoids full conversation-history Web rendering?
2. Is there another legitimate account-compatible protected-Send boundary that avoids full mobile-Web conversation rendering without hidden DOM automation/challenge bypass?
3. If neither exists, should visible Web remain diagnostic/fallback only rather than the daily-chat production Send architecture?

These are now a Human Architecture Gate; do not guess the product direction.

## Background ordering

Background resilience remains a hard product requirement, but implementation stays response-owner dependent. b45 provides positive short-background survival/buffering evidence. Native production continuation ownership is not accepted, and visible-full-Web Send now also has a pre-Send long-conversation viability failure.

## Authority / evidence boundary

- `ConversationRepository` remains sole native conversation/list/read/recovery/future accepted response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- no second Send may be created merely to obtain a stream.
- b47 Code/CI/Artifact/package identity: **passed**.
- b47 Runtime/manual: **completed**.
- b47 Native duplicated resume: **rejected with HTTP404 JSON**.
- b47 full-Web long-conversation composer viability: **failed for the reported exact-device workload**.
- Native first/exclusive resume: **Unknown / Unverified**.
- Required browser/client header subset: **Unknown / Unverified**.
- lightweight official visible send-only route: **Unknown / Unverified**.
- Native incremental response ownership/reasoning/follow-tail/background lifecycle: **Unknown / Unverified**.
- Phase 9 Stable/Frozen Send: **No**.
- PR #29 remains evidence-only and must not be merged as accepted production Send UX while this architecture gate remains unresolved.