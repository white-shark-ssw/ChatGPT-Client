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

**Active. Embedded login/persistence is accepted. b4 real-device evidence isolated native browser-route `/auth/login` as an unreliable Cloudflare-gated prerequisite. b5 now directly tests the actual account/session path and is awaiting real-device validation.**

### Accepted b2 evidence

- `DEV-auth-bootstrap-0.1.0-b2`, product source `809fa03e673afded87cb47fb755c998ab1b58e12`.
- Run `32886019320` passed; artifact ID `9577612707`; IPA SHA-256 `426c5f9b6b5e71a41c3ca571abdc73951835a55dc902691d75030a781ee61465`.
- User completed Continue with Google in embedded `WKWebView` on iPhone / iOS 17.0.
- Force-close/relaunch retained authenticated state. Default persistent `WKWebsiteDataStore` is the persistent auth-secret authority for the tested environment.

### b3 / b4 route evidence

- b3 (`0fcf040012c0698d0e3ce1628fec9865237eba3b`) showed a transient cookie-copy ephemeral `URLSession` could resolve browser-oriented `/auth/login` to authenticated `chatgpt.com` HTTP 200 under its tested conditions.
- b4 exact runtime candidate `DEV-auth-bootstrap-0.1.0-b4`, source `33ea1b96f755bdf21fdd7691a9f1084a6d624908`, artifact ID `9579720453`, was real-device tested on iPhone / iOS 17.0.
- b4 WebKit `/auth/login` initially returned HTTP 403, completed a Cloudflare challenge, then reached non-`/auth` `chatgpt.com` HTTP 200 and `session.webState=authenticated`.
- The separate native `/auth/login` request copied 46 total / 27 matching WebKit cookies but returned HTTP 403 and `session.nativeState=notAuthenticated`.
- b4 account-context probe never started because controller sequencing required that native `/auth/login` gate first. Therefore b4 is not evidence that `/api/auth/session` or accounts-check failed.

### Current b5 direct account-context candidate

- `AuthWebViewController` now starts account-context verification directly after WebKit finishes at authenticated non-`/auth` `chatgpt.com`; native `/auth/login` is no longer a prerequisite.
- `AuthSessionStore.probeAccountContext` uses the existing narrow evidence path: current WebKit ChatGPT/OpenAI cookies copied transiently to an ephemeral `URLSession` -> GET `/api/auth/session` -> transient bearer -> accounts-check -> required default account context only.
- b5 adds only safe account-probe cookie counts (`itemCount`, `matchedItemCount`). Cookie values, bearer values, Authorization headers and response bodies remain excluded from diagnostics.
- Valid candidate `DEV-auth-bootstrap-0.1.0-b5`, version `0.1.0 (5)`, exact product/workflow source `c09f981171b02dc8a4f0d8ada4624bd779c68c2f`.
- Push run `32932389742` passed Xcode 16.4 build/inspect/upload. Artifact ID `9593649485`; IPA `ChatGPTClient-0.1.0-b5-dev-auth-bootstrap.ipa`; IPA SHA-256 `d9a22635cc6ac05d2ba09a0a627eaa74d38d1a690b5e9affe2f318d2aa204f15`; ZIP digest `sha256:4ad6e95d4e30981aa63bb8bd401c0d4cd9acdddabbf83fab27b1f6fe54307066`.
- Downloaded b5 artifact was locally checked for matching version/build/candidate/source and IPA checksum.
- b5 is **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested**.

### Immediate verification order

1. Install exact b5 artifact ID `9593649485` on the intended iPhone / iOS 17.0.
2. Open the existing authentication verification page and let WebKit reach authenticated ChatGPT. b5 then directly runs account-context verification.
3. Success title: `登录会话 · 账户上下文通过`.
4. If the title is `网页登录成功 · 账户上下文未通过` or `网页登录成功 · 账户验证失败`, export the b5 diagnostic JSON without repeatedly restarting. Inspect the exact `accountContextProbe.end` stage/status: `stage=session` tests `/api/auth/session`; `stage=accounts` tests accounts-check.
5. If account context passes, close Phase 2 and only then open `DEV-protocol-read`.
6. If it fails, diagnose the exact current status/shape before considering any change. Do not add speculative retries, alternate endpoints, User-Agent spoofing, Cloudflare bypass or browser-script token extraction.

### Phase 2 acceptance gate

- Actual Google login on real device — **passed b2**.
- WebKit session persistence/re-entry — **passed b2; b4 also confirms WebKit can recover through an observed Cloudflare challenge to authenticated ChatGPT**.
- Persistent authentication-secret owner — **default `WKWebsiteDataStore`, accepted**.
- Native `/auth/login` behavior — **route-specific evidence only; b3 succeeded, b4 returned Cloudflare 403; no longer a Phase 2 prerequisite**.
- Account/workspace context owner/probe — **implemented b5; Code written + CI passed + Artifact produced; runtime pending**.
- Auth secrets excluded from logs/export — **implemented; b5 continues the same diagnostics contract**.

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

Real-device test exact `DEV-auth-bootstrap-0.1.0-b5` artifact ID `9593649485`. Use the direct account-context result and exported diagnostics to either close Phase 2 or isolate the exact `/api/auth/session` / accounts-check failure. Do not open `DEV-protocol-read` yet.
