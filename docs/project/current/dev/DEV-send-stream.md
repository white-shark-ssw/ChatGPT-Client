# DEV-send-stream

## Status

**Active — exact b49 Runtime completed. Native composer -> official Web protected Send and incremental Native text delivery are Runtime Confirmed for the diagnostic scope, but b49 captured only two short explicit text patches per turn and truncated long replies. Historical exact b40 Runtime showed the missing compact continuation form: an explicit assistant append `o/p/v` frame followed by a value-only `{v:string}` frame. Exact b50 is now Code/CI/Artifact/package verified with a minimal context-bound value-continuation parser and awaits exact-device Runtime. TD-024/TD-025 remain unchanged; b48-b50 are isolated diagnostic exceptions only.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / Native composer / Web Send engine / filtered SSE / hidden Web diagnostic`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b49 product/config source**: `20fb8f3f400200965acb868aeb8a7504b9bfb91f`; permanently reserved.
- **b49 Artifact**: `9719418761`; IPA SHA `88bd8e46b054169cb1f4338d91bb06c216edbf204b9a440a5cdc678ea6e4cd95`.
- **Exact b50 Candidate**: `DEV-send-stream-0.1.0-b50`, version/build `0.1.0 (50)`.
- **Exact b50 product/config source**: `837d5feeff05d198785f884ccf9cc4c1f71412ec`; permanently reserved after Artifact emission.
- **b50 Push CI**: Run `33270436935`, Job `99147835200` — success.
- **b50 PR CI**: Run `33270439156`, Job `99147841433` — success.
- **b50 Artifact**: `9719942650`.
- **b50 Artifact ZIP digest**: `sha256:dde656d41ea767714586a92a46740bb9bfe51531b74673e266a58aeec5dce99b`.
- **b50 IPA SHA-256**: `26431faabe0b2c836fd6c1d7aa84d31cf8811ea09d57a8ad692e127ecb42613c`.
- **b50 package identity**: `0.1.0 (50)`, Candidate b50, source marker `837d5feeff05`, Release, minimum iOS14.0, UIDeviceFamily `[1,2]`, arm64.
- **Stable/Frozen Send**: No.

## Resume / identity guard

Current-session guard revalidated from repository truth before b50 allocation/publish:

- reread branch `AGENTS.md` then `docs/project/START_HERE.md`, Development router, this checkpoint, module/product rules and `SEND_STREAM_PREFLIGHT.md`;
- user message uniquely continued `DEV-send-stream` b49 Runtime;
- exact b49 product source remained immutable after Artifact emission and branch drift from it was docs-only before b50 allocation;
- PR #29 open / mergeable / not merged;
- current `main` remained `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- `docs/project/current/dev/` contained no second Active development checkpoint;
- repository search found no prior `DEV-send-stream-0.1.0-b50` allocation;
- temporary assembly branch `assembly/dev-send-stream-b50-20260830` was based on checkpoint head `73252bce5d547bde479a6948eea51e4eb4df53b9` and is tooling-only, not Work/Candidate authority;
- assembly audit against that base showed exactly four expected product/config paths;
- core Swift diff contained only the context-bound value continuation, three structural aggregate fields, and b50 explanatory/mode text;
- Xcode diff contained only target build/Candidate `49 -> 50` changes;
- real feature branch Light Guard still matched `73252bce...` immediately before non-force fast-forward;
- complete b50 chain was published once to the real feature branch at `837d5feeff05d198785f884ccf9cc4c1f71412ec`.

b49 Runtime evidence is recorded in `docs/project/runtime-evidence/DEV-send-stream-b49-runtime.md`.

## Exact b49 Runtime result

User supplied exact b49 screenshot + diagnostics: `0.1.0 (49)`, Release, iPhone/iOS17.0, source `20fb8f3f4002`.

### Positive

1. Turn 1 Native submit -> official protected Send -> HTTP200 SSE `filtered=true` -> terminal after 406 frames.
2. Turn 2 Native submit -> official protected Send -> HTTP200 SSE `filtered=true` -> terminal after 34 frames.
3. Native received two assistant deltas on each turn and the user observed text did not appear all at once. Therefore incremental Native delivery is real for the captured fragments.
4. Web composer returned ready after both terminals; second sequential Native Send succeeded.
5. First response remained active ~94 s and survived three background intervals (~31 s, 10 s, 11 s; ~52 s total overlap) without resend, then reached terminal. This is positive Web-owned diagnostic background evidence only.

### Incomplete / rejected

Turn 1 terminal metrics:

- `removedTextPatchCount=2`
- `removedTextCharacters=18`
- `nativeDeltaCount=2`
- `nativeCharacters=18`
- `webAssistantTextCharacters=45`
- `terminal=true`

Turn 2:

- `removedTextPatchCount=2`
- `removedTextCharacters=14`
- `nativeDeltaCount=2`
- `nativeCharacters=14`
- `webAssistantTextCharacters=90`
- `terminal=true`

Both server replies were long according to direct user observation, but Native displayed only short fragments. Therefore full response interception is Runtime Rejected on b49. Existing-history virtualization remains blocked until the parser gate passes.

## Source-backed missing compact continuation

Exact prior b40 account Runtime diagnostics already recorded this sequence:

- explicit text append: event keys `o,p,v`, `operation=append`, `patchPath=/message/content/parts/0`;
- immediately following event keys only `v`, string payload, classified `value_string_patch`;
- then another structured/batch frame.

b49 recognized only the explicit first form. This directly explains the first/last-fragment behavior while hundreds of other frames passed through.

## Exact b50 implementation scope

Only the smallest parser correction justified by b40+b49 evidence was implemented:

- after an exact top-level `o:"append"`, `p:"/message/content/parts/0"`, string `v`, establish a transient assistant-text continuation context inside that one filtered response;
- while context is active, a plain object with **only** key `v` and string value is forwarded to Native and removed from the stream returned to Web;
- consecutive value-only string frames keep context active;
- any non-value-only structural frame, parse failure, terminal, close, cancel or error clears context;
- arbitrary `v:string` outside that context is not treated as assistant text;
- recursive explicit compact `o/p/v` batch matching from b49 remains;
- structural aggregate diagnostics now separately record `explicitTextPatchCount`, `contextualValueStringCount`, and `contextualValueStringCharacters` without body text;
- Settings label, Xcode build/Candidate identity and workflow Artifact identity changed to b50.

No `ConversationRepository`, `AuthSessionStore`, `RootViewController`, `ConversationFeature`, build script, attachment, history virtualization, resume behavior, TD-024/TD-025 or Stable b38 presentation code was changed. No retry/timer/watchdog/fallback was added.

## b50 Runtime gate

Fresh/new-chat diagnostic first:

1. Install exact b50 Artifact `9719942650` / IPA SHA `26431faa...2613c`.
2. Clear diagnostics.
3. Open `Native 输入 / Web Send（b50诊断）`.
4. Send one genuinely long-answer prompt from Native only.
5. Verify Native assistant text grows continuously through the body rather than only first/last fragments.
6. Wait for terminal, then send a second Native turn from the same Native composer.
7. Export diagnostics after the second terminal.

Required evidence:

- both official Sends HTTP200 SSE;
- `contextualValueStringCount > 0` on the long response;
- explicit + contextual captured character total is long-answer scale, not tens of characters;
- Native output is not truncated in the middle;
- Web composer returns ready and second Send succeeds;
- Web assistant DOM text remains small relative to Native captured response;
- no duplicate Send or stream-error event.

Passing b50 still does not itself accept production hidden/shadow Web or existing long-chat viability. Only after this parser gate passes may a separate existing-conversation **data-layer history virtualization before React** experiment be considered.

## Evidence ladder

- b49 Code/CI/Artifact/package identity: Passed.
- b49 Runtime/manual: Completed — partial incremental streaming confirmed; complete-response parser rejected.
- b50 Code written: **Yes**.
- b50 CI: **Passed** (Push + PR).
- b50 Artifact produced: **Yes** (`9719942650`).
- b50 package identity: **Verified**.
- b50 Runtime/manual: **Pending**.
- Phase 9 Stable/Frozen: **No**.

## Durable boundary retained

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b50 are diagnostic exceptions only. Do not change TD-024/TD-025 or describe hidden Web as accepted production architecture from these experiments.

## Non-atomic GitHub write-chain recovery point

### Batch A — b49 Runtime + b50 allocation

- b49 Runtime evidence: complete (`fbc4a74894c4d98c5c64f203bc3d8c1320f22c77`).
- checkpoint allocation to b50: complete (`73252bce5d547bde479a6948eea51e4eb4df53b9`).

### Batch B — non-CI b50 assembly

Complete on tooling branch; exact four expected paths only.

### Batch C — audit / publish

Complete. Assembly final `837d5feeff05d198785f884ccf9cc4c1f71412ec`; non-force feature-branch fast-forward complete after Light Guard.

### Batch D — CI / Artifact

Complete. Push + PR CI success, Push Artifact `9719942650`, ZIP/IPA hashes and package identity independently verified. b50 is permanently reserved.

### Batch E — durable docs / PR

In progress this turn. Recover stale `PROJECT_STATE`, `MODULE_STATUS`, `PROJECT_PROFILE`, `BUILD_TEST_INDEX`, roadmap/rules text where warranted, and PR #29 to b49/b50 truth using only current blobs. Do not replay the prior stale-SHA failed `PROJECT_STATE` write blindly.

## Next exact action

Finish Batch E docs/PR synchronization without touching exact b50 product/config source, then hand exact b50 IPA to the user for the Runtime gate above. On returned diagnostics, accept b50 only if long-response contextual value continuations produce complete Native text; otherwise derive the next parser correction only from new structural evidence.