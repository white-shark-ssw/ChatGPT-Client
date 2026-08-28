# DEV-conversation-round-count

## Status

**Active — exact b35 Runtime partial/failing; b36 reserved for jump-preparation stall optimization + immediate positioning feedback**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Phase 8 conversation metadata/settings bundle with compact header, round count, timestamps, Copy, adaptive round navigation, persisted Preferences, first-entry latest placement and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Current branch head before b36 reservation write**: `adf6e85ecf7d57d59c8079b39e9435a29b4c66d5`.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Only this development checkpoint is Active on the branch. Stable predecessors b21 multi-conversation and b23 list-cache-core remain Stable for recorded scopes, not Frozen.

## Accepted scope that must remain unchanged

- Physical-bottom/rubber-band adaptive direction.
- Each visible authoritative user message starts one round and is the physical quick-navigation target.
- Sequential derived-round targeting through one `ConversationRoundProjection` plus transient presentation cursor only.
- Recipient/tool/internal filtering, compact assistant Copy, timestamps/preferences/header, first-entry latest, A/B anchors, list/cache reconciliation, Sync/Reload and all existing state owners.
- `ConversationRepository` remains sole conversation/list authority.

## Candidate history

- b24 identity rejected/reserved; b25-b30 Runtime partial/failing.
- b31 accepted precise user-message semantic landing but rejected residual hitch/internal rows/Copy visual.
- b32 accepted recipient filtering, compact Copy direction and semantic landing; rejected smoothness + bottom rubber-band direction.
- b33 accepted physical-bottom direction and final precision; rejected long-distance/rapid smoothness.
- b34 removed stale completion correction against a newer not-yet-visible target; Runtime still rejected movement feel even with 0 b34 landing corrections.
- b35 replaced full-distance animation with one unified direct-position + 120pt / 0.22s ease-out presentation for both short and long jumps.

## Exact b35 identity / CI / Artifact

- **Candidate**: `DEV-conversation-round-count-0.1.0-b35`
- **Version / Build**: `0.1.0 (35)`
- **Exact product/config source**: `c3addf775483de17a0a0a9eb81d602fc18ebe611`
- Exact push Run / Job `33203663621` / `98959137672` — success.
- Runtime Artifact `9698781544`; Artifact name `ChatGPTClient-DEV-conversation-round-count-0.1.0-b35`.
- Artifact ZIP digest `sha256:903b2e51608af144097f2880d1bbb301de29d8b4a21477a74d16523e26bc473d`.
- IPA `ChatGPTClient-0.1.0-b35-dev-conversation-round-count.ipa`; SHA `b1391d06f81bc8c57d124e16a22ef138dd8151e0bd8e338db601729c6f583b0f`.
- Independent package verification: `0.1.0 (35)`, Candidate b35, source `c3addf775483`, MinimumOSVersion 14.0, arm64.
- Current-main PR merge-view against unchanged `main@a6e3b2bc...` passed; synthetic merge `151a1022719542e4971896e591e887cee76c9dd8` merges docs head `adf6e85e...` into main. Merge-view output is CI evidence only.

## Exact b35 Runtime result

User-tested exact b35 on iPhone/iOS17 and supplied `ChatGPTClient-Diagnostics-20260828-193118.json`; metadata identifies build 35, Candidate b35 and source `c3addf775483`.

Runtime result:

1. Unified direct+ease-out presentation is running and completed jumps that do finish report `landingErrorPoints=0.00` with `leadDistancePoints=120.00`.
2. Blocking defect remains: some taps appear to freeze for several seconds, especially around long-message regions; the user also reports delayed execution and requests immediate visible feedback so a long wait never looks like a missed tap.
3. The b35 trace contains 52 `answerJump.requested` and 36 `answerJump.completed` events. Three especially suspicious request-to-next-jump gaps are visible at target rows 49 (~4s), 43 (~10s) and 40 (~8s), with no completion for those requested targets before the next interaction.
4. Source logs `answerJump.requested` **before** synchronous main-thread `view.layoutIfNeeded() -> tableView.layoutIfNeeded() -> scrollToRow(animated:false) -> tableView.layoutIfNeeded()`. `ConversationMessageCell` is self-sizing Auto Layout with unbounded multiline `UILabel`. Therefore exact Runtime + source evidence supports the synchronous jump-preparation/layout path as the current optimization target. This is evidence for the tested client path, not a blanket UIKit claim.
5. The short `UIViewPropertyAnimator` itself is not yet implicated by these long stalls because the request log precedes jump preparation and the missing completions occur before a stable final short-animation completion is observed.

Therefore exact b35 is **Runtime partial/failing**, permanently reserved and not Stable/Frozen.

## User-approved b36 interaction requirement

Latest explicit requirement:

- Keep one unified method for short and long jumps.
- Optimize away the several-second tap-to-motion delay where possible.
- When positioning is not immediate, give unmistakable immediate message feedback so the user knows the tap was accepted.

## b36 reserved identity / minimal evidence-backed direction

- **Reserved Candidate**: `DEV-conversation-round-count-0.1.0-b36`
- **Version / Build**: `0.1.0 (36)`
- Exact b36 code search returned no existing repository match before reservation; b24-b35 remain permanently reserved.

Smallest planned product/config delta:

1. Keep semantic round selection, `programmaticAnswerTargetRow`, physical-boundary direction and the 120pt / 0.22s ease-out finish.
2. Remove the jump handler's explicit pre/post `view.layoutIfNeeded()` / `tableView.layoutIfNeeded()` calls. Do not force whole-table synchronous self-sizing resolution solely to prepare a round jump.
3. Keep one nonanimated direct target positioning operation, then the same short direction-consistent ease-out. Do not add full-distance animation, retry, watchdog or second semantic owner.
4. Add a dedicated lightweight jump-status presentation owned by `ConversationDetailViewController` (text `正在定位…`) when a tap is accepted; clear it when final short motion begins/completes or when real drag/detail reset cancels programmatic ownership. This is presentation feedback only, not task/network state.
5. Add privacy-safe phase timing diagnostics around direct positioning (for example `answerJump.positioned` with elapsed milliseconds and target visibility/row only) so b36 Runtime can distinguish remaining direct-position cost from the short animator. Never log message text/identity.
6. Do not introduce a row-height cache in b36 yet. Exact b35 proves synchronous preparation stalls, but first remove the explicit forced-layout work and measure the remaining `scrollToRow(false)` cost before adding a separate geometry cache.
7. No Markdown/rendering, list/cache/network, retry/timer/watchdog, compatibility shim or unrelated refactor.

## Rendering observation — out of Phase 8 scope

Raw Markdown and `filecite`-adjacent boxed glyphs remain future `DEV-message-rendering` / rich-content work. Do not mix them into b36.

## Batch recovery point

- **Batch A — b35 Runtime failure + b36 reservation/plan**: this checkpoint write.
- **Batch B pending**: atomic b36 product/config commit changing only workflow/Xcode identity plus smallest `ConversationFeature.swift` presentation/timing delta; audit exact diff before branch fast-forward.
- **Batch C pending**: exact b36 push CI, Runtime Artifact, independent package verification and current-main PR merge-view.
- **Batch D pending**: synchronize durable `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `BUILD_TEST_INDEX.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md` to b35 Runtime + b36 truth, then hand exact b36 IPA to user.
- **Must not replay/touch**: b24-b35 identities, inspection-only commits, repository/list/cache/network ownership, accepted round/filter/Copy/bottom-direction behavior, rendering scope or another task checkpoint.
- **Next exact action**: implement/audit the b36 jump-preparation delta only.

## Validation state

- **b35 Runtime/manual/real-device**: Partial/failing — several-second positioning stalls remain.
- **b36 Code written**: No.
- **b36 Static/source audit**: Pending.
- **b36 CI**: Pending.
- **b36 Artifact produced**: Pending.
- **b36 Runtime/manual/real-device**: Pending.
- **Stable/Frozen**: No.

## b36 Runtime focus

1. Tap-to-visible-motion/positioning latency around the exact long-message regions that stalled in b35.
2. `正在定位…` feedback must make every accepted tap obvious if positioning is not immediate.
3. `answerJump.positioned` duration must show whether direct positioning itself still blocks after forced layouts are removed.
4. Final semantic user-row landing remains precise.
5. Rapid taps remain one semantic round per tap and real drag immediately retakes ownership.
6. Physical-bottom/rubber-band direction and all accepted filtering/Copy/list/anchor/recovery regressions remain intact.
