# DEV-conversation-round-count

## Status

**Active — b32 Runtime partial/failing; Batch A synchronized; b33 product/config Batch B pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open.
- **Current synchronized branch head before b33 product Batch B**: `9e90e8591dd03de618f951ee090ce1af7e7750f0`.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- **Resume-guard finding resolved**: checkpoint had recorded older `main@55216bde...` and PR mergeable state. Current main advanced by 8 governance-only commits touching `AGENTS.md` and `docs/project/DOCUMENTATION_POLICY.md`. Batch A merged current main into the Work branch at `9e90e859...`; branch verification succeeded and PR #27 is mergeable again against `main@a6e3b2bc...`.
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
2. In adaptive direction resolution, physical top/bottom boundaries outrank the latest drag delta. Bottom including rubber-band overscroll must resolve to previous/up when a previous round exists; top analogously resolves next/down when applicable.
3. At `scrollViewDidEndScrollingAnimation`, measure native landing error for the requested semantic row. Apply one non-animated exact re-anchor only when absolute error is greater than `1pt`; otherwise accept the native landing without the unconditional second `scrollToRow/layoutIfNeeded` work.
4. Add privacy-safe diagnostics for `nativeLandingErrorPoints` and whether `landingCorrectionApplied` was required.
5. Do not change the accepted recipient filter, round derivation, Copy presentation, list reconciliation, network behavior, or state ownership.

Prepared but **not yet referenced by branch history** at this recovery point:

- b33 `ConversationFeature.swift` blob: `a09eb28b0ce0042bb3f4b8191b479940cf986e12`
- b33 Xcode project blob: `96a8b2124a2a6dd84ec6f682aaa9c60b205db37e`
- b33 workflow blob: `2d3fb98fd7c1c6b129c4d1dc57558e924a14f9d0`

These blobs are staging evidence only until a verified commit/ref update attaches them to the intended branch.

## Batch recovery point — 2026-08-29 b33 continuation

**Known baseline / identity**

- Work: `DEV-conversation-round-count`
- Branch: `dev/conversation-round-count-20260828`
- Original b32 branch head: `ea2b7bf4ee89acbb748f2b3aec5fcfc61555b2bc`
- Recovery checkpoint commit: `bba11dedcacbb687b392de38a20c434c634d78a7`
- Batch A synchronized head: `9e90e8591dd03de618f951ee090ce1af7e7750f0`
- PR: #27 open and mergeable against current `main@a6e3b2bc185b8d5df90b846040387262a64e6154` after Batch A.
- b32 identity is already produced/tested and permanently reserved; **never rewrite corrected code as b32**.
- Intended fresh identity: `DEV-conversation-round-count-0.1.0-b33` / `0.1.0 (33)`.

**Intended write batches**

- **Batch A — governance synchronization**: merge/synchronize current main into the Work branch, preserving branch product source and importing only current governance changes. **Completed and verified at `9e90e859...`.**
- **Batch B — b33 product/config commit**: attach only the prepared b33 `ConversationFeature.swift`, Xcode Build/Candidate identity and matching workflow identity to the synchronized branch tree. Verify exact diff and identity before depending on the commit.
- **Batch C — CI / Artifact evidence**: allow the normal branch/pull-request workflows to run, verify exact push Candidate build and current-main PR merge view, then obtain Artifact IDs, Candidate/source markers, IPA SHA and package identity.
- **Batch D — documentation evidence**: update this checkpoint and durable `BUILD_TEST_INDEX.md` / `PROJECT_STATE.md` / `MODULE_STATUS.md` / `PROJECT_PROFILE.md` or other relevant current docs with the exact b32 Runtime and b33 Code/CI/Artifact truth. Avoid pushing docs in a way that obscures which exact product/config commit owns the Runtime Candidate.

**Confirmed complete writes**

- Recovery-point checkpoint write committed at `bba11ded...`.
- Batch A merge tree/commit/ref completed and branch verification confirms `9e90e859...` with parents `bba11ded...` + `main@a6e3b2bc...`.
- PR #27 verification after Batch A: open, mergeable, base `main@a6e3b2bc...`, head `9e90e859...`.
- The three prepared b33 blobs listed above already exist in GitHub object storage, but no branch commit/ref is claimed for them yet.

**Remaining writes**

- Batch B b33 product/config commit + branch ref update.
- Batch C exact CI / Artifact verification.
- Batch D durable docs/checkpoint evidence refresh.

**Next exact action**

Construct Batch B from synchronized tree `fa590065f4cb6459f8232895941109177c91bd4b`, attaching only the three prepared b33 blobs, create the product/config commit with parent `9e90e859...`, fast-forward the Work branch, then verify the real diff/Build/Candidate identity before waiting on CI.

**Recovery must not touch / replay**

- Do not recreate or reuse b24-b32 Candidate identities or Artifacts.
- Do not modify another task checkpoint.
- Do not rewrite accepted b31/b32 semantic round derivation or b32 recipient filter/Copy merely to chase smoothness.
- Do not add retry, timer, watchdog, speculative row-height cache, alternate navigation owner, new network route, or second conversation/list authority.
- If interrupted, re-read this checkpoint and current GitHub branch/main/PR state; perform only missing deterministic batches. Never blindly replay a prior tree/commit/ref write.

## Connector-side cleanup note

An unintended temporary branch `tmp-should-not-create` was created at `bba11ded...` during tool discovery. It contains no unique product/config change and is not a Work branch, PR, Candidate or authority. The currently exposed GitHub connector functions do not provide branch/ref deletion, so it must not be reused as task state; remove it when an authorized delete-ref path is available. This side effect does not change the selected Work identity.

## Validation state

- **Code written**: b32 yes; b33 prepared as unattached blobs, not yet branch Code written.
- **Static/source audit**: b32 passed; b33 final branch diff pending.
- **CI / Artifact**: b32 passed/produced; b33 pending.
- **Runtime/manual/real-device**: b32 partial/failing — filtering + landing accepted; bottom direction + jump smoothness rejected.
- **Stable/Frozen**: **No** for this Work.

## Next human gate

After Batch B-D complete and exact identity-valid b33 IPA exists, hand that exact IPA to the user for real-device testing focused on bottom rubber-band direction, long-jump smoothness, landing accuracy, and regression of tool filtering/Copy. Do not merge PR #27 or claim Stable before exact b33 Runtime acceptance.
