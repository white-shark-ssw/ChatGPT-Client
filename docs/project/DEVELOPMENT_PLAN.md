# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b38 Runtime acceptance and final Phase 8 merge preparation._

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
- **V0.3 refinement**: Markdown/code/rich-content rendering, conversation previews, export, long-conversation tuning, pagination/search/download manager and remaining daily-use features.

## Completed foundations

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for tested scope; persistent `WKWebsiteDataStore` is sole persistent auth-secret authority.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic read scope.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is production conversation owner.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15; PR #10.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21 for recorded Plus/personal iPhone/iOS17 read-state scope; PR #23; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23 for recorded scope; PR #24; Frozen No.

### Conversation-entry scroll semantics

- First visible presentation with **no valid saved reading anchor** defaults to latest/bottom of the current branch without visibly animating through history.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A.
- Sync/Reload preserve an established resolvable anchor.
- Future active-response follow-tail belongs to Send/Stream and must not pull a user out of intentional history browsing.

## Phase 8 — `DEV-conversation-round-count`

**Runtime accepted on exact b38; final merge/state sync in progress.** Branch `dev/conversation-round-count-20260828`; PR #27.

### Accepted user-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- assistant visible-text Copy + user native context Copy;
- persisted Preferences for round count, message time and round navigation;
- first-entry latest/bottom when no valid saved reading anchor exists;
- authoritative-total list reconciliation bound and right-top refresh/top-blank presentation corrections;
- one adaptive previous/next round control with accurate semantic user-message targets and genuine continuous animation;
- long-conversation presentation architecture that avoids the severe self-sizing/scrollbar stutter reproduced in b36.

### Accepted Phase 8 architecture / interaction

- Round count and navigation share one derived active-branch `ConversationRoundProjection`.
- A visible authoritative user message starts a round. Physical quick-navigation target is the **round-start user message**.
- Tool/reasoning/system/internal-recipient nodes do not create ordinary chat rounds/rows.
- `ConversationMessagePresentationProjection` is ephemeral presentation-only state: bounded long-message display chunks, deterministic row heights/prefix offsets and message→first-row mapping derive from authoritative messages.
- `ConversationMessageCell` uses deterministic manual frame layout for bounded display chunks. Full-message Copy remains authoritative-message based.
- Real user drag controls viewport intent; programmatic presentation is not user intent.
- Rapid taps advance from the last requested semantic target via one transient cursor; real drag clears/replaces that cursor.
- Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll.
- Short and long jumps use one method.
- Accepted b38 presentation: resolve the O(1) deterministic target offset, then continuously animate from the current viewport to that target for 0.35s `.easeInOut` with one cancellable `UIViewPropertyAnimator`.
- Do not reintroduce pre-jump 120pt teleport, `scrollToRow` geometry discovery, end correction snap, debounce, timer, watchdog or retry without new evidence.

### Candidate / Runtime progression

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25-b35**: partial/failing/superseded iterations that established accepted metadata/Copy/list/semantic behavior while exposing navigation defects.
- **b36**: exact Runtime identified the dominant remaining blocker as long-message/table geometry, not animation alone. 47 direct-position samples had median ~187ms, P90 ~780ms, max ~3952ms; ordinary right-side scroll-indicator dragging also severely stuttered; one 161-visible-message table geometry expanded from ~13.8k to ~154.6k points as giant estimated/self-sized rows became realized.
- **b37**: bounded display chunks + deterministic row geometry/prefix offsets + manual frame layout. User exact-device result: **“这次确实不卡了”**. Accepted as the no-stutter geometry/performance baseline.
- **b38**: preserved all b37 geometry and restored genuine continuous full-distance round animation from current viewport to deterministic target. User exact-device result: **“没问题了”**. Accepted for the recorded iPhone/iOS17 Phase 8 scope.

### Exact accepted b38 evidence

- Candidate `DEV-conversation-round-count-0.1.0-b38`, version/build `0.1.0 (38)`.
- Exact product/config source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact product diff from checkpoint parent `73d09cb83c3eda7b255e09b17b2bd9b0897cea49`: workflow identity 2+/2-, Xcode identity 4+/4-, `ConversationFeature.swift` 8+/20- only.
- Exact push Run/Job `33230823568` / `99043233637`, success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: Candidate b38, `0.1.0 (38)`, source `0d1801137e4e`, iOS14 minimum, arm64.
- Product-head PR Run/Job `33230825189` / `99043238346` passed on synthetic merge `fd1ed7508f04e9045b99239cad88dca8f6e01450` against then-current `main@a6e3b2bc...`.
- Final merge still requires fresh current-head/current-main mergeability verification because later docs-only commits advanced the branch after the tested product source.

### Phase 8 completion gate

1. Durable docs/index reflect exact b38 Runtime acceptance.
2. Verify current branch/main/PR/active-task conflict state.
3. Verify exact product source→current branch delta is docs-only and obtain fresh current-head/current-main merge view.
4. Merge PR #27 using expected current head if still mergeable.
5. On main, record actual merge SHA/current main, promote tested Phase 8 scope to Stable (Frozen No), remove only `docs/project/current/dev/DEV-conversation-round-count.md`.

### Rendering scope boundary

Current message body remains plain-string presentation. Markdown/table/code/list/link/citation rendering is **not** Phase 8 and belongs future `DEV-message-rendering`. Do not strip raw rich-content markers speculatively.

## Phase 9 — `DEV-send-stream`

After Phase 8 is merged/closed, evidence current text Send/new-conversation/stream/stop protocol and implement composer, pending-to-authoritative identity handoff, per-conversation response lifecycle, incremental stream UI, Stop, visible reasoning and required haptics.

- Read `SEND_STREAM_PREFLIGHT.md` before activation.
- Read `CLIENT_ARCHITECTURE_GAP_REVIEW.md` and the current post-recovery sequence before creating/activating the Work.
- No global response owner.
- Hidden A may continue responding while B is visible.
- Sync/Reload never resend.
- Follow-tail applies only near latest; deliberate history browsing must not be stolen.
- Issue the earliest practical daily-chat Candidate once exact real-device text chat/stream works.

## Phase 10 — `DEV-attachments`

Immediately after accepted Send/Stream. Use `ATTACHMENT_TRANSFER_PLAN.md`: Photos/document picker, per-conversation pending attachments, evidenced upload protocol, assistant file cards, explicit tap-download-share; explicit retry only. Full download manager does not block this phase.

## Phase 11 — `DEV-message-rendering`

Implement native rich message presentation for Markdown paragraphs/headings/lists/links, emphasis, inline/fenced code, code-block Copy and tables as needed. Also investigate current user-visible rich annotation/citation markers such as `filecite` from real protocol content. Preserve authoritative visible text and do not expose hidden reasoning/tool/system content. Avoid full-conversation reparse/reload on every stream token.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted cache owner/store. Prefer list-response preview only when evidenced; otherwise bounded preview comes from Detail/Sync/Reload/Send already obtained through normal activity. Never issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current user-visible branch; never scrape mounted cells or expose hidden internal content.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve the accepted Phase 8 deterministic geometry unless new evidence justifies a change.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities, each only with current protocol/UI evidence.

## Current next action

Finish the exact b38 finalization gate above. After Phase 8 is merged and its checkpoint removed, the next planned development phase is `DEV-send-stream`; it must run its own new-task routing/preflight and evidence current protocol before code is written.
