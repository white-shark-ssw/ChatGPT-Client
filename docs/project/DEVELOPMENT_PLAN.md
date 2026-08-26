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

**Active. Embedded login/persistence is accepted. b5 real-device evidence now proves the direct native session/accounts HTTP path can reach HTTP 200 on the intended device. The remaining observed b5 failure was the superseded account parser. b6 is the current ordered-account parser candidate and also adds the requested diagnostics-clear control; runtime validation is pending.**

### Accepted web-login evidence

- b2 completed Continue with Google in embedded `WKWebView` and established persistent WebKit authentication across force-close/relaunch.
- Default persistent `WKWebsiteDataStore` remains the persistent auth-secret authority.

### Native route evidence

- b3 showed a transient native `/auth/login` request could reach authenticated ChatGPT HTTP 200 under one tested condition.
- b4 later showed WebKit could pass Cloudflare and remain authenticated while separate native `/auth/login` returned HTTP 403.
- Therefore native `/auth/login` remains route-specific evidence only and is not an account-context prerequisite.

### b5 direct account/session evidence

- Candidate `DEV-auth-bootstrap-0.1.0-b5`, exact source `c09f981171b02dc8a4f0d8ada4624bd779c68c2f`, artifact ID `9593649485`.
- First direct probe after an observed Cloudflare challenge: `/api/auth/session` HTTP 403, `stage=session`.
- Second direct probe: WebKit reached authenticated ChatGPT; `/api/auth/session` HTTP 200; required user id + transient access token parsed; bearer-authenticated accounts-check HTTP 200.
- b5 then failed with `stage=accounts`, `reason=missing_default_account`. Current source inspection shows this was caused by requiring `payload.accounts.default.account.id`.
- Thus b5 is **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** and establishes the native session/accounts transport under the successful second-run condition. It does not establish the corrected account parser.

### Current b6 account-context candidate

- `AuthSessionStore` now follows current response-shape evidence: require non-empty `account_ordering`, resolve each ordered key in the keyed `accounts` dictionary, skip entries explicitly marked `can_access_with_session=false`, and read nested `account.account_id` from the first usable entry. Optional `plan_type` / `structure` remain metadata only.
- Shape failures log safe structural counts/reason only; response bodies and authentication secrets remain excluded.
- Settings now includes `清理诊断日志`. The existing diagnostics owner clears its current JSONL and configured rotated archives without clearing WebKit login/auth state or introducing a competing store.
- Valid candidate `DEV-auth-bootstrap-0.1.0-b6`, version `0.1.0 (6)`, exact product/workflow source `19c0cd22923d8c6f4c96e676258b31814d02a942`.
- Push run `32934821144` passed Xcode 16.4 build/inspect/upload. Artifact ID `9594474567`; IPA `ChatGPTClient-0.1.0-b6-dev-auth-bootstrap.ipa`; IPA SHA-256 `c7109f691c1de675ef55da1a08695c10663b62030853453ee2fafd01fb070c8b`; ZIP digest `sha256:68c7cfc6667c362c79900be1cf46154a76aa3a363649b1995ff02a5d83b88d85`.
- Downloaded b6 artifact was locally checked for `0.1.0 (6)`, candidate b6, source `19c0cd22923d`, Release, minimum OS 14.0 and matching IPA checksum.
- b6 is **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested**.

### Immediate verification order

1. Install exact b6 artifact ID `9594474567` on the intended iPhone / iOS 17.0.
2. Optional but recommended for clean evidence: open Settings and press `清理诊断日志` once. This clears accumulated local b1-b5 diagnostics only; it does not log out WebKit.
3. Open the authentication verification page once and let WebKit reach authenticated ChatGPT; b6 then directly runs account-context verification.
4. Success title remains `登录会话 · 账户上下文通过`.
5. On any other result, export one fresh b6 diagnostic JSON. Inspect the exact `accountContextProbe.end` stage/status/reason before changing code.
6. Do not add speculative retries, alternate endpoints, User-Agent spoofing, Cloudflare bypass, browser-script token extraction or multi-shape parser fallback chains without new evidence.
7. Only after b6 account context is accepted on-device should Phase 2 close and `DEV-protocol-read` begin.

### Phase 2 acceptance gate

- Actual Google login on real device — **passed b2**.
- WebKit session persistence/re-entry — **passed**.
- Persistent authentication-secret owner — **default `WKWebsiteDataStore`, accepted**.
- Native `/auth/login` — **route-specific evidence only, not a gate**.
- Direct native `/api/auth/session` + accounts-check transport — **passed under b5 second-run condition**.
- Current account/workspace parsing/owner — **implemented b6; Code written + CI passed + Artifact produced; runtime pending**.
- Auth secrets excluded from logs/export — **implemented**.
- Explicit local diagnostics clear for repeated tests — **implemented b6; CI/artifact passed; runtime pending**.

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

Use the accepted bounded local diagnostics store/export/clear authority; do not create a competing store without a concrete need.

# Parallel-development guidance

The core chain `foundation -> auth -> protocol read -> native read -> send/stream` remains serialized. Parallel feature work is appropriate only after state owners/contracts are stable and conflict checks pass.

# Next implementation action

Real-device test exact `DEV-auth-bootstrap-0.1.0-b6` artifact ID `9594474567`. Clear accumulated diagnostics first if desired, then run auth verification once and export one fresh b6 diagnostic JSON only if the final title is not `登录会话 · 账户上下文通过`. Do not open `DEV-protocol-read` yet.
