# Project State

_Last updated: 2026-08-30 through exact b52 Runtime and exact b53 Code/CI/Artifact/package verification; b53 Runtime remains pending._

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

**b48-b53 are explicit diagnostic exceptions only.** The user requested trying the Native-composer/Web-Send-engine concept before deciding whether to change that durable boundary. Do not interpret diagnostic Code/CI/Artifact/Runtime success as a production policy change by itself.

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
- Three sequential Native submissions reached official protected Send HTTP200 SSE and terminal.
- Fresh new-chat turn 1 captured only 35 Native characters and lost a middle section.
- Turns 2/3 were complete and visibly incremental/effectively character-by-character; contextual value-only continuation carried most text.
- b50 remains a partial Runtime pass because the new-chat first turn was incomplete.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`.

### b51 — fresh-new-chat title-generation fix Runtime confirmed

b51 preserved an already-active assistant-text continuation across exact top-level `title_generation` and recorded `titleGenerationWhileContinuationCount` while keeping other b50 rules unchanged.

Exact b51 identity:

- Candidate `DEV-send-stream-0.1.0-b51`, version/build `0.1.0 (51)`.
- Exact product/config source `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`.
- Push Run / Job `33271794573` / `99151433241` — success.
- PR Run / Job `33271796259` / `99151437702` — success.
- Artifact `9720327648`; ZIP digest `sha256:247d22d0b8fa2d023f651c9c00461e90096e8fd21544b2147435e2d238a91ab2`.
- IPA SHA `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`.

Exact b51 Runtime on iPhone/iOS17.0:

- Fresh new-chat long turn: `nativeDeltaCount=284`, `nativeCharacters=11618`, `titleGenerationWhileContinuationCount=1`, terminal true, Web assistant text 0; user visually judged the reply complete.
- Second long turn was also visually complete.
- A later GitHub/project-progress request appeared to have a small leading gap; b52 later refined that remaining gap as reasoning-specific rather than final-answer truncation.

Accepted b51 conclusion: the b50 fresh-first-turn missing-middle defect is Runtime corrected by the title-generation continuation preservation. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b51-runtime.md`.

### b52 — final answer complete; reasoning beginning incomplete

Exact b52 identity:

- Candidate `DEV-send-stream-0.1.0-b52`, version/build `0.1.0 (52)`.
- Exact product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`.
- Push Run / Job `33276080936` / `99162937523` — success.
- PR Run / Job `33276082767` / `99162942750` — success.
- Artifact `9721532867`; ZIP digest `sha256:2ffd7e46e80019d3c4e8d6cbfa5c91dffa2a5f88222a30d5c4d5fb1e4fd752fc`.
- IPA SHA `a3de5c6eb4f7b790764fcd0adc4c98108fb550e7cedb3d6b02b931d266946b23`.

Exact b52 Runtime on iPhone/iOS17.0:

- official Send HTTP200 SSE / terminal true;
- `frameCount=74`, `nativeCharacters=614`, `nativeDeltaCount=26`;
- `exactTopLevelTextPatchCount=5`, `rootNonExactTextPatchCount=0`, `nestedTextPatchCount=6`;
- `contextualValueStringCount=15`, `inactiveValueStringCount=0`;
- `continuationResetWhileActiveCount=5`, `firstInactiveValueContext=none`, title-generation count 0;
- user observed **visible reasoning/thinking beginning slightly truncated but final answer complete**.

Accepted b52 conclusion: final-answer capture passes this exact reproduction. The prior root-nonexact→inactive-value hypothesis is rejected for this reproduction. User-visible reasoning capture remains partial; nested parent event/content type must be identified before reasoning/tool parser/UI work. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b52-runtime.md`.

### b53 — behavior-neutral reasoning/tool structure classifier

b53 preserves every b52 text filtering/output rule and only adds bounded unique structural evidence before the existing parser runs. It records at most 32 unique signatures containing safe event type, operation/path, structurally discoverable message role/content type/status/end-turn, key names and nested patch operation/path summaries. It records no prompt, answer, reasoning text, raw payload, raw IDs, auth/proof/header values or DOM reasoning state.

Exact b53 identity:

- Candidate `DEV-send-stream-0.1.0-b53`, version/build `0.1.0 (53)`.
- Exact product/config source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`.
- Push Run / Job `33294541342` / `99211838094` — success.
- PR Run / Job `33294542985` / `99211842336` — success.
- Artifact `9726996570`; ZIP digest `sha256:8831bbae1c5cad9c9cd7f0ad9fbcf4846d709b27ae950b0391d436e20749b38c`.
- IPA SHA `d5eee722ea01dc2c1b419a803574aec8ad2199299a3d0bbb51de4bae574f25dc`.
- Independent package inspection: `0.1.0 (53)`, Candidate b53, source marker `3204b183ca4f`, Release, minimum iOS14.0, UIDeviceFamily `[1,2]`, arm64.
- Runtime/manual: **Pending**.

Because Artifact `9726996570` exists, b53 is permanently reserved. Any product-code correction requires b54+ and exact b53 Runtime evidence.

## Reasoning/tool presentation boundary

`SEND_STREAM_PREFLIGHT.md` already places explicitly user-visible reasoning, reasoning→final transition and follow-tail inside `DEV-send-stream`. The requested reasoning collapse/expand and tap-driven tool-call detail sheet/popover are therefore part of the current Work, but are not yet implemented.

Only explicitly user-visible service reasoning/status/tool information may be shown. Hidden chain-of-thought or internal tool/system nodes must never be exposed or inferred. Exact b53 Runtime must first identify the service-visible reasoning/tool grammar.

## Current Runtime gate

The next human-only gate is one focused exact-device b53 reasoning/tool reproduction:

1. clear diagnostics and open `Native 输入 / Web Send（b53诊断）`;
2. send one prompt that naturally produces visible reasoning plus tool activity, preferably the same GitHub/project-progress style request;
3. observe whether reasoning starts complete or truncated, whether the final answer is complete, and whether visible tool activity occurs;
4. wait for terminal and export diagnostics.

The next parser/UI change must come from the emitted `streamStructure` signatures. Do not broaden parser grammar or implement reasoning/tool presentation by guess.

## Background ordering

Background resilience remains a hard product requirement, but implementation stays response-owner dependent. b45 provides positive short-background survival/buffering evidence. b49 additionally showed a long diagnostic response reaching terminal across multiple background intervals, but b48-b53 are still Web-owned diagnostic experiments rather than production response ownership.

## Authority / evidence boundary

- `ConversationRepository` remains sole native conversation/list/read/recovery/future accepted response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- no second Send may be created merely to obtain a stream.
- b48-b53 do not mutate production response state and do not modify TD-024/TD-025.
- Native first/exclusive resume: Unknown / Unverified.
- Existing-conversation history virtualization before Web React: Unknown / Unverified.
- Native production incremental response ownership/reasoning/follow-tail/background lifecycle: Unknown / Unverified.
- Phase 9 Stable/Frozen Send: No.
- PR #29 remains evidence-only and must not be merged as accepted production Send UX before the diagnostic architecture is separately accepted and production ownership is designed.
