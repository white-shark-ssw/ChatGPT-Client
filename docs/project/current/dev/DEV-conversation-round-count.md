# DEV-conversation-round-count

## Status

**Active — PR #27 open; b25 Runtime partial/failing; b26 Runtime partial/failing; b27 correction required**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style conversation header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, centralized persisted Preferences, and evidenced list-refresh presentation corrections.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable at the 2026-08-28 resume guard; branch head before this Runtime checkpoint update was `c0db59a1a686dfb0b5b02b43c37b977472163292`.
- **Active-work conflict guard**: `docs/project/current/dev/` contains only this checkpoint plus README; no competing Active development Work/candidate is present.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: `DEV-conversation-round-count-0.1.0-b24` permanently reserved / Artifact identity rejected. Never reuse.
- **b25**: `DEV-conversation-round-count-0.1.0-b25`, exact source `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`, Run `33110228837`, Artifact `9662219000`, IPA SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`. Runtime partial/failing; permanently superseded.
- **Rejected reused-b25 output**: source-fix commit `2a0d313346d44dae548d996c9037fa0ac305b974` auto-triggered Run `33114539883` before b26 identity allocation. It reused the already-tested b25 identity and is permanently invalid for testing.
- **b26 exact Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b26`, `0.1.0 (26)`, exact product/config source `7f845662185ef4e65a741bd37b09f9e9baebd723`; Run `33114798354` / Job `98666564839` success; Artifact `9664109976`; IPA `ChatGPTClient-0.1.0-b26-dev-conversation-round-count.ipa`; IPA SHA `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`; source marker `7f845662185e`. PR merge-view Run `33114802205` / Job `98666578310` also passed on merge view `b39afb8be316f37091beca0fd707eef75970d6e1`.
- **Next identity**: b26 is now real-device tested and not fully accepted, so corrected product code must not reuse b26. Next available candidate is `DEV-conversation-round-count-0.1.0-b27` / `0.1.0 (27)` after evidenced corrections are written.

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
   - Runtime is still failing on smoothness: user reports a noticeable pause after some taps before movement starts and occasional hitch/pause during animated scrolling.

3. **Header hierarchy present**
   - User screenshot shows the b26 compact two-line title view with conversation title first and `聊天 · 20轮` second.
   - No new header defect was reported in this round, but do not mark the header Stable independently until the Work closes.

4. **Earlier accepted behavior retained unless a regression is later reported**
   - Copy function, timestamp correctness/display and preference persistence were previously accepted. This round changes their requested presentation, not their data authority.

### b26 defects / explicit presentation changes requiring b27

1. **Answer-jump smoothness — failing**
   - User reports occasional delay after tapping before scroll movement starts and occasional mid-animation hitch.
   - Current source calls `updateAnswerJumpButton()` from every `scrollViewDidScroll`, including programmatic animation; that method recomputes targets and unconditionally resets SF Symbol image/accessibility/visibility. This is an evidenced avoidable main-thread hot path during the exact animation that is hitching.
   - Minimal first correction: programmatic animation must not update the jump control every frame. Update button state only on semantic events (tap target change, real drag-direction change/end, animation end/boundary), and avoid resetting the same image when direction did not change. Keep native scroll animation and the single derived `answerRows` authority. No timer/debounce/watchdog.
   - Self-sizing-row layout cost remains possible but Unverified; do not add a height-cache subsystem unless b27 evidence still shows hitch after removing the known per-frame work.

2. **Message timestamp placement — explicit change**
   - Move each message timestamp **above** its owning visible message instead of below it.
   - User timestamp remains aligned to the user-message side; assistant timestamp remains aligned to the assistant/document side.
   - Timestamp source remains authoritative `createTime`; formatting/omission rules do not change.

3. **Assistant Copy action styling — explicit official-App reference**
   - Functional Copy is retained, but the current blue/large icon presentation is rejected.
   - Match the supplied official-App action-row treatment: small `doc.on.doc` visual, no blue emphasis/background, subdued dynamic system tint, compact action-row placement below the assistant response.
   - Use dynamic UIKit colors such as `.secondaryLabel` so light/dark appearance changes automatically. Do not hard-code separate light/dark RGB values.
   - User-message Copy remains the native context-menu action.

4. **Conversation-list top blank refresh region — still failing**
   - User screenshot and prior real-device recording continue to show a blank region above the first conversation during top pull/refresh presentation with no visible refresh indication.
   - The b26 data reconcile is correct, so this is a sidebar scroll/refresh presentation issue only.
   - Current `UIRefreshControl` path can expose top overscroll/refresh space without a visible indicator and `endRefreshing()` alone does not guarantee immediate top normalization after the refresh interaction.
   - b27 should keep the existing single manual refresh request semantics, make the active pull-refresh state visibly identifiable with dynamic system styling, and normalize the table to `-adjustedContentInset.top` after refresh completion when the user is no longer actively dragging/decelerating and the table is still overscrolled. Do not mutate list data or issue another request to fix presentation.
   - Add privacy-safe presentation diagnostics around refresh-control state / contentOffset / adjusted inset only if needed to distinguish a remaining b27 visual failure; no titles/IDs.

## Current contracts retained

- Round count and answer anchors share one `ConversationRoundProjection` derived only when authoritative visible messages change.
- Hidden tool/reasoning/system nodes do not create rounds and are never copied.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; defaults stay On for round count, message time and answer quick navigation.
- Current ordinary-chat detail may present `聊天`; `工作` requires an authoritative Work/Project type source and must not be guessed from title/UI text.
- `ConversationRepository` remains sole list/detail authority; the accepted b26 total-count reconciliation must not be disturbed by presentation work.
- No new network request, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- Code written: b26 yes; b27 corrections not yet written.
- Static/local: b26 source review passed before Runtime; new Runtime evidence supersedes earlier smoothness assumptions.
- CI / Artifact: b26 exact Candidate CI/Artifact and product-head merge-view CI passed.
- Runtime/manual/real-device: **b26 partial/failing**. Tested positives: `resultCount` bounded to 29; semantic answer-target progression improved; compact header present. Blocking: jump smoothness/hitch, timestamp placement, Copy visual treatment, and top refresh blank presentation.
- Stable/Frozen: **No** for this Work.

## Next exact action

Modify only evidenced presentation owners in `ConversationFeature.swift`: remove answer-button per-frame programmatic-scroll work; move timestamps above messages; restyle assistant Copy as a small dynamic official-style action; fix sidebar refresh-control visibility/top normalization without changing repository reconciliation. Then source-diff audit, atomically allocate Build/Candidate b27, run exact CI/Artifact identity verification, update durable docs/PR, and hand exact b27 back for focused iPhone/iOS17 Runtime retest. Do not merge or claim Stable before b27 passes.
