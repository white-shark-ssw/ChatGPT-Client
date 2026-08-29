# DEV-send-stream

## Status

**Active — exact b48 Runtime completed; exact b49 compact `o/p/v` correction is Code/CI/Artifact/package-identity complete and waiting for exact-device Runtime. Native composer -> official Web protected Send already succeeded for two sequential b48 turns; b49 now tests whether assistant text is intercepted before Web React and rendered incrementally by Native. TD-024/TD-025 remain unchanged; this is still an isolated diagnostic exception.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / Native composer / Web Send engine / filtered SSE / hidden Web diagnostic`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b48 product/config source**: `6ccba03cefaa32a1186f1f468c3e696ed9457699`; permanently reserved.
- **b48 Artifact**: `9718885751`; IPA SHA `c1f2f6a4e750af8abc7438e289f709cdf23c564f06ce2118b1c9b74f2d8ed850`.
- **Exact b49 product/config source**: `20fb8f3f400200965acb868aeb8a7504b9bfb91f`; permanently reserved after Artifact emission.
- **Candidate**: `DEV-send-stream-0.1.0-b49`, `0.1.0 (49)`.
- **Push CI**: Run `33268560803`, Job `99142837459` — success.
- **PR CI**: Run `33268562114`, Job `99142840873` — success.
- **Runtime Artifact**: `9719418761`.
- **Artifact ZIP digest**: `sha256:1b59bd8c13da116b3221acd29a4ad52de9c3f841c09f262d625e60fa6fb3aaec`.
- **IPA SHA-256**: `88bd8e46b054169cb1f4338d91bb06c216edbf204b9a440a5cdc678ea6e4cd95`.
- **Package identity**: independently verified `0.1.0 (49)` / Candidate b49 / `DiagnosticsSourceCommit=20fb8f3f4002` / `DiagnosticsBuildConfiguration=Release` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64.
- **Stable/Frozen Send**: No.

## Resume / conflict guard

Current-session guard before b49:

- reread current branch `AGENTS.md` then `docs/project/START_HERE.md`;
- uniquely resumed `DEV-send-stream` from the user's exact b48 Runtime result;
- PR #29 remained open / mergeable / not merged;
- `main` remained `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- no second Active dev checkpoint existed;
- b48 product source -> pre-b49 docs head had docs-only changes;
- b49 identity was unallocated.

Assembly branch `assembly/dev-send-stream-b49-20260830` was created from checkpoint head `179c16a534485c0ecfc1b8ab0c167a093d76906e`. Audit against that baseline showed exactly four expected files and no product-owner spillover:

- `.github/workflows/ios-foundation.yml`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`
- `ChatGPTClient/SettingsViewController.swift`

Immediately before publish, the real feature branch still exactly matched `179c16a...`; non-force fast-forward to complete assembly head `20fb8f3...` succeeded.

## b48 exact Runtime result

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b48-runtime.md`.

User supplied exact b48 screenshot + diagnostics (`0.1.0 (48)`, source `6ccba03cefaa`, Release, iPhone/iOS17.0).

Accepted positive facts:

1. Native composer used the real Web `#prompt-textarea` state and submitted without user interaction with Web composer.
2. First official protected Send returned HTTP200 `text/event-stream`, wrapper `filtered=true`.
3. First stream reached `[DONE]` after 268 frames and Web composer returned ready.
4. Second Native-composer submit in the same new authoritative conversation also returned HTTP200 SSE.
5. User later opened the new conversation in ordinary Native list/detail and confirmed both assistant replies existed server-side.

First-turn negative metrics:

- `removedTextPatchCount=0`
- `removedTextCharacters=0`
- `nativeDeltaCount=0`
- `nativeCharacters=0`
- `webAssistantTextCharacters=5864`
- `webMessageNodes=2`
- `webElementCount=951`
- `terminal=true`

Thus b48 proved Native composer + two-turn Web protected Send continuity, but did **not** prove Native assistant streaming or Web-render reduction.

## Deterministic b48 defect / b49 correction

b48 matched nonexistent verbose patch fields `op/path/value`. Exact b40 current protocol source already evidenced compact fields:

- operation `o`
- path `p`
- value `v`
- batch envelope `o == "patch"`, `v` array with compact entries.

b49 makes only this evidence-backed correction:

`node.o === "append" && node.p === "/message/content/parts/0" && typeof node.v === "string"`

Recursive traversal is retained so compact entries nested in batch `v:[...]` are caught. No alternate speculative grammar was added.

Everything else remains b48 scope: same Native composer bridge, official Web owns protected Send/challenges, default persistent WebKit store, full-size hidden-under-Native Web layout, one-reader/no-clone stream transform, structural privacy-safe diagnostics, no production repository mutation, no retry/timer/watchdog/fallback.

## b49 Runtime gate

On exact iPhone/iOS17:

1. Clear diagnostics and open `Native 输入 / Web Send（b49诊断）`.
2. In a fresh/new-chat probe, send one long-answer prompt only from the Native composer.
3. Verify assistant text visibly appears **incrementally** in the Native output area.
4. Wait to terminal; then send a second Native-composer turn in the same probe session.
5. Export diagnostics after the second turn reaches terminal where practical.

Expected evidence:

- both Send responses HTTP200 SSE;
- `removedTextPatchCount > 0`;
- `removedTextCharacters > 0`;
- `nativeDeltaCount > 0`;
- `nativeCharacters > 0`;
- `webAssistantTextCharacters` near zero/small relative to Native answer, not thousands;
- terminal true and Web composer ready again;
- second sequential Native Send succeeds.

Passing b49 still does **not** prove existing long-conversation viability. Existing-conversation history/data virtualization before React is a later separate experiment only after this gate passes.

## Evidence ladder

- b48 Code/CI/Artifact/package identity: passed.
- b48 Runtime/manual: completed; Native composer/two-turn Send positive, Native streaming/filter negative due deterministic parser defect.
- b49 Code written: Yes.
- b49 CI: Passed.
- b49 Artifact produced: Yes.
- b49 package identity: Verified.
- b49 Runtime/manual: Pending.
- Phase 9 Stable/Frozen: No.

## Durable boundary retained

Do not edit TD-024/TD-025 merely because b48/b49 diagnostic exceptions exist. Still no production acceptance of hidden/shadow protected Web Send, challenge/proof replay, browser-token harvesting, DOM answer scraping, or production `ConversationRepository` ownership from this probe.

Do not expand b49 into attachments, existing-chat history virtualization, resume-header experiments or production stream ownership before exact b49 Runtime.

## Non-atomic recovery state

- Batch A b48 Runtime evidence + b49 allocation: complete.
- Batch B non-CI b49 assembly: complete.
- Batch C four-file audit + Light Guard + non-force publish: complete.
- Batch D Push/PR CI + Push Artifact + package inspection: complete.
- Batch E durable docs/PR synchronization: in progress in this docs-only batch; product source must remain exact `20fb8f3...`.

## Next exact action

Finish docs-only b48/b49 evidence synchronization without modifying product/config source, then hand exact Artifact `9719418761` IPA to the user. Next human-only gate is exact-device b49 Runtime using the procedure above. Do not rebuild b49; any later product-code correction requires b50+.