# DEV-send-stream

## Status

**Active — exact b56 Runtime falsified the assumption that `reasoning_recap` is the real visible reasoning body: the exact recap path worked, but the captured recap was only 7 characters (`思考了 40s` in the user-visible reproduction), while the real visible reasoning text remained in the existing assistant text stream and stayed concatenated with the final answer. Exact b57 is now Code/CI/Artifact/package verified. b57 uses the already-proven `assistant:reasoning_recap + reasoning_status=reasoning_ended` event only as a reasoning-phase end marker, routes existing accepted text before the marker to a separate Native `思考过程` region and text after the marker to the final answer, and adds bounded text-free structure evidence for ordinary `assistant:text` message starts to locate the still-missing leading reasoning prefix. Raw `assistant:thoughts` and raw tool payloads remain excluded. Runtime/manual on b57 is pending. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence-only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c` at the latest light guard.
- **Stable native predecessor**: b38.
- **Stable/Frozen Send**: No.

## Exact b56 Runtime

Identity:

- Candidate `DEV-send-stream-0.1.0-b56`, `0.1.0 (56)`.
- Exact product/config source `cec921030fd1af9f3853f35af52b661586b3a8ab`.
- Artifact `9728937100`; IPA SHA `da62776200ce94fef95326abaea3b980f65a5698df5dfe481bd34046e0f8dbe6`.
- Runtime export `ChatGPTClient-Diagnostics-20260830-083244.json` matched build 56 / Candidate b56 / source `cec921030fd1` / Release / iPhone iOS17.0.

User-visible result:

- real visible reasoning beginning still truncated;
- `思考摘要` control appeared and expand/collapse worked;
- recap contained only a short status/description (`思考了 40s` in this run), not the real visible reasoning body;
- real visible reasoning and final answer still appeared together in the ordinary Native body.

Transport / metrics:

- HTTP200 `text/event-stream`, terminal true;
- `frameCount=75`;
- Native 26 deltas / 504 chars;
- exact-root 4, nested 8, root-nonexact 0;
- contextual values 14 / 299 chars, inactive values 0;
- continuation resets 4;
- generic structures 32 / overflow16;
- special structures 8 / overflow0;
- recap chars 7.

Exact event ordering materially relevant to the next change:

1. event 14 `assistant:text:in_progress`;
2. event 15 exact `append /message/content/parts/0`;
3. event 16 contextual value continuation;
4. later assistant-code/tool activity;
5. event 44 `assistant:thoughts / finished_successfully`;
6. event 45 exact `assistant:reasoning_recap / finished_successfully`, recipient all, `reasoning_status=reasoning_ended`, `reasoning_recap_type=collapse`;
7. terminal true.

Accepted b56 conclusion:

- recap string is **not** the real reasoning body in this Runtime sample;
- exact recap message remains a valid explicit reasoning-phase **end marker**;
- raw `assistant:thoughts` remains non-presentational;
- persistent leading truncation has a stronger source-backed hypothesis because an ordinary `assistant:text:in_progress` message precedes the first accepted append, but b56 did not record that ordinary text message's content field shape. Do not guess the missing field.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b56-runtime.md`.

Classification: **b56 Runtime partial pass / presentation defect confirmed**.

## Exact b57 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b57`
- Version/build: `0.1.0 (57)`
- Exact product/config source: `7074b1f85a0f239a5fd615f52196e1e28145523c`
- Product tree: `c402ce522e244cf63aa44b80a6d165b84342104c`
- Push Run / Job: `33302357908 / 99232731468` — success
- PR Run / Job: `33302359351 / 99232735067` — success
- Artifact: `9729360247`
- Artifact ZIP digest: `sha256:ae5a5532e2c30624907e9a2d61966090df4b8cc9ffa57f1b5725db8b61a8d275`
- IPA: `ChatGPTClient-0.1.0-b57-dev-send-stream.ipa`
- IPA SHA-256: `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`
- Package independently verified: Release / `0.1.0 (57)` / Candidate b57 / source marker `7074b1f85a0f` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64.
- Runtime/manual: Pending.
- b57 is permanently reserved after Artifact emission. Any product-code correction requires b58+ and exact b57 Runtime evidence.

### Exact b57 scope

b57 changes only the current diagnostic presentation/parser boundary plus Candidate identity:

1. preserve official protected Send construction, SSE interception and every previously accepted `/message/content/parts/0` / contextual-value text acceptance rule;
2. treat the exact evidence-backed recap message only as `reasoning_ended`, not as the reasoning body;
3. route accepted text before that marker to `native_reasoning_delta` / the Native `思考过程` region;
4. route accepted text after that marker to `native_answer_delta` / the ordinary final-answer body;
5. while reasoning is active, the Native reasoning region is visible/expanded; on exact `reasoning_ended`, it collapses and can be expanded/collapsed explicitly;
6. if a turn reaches terminal without any reasoning-end marker, promote the pre-marker text back to the ordinary answer so non-reasoning turns are not permanently misclassified;
7. add phase counts: Native reasoning/answer deltas+chars and exact reasoning-end marker count;
8. add a separate bounded 12-entry structural channel for ordinary `assistant:text` messages, including only direct key names, string lengths, array shape/string-char counts, safe booleans/enums, and whether the message appeared before/after reasoning end;
9. do **not** extract an unproven initial text field yet;
10. do **not** display `assistant:thoughts`, raw tool args/results, connector payloads, hidden/internal reasoning/system data, auth/proof/header values.

### Atomic b57 assembly

Tooling branch `tooling/b57-assembly-20260830` was created from post-b56-Runtime evidence commit `ecb8fd90fc1aff7016a02a6b375b5d7ec17824f2`.

Assembly compare showed only the three expected Candidate files:

- `.github/workflows/ios-foundation.yml`;
- `ChatGPTClient.xcodeproj/project.pbxproj`;
- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`.

Final tree `c402ce522e244cf63aa44b80a6d165b84342104c` was attached directly to parent `ecb8fd90fc1aff7016a02a6b375b5d7ec17824f2` as exact feature commit `7074b1f85a0f239a5fd615f52196e1e28145523c`; feature ref moved once. Tooling commits are not Candidate authority.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b57 remain diagnostic exceptions only. No diagnostic result alone promotes hidden/shadow Web to production.

Only explicitly user-visible service reasoning/status/tool information may be shown. `assistant:thoughts`, hidden chain-of-thought/internal reasoning and arbitrary tool payloads remain prohibited. b57 only re-presents the already-captured user-visible assistant text stream by an explicit service-side reasoning-end marker.

## Evidence ladder

- b51 Code/CI/Artifact/package: Passed; Runtime title-generation continuation correction confirmed.
- b52 Code/CI/Artifact/package: Passed; Runtime final answer complete / visible reasoning beginning incomplete.
- b53 Code/CI/Artifact/package: Passed; Runtime recap/thoughts/tool grammar materially identified.
- b54 Code/CI/Artifact/package: Passed; Runtime partial — tool grammar identified, recap gate blocked by observer saturation.
- b55 Code/CI/Artifact/package: Passed; Runtime intended gate passed — special channel works and recap/end structure proved.
- b56 Code/CI/Artifact/package: Passed; **Runtime partial** — recap UI works, recap is only short status, real reasoning/final remain mixed, leading reasoning still truncated.
- b57 Code/CI/Artifact/package: **Passed**; Runtime pending.
- Phase 9 Stable/Frozen: No.

## Batch K recovery point

Completed in this cycle:

1. exact b56 Runtime identity, screenshots and metrics classified;
2. `docs/project/runtime-evidence/DEV-send-stream-b56-runtime.md` created;
3. b57 allocated only after concrete b56 evidence;
4. exact b57 source emitted atomically at `7074b1f85a0f239a5fd615f52196e1e28145523c`;
5. both b57 Push/PR CI jobs passed;
6. Artifact `9729360247` verified against exact head SHA;
7. ZIP digest, IPA SHA and package identity independently verified.

Later documentation/PR commits do not redefine exact b57 product/config authority. Never rebuild/reuse b56 or b57.

## Next exact action

Hand exact b57 IPA to the user for one focused exact-device reasoning/tool-active turn.

Runtime gate:

1. clear diagnostics;
2. open `Native 输入 / Web Send（b57诊断）`;
3. send one prompt that naturally produces visible reasoning plus tool activity;
4. observe whether the previously mixed visible reasoning now streams only inside `思考过程` and whether final answer begins only after the reasoning section collapses;
5. report whether the beginning of `思考过程` is still truncated;
6. expand/collapse `思考过程` once after completion;
7. confirm no raw `assistant:thoughts` or raw tool payload is displayed;
8. wait for terminal and export diagnostics.

Primary diagnostic decision signals for the remaining prefix defect:

- `assistantTextMessageCount` / before / after counts;
- `phaseTextStructureSignatureCount` / overflow;
- `streamStructure` rows with `messageRole=assistant`, `messageContentType=text`, `textPhase=before_reasoning_end` or `after_reasoning_end`;
- especially `contentKeys`, `contentStringFields`, and `contentArrayFields` for the first before-reasoning-end `assistant:text:in_progress` message.

Do not allocate b58 or guess the initial text container until exact b57 Runtime supplies that structure evidence.
