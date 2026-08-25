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

**Active. Embedded Google login, WebKit persistence, and the tested transient native-session bridge passed on real device. Account/workspace context has an identity-correct b4 candidate awaiting real-device validation.**

### Accepted b2 evidence

- `DEV-auth-bootstrap-0.1.0-b2`, product source `809fa03e673afded87cb47fb755c998ab1b58e12`.
- Run `32886019320` passed; artifact ID `9577612707`; IPA SHA-256 `426c5f9b6b5e71a41c3ca571abdc73951835a55dc902691d75030a781ee61465`.
- User completed Continue with Google in embedded `WKWebView` on iPhone / iOS 17.0.
- Force-close/relaunch retained authenticated state; diagnostics corroborated direct `/auth/login` -> logged-in `chatgpt.com` HTTP 200 with no Google navigation.
- Default persistent `WKWebsiteDataStore` is the persistent auth-secret authority for the tested environment. No system-browser fallback is justified.

### Accepted b3 evidence

- `DEV-auth-bootstrap-0.1.0-b3`, exact product source `0fcf040012c0698d0e3ce1628fec9865237eba3b`.
- Authoritative push run `32889095904`; artifact ID `9578766019`; IPA SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`.
- User screenshot shows `网页登录成功 · 原生会话通过`.
- Supplied b3 diagnostics identify build `3`, source `0fcf040012c0`, iPhone / iOS 17.0; record `session.webState=authenticated`, 54 total / 35 matched WebKit cookies, `session.nativeState=verified`, and final `chatgpt.com` HTTP 200 / `status=ok` in `1203.68 ms`.
- This proves the tested native transport can consume the current WebKit-authenticated context for `/auth/login`. It does not prove account/workspace or conversation-protocol behavior.

### Current b4 account-context candidate

- Current evidence established a narrow account-context path suitable for a diagnostic probe: authenticated `/api/auth/session`, transient session bearer, then `/backend-api/accounts/check/v4-2023-04-27` for default account context. This remains current-evidence-driven and is not a general private-protocol model.
- `AuthSessionStore` now owns an **in-memory Candidate** account context and uses a fresh ephemeral session. The bearer is a local transient value only and is not logged or persisted. Response bodies are not logged. Exported `userID` / `accountID` use existing identifier hashing.
- `AuthWebViewController` chains account verification only after the already-accepted native-session probe succeeds.
- The first b4 artifact from run `32891478482` is rejected because a stale build-script default embedded candidate b3 despite b4 filename/artifact identity. Do not test artifact ID `9579620441`.
- Commit `33ea1b96f755bdf21fdd7691a9f1084a6d624908` fixes only the stale candidate default.
- **Valid b4 candidate**: `DEV-auth-bootstrap-0.1.0-b4`, `0.1.0 (4)`, product source `33ea1b96f755bdf21fdd7691a9f1084a6d624908`.
- Corrected push run `32891798350` passed Xcode 16.4 and explicitly embedded b4 candidate/source identity.
- Artifact ID `9579720453`; IPA `ChatGPTClient-0.1.0-b4-dev-auth-bootstrap.ipa`; IPA SHA-256 `f918b1f5762458e55e89a1f0d23e5c2bf46be11d7f4599c692627a07043dab03`; ZIP digest `sha256:a11819f7473472ec074fc09ee7c0bed4101d3288d92edd9fbe2880d9e666c001`.
- b4 is **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested**.

### Immediate verification order

1. Install exact valid b4 artifact ID `9579720453` on the intended iPhone / iOS 17.0.
2. Run the existing login/auth verification flow. Native-session verification should pass first; then account-context probe runs automatically.
3. Final success title is `登录会话 · 账户上下文通过`. Failure titles distinguish not-available vs request failure; do not add fallback endpoints before reading exact diagnostics.
4. Export the b4 privacy-safe diagnostic JSON. Verify candidate `DEV-auth-bootstrap-0.1.0-b4`, build `4`, source `33ea1b96f755`, `session.accountState`, safe HTTP statuses, and hashed `userID` / `accountID` where success provides them.
5. If b4 account context passes, complete Phase 2 and only then open `DEV-protocol-read`.
6. If it fails, diagnose the exact current response/status/shape without speculative retry/fallback chains.

### Phase 2 acceptance gate

- Actual Google login on real device — **passed b2**.
- WebKit session persistence/re-entry — **passed b2**.
- Explicit safe authentication evidence owner — **passed b3**.
- Native transport can consume current authenticated context for the tested auth route — **passed b3**.
- Account/workspace context owner/probe implemented — **Code written + CI passed + Artifact produced b4; runtime pending**.
- Auth secrets excluded from logs/export — **implemented; continue validating in b4 export**.

## Phase 3 — `DEV-protocol-read`

### Entry gate

Do not start production protocol implementation until Phase 2 has runtime-evidenced authenticated/session/account context actually usable by native requests.

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

Use the accepted bounded local diagnostics store/export authority; do not create a competing store without a concrete need.

# Parallel-development guidance

The core chain `foundation -> auth -> protocol read -> native read -> send/stream` remains serialized. Parallel feature work is appropriate only after state owners/contracts are stable and conflict checks pass.

# Next implementation action

Real-device test exact identity-correct `DEV-auth-bootstrap-0.1.0-b4` artifact ID `9579720453`, then use its final title and exported diagnostics to either close the account-context gate or diagnose the exact current failure. Do not open `DEV-protocol-read` yet.
