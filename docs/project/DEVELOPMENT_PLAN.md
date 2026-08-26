# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-26._

## Purpose

This is the durable implementation sequence for the iOS-native ChatGPT client. Status must be backed by current source/CI/artifact/runtime evidence.

Current constraints: native iOS client; TrollStore IPA; intended OS ceiling iOS 17.0; lowest practical deployment target; historical WebView material reference-only; current private/internal behavior must be revalidated.

## Development principles

1. **Diagnosability before complexity**.
2. **Authentication before private protocol assumptions**.
3. **Protocol evidence before data models**.
4. **One state owner per identity**.
5. **Native data model separate from visible views**.
6. **Serial core, parallel edges**.
7. **Real-device evidence matters; CI/artifact is not runtime proof**.

## Phase 1 — `DEV-app-foundation`

**Completed / merged / Stable.** `DEV-app-foundation-0.1.0-b1` reached Code + CI + Artifact + real-device testing on iPhone / iOS 17.0.

## Phase 2 — `DEV-auth-bootstrap`

**Completed / merged / Stable for accepted scope.** `DEV-auth-bootstrap-0.1.0-b6` established embedded Google login, persistent default `WKWebsiteDataStore` auth, transient native session/accounts transport, ordered plus/personal account context and privacy-safe diagnostics on iPhone / iOS 17.0.

Durable boundary: WebKit remains the sole persistent auth-secret authority; copied cookies/bearer are transient; challenge sensitivity remains observed; no speculative automatic retry/fallback/UA spoof/Cloudflare bypass.

## Phase 3 — `DEV-protocol-read`

### Status

**Runtime acceptance passed on b7; PR #7 integration completing.** Candidate `DEV-protocol-read-0.1.0-b7`, version `0.1.0 (7)`, exact product source `44a137b973e29e2a313e9114fdacb7727dccefb9`, reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** on iPhone / iOS 17.0.

### Accepted current evidence

- First account attempt reproduced `/api/auth/session` HTTP 403; user explicitly pressed `重新开始`; second attempt returned session/accounts HTTP 200 and verified plus/personal account context. No automatic retry occurred.
- Personal-account conversation list request `GET /backend-api/conversations?offset=0&limit=28&order=updated` succeeded with transient bearer + copied ephemeral WebKit cookies only; no `chatgpt-account-id` or browser-only headers were required in this tested run.
- List response: HTTP 200, 23,697 bytes, 28 items, total 29, limit 28, offset 0.
- First detail response: HTTP 200, 13,152,411 bytes, mappingCount 2068, messageNodeCount 2067, one root/null-message node, three branching nodes, max children 2, six content types; current node present+mapped and returned conversation identity matched.
- Role counts user 22 + assistant 1235 + tool 810 + system 0 + other 0 equal all 2067 message nodes.
- End-to-end list/detail probe finished `status=ok` in 13,573.66 ms; current diagnostics do not separate transport vs parse/inspection time.
- Screenshot title `会话列表 · 会话详情通过` matches the exported result.

### Phase 3 acceptance gate

**Passed for the exact tested Plus/personal read scope.** This does not prove send/streaming/attachments, non-personal workspaces, iPad or lower-iOS runtime.

## Phase 4 — `DEV-native-read-path`

### Status

**Next core task after PR #7 integration.**

### Required first design inputs from b7

- Establish explicit production owners for conversation repository, list pagination, selected-conversation identity, detail/message-tree state and active branch resolution. The diagnostic `ProtocolReadProbe` must not become the production repository.
- Reuse accepted auth/account transport ownership; do not create a second persistent credential authority.
- Implement list/navigation/read models from the now-evidenced list/detail structure, while treating unsupported fields/semantics as Unknown until required.
- The first tested detail was **13.15 MB with 2068 mapping nodes / 2067 message nodes**. Native storage, parsing and rendering must therefore be designed for real large-conversation input rather than a tiny sample.
- Do not infer that the measured 13.57 s is rendering or parsing time; add phase-specific timing only where needed to locate actual bottlenecks.
- Preserve conversation identity under repeated rapid switching. Acceptance requires repeated real-conversation switching and long-conversation reads without identity mixing.
- Use bounded/virtualized native rendering rather than assuming all message views can remain materialized.

## Phase 5 — `DEV-send-stream`

Implement text send/new conversation only after read-path ownership is stable, then establish streaming lifecycle/incremental assistant updates and evidence-backed cancel/failure behavior. Streams must remain owned by the correct conversation under rapid switching.

## Phase 6 — `DEV-long-conversation`

Measure and stabilize bounded visible views, model/render separation, incremental updates, memory growth, input latency, scrolling, first-visible timing and background/foreground behavior on real device.

## Phase 7 — `DEV-attachments`

Add native photo/file/video attachment flows only after text chat/state ownership is stable. Upload state remains separate from send state; large video paths must avoid unnecessary full-memory loading.

## Phase 8 — Daily-use conversation features

Split search, rename/archive/delete, edit/regenerate/branch navigation, export, model/temporary-chat behavior and settings/diagnostics refinement into separate Work IDs when dependencies are stable.

## Phase 9 — Advanced capabilities

Projects, web search, image generation, Voice, Memory, Deep Research, GPTs and other current ChatGPT-specific capabilities are later roadmap candidates, not current commitments.

# Diagnostics / logging contract

Every important async path should show what started, which owner handled it, safe request/stream/upload mapping, timing, terminal result and safe error/status metadata. Never log passwords, OAuth codes, tokens, Cookie/Authorization values, full chat bodies or attachment contents.

# Parallel-development guidance

The core chain `foundation -> auth -> protocol read -> native read -> send/stream` remains serialized. Parallel feature work is appropriate only after state owners/contracts are stable and conflict checks pass.

# Next implementation action

Complete PR #7 integration and then create isolated `DEV-native-read-path` from the merged b7 baseline. Its first work must establish production conversation state ownership and the minimal native list/detail read path using the accepted protocol evidence, with explicit handling for the evidenced large detail payload.
