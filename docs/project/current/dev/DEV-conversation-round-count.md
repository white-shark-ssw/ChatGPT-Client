# DEV-conversation-round-count

## Status

**Active — b32 Runtime partial/failing; b33 clean source/config audited; final ref target prepared**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open.
- **Current branch head before final product ref update**: `8209ab7fbc4cbefd0ecfdd7a07a99ae2edac7498`.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- **Batch A synchronization**: complete. Governance-only current main was merged into this Work; PR was mergeable and no product/state-owner conflict was found.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history summary

- **b24**: Artifact identity rejected / permanently reserved; never reuse.
- **b25-b30**: Runtime partial/failing iterations; accepted pieces are retained only where later Runtime did not reject them.
- **b31**: precise user-message round landing accepted; jump hitch, raw tool/internal rows and Copy glyph rejected.
- **b32**: exact identity valid; recipient filtering and Copy visual correction implemented. Runtime accepted internal/tool-row suppression, the compact Copy direction, and continued precise semantic landing; Runtime still rejects jump smoothness and exposed a bottom rubber-band direction bug.

## Exact b32 identity / CI / Artifact

- **Candidate**: `DEV-conversation-round-count-0.1.0-b32`
- **Version / Build**: `0.1.0 (32)`
- **Exact product/config source**: `ea2b7bf4ee89acbb748f2b3aec5fcfc61555b2bc`
- **Exact push CI**: Run `33177491033`, Job `98869786437`, success; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9688235425`; ZIP `sha256:17c6639b5ec2b106cab936c5de357b65671c116701127ed88dfbe92bb8378445`.
- **IPA**: `ChatGPTClient-0.1.0-b32-dev-conversation-round-count.ipa`; SHA-256 `f1eb4e6fb8cda58db0216df080ea90098ce681e1ed47962eebda57f803f9be80`.
- **Embedded identity from CI**: Candidate b32; source marker `ea2b7bf4ee89`.
- **PR merge-view against then-current main**: Run `33177494444`, Job `98869798207`, success on merge view `7ce392714645c62549ec99162ffe1153e6b21059`; merge-view Artifact `9688245700`; merge-view IPA SHA `dc6441790e7e9a216d8c0d3c80003377ae64266d6cd7c7710a73edd83f0e454a`. Merge-view Artifact is CI evidence only.

## b32 real-device evidence

- Exact b32 Runtime remains **partial/failing**, not Stable.
- Recipient filtering is effective in the tested long/tool-heavy conversation: diagnostics reported `filteredRecipientMessageCount=748` and ordinary visible messages reduced to `84`; the previously exposed raw connector/tool invocation rows are no longer ordinary chat rows.
- Precise semantic landing at user-message rows remains accepted.
- Copy visual/function is no longer the current blocking target.
- **Failure 1 — bottom direction**: when the table is physically at/beyond the bottom during rubber-band overscroll, delta-based drag logic can flip the adaptive control to `下一轮` even though no next round exists. Physical boundary must outrank drag delta.
- **Failure 2 — jump smoothness**: native travel still has a serious hitch even after tool-row suppression. Current b32 completion path always performs a second non-animated `scrollToRow + layoutIfNeeded` re-anchor, so the next minimal correction is to measure native landing first and correct only when actual error exceeds a small threshold.

## b33 evidence-backed correction

Only these changes are in scope:

1. Preserve `ConversationRoundProjection`, user-message semantic targets, transient requested-row cursor, real-drag ownership and native animated `scrollToRow`.
2. In adaptive direction resolution, physical top/bottom boundaries outrank the latest drag delta. Bottom including rubber-band overscroll resolves previous/up when a previous round exists; top analogously resolves next/down when applicable.
3. At `scrollViewDidEndScrollingAnimation`, measure native landing error for the requested semantic row. Apply one non-animated exact re-anchor only when absolute error is greater than `1pt`; otherwise accept the native landing without the unconditional second `scrollToRow/layoutIfNeeded` work.
4. Add privacy-safe diagnostics for `nativeLandingErrorPoints` and whether `landingCorrectionApplied` was required.
5. Do not change the accepted recipient filter, round derivation, Copy presentation, list reconciliation, network behavior, or state ownership.

## Batch recovery point — final Batch B ref boundary

**Known baseline / identity**

- Work: `DEV-conversation-round-count`
- Branch: `dev/conversation-round-count-20260828`
- Verified branch head before this checkpoint write: `8209ab7fbc4cbefd0ecfdd7a07a99ae2edac7498`.
- PR #27: open; base current main `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- b32 is permanently reserved/tested; never reuse.
- Fresh Candidate: `DEV-conversation-round-count-0.1.0-b33` / `0.1.0 (33)`.

**Clean b33 assets**

- Source blob: `027c8b3df05b0bd7a15957fe3db78c551008f744`.
- Xcode identity blob: `96a8b2124a2a6dd84ec6f682aaa9c60b205db37e`.
- Workflow identity blob: `2d3fb98fd7c1c6b129c4d1dc57558e924a14f9d0`.
- Final clean product/config commit object prepared on verified head: `607e40fffad8f893e0755f6af53abb59cdf36946`; parent `8209ab7f...`; tree `3a566c4aa2269c4829684e983cc2f235e5adc518`.
- Diff from parent is exactly 3 files: workflow identity 2+/2-, Xcode build/Candidate identity 4+/4-, source 28+/15-.
- Audit confirms no accidental duplicate request-start `.resume()` changes and no network/repository/list/filter/Copy/state-owner changes.

**Confirmed complete writes**

- Batch A governance synchronization.
- Clean b33 source/config construction and diff audit.
- This checkpoint records the final deterministic ref target. Earlier staged/audit commits are unreferenced history only and must not be used as Candidate identity.

**Remaining writes**

- Fast-forward the actual branch from the checkpoint-created head to a commit carrying the exact same clean three-file b33 delta; because this checkpoint write itself advances branch history, recovery must rebuild that deterministic three-file tree on the now-current checkpoint head rather than forcing backward to `607e40ff...`.
- Verify resulting branch and PR head/base/mergeability.
- Batch C exact push CI / Runtime Artifact / current-main PR merge-view evidence.
- Batch D durable docs/checkpoint evidence refresh.

**Next exact action**

Re-read the branch head created by this checkpoint write, create exactly one b33 product/config commit on that latest head using the three clean blobs above, verify the parent->commit diff is the same exact 3-file delta, then fast-forward branch ref and continue directly through CI/Artifact.

**Recovery must not touch / replay**

- Do not recreate/reuse b24-b32 Candidate identities or Artifacts.
- Do not use dirty blob `a09eb28b...`.
- Do not force branch backward to any earlier staged product commit; checkpoint history must remain in ancestry.
- Do not add retry/timer/watchdog/row-height cache/alternate navigation owner/network route/duplicate request start/second list or conversation authority.
- Do not modify another task checkpoint.

## Validation state

- **Code written**: b33 clean source/config exists and is source-audited, but final branch product commit must be rebuilt on the checkpoint-created head before claiming branch Code written.
- **Static/source audit**: clean b33 3-file delta passed.
- **CI / Artifact**: b33 pending.
- **Runtime/manual/real-device**: b32 partial/failing; b33 pending.
- **Stable/Frozen**: **No**.

## Next human gate

After exact identity-valid b33 IPA exists and CI/package identity is verified, hand that exact IPA to the user for real-device testing of bottom rubber-band direction, long-jump smoothness, landing accuracy, tool-filter regression and Copy regression. Do not merge PR #27 or claim Stable before b33 Runtime acceptance.
