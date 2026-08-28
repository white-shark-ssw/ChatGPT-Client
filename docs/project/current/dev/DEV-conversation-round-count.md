# DEV-conversation-round-count

## Status

**Active — b32 Runtime partial/failing; exact b33 CI/Artifact ready; Runtime pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open and mergeable.
- **Exact b33 product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- **Current main at b33 Candidate production**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole conversation/list authority.

## Runtime / candidate history

- b24 identity rejected/reserved.
- b25-b30 partial/failing iterations.
- b31 accepted precise user-row landing but rejected hitch/raw internal rows/Copy glyph.
- b32 exact identity valid. Runtime accepted recipient filtering, compact Copy direction and precise semantic landing; still rejects jump smoothness and bottom-rubber-band direction.

### Exact b32

- Candidate `DEV-conversation-round-count-0.1.0-b32`; version/build `0.1.0 (32)`.
- Product/config source `ea2b7bf4ee89acbb748f2b3aec5fcfc61555b2bc`.
- Push Run/Job `33177491033` / `98869786437`, success.
- Runtime Artifact `9688235425`; ZIP `sha256:17c6639b5ec2b106cab936c5de357b65671c116701127ed88dfbe92bb8378445`.
- IPA `ChatGPTClient-0.1.0-b32-dev-conversation-round-count.ipa`; SHA `f1eb4e6fb8cda58db0216df080ea90098ce681e1ed47962eebda57f803f9be80`.
- b32 Runtime long/tool-heavy sample: `filteredRecipientMessageCount=748`, ordinary visible messages `84`; raw tool rows no longer ordinary chat rows. Landing remained precise. Bottom direction + jump smoothness rejected.

## b33 evidence-backed correction

Only these product changes are in scope and were audited in the exact product commit:

1. Preserve `ConversationRoundProjection`, user-message semantic targets, transient cursor, real-drag ownership and native animated `scrollToRow`.
2. Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll.
3. At animation completion, measure native landing; only apply one nonanimated re-anchor when absolute native landing error exceeds `1pt`.
4. Add privacy-safe `nativeLandingErrorPoints` and `landingCorrectionApplied` diagnostics.
5. Do not change accepted recipient filtering, round derivation, Copy presentation, list reconciliation, network behavior or state ownership.

Exact parent→product diff from pre-product checkpoint head `3ad0136e...` is exactly 3 files: workflow identity 2+/2-, Xcode build/Candidate identity 4+/4-, `ConversationFeature.swift` 28+/15-. Earlier dirty staged blob `a09eb28b...` is rejected and unused.

## Exact b33 Candidate / CI / Artifact

- **Candidate**: `DEV-conversation-round-count-0.1.0-b33`
- **Version / Build**: `0.1.0 (33)`
- **Exact product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`
- **Exact push Run / Job**: `33195740528` / `98932282377` — success
- **Toolchain / target**: Xcode 16.4; `arm64-apple-ios14.0`; iPhoneOS 18.5 SDK
- **Runtime Artifact**: `9695669835`
- **Artifact name**: `ChatGPTClient-DEV-conversation-round-count-0.1.0-b33`
- **Artifact ZIP digest**: `sha256:841b682ffe27a2788b2c297225705c0b4fb6bc18b527fd4e8f30c62e10312407`
- **IPA**: `ChatGPTClient-0.1.0-b33-dev-conversation-round-count.ipa`
- **IPA SHA-256**: `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`
- **Embedded identity independently inspected from downloaded Artifact**: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=33`, `DiagnosticsCandidate=DEV-conversation-round-count-0.1.0-b33`, `DiagnosticsSourceCommit=0ba15ec48fe8`, `MinimumOSVersion=14.0`, Mach-O arm64.
- CI log also prints matching Candidate/source/IPA name/SHA and `** BUILD SUCCEEDED **`.

## Current-main PR merge-view evidence

Against `main@a6e3b2bc185b8d5df90b846040387262a64e6154`:

- PR #27 remains open/mergeable.
- PR Run / Job `33195744651` / `98932296906` — success.
- GitHub checkout merge view `ca28819de6e5ed345087d04005ed05d74508881c`, with log explicitly `Merge 0ba15ec... into a6e3b2bc...`.
- Merge-view Candidate remains b33; source marker `ca28819de6e5`.
- Merge-view Artifact `9695673573`; ZIP `sha256:74799aec08cbf43cedbf1dc9c1b7bb8fd75ef524c1a0335425048f90e670f608`.
- Merge-view IPA SHA `29b578eb6c060d2e528313940e3614e476eee6c36a8d6b354f0bf8ac7f594123`.
- Merge-view output is merge evidence only. **Runtime must use exact push Artifact `9695669835`.**

## Batch recovery point — durable documentation finalization

**Known baseline / identity**

- Work branch product head at Candidate production: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- b33 Candidate identity and Artifact are produced/reserved and must never be rebuilt under corrected code.
- Current main for the above evidence: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- PR #27 open/mergeable; exact push and merge-view CI passed.

**Completed batches**

- Batch A governance synchronization complete.
- Batch B exact clean b33 product/config commit fast-forwarded to Work branch and verified.
- Batch C exact push CI/Artifact + current-main PR merge-view completed and identity verified.
- This checkpoint write starts Batch D and may advance the branch only by docs.

**Remaining Batch D writes**

- Atomically-as-practical update durable `BUILD_TEST_INDEX.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `PROJECT_SPECIFIC_RULES.md` and `DEVELOPMENT_PLAN.md` to b32 Runtime + b33 Candidate truth.
- Verify resulting branch/PR state and the latest PR merge-view after the final docs head. Docs-only commits do not redefine exact Runtime Candidate source `0ba15ec...`.
- Hand exact push IPA to the user for real-device testing. Do not merge PR #27 or claim Stable before exact b33 Runtime acceptance.

**Next exact action**

Read the branch head created by this checkpoint write; construct one durable-docs commit on that head for the six listed project docs, verify only intended docs changed, fast-forward branch, then verify current PR/base/CI state and hand off exact b33 IPA.

**Recovery must not touch / replay**

- Do not reuse b24-b32 or b33 Candidate/Artifact identity for corrected product code.
- Do not rewrite accepted b31/b32 semantic round derivation, b32 recipient filter, or Copy merely to chase smoothness.
- Do not add retry/timer/watchdog/row-height cache/alternate navigation owner/network route/duplicate request start/second conversation authority.
- Do not modify another task checkpoint.

## Connector-side cleanup note

During GitHub tool discovery, temporary branches were unintentionally created and are **not task state, Candidate, PR or authority**:

- existing earlier note: `tmp-should-not-create`
- newly confirmed: `tmp-b33-recovery-do-not-use`, `tmp-b33-recovery-do-not-use-2`, `tmp-b33-recovery-do-not-use-3`, `tmp-b33-recovery-do-not-use-4`, `tmp-b33-recovery-do-not-use-5`

They contain no unique intended product state and must never be reused. The currently exposed connector surface has no delete-ref action; remove them when an authorized branch/ref deletion path is available. This does not alter the Work branch identity.

## Validation state

- **Code written**: Yes — exact b33 product/config source `0ba15ec...`.
- **Static/source audit**: Passed for exact 3-file b33 delta.
- **CI**: Exact push passed; current-main PR merge-view passed.
- **Artifact produced**: Yes — exact Runtime Artifact `9695669835`, identity independently verified.
- **Runtime/manual/real-device**: b32 partial/failing; b33 **Pending**.
- **Stable/Frozen**: **No**.

## b33 real-device focus

1. At physical bottom, including rubber-band overscroll, adaptive control must stay/resolve to **上一轮** when a previous round exists; it must not flip to 下一轮 merely from overscroll delta.
2. Long previous/next jumps should use one smooth native animation without the prior serious end-of-animation hitch.
3. Landing must remain precise at the intended user-message round start; rapid repeated taps still advance one semantic round per tap.
4. If a correction occurs, diagnostics should show `nativeLandingErrorPoints` and `landingCorrectionApplied=true`; normal accurate native landings should often avoid correction.
5. Regression sanity: tool/internal rows remain filtered, Copy remains accepted compact visual/function, A/B anchors and Sync/Reload remain intact.
