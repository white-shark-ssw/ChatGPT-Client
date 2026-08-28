# DEV-conversation-round-count

## Status

**Active — exact b34 Runtime partial/failing; exact b35 product source emitted and exact push CI in progress**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable at last check.
- **Current main verified before b35 emission**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole conversation/list authority.

## Candidate history / accepted scope

- b24 identity rejected/reserved; b25-b30 Runtime partial/failing.
- b31 accepted precise user-message round-start landing but rejected residual hitch/raw internal rows/Copy visual.
- b32 accepted recipient filtering, compact Copy direction and semantic landing; rejected smoothness + bottom rubber-band direction.
- b33 accepted physical-bottom/rubber-band direction and final semantic precision; rejected long-distance/rapid smoothness.
- b34 removed stale/superseded completion correction against a newer not-yet-visible target, but Runtime still rejects movement feel.
- Preserve accepted physical-bottom direction, semantic user-message round starts, sequential derived-round targeting, recipient/internal filtering, compact Copy, timestamps/preferences/header, first-entry latest, list/cache reconciliation, Sync/Reload and all existing state ownership.

## Exact b34 identity / Runtime result

- Candidate `DEV-conversation-round-count-0.1.0-b34`, version/build `0.1.0 (34)`.
- Product source `bf66c7080347660e0154952a261230a24bb94f7d`.
- Push Run / Job `33200768537` / `98949366655` — success.
- Runtime Artifact `9697664416`; ZIP `sha256:0b05a435888c041286b331c554f31f7e64dda0a30d214014bf2a144d8b696c65`.
- IPA SHA `1705a2a39941ab6aee88e13b53d68d55b2fd9ff3d43d1c50d9cdcb6613c2b9b6`.
- Current-main merge-view Run / Job `33200813591` / `98949517057`, success; merge `a42408a64a4ff7fba7d799f39c897ae6930daf6f`.
- User-tested exact b34 on iPhone/iOS17. A long-answer round still produces noticeable stutter/gear feel.
- Supplied b34 trace after the b34 `ready` boundary has **42 requested / 42 completed jumps, 0 landing corrections and 0 ignored completions**. Several completions report near-zero native landing error while the user still perceives gear/stutter.
- Therefore the residual b34 issue no longer depends on the old final-correction snap; current Runtime evidence supports replacing full-distance animated `scrollToRow` for this interaction.
- b34 is **Runtime partial/failing**, permanently reserved, not Stable/Frozen.

## User-approved b35 interaction contract

The user explicitly requires **the same method for both short and long distances**.

For every `上一轮` / `下一轮` jump:

1. Keep `ConversationRoundProjection`, `programmaticAnswerTargetRow`, adaptive direction rules and user-message round-start semantics.
2. Stop any in-progress round-jump presentation animator immediately before retargeting; no debounce/wait gate.
3. Nonanimated `scrollToRow(..., .top, animated:false)` to the semantic target and lay out real self-sized geometry.
4. Capture the exact final target content offset.
5. Move nonanimated to a direction-consistent lead point about **120pt** from final, clamped to physical bounds: previous starts below final; next starts above final.
6. Animate only that final segment with `UIViewPropertyAnimator`, about **0.22s easeOut**. Full conversation distance is never animated.
7. Final state is the captured exact target offset; no second landing-correction snap.
8. Rapid taps stop the prior short animator and immediately repeat the same direct+ease-out sequence for the next semantic target.
9. Real user drag stops the animator, clears programmatic target/cursor and returns direction ownership to user intent.
10. No timer, watchdog, retry, row-height cache, alternate semantic index, second repository/state owner, network change or rendering work.

`UIViewPropertyAnimator` is presentation-only inside `ConversationDetailViewController`; it owns no conversation or semantic state.

## Exact b35 product source

- **Candidate**: `DEV-conversation-round-count-0.1.0-b35`
- **Version / Build**: `0.1.0 (35)`
- **Exact product/config source**: `c3addf775483de17a0a0a9eb81d602fc18ebe611`
- **Parent checkpoint source**: `399e7bdcbe05d5f0f2d29db89dd89260609dcb3f`
- Exact parent→product diff audited before branch fast-forward and contains only:
  - `.github/workflows/ios-foundation.yml`: 2 additions / 2 deletions, b34→b35 Candidate/Artifact labels only;
  - `ChatGPTClient.xcodeproj/project.pbxproj`: 4 additions / 4 deletions, Debug+Release build 34→35 and Candidate b34→b35 only;
  - `ChatGPTClient/Conversation/ConversationFeature.swift`: 52 additions / 37 deletions, round-jump presentation delta only.
- A temporary unreferenced source-inspection commit `00df3e5d...` exposed one manual full-file assembly typo and was never attached to the branch. It is rejected/unused. Corrected unreferenced inspection `8f6cd1c...` verified the final Swift diff before product emission; neither inspection commit is Candidate authority.
- Real branch was fast-forwarded non-force to exact b35 product source `c3addf775483...` only after the exact three-file diff passed.

### b35 implementation delta

- `answerJumpAnimationInFlight` replaced by presentation-only `UIViewPropertyAnimator?`.
- Uniform lead distance `120pt`, duration `0.22s`, `.easeOut`.
- Every jump direct-positions nonanimated to target, captures final offset, shifts to direction lead point, then animates only that short segment to final.
- Rapid retarget and real drag terminate only the short animator while preserving/clearing semantic cursor according to existing ownership rules.
- Removed round-navigation `scrollViewDidEndScrollingAnimation` correction/ignored-completion path; no second correction snap remains.
- Diagnostics now mark `presentationMode=direct_then_ease_out`, lead distance and final landing error.
- Recipient filtering, round derivation, Copy, timestamps/preferences/header, cache/list/network and repository ownership are unchanged.

## Exact b35 CI currently running

- Exact push Run `33203663621`; exact Job `98959137672`.
- Run `head_sha` independently verified as `c3addf775483de17a0a0a9eb81d602fc18ebe611`.
- Run base/associated PR still points to `main@a6e3b2bc185b8d5df90b846040387262a64e6154` at emission.
- Checkout and Toolchain steps passed; Build IPA step was in progress at this checkpoint update.
- Artifact/Runtime are not claimed until the run completes and package identity is independently verified.

## Rendering observation — out of Phase 8 scope

Raw Markdown and `filecite`-adjacent boxed glyphs from the supplied recording remain Phase 11 `DEV-message-rendering` / future rich-content evidence. Do not mix them into b35.

## Batch recovery point

- **Batch A — b34 Runtime + b35 contract/reservation**: complete at checkpoint commit `399e7bdc...`.
- **Batch B — atomic b35 product/config source + diff audit + branch fast-forward**: complete at exact product source `c3addf775483...`.
- **Batch C — exact b35 push CI/Artifact + identity verification + current-main merge-view**: in progress; exact push Run/Job `33203663621` / `98959137672`.
- **Batch D pending**: update six durable project docs to b34 Runtime + b35 Candidate/Artifact truth, verify docs-only diff, update this checkpoint to handoff state, then hand exact b35 IPA to user.
- **Next exact action**: resolve exact Run `33203663621`; on success inspect/download its Artifact and independently verify b35 package identity before Runtime handoff.
- **Must not touch/replay**: b24-b34 identities, inspection-only commits, rendering scope, repository/list/cache/network ownership, accepted bottom-direction/round/filter/Copy behavior, or another task checkpoint.

## Validation state

- **b34 Runtime/manual/real-device**: Partial/failing.
- **b35 Code written**: Yes — exact source `c3addf775483...`.
- **b35 Static/source audit**: Passed — exact three-file scoped diff.
- **b35 CI**: In progress — exact Run/Job above.
- **b35 Artifact produced**: Pending.
- **b35 Runtime/manual/real-device**: Pending.
- **Stable/Frozen**: No.

## b35 Runtime focus

1. Short and long jumps must use the same direct-near-target + brief ease-out; no full-distance traversal.
2. Long-answer jumps should no longer show the prior multi-cell gear/stutter traversal.
3. Final semantic landing must stay at the intended user-message round start.
4. Rapid taps must advance one semantic round per tap without waiting for prior ease-out.
5. Physical-bottom/rubber-band direction must remain accepted.
6. Regression sanity: recipient/tool filtering, Copy, first-entry latest, A/B anchors, timestamps/preferences, list reconcile, Sync/Reload.
