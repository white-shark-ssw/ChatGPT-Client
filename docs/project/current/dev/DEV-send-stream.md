# DEV-send-stream

## Status

**Active — exact b50 Runtime materially passes the core diagnostic architecture on turns 2–3: Native composer -> official Web protected Send -> intercepted SSE -> incremental Native assistant text -> terminal -> next Native turn all work, while Web assistant DOM text remains small. New-chat turn 1 still truncates after one contextual value-only continuation. Historical b40/b41 evidence says new-chat first Send emits `title_generation`; b50 clears assistant-text continuation on every non-value structural frame, so b51 is allocated to test the smallest evidence-backed correction: preserve continuation only across `title_generation`, with a structural counter proving whether that event actually occurred while continuation was active. TD-024/TD-025 remain unchanged; b48-b51 are diagnostic exceptions only.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / Native composer / Web Send engine / filtered SSE / hidden Web diagnostic`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b50 Candidate**: `DEV-send-stream-0.1.0-b50`, `0.1.0 (50)`.
- **Exact b50 product/config source**: `837d5feeff05d198785f884ccf9cc4c1f71412ec`; permanently reserved.
- **b50 Push CI**: `33270436935 / 99147835200` — success.
- **b50 PR CI**: `33270439156 / 99147841433` — success.
- **b50 Artifact**: `9719942650`.
- **b50 ZIP SHA-256**: `dde656d41ea767714586a92a46740bb9bfe51531b74673e266a58aeec5dce99b`.
- **b50 IPA SHA-256**: `26431faabe0b2c836fd6c1d7aa84d31cf8811ea09d57a8ad692e127ecb42613c`.
- **b50 package identity**: `0.1.0 (50)` / Candidate b50 / source marker `837d5feeff05` / Release / iOS14 minimum / `[1,2]` / arm64.
- **Allocated next Candidate**: `DEV-send-stream-0.1.0-b51`, `0.1.0 (51)`.
- **Stable/Frozen Send**: No.

## Resume / conflict guard

Current-session Full/Light guard:

- reread current branch `AGENTS.md`, then `docs/project/START_HERE.md`, Development router, project profile/state/module/technical/rules/docs policy, `CLIENT_ARCHITECTURE_GAP_REVIEW.md` and `SEND_STREAM_PREFLIGHT.md`;
- user feedback uniquely continues `DEV-send-stream` exact b50 Runtime;
- real feature branch before this checkpoint was `93229404fe62c8a44eb79fa20e564abea5aec695`;
- branch delta from exact b50 product source `837d5fe...` to `93229404...` is docs-only checkpoint state;
- PR #29 remains open / mergeable / not merged;
- `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- `docs/project/current/dev/` contains no second Active development checkpoint;
- repository search found no existing b51 allocation;
- b50 is immutable after Artifact emission; any product correction is b51+.

## Exact b50 Runtime — 2026-08-29

Detailed evidence file: `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`.

Uploaded diagnostics identity:

- app `0.1.0`, build `50`;
- Candidate `DEV-send-stream-0.1.0-b50`;
- source `837d5feeff05`;
- Release;
- iPhone / iOS17.0.

User direct observation:

- three sequential Native-composer turns were tested in one fresh probe session;
- turns 2 and 3 were complete and visibly incremental, described as effectively character-by-character output;
- turn 1 was long server-side but Native output lost a middle section;
- overall interaction quality was reported as very good.

### Turn 1 — new-chat first turn / incomplete

- official Send HTTP200 `text/event-stream`, `filtered=true`;
- `frameCount=34`, terminal true, composer ready afterward;
- `explicitTextPatchCount=2`;
- `contextualValueStringCount=1`, `contextualValueStringCharacters=16`;
- `nativeDeltaCount=3`, `nativeCharacters=35`;
- `removedTextPatchCount=3`, `removedTextCharacters=35`;
- `webAssistantTextCharacters=45`;
- direct user observation says answer was materially longer, so complete Native interception is rejected for this turn.

### Turn 2 — accepted positive diagnostic turn

- official Send HTTP200 SSE, terminal true, composer ready;
- `frameCount=21`;
- `explicitTextPatchCount=2`;
- `contextualValueStringCount=8`, `contextualValueStringCharacters=152`;
- `nativeDeltaCount=10`, `nativeCharacters=191`;
- `removedTextPatchCount=10`, `removedTextCharacters=191`;
- `webAssistantTextCharacters=45`;
- user observed complete incremental output.

### Turn 3 — strongest accepted positive diagnostic turn

- official Send HTTP200 SSE, terminal true, composer ready;
- `frameCount=42`;
- `explicitTextPatchCount=2`;
- `contextualValueStringCount=29`, `contextualValueStringCharacters=652`;
- `nativeDeltaCount=31`, `nativeCharacters=671`;
- `removedTextPatchCount=31`, `removedTextCharacters=671`;
- `webAssistantTextCharacters=45`;
- user observed complete incremental output.

Accepted b50 conclusions:

1. Context-bound value-only `v:string` continuation is real and carries most assistant text on successful turns.
2. Native incremental text delivery is Runtime Confirmed for this diagnostic path; it is not a completion-time dump.
3. Three sequential Native submissions all reached official protected Send HTTP200 SSE and terminal, so continuity through at least three turns is positive.
4. Web assistant DOM text stayed small while Native captured 191/671 characters on turns 2/3, supporting the intended pre-React text removal direction.
5. b50 does **not** pass the complete parser gate because fresh new-chat turn 1 truncated.

## b51 evidence-backed hypothesis and exact scope

Historical exact b40/b41 Runtime already established that a new-chat first Send emits `title_generation`. b50 currently executes `aggregate.textContinuationActive = false` for every parsed frame that is neither explicit assistant append nor contextual value-only string.

The only cross-turn structural distinction established by current evidence is that turn 1 is the fresh/new-chat turn while turns 2/3 are subsequent existing-conversation turns. Therefore b51 tests only this narrow hypothesis:

> a `title_generation` frame may occur after assistant text continuation begins; it is metadata for the new conversation and must not invalidate the compressed assistant append context.

b51 may only:

- detect exact top-level `payload.type === "title_generation"` while assistant text continuation is active;
- preserve `textContinuationActive` across that frame instead of clearing it;
- forward the `title_generation` frame unchanged to Web;
- count `titleGenerationWhileContinuationCount` structurally in terminal metrics;
- keep all other b50 continuation/reset behavior unchanged;
- update diagnostic label/mode and Candidate/build/workflow identity to b51.

Do **not** preserve continuation generically across arbitrary structural frames. Do not modify `ConversationRepository`, `AuthSessionStore`, `RootViewController`, `ConversationFeature`, build scripts, attachments, history virtualization, resume behavior, TD-024/TD-025 or Stable b38 presentation. No retry/timer/watchdog/fallback.

## b51 Runtime gate

Use a fresh/new-chat diagnostic because that is the only failing b50 case:

1. clear diagnostics and open b51 probe;
2. first Native turn must request a genuinely long answer;
3. verify the first answer remains incrementally visible through the entire body with no missing middle;
4. wait terminal and send a second Native turn;
5. export diagnostics after second terminal.

Required first-turn evidence:

- HTTP200 SSE / terminal true;
- `titleGenerationWhileContinuationCount > 0` if the hypothesis is correct;
- `contextualValueStringCount` and Native character count rise to long-answer scale instead of b50's 1 / 35-character pattern;
- user-visible first answer is complete, not only beginning/end fragments;
- Web assistant DOM remains small relative to Native captured text;
- second turn still succeeds.

If `titleGenerationWhileContinuationCount == 0` or first turn still truncates, do not broaden parser grammar by guess. Add/inspect only the smallest structural evidence needed to identify the actual reset frame.

## Evidence ladder

- b50 Code/CI/Artifact/package identity: Passed.
- b50 Runtime/manual: **Partial pass** — core architecture and complete incremental turns 2/3 confirmed; new-chat turn 1 parser incomplete.
- b51 Code: Pending.
- b51 CI: Pending.
- b51 Artifact: Pending.
- b51 Runtime: Pending.
- Phase 9 Stable/Frozen: No.

## Durable boundary retained

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b51 remain diagnostic exceptions. TD-024/TD-025 are not changed by these tests.

## Non-atomic GitHub write-chain recovery point

Known baseline before b51 work: `dev/send-stream-20260829@93229404fe62c8a44eb79fa20e564abea5aec695`; exact b50 product source `837d5fe...` is immutable.

### Batch A — b50 Runtime evidence + b51 allocation

- checkpoint b50 Runtime/b51 allocation: this write;
- add `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`;
- verify branch head and file presence before product assembly.

### Batch B — non-CI b51 assembly

Create tooling-only assembly branch from post-Batch-A head. Expected product/config paths only:

- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`
- `ChatGPTClient/SettingsViewController.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `.github/workflows/ios-foundation.yml`

### Batch C — audit / publish

- compare assembly against exact post-Batch-A development head;
- require exactly four expected paths;
- inspect core Swift diff for title-generation-only continuation preservation;
- Light Guard real branch head immediately before publish;
- non-force fast-forward complete assembly to feature branch.

### Batch D — CI / Artifact

- accept only CI whose head is exact b51 product/config source;
- require Push + PR CI when both emit;
- inspect Push Artifact package identity and SHA independently;
- once Artifact emits, b51 is permanently reserved.

### Batch E — durable docs / PR

Synchronize stale `PROJECT_STATE`, `MODULE_STATUS`, `PROJECT_PROFILE`, `BUILD_TEST_INDEX`, `PROJECT_SPECIFIC_RULES` and PR #29 to b48-b51 truth as warranted. Product/config source must not change during this docs-only batch.

## Next exact action

Complete Batch A by adding exact b50 Runtime evidence, then build b51 on a tooling-only assembly branch, audit/publish non-force, continue autonomously through exact CI/Artifact/package verification, and hand the uniquely identified b51 IPA to the user for the fresh-new-chat Runtime gate.