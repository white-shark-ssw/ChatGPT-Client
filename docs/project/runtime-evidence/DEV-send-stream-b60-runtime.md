# DEV-send-stream b60 Runtime Evidence

## Identity

Exact user export: `ChatGPTClient-Diagnostics-20260830-122917.json`.

- Candidate: `DEV-send-stream-0.1.0-b60`
- Version/build: `0.1.0 (60)`
- Build configuration: Release
- Source marker: `8ca445f3c172`
- Exact product/config source: `8ca445f3c17233ac36832f46417a8e53a138499e`
- Device class: iPhone
- iOS: 17.0
- Deployment target: 14.0
- Artifact: `9731477362`
- IPA SHA: `7cae323231b6b9d1aa837b03506450daa99f457fd8b4025deedb368dc008cd42`

The export exactly matches the emitted b60 package identity. User performed two consecutive tool-active turns in the same diagnostic session.

## Direct user observation

For both turns:

- after Send, Native showed `正在思考`;
- visible reasoning then streamed normally;
- a visible paragraph/segment break was present;
- user saw no obvious leading or middle truncation.

Direct visual observation is accepted as the presentation result for this exact device/run.

## Turn 1

Transport / text:

- HTTP 200 `text/event-stream`, filtered by the diagnostic bridge
- terminal: true
- frameCount: 88
- Native total: 31 deltas / 671 chars
- reasoning: 14 deltas / 209 chars
- final answer: 17 deltas / 462 chars
- exact `reasoning_ended`: 1
- terminal fallback: false
- inactive value-string count: 0

Thinking / segmentation:

- thinking preambles: 2 / 10 chars
- service reasoning-active signals: 2
- Native thinking presentations: 3
- service reasoning segment breaks: 1
- Native reasoning segment breaks: 1

Tool association:

- completed invocation presentations: 13
- invocation identities observed in memory: 15
- completed tool results: 15
- result parent present: 15
- result parent matched to an observed invocation ID: 15
- result parent unmatched: 0
- result parent missing: 0
- result author-name == invocation recipient: 14

This turn proves that completed-presentation count is not an identity count: two invocation identities were observed before satisfying the stricter completed/presented invocation condition. All 15 results nevertheless matched an invocation by exact `parent_id`.

## Turn 2

Transport / text:

- HTTP 200 `text/event-stream`, filtered
- terminal: true
- frameCount: 101
- Native total: 71 deltas / 1143 chars
- reasoning: 17 deltas / 221 chars
- final answer: 54 deltas / 922 chars
- exact `reasoning_ended`: 1
- terminal fallback: false
- inactive value-string count: 0

Thinking / segmentation:

- thinking preambles: 2 / 32 chars
- service reasoning-active signals: 3
- Native thinking presentations: 3
- service reasoning segment breaks: 1
- Native reasoning segment breaks: 1

Tool association:

- completed invocation presentations: 5
- invocation identities observed in memory: 5
- completed tool results: 5
- result parent present: 5
- result parent matched: 5
- result parent unmatched: 0
- result parent missing: 0
- result author-name == invocation recipient: 3

Again, exact `parent_id` pairing is complete while author/recipient-name equality is not.

## Accepted b60 conclusions

1. **Initial waiting presentation passes the tested Runtime gate.** Both turns produced lifecycle-derived `正在思考` after accepted Send.
2. **Return-to-reasoning presentation passes the tested Runtime gate.** Exact `reasoning_status=is_reasoning` signals produced later thinking states without presenting `assistant:thoughts` body.
3. **Reasoning segmentation passes the tested Runtime gate.** Later exact thinking preambles produced one Native-only paragraph break in each turn, and user confirmed visible separation.
4. **Text completeness remains Runtime positive for these two turns.** Both terminal responses had no inactive value-string loss and the user saw no obvious truncation.
5. **Invocation -> result association is now Runtime established for the tested traffic by exact result `parent_id`.** Across the two turns, 20/20 completed tool results had a parent and 20/20 matched a previously observed invocation identity; 0 unmatched and 0 missing.
6. **Do not use adjacency, raw count equality, or author-name/recipient equality as the pairing rule.** Turn 1 had 13 presented invocations but 15 invocation identities/results, and author/recipient equality was only 14/15; turn 2 equality was only 3/5.
7. **Raw tool request/result bodies are still not authorized for Native presentation.** b60 observed result content shapes including `text`, `code` and `multimodal_text`, sometimes with large bodies. Exact parent pairing proves ownership/association, not which body fields official UI intends to expose.
8. `assistant:thoughts` remains non-presentational. Safe status/structural metadata may guide diagnostics only.

## Next evidence boundary

A later Candidate may consume exact `parent_id` association for Native tool-entry lifecycle. Before displaying detailed request/result bodies, it must identify user-visible field semantics with bounded structural evidence only. Candidate diagnostics may inspect types/direct keys/counts of already observed candidate metadata such as connector/tool presentation metadata, but must not log or display raw connector payloads, tool result bodies, prompt, reasoning body, final-answer body, message IDs or hidden thoughts.

Classification: **b60 Runtime pass for tested thinking-state presentation, reasoning segmentation, text completeness and exact parent association; Phase 9 remains Active because verified expandable tool-detail semantics and production response ownership are still pending.**
