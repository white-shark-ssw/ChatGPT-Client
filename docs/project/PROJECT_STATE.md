# Project State

_Last updated: 2026-08-30 through exact b56 Runtime and exact b57 Code/CI/Artifact/package verification; b57 Runtime remains pending._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen.

## Current target / Work

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / not merged and evidence-only.

Current `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c` at the latest light guard. Final synchronization remains required before any future merge.

The exact current testable Candidate is **`DEV-send-stream-0.1.0-b57` / `0.1.0 (57)`**, exact product/config source `7074b1f85a0f239a5fd615f52196e1e28145523c`, Artifact `9729360247`, IPA SHA `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`.

## Durable Phase 9 security/product boundary

Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output (PoW, Turnstile and `so`). Pure-native/transient-auth protected Send remains blocked.

The separately billed API-product route remains rejected. Primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.

The durable production boundary still rejects challenge solver/bypass/replay, copied proof/token values, guessed protected-Send endpoints, hidden/shadow protected Web Send, Native injection into a covered Web composer, synthetic hidden Send clicks, DOM answer/reasoning scraping and hidden file-input injection.

**b48-b57 are explicit diagnostic exceptions only.** Their success does not by itself approve hidden/shadow Web as production architecture or transfer production response ownership away from `ConversationRepository`.

`/backend-api/f/conversation/resume` remains a post-Send continuation/read path and does not weaken the protected-Send boundary.

## Full-Web / continuation evidence

- b43 shorter visible-Web interaction was acceptable for its tested sequence; Web `+` around 100–200ms.
- b44 full-page Native→Web→Native product form was rejected; immediate Native reconciliation could lag Web-visible output.
- b47 exact-device evidence established long-answer mobile-Web composer failure; full existing-conversation Web rendering is not a daily production dependency.
- b45 Runtime Confirmed official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` returning HTTP200 SSE and continuing the same response.
- b46/b47 Native duplicated-after-official-success Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.

## Native composer / Web Send-engine progression

- b48 proved Native input can drive sequential official protected Sends; b49 proved real compact incremental delivery; b50 added contextual `{v:string}` continuation.
- b51 Runtime confirmed the `title_generation` continuation-preserve correction fixes the fresh-new-chat missing-middle defect.
- b52 Runtime kept final answer complete but visible reasoning beginning truncated.
- b53 directly identified `assistant:reasoning_recap`, separate `assistant:thoughts`, `assistant:code`, and multiple tool message classes.
- b54 materially identified assistant tool invocation→tool-result grammar but generic structure observation saturated.
- b55's independent special channel passed (`7 / overflow0`) and deterministically captured exact `assistant:reasoning_recap` with `reasoning_status=reasoning_ended` and `reasoning_recap_type=collapse`.

Detailed Runtime records are in `docs/project/runtime-evidence/DEV-send-stream-b51-runtime.md` through `DEV-send-stream-b56-runtime.md` where applicable.

### Exact b56 Runtime — recap presentation assumption corrected

Exact b56 matched Release / build 56 / Candidate b56 / source `cec921030fd1` on iPhone/iOS17.0. One protected Send returned HTTP200 SSE and terminal true.

Metrics: `frameCount=75`, Native 26 deltas / 504 chars, exact-root 4, nested 8, contextual value strings 14 / 299 chars, inactive strings 0, generic structures 32 / overflow16, special structures 8 / overflow0, recap chars 7.

User-visible evidence:

- real visible reasoning beginning still truncated;
- `思考摘要` appeared and expanded/collapsed correctly;
- the recap was only the short status/description `思考了 40s` in this reproduction, not the real visible reasoning body;
- the real visible reasoning text remained concatenated with the final answer in the ordinary body.

Accepted correction:

- the exact recap **string is not the reasoning body** in this sample;
- the exact recap event remains a trustworthy explicit **reasoning-phase end marker** because it carries `reasoning_status=reasoning_ended`;
- `assistant:thoughts` remains separate and non-presentational;
- event ordering shows an ordinary `assistant:text:in_progress` message before the first accepted `/message/content/parts/0` append, giving a concrete hypothesis for the leading truncation, but b56 did not prove that message's content field shape. Do not guess the missing field.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b56-runtime.md`.

### Exact b57 Candidate — phase split + missing-prefix structure gate

Identity:

- Candidate `DEV-send-stream-0.1.0-b57`, version/build `0.1.0 (57)`.
- Exact product/config source `7074b1f85a0f239a5fd615f52196e1e28145523c`.
- Product tree `c402ce522e244cf63aa44b80a6d165b84342104c`.
- Push `33302357908 / 99232731468` — success.
- PR `33302359351 / 99232735067` — success.
- Artifact `9729360247`; ZIP `sha256:ae5a5532e2c30624907e9a2d61966090df4b8cc9ffa57f1b5725db8b61a8d275`.
- IPA SHA `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`.
- Package: Release / `0.1.0 (57)` / Candidate b57 / source `7074b1f85a0f` / iOS14 / `[1,2]` / arm64.

b57 preserves all prior accepted protected-Send and text acceptance rules. It changes presentation/diagnostics only at the newly proven boundary:

- accepted text before exact reasoning-end marker -> Native `思考过程`;
- accepted text after marker -> final answer;
- marker itself is phase state, not reasoning body content;
- reasoning section is expanded while active and collapses on exact reasoning end;
- if no reasoning-end marker exists by terminal, the provisional pre-marker text is promoted back into the ordinary answer so non-reasoning turns are not permanently misclassified;
- a separate bounded 12-entry ordinary `assistant:text` structure channel records only direct key names, string lengths, array shapes/string-char counts, safe booleans/enums and before/after marker phase;
- no unproven initial text field is extracted yet;
- no raw `assistant:thoughts`, raw tool args/results, connector payloads, hidden/internal reasoning/system data, auth/proof/header values are shown or persisted.

b57 Code/CI/Artifact/package are verified and permanently reserved. Runtime/manual remains Pending.

## Reasoning / tool presentation boundary

- Only explicitly user-visible service reasoning/status/tool information may enter Native presentation.
- `assistant:thoughts`, hidden chain-of-thought/internal reasoning, system/internal tool nodes and raw tool payloads remain prohibited.
- The b55/b56 evidence authorizes exact `reasoning_ended` as a phase marker, **not** `reasoning_recap` text as the reasoning body.
- b57 re-presents only the same previously accepted visible assistant text stream across that explicit marker.
- Tool invocation/result pairing is structurally evidenced from b54/b55, but exact user-visible tool-node presentation remains unresolved and no tool UI is added in b57.

## Current Runtime gate

Human gate is exact b57 on iPhone/iOS17:

1. clear diagnostics and open b57 diagnostic surface;
2. send one reasoning/tool-active request;
3. verify visible reasoning is separated into `思考过程` and final answer begins after reasoning collapse;
4. report whether the beginning of `思考过程` is still truncated;
5. expand/collapse the completed reasoning region once;
6. confirm raw thoughts/tool payloads are absent;
7. wait for terminal and export diagnostics.

Primary missing-prefix evidence is the first `assistant:text` `streamStructure` entry before reasoning end, especially `contentKeys`, `contentStringFields`, `contentArrayFields`, plus `assistantTextMessageCount` / before / after counts and phase-structure count/overflow.

Do not allocate b58 or guess an initial text container until exact b57 Runtime supplies that evidence.

## Background / authority boundary

Background resilience remains a hard requirement but production implementation stays response-owner dependent. b48-b57 remain Web-owned diagnostic response experiments, not accepted production ownership.

- `ConversationRepository` remains sole native conversation/list/read/recovery/future accepted response authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate.
- no second Send may be created merely to obtain a stream.
- Native first/exclusive resume, existing-conversation pre-React history virtualization, production Native incremental-response ownership/follow-tail/background lifecycle remain Unknown / Unverified.
- Phase 9 Stable/Frozen Send: No.
- PR #29 remains evidence-only and must not be merged as accepted production Send UX before the architecture/ownership gate is separately resolved.
