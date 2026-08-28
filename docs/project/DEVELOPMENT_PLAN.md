# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b35 Runtime and exact b36 Candidate/CI/Artifact/current-main merge-view evidence._

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
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23 for recorded scope; PR #24.

### Conversation-entry scroll semantics

- First visible presentation with **no valid saved reading anchor** defaults to latest/bottom of the current branch without visibly animating through history.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A.
- Sync/Reload preserve an established resolvable anchor.
- Future active-response follow-tail belongs to Send/Stream and must not pull a user out of intentional history browsing.

## Phase 8 — `DEV-conversation-round-count`

**Active at exact b36 Runtime gate.** Branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable, not merged. Do not claim Stable or merge until exact b36 passes real-device Runtime.

### User-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- one adaptive previous/next round control;
- assistant visible-text Copy + user native context Copy;
- persisted Preferences for round count, message time and round navigation;
- first-entry latest/bottom when no valid saved reading anchor exists;
- evidence-backed list refresh/reconcile presentation corrections without a second list/network owner.

### Shared derivation / navigation contracts

- Round count and navigation share one derived active-branch `ConversationRoundProjection`.
- A visible authoritative user message starts a round. Accepted physical quick-navigation target is the **round-start user-message row**.
- Tool/reasoning/system/internal-recipient nodes do not create ordinary chat rounds/rows.
- Derive rows only when authoritative visible messages change; do not scan all messages in every scroll callback.
- Real user drag controls user intent; programmatic presentation is not user intent.
- Rapid taps advance from the last requested derived target via one transient presentation cursor; real drag clears/replaces that cursor.
- Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll; b33 Runtime accepts the tested physical-bottom path.
- The user's current explicit requirement is one **uniform method for short and long jumps**.
- Current presentation route: direct nonanimated positioning to the semantic target row, capture exact final offset, shift to a direction-consistent lead of about 120pt, then animate only that short final segment for about 0.22s ease-out.
- Do not return to full-distance animated traversal or the old end-correction snap without new exact Runtime evidence.
- b36 removes explicit root/table forced layouts from jump preparation and reuses the existing round button as immediate `定位中` feedback. New `answerJump.positioned` timing tells whether remaining latency belongs to direct positioning itself.
- No speculative debounce, timer, watchdog, retry or row-height cache subsystem.

### Candidate / Runtime history

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25-b30**: partial/failing iterations that established accepted Copy/time/preferences, compact header, bounded list reconciliation, right-top refresh correction and restored automatic self-sizing while exposing navigation defects.
- **b31**: precise user-message round-start landing accepted; remaining hitch/internal-row/Copy issues required correction.
- **b32**: recipient/tool filtering, compact Copy direction and precise semantic landing accepted; long-jump smoothness and physical-bottom direction rejected.
- **b33**: physical-bottom direction and final semantic landing accepted; long-distance movement still gear-like.
- **b34**: Runtime still rejected movement feel although its tested trace had 42 requested / 42 completed jumps, 0 landing corrections and 0 ignored completions. This ruled out the old correction snap as the remaining tested cause.
- **b35**: replaced full-distance traversal with the uniform direct+ease-out route; completed landings were precise but multi-second tap-to-position stalls remained around long-message regions.
- **b36**: exact Code/Static/CI/Artifact/current-main merge-view complete; Runtime pending.

### Exact b35 Runtime evidence

- Candidate `DEV-conversation-round-count-0.1.0-b35`, build `0.1.0 (35)`, exact source `c3addf775483de17a0a0a9eb81d602fc18ebe611`.
- Push Run/Job `33203663621` / `98959137672`; Runtime Artifact `9698781544`; IPA SHA `b1391d06f81bc8c57d124e16a22ef138dd8151e0bd8e338db601729c6f583b0f`.
- Exact real-device trace had 52 `answerJump.requested` / 36 `answerJump.completed`; suspicious gaps around 4s, 10s and 8s appeared near long-message regions.
- Completed jumps report `landingErrorPoints=0.00` and lead distance 120pt; therefore the blocking b35 issue is tap-to-position latency rather than final landing precision.
- Source performed synchronous root/table forced layout around direct `scrollToRow(false)` after the request log, providing the evidence-backed b36 optimization target.
- b35 is Runtime partial/failing and permanently reserved.

### Exact b36 Candidate / evidence

- Candidate `DEV-conversation-round-count-0.1.0-b36`, version/build `0.1.0 (36)`.
- Exact product/config source `8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- Exact product diff from checkpoint parent `c6c21e0f...` is only workflow identity 2+/2-, Xcode identity 4+/4-, and `ConversationFeature.swift` 25+/6-.
- Static source parse passed; audited Swift blob `1a710353cb1864c99dda62c66eb7398c82ed5e64`.
- Removes jump-path `view.layoutIfNeeded()` and pre/post `tableView.layoutIfNeeded()` calls, while retaining UIKit automatic self-sizing generally.
- Reuses the existing quick-navigation button for immediate `定位中` / accessibility `正在定位` presentation; this is not a second state owner.
- Keeps one nonanimated target `scrollToRow(false)` and the same 120pt / 0.22s ease-out finish.
- Adds privacy-safe `answerJump.positioned` timing with `directPositionDurationMs`, `preparationDurationMs`, `targetVisible` and row/role only.
- No row-height cache, network change, rendering change, retry, timer or watchdog.
- Exact push Run/Job `33207505424` / `98972194770`, success.
- Runtime Artifact `9700254733`; ZIP `sha256:718e8500ea41bcc73b41f5bebd9a4850b93246368a87304be0b2c4751702e576`.
- IPA `ChatGPTClient-0.1.0-b36-dev-conversation-round-count.ipa`; SHA `cdf2c7278ec0a4f6f5125a711f78d7bbda8c606a32dda87f614d710f662bd867`.
- Independent package inspection matches `0.1.0 (36)`, Candidate b36, source `8f8614508eef`, iOS14 minimum and arm64.
- Current main remained `a6e3b2bc185b8d5df90b846040387262a64e6154`; PR Run/Job `33207508869` / `98972206567` passed on synthetic merge `e7ff5b368faaea3debbe5d5547c0424996653fa0`, explicitly merging exact b36 source into main.
- Merge-view output is CI evidence only. Runtime must use exact push Artifact `9700254733`.

### b36 Runtime acceptance focus

1. Repeat b35 long-message regions; tap-to-visible positioning should no longer stall for several seconds, or should be materially reduced.
2. If positioning is not immediate, the existing round button must visibly show `定位中` so the tap is never ambiguous.
3. If any stall remains, export diagnostics and use `answerJump.positioned.directPositionDurationMs` / `preparationDurationMs` to determine whether direct `scrollToRow(false)` itself is still the bottleneck.
4. Final semantic landing must remain precise at the intended user-message round start.
5. Rapid taps remain one semantic round per tap; real drag immediately retakes ownership.
6. Physical-bottom direction plus recipient/tool filtering, Copy, first-entry latest, A/B anchors, timestamps/preferences, list reconcile and Sync/Reload remain intact.

If b36 is rejected, record the exact Runtime defect first and allocate b37 or later before corrected product output. Never rebuild b36.

### Rendering scope boundary from supplied recording

The supplied official-app/current-client recording shows the current client displaying raw Markdown syntax for headings, bold text, inline code and tables. It also shows boxed-question-mark glyphs adjacent to raw `filecite ...` marker text.

Current Phase 8 source intentionally has only plain-string presentation: `visibleText(from:)` concatenates `content.text` and string `parts`; `ConversationMessageCell` assigns the resulting string to `UILabel.text`. Therefore:

- Markdown/table/code/list/link rendering is **not** part of Phase 8. It belongs future `DEV-message-rendering`.
- Raw `filecite`/boxed-glyph behavior requires rich citation/annotation parsing/rendering evidence; do not blindly strip it as a font workaround in Phase 8.
- If future protocol evidence shows file citations map to attachment/file-card ownership, coordinate with attachment rendering rather than inventing a second representation.

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

Implement native rich message presentation for Markdown paragraphs/headings/lists/links, emphasis, inline/fenced code, code-block Copy and tables as needed. Also investigate current user-visible rich annotation/citation markers such as the supplied `filecite` example from real protocol content. Preserve authoritative visible text and do not expose hidden reasoning/tool/system content. Avoid full-conversation reparse/reload on every stream token.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted cache owner/store. Prefer list-response preview only when evidenced; otherwise bounded preview comes from Detail/Sync/Reload/Send already obtained through normal activity. Never issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current user-visible branch; never scrape mounted cells or expose hidden internal content.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Do not duplicate Phase 8 quick-navigation ownership after that Work is accepted.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities, each only with current protocol/UI evidence.

## Current next action

Install/test exact b36 Runtime Artifact `9700254733` / IPA SHA `cdf2c7278ec0a4f6f5125a711f78d7bbda8c606a32dda87f614d710f662bd867` on the accepted iPhone/iOS17 scope. If accepted, record Runtime evidence, re-check current main/PR conflicts and merge-view, then merge/close Phase 8 and promote only the tested accepted scope to Stable. If rejected, use b36's `answerJump.positioned` timings to identify the remaining direct-position cost, record the defect first and allocate b37+ before corrected product output.
