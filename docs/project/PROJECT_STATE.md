# Project State

_Last updated: 2026-08-30 through exact b55 Runtime and exact b56 Code/CI/Artifact/package verification; b56 Runtime remains pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen.

## Current target / Work

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / not merged and evidence-only.

Current `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c` at the latest Resume/Runtime guard. Final synchronization is still required before any future merge.

The exact current testable Candidate is **`DEV-send-stream-0.1.0-b56` / `0.1.0 (56)`**, exact product/config source `cec921030fd1af9f3853f35af52b661586b3a8ab`.

## Durable Phase 9 security/product boundary

Exact b42 proved successful ChatGPT-account protected Send requires browser anti-abuse challenge output (PoW, Turnstile and `so`). Pure-native/transient-auth protected Send remains blocked.

The separately billed API-product route remains rejected. Primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.

The durable production boundary still rejects challenge solver/bypass/replay, copied proof/token values, guessed protected-Send endpoints, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping and hidden file-input injection.

**b48-b56 are explicit diagnostic exceptions only.** Their success does not by itself approve hidden/shadow Web as production architecture or transfer production response ownership away from `ConversationRepository`.

`/backend-api/f/conversation/resume` remains a post-Send continuation/read path and does not weaken the protected-Send boundary.

## Full-Web product evidence

- b43 showed visible official-Web interaction could be acceptable in a shorter tested sequence, including Web `+` around 100–200ms.
- b44 full-page Native→Web→Native product form was rejected; immediate Native reconciliation could lag Web-visible output.
- b47 exact-device evidence established a long-answer conversation could repeatedly freeze when trying to use the mobile-Web composer even with only a few rounds.
- Earlier wrapped-Web/userscript experience also showed that hiding most rendered rounds did not make the full-Web conversation surface acceptable.

The internal cause of the composer freeze remains Unknown / Unverified. Product consequence is accepted: full existing-conversation Web rendering before every Send is not a daily production dependency.

## Official no-resend continuation / Native parity

- b45 Runtime Confirmed official `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` returning HTTP200 SSE and repeatedly continuing the same response without a second Send. Short background/lock survival/buffering was also positive.
- b46/b47 Native duplicated-after-official-success Cookie+Bearer-only resume each returned HTTP404 JSON while later official resume remained healthy.
- Native first/exclusive resume and the exact additional browser/client context it may require remain Unknown / Unverified.

## Native composer / Web Send-engine diagnostic progression

### b48-b50 — transport and compact streaming grammar

- b48 proved Native input can drive sequential official protected Sends; parser used wrong long-form patch names.
- b49 proved real incremental Native delivery from compact `o/p/v` patches but captured only short explicit fragments.
- b50 added contextual `{v:string}` continuation and materially passed established turns, while fresh new-chat turn 1 still lost a middle section.

### b51 — fresh-new-chat missing-middle corrected

Exact b51 preserved active assistant-text continuation across top-level `title_generation`. Fresh long turn delivered 11,618 Native chars / 284 deltas with title-generation count 1 and was visually complete; second long turn was also complete.

Accepted: the b50 fresh-first-turn missing-middle defect is Runtime corrected. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b51-runtime.md`.

### b52 — remaining gap is reasoning-specific

Exact b52 Runtime: HTTP200 SSE / terminal true; final answer complete; visible reasoning beginning slightly truncated. `rootNonExactTextPatchCount=0`, `inactiveValueStringCount=0`, so the prior root-nonexact/inactive-value theory is rejected for that reproduction.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b52-runtime.md`.

### b53 — explicit reasoning/tool message classes identified

Exact b53 Runtime user observation:

- visible reasoning beginning still truncated;
- final answer complete;
- Native showed no tool-call presentation.

The stream directly identified:

- `assistant:reasoning_recap`;
- separate `assistant:thoughts`;
- `assistant:code`;
- `tool:text`, `tool:code`, `tool:multimodal_text`.

Accepted boundary:

- service-side tool activity is real even though Native showed no tool UI;
- `reasoning_recap` is a direct candidate for explicitly user-visible reasoning;
- raw `thoughts` is non-presentational and must not be exposed;
- content type alone does not prove user-visible tool/result boundaries.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b53-runtime.md`.

### b54 — tool pairing identified; recap gate blocked by diagnostic saturation

Exact b54 identity:

- Candidate `DEV-send-stream-0.1.0-b54`, version/build `0.1.0 (54)`.
- Exact source `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`.
- Push `33296672444 / 99217423647`; PR `33296674388 / 99217428590` — success.
- Artifact `9727636043`; ZIP `sha256:28d07c99634a1b4f917561e95cf04a4e95666106985cb03bca09798b0dc7065c`.
- IPA SHA `d4b85cffe4db499252d0bc9a2c7c8ea582acf2b88f3d28eeb60e366ee471153b`.

Exact b54 Runtime diagnostics matched build 54 / Candidate b54 / source `6a6903c7ad56` / Release / iPhone iOS17.0. One Send returned HTTP200 SSE and terminal true.

Key metrics: `frameCount=73`, Native 22 deltas / 412 chars, exact-root text patches 4, nested 3, contextual value strings 15 / 312 chars, inactive value strings 0, generic structure signatures **32 / overflow 13**.

New tool facts:

- assistant `code` invocation messages carry concrete recipients such as `api_tool.list_resources` / `api_tool.call_tool`;
- completed assistant code carries `is_complete:true`, `connector_tool_payload`, `tool_icons` metadata;
- tool results identify author names such as `api_tool` / `api_tool.call_tool`, `recipient=all`, and text/code/multimodal result containers;
- `invoked_plugin` / `invoked_resource` metadata exists where applicable.

Accepted: invocation/result nodes can be paired structurally. Raw arguments/results and every internal node are not automatically user-visible.

New reasoning facts:

- `assistant:thoughts / finished_successfully` contains a `thoughts` array whose object has keys `chunks,content,finished,summary`;
- metadata includes `can_save:false`, `reasoning_status:is_reasoning`, `tool_summary_type:github`, and structural `inline_cot_expandable_content` / `tool_icons` state.

Raw thoughts/chunks/internal reasoning remain excluded from presentation. Because the generic observer saturated at 32 and overflowed 13 later unique structures, the absence of logged `reasoning_recap` cannot be interpreted as protocol absence. b54 is therefore a **partial Runtime pass**: tool grammar materially identified, recap display-container gate inconclusive.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b54-runtime.md`.

### b55 — special channel passes; recap container/presentation semantics proved

Exact b55 identity:

- Candidate `DEV-send-stream-0.1.0-b55`, version/build `0.1.0 (55)`.
- Exact product/config source `aae856069b461e12dc11ee7d2d450a40ca621d21`.
- Push Run / Job `33299965737 / 99226125826` — success.
- PR Run / Job `33299967033 / 99226129092` — success.
- Artifact `9728606514`.
- ZIP digest `sha256:fda8dfb16e3d734b9e0f0d55c4e49c0f6cd656e4ec228b13dab3cae108c0a7e3`.
- IPA SHA `f5106949814b44c6c97e2f519ff181498f6a75ff7b9bf9edf0dc0bb0bd299ad1`.

Exact b55 Runtime matched build 55 / Candidate b55 / source `aae856069b46` on iPhone/iOS17.0 and completed one HTTP200 SSE Send to terminal.

Key metrics: `frameCount=69`, Native 24 deltas / 481 chars, generic structures **32 / overflow14**, special structures **7 / overflow0**, inactive value strings 0.

The intended late special message was retained at event 41:

- `assistant:reasoning_recap`;
- status `finished_successfully`;
- recipient `all`;
- content keys `content,content_type`;
- exact-turn content string shape `content_type:15,content:7`;
- `can_save:false`;
- `reasoning_status:reasoning_ended`;
- `reasoning_recap_type:collapse`.

Accepted: the concrete service recap text container is `message.content.content`, and the service provides a direct reasoning-end + collapsed-recap presentation boundary.

`assistant:thoughts` remained a separate structure immediately before the recap and is still prohibited from presentation. Tool invocation/result structure remained available, but exact tool-node user visibility remains unproven.

Classification: **b55 Runtime pass for its intended gate.** Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b55-runtime.md`.

### b56 — exact Native reasoning-recap presentation Candidate

Exact identity:

- Candidate `DEV-send-stream-0.1.0-b56`, version/build `0.1.0 (56)`.
- Exact product/config source `cec921030fd1af9f3853f35af52b661586b3a8ab`.
- Product tree `3ef2884676132becfde01b42826a711a8b3ca893`.
- Push Run / Job `33301008807 / 99229039032` — success.
- PR Run / Job `33301010617 / 99229043710` — success.
- Artifact `9728937100`.
- ZIP digest `sha256:2f4b5a216298e9c79ccbec2a7f4420719c8406120815f568c0ddd8b89d46d430`.
- IPA SHA `da62776200ce94fef95326abaea3b980f65a5698df5dfe481bd34046e0f8dbe6`.
- Package independently verified: Release / `0.1.0 (56)` / Candidate b56 / source marker `cec921030fd1` / minimum iOS14 / `[1,2]` / arm64.

b56 preserves b55 protected-Send and text interception behavior. It adds only an evidence-backed recap path:

- exact assistant `reasoning_recap` + `finished_successfully` + `recipient=all` + `reasoning_ended` + `collapse`;
- non-empty `message.content.content` bridged to Native;
- distinct `思考摘要 ▸` region appears only after a matching recap;
- default collapsed, explicit user expand/collapse;
- diagnostics log only character count/presentation state, never recap text;
- raw `assistant:thoughts`, raw tool payloads, tool UI and reasoning→final text-phase separation remain unchanged/unimplemented.

b56 Code/CI/Artifact/package are verified and the identity is permanently reserved. Runtime/manual remains Pending.

## Reasoning / tool presentation boundary

Reasoning collapse/expand and tap-driven tool detail presentation remain in-scope for `DEV-send-stream`, but implementation remains evidence-gated.

Current accepted rules:

- only explicitly user-visible service reasoning/status/tool information may be presented;
- exact b55 authorizes the `reasoning_recap` string for diagnostic Native presentation;
- raw `assistant:thoughts`, hidden chain-of-thought, internal tool/system nodes, raw tool arguments and raw tool results are not authorized presentation data;
- b54/b55 prove a structural assistant-invocation→tool-result pairing grammar, but not exact user-visible tool-node boundaries;
- b56 must Runtime-confirm that the exact recap extraction produces a coherent visible summary and correct collapse/expand behavior before any broader reasoning-phase parser changes.

## Current Runtime gate

Human gate is exact b56 on iPhone/iOS17:

1. install exact b56 and clear diagnostics;
2. open the b56 Native/Web-Send diagnostic surface;
3. send one request that naturally produces visible reasoning plus tool activity;
4. verify `思考摘要 ▸` appears only after the service recap;
5. expand/collapse and visually confirm the recap is coherent user-visible summary content;
6. confirm raw thoughts/tool payloads are absent;
7. wait for terminal and export diagnostics.

The current text area intentionally remains b55 behavior; b56 does not yet prove or implement the exact reasoning→final text-patch phase split.

Do not allocate b57 until exact b56 Runtime supplies a concrete smallest next change.

## Background ordering

Background resilience remains a hard requirement, but production implementation stays response-owner dependent. b45 and later diagnostic evidence provide positive short-background signals only; b48-b56 remain diagnostic Web-owned response experiments, not accepted production response ownership.

## Authority / evidence boundary

- `ConversationRepository` remains sole native conversation/list/read/recovery/future accepted response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- no second Send may be created merely to obtain a stream.
- b48-b56 do not mutate production response state and do not modify TD-024/TD-025.
- Native first/exclusive resume: Unknown / Unverified.
- Existing-conversation history virtualization before Web React: Unknown / Unverified.
- Native production incremental response ownership/reasoning/follow-tail/background lifecycle: Unknown / Unverified.
- Phase 9 Stable/Frozen Send: No.
- PR #29 remains evidence-only and must not be merged as accepted production Send UX before the diagnostic architecture is separately accepted and production ownership is designed.
