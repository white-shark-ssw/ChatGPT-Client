# Project State

_Last updated: 2026-08-30 through exact b54 Runtime and exact b55 Code/CI/Artifact/package verification; b55 Runtime remains pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen.

## Current target / Work

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / not merged and evidence-only.

Current `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c` at the latest Resume/Runtime guard. Final synchronization is still required before any future merge.

The exact current testable Candidate is **`DEV-send-stream-0.1.0-b55` / `0.1.0 (55)`**, exact product/config source `aae856069b461e12dc11ee7d2d450a40ca621d21`.

## Durable Phase 9 security/product boundary

Exact b42 proved successful ChatGPT-account protected Send requires browser anti-abuse challenge output (PoW, Turnstile and `so`). Pure-native/transient-auth protected Send remains blocked.

The separately billed API-product route remains rejected. Primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.

The durable production boundary still rejects challenge solver/bypass/replay, copied proof/token values, guessed protected-Send endpoints, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping and hidden file-input injection.

**b48-b55 are explicit diagnostic exceptions only.** Their success does not by itself approve hidden/shadow Web as production architecture or transfer production response ownership away from `ConversationRepository`.

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

### b55 — exact special-structure-capacity Candidate

b55 is the smallest evidence-backed correction to b54's diagnostic limitation. It preserves all b54 protected-Send, SSE filtering, response-text extraction and Native output behavior.

Exact identity:

- Candidate `DEV-send-stream-0.1.0-b55`, version/build `0.1.0 (55)`.
- Exact product/config source `aae856069b461e12dc11ee7d2d450a40ca621d21`.
- Push Run / Job `33299965737 / 99226125826` — success.
- PR Run / Job `33299967033 / 99226129092` — success.
- Artifact `9728606514`.
- ZIP digest `sha256:fda8dfb16e3d734b9e0f0d55c4e49c0f6cd656e4ec228b13dab3cae108c0a7e3`.
- IPA SHA `f5106949814b44c6c97e2f519ff181498f6a75ff7b9bf9edf0dc0bb0bd299ad1`.
- Independent package inspection: Release / `0.1.0 (55)` / Candidate b55 / source marker `aae856069b46` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64.

Implementation-only difference from b54:

- generic unique structure set remains capped at 32;
- only `assistant:reasoning_recap`, `assistant:thoughts`, `assistant:code`, and `tool:*` additionally use a separate 24-entry special-structure set;
- special structures can still be logged after generic saturation;
- terminal metrics add special count/overflow;
- no new raw prompt/answer/reasoning/tool payload/output/ID/auth/proof data is logged.

b55 is Code/CI/Artifact/package verified and permanently reserved. Runtime/manual remains Pending.

## Reasoning / tool presentation boundary

Reasoning collapse/expand and tap-driven tool detail presentation remain in-scope for `DEV-send-stream`, but implementation is evidence-gated.

Current accepted rules:

- only explicitly user-visible service reasoning/status/tool information may be presented;
- raw `assistant:thoughts`, hidden chain-of-thought, internal tool/system nodes, raw tool arguments and raw tool results are not authorized presentation data;
- b54 proves a structural assistant-invocation→tool-result pairing grammar;
- b55 must deterministically preserve late special structures and, if `reasoning_recap` appears, expose only its text-free container/presentation metadata for the next decision.

## Current Runtime gate

Human gate is exact b55 on iPhone/iOS17:

1. install exact b55 and clear diagnostics;
2. open the b55 Native/Web-Send diagnostic surface;
3. send one request that naturally produces visible reasoning plus tool activity;
4. wait for terminal;
5. export diagnostics.

Expected UI behavior may remain similar to b54 because b55 is evidence-only.

Primary decision signals:

- `specialStructureSignatureCount` / overflow must show the special observer itself did not saturate;
- `assistant:reasoning_recap`, if emitted, must provide a concrete display-container/presentation boundary before visible reasoning UI is implemented;
- invocation/result special structures should remain available even if the generic 32-entry set fills.

Do not allocate b56 until exact b55 Runtime justifies a concrete smallest next change.

## Background ordering

Background resilience remains a hard requirement, but production implementation stays response-owner dependent. b45 and later diagnostic evidence provide positive short-background signals only; b48-b55 remain diagnostic Web-owned response experiments, not accepted production response ownership.

## Authority / evidence boundary

- `ConversationRepository` remains sole native conversation/list/read/recovery/future accepted response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- no second Send may be created merely to obtain a stream.
- b48-b55 do not mutate production response state and do not modify TD-024/TD-025.
- Native first/exclusive resume: Unknown / Unverified.
- Existing-conversation history virtualization before Web React: Unknown / Unverified.
- Native production incremental response ownership/reasoning/follow-tail/background lifecycle: Unknown / Unverified.
- Phase 9 Stable/Frozen Send: No.
- PR #29 remains evidence-only and must not be merged as accepted production Send UX before the diagnostic architecture is separately accepted and production ownership is designed.
