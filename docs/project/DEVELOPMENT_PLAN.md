# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b33 Runtime result._

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

**Active after exact b33 Runtime partial/failure.** Branch `dev/conversation-round-count-20260828`; PR #27 open/mergeable. Do not merge/close or claim Stable until a corrected Candidate passes real-device Runtime.

### User-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- one adaptive previous/next round control;
- assistant visible-text Copy + user native context Copy;
- persisted Preferences for round count, message time and round navigation;
- first-entry latest/bottom when no valid saved reading anchor exists;
- evidence-backed list refresh/reconcile presentation corrections without a second list/network owner.

### Shared derivation / round navigation contracts

- Round count and navigation share one derived active-branch `ConversationRoundProjection`.
- A visible authoritative user message starts a round. Accepted physical quick-navigation target is the **round-start user-message row**.
- Tool/reasoning/system/internal-recipient nodes do not create ordinary chat rounds/rows.
- Derive rows only when authoritative visible messages change; do not scan all messages in every scroll callback.
- Real user drag controls user intent; programmatic motion is not user intent.
- Rapid taps advance from the last requested derived round target via one transient presentation cursor; real drag clears/replaces that cursor.
- Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll; exact b33 Runtime accepts this for the tested physical-bottom path.
- Native animated `scrollToRow(..., .top, animated:true)` remains the movement owner unless stronger Runtime evidence justifies a different native strategy.
- No debounce, timer, watchdog or speculative row-height cache subsystem.

### Candidate / Runtime history

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25-b30**: partial/failing iterations that established accepted Copy/time/preferences, compact header, bounded list reconciliation, right-top refresh correction and restored automatic self-sizing while exposing navigation defects.
- **b31**: precise user-message round-start landing accepted; remaining hitch/internal-row/Copy issues required correction.
- **b32**: Runtime partial/failing. Recipient/tool filtering, compact Copy direction and precise semantic landing accepted; long-jump smoothness and physical-bottom rubber-band direction rejected.
- **b33**: Runtime partial/failing. Physical-bottom direction and final semantic landing accepted; long-distance smoothness still rejected.

### Exact b33 Runtime evidence

- Candidate `DEV-conversation-round-count-0.1.0-b33`, version/build `0.1.0 (33)`, exact source `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- Exact push Run / Job `33195740528` / `98932282377`, Runtime Artifact `9695669835`, IPA SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`.
- User accepts physical-bottom/rubber-band direction and final user-round precision.
- User rejects long-distance movement as not sufficiently smooth / gear-like.
- Diagnostics show 74 completed jumps and 14 end corrections. Ordinary corrections include roughly 66.67–504pt; rapid retargeting produced extreme native errors before correction up to about 8258.67pt while final corrected error returned to ~0.
- Therefore b33 is not Stable; b33 identity is permanently reserved.

### b34 evidence-backed direction

`DEV-conversation-round-count-0.1.0-b34` / `0.1.0 (34)` is the next reserved corrected identity; no b34 product output exists yet.

Current b33 retarget path cancels the older animation nonanimated, assigns a new current target, then starts another native animated row scroll. `scrollViewDidEndScrollingAnimation` has no target identity and currently corrects against whatever target is current when the callback arrives. The rapid-retarget trace strongly supports stale/cancelled completion callbacks being able to act on a newer target.

Minimal b34 correction:

- before applying the existing >1pt end correction, require that the **current target row is visible**;
- if it is not visible, treat this callback as stale/superseded presentation completion, emit a privacy-safe ignored-completion diagnostic and do not snap/correct or clear current target ownership;
- when the current target is visible, retain the existing landing measurement/correction path so final semantic precision remains protected.

Do not alter b33-accepted physical-bottom direction, semantic user-row derivation, b32 recipient filter, Copy/timestamps/preferences/header, list/cache/network semantics or state ownership.

### Rendering scope boundary from supplied recording

The supplied official-app/current-client recording shows the current client displaying raw Markdown syntax for headings, bold text, inline code and tables. It also shows boxed-question-mark glyphs adjacent to raw `filecite ...` marker text.

Current Phase 8 source intentionally has only plain-string presentation: `visibleText(from:)` concatenates `content.text` and string `parts`; `ConversationMessageCell` assigns the resulting string to `UILabel.text`. Therefore:

- Markdown/table/code/list/link rendering is **not** part of Phase 8. It belongs Phase 11 `DEV-message-rendering`.
- Raw `filecite`/boxed-glyph behavior appears to require rich citation/annotation parsing/rendering evidence; do not blindly strip it as a font workaround in Phase 8.
- If future protocol evidence shows file citations map to attachment/file-card ownership, coordinate with Phase 10 attachment rendering rather than inventing a second representation.

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

Measure network / parse-model / first-visible-render / Markdown-layout timing and optimize only evidenced bottlenecks.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities, each only with current protocol/UI evidence.

## Current next action

Do not rebuild b33. Produce the smallest b34 product/config change described above, run exact source audit + push CI/Artifact + current-main PR merge-view, verify b34 package identity, then real-device test long-distance/rapid round navigation with special attention to whether stale-completion snaps disappear while final precision and b33 physical-bottom direction remain intact.