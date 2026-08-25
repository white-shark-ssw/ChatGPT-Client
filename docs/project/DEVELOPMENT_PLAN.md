# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-26._

## Purpose

This is the durable implementation sequence for the new iOS-native ChatGPT client. It defines dependency order and acceptance gates; implementation status must be backed by current source/CI/runtime evidence.

Current product constraints:

- native iOS client;
- distributable as an IPA installed through TrollStore;
- intended user OS environment does not exceed iOS 17.0;
- prefer the lowest practical deployment target supported by real requirements and validation;
- historical WebView project material is experience/reference only;
- current ChatGPT private/internal protocol behavior must be revalidated from current evidence.

## Development principles

1. **Diagnosability before complexity**: the executable app foundation includes structured local diagnostics/logging from the start.
2. **Authentication before private protocol assumptions**: establish a real current authenticated session before building conversation API clients.
3. **Protocol evidence before data models**: do not generate a large model layer from old endpoint memory. Capture current list/detail/send/stream shapes first.
4. **One state owner per identity**: session/account/conversation/message-stream/upload identities must have explicit owners; UI labels are consumers, not authorities.
5. **Native data model separate from visible views**: keep complete conversation state independent from the currently mounted/rendered message views.
6. **Serial core, parallel edges**: app foundation -> auth -> protocol read -> native read -> send/stream are strongly dependent and should normally be completed in order. Later features may parallelize only after conflict checks.
7. **Real-device evidence matters**: artifact/CI success is not runtime proof. Each runnable milestone should be tested through TrollStore on the intended iOS environment.

## Phase 1 — `DEV-app-foundation`

### Status

**Accepted / Stable foundation.** `DEV-app-foundation-0.1.0-b1` reached Code written + CI passed + Artifact produced + Runtime/manual/real-device tested on iPhone / iOS 17.0. The foundation modules are Stable, not Frozen. Lower iOS versions and iPad runtime remain unverified.

### Goal

Create the smallest real Xcode/iOS baseline that can be built into a TrollStore-installable IPA and can produce useful diagnostics before any ChatGPT-specific implementation is added.

### Implemented scope

- Swift 5 + UIKit Xcode project/application target with no third-party dependencies.
- iOS 14.0 deployment target, chosen from current system-API requirements rather than defaulting to iOS 17.0.
- Basic app shell, Settings entry and build/runtime metadata display.
- Reproducible unsigned IPA packaging path for TrollStore validation.
- Structured OSLog diagnostics, bounded persistent JSONL history, trace/span timing, secret-field filtering and user-triggered redacted diagnostic JSON export.
- GitHub Actions Xcode/IPA build and artifact validation.

### Acceptance evidence

- Xcode 16.4 CI built `arm64-apple-ios14.0` successfully.
- Accepted candidate: `DEV-app-foundation-0.1.0-b1`, version `0.1.0 (1)`.
- Accepted IPA SHA-256: `dcdefac9e508c5fd55c3c418fc0ea497c736f54fadc3b5e946300c5c1c032760`.
- User installed/launched the candidate through TrollStore on iPhone / iOS 17.0 with no reported problem.
- Settings/sample diagnostic event/export worked.
- Exported diagnostics contain correct build/device/runtime identity and demonstrate persistent events surviving app relaunch.
- No password/token/Cookie/Authorization/OAuth secret fields were observed in the supplied export.

## Phase 2 — `DEV-auth-bootstrap`

### Goal

Prove a current login/session bootstrap on real hardware before implementing native conversation APIs.

### Historical evidence

The user reports that the previous Web-based IPA successfully used ChatGPT web login and that their account uses **Continue with Google**. This proves that the historical implementation worked at that time only.

### Current verification order

1. Start from the simplest current ChatGPT web-login bootstrap and reproduce the real navigation on-device.
2. Attempt the user's normal Google sign-in route and record navigation/auth state transitions with safe logging.
3. If current Google OAuth blocks an embedded `WKWebView`/embedded user-agent, capture the exact current failure/redirect evidence first. Do not immediately add multiple fallback paths.
4. Only then evaluate the smallest supported system-browser/auth handoff needed to complete login, based on current behavior.
5. After successful login, determine from evidence how the authenticated ChatGPT session can be consumed by the native client. Do not assume WebKit cookie stores, `URLSession`, system browser cookies or token state are interchangeable.
6. Verify session persistence/re-entry behavior after app relaunch while the server session is still valid.

### Current external risk

Google OAuth guidance warns that authorization endpoints in embedded user-agents such as `WKWebView` may fail with `disallowed_useragent` and recommends supported system/SDK authentication flows. Historical success therefore does not remove the need for a current real-device verification.

### Acceptance gate

- User can complete their actual Google-based ChatGPT login on the test device.
- Client has a verified way to determine authenticated vs unauthenticated state.
- Session/account context used by later native network requests is evidenced and documented.
- No password, OAuth code, access token, session cookie or equivalent secret is written to logs.

## Phase 3 — `DEV-protocol-read`

### Goal

Establish the current authenticated read protocol before native UI depends on it.

### Evidence targets

- current user/account/workspace context required for requests;
- conversation-list request, pagination/cursor behavior and essential metadata;
- conversation-detail request and current response shape;
- node/message identity and active-branch semantics;
- status/error behavior;
- headers/context required for successful requests, with secret values excluded from durable docs/logs.

### Acceptance gate

A minimal authenticated diagnostic harness can load conversation list and one conversation detail on-device, with request/response metadata and timing visible in safe logs. Current protocol evidence is documented before production models are expanded.

## Phase 4 — `DEV-native-read-path`

### Goal

Build the first fully native read-only chat experience.

### Scope

- Native conversation list/navigation.
- Single authoritative selected-conversation identity.
- Conversation repository/store.
- Message tree / active-branch resolver based on current evidence.
- Native message list with incremental/virtualized view creation.
- Markdown/code rendering sufficient for real conversations.
- Preserve scroll anchor while loading older history where the current protocol supports pagination/history loading.

### Acceptance gate

- Switch repeatedly between two real conversations without identity mixing.
- Open short and long real conversations.
- Return to a conversation with correct state/scroll behavior according to the implemented contract.
- Logs can trace navigation -> selected conversation -> network request -> model update -> first visible content using correlated identifiers.

## Phase 5 — `DEV-send-stream`

### Goal

Complete the core daily-use text-chat vertical loop.

### Scope

- New conversation / existing conversation send path as supported by current protocol evidence.
- Composer state.
- User message state transition.
- Streaming parser and stream lifecycle.
- Incremental assistant-message update without broad list reload.
- Stop/cancel if current protocol supports it.
- Clear failure state and retry policy only where current evidence justifies it.

### Acceptance gate

- Send text successfully in existing and newly created conversations as applicable.
- Stream appears incrementally and finalizes to the correct conversation/message node.
- Rapid conversation switching cannot redirect a stream into the wrong conversation.
- Logs include send-to-first-event, send-to-first-visible-token/update, stream duration, event count, bytes, terminal reason and error status without logging message bodies by default.

## Phase 6 — `DEV-long-conversation`

### Goal

Make long conversations a first-class performance target instead of a later patch.

### Scope / measurements

- bounded visible view/cell population;
- message model and rendered-view separation;
- incremental stream updates;
- branch-aware active path;
- load/parse/model/render timing;
- first visible content timing;
- memory growth and memory-warning behavior;
- input latency and scroll hitch investigation;
- background/foreground behavior.

### Acceptance gate

Real-device long-conversation tests show usable scrolling/input/streaming behavior with measured evidence. CI or IPA production alone is not sufficient.

## Phase 7 — `DEV-attachments`

### Goal

Add native-first attachment handling after text chat and conversation ownership are stable.

### Scope

- Files, photos and videos including iOS screen recordings where current backend behavior permits them.
- Upload task state separate from message-send state.
- Streaming/chunk/file URL handling that avoids loading large videos fully into memory unnecessarily.
- Upload progress, failure diagnosis and temporary-file cleanup ownership.
- Current protocol evidence for upload identity/metadata and message attachment references.

### Acceptance gate

At least one photo, one regular file and one video/screen-recording flow are validated where supported by current ChatGPT behavior, with safe progress/error logs.

## Phase 8 — Daily-use conversation features

Split into separate Work IDs rather than one oversized branch when implementation begins. Likely sequence:

- conversation search;
- rename / archive / delete;
- edit / regenerate / branch navigation;
- export from the authoritative conversation model, never from only visible UI;
- model selection / temporary-chat behavior when current protocol evidence is available;
- settings and diagnostics UX refinement.

## Phase 9 — Advanced capabilities

Only after the core client is stable and current protocol evidence is available:

- Projects;
- web search;
- image generation / richer multimodal presentation;
- Voice;
- Memory management;
- Deep Research;
- GPTs and other current ChatGPT-specific capabilities.

These are roadmap candidates, not current scope commitments.

# Diagnostics / logging contract

## Goal

Every important asynchronous path must leave enough local evidence to answer: **what action started, which state owner handled it, which request/stream/upload it mapped to, how long each stage took, where it terminated, and what safe error/status evidence exists.**

The default implementation is local diagnostics, not remote analytics/telemetry. No server-side telemetry/upload service is implied unless explicitly added later.

## Event shape

Use the accepted structured event envelope concepts:

- timestamp;
- severity;
- category;
- event name;
- app version/build/candidate;
- runtime iOS/device metadata where appropriate;
- action/trace correlation ID;
- safe request/stream/upload correlation ID;
- safe/redacted conversation/message reference when needed for state debugging;
- duration / byte count / item count / status / error domain+code where relevant.

## Required categories

At minimum cover as modules are introduced:

- app lifecycle / startup;
- authentication / web-login navigation state;
- session/account context state transitions;
- network request start/end/status/timing/size;
- protocol parse/validation;
- conversation selection and repository/store updates;
- streaming lifecycle;
- message render/performance spans;
- attachment selection/upload/cleanup;
- persistence/cache where introduced;
- build/artifact/runtime diagnostic metadata;
- errors and invariant violations.

## Privacy and secret handling

Never log by default:

- passwords;
- OAuth authorization codes;
- access/refresh/session tokens;
- Cookie values or full `Cookie`/`Authorization` headers;
- full chat message text;
- full request/response bodies containing user content;
- attachment file contents.

Prefer metadata such as byte length, MIME/type, node counts, status codes and timings. Identifiers needed for local state debugging may be stored locally under the app's private container, but diagnostic export should redact/hash sensitive identifiers and must not export authentication secrets.

## Persistence

Use the accepted bounded persistent rolling diagnostic store in addition to normal developer console/unified logging, because failures may occur on a TrollStore-installed device away from Xcode. Retention must remain size/count bounded; logs must not grow without limit.

## Diagnostic export

The accepted foundation provides user-triggered diagnostic JSON export containing app/build/candidate/source identity, deployment/runtime metadata and recent redacted structured logs. Future tasks may add additional safe performance counters/reason metadata when justified, but must not expose login secrets or full chat content by default.

## Performance milestones

Instrument from the start so later work can compare candidates rather than rely on impressions. Important spans include:

- cold/warm app startup;
- login bootstrap duration;
- conversation-list load;
- conversation-detail load and parse;
- model construction;
- first visible message content;
- send -> first stream event;
- send -> first visible assistant update;
- stream completion;
- attachment upload throughput/duration;
- long-conversation memory/performance observations.

# Parallel-development guidance

The first five implementation phases share authentication/session/protocol/conversation state and should normally be serialized. Do not open independent branches for `auth`, `protocol`, `native read` and `send/stream` simultaneously unless the earlier contracts are already merged and stable enough to avoid duplicated state owners.

After the core conversation model/store and transport contracts are stable, attachments, export and independent settings/diagnostics UX may become candidates for parallel work, subject to the normal conflict check.

# Next implementation task

The foundation gate is accepted. The next serial product-code Work is **`DEV-auth-bootstrap`**: reproduce the user's current Google-based ChatGPT login path on-device, capture safe auth/navigation evidence, and establish current authenticated session/account context before any private ChatGPT conversation protocol implementation begins.
