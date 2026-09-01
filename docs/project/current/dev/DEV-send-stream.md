# DEV-send-stream

## Status

**Active — b82 Runtime remains Partial. Passive official Web is Runtime Rejected. Official iOS static evidence proves a separate topic-based realtime layer. A research-only Foundation WebSocket observer has been written and CI-built; it now includes an in-app `Probe` export button so Filza is not required. Exact registration/topic/current-account behavior is still Runtime Pending; therefore b83 remains unallocated. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main` last verified: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b82 product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Candidate: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- Canonical b82 Artifact: `9811406038`
- b82 IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- b39-b82 permanently reserved
- b83: **not allocated**
- Stable/Frozen Send: No

## Current accepted Runtime evidence

### b82

b82 automatically acquires a completed remote turn without manual Sync, but the first exact-conversation user-socket `targetMatch=true` frame arrived only when authoritative Detail already advanced `8 -> 10`. No earlier socket frame, external snapshot or Repository live response was observed during generation. Therefore that socket event is accepted only as a completion/update hint for the tested flow, not a request-start/live-stream signal.

### Visible official Web

The user tested official ChatGPT Web already open on the same conversation before a remote long turn. It did not automatically show the remote user row, live response, or even the completed turn without explicit refresh/navigation. Passive page visibility/focus is therefore rejected as the missing acquisition mechanism.

## Official iOS static realtime architecture

The supplied official package (`com.openai.chat` 1.2026.202 / build 30140022279) exposes static native models/services including:

- `WebSocketRegisterResponse.websocketURL`;
- `WebSocketTopic(topicId, offset)`;
- `SubscribePayload(topicId, lastOffset, recovered, catchups)`;
- `connect`, `subscribe`, `presence`;
- topic `catchup` / `live`, `message` / `reply` semantics;
- `WebSocketConversationEventsService` / `WebSocketConversationObserver`;
- `conversation-update`, `add-messages`, title/async-status/task/stop updates;
- `ConversationPollingManager` with bounded/state-aware termination diagnostics.

This proves official iOS has a separate native realtime layer. It does not prove the exact current network contract.

The supplied research package already contains a TrollFools-style injection chain (`CydiaSubstrate.framework`, `.troll-fools`, existing `ChatGPTEnhancer` dylib). The official framework remains an evidence oracle, not a product dependency.

## Research realtime Probe

Research source/tooling:

- `scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m`
- `scripts/research/official_ios_realtime_probe/ProbeExportUI.m`
- `scripts/research/official_ios_realtime_probe/build_probe.sh`
- `scripts/research/official_ios_realtime_probe/README.md`
- `.github/workflows/research-official-ios-realtime-probe.yml`

### Latest exact research identity

- Research source head: `a1d6ca0be8099a0e36c04ebecb649a31be5b48b9`
- Workflow: `Research Official iOS Realtime Probe`
- Run: `33553941529` — **success**
- Artifact ID: `9818535820`
- Artifact: `ChatGPTRealtimeProbe-a1d6ca0be8099a0e36c04ebecb649a31be5b48b9`
- Artifact ZIP digest: `sha256:37068668207a813b66b661c20ee7e040f2abe7628523d237656f8cad632dd9b8`
- Exact dylib SHA-256: `85782137ddce0fdab022805f2f822ed6ce5f50beefab4c446c97007bcf5d19c7`
- Exact dylib size: `134896` bytes

Build, Mach-O validation and Artifact upload passed. This is **CI/Artifact evidence only**, not Runtime proof.

### Probe privacy boundary

The Probe records only privacy-safe structure:

- likely realtime registration HTTP method/path/status and response JSON key names;
- WebSocket host/path plus query presence/count, never signed query values;
- outbound command/frame keys, command type, safe symbolic topic, offset value class;
- inbound frame/payload keys, event/update type, message count and short SHA-256 conversation identity hash;
- transport error domain/code.

It does not intentionally record Cookie/Authorization/token/challenge values, request/response body text, prompt/answer/reasoning/tool text or raw conversation IDs.

### TrollStore-only device adaptation

The target phone has TrollStore but no jailbreak/Filza. The Probe now links UIKit and adds a small `Probe` button to the active official ChatGPT window. Tapping it shares `ChatGPTRealtimeProbe.jsonl` through the normal iOS share sheet, so Filza and app file-sharing entitlements are not required.

A visible `Probe` button would prove only that the research dylib/UI constructor loaded. The JSONL is still required to prove the WebSocket hook observed the relevant protocol.

If the device has only TrollStore itself and no separate dylib-injection entry, do not ask for jailbreak/Filza. TrollStore alone is not a generic dylib injector. The next exact packaging action is a research-only TrollStore-installable official-app test IPA based on the user-supplied decrypted package, wiring this exact Probe into the package's existing research injection chain while preserving the existing ChatGPTEnhancer behavior.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-build-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-export-ui-20260902.md`

## Product decision for official-package use

The official package is an **evidence oracle**, not a product dependency.

Allowed research use:

- static reflection/string/type/state-machine analysis;
- research-only runtime instrumentation of the supplied official app to observe exact network structure;
- compare current official behavior with our own implementation.

Rejected product route:

- embed/link/call official `ChatGPT.framework` from ChatGPTClient;
- redistribute official internal code/framework as our dependency;
- depend on official DI containers/private Swift ABI for product state;
- let official WebSocket service become a second conversation/auth/response owner.

After exact Runtime evidence, reimplement only the minimum verified protocol in our own Swift/Foundation code.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole response/content owner.
- `AuthSessionStore` remains sole native auth/account owner; default persistent WebKit store remains sole persistent auth-secret owner.
- no duplicate Send/resend, fake stream, speculative retry/watchdog/fallback or second response store.
- WebSocket payload bodies do not become product message authority until exact Runtime evidence proves completeness/identity/branch/lifecycle semantics.

## Integration direction if native topic path is confirmed

Preferred product shape:

`AuthSessionStore verified transient context -> our URLSession / URLSessionWebSocketTask -> verified registration + topic subscription -> realtime event -> existing ConversationRepository acquisition/response owner`.

Initially use native WebSocket events as notification/state triggers and keep existing Detail/SSE/resume/plural paths authoritative for message/reasoning/final content. Promote WebSocket content only after separate exact evidence.

If native topic subscription cannot be reproduced under the accepted auth boundary, explicitly design the bounded selected-conversation status-monitor branch using official `ConversationPollingManager` evidence. Do not add hidden fixed polling.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 7**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

**Do not allocate b83 yet.**

Because the user's phone has only TrollStore and no Filza, first determine whether the existing device setup has a dylib-injection entry. If it does, inject exact Probe SHA `85782137ddce0fdab022805f2f822ed6ce5f50beefab4c446c97007bcf5d19c7`, fully relaunch official ChatGPT, confirm the visible `Probe` button, run one long cross-platform turn, then export `ChatGPTRealtimeProbe.jsonl` through the Probe button.

If the device truly has TrollStore only and no dylib-injection tool, package a research-only TrollStore-installable official ChatGPT test IPA from the user-supplied decrypted package with the Probe already wired into its existing research injection chain. Preserve existing ChatGPTEnhancer behavior. This packaging is research tooling only and must not consume b83.

The decisive protocol evidence remains whether a target-matching `conversation-update`, `add-messages`, async-status or per-turn subscription event arrives before completion, plus exact registration path and subscribe framing.
