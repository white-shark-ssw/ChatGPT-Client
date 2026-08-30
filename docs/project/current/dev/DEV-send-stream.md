# DEV-send-stream

## Status

**Active — exact b60 Runtime passes the tested thinking-state, reasoning-segmentation, text-completeness and invocation→result parent-association gate. Exact b61 is now Code / Push CI / PR CI / Artifact / package Passed and awaits one tool-active iPhone/iOS17 Runtime turn. b61 preserves b60 Send/text/reasoning/thinking behavior, uses the Runtime-proven result `parent_id` association to update the correct transient Native tool entry, and records only privacy-safe shapes for candidate official detail fields. Raw tool request/result bodies, connector payload values and `assistant:thoughts` remain non-presentational. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged; PR #29 stays evidence-only / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Current target main verified: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Other Active development checkpoints: none
- Stable native predecessor: b38
- Stable/Frozen Send: No

## Exact b60 Runtime conclusion

Exact b60 product/config source `8ca445f3c17233ac36832f46417a8e53a138499e`; Artifact `9731477362`; IPA SHA `7cae323231b6b9d1aa837b03506450daa99f457fd8b4025deedb368dc008cd42`.

User export `ChatGPTClient-Diagnostics-20260830-122917.json` exactly matches Release / build60 / Candidate b60 / source `8ca445f3c172` / iPhone / iOS17.0. Two consecutive tool-active turns were tested.

- Turn 1: HTTP200 SSE / terminal / frameCount 88; Native reasoning `14 / 209 chars`; final `17 / 462`; preambles `2 / 10`; reasoning-active signals 2; Native `正在思考` presentations 3; service/Native segment breaks `1/1`; exact reasoning-end 1; fallback false; completed invocation presentations 13; invocation identities 15; results 15; parent present/matched/unmatched/missing `15/15/0/0`; author-name==recipient 14/15.
- Turn 2: HTTP200 SSE / terminal / frameCount 101; Native reasoning `17 / 221 chars`; final `54 / 922`; preambles `2 / 32`; reasoning-active signals 3; Native `正在思考` presentations 3; service/Native segment breaks `1/1`; exact reasoning-end 1; fallback false; invocation identities/completed/results `5/5/5`; parent present/matched/unmatched/missing `5/5/0/0`; author-name==recipient 3/5.
- Direct user result for both turns: Send 后先出现 `正在思考`, then reasoning streamed with visible line/paragraph separation; no obvious truncation.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b60-runtime.md`.

Classification: **b60 Runtime pass for tested presentation + parent association scope.** For tested traffic, completed tool-result metadata `parent_id` is the accepted invocation→result association key when it equals an invocation service message ID observed in the same stream. Raw IDs remain transient and unlogged. Adjacency/count/tool-name pairing is rejected; author-name/recipient equality is not authoritative.

## Exact b61 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b61`
- Version/build: `0.1.0 (61)`
- Exact product/config source: `2386872af03e0684eee8deca87f636dc265114ec`
- Product tree: `a687500c88cffabf3a8496652fd5e0b633264836`
- Product parent / last docs head: `b7b2bd3a7229d512fa7abdec8e35eaa0aa419bf8`
- Push Run / Job: `33312809061 / 99260781131` — success
- PR Run / Job: `33312811455 / 99260788483` — success
- Artifact: `9732514781`
- Artifact name: `ChatGPTClient-DEV-send-stream-0.1.0-b61`
- ZIP digest / independently verified SHA: `sha256:66976ecb53ac8fc2b116dcbce753fdf05499cea88dd29f0ae4223ab8baa5bf28`
- IPA SHA / sidecar / independent verification: `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`
- Package: Release / `0.1.0 (61)` / Candidate b61 / source `2386872af03e` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64
- b61 is permanently reserved after Artifact emission.

Evidence ladder: **Code written / Push CI passed / PR CI passed / Artifact produced / package identity independently verified; Runtime/manual pending; Stable/Frozen No.**

## b61 bounded behavior

1. Protected Web Send, b60 text patch grammar, exact thinking-preamble handling, event-driven `正在思考`, exact `reasoning_ended`, final-answer path and terminal fallback remain unchanged.
2. Invocation identities are assigned transient local slots in the Web diagnostic layer. A completed result whose metadata `parent_id` matches one observed invocation updates that exact slot. Raw service IDs never cross to Native or diagnostics.
3. Native tool rows now represent invocation lifecycle as `调用中` / `已完成`; a paired result may refine the already-authorized bounded `reasoning_title`. No request/result body is displayed.
4. b61 records only bounded shape descriptors for `connector_tool_payload`, `inline_cot_expandable_content`, `reasoning_titles`, `tool_icons`, `invoked_plugin`, and `invoked_resource`: primitive type, array length/item keys, object direct keys/types, or string length. Values and bodies are not logged.
5. `assistant:thoughts`, arbitrary raw tool bodies, connector payload values, prompt/answer bodies, auth/challenge values and service IDs remain prohibited.
6. Production `ConversationRepository`, auth ownership, resume transport, Stable b38 modules and attachments are untouched.

## Official-like target / remaining gate

The target remains event-driven: accepted/waiting -> visible reasoning -> zero or more real tool phases interleaved with reasoning-active states -> exact `reasoning_ended` -> final answer. A no-tool turn must never fabricate tools.

b61 Runtime must prove two things before any later Candidate may expose expandable tool detail:

- result-driven Native tool completion updates hit the correct visible entry without dropping identities such as b60 Turn 1's `15 identities / 13 completed invocation presentations / 15 matched results` case;
- shape evidence identifies a bounded service field that can be proven user-visible rather than an internal connector payload.

## Batch P recovery point

Confirmed complete:

1. b60 two-turn Runtime accepted and durable runtime evidence created;
2. b61 uniqueness/conflict guard passed; main still `1ac202c...`, no other Active development checkpoint, PR #29 dedicated/open/unmerged;
3. b61 assembled on an isolation branch and exact feature diff verified as only three Candidate files;
4. exact product/config source `2386872a...` created from one tree and feature branch moved once;
5. Push + PR CI succeeded;
6. Push Artifact `9732514781` downloaded and independently verified against GitHub digest, IPA sidecar, Info.plist and Mach-O identity;
7. later checkpoint/docs commits do not redefine exact b61 product/config source.

## Next exact action

Hand exact b61 IPA to the user. Clear diagnostics, open `Native 输入 / Web Send`, run one tool-active GitHub/repository question that naturally invokes several tools, wait for terminal, and export diagnostics. Observe whether each visible tool row advances from `调用中` to `已完成`, whether any duplicate/missing tool row is visible, whether `正在思考` / reasoning / final answer remain complete, and upload the export. Do not allocate b62 until exact b61 Runtime identifies the user-visible detail boundary or exposes a concrete pairing defect.
