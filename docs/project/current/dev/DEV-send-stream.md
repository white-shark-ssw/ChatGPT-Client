# DEV-send-stream

## Status

**Active — exact b59 Runtime passes the tested text-completeness gate: the service-marked thinking preambles, reasoning stream, compact tool activity and final answer were all visible and complete on the primary iPhone/iOS17 run. b59 also exposes the next presentation gaps: separate reasoning messages are visually concatenated because Native does not preserve segment breaks; official-Web expandable tool request/result details are not yet represented; and the desired official lifecycle includes an explicit `正在思考` state before/among reasoning/tool phases. The same b59 traffic now proves two thinking preambles in one reasoning phase and an explicit `reasoning_status=is_reasoning` signal after tool activity, so the official-like state skeleton is evidence-backed. Tool detail bodies remain evidence-gated because the run has 12 accepted completed invocations but 13 tool results, so adjacency pairing is unsafe. TD-024/TD-025/TD-028 and production response ownership remain unchanged; PR #29 remains evidence-only.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Current target main: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Exact b59 product/config source: `138c09a5d11121945bc45f1d866c449aa0f7611e`
- Guarded branch head before this checkpoint write: `bfcd9b874ef3214cd74612c96089d6556a4b0f33` (b59 source plus docs-only Runtime evidence)
- Other Active development checkpoints: none
- Stable native predecessor: b38
- Stable/Frozen Send: No

## Exact b59 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b59`
- Version/build: `0.1.0 (59)`
- Exact product/config source: `138c09a5d11121945bc45f1d866c449aa0f7611e`
- Product tree: `c28eb92616e494a15aa2e370e2fd5150986b2452`
- Push Run / Job: `33305680998 / 99241706079` — success
- PR Run / Job: `33305683021 / 99241711695` — success
- Artifact: `9730376958`
- ZIP digest: `sha256:4c13fc5941786b6db1797d72b8938f763cdaec2b76b8d15998fd4d6f235763ef`
- IPA SHA: `5758cf40b287c7d9c5cef2f13163d5c8239834ee617468692c56b4bdb0349252`
- Package: Release / `0.1.0 (59)` / Candidate b59 / source `138c09a5d111` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64
- b59 is permanently reserved.

## Exact b59 Runtime

User export `ChatGPTClient-Diagnostics-20260830-103539.json` exactly matches Release / build59 / Candidate b59 / source `138c09a5d111` / iPhone / iOS17.0.

Transport / text:

- official protected Send HTTP200 SSE, terminal true
- `frameCount=83`
- Native total `30 deltas / 564 chars`
- reasoning `12 / 207 chars`
- final answer `18 / 357 chars`
- `reasoningEndMarkerCount=1`
- fallback false
- assistant text before/after end `2 / 1`

Thinking preambles:

- `reasoningPreambleCount=2`
- `reasoningPreambleCharacters=13`
- first preamble: one 10-character string part, `is_thinking_preamble_message=true`
- second preamble: one 3-character string part with the same exact service marker after earlier tool activity
- direct user result: no leading truncation; reasoning appears complete.

Tool activity:

- invocations 12; invocation titles 2
- results 13; result titles 12
- Native compact presentations 12
- direct user result: compact activity is complete enough for the tested turn, but official-Web expandable request/result detail is absent.

Presentation defect / new requirement:

- direct user comparison shows Native reasoning does not preserve official paragraph/segment breaks;
- user explicitly wants eventual lifecycle: `发送 -> 正在思考 -> 思考流式输出 -> 工具调用/可展开用户可见详情 -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出最终回答`;
- this remains part of `DEV-send-stream`, not a separate Work;
- b59 structurally contains `reasoning_status=is_reasoning` after tool activity followed by the second thinking preamble, proving a return-to-reasoning state signal without exposing `assistant:thoughts` body.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b59-runtime.md`.

Classification: **b59 Runtime passes the tested preamble/reasoning/final completeness correction; overall Phase 9 remains Active because official-equivalent ordered presentation/tool-detail semantics and production response ownership are not yet accepted.**

## b60 evidence-backed scope

Build/Candidate 60 may be allocated only after confirming it is unused. Intended scope is deliberately bounded:

1. Preserve b59 protected Send, accepted patch grammar, preamble inclusion, `reasoning_ended` final split, terminal fallback and compact tool-activity behavior.
2. Preserve reasoning service-character metrics while fixing presentation segmentation: a later exact service-marked thinking preamble starts a new visible reasoning paragraph; insert a Native-only paragraph separator only when prior reasoning text already exists. No leading separator on the first preamble.
3. Add a bounded explicit reasoning-active observer for safe service status `metadata.reasoning_status=is_reasoning`; never present `assistant:thoughts` body.
4. Initial post-Send `正在思考` may be a response-lifecycle presentation state (`protected Send accepted / response active / no visible reasoning yet`), never timer-based or hidden-content-derived. Diagnostics must distinguish lifecycle-derived initial waiting from explicit later service reasoning-active signals.
5. Do **not** expose tool request/result bodies yet. Add only privacy-safe pairing diagnostics that compare service identities in memory and export booleans/counts, so the 12-invocation/13-result case can establish an exact association rule without logging raw IDs.
6. Add only bounded structural evidence needed to identify which invocation/result content fields correspond to the official user-visible expandable card. No raw tool text, connector payload, auth/challenge value, `assistant:thoughts`, prompt, reasoning body or final-answer body in diagnostics.
7. Do not restructure production `ConversationRepository` or promote diagnostic Web transport ownership in b60.

## Official-equivalent presentation target

The evidence-backed target is one ordered response presentation timeline, eventually owned by the accepted response lifecycle rather than separate ad-hoc UI stores:

- response accepted / waiting -> `正在思考` presentation;
- visible reasoning segment streams;
- exact user-visible tool invocation appears at its real chronological position and can later expose only verified user-visible request/result details;
- explicit reasoning-active signal can return presentation to `正在思考` after a tool;
- later reasoning segments continue in order;
- exact `reasoning_ended` fires once, collapses the complete reasoning/tool timeline and hands subsequent accepted text to final answer;
- final answer remains the primary visible output while completed reasoning can be manually expanded.

The interaction/state ordering can be made official-like from current evidence. Exact pixel identity and every tool-card subtype remain Runtime/evidence dependent and must not be promised before their fields are verified.

## Batch N recovery point

Confirmed complete:

1. startup governance re-read (`AGENTS.md` then `START_HERE.md`) and Development route resolved to existing `DEV-send-stream`;
2. resume guard: feature exact b59 head `138c09a5...` before docs, PR #29 open/mergeable/unmerged, target main unchanged `1ac202c...`, only one Active checkpoint;
3. exact b59 Runtime diagnostics + four user screenshots classified;
4. b59 Runtime evidence file created at commit `bfcd9b874ef3214cd74612c96089d6556a4b0f33`;
5. user requirement establishes official-like ordered reasoning/tool lifecycle as the `DEV-send-stream` target.

Pending deterministic actions:

1. synchronize `BUILD_TEST_INDEX`, `PROJECT_STATE`, `MODULE_STATUS`, `PROJECT_PROFILE`, `DEVELOPMENT_PLAN`, `PROJECT_SPECIFIC_RULES` and PR #29 through b59 Runtime;
2. confirm b60 identity/artifact name is unused;
3. if unused, allocate b60 and implement only the bounded scope above;
4. verify product diff, Push + PR CI, Artifact, ZIP/IPA/package identity;
5. hand exact b60 to the user for one tool-active Runtime turn focused on segment breaks, thinking-state transitions and new safe association metrics;
6. only after b60 pairing/field evidence may a later Candidate expose expandable tool request/result details.

Do not modify Stable b38 modules, auth ownership, attachments, resume transport or production `ConversationRepository` in Batch N. b61 must not be allocated by guess.

## Next exact action

Synchronize durable docs through exact b59 Runtime, confirm build60 is unused, then assemble the bounded b60 presentation/diagnostic candidate above.
