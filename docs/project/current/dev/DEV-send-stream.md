# DEV-send-stream

## Status

**Active — exact b55 Runtime passed its intended evidence gate: the independent special observer retained `assistant:reasoning_recap` under generic-observer saturation and directly proved the recap text container plus collapse/end semantics. Exact b56 is now Code/CI/Artifact/package verified and implements only an exact Native recap presentation: `assistant + reasoning_recap + finished_successfully + recipient=all + reasoning_status=reasoning_ended + reasoning_recap_type=collapse` -> `message.content.content`, shown in a distinct default-collapsed Native region. Existing b55 text interception remains unchanged; raw `assistant:thoughts` and tool payloads remain excluded. The next human gate is one focused exact-device b56 reasoning/tool turn. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / not merged; evidence-only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c` at the latest light guard.
- **Stable native predecessor**: b38.
- **Stable/Frozen Send**: No.

## Exact b55 Runtime — accepted evidence gate

User supplied `ChatGPTClient-Diagnostics-20260830-080229.json`; metadata exactly matched b55: `0.1.0 (55)`, Candidate `DEV-send-stream-0.1.0-b55`, source marker `aae856069b46`, Release, iPhone/iOS17.0.

Transport / aggregate:

- official protected Send HTTP200 `text/event-stream`, terminal true;
- `frameCount=69`;
- Native 24 deltas / 481 chars;
- exact top-level text patches 4, nested text patches 8, root-nonexact 0;
- contextual value strings 12 / 236 chars;
- inactive value strings 0;
- continuation resets 4;
- generic structures 32 / overflow 14;
- **special structures 7 / overflow 0**;
- Web assistant text chars 0.

The exact target special message was retained at event index 41:

- role `assistant`;
- content type `reasoning_recap`;
- status `finished_successfully`;
- recipient `all`;
- content keys `content,content_type`;
- exact-turn content string shape `content_type:15,content:7`;
- `can_save:false`;
- `reasoning_status:reasoning_ended`;
- `reasoning_recap_type:collapse`.

Accepted: the service-defined recap text container is `message.content.content`; the exact message declares reasoning ended and a collapsed recap presentation. A following Candidate may expose only this recap string in a separate Native collapsible region.

Immediately before it, event 40 remained a separate `assistant:thoughts` message with `thoughts` array / `chunks,content,finished,summary`, `reasoning_status:is_reasoning`, `tool_summary_type:github`. Raw thoughts/chunks/internal reasoning remain prohibited from presentation.

Tool invocation/result structures also remained captured, but b55 still does not prove an exact user-visible tool-node presentation boundary. Raw tool arguments/results/connector payloads remain excluded.

Classification: **b55 Runtime pass for its intended gate**. Durable record: `docs/project/runtime-evidence/DEV-send-stream-b55-runtime.md`.

## Exact b56 identity / validation

- Candidate: `DEV-send-stream-0.1.0-b56`
- Version/build: `0.1.0 (56)`
- Exact product/config source: `cec921030fd1af9f3853f35af52b661586b3a8ab`
- Product tree: `3ef2884676132becfde01b42826a711a8b3ca893`
- Push Run / Job: `33301008807 / 99229039032` — success
- PR Run / Job: `33301010617 / 99229043710` — success
- Artifact: `9728937100`
- Artifact ZIP digest: `sha256:2f4b5a216298e9c79ccbec2a7f4420719c8406120815f568c0ddd8b89d46d430`
- IPA: `ChatGPTClient-0.1.0-b56-dev-send-stream.ipa`
- IPA SHA-256: `da62776200ce94fef95326abaea3b980f65a5698df5dfe481bd34046e0f8dbe6`
- Package: Release / `0.1.0 (56)` / Candidate b56 / source `cec921030fd1` / minimum iOS14.0 / UIDeviceFamily `[1,2]` / arm64.
- Runtime/manual: Pending.
- b56 is permanently reserved after Artifact emission. Any product-code correction requires b57+ and exact b56 Runtime evidence.

### Exact b56 scope

Only `NativeWebSendEngineProbe.swift` product behavior changed, plus b56 build/workflow identity.

1. Preserve all b55 protected-Send and text interception behavior.
2. Before existing text filtering, inspect the already-parsed message only for the exact evidence-backed recap shape:
   - `author.role == assistant`;
   - `content.content_type == reasoning_recap`;
   - `status == finished_successfully`;
   - `recipient == all`;
   - `metadata.reasoning_status == reasoning_ended`;
   - `metadata.reasoning_recap_type == collapse`;
   - non-empty string `content.content`.
3. Bridge only that recap string to Native as `native_reasoning_recap`.
4. Show a distinct `思考摘要 ▸` region, hidden until a recap arrives and collapsed by default.
5. User tap toggles only that recap region; diagnostics persist only state and character count, never recap text.
6. Reset the diagnostic recap view at the beginning of each Native submission.
7. Add `reasoningRecapCharacters` to terminal aggregate logging.
8. Do not display `assistant:thoughts`, raw tool args/results, connector payloads, hidden/internal system data, or copied auth/challenge material.
9. Do not alter current b55 mixed/final text parser; exact reasoning→final patch-phase separation remains a later evidence gate.

### Atomic b56 assembly

Tooling branch `tooling/b56-assembly-20260830` was created from the post-b55-Runtime feature parent `5c09d2b96402ece5414ee7f35ce45d1766299113`. Three expected Candidate files were assembled there; compare showed only:

- `.github/workflows/ios-foundation.yml`;
- `ChatGPTClient.xcodeproj/project.pbxproj`;
- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`.

Final tree `3ef2884676132becfde01b42826a711a8b3ca893` was attached directly to parent `5c09d2b96402ece5414ee7f35ce45d1766299113` as exact feature commit `cec921030fd1af9f3853f35af52b661586b3a8ab`; feature ref moved once. Tooling commits are not Candidate authority.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b56 are diagnostic exceptions only. No diagnostic result alone promotes hidden/shadow Web to production.

Only explicitly user-visible service reasoning/status/tool information may be shown. Exact b55 now authorizes only the `reasoning_recap` string for this diagnostic presentation. `assistant:thoughts`, hidden chain-of-thought/internal reasoning and arbitrary tool payloads remain prohibited.

## Evidence ladder

- b51 Code/CI/Artifact/package: Passed; Runtime title-generation continuation correction confirmed.
- b52 Code/CI/Artifact/package: Passed; Runtime final answer complete / visible reasoning beginning incomplete.
- b53 Code/CI/Artifact/package: Passed; Runtime recap/thoughts/tool grammar materially identified.
- b54 Code/CI/Artifact/package: Passed; Runtime partial — tool grammar identified, recap gate blocked by observer saturation.
- b55 Code/CI/Artifact/package: Passed; **Runtime intended gate passed** — special channel works; exact recap container/collapse/end semantics proved.
- b56 Code/CI/Artifact/package: **Passed**; Runtime pending.
- Phase 9 Stable/Frozen: No.

## Batch J recovery point

Completed in this cycle:

1. exact b55 Runtime identity and metrics verified from user export;
2. `DEV-send-stream-b55-runtime.md` created;
3. b56 allocated only after concrete b55 evidence;
4. exact b56 source emitted atomically at `cec921030fd1af9f3853f35af52b661586b3a8ab`;
5. both b56 Push/PR CI jobs passed;
6. Artifact `9728937100` verified against exact head SHA;
7. ZIP digest, IPA SHA and package identity independently verified.

Later docs-only commits do not redefine exact b56 product/config authority. Never rebuild/reuse b55 or b56.

## Next exact action

Hand exact b56 IPA to the user for one focused exact-device turn that naturally produces visible reasoning plus tool activity.

Runtime gate:

1. clear diagnostics;
2. open `Native 输入 / Web Send（b56诊断）`;
3. send one reasoning/tool-active request;
4. verify that a `思考摘要 ▸` control appears only after the service recap is received;
5. tap once to expand and confirm the recap is a coherent user-visible summary, then tap again to collapse;
6. confirm raw `thoughts` or raw tool payloads are not shown;
7. final/current text area is intentionally still b55 behavior in this Candidate;
8. wait for terminal and export diagnostics.

Primary signals: `nativeWebSendEngineProbe.reasoningRecap` with nonzero character count, expand/collapse presentation events if tapped, `reasoningRecapCharacters` in terminal metrics, and user visual confirmation that the displayed recap matches an explicitly visible reasoning summary rather than internal thoughts.

Do not implement tool UI or reasoning→final text-phase separation until b56 Runtime establishes the recap presentation and supplies the next concrete smallest change.
