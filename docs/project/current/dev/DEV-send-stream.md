# DEV-send-stream

## Status

**Active — exact b61 Runtime is Partial: the tested parent-paired Native tool lifecycle passed (14/14 result parent matches and 14 Native completion updates) and the successful turn retained complete thinking/reasoning/final presentation, but an independent cold/new-page Send-entry defect was captured where generic `textarea` was treated as ready, `submitResult=submitted` was emitted, and no official protected Send request followed. Exact b62 removes only that false-ready generic-textarea authority. b62 is now Code / Push CI / PR CI / Artifact / package Passed and awaits focused iPhone/iOS17 Runtime. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged; PR #29 stays evidence-only / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Other Active development checkpoints: none at last verified guard
- Stable native predecessor: b38
- Stable/Frozen Send: No

## Exact b61 Runtime conclusion

Exact b61 identity:

- Candidate `DEV-send-stream-0.1.0-b61`
- Version/build `0.1.0 (61)`
- Source `2386872af03e0684eee8deca87f636dc265114ec`
- Artifact `9732514781`
- IPA SHA `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`

Two user-provided exports were classified separately.

### Attempt 1 — Send-entry defect

`ChatGPTClient-Diagnostics-20260830-134827.json` plus direct screenshot/observation:

- `new_or_other` page;
- composer `ready=true`, strategy `textarea`;
- Native `nativeSubmit` recorded;
- submit path still saw strategy `textarea`;
- `submitResult=submitted` recorded;
- no `sendObserved`, `sendResponse`, thinking presentation or stream metrics followed;
- user observed no `正在思考` and no answer activity.

Classification: **Runtime defect — generic textarea false-ready / false-submitted.** This occurs before official protected Send and is not an SSE/model-generation stall.

### Attempt 2 — successful tool-active turn

After clearing diagnostics and force-quitting/relaunching, the official composer reached `prompt_textarea` and the turn completed:

- HTTP200 SSE / terminal;
- frameCount 135;
- Native reasoning `10 / 251 chars`;
- final `68 / 2363 chars`;
- preambles `2 / 11 chars`;
- service/Native reasoning segment breaks `1/1`;
- exact reasoning-end 1; fallback false;
- thinking presentations 3;
- invocation identities/results `14/14`;
- parent present/matched/unmatched/missing `14/14/0/0`;
- paired presentations 14;
- Native tool presentations/completion updates `14/14`.

Direct user result: reasoning opening appeared complete, tool rows showed `调用中` and `已完成`, final answer looked complete.

Classification: **Runtime pass for the tested parent-paired tool lifecycle and successful response-presentation scope.** Overall b61 remains **Runtime Partial** because of Attempt 1.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b61-runtime.md`.

## Exact b62 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b62`
- Version/build: `0.1.0 (62)`
- Exact product/config source: `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`
- Product tree: `d3432dfe2e32cddcfac7a5a56d7880772dc6989d`
- Product parent / prior docs head: `af8d3aa5f64b58a62222c4f8c24d27920dcfbbbf`
- Push Run / Job: `33316398081 / 99270535435` — success
- PR Run / Job: `33316399402 / 99270539763` — success
- Artifact: `9733577825`
- Artifact name: `ChatGPTClient-DEV-send-stream-0.1.0-b62`
- ZIP digest / independent SHA: `sha256:d53ddb88c5d2092294592416e10e5a0a752cb7afb0bbe0a39c2c137d021082d0`
- IPA SHA / sidecar / independent verification: `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`
- Package: Release / `0.1.0 (62)` / Candidate b62 / source marker `e1b44f7ab6c4` / minimum iOS14 / UIDeviceFamily `[1,2]` / Mach-O arm64
- b62 is permanently reserved after Artifact emission.

Evidence ladder: **Code written / Push CI passed / PR CI passed / Artifact produced / package identity independently verified; Runtime/manual pending; Stable/Frozen No.**

## b62 bounded behavior

1. Remove only the generic `textarea:not([disabled])` composer fallback that produced exact b61 false-ready evidence.
2. Composer authority remains `#prompt-textarea` or explicit `[contenteditable="true"][role="textbox"]` only.
3. No retry, timer, polling, watchdog or speculative fallback is added.
4. b61 protected Send, text patch grammar, thinking/reasoning split, exact `reasoning_ended`, parent-paired tool lifecycle and bounded detail-shape diagnostics remain unchanged.
5. Raw tool request/result bodies, connector payload values, service IDs and `assistant:thoughts` remain non-presentational.
6. Production `ConversationRepository`, auth ownership, resume transport, Stable b38 modules and attachments remain untouched.

## Runtime acceptance gate for b62

The b61 false-ready state is intermittent and **does not need to reproduce** for b62 to be evaluated.

Required normal-path evidence:

- after a cold/force-quit launch, Native Send must remain unavailable while the probe has no evidenced official composer; a transient unrelated generic textarea must never be reported as an accepted composer strategy;
- once Send becomes available and the user sends a prompt, the run must show a real protected-Send lifecycle (`sendObserved`, HTTP200 SSE where service succeeds) rather than only `submitResult=submitted`;
- `正在思考`, reasoning, tool rows and final answer must retain the b61 accepted behavior; tool-active turns should show matched visible entries moving `调用中 -> 已完成` without obvious duplicates/missing rows;
- terminal successful text should have no obvious opening/middle truncation.

Special-case evidence if it naturally appears:

- if startup sits for a while before the official composer is ready, the disabled/not-ready state is **expected b62 behavior**, not failure;
- if any run again reports a submitted action but no `sendObserved`, export diagnostics immediately; that would reject the current narrow fix even if other runs pass;
- absence of that rare reproduction is not by itself proof that the race is impossible, so b62 can be accepted only for the tested gate, not as a universal Web-page invariant.

## Recovery point

Completed this cycle:

1. b61 two-run Runtime classified and persisted;
2. source-level false-ready cause matched exact generic-textarea fallback;
3. fresh uniqueness/conflict check permitted b62;
4. b62 source/build/workflow identity assembled in one product commit and feature ref moved once;
5. exact product/config source `e1b44f7a...` differs from b61 only in Candidate metadata plus removal of generic textarea fallback / diagnostic wording;
6. Push + PR CI succeeded;
7. Artifact `9733577825` downloaded; ZIP digest, IPA sidecar, built Info.plist and Mach-O independently verified;
8. `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md`, `PROJECT_SPECIFIC_RULES.md`, `BUILD_TEST_INDEX.md` and b61 Runtime evidence synchronized through b62 Artifact;
9. PR #29 title/body synchronized to `b62 verified-composer Send-entry Runtime gate`; PR remains open / mergeable / unmerged;
10. later docs-only commits do not redefine exact b62 product/config source.

## Next exact action

Hand exact b62 IPA to the user. Preferred focused test: force-quit the app, reopen `Native 输入 / Web Send`, watch the Send button during initial page setup, then run one repository/GitHub tool-active question after Send becomes enabled. Do not wait indefinitely trying to reproduce b61's rare generic-textarea race. After terminal, export diagnostics. If desired, repeat one additional cold launch as a lightweight confidence check. Classify b62 from actual observed composer strategy / protected-Send lifecycle / response/tool completeness; do not allocate b63 by guess.
