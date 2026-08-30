# DEV-send-stream

## Status

**Active — exact b64 has now passed the tested verified-composer / protected-Send / complete-looking reasoning-final / exact-parent GitHub tool-detail lifecycle, including successful Native expand/collapse and visible input/output. Runtime rejected only the current detail presentation shape: b64 dumps the paired `message.content` as one outer JSON string, so nested `parts` / `text` strings stay escaped and a large output is shown all at once. b65 is justified as a presentation-only correction: nested `工具输入` / `工具输出` disclosures plus outer-content decoding/readable formatting. Stable/Frozen Send remains No. PR #29 stays evidence-only / open / mergeable / unmerged. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Other Active development checkpoints: none at latest guard
- Current actual `main`: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Stable native predecessor: b38
- Exact current Runtime-tested Candidate: `DEV-send-stream-0.1.0-b64`
- Exact b64 product/config source: `6ce1fbd242c903d85930b0e8a8d2aadc29669cc1`
- b64 Push Run / Job: `33325292890 / 99294233652` — success
- b64 PR Run / Job: `33325295457 / 99294240336` — success
- b64 Artifact: `9736051023`
- b64 ZIP SHA-256: `5a4ba89298f6bdd467ed66294133b0a38bae58f30c90d3b104d1ea3954db856a`
- b64 IPA SHA-256: `49b5e8021ca78da3e87f67721682edf306b300995be3566a391a6c35d573c6fc`
- b64 package: Release / `0.1.0 (64)` / source marker `6ce1fbd242c9` / iOS14 / `[1,2]` / arm64
- b39-b64 emitted identities: permanently reserved
- Next unique Candidate after current guard: `DEV-send-stream-0.1.0-b65` / `0.1.0 (65)`; repository search found no existing b65 identity

## Exact b64 Runtime — Partial / formatting defect only

User export: `ChatGPTClient-Diagnostics-20260830-174329.json`.

Package identity matched exact b64: Release / build64 / Candidate b64 / source `6ce1fbd242c9` / iPhone / iOS17.0.

### Send / reasoning / final

Observed path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 text/event-stream -> terminal`.

Terminal metrics:

- frameCount `344`, terminal `true`;
- exact reasoning-end `1`, fallback false;
- Native reasoning `27 deltas / 440 chars`;
- Native final answer `215 deltas / 6716 chars`;
- Native total `242 deltas / 7156 chars`;
- thinking preambles `3 / 33 chars`;
- reasoning-active signals `7`;
- Native thinking presentations `4`;
- service/native reasoning segment breaks `2/2`;
- inactive value strings `0`;
- root-nonexact text patches `0`.

The user reported no apparent truncation in the tested round.

### Tool lifecycle / detail

- invocation identities `30`;
- results `35`;
- parent present `35`;
- exact parent matches `30`;
- unmatched `5`;
- missing `0`;
- Native tool presentations/completion updates `30/30`;
- paired presentations `30`;
- Native detail-available rows `26`;
- terminal-time detail expansion metric `7`;
- complete exported interaction contains multiple successful expand/collapse events.

Unmatched results were not force-paired. Exact `parent_id` remains the row authority.

User-visible b64 result: tool rows reached `已完成`; GitHub rows with authorized paired detail could be opened/closed; `工具输入` and `工具输出` were visible. The rejected part is only formatting/density of the output.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b64-runtime.md`.

## Evidence-backed b65 correction

Current b64 source proves the presentation defect mechanically:

- Web bridge uses `JSON.stringify(content)` for the exact paired result `message.content`;
- Native `renderToolActivity()` calls `prettyJSONString()` on that outer JSON string;
- nested strings inside `parts` / `text` therefore remain escaped (`\"`, `\\`, escaped newlines) and the whole nested body is dumped as soon as the row is opened.

b65 may change only the detail presentation layer:

1. preserve b64 composer identity, protected Send, SSE filtering/text grammar, reasoning-final split, exact `reasoning_ended`, transient invocation map, exact result `parent_id` pairing, GitHub-only detail authorization and diagnostics privacy rules;
2. after a tool row opens, render `工具输入` and `工具输出` as separate disclosure links, both collapsed by default;
3. opening `工具输入` displays the already-authorized connector payload as readable pretty JSON;
4. opening `工具输出` parses the already-authorized outer `message.content` JSON and formats known/generic structures recursively enough to remove the second JSON-string escaping layer: dictionaries/arrays show hierarchy/counts; string values display as their actual string text rather than JSON-escaped literals; if a string itself is valid JSON, it may be pretty-printed as decoded JSON;
5. do not add an arbitrary character truncation merely to reduce density; hierarchy/collapse is the evidence-backed fix;
6. do not expose `assistant:thoughts`, raw service IDs, unmatched results or unrelated connector families;
7. raw tool input/output values remain response-local presentation state and never enter exported diagnostics;
8. add no retry, timer, polling, watchdog, compatibility shim, second response owner or production repository mutation.

## Batch recovery point — b65 product/config assembly

Known state before product mutation:

- feature branch currently contains exact b64 product source plus docs-only b64 Runtime evidence/checkpoint commits;
- exact b64 product source remains immutable `6ce1fbd242c903d85930b0e8a8d2aadc29669cc1`;
- b64 Artifact `9736051023` is valid and b64 is permanently reserved;
- `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- PR #29 remains open / mergeable / unmerged;
- only `DEV-send-stream` is Active;
- b65 identity search returned no existing `DEV-send-stream-0.1.0-b65`.

Pending coherent batches:

1. **Product/config batch:** fetch the new checkpoint head/tree. Create one detached Git tree/commit containing exactly `NativeWebSendEngineProbe.swift` presentation-only b65 changes, Xcode build/Candidate `65/b65`, and workflow Artifact identity b65. Audit the diff, then move `dev/send-stream-20260829` exactly once to the complete product/config commit. No intermediate b65-code/b64-identity branch state.
2. **Validation batch:** verify exact product diff, Push + PR CI, Artifact, ZIP/IPA SHA and package Info.plist/arm64 identity.
3. **Documentation batch:** record b64 Runtime + exact b65 evidence in `BUILD_TEST_INDEX`, `PROJECT_STATE`, `MODULE_STATUS`, `PROJECT_PROFILE`, `DEVELOPMENT_PLAN`, `PROJECT_SPECIFIC_RULES`, checkpoint and PR #29. Later docs-only commits must not redefine the exact b65 product source.

Recovery rule: after interruption, re-read this checkpoint plus actual branch/PR/head and perform only missing deterministic writes. Do not reuse b64 or any emitted b65 identity.

## Next exact action

Fetch the new checkpoint head/tree and current b64 Swift/Xcode/workflow blobs, assemble exact b65 as one detached product/config commit, audit the diff, move the formal feature branch once, then continue autonomously through CI/Artifact/package verification. The next normal human gate is exact b65 iPhone/iOS17 Runtime focused on nested tool input/output disclosure and readable output formatting.
