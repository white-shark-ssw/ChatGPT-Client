# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-26._

## Purpose

This is the durable implementation sequence for the iOS-native ChatGPT client. Status must be backed by current source/CI/artifact/runtime evidence.

Current constraints: native iOS client; TrollStore IPA; intended OS ceiling iOS 17.0; current deployment target iOS 14.0; historical WebView material reference-only; current private/internal behavior must be revalidated.

## Delivery goal — usable as early as possible

The product should become useful on the user's real device in small accepted increments instead of waiting for the entire roadmap to finish.

- Produce a uniquely identified TrollStore IPA whenever a meaningful minimal user loop becomes testable and the task has reached its artifact gate.
- Real-device use starts as soon as a coherent milestone is safe enough to test; later features are added while the client is already being used.
- Do not delay the core chat loop for advanced features, broad settings, visual reinvention or speculative compatibility work.
- Candidate success still requires exact source/build/artifact identity and must distinguish Code / CI / Artifact / Runtime evidence.

### Usability milestones

**V0.1 read-use milestone**: official-style native shell + conversation list + conversation detail/message rendering + manual sync/reload.

**V0.2 chat-use milestone**: V0.1 + text send/new conversation + streaming + stop + user-visible reasoning state/detail + reasoning-to-final haptics + manual recovery integration.

**V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments, search/rename/archive/delete, edit/regenerate/branch behavior, settings/diagnostics refinement and other daily-use edges.

Small low-risk UX enhancements may be inserted between core phases when their dependencies are already merged and they do not create state-owner or branch conflicts.

## Development principles

1. **Fast usable loop before breadth**.
2. **Diagnosability before complexity**.
3. **Authentication before private protocol assumptions**.
4. **Protocol evidence before authoritative data models**.
5. **One state owner per identity**.
6. **Native data model separate from visible views**.
7. **Official ChatGPT iOS interaction is the default UI baseline; improve only where there is an explicit requirement or evidenced pain point**.
8. **Serial core, parallel edges after shared owners/contracts stabilize**.
9. **Real-device evidence matters; CI/artifact is not runtime proof**.

## Phase 1 — `DEV-app-foundation`

**Completed / merged / Stable.** `DEV-app-foundation-0.1.0-b1` reached Code + CI + Artifact + real-device testing on iPhone / iOS 17.0.

## Phase 2 — `DEV-auth-bootstrap`

**Completed / merged / Stable for accepted scope.** `DEV-auth-bootstrap-0.1.0-b6` established embedded Google login, persistent default `WKWebsiteDataStore` auth architecture, transient native session/accounts transport, ordered Plus/personal account context and privacy-safe diagnostics on iPhone / iOS 17.0.

Install/update persistence of usable WebKit auth remains separately Unverified from later b9 evidence; do not add speculative recovery.

## Phase 3 — `DEV-protocol-read`

**Completed / merged / Stable for the tested read scope.** `DEV-protocol-read-0.1.0-b7` established the accepted Plus/personal diagnostic conversation list + one-detail read path on iPhone / iOS 17.0.

## Phase 4 — `DEV-native-read-path`

### User-facing name

**官方 App UI 主框架与原生会话读取**

### Status

**Completed / merged / Stable for tested b9 scope.** `DEV-native-read-path-0.1.0-b9`, source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`, reached Code + CI + Artifact + real-device acceptance and PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.

Accepted production ownership:

- `ConversationRepository` owns production conversation summaries, selected identity, loaded detail and current visible branch.
- `ConversationSidebarViewController` owns list presentation.
- `ConversationDetailViewController` owns current detail/message presentation.
- `ProtocolReadProbe` remains diagnostic-only.

Real-device b9 acceptance included two distinct selected conversations, including 7.50 MB / 2023 mapping nodes / 843 visible messages. Long-conversation performance decomposition remains later work.

## Phase 5 — `DEV-conversation-recovery`

### User-facing name

**会话同步与重载**

### Priority

**Next serialized core task.**

### `同步最新消息`

Use the current authoritative conversation identity to fetch current server detail and reconcile through `ConversationRepository` so server-completed content can replace stale local thinking/streaming state.

It must not resend the user's prompt, regenerate, create a new conversation or automatically loop retries.

### `重载当前会话`

Manually request the current conversation again and rebuild that conversation through the authoritative owner when loading timed out, failed, remained blank/spinning or became unusable.

- Preserve unsent composer draft when practical.
- Do not resend messages.
- Terminal load error provides direct `重新加载`; loaded-but-stale/broken state may expose `重载当前会话` in the overflow menu.

### Diagnostics

Record safe start/end/status/timing/count/diff/state-transition evidence sufficient to distinguish server-state, local merge/store and UI-render failures. Do not log message bodies or auth secrets.

## Phase 6 — `DEV-conversation-round-count`

### User-facing name

**会话轮数显示**

### Goal

Add a small optional conversation-round indicator to the existing title subtitle without changing the official-style layout or introducing a second conversation state authority.

### UI

The title's second line remains the conversation type and becomes a compact centered metadata row:

- `聊天 · 23轮`
- `工作 · 23轮`

The round count appears to the **right of the existing type label**. When the setting is disabled, the subtitle remains only `聊天` or `工作`.

Do not show a misleading `0轮` while detail has not loaded. Until the authoritative detail/branch is available, show only the type label; add the count when it is known.

### Round-count semantics

`轮数` is derived from the **current active branch**, not raw conversation `mapping` size.

- Each user message on the current active branch counts as one round.
- Assistant, tool, system, reasoning/status and other non-user nodes do not add rounds.
- Regenerating an assistant answer does not increase the round count by itself.
- Editing/switching branches recalculates from the newly active branch, so branch alternatives are not summed together.
- Once send/stream exists, a newly submitted user message counts when it becomes part of the authoritative local active branch; completion of the assistant stream is not required to invent a second counter.

This definition keeps the number useful as “how many user turns this active conversation path has had” and remains compatible with future Edit/Regenerate/branch navigation.

### State ownership / implementation constraint

- Derive the value from `ConversationRepository`'s current active visible branch / production conversation view state.
- Do **not** maintain a separately mutable persistent round counter.
- No new network request is required.
- When sync/reload/branch selection changes authoritative detail, the displayed count follows the same updated branch automatically.

The exact Swift property/type name is not frozen by planning; implementation must inspect current b9 source and use the existing model/state structure.

### Setting

Add an app setting:

**显示会话轮数**

- Default: **On**.
- Persist using the app's existing settings-preference mechanism after verifying its current owner.
- Turning it off hides only the `· N轮` portion; it does not affect type display or conversation data.

### Acceptance

- Two conversations with different known active-branch user-turn counts display different correct counts.
- Rapid A/B switching never leaves the previous conversation's count behind.
- Toggle Off/On updates presentation and persists across relaunch.
- Reloading an already loaded conversation does not duplicate/increment the count.
- Count remains derived from authoritative branch state and requires no extra server call.

### Scheduling

This is a small Work whose dependencies are already satisfied by merged b9. Keep it **serial with `DEV-conversation-recovery`** because both can touch `ConversationRepository` / conversation-detail UI. Planned order: recovery first, then round-count, then send/stream. If future conflict scanning proves the files/owners have diverged enough for safe parallel work, the normal parallel-development rules still apply.

## Phase 7 — `DEV-send-stream`

### User-facing name

**消息发送、流式回复与推理交互**

### Goal

Reach the first daily-chat candidate as quickly as possible after read/recovery ownership is stable.

### Scope

- Establish current evidence for text send/new-conversation protocol before production implementation.
- Composer send path, user-message state and evidence-backed stop/cancel behavior.
- Streaming parser/lifecycle and incremental assistant-message updates without broad list reload.
- Stream identity must remain owned by the correct conversation/message under rapid conversation switching.
- User-visible reasoning UI follows `UI_INTERACTION_BASELINE.md`: gray/shimmer thinking state when current protocol provides a user-visible reasoning status/detail; tap to expand/collapse user-visible reasoning detail; completed state such as `思考了 Xs` when duration is evidenced/available.
- Only render reasoning summary/detail/tool-status that the current service explicitly returns for user display. Never infer or expose hidden chain-of-thought.
- On the real-time transition from reasoning to final-answer presentation, reproduce the official-style **two short haptic feedback pulses**. Exact intensity/spacing must be tuned on real device rather than guessed from screen recording.
- Haptic ownership belongs to the response lifecycle transition, not cell redraw/reload. Reopening/reloading an already completed response must not replay the transition haptics.
- Integrate manual `同步最新消息` as the safe recovery action for an incomplete/stale stream; do not automatically resend the prompt.

### V0.2 daily-chat gate

Once read + send + stream + stop + basic reasoning presentation + manual recovery work on-device, issue a daily-use candidate immediately. Do not wait for attachments, Projects, search, Voice or the complete advanced roadmap.

## Phase 8 — `DEV-markdown-export`

### User-facing name

**Markdown 会话导出**

This is a product enhancement, not an official-App feature. The `导出 Markdown` item visible in the user's reference recording came from the user's injected dylib.

- Export from the authoritative conversation model, never from currently mounted UI cells.
- First version exports the current active/user-visible branch to `.md` with useful Markdown structure, code blocks and supported visible attachment references.
- Do not export hidden/internal reasoning/tool nodes that are not user-visible.
- Place the action naturally in the existing official-style conversation menu.

## Phase 9 — `DEV-long-conversation`

**超长会话性能优化**

Measure and stabilize bounded visible views, model/render separation, incremental updates, memory growth, input latency, scrolling, first-visible timing, parse/model/render timing and background/foreground behavior on real device. b9's 7.50 MB / 2023-node / 20.74 s production detail is a current real design input.

## Phase 10 — `DEV-attachments`

**附件上传与文件处理**

Add native photo/file/video attachment flows after text-chat ownership is stable. Upload state remains separate from send state; large video paths must avoid unnecessary full-memory loading. Current upload protocol must be evidenced before production assumptions.

## Phase 11 — Daily-use conversation features

Split into separate Work IDs when dependencies are stable:

- 会话搜索
- 会话重命名 / 归档 / 删除
- 消息编辑 / 重新生成 / 分支切换
- 模型选择与临时聊天
- 设置与诊断界面完善
- other small daily-use capabilities supported by current evidence

## Phase 12 — Advanced capabilities

Later roadmap candidates, each requiring current protocol/UI evidence before implementation:

- Projects
- 联网搜索
- 图片与多模态 / 图片生成
- 语音
- Memory
- Deep Research
- GPTs
- other current ChatGPT-specific capabilities

These must not block early daily use.

# Official-App interaction baseline

See `docs/project/UI_INTERACTION_BASELINE.md`.

# Diagnostics / logging contract

Every important async path should show what started, which owner handled it, safe request/stream/upload mapping, timing, terminal result and safe error/status metadata. Never log passwords, OAuth codes, tokens, Cookie/Authorization values, full chat bodies or attachment contents.

# Parallel-development guidance

Core state-owner work remains serialized. Small edge tasks may parallelize only after branch/checkpoint/file/state-owner conflict scanning proves that they do not share a core owner or unmerged dependency.

# Next implementation action

Create isolated `DEV-conversation-recovery` from the current merged b9 baseline. After recovery is merged, `DEV-conversation-round-count` is the next planned small UI/data-derived enhancement before `DEV-send-stream`.
