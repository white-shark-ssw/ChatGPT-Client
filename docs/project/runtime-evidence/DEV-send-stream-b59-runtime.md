# DEV-send-stream — exact b59 Runtime evidence

_Date: 2026-08-30_

## Identity

- Candidate: `DEV-send-stream-0.1.0-b59`
- Version/build: `0.1.0 (59)`
- Exact product/config source: `138c09a5d11121945bc45f1d866c449aa0f7611e`
- Artifact: `9730376958`
- ZIP digest: `sha256:4c13fc5941786b6db1797d72b8938f763cdaec2b76b8d15998fd4d6f235763ef`
- IPA SHA: `5758cf40b287c7d9c5cef2f13163d5c8239834ee617468692c56b4bdb0349252`
- User export: `ChatGPTClient-Diagnostics-20260830-103539.json`
- Export identity: Release / build59 / Candidate b59 / source `138c09a5d111` / iPhone / iOS17.0

## Transport / terminal

- official protected Send returned HTTP200 `text/event-stream`
- `frameCount=83`
- terminal true
- `reasoningEndMarkerCount=1`
- `reasoningFallbackPromoted=false`

## Native text

- total: `30 deltas / 564 chars`
- reasoning: `12 deltas / 207 chars`
- final answer: `18 deltas / 357 chars`
- assistant text messages before/after reasoning end: `2 / 1`
- exact-root text patches: 4
- nested text patches: 6
- contextual values: `18 / 357 chars`
- inactive values: 0
- continuation resets: 4

Direct user result: reasoning, tool activity and final answer all appeared complete. The b58 leading-prefix defect did not reproduce.

## Thinking preamble result

- `reasoningPreambleCount=2`
- `reasoningPreambleCharacters=13`
- event 14: before reasoning end, assistant text in-progress, recipient `all`, exact `is_thinking_preamble_message=true`, one string part of 10 characters
- event 31: a second before-end assistant text in-progress with the same service marker, one string part of 3 characters

This proves b59 is not merely fixing the first prefix. The service can emit a later thinking preamble after tool activity while the same reasoning phase remains active.

Classification: **b59 thinking-preamble completeness Runtime passed for the tested turn.**

## Remaining reasoning presentation defect

The user compared Native with official mobile Web and reported that Native does not preserve the visible reasoning paragraph/segment breaks correctly. Current b59 appends every accepted reasoning string into one `UITextView` and the thinking-preamble bridge does not carry an explicit segment-boundary presentation flag, so separate reasoning messages can concatenate visually.

The strongest evidenced minimal correction is presentation-only: a later service-marked thinking preamble starts a new visible reasoning segment. If reasoning text already exists, Native may insert a presentation paragraph separator before that new segment; the first preamble must not receive a leading separator. The separator is UI formatting and must not alter service character metrics.

## Tool activity result

- `toolInvocationCount=12`
- `toolInvocationWithTitleCount=2`
- `toolResultCount=13`
- `toolResultWithTitleCount=12`
- `nativeToolPresentationCount=12`

Direct user result: compact Native tool activity remained visible and useful, but unlike official Web it has no expandable request/result details.

Important pairing boundary: the tested turn has 12 accepted completed invocations but 13 completed tool results. Therefore adjacency/count order alone is not a safe production pairing rule. Before exposing tool request/result bodies, the next diagnostic must establish an exact invocation→result relation (for example by comparing service parent/reference identity in memory and exporting only booleans/counts, never raw IDs) and identify which service fields correspond to the official user-visible request/reply card. Do not expose `connector_tool_payload` or arbitrary tool bodies by guess.

## Reasoning-active state evidence

The same turn contains a completed assistant `thoughts` structural message with `metadata.reasoning_status=is_reasoning` after tool activity, followed by the second service-marked thinking preamble. The `assistant:thoughts` body remains non-presentational, but the explicit safe status token is evidence that the service can signal a return to reasoning after tools.

The initial post-Send waiting UI may be represented from the response lifecycle (`Send accepted / active receiving / no visible reasoning yet`) without a timer. Exact equivalence to an official service-side initial `正在思考` signal remains to be diagnosed; do not invent a hidden reasoning body or time-based transition.

## Official-equivalent target confirmed by user

The user explicitly wants the eventual Native interaction to follow the official sequence as closely as evidence permits:

`发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开查看用户可见的调用详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考过程 -> 只突出完整最终回答`

This remains part of `DEV-send-stream`. It is a response-lifecycle/reasoning/tool presentation requirement, not a new independent Work.

## Architecture boundary

This Runtime result does not promote the b48-b59 diagnostic Web Send-engine into accepted production response ownership. `ConversationRepository`, `AuthSessionStore`, default persistent `WKWebsiteDataStore`, TD-024/TD-025/TD-028 and the no-resend/no-duplicate-owner rules remain unchanged.
