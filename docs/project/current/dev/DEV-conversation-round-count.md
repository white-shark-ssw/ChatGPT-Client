# DEV-conversation-round-count

## Status

**Active — exact b33 Runtime partial/failing; exact b34 Code/Static/CI/Artifact/merge-view ready; Runtime human gate**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Exact b34 product/config source**: `bf66c7080347660e0154952a261230a24bb94f7d`.
- **Durable-docs evidence commit**: `03f4167043b86b98143023e29d40db5a5413e805`; compare from prior checkpoint head confirms exactly six durable project docs changed and no product/config/workflow change.
- **Current main at b34 validation**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole conversation/list authority.

## Runtime / Candidate history

- b24 identity rejected/reserved.
- b25-b30 partial/failing iterations.
- b31 accepted precise user-row semantic landing but rejected residual hitch/raw internal rows/Copy visual.
- b32 accepted recipient filtering, compact Copy direction and precise semantic landing; rejected jump smoothness and physical-bottom rubber-band direction.
- b33 Runtime accepts physical-bottom direction and final semantic precision; rejects long-distance/rapid jump smoothness.
- b34 is the fresh correction Candidate. Runtime is not yet claimed.

## Exact b33 Runtime evidence

- Candidate `DEV-conversation-round-count-0.1.0-b33`, version/build `0.1.0 (33)`, exact source `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- Push Run / Job `33195740528` / `98932282377`; Runtime Artifact `9695669835`; IPA SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`.
- User-tested exact b33 on iPhone/iOS17.
- Accepted: physical-bottom/rubber-band direction and final landing at intended user-message round start.
- Recipient/tool filtering remained operational; supplied long/tool-heavy response had `mappingCount=3959`, `filteredRecipientMessageCount=1639`, `visibleMessageCount=96`.
- Rejected: long-distance jumps still feel gear-like.
- Diagnostics contain 74 `answerJump.completed`; 14 applied correction. Ordinary correction examples are ~66.67–504pt. Rapid retargeting produced pre-correction native errors including `-1804.33`, `-2897`, `-3356.67`, `-4932.67`, `-7047.67`, `-8237`, `-8258.67` points, then final error ~0.
- This supports the source-backed stale/cancelled completion hypothesis and establishes b33 as **Runtime partial/failing**, not Stable.

## Exact b34 scoped correction

- **Candidate**: `DEV-conversation-round-count-0.1.0-b34`
- **Version / Build**: `0.1.0 (34)`
- **Exact product/config source**: `bf66c7080347660e0154952a261230a24bb94f7d`
- **Parent checkpoint head**: `b891cffb47ba4ed469d38b590bfdb30d75b2d34e`
- Exact parent→product diff is only 3 files:
  - `.github/workflows/ios-foundation.yml`: b33→b34 Candidate/Artifact labels only;
  - `ChatGPTClient.xcodeproj/project.pbxproj`: build 33→34 and Candidate b33→b34 only;
  - `ChatGPTClient/Conversation/ConversationFeature.swift`: 7 additions / 1 deletion.
- Swift change only affects `scrollViewDidEndScrollingAnimation`:
  1. if current `programmaticAnswerTargetRow` is not visible, log privacy-safe `answerJump.completionIgnored` / `current_target_not_visible` and return;
  2. do not clear `answerJumpAnimationInFlight` in that stale/superseded path, preserving newer target animation/cursor ownership;
  3. only when current target is visible may b33's >1pt native landing measurement/correction run;
  4. no target still clears in-flight state normally.
- Native animated `scrollToRow` remains movement owner. No timer, debounce, watchdog, row-height cache, fallback owner or alternate state authority.
- Accepted b33 bottom-direction rule, semantic user-row targets, b32 recipient filtering, Copy/timestamps/preferences/header, list/cache/network behavior and repository ownership are unchanged.

## Exact b34 push CI / Runtime Artifact

- Push Run / Job `33200768537` / `98949366655` — success.
- Exact push `head_sha`: `bf66c7080347660e0154952a261230a24bb94f7d`.
- Xcode 16.4; iPhoneOS18.5 SDK; target `arm64-apple-ios14.0`.
- Runtime Artifact `9697664416`.
- Artifact name `ChatGPTClient-DEV-conversation-round-count-0.1.0-b34`.
- Artifact ZIP digest `sha256:0b05a435888c041286b331c554f31f7e64dda0a30d214014bf2a144d8b696c65`.
- IPA `ChatGPTClient-0.1.0-b34-dev-conversation-round-count.ipa`.
- IPA SHA `1705a2a39941ab6aee88e13b53d68d55b2fd9ff3d43d1c50d9cdcb6613c2b9b6`.
- Independent local package verification matches: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=34`, `DiagnosticsCandidate=DEV-conversation-round-count-0.1.0-b34`, `DiagnosticsSourceCommit=bf66c7080347`, `MinimumOSVersion=14.0`, bundle ID `com.whitesharkssw.chatgptclient`, Mach-O arm64.

## Current-main PR merge-view evidence

- Main remained `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Merge-view used PR head `d9b3a4846e05bf04a2bce962beeef918d7b91d26`; this head adds checkpoint docs only after product source `bf66c708...`.
- PR Run / Job `33200813591` / `98949517057` — success.
- GitHub checkout explicitly used merge `a42408a64a4ff7fba7d799f39c897ae6930daf6f` = `d9b3a484...` into `main@a6e3b2...`.
- Merge-view Artifact `9697686876`; ZIP digest `sha256:82efb395840a01403fba0b4dad61c2957e6cc84c2c70b0f34f94fcfa19cc192c`; merge-view IPA SHA `54614e6a1f995b8232bc81c6af518984cc7f286bbc9d98fbd0844aba7d7e6e9e`.
- Merge-view output is CI evidence only. **Never hand it to Runtime testing in place of exact Artifact `9697664416`.**

## Rendering observation — out of Phase 8 scope

The supplied official-app/current-client recording shows raw Markdown syntax and raw `filecite`-adjacent boxed glyphs in this client. Current source only concatenates string content and assigns it to `UILabel.text`; there is no Markdown/rich-annotation renderer.

- Markdown/heading/list/table/code formatting belongs to Phase 11 `DEV-message-rendering`, not this Work.
- `filecite`/boxed-glyph behavior should be investigated as rich citation/annotation content with evidence; do not strip/reinterpret it in Phase 8.

## Batch recovery point — completed through b34 handoff

- Batch A b34 product/config commit: complete at exact source `bf66c7080347660e0154952a261230a24bb94f7d`.
- Batch B exact 3-file diff audit + branch fast-forward: complete.
- Batch C exact push CI/Artifact + independent package identity + current-main PR merge-view: complete.
- Batch D six durable project docs: complete at `03f4167043b86b98143023e29d40db5a5413e805`; exact six-file diff verified; no product/config/workflow change.
- This checkpoint write is handoff state only and does not redefine b34 product/Candidate identity.

## Current human gate / next exact action

Install/test **exact Runtime Artifact `9697664416`** / `ChatGPTClient-0.1.0-b34-dev-conversation-round-count.ipa` / SHA `1705a2a39941ab6aee88e13b53d68d55b2fd9ff3d43d1c50d9cdcb6613c2b9b6` on the accepted iPhone/iOS17 scope.

If accepted:

1. record exact b34 Runtime evidence;
2. re-check current main / PR head / conflicts / current merge-view because base may advance;
3. merge/close Phase 8 only if safe;
4. promote only exact tested scope to Stable; Frozen remains No unless explicitly justified;
5. remove only this task checkpoint on completion.

If a defect remains:

1. record exact defect first;
2. b34 remains permanently reserved;
3. allocate b35 or later before any corrected product output;
4. make only the smallest evidence-supported correction; never rebuild b34.

## Validation state

- **b34 Code written**: Yes — exact product/config source `bf66c708...`.
- **b34 Static/source audit**: Passed for exact 3-file product delta.
- **b34 CI**: Passed — exact push Run/Job `33200768537` / `98949366655`; PR merge-view Run/Job `33200813591` / `98949517057`.
- **b34 Artifact produced**: Yes — exact Runtime Artifact `9697664416`; identity independently verified.
- **b34 Runtime/manual/real-device**: **Pending**.
- **Stable/Frozen**: **No**.

## b34 real-device focus

1. Re-run long-distance previous/next jumps and rapid repeated taps; b33's stale-completion hard snap/gear effect should disappear or be materially reduced.
2. Final semantic landing must remain precise.
3. Physical-bottom/rubber-band direction must remain accepted (`上一轮` when previous exists).
4. Diagnostics may show `answerJump.completionIgnored` for stale callbacks. Huge corrections against a not-yet-visible newer target should no longer occur; any remaining `landingCorrectionApplied=true` should be inspected by magnitude.
5. Regression sanity: recipient/tool filtering, Copy, first-entry latest, A/B anchors, timestamps/preferences, list reconcile, Sync/Reload remain intact.

## Recovery must not touch / replay

- Never reuse b24-b34 Candidate/Artifact identities for corrected product code.
- Do not rewrite accepted semantic round derivation, recipient filter, Copy, cache/list/network behavior or state owners.
- Do not fold Markdown/rich-content rendering into this Work.
- Do not add retry/timer/watchdog/row-height cache/alternate navigation owner/network route/duplicate request start/second conversation authority.
- Do not modify another task checkpoint.
