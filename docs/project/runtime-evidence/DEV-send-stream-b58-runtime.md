# DEV-send-stream b58 Runtime Evidence

_Date: 2026-08-30_

## Exact candidate identity

- Candidate: `DEV-send-stream-0.1.0-b58`
- Version/build: `0.1.0 (58)`
- Exact product/config source: `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`
- Product tree: `ddb396aa942c48222e69671eaf3610127d9797e9`
- Artifact: `9729864129`
- IPA SHA-256: `0d5988caf21300bfb29e81b3f1f8bbf6eaa69a84f09efeda601e6d6f9b7b8875`
- Runtime export: `ChatGPTClient-Diagnostics-20260830-094146.json`
- Export identity: Release / build58 / Candidate b58 / source `d9dbf208625e` / iPhone / iOS17.0

## Direct user-visible result

The user supplied both the Native diagnostic screen and the complete official-Web rendering for the same turn.

Accepted visual evidence:

- Native `思考过程` again begins after the real visible reasoning start; the leading prefix is truncated.
- The official-Web screenshot contains an 8-character opening preamble that is absent from the Native reasoning screenshot.
- The final answer is visually complete in Native.
- A separate Native `工具调用` region appears and contains four activity lines.
- One activity line uses a coherent service-provided title; the remaining invocations use the intentional generic `工具调用` fallback.
- No raw tool arguments, raw tool results, connector payload or `assistant:thoughts` is presented in the Native diagnostic surface.

The actual reasoning/tool body text is intentionally not copied into this evidence file.

## Transport / terminal evidence

One official protected Send:

- HTTP status `200`
- content type `text/event-stream`
- `frameCount=53`
- terminal `true`
- `reasoningEndMarkerCount=1`
- `reasoningFallbackPromoted=false`

## Native text metrics

- Native total: `18 deltas / 338 chars`
- Native reasoning: `4 deltas / 52 chars`
- Native final answer: `14 deltas / 286 chars`
- `assistantTextMessageCount=2`
- before reasoning end: `1`
- after reasoning end: `1`
- phase text structures: `2 / overflow0`

The reasoning→final phase split therefore remains working in this exact turn even though the opening reasoning preamble is missing.

## Exact leading-prefix structure

The first before-reasoning-end ordinary assistant text message is event 14:

- role `assistant`
- content type `text`
- status `in_progress`
- recipient `all`
- direct content keys `content_type,parts`
- `parts:1:string:chars8`
- direct metadata includes `is_thinking_preamble_message:true`

Event 15 is then the first exact top-level `append /message/content/parts/0` text patch.

The user-provided official-Web screenshot has an 8-character opening phrase that is absent from the Native screenshot. That missing visual length exactly matches the event-14 service-marked preamble length. This is materially stronger evidence than b57's prior visual-only no-truncation observation.

Accepted conclusion: the exact service-marked `is_thinking_preamble_message` single string part is user-visible reasoning presentation data for this Runtime sample and is currently omitted by the b58 Native path.

## Existing parser metrics

- `exactTopLevelTextPatchCount=3`
- `rootNonExactTextPatchCount=0`
- `nestedTextPatchCount=5`
- `contextualValueStringCount=10`
- `contextualValueStringCharacters=207`
- `inactiveValueStringCount=0`
- `inactiveValueStringCharacters=0`
- `continuationResetWhileActiveCount=3`
- `titleGenerationWhileContinuationCount=0`
- generic structures `32 / overflow2`
- special structures `8 / overflow0`

No existing b50-b57 compact-patch correction is implicated by this reproduction. The missing text is the separate initial preamble message, not a root-nonexact or inactive-value continuation failure.

## Tool activity metrics

- `toolInvocationCount=4`
- `toolInvocationWithTitleCount=1`
- `toolResultCount=4`
- `toolResultWithTitleCount=3`
- `nativeToolPresentationCount=4`

Exact completed invocation/result structure continues to match the b58 rule. Result titles are observed structurally but remain non-presentational under b58; no guessed invocation/result pairing is introduced.

Accepted classification for the tested scope: **bounded tool activity Runtime pass**.

## Runtime classification

**b58 Runtime partial pass.**

Passed:

- official protected Send / SSE interception for this turn;
- reasoning→final phase separation;
- final-answer completeness by direct user observation;
- bounded tool-activity presentation;
- privacy boundary for raw tool/thought payloads.

Failed:

- Native reasoning opening completeness; exact 8-character user-visible preamble omitted.

## Smallest evidence-backed next change

A later Candidate may consume only an exact pre-reasoning-end message satisfying all of:

1. assistant role;
2. `content_type=text`;
3. `status=in_progress`;
4. recipient `all`;
5. non-empty service message ID;
6. `metadata.is_thinking_preamble_message === true`;
7. `content.parts` is exactly one non-empty string.

That string may be posted once through the existing Native reasoning-delta path, deduplicated in memory by service message ID. Diagnostics may record only preamble count and character count, never the text or ID.

Do not broaden arbitrary assistant initial content, arbitrary `parts`, recap text, `assistant:thoughts`, tool args/results or generic structural messages into visible reasoning.

## Architecture boundary

This Runtime evidence does not change TD-024/TD-025/TD-028, does not approve the diagnostic hidden/shadow Web Send-engine as production architecture, and does not transfer future accepted response ownership away from `ConversationRepository`.
