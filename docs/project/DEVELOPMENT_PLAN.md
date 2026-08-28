# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-28 through b30 Candidate evidence and b29 Runtime failure._

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
- **V0.1 cache-use increment**: account-scoped persistent list snapshot and rapid-relaunch suppression.
- **V0.2 chat-use**: stable multi-conversation ownership + metadata/preferences + Copy + answer navigation + text Send/new conversation + stream/stop/reasoning/haptics.
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
- b28 proved no-anchor latest had not actually been implemented. b29 added the current nonanimated latest path, but b29's broken row layout prevents honest visual acceptance; b30 must retest after message layout is normal.

## Phase 8 — `DEV-conversation-round-count`

**Active at b30 Runtime gate.** Branch `dev/conversation-round-count-20260828`; PR #27 open. Do not merge/close or claim Stable until exact b30 passes real-device Runtime.

### Candidate history

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25**: Runtime partial/failing. Copy/time/preferences accepted; header, rapid jump and refresh presentation rejected; authoritative `total=29` but result 30 exposed.
- Post-b25 source-fix output reused b25 identity before b26 allocation; permanently invalid for testing.
- **b26**: Runtime partial/failing. Accepted cold `30 -> 29` authoritative-total bound plus repeated `29/29`, sequential rapid answer targets and compact title-first header.
- **b27**: Runtime partial/failing. 1063-message stress run retained sequential target semantics but jump still paused/hitched; right-top refresh changed adjusted top inset ~97.67 -> 131.67; Copy visual rejected as too large.
- **b28**: Runtime partial/failing. 1577-message run recorded answer landing drift of thousands of points, programmatic direction flips without drag, first entry at top and continued refresh blank band.
- **b29**: Runtime partial/failing. **Accepted**: right-top refresh no longer leaves the blank top region; normal adjusted inset remains stable and known list reconciliation remains `28/29 -> 29`. **Rejected**: setting `estimatedRowHeight=0` caused severe self-sizing message-row deformation/invisible body content even though Detail parsing still returned hundreds/thousands of visible messages. Because rows are broken, b29 cannot accept jump or first-entry visual behavior.
- **Current b30**: Candidate `DEV-conversation-round-count-0.1.0-b30`, `0.1.0 (30)`, exact source `a091327508d8393822784bb286245aff64c028a8`. Push Run `33160005440` / Job `98811893174` success; Runtime Artifact `9681236213`; IPA SHA `91f5ee21e904fbe66932e306b7184dc645f33006e5bb10c33f8b3e3b22639db9`; ZIP `sha256:18de824c977fc825f041a6ae1e38974011f92888c6a7ba1eb38fb155f5ecd52f`. Initial PR merge-view Run `33160008270` / Job `98811903542` success on merge `fe7eb9f15bd06279338d96b5628f9873f813968d`. Runtime pending.

### User-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- one adaptive previous/next answer control;
- assistant visible-text Copy + user native context Copy;
- persisted Preferences for round count, message time and quick answer navigation;
- first-entry latest/bottom when no valid saved reading anchor exists.

### Header/type rule

Real-device comparison establishes title-first compact hierarchy. Current ordinary-chat detail may show `聊天 · N轮` / `聊天`. `工作` remains deferred until authoritative Work/Project type evidence exists.

### Preferences

- `显示会话轮数`: On by default.
- `显示消息时间`: On by default.
- `显示回答快速跳转`: On by default.

One `AppPreferences` owner persists all three. Toggling presentation must not mutate conversation state or issue requests.

### Shared derivation / answer navigation

- Round count and answer navigation share one derived active-branch `ConversationRoundProjection`.
- A visible user message starts a round; first visible assistant before the next visible user is the answer anchor. Tool/reasoning/system nodes do not create rounds.
- Derive answer rows only when authoritative visible messages change; do not scan all messages in every scroll callback.
- Real user drag controls semantic direction; programmatic motion is not user intent.
- Rapid taps advance from the last requested derived answer target via a transient presentation cursor; a real drag clears the cursor.
- b26/b27 retained sequential target progression.
- b27 disproved repeated long-distance `scrollToRow(...animated:true)` as sufficiently smooth.
- b28 disproved fixed 96pt estimated self-sizing geometry for precise long-distance target offsets.
- **b29 then disproved `estimatedRowHeight=0` for this self-sizing message table** because the rows themselves collapsed/deformed. Do not retain this optimization.
- **b30 layout contract**: keep `rowHeight = UITableView.automaticDimension` and restore `estimatedRowHeight = UITableView.automaticDimension`. This correction restores ordinary UIKit self-sizing behavior only; it does not prove answer-jump accuracy/smoothness.
- Current clicked programmatic direction remains retained while both directions are valid; only real drag or boundary may change it.
- No debounce, timer, watchdog or speculative height-cache subsystem. Add a broader caching strategy only with new exact Runtime evidence.

### Timestamp / Copy

- Historical timestamps remain authoritative `createTime` and appear above their owning visible messages; missing time is omitted.
- Copy never includes hidden reasoning/tool/system material and never triggers network requests.
- User supplied an official ChatGPT iOS screenshot specifically pointing to Copy. On the 430pt @3x reference, measured Copy glyph bounds are about **14.7pt**. Current b30 retains **14pt regular `doc.on.doc`**, clear background, dynamic `.secondaryLabel`, left alignment and compact invisible layout slot. Do not arbitrarily shrink it to compensate for b29's broken rows; judge final visual scale only under restored normal b30 layout.

### List refresh presentation

- Repository request/reconciliation semantics remain unchanged; `ConversationRepository` is sole authority.
- Right-top refresh and pull-to-refresh are separate presentation sources over the same manual refresh request path.
- Right-top refresh must never begin/resize/change `UIRefreshControl` and must not use `navigationItem.prompt`.
- Genuine pull uses native spinner + `endRefreshing()` only; no attributed/text title.
- b29 Runtime accepts the tested right-top fix: first row no longer gets the persistent blank band and adjusted top inset remains at the ordinary value.
- b27 contentOffset-normalization workaround remains rejected.
- With authoritative total present, page-1 reconcile preserves no more than `max(0, total - authoritativePage.count)` prior off-page items. b26 accepts this for the known `28/29` sequence; unchanged in b30.

### First-entry / historical scroll

- No valid saved reading anchor => nonanimated latest/bottom placement of the current visible branch.
- Loading/empty placeholder top offset is never adopted as a reading anchor.
- Established A/B semantic anchors remain independent and restore on return.
- Sync/Reload preserve an established anchor only while the same message exists.
- b29 source contains the latest-placement correction, but b29's deformed rows prevent visual acceptance; b30 must retest it.
- Future response follow-tail remains Phase 9 and must consume authoritative Send/Stream lifecycle.

### b30 Runtime acceptance focus

1. **First gate: message-row integrity.** Open normal and long conversations and confirm user bubbles, assistant text, timestamps, Copy rows and row heights are all visually normal; no collapsed bars/large blank rows/invisible body.
2. Confirm b29-accepted right-top list refresh blank-region fix remains intact; known list `resultCount` stays <= authoritative total.
3. Compare assistant Copy directly with the supplied official screenshot: small ~15pt gray outline glyph, no visible button block, aligned with response actions; verify Light/Dark dynamic tint and copy function.
4. Only after row integrity passes, test no-anchor first entry directly at latest/bottom.
5. Only after row integrity passes, retest rapid previous/next answer navigation for semantic target accuracy, clicked-direction retention, start/mid-animation hitch and landing correctness.
6. Real drag must regain viewport/direction authority.
7. Retain A/B semantic anchors, Sync/Reload behavior, time/preferences/header and basic Dynamic Type/VoiceOver sanity.

## Phase 9 — `DEV-send-stream`

After Phase 8 acceptance, evidence current text Send/new-conversation/stream/stop protocol and implement composer, pending-to-authoritative identity handoff, per-conversation response lifecycle, incremental stream UI, Stop, visible reasoning and required haptics.

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

Install/test exact b30 Runtime Artifact `9681236213` / IPA SHA `91f5ee21e904fbe66932e306b7184dc645f33006e5bb10c33f8b3e3b22639db9` on the accepted iPhone/iOS17 scope using the b30 matrix above. If a Runtime defect remains, record it first and allocate a fresh Candidate before corrected product output. Only after accepted Runtime, synchronize final PR merge-view against current main, merge/close Phase 8 as Stable for the tested scope, then proceed to `DEV-send-stream`.
