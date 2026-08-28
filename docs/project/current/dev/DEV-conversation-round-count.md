# DEV-conversation-round-count

## Status

**Active — exact b33 Runtime partial/failing; exact b34 Code/source audit complete; CI/Artifact pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Exact b33 product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- **Exact b34 product/config source**: `bf66c7080347660e0154952a261230a24bb94f7d`.
- **Current main verified for b34 product emission**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole conversation/list authority.

## Runtime / Candidate history

- b24 identity rejected/reserved.
- b25-b30 partial/failing iterations.
- b31 accepted precise user-row semantic landing but rejected residual hitch/raw internal rows/Copy visual.
- b32 Runtime accepted recipient filtering, compact Copy direction and precise semantic landing; rejected jump smoothness and physical-bottom rubber-band direction.
- b33 Runtime accepts physical-bottom direction and final semantic precision; long-distance smoothness still fails.
- b34 is the fresh correction Candidate; Code/source audit complete, Runtime not claimed.

## Exact b33 Candidate / Runtime evidence

- **Candidate**: `DEV-conversation-round-count-0.1.0-b33`
- **Version / Build**: `0.1.0 (33)`
- **Exact product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`
- **Exact push Run / Job**: `33195740528` / `98932282377` — success
- **Runtime Artifact**: `9695669835`
- **Artifact ZIP digest**: `sha256:841b682ffe27a2788b2c297225705c0b4fb6bc18b527fd4e8f30c62e10312407`
- **IPA**: `ChatGPTClient-0.1.0-b33-dev-conversation-round-count.ipa`
- **IPA SHA-256**: `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`
- **Embedded identity**: `0.1.0 (33)`, Candidate b33, source marker `0ba15ec48fe8`, minimum iOS14.0, arm64.

User-tested exact b33 on iPhone/iOS17; diagnostics metadata confirms build 33 / Candidate b33 / source `0ba15ec48fe8`.

Accepted:

1. Physical bottom including rubber-band overscroll now keeps/resolves to **上一轮** when a previous round exists.
2. Final landing remains precise at the intended user-message round start.
3. Existing recipient/tool filtering and read-state behavior remained operational in supplied diagnostics; a 19 MB Detail sample parsed 3959 mapping nodes to 96 ordinary visible messages with `filteredRecipientMessageCount=1639`.

Rejected / blocking:

1. Long-distance round jumps still feel insufficiently smooth / have a visible "gear" sensation.
2. Diagnostics contain 74 `answerJump.completed` events, of which 14 applied `landingCorrectionApplied=true`.
3. Some ordinary non-retarget completions required corrections of about 66.67pt, 203pt, 202.33pt, 496.33pt and 504pt.
4. During rapid retargeting, corrections became extreme: examples include `-1804.33`, `-2897`, `-3356.67`, `-4932.67`, `-7047.67`, `-8237`, and `-8258.67` points, while final post-correction error logged as ~0.
5. This supports the user's suspicion that the nonanimated end correction contributes materially to the perceived gear/snap behavior. b33 is **Runtime partial/failing**, not Stable.

## Exact b34 scoped correction

- **Candidate reserved**: `DEV-conversation-round-count-0.1.0-b34`
- **Version / Build**: `0.1.0 (34)`
- **Exact product/config source**: `bf66c7080347660e0154952a261230a24bb94f7d`
- **Parent checkpoint head**: `b891cffb47ba4ed469d38b590bfdb30d75b2d34e`
- Exact parent→product diff is **only 3 files**:
  - `.github/workflows/ios-foundation.yml`: 2 additions / 2 deletions, b33→b34 Candidate/Artifact labels only;
  - `ChatGPTClient.xcodeproj/project.pbxproj`: 4 additions / 4 deletions, Debug+Release build 33→34 and Candidate b33→b34 only;
  - `ChatGPTClient/Conversation/ConversationFeature.swift`: 7 additions / 1 deletion.
- The Swift delta changes only `scrollViewDidEndScrollingAnimation`:
  1. if the current `programmaticAnswerTargetRow` exists but is not in `indexPathsForVisibleRows`, log privacy-safe `answerJump.completionIgnored` with reason `current_target_not_visible` and return;
  2. do **not** clear `answerJumpAnimationInFlight` in that stale/superseded path, so the newer target animation/cursor keeps ownership;
  3. only when the current target is visible does b33's >1pt native landing measurement/correction execute;
  4. when there is no valid target, clear the in-flight flag normally.
- This retains native animated `scrollToRow` as movement owner and adds no timer, debounce, watchdog, row-height cache, fallback owner or alternate state authority.
- Accepted b33 bottom-direction rule, semantic user-row targets, b32 recipient filtering, Copy/timestamps/preferences/header, list/cache/network behavior and repository ownership are unchanged.

## Rendering observation from supplied recording — out of Phase 8 scope

The supplied official-app vs current-client recording shows headings, bold, inline code and tables rendered structurally in the official app while this client shows raw Markdown syntax. It also shows boxed-question-mark glyphs adjacent to raw `filecite ...` marker text.

Current source confirms `visibleText(from:)` merely concatenates `content.text` / string `parts`, and `ConversationMessageCell` assigns the resulting plain string directly to `UILabel.text`. There is no Markdown/rich-annotation renderer in Phase 8.

Scope decision:

- Markdown/heading/list/table/code formatting belongs to roadmap Phase 11 `DEV-message-rendering`, not this metadata/settings Work.
- The `filecite`/boxed-glyph observation appears to be an unparsed rich citation/annotation representation rather than an ordinary font-only problem. It should be investigated with message rendering/rich-content evidence, not mixed into b34.
- Do not strip or reinterpret citation markers in Phase 8 without authoritative content/annotation evidence.

## Batch recovery point — b34 product emission

- **Verified pre-product branch head**: `b891cffb47ba4ed469d38b590bfdb30d75b2d34e`.
- **Verified base**: `main@a6e3b2bc185b8d5df90b846040387262a64e6154`; PR #27 open, mergeable; it was the only open PR found.
- **Candidate**: `DEV-conversation-round-count-0.1.0-b34`, build 34. b24-b33 remain permanently reserved.
- **Batch A atomic product/config commit**: complete at `bf66c7080347660e0154952a261230a24bb94f7d`.
- **Batch B exact diff audit + branch fast-forward**: complete; exact 3-file diff verified before ref update, then branch fast-forwarded with force=false.
- **Batch C pending**: obtain exact b34 push CI/Artifact and current-main PR merge-view; inspect package identity independently.
- **Batch D pending**: update this checkpoint and durable project docs to exact b33 Runtime + b34 Candidate/Artifact truth; hand exact b34 Runtime IPA to user.
- **Next exact action**: resolve the CI run triggered by exact b34 product/config source `bf66c708...`; if successful, verify Artifact identity before any Runtime handoff.
- **Must not touch/replay**: any prior Candidate identity, Markdown/rich-content scope, repository/list/cache/network ownership, accepted b33 bottom-direction rule, accepted semantic round derivation/filtering/Copy behavior, or any other task checkpoint.

## Validation state

- **b34 Code written**: Yes — exact product/config source `bf66c708...`.
- **b34 Static/source audit**: Passed for exact 3-file delta.
- **b34 CI**: Pending.
- **b34 Artifact produced**: Pending.
- **b34 Runtime/manual/real-device**: Pending.
- **Stable/Frozen**: **No**.

## b34 Runtime focus

1. Re-run long-distance previous/next jumps and rapid repeated taps; the prior large nonanimated gear/snap events from stale retarget completions should disappear.
2. Final semantic landing must remain precise.
3. Bottom rubber-band direction must remain accepted.
4. Diagnostics should distinguish ignored stale completion from genuine visible-target completion/correction; huge corrections against a not-yet-visible current target should no longer occur.
5. Regression sanity: recipient/tool filtering, Copy, first-entry latest, A/B anchors, timestamps/preferences, list reconcile, Sync/Reload remain intact.

## Recovery must not touch / replay

- Never reuse b24-b33 Candidate/Artifact identities for corrected product code.
- Do not rewrite accepted semantic round derivation, recipient filter, Copy, cache/list/network behavior or state owners.
- Do not fold Markdown/rich-content rendering into this Work.
- Do not add retry/timer/watchdog/row-height cache/alternate navigation owner/network route/duplicate request start/second conversation authority.
- Do not modify another task checkpoint.
