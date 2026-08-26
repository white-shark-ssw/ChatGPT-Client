# DEV-multi-conversation-state

## Status

**Active**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将当前单 selected conversation detail/state owner 演进为 account-scoped 的 per-conversation resident state，为后续 send/stream 建立可靠的多会话状态与异步 freshness 基线。
- **User intent / acceptance criteria**: 普通 A -> B -> A 导航不销毁 A 的权威本地会话状态、不因 selection change 丢弃 A 的有效返回、不仅为返回 A 而重复请求；不同会话状态严格隔离；手动 Sync/Reload 只影响目标会话；旧异步结果不能覆盖较新的目标会话状态；account/context 变化后旧 resident state/late callbacks 不得进入新上下文；在真实设备测量后确定有界 resident/LRU 策略。完整接受边界以 `MULTI_CONVERSATION_STATE_PLAN.md` 为准。
- **Baseline**: `0.1.0 (15)` Stable recovery baseline; base branch `main`; base commit `f155ddb873540f7c80d6e66ebbfeb59ded26f011`; merged recovery PR #10 / runtime-accepted candidate `DEV-conversation-recovery-0.1.0-b15`.
- **Working branch / PR / head commit**: `dev/multi-conversation-state-20260827`; PR `Not created`; initial head `f155ddb873540f7c80d6e66ebbfeb59ded26f011` before this checkpoint commit.
- **Candidate identity**: `Not allocated` — must inspect real version/build source and `BUILD_TEST_INDEX.md` immediately before first testable artifact.
- **Evidence**: Recovery merged Stable; current project docs identify single-selected `ConversationRepository` freshness/request lifecycle as intentionally non-resident and place this Work next before send/stream. No product-code changes or validation yet in this Work.
- **Files / modules in scope**: expected primary owner `ChatGPTClient/Conversation/ConversationFeature.swift`; related `ConversationSidebarViewController` / `ConversationDetailViewController`, auth account-context integration, diagnostics, deterministic state-test support if justified, Xcode project only if a minimal test target is added; durable project docs after verified milestones.
- **State owner / shared dependencies**: `ConversationRepository` remains sole production conversation-data authority; verified account/workspace context remains owned by `AuthSessionStore`; UIKit selection/navigation remains presentation state only; diagnostics use existing privacy-safe owner.
- **Frozen / do-not-touch**: no business module is currently Frozen. Do not change accepted auth/protocol endpoint/header semantics, add second repository/state authority, retain UIKit hierarchy as cache, add persistent chat-body storage, retry/timer/watchdog/fallback machinery, or infer send/stream behavior before evidence.
- **Parallel conflicts checked against**: `docs/project/current/dev/` contains no Active task checkpoint as of branch creation. Existing `rules/multi-conversation-state-plan-20260827` is planning/governance only and is not reused as the development branch. No allocated candidate conflict.
- **Completed**: repository governance startup; required project/planning docs read; post-recovery sequence confirmed; Active-task/conflict scan complete; current `main` head verified; isolated development branch created.
- **Validation state**: governance/baseline verification only. `Code written`: No. `Static/local checks`: No. `CI`: No. `Artifact`: No. `Runtime/manual/real-device`: No. `Stable/Frozen`: No.
- **Pending**: inspect current real `ConversationRepository` definitions/call sites/parsers/account scope/UI consumers/diagnostics/build config; identify the smallest ownership-preserving resident-state change; determine whether minimal deterministic XCTest support is justified without delaying candidate; implement and validate incrementally.
- **Next exact action**: read current branch source for `ConversationFeature.swift`, sidebar/detail consumers, `AuthSessionStore.swift`, diagnostics, Xcode project/build workflow; map the exact single-slot state, request-generation/task lifecycle and account-context handoff before proposing code changes.
- **Rejected / do-not-repeat**: separate repository per screen/conversation; retained VC/cell cache; cancellation merely on selection/view disappearance; reload-on-every-navigation; unlimited resident detail retention; persistent body/draft disk cache without requirement; speculative retry/timer/watchdog/fallback; treating UI title/text as identity; guessing send/stream node requirements.
- **Open questions / risks**: exact current account-context key available to `ConversationRepository`; current detail model fields available to retain minimum node identity; cleanest bounded resident/LRU extraction; whether adding a minimal XCTest target is conflict-light; concrete resident bound must come from real-device measurement, not planning guess.
