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
- **Evidence**: Foundation through b7 real-device evidence.
- **Rejected / do-not-repeat**: Do not log passwords, OAuth codes, tokens, Cookie/Authorization values, full chat bodies or attachment contents; do not create a competing log authority without evidence.
- **Affected modules**: Whole product.
- **Validation level**: Code + CI + Artifact + real-device evidence.
- **Supersedes**: None.

### TD-005 — WebKit is the persistent login authority; tested native consumption is transient and route-specific

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Authentication sequencing / session authority / native bridge
- **Decision**: Embedded `WKWebView` at `https://chatgpt.com/auth/login` is the current authentication bootstrap. Default persistent `WKWebsiteDataStore` is the only persistent auth-secret authority. Native transport may copy current WebKit cookies transiently into ephemeral `URLSession` for evidence-backed requests; no second persistent credential store.
- **Evidence**: b2 login/persistence; b3/b4 native `/auth/login` route-specific behavior; b5-b7 transient native consumption.
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
- **Evidence**: b4-b7. b7 again produced first-attempt session 403 followed by success only after explicit user restart.
- **Rejected / do-not-repeat**: No speculative automatic retry, UA spoof, Cloudflare bypass, duplicate gate or fallback endpoint.
- **Affected modules**: AuthWebViewController, AuthSessionStore, diagnostics.
- **Validation level**: Runtime/manual/real-device tested on iPhone / iOS 17.0.
- **Supersedes**: Native `/auth/login` gating.

### TD-008 — Parse accounts-check by ordered account identity, not `accounts.default`

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Account-context response parsing
- **Decision**: Parse non-empty `account_ordering` plus keyed `accounts`; choose first ordered entry not explicitly denied and read nested `account.account_id`.
- **Evidence**: b5 contradicted old `accounts.default`; b6 and b7 verified ordered plus/personal context.
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
- **Decision**: For the tested Plus/personal account on iPhone / iOS 17.0, the current accepted first read path is transient authenticated native transport using copied ephemeral WebKit cookies + transient bearer, `GET /backend-api/conversations?offset=0&limit=28&order=updated`, then `GET /backend-api/conversation/{conversation_id}` for a returned ID. The tested request succeeded without `chatgpt-account-id` or browser-only headers. Detail identity/current-node/mapping structure is accepted for this exact scope. `ProtocolReadProbe` remains diagnostic-only; production conversation ownership belongs to the next task.
- **Evidence**: `DEV-protocol-read-0.1.0-b7`, exact product source `44a137b973e29e2a313e9114fdacb7727dccefb9`, run `32938912018`, artifact `9595827498`, user runtime export matching b7/build 7/source `44a137b973e2`, iPhone/iOS 17.0. List HTTP 200 with 28 items / total 29. First detail HTTP 200 with 13,152,411 bytes, mapping 2068 / message nodes 2067, current node present+mapped and conversation identity matched. End-to-end probe `status=ok` in 13,573.66 ms. Screenshot title `会话列表 · 会话详情通过`.
- **Alternatives considered**: Add `chatgpt-account-id` preemptively; duplicate browser headers; fallback endpoints; infer production models before runtime evidence.
- **Rejected / do-not-repeat**: Do not add account/browser headers, retries, alternate endpoints or compatibility shims without a concrete new failure. Do not generalize this personal-account success to non-personal workspaces or to send/streaming/attachments. Do not use the 13.57 s total as proof that parsing, rendering or network alone is the bottleneck.
- **Affected modules**: `AuthTransientSession`, `ProtocolReadProbe`, future `DEV-native-read-path` repository/models/rendering.
- **Validation level**: **Code + CI + Artifact + Runtime/manual/real-device tested** on iPhone / iOS 17.0.
- **Supersedes**: Phase-3 Unknown/Unverified list/detail status for the exact tested scope.
- **Notes**: The observed first detail is large (13.15 MB / 2068 mapping nodes), which is a concrete design input for native storage/parsing/rendering and long-conversation handling.

### TD-011 — Official ChatGPT iOS interaction is the default UI baseline

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Product UI / interaction / user experience
- **Decision**: Use the current official ChatGPT iOS interaction model as the default behavior baseline where the user considers it acceptable. Implement the baseline directly in feature work instead of inserting a separate visual-reinvention phase. Target native UIKit/system behavior rather than pixel-perfect copying. Explicit project enhancements should fit into the same interaction language.
- **Evidence**: User-provided official-App interaction recordings and explicit statement that the official interaction is acceptable and does not need a separate invented design language.
- **Alternatives considered**: Design a fully custom navigation/message/composer system before native read implementation.
- **Rejected / do-not-repeat**: Do not block native read on a separate speculative UI redesign. Do not cite the recording's `导出 Markdown` entry as official; user confirmed it was injected by their dylib.
- **Affected modules**: Native shell, sidebar/navigation, conversation UI, composer, messages, menus/sheets, later Projects/advanced surfaces.
- **Validation level**: User-confirmed product requirement + visual recording reference; future implementation still requires real-device acceptance.
- **Supersedes**: Earlier open-ended UI-planning assumption.
- **Notes**: Durable details live in `docs/project/UI_INTERACTION_BASELINE.md`.

### TD-012 — Ship small usable TrollStore candidates before roadmap completeness

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Delivery / roadmap / validation cadence
- **Decision**: Prioritize the earliest coherent usable loop. Produce uniquely identified test candidates as soon as a meaningful milestone becomes real-device testable, rather than withholding usage until all daily-use/advanced features are complete. V0.1 targets native read + recovery; V0.2 targets the core daily text-chat loop; later work refines breadth/performance.
- **Evidence**: User explicitly wants to start using the client as soon as possible; existing candidate/diagnostic infrastructure already supports repeated real-device validation.
- **Alternatives considered**: Complete UI breadth, attachments, search, Projects and advanced features before issuing a daily-use candidate.
- **Rejected / do-not-repeat**: Do not block first use on roadmap completeness. Speed does not permit candidate identity reuse or claiming CI/artifact success as runtime proof.
- **Affected modules**: Roadmap, build/test cadence, all feature tasks.
- **Validation level**: User-confirmed delivery requirement; existing candidate pipeline runtime-proven through b7.
- **Supersedes**: More conservative interpretation that 'weeks to maturity' implies 'weeks before first use'.

### TD-013 — Manual sync/reload are explicit recovery actions, not automatic retry machinery

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Conversation state / reliability / recovery UX
- **Decision**: Add two explicit user-triggered recovery operations after production conversation ownership exists. `同步最新消息` reconciles the current conversation with server detail when local thinking/stream state may lag server completion. `重载当前会话` re-fetches/rebuilds the current conversation after load failure/timeout/blank/unusable state. Both operate through the authoritative conversation owner and never resend existing prompts/messages.
- **Evidence**: User reports frequent real-world cases in the official App where server inference has completed/notification arrived while the App remains thinking/streaming, and separate cases where the current conversation times out or never loads.
- **Alternatives considered**: Automatic stream timeout -> sync -> reload -> resend fallback chains.
- **Rejected / do-not-repeat**: No automatic resend, infinite retry, watchdog chain or second conversation-state authority. Preserve exact failure evidence in diagnostics.
- **Affected modules**: Future conversation repository/store, network read path, chat UI, stream integration, diagnostics.
- **Validation level**: User-confirmed failure classes/requirement; implementation/runtime remains Unverified until its dedicated work.
- **Supersedes**: None.

### TD-014 — Reasoning UI includes expandable user-visible detail and a two-pulse transition haptic

- **Status**: Confirmed
- **Date**: 2026-08-26
- **Scope**: Streaming / reasoning UX / haptics
- **Decision**: When current protocol evidence provides user-visible reasoning status/detail, present an official-style subdued gray active reasoning label with shimmer/flowing-light treatment; allow tap expand/collapse of explicit user-visible detail; convert to a static completed summary such as `思考了 Xs` when supported; and emit two short haptic pulses on the real-time reasoning -> final-answer transition. Haptics are lifecycle events, not render callbacks.
- **Evidence**: User-provided official-App recording shows the reasoning visual/detail interaction; user explicitly reports the two-pulse physical feedback on real device.
- **Alternatives considered**: Plain non-interactive `正在思考`; per-token vibration; expose inferred/hidden reasoning.
- **Rejected / do-not-repeat**: Do not vibrate per token or replay transition haptics when reloading completed content. Never expose hidden chain-of-thought; only render server content explicitly intended for user display.
- **Affected modules**: Future send/stream response lifecycle, reasoning presentation, message rendering.
- **Validation level**: Visual recording + user-confirmed haptic requirement; exact implementation/intensity/spacing remains real-device Unverified until `DEV-send-stream`.
- **Supersedes**: None.

## Rule

Do not write speculation here as fact. A historical plan or CI artifact is not runtime proof.
