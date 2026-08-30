# DEV-send-stream

## Status

**Active — exact b63 is now the current diagnostic Candidate and has passed code-diff audit, Push CI, PR CI, Artifact production and independent package-identity verification. Runtime/manual/real-device is still Pending. b63 is diagnostic-only: it preserves exact b62 Send/text/reasoning/tool behavior and adds only bounded `connector_tool_payload` JSON top-level structure fingerprints plus aggregate `inline_cot_expandable_content.source_message_ids` association counts. No raw IDs/values/bodies are exported and no expandable body is presented yet. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged; PR #29 remains evidence-only / open / unmerged. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Other Active development checkpoints: none at latest guard
- Current actual `main`: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Stable native predecessor: b38
- Current exact diagnostic Candidate: `DEV-send-stream-0.1.0-b63`
- Version / build: `0.1.0 (63)`
- Exact b63 product/config source: `0c2e2b870e51c363c7734182d49618c438839cc2`
- Exact b63 product tree: `cae7f27e2800fe48f8d492bfd364c91755935c67`
- Push Run / Job: `33321982009 / 99285436158` — success
- PR Run / Job: `33321983658 / 99285440962` — success
- Artifact: `9735145598`
- Artifact name: `ChatGPTClient-DEV-send-stream-0.1.0-b63`
- Artifact ZIP SHA-256: `645cba67a91387f79d386931b5d0f4ead2502408b15c7f339013505e3f0ec7da`
- IPA: `ChatGPTClient-0.1.0-b63-dev-send-stream.ipa`
- IPA SHA-256: `b347d1e41ca5a4e1355a9cc713574ea96247e11918ccfb1f5ff621a0f9f6ff36`
- Package identity: Release / `0.1.0 (63)` / Candidate b63 / source marker `0c2e2b870e51` / minimum iOS14 / UIDeviceFamily `[1,2]` / Mach-O 64-bit arm64
- b39-b63 emitted identities: permanently reserved

## Accepted predecessor evidence

### Exact b62 focused Runtime pass

User export `ChatGPTClient-Diagnostics-20260830-151146.json` matched exact b62 / iPhone / iOS17.0.

Observed Send-entry sequence:

`ready=false / none -> ready=true / prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 text/event-stream -> terminal`

Terminal response evidence included:

- Native reasoning `34 deltas / 497 chars`;
- thinking preambles `3 / 20 chars`;
- reasoning segment breaks `2`;
- reasoning-active signals `3`;
- exact reasoning-end `1`, fallback false;
- final answer `93 deltas / 2878 chars`;
- tool results parent present/matched/unmatched/missing `20/20/0/0`;
- Native tool presentations/completion updates `20/20`.

User reported the tested round looked normal. This remains a focused Runtime pass for the exact b62 verified-composer + reasoning/final + exact-parent tool lifecycle scope; it does not universally prove every official-page state.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

## Exact b63 evidence-backed diagnostic scope

b62/current source evidence established:

- finished assistant `code` invocation messages addressed to tool recipients repeatedly carry `metadata.connector_tool_payload` as a short string-shaped field;
- completed tool messages remain separately parent-paired through `metadata.parent_id`;
- `assistant:thoughts` messages can carry object-shaped `metadata.inline_cot_expandable_content` with `source_message_ids`;
- the parser already owns one response-local transient `toolInvocationIdentityByID` Map used for exact result-parent association.

b63 therefore changes only diagnostic structure observation:

1. `connector_tool_payload` string is JSON-parsed only inside the diagnostic Web script. Exported evidence is capped to parse class plus sanitized top-level key names, direct child primitive/object/array type, and direct string/array length. String values, nested body contents and raw JSON are never exported.
2. For finished assistant `thoughts` messages with `inline_cot_expandable_content.source_message_ids`, b63 exports only aggregate message/reference counts and how many source references match response-local known invocation/tool-activity identities. Raw source/invocation IDs are never exported.
3. b62 composer detection, Native submit bridge, official protected Send, SSE text-patch grammar, reasoning/final split, exact `reasoning_ended`, tool-row invocation/result lifecycle, parent pairing and Native UI updates are unchanged.
4. No retry, polling, timer, watchdog, fallback, compatibility shim, production repository mutation or second persistent state owner was added.
5. b63 does **not** display raw expandable request/result bodies and does not authorize `assistant:thoughts` presentation.

## Exact b63 pre-Runtime validation

### Product/config assembly

To prevent an invalid transient artifact with new b63 code under b62 package identity, b63 was assembled as detached Git objects first and the feature branch was moved once only after diff audit.

- recovery-point parent: `e29952e1cfa3a6d87d9ea733cf72a6c1c6678fde`
- Swift blob: `6775b9408b60cf141b211a95d05448653f950720`
- Xcode build/Candidate blob: `6c3294704ce87b1462e5e2d1896efa5fd7e1eb2a`
- workflow blob: `da40b75a1b94742a6f91f920d8a830d14dc4f8a1`
- assembled tree: `cae7f27e2800fe48f8d492bfd364c91755935c67`
- exact product/config commit: `0c2e2b870e51c363c7734182d49618c438839cc2`

Compare `e29952e1... -> 0c2e2b87...` showed exactly three modified files:

- `.github/workflows/ios-foundation.yml`: 2 additions / 2 deletions;
- `ChatGPTClient.xcodeproj/project.pbxproj`: 4 additions / 4 deletions;
- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`: 66 additions / 8 deletions.

No unrelated product file changed.

### CI / Artifact

Both workflow executions on exact source `0c2e2b87...` completed successfully:

- Push `33321982009`, job `99285436158`;
- PR `33321983658`, job `99285440962`.

Chosen Runtime Artifact authority is Push Artifact `9735145598`. GitHub reported ZIP digest `sha256:645cba67a91387f79d386931b5d0f4ead2502408b15c7f339013505e3f0ec7da`; independent local SHA-256 calculation matched exactly.

ZIP contents:

- `ChatGPTClient-0.1.0-b63-dev-send-stream.ipa`
- matching `.ipa.sha256` sidecar.

Independent IPA SHA-256 calculation matched the sidecar: `b347d1e41ca5a4e1355a9cc713574ea96247e11918ccfb1f5ff621a0f9f6ff36`.

Built `Info.plist` and executable inspection confirmed:

- `CFBundleShortVersionString=0.1.0`;
- `CFBundleVersion=63`;
- `DiagnosticsCandidate=DEV-send-stream-0.1.0-b63`;
- `DiagnosticsSourceCommit=0c2e2b870e51`;
- `MinimumOSVersion=14.0`;
- `UIDeviceFamily=[1,2]`;
- executable is Mach-O 64-bit arm64.

Classification: **Code written / diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**

## Non-authoritative tooling refs

During detached assembly, the connector exposed branch creation while searching for lower-level Git write functions and created the following tooling-only refs, all from the docs-only recovery head rather than the b63 product commit:

- `tmp-b63-assembly-20260830`
- `tmp-b63-assembly-20260830-unused`
- `tmp-b63-do-not-use`
- `tmp-b63-tooling-ignore`

They have no Active checkpoint, no PR, no Candidate/Artifact authority and are **not** development branches. The available connector currently exposes create/update ref but not delete-ref, so they could not be removed in-chat. Future resume guards must ignore them as tooling-only refs unless repository state later shows they were manually deleted. Do not route work to them and do not infer candidate conflict from their existence.

## Recovery point

Completed in the b63 product / validation / documentation chain:

1. b63 scope justified from exact b62 structural evidence;
2. recovery checkpoint committed before non-atomic product assembly;
3. three product/config blobs assembled into one detached tree/commit;
4. detached diff audit confirmed only the intended three files;
5. formal feature branch moved exactly once to the complete b63 product/config commit;
6. PR #29 head confirmed exact b63 source;
7. Push and PR CI both passed;
8. Artifact `9735145598` produced and its ZIP/IPA/package identities independently verified;
9. b63 is permanently reserved;
10. `BUILD_TEST_INDEX.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md` and `PROJECT_SPECIFIC_RULES.md` synchronized through exact b63 pre-Runtime truth;
11. PR #29 synchronized to `b63 expandable-detail structure Runtime gate` and remains open / mergeable / unmerged;
12. compare `0c2e2b87... -> 8f917399...` confirmed all seven commits after the exact b63 product/config source were docs-only under `docs/project/`; no product/config/workflow/script file changed.

No autonomous product work remains before the real-device gate. Later docs-only commits do not redefine exact b63 product/config source `0c2e2b870e51c363c7734182d49618c438839cc2`.

## Next exact action

Hand the exact b63 IPA from Artifact `9735145598` to the user. Focused Runtime gate on iPhone/iOS17:

1. install exact `0.1.0 (63)` and verify Candidate/source marker;
2. clear diagnostics;
3. open `Native 输入 / Web Send` and send one GitHub/tool-active request that naturally causes multiple tool calls and a normal final answer;
4. wait for terminal and confirm Native reasoning/final text still looks complete and tool rows reach `已完成`;
5. switch to `显示 Web`; if official Web exposes expandable tool details for that same response, expand at least one representative tool row and capture a screenshot of what the official UI actually shows;
6. export diagnostics and upload them.

Interpret only b63 structural fields: `connectorToolPayloadJSONShape`, `inlineExpandableMessageCount`, `inlineExpandableSourceIDCount`, `inlineExpandableSourceInvocationMatchCount`, `inlineExpandableSourceToolActivityMatchCount`, `inlineExpandableSourceUnmatchedCount`, together with existing exact-parent / reasoning / final / terminal metrics. User-visible official-Web screenshot remains higher-priority presentation evidence. Do not implement expandable Native bodies until same-run evidence proves a specific safe user-visible mapping. Do not allocate b64 before this exact b63 Runtime evidence.
