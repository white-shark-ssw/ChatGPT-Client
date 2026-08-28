# DEV-conversation-round-count

## Status

**Active — PR #27 open; b30 Runtime partial/failing; b31 correction in progress**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, centralized persisted Preferences, first-entry latest placement, and evidenced list-refresh presentation corrections.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Exact b30 product/config source**: `a091327508d8393822784bb286245aff64c028a8`. Later docs-only commits do not redefine the b30 Runtime Candidate source.
- **Current branch head before b31 product allocation**: docs may advance beyond b30 source; exact product identity remains tied to the Candidate source recorded above.
- **Active-work conflict guard**: only this Active dev checkpoint plus README exists; no competing Active Work/candidate conflict.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: Artifact identity rejected / permanently reserved; never reuse.
- **b25**: Runtime partial/failing. Copy function, historical time and preference persistence accepted; header/jump/refresh rejected; exposed `30/29` reconcile defect.
- **Rejected reused-b25 output**: source-fix output reused an already-produced b25 identity; permanently invalid for testing.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound (`30 -> 29`, repeated `29/29`), sequential answer targets and compact header.
- **b27**: Runtime partial/failing. 1063-message stress run retained sequential targets but jump still paused/hitched; right-top refresh inflated adjusted top inset ~97.67 -> 131.67; Copy visual rejected as too large.
- **b28**: Runtime partial/failing. 1577-message run showed large answer landing drift (~-1950/-7330/-11407pt), direction flips without real drag, first entry at top, refresh blank band persisted.
- **b29**: Runtime partial/failing. List top blank-region fix accepted, but `estimatedRowHeight=0` catastrophically broke message self-sizing/body presentation.
- **b30**: Runtime partial/failing. Message body/self-sizing is restored and the former severe jump hitch is materially reduced, but Copy visual remains too large and long-distance answer landing remains grossly inaccurate. Superseded for correction by b31.

## Accepted semantic contract — round vs jump target

- A visible authoritative **user** message starts one round.
- The **first following visible assistant message before the next user message** is that round's answer anchor.
- Therefore header `N轮` is user-turn-derived, while `上一轮回答 / 下一轮回答` must land at the corresponding **assistant answer start**, not the user bubble.
- `ConversationRoundProjection` already implements exactly this contract; b30 Runtime does not justify changing semantic ownership or introducing a second index.

## b29 accepted Runtime evidence retained

### Conversation-list top blank region

- Exact b29 fixed the previous persistent blank region above the first conversation during right-top refresh.
- Normal adjusted top inset remained around `97.67`; known list reconciliation stayed bounded (`pageCount=28`, `totalCount=29`, `resultCount=29`).
- Keep the no-`navigationItem.prompt` list-refresh presentation in b31; Repository request/reconcile behavior is not in scope.

## b30 real-device evidence — 2026-08-28

### Exact identity confirmed

The user supplied a diagnostics export whose metadata records:

- `appVersion=0.1.0`
- `buildNumber=30`
- `candidate=DEV-conversation-round-count-0.1.0-b30`
- `sourceCommit=a091327508d8`
- `deviceClass=iPhone`
- `systemVersion=17.0`

This is exact b30 Runtime evidence, not a stale package.

### Message layout restored

- The supplied b30 screenshot shows ordinary user bubbles, assistant text, timestamps and response action rows visible again.
- This clears the b29 `estimatedRowHeight=0` body-layout regression for the supplied b30 screen.
- Keep `rowHeight = UITableView.automaticDimension` and `estimatedRowHeight = UITableView.automaticDimension`; do not return to `estimatedRowHeight=0`.

### Jump smoothness improved, accuracy failed

- User reports the previous obvious heavy hitch is no longer present; only slight residual hitch is perceived. Record this as an improvement, not full smoothness acceptance.
- Exact b30 diagnostics contain **35** `answerJump.completed` events.
- Only **10/35** complete within `0.5pt` of the then-resolved target offset.
- **25/35** exceed `100pt`; **21/35** exceed `1000pt`.
- Median absolute landing error is about **3271pt**; maximum observed absolute error is about **64252.66pt**.
- Concrete failures include target row 801 around `+27804.33pt`, row 716 around `+64249.66pt`, row 360 around `+63542.66pt`, row 206 around `+62010.33pt` and row 105 around `+29559.67pt`.
- Nearby/already-resolved targets can still land at `-0.00pt`, proving the semantic target cursor itself is not universally wrong. The failure scales with unresolved self-sizing geometry over long distances.
- Current b30 path computes an absolute `targetOffsetY` from `rectForRow`, then fixes that numeric offset into `setContentOffset(..., animated:true)`. As rows are measured during travel, the destination row's real Y changes while the animation target does not. Recomputing another numeric rect at animation end is insufficient when the intended target row is still not the actually materialized row.
- b31 must retain assistant answer semantics and the transient semantic cursor, but use UITableView's row-targeting semantics for the final/authoritative landing rather than treating an estimated absolute Y as authoritative.

### Copy visual still rejected

- User explicitly reports the b30 Copy icon remains much larger/different from the official ChatGPT iOS reference.
- Direct measurement of the supplied native 1290×2796 b30 screenshot gives a visible Copy glyph bounding box of roughly **54×66px ≈ 18×22pt** even though source config says `pointSize: 14`.
- Therefore the earlier assumption that the source `14pt` value itself matched the official visual size is superseded by real-device evidence.
- Prior official reference was roughly ~44px maximum visible scale on the same 1290px-wide class of screenshot. Scaling the current rendered glyph by that evidence points near a 9–10pt symbol configuration.
- b31 direction: use **10pt regular `doc.on.doc`**, retain clear background, dynamic subdued tint and the invisible hit/layout slot unless new evidence requires changing hit geometry. Do not shrink the tap target together with the visual glyph.

## b31 evidence-backed correction direction

### Answer landing

- Keep `ConversationRoundProjection`, `answerRows`, `programmaticAnswerTargetRow`, direction ownership and rapid-tap semantic progression unchanged.
- Keep normal automatic row estimation; b29 proved disabling it breaks message presentation.
- Stop treating an off-screen estimated `rectForRow` absolute Y as the authoritative final destination.
- Use UITableView row targeting for the requested assistant row so self-sizing layout can resolve against the row identity rather than a stale absolute coordinate. Preserve interruptibility by stopping an in-flight programmatic animation before a new semantic target is requested.
- At animation completion, verify the target row's real placement; if correction is required, correct by **row identity** (`scrollToRow(..., .top, animated:false)`) and only then compute/log residual placement error. This is not a second semantic authority; it is the same target row enforced through UITableView's own row API.
- Do not add debounce, timer, retry, watchdog, fallback endpoint, speculative full height cache or duplicate answer index.

### Copy

- Shrink only the rendered assistant Copy glyph to `10pt regular` based on exact b30 screenshot measurement.
- Preserve visible-text Copy behavior, system pasteboard, no network request, clear background and dynamic tint.

## Exact b30 Candidate evidence

- **Candidate**: `DEV-conversation-round-count-0.1.0-b30`
- **Version / Build**: `0.1.0 (30)`
- **Product/config source**: `a091327508d8393822784bb286245aff64c028a8`
- **Exact push CI**: Run `33160005440`, Job `98811893174`, success; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9681236213`; ZIP digest `sha256:18de824c977fc825f041a6ae1e38974011f92888c6a7ba1eb38fb155f5ecd52f`.
- **IPA**: `ChatGPTClient-0.1.0-b30-dev-conversation-round-count.ipa`; SHA-256 `91f5ee21e904fbe66932e306b7184dc645f33006e5bb10c33f8b3e3b22639db9`.
- **Independent package inspection**: embedded `0.1.0 (30)`, Candidate b30, source marker `a091327508d8`, minimum iOS14, device families `[1,2]`; executable Mach-O arm64.
- **Initial b30 PR merge-view CI**: Run `33160008270`, Job `98811903542`, success on merge `fe7eb9f15bd06279338d96b5628f9873f813968d` into unchanged main.

## Current contracts retained

- Round count and answer anchors share one derived `ConversationRoundProjection`; hidden tool/reasoning/system nodes do not create rounds.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; all three defaults remain On.
- Ordinary-chat detail may present `聊天`; `工作` requires authoritative Work/Project evidence and must not be guessed.
- `ConversationRepository` remains sole list/detail authority; b26 total-count reconciliation stays unchanged.
- No valid saved reading anchor => first presentation should show latest/bottom without visibly scrolling through history.
- Right-top list refresh must not use `navigationItem.prompt` or mutate pull-refresh presentation; b29 Runtime accepts the tested top-blank correction.
- Copy uses only visible authoritative text; hidden reasoning/tool/system material is never copied.
- No new request path, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- **Code written**: b30 yes; b31 not yet at this checkpoint update.
- **Static/source audit**: b30 passed; b31 pending.
- **CI**: b30 exact push and initial merge-view passed; b31 pending.
- **Artifact produced**: b30 exact identity-valid Artifact `9681236213`; b31 none yet.
- **Runtime/manual/real-device**: **b30 partial/failing**. Message layout restored; severe hitch materially improved; Copy visual and long-distance answer landing rejected.
- **Stable/Frozen**: **No** for this Work.

## Next exact action

Implement the smallest b31 source correction: preserve user-defined round / assistant-defined answer semantics, replace stale absolute-offset authority with row-identity landing/verification, and reduce the rendered assistant Copy glyph to 10pt while preserving its hit slot. Allocate a fresh unique `DEV-conversation-round-count-0.1.0-b31` identity atomically with product/config source, run exact CI/Artifact identity verification and PR merge-view CI, then real-device test answer landing accuracy/smoothness plus Copy visual. Do not merge PR #27 or claim Stable before exact b31 Runtime acceptance.
