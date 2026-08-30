# DEV-send-stream

## Status

**Active — exact b64 Runtime passed the tested verified-composer / protected-Send / complete-looking reasoning-final / exact-parent GitHub tool-detail lifecycle, but rejected b64 detail formatting/density only. Exact b65 is now Code/CI/Artifact/package verified and is the current human Runtime gate for nested `工具输入` / `工具输出` disclosures and readable decoded output. Stable/Frozen Send remains No. PR #29 remains evidence-only / open / mergeable / unmerged. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Other Active development checkpoints: none at latest guard
- Current actual `main`: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Stable native predecessor: b38
- Exact latest Runtime-tested Candidate: `DEV-send-stream-0.1.0-b64`
- Exact current Artifact Candidate: `DEV-send-stream-0.1.0-b65`
- Exact b65 product/config source: `44138db766d00e62cfda7f20182f6d20f1ec3352`
- Exact b65 product tree: `fb02dfa7512e9c8428c4b0e9b7184a56d602f688`
- b65 Push Run / Job: `33328232044 / 99302071335` — success
- b65 PR Run / Job: `33328233842 / 99302076369` — success
- b65 Push Artifact: `9736876465`
- b65 PR Artifact: `9736874445`
- b65 Push Artifact ZIP SHA-256: `d9a52ecb0cd7d5131e22fc399bc5db0d573a9de3e5d80838f3a8d2b3164ceb7a`
- b65 IPA SHA-256: `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`
- b65 package: Release / `0.1.0 (65)` / Candidate `DEV-send-stream-0.1.0-b65` / source marker `44138db766d0` / iOS14 / `[1,2]` / arm64
- b39-b65 emitted identities: permanently reserved
- Do not allocate b66 before exact b65 Runtime yields a concrete defect or next evidence need.

## Exact b64 Runtime — Partial / formatting defect only

User export: `ChatGPTClient-Diagnostics-20260830-174329.json`.

Package identity matched exact b64: Release / build64 / Candidate b64 / source `6ce1fbd242c9` / iPhone / iOS17.0.

Observed path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 text/event-stream -> terminal`.

Terminal evidence:

- frameCount `344`, terminal `true`;
- exact reasoning-end `1`, fallback false;
- Native reasoning `27 deltas / 440 chars`;
- Native final answer `215 deltas / 6716 chars`;
- Native total `242 deltas / 7156 chars`;
- thinking preambles `3 / 33 chars`;
- reasoning-active signals `7`;
- service/native reasoning segment breaks `2/2`;
- invocation identities `30`, results `35`;
- parent present `35`, exact parent matches `30`, unmatched `5`, missing `0`;
- Native tool presentations/completion updates `30/30`;
- Native detail-available rows `26`;
- terminal-time detail expansion metric `7`, with multiple successful expand/collapse events in the exported run.

The user reported no apparent truncation. Exact-parent tool association and input/output availability worked. Runtime rejected only b64's presentation shape: opening one tool row immediately dumped both details and `message.content` remained a pretty-printed outer JSON object whose nested strings still showed escaped quotes/backslashes/newlines.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b64-runtime.md`.

## Exact b65 product correction

b65 changes only Native detail presentation on top of b64's already-authorized GitHub exact-parent input/output mapping:

1. tool row remains the first disclosure;
2. after the row opens, `工具输入` and `工具输出` are independent second-level disclosure links and both start collapsed;
3. `工具输入` continues to show the already-authorized connector payload as pretty JSON;
4. `工具输出` decodes b64's outer `message.content` JSON and presents dictionaries/arrays hierarchically; string values are shown as actual string text instead of JSON-escaped literals; string values that themselves contain a complete JSON object/array may be decoded one additional structural layer;
5. no arbitrary character truncation was added; collapse/hierarchy is the density control;
6. b64 composer selection, protected Send, SSE filtering/text grammar, reasoning/final split, exact `reasoning_ended`, transient invocation identity, exact result `parent_id` pairing and GitHub-only detail authorization are unchanged;
7. raw tool values remain response-local presentation state and are not exported to diagnostics; `assistant:thoughts`, raw IDs, unmatched results and unrelated connector families remain non-presentational;
8. no retry, timer, polling, watchdog, fallback, compatibility shim, duplicate owner or production repository mutation was added.

Detached parent→b65 diff was audited before moving the formal branch: exactly three product/config files changed — `.github/workflows/ios-foundation.yml`, `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`. The formal branch then fast-forwarded once to exact source `44138db766d00e62cfda7f20182f6d20f1ec3352`.

## b65 validation evidence

- Push CI `33328232044 / 99302071335`: completed success.
- PR CI `33328233842 / 99302076369`: completed success.
- Push Artifact `9736876465`: name `ChatGPTClient-DEV-send-stream-0.1.0-b65`, head exact `44138db766d00e62cfda7f20182f6d20f1ec3352`, digest `sha256:d9a52ecb0cd7d5131e22fc399bc5db0d573a9de3e5d80838f3a8d2b3164ceb7a`.
- PR Artifact `9736874445`: same Candidate/head; independent PR-container digest differs as expected.
- Downloaded Push Artifact ZIP independently hashed to the exact GitHub digest.
- ZIP contains `ChatGPTClient-0.1.0-b65-dev-send-stream.ipa` plus matching sidecar.
- Sidecar and independent IPA hash both equal `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`.
- Built `Info.plist`: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=65`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b65`, `DiagnosticsSourceCommit=44138db766d0`, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`.
- Executable: Mach-O 64-bit arm64.

Evidence ladder: **Code written / diff audited / CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**

## Recovery point

Exact product/config authority is permanently `44138db766d00e62cfda7f20182f6d20f1ec3352`. Any later docs-only commits do not redefine that source. Because a valid b65 Artifact exists, b65 is permanently reserved; any product-code correction must use b66+ and only after exact b65 Runtime evidence.

Documentation/metadata batch is complete through this handoff:

- `BUILD_TEST_INDEX.md` preserves exact historical Candidate evidence and records b63 Runtime mapping, b64 Runtime partial-pass and b65 exact CI/Artifact/package identity;
- `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md` and `PROJECT_SPECIFIC_RULES.md` are synchronized through b64 Runtime / b65 Artifact;
- PR #29 title/body is synchronized to the b65 structured tool-detail Runtime gate and remains open / mergeable / unmerged;
- all commits after exact product source `44138db766d00e62cfda7f20182f6d20f1ec3352` are documentation-only and do not redefine b65 package authority.

## Next exact action

Hand the exact b65 IPA to the user. On the primary iPhone/iOS17 device, clear diagnostics, open `Native 输入 / Web Send`, run one GitHub/repository request that naturally creates multiple tool rows, and verify:

- real `sendObserved` -> HTTP200 SSE -> terminal still occurs;
- reasoning/final still appear complete;
- completed exact-parent GitHub tool rows can expand/collapse;
- opening one row initially shows only collapsed `工具输入` and `工具输出` children;
- each child can expand/collapse independently;
- output is readable hierarchical text without b64's second-layer escaped `\"` / `\\` wall;
- no tool/result body is unexpectedly lost or truncated.

Export diagnostics after terminal. If this focused b65 Runtime passes, close this presentation defect without allocating b66. Keep PR #29 open/unmerged until the broader `DEV-send-stream` acceptance boundary is explicitly resolved.