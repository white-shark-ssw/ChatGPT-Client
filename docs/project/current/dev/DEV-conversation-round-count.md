# DEV-conversation-round-count

## Status

**Active — PR #27 open; b31 Runtime partial/failing; b32 correction direction evidenced**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Current branch head before b32 product work**: `384c88ac4fedd08ddf226f7c430230f8bd9ee90c`.
- **Current main**: `55216bde139f1058517ad852d98669f1c5cb54f1`; its send-stream preflight docs do not overlap this Work's current product correction.
- **Only Active development checkpoint**: this Work plus `current/dev/README.md`; no duplicate branch/candidate conflict found.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: Artifact identity rejected / permanently reserved; never reuse.
- **b25**: Runtime partial/failing. Copy function, historical time and preference persistence accepted; header/jump/refresh rejected; exposed `30/29` reconcile defect.
- **Rejected reused-b25 output**: source-fix output reused an already-produced b25 identity; permanently invalid for testing.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound (`30 -> 29`, repeated `29/29`), sequential targets and compact header.
- **b27**: Runtime partial/failing. 1063-message stress run retained sequential targets but jump paused/hitched; right-top refresh inflated adjusted top inset; Copy visual rejected as too large.
- **b28**: Runtime partial/failing. 1577-message run showed large answer landing drift, direction flips without real drag, first entry at top and refresh blank band.
- **b29**: Runtime partial/failing. Right-top list blank-region fix accepted; `estimatedRowHeight=0` catastrophically broke message self-sizing/body presentation.
- **b30**: Runtime partial/failing. Message body/self-sizing restored and severe hitch materially improved, but Copy remained too large and long-distance assistant-answer landing remained grossly inaccurate.
- **Rejected duplicate b30 staging output**: Run `33167629825`, Artifact `9684234692`; reused an already-produced b30 identity and is permanently invalid.
- **b31**: Runtime partial/failing. **Accepted: precise semantic round landing at user-message rows. Rejected: serious jump hitch during travel, raw tool-call/internal assistant nodes rendered as ordinary chat rows with Copy, Copy glyph shape still unlike official reference.** Superseded for correction by fresh b32.

## Exact b31 identity / CI / Artifact

- **Candidate**: `DEV-conversation-round-count-0.1.0-b31`
- **Version / Build**: `0.1.0 (31)`
- **Exact product/config source**: `9b0fae856380b44a5d0495f32618ea6da31a0e0d`
- **Exact push CI**: Run `33169669050`, Job `98843431963`, success; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9685082018`; ZIP `sha256:166d13cd8f298903e3620e3fbf286f50ca5d3d67caeac6f6528add31c3132bde`.
- **IPA**: `ChatGPTClient-0.1.0-b31-dev-conversation-round-count.ipa`; SHA-256 `bd3cb30630538c6e3bb9c3f8e9d4d8e1d426691e8c06c8291b530f41fc81f422`.
- **Independent package inspection**: embedded `0.1.0 (31)`, Candidate b31, source `9b0fae856380`, minimum iOS14, device families `[1,2]`, Mach-O arm64.
- **PR merge-view against current main**: Run `33169672792`, Job `98843444383`, success on `64a906bc4bc8cdc4c0c67d52efe566eafc715201`; checkout explicitly merged b31 source into `main@55216bde139f1058517ad852d98669f1c5cb54f1`. Merge-view Artifact is merge evidence only.

## b31 real-device evidence — 2026-08-28

### Exact identity confirmed

The user supplied `ChatGPTClient-Diagnostics-20260828-122548.json` from exact b31:

- `appVersion=0.1.0`
- `buildNumber=31`
- `candidate=DEV-conversation-round-count-0.1.0-b31`
- `sourceCommit=9b0fae856380`
- device class iPhone / iOS 17.0.

### Round landing accuracy — accepted

- User reports round jumping is now precise.
- The supplied diagnostics contain **32 `answerJump.requested` + 32 `answerJump.completed` events**.
- Every completion targets `targetRole=user` and records `landingErrorPoints=-0.00`; observed max absolute landing error is 0 in this sample.
- This accepts the b31 semantic/physical landing choice: navigation rows derive from `ConversationRoundProjection.rounds[].userMessageID` and native table row targeting.
- **Do not rewrite this accepted semantic landing algorithm in b32 merely to chase smoothness.**

### Jump smoothness — rejected

- User explicitly reports a comparatively serious hitch/stutter during jump travel despite accurate landing.
- Perfect landing diagnostics do not contradict a frame-time/rendering hitch; accuracy and smoothness are separate acceptance dimensions.
- Current b31 diagnostics for the tested conversation report approximately **14.25 MB Detail payload, `mappingCount=2105`, `visibleMessageCount=832`, and resident visible-text bytes about 460,926**.
- The supplied screenshot header reports only **23 rounds**, while the body visibly contains many raw GitHub connector/tool-call JSON rows. This makes over-projected intermediate assistant/tool rows a concrete high-cost presentation factor to remove before introducing any new scrolling subsystem.

### Raw tool/internal rows — rejected presentation

- The screenshot visibly shows raw connector invocations such as GitHub `fetch_file`/argument JSON rendered as ordinary assistant text, each receiving an assistant Copy action.
- Current source explains it: `parseCurrentBranch` accepts any `user`/`assistant` node, while `visibleText(from:)` blindly concatenates textual `content.text` / `content.parts`; it does not inspect assistant `recipient` routing before publishing the node.
- The conversation graph containing tool/internal nodes is expected protocol data. **Rendering raw tool invocation payloads as ordinary user-facing assistant messages is not the intended client presentation.**
- Current assistant Copy duplication is largely a consequence of this over-projection because every projected assistant row gets a Copy action.

### Copy visual — size close, glyph shape rejected

- User says the b31 Copy size is now broadly close, but the visible `doc.on.doc` shape remains too document-like/sharp compared with the official screenshot.
- Official reference shows a simpler, rounder overlapping-square Copy glyph.
- b32 should keep the current 10pt-class visual scale and 28×28pt invisible hit/layout slot, but use system `square.on.square` for the visible assistant quick action.

## b32 evidence-backed correction direction

### 1. Preserve accepted round-navigation semantics

- Keep `ConversationRoundProjection` as the sole round derivation authority.
- Keep b31 `rounds[].userMessageID` physical targets, transient requested-row cursor, real-drag direction ownership, native `scrollToRow(..., .top, animated:true)` and completion re-anchor.
- Do not add debounce, timer, watchdog, speculative row-height cache or another navigation state owner.

### 2. Suppress explicit tool-recipient assistant invocations from ordinary visible chat

Use the smallest semantic filter supported by current source/protocol shape:

- During current-branch projection, for an `assistant` message inspect top-level `message["recipient"]` when it is a string.
- Normalize whitespace.
- Preserve nil/empty recipient and `all` as potentially user-facing.
- If recipient is explicitly non-empty and not `all`, do **not** publish that node as an ordinary `ConversationMessage`; increment only a privacy-safe filtered count.
- Do not hard-code GitHub/tool names, inspect JSON text heuristically, or log recipient names/bodies.
- Add a count such as `filteredRecipientMessageCount` to `detail.response` diagnostics so exact Runtime can prove whether this filter addresses the observed over-projection.
- This is intentionally conservative. If Runtime still exposes raw tool rows, gather new protocol evidence rather than guessing additional fields.

### 3. Copy symbol

- Visible assistant quick-action glyph: switch `doc.on.doc` -> `square.on.square`.
- Retain 10pt regular configuration, dynamic `.secondaryLabel`, clear background, left alignment and existing 28×28pt hit/layout slot.
- User context-menu Copy is not the visual target and need not be changed for this correction.

### 4. Smoothness verification order

- First remove the evidenced internal/tool rows and re-measure the same long conversation.
- Expectation to test, not claim: substantially fewer visible self-sizing rows should reduce layout work during long native jumps.
- If hitch remains after the projection is corrected, collect new exact b32 diagnostics/runtime evidence before modifying the accepted b31 navigation implementation.

## Current contracts retained

- Visible authoritative user messages define round count.
- Historical time uses authoritative `createTime`; absent means omit.
- `AppPreferences` remains sole persisted settings owner; all three defaults On.
- Ordinary supported detail may show `聊天`; `工作` requires authoritative type evidence.
- `ConversationRepository` remains sole list/detail authority; b26 total-count reconcile and b29 list-refresh correction remain unchanged.
- No valid saved reading anchor => first presentation should show latest/bottom without visible history travel.
- Copy never includes hidden/internal/tool payloads that are not projected as user-visible chat.
- No new network route, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- **Code written**: b31 yes; b32 pending at this checkpoint.
- **Static/source audit**: b31 passed; b32 pending.
- **CI / Artifact**: b31 passed/produced; b32 pending.
- **Runtime/manual/real-device**: **b31 partial/failing** — landing accuracy accepted; jump smoothness, raw tool-row presentation and Copy glyph shape rejected.
- **Stable/Frozen**: **No** for this Work.

## Next exact action

Allocate fresh unique `DEV-conversation-round-count-0.1.0-b32` / `0.1.0 (32)` and implement only the three evidenced b32 deltas: conservative explicit non-`all` assistant-recipient filtering with privacy-safe filtered count diagnostics, `square.on.square` assistant Copy visual at the existing scale/hit slot, and build/workflow identity. Keep the accepted b31 jump algorithm unchanged. Run exact CI/Artifact identity verification and PR merge-view against current main, then real-device test the same long/tool-heavy conversation for filtered-row count, raw tool JSON disappearance, Copy appearance and jump smoothness. Do not merge PR #27 or claim Stable before exact b32 Runtime acceptance.
