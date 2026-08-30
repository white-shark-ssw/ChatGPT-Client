# DEV-send-stream

## Status

**Active — exact b52 Runtime materially narrows the remaining gap: final answer complete, user-visible reasoning/thinking beginning slightly truncated. b52 rejects the inactive value-only/root-nonexact hypothesis for this reproduction. Exact b53 product/config source is now written atomically as a diagnostic-only reasoning/tool SSE structure classifier; CI/Artifact pending. No reasoning UI/parser broadening is allowed until exact b53 evidence identifies the service-visible reasoning/tool event grammar. TD-024/TD-025 remain unchanged; PR #29 remains evidence-only.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; no base drift.
- **Other Active development checkpoints**: none.
- **Stable native predecessor**: b38.
- **Exact b52**: `DEV-send-stream-0.1.0-b52`, `0.1.0 (52)`, product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`, Push `33276080936 / 99162937523`, PR `33276082767 / 99162942750`, Artifact `9721532867`, ZIP `sha256:2ffd7e46e80019d3c4e8d6cbfa5c91dffa2a5f88222a30d5c4d5fb1e4fd752fc`, IPA SHA `a3de5c6eb4f7b790764fcd0adc4c98108fb550e7cedb3d6b02b931d266946b23`.
- **Exact b53**: `DEV-send-stream-0.1.0-b53`, `0.1.0 (53)`, exact product/config source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`; CI/Artifact pending.
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

## Batch G — b52 Runtime -> b53 reasoning/tool structural evidence

Baseline / identity:

- Batch start feature head `aee7b0c0a4f8556c68ba4aeb88cf004a5e622849`;
- exact immutable b52 product source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`;
- target `main@1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- PR #29 open / mergeable;
- b53 allocated uniquely as `DEV-send-stream-0.1.0-b53`, `0.1.0 (53)`.

Confirmed writes:

1. Batch G recovery checkpoint;
2. exact b52 Runtime evidence file at commit `a95ea2bc6c463146afa94b1108717f85ab9b802d`;
3. atomic b53 product/config commit `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`.

Still pending:

4. verify exact b53 Push/PR CI, Artifact and package identity;
5. synchronize PR #29 and durable project docs;
6. hand exact b53 IPA to user for one reasoning/tool-style reproduction and diagnostics export.

Recovery rule: if interrupted, re-read this checkpoint and actual GitHub branch/PR/Artifact state; perform only missing deterministic writes. Never alter/rebuild b52. Once b53 Artifact exists, b53 is permanently reserved.

## Durable boundary

`ConversationRepository` remains sole native production conversation/response authority; `AuthSessionStore` remains auth owner; default persistent `WKWebsiteDataStore` remains persistent auth-secret authority. b48-b53 are diagnostic exceptions only. TD-024/TD-025 remain unchanged. No diagnostic result alone promotes hidden/shadow Web to production.

## Evidence ladder

- b51 Code/CI/Artifact/package: Passed; Runtime confirmed fresh-new-chat title-generation correction.
- b52 Code/CI/Artifact/package: Passed; Runtime **final answer complete / reasoning leading content incomplete**.
- b53 Code/config: Written atomically at `3204b183...`; CI/Artifact/Runtime pending.
- Phase 9 Stable/Frozen: No.

## Next exact action

Verify exact b53 CI for source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`. If CI/Artifact/package are valid, synchronize durable docs/PR and hand exact b53 IPA to the user. Runtime focus: one prompt that naturally produces visible reasoning plus tool activity; export diagnostics after terminal. Do not implement reasoning collapse/expand, tool sheet UI, reasoning lifecycle state or parser broadening until that evidence identifies the actual user-visible grammar.