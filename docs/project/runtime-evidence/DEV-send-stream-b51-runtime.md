# DEV-send-stream b51 Runtime Evidence

_Date: 2026-08-30 (device log timestamps 2026-08-29 UTC)_

## Exact identity

- Work: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b51`
- Version/build: `0.1.0 (51)`
- Product/config source: `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`
- Artifact: `9720327648`
- IPA SHA-256: `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`
- Runtime device metadata exported by app: iPhone / iOS 17.0 / Release / deployment target 14.0 / source marker `bd8f056cc4d1`.

## User observation

The user tested three sequential Native-composer turns. The first two were long-text replies and were visually judged effectively complete / without missing text. The third turn asked ChatGPT to use the GitHub project address to read the current development progress; its Native reply showed a small truncation at the **beginning**. A supplied screenshot begins mid-phrase, consistent with the direct observation.

## Turn 1 — fresh new chat / long answer

- protected Send: HTTP200 `text/event-stream`
- terminal: true
- `frameCount=307`
- `explicitTextPatchCount=2`
- `contextualValueStringCount=282`
- `contextualValueStringCharacters=11592`
- `nativeDeltaCount=284`
- `nativeCharacters=11618`
- `removedTextPatchCount=284`
- `removedTextCharacters=11618`
- `titleGenerationWhileContinuationCount=1`
- `webAssistantTextCharacters=0`
- `webMessageNodes=2`

Runtime conclusion: the exact b51 title-generation preservation path was exercised, and the previously failing fresh-new-chat long first response was visually complete. This directly supports the b51 hypothesis for the b50 fresh-first-turn missing-middle defect.

## Turn 2 — established turn / long answer

- protected Send: HTTP200 SSE
- terminal: true
- `frameCount=53`
- `explicitTextPatchCount=2`
- `contextualValueStringCount=40`
- `contextualValueStringCharacters=1348`
- `nativeDeltaCount=42`
- `nativeCharacters=1363`
- `titleGenerationWhileContinuationCount=0`
- `webAssistantTextCharacters=0`
- `webMessageNodes=4`

User visually judged this reply complete.

## Turn 3 — GitHub/tool-style request

Prompt category from user description: use repository address `https://github.com/white-shark-ssw/ChatGPT-Client.git` to obtain current development task/progress.

- protected Send: HTTP200 SSE
- terminal: true
- `frameCount=40`
- `explicitTextPatchCount=8`
- `contextualValueStringCount=8`
- `contextualValueStringCharacters=335`
- `nativeDeltaCount=16`
- `nativeCharacters=554`
- `removedTextPatchCount=16`
- `removedTextCharacters=554`
- `titleGenerationWhileContinuationCount=0`
- `webAssistantTextCharacters=0`
- `webMessageNodes=5`

User observed a small leading truncation. This is a separate failure shape from b50's fresh-first-turn missing middle and cannot be attributed to `title_generation` because the count is zero.

## Source-level follow-up boundary

Exact b51 source activates contextual value-only continuation only after an exact top-level assistant text append whose key set is exactly `o/p/v`. Other assistant text append objects may still be found recursively by `scrubTextPatches` and delivered to Native, but existing metrics do not distinguish root-with-extra-fields versus nested patches and do not count value-only strings seen while continuation is inactive.

The third turn's `explicitTextPatchCount=8` versus `2` on each complete turn makes this boundary worth measuring, but it is **not proof** that non-exact/nested text patches caused the truncation.

Next Candidate b52 therefore adds structural aggregate classification only. It must not broaden parser acceptance or forward inactive value-only frames to Native until exact Runtime evidence identifies the gap class.

## Acceptance classification

- b51 fresh-new-chat title-generation fix: **Runtime Confirmed for this exact test**.
- b51 established ordinary long response: **Runtime Confirmed for this exact test**.
- b51 complete parser coverage across GitHub/tool-style response: **Rejected / incomplete due leading truncation**.
- Overall b51: **partial Runtime pass; superseded by diagnostic-only b52 evidence collection, not Stable**.
- Production architecture / TD-024 / TD-025: unchanged.
