# DEV-send-stream

## Status

**Active — exact b79 is Code/static/Simulator/Push+PR CI/Artifact/package verified and is now at the real-device Human Runtime gate. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal b79 product/config source: `a3d307b05d70e95568672bc29b0c939b7f3b8141`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)`
- Guarded staging validation: `33488975445 / 99795672696` — exact scope + `git diff --check` + Xcode 16.4 Simulator passed
- Formal Push CI: `33489654106 / 99797864816` — success
- Formal PR CI: `33489658656 / 99797878467` — success
- Canonical Push Artifact: `9793240789`
- Artifact ZIP SHA: `2016508002ae7ff43d803c90fcbb92ba01c45906c885be6f6e50a1e43e1e87fc`
- IPA: `ChatGPTClient-0.1.0-b79-dev-send-stream.ipa`
- IPA SHA: `39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`
- Independent package inspection: Release `0.1.0 (79)`, Candidate b79, source marker `a3d307b05d70`, MinimumOSVersion 14.0, Mach-O arm64
- b39-b79 permanently reserved
- Runtime/manual/real-device b79: **Pending / Unverified**
- Stable/Frozen Send: **No**

Durable predecessor Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b78-device-runtime-20260901.md`.

## Resume / identity / conflict guard

The selected Work remains `DEV-send-stream`. Immediately before b79 formal assembly:

- feature branch was `dev/send-stream-20260829` at `b88c5269cfd0fb4e76f3a19ee4475cd03785a753`;
- PR #29 remained open / mergeable / unmerged and based on `main`;
- `main` remained `d323b9eed2dda75b9986fc06e14014d3e9b365fb`, so no target/base drift occurred;
- b79 had been allocated by the evidence-only checkpoint commit and no parallel Active checkpoint conflict was found;
- the formal b79 product diff from `b88c...` to `a3d307...` is exactly four files: `ChatGPTClient/RootViewController.swift`, `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient.xcodeproj/project.pbxproj`, `.github/workflows/ios-foundation.yml`.

## b78 Runtime evidence accepted as the b79 basis

1. **Tool presentation partial-positive / spacing rejected.** Tool operation prominence/line-height was visibly active, but reasoning -> tool and tool -> next spacing differed because the separator inherited the preceding paragraph style.
2. **User-message clipping focused positive.** The supplied long link-bearing message was no longer truncated; this did not promote full official-rendering parity to Stable.
3. **Cross-platform reasoning/tools only page-snapshot granular.** External snapshots changed reasoning/tool state, but not at SSE/token-delta cadence.
4. **Progressive external final rejected.** Final remained zero characters across repeated snapshots and then jumped to the full body at terminal. No fake typewriter, polling, DOM-body or WebSocket-body authority is allowed.
5. **Already-open new external turn rejected.** Manual Sync could reveal the new user turn but the already-current covered page was not re-entered/reloaded, so no new page-owned external-response lifecycle started.
6. **External manual stop rejected.** The terminal fallback promoted external reasoning into final body text when no real final existed.

## Exact b79 product corrections

### 1. Deterministic reasoning/tool transition spacing

Reasoning and tool paragraphs no longer own inter-item spacing. A neutral 12-point separator owns each inter-item transition, so reasoning -> tool and tool -> next no longer depend on the preceding item's line height.

### 2. Explicit manual-Sync external re-arm

After an explicit successful `同步最新消息`, if the authoritative Detail shows a changed latest user turn, the same conversation is still selected, and no Repository live response is active, Native forces one reload/re-arm of the already-current covered official page. The page still owns its own `stream_status` / plural conversation reads and any resume behavior.

This is event-driven from the user's explicit Sync. It is **not** automatic polling and adds no retry/timer/watchdog/cadence.

### 3. External stopped-thinking semantics

`external_page_owned` terminal-without-real-final no longer promotes reasoning into final. Reasoning/tools are preserved, the live body is empty rather than synthesized, copy is suppressed for the empty body, and the reasoning disclosure title becomes `已停止思考`.

The b67 local protected-Send compatibility fallback remains unchanged for local responses.

## Retained architecture / protocol boundaries

- `ConversationRepository` remains sole production conversation/list/detail/recovery/response owner.
- `AuthSessionStore` remains sole native auth/account owner; `WKWebsiteDataStore.default()` remains sole persistent browser auth-secret authority.
- Covered official Web remains challenge/protected-Send/page-owned observation transport only, not a second message store.
- b67 local protected Send and b72 tested simultaneous ownership remain accepted predecessors.
- `assistant:thoughts` / hidden COT remain non-presentational.
- No Native polling/cadence, Native resume/offset synthesis, duplicate Send, retry/timer/watchdog, guessed fallback, compatibility shim, second response owner, fake final streaming, DOM-body authority or WebSocket-body authority.

## Automatic Sync boundary

Automatic Sync is technically feasible but remains **not implemented**. Current evidence does not justify a fixed timer/poll/watchdog. A future implementation should be event-driven from a proven page-owned/lifecycle signal; the b78 evidence specifically showed the already-loaded page does not reliably emit the needed new-turn signal by itself.

## Human Runtime gate — exact b79

Install the canonical b79 IPA and test the following on the primary iPhone/iOS17 device:

1. **Tool spacing:** use a response containing reasoning + multiple tool rows and confirm the vertical gap above and below each tool operation is visually symmetric/consistent.
2. **Already-open remote turn:** keep Native inside conversation A, start a long response for A on another platform, then tap `同步最新消息` once while the remote response is still active. Confirm the new user turn appears and Native then adopts page-owned thinking/reasoning/tools without waiting for server completion. Do not send from Native in this test.
3. **External manual stop:** start a remote response, stop it while still thinking, then Sync/re-arm as needed. Confirm Native preserves the stopped reasoning/tools under `已停止思考` and does not render the reasoning text as normal final body text.
4. **Progressive final observation:** note whether final body still appears only at terminal. b79 does not claim to fix progressive final streaming.
5. **Regression where practical:** one normal local Native Send still follows the b67 protected-Send HTTP200 SSE path; b72-style A-generating + B-send/generate ownership remains correct.
6. Export diagnostics after tests 2/3 even if they pass.

## Evidence classification

- Code written: **Yes**
- Static/exact scope checks: **Passed**
- Xcode 16.4 Simulator build: **Passed**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced: **Yes**
- Package identity independently verified: **Yes**
- Runtime/manual/real-device b79: **Pending / Unverified**
- Stable/Frozen Send: **No**

## Next exact action

Human Runtime-test the exact canonical b79 package above and return screenshots/diagnostics for the tool-spacing, already-open remote-turn manual-Sync re-arm, and externally stopped-thinking cases. Do **not** allocate b80 before b79 Runtime evidence is classified. If b79 passes those scopes, continue from the remaining proven gap: external progressive final still lacks an authorized incremental source, plus any regression that the b79 Runtime actually reproduces.
