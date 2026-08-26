# DEV-conversation-recovery

## Status

**Active**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / conversation recovery`
- **Task**: Implement explicit manual `同步最新消息` and complete `重载当前会话` through the authoritative production conversation owner.
- **User intent / acceptance criteria**: Current conversation can explicitly fetch the latest server-backed detail without resending/regenerating; current conversation can be fully re-requested/rebuilt even when already loaded; terminal load error keeps direct `重新加载`; loaded conversation exposes manual recovery actions; no automatic retry/watchdog/resend chain; diagnostics distinguish recovery action/status/timing/count/diff/state transition without message bodies or auth secrets.
- **Baseline**: `main` at `3f37db66cd5ee36b632497d247c43e5f944737a0`; product code unchanged from accepted `DEV-native-read-path-0.1.0-b9` source/merge scope, with the six later `main` commits limited to project documentation. Accepted runtime baseline: b9 production native shell/list/two-detail/current-branch rendering on iPhone / iOS 17.0.
- **Working branch / PR / head commit**: `dev/conversation-recovery-20260826`; PR not created yet; branch created from `3f37db66cd5ee36b632497d247c43e5f944737a0` (checkpoint commit pending at task start).
- **Candidate identity**: Not allocated. Existing accepted highest build is b9; uniqueness must be rechecked before artifact production.
- **Evidence**: `ConversationRepository` already owns selected identity + loaded detail/current branch. Current detail load path updates `selectedConversation` only after successful server detail read. `ConversationDetailViewController.reloadCurrentConversation()` routes back through `showConversation(id:)`, while `showConversation` short-circuits when the same conversation is already loaded; therefore current loaded-state reload is not complete. No independent `同步最新消息` operation/diagnostics/menu exists on the current source. Terminal failure `重新加载` exists from b9 but was not real-device exercised.
- **Files / modules in scope**: `ChatGPTClient/Conversation/ConversationFeature.swift`; `RootViewController.swift` only if authoritative recovery routing requires it; Xcode version/build source only when allocating a test candidate; relevant `docs/project/` state/checkpoint/index files.
- **State owner / shared dependencies**: `ConversationRepository` is the authoritative production conversation owner; `ConversationDetailViewController` is a UI consumer; `AuthSessionStore`/transient native transport remain unchanged unless current evidence proves otherwise.
- **Frozen / do-not-touch**: No Frozen module. Keep accepted b9 auth/session/header/endpoint behavior unchanged; do not turn `ProtocolReadProbe` into production state; no second conversation store; no speculative timer/watchdog/retry/fallback/resend chain.
- **Parallel conflicts checked against**: `docs/project/current/dev/` contained no Active development checkpoint; repository had no open PR; no `conversation-recovery` branch existed; no candidate identity is currently allocated to another Active task.
- **Completed**: Governance startup; task routing; stable-core/rule review; current branch/PR scan; b9-to-main compare (docs-only advancement); branch creation; source inspection proving current loaded-state reload short-circuit and absence of latest-message sync.
- **Validation state**: Baseline only. No recovery product code written yet; no new CI/artifact/runtime evidence yet.
- **Pending**: Implement minimum authoritative recovery operations + UI menu/actions + safe diagnostics; inspect real build/version source and CI trigger; run static/build validation; allocate unique candidate before artifact; update durable docs after evidence changes; real-device acceptance remains required.
- **Next exact action**: Inspect the full detail-controller/menu surface and build/version/CI configuration, then make the smallest `ConversationRepository` + `ConversationDetailViewController` change that gives `同步最新消息` and a force-capable full reload without adding a second state owner.
- **Rejected / do-not-repeat**: Do not implement automatic timeout/retry/watchdog; do not resend or regenerate; do not clear auth or create a second persistent session; do not infer stream-specific state before `DEV-send-stream`; do not add fallback endpoints/headers.
- **Open questions / risks**: With send/stream not yet implemented, `同步最新消息` currently reconciles the loaded read model by replacing it with the latest server detail; stream-state-specific diff semantics will be integrated later by `DEV-send-stream`. Real-device behavior of terminal reload remains Unverified until a failure or explicit loaded-state reload is manually exercised.
