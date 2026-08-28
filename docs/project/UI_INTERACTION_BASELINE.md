# UI / Interaction Baseline — Native iOS ChatGPT Client

_Last updated: 2026-08-28 through b28 Candidate evidence._

## Purpose

Durable UI/interaction baseline for the native client, based on user-supplied official ChatGPT iOS recordings/references, explicit requirements and current real-device evidence.

> **Use the official ChatGPT iOS interaction model as the baseline where acceptable; make targeted improvements only for explicit requirements or evidenced pain points.**

This is an interaction/behavior baseline rather than permission to invent unsupported protocol behavior. Prefer native UIKit/system behavior and preserve iOS14 compatibility unless a concrete requirement changes it.

## Global interaction principle

Do not create a second UI language merely to be different from the official App. Prefer official-style navigation, top bar, composer, role presentation, message actions, menus/sheets, loading/error states and later advanced navigation.

## Main chat structure

Minimal chat screen:

- native compact list/detail navigation;
- minimal top bar with current-context title/controls;
- top-right new-chat/overflow patterns as capabilities exist;
- vertically scrolling message region;
- bottom composer once Send is supported.

Do not crowd the top bar with dedicated recovery/export buttons. Ordinary manual recovery lives in the conversation overflow menu.

### Startup sidebar/list usability

On compact iPhone with no selected conversation, the useful startup root is the **conversation list**, not a blank `新对话` secondary placeholder. Opening/revealing navigation must not be what starts the initial list request.

Accepted b14 shell rules:

- cold start reaches conversation-list root after accepted WebKit warm-up;
- no duplicate custom/system sidebar controls;
- UISplitViewController/native navigation is the single compact list/detail navigation owner;
- selecting a conversation enters detail and native Back/system navigation returns to list.

## Conversation header metadata

Real-device official-App comparison establishes:

- conversation title is primary first line;
- type/round metadata is a subdued compact second line;
- supported ordinary-chat path presents `聊天 · N轮` when count is On and `聊天` when Off;
- metadata must not sit above title or create prompt-style extra nav-bar height;
- detail metadata must not use `navigationItem.prompt` as its title owner.

Round count is derived from authoritative active-branch user messages, never a mutable second authority. `工作 · N轮` is only valid once current authoritative Work/Project type evidence exists; never infer `工作` from title/presentation text.

## Sidebar / conversation list

Use an official-style drawer/sidebar/list model rather than a custom tab-heavy system. Prioritize recent conversations, selected state, loading/pagination, settings/account entry and native compact navigation ownership.

### Persistent list / future preview

The accepted b23 cache core supplies an account-scoped persistent summary snapshot behind `ConversationRepository`. Future preview enhancement must reuse that owner/store.

- title remains primary line;
- future preview is one subdued clipped secondary line;
- Dynamic Type may increase row height; do not force clipping fixed heights;
- preview is derived display metadata only;
- never issue one Detail request per row merely to create previews;
- hidden/system/tool/reasoning content is never a preview source;
- future `显示会话消息预览` preference uses centralized `AppPreferences` and triggers no network request.

### List refresh presentation

Manual list refresh is one repository request path with two distinct presentation sources:

1. **Right-top refresh button** — uses the existing navigation prompt/status feedback. It must never begin, resize or mutate `UIRefreshControl` presentation.
2. **Pull-to-refresh gesture** — uses the native `UIRefreshControl` spinner and `endRefreshing()` only.

Durable rules from b27 real-device evidence:

- Do not assign an attributed/text title to `UIRefreshControl`. b27 showed ordinary top `adjustedInsetTop≈97.67`; right-button refresh then produced `≈131.67` while `contentOffsetY` simply followed the new top and `overscrolled=false`. The extra ~34pt blank band was therefore refresh-control/inset presentation, not missing list data.
- Do not reintroduce b27's contentOffset/top-normalization workaround for this defect. Runtime disproved stranded overscroll as the root cause.
- The pull region must visibly show the native spinner while genuinely refreshing and collapse cleanly at completion.
- If a manual list load is already active, reject a redundant trigger without starting a second request. If the redundant trigger came from pull-to-refresh, end that newly started spinner presentation promptly.
- Right-button refresh must leave the first row at the same normal top position; it must not reserve pull-control height.
- Successful/failed manual refresh continues to use existing navigation feedback (`正在刷新会话列表…`, success count, retained-cache failure).
- Diagnostics may record refresh source, spinner state, `contentOffset` and adjusted inset, but not conversation titles/IDs.
- Repository reconcile/network semantics are not presentation concerns. b26 real-device accepted the authoritative-total bound for the tested `28/29 -> 29` sequence; b28 leaves it unchanged.

## Conversation messages

### User messages

Use compact rounded bubble/background treatment similar to official App. When message-time display is enabled, show subdued timestamp **above** the bubble aligned to the user side. Timestamp is presentation metadata, not body/identity/Copy content.

### Assistant messages

Use wide readable document-style content without a large enclosing bubble. When message-time display is enabled, show subdued timestamp **above** the assistant response aligned to the assistant/document side. Reasoning/status rows do not become independent assistant messages unless the authoritative model says so.

### Timestamp source

- Historical/server-backed messages use authoritative `createTime` / service `create_time` already present in the model; do not refetch solely for timestamps.
- Use current locale/time zone.
- Same-day may show time only; older messages include date context.
- Missing authoritative historical timestamp is omitted rather than fabricated.
- Future optimistic Send may use provisional local time only if authoritative response ownership requires it, and must hand off once server time exists.

## Message actions / Copy

Copy is a required daily-use interaction.

### Assistant Copy

- Visible assistant text exposes Copy in the response quick-action area.
- User explicitly requires this treatment to visually match the official ChatGPT iOS action scale rather than merely be generically “official-style”.
- Baseline: small outline `doc.on.doc`-style glyph, no emphasized button background, subdued dynamic system tint, left aligned with assistant content and compact action-row spacing.
- b27's 17pt glyph / 36×32 slot remained visibly too large in real-device recording.
- b28 uses a **14pt** `doc.on.doc` glyph in a compact **28×28** clear layout slot with `.secondaryLabel` tint. This exact size is current implementation direction, not yet Runtime-accepted until exact b28 is tested.
- Do not add unrelated official-App actions merely to fill the row before their functionality exists.

### User Copy

Visible user messages expose Copy through the native context action surface without requiring manual text selection.

### Copy semantics

- Copy authoritative **user-visible** text only.
- Hidden reasoning/tool/system material is never copied merely because it exists in protocol data.
- Use system pasteboard; no message mutation/network request.
- Compact immediate feedback such as `已复制` is acceptable.
- Future code-block scoped Copy must copy code block content while retaining whole-message Copy unless explicitly changed later.

## Conversation entry / reading position

Official-style default is **latest-message first**, while an established per-conversation reading anchor is preserved.

### First entry with no local reading anchor

- Present latest/bottom of current visible branch by default.
- Loading/empty placeholder position is not a reading anchor.
- A long conversation should appear at final placement without visibly animating from top through history.
- Hidden-completed Detail shown first time with no anchor follows the same rule.

### Return to already-read conversation

- Once A has a real semantic anchor, A -> B -> A restores A.
- B owns its independent anchor; scrolling/jumping B must not mutate A.
- Sync/Reload/current-branch replacement preserves an established anchor when the same anchored message remains.
- If replacement removes the anchor message, discard explicitly rather than converting arbitrary raw offset into a new semantic anchor.

### Future stream follow-tail

When authoritative Send/Stream exists:

- near-latest user may follow new streamed content naturally;
- deliberate upward history browsing exits follow-tail and must not be stolen back;
- navigating away does not cancel hidden conversation response merely because viewport changed;
- exact response/follow-tail state belongs to `DEV-send-stream`.

## Quick previous / next answer navigation

User-required long-conversation enhancement, optional via settings.

### Semantic target

- `上一轮回答` / `下一轮回答` navigate by derived round answer anchors, not pixel percentages.
- A round begins at an authoritative visible user message; its answer anchor is the first visible assistant reply before the next user message.
- Tool/reasoning/system nodes do not become rounds; a missing assistant reply gets no fabricated anchor.
- Header round count and answer navigation share the same `ConversationRoundProjection`.

### Button design

Use **one adaptive floating button**, not two permanent large controls.

- trailing safe-area region, about 12–16pt inward;
- about 12–16pt above bottom/composer area;
- compact circular/material-like visual, with at least 44pt effective tap target;
- compatible SF Symbol arrow/chevron;
- subtle system background/shadow only as needed;
- VoiceOver label exposes full action `上一轮回答` / `下一轮回答`.

### Direction behavior

- Real user drag toward older content => previous/up state.
- Real user drag toward newer content => next/down state.
- Programmatic movement is not user intent and must not flip direction merely because content moved.
- At boundaries, the only valid adjacent target wins; with no useful target the control hides.
- No auto-hide timer/watchdog.

### Rapid tap semantics

b25 proved recomputing from a still-moving viewport can repeat a stale answer target. Correct contract:

- rapid consecutive taps advance from the **last requested derived answer target**;
- the cursor is transient presentation state pointing into existing `answerRows`, never a second semantic index;
- real user drag clears the cursor and re-establishes context from the actual viewport.

b26/b27 diagnostics prove sequential target progression, including `214 -> 221 -> 227`, so semantic cursor/projection is retained.

### b28 scrolling execution

b27 real-device stress on **1063 visible messages / 2331 mapping nodes** showed sequential targets but still had a noticeable pause after tap and non-uniform/hitching movement. Per-frame answer-button recomputation had already been removed, so b28 changes only the execution path:

- resolve the intended derived assistant row start;
- lay out the table as needed and compute that row's valid content offset;
- use native `setContentOffset(..., animated:true)` for spatial continuity;
- if another answer tap arrives while programmatic motion is active, first stop the old animation **at the current visible offset**, then immediately target the next derived answer;
- a real drag interrupts/clears programmatic state and takes priority;
- at animation end, compare target vs actual offset; a small nonanimated landing correction is allowed if necessary;
- diagnostics may record target row index, start/target/actual offset and landing error, not message identity/body.

Do **not** use debounce, timer stepping, watchdogs or a speculative full row-height cache. A height-cache subsystem may only be considered if exact b28 Runtime still provides evidence that self-sizing layout cost is the remaining bottleneck.

For long conversations, keep the lightweight derived answer-row projection updated only when authoritative messages change; never rescan all messages on every `scrollViewDidScroll`.

### Multi-conversation / Sync / Reload

- Quick navigation uses the existing conversation presentation owner; no competing saved-scroll authority.
- Using it in B never mutates A's saved anchor.
- Sync/Reload/current-branch replacement re-derives answer anchors from authoritative messages; stale row indexes are not identity.
- Preference toggle changes presentation only.

## Composer / attachments / files

Once Send exists, follow official rounded multiline composer with supported attachment/tool entry, send affordance and exact Stop behavior from authoritative response state. Do not preload unsupported tools.

After text Send/Stream acceptance, attachment support is high priority:

- native Photos/PHPicker and document picker;
- per-conversation pending attachment cards/removal;
- evidence upload protocol before implementation;
- assistant file card -> explicit download -> app-private local file -> immediate `UIActivityViewController`;
- visible failure + explicit retry only; no automatic retry loop;
- full custom download manager is later and must not block basic tap-download-share.

## Reasoning / haptics

When protocol supplies user-visible reasoning status/detail, use subdued status, expandable visible detail and a completed static state where duration is actually available. Never manufacture hidden chain-of-thought. Required two short haptic pulses occur on the real reasoning->final lifecycle transition, not cell redraw.

## Manual recovery

- `同步最新消息` and `重载当前会话` remain explicit user recovery through `ConversationRepository`.
- Available during ordinary initial Detail loading where accepted.
- Never resend/regenerate or become automatic retry machinery.
- Replacement of an in-flight same-target Detail request follows accepted cancel-before-replacement + generation/freshness rules.

## Loading / error / menus

Use compact native states. Terminal failure stops indefinite spinner and exposes concise recovery. A valid cached list is useful content; refresh failure may retain it with separate feedback. Prefer native menus/sheets/context menus compatible with iOS14. Destructive actions use standard destructive presentation.

## Visual direction

- Native iOS feel.
- System font/SF Symbols where available.
- Light/Dark follows dynamic system colors.
- Moderate density similar to official App.
- Do not raise deployment target for decoration.

## State ownership requirements

UI is a consumer of authoritative state.

- Titles/text are not identity.
- `ConversationRepository` remains sole conversation/list authority.
- Persistent list cache is a scope-bound storage snapshot behind the repository, not another list owner.
- Round count/answer anchors are derived presentation data.
- Message time is derived from authoritative message time where present; toggle is preference state only.
- Copy reads authoritative visible content.
- First-entry latest placement and return-anchor restoration belong to one per-conversation presentation owner.
- Rapid answer-target cursor and answer animation state are transient UI state only.
- Stream/reasoning lifecycle belongs to future per-conversation response owner.
- Pending outgoing attachments belong to owning conversation draft; incoming download state belongs to owning attachment identity.
- Export reads authoritative model, not mounted cells.

## Current validation expectations

- b14 compact startup/navigation real-device accepted.
- b25 accepted Copy function/time/preferences but rejected header/jump/refresh and exposed `30/29` list issue.
- b26 accepted compact header, sequential answer targets and bounded `29/29`; smoothness/Copy/refresh presentation still failed.
- b27 exact real-device evidence retained sequential target semantics but still showed long-conversation animation delay/hitch; proved right-top refresh inflated adjusted top inset ~34pt despite correct list data; rejected Copy visual as too large.
- b28 contains the scoped corrections above and currently has **Code + source/static audit + exact Candidate CI + identity-valid Runtime Artifact + initial PR merge-view CI only. Runtime pending.**

### Focused b28 real-device matrix

- Long conversation: rapid previous/next while motion is active, prompt start, smooth continuity, one semantic target per tap, correct answer-start landing, real-drag interruption.
- Right-top refresh: first row stays flush at ordinary top; adjusted top inset does not reproduce b27 ~97.67→131.67 growth.
- Real pull refresh: native spinner appears and collapses cleanly; no persistent blank region or duplicate request.
- List reconcile remains `resultCount<=authoritative total` for the known `28/29` sequence.
- Copy: smaller official-scale assistant glyph in Light/Dark, functional visible-text clipboard; user context Copy remains functional.
- Timestamps remain above both roles.
- A/B independent reading anchors and Sync/Reload answer-anchor rebuild remain sane.
- Basic Dynamic Type/VoiceOver sanity.

## Maintenance rule

Update this document when newer user interaction evidence, explicit preference changes or real-device results intentionally change the baseline. Runtime evidence outranks earlier visual hypotheses.
