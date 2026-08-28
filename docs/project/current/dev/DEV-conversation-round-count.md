# DEV-conversation-round-count

## Status

**Active — PR #27 open; b31 exact CI/Artifact identity-valid; Runtime/manual validation pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidenced list-refresh presentation corrections.
- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Current main verified before b31 finalization**: `main@55216bde139f1058517ad852d98669f1c5cb54f1`. The advance from prior `e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2` only added `docs/project/SEND_STREAM_PREFLIGHT.md` and changed one line in `docs/project/START_HERE.md`; no product/state-owner/Candidate overlap with this Work was found.
- **Exact b31 product/config source**: `9b0fae856380b44a5d0495f32618ea6da31a0e0d`. Later docs-only commits do not redefine the b31 Runtime Candidate source.
- **Active-work conflict guard**: no competing Active dev checkpoint/candidate was found; main's new send-stream planning docs are non-overlapping with this Work.
- **Stable predecessors**: merged b21 multi-conversation read-state and merged b23 conversation-list cache-core remain Stable for recorded scopes, not Frozen. `ConversationRepository` remains sole list/detail authority.

## Candidate history

- **b24**: Artifact identity rejected / permanently reserved; never reuse.
- **b25**: Runtime partial/failing. Copy function, historical time and preference persistence accepted; header/jump/refresh rejected; exposed `30/29` reconcile defect.
- **Rejected reused-b25 output**: source-fix output reused an already-produced b25 identity; permanently invalid for testing.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound (`30 -> 29`, repeated `29/29`), sequential targets and compact header.
- **b27**: Runtime partial/failing. 1063-message stress run retained sequential targets but jump still paused/hitched; right-top refresh inflated adjusted top inset; Copy visual rejected as too large.
- **b28**: Runtime partial/failing. 1577-message run showed large answer landing drift, direction flips without real drag, first entry at top, refresh blank band persisted.
- **b29**: Runtime partial/failing. List top blank-region fix accepted, but `estimatedRowHeight=0` catastrophically broke message self-sizing/body presentation.
- **b30**: Runtime partial/failing. Message body/self-sizing restored and severe jump hitch materially improved, but Copy visual remained too large and long-distance assistant-answer landing remained grossly inaccurate.
- **Rejected duplicate b30 output during b31 staging**: commit `50ec1c72b1638eebc2b485ed423f4d5d294ae4c9` changed only the settings label before b31 build identity was allocated. Push Run `33167629825`, Job `98836731029`, Artifact `9684234692`, ZIP digest `sha256:b001c5fdac2f9f8caf92a814314047ad88b798eeb38d53b451a8b4c59ac6720b`, IPA SHA `d6b2102079accd864cef9334a2f7760b39516ab07a7fb7cabe24e4ca7ff7516f`, embedded Candidate b30 and source `50ec1c72b163`. Because formal b30 had already produced/tested Artifact `9681236213`, this later b30-named output is **identity-invalid, permanently rejected, and must never be installed/tested**.
- **b31**: current exact Runtime Candidate. User-turn navigation, direct row identity targeting, 10pt Copy visual, and renamed setting are compiled and packaged; Runtime/manual validation is pending.

## Current semantic contract — round and jump target

- A visible authoritative **user** message starts one round and remains the source of header `N轮` counting.
- `ConversationRoundProjection` remains the only round derivation authority. The first following visible assistant message may remain derived metadata for that round, but it is no longer the physical quick-jump target in b31.
- Latest explicit user requirement on 2026-08-28: if user-message targeting makes accurate jumping simpler and more reliable, that behavior is acceptable and preferred over preserving assistant-start landing with unstable long-distance geometry.
- b31 derives navigation rows from `ConversationRoundProjection.rounds[].userMessageID` and scrolls directly to that user-message row with `UITableView.scrollToRow(..., .top, animated: true)`.
- The transient programmatic target row is presentation state only; it is not a second round/index authority. Rapid taps progress from that semantic row, while a real drag clears the programmatic cursor and reclaims direction/context ownership.
- On animation completion, correctness is re-anchored to the same target user row rather than retaining an earlier fixed absolute Y destination.
- Hidden tool/reasoning/system nodes do not create rounds.
- Accessibility wording is `上一轮` / `下一轮`; Settings wording is `显示轮次快速跳转`.
- No speculative height-cache subsystem, timer, debounce, retry, watchdog or parallel navigation state owner was added.

## Accepted evidence retained from earlier candidates

### Conversation-list top blank region

- Exact b29 fixed the previous persistent blank region above the first conversation during right-top refresh.
- Known list reconciliation remained bounded (`pageCount=28`, `totalCount=29`, `resultCount=29`).
- Keep the no-`navigationItem.prompt` list-refresh presentation; Repository request/reconcile behavior is not changed by b31.

### Message body / self-sizing

- Exact b30 restored ordinary user bubbles, assistant text, timestamps and response action rows after the b29 `estimatedRowHeight=0` regression.
- Keep `rowHeight = UITableView.automaticDimension` and `estimatedRowHeight = UITableView.automaticDimension`.

### Why b31 changes the physical jump target

- Exact b30 diagnostics contained 35 `answerJump.completed` events; only 10/35 completed within 0.5pt of the then-resolved target offset, while 25/35 exceeded 100pt and 21/35 exceeded 1000pt.
- Median absolute error was about 3271pt and maximum observed absolute error about 64252.66pt. Nearby/already-resolved targets could still land correctly, indicating the semantic cursor was not universally wrong.
- b30 computed/fixed a long-distance absolute offset from self-sizing geometry before travel. Row measurement changes during travel invalidated that numeric destination.
- b31 therefore uses the already-authoritative round-start user row as the physical target, matching the latest user requirement and removing the need to preserve unstable assistant-start geometry.

## Copy presentation contract

- Exact b30 real-device evidence showed the 14pt source symbol rendered visually much larger than the official reference.
- b31 uses **10pt regular `doc.on.doc`** for the visible assistant Copy glyph while retaining the existing **28×28pt invisible hit/layout slot**, clear background, dynamic subdued tint, system pasteboard and visible-text-only behavior.
- User messages retain native context-menu Copy.

## Exact b31 Candidate evidence

- **Candidate**: `DEV-conversation-round-count-0.1.0-b31`
- **Version / Build**: `0.1.0 (31)`
- **Product/config source**: `9b0fae856380b44a5d0495f32618ea6da31a0e0d`
- **Exact push CI**: Run `33169669050`, Job `98843431963`, success; Xcode 16.4; target `arm64-apple-ios14.0`.
- **Runtime Artifact**: `9685082018`; Artifact name `ChatGPTClient-DEV-conversation-round-count-0.1.0-b31`; ZIP digest `sha256:166d13cd8f298903e3620e3fbf286f50ca5d3d67caeac6f6528add31c3132bde`.
- **IPA**: `ChatGPTClient-0.1.0-b31-dev-conversation-round-count.ipa`; SHA-256 `bd3cb30630538c6e3bb9c3f8e9d4d8e1d426691e8c06c8291b530f41fc81f422`.
- **Independent package inspection**: embedded `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=31`, `DiagnosticsCandidate=DEV-conversation-round-count-0.1.0-b31`, `DiagnosticsSourceCommit=9b0fae856380`, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`; executable is Mach-O 64-bit arm64.

## PR merge-view evidence against current main

For b31 product source `9b0fae856380b44a5d0495f32618ea6da31a0e0d`:

- Pull-request Run `33169672792`, Job `98843444383` — success.
- GitHub checkout explicitly built merge view `64a906bc4bc8cdc4c0c67d52efe566eafc715201` with log: `Merge 9b0fae856380b44a5d0495f32618ea6da31a0e0d into 55216bde139f1058517ad852d98669f1c5cb54f1`.
- Merge-view Artifact `9685080936`; ZIP digest `sha256:66eeff33891f6e9505938337e584aced7ad23aad44aaba8d61cbd04bc354b275`.
- Merge-view IPA SHA-256 `2778e21cc519af82d0821ddbb7dc39b7c3d1ad55c1344eccd9a26ce5b5c35deb`; source marker `64a906bc4bc8`.
- The merge-view Artifact is **merge evidence only** and does not replace exact Runtime Artifact `9685082018`.

## Current contracts retained

- Message time uses authoritative `createTime`; missing time is omitted.
- `AppPreferences` remains the single persisted settings owner; all three defaults remain On.
- Ordinary-chat detail may present `聊天`; `工作` requires authoritative Work/Project evidence and must not be guessed.
- `ConversationRepository` remains sole list/detail authority; b26 total-count reconciliation stays unchanged.
- No valid saved reading anchor => first presentation should show latest/bottom without visibly scrolling through history.
- Right-top list refresh must not use `navigationItem.prompt` or mutate pull-refresh presentation; b29 Runtime accepts the tested top-blank correction.
- Copy uses only visible authoritative text; hidden reasoning/tool/system material is never copied.
- No new request path, retry, timer, watchdog, polling, fallback endpoint, second list owner or second conversation authority.

## Validation state

- **Code written**: **Yes — b31**.
- **Static/source audit**: **Passed for the b31 change scope**. The final product delta from `50ec1c72...` is limited to b31 build/workflow identity plus `ConversationFeature.swift` user-turn row targeting/10pt Copy; no Repository/network/reconcile path changed.
- **CI**: **Exact b31 push CI passed**; initial PR merge-view CI against current main also passed.
- **Artifact produced**: **Yes — exact identity-valid Runtime Artifact `9685082018`**; independent package identity inspection passed.
- **Runtime/manual/real-device**: **Pending for b31**. No device acceptance may be inferred from CI/Artifact success.
- **Stable/Frozen**: **No** for this Work.

## Next exact action

Install and test exact Runtime Artifact `9685082018` / `ChatGPTClient-0.1.0-b31-dev-conversation-round-count.ipa`. Confirm diagnostics show `0.1.0 (31)`, Candidate b31 and source `9b0fae856380`. In a long conversation, rapidly tap previous/next and verify each tap progresses exactly one adjacent round and lands with that round's **user message at the top/round start**; long-distance b30-style multi-thousand-point misses must not recur. Interrupt a programmatic jump with a real drag and verify user direction immediately becomes authoritative. Compare the assistant Copy glyph directly with the official reference while confirming its function/hit area remains usable. Recheck automatic message body sizing, first-entry latest/bottom, b29 accepted right-top refresh behavior, bounded list total, timestamps, preference persistence, A/B anchors, Sync/Reload and basic VoiceOver/Dynamic Type. Do not merge PR #27 or claim Stable before exact b31 Runtime acceptance.
