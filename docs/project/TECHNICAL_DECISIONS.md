# Technical Decisions

This file records durable, evidence-backed technical decisions and rejected routes.

## Decision template

### TD-XXX — <title>

- **Status**: Proposed / Confirmed / Rejected / Frozen / Superseded
- **Date**:
- **Scope**:
- **Decision**:
- **Evidence**:
- **Alternatives considered**:
- **Rejected / do-not-repeat**:
- **Affected modules**:
- **Validation level**:
- **Supersedes**:
- **Notes**:

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Product direction / architecture baseline
- **Decision**: Develop a native iOS ChatGPT client from the Swift/UIKit baseline rather than converting the previous WebView chat implementation into the product source.
- **Evidence**: User requirement; accepted foundation runtime baseline.
- **Rejected / do-not-repeat**: Do not inherit the historical WebView chat architecture as the new source baseline.
- **Affected modules**: Whole product.
- **Validation level**: User-confirmed + runtime-tested foundation.
- **Supersedes**: None.

### TD-002 — Previous-project history is reference-only evidence

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Historical evidence / protocol research
- **Decision**: Historical endpoint names, shapes, workarounds and architecture suggestions must be revalidated before becoming current contracts.
- **Evidence**: User classification of the history pack and its warnings.
- **Rejected / do-not-repeat**: Do not implement current private protocol from old names or memory alone.
- **Affected modules**: Authentication, protocol/network, conversation, streaming, attachments.
- **Validation level**: User-confirmed evidence classification.
- **Supersedes**: None.

### TD-003 — TrollStore IPA distribution with iOS 17.0 ceiling and lowest-practical deployment target

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Runtime compatibility / distribution
- **Decision**: Distribute as IPA for TrollStore. iOS 17.0 is an intended environment ceiling, not the minimum. Keep minimum as low as practical when real requirements permit.
- **Evidence**: User requirement; iOS 14.0 build baseline and iOS 17.0 runtime evidence.
- **Rejected / do-not-repeat**: Do not raise minimum merely because CI uses a newer SDK.
- **Affected modules**: Xcode/build/dependencies/runtime APIs.
- **Validation level**: Build target iOS 14.0; runtime iPhone/iOS 17.0.
- **Supersedes**: None.

### TD-004 — Diagnostics/logging is part of the application foundation

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Observability / debugging / performance evidence
- **Decision**: Important async/auth/network/protocol/state operations use the accepted structured local diagnostics authority with bounded persistence, redacted export and explicit user clearing.
- **Evidence**: Foundation through b8 real-device evidence.
- **Rejected / do-not-repeat**: Do not log passwords, OAuth codes, tokens, Cookie/Authorization values, full chat bodies or attachment contents; do not create a competing log authority without evidence.
- **Affected modules**: Whole product.
- **Validation level**: Code + CI + Artifact + real-device evidence.
- **Supersedes**: None.

### TD-005 — WebKit is the persistent login authority; tested native consumption is transient and route-specific

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Authentication sequencing / session authority / native bridge
- **Decision**: Embedded `WKWebView` at `https://chatgpt.com/auth/login` is the current authentication bootstrap. Default persistent `WKWebsiteDataStore` is the only persistent auth-secret authority. Native transport may copy current WebKit cookies transiently into ephemeral `URLSession` for evidence-backed requests; no second persistent credential store.
- **Evidence**: b2 login/persistence; b3/b4 native `/auth/login` route-specific behavior; b5-b8 transient native consumption.
- **Rejected / do-not-repeat**: Do not persist copied secrets or generalize one route's success/failure to all routes.
- **Affected modules**: Auth/session/network transport.
- **Validation level**: Runtime/manual/real-device tested on iPhone / iOS 17.0.
- **Supersedes**: Broad assumption that native `/auth/login` could be a durable prerequisite.

### TD-006 — Foundation baseline is Swift/UIKit with iOS 14.0 minimum

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Foundation / UI / deployment
- **Decision**: Use Swift 5 + UIKit/Foundation/OSLog/CryptoKit with no third-party dependencies and `IPHONEOS_DEPLOYMENT_TARGET=14.0` until a real requirement justifies change.
- **Evidence**: Current project, CI and real-device foundation testing.
- **Rejected / do-not-repeat**: Do not raise minimum for convenience or add dependencies without concrete need.
- **Affected modules**: Xcode project and feature availability decisions.
- **Validation level**: Code + CI + Artifact + real-device foundation test.
- **Supersedes**: None.

### TD-007 — Probe actual account/session path directly after authenticated WebKit navigation

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Account-context sequencing
- **Decision**: Account verification is not gated by native browser-oriented `/auth/login`. After authenticated WebKit, test ephemeral current WebKit context -> `/api/auth/session` -> transient bearer -> accounts-check.
- **Evidence**: b4-b8. b8 production repository reused the same accepted account bridge after explicit login verification.
- **Rejected / do-not-repeat**: No speculative automatic retry, UA spoof, Cloudflare bypass, duplicate gate or fallback endpoint.
- **Affected modules**: AuthWebViewController, AuthSessionStore, diagnostics.
- **Validation level**: Runtime/manual/real-device tested on iPhone / iOS 17.0.
- **Supersedes**: Native `/auth/login` gating.

### TD-008 — Parse accounts-check by ordered account identity, not `accounts.default`

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Account-context response parsing
- **Decision**: Parse non-empty `account_ordering` plus keyed `accounts`; choose first ordered entry not explicitly denied and read nested `account.account_id`.
- **Evidence**: b5 contradicted old `accounts.default`; b6-b8 verified ordered plus/personal context.
- **Rejected / do-not-repeat**: Do not restore `accounts.default.account.id` or speculative multi-shape fallbacks without new evidence.
- **Affected modules**: AuthSessionStore.
- **Validation level**: Code + CI + Artifact + real-device tested.
- **Supersedes**: Old default-account parser assumption.

### TD-009 — Auth bootstrap gate is satisfied by b6 account-context evidence

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Roadmap / task boundary
- **Decision**: Authentication/account-context gate is satisfied. Protocol work remains separately evidenced and cannot be inferred from auth success.
- **Evidence**: b2-b6 accepted auth/account results.
- **Rejected / do-not-repeat**: Do not treat auth success as proof of conversation protocol.
- **Affected modules**: Roadmap, auth, protocol/network work.
- **Validation level**: Real-device auth/account evidence.
- **Supersedes**: Phase-2 pending status.

### TD-010 — Current personal-account conversation list + detail read path is accepted from b7

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Conversation read protocol / native read prerequisite
- **Decision**: For the tested Plus/personal account on iPhone / iOS 17.0, the accepted first read path is transient authenticated native transport using copied ephemeral WebKit cookies + transient bearer, `GET /backend-api/conversations?offset=0&limit=28&order=updated`, then `GET /backend-api/conversation/{conversation_id}` for a returned ID. The tested request succeeded without `chatgpt-account-id` or browser-only headers. Detail identity/current-node/mapping structure is accepted for this exact scope. `ProtocolReadProbe` remains diagnostic-only.
- **Evidence**: `DEV-protocol-read-0.1.0-b7`, source `44a137b973e29e2a313e9114fdacb7727dccefb9`, run `32938912018`, artifact `9595827498`, matching iPhone/iOS 17.0 export. List HTTP 200 with 28/29. First detail HTTP 200 with 13,152,411 bytes, mapping 2068/message nodes 2067, current node present+mapped and identity matched.
- **Alternatives considered**: Add `chatgpt-account-id` preemptively; duplicate browser headers; fallback endpoints; infer production models before runtime evidence.
- **Rejected / do-not-repeat**: Do not add account/browser headers, retries, alternate endpoints or compatibility shims without a concrete new failure. Do not generalize to non-personal workspaces or send/streaming/attachments. Do not use total duration as proof that one subsystem is the bottleneck.
- **Affected modules**: `AuthTransientSession`, `ProtocolReadProbe`, production conversation repository/models/rendering.
- **Validation level**: **Code + CI + Artifact + Runtime/manual/real-device tested** on iPhone / iOS 17.0.
- **Supersedes**: Phase-3 Unknown/Unverified list/detail status for exact tested scope.
- **Notes**: b8 later observed one production selected-detail HTTP 500 after 30.9 s. That does not revoke b7 route evidence, but it requires conversation-specific/systematic discrimination before changing transport.

### TD-011 — Official ChatGPT iOS interaction is the default UI baseline

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Product UI / interaction / user experience
- **Decision**: Use the current official ChatGPT iOS interaction model as the default behavior baseline where acceptable. Implement it directly in feature work; target native UIKit/system behavior rather than pixel-perfect copying.
- **Evidence**: User-provided official-App interaction recordings and explicit requirement.
- **Rejected / do-not-repeat**: Do not block native read on a separate speculative UI redesign. Do not treat the recording's injected `导出 Markdown` entry as official.
- **Affected modules**: Native shell, sidebar/navigation, conversation UI, composer, messages, menus/sheets, future advanced surfaces.
- **Validation level**: User-confirmed product requirement + visual reference; implementation requires real-device acceptance.
- **Supersedes**: Earlier open-ended UI-planning assumption.

### TD-012 — Ship small usable TrollStore candidates before roadmap completeness

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Delivery / roadmap / validation cadence
- **Decision**: Prioritize the earliest coherent usable loop. Produce uniquely identified test candidates as soon as a meaningful milestone becomes real-device testable rather than withholding use until roadmap completeness.
- **Evidence**: User explicitly wants to start using the client as soon as possible; candidate infrastructure is already established.
- **Rejected / do-not-repeat**: Do not block first use on roadmap completeness. Speed does not permit candidate identity reuse or calling CI/artifact success runtime proof.
- **Affected modules**: Roadmap, build/test cadence, all feature tasks.
- **Validation level**: User-confirmed delivery requirement; candidate pipeline runtime-proven.
- **Supersedes**: More conservative first-use sequencing.

### TD-013 — Manual sync/reload are explicit recovery actions, not automatic retry machinery

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Conversation state / reliability / recovery UX
- **Decision**: `同步最新消息` and `重载当前会话` are explicit user-triggered operations through the authoritative production conversation owner. Terminal load errors should expose direct `重新加载`. They never resend existing prompts/messages and must not become automatic retry/watchdog chains.
- **Evidence**: User-reported official-App failure classes; b8 terminal detail HTTP 500 provides direct evidence for a manual terminal reload affordance. b9 implements the terminal one-shot reload portion.
- **Alternatives considered**: Automatic stream timeout -> sync -> reload -> resend fallback chains.
- **Rejected / do-not-repeat**: No automatic resend, infinite retry, watchdog chain or second conversation-state authority. Preserve exact failure evidence.
- **Affected modules**: Conversation repository/store, read path, chat UI, later stream integration, diagnostics.
- **Validation level**: Requirement + b8 runtime failure evidence; b9 implementation is Code + CI + Artifact, runtime pending.
- **Supersedes**: None.

### TD-014 — Reasoning UI includes expandable user-visible detail and a two-pulse transition haptic

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Streaming / reasoning UX / haptics
- **Decision**: When current protocol evidence provides user-visible reasoning status/detail, present official-style subdued gray active reasoning with shimmer/flowing-light treatment; allow tap expand/collapse of explicit user-visible detail; convert to a static completed summary when supported; emit two short haptic pulses on the real-time reasoning -> final-answer transition. Haptics are lifecycle events, not render callbacks.
- **Evidence**: User-provided official-App recording and explicit real-device haptic report.
- **Rejected / do-not-repeat**: Do not vibrate per token or replay transition haptics when reloading completed content. Never expose hidden chain-of-thought.
- **Affected modules**: Future send/stream response lifecycle, reasoning presentation, message rendering.
- **Validation level**: Visual recording + user-confirmed requirement; exact implementation remains runtime Unverified until `DEV-send-stream`.
- **Supersedes**: None.

### TD-015 — Production detail diagnostics use privacy-safe hashed identity plus list position

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Conversation diagnostics / failure discrimination
- **Decision**: When a production conversation request must be correlated across selection, request, response/failure and manual retry, log an irreversible short SHA-256-derived identity marker plus the 1-based position in the currently loaded list. Never log the raw conversation ID or chat body. Keep the marker stable within the same ID so repeated attempts can be compared.
- **Evidence**: b8 produced one selected detail HTTP 500 but its diagnostics had no safe selected identity marker, so the export could not distinguish conversation-specific from systematic failure. Existing diagnostics policy already permits hashed identifiers; b9 implements the minimum local-safe equivalent before persistence/export.
- **Alternatives considered**: Raw conversation ID; title text; random per-request correlation only; broad payload logging.
- **Rejected / do-not-repeat**: No raw conversation IDs, no title-as-identity, no message/payload content logging. Do not change transport merely because one hashed selection returns HTTP 500.
- **Affected modules**: `ConversationRepository`, sidebar/detail diagnostics.
- **Validation level**: Code + CI + Artifact in b9; real-device discrimination pending.
- **Supersedes**: b8 identity-less selected-detail diagnostics.

### TD-016 — Background completion uses a public baseline first, then an isolated TrollStore true-background experiment

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Background execution / local notifications / TrollStore-specific process control
- **Decision**: After the production send/stream lifecycle is established, implement background completion in two stages. First, `DEV-background-notify` uses the existing response lifecycle plus normal iOS background-task time and local completion notifications; if the task expires, it never resends and foreground recovery uses `同步最新消息`. Second, `DEV-trollstore-true-background` may test TrollStore-only long-running process techniques as an isolated experiment. Any elevated/background-preservation state is response-scoped and released on final/cancel/error; idle app behavior remains normal. If privilege is required, prefer a minimal helper that controls process lifetime without receiving ChatGPT cookies/tokens/message content; do not blanket-copy broad private entitlements into the main authenticated client.
- **Evidence**: User explicitly chose local completion notifications and asked to evaluate the TrollStore utility `巨魔真后台`. Public distribution material identifies that utility/developer/support range but no public source was found. Open-source TrollSpeed at `a609be260c8261ead36509c3bc4ded8479da9c40` demonstrates TrollStore/root-persona spawning plus private memorystatus/jetsam/non-freezable process controls; this proves technical plausibility of long-running TrollStore processes, not compatibility with this client's stream. Apple public background APIs do not guarantee user-selected 30-minute/1-hour execution windows.
- **Alternatives considered**: Public-only background task forever; fake 30m/1h selector; silent-audio/location background abuse; remote server holding ChatGPT credentials; immediately granting the main app platform/no-sandbox/jetsam entitlements; moving authenticated streaming into a privileged helper.
- **Rejected / do-not-repeat**: Do not promise 30m/1h until the exact candidate survives real-device tests. Do not claim the exact `巨魔真后台` implementation without source. No automatic resend/regenerate. No remote credential upload. No broad privileged helper/main-app architecture before a dedicated experiment proves necessity.
- **Affected modules**: Future send/stream lifecycle, app lifecycle, local notifications, diagnostics; possible isolated TrollStore helper/entitlements only in dedicated experiment.
- **Validation level**: User-confirmed direction + public/source research; no product implementation, candidate or runtime proof yet.
- **Supersedes**: Public-background-only planning assumption.
- **Notes**: Durable implementation/validation details are in `docs/project/BACKGROUND_EXECUTION_PLAN.md`.

## Rule

Do not write speculation here as fact. A historical plan or CI artifact is not runtime proof.
