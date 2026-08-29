# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b42 Phase 9 protocol Runtime; current native Send path is architecture-blocked._

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
- **V0.2 chat-use**: stable multi-conversation ownership + metadata/preferences + Copy + round navigation + text Send/new conversation + stream/stop/reasoning/haptics. **Currently blocked on production Send transport architecture.**
- **V0.2 attachment-use increment**: image/file sending + assistant-file tap-download-share. Blocked until an accepted Send architecture exists.
- **V0.3 refinement**: Markdown/code/rich-content rendering, conversation previews, export, long-conversation tuning, pagination/search/download manager and remaining daily-use features.

## Completed foundations

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for tested scope; persistent `WKWebsiteDataStore` is sole persistent auth-secret authority.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic read scope.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is production conversation owner.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15; PR #10.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21 for recorded Plus/personal iPhone/iOS17 read-state scope; PR #23; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23 for recorded scope; PR #24; Frozen No.
- **Phase 8 `DEV-conversation-round-count`: merged Stable b38 for recorded iPhone/iOS17 scope; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

### Conversation-entry scroll semantics

- First visible presentation with **no valid saved reading anchor** defaults to latest/bottom of the current branch without visibly animating through history.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A.
- Sync/Reload preserve an established resolvable anchor.
- Future active-response follow-tail belongs to Send/Stream and must not pull a user out of intentional history browsing.

## Phase 8 — `DEV-conversation-round-count` — Completed

### Stable user-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- assistant visible-text Copy + user native context Copy;
- persisted Preferences for round count, message time and round navigation;
- first-entry latest/bottom when no valid saved reading anchor exists;
- authoritative-total list reconciliation bound and right-top refresh/top-blank presentation corrections;
- one adaptive previous/next round control with accurate semantic user-message targets and genuine continuous animation;
- long-conversation presentation architecture that avoids the severe self-sizing/scrollbar stutter reproduced in b36.

### Stable Phase 8 architecture / interaction

- Round count and navigation share one derived active-branch `ConversationRoundProjection`.
- A visible authoritative user message starts a round. Physical quick-navigation target is the **round-start user message**.
- Tool/reasoning/system/internal-recipient nodes do not create ordinary chat rounds/rows.
- `ConversationMessagePresentationProjection` is ephemeral presentation-only state: bounded long-message display chunks, deterministic row heights/prefix offsets and message→first-row mapping derive from authoritative messages.
- `ConversationMessageCell` uses deterministic manual frame layout for bounded display chunks. Full-message Copy remains authoritative-message based.
- Real user drag controls viewport intent; programmatic presentation is not user intent.
- Rapid taps advance from the last requested semantic target via one transient cursor; real drag clears/replaces that cursor.
- Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll.
- Short and long jumps use one method.
- Stable b38 presentation: resolve the O(1) deterministic target offset, then continuously animate from the current viewport to that target for 0.35s `.easeInOut` with one cancellable `UIViewPropertyAnimator`.
- Do not reintroduce pre-jump 120pt teleport, `scrollToRow` geometry discovery, end correction snap, debounce, timer, watchdog or retry without new evidence.

### Candidate / Runtime progression

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25-b35**: partial/failing/superseded iterations that established accepted metadata/Copy/list/semantic behavior while exposing navigation defects.
- **b36**: exact Runtime identified the dominant remaining blocker as long-message/table geometry, not animation alone. 47 direct-position samples had median ~187ms, P90 ~780ms, max ~3952ms; ordinary right-side scroll-indicator dragging also severely stuttered; one 161-visible-message table geometry expanded from ~13.8k to ~154.6k points as giant estimated/self-sized rows became realized.
- **b37**: bounded display chunks + deterministic row geometry/prefix offsets + manual frame layout. User exact-device result: **“这次确实不卡了”**. Accepted as the no-stutter geometry/performance baseline.
- **b38**: preserved all b37 geometry and restored genuine continuous full-distance round animation from current viewport to deterministic target. User exact-device result: **“没问题了”**. Accepted and merged as the Stable Phase 8 baseline for recorded scope.

### Exact Stable b38 evidence

- Candidate `DEV-conversation-round-count-0.1.0-b38`, version/build `0.1.0 (38)`.
- Exact tested product/config source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact push Run/Job `33230823568` / `99043233637`, success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: Candidate b38, `0.1.0 (38)`, source `0d1801137e4e`, iOS14 minimum, arm64.
- Final PR head `57b3efe576dbf187171439a68d6d2dfe2fba0ebc`; exact tested product→final PR head delta was docs-only.
- Fresh pre-merge synthetic merge `8168fc1aad006ab665f13f77972159f633361b61` was clean against then-current `main@a6e3b2bc...`.
- PR #27 actual merge commit `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Stable / merged for recorded Phase 8 scope; Frozen No.

### Rendering scope boundary

Current message body remains plain-string presentation. Markdown/table/code/list/link/citation rendering is **not** Phase 8 and belongs future `DEV-message-rendering`. Do not strip raw rich-content markers speculatively.

## Phase 9 — `DEV-send-stream` — Active / architecture-blocked

The phase was activated on its own branch/checkpoint/PR and used unique b39-b42 evidence Candidates. It **did not implement production native Send** because exact protocol Runtime established a security/transport blocker before an evidence-backed native precursor existed.

### Accepted protocol evidence

- Existing and new conversation Send use `POST /backend-api/f/conversation`; existing includes `conversation_id`, new omits it.
- Normal response is HTTP 200 `text/event-stream` using `v1`, early authoritative conversation identity, input/message events, assistant patches, `message_stream_complete`, trailing conversation metadata and `[DONE]`; new chat emits `title_generation`.
- Official server Stop is `POST /backend-api/stop_conversation` with `{ conversation_id, exclude_async_types: [] }`, and a successful Stop may terminate the Send stream without normal `message_stream_complete` / `[DONE]` tail.
- Exact b42 default-primary-assistant new-chat Runtime shows Sentinel `proofOfWork.required=true`, `turnstile.required=true`, `so.required=true`, followed by non-empty PoW and Turnstile finalize submissions before successful Send.

### Current decision

- Current pure-native/transient-WebKit-auth ChatGPT-account Send is **blocked under the current architecture**.
- Do not implement PoW/Turnstile/Sentinel challenge solvers or bypasses, browser-fingerprint replay/emulation, captured proof/token replay, hidden production WebView transport, or guessed alternate/fallback endpoints.
- b42 is accepted protocol/security-boundary Runtime evidence only. Native production Send/Stream, response ownership, follow-tail, reasoning UI and haptics remain unimplemented/unaccepted.
- No b43 is justified merely to repeat the same challenge decision.

### Architecture gate

Further Phase 9 code requires one explicit product/architecture choice:

1. **Defer account-session Send** and keep the current native read/recovery client until an officially supported/non-challenge ChatGPT-account transport exists.
2. **Adopt a user-visible official-Web send surface** while retaining native read/navigation where useful; this is not pure native Send and must be treated as a deliberate architecture change.
3. **Use a separately authenticated officially supported API/product path** if the user explicitly accepts the separate credential/billing/product model; do not silently treat it as the existing ChatGPT-account session.

The agent must not choose among these without the user's product decision.

## Phase 10 — `DEV-attachments`

Originally planned immediately after accepted Send/Stream. It is now **dependency-blocked** until a production Send architecture is chosen and accepted. When unblocked, use `ATTACHMENT_TRANSFER_PLAN.md`: Photos/document picker, per-conversation pending attachments, evidenced upload protocol, assistant file cards, explicit tap-download-share; explicit retry only. Full download manager does not block this phase.

## Phase 11 — `DEV-message-rendering`

Implement native rich message presentation for Markdown paragraphs/headings/lists/links, emphasis, inline/fenced code, code-block Copy and tables as needed. Also investigate current user-visible rich annotation/citation markers such as `filecite` from real protocol content. Preserve authoritative visible text and do not expose hidden reasoning/tool/system content. Avoid full-conversation reparse/reload on every stream token.

This phase does not intrinsically depend on production Send and may be reconsidered as an independent roadmap item if the user explicitly reprioritizes while Phase 9 remains blocked.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted cache owner/store. Prefer list-response preview only when evidenced; otherwise bounded preview comes from Detail/Sync/Reload/Send already obtained through normal activity. Never issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current user-visible branch; never scrape mounted cells or expose hidden internal content.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve the Stable Phase 8 deterministic geometry unless new evidence justifies a change.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

Background completion remains dependent on a real production response lifecycle and must not be opened while Phase 9 lacks an accepted transport.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities, each only with current protocol/UI evidence.

## Current next action

`DEV-send-stream` is blocked at an explicit architecture-choice human gate after exact b42 Runtime. Do not allocate another Send Candidate or write production Send code until the user chooses a permitted architecture direction. Preserve b39-b42 evidence and the Stable b38 merged baseline.
