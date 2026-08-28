# DEV-conversation-round-count

## Status

**Active — PR #27 open; b27 Runtime partial/failing; b28 correction required**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style conversation header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, centralized persisted Preferences, and evidenced list-refresh presentation corrections.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable at the 2026-08-28 b27 Runtime resume guard.
- **Current branch head before this Runtime checkpoint update**: `17d99bb1d92cd23a22cff5ef5f3c817125600ef7`; exact b27 product/config source remains `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`; commits after that source were docs-only.
- **Active-work conflict guard**: `docs/project/current/dev/` contains only this checkpoint plus README; no competing Active development Work/candidate is present.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: `DEV-conversation-round-count-0.1.0-b24` permanently reserved / Artifact identity rejected. Never reuse.
- **b25**: `DEV-conversation-round-count-0.1.0-b25`, exact source `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`, Run `33110228837`, Artifact `9662219000`, IPA SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`. Runtime partial/failing; permanently superseded.
- **Rejected reused-b25 output**: source-fix commit `2a0d313346d44dae548d996c9037fa0ac305b974` auto-triggered Run `33114539883` before b26 identity allocation. It reused the already-tested b25 identity and is permanently invalid for testing.
- **b26**: `DEV-conversation-round-count-0.1.0-b26`, exact source `7f845662185ef4e65a741bd37b09f9e9baebd723`; Run `33114798354` / Job `98666564839`; Artifact `9664109976`; IPA SHA `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`. Runtime partial/failing; accepted authoritative-total reconciliation for the tested 28/29 sequence and sequential answer-target progression, but smoothness and presentation defects remained.
- **b27**: `DEV-conversation-round-count-0.1.0-b27`, `0.1.0 (27)`, exact product/config source `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`; push Run `33144420732` / Job `98762229798` success; exact Runtime Artifact `9675208202`; IPA `ChatGPTClient-0.1.0-b27-dev-conversation-round-count.ipa`; IPA SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b`; ZIP digest `sha256:038d3fe60ea49257a1f6ad0f09752facce8aeaecda484042b5df5cdb0f854cbd`; embedded source marker `3bda8d8d78ec`. PR merge-view Run `33144422834` / Job `98762236037` also passed on merge `3080dee98e3f6a1029dd66c992b99bfcb09e28a4`. **Runtime partial/failing on exact b27 and permanently superseded for corrected output.**
- **Next identity**: corrected product code must not reuse b27. Allocate `DEV-conversation-round-count-0.1.0-b28` / `0.1.0 (28)` only after the evidenced source corrections and source-diff audit are complete and b28 uniqueness is rechecked.

## Accepted evidence retained from b25/b26

- Assistant visible-text Copy function works; hidden reasoning/tool/system content is not copied.
- Historical timestamp data/formatting and persisted Preferences worked in prior real-device tests; b27/b28 only tune presentation placement/style.
- Compact title-first header with ordinary-chat metadata is present; `工作` still requires an authoritative Work/Project type source and must never be guessed from title/UI text.
- b26 authoritative-total reconciliation is accepted for the tested sequence: a historical 30-row cache plus authoritative `pageCount=28 / totalCount=29` discarded one excess stale off-page row and produced 29; repeated manual refresh remained at 29. Do not change this reconciliation logic without contradictory evidence.
- The transient derived-answer target cursor fixes the earlier repeated-same-target semantic defect for the tested sequences. Later diagnostics show ordered targets such as `214 -> 221 -> 227`.

## b27 real-device evidence — 2026-08-28

User supplied two screen recordings (`上下跳轮卡顿.mp4`, `点击右上角刷新.mp4`) plus diagnostics export `ChatGPTClient-Diagnostics-20260828-061430.json`. Export metadata identifies exact `DEV-conversation-round-count-0.1.0-b27`, build 27, source marker `3bda8d8d78ec`, iPhone, iOS17.0, zh_CN.

### 1. Answer-jump semantics retained, smoothness still failing

- Stress conversation returned `mappingCount=2331`, `visibleMessageCount=1063`, payload ~9.54 MB; this is strong long-conversation Runtime evidence.
- Diagnostics continue to show semantic target progression rather than repeated stale targets, including sequences `61 -> 105 -> 143 -> 165 -> 214 -> 221 -> 227 -> 238 -> 241 -> 247 -> 253` and later `253 -> 259 -> 269 -> 275`.
- Screen recording visibly shows the floating jump button entering pressed state while the viewport remains stationary for a noticeable interval before movement begins, plus non-uniform/hitching movement during some jumps.
- b27 already removed per-frame programmatic answer-button recomputation, so that hypothesis is rejected as the complete cause.
- Current remaining execution path is self-sizing `UITableView` (`automaticDimension`, estimated height 96) plus repeated `scrollToRow(..., .top, animated: true)` over a 1063-message conversation. This is now the evidenced area to correct.
- Minimal b28 direction: retain the same `answerRows` and target cursor; replace queued/re-targeted `scrollToRow` behavior with interruptible native content-offset animation from the current visible offset toward the derived row rect, cancelling an in-flight programmatic animation at its current position before retargeting. Do not add timer/debounce/watchdog. Add only privacy-safe offset/target diagnostics needed to prove landing/retarget behavior. A broad height-cache subsystem remains deferred unless b28 still proves layout cost after this narrower correction.

### 2. Right-top refresh blank region — root cause corrected from prior hypothesis

- Video shows the first conversation initially flush under the navigation area, then after tapping the **right-top refresh button** the whole list is shifted down by a persistent blank band.
- Normal/automatic completion diagnostics show `adjustedInsetTop=97.67`, `contentOffsetY=-97.67`.
- After manual right-top refresh, diagnostics repeatedly show `adjustedInsetTop=131.67`, `contentOffsetY=-131.67`, `overscrolled=false`, including successful and failed manual refresh paths.
- Therefore the blank region is **not stranded overscroll**. The table itself believes `-131.67` is its real top because adjusted top inset grew by about 34 pt.
- Current source gives the same selector to the right-top refresh button and `UIRefreshControl`, and on every force refresh sets `refreshControl.attributedTitle = "正在刷新…"`; b27 also leaves a persistent `"下拉刷新"` attributed title. This is the direct presentation owner consistent with the observed ~34 pt refresh-control height/inset increase.
- b28 must separate right-top-button refresh presentation from genuine pull-to-refresh presentation. The right-top button must never alter/begin the pull refresh control; existing navigation prompt is sufficient button-refresh feedback. Remove `UIRefreshControl.attributedTitle` occupancy and the b27 content-offset normalization workaround; genuine pull refresh uses the native spinner and `endRefreshing()` only. Do not change repository request/reconciliation semantics and do not add a second request/retry.

### 3. Assistant Copy visual — functional but rejected

- b27 source uses `doc.on.doc` with `17 pt` symbol and a fixed `36 x 32 pt` button slot. User recording confirms this still appears substantially larger than the official ChatGPT iOS response action row.
- User explicitly requires the Copy treatment to match the official App, not merely be "official-style".
- OpenAI's own published iOS screenshot shows quick actions always visible below the assistant message as a compact row of small subdued outline glyphs with no emphasized button background; the Copy glyph is materially smaller than b27's current treatment.
- b28 should keep the same system `doc.on.doc` concept but reduce the visible glyph/button footprint to the official quick-action scale, clear background, subdued dynamic tint, compact below-response row, while preserving user-message context Copy and visible-text pasteboard semantics.

### 4. List data authority remains accepted

- b27 diagnostics still show `pageCount=28`, `authoritativeTotalCount=29`, `preservedOffPageCount=1`, `discardedExcessOffPageCount=0`, `resultCount=29` on repeated refreshes.
- This reinforces that the blank region is presentation/inset, not missing list data. Repository reconciliation remains unchanged for b28.

## Current contracts retained

- Round count and answer anchors share one `ConversationRoundProjection` derived only when authoritative visible messages change.
- Hidden tool/reasoning/system nodes do not create rounds and are never copied.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; defaults stay On for round count, message time and answer quick navigation.
- Current ordinary-chat detail may present `聊天`; `工作` requires an authoritative Work/Project type source and must not be guessed from title/UI text.
- `ConversationRepository` remains sole list/detail authority; accepted total-count reconciliation remains untouched.
- No new network request, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- **Code written**: b27 yes; b28 corrections not yet written at this checkpoint.
- **Static/local**: b27 source diff audit passed before CI; new Runtime evidence supersedes b27 smoothness/refresh/Copy assumptions.
- **CI / Artifact**: b27 exact Candidate CI/Artifact and PR merge-view CI passed.
- **Runtime/manual/real-device**: **b27 partial/failing**. Accepted/retained: semantic answer target progression, timestamps above messages unless later regression is reported, list reconciliation remains 29/29. Blocking: answer-jump start/mid-animation hitch, right-top refresh leaving ~34 pt persistent inset/blank region, assistant Copy visual too large versus official App.
- **Stable/Frozen**: **No** for this Work.

## Next exact action

Inspect and minimally modify only `ConversationFeature.swift` presentation owners: (1) retarget answer jumps via interruptible native offset animation instead of repeated long-distance `scrollToRow` on the self-sizing table, retaining the same derived answer semantics; (2) separate right-top refresh from pull-to-refresh and remove attributed-title/inset-normalization presentation that inflates adjusted top inset; (3) match assistant Copy to the official small inline quick-action glyph scale. Then source-diff audit, verify b28 is unused, atomically allocate Build/Candidate b28 plus workflow identity, run exact CI/Artifact + PR merge-view identity verification, update durable docs/PR, and hand exact b28 back for focused iPhone/iOS17 Runtime retest. Do not merge or claim Stable before b28 passes.
