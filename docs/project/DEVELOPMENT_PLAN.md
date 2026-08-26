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

**Active b12 real-device candidate.**

- b10: accepted core `同步最新消息` / clear-then-fetch `重载当前会话` runtime on iPhone/iOS17.
- b11: request paths remained successful, but `navigationItem.prompt` feedback was not visible to the user and is rejected as final presentation.
- b12: **Code + static/source review + CI + Artifact**. Run `32993589071`; artifact `9615588166`; IPA SHA-256 `2bd24e1dff89d2c04c82e838b44bf9e584d1587534ab6338b33b23bde0861aab`. Runtime pending.

### Manual recovery contract

- `同步最新消息` uses the authoritative selected conversation identity and existing detail path. It never resends/regenerates.
- Success reconciles server-backed detail; failure preserves the previously loaded detail.
- `重载当前会话` clears authoritative selected detail first, then performs one fresh detail request and rebuilds from returned server state.
- Terminal `重新加载` uses the full-reload path.
- No automatic retry/watchdog/fallback chain.

### b12 sync feedback

- Center-screen native toast, not navigation-bar prompt.
- While syncing: `正在同步最新消息…`.
- Success unchanged: `已是最新`.
- Success changed: `已同步最新消息`.
- Success result remains visible for 2 seconds; this timer is presentation-only.
- Failure removes toast and uses the explicit failure alert.

### Cold-start login-state recovery ownership

Latest project governance assigns this to **the same `DEV-conversation-recovery` Work**. Do not create a separate auth-resume task.

b12 tests the minimum evidence-backed hypothesis:

1. `AuthSessionStore` initializes `WKWebsiteDataStore.default()` using public APIs, records safe cookie counts before/after and website-data record count.
2. `RootViewController` waits for that warm-up to complete before installing sidebar/detail controllers.
3. Sidebar's existing initial list load then performs the same **single** normal account-context probe.
4. Default `WKWebsiteDataStore` remains the only persistent auth-secret authority.
5. No hidden/shadow WebView, no copied persistent token/cookie store, no retry loop, no automatic visible login navigation.
6. If the one background warm-up + normal probe fails, keep the existing explicit `登录 / 账户验证` UI as foreground fallback and preserve diagnostics before changing strategy.

### Acceptance gate

Exact b12 must be tested on iPhone/iOS17 for:

- true cold launch after force-quit **without tapping Login first**;
- centered sync progress/result toast and 2-second result visibility;
- existing full reload behavior remains intact.

If cold start fails, export diagnostics before visible login and treat b12 as partial/failing Runtime evidence rather than adding retries by guess.

## Phase 6 — `DEV-multi-conversation-state`

### Goal

Establish stable multi-conversation session/runtime ownership before send/stream work. See `docs/project/MULTI_CONVERSATION_STATE_PLAN.md` for the authoritative detailed plan.

### Scheduling

Starts **after recovery is merged/accepted**. This precedes round-count/preferences and send/stream because those features depend on clear multi-conversation identity/runtime ownership.

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

Real-device test exact `DEV-conversation-recovery-0.1.0-b12`. If accepted, record Runtime evidence, perform final main/PR/conflict check, merge PR #10 and complete/archive recovery. Then create `DEV-multi-conversation-state` as the next serialized core Work.
