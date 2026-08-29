# UI / Interaction Baseline — Native iOS ChatGPT Client

_Last updated: 2026-08-28 through b29 Candidate evidence and b28 Runtime failure._

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

1. **Right-top refresh button** — must stay within fixed-height navigation presentation and must never begin, resize or mutate `UIRefreshControl`.
2. **Pull-to-refresh gesture** — uses native `UIRefreshControl` spinner and `endRefreshing()` only.

Durable Runtime rules:

- b27 showed ordinary top `adjustedInsetTop≈97.67`; after right-button refresh it became `≈131.67` while list data remained correct and the table did not report stranded overscroll. The blank band is therefore presentation/inset height, not missing data.
- b28 removed `UIRefreshControl.attributedTitle`, but the user still reproduced the blank band. Source inspection showed right-button refresh/status still used `navigationItem.prompt`; prompt itself changes navigation-bar height and adjusted top inset. The earlier rule that refresh-control title was the root cause is superseded.
- **Do not use `navigationItem.prompt` for ordinary conversation-list refresh/cache status.** Current b29 implementation uses fixed-height navigation title text instead.
- Do not assign an attributed/text title to `UIRefreshControl`.
- Do not reintroduce b27's contentOffset/top-normalization workaround. Runtime disproved stranded overscroll as the root cause.
- The pull region must visibly show the native spinner while genuinely refreshing and collapse cleanly at completion.
- If a manual list load is already active, reject a redundant trigger without starting a second request. If the redundant trigger came from pull-to-refresh, end that newly started spinner presentation promptly.
- Right-button refresh must leave the first row at the same normal top position; it must not reserve pull-control/prompt height.
- Diagnostics may record refresh source, spinner state, `contentOffset` and adjusted inset, but not conversation titles/IDs.
- Repository reconcile/network semantics are not presentation concerns. b26 real-device accepted the authoritative-total bound for the tested `28/29 -> 29` sequence; b29 leaves it unchanged.

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
- Current implementation uses a **14pt** `doc.on.doc` glyph in a compact **28×28** clear layout slot with `.secondaryLabel` tint.
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
- b28 Runtime explicitly proved this had not been implemented: after loading a 1577-visible-message conversation, the first answer-jump diagnostics began from ordinary top `contentOffsetY≈-97.67`.
- b29 implements nonanimated `.bottom` placement of the final visible message when no valid saved reading anchor exists. Exact Runtime acceptance remains pending.

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
- While a programmatic answer cursor exists and both directions are available, retain the currently clicked direction. Only real drag or boundary can override it.
- At boundaries, the only valid adjacent target wins; with no useful target the control hides.
- No auto-hide timer/watchdog.
- b28 Runtime directly rejected the previous fallback: continuous programmatic taps produced `next -> previous -> next -> previous` without matching real drag because source reused stale `lastUserDragDirection`.

### Rapid tap semantics

b25 proved recomputing from a still-moving viewport can repeat a stale answer target. Correct contract:

- rapid consecutive taps advance from the **last requested derived answer target**;
- the cursor is transient presentation state pointing into existing `answerRows`, never a second semantic index;
- real user drag clears the cursor and re-establishes context from the actual viewport.

b26/b27 diagnostics proved sequential target progression, including `214 -> 221 -> 227`, so semantic cursor/projection is retained.

### Long-conversation scrolling execution

- b27 real-device stress on **1063 visible messages / 2331 mapping nodes** showed sequential targets but noticeable pause/hitch with repeated long-distance `scrollToRow(...animated:true)`.
- b28 switched to interruptible native `setContentOffset(..., animated:true)`, stopping current programmatic motion before rapid retargeting.
- b28 Runtime on a **1577-visible-message** conversation then recorded material target-coordinate drift as self-sizing cells resolved, including examples around `-1950`, `-7330`, and `-11407` pt landing error. Source still used fixed `estimatedRowHeight=96` for unseen rows.
- **b29 execution direction**: keep the same semantic cursor and interruptible native offset animation, but disable the fixed estimated-row geometry and lay out before resolving the target row rect/offset.
- At animation end, compare target vs actual offset; a small nonanimated landing correction remains acceptable when required.
- diagnostics may record target row index, start/target/actual offset and landing error, not message identity/body.

Do **not** use debounce, timer stepping, watchdogs or a speculative full row-height cache. Disabling an evidenced-wrong fixed estimate does not justify a second height-cache authority. A cache may only be considered if exact b29 Runtime still provides evidence requiring it.

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
- b27 retained sequential target semantics but still showed long-conversation animation delay/hitch; right-top refresh inflated adjusted top inset ~34pt despite correct list data; Copy visual too large.
- b28 is **Runtime partial/failing**: long-row target geometry drifted by thousands of points, programmatic direction flipped without drag, first entry remained at top and right-top refresh blank region persisted.
- b29 contains the scoped corrections above and currently has **Code + source/static audit + exact Candidate CI + identity-valid Runtime Artifact + initial PR merge-view CI only. Runtime pending.**

### Focused b29 real-device matrix

- First entry to long conversation with no saved reading anchor: directly latest/bottom, no visible top-to-bottom animation.
- Long conversation: rapid previous/next while motion is active, one semantic target per tap, clicked direction retained unless real drag/boundary, correct answer-start landing, no b28-scale landing error/hitch.
- Real drag: immediately regains viewport/direction authority.
- Right-top refresh: first row stays flush at ordinary top; adjusted top inset does not grow from prompt height; no blank top band.
- Real pull refresh: native spinner appears and collapses cleanly; no persistent blank region or duplicate request.
- List reconcile remains `resultCount<=authoritative total` for known `28/29` sequence.
- Copy/time/preferences/header remain functional/presented correctly.
- A/B independent reading anchors and Sync/Reload answer-anchor rebuild remain sane.
- Basic Dynamic Type/VoiceOver sanity.

## Maintenance rule

Update this document when newer user interaction evidence, explicit preference changes or real-device results intentionally change the baseline. Runtime evidence outranks earlier visual hypotheses.
