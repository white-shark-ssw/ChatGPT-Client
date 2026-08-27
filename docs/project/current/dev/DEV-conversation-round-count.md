# DEV-conversation-round-count

## Status

**Active — PR #27 open; b25 Runtime partial/failing; b26 correction required**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style conversation header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, and centralized persisted Preferences.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open and mergeable. Resume guard on 2026-08-28 reconfirmed `main` has not advanced and branch head before this checkpoint update was `c9cc9468c5de52e097c2aca1c8ff57ef31f3d436`. No parallel Active development checkpoint/candidate conflict is known.
- **Stable predecessors**: merged b21 multi-conversation read-state baseline and merged b23 conversation-list cache-core baseline remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority; presentation fixes stay in existing sidebar/detail owners.

## Candidate history

- **b24**: `DEV-conversation-round-count-0.1.0-b24` permanently reserved / Artifact identity rejected. Run `33109613596` compiled, but stale packaging produced a cache-core-b23 Candidate/slug. Never reuse.
- **b25 exact Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b25`, `0.1.0 (25)`, exact product/config source `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`; Run `33110228837` / Job `98650799276` success; Artifact `9662219000`; IPA `ChatGPTClient-0.1.0-b25-dev-conversation-round-count.ipa`; IPA SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`. PR merge-view `2ca94890aed44493dc4b92be36056c57d5fea664`, Run `33111269347` / Job `98654406946`, also passed.
- **Next identity**: b25 is now Runtime-tested and failing, so corrected code must not reuse it. Next available candidate is `DEV-conversation-round-count-0.1.0-b26` / `0.1.0 (26)` after the evidenced fixes are written.

## b25 real-device evidence — 2026-08-28

Exact user-supplied diagnostics identify `DEV-conversation-round-count-0.1.0-b25`, source marker `5e6a61a45b5a`, iPhone, iOS17.0, Plus/personal scope.

### Runtime accepted within b25

- **Copy**: assistant visible-text Copy works; diagnostics record `interaction/message.copy` for assistant.
- **Message time**: historical timestamps display correctly enough for this test; no timestamp correctness defect reported.
- **Preferences persistence**: the three settings persist across app restart and toggle behavior is accepted by the user.

These accepted sub-results do not make b25 Stable because the same candidate has blocking presentation/navigation defects below.

### Runtime defects requiring correction

1. **Conversation header presentation — failing**
   - User screenshot versus official ChatGPT iOS screenshot shows the current `navigationItem.prompt` implementation puts `40轮` above the conversation title and expands the navigation bar substantially.
   - Latest explicit requirement: match the official compact hierarchy for this surface: conversation **title is the primary first line**, metadata is the compact second line; for the currently supported ordinary chat presentation the second line is `聊天 · N轮` when round count is enabled, and `聊天` when the round-count preference is disabled.
   - The current prompt-based layout is rejected. Use a compact native/custom `navigationItem.titleView` presentation rather than `navigationItem.prompt` for conversation metadata so the navigation bar stays at the normal compact height.
   - `工作` must not be fabricated from title text; when/if a real Work/Project type source is evidenced, it may replace the current ordinary-chat presentation label.

2. **Previous/next answer jump — failing**
   - User reports some jumps do not land at the start of the intended answer.
   - Diagnostics prove rapid repeated taps repeatedly request the same target row (`61` many times, then `105` many times, then `143` many times) instead of advancing one answer per tap while native animation is still moving.
   - Root cause in current source: each tap recomputes adjacency only from the still-changing visible rows, and far-row positioning uses a raw `rectForRow`/contentOffset calculation with self-sizing rows.
   - Correction direction: keep only a transient programmatic target cursor into the already-derived `answerRows` so consecutive taps advance from the last requested answer until a real user drag resets the cursor; use native `scrollToRow(..., .top, animated: true)` so the target assistant cell start is the navigation destination. This cursor is presentation-only and is not a second semantic round/answer authority.

3. **Conversation-list refresh presentation — failing edge case**
   - User recording shows the first row pushed down by an apparently empty refresh area, then snapping back when the existing list load completes.
   - Source proves `reloadConversations()` can be triggered by `UIRefreshControl` while `loading == true`; `loadConversations` immediately returns at `guard !loading`, leaving that newly-started refresh-control presentation active until the earlier load completion eventually calls `endRefreshing()`.
   - Minimal correction: when a refresh trigger arrives during an existing load, explicitly end that refresh-control presentation instead of leaving it orphaned. Do not add retry/debounce/timer behavior.

4. **Conversation-list reconciliation — failing invariant exposed by b25 logs**
   - b25 diagnostics show `pageCount=28`, authoritative `totalCount=29`, but `preservedOffPageCount=2` and `resultCount=30` on two reconciliations.
   - Current `reconcileConversationPage` appends every cached item absent from page 1 and ignores server total count.
   - Correction: pass authoritative parsed `total` into reconciliation and cap preserved off-page rows to `max(0, totalCount - authoritativePage.count)`. Preserve the earliest prior off-page candidates up to that bound; log any excess cached off-page rows discarded. If no authoritative total exists, retain current conservative behavior rather than inventing deletion evidence.

## Current contracts retained

- Round count and answer anchors continue to share one `ConversationRoundProjection` derived only when authoritative visible messages change.
- Hidden tool/reasoning/system nodes do not create rounds and are never copied.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; defaults stay On for round count, message time and answer quick navigation.
- No new network request, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority is permitted.

## Validation state

- Code written: b25 yes; b26 correction not yet written.
- Static/local: b25 passed source review; new Runtime evidence supersedes prior assumptions.
- CI / Artifact: b25 exact CI and Artifact passed identity checks.
- Runtime/manual/real-device: **b25 partial/failing** — Copy/time/preferences accepted; header, answer jump and list-refresh presentation rejected; logs also expose 30/29 cache-reconcile invariant failure.
- Stable/Frozen: **No** for this Work.

## Next exact action

Modify only evidenced owners in `ConversationFeature.swift` (compact titleView metadata, transient jump target cursor + native top-row scrolling, refresh-control early-return cleanup, total-bounded list reconciliation), update the UI/rule/build evidence docs to the new runtime truth, then atomically allocate Build/Candidate b26 and run exact CI/Artifact identity verification before handing b26 back for real-device testing.
