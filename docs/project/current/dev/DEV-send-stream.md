# DEV-send-stream

## Status

**Active — exact b50 Runtime materially passes the diagnostic core on turns 2–3: Native composer -> official Web protected Send -> intercepted SSE -> incremental Native assistant text -> terminal -> next Native turn all work, while Web assistant DOM text stays small. Fresh-new-chat turn 1 still truncated. Historical b40/b41 evidence says new-chat first Send emits `title_generation`; exact b51 changes only that reset boundary and is Code/CI/Artifact/package verified. The next gate is exact-device fresh-new-chat b51 Runtime. TD-024/TD-025 remain unchanged; b48-b51 are isolated diagnostic exceptions only.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / Native composer / Web Send engine / filtered SSE / hidden Web diagnostic`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b50 Candidate**: `DEV-send-stream-0.1.0-b50`, `0.1.0 (50)`; product source `837d5feeff05d198785f884ccf9cc4c1f71412ec`; Artifact `9719942650`; IPA SHA `26431faabe0b2c836fd6c1d7aa84d31cf8811ea09d57a8ad692e127ecb42613c`; permanently reserved.
- **Exact b51 Candidate**: `DEV-send-stream-0.1.0-b51`, `0.1.0 (51)`.
- **Exact b51 product/config source**: `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`; permanently reserved after Artifact emission.
- **b51 Push CI**: Run `33271794573`, Job `99151433241` — success.
- **b51 PR CI**: Run `33271796259`, Job `99151437702` — success.
- **b51 Artifact**: `9720327648`.
- **b51 Artifact ZIP digest**: `sha256:247d22d0b8fa2d023f651c9c00461e90096e8fd21544b2147435e2d238a91ab2`.
- **b51 IPA SHA-256**: `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`.
- **b51 package identity**: independently verified `0.1.0 (51)` / Candidate b51 / `DiagnosticsSourceCommit=bd8f056cc4d1` / Release / iOS14 minimum / UIDeviceFamily `[1,2]` / arm64.
- **Stable/Frozen Send**: No.

## Exact b50 Runtime summary

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`.

- Three sequential Native submissions all reached official protected Send HTTP200 SSE and terminal.
- Turn 1 new-chat first turn: `contextualValueStringCount=1`, `nativeDeltaCount=3`, `nativeCharacters=35`; user reported a long reply with a missing middle.
- Turn 2: `contextualValueStringCount=8`, `nativeDeltaCount=10`, `nativeCharacters=191`, Web assistant text 45; user reported complete visible incremental output.
- Turn 3: `contextualValueStringCount=29`, `nativeDeltaCount=31`, `nativeCharacters=671`, Web assistant text 45; user reported complete incremental/effectively character-by-character output.
- Therefore Native incremental delivery and the contextual compact value-only continuation are Runtime Confirmed for this diagnostic path on established turns; b50 remains partial because fresh first turn truncated.

## b51 exact implementation

Historical b40/b41 Runtime established new-chat first Send emits `title_generation`. b51 changes only this narrow b50 reset rule:

- if assistant-text continuation is active and an exact top-level object has `type == "title_generation"` with no `o`/`p`, forward that frame unchanged and preserve continuation;
- increment `titleGenerationWhileContinuationCount`;
- keep every other b50 continuation/reset/filter rule unchanged.

No generic structural preservation, Repository/Auth/Root/ConversationFeature/attachment/history-virtualization/resume change, retry, timer, watchdog or fallback was added.

## b51 Runtime gate

1. clear diagnostics and open `Native 输入 / Web Send（b51诊断）`;
2. use a fresh/new chat and request a genuinely long first answer;
3. verify first answer grows incrementally through the whole middle;
4. after terminal, send a second Native turn;
5. export diagnostics after the second terminal.

Pass evidence: first turn HTTP200 SSE / terminal true; `titleGenerationWhileContinuationCount > 0` if the hypothesis is right; long-answer-scale contextual/native counts; complete first answer; small Web assistant DOM; successful second turn.

If the metric is zero or truncation remains, do not broaden parser grammar by guess; collect the smallest structural evidence for the actual reset frame.

## Evidence ladder

- b50 Code/CI/Artifact/package: Passed.
- b50 Runtime: Partial pass — core architecture and complete turns 2/3 confirmed; fresh first-turn parser incomplete.
- b51 Code/CI/Artifact/package: Passed.
- b51 Runtime: Pending.
- Phase 9 Stable/Frozen: No.

## Durable boundary retained

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b51 are diagnostic exceptions only. TD-024/TD-025 are unchanged and PR #29 must not be merged as accepted production Send UX yet.

## Non-atomic recovery state

- Batches A-D: complete.
- Batch E: all durable docs files synchronized to b51; only PR #29 metadata and this checkpoint final closeout remain.

## Next exact action

Update PR #29 title/body to b51 fresh-new-chat Runtime gate, mark Batch E complete, then hand exact Artifact `9720327648` IPA to the user. Do not rebuild b51; later product correction requires b52+.