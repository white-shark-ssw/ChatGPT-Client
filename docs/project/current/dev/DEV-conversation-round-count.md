# DEV-conversation-round-count

## Status

**Active — exact b35 Runtime partial/failing; exact b36 Code/Static/CI/Artifact/current-main merge-view complete; Runtime Pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Phase 8 conversation metadata/settings bundle with compact header, round count, timestamps, Copy, adaptive round navigation, persisted Preferences, first-entry latest placement and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable, not merged.
- **Exact b36 product/config source**: `8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- **Current main at b36 validation**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Only this development checkpoint is Active. Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for recorded scopes, not Frozen.

## Accepted scope that must remain unchanged

- Physical-bottom/rubber-band adaptive direction.
- Each visible authoritative user message starts one round and is the physical quick-navigation target.
- Sequential derived-round targeting through one `ConversationRoundProjection` plus transient presentation cursor only.
- Recipient/tool/internal filtering, compact assistant Copy, timestamps/preferences/header, first-entry latest, A/B anchors, list/cache reconciliation, Sync/Reload and existing state owners.
- `ConversationRepository` remains sole conversation/list authority.

## Candidate progression

- b24 identity rejected/reserved; b25-b30 Runtime partial/failing.
- b31 accepted precise user-message semantic landing but rejected residual hitch/internal rows/Copy visual.
- b32 accepted recipient filtering, compact Copy direction and semantic landing; rejected smoothness + bottom rubber-band direction.
- b33 accepted physical-bottom direction and final precision; rejected long-distance/rapid smoothness.
- b34 removed stale completion correction; exact Runtime still rejected movement feel with 42 requested / 42 completed and 0 corrections/ignored completions.
- b35 replaced full-distance animation with one unified direct target position + about 120pt / 0.22s ease-out for short and long jumps. Exact Runtime still exposed multi-second tap-to-position stalls around long-message regions.
- b36 removes explicit root/table forced layouts from the jump path, gives immediate positioning feedback on the existing quick-nav button, and adds direct-position timing diagnostics. Runtime pending.

## Exact b35 Runtime result

- Candidate `DEV-conversation-round-count-0.1.0-b35`, `0.1.0 (35)`; exact source `c3addf775483de17a0a0a9eb81d602fc18ebe611`.
- Push Run / Job `33203663621` / `98959137672`; Runtime Artifact `9698781544`; ZIP `sha256:903b2e51608af144097f2880d1bbb301de29d8b4a21477a74d16523e26bc473d`; IPA SHA `b1391d06f81bc8c57d124e16a22ef138dd8151e0bd8e338db601729c6f583b0f`.
- User-tested exact b35 on iPhone/iOS17; supplied diagnostics identify build 35, Candidate b35 and source `c3addf775483`.
- Completed jumps retained `landingErrorPoints=0.00` with `leadDistancePoints=120.00`, but some taps visibly stalled for several seconds near long-message regions.
- Trace contains 52 `answerJump.requested` / 36 `answerJump.completed`; suspicious request-to-next-interaction gaps include about 4s, 10s and 8s.
- Source logged `answerJump.requested` before synchronous main-thread `view.layoutIfNeeded() -> tableView.layoutIfNeeded() -> scrollToRow(false) -> tableView.layoutIfNeeded()`, while rows are self-sizing multiline UILabel cells. This exact Runtime + source evidence justified targeting synchronous jump preparation before adding any geometry cache.
- b35 is **Runtime partial/failing**, permanently reserved, not Stable/Frozen.

## Exact b36 product source / implementation

- **Candidate**: `DEV-conversation-round-count-0.1.0-b36`
- **Version / Build**: `0.1.0 (36)`
- **Exact product/config source**: `8f8614508eef5197f9fff4bb9d10c14354d5821e`
- Parent checkpoint source: `c6c21e0f1d032c28451f36506cd4c90936dba1cb`.
- Exact parent→product diff is only three files:
  - `.github/workflows/ios-foundation.yml`: 2 additions / 2 deletions, Candidate/Artifact b35→b36 only;
  - `ChatGPTClient.xcodeproj/project.pbxproj`: 4 additions / 4 deletions, Debug+Release build 35→36 and Candidate b35→b36 only;
  - `ChatGPTClient/Conversation/ConversationFeature.swift`: 25 additions / 6 deletions, round-jump presentation/timing only.
- Static source parse passed; formal Swift blob `1a710353cb1864c99dda62c66eb7398c82ed5e64` matches the audited b36 source.

Actual b36 behavior:

1. Keeps one unified direct-position + 120pt / 0.22s ease-out method for short and long jumps.
2. Removes the jump handler's explicit `view.layoutIfNeeded()` and pre/post `tableView.layoutIfNeeded()` calls; does not force whole-table self-sizing solely to prepare the jump.
3. Reuses the existing 44pt quick-navigation button for immediate feedback: image is temporarily replaced by `定位中`, accessibility becomes `正在定位`; only that button/layer is flushed, not the table/root hierarchy.
4. Performs one nonanimated `scrollToRow(..., .top, animated:false)`, captures the resulting exact offset, then keeps the same short direction-consistent ease-out finish.
5. Adds privacy-safe `answerJump.positioned` with `directPositionDurationMs`, `preparationDurationMs`, `targetVisible`, target row/role and presentation mode only.
6. Restores the normal arrow immediately after positioning preparation; completion still records final landing error.
7. No row-height cache, timer, retry, watchdog, alternate semantic index, new repository/state owner, network change or rendering change.

## Exact b36 CI / Artifact

- Exact push Run / Job: `33207505424` / `98972194770` — success.
- Run `head_sha` is exact product source `8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- Runtime Artifact `9700254733`; name `ChatGPTClient-DEV-conversation-round-count-0.1.0-b36`.
- Artifact ZIP digest `sha256:718e8500ea41bcc73b41f5bebd9a4850b93246368a87304be0b2c4751702e576`.
- IPA `ChatGPTClient-0.1.0-b36-dev-conversation-round-count.ipa`; SHA `cdf2c7278ec0a4f6f5125a711f78d7bbda8c606a32dda87f614d710f662bd867`.
- Independent package verification: `0.1.0 (36)`, Candidate b36, source `8f8614508eef`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.

## Current-main merge-view evidence

- Main remained `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- PR #27 remains open, mergeable and not merged.
- PR Run / Job `33207508869` / `98972206567` — success.
- GitHub synthetic merge `e7ff5b368faaea3debbe5d5547c0424996653fa0` explicitly merges exact b36 product source `8f861450...` into `main@a6e3b2...`.
- Merge-view is CI evidence only and does not replace exact Runtime Artifact `9700254733`.

## Temporary assembly evidence / authority boundary

- Because the connector exposes no direct patch write for the large Swift file, a tooling-only temporary branch was used to materialize audited source/pbx blobs before the clean product commit.
- First temporary Run `33207249003` failed deterministically because the temporary patch file lacked a final newline (`corrupt patch`); no product branch change occurred.
- Corrected temporary materialization produced the exact audited Swift/pbx blobs; formal b36 product commit was then created directly from the pre-b36 checkpoint tree with only the three intended product/config files.
- `tmp/b36-assembly-20260829` was reset to the pre-product checkpoint after blob harvest. Any `tmp/b36-assembly-20260829-check*` branches are non-authoritative tooling branches at the pre-product checkpoint and must never be selected as Work/Candidate branches.

## Rendering observation — out of Phase 8 scope

Raw Markdown and `filecite`-adjacent boxed glyphs remain future `DEV-message-rendering` / rich-content work. Do not mix them into b36.

## Batch recovery point

- **Batch A — b35 Runtime failure + b36 reservation**: complete at `c6c21e0f...`.
- **Batch B — atomic b36 product/config source + exact diff audit**: complete at `8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- **Batch C — exact push CI/Artifact/package verification/current-main merge-view**: complete with Run/Job/Artifact/merge identities above.
- **Batch D — durable docs sync + handoff**: in progress at this checkpoint update. Product source must not change during this batch.
- **Next exact action**: synchronize `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `BUILD_TEST_INDEX.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md` to b35 Runtime + b36 evidence, verify docs-only diff, then hand exact b36 IPA to the user.
- **Must not replay/touch**: b24-b36 identities, product/config source `8f861450...`, repository/list/cache/network ownership, accepted round/filter/Copy/bottom-direction behavior, rendering scope or another task checkpoint.

## Validation state

- **b35 Runtime/manual/real-device**: Partial/failing.
- **b36 Code written**: Yes.
- **b36 Static/source audit**: Passed.
- **b36 exact push CI**: Passed.
- **b36 identity-valid Runtime Artifact**: Produced and independently verified.
- **b36 current-main merge-view CI**: Passed.
- **b36 Runtime/manual/real-device**: Pending.
- **Stable/Frozen**: No.

## b36 Runtime focus

1. Repeat the b35 long-message regions and verify tap-to-visible positioning no longer stalls for several seconds, or is materially reduced.
2. If positioning is not immediate, the existing quick-nav button must visibly show `定位中` so an accepted tap is never ambiguous.
3. If any stall remains, export diagnostics. `answerJump.positioned.directPositionDurationMs` / `preparationDurationMs` now distinguishes remaining direct `scrollToRow(false)` cost from the short animator.
4. Final semantic landing remains at the intended user-message round start.
5. Rapid taps remain one semantic round per tap; real drag immediately retakes ownership.
6. Physical-bottom/rubber-band direction and filtering/Copy/first-entry latest/A-B anchors/timestamps/preferences/list reconcile/Sync/Reload remain intact.
7. If b36 Runtime proves `directPositionDurationMs` itself remains multi-second, record that evidence first and allocate b37 before any geometry strategy; never rebuild b36.
