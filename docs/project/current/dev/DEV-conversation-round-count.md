# DEV-conversation-round-count

## Status

**Active — PR #27 open; b25 Runtime partial/failing; b26 identity-valid CI/Artifact ready for Runtime**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style conversation header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, and centralized persisted Preferences.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable at last check. Main remained unchanged on the final 2026-08-28 guard. Exact b26 product/config source is `7f845662185ef4e65a741bd37b09f9e9baebd723`; later docs-only commits do not redefine the Runtime Candidate product source.
- **Active-work conflict guard**: `docs/project/current/dev/` contains only this checkpoint plus README; no competing Active development Work/candidate is present on this branch.
- **Stable predecessors**: merged b21 multi-conversation read-state baseline and merged b23 conversation-list cache-core baseline remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority; presentation fixes stay in existing sidebar/detail owners.

## Candidate history

- **b24**: `DEV-conversation-round-count-0.1.0-b24` permanently reserved / Artifact identity rejected. Run `33109613596` compiled, but stale packaging produced a cache-core-b23 Candidate/slug. Never reuse.
- **b25 exact Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b25`, `0.1.0 (25)`, exact product/config source `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`; Run `33110228837` / Job `98650799276` success; Artifact `9662219000`; IPA `ChatGPTClient-0.1.0-b25-dev-conversation-round-count.ipa`; IPA SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`. b25 is Runtime partial/failing and permanently superseded.
- **Rejected reused-b25 post-Runtime build**: source-fix commit `2a0d313346d44dae548d996c9037fa0ac305b974` automatically triggered Run `33114539883` / Job `98665686885` before the b26 identity allocation landed. That workflow succeeded and uploaded Artifact `9663935606`, but it reused the already-tested b25 Candidate identity. It is therefore **identity-invalid for testing and permanently rejected**, regardless of compile success; never install or index it as a candidate.
- **b26 current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b26`, `0.1.0 (26)`, exact product/config source `7f845662185ef4e65a741bd37b09f9e9baebd723`. Exact push Run `33114798354` / Job `98666564839` succeeded on Xcode 16.4. Actual IPA is `ChatGPTClient-0.1.0-b26-dev-conversation-round-count.ipa`; IPA SHA `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`; embedded Candidate is `DEV-conversation-round-count-0.1.0-b26`; source marker is `7f845662185e`; Artifact `9664109976`; Artifact ZIP digest `sha256:c93951d3756f2440b04f895e8aeca85ad66b4499617ff686cb7c4735d5fa51af`. This is identity-valid CI/Artifact evidence only; b26 Runtime is pending.

## b25 real-device evidence — 2026-08-28

Exact user-supplied diagnostics identify `DEV-conversation-round-count-0.1.0-b25`, source marker `5e6a61a45b5a`, iPhone, iOS17.0, Plus/personal scope.

### Runtime accepted within b25

- **Copy**: assistant visible-text Copy works; diagnostics record `interaction/message.copy` for assistant.
- **Message time**: historical timestamps display correctly enough for this test; no timestamp correctness defect reported.
- **Preferences persistence**: the three settings persist across app restart and toggle behavior is accepted by the user.

These accepted sub-results do not make b25 Stable because the same candidate has blocking presentation/navigation/list defects below.

### Runtime defects corrected in b26 code

1. **Conversation header presentation — b25 failing**
   - User screenshot versus official ChatGPT iOS screenshot shows the b25 `navigationItem.prompt` implementation put `40轮` above the conversation title and expanded the navigation bar substantially.
   - Required hierarchy for this surface: conversation **title is the primary first line**, metadata is the compact second line; for the currently supported ordinary chat presentation the second line is `聊天 · N轮` when round count is enabled, and `聊天` when the round-count preference is disabled.
   - b26 replaces detail `navigationItem.prompt` metadata with a compact `navigationItem.titleView` two-line stack: title first, secondary metadata second. `工作` remains deferred until an authoritative Work/Project type source exists; it is never inferred from title text.

2. **Previous/next answer jump — b25 failing**
   - User reports some jumps did not land at the start of the intended answer.
   - b25 diagnostics prove rapid repeated taps repeatedly requested the same target row (`61` many times, then `105` many times, then `143` many times) instead of advancing one answer per tap while native animation was still moving.
   - b26 keeps a transient `programmaticAnswerTargetRow` cursor into the existing derived `answerRows`: consecutive programmatic taps advance from the last requested answer, a real user drag clears the cursor, and semantic round/answer ownership remains `ConversationRoundProjection` only. The jump uses native `UITableView.scrollToRow(..., .top, animated: true)` so the target assistant row start is the destination. No debounce/timer/watchdog was added.

3. **Conversation-list refresh presentation — b25 failing edge case**
   - User recording shows the first row pushed down by an apparently empty refresh area, then snapping back when the existing list load completes.
   - Source proves pull-to-refresh could fire while `loading == true`; the older guard returned without ending the newly-started refresh-control presentation.
   - b26 explicitly ends that redundant `UIRefreshControl` presentation and returns without starting a duplicate request. No retry/debounce/timer behavior was added.

4. **Conversation-list reconciliation — b25 failing invariant**
   - b25 diagnostics show `pageCount=28`, authoritative `totalCount=29`, but `preservedOffPageCount=2` and `resultCount=30` on repeated reconciliations.
   - b26 passes authoritative parsed `total` into reconciliation and caps preserved off-page rows to `max(0, totalCount - authoritativePage.count)`, logging `authoritativeTotalCount` and `discardedExcessOffPageCount`. If authoritative total is absent, conservative preservation remains unchanged rather than inventing deletion evidence.
   - The identity of which stale off-page cached row should be discarded is not server-evidenced by page 1 alone; b26 preserves prior off-page order up to the authoritative count bound. Exact identity correctness remains a Runtime/evidence boundary until pagination/current service evidence can prove it.

## Current contracts retained

- Round count and answer anchors continue to share one `ConversationRoundProjection` derived only when authoritative visible messages change.
- Hidden tool/reasoning/system nodes do not create rounds and are never copied.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; defaults stay On for round count, message time and answer quick navigation.
- Current ordinary-chat detail metadata may present `聊天`; `工作` requires an authoritative Work/Project type source and must not be guessed from title/UI text.
- No new network request, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority is permitted.

## Validation state

- Code written: **b26 Yes** — exact source/config `7f845662185ef4e65a741bd37b09f9e9baebd723`.
- Static/local: source diff review passed for the four evidenced fixes; local macOS/Xcode unavailable in this environment.
- CI: exact b26 push Run `33114798354` / Job `98666564839` passed.
- Artifact: identity-valid b26 Artifact `9664109976` produced; IPA SHA `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`.
- Local artifact extraction check: downloaded Artifact ZIP was unpacked; exact IPA file existed and local SHA-256 recomputation matched `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`.
- Runtime/manual/real-device: **b25 partial/failing; b26 not tested yet**. b25 Copy/time/preferences are accepted sub-results only.
- Stable/Frozen: **No** for this Work.

## Durable docs synchronized this round

- `docs/project/PROJECT_STATE.md`: b25 Runtime partial/failing + b26 Runtime gate.
- `docs/project/MODULE_STATUS.md`: module/candidate/runtime boundaries updated.
- `docs/project/BUILD_TEST_INDEX.md`: b25 Runtime result, rejected reused-b25 output, exact b26 identity/Artifact, historical b23 SHA rechecked/corrected.
- `docs/project/DEVELOPMENT_PLAN.md`: Phase 8 and next action moved to b26 Runtime retest.
- `docs/project/UI_INTERACTION_BASELINE.md`: compact title/type/round hierarchy, rapid-tap navigation semantics and redundant refresh presentation rule updated from user evidence.

## Next exact action

Install/test exact b26 Artifact `9664109976` / IPA `ChatGPTClient-0.1.0-b26-dev-conversation-round-count.ipa` on iPhone/iOS17. Focus on: (1) compact title + `聊天 · N轮` hierarchy/height; (2) rapid repeated previous/next taps advancing one answer per tap and landing at each assistant-answer start; (3) a real drag resetting jump context; (4) pull-refresh during an existing list load leaving no invisible spacer/no duplicate request; (5) diagnostics showing authoritative-total-bounded reconciliation (`totalCount=29` => `resultCount<=29`); and (6) regression check of Copy/time/preferences. Do not merge or claim Stable until b26 Runtime passes.
