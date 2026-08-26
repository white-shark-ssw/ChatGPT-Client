# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-27._

## Purpose

This is the durable implementation sequence for the iOS-native ChatGPT client. Current source, CI/artifact evidence, real-device evidence and specialized plans under `docs/project/` take priority over stale historical wording.

Current constraints: native UIKit iOS client; TrollStore IPA; intended primary runtime iPhone/iOS17; deployment target iOS14; current ChatGPT private/internal behavior must be evidenced rather than guessed.

## Delivery principles

1. Fast usable loop before breadth.
2. Diagnosability before complexity.
3. Authentication/session ownership before protocol assumptions.
4. One authoritative owner per identity/state domain.
5. Native model/state separate from mounted UI.
6. Official ChatGPT iOS interaction is the default visual/interaction baseline unless explicit requirements or runtime pain points justify deviation.
7. Core owner work is serial; edge work parallelizes only after conflict scanning.
8. Always distinguish Code, static checks, CI, Artifact, Runtime and Stable/Frozen evidence.
9. Do not add speculative retry, fallback, watchdog, duplicate state or compatibility machinery.

## Usability milestones

- **V0.1 read-use**: native shell + conversation list/detail/message rendering + manual sync/full reload + usable cold-start login-state recovery.
- **V0.2 chat-use**: V0.1 + stable multi-conversation state ownership + text send/new conversation + streaming + stop + user-visible reasoning interaction/haptics + recovery integration.
- **V0.3 daily-use refinement**: preferences/metadata, Markdown export, long-conversation tuning, attachments and remaining daily-use conversation features.

## Completed foundations

### Phase 1 — `DEV-app-foundation`

Completed / merged / Stable. b1 reached Code + CI + Artifact + real-device acceptance.

### Phase 2 — `DEV-auth-bootstrap`

Completed / merged / Stable for tested scope. b6 established embedded visible login, default persistent `WKWebsiteDataStore` as sole persistent auth-secret authority, transient native authorized transport and ordered Plus/personal account context.

### Phase 3 — `DEV-protocol-read`

Completed / merged / Stable for accepted diagnostic read scope. b7 established current list/detail protocol evidence without making the diagnostic probe a production state owner.

### Phase 4 — `DEV-native-read-path`

Completed / merged / Stable for tested b9 scope. `ConversationRepository` owns production conversation summaries/selected detail/current visible branch; sidebar/detail controllers are presentation consumers. b9 accepted shell/list/two distinct details/current-branch visible messages on iPhone/iOS17.

## Phase 5 — `DEV-conversation-recovery`

### User-facing scope

**会话同步与重载 + 冷启动登录状态恢复**

### Current status

**Active b14 real-device candidate.**

- b10: accepted core `同步最新消息` / clear-then-fetch `重载当前会话` runtime.
- b11: request paths worked, but `navigationItem.prompt` feedback was invisible and rejected.
- b12: centered sync feedback + public WebKit warm-up accepted; first list load remained gated by lazy compact sidebar reveal.
- b13: real-device partial/failing. Initial list loading now starts immediately after warm-up and stale generation rejection works, but compact startup stayed on `新对话`, duplicate sidebar icons appeared, sidebar reveal was unreliable, and overlapping manual replacement detail requests produced HTTP429.
- b14: **Code + static/source review + CI + Artifact**. Run `33000566633`; artifact `9618410313`; IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`. Runtime pending.

### Manual recovery contract

- `同步最新消息` uses the authoritative selected conversation identity and existing detail path. It never resends/regenerates.
- Success reconciles server-backed detail; failure preserves previously loaded detail when one exists.
- `重载当前会话` clears authoritative selected detail first, then performs one fresh detail request and rebuilds from returned server state.
- Terminal `重新加载` uses the full-reload path.
- During an **ordinary initial detail load**, overflow `同步最新消息` and `重载当前会话` remain available so the user can explicitly recover from a stuck load.
- Current generation guard rejects older selected-detail completions as `operation_superseded` once a newer operation owns the selected detail.
- Duplicate manual recovery taps are disabled while the manual action itself is active.
- No automatic retry/watchdog/fallback/resend chain.

### Recovery overlap evidence still pending correction

b13 showed a separate failure mode while exercising recovery during load:

- ordinary detail generation 1 remained in flight and later succeeded;
- manual reload generations 2 and 3 were started as additional requests and each received HTTP429 in about 1.1 s;
- generation 1's later success was correctly discarded as stale.

Therefore the freshness guard is valid, but the request lifecycle still needs a minimum correction so explicit replacement recovery does not intentionally leave the older selected-detail network task active. **b14 does not implement that correction.** Once b14 shell behavior is accepted, use a fresh candidate identity for any cancellation/replacement change after the normal conflict/build-number check.

### Sync feedback

- Center-screen native toast, not navigation-bar prompt.
- While syncing: `正在同步最新消息…`.
- Success unchanged: `已是最新`.
- Success changed: `已同步最新消息`.
- Success result remains visible for 2 seconds; this timer is presentation-only.
- Failure removes toast and uses explicit failure UI.
- b12 real-device testing accepted this presentation.

### Cold-start auth/list evidence

Cold-start login-state recovery belongs to this same Work; do not create a separate auth-resume task.

Accepted evidence:

1. b12 public `WKWebsiteDataStore.default()` warm-up restored cookie visibility 0/0 -> 41/22 in `194.97 ms`; unchanged normal account/list verification later succeeded without visible Login.
2. b13 repeated the warm-up successfully 0/0 -> 39/20 in `177.47 ms` and started `listLoad` immediately afterwards.
3. b13's tested account probe took `17089.96 ms`, whole list load `22005.52 ms`, list HTTP200 28/29. This is an end-to-end latency signal; do not guess which subcomponent is the bottleneck.
4. User's much longer wait to reach the list was a compact shell/navigation presentation defect, not delayed list initiation.

### b14 compact startup/navigation correction

b14 isolates that presentation defect:

1. `AppDelegate` completes the accepted public WebKit warm-up before installing the product `RootViewController`.
2. `RootViewController` constructs primary/sidebar and secondary/detail columns synchronously before first product presentation.
3. With no selected conversation, the split delegate chooses `.primary` as the compact top column; current read-only startup should therefore land on the conversation list, even if rows are still loading.
4. Remove the b13 custom `sidebar.left` button and custom `show(.primary)` action. Native UISplitViewController/navigation is the single compact navigation owner.
5. Selecting a conversation still presents secondary; native Back/system split navigation should return to the list.
6. Auth endpoints/parser/headers, list/detail routes, sync toast and generation guard are unchanged.

### b14 acceptance gate

Exact b14 on iPhone/iOS17 must prove:

- force-quit -> launch: after the short warm-up, first product screen is the conversation list, not blank `新对话` detail;
- no duplicate pair of top-left sidebar icons;
- list loading starts automatically after warm-up, without requiring a sidebar tap;
- select conversation -> detail -> native Back/system split navigation reliably returns to list;
- centered sync feedback and ordinary full reload remain intact.

Do not use b14 to claim the b13 selected-detail overlap/HTTP429 issue is solved.

## Phase 6 — `DEV-multi-conversation-state`

### Goal

Establish stable multi-conversation session/runtime ownership before send/stream work. See `docs/project/MULTI_CONVERSATION_STATE_PLAN.md`.

### Scheduling

Starts **after recovery is merged/accepted**. This precedes round-count/preferences and send/stream because those features depend on clear multi-conversation identity/runtime ownership. Current single-selected generation logic is deliberately minimal and will later be generalized into account-scoped per-conversation freshness.

## Phase 7 — `DEV-conversation-round-count`

### User-facing scope

**会话轮数显示 / preferences integration**

- Display `聊天 · N轮` / `工作 · N轮` when enabled.
- One user message on current active branch equals one round; assistant/tool/system/reasoning nodes do not add rounds.
- Derive from authoritative active-branch state, never a second persistent mutable counter.
- `显示会话轮数` defaults On and persists through the existing preference owner once verified.
- No extra network request.

Scheduling: after `DEV-multi-conversation-state`, before send/stream, unless a later explicit conflict/dependency review changes the order.

## Phase 8 — `DEV-send-stream`

### Goal

Reach the first daily-chat candidate after read/recovery/multi-conversation ownership is stable.

Scope includes:

- evidence current text send/new-conversation protocol before production assumptions;
- composer send path, streaming lifecycle and stop/cancel behavior;
- stream identity bound to correct conversation/message under rapid switching;
- user-visible reasoning status/detail only when service explicitly supplies displayable material;
- official-style reasoning-to-final haptic transition tuned on real device;
- manual `同步最新消息` as recovery, never automatic prompt resend.

See `CLIENT_ARCHITECTURE_GAP_REVIEW.md`, `MULTI_CONVERSATION_STATE_PLAN.md` and `UI_INTERACTION_BASELINE.md`.

## Phase 9 — `DEV-markdown-export`

Export current authoritative user-visible branch to Markdown; do not scrape mounted cells or expose hidden/internal reasoning/tool content.

## Phase 10 — `DEV-long-conversation`

Measure/improve parse/model/render timing, first-visible latency, mounted-view bounds, memory growth, scrolling/input latency and lifecycle behavior. Existing multi-megabyte / thousands-of-node details remain real design inputs.

## Phase 11 — `DEV-attachments`

Add native photo/file/video attachment flows after text-chat ownership is stable. Evidence current upload protocol before production implementation.

## Phase 12 — remaining daily-use features

Split into isolated Work IDs as dependencies stabilize: search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement and other evidenced daily-use capabilities.

## Phase 13 — advanced capabilities

Later candidates: Projects, web search, image/multimodal, Voice, Memory, Deep Research, GPTs and other current ChatGPT-specific capabilities. These do not block early daily use.

## Current next action

Real-device test exact `DEV-conversation-recovery-0.1.0-b14` for compact startup/list-detail navigation. If accepted, record Runtime evidence, then allocate a fresh candidate for the minimum selected-detail replacement/cancellation correction unless the user explicitly scopes that b13 HTTP429 defect out. Recovery remains unmerged until its accepted scope is complete.