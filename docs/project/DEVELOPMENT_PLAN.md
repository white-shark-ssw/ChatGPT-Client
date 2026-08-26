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

**V0.1 read-use milestone**: official-style native shell + conversation list + conversation detail/message rendering + manual sync/reload. This is useful before send/stream exists and should be issued for real-device use as soon as accepted.

**V0.2 chat-use milestone**: V0.1 + text send/new conversation + streaming + stop + user-visible reasoning state/detail + reasoning-to-final haptics + manual recovery integration. This is the first daily-chat candidate and is the highest scheduling priority after V0.1.

**V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments, search/rename/archive/delete, edit/regenerate/branch behavior, settings/diagnostics refinement and other daily-use edges as their dependencies become stable.

These are product milestones, not promises that every item is already implemented or protocol-verified.

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

**Completed / merged / Stable for accepted scope.** `DEV-auth-bootstrap-0.1.0-b6` established embedded Google login, persistent default `WKWebsiteDataStore` auth, transient native session/accounts transport, ordered plus/personal account context and privacy-safe diagnostics on iPhone / iOS 17.0.

Durable boundary: WebKit remains the sole persistent auth-secret authority; copied cookies/bearer are transient; challenge sensitivity remains observed; no speculative automatic retry/fallback/UA spoof/Cloudflare bypass.

## Phase 3 — `DEV-protocol-read`

**Completed / merged / Stable for the tested read scope.** `DEV-protocol-read-0.1.0-b7`, version `0.1.0 (7)`, exact product source `44a137b973e29e2a313e9114fdacb7727dccefb9`, reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** on iPhone / iOS 17.0. PR #7 merged at `6208102eb3df79a1916b356cc95ff7916ff8f593`.

Accepted scope includes current Plus/personal conversation list + one-detail read. First tested detail was 13,152,411 bytes with mappingCount 2068 / messageNodeCount 2067 and mapped `current_node`. Send/streaming/attachments and non-personal workspace behavior remain Unverified.

## Phase 4 — `DEV-native-read-path`

### User-facing name

**官方 App UI 主框架与原生会话读取**

### Priority

**Next core task / V0.1 foundation.** Do not insert a separate visual-design implementation phase before it. The durable UI interaction baseline is `docs/project/UI_INTERACTION_BASELINE.md` and should be consumed directly by this task.

### Scope

- Establish explicit production owners for conversation repository, list pagination, selected-conversation identity, detail/message-tree state and active-branch resolution. `ProtocolReadProbe` must remain diagnostic-only.
- Build the minimal official-style native shell needed for actual read use: sidebar/conversation navigation, chat top bar, message area, loading/empty/error states and menu extension points.
- Implement current conversation list/detail models from b7 evidence while leaving unsupported semantics Unknown until required.
- Render current active branch with bounded/virtualized native views; do not materialize all views for the evidenced 13.15 MB / 2068-node conversation.
- Support user/assistant visible Markdown text and the minimum evidence-backed content types needed by tested conversations. Unsupported node types must fail visibly/diagnosably rather than silently becoming authoritative assumptions.
- Preserve exact selected-conversation identity during rapid A/B switching.
- Add phase timings only where they locate actual transport/parse/model/render bottlenecks; do not infer the b7 13.57 s end-to-end probe bottleneck.

### First usable candidate gate — V0.1 read

As soon as the native list/detail path is coherent and real-device testable, produce a unique candidate rather than waiting for send/stream or later daily-use features.

## Phase 5 — `DEV-conversation-recovery`

### User-facing name

**会话同步与重载**

### Goal

Provide explicit manual recovery for two observed real-world failure classes without creating automatic retry loops.

### `同步最新消息`

Use the current conversation identity to fetch current server conversation detail and reconcile the authoritative local conversation state so that server-completed content can replace stale local thinking/streaming state.

Intended case: server reasoning/answer has already completed (including cases where a completion notification has arrived) while the client still shows thinking or an incomplete stream.

It must not resend the user's prompt, regenerate an answer, create a new conversation or automatically loop retries.

### `重载当前会话`

Manually request the current conversation again and rebuild that conversation's local authoritative state when initial/current loading timed out, failed, remained blank/spinning or became unusable.

- Preserve unsent composer draft when practical.
- Do not resend messages.
- Present a direct `重新加载` action in the conversation load-error state, with a manual menu entry also available for a visibly stale/broken loaded conversation.

### Diagnostics

Record safe start/end/status/timing/count/diff/state-transition evidence sufficient to distinguish server-stale vs local-merge vs UI-render failures. Do not log message bodies or auth secrets.

### V0.1 acceptance

V0.1 should include these recovery controls if the native read owner is stable enough to implement them without a second state authority. If the read task needs to ship a first candidate before this Work completes, issue the earlier read candidate and follow immediately with the recovery candidate rather than blocking all real-device use.

## Phase 6 — `DEV-send-stream`

### User-facing name

**消息发送、流式回复与推理交互**

### Goal

Reach the first daily-chat candidate as quickly as possible after the read/recovery ownership is stable.

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

## Phase 7 — `DEV-markdown-export`

### User-facing name

**Markdown 会话导出**

This is a product enhancement, not an official-App feature. The `导出 Markdown` item visible in the user's reference recording came from the user's injected dylib.

- Export from the authoritative conversation model, never from currently mounted UI cells.
- First version exports the current active/user-visible branch to `.md` with useful Markdown structure, code blocks and supported visible attachment references.
- Do not export hidden/internal reasoning/tool nodes that are not user-visible.
- Place the action naturally in the existing official-style conversation menu rather than inventing a separate navigation system.

This feature may run as a parallel edge after the production conversation model is stable if conflict scanning shows it does not overlap an Active core owner.

## Phase 8 — `DEV-long-conversation`

**超长会话性能优化**

Measure and stabilize bounded visible views, model/render separation, incremental updates, memory growth, input latency, scrolling, first-visible timing, parse/model/render timing and background/foreground behavior on real device. The accepted 13.15 MB / 2068-node conversation is a required real design/test input.

Do not delay the first usable candidates for every possible performance refinement; fix blockers and severe real-device regressions first, then optimize from measurement.

## Phase 9 — `DEV-attachments`

**附件上传与文件处理**

Add native photo/file/video attachment flows after text-chat ownership is stable. Upload state remains separate from send state; large video paths must avoid unnecessary full-memory loading. Current upload protocol must be evidenced before production assumptions.

## Phase 10 — Daily-use conversation features

Split into separate Work IDs when dependencies are stable:

- 会话搜索
- 会话重命名 / 归档 / 删除
- 消息编辑 / 重新生成 / 分支切换
- 模型选择与临时聊天
- 设置与诊断界面完善
- other small daily-use capabilities supported by current evidence

## Phase 11 — Advanced capabilities

Later roadmap candidates, each requiring current protocol/UI evidence before implementation:

- Projects
- 联网搜索
- 图片与多模态 / 图片生成
- 语音
- Memory
- Deep Research
- GPTs
- other current ChatGPT-specific capabilities

These must not block V0.1/V0.2 daily use.

# Official-App interaction baseline

See `docs/project/UI_INTERACTION_BASELINE.md`.

Core rule: where the official ChatGPT iOS interaction is acceptable, reproduce the interaction pattern rather than inventing a new product language. Our additions must fit into that interaction system. Explicit improvements currently include manual latest-message sync, manual current-conversation reload, Markdown export and diagnostics/support surfaces.

# Diagnostics / logging contract

Every important async path should show what started, which owner handled it, safe request/stream/upload mapping, timing, terminal result and safe error/status metadata. Never log passwords, OAuth codes, tokens, Cookie/Authorization values, full chat bodies or attachment contents.

# Parallel-development guidance

The dependency chain through production read ownership and send/stream remains strongly serialized. After the production conversation model/store contract is merged and stable, low-overlap edges such as Markdown export or settings/diagnostics refinement may run in parallel only after normal checkpoint/file/state-owner conflict scanning.

Do not parallelize two tasks that both own the same conversation store, stream lifecycle, shared UI controller/core, build candidate or unmerged dependency.

# Next implementation action

Create isolated `DEV-native-read-path` from the current merged main baseline. Consume `UI_INTERACTION_BASELINE.md` directly, establish production conversation state ownership and build the smallest official-style native list/detail experience that can produce the first real-device V0.1 read candidate.
