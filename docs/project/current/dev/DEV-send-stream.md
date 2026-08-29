# DEV-send-stream

## Status

**Active — exact b51 Runtime confirms the fresh-new-chat `title_generation` fix: the first long response was complete/incremental with `titleGenerationWhileContinuationCount=1`. A third GitHub/tool-style turn still showed a small leading truncation with `titleGenerationWhileContinuationCount=0`. Exact b52 is now Code/config written as a diagnostic-only structural classifier; CI/Artifact pending. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / not merged; evidence branch only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b51**: `DEV-send-stream-0.1.0-b51`, `0.1.0 (51)`, product/config source `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`, Push `33271794573 / 99151433241`, PR `33271796259 / 99151437702`, Artifact `9720327648`, ZIP `sha256:247d22d0b8fa2d023f651c9c00461e90096e8fd21544b2147435e2d238a91ab2`, IPA SHA `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`.
- **Exact b52**: `DEV-send-stream-0.1.0-b52`, `0.1.0 (52)`, product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`; CI/Artifact pending.
- **Stable/Frozen Send**: No.

## Exact b51 Runtime

Evidence: `docs/project/runtime-evidence/DEV-send-stream-b51-runtime.md`.

Three sequential Native submissions all reached official protected Send HTTP200 SSE and terminal on exact b51 / iPhone / iOS17.0.

1. **Turn 1 — fresh new chat, long answer**: `frameCount=307`, `explicitTextPatchCount=2`, `contextualValueStringCount=282`, `contextualValueStringCharacters=11592`, `nativeDeltaCount=284`, `nativeCharacters=11618`, `titleGenerationWhileContinuationCount=1`, `webAssistantTextCharacters=0`. User visually judged the long reply complete.
2. **Turn 2 — long answer**: `frameCount=53`, `explicitTextPatchCount=2`, `contextualValueStringCount=40`, `nativeDeltaCount=42`, `nativeCharacters=1363`, title-generation count `0`, terminal true. User visually judged it complete.
3. **Turn 3 — GitHub project-address/current-development-progress request**: `frameCount=40`, `explicitTextPatchCount=8`, `contextualValueStringCount=8`, `contextualValueStringCharacters=335`, `nativeDeltaCount=16`, `nativeCharacters=554`, title-generation count `0`, terminal true, Web assistant text `0`. User observed a small truncation at the **beginning** of the Native reply.

Accepted b51 conclusion: the b50 fresh-first-turn missing-middle defect was caused by the evidenced `title_generation` continuation reset and is Runtime corrected on b51. Complete parser acceptance is still **No** because the separate third-turn leading truncation remains.

## b52 diagnostic-only implementation

Current b51 parser activates `textContinuationActive` only for an exact top-level assistant append object whose key set is exactly `o/p/v`. Other assistant text append objects may be recursively scrubbed and delivered to Native without activating continuation. This remains a hypothesis for the third-turn gap, not an accepted parser rule.

Exact b52 source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f` preserves b51 filtering/output behavior and adds only aggregate structural fields:

- `exactTopLevelTextPatchCount`;
- `rootNonExactTextPatchCount`;
- `nestedTextPatchCount`;
- `inactiveValueStringCount` / `inactiveValueStringCharacters`;
- `continuationResetWhileActiveCount`;
- bounded `firstInactiveValueContext`.

b52 does **not** send inactive value-only strings to Native, does not preserve any new structural frame, and does not alter the b51 `title_generation` behavior.

The Swift source, both target build configurations (`CURRENT_PROJECT_VERSION=52`, Candidate b52), and workflow Artifact identity `ChatGPTClient-DEV-send-stream-0.1.0-b52` were assembled in one Git tree/commit and the feature ref moved once. This avoids any intermediate feature head containing b52 code under b51 identity.

## Evidence ladder

- b50 Code/CI/Artifact/package: Passed; Runtime partial pass.
- b51 Code/CI/Artifact/package: Passed; Runtime **partial pass with fresh-new-chat fix confirmed; separate tool/GitHub-style leading truncation remains**.
- b52 Code/config: Written at `5c0690ce...`; CI/Artifact/package pending; Runtime pending.
- Phase 9 Stable/Frozen: No.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b52 are diagnostic exceptions only. TD-024/TD-025 remain unchanged; no diagnostic success alone promotes hidden/shadow Web to production.

## Recovery state

**Batch F — b51 Runtime -> b52 structural diagnostic**

Baseline: `main@1ac202c972f2dee6945fe8d0688df8e10f5d462c`.

Completed:

1. checkpointed b51 Runtime / b52 plan;
2. persisted `DEV-send-stream-b51-runtime.md` at commit `436b376259e01ad9ce9ab226efe882d42060d289`;
3. assembled b52 Swift + build/Candidate + workflow identity in one tree;
4. moved feature branch to exact b52 source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`.

Remaining:

5. verify exact b52 Push/PR CI, Artifact and package identity;
6. update durable project docs / `BUILD_TEST_INDEX.md` and PR #29 metadata;
7. hand exact b52 Artifact to user for one focused GitHub/tool-style reproduction.

If interrupted, re-read this checkpoint and actual GitHub state; perform only missing deterministic writes. Never rebuild corrected code under b51.

## Next exact action

Verify CI for exact source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`. If CI/Artifact/package are valid, persist b52 identity/evidence and hand it to the user. The b52 Runtime gate is one focused reproduction of a GitHub/tool-style response that previously showed leading truncation, plus diagnostics export. Parser behavior remains frozen until that evidence identifies the actual gap class.