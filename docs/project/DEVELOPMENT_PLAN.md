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

**Completed / merged / Stable for the accepted scope.** PR #6 merged at `78f42a06e6254088e3b495cb4529e549a1d4717f`. Embedded Google login, persistent WebKit auth, direct native session/accounts transport, ordered account-context parsing, privacy-safe diagnostics, and the clear-log control are accepted on iPhone / iOS 17.0 through b6.

### Durable authentication boundary

- Default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority.
- `AuthSessionStore` is the accepted in-memory account-context owner.
- Copied WebKit cookies and `/api/auth/session` bearer are transient only.
- Challenge sensitivity is observed; no speculative automatic retry, fallback, UA spoof or Cloudflare bypass is part of the accepted architecture.
- Authentication/account success does not prove conversation protocol behavior.

## Phase 3 — `DEV-protocol-read`

### Status

**Active — b7 ready for real-device protocol validation.** `DEV-protocol-read-0.1.0-b7`, version `0.1.0 (7)`, exact product source `44a137b973e29e2a313e9114fdacb7727dccefb9`, has reached **Code written + CI passed + Artifact produced**. Authoritative push run `32938912018` produced artifact ID `9595827498`; IPA `ChatGPTClient-0.1.0-b7-dev-protocol-read.ipa`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`. Runtime conversation-list/detail evidence is still pending.

### Current diagnostic scope

- Reuse accepted WebKit/AuthSessionStore owners; do not introduce another persistent credential authority.
- After account verification, create a short-lived ephemeral authorized transport with the transient bearer hidden inside the transport owner.
- Perform one conversation-list GET with the current evidence-backed first-page query, select one returned conversation ID only in memory, then perform one conversation-detail GET.
- Record only safe status/timing/byte/item/pagination/tree/role/content-type structural evidence. Do not log full titles, message bodies/parts, payload dumps, raw conversation/message IDs or auth secrets.
- Do not introduce production conversation models/repository/rendering in this phase.

### CI history

- b7 run `32938007843`: compile-only failure because Swift could not type-check one large closure in reasonable time.
- b7 run `32938132841`: compile-only failure on one large detail diagnostics dictionary literal.
- Product source `44a137...` split only those expressions for compiler tractability, preserving protocol behavior.
- Push run `32938912018`: Xcode 16.4 Release build succeeded for `arm64-apple-ios14.0`; IPA and artifact hashes were independently rechecked after download.

### Phase 3 acceptance gate

A minimal authenticated diagnostic harness must load the current conversation list and one conversation detail on-device, with exported safe evidence sufficient to confirm or reject the tested path/shape. CI and artifact production alone do not satisfy this gate.

### Next exact runtime action

Install b7, clear accumulated diagnostics through Settings, run `开始会话列表与详情验证`, and export diagnostics immediately after the result. If the account/session gate is challenge-sensitive, preserve the exact failure and use only an explicit user-triggered restart; do not add automatic retries. If list/detail fails, keep the exact stage/status and change only what current runtime evidence justifies.

## Phase 4 — `DEV-native-read-path`

**Blocked on Phase 3 runtime acceptance.** After protocol-read evidence is accepted, build native conversation list/navigation, authoritative selected-conversation identity, conversation repository/store, message-tree active-branch resolver and virtualized native message rendering. Acceptance requires repeated real-conversation switching and long-conversation reads without identity mixing.

## Phase 5 — `DEV-send-stream`

Implement text send/new conversation only after read-path ownership is stable, then establish streaming lifecycle/incremental assistant updates and evidence-backed cancel/failure behavior. Streams must remain owned by the correct conversation under rapid switching.

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

Obtain real-device b7 conversation-list/detail evidence. Do not start `DEV-native-read-path` or modify protocol headers/endpoints without the b7 runtime result.
