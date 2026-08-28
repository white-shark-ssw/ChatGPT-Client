# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-28 through b28 Candidate evidence._

## Purpose

Durable implementation sequence for the native iOS ChatGPT client. Current real source, exact CI/Artifact evidence, real-device evidence and the user's latest explicit requirements outrank stale plan wording.

Constraints: UIKit native client, TrollStore IPA, primary tested runtime iPhone/iOS17, deployment target iOS14, private/internal ChatGPT behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns unless an explicit requirement says otherwise.
4. Do not add speculative retry/fallback/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency daily-use interactions such as Copy and later attachments outrank low-value polish once dependencies exist.
7. Optimize only evidenced bottlenecks, especially for long conversations.

## Usability milestones

- **V0.1 read-use**: native shell + list/detail + manual recovery + accepted cold-start auth warm-up.
- **V0.1 cache-use increment**: account-scoped persistent conversation-list snapshot and rapid-relaunch suppression.
- **V0.2 chat-use**: stable multi-conversation ownership + metadata/preferences + Copy + answer navigation + text Send/new conversation + stream/stop/reasoning/haptics.
- **V0.2 attachment-use increment**: image/file sending + assistant-file tap-download-share.
- **V0.3 refinement**: Markdown/code, conversation previews, export, long-conversation tuning, pagination/search/download manager and remaining daily-use features.

## Completed foundations

### Phase 1 — `DEV-app-foundation`
Completed / merged / Stable.

### Phase 2 — `DEV-auth-bootstrap`
Completed / merged / Stable for tested scope. Default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.

### Phase 3 — `DEV-protocol-read`
Completed / merged / accepted diagnostic read scope.

### Phase 4 — `DEV-native-read-path`
Completed / merged / Stable b9 for recorded scope. `ConversationRepository` is production conversation owner.

### Phase 5 — `DEV-conversation-recovery`
Completed / merged / Stable b15 for recorded Plus/personal iPhone/iOS17 scope; PR #10.

### Phase 6 — `DEV-multi-conversation-state`
Completed / merged / Stable b21 for recorded Plus/personal iPhone/iOS17 read-state scope; PR #23. Accepted account-scoped residents, operation freshness/coalescing/replacement, minimum current-node identity, independent historical scroll, measured resident footprint and selected-title lifecycle. Frozen No.

### Conversation-entry scroll semantics

- First visible presentation with **no valid saved reading anchor** should default to latest/bottom of the current branch without visibly animating through a long conversation.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A.
- Sync/Reload preserve an established resolvable anchor.
- Future active-response follow-tail belongs to Send/Stream and must not pull a user out of intentional history browsing.

### Phase 7 — `DEV-conversation-list-cache-core`
Completed / merged / Stable b23 for recorded Plus/personal iPhone/iOS17 scope; PR #24. Accepted storage-only account-scoped summary snapshot behind `ConversationRepository`, fast provisional cached titles, 60-second rapid-relaunch `recent_skip`, offline retained cache, one-request manual refresh, explicit retained-list feedback and real `28 + 1 -> 29` page-1 preservation. Conditional account-switch/corrupt-cache/iPad/lower-iOS/non-personal paths remain Unverified.

## Phase 8 — `DEV-conversation-round-count`

**Active at b28 Runtime gate.** Branch `dev/conversation-round-count-20260828`; PR #27 open. Do not merge/close or claim Stable until exact b28 passes real-device Runtime.

### Candidate history

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25**: identity-valid Runtime partial/failing. Copy/time/preferences accepted; header, rapid jump, refresh presentation rejected; diagnostics exposed authoritative `total=29` but result 30.
- Post-b25 source-fix output reused b25 identity before b26 allocation; permanently invalid for testing.
- **b26**: Runtime partial/failing. Accepted cold `30 -> 29` authoritative-total bound plus repeated `29/29`, sequential rapid answer targets and compact title-first header. Remaining blockers: jump start/mid-animation hitch, timestamp-above request, large Copy visual and blank top refresh region.
- **b27**: exact source `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`, Run `33144420732`, Artifact `9675208202`, IPA SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b`. Real-device partial/failing. In a stress conversation with 1063 visible messages / 2331 mapping nodes, targets remained sequential but tap-to-motion delay and animation hitch persisted. Right-top refresh changed adjusted top inset from about 97.67 to 131.67 while list reconciliation stayed `28/29 -> 29`, proving the blank band was refresh-control/inset presentation rather than missing data or stranded overscroll. Copy visual remained too large. Superseded.
- **Current b28**: Candidate `DEV-conversation-round-count-0.1.0-b28`, `0.1.0 (28)`, exact product/config source `eacd3e68469e976f6cb41a600729c211f6cd32af`. Push Run `33149698659` / Job `98778576898` success; Runtime Artifact `9677214430`; IPA SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f`; ZIP `sha256:0f51b3172aad23471991f3c04c467bb9da1b6256558001c8f60e55fca5f26c7b`. Initial PR merge-view Run `33149701577` / Job `98778585595` success on merge `f548cc8f568136d08128cc024612f89667680616`. Runtime pending.

### User-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count derived from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- one adaptive previous/next answer control;
- assistant visible-text Copy + user native context Copy;
- centralized persisted Preferences for round count, message time and quick answer navigation.

### Header/type rule

Real-device comparison establishes title-first compact hierarchy. Currently supported ordinary-chat detail may show `聊天 · N轮` / `聊天`. This does not establish a generic Chat/Work resolver; `工作` remains deferred until authoritative current Work/Project type evidence exists.

### Preferences for this Work

- `显示会话轮数`: On by default.
- `显示消息时间`: On by default.
- `显示回答快速跳转`: On by default.

One `AppPreferences` owner persists all three. Toggling presentation must not mutate conversation state or issue requests.

### Shared derivation / answer navigation

- Round count and answer navigation share one derived active-branch `ConversationRoundProjection`.
- A visible user message starts a round; first visible assistant before next visible user is the answer anchor. Tool/reasoning/system nodes do not create rounds.
- Derive answer rows only when authoritative visible messages change; do not scan all messages in every scroll callback.
- Real user drag controls semantic direction; programmatic motion is not user intent.
- Rapid taps advance from the last requested derived answer target via a transient presentation cursor; a real drag clears the cursor.
- b27 Runtime retained correct target progression but disproved repeated long-distance `scrollToRow(...animated:true)` as sufficiently smooth on a 1063-message conversation.
- **b28 execution contract**: resolve the derived answer-row start, compute its valid table offset, and use native `setContentOffset(...animated:true)`. If another answer tap arrives during programmatic motion, stop that motion at the current visible offset and immediately retarget the next derived answer. User drag interrupts and takes priority.
- At animation end, privacy-safe diagnostics may record target/actual offset and landing error; a small final position correction may be nonanimated when required.
- No debounce, timer, watchdog or speculative height-cache subsystem. Add broader row-height caching only if b28 Runtime still provides evidence that layout cost is the bottleneck.

### Timestamp / Copy

- Historical timestamps remain authoritative `createTime` and appear above their owning visible messages; missing time is omitted.
- Copy never includes hidden reasoning/tool/system material and never triggers network requests.
- Assistant Copy uses official small response-action direction. b28 uses a 14pt `doc.on.doc`, clear background, dynamic `.secondaryLabel`, compact 28×28 left-aligned slot. User context Copy remains native. Exact b28 visual remains Runtime-pending.

### List refresh presentation

- Repository list request/reconciliation semantics remain unchanged; `ConversationRepository` is sole authority.
- Right-top refresh and pull-to-refresh are separate presentation sources over the same manual refresh request path.
- Right-top refresh uses navigation feedback only and must never begin/resize/change `UIRefreshControl`.
- Genuine pull refresh uses the native `UIRefreshControl` spinner and `endRefreshing()` only. Do not assign attributed title text that reserves extra height.
- b27 top contentOffset-normalization workaround is removed because Runtime showed the table considered the inflated adjusted inset its real top; overscroll was not the root cause.
- Redundant manual trigger while a list load is active must not start a second request; a newly started pull presentation ends promptly.
- With authoritative total present, page-1 reconcile may preserve no more than `max(0, total - authoritativePage.count)` prior off-page items. b26 real-device accepts this for the tested `28/29` sequence; b28 does not change it.

### b28 Runtime acceptance focus

- In the same long/stress conversation, rapidly tap previous/next while motion is still active: each tap must advance one semantic answer, motion should begin promptly and remain visually continuous, and a real drag must immediately regain control.
- Verify answer landing is at intended assistant answer start and diagnostics do not show material landing error.
- Click right-top refresh repeatedly: the first row must not shift down; adjusted top inset should remain at its ordinary value rather than reproduce the ~34pt b27 increase.
- Exercise actual pull refresh: native spinner must appear/collapse cleanly with no persistent blank band and no duplicate request.
- Verify assistant Copy is visibly closer to official small quick-action scale in Light/Dark and remains functional; user context Copy still works.
- Verify timestamps remain above both roles.
- Confirm list `pageCount=28 / totalCount=29` remains `resultCount<=29`.
- Retain A/B independent semantic anchors and Sync/Reload answer-anchor rebuild.
- Basic Dynamic Type/VoiceOver sanity.

## Phase 9 — `DEV-send-stream`

After Phase 8 acceptance, evidence current text Send/new-conversation/stream/stop protocol and implement composer, pending-to-authoritative conversation identity handoff, per-conversation response lifecycle, incremental stream UI, Stop, user-visible reasoning and required reasoning-to-final haptics.

- No global response owner.
- Hidden A may continue responding while B is visible.
- Sync/Reload never resend.
- Follow-tail applies only while user remains near latest; deliberate history browsing must not be stolen.
- As soon as exact real-device text chat/stream works, issue the earliest practical daily-chat Candidate.

## Phase 10 — `DEV-attachments`

High-priority immediately after accepted Send/Stream. Use `ATTACHMENT_TRANSFER_PLAN.md`. First Candidate: native Photos/document picker, per-conversation pending attachment state/removal, evidenced upload protocol, assistant file cards, tap -> explicit download -> app-private file -> `UIActivityViewController`; explicit retry only, no automatic retry. Full download manager does not block this phase.

## Phase 11 — `DEV-message-rendering`

Markdown paragraphs/headings/lists/links, inline/fenced code, code-block Copy, tables as needed; avoid full-conversation reparse/reload on every stream token.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted cache owner/store. Prefer list-response preview only when evidenced; otherwise bounded preview comes from Detail/Sync/Reload/Send already obtained through normal activity. Never issue one Detail per row merely to manufacture previews. Use centralized future preview preference.

## Phase 13 — `DEV-markdown-export`

Export authoritative current user-visible branch; never scrape mounted cells or expose hidden internal content.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / Markdown-layout timing and optimize only evidenced bottlenecks.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, conversation pagination, background completion, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other current capabilities, each only with current protocol/UI evidence.

## Current next action

Install/test exact b28 Runtime Artifact `9677214430` / IPA SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f` on the accepted iPhone/iOS17 scope using the b28 matrix above. If any Runtime defect remains, record it first and allocate a fresh unique Candidate before corrected product output. Only after accepted b28 Runtime update docs/evidence, confirm final PR merge-view against current main, merge/close Phase 8 as Stable for the tested scope, then proceed to `DEV-send-stream`.
