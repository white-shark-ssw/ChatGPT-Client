# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: 将“每条用户/助手消息显示时间 + 设置开关”纳入后续开发步骤，并与现有会话轮数/统一设置 owner 规划对齐。
- **User intent / acceptance criteria**: 每条用户消息和每条 AI 可见回复都支持时间显示；设置中可统一开关；不为历史消息增加额外网络请求；不与当前 `DEV-multi-conversation-state` b18 产品实现并行冲突。
- **Baseline**: `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; rules branch `rules/message-timestamps-plan-20260827`; current multi-conversation branch head verified separately and left untouched.
- **Evidence / reason**: current `ConversationMessage` already carries optional server-derived `createTime`; current roadmap already schedules `DEV-conversation-round-count` to establish the first centralized preference owner before Send/Stream.
- **Files in scope**: `DEVELOPMENT_PLAN.md`, `CLIENT_ARCHITECTURE_GAP_REVIEW.md`, `UI_INTERACTION_BASELINE.md`, `PROJECT_SPECIFIC_RULES.md`, this rules checkpoint.
- **Do-not-touch**: active development checkpoint/branch/product code, candidate/build/artifact identity, multi-conversation b18 runtime scope.
- **Completed**: governance startup; current main/active branch/open-PR state checked; feature placement and state-owner direction determined.
- **Validation state**: Rule drafted in progress; no product Code/CI/Artifact/Runtime changes.
- **Pending**: persist exact display/source/setting semantics in durable docs; review diff; reset this checkpoint to Idle; open/merge planning PR.
- **Next exact action**: update durable planning/UI/product-rule documents on this rules branch only.
- **Rejected / do-not-repeat**: separate per-cell UserDefaults keys; mutable duplicated timestamp state; extra Detail request solely for timestamps; changing b18 product code from this rules session.
- **Open questions / risks**: exact visual date/time formatting and default toggle value are not user-specified and must remain implementation-level/unfrozen; future optimistic Send timestamps must hand off to authoritative server time rather than become a second authority.

## Active task template

When a multi-step rules task starts, switch to `Active` early and maintain:

- **Task**
- **User intent / acceptance criteria**
- **Baseline**: rule files / branch / PR / commit
- **Evidence / reason**
- **Files in scope**
- **Do-not-touch**
- **Completed**
- **Validation state**: Rule drafted / documented / PR opened / merged
- **Pending**
- **Next exact action**
- **Rejected / do-not-repeat**
- **Open questions / risks**

## Proactive checkpoint rule

The conversation/context limit is unpredictable. Once the rules problem and usable direction are clear, establish an Active checkpoint. Refresh at meaningful rule decisions, permanent-rule edits, PR state changes, or direction changes.

## Completion

When complete, move durable rules to permanent rule files, reset only this file to `Idle`, and do not modify/delete/reset any Active development checkpoint merely to finish rules work.
