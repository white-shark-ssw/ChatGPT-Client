# DEV-conversation-round-count

## Status

**Active — PR #27 open; b27 Runtime partial/failing; b28 identity-valid CI/Artifact ready for Runtime**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style conversation header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, centralized persisted Preferences, and evidenced list-refresh presentation corrections.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Exact b28 product/config source**: `eacd3e68469e976f6cb41a600729c211f6cd32af`. Later docs-only commits do not redefine this Runtime Candidate product source.
- **Active-work conflict guard**: only this Active dev checkpoint plus README exists; no competing Active Work/candidate conflict.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: Artifact identity rejected / permanently reserved; never reuse.
- **b25**: identity-valid Runtime partial/failing. Accepted Copy function, historical time and preference persistence; rejected header, repeated answer-jump target behavior, refresh presentation and exposed `30/29` reconcile defect.
- **Rejected reused-b25 output**: source-fix commit `2a0d313346d44dae548d996c9037fa0ac305b974` produced an already-used b25 identity; permanently invalid for testing.
- **b26**: exact source `7f845662185ef4e65a741bd37b09f9e9baebd723`, Run `33114798354`, Artifact `9664109976`, IPA SHA `24d69c62e370c7d0f8b93405a2cc164417d7798a645b510da0d0543247af308d`. Runtime accepted bounded `29/29` reconciliation and sequential answer targets, but jump smoothness and presentation defects remained.
- **b27**: exact source `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`, Run `33144420732`, Artifact `9675208202`, IPA SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b`. **Runtime partial/failing and permanently superseded.**
- **b28 current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b28`, `0.1.0 (28)`, exact product/config source `eacd3e68469e976f6cb41a600729c211f6cd32af`.

## b27 real-device evidence — 2026-08-28

User-supplied recordings and diagnostics identify exact b27 on iPhone/iOS17.0.

### Answer jump

- Stress conversation: `mappingCount=2331`, `visibleMessageCount=1063`, payload about 9.54 MB.
- Semantic target progression remains correct, including ordered targets such as `61 -> 105 -> 143 -> 165 -> 214 -> 221 -> 227` and later `253 -> 259 -> 269 -> 275`.
- Recording still shows a noticeable delay after tap before movement plus non-uniform/hitching motion.
- b27 had already removed per-frame answer-button recomputation; that hypothesis is rejected as the full cause.
- The evidenced remaining execution path was self-sizing `UITableView` plus repeated long-distance `scrollToRow(..., animated:true)`.

### Right-top refresh blank region

- Normal state: `adjustedInsetTop≈97.67`, `contentOffsetY≈-97.67`.
- After right-top refresh: `adjustedInsetTop≈131.67`, `contentOffsetY≈-131.67`, `overscrolled=false`.
- List data simultaneously remained `pageCount=28`, `totalCount=29`, `resultCount=29`.
- Therefore the blank band was not missing list data or stranded overscroll; adjusted top inset itself grew by about 34 pt.
- b27 shared presentation between the right-top button and `UIRefreshControl` and assigned an attributed title to the refresh control, matching the observed inset increase. The previous contentOffset-normalization hypothesis is rejected.

### Assistant Copy

- Functional visible-text Copy remained accepted.
- b27 `17pt` glyph in a `36×32` slot was still visibly too large versus the official ChatGPT iOS response quick-action treatment.

## b28 product corrections

### Answer-jump execution

- Retains the same `ConversationRoundProjection`, `answerRows`, direction rules and transient semantic target cursor.
- Adds only presentation state `answerJumpAnimationInFlight`.
- Resolves a target offset from the existing derived row rect, clamps to valid table bounds, and animates with native `setContentOffset(..., animated:true)`.
- A rapid second tap first stops the previous programmatic animation at the current visible offset, then immediately retargets the next derived answer.
- A real user drag clears the programmatic cursor/in-flight state and regains viewport authority.
- Animation-end diagnostics record privacy-safe target/actual offset and landing error; a >0.5pt final error is corrected nonanimated.
- No timer, debounce, watchdog, speculative retry or height-cache subsystem was added.

### Refresh presentation

- Right-top refresh and genuine pull-to-refresh now have separate selectors/presentation sources.
- Right-top refresh never changes/begins the `UIRefreshControl`; its feedback remains the existing navigation prompt.
- `UIRefreshControl.attributedTitle` was removed completely; pull refresh uses native spinner plus `endRefreshing()` only.
- b27 overscroll/top-normalization workaround was removed because Runtime disproved that root cause.
- Privacy-safe diagnostics identify refresh source and record offset/inset at presentation completion.
- Repository network/reconciliation behavior is unchanged; no second request authority or retry path exists.

### Copy visual

- Assistant Copy remains `doc.on.doc`, clear background and dynamic `.secondaryLabel`.
- Visible glyph reduced to 14pt with compact 28×28 layout slot and left alignment to match the official small response quick-action scale more closely.
- User context-menu Copy and pasteboard semantics remain unchanged.

## Exact b28 Candidate evidence

- **Candidate**: `DEV-conversation-round-count-0.1.0-b28`
- **Version / Build**: `0.1.0 (28)`
- **Product/config source**: `eacd3e68469e976f6cb41a600729c211f6cd32af`
- **Source/static audit**: pre-branch audit changed only `ConversationFeature.swift`; final atomic Candidate diff changed exactly `ConversationFeature.swift`, Xcode Build/Candidate identity and workflow Candidate/Artifact label. Repository/network/reconcile/Preferences owners were untouched.
- **Exact push CI**: Run `33149698659`, Job `98778576898`, success; checkout exact `eacd3e68469e976f6cb41a600729c211f6cd32af`; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9677214430`; Artifact ZIP digest `sha256:0f51b3172aad23471991f3c04c467bb9da1b6256558001c8f60e55fca5f26c7b`.
- **IPA**: `ChatGPTClient-0.1.0-b28-dev-conversation-round-count.ipa`; SHA-256 `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f`.
- **Embedded identity independently rechecked after download**: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=28`, `DiagnosticsCandidate=DEV-conversation-round-count-0.1.0-b28`, `DiagnosticsSourceCommit=eacd3e68469e`, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`; executable is Mach-O arm64.
- **PR merge-view CI**: Run `33149701577`, Job `98778585595`, success; checkout `refs/pull/27/merge` at `f548cc8f568136d08128cc024612f89667680616`, explicitly `Merge eacd3e68469e976f6cb41a600729c211f6cd32af into e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`.
- **Merge-view Artifact**: `9677198538`; ZIP digest `sha256:fb88b01eba0b16217e33ff0c761adff679430b64340e098cb59c459fa00331a7`; IPA SHA `6bdc868fc1e673554a8bd2badf10d9667e4d497bc7953fd079b7f2f571d99a48`. Merge-view output is merge evidence only and must not replace Runtime Artifact `9677214430`.

## Current contracts retained

- Round count and answer anchors share one derived `ConversationRoundProjection`; hidden tool/reasoning/system nodes do not create rounds.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; all three current defaults remain On.
- Current ordinary-chat detail may present `聊天`; `工作` requires an authoritative Work/Project type source and must not be guessed.
- `ConversationRepository` remains sole list/detail authority; b26 accepted total-count reconciliation is unchanged in b28.
- No new network request, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- **Code written**: b28 yes at exact source `eacd3e68469e976f6cb41a600729c211f6cd32af`.
- **Static/source audit**: Passed for the scoped b28 diff.
- **CI**: exact push CI passed; initial b28 PR merge-view CI passed.
- **Artifact produced**: exact identity-valid Runtime Artifact `9677214430`; downloaded package identity and SHA independently verified.
- **Runtime/manual/real-device**: **Pending for b28**. b27 remains partial/failing evidence; no b28 Runtime behavior is accepted yet.
- **Stable/Frozen**: **No** for this Work.

## Next exact action

Install exact push Artifact `9677214430` / IPA SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f` on the iPhone/iOS17 target. Focus the b28 Runtime retest on: rapid repeated previous/next in the same long conversation plus real-drag interruption; right-top refresh must not move the first row down or inflate adjusted top inset (compare ordinary top around the prior ~97.67 evidence); genuine pull refresh must still show native spinner and collapse cleanly; assistant Copy must look like the smaller official quick-action glyph while remaining functional in Light/Dark; timestamps stay above messages; list reconciliation remains at/below authoritative total; A/B anchors and Sync/Reload remain sane. Do not merge PR #27 or claim Stable before exact b28 passes Runtime.
