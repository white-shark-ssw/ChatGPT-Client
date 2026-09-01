# DEV-send-stream

## Status

**Active — b79 Runtime is partial-positive / partial-rejected. `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)` is allocated and its exact four-file patch has passed guarded exact-scope/static checks plus Xcode 16.4 Simulator build, but formal product persistence / Push+PR CI / Artifact are still pending. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b79 product/config source: `a3d307b05d70e95568672bc29b0c939b7f3b8141`
- Allocated b80 Candidate / Version-Build: `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)`
- b39-b80 permanently reserved
- b79 Runtime/manual/real-device: **Partial / rejected**
- b80 Runtime/manual/real-device: **Not yet produced**
- Stable/Frozen Send: **No**

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-account-wide-web-notification-20260901.md`

## Resume / identity / conflict guard

Before b80 allocation, the feature branch / PR / `main` / candidate non-use guard was clean and no parallel Active Work conflict was found. b80 was allocated exactly once. The latest formal branch before the new Web-evidence docs commit was `15ac2afb9d78a4f0c50ac8dc8abf7e9ca3e2da66`; the account-wide Web evidence commit then advanced docs only. Re-run the light branch/PR/base guard immediately before formalizing the b80 product commit.

Do not allocate b81 until b80 Runtime is classified.

## Exact b79 Runtime classification

### Tool presentation

**Partial positive / rejected.** Tool-operation prominence remains visible, but the final tool/timeline -> reasoning-divider boundary is still asymmetric because the terminal divider boundary has a separate geometry-owned spacing path instead of the same neutral separator owner used between timeline items.

### Manual-Sync external re-arm

**Positive.** One explicit Sync that discovers a changed latest user turn re-arms/reloads the same covered official page once and allows page-owned reasoning/tool snapshots to be adopted before completion.

### External stopped-thinking semantics

**Positive.** External terminal-without-real-final preserves reasoning/tools instead of promoting reasoning into normal final body text.

### Cross-platform streaming boundary

**Reasoning/tools: page-snapshot granular only.** Tool/service-message structure advances, but this is not token/SSE-delta reasoning streaming.

**Progressive final: unavailable from the current authorized source.** Final characters stayed zero through the observed final phase. No fake typewriter, Native polling/cadence, DOM-body authority or WebSocket-body authority is justified.

### COMPLETE/final-materialization race

**Rejected; root cause localized.** Page `COMPLETE` can arrive while `reasoningEnded == true` and `finalText.isEmpty`. b79 then terminalizes/releases the covered executor before the final assistant message has materialized in authoritative Detail. The immediate reconcile can still show no new assistant message, and the later final is then missed until another manual Sync.

### Large-conversation Sync latency

One supplied Detail Sync transferred roughly 2.2 MB and took about 10.27 seconds. This explains a separate short-lived `正在同步最新消息…` delay, but not the later missing-final case above.

## Account-wide official completion/new-answer signal evidence

Two user Runtime observations now align:

1. Official iOS can emit a two-stage haptic when **any** account conversation completes even while another screen/conversation is visible.
2. Official PC Web can remain on conversation A; even if conversation B has never been opened in that browser session, when B produces a new answer the Web UI shows an upper-right notification bubble.

The second observation materially upgrades the evidence: **an account-wide new-answer/completion signal exists inside the official Web runtime and is not inherently tied to the currently open conversation page or to having opened the target conversation first.**

Still Unknown / Unverified:

- exact transport/mechanism;
- exact event schema;
- whether it carries a usable conversation identifier directly;
- whether the same account-level signal is observable under this app's covered `WKWebsiteDataStore.default()` runtime;
- foreground/background iOS delivery semantics.

Architecture consequence: automatic Sync + completion haptic is now a stronger evidence-backed direction, but **not yet an implementation scope**. A future privacy-safe Web Rule Lab capture should keep official Web on A while B completes and identify the actual account-level event source. If proven, one deduplicated accepted event may drive both a haptic and one bounded authoritative list/detail refresh without polling.

Do not infer WebSocket/APNs/service-worker semantics from the UI notification alone. Do not add timer/poll/watchdog imitation.

## Exact b80 product scope

Only these changes are authorized:

1. **Final timeline/tool -> reasoning-divider spacing:** use the same neutral separator representation for the terminal expanded-timeline boundary; remove the separate pre-divider spacing owner; do not increase the 36-point tool line height.
2. **Normal external COMPLETE materialization gate:** if page-owned `complete=true` arrives with `reasoningEnded == true` but `finalText` still empty, keep the same covered page observation alive rather than terminalizing/releasing. Terminal normally when a real final body appears. Preserve the b79-positive stopped-thinking case where reasoning did not end and no final exists.
3. **Bridge ownership correction:** do not clear page-owned external observation state merely because the first COMPLETE-associated plural snapshot was posted; Native release remains the terminal owner.
4. **Identity-only b80 changes:** Xcode Build 80/Candidate b80 and workflow artifact identity.

Explicitly excluded from b80:

- account-wide haptic / automatic Sync implementation;
- timer/poll/retry/watchdog;
- duplicate Sync/Send;
- fake progressive final/typewriter;
- DOM-body or WebSocket-body authority;
- Native resume/offset synthesis;
- second response owner or unrelated refactor.

Expected exact product/config scope: `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`, `ChatGPTClient.xcodeproj/project.pbxproj`, `.github/workflows/ios-foundation.yml`.

## b80 assembly evidence so far

Guarded tooling run `33503820103`:

- exact four-file patch applied: **Passed**
- `git diff --check` / exact scope / prohibited-pattern guard: **Passed**
- Xcode 16.4 Simulator build: **Passed**
- validated product commit persistence: **Failed only at GitHub push permission**, because the Actions token was not allowed to update `.github/workflows/ios-foundation.yml` without `workflows` permission

Therefore:

- Code patch assembled: **Yes**
- Static/exact scope: **Passed**
- Xcode 16.4 Simulator: **Passed**
- Formal b80 product source commit: **Pending**
- Push CI: **Pending**
- PR CI: **Pending**
- Artifact/package: **Pending**
- Runtime: **Pending**

The tooling persistence failure is not product-code or Xcode failure.

## Retained architecture / protocol boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response owner.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned observation transport only, not a second message store.
- b67 local protected Send and b72 simultaneous ownership remain accepted predecessors.
- b79 manual-Sync re-arm and stopped-thinking semantics are positive predecessors to preserve.
- No Native polling/cadence, Native resume/offset synthesis, duplicate Send, retry/timer/watchdog, guessed fallback, fake final streaming, DOM-body authority or WebSocket-body authority.

## Next exact action

1. Re-check formal branch / PR / `main` base after this docs-only evidence update.
2. Persist the already-validated three non-workflow product blobs from the guarded assembly path, apply `.github/workflows/ios-foundation.yml` b80 identity through the GitHub connector, and formalize one exact four-file b80 product/config commit.
3. Run formal Push + PR CI, produce the canonical b80 IPA, independently verify Release/Build/Candidate/source marker/Mach-O identity, and update checkpoint/durable docs/PR in the same round.
4. Human Runtime gate: verify symmetric final tool/divider spacing; verify a normal remote response no longer terminalizes before final materialization; preserve stopped-thinking + manual-Sync re-arm positives; progressive final token streaming remains an open protocol gap.
5. Separately, after b80 Runtime classification, use a privacy-safe Web Rule Lab account-signal probe on A while B completes before implementing account-wide haptic/automatic Sync.

Do not claim CI/Artifact success as Runtime success.
