# DEV-conversation-round-count

## Status

**Active — exact b33 Runtime partial/failing; b34 correction planned, not yet produced**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Exact b33 product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- **Current main at b33 Runtime result**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole conversation/list authority.

## Runtime / Candidate history

- b24 identity rejected/reserved.
- b25-b30 partial/failing iterations.
- b31 accepted precise user-row semantic landing but rejected residual hitch/raw internal rows/Copy visual.
- b32 Runtime accepted recipient filtering, compact Copy direction and precise semantic landing; rejected jump smoothness and physical-bottom rubber-band direction.
- b33 Runtime now accepts physical-bottom direction and final semantic precision; long-distance smoothness still fails.

## Exact b33 Candidate / CI / Artifact

- **Candidate**: `DEV-conversation-round-count-0.1.0-b33`
- **Version / Build**: `0.1.0 (33)`
- **Exact product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`
- **Exact push Run / Job**: `33195740528` / `98932282377` — success
- **Runtime Artifact**: `9695669835`
- **Artifact ZIP digest**: `sha256:841b682ffe27a2788b2c297225705c0b4fb6bc18b527fd4e8f30c62e10312407`
- **IPA**: `ChatGPTClient-0.1.0-b33-dev-conversation-round-count.ipa`
- **IPA SHA-256**: `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`
- **Embedded identity**: `0.1.0 (33)`, Candidate b33, source marker `0ba15ec48fe8`, minimum iOS14.0, arm64.

## Exact b33 Runtime evidence — 2026-08-29

User-tested exact b33 on iPhone/iOS17; diagnostics metadata confirms build 33 / Candidate b33 / source `0ba15ec48fe8`.

Accepted:

1. Physical bottom including rubber-band overscroll now keeps/resolves to **上一轮** when a previous round exists. The b32 direction defect is accepted fixed for this tested path.
2. Final landing remains precise at the intended user-message round start.
3. Existing recipient/tool filtering and read-state behavior remained operational in supplied diagnostics; a 19 MB Detail sample parsed 3959 mapping nodes to 96 ordinary visible messages with `filteredRecipientMessageCount=1639`.

Rejected / blocking:

1. Long-distance round jumps still feel insufficiently smooth / have a visible "gear" sensation.
2. Diagnostics contain 74 `answerJump.completed` events, of which 14 applied `landingCorrectionApplied=true`.
3. Some ordinary non-retarget completions required corrections of about 66.67pt, 203pt, 202.33pt, 496.33pt and 504pt.
4. During rapid retargeting, corrections became extreme: examples include `-1804.33`, `-2897`, `-3356.67`, `-4932.67`, `-7047.67`, `-8237`, and `-8258.67` points, while final post-correction error logged as ~0.
5. This supports the user's suspicion that the nonanimated end correction contributes materially to the perceived gear/snap behavior. b33 is therefore **Runtime partial/failing**, not Stable.

## Source-backed b34 correction direction

Current b33 source does this on retarget:

1. if an animation is in flight, call `tableView.setContentOffset(tableView.contentOffset, animated: false)` to stop it;
2. assign the new `programmaticAnswerTargetRow`;
3. start a new native `scrollToRow(... animated:true)`;
4. every `scrollViewDidEndScrollingAnimation` callback measures/corrects against the **current** target row.

The b33 rapid-retarget trace strongly indicates that an old/cancelled animation-end callback can arrive after a newer target has become current, then apply a nonanimated correction toward that newer target before the newer animation has actually completed.

**Minimal b34 rule:** an animation-end callback may run the >1pt correction only when the current target row is actually visible. If the current target row is not visible, treat that callback as stale/superseded presentation completion, log a privacy-safe ignored-completion diagnostic, keep the current animation/cursor ownership intact, and do not snap/correct. The final callback for the current target may still measure/correct once that target is visible.

This change must not alter:

- physical top/bottom direction rule accepted on b33;
- `ConversationRoundProjection` or semantic user-row targets;
- b32 recipient filtering;
- Copy/timestamps/preferences/header;
- list reconciliation/cache/network behavior;
- repository/state ownership;
- native animated `scrollToRow` movement owner;
- no timer/debounce/watchdog/row-height cache/fallback owner.

## Rendering observation from supplied recording — out of Phase 8 scope

The supplied official-app vs current-client recording shows headings, bold, inline code and tables rendered structurally in the official app while this client shows raw Markdown syntax. It also shows boxed-question-mark glyphs adjacent to raw `filecite ...` marker text.

Current source confirms `visibleText(from:)` merely concatenates `content.text` / string `parts`, and `ConversationMessageCell` assigns the resulting plain string directly to `UILabel.text`. There is no Markdown/rich-annotation renderer in Phase 8.

Scope decision:

- Markdown/heading/list/table/code formatting belongs to roadmap Phase 11 `DEV-message-rendering`, not this metadata/settings Work.
- The `filecite`/boxed-glyph observation appears to be an unparsed rich citation/annotation representation rather than an ordinary font-only problem. It should be investigated with message rendering/rich-content evidence, not mixed into b34.
- Do not strip or reinterpret citation markers in Phase 8 without authoritative content/annotation evidence.

## Candidate allocation

- b33 is permanently reserved and must never be rebuilt with corrected code.
- Search found no existing `DEV-conversation-round-count-0.1.0-b34` identity in repository state.
- **Next candidate reserved for corrected product output: `DEV-conversation-round-count-0.1.0-b34`, `0.1.0 (34)`**, subject to final source/config commit and CI identity verification.

## Validation state

- **b33 Code written**: Yes.
- **b33 Static/source audit**: Passed.
- **b33 CI / Artifact**: Passed / produced / identity verified.
- **b33 Runtime/manual/real-device**: **Partial/failing** — direction + final precision accepted; long-distance smoothness rejected.
- **Stable/Frozen**: **No**.

## Next exact action

On the latest checkpoint head, create the smallest b34 product/config commit: build/Candidate identity 34 plus the current-target-visible guard for end-of-animation correction and an ignored-completion diagnostic. Audit the exact diff, fast-forward the Work branch, run exact push CI/Artifact and current-main PR merge-view, verify package identity, update durable docs, then hand exact b34 IPA to the user for focused real-device testing.

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
