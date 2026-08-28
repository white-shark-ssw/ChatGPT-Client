# DEV-conversation-round-count

## Status

**Active — b32 Runtime partial/failing; exact b33 Code/Static/CI/Artifact ready; Runtime human gate**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open.
- **Exact b33 product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- **Durable-docs finalization commit**: `cfd9d53898d68dd4d4647875c0ec37a96cf27600`; exactly six durable project docs changed from the previous checkpoint head, no product/config/workflow change.
- **Current main verified after durable-docs finalization**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for their recorded scopes, not Frozen. `ConversationRepository` remains sole conversation/list authority.

## Runtime / Candidate history

- b24 identity rejected/reserved.
- b25-b30 partial/failing iterations.
- b31 accepted precise user-row semantic landing but rejected residual hitch/raw internal rows/Copy visual.
- b32 exact Runtime accepted recipient filtering, compact Copy direction and precise semantic landing; still rejected jump smoothness and physical-bottom rubber-band direction.

### Exact b32 Runtime

- Candidate `DEV-conversation-round-count-0.1.0-b32`; version/build `0.1.0 (32)`.
- Product/config source `ea2b7bf4ee89acbb748f2b3aec5fcfc61555b2bc`.
- Push Run/Job `33177491033` / `98869786437`, success.
- Runtime Artifact `9688235425`; ZIP `sha256:17c6639b5ec2b106cab936c5de357b65671c116701127ed88dfbe92bb8378445`.
- IPA `ChatGPTClient-0.1.0-b32-dev-conversation-round-count.ipa`; SHA `f1eb4e6fb8cda58db0216df080ea90098ce681e1ed47962eebda57f803f9be80`.
- Long/tool-heavy sample: `filteredRecipientMessageCount=748`, ordinary visible messages `84`; raw tool/internal rows no longer ordinary chat rows. User-round landing remained precise. Bottom direction + jump smoothness rejected.

## b33 evidence-backed correction

Only these product changes are in scope and were audited in the exact product commit:

1. Preserve `ConversationRoundProjection`, user-message semantic targets, transient cursor, real-drag ownership and native animated `scrollToRow`.
2. Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll.
3. At animation completion, measure native landing; apply one nonanimated same-target re-anchor only when absolute native landing error exceeds `1pt`.
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
- **Embedded identity independently inspected**: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=33`, `DiagnosticsCandidate=DEV-conversation-round-count-0.1.0-b33`, `DiagnosticsSourceCommit=0ba15ec48fe8`, `MinimumOSVersion=14.0`, Mach-O arm64.

## Merge / docs-head evidence

Against unchanged `main@a6e3b2bc185b8d5df90b846040387262a64e6154`:

- Exact product-source PR merge-view Run/Job `33195744651` / `98932296906` succeeded on merge `ca28819de6e5ed345087d04005ed05d74508881c`. Merge-view Artifact `9695673573` is merge evidence only.
- Durable docs were finalized in commit `cfd9d53898d68dd4d4647875c0ec37a96cf27600`; compare from prior head shows exactly `BUILD_TEST_INDEX.md`, `DEVELOPMENT_PLAN.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `PROJECT_SPECIFIC_RULES.md`, `PROJECT_STATE.md` changed.
- Final durable-docs PR Run/Job `33197708898` / `98938976553` succeeded.
- GitHub current merge view for durable-docs head is `239fbe080911cd18884a7a9172e3f281787afa39`, explicitly `Merge cfd9d538... into a6e3b2bc...`.
- Docs-head CI Artifact `9696449913` is CI/merge evidence only. **It does not replace exact Runtime Artifact `9695669835`.**

## Batch recovery point — completed

- Batch A governance synchronization: complete.
- Batch B exact clean b33 product/config commit: complete and verified.
- Batch C exact push CI/Artifact + current-main product merge-view: complete and identity verified.
- Batch D six durable project docs: complete at `cfd9d53898d68dd4d4647875c0ec37a96cf27600`; exact six-file diff verified; docs-head PR CI/merge view succeeded.
- This checkpoint write is handoff state only and does not redefine b33 product/Candidate identity.

## Current human gate / next exact action

Install and test **exact Runtime Artifact `9695669835`** / `ChatGPTClient-0.1.0-b33-dev-conversation-round-count.ipa` / SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855` on the accepted iPhone/iOS17 scope using the matrix below.

After Runtime result:

- If accepted: record exact b33 Runtime evidence, re-check current main/PR merge view and conflicts, then merge/close Phase 8 and promote only the accepted tested scope to Stable.
- If a defect remains: record the observed defect first; b33 stays permanently reserved; allocate b34 or later before any corrected product output. Do not rebuild b33.

## Recovery must not touch / replay

- Do not reuse b24-b32 or b33 Candidate/Artifact identity for corrected product code.
- Do not rewrite accepted b31/b32 semantic round derivation, b32 recipient filter, or Copy merely to chase smoothness.
- Do not add retry/timer/watchdog/row-height cache/alternate navigation owner/network route/duplicate request start/second conversation authority.
- Do not modify another task checkpoint.

## Connector-side cleanup note

Temporary branches created during earlier tool discovery are not task state, Candidate, PR or authority and must never be reused: `tmp-should-not-create`, `tmp-b33-recovery-do-not-use`, `tmp-b33-recovery-do-not-use-2`, `tmp-b33-recovery-do-not-use-3`, `tmp-b33-recovery-do-not-use-4`, `tmp-b33-recovery-do-not-use-5`. Remove only when an authorized branch/ref deletion path is available.

## Validation state

- **Code written**: Yes — exact b33 product/config source `0ba15ec...`.
- **Static/source audit**: Passed for exact 3-file b33 product delta.
- **CI**: Exact b33 push passed; exact product merge-view passed; durable-docs head PR CI passed.
- **Artifact produced**: Yes — exact Runtime Artifact `9695669835`, identity independently verified.
- **Runtime/manual/real-device**: b32 partial/failing; b33 **Pending**.
- **Stable/Frozen**: **No**.

## b33 real-device focus

1. At physical bottom, including rubber-band overscroll, adaptive control must stay/resolve to **上一轮** when a previous round exists; it must not flip to 下一轮 merely from overscroll delta.
2. Long previous/next jumps should use one smooth native animation without the prior serious end-of-animation hitch.
3. Landing must remain precise at the intended user-message round start; rapid repeated taps still advance one semantic round per tap.
4. If a correction occurs, diagnostics should show `nativeLandingErrorPoints` and `landingCorrectionApplied=true`; normal accurate native landings should often avoid correction.
5. Regression sanity: tool/internal rows remain filtered, Copy remains accepted compact visual/function, first-entry latest/bottom, A/B anchors, timestamps/preferences, list reconcile, Sync/Reload remain intact.
