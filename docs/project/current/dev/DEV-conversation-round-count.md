# DEV-conversation-round-count

## Status

**Active — PR #27 open; b28 Runtime partial/failing; b29 identity-valid CI/Artifact ready for Runtime**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style conversation header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, centralized persisted Preferences, first-entry latest placement, and evidenced list-refresh presentation corrections.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Exact b29 product/config source**: `0b0c2fea44503423e75696f777fbf627aefac500`. Later docs-only commits do not redefine this Runtime Candidate product source.
- **Active-work conflict guard**: only this Active dev checkpoint plus README exists; no competing Active Work/candidate conflict was found at b29 allocation.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: Artifact identity rejected / permanently reserved; never reuse.
- **b25**: Runtime partial/failing. Accepted Copy function, historical time and preference persistence; rejected header, repeated answer-jump behavior and refresh presentation; exposed `30/29` reconcile defect.
- **Rejected reused-b25 output**: source-fix output reused an already-produced b25 identity; permanently invalid for testing.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound (`30 -> 29`, repeated `29/29`), sequential answer targets and compact header; jump smoothness/presentation defects remained.
- **b27**: Runtime partial/failing. On 1063 visible messages / 2331 mapping nodes semantic targets remained sequential but animation still paused/hitched; right-top refresh inflated adjusted top inset ~97.67 -> 131.67 while list stayed `28/29 -> 29`; Copy visual remained too large.
- **b28**: exact source `eacd3e68469e976f6cb41a600729c211f6cd32af`, Run `33149698659`, Artifact `9677214430`, IPA SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f`. **Runtime partial/failing and superseded by b29.**
- **b29 current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b29`, `0.1.0 (29)`, exact product/config source `0b0c2fea44503423e75696f777fbf627aefac500`.

## b28 real-device evidence — 2026-08-28

The user explicitly reported that a new recording was unnecessary because the overall behavior matched the previous run. The supplied exact-b28 diagnostics are sufficient to classify the failures below.

### Answer jump accuracy and hitch

- Stress conversation reached `visibleMessageCount=1577`.
- b28 no longer merely showed a subjective hitch: animation-completion diagnostics recorded material target drift, including approximately:
  - target row 31: landing error `-1950 pt`;
  - target row 121: landing error `-7330 pt`;
  - target row 236: landing error `-11407 pt`.
- Current source used self-sizing rows with `estimatedRowHeight=96` while computing off-screen target geometry through `rectForRow`. The large error growth as real heights resolved is consistent with the Runtime evidence.
- The b28 execution path is therefore rejected for long-conversation target accuracy/smoothness. This is evidence for removing the fixed estimated-row geometry from target calculations, not evidence for adding a speculative height-cache subsystem.

### Direction flips without user drag

- During continuous programmatic taps, diagnostics showed direction changes such as `next -> previous -> next -> previous` without corresponding real user-drag input.
- Source confirmed the cause: when both adjacent targets existed, `updateAnswerJumpButton()` fell back to `lastUserDragDirection`; that value is initialized to `.previous` on conversation presentation.
- Contract: programmatic motion is not user intent. While a programmatic target cursor exists and both directions remain valid, retain the current clicked direction; only a real drag or a boundary may override it.

### First entry was incorrectly at the top

- The documented product/UI contract already requires: no valid saved reading anchor => present latest/bottom of the current visible branch, without visibly animating through a long conversation.
- Exact b28 diagnostics on the 1577-message conversation showed the first jump beginning from `contentOffsetY≈-97.67`, i.e. the ordinary top.
- Source confirmed `restoreScrollAnchor` called `resetScrollPositionToTop()` when no saved anchor existed.
- This is a current Phase 8/read-presentation defect, not a future Send/Stream-only feature.

### Right-top refresh blank region — corrected root cause

- b28 had already removed `UIRefreshControl.attributedTitle`, yet the blank top region still reproduced.
- Source still wrote right-button refresh status through `navigationItem.prompt` (`正在刷新…`, success/failure status). `navigationItem.prompt` changes navigation-bar height and therefore changes the table's adjusted top inset.
- The durable b27/b28 explanation that the refresh-control title itself was the root cause is superseded. The accepted current root owner is the prompt-height presentation path.
- Repository list data/reconciliation remains correct and unchanged; this remains a presentation defect.

## b29 product corrections

### Stable target geometry without a second semantic authority

- `ConversationRoundProjection`, `answerRows` and the transient semantic target cursor remain unchanged as the sole answer-target derivation.
- `UITableView.estimatedRowHeight` is disabled (`0`) so long-distance row geometry is not based on the b28 fixed 96pt estimate.
- Before resolving/retargeting an answer offset, the table is laid out and the current real row rect is used.
- Interruptible native `setContentOffset(..., animated:true)` remains; rapid retargeting still stops the previous programmatic animation at the current visible offset before targeting the next derived answer.
- No timer, debounce, watchdog, retry or speculative row-height cache was added.

### Direction ownership

- When a programmatic answer target exists and both directions remain available, the button retains `currentAnswerJumpDirection` instead of falling back to stale `lastUserDragDirection`.
- A real user drag still clears the programmatic target and re-establishes direction from actual user movement.
- Boundaries still force the only valid adjacent direction.

### First-entry latest placement

- No saved reading anchor now uses `scrollToLatestMessage`: nonanimated `.bottom` placement of the last visible authoritative message after layout.
- A privacy-safe diagnostic `scrollAnchor.defaultLatest` records only target row and content offset.
- Existing per-conversation saved-anchor restoration remains unchanged.
- Existing missing-saved-anchor-message discard behavior remains a separate conditional path and was not broadened speculatively.

### Refresh presentation

- `navigationItem.prompt` is no longer used for ordinary list refresh/cache status.
- Fixed-height navigation title text is used for `正在刷新…`, success/failure/cache status; nil restores `ChatGPT`.
- Right-top refresh still never begins or mutates `UIRefreshControl`.
- `endRefreshing()` is called only when the pull control is actually refreshing.
- Repository request/reconcile behavior is unchanged.

## Exact b29 Candidate evidence

- **Candidate**: `DEV-conversation-round-count-0.1.0-b29`
- **Version / Build**: `0.1.0 (29)`
- **Product/config source**: `0b0c2fea44503423e75696f777fbf627aefac500`
- **Scoped source audit**: temporary audit commit changed only `ConversationFeature.swift`; final atomic Candidate commit changed exactly `ConversationFeature.swift`, Xcode Build/Candidate identity and workflow Candidate/Artifact label. Repository/network/reconcile/Preferences owners were untouched.
- **Exact push CI**: Run `33155124626`, Job `98795968389`, success; checkout exact `0b0c2fea44503423e75696f777fbf627aefac500`; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9679291236`; Artifact ZIP digest `sha256:a6b481acd410c97a7db37c467decc11504f3925e2a45fa9b7e2e5ba3a10e907c`.
- **IPA**: `ChatGPTClient-0.1.0-b29-dev-conversation-round-count.ipa`; SHA-256 `4378fe9b6a7340ea64a5c82063b0f7e3368e92deaf567d5e0ac40c08055a5360`.
- **Embedded identity independently rechecked after download**: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=29`, `DiagnosticsCandidate=DEV-conversation-round-count-0.1.0-b29`, `DiagnosticsSourceCommit=0b0c2fea4450`, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`; executable is Mach-O arm64.
- **Initial PR merge-view CI**: Run `33155126832`, Job `98795975759`, success; checkout `refs/pull/27/merge` at `a9a0cc286856e36df7378aa62be67f379ca631c2`, explicitly `Merge 0b0c2fea44503423e75696f777fbf627aefac500 into e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`.
- **Merge-view Artifact**: `9679295199`; ZIP digest `sha256:873fe48beef6d5626e3fc1eae5b42ff0c3fba5cb37eba77f586f6f9f950c7fd1`; merge-view IPA SHA `15dfed506a9ddc725c2b072222b2111ae23cc8e8d51079eebccbf75f76e4a3d9`. Merge-view output is merge evidence only and must not replace Runtime Artifact `9679291236`.

## Current contracts retained

- Round count and answer anchors share one derived `ConversationRoundProjection`; hidden tool/reasoning/system nodes do not create rounds.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; all three current defaults remain On.
- Current ordinary-chat detail may present `聊天`; `工作` requires an authoritative Work/Project type source and must not be guessed.
- `ConversationRepository` remains sole list/detail authority; b26 accepted total-count reconciliation is unchanged in b29.
- First visible presentation with no valid saved reading anchor defaults to latest/bottom; loading-placeholder offsets are not anchors.
- No new network request, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- **Code written**: b29 yes at exact source `0b0c2fea44503423e75696f777fbf627aefac500`.
- **Static/source audit**: Passed for the scoped b29 diff.
- **CI**: exact push CI passed; initial b29 PR merge-view CI passed.
- **Artifact produced**: exact identity-valid Runtime Artifact `9679291236`; downloaded ZIP/IPA identity and SHA independently verified.
- **Runtime/manual/real-device**: **Pending for b29**. b28 is recorded partial/failing Runtime evidence.
- **Stable/Frozen**: **No** for this Work.

## Next exact action

Install exact b29 Runtime Artifact `9679291236` / IPA SHA `4378fe9b6a7340ea64a5c82063b0f7e3368e92deaf567d5e0ac40c08055a5360` on the accepted iPhone/iOS17 scope. Focus on: (1) first entry into a long conversation with no saved reading anchor starts directly at latest/bottom; (2) rapid repeated answer taps keep the clicked direction until real drag/boundary, land at the intended assistant start and no longer show b28-scale landing errors/hitch; (3) real drag immediately regains direction/context; (4) right-top refresh does not create the prior blank top band or change normal adjusted top inset; (5) genuine pull refresh still shows/collapses the native spinner without duplicate request; (6) Copy/time/preferences/header remain sane; (7) list remains at/below authoritative total; (8) A/B anchors and Sync/Reload remain sane. Do not merge PR #27 or claim Stable before exact b29 passes Runtime.
