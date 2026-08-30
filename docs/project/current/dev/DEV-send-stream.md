# DEV-send-stream

## Status

**Active — exact b58 Runtime is a partial pass. The bounded Native tool-activity region works on the primary iPhone/iOS17 Runtime: 4 exact completed assistant-code invocations produced 4 Native activity entries, 4 tool results were observed, and no raw args/results/connector payloads were shown. The b57 reasoning→final phase split also remains correct, but the leading reasoning prefix defect reproduced. This time the user supplied both Native and complete official-Web screenshots: the Native reasoning is missing exactly the 8-character opening preamble, while the first before-marker `assistant:text:in_progress` message is exactly `parts:1:string:chars8` with `is_thinking_preamble_message=true`. That is concrete evidence for one smallest b59 parser change: consume only this exact service-marked thinking preamble into Native reasoning before the existing patch stream. TD-024/TD-025/TD-028 and production response ownership remain unchanged; PR #29 remains evidence-only.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Current target main: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Guarded branch head before this checkpoint write: `703159d24cbf8f337b5affda03b4967727b42681`
- Other Active development checkpoints: none
- Stable native predecessor: b38
- Stable/Frozen Send: No

## Exact b58 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b58`
- Version/build: `0.1.0 (58)`
- Exact product/config source: `d9dbf208625e46b8eb4e7ec69209c9d519d0e5eb`
- Product tree: `ddb396aa942c48222e69671eaf3610127d9797e9`
- Push Run / Job: `33303998650 / 99237187408` — success
- PR Run / Job: `33304001877 / 99237195550` — success
- Artifact: `9729864129`
- ZIP digest: `sha256:3a907e6bb5f1cbd7f57d54b01e64805196247e612e2de961dac99d92df2060ac`
- IPA SHA: `0d5988caf21300bfb29e81b3f1f8bbf6eaa69a84f09efeda601e6d6f9b7b8875`
- Package: Release / `0.1.0 (58)` / Candidate b58 / source `d9dbf208625e` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64
- b58 is permanently reserved.

## Exact b58 Runtime

User export `ChatGPTClient-Diagnostics-20260830-094146.json` exactly matches Release / build58 / Candidate b58 / source `d9dbf208625e` / iPhone / iOS17.0.

Transport / terminal:

- official protected Send HTTP200 `text/event-stream`
- `frameCount=53`
- terminal true
- exact reasoning-end marker 1
- fallback promotion false

Native text:

- total `18 deltas / 338 chars`
- reasoning `4 deltas / 52 chars`
- final answer `14 deltas / 286 chars`
- assistant text messages before/after reasoning end: `1 / 1`
- phase structures `2 / overflow0`

Parser structure:

- exact-root text patches 3
- nested text patches 5
- root-nonexact 0
- contextual values `10 / 207 chars`
- inactive values 0
- continuation resets 3
- title-generation while continuation 0
- generic structures `32 / overflow2`; special `8 / overflow0`

Tool activity:

- `toolInvocationCount=4`
- `toolInvocationWithTitleCount=1`
- `toolResultCount=4`
- `toolResultWithTitleCount=3`
- `nativeToolPresentationCount=4`
- direct user screenshot confirms a separate Native `工具调用` region appeared; one invocation used a coherent service title and the remaining invocations used the intentional generic fallback; raw tool args/results were not presented.

Leading-prefix evidence:

- event 14 is `assistant:text:in_progress`, recipient `all`, before reasoning end;
- its direct content shape is `content_type,parts` with exactly one string part and `chars8`;
- direct metadata includes `is_thinking_preamble_message=true`;
- event 15 is the first exact `/message/content/parts/0` append;
- the Native screenshot begins after an 8-character opening phrase that is present in the user's complete official-Web screenshot;
- therefore the visually missing prefix length exactly matches the service-marked preamble length. The preamble text itself is not persisted in diagnostics/docs.

Accepted conclusion: **b58 tool activity Runtime gate passed, but b58 overall is partial because leading reasoning preamble is omitted.** The prior b57 no-visible-truncation observation no longer justifies rejecting the preamble path; b58 supplies the stronger side-by-side evidence required by the durable rule.

## b59 evidence-backed scope

A product-code correction may now use build/Candidate 59 only after identity checks complete. The intended change is deliberately narrow:

1. Preserve b58 protected-Send construction, SSE patch grammar, reasoning-end split/collapse, final-answer path, terminal fallback and tool-activity UI unchanged.
2. Before reasoning has ended, detect only a message satisfying all of:
   - role `assistant`;
   - `content_type=text`;
   - `status=in_progress`;
   - recipient `all`;
   - non-empty service message ID;
   - `metadata.is_thinking_preamble_message === true`;
   - `content.parts` is exactly one non-empty string.
3. Deduplicate this preamble in memory by service message ID; never log/export the ID.
4. Post that one string through the existing Native reasoning delta path before subsequent accepted text patches.
5. Record only aggregate preamble count/character count; never persist preamble text.
6. Do not consume arbitrary assistant initial content, arbitrary `parts`, `assistant:thoughts`, recap text, raw tool data or any other structural message.
7. Do not modify tool-title/result semantics in b59; b58's bounded tool activity is already Runtime positive for its tested scope.

## Batch M recovery point

Confirmed complete before this checkpoint:

1. startup governance re-read: branch `AGENTS.md` then `docs/project/START_HERE.md`;
2. Development route resolved to existing `DEV-send-stream` from the ongoing exact b58 Runtime gate;
3. Resume guard: only one Active checkpoint, PR #29 open/mergeable/unmerged, feature head `703159d2...`, target `main@1ac202c...`, exact b58 product source unchanged;
4. exact b58 Runtime diagnostics + both screenshots classified;
5. current source/rules/build-index boundaries re-read; b58 is reserved and b59 has not yet been emitted.

Pending deterministic writes/actions:

1. create `docs/project/runtime-evidence/DEV-send-stream-b58-runtime.md`;
2. bring `BUILD_TEST_INDEX.md` through b57/b58 Runtime/Artifact truth and confirm build59 is unused;
3. allocate `DEV-send-stream-0.1.0-b59` / build59;
4. atomically assemble exactly three Candidate files: `NativeWebSendEngineProbe.swift`, Xcode Candidate/build identity, workflow Artifact identity;
5. move feature ref once to the exact b59 product commit;
6. verify Push + PR CI, Artifact, ZIP digest, IPA SHA and built package identity;
7. synchronize PR #29 and durable project docs through b58 Runtime / b59 Artifact;
8. hand exact b59 IPA to the user for one focused reasoning/tool-active Runtime turn.

Do not modify `ConversationRepository`, auth ownership, Stable b38 modules, resume transport, attachments or production architecture in Batch M. Tooling assembly commits are never Candidate authority.

## Next exact action

Create the durable b58 Runtime evidence record, update the build/test index reservation truth, then allocate b59 and implement only the exact service-marked thinking-preamble path above. b60 must not be allocated unless exact b59 Runtime supplies new evidence.
