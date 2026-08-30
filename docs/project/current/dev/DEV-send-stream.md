# DEV-send-stream

## Status

**Active — exact b52 Runtime materially narrows the remaining gap: the final answer was visually complete, while only the beginning of the user-visible reasoning/thinking portion was slightly truncated. b52 structural metrics reject the earlier inactive value-only hypothesis for this reproduction (`inactiveValueStringCount=0`, `rootNonExactTextPatchCount=0`) and instead show multiple nested text patches / structural resets. Exact b53 is allocated as a diagnostic-only reasoning/tool SSE structure classifier; no reasoning UI/parser broadening is allowed until exact b53 evidence identifies the service-visible reasoning/tool event grammar. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Current branch head at Batch G start**: `aee7b0c0a4f8556c68ba4aeb88cf004a5e622849`.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; no base drift from prior checkpoint.
- **Other Active development checkpoints**: none; `docs/project/current/dev/` contains only this Work plus template README.
- **Stable native predecessor**: b38.
- **Exact b52**: `DEV-send-stream-0.1.0-b52`, `0.1.0 (52)`, product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`, Push `33276080936 / 99162937523`, PR `33276082767 / 99162942750`, Artifact `9721532867`, ZIP `sha256:2ffd7e46e80019d3c4e8d6cbfa5c91dffa2a5f88222a30d5c4d5fb1e4fd752fc`, IPA SHA `a3de5c6eb4f7b790764fcd0adc4c98108fb550e7cedb3d6b02b931d266946b23`.
- **Allocated next Candidate**: `DEV-send-stream-0.1.0-b53`, version/build `0.1.0 (53)`; not yet emitted at Batch G start.
- **Stable/Frozen Send**: No.

## Accepted b51 conclusion

Exact b51 first fresh long response delivered `11618` Native characters across `284` deltas with `titleGenerationWhileContinuationCount=1`, terminal true and Web assistant text 0; user visually judged it complete. b51 Runtime therefore confirms the b50 fresh-new-chat missing-middle defect was caused by the evidenced `title_generation` continuation reset and is corrected by preserving continuation across that exact structural event.

## Exact b52 Runtime — 2026-08-30

User supplied exact `DEV-send-stream-0.1.0-b52` diagnostics (`buildNumber=52`, source marker `5c0690ce062e`, iPhone/iOS17.0) and reported:

- the **user-visible reasoning/thinking beginning was slightly truncated**;
- the **real/final answer was not truncated**.

One Native submission reached official protected Send HTTP200 `text/event-stream` and terminal true. Aggregate metrics:

- `frameCount=74`;
- `removedTextPatchCount=26`, `removedTextCharacters=614`;
- `explicitTextPatchCount=11`;
- `exactTopLevelTextPatchCount=5`;
- `rootNonExactTextPatchCount=0`;
- `nestedTextPatchCount=6`;
- `contextualValueStringCount=15`, `contextualValueStringCharacters=355`;
- `inactiveValueStringCount=0`, `inactiveValueStringCharacters=0`;
- `continuationResetWhileActiveCount=5`;
- `firstInactiveValueContext=none`;
- `titleGenerationWhileContinuationCount=0`;
- `nativeDeltaCount=26`, `nativeCharacters=614`;
- `webAssistantTextCharacters=0`, terminal true.

Accepted b52 conclusions:

1. The earlier b51 GitHub/tool-style observation must be refined from generic “reply leading truncation” to **reasoning/thinking leading truncation with final answer complete** for the exact b52 reproduction.
2. The b52 reproduction does **not** support the hypothesis that an exact/root non-exact assistant patch failed to activate value-only continuation: no root non-exact patch and no inactive value-only string occurred.
3. Multiple nested assistant-text patches and multiple structural resets occurred while final answer capture still completed. Current metrics cannot identify which nested parent/event/content type belongs to user-visible reasoning or tool presentation.
4. Complete final-answer capture for this exact reproduction is Runtime passed; complete user-visible reasoning capture remains Runtime rejected/partial.
5. Do not merge reasoning and final answer into one undifferentiated production text stream. The next evidence must identify explicit service-visible reasoning/tool structure before Native reasoning UI/state is implemented.

## Reasoning / tool presentation scope

`SEND_STREAM_PREFLIGHT.md` already places user-visible reasoning, reasoning→final transition and follow-tail inside `DEV-send-stream`. The user's requested future UX — reasoning collapse/expand plus a tap-driven sheet/popover for tool-call status/details — therefore remains in this Work. However, the preflight also requires that only explicitly user-visible service data be shown and prohibits exposing hidden chain-of-thought or inferring reasoning from internal/tool nodes.

Current b40/b41 durable protocol evidence explicitly left user-visible reasoning Unknown/Unverified. The earlier b41 structural probe already contains a privacy-safe pattern that records event type, operation, patch path, message role, message content type, key names and nested batch patch paths without recording text or IDs. b53 should reuse this evidenced structural-observation pattern inside the current pre-React Send interception path.

## Exact b53 diagnostic objective

b53 must preserve every b52 filtering/output behavior and add **structure-only evidence**, bounded by unique signatures/counts. No prompt, answer, reasoning text, raw payload, raw IDs, auth/proof/header values or DOM reasoning scraping may be logged.

Required evidence fields, only where safely structural:

- frame/event index;
- event `type`;
- top-level operation `o` and patch path `p`;
- message author role and `content.content_type` when structurally present;
- message status/end-turn boolean when present;
- bounded top-level/value key names;
- bounded nested patch operation/path summaries for patch batches;
- unique signature count / overflow count at terminal.

The diagnostic must be bounded (unique signatures only, hard cap) and must not alter the body returned to Web or the Native text currently captured by b52.

## Batch G — b52 Runtime -> b53 reasoning/tool structural evidence

Baseline / identity:

- feature branch head: `aee7b0c0a4f8556c68ba4aeb88cf004a5e622849`;
- exact immutable b52 product source: `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`;
- target `main@1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- PR #29 open / mergeable / head matches feature branch;
- b53 allocated uniquely as `DEV-send-stream-0.1.0-b53`, `0.1.0 (53)`.

Planned coherent writes:

1. persist `docs/project/runtime-evidence/DEV-send-stream-b52-runtime.md`;
2. implement b53 structure-only classifier in `NativeWebSendEngineProbe.swift` without changing b52 text filtering/output;
3. atomically update b53 Swift + target build/Candidate + workflow Artifact identity in one product/config commit so no b53 code can build under b52 identity;
4. verify exact b53 Push/PR CI, Artifact and package identity;
5. synchronize PR #29 and durable project docs;
6. hand exact b53 IPA to user for one reasoning/tool-style reproduction and diagnostics export.

Writes confirmed complete at Batch G start:

- Resume Guard and b52 exact runtime metrics reviewed;
- b53 identity availability checked against `BUILD_TEST_INDEX.md` and Active checkpoints;
- this Batch G recovery point.

Still pending:

- b52 Runtime evidence file;
- b53 product/config commit;
- CI/Artifact/package verification;
- durable docs / PR metadata synchronization;
- exact-device b53 Runtime.

Recovery rule: if interrupted, re-read this checkpoint and actual GitHub branch/PR/Artifact state; perform only missing deterministic writes. Never alter/rebuild b52. Once b53 Artifact exists, b53 becomes permanently reserved.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b53 are diagnostic exceptions only. TD-024/TD-025 remain unchanged. No diagnostic result alone promotes hidden/shadow Web to production.

## Evidence ladder

- b51 Code/CI/Artifact/package: Passed; Runtime confirmed fresh-new-chat title-generation correction; later tool-style reasoning gap remained.
- b52 Code/CI/Artifact/package: Passed; Runtime **final answer complete / reasoning leading content incomplete**.
- b53 identity: Allocated; Code/CI/Artifact/Runtime pending.
- Phase 9 Stable/Frozen: No.

## Next exact action

Persist exact b52 Runtime evidence, then implement the b53 privacy-safe structural signature classifier using the already evidenced b41 structural probe pattern. Do not implement reasoning collapse/expand, tool sheet UI, reasoning lifecycle state or parser broadening until b53 identifies the actual user-visible reasoning/tool event grammar.