# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b33 Candidate/Artifact evidence and b32 Runtime result._

## Purpose

Durable implementation sequence for the native iOS ChatGPT client. Current real source, exact CI/Artifact evidence, real-device evidence and the user's latest explicit requirements outrank stale plan wording.

Constraints: UIKit native client, TrollStore IPA, primary tested runtime iPhone/iOS17, deployment target iOS14, private/internal ChatGPT behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns unless an explicit requirement says otherwise.
4. Do not add speculative retry/fallback/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency daily-use interactions such as Copy and attachments outrank low-value polish once dependencies exist.
7. Optimize only evidenced bottlenecks, especially for long conversations.

## Usability milestones

- **V0.1 read-use**: native shell + list/detail + manual recovery + accepted cold-start auth warm-up.
- **V0.1 cache-use increment**: account-scoped persistent list snapshot and rapid-relaunch suppression.
- **V0.2 chat-use**: stable multi-conversation ownership + metadata/preferences + Copy + round navigation + text Send/new conversation + stream/stop/reasoning/haptics.
- **V0.2 attachment-use increment**: image/file sending + assistant-file tap-download-share.
- **V0.3 refinement**: Markdown/code, conversation previews, export, long-conversation tuning, pagination/search/download manager and remaining daily-use features.

## Completed foundations

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for tested scope; persistent `WKWebsiteDataStore` is sole persistent auth-secret authority.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic read scope.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is production conversation owner.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15; PR #10.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21 for recorded Plus/personal iPhone/iOS17 read-state scope; PR #23; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23 for recorded scope; PR #24; accepted storage-only account-scoped summary cache, provisional titles, 60-second `recent_skip`, offline retention, one-request manual refresh and real `28 + 1 -> 29` preservation.

### Conversation-entry scroll semantics

- First visible presentation with **no valid saved reading anchor** defaults to latest/bottom of the current branch without visibly animating through history.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A.
- Sync/Reload preserve an established resolvable anchor.
- Future active-response follow-tail belongs to Send/Stream and must not pull a user out of intentional history browsing.

## Phase 8 — `DEV-conversation-round-count`

**Active at exact b33 Runtime gate.** Branch `dev/conversation-round-count-20260828`; PR #27 open. Do not merge/close or claim Stable until exact b33 passes real-device Runtime.

### User-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- one adaptive previous/next round control;
- assistant visible-text Copy + user native context Copy;
- persisted Preferences for round count, message time and round navigation;
- first-entry latest/bottom when no valid saved reading anchor exists;
- evidence-backed list refresh/reconcile presentation corrections without a second list/network owner.

### Header/type rule

Real-device comparison establishes title-first compact hierarchy. Current ordinary-chat detail may show `聊天 · N轮` / `聊天`. `工作` remains deferred until authoritative Work/Project type evidence exists.

### Preferences

- `显示会话轮数`: On by default.
- `显示消息时间`: On by default.
- `显示轮次快速跳转`: On by default.

One `AppPreferences` owner persists all three. Toggling presentation must not mutate conversation state or issue requests.

### Shared derivation / round navigation

- Round count and navigation share one derived active-branch `ConversationRoundProjection`.
- A visible authoritative user message starts a round. The first visible assistant before the next visible user may remain round metadata, but the accepted physical quick-navigation target is the **round-start user-message row**.
- Tool/reasoning/system/internal-recipient nodes do not create ordinary chat rounds/rows.
- Derive rows only when authoritative visible messages change; do not scan all messages in every scroll callback.
- Real user drag controls user intent; programmatic motion is not user intent.
- Rapid taps advance from the last requested derived round target via one transient presentation cursor; real drag clears/replaces that cursor.
- Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll.
- Native animated `scrollToRow(..., .top, animated:true)` remains the movement owner.
- At animation completion, measure native landing; apply one nonanimated same-target re-anchor only when absolute native landing error exceeds `1pt`.
- No debounce, timer, watchdog or speculative row-height cache subsystem.

### Timestamp / Copy

- Historical timestamps use authoritative `createTime` and appear with their owning visible messages; missing time is omitted.
- Copy never includes hidden reasoning/tool/system material and never triggers network requests.
- Assistant Copy remains compact, clear-background and dynamically tinted; do not modify it merely to chase navigation smoothness without new evidence.

### List refresh / cache presentation

- `ConversationRepository` remains sole list/conversation authority.
- Right-top refresh and pull-to-refresh are separate presentation sources over the same manual refresh request path.
- Right-top refresh must never begin/resize/change `UIRefreshControl` and must not use `navigationItem.prompt`.
- Genuine pull uses native spinner + `endRefreshing()` only; no attributed/text title.
- b29 Runtime accepts the tested right-top fix: first row no longer gets the persistent blank band and adjusted top inset remains ordinary.
- b26 accepted the authoritative-total stale-row cap (`30 -> 29`, repeated `29/29`); retain unchanged.

### Candidate / Runtime history

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25**: Runtime partial/failing; Copy/time/preferences accepted, header/jump/refresh rejected, list count over authoritative total exposed.
- **b26**: Runtime partial/failing; bounded list reconciliation, sequential targets and compact header accepted.
- **b27**: Runtime partial/failing; long-conversation jump hitch persisted, right-top refresh inflated inset, Copy visual rejected.
- **b28**: Runtime partial/failing; large assistant-answer landing drift, direction flips, first-entry top and blank refresh band reproduced.
- **b29**: Runtime partial/failing; right-top refresh correction accepted, but `estimatedRowHeight=0` broke self-sizing message presentation and is rejected.
- **b30**: Runtime partial/failing; automatic self-sizing restored, prior severe hitch improved, but Copy remained too large and assistant-answer landing remained grossly inaccurate.
- **b31**: Runtime partial/failing; physical target moved to semantic user-message round starts and landing became precise; remaining hitch/internal-row/Copy issues required correction.
- **b32**: exact Runtime partial/failing. Long/tool-heavy sample accepted recipient/tool filtering (`filteredRecipientMessageCount=748`, ordinary visible messages `84`), compact Copy direction and precise semantic landing. Remaining defects: jump smoothness and physical-bottom rubber-band direction.

### Exact b33 Candidate

- Candidate `DEV-conversation-round-count-0.1.0-b33`, version/build `0.1.0 (33)`.
- Exact product/config source `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- Product delta is intentionally narrow: physical boundaries outrank drag delta; native animated row scrolling retained; one >1pt end-of-animation same-target correction; privacy-safe landing diagnostics. b32 filtering/round derivation/Copy/list/network/state ownership unchanged.
- Exact push Run / Job `33195740528` / `98932282377`, success.
- Runtime Artifact `9695669835`; ZIP `sha256:841b682ffe27a2788b2c297225705c0b4fb6bc18b527fd4e8f30c62e10312407`.
- IPA `ChatGPTClient-0.1.0-b33-dev-conversation-round-count.ipa`; IPA SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`.
- Package inspection independently matches `0.1.0 (33)`, Candidate b33, source `0ba15ec48fe8`, iOS14 minimum, arm64.
- PR merge-view against `main@a6e3b2bc185b8d5df90b846040387262a64e6154`: Run / Job `33195744651` / `98932296906`, success on `ca28819de6e5ed345087d04005ed05d74508881c`; merge Artifact `9695673573`. Merge-view output is CI evidence only and is not the Runtime Artifact.

### b33 Runtime acceptance focus

1. At physical bottom, including rubber-band overscroll, adaptive control must remain/resolve to **上一轮** when a previous round exists; it must not flip to 下一轮 merely from overscroll delta.
2. Long previous/next jumps should use one smooth native animation without the prior serious end-of-animation hitch.
3. Landing must remain precise at the intended user-message round start; rapid repeated taps advance one semantic round per tap.
4. If correction occurs, diagnostics should show `nativeLandingErrorPoints` and `landingCorrectionApplied=true`; normal accurate native landings should generally avoid correction.
5. Regression sanity: tool/internal rows remain filtered, Copy remains accepted compact visual/function, first-entry latest/bottom remains correct, A/B anchors and Sync/Reload remain intact, timestamps/preferences/header/list reconcile remain intact.

## Phase 9 — `DEV-send-stream`

After Phase 8 acceptance, evidence current text Send/new-conversation/stream/stop protocol and implement composer, pending-to-authoritative identity handoff, per-conversation response lifecycle, incremental stream UI, Stop, visible reasoning and required haptics.

- Read `SEND_STREAM_PREFLIGHT.md` before activation.
- No global response owner.
- Hidden A may continue responding while B is visible.
- Sync/Reload never resend.
- Follow-tail applies only near latest; deliberate history browsing must not be stolen.
- Issue the earliest practical daily-chat Candidate once exact real-device text chat/stream works.

## Phase 10 — `DEV-attachments`

Immediately after accepted Send/Stream. Use `ATTACHMENT_TRANSFER_PLAN.md`: Photos/document picker, per-conversation pending attachments, evidenced upload protocol, assistant file cards, explicit tap-download-share; explicit retry only. Full download manager does not block this phase.

## Phase 11 — `DEV-message-rendering`

Markdown paragraphs/headings/lists/links, inline/fenced code, code-block Copy and tables as needed; avoid full-conversation reparse/reload on every stream token.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted cache owner/store. Prefer list-response preview only when evidenced; otherwise bounded preview comes from Detail/Sync/Reload/Send already obtained through normal activity. Never issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current user-visible branch; never scrape mounted cells or expose hidden internal content.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / Markdown-layout timing and optimize only evidenced bottlenecks.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities, each only with current protocol/UI evidence.

## Current next action

Install/test **exact b33 Runtime Artifact `9695669835`** / IPA SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855` on the accepted iPhone/iOS17 scope using the b33 matrix above. If a Runtime defect remains, record it first and allocate a fresh Candidate before corrected product output. Only after accepted Runtime, synchronize final PR merge-view against current main, merge/close Phase 8 as Stable for the tested scope, then proceed to `DEV-send-stream`.