# DEV-send-stream

## Status

**Active — b82 Runtime remains Partial. Passive official Web is Runtime Rejected. Official iOS static evidence proves a separate topic-based realtime layer, and a research-only Foundation WebSocket observer has now been written, compiled with the iOS SDK, validated as a Mach-O dylib and produced as a unique workflow Artifact. Exact registration/topic/current-account behavior is still Runtime Pending; therefore b83 remains unallocated. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Branch head before this checkpoint write: `549a551fef56a99d620b85dc8c9fccbc59a4e3a5`
- Actual `main` verified this round: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
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

Whole-package inspection also proves the supplied research package already contains a TrollFools-style injection chain (`CydiaSubstrate.framework`, `.troll-fools`, existing `ChatGPTEnhancer` dylib). The official framework remains an evidence oracle, not a product dependency.

## Research realtime probe — ready for Runtime injection

Research source/tooling:

- `scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m`
- `scripts/research/official_ios_realtime_probe/build_probe.sh`
- `scripts/research/official_ios_realtime_probe/README.md`
- `.github/workflows/research-official-ios-realtime-probe.yml`

Research source/workflow head:

- `501839a8aad91373c2a90397c08cf84251553f41`

CI / Artifact:

- Workflow: `Research Official iOS Realtime Probe`
- Run: `33552727671` — **success**
- Job: `100005909674`
- `Build research dylib`: success
- `Validate research artifact`: success
- `Upload research probe`: success
- Artifact ID: `9818074442`
- Artifact: `ChatGPTRealtimeProbe-501839a8aad91373c2a90397c08cf84251553f41`
- Artifact ZIP digest: `sha256:220c19a6074ca2678b3a70c30fe60bfda257be3df3cb1a607d995665d06ec056`
- Exact dylib SHA-256: `7b449f91bc903fa56216d142f2373c0f0c94065271ba7a7160aae0a0f5c4b6ff`
- Exact dylib size: `112352` bytes

Downloaded Artifact re-verification reproduced the exact dylib SHA above.

The dylib links only system Foundation / Objective-C / System / CoreFoundation libraries. It does **not** link `ChatGPT.framework`, CydiaSubstrate or ChatGPTEnhancer.

### Probe observation boundary

The probe records only privacy-safe structure:

- likely realtime registration HTTP method/path/status and response JSON key names;
- WebSocket host/path plus query presence/count, never signed query values;
- outbound command/frame keys, command type, safe symbolic topic, offset value class;
- inbound frame/payload keys, event/update type, message count and short SHA-256 conversation identity hash;
- transport error domain/code.

It does not intentionally record Cookie/Authorization/token/challenge values, request/response body text, prompt/answer/reasoning/tool text or raw conversation IDs. Post-build string spot-check found none of the sensitive/body logging tokens checked.

Durable build evidence:

- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-build-20260902.md`

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

## Integration direction if the native topic path is confirmed

Preferred product shape:

`AuthSessionStore verified transient context -> our URLSession / URLSessionWebSocketTask -> verified registration + topic subscription -> realtime event -> existing ConversationRepository acquisition/response owner`.

Initially use native WebSocket events as notification/state triggers and keep existing Detail/SSE/resume/plural paths authoritative for message/reasoning/final content. Promote WebSocket content only after separate exact evidence.

If the native topic subscription cannot be reproduced under the accepted auth boundary, explicitly design the bounded selected-conversation status-monitor branch using official `ConversationPollingManager` evidence. Do not add hidden fixed polling.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 5**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action — Human Runtime Gate

Do **not** allocate b83 yet.

Inject the exact research dylib SHA `7b449f91bc903fa56216d142f2373c0f0c94065271ba7a7160aae0a0f5c4b6ff` into the supplied official ChatGPT TrollStore app as an additional TrollFools dylib. Keep the existing ChatGPTEnhancer injection.

Then:

1. fully terminate and relaunch official ChatGPT;
2. verify `ChatGPTRealtimeProbe.jsonl` is created and contains `probe.loaded` / `probe.hooks_installed`;
3. keep target conversation A available;
4. from another platform, send one deliberately long text turn to A;
5. do not manually refresh A during generation;
6. after completion, provide only `ChatGPTRealtimeProbe.jsonl` for analysis.

The decisive evidence is whether a target-matching `conversation-update`, `add-messages`, async-status or per-turn subscription event arrives before completion, plus the exact registration path and subscribe framing observed on the current account/version.

If probe loading fails, do not alter product code or allocate b83; first diagnose injection/load/hook execution only.
