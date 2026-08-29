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

## Resume / conflict guard

Current-session guard is satisfied:

- current `AGENTS.md` then `docs/project/START_HERE.md` reloaded before continuation;
- user request uniquely continues `DEV-send-stream`;
- branch / PR / exact b51 source / Artifact identity revalidated from current GitHub state;
- current feature head after b51 product is docs-only over exact source `bd8f056...`;
- PR #29 remains open / mergeable / not merged;
- `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- no second Active development checkpoint exists;
- no product/config write has occurred after b51 Artifact emission.

## Exact b50 Runtime — 2026-08-29

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`.

User tested three sequential Native-composer turns in one fresh probe session and described the overall result as very good. Turns 2 and 3 were complete and visibly incremental, effectively character-by-character; turn 1 was a long server reply whose Native display lost a middle section.

### Turn 1 — new-chat first turn / incomplete

- official Send HTTP200 `text/event-stream`, `filtered=true`, terminal true, composer ready;
- `frameCount=34`;
- `explicitTextPatchCount=2`;
- `contextualValueStringCount=1`, `contextualValueStringCharacters=16`;
- `nativeDeltaCount=3`, `nativeCharacters=35`;
- `webAssistantTextCharacters=45`.

Complete Native interception is rejected for this turn because direct user observation says the answer was materially longer.

### Turn 2 — accepted positive diagnostic turn

- HTTP200 SSE, terminal true, composer ready;
- `explicitTextPatchCount=2`;
- `contextualValueStringCount=8`, `contextualValueStringCharacters=152`;
- `nativeDeltaCount=10`, `nativeCharacters=191`;
- `webAssistantTextCharacters=45`;
- user observed complete incremental output.

### Turn 3 — strongest accepted positive diagnostic turn

- HTTP200 SSE, terminal true, composer ready;
- `explicitTextPatchCount=2`;
- `contextualValueStringCount=29`, `contextualValueStringCharacters=652`;
- `nativeDeltaCount=31`, `nativeCharacters=671`;
- `webAssistantTextCharacters=45`;
- user observed complete incremental output.

Accepted b50 conclusions:

1. Context-bound value-only `v:string` continuation is real and carries most assistant text on successful turns.
2. Native incremental text delivery is Runtime Confirmed for this diagnostic path; it is not a completion-time dump.
3. Three sequential Native submissions all reached official protected Send HTTP200 SSE and terminal.
4. Web assistant DOM text stayed small while Native captured materially larger answer text on turns 2/3.
5. b50 does not pass the complete parser gate because fresh new-chat turn 1 truncated.

## b51 exact implementation

Historical exact b40/b41 Runtime established that a new-chat first Send emits `title_generation`. b50 cleared `textContinuationActive` on every parsed frame that was neither explicit assistant append nor contextual value-only string. b51 changes only this narrow rule:

- when continuation is active and an exact top-level object has `type == "title_generation"` with no `o`/`p`, preserve `textContinuationActive`;
- forward that title-generation frame unchanged to Web;
- increment `titleGenerationWhileContinuationCount`;
- keep every other b50 continuation/reset rule unchanged.

No generic structural-frame preservation was added. No `ConversationRepository`, `AuthSessionStore`, `RootViewController`, `ConversationFeature`, build-script, attachment, history-virtualization or resume change was made. No retry/timer/watchdog/fallback was added.

## b51 Runtime gate

Use a fresh/new-chat probe because that is the only failing b50 case:

1. clear diagnostics and open `Native 输入 / Web Send（b51诊断）`;
2. first Native turn should request a genuinely long answer;
3. verify the first answer grows incrementally through the entire body with no missing middle;
4. wait for terminal, then send a second Native turn;
5. export diagnostics after second terminal.

Required first-turn evidence:

- HTTP200 SSE / terminal true;
- `titleGenerationWhileContinuationCount > 0` if the hypothesis is correct;
- contextual value-only count and Native character count rise to long-answer scale instead of b50's `1 / 35` pattern;
- user-visible first answer is complete;
- Web assistant DOM remains small relative to Native captured text;
- second turn still succeeds.

If `titleGenerationWhileContinuationCount == 0` or the first turn still truncates, do not broaden parser grammar by guess. Collect only the smallest structural evidence needed to identify the actual reset frame.

## Evidence ladder

- b50 Code/CI/Artifact/package identity: Passed.
- b50 Runtime/manual: **Partial pass** — core architecture and complete incremental turns 2/3 confirmed; new-chat turn 1 parser incomplete.
- b51 Code written: Yes.
- b51 CI: Passed.
- b51 Artifact produced: Yes.
- b51 package identity: Verified.
- b51 Runtime/manual: Pending.
- Phase 9 Stable/Frozen: No.

## Durable boundary retained

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b51 remain diagnostic exceptions. TD-024/TD-025 are not changed by these tests. PR #29 remains evidence-only and must not be merged as accepted production Send UX.

## Non-atomic recovery state

- Batch A — b50 Runtime evidence + b51 allocation: complete.
- Batch B — non-CI b51 assembly: complete.
- Batch C — exact four-file audit + Light Guard + non-force publish: complete.
- Batch D — exact-source Push/PR CI + Push Artifact + package inspection: complete.
- Batch E — all durable file synchronization is complete. PR #29 metadata is the only remaining write before final checkpoint closeout.

## Next exact action

Update PR #29 title/body to the exact b51 fresh-new-chat Runtime gate, then mark Batch E complete without changing exact b51 product/config source. Hand exact Artifact `9720327648` IPA to the user. The next human-only gate is fresh-new-chat b51 Runtime. Do not rebuild b51; any later product correction requires b52+.