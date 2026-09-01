# DEV-send-stream

## Status

**Active — b82 Runtime remains Partial. Passive official Web is now Runtime Rejected as an early or guaranteed completion refresh source. Static analysis of the user-supplied official iOS package proves a separate native topic-based WebSocket conversation layer and a bounded polling manager, but the exact registration URL/topic/auth/offset contract remains Unverified. Whole-package inspection found no ordinary literal `/backend-api/celsius/ws/user`; the supplied TrollStore research package already contains a usable dylib injection chain, so the next evidence path is runtime observation of the official app rather than borrowing its framework. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Branch head before this checkpoint write: `040f69844f0a95eb5f3ed7c4ea7370c8d71bd7ea`
- Actual `main` last verified: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b82 product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Candidate: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- Canonical Artifact: `9811406038`
- IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- b39-b82 permanently reserved
- b83: **not allocated**
- Stable/Frozen Send: No

## Current accepted evidence

### b82

b82 automatically acquires a completed remote turn without manual Sync, but the first exact-conversation user-socket `targetMatch=true` frame arrived only when authoritative Detail already advanced `8 -> 10`. No earlier socket frame, external snapshot or Repository live response was observed during generation. Therefore that socket event is accepted only as a completion/update hint for the tested flow, not a request-start/live-stream signal.

### Visible official Web

The user tested official ChatGPT Web already open on the same conversation before a remote long turn. It did not automatically show the remote user row, live response, or even the completed turn without explicit refresh/navigation. Passive page visibility/focus is therefore rejected as the missing acquisition mechanism.

### Official iOS static realtime architecture

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

### Whole-package static limit

The complete decrypted app bundle was searched. Neither literal `/backend-api/celsius/ws/user` nor JSON spelling `websocket_url` is present as an ordinary searchable string. The third-party implementation reporting that route and a `conversations` topic remains hypothesis/cross-check evidence only.

The likely explanation is generated API/configuration/closure wiring. Do not spend more time treating absence of a cstring as a product defect.

### Existing runtime injection path

The supplied package already contains:

- `CydiaSubstrate.framework` plus `.troll-fools` marker;
- `ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`;
- `Assets.framework/Assets` weak-loads that injected dylib.

Therefore a research-only runtime observer can use the existing injection style to observe the official app's real registration request and WebSocket control/event frames on the user's current version/account.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b82-device-runtime-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-visible-web-native-realtime-evidence-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-ios-runtime-hook-plan-20260902.md`

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

After exact evidence, reimplement only the minimum verified protocol in our own Swift/Foundation code.

## Runtime probe boundary

The official-app observer may inspect only privacy-safe structure:

- normalized registration path, method, HTTP status and response key names;
- WebSocket host/path shape without signed query values;
- outbound command type/id/key names/topic/offset class;
- inbound frame type/topic/offset, catchup/live/reply classification;
- target-conversation match, update type and update-content key names/counts;
- timing relative to remote Send and completion.

Never export Cookie/Authorization/token/challenge values, signed WebSocket query values, prompt/answer/reasoning/tool bodies or raw conversation IDs.

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

At first, use native WebSocket events as notification/state triggers and keep Detail/SSE/resume/plural paths authoritative for message/reasoning/final content. Promote WebSocket content only after separate exact evidence.

If the WebSocket contract cannot be reproduced under our accepted auth boundary, explicitly design a bounded selected-conversation status monitor using official `ConversationPollingManager` evidence. Do not introduce hidden fixed polling by default.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 3**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Do **not** allocate b83 yet. Build/prepare a research-only official-app WebSocket observer using the supplied package's existing injection path. Capture the current account/version's exact registration request and structural `connect`/`subscribe`/conversation-update frames during one cross-platform long turn. Use that evidence to decide the minimal b83 protocol scope. The existing Web Rule Lab remains an optional quicker same-origin check, but runtime official-app observation is the stronger authority for dynamic registration/topic/auth behavior.