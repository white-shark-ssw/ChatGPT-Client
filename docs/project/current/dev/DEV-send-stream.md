# DEV-send-stream

## Status

**Active — exact b52 Runtime materially narrows the remaining gap: final answer complete, user-visible reasoning/thinking beginning slightly truncated. b52 rejects the inactive value-only/root-nonexact hypothesis for this reproduction. Exact b53 is now Code/CI/Artifact/package verified as a diagnostic-only reasoning/tool SSE structure classifier; the next gate is one focused exact-device reasoning/tool reproduction. No reasoning UI/parser broadening is allowed until exact b53 evidence identifies the service-visible reasoning/tool event grammar. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; title/body synchronized to b53 Runtime gate.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; no base drift.
- **Other Active development checkpoints**: none.
- **Stable native predecessor**: b38.
- **Exact b52**: `DEV-send-stream-0.1.0-b52`, `0.1.0 (52)`, product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`, Push `33276080936 / 99162937523`, PR `33276082767 / 99162942750`, Artifact `9721532867`, ZIP `sha256:2ffd7e46e80019d3c4e8d6cbfa5c91dffa2a5f88222a30d5c4d5fb1e4fd752fc`, IPA SHA `a3de5c6eb4f7b790764fcd0adc4c98108fb550e7cedb3d6b02b931d266946b23`.
- **Exact b53**: `DEV-send-stream-0.1.0-b53`, `0.1.0 (53)`, exact product/config source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`, Push `33294541342 / 99211838094`, PR `33294542985 / 99211842336`, Artifact `9726996570`, ZIP `sha256:8831bbae1c5cad9c9cd7f0ad9fbcf4846d709b27ae950b0391d436e20749b38c`, IPA SHA `d5eee722ea01dc2c1b419a803574aec8ad2199299a3d0bbb51de4bae574f25dc`, Release/iOS14/`[1,2]`/arm64.
- **Stable/Frozen Send**: No.

## Accepted b51 conclusion

Exact b51 first fresh long response delivered `11618` Native characters across `284` deltas with `titleGenerationWhileContinuationCount=1`, terminal true and Web assistant text 0; user visually judged it complete. b51 Runtime therefore confirms the b50 fresh-new-chat missing-middle defect was corrected by preserving continuation across the evidenced exact `title_generation` event.

## Exact b52 Runtime — 2026-08-30

Durable record: `docs/project/runtime-evidence/DEV-send-stream-b52-runtime.md`.

User supplied exact b52 diagnostics (`buildNumber=52`, source marker `5c0690ce062e`, iPhone/iOS17.0) and reported:

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

1. Remaining visible gap is reasoning/thinking-specific on this reproduction; final answer capture passed.
2. No root non-exact assistant patch and no inactive value-only string occurred, so the prior non-exact-root→inactive-`v` hypothesis is rejected for this reproduction.
3. Six nested assistant-text patches and five structural resets occurred, but the existing counters cannot identify which parent event/content type owns visible reasoning/tool presentation.
4. Complete user-visible reasoning capture remains Runtime rejected/partial.
5. Do not merge reasoning and final answer into one undifferentiated production text stream.

## Reasoning / tool presentation scope

`SEND_STREAM_PREFLIGHT.md` already places user-visible reasoning, reasoning→final transition and follow-tail inside `DEV-send-stream`. The requested future UX — reasoning collapse/expand plus a tap-driven sheet/popover for tool-call status/details — remains in this Work. Only explicitly user-visible service data may be shown; hidden chain-of-thought/internal tool nodes must never be exposed or inferred.

Current b40/b41 protocol evidence left user-visible reasoning Unknown/Unverified. b41 already contains a privacy-safe structural probe pattern that records event type, operation, patch path, message role/content type, structural key names and nested batch patch paths without recording text or raw IDs.

## Exact b53 implementation

Exact product/config source: `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`.

b53 preserves b52 text filtering/output behavior and adds only bounded unique structure observation before existing parser behavior runs:

- at most 32 unique structure signatures are emitted to diagnostics;
- fields: event/frame index, event `type`, root operation/path, first structurally discoverable message role/content type/status/end-turn, bounded top-level/value key names, bounded nested patch operation/path list;
- terminal metrics add unique-signature count and overflow count;
- no prompt, answer, reasoning text, raw payload, raw IDs, auth/proof/header values or DOM reasoning scraping are logged;
- inactive value-only behavior, title-generation handling, scrub behavior and Native text output are unchanged from b52.

The b53 Swift source, both target build configurations (`CURRENT_PROJECT_VERSION=53`, Candidate b53), and workflow Artifact identity `ChatGPTClient-DEV-send-stream-0.1.0-b53` were assembled in one Git tree/commit and the branch ref moved once. No intermediate feature head contained b53 code under b52 identity.

## b53 validation / package identity

- Push Run / Job `33294541342 / 99211838094` — success.
- PR Run / Job `33294542985 / 99211842336` — success.
- Push Artifact `9726996570`; digest `sha256:8831bbae1c5cad9c9cd7f0ad9fbcf4846d709b27ae950b0391d436e20749b38c`.
- IPA `ChatGPTClient-0.1.0-b53-dev-send-stream.ipa`; SHA `d5eee722ea01dc2c1b419a803574aec8ad2199299a3d0bbb51de4bae574f25dc`.
- Independent package inspection: `0.1.0 (53)`, Candidate `DEV-send-stream-0.1.0-b53`, source marker `3204b183ca4f`, `DiagnosticsBuildConfiguration=Release`, minimum iOS14.0, UIDeviceFamily `[1,2]`, Mach-O arm64.
- Runtime/manual: Pending.

Because Artifact `9726996570` exists, b53 is permanently reserved. Any later product-code correction requires b54+ and must be justified by exact b53 Runtime.

## Batch G — b52 Runtime -> b53 reasoning/tool structural evidence

**Complete through exact Artifact/package verification, PR metadata and durable documentation synchronization.**

Confirmed:

1. Batch G recovery checkpoint established from feature head `aee7b0c0a4f8556c68ba4aeb88cf004a5e622849` / target `main@1ac202c...`;
2. exact b52 Runtime evidence persisted at `docs/project/runtime-evidence/DEV-send-stream-b52-runtime.md`;
3. atomic b53 product/config source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`;
4. exact b53 Push/PR CI success and Artifact/package identity verified;
5. PR #29 title/body synchronized to the b53 reasoning/tool structure Runtime gate;
6. `PROJECT_STATE.md`, `MODULE_STATUS.md`, `BUILD_TEST_INDEX.md`, `PROJECT_PROFILE.md`, `DEVELOPMENT_PLAN.md` and `PROJECT_SPECIFIC_RULES.md` synchronized through b52 Runtime / b53 Artifact truth.

Later commits after `3204b183...` are docs-only and do not redefine exact b53 product/config identity. Never alter/rebuild b52 or b53.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b53 are diagnostic exceptions only. TD-024/TD-025 remain unchanged. No diagnostic result alone promotes hidden/shadow Web to production.

## Evidence ladder

- b51 Code/CI/Artifact/package: Passed; Runtime confirmed fresh-new-chat title-generation correction.
- b52 Code/CI/Artifact/package: Passed; Runtime **final answer complete / reasoning leading content incomplete**.
- b53 Code/CI/Artifact/package: Passed; Runtime pending.
- Phase 9 Stable/Frozen: No.

## Next exact action

Hand exact Artifact `9726996570` to the user. Runtime focus: one prompt that naturally produces visible reasoning plus tool activity, preferably the same GitHub/project-progress style request; observe reasoning beginning completeness, final-answer completeness and visible tool activity, then export diagnostics after terminal. Do not implement reasoning collapse/expand, tool sheet UI, reasoning lifecycle state or parser broadening until that evidence identifies the actual user-visible grammar. Do not allocate b54 by guess.