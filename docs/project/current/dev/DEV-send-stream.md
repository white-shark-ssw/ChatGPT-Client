# DEV-send-stream

## Status

**Active — exact b62 has a focused iPhone/iOS17 Runtime pass for the verified-composer Send-entry / reasoning-final / exact-parent tool lifecycle gate. Current evidence still does not authorize raw expandable tool detail. Existing b62 traffic now gives one concrete diagnostic need for b63: `connector_tool_payload` repeatedly appears as a string on finished assistant tool-invocation messages, while `inline_cot_expandable_content` appears as an object containing `source_message_ids`; b62 already owns a per-response transient invocation-ID map for exact parent pairing. b63 is therefore justified as a diagnostic-only candidate that records only bounded JSON key/type fingerprints and aggregate source-reference match counts, with no raw IDs/values/bodies and no Send/parser/presentation behavior change. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged; PR #29 stays evidence-only / unmerged. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Other Active development checkpoints: none at latest guard
- Current feature head before b63 product batch: `4fadbce4a92996366a16319ac23ec039dabcdb8f`
- Current actual `main`: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Stable native predecessor: b38
- Current exact tested diagnostic Candidate: `DEV-send-stream-0.1.0-b62`
- Exact b62 product/config source: `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`
- b62 Artifact: `9733577825`
- b62 IPA SHA: `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`
- b39-b62 emitted identities: permanently reserved
- Proposed next identity after fresh uniqueness guard: `DEV-send-stream-0.1.0-b63` / build 63

## Exact b62 Runtime — focused pass

User export: `ChatGPTClient-Diagnostics-20260830-151146.json`.

Package identity matched exact b62: Release / build62 / Candidate b62 / source `e1b44f7ab6c4` / iPhone / iOS17.0.

### Composer / protected-Send gate

Observed startup sequence:

1. composer `ready=false`, strategy `none`;
2. page loaded `new_or_other`;
3. composer remained `ready=false`, strategy `none`;
4. only later composer became `ready=true`, strategy `prompt_textarea`;
5. submit-time composer remained `prompt_textarea`;
6. `submitResult=submitted` was immediately followed by real `sendObserved`;
7. response was HTTP200 `text/event-stream` and entered `lifecycle_send_accepted` thinking state.

This passes the exact b62 primary gate for the tested cold-launch path. It directly differs from the rejected b61 generic-textarea run. One positive run does not prove the official page can never present another future race.

### Reasoning / final presentation

Terminal metrics:

- `frameCount=196`
- `terminal=true`
- Native reasoning `34 deltas / 497 chars`
- Native reasoning segment breaks `2`
- thinking preambles `3 / 20 chars`
- reasoning-active signals `3`
- Native thinking presentations `4`
- exact reasoning-end markers `1`
- fallback promoted `false`
- final answer `93 deltas / 2878 chars`
- Native total `127 deltas / 3375 chars`
- inactive value strings `0`
- root-nonexact text patches `0`

User directly reported the one tested round looked normal; screenshot showed populated reasoning, completed tool rows and complete-looking final text with no obvious truncation.

### Tool lifecycle

- tool invocations presented: `20`
- invocation identities observed: `21`
- results: `20`
- result parent present/matched/unmatched/missing: `20/20/0/0`
- paired Native result presentations: `20`
- Native tool presentations/completion updates: `20/20`

The extra observed invocation identity is **not** force-paired by count/order. Every completed result in the tested set had an exact parent match and corresponding Native completion update.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

Classification: **b62 focused Runtime pass for verified-composer Send entry + preserved tested reasoning/final + exact-parent tool lifecycle. Stable/Frozen No.**

## Evidence-backed b63 diagnostic scope

Existing exact b62 / prior tool-active diagnostics establish:

- finished assistant `code` invocation messages addressed to `api_tool.call_tool` repeatedly contain `metadata.connector_tool_payload` as a short string-shaped field;
- some of the same invocation messages also contain bounded `reasoning_titles` / `tool_icons` arrays;
- completed tool messages remain separately parent-paired through `metadata.parent_id`;
- `assistant:thoughts` messages can contain `metadata.inline_cot_expandable_content` shaped as an object with `source_message_ids`;
- b62 already keeps `aggregate.toolInvocationIdentityByID` as a response-local transient Map solely for exact parent association and never exports raw IDs.

This supports only the following bounded b63 diagnostics:

1. For string-valued `connector_tool_payload`, attempt JSON parsing and record only a capped top-level structural fingerprint: parse class plus sanitized direct key names, primitive/direct child type and direct string/array length. Never log string values, nested bodies or raw JSON.
2. For `inline_cot_expandable_content.source_message_ids`, count only aggregate source-reference entries and how many match the existing transient invocation map in the same response. Never export any source/invocation ID.
3. Preserve all b62 composer, protected Send, text patch grammar, reasoning/final split, exact `reasoning_ended`, tool-row lifecycle, result parent pairing and UI behavior unchanged.
4. Add no retry, polling, timer, watchdog, fallback, second state owner or production repository mutation.
5. Do not display expandable request/result bodies in b63; field names/shape remain evidence, not presentation authorization.

## b63 uniqueness / conflict guard

Latest guard before this recovery point:

- only Active development checkpoint is `DEV-send-stream`;
- PR #29 remains open / mergeable / unmerged and its head matched `4fadbce4...` before this docs-only checkpoint write;
- actual `main` remains `1ac202c...`;
- repository search found no existing `DEV-send-stream-0.1.0-b63` identity;
- product modification surface is limited to `NativeWebSendEngineProbe.swift`, Xcode build/Candidate metadata and the existing iOS workflow artifact identity;
- no `ConversationRepository`, auth owner, Stable b38 module or attachment/background code is in scope.

## Batch recovery point — b63 product/config assembly

Known baseline before this checkpoint write: feature head `4fadbce4a92996366a16319ac23ec039dabcdb8f`, tree `fead61ccdb8bee8ce5ffe1ff96da707145a7d1dd`.

Confirmed complete before product mutation:

1. b62 Runtime and durable documentation cycle closed;
2. b63 evidence need narrowed to connector-payload JSON top-level structure plus inline-expandable source-reference aggregate matching;
3. source inspection confirmed the existing transient invocation-ID Map can perform matching without a second identity owner;
4. initial b63 uniqueness/parallel/base guard passed.

Pending coherent batches:

1. **Product/config batch:** after this checkpoint commit, fetch its new head/tree and create one Git tree/commit containing exactly:
   - `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift` — b63 diagnostic-only structural additions;
   - `ChatGPTClient.xcodeproj/project.pbxproj` — build 63 / Candidate b63 in Debug + Release;
   - `.github/workflows/ios-foundation.yml` — b63 Candidate comment / Artifact name.
   Move `dev/send-stream-20260829` exactly once to that product/config commit. Do not create an intermediate branch state with b63 code under b62 identity.
2. **Validation batch:** verify product commit diff, allow Push + PR CI, inspect both results, then obtain/verify exact b63 Artifact/package identity.
3. **Documentation batch:** after real CI/Artifact facts exist, synchronize checkpoint, `BUILD_TEST_INDEX.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md`, `PROJECT_SPECIFIC_RULES.md` and PR #29. Later docs-only commits must not redefine exact b63 product/config source.

Recovery rules:

- if interrupted, re-read this checkpoint and actual branch/PR/head before any write;
- perform only missing deterministic writes; never replay the whole chain;
- b62 source `e1b44f7a...` and Artifact `9733577825` remain immutable historical authority;
- do not reserve/claim b63 as Artifact-produced until an actual b63 Artifact exists;
- if an Artifact is emitted from valid b63 identity, b63 becomes permanently reserved even if Runtime later rejects it.

## Next exact action

Fetch the new checkpoint commit/tree, assemble the three b63 product/config blobs from that tree, create one product/config commit, then move the feature branch once. Continue through CI/Artifact/package verification autonomously. The next normal human gate is exact b63 iPhone/iOS17 Runtime after a verified IPA exists; do not stop merely for an intermediate code/CI/checkpoint milestone.
