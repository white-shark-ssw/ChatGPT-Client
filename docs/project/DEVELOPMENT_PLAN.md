# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-28 through b29 Candidate evidence and b28 Runtime failure._

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

- First visible presentation with **no valid saved reading anchor** defaults to latest/bottom of the current branch without visibly animating through a long conversation.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A.
- Sync/Reload preserve an established resolvable anchor.
- Future active-response follow-tail belongs to Send/Stream and must not pull a user out of intentional history browsing.
- b28 Runtime proved the no-anchor latest rule had not actually been implemented: a 1577-visible-message conversation remained at ordinary top (`contentOffsetY≈-97.67`). b29 corrects the current read/presentation path; this is not deferred to Send/Stream.

### Phase 7 — `DEV-conversation-list-cache-core`
Completed / merged / Stable b23 for recorded Plus/personal iPhone/iOS17 scope; PR #24. Accepted storage-only account-scoped summary snapshot behind `ConversationRepository`, fast provisional cached titles, 60-second rapid-relaunch `recent_skip`, offline retained cache, one-request manual refresh, explicit retained-list feedback and real `28 + 1 -> 29` page-1 preservation. Conditional account-switch/corrupt-cache/iPad/lower-iOS/non-personal paths remain Unverified.

## Phase 8 — `DEV-conversation-round-count`

**Active at b29 Runtime gate.** Branch `dev/conversation-round-count-20260828`; PR #27 open. Do not merge/close or claim Stable until exact b29 passes real-device Runtime.

### Candidate history

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25**: identity-valid Runtime partial/failing. Copy/time/preferences accepted; header, rapid jump and refresh presentation rejected; diagnostics exposed authoritative `total=29` but result 30.
- Post-b25 source-fix output reused b25 identity before b26 allocation; permanently invalid for testing.
- **b26**: Runtime partial/failing. Accepted cold `30 -> 29` authoritative-total bound plus repeated `29/29`, sequential rapid answer targets and compact title-first header. Remaining blockers were jump start/mid-animation hitch, timestamp-above request, large Copy visual and blank top refresh region.
- **b27**: exact source `3bda8d8d78ecd03e4a8d0b2343458189df4b000e`, Run `33144420732`, Artifact `9675208202`, IPA SHA `a8cccaf41a850d55b455d0484f4baaf3c051075ba5bad9045a739311f1c6288b`. Runtime partial/failing. In a stress conversation with 1063 visible messages / 2331 mapping nodes, targets remained sequential but tap-to-motion delay and animation hitch persisted. Right-top refresh changed adjusted top inset from about 97.67 to 131.67 while list reconciliation stayed `28/29 -> 29`; Copy visual remained too large. Superseded.
- **b28**: Candidate `DEV-conversation-round-count-0.1.0-b28`, source `eacd3e68469e976f6cb41a600729c211f6cd32af`, push Run `33149698659`, Runtime Artifact `9677214430`, IPA SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f`. Runtime partial/failing. On a 1577-visible-message conversation, completion diagnostics showed major target drift (examples about `-1950`, `-7330`, `-11407` pt); continuous taps could flip direction without real drag; first entry remained at top; right-top refresh still produced the blank top region after refresh-control attributed text was already removed. Superseded.
- **Current b29**: Candidate `DEV-conversation-round-count-0.1.0-b29`, `0.1.0 (29)`, exact product/config source `0b0c2fea44503423e75696f777fbf627aefac500`. Push Run `33155124626` / Job `98795968389` success; Runtime Artifact `9679291236`; IPA SHA `4378fe9b6a7340ea64a5c82063b0f7e3368e92deaf567d5e0ac40c08055a5360`; ZIP `sha256:a6b481acd410c97a7db37c467decc11504f3925e2a45fa9b7e2e5ba3a10e907c`. Initial PR merge-view Run `33155126832` / Job `98795975759` success on merge `a9a0cc286856e36df7378aa62be67f379ca631c2`. Runtime pending.

### User-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count derived from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- one adaptive previous/next answer control;
- assistant visible-text Copy + user native context Copy;
- centralized persisted Preferences for round count, message time and quick answer navigation;
- first-entry latest/bottom presentation when no valid saved reading anchor exists.

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
- b26/b27 Runtime retained correct sequential target progression.
- b27 disproved repeated long-distance `scrollToRow(...animated:true)` as sufficiently smooth.
- b28 replaced that execution with interruptible native content-offset animation, but Runtime then proved off-screen target coordinates derived from self-sizing rows with a fixed 96pt estimate could drift by thousands of points as actual heights resolved.
- **b29 execution contract**: retain the same derived semantic cursor; disable the fixed estimated-row height, lay out before resolving target row rect/offset, then use the existing interruptible native content-offset animation. While a programmatic target exists and both directions remain available, retain the current clicked direction; only real user drag or a boundary changes direction.
- At animation end, privacy-safe diagnostics may record target/actual offset and landing error; a small final nonanimated correction may remain when necessary.
- No debounce, timer, watchdog or speculative height-cache subsystem. Add broader row-height caching only if exact b29 Runtime still provides evidence that a cache is required.

### Timestamp / Copy

- Historical timestamps remain authoritative `createTime` and appear above their owning visible messages; missing time is omitted.
- Copy never includes hidden reasoning/tool/system material and never triggers network requests.
- Assistant Copy uses official small response-action direction: 14pt `doc.on.doc`, clear background, dynamic `.secondaryLabel`, compact 28×28 left-aligned slot. User context Copy remains native.

### List refresh presentation

- Repository list request/reconciliation semantics remain unchanged; `ConversationRepository` is sole authority.
- Right-top refresh and pull-to-refresh are separate presentation sources over the same manual refresh request path.
- Right-top refresh must never begin/resize/change `UIRefreshControl`.
- Genuine pull refresh uses native `UIRefreshControl` spinner and `endRefreshing()` only; no attributed/text title is assigned.
- b28 Runtime disproved the narrower assumption that removing refresh-control attributed text alone fixed the blank band. The b28 source still used `navigationItem.prompt`; prompt changes nav-bar height/adjusted inset.
- **b29 rule**: ordinary refresh/cache status must stay in fixed-height navigation presentation (current implementation uses the title) and must not use `navigationItem.prompt`.
- b27 top contentOffset-normalization workaround remains rejected because Runtime showed the table considered the changed adjusted inset its real top; overscroll was not the root cause.
- Redundant manual trigger while a list load is active must not start a second request; a newly started pull presentation ends promptly.
- With authoritative total present, page-1 reconcile may preserve no more than `max(0, total - authoritativePage.count)` prior off-page items. b26 accepts this for the tested `28/29` sequence; b29 does not change it.

### First-entry / historical scroll

- No valid saved reading anchor => nonanimated latest/bottom placement of the current visible branch.
- Loading/empty placeholder top offset is never adopted as a reading anchor.
- Established A/B semantic anchors remain independent and restore on return.
- Sync/Reload preserve an established anchor only when the same message still exists; missing-anchor-message discard remains an explicit separate path.
- Future response follow-tail remains Phase 9 and must consume authoritative Send/Stream lifecycle rather than being guessed now.

### b29 Runtime acceptance focus

- Enter the same long/stress conversation with no saved local reading anchor: it must appear directly at latest/bottom without visibly scrolling through history.
- Rapidly tap previous/next while motion is active: each tap must advance one semantic answer; the clicked direction must not flip without real drag or boundary; landing should be at intended assistant start and diagnostics must not reproduce b28-scale errors.
- Real drag must immediately regain viewport authority/direction.
- Click right-top refresh repeatedly: first row must remain at ordinary top; adjusted top inset must not grow from navigation prompt height; no persistent blank band.
- Exercise actual pull refresh: native spinner must appear/collapse cleanly with no duplicate request.
- Verify Copy/time/preferences/header remain sane and list `resultCount<=authoritative total` for the known `28/29` sequence.
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

Install/test exact b29 Runtime Artifact `9679291236` / IPA SHA `4378fe9b6a7340ea64a5c82063b0f7e3368e92deaf567d5e0ac40c08055a5360` on the accepted iPhone/iOS17 scope using the b29 matrix above. If any Runtime defect remains, record it first and allocate a fresh unique Candidate before corrected product output. Only after accepted b29 Runtime update docs/evidence, confirm final PR merge-view against current main, merge/close Phase 8 as Stable for the tested scope, then proceed to `DEV-send-stream`.
