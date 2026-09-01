# DEV-send-stream

## Status

**Active — b79 Runtime is partial-positive / partial-rejected. `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)` is allocated. The exact b80 patch has passed guarded exact-scope/static checks and Xcode 16.4 Simulator build; validated non-workflow product blobs are persisted on the tooling branch. Formal four-file product commit / Push+PR CI / canonical IPA / Runtime are still pending. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Formal feature head before this checkpoint write: `8e850233127fea29d954ad8fdda52abaeade575f`
- Current `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b79 product/config source: `a3d307b05d70e95568672bc29b0c939b7f3b8141`
- Allocated b80 Candidate / Version-Build: `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)`
- b39-b80 permanently reserved
- b79 Runtime/manual/real-device: **Partial / rejected**
- b80 Runtime/manual/real-device: **Not yet produced**
- Stable/Frozen Send: **No**

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-account-wide-web-notification-20260901.md`

## Resume / identity / conflict guard — 2026-09-01

The full resume guard was re-run after the tooling interruption.

- feature branch exists and still pointed to `8e850233127fea29d954ad8fdda52abaeade575f` before this checkpoint write;
- PR #29 remains open and targets `main`;
- `docs/project/current/dev/` on the selected branch contains only this Active Work checkpoint plus README, so no second Active branch/Candidate owner is present there;
- b80 was already allocated exactly once; do not allocate b81 until b80 Runtime is classified;
- `main` advanced from the previously recorded `d323b9eed2dda75b9986fc06e14014d3e9b365fb` to `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- compare of that main-only drift shows the net changed file is `docs/project/COMPOSER_PARITY_PLAN.md` only; no b80 product/config file or Send state owner overlaps;
- therefore the main drift does not invalidate the already-validated b80 product patch and does not require speculative product changes.

## Non-atomic b80 formalization recovery point

Known baseline before the write chain:

- formal feature head: `8e850233127fea29d954ad8fdda52abaeade575f`;
- validated tooling commit containing the three non-workflow b80 product blobs: `e3f03f7349b71287fc528c41169af4b9090d03d8`;
- guarded assembly run `33506668882`: **success**;
- exact workflow transformation is evidence-backed by `.github/scripts/b80_apply.py`: replace the two `DEV-send-stream-0.1.0-b79` identities in `.github/workflows/ios-foundation.yml` with `DEV-send-stream-0.1.0-b80` and make no other workflow change.

Intended write batches:

1. **This checkpoint recovery write** — records the verified identities and deterministic remaining chain.
2. **Formal b80 product commit** — create one tree/commit from this checkpoint head changing exactly four paths: `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`, `ChatGPTClient.xcodeproj/project.pbxproj`, `.github/workflows/ios-foundation.yml`; reuse the already-validated three non-workflow blobs and apply only the exact workflow identity replacement.
3. **Validation / Artifact** — verify exact diff/scope, observe formal Push + PR CI, obtain canonical b80 artifact, independently verify Release/Build/Candidate/source marker/Mach-O identity.
4. **Documentation sync** — update this checkpoint, durable build/runtime docs and PR metadata with the exact formal source/run/artifact identities before handing b80 to Runtime.

Confirmed completed before this recovery point:

- exact four-file patch assembled;
- prohibited-pattern/exact-scope/static checks passed;
- Xcode 16.4 Simulator build passed;
- the three non-workflow product blobs were persisted by tooling run `33506668882` / commit `e3f03f7349b71287fc528c41169af4b9090d03d8`.

Still remaining:

- formal b80 four-file source commit on `dev/send-stream-20260829`;
- formal Push CI and PR CI;
- canonical IPA and independent package identity verification;
- human real-device Runtime classification.

Recovery must **not** touch or allocate b81, add account-wide haptic/automatic Sync, polling/timer/retry/watchdog, duplicate Sync/Send, fake progressive final/typewriter, DOM/WebSocket body authority, Native resume/offset synthesis, a second response owner, Composer work, or unrelated refactors.

If execution is interrupted after this point, re-read this checkpoint and actual branch state and perform only the missing deterministic batch; do not replay a completed batch blindly.

## Exact b79 Runtime classification retained

### Tool presentation

**Partial positive / rejected.** Tool-operation prominence remains visible, but the final tool/timeline -> reasoning-divider boundary is still asymmetric because the terminal divider boundary has a separate geometry-owned spacing path instead of the neutral separator owner used between timeline items.

### Manual-Sync external re-arm

**Positive.** One explicit Sync that discovers a changed latest user turn re-arms/reloads the same covered official page once and allows page-owned reasoning/tool snapshots to be adopted before completion.

### External stopped-thinking semantics

**Positive.** External terminal-without-real-final preserves reasoning/tools instead of promoting reasoning into normal final body text.

### Cross-platform streaming boundary

**Reasoning/tools: page-snapshot granular only.** Tool/service-message structure advances, but this is not token/SSE-delta reasoning streaming.

**Progressive final: unavailable from the current authorized source.** No fake typewriter, Native polling/cadence, DOM-body authority or WebSocket-body authority is justified.

### COMPLETE/final-materialization race

**Rejected; root cause localized.** Page `COMPLETE` can arrive while `reasoningEnded == true` and `finalText.isEmpty`. b79 then terminalizes/releases the covered executor before the final assistant message materializes in authoritative Detail, so the later final can be missed until another manual Sync.

### Large-conversation Sync latency

One supplied Detail Sync transferred roughly 2.2 MB and took about 10.27 seconds. This is a separate latency source and does not explain the missing-final race above.

## Account-wide official completion/new-answer signal evidence

User Runtime evidence establishes that official iOS can emit a two-stage haptic for another account conversation and official PC Web can remain on conversation A while a never-opened conversation B completes and still show an upper-right new-answer notification.

This supports the existence of an account-wide completion/new-answer signal in the official Web runtime, but its exact transport, event schema, conversation identity field, covered-WKWebView observability and foreground/background delivery semantics remain **Unknown / Unverified**.

This is not b80 implementation scope. Do not infer WebSocket/APNs/service-worker semantics and do not imitate the signal with polling/timers.

## Exact b80 product scope

Only these changes are authorized:

1. **Final timeline/tool -> reasoning-divider spacing:** use the same neutral separator representation for the terminal expanded-timeline boundary; remove the separate pre-divider spacing owner; do not increase the 36-point tool line height.
2. **Normal external COMPLETE materialization gate:** if page-owned `complete=true` arrives with `reasoningEnded == true` but `finalText` still empty, keep the same covered page observation alive rather than terminalizing/releasing. Terminal normally when a real final body appears. Preserve the b79-positive stopped-thinking case where reasoning did not end and no final exists.
3. **Bridge ownership correction:** do not clear page-owned external observation state merely because the first COMPLETE-associated plural snapshot was posted; Native release remains the terminal owner.
4. **Identity-only b80 changes:** Xcode Build 80/Candidate b80 and workflow artifact identity.

Expected exact product/config scope: `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`, `ChatGPTClient.xcodeproj/project.pbxproj`, `.github/workflows/ios-foundation.yml`.

## Validation state before formal product commit

- Code patch assembled: **Yes**
- Static/exact scope/prohibited-pattern guard: **Passed**
- Xcode 16.4 Simulator build: **Passed**
- Formal b80 product source commit: **Pending**
- Push CI: **Pending**
- PR CI: **Pending**
- Artifact/package: **Pending**
- Runtime/manual/real-device: **Pending**

The earlier tooling persistence failure was a GitHub Actions workflow-permission limitation, not a product-source or Xcode failure.

## Retained architecture / protocol boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response owner.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned observation transport only, not a second message store.
- b67 local protected Send and b72 simultaneous ownership remain accepted predecessors.
- b79 manual-Sync re-arm and stopped-thinking semantics are positive predecessors to preserve.
- No Native polling/cadence, Native resume/offset synthesis, duplicate Send, retry/timer/watchdog, guessed fallback, fake final streaming, DOM-body authority or WebSocket-body authority.

## Next exact action

1. Create and fast-forward the formal exact four-file b80 product commit from this checkpoint head.
2. Verify the formal diff contains only the four authorized product/config paths and the expected b80 changes.
3. Observe formal Push + PR CI, obtain the canonical b80 IPA, independently verify package identity, and update checkpoint/durable docs/PR in the same round.
4. Human Runtime gate: verify symmetric final tool/divider spacing; verify a normal remote response no longer terminalizes before final materialization; preserve stopped-thinking + manual-Sync re-arm positives. Progressive final token streaming remains an open protocol gap.
5. After b80 Runtime classification, separately run the privacy-safe account-signal Web Rule Lab probe before implementing account-wide haptic/automatic Sync.

Do not claim CI/Artifact success as Runtime success.
