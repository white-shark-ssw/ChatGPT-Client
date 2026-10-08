# DEV-send-stream b62 Runtime Evidence

## Identity

- Candidate: `DEV-send-stream-0.1.0-b62`
- Version/build: `0.1.0 (62)`
- Exact product/config source: `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`
- Artifact: `9733577825`
- IPA SHA: `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`
- Runtime export: `ChatGPTClient-Diagnostics-20260830-151146.json`
- Runtime package metadata: Release / build 62 / Candidate b62 / source marker `e1b44f7ab6c4` / iPhone / iOS 17.0

## User-observed result

One cold/force-quit style tool-active repository turn was tested. User reported that the round looked normal overall. Screenshot showed visible reasoning, completed tool rows, and a complete-looking final answer with no obvious opening or middle truncation.

## Composer / Send-entry evidence

Startup did not falsely authorize a generic textarea:

- `15:08:55Z`: composer `ready=false`, strategy `none`
- page loaded as `new_or_other`
- `15:08:56Z`: composer still `ready=false`, strategy `none`
- `15:08:58Z`: composer became `ready=true`, strategy `prompt_textarea`

The user submitted only after the evidenced official composer was ready:

- `nativeSubmit` attempt 1
- submit-time composer `ready=true`, strategy `prompt_textarea`
- `submitResult=submitted`
- same second: `sendObserved` with `pageKind=existing_conversation`
- same second: `sendResponse` HTTP 200, `contentType=text/event-stream`
- initial thinking presentation entered from `lifecycle_send_accepted`

Classification: **focused Runtime pass for the b62 verified-composer Send-entry gate.** This run directly differs from b61's rejected false-ready sequence, where strategy `textarea` produced `submitted` with no subsequent `sendObserved`.

This single positive run does **not** prove the intermittent b61 page race can never recur under every future official-Web state. It proves the current b62 rule behaved correctly for this exact cold-launch path.

## Response / reasoning evidence

Terminal stream metrics:

- HTTP 200 SSE
- `terminal=true`
- `frameCount=196`
- `nativeReasoningCharacters=497`
- `nativeReasoningDeltaCount=34`
- `nativeReasoningSegmentBreakCount=2`
- `reasoningPreambleCount=3`
- `reasoningPreambleCharacters=20`
- `reasoningActiveSignalCount=3`
- `nativeThinkingPresentationCount=4`
- `reasoningEndMarkerCount=1`
- `reasoningFallbackPromoted=false`
- `nativeAnswerCharacters=2878`
- `nativeAnswerDeltaCount=93`
- `nativeCharacters=3375`
- `inactiveValueStringCount=0`
- `rootNonExactTextPatchCount=0`

The service returned explicit reasoning-active states and exact reasoning end; user-observed reasoning/final presentation remained complete-looking.

Classification: **Runtime pass for the tested b60-b61 reasoning/final presentation behavior preserved by b62.**

## Tool lifecycle evidence

The turn was strongly tool-active:

- `toolInvocationCount=20`
- `toolInvocationIdentityCount=21`
- `toolResultCount=20`
- `toolResultParentPresentCount=20`
- `toolResultParentMatchCount=20`
- `toolResultParentUnmatchedCount=0`
- `toolResultParentMissingCount=0`
- `toolResultPairedPresentationCount=20`
- `nativeToolPresentationCount=20`
- `nativeToolCompletionUpdateCount=20`

All 20 completed results with a parent reference matched an observed invocation identity and all 20 visible Native rows received completion updates. The extra invocation identity without a corresponding result in the final aggregate does not create a visible completion mismatch in the tested completed-result set and must not be force-paired by count/order.

Classification: **Runtime pass for the tested exact-parent paired `调用中 -> 已完成` lifecycle.**

## Safe detail-shape observations

The bounded b61/b62 shape diagnostics observed, among other structures:

- `connector_tool_payload`: string-shaped in multiple assistant code messages
- `reasoning_titles`: array of one string in some assistant code messages
- `tool_icons`: array of one string in several assistant code messages
- `invoked_resource`: object-shaped on several tool results
- `inline_cot_expandable_content`: object with `source_message_ids` on one `assistant:thoughts` structure

These are **shape observations only**. This Runtime does not authorize exposing raw tool requests/results, connector payload values, `assistant:thoughts`, or arbitrary invoked-resource fields. Exact user-visible expandable-detail schema remains Unknown / Unverified.

## Overall classification

**b62 focused Runtime pass** for the tested primary gate:

1. no generic-textarea false readiness in the observed cold-launch path;
2. verified `prompt_textarea` before Native submit;
3. real official protected Send observed after submit;
4. HTTP200 SSE reached terminal;
5. thinking/reasoning/final text remained complete-looking;
6. exact-parent tool lifecycle completed 20/20 for returned results.

b62 remains a diagnostic exception only. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership are unchanged. Stable/Frozen Send remains No.

## Next evidence boundary

Do not allocate a product change solely because b62 passed. The next code change must be tied to a concrete current evidence need. Expandable tool detail remains the nearest unresolved `DEV-send-stream` presentation target, but current evidence authorizes only bounded structural shape, not raw values/bodies. A next diagnostic may inspect a narrowly selected candidate field only if needed to prove which exact service field corresponds to official user-visible expandable detail, while continuing to prohibit raw connector/tool bodies and `assistant:thoughts`.
