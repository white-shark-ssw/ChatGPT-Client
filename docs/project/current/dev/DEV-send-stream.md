# DEV-send-stream

## Status

**Active — exact b54 Runtime materially identifies the tool invocation/result grammar but leaves the reasoning-recap display-container gate unresolved because the shared generic 32-signature observer saturated. Exact b55 is now Code/CI/Artifact/package verified and changes only structure-diagnostic capacity: special reasoning/tool messages have a separate bounded dedupe channel while every b54 Send/filter/output rule is preserved. The next gate is one focused exact-device b55 reasoning/tool reproduction. No reasoning/tool UI is authorized yet. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; metadata synchronization to b55 gate is pending in this docs batch.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; unchanged at b54 Runtime guard.
- **Stable native predecessor**: b38.
- **Stable/Frozen Send**: No.

## Exact b53 Runtime

- Candidate `DEV-send-stream-0.1.0-b53`, `0.1.0 (53)`.
- Exact source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`; Artifact `9726996570`; IPA SHA `d5eee722ea01dc2c1b419a803574aec8ad2199299a3d0bbb51de4bae574f25dc`.
- User observation: visible reasoning beginning still truncated; final answer complete; no Native tool-call presentation.
- Runtime structurally identified `assistant:reasoning_recap`, `assistant:thoughts`, `assistant:code`, and `tool:*`.
- Durable record: `docs/project/runtime-evidence/DEV-send-stream-b53-runtime.md`.

## Exact b54 identity / Runtime

- Candidate `DEV-send-stream-0.1.0-b54`, `0.1.0 (54)`.
- Exact source `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`.
- Push `33296672444 / 99217423647` success; PR `33296674388 / 99217428590` success.
- Artifact `9727636043`; ZIP `sha256:28d07c99634a1b4f917561e95cf04a4e95666106985cb03bca09798b0dc7065c`.
- IPA SHA `d4b85cffe4db499252d0bc9a2c7c8ea582acf2b88f3d28eeb60e366ee471153b`.
- Package Release / source marker `6a6903c7ad56` / iOS14 / `[1,2]` / arm64.
- b54 permanently reserved.

Exact b54 Runtime diagnostics matched build 54 / Candidate b54 / source `6a6903c7ad56` / Release / iPhone iOS17.0. One Send reached HTTP200 SSE and terminal true.

Metrics:

- `frameCount=73`;
- `nativeDeltaCount=22`, `nativeCharacters=412`;
- `explicitTextPatchCount=7`, exact-root 4, nested 3, root-nonexact 0;
- contextual value strings 15 / 312 chars; inactive value strings 0;
- continuation resets 4; first inactive context none;
- generic structure signatures **32**, overflow **13**;
- terminal true.

Tool evidence accepted:

- assistant `code` messages target `api_tool.list_resources` / `api_tool.call_tool` recipients;
- completed assistant code carries `is_complete:true`, `connector_tool_payload`, `tool_icons` metadata;
- tool results have author names such as `api_tool` / `api_tool.call_tool`, `recipient=all`, content types text/code/multimodal_text and evidence-backed result containers (`parts` or `text`);
- tool metadata includes `invoked_plugin` / `invoked_resource` where present.

This proves explicit invocation/result nodes and a structural pairing boundary, not that raw arguments/results or every internal node are user-visible.

Reasoning evidence accepted:

- `assistant:thoughts / finished_successfully`, recipient all;
- content keys `content_type,source_analysis_msg_id,thoughts`;
- `thoughts` array item keys `chunks,content,finished,summary`;
- metadata `can_save:false`, `reasoning_status:is_reasoning`, `tool_summary_type:github`, and structural keys including `inline_cot_expandable_content` / `tool_icons`.

Raw thoughts/chunks/internal reasoning remain non-presentational. b54 did not prove the exact authorized display field.

`assistant:reasoning_recap` was not emitted into b54 diagnostics, but the generic observer was saturated at 32 with 13 overflowed unique structures. Therefore b54 cannot distinguish recap absence from observer suppression. Durable record: `docs/project/runtime-evidence/DEV-send-stream-b54-runtime.md`.

## Exact b55 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b55`
- Version/build: `0.1.0 (55)`
- Exact product/config source: `aae856069b461e12dc11ee7d2d450a40ca621d21`
- Push Run / Job: `33299965737 / 99226125826` — success
- PR Run / Job: `33299967033 / 99226129092` — success
- Artifact: `9728606514`
- ZIP digest: `sha256:fda8dfb16e3d734b9e0f0d55c4e49c0f6cd656e4ec228b13dab3cae108c0a7e3`
- IPA: `ChatGPTClient-0.1.0-b55-dev-send-stream.ipa`
- IPA SHA-256: `f5106949814b44c6c97e2f519ff181498f6a75ff7b9bf9edf0dc0bb0bd299ad1`
- Independent package inspection: `0.1.0 (55)`, Candidate b55, source marker `aae856069b46`, Release, minimum iOS14.0, UIDeviceFamily `[1,2]`, Mach-O arm64.
- Runtime/manual: Pending.
- b55 is permanently reserved after Artifact emission. Any later product-code correction requires b56+ and exact b55 Runtime evidence.

### Exact b55 change

b55 preserves every b54 protected-Send, SSE filtering, assistant text extraction and Native output rule. It changes diagnostics only:

1. generic `structureSeen` remains capped at 32 exactly as b54;
2. `assistant:reasoning_recap`, `assistant:thoughts`, `assistant:code`, and all `tool:*` also use an independent `specialStructureSeen` set capped at 24;
3. a new special structure is emitted even when the generic set is already full;
4. special dedupe uses role/content type/status/recipient/author plus structural content/metadata keys and safe boolean/enum metadata, not raw text or IDs;
5. terminal metrics add `specialStructureSignatureCount` and `specialStructureSignatureOverflowCount`;
6. no prompt, answer, reasoning text, raw tool payload, raw tool output, raw IDs, auth/proof/header values are newly logged.

No reasoning collapse/expand, tool card/sheet, haptics, retry, fallback, timer, watchdog or production-response ownership change exists in b55.

### Atomic b55 assembly

Tooling branch `tooling/b55-assembly-20260830` assembled the three exact Candidate files from the b54-runtime evidence head. Compare confirmed only:

- `.github/workflows/ios-foundation.yml` — Candidate/Artifact name b55;
- `ChatGPTClient.xcodeproj/project.pbxproj` — build 55 / Candidate b55;
- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift` — special-structure observer capacity only.

The final assembly tree `e80eb12544f9659d00895c00523b5c1a0ed58b93` was attached directly to parent `7af5e55fda38df8709b594442901efdf923000b2` as exact feature commit `aae856069b461e12dc11ee7d2d450a40ca621d21`, then the feature ref moved once. Tooling commits are not Candidate authority.

An accidental inert branch named `noop` was created from `7af5e55fda38df8709b594442901efdf923000b2` while discovering branch/ref tooling. It received no product commits and is not an Active Work/State/Candidate authority. The currently available connector exposes no branch-delete action; do not use this branch for any development or identity decision.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b55 are diagnostic exceptions only. TD-024/TD-025 remain unchanged. No diagnostic result alone promotes hidden/shadow Web to production.

Only explicitly user-visible service reasoning/status/tool information may be shown. Hidden chain-of-thought/internal tool/system data remains prohibited. Raw `assistant:thoughts` is explicitly non-presentational under the current evidence boundary.

## Evidence ladder

- b51 Code/CI/Artifact/package: Passed; Runtime title-generation correction confirmed.
- b52 Code/CI/Artifact/package: Passed; Runtime final answer complete / visible reasoning beginning incomplete.
- b53 Code/CI/Artifact/package: Passed; Runtime recap/thoughts/tool grammar materially identified.
- b54 Code/CI/Artifact/package: Passed; Runtime **partial pass** — tool call/result grammar identified; recap gate inconclusive because generic observer saturated at 32/overflow13.
- b55 Code/CI/Artifact/package: **Passed**; Runtime pending.
- Phase 9 Stable/Frozen: No.

## Batch I recovery point

Confirmed:

1. exact b54 Runtime evidence persisted in `docs/project/runtime-evidence/DEV-send-stream-b54-runtime.md`;
2. exact b55 source `aae856069b461e12dc11ee7d2d450a40ca621d21` emitted atomically;
3. both exact b55 Push/PR CI jobs succeeded;
4. Artifact `9728606514` is attached to exact b55 source;
5. ZIP digest, IPA SHA and package identity independently verified;
6. b55 is permanently reserved.

Pending docs-only work in this batch:

- synchronize PR #29 and durable project/index wording to b54 Runtime + b55 Artifact truth.

Recovery rule: later docs-only commits do not redefine exact b55 product/config source `aae856069b46…`. Never rebuild b54 or b55. Do not allocate b56 before exact b55 Runtime supplies a concrete smallest next change.

## Next exact action

User installs exact b55 IPA, clears diagnostics, opens the b55 diagnostic surface, and sends one prompt that naturally produces visible reasoning plus tool activity. Wait for terminal and export diagnostics. Visual behavior is intentionally expected to remain similar to b54 because b55 is evidence-only.

Primary decision signals:

- `specialStructureSignatureCount` / overflow must prove the special channel itself did not saturate;
- if `assistant:reasoning_recap` appears, inspect only its text-free content-container and presentation metadata to identify the authorized visible-reasoning surface;
- tool invocation/result structures should remain captured even after generic structure count reaches 32.

Only after this evidence proves an explicit display boundary may a following Candidate implement Native reasoning-summary separation/collapse and evidence-backed tool-call presentation. Raw thoughts/internal tool payloads remain excluded.
