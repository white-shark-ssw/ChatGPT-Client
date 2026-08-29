# DEV-send-stream

## Status

**Active — exact b49 Runtime completed. Native composer -> official Web protected Send and incremental Native text delivery are Runtime Confirmed for the diagnostic scope, but b49 captures only two short explicit text patches per turn and truncates long replies. Historical exact b40 Runtime already shows the missing compact continuation form: an explicit assistant append `o/p/v` frame followed by a value-only `{v:string}` frame. b50 is allocated for the smallest context-bound value-continuation correction. TD-024/TD-025 remain unchanged; this is still an isolated diagnostic exception.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / Native composer / Web Send engine / filtered SSE / hidden Web diagnostic`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b49 product/config source**: `20fb8f3f400200965acb868aeb8a7504b9bfb91f`; permanently reserved.
- **b49 Artifact**: `9719418761`; IPA SHA `88bd8e46b054169cb1f4338d91bb06c216edbf204b9a440a5cdc678ea6e4cd95`.
- **Allocated next Candidate**: `DEV-send-stream-0.1.0-b50`, version/build `0.1.0 (50)`.
- **Stable/Frozen Send**: No.

## Resume / identity guard

Current-session guard revalidated from repository truth before b50 allocation:

- reread branch `AGENTS.md` then `docs/project/START_HERE.md`, Development router, this checkpoint, module/product rules and `SEND_STREAM_PREFLIGHT.md`;
- user message uniquely continues `DEV-send-stream` b49 Runtime;
- real feature branch before b49 Runtime evidence write was `39a96db36c23f151d0ef7bb01a52f392108b1d0e` and differed from exact b49 product source only by this checkpoint docs file;
- PR #29 open / mergeable / not merged;
- current `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- `docs/project/current/dev/` contains no second Active development checkpoint;
- repository search found no prior `DEV-send-stream-0.1.0-b50` allocation;
- exact b49 product source remains immutable after Artifact emission.

b49 Runtime evidence file was added in docs-only commit `fbc4a74894c4d98c5c64f203bc3d8c1320f22c77`.

## Exact b49 Runtime result

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b49-runtime.md`.

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

Both server replies were long according to the user's direct observation, but Native displayed only short fragments. Therefore full response interception is Runtime Rejected on b49. Do not advance to existing-history virtualization yet.

## Source-backed missing compact continuation

Exact prior b40 account Runtime diagnostics already recorded this sequence:

- explicit text append: event keys `o,p,v`, `operation=append`, `patchPath=/message/content/parts/0`;
- immediately following event keys only `v`, string payload, classified `value_string_patch`;
- then another structured/batch frame.

b49 only recognizes the explicit first form. This explains the observed short first/last fragments while hundreds of other frames pass through.

## b50 exact scope

Make only the smallest parser correction justified by b40+b49 evidence:

- after an explicit `o:"append"`, `p:"/message/content/parts/0"`, string `v`, establish a transient **assistant-text continuation context** inside that one filtered response;
- while that context is active, if the next parsed payload is a plain object with **only** key `v` and `typeof v === "string"`, forward that string to Native and remove that frame from the stream returned to Web;
- keep the continuation context for consecutive value-only string frames;
- clear the context on any non-value-only structural frame, explicit new operation/path, terminal, stream close or error;
- do not treat arbitrary `v:string` globally as assistant text;
- retain recursive explicit `o/p/v` batch matching from b49;
- add aggregate structural counts for explicit text patches vs contextual value-only text frames, never body text;
- update Settings/Xcode/workflow identity to b50 only.

Do not modify `ConversationRepository`, `AuthSessionStore`, `RootViewController`, `ConversationFeature`, build scripts, attachments, history virtualization, resume code, TD-024/TD-025, or Stable b38 presentation. No retry/timer/watchdog/fallback.

## b50 Runtime gate

Fresh/new-chat diagnostic first:

1. Send one genuinely long-answer prompt from Native only.
2. Verify Native assistant text grows continuously through the body rather than only first/last fragments.
3. Wait to terminal and send a second Native turn.
4. Export diagnostics after second terminal.

Required evidence:

- both official Sends HTTP200 SSE;
- explicit + contextual captured character total is large enough to match the visibly long response class, not tens of characters;
- contextual value-only frame count `> 0` on the long response;
- Native output is not truncated in the middle;
- Web composer returns ready and second Send succeeds;
- Web assistant DOM text remains small relative to the Native captured response.

Passing b50 still does not itself accept production hidden/shadow Web or existing long-chat viability. Only then may a later existing-conversation **data-layer history virtualization before React** experiment be considered.

## Evidence ladder

- b49 Code/CI/Artifact/package identity: passed.
- b49 Runtime/manual: completed — partial incremental streaming confirmed; complete-response parser rejected.
- b50 Code: Pending.
- b50 CI: Pending.
- b50 Artifact: Pending.
- b50 Runtime: Pending.
- Phase 9 Stable/Frozen: No.

## Durable boundary retained

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b50 are diagnostic exceptions only. Do not change TD-024/TD-025 or describe hidden Web as accepted production architecture from these experiments.

## Non-atomic GitHub write-chain recovery point

Known baseline after b49 Runtime evidence: feature branch includes docs-only b49 evidence on top of exact product source `20fb8f3...`; product/config source must not be rewritten under b49.

### Batch A — b49 Runtime + b50 allocation

- b49 Runtime evidence file: complete (`fbc4a748...`).
- checkpoint allocation to b50: this write.

### Batch B — non-CI b50 assembly

Create a temporary assembly branch from the post-checkpoint head. Expected product/config changes only:

- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`
- `ChatGPTClient/SettingsViewController.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `.github/workflows/ios-foundation.yml`

### Batch C — audit / publish

- compare assembly against real development head;
- require exactly those four expected paths;
- Light Guard real branch head immediately before publish;
- non-force fast-forward complete b50 chain onto `dev/send-stream-20260829`.

### Batch D — CI / Artifact

- accept only complete b50 exact source CI;
- require Push + PR CI when emitted;
- inspect Push Artifact package identity/hashes independently;
- once Artifact emits, b50 becomes permanently reserved.

### Batch E — durable docs / PR

Recover the previously stale `PROJECT_STATE`, `MODULE_STATUS`, `PROJECT_PROFILE`, `BUILD_TEST_INDEX`, roadmap/rules text where warranted, and PR #29 to b49/b50 truth. Perform only current-blob deterministic writes; do not replay the prior failed `PROJECT_STATE` write blindly.

## Next exact action

Create the non-CI b50 assembly branch from the current post-checkpoint head, implement only context-bound value-only continuation plus b50 identity files, audit the exact four-file diff, publish non-force, then autonomously continue through CI/package verification to the exact-device b50 Runtime gate.