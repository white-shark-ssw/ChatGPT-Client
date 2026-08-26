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

**Acceptance achieved on `DEV-auth-bootstrap-0.1.0-b6`; pending PR #6 integration/merge.** Embedded Google login, persistent WebKit auth, current direct native session/accounts transport, ordered account-context parsing, privacy-safe diagnostics, and the requested clear-log control are implemented. The accepted account-context path is real-device tested on iPhone / iOS 17.0.

### Accepted evidence

- b2 completed Continue with Google in embedded `WKWebView` and established persistent WebKit authentication across force-close/relaunch.
- Default persistent `WKWebsiteDataStore` remains the sole persistent auth-secret authority.
- b3/b4 established that native browser-oriented `/auth/login` is route-specific evidence only and is not a durable account gate.
- b5 established direct native `/api/auth/session` HTTP 200 + bearer-authenticated accounts-check HTTP 200 under a successful device run, then exposed the obsolete `accounts.default.account.id` parser.
- b6 exact identity: `DEV-auth-bootstrap-0.1.0-b6`, version `0.1.0 (6)`, source `19c0cd22923d8c6f4c96e676258b31814d02a942`, run `32934821144`, artifact ID `9594474567`, IPA SHA-256 `c7109f691c1de675ef55da1a08695c10663b62030853453ee2fafd01fb070c8b`.
- b6 first direct attempt returned `/api/auth/session` HTTP 403 after authenticated WebKit re-entry. The user explicitly pressed `重新开始`; the second attempt returned `/api/auth/session` HTTP 200 and accounts-check HTTP 200, observed `accountCount=2`, `accountOrderingCount=1`, selected `plus` / `personal`, set `session.accountState=verified`, and ended `accountContextProbe status=ok` in 1289.71 ms.
- User screenshot title reads `登录会话 · 账户上下文通过`.
- This success is not an automatic retry behavior; current code still intentionally has no speculative retry loop.
- Settings provides `清理诊断日志` through the existing diagnostics store; it clears current/rotated local logs without clearing WebKit/auth state. The supplied b6 export contains only the fresh test cycle, consistent with the clean-log workflow.

### Phase 2 acceptance gate

- Actual Google login on real device — **passed**.
- WebKit session persistence/re-entry — **passed**.
- Persistent authentication-secret owner — **default `WKWebsiteDataStore`, accepted**.
- Native `/auth/login` — **route-specific evidence only, not a gate**.
- Direct native `/api/auth/session` + accounts-check transport — **passed under accepted b6 success condition**.
- Current account/workspace parser/owner — **passed b6 on-device; accepted/Stable for current scope**.
- Auth secrets excluded from logs/export — **implemented**.
- Explicit local diagnostics clear — **implemented; fresh b6 export is consistent with use**.

### Phase 2 integration step

Before opening the next core feature task, re-check `main`, PR #6 head, branch conflicts and final CI relevance. Merge only with explicit user approval. Do not implement conversation protocol inside this auth checkpoint.

## Phase 3 — `DEV-protocol-read`

### Entry gate

**Authentication/account-context prerequisite is now satisfied by b6 runtime evidence.** Phase 3 may begin as a separate Work ID after auth changes are integrated.

### Goal / evidence targets

Establish current conversation-list request/pagination/metadata, conversation-detail shape, node/message/branch semantics, status/error behavior and required safe request context before production models depend on them.

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

Use the accepted bounded local diagnostics store/export/clear authority; do not create a competing store without a concrete need.

# Parallel-development guidance

The core chain `foundation -> auth -> protocol read -> native read -> send/stream` remains serialized. Parallel feature work is appropriate only after state owners/contracts are stable and conflict checks pass.

# Next implementation action

Finalize/integrate PR #6 with explicit user approval. After merge, start a new isolated `DEV-protocol-read` task and establish current conversation-list/detail request evidence from the accepted b6 auth/account context. Do not guess private protocol shapes from historical material.
