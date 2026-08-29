# DEV-send-stream

## Status

**Active — exact b50 Runtime materially passes the diagnostic core on turns 2–3; fresh new-chat turn 1 still truncates. Exact b51 changes only the evidenced `title_generation` continuation reset boundary and is Code/CI/Artifact/package verified. The next gate is exact-device fresh-new-chat b51 Runtime. TD-024/TD-025 remain unchanged; b48-b51 are isolated diagnostic exceptions only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only; title/body synchronized to the b51 Runtime gate.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b50**: `DEV-send-stream-0.1.0-b50`, source `837d5feeff05d198785f884ccf9cc4c1f71412ec`, Artifact `9719942650`, IPA SHA `26431faabe0b2c836fd6c1d7aa84d31cf8811ea09d57a8ad692e127ecb42613c`.
- **Exact b51**: `DEV-send-stream-0.1.0-b51`, `0.1.0 (51)`, source `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`, Push `33271794573 / 99151433241`, PR `33271796259 / 99151437702`, Artifact `9720327648`, ZIP `sha256:247d22d0b8fa2d023f651c9c00461e90096e8fd21544b2147435e2d238a91ab2`, IPA SHA `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`, Release/iOS14/`[1,2]`/arm64.
- **Stable/Frozen Send**: No.

## b50 Runtime

Evidence: `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`.

- Three sequential Native submissions all reached official protected Send HTTP200 SSE and terminal.
- Turn 1 fresh new-chat: 35 Native chars / 3 deltas; user reported a long answer with a missing middle.
- Turn 2: 191 chars / 10 deltas / 8 contextual value-only frames; complete visible incremental output.
- Turn 3: 671 chars / 31 deltas / 29 contextual value-only frames; complete incremental/effectively character-by-character output.
- Web assistant terminal text stayed small on successful turns.

Accepted: Native incremental streaming and contextual value-only compact continuation are Runtime Confirmed for the diagnostic path on established turns. Fresh-first-turn completeness is not accepted.

## b51 implementation / gate

Historical b40/b41 evidence says fresh new-chat first Send emits `title_generation`. b51 only preserves an already-active assistant-text continuation across exact top-level `type == "title_generation"` with no `o`/`p`, forwards that frame unchanged, and records `titleGenerationWhileContinuationCount`. Every other b50 parser/reset rule remains unchanged.

Fresh-new-chat Runtime gate:

1. clear diagnostics; open `Native 输入 / Web Send（b51诊断）`;
2. request a genuinely long first answer;
3. verify the whole first answer streams without missing middle;
4. send a second Native turn after terminal;
5. export diagnostics.

Pass signal: HTTP200 SSE/terminal, `titleGenerationWhileContinuationCount > 0` if the hypothesis is correct, long-answer-scale contextual/native counts, complete first answer, small Web assistant text, successful second turn.

If the count is zero or truncation remains, do not broaden parser grammar by guess.

## Evidence ladder

- b50 Code/CI/Artifact/package: Passed; Runtime partial pass.
- b51 Code/CI/Artifact/package: Passed; Runtime pending.
- Phase 9 Stable/Frozen: No.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b51 are diagnostic exceptions only. TD-024/TD-025 are unchanged; PR #29 remains evidence-only.

## Recovery state

Batches A-E are complete. PR #29 title/body already match the b51 fresh-new-chat Runtime gate. New-session Full Resume Guard revalidated `main@1ac202c972f2dee6945fe8d0688df8e10f5d462c`, feature head `c9260bf0dcf26a077b8ebf47ca472c1215712b8f` before this docs-only checkpoint, PR #29 open/not merged, and exactly one Active development checkpoint on the feature branch.

The exact Push run `33271794573` was independently re-read and confirms `head_sha=bd8f056cc4d13ea2f1ab178353d926d8e4d21992`, success. Artifact `9720327648` was re-downloaded and independently inspected: ZIP digest `247d22d0b8fa2d023f651c9c00461e90096e8fd21544b2147435e2d238a91ab2`; IPA SHA `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`; built Info.plist `0.1.0 (51)`, Candidate `DEV-send-stream-0.1.0-b51`, source marker `bd8f056cc4d1`, Release, iOS14.0, UIDeviceFamily `[1,2]`; executable arm64. No product rebuild is permitted under b51.

## Next exact action

User installs the exact b51 IPA and performs the fresh-new-chat Runtime gate above. After the user returns with direct observation and exported diagnostics, classify b51 Runtime, persist exact Runtime evidence, and allocate b52 only if the b51 evidence justifies a specific smallest correction.