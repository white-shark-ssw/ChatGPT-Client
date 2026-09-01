# DEV-send-stream

## Status

**Active — exact b78 Runtime is now partial-positive / partial-rejected. The next evidence-backed product candidate is b79, but b79 is not yet allocated at this checkpoint. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal branch head before this b78 Runtime evidence sync: `16df79333b8d50879e227b4696262e445424fcef`
- Clean b78 product commit: `180065e0faf947292a9f21b56c4ea366a5c322fe`
- Exact b78 product/config source: `031b1a1f2c1d01900c2ab79ff14b1f2fb6c7e809`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b78` / `0.1.0 (78)`
- Final b78 Xcode validation: `33482721335 / 99775722851` — success
- Formal Push CI: `33482983693 / 99776545604` — success
- Formal PR CI: `33482987997 / 99776557269` — success
- Canonical Push Artifact: `9790836559`
- Artifact ZIP SHA: `7b5900a960ef680cce34642ca6cef232f201a260b182d6b640266e81982b081f`
- IPA SHA: `726e3c09bcac4eb8a40a8ecb79b8abb0f145d89e41481083bc51941a7978620e`
- b39-b78 permanently reserved
- Runtime/manual/real-device b78: **Partial / rejected**
- Stable/Frozen Send: **No**

Durable b78 evidence: `docs/project/runtime-evidence/DEV-send-stream-b78-device-runtime-20260901.md`.

## Resume / identity / conflict guard

This remains the continuously selected Work. The current Runtime classification was made against the exact canonical b78 package: supplied diagnostics identify Build 78 / Candidate `DEV-send-stream-0.1.0-b78` / source marker `031b1a1f2c1d`.

Immediately before staging the next correction:

- formal branch was `dev/send-stream-20260829` at `16df79333b8d50879e227b4696262e445424fcef` before the new evidence-only docs commit;
- PR #29 remained open / mergeable / unmerged;
- PR base remained `main` at `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- `docs/project/current/dev/` contained only this Active task checkpoint plus README, so no parallel Active task conflict was found on the feature branch;
- exact repository search found no `DEV-send-stream-0.1.0-b79`, so b79 remained unallocated at this checkpoint.

## b78 Runtime evidence now accepted

### Tool presentation

**Partial positive / partial rejected.** b78's stronger tool-operation styling and larger operation line height are visibly active. The remaining asymmetry is source-localized: timeline separators inherit the previous item's paragraph style, so reasoning -> tool uses the reasoning line height while tool -> next uses the tool line height. Inter-item spacing still lacks one neutral owner.

### User-message integrity

**Positive for the supplied long-message clipping case.** The prior b77 mid-text truncation is no longer reproduced; the supplied long user bubble reaches its final line and link styling is present. Broader pixel-level official rendering parity is not promoted to Stable by this one screenshot.

### Cross-platform external response

**Thinking/reasoning/tools remain available only at page-owned snapshot granularity.** In the captured b78 run, external snapshots advance reasoning from 131 to 260 characters and tool count from 2 to 8 in coarse page-owned updates. This is not SSE/token-delta reasoning streaming.

**Final body remains rejected as progressive streaming.** Repeated final-phase snapshots stay at `finalCharacters=0`, then jump directly to the complete body (`7006` characters in the captured run) at terminal. Current evidence still authorizes no progressive final source, no fake typewriter, no Native polling/cadence, no DOM body and no WebSocket body.

### Already-open conversation + new external turn

**Rejected; root cause localized.** When Native is already displaying the conversation and another platform starts a new turn, explicit Sync can add the new user message but no external live response starts. Diagnostics show the already-loaded covered page emits no new `externalStreamingObserved` lifecycle until the page is freshly entered/reloaded. Current `observeExistingConversation` only calls `probeComposer(true)` when the page is already on the same conversation; it does not re-enter/reload the official page.

The minimum allowed correction is event-driven from explicit manual Sync: if Sync discovers a new latest user turn and no Native live response is active, re-arm/reload that same covered page once. This is not automatic polling.

### External manual stop

**Rejected; exact root cause identified.** Immediately before terminal, the external response has `reasoningCharacters=263`, `finalCharacters=0`, four tools. At terminal the current fallback converts that reasoning into `finalCharacters=265` and removes reasoning, which matches the user's wrong Native screenshot. For `external_page_owned` responses (`promptText` empty), terminal-without-real-final must preserve reasoning/tool state. The b67 local protected-Send compatibility fallback remains unchanged.

### Relaunch Detail lifecycle

The permanent b77 zombie `detail.coalesced` failure is not reproduced in the supplied b78 run and multiple Detail operations reach terminal HTTP200. The exact b77 concurrent list-403 + Detail cancellation condition was not clearly reproduced, so the fix is not negatively contradicted but is not re-qualified under the identical failure condition.

## Automatic Sync — answer boundary only

Automatic Sync is technically feasible, but it is **not part of the next product scope**. A fixed timer/poll/watchdog is not authorized. Preferred future design is event-driven from a proven page-owned/lifecycle signal. Current b78 evidence shows an already-loaded covered page does not emit a reliable signal when a new turn begins elsewhere, so truly automatic instant Sync needs more protocol evidence first.

## Retained architecture / protocol boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned observation transport only; it is not a second conversation/message store.
- b67 local Native Send -> one protected official Web Send -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile remains Runtime accepted.
- b72 tested A-generating + B-send/generate ownership remains Runtime positive.
- `assistant:thoughts` / inline COT remain non-presentational.
- No Native polling/cadence, Native resume/offset synthesis, duplicate Send, retry/timer/watchdog, guessed fallback, compatibility shim, second response owner, fake final streaming, DOM-body authority or WebSocket-body authority.

## Evidence-backed b79 scope — not yet allocated at this checkpoint

Only these product changes are authorized by b78 Runtime:

1. **Deterministic inter-item tool/reasoning spacing:** transition spacing must have one neutral owner rather than inherit the preceding reasoning/tool line height.
2. **Manual-Sync external re-arm:** after an explicit successful `同步最新消息` detects a newly changed latest user turn while no live response is active, re-enter/reload the existing covered official page once for that same conversation so its own page-owned `stream_status` / plural read behavior can discover an active remote response.
3. **External stopped-thinking terminal semantics:** an external-page-owned terminal with no actual final body must not promote reasoning into final. Preserve reasoning/tools; retain local protected-Send fallback behavior.
4. **No progressive-final invention and no automatic Sync implementation.**

Expected minimum source scope after exact call-site inspection: `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`, plus identity-only Xcode/workflow changes if b79 is allocated.

## Exact next action

1. Re-check formal branch / PR / main base and exact b79 non-use immediately before allocation.
2. Allocate `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)` once.
3. Implement only the three evidence-backed corrections above.
4. Run exact-scope/static checks and Xcode 16.4 Simulator build through the guarded assembly path.
5. If assembly passes, transplant the clean product commit to the formal feature branch, run Push + PR CI, produce and independently verify the canonical IPA, then update this checkpoint and durable project status in the same round.
6. Human Runtime gate: verify symmetric tool spacing, manual-Sync re-arm of a newly-started remote turn, stopped-thinking no longer rendered as final, and retained b67/b72 behavior where practical.

Do not claim CI/Artifact success as Runtime success.
