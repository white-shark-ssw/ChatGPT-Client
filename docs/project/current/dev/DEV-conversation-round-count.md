# DEV-conversation-round-count

## Status

**Active — exact b34 Runtime partial/failing; b35 reserved for unified direct-position + ease-out round navigation**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Pre-b35 branch head verified**: `ea877f929f7ed958e414197294eb379f9376845a`.
- **Current main verified**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole conversation/list authority.

## Candidate history / accepted scope

- b24 identity rejected/reserved.
- b25-b30 Runtime partial/failing iterations.
- b31 accepted precise user-row semantic landing but rejected residual hitch/raw internal rows/Copy visual.
- b32 accepted recipient filtering, compact Copy direction and precise semantic landing; rejected jump smoothness and physical-bottom rubber-band direction.
- b33 accepted physical-bottom/rubber-band direction and final semantic precision; rejected long-distance/rapid jump smoothness.
- b34 removed stale/superseded completion correction against a newer not-yet-visible target, but Runtime still rejects the remaining movement feel.
- Accepted behavior that must remain unchanged: physical-bottom direction, semantic user-message round starts, sequential derived-round targeting, recipient/internal filtering, compact Copy, timestamps/preferences/header, first-entry latest, list/cache reconciliation, Sync/Reload behavior and repository/state ownership.

## Exact b34 identity / CI / Artifact

- **Candidate**: `DEV-conversation-round-count-0.1.0-b34`
- **Version / Build**: `0.1.0 (34)`
- **Exact product/config source**: `bf66c7080347660e0154952a261230a24bb94f7d`
- Push Run / Job `33200768537` / `98949366655` — success.
- Runtime Artifact `9697664416`.
- Artifact ZIP `sha256:0b05a435888c041286b331c554f31f7e64dda0a30d214014bf2a144d8b696c65`.
- IPA `ChatGPTClient-0.1.0-b34-dev-conversation-round-count.ipa`; SHA `1705a2a39941ab6aee88e13b53d68d55b2fd9ff3d43d1c50d9cdcb6613c2b9b6`.
- Independent package verification: `0.1.0 (34)`, Candidate b34, source marker `bf66c7080347`, minimum iOS14.0, arm64.
- Current-main merge-view Run / Job `33200813591` / `98949517057`, success; merge `a42408a64a4ff7fba7d799f39c897ae6930daf6f`. Merge-view Artifact is CI evidence only.

## Exact b34 Runtime result

User-tested exact b34 on iPhone/iOS17 and supplied `ChatGPTClient-Diagnostics-20260828-190001.json`; the log contains an app `ready` event identifying `DEV-conversation-round-count-0.1.0-b34`.

Runtime result:

1. A round with a long answer still produces noticeable stutter and a gear-like movement feel.
2. The user explicitly prefers to stop pursuing full-distance smooth scrolling for this Phase and instead simulate a consistent short ease-out after direct positioning.
3. Parsed b34-only events after the b34 `ready` boundary contain **42 `answerJump.requested` and 42 `answerJump.completed` events, with 0 `landingCorrectionApplied=true` and 0 `answerJump.completionIgnored`**.
4. Multiple b34 completions report `nativeLandingErrorPoints` approximately `0.00` while the user still perceives the gear effect. This materially rejects the remaining hypothesis that b33-style final correction is required for the b34 Runtime defect.
5. Current evidence instead points to `UITableView.scrollToRow(..., animated: true)` traversing long/self-sizing content as the remaining presentation problem. This is Runtime evidence for changing the movement strategy, not a claim about a UIKit defect outside this tested client path.

Therefore exact b34 is **Runtime partial/failing**, permanently reserved, and must not be rebuilt or merged as Stable.

## User-approved b35 interaction contract

The user first requested direct positioning near the target plus an ease-out finish for difficult long jumps, then explicitly clarified: **use the same method for both long and short distances to keep behavior unified.** This latest requirement supersedes the earlier Phase-8 rule that native animated `scrollToRow` must own every jump.

For every `上一轮` / `下一轮` jump in b35:

1. Preserve `ConversationRoundProjection`, `programmaticAnswerTargetRow`, adaptive direction rules and user-message round-start semantics.
2. Stop any in-progress round-jump presentation animation at its current presentation state before retargeting; no debounce/wait gate.
3. Nonanimated `scrollToRow(..., .top, animated: false)` to the semantic target and layout the table so the target's real self-sized geometry is resolved.
4. Capture the exact final target content offset produced by that direct positioning.
5. Move nonanimated to a small direction-consistent lead position approximately **120pt** away from the final target, clamped to physical scroll bounds:
   - `previous`: start below the final target (`finalY + lead`) then move upward into it;
   - `next`: start above the final target (`finalY - lead`) then move downward into it.
6. Animate only that short final segment with one UIKit `UIViewPropertyAnimator` using an approximately **0.22s ease-out** curve. The full conversation distance is never animated.
7. Final state is the captured exact target offset. Remove the b33/b34 end-of-`scrollToRow` correction path from round navigation; do not add a second correction snap.
8. Rapid repeated taps immediately stop the current short animator and repeat the same direct-position + ease-out sequence for the next semantic round.
9. A real user drag immediately stops the short animator, clears programmatic target/cursor ownership and returns direction ownership to the user's viewport.
10. No timer, watchdog, retry, row-height cache, alternate semantic index, second conversation owner, network change or Markdown/rendering work.

The `UIViewPropertyAnimator` is a presentation-only animation owner inside `ConversationDetailViewController`; it does not own semantic round state or repository data.

## Rendering observation — out of Phase 8 scope

The supplied official-app/current-client recording shows raw Markdown syntax and raw `filecite`-adjacent boxed glyphs in this client. Markdown/heading/list/table/code formatting and rich citation/annotation rendering remain Phase 11 `DEV-message-rendering`; do not mix them into b35.

## b35 identity / batch recovery point

- **Next reserved Candidate**: `DEV-conversation-round-count-0.1.0-b35`
- **Version / Build**: `0.1.0 (35)`
- b24-b34 remain permanently reserved and may not be reused.
- Current verified branch/head before b35 product emission: `dev/conversation-round-count-20260828@ea877f929f7ed958e414197294eb379f9376845a`.
- Current verified base: `main@a6e3b2bc185b8d5df90b846040387262a64e6154`; PR #27 open/mergeable; no other Active dev checkpoint exists on this task branch.
- **Batch A**: this checkpoint records b34 Runtime failure, the unified interaction decision and b35 reservation — complete when this commit is verified.
- **Batch B pending**: create one atomic product/config commit changing only Candidate/build identity plus the smallest `ConversationFeature.swift` presentation delta described above; verify exact diff before branch fast-forward.
- **Batch C pending**: exact b35 push CI/Artifact, independent package identity verification, and current-main PR merge-view.
- **Batch D pending**: update durable project docs to b34 Runtime + b35 truth, verify docs-only diff, then hand exact b35 Runtime IPA to user.
- **Next exact action**: inspect/update the existing jump presentation code only; do not replay any b34 output or touch out-of-scope modules.

## Validation state

- **b34 Runtime/manual/real-device**: **Partial/failing** — gear/stutter remains despite zero b34 end corrections in supplied trace.
- **b35 Code written**: No.
- **b35 Static/source audit**: Pending.
- **b35 CI**: Pending.
- **b35 Artifact produced**: Pending.
- **b35 Runtime/manual/real-device**: Pending.
- **Stable/Frozen**: **No**.

## b35 Runtime focus

1. Every short or long jump should visibly use the same direct-near-target + brief ease-out motion; no full-distance scrolling.
2. Long-answer jumps should no longer exhibit the previous multi-cell gear/stutter traversal.
3. Final semantic landing must stay at the intended user-message round start.
4. Rapid taps must still advance one semantic round per tap without waiting for the prior ease-out.
5. Physical-bottom/rubber-band direction must remain accepted.
6. Regression sanity: recipient/tool filtering, Copy, first-entry latest, A/B anchors, timestamps/preferences, list reconcile, Sync/Reload remain intact.

## Recovery must not touch / replay

- Never reuse b24-b34 Candidate/Artifact identities for corrected product code.
- Do not rewrite accepted semantic round derivation, recipient filter, Copy, cache/list/network behavior or state owners.
- Do not fold Markdown/rich-content rendering into this Work.
- Do not add retry/timer/watchdog/row-height cache/alternate semantic owner/network route/duplicate request start/second conversation authority.
- Do not modify another task checkpoint.
