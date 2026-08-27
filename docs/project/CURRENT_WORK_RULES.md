# Current Work — Rules

## Status

**Active**

- **Task**: 规划会话列表消息预览、持久化列表缓存与冷启动增量刷新，并与现有多会话/Send 路线隔离。
- **User intent / acceptance criteria**: 冷启动不再等待列表网络请求后才显示；列表可显示裁切消息预览但绝不为了预览批量请求所有 Conversation Detail；缓存与刷新按账号隔离；尽量增量更新而不是整页闪烁/重建；消息预览可利用持久化缓存获得最高性能。
- **Baseline**: `main@0ea4d7296f574722ec665b40633ecba42fc680e8`; rules branch `rules/conversation-list-cache-plan-20260827`; active development branch `dev/multi-conversation-state-20260827@ca2a18224d4fa10d724380144a21532f3c574da6` remains untouched.
- **Evidence / reason**: current `ConversationSummary` contains only `id/title/updateTime`; list UI calls `loadConversations()` on `viewDidLoad`; repository list state is memory-only; current parser uses only `id/title/update_time`. No current evidence proves a server-provided preview field.
- **Files in scope**: durable planning/UI docs plus a new dedicated list-cache plan; this rules checkpoint only.
- **Do-not-touch**: active multi-conversation product code/checkpoint/candidate, build/version/CI/artifact, overlapping multi-conversation durable state files.
- **Completed**: governance startup; current source/list owner inspected; core cache/preview safety direction selected.
- **Validation state**: planning only; no product Code/CI/Artifact/Runtime changes.
- **Pending**: persist cache ownership, cold-start/stale-while-refresh, incremental reconciliation, preview source/freshness/privacy, development ordering and acceptance matrix; conflict-scan; reset Rules checkpoint; PR/merge.
- **Next exact action**: add dedicated cache plan and update only non-overlapping roadmap/UI entry docs.
- **Rejected / do-not-repeat**: N Detail requests for N list rows; automatic background polling; full ConversationDetail/raw JSON disk cache solely for list preview; showing a cache from an unverified/wrong account scope.
- **Open questions / risks**: current list payload may or may not contain a usable preview-like field; verify only key/type presence in the future implementation Work. A cached preview can be locally stale if the conversation changed on another client and the list endpoint does not supply preview content.

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
