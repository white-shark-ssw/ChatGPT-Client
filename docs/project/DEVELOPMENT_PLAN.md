# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-26._

## Purpose

This is the durable implementation sequence for the new iOS-native ChatGPT client. Status must be backed by current source/CI/artifact/runtime evidence.

Current constraints: native iOS client; TrollStore IPA distribution; intended user OS ceiling iOS 17.0; lowest practical deployment target; historical WebView material reference-only; current ChatGPT private/internal behavior must be revalidated.

## Development principles

1. **Diagnosability before complexity**.
2. **Authentication before private protocol assumptions**.
3. **Protocol evidence before data models**.
4. **One state owner per identity**.
5. **Native data model separate from visible views**.
6. **Serial core, parallel edges**.
7. **Real-device evidence matters; CI/artifact is not runtime proof**.

## Phase 1 — `DEV-app-foundation`

### Status

**Accepted / Stable foundation.** `DEV-app-foundation-0.1.0-b1` reached Code written + CI passed + Artifact produced + Runtime/manual/real-device tested on iPhone / iOS 17.0. Foundation is Stable, not Frozen.

### Established scope

Swift 5 + UIKit, iOS 14.0 target, no third-party dependencies, application shell/settings, build/runtime identity, bounded local diagnostics/redacted export, reproducible unsigned IPA packaging and GitHub Actions build/artifact path.

## Phase 2 — `DEV-auth-bootstrap`

### Status

**Active. Embedded Google login and WebKit persistence passed; native-session consumption runtime gate remains open.**

### Accepted b2 evidence

- `DEV-auth-bootstrap-0.1.0-b2`, product source `809fa03e673afded87cb47fb755c998ab1b58e12`.
- Run `32886019320` passed; artifact ID `9577612707`; IPA SHA-256 `426c5f9b6b5e71a41c3ca571abdc73951835a55dc902691d75030a781ee61465`.
- User completed Continue with Google in embedded `WKWebView` on iPhone / iOS 17.0.
- Force-close/relaunch retained authenticated state. Supplied diagnostics corroborate `/auth/login` immediately resolving to non-auth `chatgpt.com` HTTP 200 with no Google navigation.
- Default persistent `WKWebsiteDataStore` is the current persistent web-auth authority on the tested environment.
- No system-browser fallback is currently justified.

### Current b3 evidence step

`DEV-auth-bootstrap-0.1.0-b3` adds one narrow native-session-consumption probe:

- `AuthSessionStore` owns safe auth evidence state only; it does not persist auth secrets.
- After authenticated WebView navigation, current ChatGPT/OpenAI WebKit cookies are copied transiently into an ephemeral `URLSession`.
- That native session requests the already-verified `https://chatgpt.com/auth/login` route.
- Success is judged from final safe destination/status only; Cookie/token/Authorization values are never logged or persisted by the probe.
- Exact product source `0fcf040012c0698d0e3ce1628fec9865237eba3b` passed push run `32889095904` and produced artifact ID `9578766019`.
- IPA `ChatGPTClient-0.1.0-b3-dev-auth-bootstrap.ipa`; SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`.
- **Runtime native-session result is pending.**

### Immediate verification order

1. Install exact b3 push artifact and open `开始登录与原生会话验证`.
2. Verify the WebView remains authenticated or complete login if needed.
3. Record whether the native probe ends at `网页登录成功 · 原生会话通过`, `...未通过`, or `...验证失败`.
4. Export b3 redacted diagnostics and confirm `session.nativeState` plus safe final destination/status.
5. If native session consumption succeeds, establish current account/workspace context and one explicit owner.
6. Only then advance to `DEV-protocol-read`.
7. If the probe fails, diagnose the exact current failure. Do not add speculative fallback/retry chains.

### Phase 2 acceptance gate

- Actual Google login on real device — **passed b2**.
- WebKit session persistence/re-entry — **passed b2**.
- Explicit safe authentication evidence owner — **implemented b3; runtime behavior pending**.
- Native transport can consume current authenticated context — **pending b3 runtime**.
- Account/workspace context needed by later native requests — **pending**.
- Auth secrets excluded from logs/export — **implemented; continue runtime verification**.

## Phase 3 — `DEV-protocol-read`

### Entry gate

Do not start production protocol implementation until Phase 2 has evidenced authenticated/session/account context actually usable by native requests.

### Goal / evidence targets

Establish current user/account/workspace context, conversation-list request/pagination/metadata, conversation-detail shape, node/message/branch semantics, status/error behavior and required safe request context before production models depend on them.

### Acceptance gate

A minimal authenticated diagnostic harness loads conversation list and one detail on-device with safe request/response/timing evidence.

## Phase 4 — `DEV-native-read-path`

Build native conversation list/navigation, authoritative selected-conversation identity, conversation repository/store, message-tree active-branch resolver and virtualized native message rendering. Acceptance requires repeated real-conversation switching and long-conversation reads without identity mixing.

## Phase 5 — `DEV-send-stream`

Implement text send/new conversation as current protocol permits, composer/user-message state, streaming lifecycle/incremental assistant updates and evidence-backed cancel/failure behavior. Streams must remain owned by the correct conversation under rapid switching.

## Phase 6 — `DEV-long-conversation`

Measure and stabilize bounded visible views, model/render separation, incremental stream updates, memory growth, input latency, scrolling, first-visible timing and background/foreground behavior on real device.

## Phase 7 — `DEV-attachments`

Add native photo/file/video attachment flows only after text chat/state ownership is stable. Upload state remains separate from send state; large video paths must avoid unnecessary full-memory loading.

## Phase 8 — Daily-use conversation features

Split search, rename/archive/delete, edit/regenerate/branch navigation, export, model/temporary-chat behavior and settings/diagnostics refinement into separate Work IDs when dependencies are stable.

## Phase 9 — Advanced capabilities

Projects, web search, image generation, Voice, Memory, Deep Research, GPTs and other current ChatGPT-specific capabilities are later roadmap candidates, not current commitments.

# Diagnostics / logging contract

Every important async path should show what started, which owner handled it, what safe request/stream/upload it mapped to, timing, terminal result and safe error/status metadata.

Never log passwords, OAuth codes, access/refresh/session tokens, Cookie values/full Cookie headers, Authorization values, full chat bodies or attachment contents. Prefer counts, sizes, statuses, timings and redacted/hashed identifiers.

Use the accepted bounded local diagnostics store/export authority; do not create a competing store without a concrete need.

# Parallel-development guidance

The core chain `foundation -> auth -> protocol read -> native read -> send/stream` remains serialized. Parallel feature work is appropriate only after state owners/contracts are stable and conflict checks pass.

# Next implementation action

Continue `DEV-auth-bootstrap`: real-device test exact b3 push artifact, then use that evidence to either establish native-auth consumption and account/workspace context or diagnose the concrete failure. Do not open `DEV-protocol-read` yet.
