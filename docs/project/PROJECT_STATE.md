# Project State

_Last updated: 2026-08-30 through exact b48 Code/CI/Artifact/package verification; b48 Runtime remains pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen.

## Current target/base status

`DEV-send-stream` was activated from `main@34811877896ca88c6656be6676f5466a19931ce6`.

Current `main` is `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; its target-only delta is repository-governance work with no current product/state-owner conflict established. Final synchronization remains required before any future merge.

Current feature branch: `dev/send-stream-20260829`; PR #29 remains open / mergeable / not merged.

## Phase 9 security/product boundary

Exact b42 proved successful ChatGPT-account **protected Send** requires browser anti-abuse challenge output: PoW, Turnstile and `so`; non-empty PoW + Turnstile were finalized before successful Send. Pure-native/transient-auth protected Send remains blocked.

The user explicitly rejects the separately billed API-product route and has also blocked primary-account Sub2API/Codex-subscription Runtime because of account-safety concerns.

The durable production boundary still prohibits challenge solver/bypass/replay, copied proof/token values, guessed Send/continuation endpoints, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Web Send clicks, DOM answer/reasoning scraping and hidden file-input injection.

**b48 is an explicit diagnostic exception only.** The user asked to try one version before deciding whether to change that durable boundary. Do not interpret b48 Code/CI/Artifact success as production policy change.

`/backend-api/f/conversation/resume` remains a **post-Send continuation/read path** and does not weaken the b42 protected-Send boundary.

## Visible-Web product evidence

- b43: visible official-Web interaction was sufficiently smooth for its tested shorter iPhone/iOS17 sequence; Web `+` ~100–200ms; Photos chooser filtered videos; standalone Web-chat product form not accepted.
- b44: tested `/c/<id>` A/B mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; full-page Native -> Web -> Native product form rejected. No timer/poll/retry workaround is accepted.
- b47 exact-device long-conversation evidence materially narrows b43: an older conversation with only about three rounds but long answers repeatedly froze when trying to bring up/use the mobile-Web composer, so the user completed protocol testing in a new conversation.
- The user's prior wrapped-Web/userscript experiment also showed that loading the full conversation and hiding all but roughly two visible rounds did not make the Web `+`/overall interaction acceptable.

The internal owner of the b47 composer freeze remains Unknown / Unverified. Product impact is direct: full existing-conversation Web rendering before every protected Send is not accepted as the daily-chat production dependency.

## Exact b45 official no-resend continuation

- Candidate `DEV-send-stream-0.1.0-b45`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868`.
- Uninterrupted Send uses original `/backend-api/f/conversation` SSE through terminal.
- Clean default-primary new-chat response survived/buffered repeated active-response background/lock including ~126s continuous without resend/refresh.
- Forced interruption proved official `POST /backend-api/f/conversation/resume` body `{conversation_id: string, offset: number}` and HTTP200 `text/event-stream` continuation that can repeatedly continue the same response to `[DONE]` without a second Send.

Official resume request header-name evidence includes ordinary auth/client/session/route names and `x-conduit-token`; no Sentinel/Turnstile/PoW names were observed on resume. Header-name presence alone does not establish requirement.

## Exact b46/b47 Native duplicated resume parity

### b46

- Candidate `DEV-send-stream-0.1.0-b46`, exact source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`, legitimate Artifact `9715903443`, IPA SHA `2c64a6356fdf419ea540b8c40fd9026061f5afaec9631bdb79bbeab8164becec`.
- Official offset 18 resume returned HTTP200 SSE.
- Native same-body request using WebKit-derived transient cookie + bearer returned HTTP404 `application/json`, 116 bytes, 0 SSE frames.
- Later official offset 54 resume again returned HTTP200 SSE.

### b47

- Candidate `DEV-send-stream-0.1.0-b47`, exact source `21028bbff7982abeb42f130c56fcb21e6ef44d7a`, legitimate Artifact `9716878034`, IPA SHA `49d1bd4886310f7761883784f73fc5532fe1a9532773619f0796cd7aab816909`.
- Official offset 23 resumed with HTTP200 SSE after the forced connectivity interruption.
- One Native same-body duplicate again returned HTTP404 `application/json`, ~707ms, 116 bytes, 0 SSE frames; rejection shape `{detail:{code:string,message:string}}`.
- Later official offset 74 resume again returned HTTP200 SSE.
- No Native retry occurred.

Accepted: official no-resend resume Runtime Confirmed; Native Cookie+Bearer-only **duplicated-after-official-success** resume Runtime Rejected. Native first/exclusive resume and required browser/client context remain Unknown / Unverified.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`, `docs/project/runtime-evidence/DEV-send-stream-b47-runtime.md`.

## Exact b48 Native composer / filtered Web Send experiment

The user explicitly requested one isolated experiment before any durable change to the hidden/shadow-Web boundary.

- Candidate `DEV-send-stream-0.1.0-b48`, version/build `0.1.0 (48)`.
- Exact product/config source `6ccba03cefaa32a1186f1f468c3e696ed9457699`.
- Push Run / Job `33266782947` / `99138125987` — success.
- PR Run / Job `33266784665` / `99138130204` — success.
- Legitimate Push Artifact `9718885751`.
- Artifact ZIP digest `sha256:b990c539750e042d2912f3ea197568c9a5253b6393b9103b3cf6d4703f951afd`.
- IPA SHA `c1f2f6a4e750af8abc7438e289f709cdf23c564f06ce2118b1c9b74f2d8ed850`.
- Package identity independently verified: `0.1.0 (48)`, Candidate b48, Release, source marker `6ccba03cefaa`, minimum iOS14, `[1,2]`, arm64.

b48 is a **diagnostic controller only**:

- a full-size official `WKWebView` on the default persistent WebKit data store remains behind an opaque Native surface;
- user normally operates only a Native `UITextView` composer + Native Send button;
- document-start JavaScript transfers the Native text into the actual Web composer state and invokes the page's own form/Send control;
- the official page remains responsible for login, browser challenges and protected `/backend-api/f/conversation` construction;
- the Send SSE is consumed once before Web React; evidenced assistant text append patches at `/message/content/parts/0` are forwarded to Native memory/UI and removed from the stream returned to Web while remaining lifecycle/identity frames and `[DONE]` are preserved;
- Web user/assistant message elements are CSS-suppressed for the diagnostic surface;
- no `response.clone()` is used on this interception path;
- diagnostics record structural counts/status/DOM metrics only, never prompt/answer/reasoning text;
- no `ConversationRepository` production response state is mutated;
- no retry/timer/watchdog/fallback is added;
- b48 is new-chat focused and does **not** yet virtualize existing conversation-detail history before React.

Evidence ladder for b48:

- Code written: **Yes**.
- CI: **Passed**.
- Artifact produced: **Yes**.
- Package identity: **Verified**.
- Runtime/manual/real-device: **Pending**.
- Stable/Frozen: **No**.

Because Artifact `9718885751` now exists, exact b48 source is permanently reserved. Any product-code correction after Runtime must use b49+.

## b48 Runtime gate

Exact-device testing must determine:

1. Native composer can submit without the user touching the Web composer.
2. Official Web protected Send still succeeds.
3. Native receives incremental assistant text while the corresponding text patch is withheld from Web React.
4. Web assistant text/DOM footprint stays small during a long answer.
5. A second Native-composer turn succeeds in the same Web session after terminal `[DONE]`.
6. Native typing/Send interaction feels smooth.

Passing b48 would only justify a later experiment on **existing-conversation data-layer history virtualization before React**. It would not by itself change TD-024/TD-025 or prove long existing-chat performance.

## Background ordering

Background resilience remains a hard product requirement, but implementation stays response-owner dependent. b45 provides positive short-background survival/buffering evidence. Native production continuation ownership is not accepted, and visible-full-Web Send has a separate pre-Send long-conversation viability failure.

## Authority / evidence boundary

- `ConversationRepository` remains sole native conversation/list/read/recovery/future accepted response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- no second Send may be created merely to obtain a stream.
- b48 is not production state ownership and not a durable security-boundary change.
- Native first/exclusive resume: **Unknown / Unverified**.
- Existing-conversation history virtualization before Web React: **Unknown / Unverified**.
- Native production incremental response ownership/reasoning/follow-tail/background lifecycle: **Unknown / Unverified**.
- Phase 9 Stable/Frozen Send: **No**.
- PR #29 remains evidence-only and must not be merged as accepted production Send UX before b48 Runtime and a later explicit architecture decision.