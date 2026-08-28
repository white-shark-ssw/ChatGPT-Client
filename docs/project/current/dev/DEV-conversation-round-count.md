# DEV-conversation-round-count

## Status

**Active — b32 Runtime partial/failing; clean b33 product/config commit audited; Batch B ref update pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open.
- **Current branch head before clean b33 ref update**: `f240383c676bfaa1fd75a1568d67d65b41ba24c7`.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- **Batch A synchronization**: complete. Governance-only current main was merged into this Work; PR became mergeable and no product/state-owner conflict was found.
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

### Clean b33 source/config audit

- Clean source blob: `027c8b3df05b0bd7a15957fe3db78c551008f744`.
- Xcode b33 identity blob: `96a8b2124a2a6dd84ec6f682aaa9c60b205db37e`.
- Workflow b33 identity blob: `2d3fb98fd7c1c6b129c4d1dc57558e924a14f9d0`.
- Audited final product/config commit, not yet branch-referenced at this checkpoint: `155d19b043f0db86aef27ff8b881bf23f7db902d`; parent `f240383c...`; tree `e521826066720a0c216f20f961b472b9f2ca5df8`.
- Exact diff from `f240383c...` is **3 files only**: workflow identity (2+/2-), Xcode build/Candidate identity (4+/4-), and `ConversationFeature.swift` (28+/15-).
- Source audit confirms the previously detected accidental duplicate request starts are absent: no added `}.resume()` on the list request and no added `task.resume()` after storing Detail task. `AuthTransientSession.dataTask` remains the existing request-start authority.
- The source diff contains only the evidenced physical-boundary and conditional-landing-correction changes described above; no repository/list reconciliation, recipient filtering, Copy, network route, retry, timer, watchdog or second state owner change.

## Batch recovery point — 2026-08-29 b33 continuation

**Known baseline / identity**

- Work: `DEV-conversation-round-count`
- Branch: `dev/conversation-round-count-20260828`
- Branch head before Batch B ref update: `f240383c676bfaa1fd75a1568d67d65b41ba24c7`
- PR: #27 open/mergeable against current main.
- Current main: `a6e3b2bc185b8d5df90b846040387262a64e6154`
- b32 identity is already produced/tested and permanently reserved; **never rewrite corrected code as b32**.
- Fresh intended identity: `DEV-conversation-round-count-0.1.0-b33` / `0.1.0 (33)`.

**Intended write batches**

- **Batch A — governance synchronization**: complete and verified.
- **Batch B — b33 product/config commit**: clean commit `155d19b0...` audited; branch ref update still pending at this recovery boundary.
- **Batch C — CI / Artifact evidence**: after Batch B ref verification, verify exact push Candidate build and current-main PR merge view, then obtain Artifact IDs, Candidate/source markers, IPA SHA and package identity.
- **Batch D — documentation evidence**: update this checkpoint and durable `BUILD_TEST_INDEX.md` / `PROJECT_STATE.md` / `MODULE_STATUS.md` / `PROJECT_PROFILE.md` / applicable current rules with exact b32 Runtime and b33 Code/CI/Artifact truth.

**Confirmed complete writes**

- Batch A governance synchronization.
- Clean b33 blobs, tree and audited final commit object exist.
- Checkpoint now records the exact clean audit boundary before ref mutation.

**Remaining writes**

- Move Work branch ref forward to audited commit `155d19b0...` and verify branch/PR state.
- Batch C exact CI / Artifact verification.
- Batch D durable docs/checkpoint evidence refresh.

**Next exact action**

Fast-forward `dev/conversation-round-count-20260828` from current verified head to `155d19b043f0db86aef27ff8b881bf23f7db902d`, verify actual branch and PR head/base/mergeability, then continue directly into exact b33 CI/Artifact evidence.

**Recovery must not touch / replay**

- Do not recreate or reuse b24-b32 Candidate identities or Artifacts.
- Do not modify another task checkpoint.
- Do not use the earlier dirty prepared source blob `a09eb28b...` or unreferenced WIP inspection commits as b33 source identity.
- Do not rewrite accepted b31/b32 semantic round derivation or b32 recipient filter/Copy merely to chase smoothness.
- Do not add retry, timer, watchdog, speculative row-height cache, alternate navigation owner, new network route, duplicate request-start call, or second conversation/list authority.
- If interrupted, re-read this checkpoint and current GitHub branch/main/PR state; perform only missing deterministic batches. Never blindly replay a prior tree/commit/ref write.

## Validation state

- **Code written**: b32 yes; clean b33 code/config audited as commit object, branch ref pending.
- **Static/source audit**: clean b33 scoped diff passed.
- **CI / Artifact**: b32 passed/produced; b33 pending.
- **Runtime/manual/real-device**: b32 partial/failing — filtering + landing accepted; bottom direction + jump smoothness rejected.
- **Stable/Frozen**: **No** for this Work.

## Next human gate

After Batch B-D complete and exact identity-valid b33 IPA exists, hand that exact IPA to the user for real-device testing focused on bottom rubber-band direction, long-jump smoothness, landing accuracy, and regression of tool filtering/Copy. Do not merge PR #27 or claim Stable before exact b33 Runtime acceptance.
