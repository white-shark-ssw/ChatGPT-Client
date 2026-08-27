# UI / Interaction Baseline — Native iOS ChatGPT Client

_Last updated: 2026-08-27._

## Purpose

This document is the durable UI/interaction baseline for the native client. It is based on the user's current official ChatGPT iOS usage recordings plus explicit user requirements and current real-device evidence.

The default product rule is:

> **Use the official ChatGPT iOS interaction model as the baseline where it is acceptable; make targeted improvements only for explicit requirements or evidenced pain points.**

This is an interaction/behavior baseline, not a requirement for pixel-perfect copying. Use native UIKit/system behavior where practical and preserve iOS14 compatibility unless a concrete requirement justifies a higher API.

## Global interaction principle

Do not invent a second UI language merely to be different from the official App. Prefer official-style patterns for sidebar/navigation, conversation top bar/overflow, composer, role presentation, message actions, menus/sheets, loading/error states and later advanced navigation.

## Main chat structure

The minimal chat screen uses:

- native compact list/detail navigation;
- minimal top bar with current-context title/controls;
- top-right new-chat / overflow actions following the official pattern;
- vertically scrolling message region;
- bottom composer when send becomes supported.

Do not crowd the top bar with dedicated recovery/export buttons. Put ordinary manual recovery in the conversation overflow menu.

### Startup sidebar/list usability

On compact iPhone with no selected conversation, the useful startup root is the **conversation list**, not a blank secondary `新对话` placeholder. Opening/revealing a sidebar must not be what starts the initial list request.

b14 real-device acceptance establishes the current native interaction baseline for the tested iPhone/iOS17 scope:

- cold start reaches the conversation-list root after the accepted WebKit warm-up;
- no duplicate custom/system sidebar controls;
- UISplitViewController/native navigation is the single compact list/detail navigation owner;
- selecting a conversation enters detail and native Back/system navigation returns to the list.

Do not reintroduce a second custom compact sidebar button on top of UISplitViewController navigation.

## Conversation header metadata

The conversation title remains primary top-bar text. The existing second-line conversation type (`聊天` or `工作`) is the metadata row.

The project adds optional conversation round count to the right in a future Work:

- `聊天 · 23轮`
- `工作 · 23轮`

Round count is derived presentation data from authoritative active-branch user messages, never a second mutable authority.

## Sidebar / conversation navigation

Use the official-style drawer/sidebar/list model rather than a custom tab-heavy system. Prioritize recent conversations, selected state, loading/pagination, settings/account entry and native compact navigation ownership.

## Conversation messages

### User messages
Use a compact rounded bubble/background treatment similar to the official App.

When `显示消息时间` is enabled, show subdued timestamp metadata below each visible user bubble, aligned to the user-message side. The timestamp is not part of the message body and must not change message identity or copying/export semantics.

### Assistant messages
Use wide readable document-style content without a large enclosing bubble. Later support Markdown/headings/lists/links/code/tables/visible attachments as evidence and roadmap require.

When `显示消息时间` is enabled, show subdued timestamp metadata below each visible assistant response, aligned to the assistant/document side. Reasoning/status rows are not independent assistant messages merely because they are visible UI; timestamp ownership follows the actual visible assistant message model supplied by the service/response owner.

### Message timestamp source and formatting

- Historical/server-backed messages use the authoritative message `createTime` / service `create_time` already present in the conversation model; do not refetch Detail solely for timestamps.
- Use the device's current locale and time zone.
- Same-day messages may use time-only; older messages include enough date context to avoid ambiguity. Exact localized formatting/spacing is implementation-level and should be tuned on real device without raising the deployment target.
- If a historical message has no authoritative timestamp, omit the metadata rather than fabricate a current time.
- Future optimistic Send presentation may temporarily show a provisional local timestamp only if the authoritative response/message owner needs it; once server-backed time exists, the display must hand off to that authoritative value rather than keep a second durable timestamp authority.

## Quick previous / next answer navigation

This is a user-required long-conversation enhancement and is optional through settings.

### Semantic target

- `上一轮回答` / `下一轮回答` navigate by derived **round answer anchors**, not raw pixel percentages.
- A round begins at an authoritative visible user message. Its historical answer anchor is the first visible assistant reply after that user message and before the next visible user message.
- Multiple tool/reasoning/system nodes do not independently become “rounds”. A missing historical assistant reply does not get a fabricated anchor.
- The same derived round projection should support header round count and answer navigation, avoiding parallel mutable indexes.

### Button design and placement

Use **one adaptive floating button**, not two large always-visible controls.

Recommended compact-iPhone placement:

- trailing edge of the conversation viewport;
- approximately 12–16 pt inside the trailing safe area;
- approximately 12–16 pt above the composer when a composer is present;
- before Send/Composer exists, use the bottom safe-area region as the lower anchor;
- when the keyboard/composer moves, the button moves with that layout so it never sits underneath the composer.

Visual direction:

- compact circular/material-like control, roughly 36–40 pt visible size with at least a 44 pt effective tap target;
- SF Symbol chevron/arrow compatible with the iOS14 deployment target;
- subtle system/material background, light shadow/border only as needed for readability over message content;
- no large text pill permanently covering the document area;
- VoiceOver/accessibility label is the full action (`上一轮回答` or `下一轮回答`) even if the visible control is icon-only.

### Direction behavior

The control follows the user's latest **real drag direction**:

- user browses toward older content -> upward state / `上一轮回答`;
- user browses toward newer content -> downward state / `下一轮回答`.

Important boundaries:

- Programmatic animated scrolling caused by the button is not a user drag and must not immediately reverse the control's semantic direction.
- If only one adjacent answer target is valid at the current boundary, show that valid direction even if the previous user-drag direction pointed the other way.
- If no useful adjacent answer exists (for example too few answer anchors), hide the control.
- Do not require an auto-hide timer; visibility/direction should be deterministic from preference, current conversation/anchor availability and user drag intent.

A short native cross-fade/symbol transition when the direction changes is acceptable, but direction must be event-driven rather than timer/watchdog-driven.

### Tap / scrolling behavior

Tapping must produce visible spatial continuity:

- resolve the adjacent answer anchor in the chosen direction from the current visible round context;
- scroll the existing `UITableView`/`UIScrollView` to that assistant-answer start with native animation;
- position the answer start with a modest readable top inset below the navigation area;
- do **not** instantly teleport to a final raw offset;
- do **not** fake a long jump with timer-stepped offsets;
- a user touch/drag may naturally interrupt the animation and takes priority.

For long conversations, derive/store the lightweight answer-row/index projection when message data changes. Do not scan all messages during every `scrollViewDidScroll` callback.

### Multi-conversation and refresh interaction

- Quick navigation consumes the current conversation's existing presentation/scroll owner; it does not create a second saved-scroll authority.
- Using the control in B must never mutate A's semantic scroll anchor.
- After Sync/Reload/current-branch replacement, answer anchors are re-derived from authoritative visible messages; stale row indexes are not retained as identity.
- The setting toggle hides/shows only the navigation presentation; it does not change message data or resident conversation state.

### Future active-response interaction

The first implementation may navigate server-backed/current visible branch answers before Send/Stream exists.

Once an authoritative response lifecycle exists:

- switching/jumping to an older round must never Stop or cancel a still-generating response merely because it is no longer visible;
- active-response/follow-tail behavior is owned by the per-conversation Send/Stream lifecycle, not by this floating button;
- programmatic jump animation must not masquerade as a user's manual follow-tail/exit-follow-tail gesture.

Exact active-response “jump to newest” behavior should be validated with the real Send/Stream owner rather than guessed in the read-only phase.

## Composer

Follow the official model: rounded composer, multiline growth, leading attachment/tool entry when supported, send affordance when valid, and stop control while an evidenced response is active. Do not preload unsupported future tools.

## Reasoning / thinking interaction

When current protocol supplies user-visible reasoning status/detail:

- active state uses subdued gray status plus an iOS14-compatible shimmer/flowing-light treatment;
- user-visible detail may expand/collapse;
- completed state becomes static only when duration is actually available;
- never manufacture or expose hidden chain-of-thought.

### Reasoning-to-final haptic

Emit the user-required two short haptic pulses on the real lifecycle transition from reasoning to final answer. Trigger from response lifecycle, not cell redraw; exact feel requires real-device tuning.

## Manual recovery enhancements

### `同步最新消息`

- available whenever an authoritative selected conversation identity exists, including during ordinary initial detail loading;
- explicit user-triggered recovery through the authoritative conversation owner;
- never resend/regenerate or enter an automatic retry loop;
- accepted centered feedback: `正在同步最新消息…`, then `已是最新` or `已同步最新消息` for about 2 seconds.

### `重载当前会话`

- terminal load-error UI provides direct `重新加载`;
- overflow reload remains available during ordinary initial detail loading;
- rebuilds from current server detail through the authoritative owner;
- never resends existing messages.

### Recovery-during-load request lifecycle

b13 runtime proved that generation-based stale-result rejection works, but also exposed HTTP429 when a manual recovery starts a replacement detail request while the older selected-detail network request is still active.

Current interaction contract therefore requires the authoritative owner to **cancel/replace the older selected-detail request before starting the explicit manual replacement request**, while retaining stale-generation rejection for late callbacks. This is explicit user recovery, not automatic retry machinery.

## Markdown export enhancement

`导出 Markdown` is our enhancement, not official-App behavior. Export authoritative current user-visible branch data rather than mounted cells; never expose hidden/internal reasoning/tool content.

## Loading / empty / error states

Use compact native official-style states.

- Initial/current conversation loading may show centered/system-style progress.
- Manual recovery remains reachable during ordinary detail loading.
- Terminal failure stops indefinite visual spinning and presents concise failure state with direct reload.
- Empty/new-chat state remains simple.
- Preserve original error evidence instead of hiding repeated failures behind silent retries.

## Menus and sheets

Prefer native UIKit/system menus/sheets/context menus compatible with deployment target. Conversation overflow reserves natural positions for recovery and future actions; destructive actions use standard destructive presentation.

## Visual direction

- Native iOS feel.
- System font/SF Symbols where available.
- Light/Dark support following system/application appearance policy.
- Moderate density similar to official App.
- Do not raise deployment target for decoration.

## State ownership requirements

UI remains a consumer of authoritative state.

- Conversation title/text is not identity.
- Selected conversation has one production owner.
- Round count is derived from authoritative active branch.
- Message timestamp display is derived from the authoritative message timestamp where available; the display toggle is preference state, not message state.
- Answer-jump anchors are a lightweight derived presentation index over the authoritative visible active branch; they are not message/conversation identity and are rebuilt after authoritative message projection changes.
- Per-conversation semantic scroll state remains owned by the existing conversation presentation owner; quick navigation cannot introduce a competing saved-offset store.
- Stream/reasoning state belongs to owning conversation/response lifecycle.
- Sync/reload operate through production conversation owner and do not create second stores/identities.
- A freshness/operation-generation guard may reject obsolete selected-detail results; request-task cancellation/replacement remains lifecycle ownership at the same authoritative repository.
- Export reads authoritative model rather than rendered UI.

## Validation expectations

Distinguish visual/code implementation, CI/build, artifact availability and real-device interaction. b14 compact startup/list-detail navigation is real-device accepted for iPhone/iOS17. Selected-detail cancellation/replacement, future reasoning UI/haptics, composer behavior, round-count behavior, message-timestamp behavior and adaptive answer-jump behavior require their own runtime acceptance as applicable.

For answer navigation, real-device validation should include a long conversation, repeated upward/downward direction changes, first/last-boundary behavior, A/B independent scroll anchors, Sync/Reload anchor rebuild, keyboard/composer coexistence when available, and confirmation that jumps visibly animate rather than teleport.

## Maintenance rule

Update this document when the user supplies newer interaction evidence, explicitly changes a preferred interaction, or a real-device implementation proves an intentional compatibility/product deviation.
