# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-27._

## Purpose

This is the durable implementation sequence for the iOS-native ChatGPT client. Current source, CI/artifact evidence, real-device evidence and the specialized plans under `docs/project/` take priority over stale historical phase wording.

Current constraints: native UIKit iOS client; TrollStore IPA; intended primary runtime iPhone/iOS 17.0; deployment target iOS 14.0; current ChatGPT private/internal behavior must be evidenced rather than guessed.

## Delivery principles

1. Fast usable loop before breadth.
2. Diagnosability before complexity.
3. Authentication/session ownership before protocol assumptions.
4. One authoritative owner per identity/state domain.
5. Native model/state separate from mounted UI.
6. Official ChatGPT iOS interaction is the default visual/interaction baseline unless an explicit requirement or runtime pain point justifies a deviation.
7. Core owner work is serial; edge work may parallelize only after conflict scanning.
8. Always distinguish Code written, static checks, CI, Artifact, Runtime and Stable/Frozen evidence.
9. Do not add speculative retry, fallback, watchdog, duplicate state or compatibility machinery.

## Usability milestones

- **V0.1 read-use**: native shell + conversation list/detail/message rendering + manual sync/full reload + usable cold-start login-state recovery.
- **V0.2 chat-use**: V0.1 + stable multi-conversation state ownership + text send/new conversation + streaming + stop + user-visible reasoning interaction/haptics + recovery integration.
- **V0.3 daily-use refinement**: preferences/metadata, Markdown export, long-conversation tuning, attachments and remaining daily-use conversation features.

## Completed foundations

### Phase 1 — `DEV-app-foundation`

Completed / merged / Stable. b1 reached Code + CI + Artifact + real-device acceptance.

### Phase 2 — `DEV-auth-bootstrap`

Completed / merged / Stable for tested scope. b6 established embedded visible login, default persistent `WKWebsiteDataStore` as the sole persistent auth-secret authority, transient native authorized transport and ordered Plus/personal account context.

### Phase 3 — `DEV-protocol-read`

Completed / merged / Stable for accepted diagnostic read scope. b7 established current list/detail protocol evidence without making the diagnostic probe a production state owner.

### Phase 4 — `DEV-native-read-path`

Completed / merged / Stable for tested b9 scope. `ConversationRepository` owns production conversation summaries/selected detail/current visible branch; sidebar/detail controllers are presentation consumers. b9 accepted shell/list/two distinct details/current-branch visible messages on iPhone/iOS17.

## Phase 5 — `DEV-conversation-recovery`

### User-facing scope

**会话同步与重载 + 冷启动登录状态恢复**

### Current status

**Active b13 test candidate.**

- b10: accepted core `同步最新消息` / clear-then-fetch `重载当前会话` runtime on iPhone/iOS17.
- b11: request paths remained successful, but `navigationItem.prompt` feedback was not visible and is rejected.
- b12: **Code + CI + Artifact + real-device partial acceptance**. Centered sync feedback is accepted. Public WebKit warm-up hydrated 0/0 -> 41/22 cookies and later normal account/list verification succeeded without Login, but the first list request was delayed until the primary/sidebar view was revealed because `ConversationSidebarViewController.viewDidLoad` was lazy on compact iPhone.
- b13: **Code + static/source review + CI + Artifact**. Run `32997544435`; artifact `9617184873`; IPA SHA-256 `2af6334278bcb88683cc123d47617e6956c0efb83aceb9b294961827f3e80040`. Runtime pending.

### Manual recovery contract

- `同步最新消息` uses the authoritative selected conversation identity and existing detail path. It never resends/regenerates.
- Success reconciles server-backed detail; failure preserves previously loaded detail when one exists.
- `重载当前会话` clears authoritative selected detail first, then performs one fresh detail request and rebuilds from returned server state.
- Terminal `重新加载` uses the full-reload path.
- While an **ordinary initial detail load** is still active, the overflow menu keeps both `同步最新消息` and `重载当前会话` available so the user may explicitly recover from a stuck load.
- A manual recovery request supersedes the older ordinary selected-detail operation. The repository rejects a later old completion as `operation_superseded` rather than letting it overwrite the newer result.
- Duplicate manual recovery taps are disabled only while that manual action itself is active.
- No automatic retry/watchdog/fallback/resend chain.

### Sync feedback

- Center-screen native toast, not navigation-bar prompt.
- While syncing: `正在同步最新消息…`.
- Success unchanged: `已是最新`.
- Success changed: `已同步最新消息`.
- Success result remains visible for 2 seconds; this timer is presentation-only.
- Failure removes toast and uses explicit failure UI.
- b12 real-device testing accepted this presentation.

### Cold-start login/list sequencing

Cold-start login-state recovery belongs to the same `DEV-conversation-recovery` Work. Do not create a separate auth-resume task.

Accepted b12 evidence for the tested iPhone/iOS17 cold start:

1. `AuthSessionStore` public `WKWebsiteDataStore.default()` warm-up restored persisted WebKit cookie visibility from `0/0` to `41/22` in `194.97 ms`.
2. The later existing normal account probe succeeded without visible Login and list returned 28/29.
3. Therefore the b12 observed long startup wait was not an auth failure; list loading was simply not started until the lazy sidebar view loaded.

b13 keeps the accepted warm-up and changes only the evidenced startup issue:

1. `RootViewController` installs the shell after warm-up and immediately forces the sidebar view/load path so its existing first list request starts without waiting for user navigation.
2. The detail screen uses an explicit native sidebar button owned by `RootViewController`; tapping it presents `.primary` directly.
3. Default `WKWebsiteDataStore` remains the sole persistent auth-secret authority.
4. No hidden/shadow WebView, copied persistent token/cookie store, retry loop, timer/watchdog or automatic visible Login navigation.

### b13 acceptance gate

Exact b13 must be tested on iPhone/iOS17 for:

- force-quit -> cold launch without tapping Login; the initial list request starts automatically after warm-up, not after sidebar reveal;
- the explicit top-left sidebar action is usable immediately while the list may still be loading;
- open a conversation and, while `正在读取会话…` is still visible, verify `同步最新消息` and `重载当前会话` are enabled;
- invoke one manual recovery before the ordinary load completes; the newer recovery result wins and any older completion cannot overwrite it;
- centered sync feedback remains correct and full reload remains functional.

Only real-device acceptance can close recovery and allow PR #10 to merge.

## Phase 6 — `DEV-multi-conversation-state`

### Goal

Establish stable multi-conversation session/runtime ownership before send/stream work. See `docs/project/MULTI_CONVERSATION_STATE_PLAN.md` for the authoritative detailed plan.

### Scheduling

Starts **after recovery is merged/accepted**. This precedes round-count/preferences and send/stream because those features depend on clear multi-conversation identity/runtime ownership. The b13 single-selected detail-operation generation is deliberately minimal and will later be generalized into the account-scoped per-conversation freshness model planned here.

## Phase 7 — `DEV-conversation-round-count`

### User-facing scope

**会话轮数显示 / preferences integration**

- Display `聊天 · N轮` / `工作 · N轮` when enabled.
- One user message on the current active branch equals one round; assistant/tool/system/reasoning nodes do not add rounds.
- Derive from authoritative active-branch state, never a second persistent mutable counter.
- `显示会话轮数` defaults On and persists through the existing preference owner once current implementation verifies that owner.
- No extra network request.

Scheduling: after `DEV-multi-conversation-state`, before send/stream, unless a later explicit conflict/dependency review changes the order.

## Phase 8 — `DEV-send-stream`

### Goal

Reach the first daily-chat candidate after read/recovery/multi-conversation ownership is stable.

Scope includes:

- current evidence for text send/new-conversation protocol before production assumptions;
- composer send path, streaming lifecycle and stop/cancel behavior;
- stream identity bound to the correct conversation/message under rapid switching;
- user-visible reasoning status/detail only when the service explicitly provides user-visible material;
- official-style reasoning-to-final haptic transition tuned on real device;
- manual `同步最新消息` as recovery for stale/incomplete server state, never automatic prompt resend.

See `CLIENT_ARCHITECTURE_GAP_REVIEW.md`, `MULTI_CONVERSATION_STATE_PLAN.md` and `UI_INTERACTION_BASELINE.md` for current constraints.

## Phase 9 — `DEV-markdown-export`

Product enhancement: export current authoritative user-visible branch to Markdown. Do not scrape mounted UI cells and do not expose hidden/internal reasoning/tool content.

## Phase 10 — `DEV-long-conversation`

Measure and improve parse/model/render timing, first-visible latency, bounded mounted views, memory growth, scrolling/input latency and lifecycle behavior. b9's accepted 7.50 MB / 2023-node / 20.74 s detail remains a real design input.

## Phase 11 — `DEV-attachments`

Add native photo/file/video attachment flows after text-chat ownership is stable. Evidence current upload protocol before production implementation; keep upload state separate from send state.

## Phase 12 — remaining daily-use features

Split into isolated Work IDs as dependencies stabilize: search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement and other evidenced daily-use capabilities.

## Phase 13 — advanced capabilities

Later candidates: Projects, web search, image/multimodal, Voice, Memory, Deep Research, GPTs and other current ChatGPT-specific capabilities. These do not block early daily use.

## Current next action

Real-device test exact `DEV-conversation-recovery-0.1.0-b13`. If accepted, record Runtime evidence, perform final main/PR/conflict check, merge PR #10 and complete recovery. Then create `DEV-multi-conversation-state` as the next serialized core Work.