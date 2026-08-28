# DEV-conversation-round-count

## Status

**Active — PR #27 open; b26 Runtime partial/failing; b27 identity-valid CI/Artifact ready for Runtime**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style conversation header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, centralized persisted Preferences, and evidenced list-refresh presentation corrections.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open. Exact b27 product/config source is `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`; later docs-only commits do not redefine the Runtime Candidate product source.
- **Active-work conflict guard**: `docs/project/current/dev/` contains only this checkpoint plus README; no competing Active development Work/candidate is present.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: `DEV-conversation-round-count-0.1.0-b24` permanently reserved / Artifact identity rejected. Never reuse.
- **b25**: `DEV-conversation-round-count-0.1.0-b25`, exact source `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`, Run `33110228837`, Artifact `9662219000`, IPA SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`. Runtime partial/failing; permanently superseded.
- **Rejected reused-b25 output**: source-fix commit `2a0d313346d44dae548d996c9037fa0ac305b974` auto-triggered Run `33114539883` before b26 identity allocation. It reused the already-tested b25 identity and is permanently invalid for testing.
- **b26 exact Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b26`, `0.1.0 (26)`, exact source `7f845662185ef4e65a741bd37b09f9e9baebd723`; Run `33114798354` / Job `98666564839` success; Artifact `9664109976`; IPA SHA `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`. Runtime partial/failing and superseded by b27.
- **b27 current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b27`, `0.1.0 (27)`, exact product/config source `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`; push Run `33144420732` / Job `98762229798` succeeded on Xcode 16.4. Exact IPA `ChatGPTClient-0.1.0-b27-dev-conversation-round-count.ipa`; IPA SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b`; embedded Candidate `DEV-conversation-round-count-0.1.0-b27`; source marker `3bda8d8d78ec`; Artifact `9675208202`; Artifact ZIP digest `sha256:038d3fe60ea49257a1f6ad0f09752facce8aeaecda484042b5df5cdb0f854cbd`.
- **b27 PR merge-view evidence**: Run `33144422834` / Job `98762236037` succeeded after checking out `refs/pull/27/merge` at `3080dee98e3f6a1029dd66c992b99bfcb09e28a4`, explicitly `Merge 3bda8d8d78ecd03e4a8d0b2343458189df4b000e into e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`. Merge-view IPA SHA is `a65987b093c63de1e3cc85aa7cbf7c3ea7beafd01fc7d061585c4fb668d5a2f7`; Artifact `9675212104`; ZIP digest `sha256:22883a26e7e38f605d71ca76aee8ab8b8cef42c142e1ee4c4c493197bec4c275`. This is merge evidence only; Runtime must use exact push Artifact `9675208202`.

## b25 Runtime evidence retained

Accepted sub-results on exact b25: assistant Copy function works, historical message time displays, and all three preferences persist across relaunch. Rejected: prompt-based header hierarchy/height, repeated answer-jump targets, redundant refresh presentation, and unbounded `28 + 2 -> 30` list reconciliation.

## b26 real-device evidence — 2026-08-28

User-supplied diagnostics identify exact `DEV-conversation-round-count-0.1.0-b26`, build 26, source marker `7f845662185e`, iPhone, iOS17.0, zh_CN, Plus/personal scope.

### Evidence accepted / improved within b26

1. **List reconciliation bound works on device**
   - Cold launch provisional cache still contained 30 historical entries, then the authoritative response returned `pageCount=28`, `totalCount=29`.
   - b26 logged `discardedExcessOffPageCount=1`, `preservedOffPageCount=1`, `resultCount=29` and persisted 29 rows.
   - Two later manual refreshes each logged `pageCount=28`, `totalCount=29`, `preservedOffPageCount=1`, `discardedExcessOffPageCount=0`, `resultCount=29`.
   - This accepts the b26 authoritative-total count bound for the tested sequence. Do not change this reconciliation logic without new evidence.

2. **Answer-jump semantic progression improved**
   - b26 no longer shows b25's rapid repeated same-target pattern. Diagnostics include sequential rapid targets such as `214 -> 221 -> 227` within the same second and later ordered previous/next progression.
   - The transient programmatic target cursor therefore fixes the evidenced duplicate-target semantic defect for this test sequence.
   - Runtime still failed on smoothness: user reported a noticeable pause after some taps before movement started and occasional hitch/pause during animated scrolling.

3. **Header hierarchy present**
   - User screenshot shows the compact two-line title view with conversation title first and `聊天 · 20轮` second.
   - No new header defect was reported in b26, but do not mark the header Stable independently until the Work closes.

4. **Earlier accepted behavior retained unless a regression is later reported**
   - Copy function, timestamp correctness/display and preference persistence were previously accepted. b27 changes requested presentation, not their data authority.

## b27 product corrections written

1. **Answer-jump animation hot path**
   - Removed `updateAnswerJumpButton()` from every programmatic `scrollViewDidScroll` frame.
   - Real drag direction updates only when the direction actually changes; button state is recomputed at semantic boundaries: drag begin/end, deceleration end, programmatic animation end and tap target change.
   - SF Symbol/accessibility state is reset only when the effective direction changes.
   - Existing native `UITableView.scrollToRow(..., at: .top, animated: true)` and `programmaticAnswerTargetRow` progression remain. No timer/debounce/watchdog/height cache was added.
   - Self-sizing row cost remains **Unverified**; do not add a height-cache subsystem unless b27 Runtime still shows hitch after this known per-frame work is removed.

2. **Message timestamp placement**
   - Timestamp is now laid out above each owning visible message.
   - User timestamp is right aligned; assistant timestamp is left aligned.
   - Source remains authoritative service `createTime`; formatting/omission behavior is unchanged.

3. **Assistant Copy treatment**
   - Functional visible-text Copy remains unchanged.
   - Assistant action now uses compact `doc.on.doc`, clear background and dynamic `.secondaryLabel` tint so light/dark appearance follows UIKit automatically.
   - User messages still use the native context-menu Copy action.
   - The action row is a stack with the Copy arranged subview hidden for user messages, so user cells do not reserve assistant action-row height.

4. **Conversation-list refresh presentation**
   - Repository list reconciliation/network semantics are unchanged.
   - Pull-to-refresh now has a visible dynamic-system title/tint (`下拉刷新` / `正在刷新…`).
   - Redundant pull while a list load is already active ends only the extra refresh presentation and starts no second request.
   - Refresh completion normalizes an otherwise stranded negative top overscroll to `-adjustedContentInset.top` once the user is no longer dragging/decelerating; if the gesture is still active, normalization waits for drag/deceleration end.
   - Added privacy-safe UI diagnostics `conversationList.refreshPresentation` / `conversationList.refreshTopNormalized` containing only refresh state, offset/inset and reason; no titles or conversation IDs.

## Current contracts retained

- Round count and answer anchors share one `ConversationRoundProjection` derived only when authoritative visible messages change.
- Hidden tool/reasoning/system nodes do not create rounds and are never copied.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; defaults stay On for round count, message time and answer quick navigation.
- Current ordinary-chat detail may present `聊天`; `工作` requires an authoritative Work/Project type source and must not be guessed from title/UI text.
- `ConversationRepository` remains sole list/detail authority; the accepted b26 total-count reconciliation is unchanged in b27.
- No new network request, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- **Code written**: b27 yes at exact source `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`.
- **Static/local**: source-only dry-run/diff audit passed before branch allocation; final candidate diff is exactly `ConversationFeature.swift`, `project.pbxproj`, and workflow, with repository reconcile/network unchanged. No separate local Xcode environment evidence exists beyond CI.
- **CI**: exact b27 push Run `33144420732` / Job `98762229798` success; PR merge-view Run `33144422834` / Job `98762236037` success.
- **Artifact produced**: exact Runtime Artifact `9675208202`, IPA SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b`, source marker `3bda8d8d78ec`.
- **Runtime/manual/real-device**: **Pending for b27**. b26 remains partial/failing; b27 has not yet been installed or manually tested.
- **Stable/Frozen**: **No** for this Work.

## Next exact action

Install exact push Artifact `9675208202` / IPA SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b` on the iPhone/iOS17 target and run the focused b27 Runtime test: rapid repeated previous/next answer jumps plus manual drag interruption; verify timestamps are above both message roles; verify compact assistant Copy in light and dark appearance; repeatedly exercise cold-load/manual/top-pull list refresh and confirm no persistent blank top region. If the list issue reproduces, capture diagnostics containing `conversationList.refreshPresentation` / `conversationList.refreshTopNormalized`. Also confirm list `resultCount` remains bounded by authoritative total, without changing the already-accepted reconcile implementation. Do not merge or claim Stable before b27 Runtime passes.
