# DEV-send-stream

## Status

**Active — exact b59 Runtime passes the tested completeness gate. Exact b60 is now Code / CI / Artifact / package Passed and awaits one iPhone/iOS17 Runtime turn. b60 preserves b59 Send/text/tool behavior, adds event-driven `正在思考`, preserves later thinking-preamble paragraph boundaries, and records privacy-safe tool invocation→result association counts without displaying raw tool request/result bodies. Tool phases are optional and appear only when real events occur. TD-024/TD-025/TD-028 and production response ownership remain unchanged; PR #29 remains evidence-only / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Current target main last verified: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Other Active development checkpoints: none
- Stable native predecessor: b38
- Stable/Frozen Send: No

## Exact b59 Runtime conclusion

Exact b59 product/config source `138c09a5d11121945bc45f1d866c449aa0f7611e`; Artifact `9730376958`; IPA SHA `5758cf40b287c7d9c5cef2f13163d5c8239834ee617468692c56b4bdb0349252`.

User export `ChatGPTClient-Diagnostics-20260830-103539.json` matched Release / build59 / Candidate b59 / iPhone iOS17.0. One official protected Send returned HTTP200 SSE and terminal true. Native delivered reasoning `12 / 207 chars`, final `18 / 357 chars`; two exact service-marked thinking preambles totaling 13 chars were included; 12 completed tool invocations produced 12 compact Native activity entries; direct user comparison confirmed no leading truncation and complete final answer. Remaining gaps: Native did not preserve the official paragraph break before the later preamble, `正在思考` state was not yet presented, and official expandable tool request/result details remained absent. Tool results were `13`, so adjacency pairing was explicitly rejected.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b59-runtime.md`.

Classification: **b59 Runtime passes tested content completeness; Phase 9 remains Active.**

## Exact b60 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b60`
- Version/build: `0.1.0 (60)`
- Exact product/config source: `8ca445f3c17233ac36832f46417a8e53a138499e`
- Product tree: `1f0b612cc233d4541336cc43177d8384ef5072bd`
- Product parent / last docs head: `792db8886b82fba2b5338c809105e565514eb215`
- Push Run / Job: `33309296932 / 99251320370` — success
- PR Run / Job: `33309298759 / 99251325144` — success
- Artifact: `9731477362`
- Artifact name: `ChatGPTClient-DEV-send-stream-0.1.0-b60`
- ZIP digest / independently verified SHA: `sha256:167d32071f33639f1afe006aefd6b73900805f611f653ca24d908dfe1fdef17a`
- IPA SHA: `7cae323231b6b9d1aa837b03506450daa99f457fd8b4025deedb368dc008cd42`
- Package: Release / `0.1.0 (60)` / Candidate b60 / source `8ca445f3c172` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64
- b60 is permanently reserved after Artifact emission.

Evidence ladder: **Code written / CI passed / Artifact produced / package identity independently verified; Runtime/manual pending; Stable/Frozen No.**

## b60 bounded behavior

1. Protected Web Send, b59 accepted text patch grammar, exact thinking-preamble content, `reasoning_ended` split/collapse, terminal fallback, final-answer path and compact tool activity remain unchanged.
2. The second and later exact `is_thinking_preamble_message=true` preamble starts a Native-only paragraph break when prior visible reasoning exists; separator characters are presentation-only and do not alter service-character metrics.
3. After an accepted HTTP200 SSE Send and before visible reasoning, Native can show `正在思考…` from response lifecycle state. Exact safe service `reasoning_status=is_reasoning` can re-enter that state after tool activity. No timer and no `assistant:thoughts` body exposure.
4. Tool invocation is optional/event-driven. Zero real tool events means no tool phase is fabricated.
5. Raw tool request/result bodies are still not shown in b60. In-memory invocation IDs/recipients and tool-result `parent_id` are compared only to emit aggregate counts: parent present/matched/unmatched/missing and author-recipient match. Raw IDs never leave memory or diagnostics.
6. Production `ConversationRepository`, auth ownership, resume transport, attachments and Stable b38 modules are untouched.

## Official-like event-driven target

The target is not a fixed script. Actual response events may be: accepted/waiting -> visible reasoning -> zero or more real tool invocation/result phases interleaved with reasoning-active states -> one exact `reasoning_ended` -> final answer. A no-tool response must proceed directly according to the events received. Completed reasoning/tool history should eventually collapse at reasoning end while final answer remains primary; expandable per-tool details are still evidence-gated.

Model selection / thinking-effort product controls are not part of this Phase 9 closure; they remain later product work. Phase 9 may observe safe service model/effort enums where needed but must not hard-code current test values.

## Batch N recovery point

Confirmed complete:

1. governance/resume guard and b59 Runtime classification;
2. b59 Runtime evidence + durable docs synchronized;
3. PR #29 synchronized to b60 gate;
4. exact b60 assembled atomically from docs parent `792db888...`; feature ref moved once to product commit `8ca445f3...`;
5. exact 3-file product diff verified;
6. Push + PR CI succeeded;
7. Push Artifact `9731477362` downloaded and independently verified, including ZIP digest, sidecar IPA SHA, built Info.plist and arm64 package identity.

Pending:

1. synchronize remaining durable status/index docs through b60 Artifact;
2. hand exact b60 IPA to user;
3. one focused exact-device Runtime turn. Inspect paragraph segmentation, initial and post-tool `正在思考`, optional tool behavior, complete final answer, and aggregate tool association metrics;
4. only if b60 proves a reliable association rule may a later Candidate display verified expandable tool request/result details.

## Next exact action

Install exact b60 and run one response that naturally reasons; a tool-active GitHub request is useful for association evidence, but tools must not be forced. Wait for terminal, observe lifecycle/paragraph behavior, and export diagnostics. Do not allocate b61 until exact b60 Runtime provides concrete evidence.
