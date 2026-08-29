# Project State

_Last updated: 2026-08-30 through exact b50 Runtime and exact b51 Code/CI/Artifact/package verification; b51 Runtime remains pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen.

## Current target/base status

`DEV-send-stream` was activated from `main@34811877896ca88c6656be6676f5466a19931ce6`.

Current `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; its target-only delta is repository-governance work with no current product/state-owner conflict established. Final synchronization remains required before any future merge.

Current feature branch: `dev/send-stream-20260829`; PR #29 remains open / mergeable / not merged and is evidence-only.

## Phase 9 security/product boundary

Exact b42 proved successful ChatGPT-account **protected Send** requires browser anti-abuse challenge output: PoW, Turnstile and `so`; non-empty PoW + Turnstile were finalized before successful Send. Pure-native/transient-auth protected Send remains blocked.

The user rejects the separately billed API-product route and has also blocked primary-account Sub2API/Codex-subscription Runtime because of account-safety concerns.

The durable production boundary still prohibits challenge solver/bypass/replay, copied proof/token values, guessed Send/continuation endpoints, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Web Send clicks, DOM answer/reasoning scraping and hidden file-input injection.

**b48-b51 are explicit diagnostic exceptions only.** The user requested trying the Native-composer/Web-Send-engine concept before deciding whether to change that durable boundary. Do not interpret diagnostic Code/CI/Artifact/Runtime success as a production policy change by itself.

`/backend-api/f/conversation/resume` remains a post-Send continuation/read path and does not weaken the b42 protected-Send boundary.

## Full-Web product evidence

- b43: visible official-Web interaction was sufficiently smooth for its tested shorter iPhone/iOS17 sequence; Web `+` ~100–200ms; Photos chooser filtered videos; standalone Web-chat product form not accepted.
- b44: tested `/c/<id>` A/B mapping worked, but immediate Native reconciliation could lag assistant output already visible in Web; full-page Native -> Web -> Native product form rejected. No timer/poll/retry workaround is accepted.
- b47 exact-device long-conversation evidence materially narrows b43: an older conversation with only about three rounds but long answers repeatedly froze when trying to bring up/use the mobile-Web composer, so the user completed protocol testing in a new conversation.
- The user's earlier wrapped-Web/userscript experiment also showed that loading the full conversation and hiding all but roughly two visible rounds did not make the Web `+`/overall interaction acceptable.

The internal owner of the b47 composer freeze remains Unknown / Unverified. Product impact is direct: full existing-conversation Web rendering before every protected Send is not accepted as the daily-chat production dependency.

## Exact b45 official no-resend continuation

- Candidate `DEV-send-stream-0.1.0-b45`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, legitimate Artifact `9713774868`.
- Uninterrupted Send uses original `/backend-api/f/conversation` SSE through terminal.
- Clean default-primary new-chat response survived/buffered repeated active-response background/lock including ~126s continuous without resend/refresh.
- Forced interruption proved official `POST /backend-api/f/conversation/resume` body `{conversation_id: string, offset: number}` and HTTP200 `text/event-stream` continuation that can repeatedly continue the same response to `[DONE]` without a second Send.

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

## Native-composer / Web-Send-engine diagnostic progression

### b48 — Native Send path works; parser field names wrong

- Candidate `DEV-send-stream-0.1.0-b48`, exact product/config source `6ccba03cefaa32a1186f1f468c3e696ed9457699`, Artifact `9718885751`, IPA SHA `c1f2f6a4e750af8abc7438e289f709cdf23c564f06ce2118b1c9b74f2d8ed850`.
- Exact-device Runtime proved the Native composer can drive the official page's own protected Send for two sequential turns and preserve enough Web conversation state for the second Send.
- The Send SSE was intercepted, but the b48 parser used long-form `op/path/value` while current compact Runtime evidence uses `o/p/v`; zero assistant text patches were captured to Native and Web received the full answer.
- b48 is Runtime-completed/superseded, not Stable.

### b49 — real incremental Native delivery, incomplete response capture

- Candidate `DEV-send-stream-0.1.0-b49`, exact source `20fb8f3f400200965acb868aeb8a7504b9bfb91f`, Artifact `9719418761`, IPA SHA `88bd8e46b054169cb1f4338d91bb06c216edbf204b9a440a5cdc678ea6e4cd95`.
- Exact-device Runtime proved real incremental Native text delivery for two sequential protected Sends, but only two short explicit compact `o/p/v` text patches per turn were captured.
- Historical b40 evidence explained the missing middle: contextual value-only `{v:string}` continuation frames follow explicit assistant append patches.
- Complete-response interception was rejected on b49.

### b50 — diagnostic core materially passes on established turns

- Candidate `DEV-send-stream-0.1.0-b50`, exact source `837d5feeff05d198785f884ccf9cc4c1f71412ec`, Artifact `9719942650`, IPA SHA `26431faabe0b2c836fd6c1d7aa84d31cf8811ea09d57a8ad692e127ecb42613c`.
- User tested three sequential Native-composer turns and described the overall effect as very good.
- All three Native submissions reached official protected Send HTTP200 SSE and normal terminal; composer returned ready for following turns.
- Turn 1 (fresh new-chat first turn): `frameCount=34`, `contextualValueStringCount=1`, `nativeDeltaCount=3`, `nativeCharacters=35`; user reported the actual server answer was long and Native lost a middle section. Complete interception rejected for this turn.
- Turn 2: `contextualValueStringCount=8`, `nativeDeltaCount=10`, `nativeCharacters=191`, `webAssistantTextCharacters=45`; user reported complete visibly incremental output.
- Turn 3: `contextualValueStringCount=29`, `nativeDeltaCount=31`, `nativeCharacters=671`, `webAssistantTextCharacters=45`; user reported complete visibly incremental, effectively character-by-character output.
- Accepted diagnostic conclusions: contextual value-only compact continuation is real and carries most assistant text; Native incremental streaming is Runtime Confirmed for this diagnostic path; Web assistant DOM can remain small while Native receives materially more text; sequential official protected Send remains viable in the fresh session.
- b50 remains a **partial Runtime pass** because the new-chat first turn was incomplete.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`.

### b51 — exact new-chat title-generation continuation experiment

Historical exact b40/b41 evidence established that a new-chat first Send emits a `title_generation` structural event. b50 cleared active assistant-text continuation on every structural frame that was not explicit assistant append or contextual value-only text. This exactly matches the one case that still failed: the first turn of a new conversation.

b51 makes only the narrow diagnostic change:

- when assistant-text continuation is active and an exact top-level event has `type == "title_generation"` with no `o`/`p`, forward it unchanged to Web **without** clearing the continuation;
- record `titleGenerationWhileContinuationCount`;
- keep all other b50 reset/filter rules unchanged.

Exact b51 identity:

- Candidate `DEV-send-stream-0.1.0-b51`, version/build `0.1.0 (51)`.
- Exact product/config source `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`.
- Push Run / Job `33271794573` / `99151433241` — success.
- PR Run / Job `33271796259` / `99151437702` — success.
- Artifact `9720327648`.
- Artifact ZIP digest `sha256:247d22d0b8fa2d023f651c9c00461e90096e8fd21544b2147435e2d238a91ab2`.
- IPA SHA `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`.
- Package identity independently verified: `0.1.0 (51)`, Candidate b51, source marker `bd8f056cc4d1`, Release, minimum iOS14.0, UIDeviceFamily `[1,2]`, arm64.
- Runtime/manual: **Pending**.

Because Artifact `9720327648` exists, exact b51 is permanently reserved; any product-code correction requires b52+.

## Current Runtime gate

The next human-only gate is exact-device b51 fresh-new-chat testing:

1. clear diagnostics and open `Native 输入 / Web Send（b51诊断）`;
2. first Native turn requests a genuinely long answer;
3. verify first answer is incrementally complete through the middle;
4. after terminal, send a second Native turn;
5. export diagnostics after second terminal.

Pass signal for the first turn includes `titleGenerationWhileContinuationCount > 0` if the hypothesis is correct, long-answer-scale contextual/native character counts, terminal true, small Web assistant DOM text, and a successful second Send. If the metric is zero or truncation remains, parser grammar must not be broadened by guess; collect the smallest structural evidence needed to identify the actual reset frame.

## Background ordering

Background resilience remains a hard product requirement, but implementation stays response-owner dependent. b45 provides positive short-background survival/buffering evidence. b49 additionally showed a long diagnostic response reaching terminal across multiple background intervals, but b48-b51 are still Web-owned diagnostic experiments rather than production response ownership.

## Authority / evidence boundary

- `ConversationRepository` remains sole native conversation/list/read/recovery/future accepted response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- no second Send may be created merely to obtain a stream.
- b48-b51 do not mutate production response state and do not modify TD-024/TD-025.
- Native first/exclusive resume: Unknown / Unverified.
- Existing-conversation history virtualization before Web React: Unknown / Unverified.
- Native production incremental response ownership/reasoning/follow-tail/background lifecycle: Unknown / Unverified.
- Phase 9 Stable/Frozen Send: No.
- PR #29 remains evidence-only and must not be merged as accepted production Send UX before the diagnostic architecture is separately accepted and production ownership is designed.