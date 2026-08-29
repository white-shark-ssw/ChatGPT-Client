# DEV-send-stream

## Status

**Active — exact b51 Runtime confirms the fresh-new-chat `title_generation` fix: the first long response was complete/incremental with `titleGenerationWhileContinuationCount=1`. A third GitHub/tool-style turn still showed a small leading truncation with `titleGenerationWhileContinuationCount=0`. b52 is allocated as a diagnostic-only structural classifier; it must not change filtering or continuation semantics. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / not merged; evidence branch only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b51**: `DEV-send-stream-0.1.0-b51`, `0.1.0 (51)`, product/config source `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`, Push `33271794573 / 99151433241`, PR `33271796259 / 99151437702`, Artifact `9720327648`, ZIP `sha256:247d22d0b8fa2d023f651c9c00461e90096e8fd21544b2147435e2d238a91ab2`, IPA SHA `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`.
- **Allocated next diagnostic identity**: `DEV-send-stream-0.1.0-b52`, `0.1.0 (52)`. Not yet emitted; reserved for the structural classifier described below.
- **Stable/Frozen Send**: No.

## Exact b51 Runtime

Evidence file to persist: `docs/project/runtime-evidence/DEV-send-stream-b51-runtime.md`.

Three sequential Native submissions all reached official protected Send HTTP200 SSE and terminal on exact b51 / iPhone / iOS17.0.

1. **Turn 1 — fresh new chat, long answer**: `frameCount=307`, `explicitTextPatchCount=2`, `contextualValueStringCount=282`, `contextualValueStringCharacters=11592`, `nativeDeltaCount=284`, `nativeCharacters=11618`, `titleGenerationWhileContinuationCount=1`, `webAssistantTextCharacters=0`. User visually judged the long reply complete, effectively without missing text.
2. **Turn 2 — long answer**: `frameCount=53`, `explicitTextPatchCount=2`, `contextualValueStringCount=40`, `nativeDeltaCount=42`, `nativeCharacters=1363`, title-generation count `0`, terminal true. User visually judged it complete.
3. **Turn 3 — GitHub project-address/current-development-progress request**: `frameCount=40`, `explicitTextPatchCount=8`, `contextualValueStringCount=8`, `contextualValueStringCharacters=335`, `nativeDeltaCount=16`, `nativeCharacters=554`, title-generation count `0`, terminal true, Web assistant text `0`. User observed a small truncation at the **beginning** of the Native reply; supplied screenshot shows the response begins mid-phrase.

Accepted b51 conclusion: the b50 fresh-first-turn missing-middle defect was caused by the evidenced `title_generation` continuation reset and is Runtime corrected on b51. Complete parser acceptance is still **No** because the separate third-turn leading truncation remains.

## Current source evidence / b52 diagnostic hypothesis

Current b51 parser activates `textContinuationActive` only for an exact top-level assistant append object whose key set is exactly `o/p/v`. Any other assistant text append found by recursive `scrubTextPatches` is still delivered to Native, but the parser has already cleared continuation and does not classify whether that append was root-with-extra-fields or nested. Existing b51 metrics therefore cannot tell whether the third-turn missing prefix came from value-only frames following a non-exact/nested assistant append.

This is a **hypothesis only**, not permission to broaden parsing.

b52 must preserve all b51 output/filter behavior and add aggregate structural diagnostics only:

- exact top-level text-append count;
- root text-append with extra/non-exact key-set count;
- nested text-append count;
- value-only string count/characters observed while continuation is inactive;
- continuation reset-while-active count;
- one bounded enum/context label for the first inactive value-only gap (for example after exact-root / nonexact-root / nested / reset / no-prior-text), without logging prompt/answer text or raw IDs.

Do not send inactive value-only strings to Native in b52; do not preserve any new structural frame; do not alter title-generation behavior.

## Evidence ladder

- b50 Code/CI/Artifact/package: Passed; Runtime partial pass.
- b51 Code/CI/Artifact/package: Passed; Runtime **partial pass with fresh-new-chat fix confirmed; separate tool/GitHub-style leading truncation remains**.
- b52: identity allocated; Code pending.
- Phase 9 Stable/Frozen: No.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b52 are diagnostic exceptions only. TD-024/TD-025 remain unchanged; no diagnostic success alone promotes hidden/shadow Web to production.

## Recovery state

Batches A-E complete. **Batch F — b51 Runtime -> b52 structural diagnostic** starts from feature head `c27b3975922424aff32ce1c56ed0678ac2d33492` and `main@1ac202c972f2dee6945fe8d0688df8e10f5d462c`.

Confirmed before Batch F: PR #29 open/not merged; only this Work is Active on the feature branch; b52 is not present in `BUILD_TEST_INDEX.md`; exact b51 is permanently reserved.

Intended Batch F writes:

1. checkpoint this recovery point — **completed by this commit**;
2. persist `DEV-send-stream-b51-runtime.md`;
3. implement diagnostic-only b52 structural counters in `NativeWebSendEngineProbe.swift` without parser behavior change;
4. update build/Candidate identity to b52 and CI artifact identity;
5. update durable project docs / build-test index for b51 Runtime + b52 Code/CI/Artifact evidence;
6. update PR #29 metadata and hand exact b52 Artifact to user for one focused GitHub/tool-style reproduction.

If interrupted, re-read this checkpoint and actual GitHub state; perform only missing deterministic writes. Never rebuild corrected code under b51.

## Next exact action

Persist the exact b51 Runtime evidence file, then implement b52 diagnostic-only structural classification. After CI/Artifact/package verification, hand b52 to the user. The b52 Runtime gate is one focused reproduction of a GitHub/tool-style response that previously showed leading truncation, plus diagnostics export. Parser behavior remains frozen until that evidence identifies the actual gap class.