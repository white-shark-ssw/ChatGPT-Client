# DEV-send-stream

## Status

**Active — exact b53 Runtime identifies distinct `assistant:reasoning_recap`, non-presentational `assistant:thoughts`, and real `assistant:code` / `tool:*` structures. Final answer is complete; visible reasoning beginning remains truncated; Native shows no tool-call presentation. Exact b54 product/config source is now written atomically as a behavior-neutral visibility/content-shape refinement. CI/Artifact/Runtime remain pending. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: Send, Stream, reasoning, 思考, 工具调用, tool call
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged at Batch H Resume Guard.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; unchanged.
- **Other Active development checkpoints**: none.
- **Stable native predecessor**: b38.
- **Stable/Frozen Send**: No.

## Exact b52

`DEV-send-stream-0.1.0-b52`, `0.1.0 (52)`, exact product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`, Artifact `9721532867`, IPA SHA `a3de5c6eb4f7b790764fcd0adc4c98108fb550e7cedb3d6b02b931d266946b23`.

Runtime conclusion: final answer complete; beginning of visible reasoning/thinking slightly truncated. `rootNonExactTextPatchCount=0`, `inactiveValueStringCount=0`; the prior root-nonexact→inactive-value hypothesis is rejected for that reproduction. Durable record: `runtime-evidence/DEV-send-stream-b52-runtime.md`.

## Exact b53 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b53`
- Version/build: `0.1.0 (53)`
- Exact product/config source: `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`
- Push Run / Job: `33294541342 / 99211838094` — success
- PR Run / Job: `33294542985 / 99211842336` — success
- Artifact: `9726996570`
- ZIP: `sha256:8831bbae1c5cad9c9cd7f0ad9fbcf4846d709b27ae950b0391d436e20749b38c`
- IPA SHA: `d5eee722ea01dc2c1b419a803574aec8ad2199299a3d0bbb51de4bae574f25dc`
- Package: Release / iOS14 / UIDeviceFamily `[1,2]` / arm64
- b53 is permanently reserved.

## Exact b53 Runtime — 2026-08-30

Durable record: `docs/project/runtime-evidence/DEV-send-stream-b53-runtime.md`.

User observation:

- visible reasoning/thinking beginning: **still truncated**;
- final answer: **complete**;
- Native tool-call presentation: **not visible**.

Exact diagnostics metadata matched b53 (`buildNumber=53`, Candidate b53, source marker `3204b183ca4f`, iPhone/iOS17.0). One Send reached HTTP200 SSE and terminal true.

Aggregate metrics:

- `frameCount=71`;
- `nativeDeltaCount=21`, `nativeCharacters=476`;
- `exactTopLevelTextPatchCount=4`;
- `rootNonExactTextPatchCount=0`;
- `nestedTextPatchCount=6`;
- `contextualValueStringCount=11`, `contextualValueStringCharacters=196`;
- `inactiveValueStringCount=0`;
- `continuationResetWhileActiveCount=4`;
- `firstInactiveValueContext=none`;
- `structureSignatureCount=32`, overflow `1`;
- terminal true, Web assistant text 0.

New exact structural evidence:

1. `assistant / text / in_progress` followed by `/message/content/parts/0` append/value continuation exists.
2. `assistant / code / in_progress` exists; a batch then appends `/message/content/text`.
3. Service emitted `tool / text`, `tool / code`, and `tool / multimodal_text` finished messages.
4. Service emitted `assistant / thoughts / finished_successfully`.
5. Service emitted distinct `assistant / reasoning_recap / finished_successfully`.
6. Final-answer phase includes citation/content-reference-rich nested `/message/content/parts/0` patches before `message_stream_complete`.

Accepted interpretation:

- `reasoning_recap` is the first direct reasoning-named assistant content type evidenced on exact Runtime and is a candidate for explicitly user-visible reasoning presentation.
- `thoughts` must **not** be exposed. Its presence does not authorize hidden chain-of-thought UI.
- Tool execution definitely occurred structurally, so the user's missing tool UI is a current presentation gap. However role/content type alone does not prove which tool/code nodes are officially user-visible versus internal-only.
- b53 does not expose the concrete content container of `reasoning_recap` or the visibility/presentation metadata on code/tool nodes. Direct parser/UI implementation from content type alone would still be a guess.

## Batch H — b53 Runtime -> b54 visibility/content-shape refinement

### Resume Guard

Verified before product edits:

- feature branch existed and head was `52fc1e2a6c0297ee285f94230018356c62256de7` before b53 Runtime docs;
- PR #29 open / mergeable / head matched feature branch;
- `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- only this Work is Active;
- b39-b53 are already reserved;
- repository search found no `DEV-send-stream-0.1.0-b54` identity.

### Exact b54 product/config source

- Candidate: `DEV-send-stream-0.1.0-b54`
- Version/build: `0.1.0 (54)`
- Exact product/config source: `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`
- Product/config commit changes only:
  - `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`;
  - `ChatGPTClient.xcodeproj/project.pbxproj`;
  - `.github/workflows/ios-foundation.yml`.
- Atomic assembly: a tooling-only `[skip ci]` branch assembled the three files from checkpoint head; its final tree was attached to the feature checkpoint parent in one commit and the feature ref moved once. Tooling assembly commits are not Candidate authority.
- Push/PR CI: pending.
- Artifact/package: pending.
- Runtime: pending.

### b54 implementation

b54 preserves every b53 filtering/output behavior. It adds special-message structure diagnostics only for:

- `assistant:reasoning_recap`;
- `assistant:thoughts` (structure only, never presentation/text);
- `assistant:code`;
- `tool:*`.

Added text-free bounded fields:

- message/author/content/metadata key names;
- safe `recipient` and author-name protocol tokens when present;
- direct content string-field names + character counts, never values;
- content array field names/counts/item primitive types, aggregate direct string-character counts and first object-item key names;
- direct metadata boolean fields with values;
- bounded metadata enum-like fields only for visibility/presentation/status/type/kind/category/mode/phase/result-style keys whose values pass the existing protocol-token sanitizer.

No Native response text/filtering behavior changed. b54 does not show `thoughts`, does not extract/show `reasoning_recap` text, does not present tool nodes, and adds no reasoning haptics/UI.

Purpose:

1. identify the actual content container for `reasoning_recap` without logging recap text;
2. identify evidence-backed visibility/presentation markers on tool/code messages;
3. determine whether the next Candidate can safely implement reasoning extraction/collapse and user-visible tool-call presentation.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b54 are diagnostic exceptions only. TD-024/TD-025 remain unchanged. No diagnostic result alone promotes hidden/shadow Web to production.

Reasoning and final answer remain separate presentation domains. Only explicitly user-visible service reasoning/status/tool information may be shown. Hidden chain-of-thought/internal tool/system nodes remain prohibited.

## Evidence ladder

- b51 Code/CI/Artifact/package: Passed; Runtime confirmed fresh-new-chat title-generation correction.
- b52 Code/CI/Artifact/package: Passed; Runtime final answer complete / reasoning beginning incomplete.
- b53 Code/CI/Artifact/package: Passed; Runtime **reasoning still incomplete, final complete; `reasoning_recap` + tool grammar materially identified**.
- b54 Code/config: written atomically at `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`; CI/Artifact/Runtime pending.
- Phase 9 Stable/Frozen: No.

## Batch H recovery point

Confirmed writes:

1. exact b53 Runtime evidence persisted at commit `d023d9b7945c87ccf8a7fb9468978425307966d5`;
2. Batch H checkpoint created at `4ba1726763de95472acfe6846ad13603ad15abdd`;
3. atomic b54 product/config source `6a6903c7ad56e534303bfca6a486b83b2d6fe35f` emitted on the feature branch.

Pending:

4. verify exact b54 Push/PR CI and Artifact/package identity;
5. synchronize PR and durable project docs;
6. hand exact b54 IPA to user for one focused reasoning/tool reproduction and diagnostics export.

Recovery rule: if interrupted, re-read this checkpoint and actual GitHub branch/PR state. Perform only missing deterministic writes. Never alter/rebuild b53. Once any b54 Artifact is emitted, b54 becomes permanently reserved. Later docs-only commits do not redefine exact b54 product/config source `6a6903c7...`.

## Next exact action

Verify exact b54 CI for source `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`. If CI/Artifact/package identity are valid, synchronize PR/durable docs and hand exact b54 IPA to the user. Runtime gate: repeat one prompt that produces reasoning/tool activity and export diagnostics after terminal. The next presentation/parser decision must come from b54 structure evidence, not guesses.
