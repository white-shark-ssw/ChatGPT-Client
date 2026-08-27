# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-28._

## Purpose

This is the durable implementation sequence for the iOS-native ChatGPT client. Current source, CI/artifact evidence, real-device evidence, explicit user requirements and specialized plans under `docs/project/` take priority over stale historical wording.

Current constraints: native UIKit iOS client; TrollStore IPA; primary tested runtime iPhone/iOS17; deployment target iOS14; current ChatGPT private/internal behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns unless an explicit requirement says otherwise.
4. Do not add speculative retry/fallback/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency operations such as Copy and image/file transfer outrank lower-frequency polish once their dependencies exist.
7. Persistent list caching is early infrastructure/performance because repeated cold starts otherwise begin with no list data and may cause unnecessary repeated list requests during development/testing.

## Usability milestones

- **V0.1 read-use**: native shell + list/detail + manual recovery + accepted cold-start auth warm-up.
- **V0.1 cache-use increment**: V0.1 + account-scoped persistent conversation-list snapshot so cold start can show known rows immediately and rapid relaunches can avoid needless automatic list refreshes when the cache was just synchronized.
- **V0.2 chat-use**: stable multi-conversation ownership + metadata/preferences + message Copy + answer navigation + text send/new conversation + stream/stop/reasoning/haptics.
- **V0.2 attachment-use increment**: image/file sending + assistant-file tap-download-share.
- **V0.3 refinement**: Markdown/code rendering, conversation-list previews, Markdown export, long-conversation tuning, pagination/search/download manager and remaining daily-use features.

## Completed foundations

### Phase 1 — `DEV-app-foundation`
Completed / merged / Stable.

### Phase 2 — `DEV-auth-bootstrap`
Completed / merged / Stable for tested scope. Default persistent `WKWebsiteDataStore` remains the sole persistent auth-secret authority.

### Phase 3 — `DEV-protocol-read`
Completed / merged / Stable for accepted diagnostic read scope.

### Phase 4 — `DEV-native-read-path`
Completed / merged / Stable for tested b9 scope. `ConversationRepository` is the production conversation owner.

### Phase 5 — `DEV-conversation-recovery`
Completed / merged / Stable for recorded Plus/personal iPhone/iOS17 scope. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`; exact evidence remains in `BUILD_TEST_INDEX.md`.

### Phase 6 — `DEV-multi-conversation-state`

**Completed / merged / Stable for the recorded Plus/personal iPhone/iOS17 read-state scope.** PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`; final Runtime Candidate is `DEV-multi-conversation-state-0.1.0-b21` with exact product/config source `6b50ead167bfde305d2ad58dd16fee6edaabf597`. Frozen remains No.

Accepted scope includes account-scoped per-conversation resident state, stale-operation protection, same-target coalescing/replacement ownership, minimum current-node identity, independent historical scroll presentation, measured 0→8 resident process footprint, selected-title lifecycle ordering, and same-target Reload replacement-under-load/hidden-rejoin behavior.

Evidence boundaries retained after closure: natural failed-resident navigation, supported account-switch purge, non-personal workspace identity and missing-anchor-message discard remain Unknown / Unverified where applicable; normal LRU capacity remains unfrozen because current real-device evidence does not justify one. Future active-response follow-tail belongs to Send/Stream.

### Conversation-entry scroll semantics

- First visible presentation with **no valid saved reading anchor** defaults to the latest message / bottom of the current branch.
- This first placement does not visibly animate from the top through a long conversation.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A rather than forcing bottom.
- Sync/Reload preserve an established reading anchor through the existing presentation owner.
- Future Send/Stream follow-tail applies only while the user remains at/near the latest edge; deliberate history browsing must not be pulled back to bottom.

### Phase 7 — `DEV-conversation-list-cache-core`

**Completed / merged / Stable for the recorded Plus/personal iPhone/iOS17 cache-core scope.** PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`; final Runtime Candidate is `DEV-conversation-list-cache-core-0.1.0-b23`.

Accepted scope includes:

- one account-scoped persistent conversation-list snapshot behind `ConversationRepository`;
- fast provisional cached-title presentation on cold start while preserving verified auth/account authority boundaries;
- accepted 60-second rapid-relaunch `recent_skip` behavior for the recorded use case;
- offline retained-cache presentation after temporary auth transport failure;
- manual refresh bypass with explicit success/failure presentation;
- first-page reconciliation that preserves known off-page rows when the server returns 28 of total 29;
- app-private versioned storage without Detail/message-body persistence, copied auth secrets, per-row Detail prefetch, retry/timer/watchdog/polling, or a second list authority.

Conditional supported account-switch mismatch, corrupt/schema rejection, provisional-row Detail-block tap, iPad, runtime below iOS17 and non-personal workspace identity remain Unknown / Unverified where applicable. They do not block the next serialized Work.

## Phase 8 — `DEV-conversation-round-count`

**Active at Runtime gate.** Dedicated branch: `dev/conversation-round-count-20260828`.

- Historical b24 compiled but its actual package identity was invalid: the stale build script overrode the intended Candidate with cache-core b23 and retained the cache-core IPA slug. b24 is permanently rejected/reserved and was never installed.
- Current exact Runtime Candidate is `DEV-conversation-round-count-0.1.0-b25` / `0.1.0 (25)` with product/config source `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`.
- Exact b25 CI Run `33110228837` / Job `98650799276` succeeded; identity-valid Artifact `9662219000`; IPA `ChatGPTClient-0.1.0-b25-dev-conversation-round-count.ipa`; IPA SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`; embedded Candidate `DEV-conversation-round-count-0.1.0-b25`; source marker `5e6a61a45b5a`.
- Evidence level is currently Code + static/source/package review + exact CI + identity-valid Artifact. **Runtime/manual/real-device remains Not tested; Stable/Frozen No.**

### User-facing bundle

- round metadata derived from authoritative visible user turns;
- per-user/per-assistant message timestamps from authoritative `createTime` when available;
- adaptive `上一轮回答` / `下一轮回答` floating navigation with native animated scrolling;
- basic one-tap Copy for visible user and assistant message text;
- first centralized Preferences owner for these toggles and later settings.

Historical interaction planning described `聊天 · N轮` / `工作 · N轮`. Current source/repository evidence does **not** establish an authoritative Chat/Work conversation-type owner, and architecture rules forbid guessing identity from UI text. Until such a source is evidenced, this Work presents only verified `N轮`; adding `聊天` / `工作` is deferred rather than fabricated.

### Preferences frozen for this Work

- `显示会话轮数`: On by default;
- `显示消息时间`: On by default;
- `显示回答快速跳转`: On by default.

All three are persisted by the single centralized `AppPreferences` owner. Toggling presentation settings must not mutate conversation/message authority or issue network requests.

### Shared derivation / behavior

- Round count and answer navigation share one derived active-branch round projection, not parallel mutable counters.
- A visible user message starts a round; the first visible assistant reply before the next user message is that round's answer anchor.
- Tool/reasoning/system nodes do not create rounds.
- Recompute answer anchors only when authoritative visible messages change, not on every scroll callback.
- Quick-jump animation is native scroll-container animation, not timer-stepped fake scrolling.
- Quick-jump direction follows real user drag intent; programmatic jump animation must not masquerade as a new user drag, and valid boundary availability wins.
- Copy never includes hidden reasoning/tool/system material and never triggers network requests.
- Historical timestamps use existing authoritative service time; if it is absent, omit the timestamp rather than fabricate one.

### Runtime acceptance focus for b25

- verify round count against a known long conversation and confirm the Off setting removes only presentation;
- verify all three preferences persist after leaving Settings and after process relaunch;
- verify user/assistant historical timestamps use plausible local formatting and messages with absent authoritative time do not get fabricated metadata;
- verify assistant one-tap Copy and user context-menu Copy copy only visible text with `已复制` feedback;
- repeatedly drag/jump older/newer through a long conversation, including first/last boundaries; jumps must visibly animate to the adjacent answer and never trigger extra Detail requests;
- verify A/B conversation switching preserves independent semantic scroll anchors; jumping in B must not mutate A;
- verify Sync/Reload re-derive answer anchors and preserve/discard the existing semantic scroll anchor according to the established presentation owner;
- basic Dynamic Type/VoiceOver sanity for the new metadata/actions/control.

## Phase 9 — `DEV-send-stream`

Evidence the current text Send/new-conversation/stream/stop protocol, then implement composer, pending-to-authoritative identity handoff, per-conversation response lifecycle, incremental stream presentation, Stop, user-visible reasoning interaction and required reasoning-to-final haptic behavior.

- No global response owner.
- A hidden conversation may continue responding while another is visible.
- Sync/Reload never resend messages.
- If user is at/near latest, stream may follow tail; once user intentionally browses history, stream must not steal the viewport.
- Once new-chat creation is genuinely usable, transition the compact startup/navigation UX from the current read-stage conversation-list-first shell toward the official-style new-chat main surface with the sidebar as navigation/history entry; Projects remain a later evidenced capability and do not block that shell transition.

**As soon as exact real-device text chat/stream works, issue the earliest practical daily-chat Candidate.**

## Phase 10 — `DEV-attachments`

High-priority immediately after accepted text Send/Stream. Durable design: `ATTACHMENT_TRANSFER_PLAN.md`.

Core first Candidate:

- native photo/image picker;
- native document/file picker;
- per-conversation pending attachment cards/thumbnails and removal before Send;
- evidence current upload/asset/message attachment protocol before implementation;
- assistant user-visible file cards;
- tap file -> explicit file-backed download -> app-private local file -> immediate `UIActivityViewController` share sheet;
- visible transfer failure, explicit user retry only; no automatic retry loop;
- full custom download manager does not block this phase.

## Phase 11 — `DEV-message-rendering`

Improve development-chat readability:

- Markdown paragraphs/headings/lists/links;
- inline/fenced code;
- code-block one-tap Copy while retaining whole-message Copy;
- tables when needed;
- no full-conversation reparse/reload on every streamed token.

## Phase 12 — `DEV-conversation-list-preview`

This is the **preview/UI enhancement built on the accepted cache core** rather than a second persistence implementation.

- Reuse the same persistent list snapshot/store and repository owner from `DEV-conversation-list-cache-core`.
- First verify whether the current list response itself exposes a safe user-visible preview/snippet field.
- If not, populate bounded previews only from Detail/Sync/Reload already obtained through normal user activity and from later authoritative Send/Stream events.
- Never issue one Detail request per row solely to manufacture previews.
- Show one clipped secondary preview line and use the centralized `显示会话消息预览` preference.
- Streaming must not write preview data to disk token-by-token.

Do not create a second list/cache store for this phase.

## Phase 13 — `DEV-markdown-export`

Export the authoritative current user-visible branch to Markdown; never scrape mounted cells or expose hidden/internal reasoning/tool content.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / Markdown-layout timing and optimize only evidenced bottlenecks.

## Phase 15 — remaining daily-use features

Split into isolated Work IDs as dependencies stabilize:

- `DEV-download-manager` — persistent download history/progress/re-share/storage controls;
- conversation pagination/load-more using the same list-cache/reconciliation owner;
- background wait/completion notification and later TrollStore true-background experiment;
- search;
- rename/archive/delete;
- edit/regenerate/branch switching;
- model selection/temporary chat;
- settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other current capabilities, each only with current protocol/UI evidence.

## Current next action

`DEV-conversation-round-count` remains the Active serialized development Work. b25 is the exact identity-valid Runtime Candidate; do not change product/config code or candidate identity while merely performing governance/PR documentation work.

Next sequence:

1. synchronize remaining durable docs and open the Work PR after final base/conflict guard;
2. treat PR merge-view CI/Artifact as merge evidence only, not Runtime evidence;
3. install/test exact b25 on the accepted iPhone/iOS17 scope using the Runtime focus above;
4. only after accepted Runtime update checkpoint/state/index, merge/close the Work as Stable for the tested scope;
5. then proceed `DEV-send-stream -> earliest daily-chat Candidate -> DEV-attachments -> DEV-message-rendering -> DEV-conversation-list-preview`.