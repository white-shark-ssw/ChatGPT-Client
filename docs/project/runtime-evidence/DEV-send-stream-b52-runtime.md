# DEV-send-stream b52 Runtime Evidence

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b52`
- Version/build: `0.1.0 (52)`
- Exact product/config source: `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`
- Runtime device: iPhone / iOS 17.0
- Diagnostics export: `2026-08-30T05:08:13Z`
- Evidence class: exact-device Native-composer/Web-Send-engine diagnostic Runtime; not production Send acceptance.

## User-observed result

The user explicitly reported that, in this b52 reproduction:

- the **beginning of the visible reasoning/thinking portion was slightly truncated**;
- the **real/final answer was not truncated**.

This refines the earlier b51 tool/GitHub-style observation: the remaining visible gap is reasoning-specific on this reproduction rather than a final-answer prefix loss.

## Exact transport / terminal result

One Native submission was made from the b52 diagnostic surface.

- Native prompt character count: `135`.
- Official protected Send observed on an existing conversation.
- Send response: HTTP `200`, `text/event-stream`, interception active.
- Terminal: `true`.
- Web composer returned ready after terminal.
- Web assistant terminal DOM text: `0` characters.

## Exact b52 aggregate stream metrics

- `frameCount=74`
- `removedTextPatchCount=26`
- `removedTextCharacters=614`
- `explicitTextPatchCount=11`
- `exactTopLevelTextPatchCount=5`
- `rootNonExactTextPatchCount=0`
- `nestedTextPatchCount=6`
- `contextualValueStringCount=15`
- `contextualValueStringCharacters=355`
- `inactiveValueStringCount=0`
- `inactiveValueStringCharacters=0`
- `continuationResetWhileActiveCount=5`
- `firstInactiveValueContext=none`
- `titleGenerationWhileContinuationCount=0`
- `nativeDeltaCount=26`
- `nativeCharacters=614`
- `terminal=true`

## Accepted conclusions

1. **Final-answer capture passed for this exact reproduction.** The user observed no truncation in the real/final answer and the stream reached normal terminal.
2. **User-visible reasoning capture remains incomplete.** The beginning of the reasoning/thinking portion was visibly truncated.
3. The b52 evidence rejects the specific hypothesis that this reproduction lost text because a root non-exact assistant append failed to activate subsequent value-only continuation: `rootNonExactTextPatchCount=0` and `inactiveValueStringCount=0`.
4. The stream did contain `6` nested assistant text patches and `5` structural resets while active continuation existed. The final answer still completed, so these counters alone cannot identify which parent event/content type belongs to user-visible reasoning/tool presentation.
5. The b51 fresh-new-chat `title_generation` conclusion remains intact. This b52 turn had `titleGenerationWhileContinuationCount=0`; the remaining reasoning gap is a separate structure class.
6. Current evidence is insufficient to implement reasoning/tool UI or broaden parser grammar safely. The next diagnostic must identify service-visible event type / patch path / message role / content type without logging text or raw identifiers.

## Rejected / superseded hypothesis

The prior generic “tool-style leading reply truncation may be caused by non-exact root patch followed by inactive `{v:string}` continuation” hypothesis is **not supported by this exact b52 reproduction**.

Do not add a generic inactive-value fallback, generic patch-path acceptance or arbitrary `v:string` capture based on the b52 result.

## Next evidence gate

Use exact b53 as a behavior-neutral structure classifier over the same pre-React Send SSE path. Reuse the privacy-safe b41 structural-probe pattern to record only bounded unique signatures including event type, operation, patch path, message role/content type, structural key names and nested batch patch paths.

The b53 Runtime reproduction should naturally invoke visible reasoning and tool activity. Only after those structures are identified should the task implement Native reasoning lifecycle, collapse/expand presentation or a tool-call detail sheet.