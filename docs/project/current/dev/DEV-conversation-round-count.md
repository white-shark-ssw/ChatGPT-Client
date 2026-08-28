# DEV-conversation-round-count

## Status

**Active — PR #27 open; b29 Runtime partial/failing; b30 identity-valid CI/Artifact ready for Runtime**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮回答 / 下一轮回答 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive answer navigation, centralized persisted Preferences, first-entry latest placement, and evidenced list-refresh presentation corrections.
- **Baseline / branch / PR**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Exact b30 product/config source**: `a091327508d8393822784bb286245aff64c028a8`. Later docs-only commits do not redefine the Runtime Candidate source.
- **Active-work conflict guard**: only this Active dev checkpoint plus README exists; no competing Active Work/candidate conflict.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: Artifact identity rejected / permanently reserved; never reuse.
- **b25**: Runtime partial/failing. Copy function, historical time and preference persistence accepted; header/jump/refresh rejected; exposed `30/29` reconcile defect.
- **Rejected reused-b25 output**: source-fix output reused an already-produced b25 identity; permanently invalid for testing.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound (`30 -> 29`, repeated `29/29`), sequential answer targets and compact header.
- **b27**: Runtime partial/failing. 1063-message stress run retained sequential targets but jump still paused/hitched; right-top refresh inflated adjusted top inset ~97.67 -> 131.67; Copy visual rejected as too large.
- **b28**: Runtime partial/failing. 1577-message run showed large answer landing drift (~-1950/-7330/-11407pt), direction flips without real drag, first entry at top, refresh blank band persisted.
- **b29**: Runtime partial/failing. List top blank-region fix is accepted, but message self-sizing layout catastrophically regressed; current body/row presentation became deformed/invisible, making jump/first-entry visual validation unreliable. Superseded by b30.
- **b30 current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b30`, `0.1.0 (30)`, exact product/config source `a091327508d8393822784bb286245aff64c028a8`.

## b29 real-device evidence — 2026-08-28

### Accepted: conversation-list top blank region

- User explicitly reports the previous blank region above the first conversation is fixed on exact b29.
- Diagnostics retained normal top presentation around `adjustedInsetTop≈97.67` / `contentOffsetY≈-97.67` through right-top refresh.
- Known list reconciliation stayed bounded at authoritative total (`pageCount=28`, `totalCount=29`, `resultCount=29`).
- Therefore the b29 list-presentation correction — no ordinary refresh status through `navigationItem.prompt` — is retained in b30 and should only receive regression sanity.

### Rejected: message self-sizing layout

- Exact b29 screenshots show conversation rows badly deformed: visible text largely disappears, user bubbles collapse into thin bars, assistant rows leave large blank areas, while timestamps/Copy glyphs remain visible.
- Diagnostics prove this is not a network/parser absence: successful Detail responses still produced hundreds/thousands of visible messages (examples 367 and 1630 visible messages).
- The only b29 layout change directly relevant to this failure was `UITableView.automaticDimension` row sizing combined with `tableView.estimatedRowHeight = 0`.
- This b29 route is rejected. Disabling row-height estimation is not a valid long-conversation optimization for this UIKit table.
- Because the body layout is broken, b29 cannot honestly accept answer-jump accuracy/smoothness or first-entry latest presentation even if code paths execute.

### Copy official-size reference

- User supplied an official ChatGPT iOS screenshot and explicitly pointed to the assistant Copy quick-action glyph.
- Screenshot is 1290px wide for a 430pt @3x device presentation. Measured Copy glyph bounds are roughly 44×44px ≈ 14.7×14.7pt, with a subdued gray outline, transparent/no visible button background and response-row left alignment around the ordinary content margin.
- Current implementation is already evidence-aligned at the glyph level: 14pt regular `doc.on.doc`, dynamic `.secondaryLabel`, clear background, left aligned. Its invisible layout slot remains 28×28pt for interaction/layout.
- Do not shrink to an arbitrary 10/12pt only to compensate for b29's broken row layout. Final visual scale remains Runtime pending after normal message layout is restored.

## b30 product correction

- Restore normal UIKit self-sizing behavior by changing only `tableView.estimatedRowHeight` from `0` to `UITableView.automaticDimension` while retaining `rowHeight = UITableView.automaticDimension`.
- Do not change the b29 list-refresh fix, Repository/network/reconcile, Preferences, answer semantic projection/cursor, first-entry latest logic, or Copy glyph configuration in this correction.
- No timer, debounce, retry, watchdog, fallback, height cache or secondary state owner is introduced.

### Scoped source audit

Formal b30 Candidate commit relative to the preceding docs head changes exactly three files:

1. `ChatGPTClient/Conversation/ConversationFeature.swift` — one-line self-sizing estimate restoration.
2. `ChatGPTClient.xcodeproj/project.pbxproj` — Build/Candidate 29 -> 30.
3. `.github/workflows/ios-foundation.yml` — b30 Candidate/Artifact label.

`ConversationRepository`, list request/reconcile, auth, cache and Preferences owners are untouched.

## Exact b30 Candidate evidence

- **Candidate**: `DEV-conversation-round-count-0.1.0-b30`
- **Version / Build**: `0.1.0 (30)`
- **Product/config source**: `a091327508d8393822784bb286245aff64c028a8`
- **Exact push CI**: Run `33160005440`, Job `98811893174`, success; checkout exact b30 source; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9681236213`; Artifact ZIP digest `sha256:18de824c977fc825f041a6ae1e38974011f92888c6a7ba1eb38fb155f5ecd52f`.
- **IPA**: `ChatGPTClient-0.1.0-b30-dev-conversation-round-count.ipa`; SHA-256 `91f5ee21e904fbe66932e306b7184dc645f33006e5bb10c33f8b3e3b22639db9`.
- **Independent package inspection after download**: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=30`, `DiagnosticsCandidate=DEV-conversation-round-count-0.1.0-b30`, `DiagnosticsSourceCommit=a091327508d8`, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`; executable Mach-O arm64; local SHA matches CI sidecar/log.
- **Initial b30 PR merge-view CI**: Run `33160008270`, Job `98811903542`, success; checkout `fe7eb9f15bd06279338d96b5628f9873f813968d`, explicitly `Merge a091327508d8393822784bb286245aff64c028a8 into e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`.
- **Merge-view output**: Artifact `9681226498`; ZIP digest `sha256:03d1f259fb77b907ad4709516734751f67a2a81df24080317626abf22cd3ea4d`; merge-view IPA SHA `cb2eca27416e61f18cc0e432023ae43ce97fe0e27f32a7ae90c1a7fb9898efcf`. Merge-view output is merge evidence only and must not replace Runtime Artifact `9681236213`.

## Current contracts retained

- Round count and answer anchors share one derived `ConversationRoundProjection`; hidden tool/reasoning/system nodes do not create rounds.
- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; all three current defaults remain On.
- Current ordinary-chat detail may present `聊天`; `工作` requires authoritative Work/Project type evidence and must not be guessed.
- `ConversationRepository` remains sole list/detail authority; b26 accepted total-count reconciliation remains unchanged.
- No valid saved reading anchor => first presentation should show latest/bottom without visibly scrolling through history.
- Right-top list refresh must not use `navigationItem.prompt` or mutate pull-refresh presentation; b29 Runtime accepts the tested top-blank correction.
- Copy uses only visible authoritative text and stays a small official-style response action; hidden reasoning/tool/system material is never copied.
- No new request path, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- **Code written**: b30 yes at exact source `a091327508d8393822784bb286245aff64c028a8`.
- **Static/source audit**: Passed for the scoped b30 diff.
- **CI**: exact b30 push CI passed; initial b30 PR merge-view CI passed.
- **Artifact produced**: exact identity-valid Runtime Artifact `9681236213`; downloaded ZIP/IPA identity and SHA independently verified.
- **Runtime/manual/real-device**: **Pending for b30**. b29 is recorded Runtime partial/failing; list top blank correction accepted, message layout rejected.
- **Stable/Frozen**: **No** for this Work.

## Next exact action

Install exact b30 Runtime Artifact `9681236213` / IPA SHA `91f5ee21e904fbe66932e306b7184dc645f33006e5bb10c33f8b3e3b22639db9` on the accepted iPhone/iOS17 scope. First verify that message bodies, user bubbles, assistant text, timestamps and row heights are visually normal again. Then verify the b29-accepted list top blank fix did not regress and compare the assistant Copy glyph against the supplied official screenshot. Only after normal body layout is confirmed should answer-jump accuracy/smoothness/direction and first-entry latest/bottom be judged again. Do not merge PR #27 or claim Stable before exact b30 passes Runtime.
