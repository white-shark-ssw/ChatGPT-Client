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

### Assistant messages
Use wide readable document-style content without a large enclosing bubble. Later support Markdown/headings/lists/links/code/tables/visible attachments as evidence and roadmap require.

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
- Stream/reasoning state belongs to owning conversation/response lifecycle.
- Sync/reload operate through production conversation owner and do not create second stores/identities.
- A freshness/operation-generation guard may reject obsolete selected-detail results; request-task cancellation/replacement remains lifecycle ownership at the same authoritative repository.
- Export reads authoritative model rather than rendered UI.

## Validation expectations

Distinguish visual/code implementation, CI/build, artifact availability and real-device interaction. b14 compact startup/list-detail navigation is real-device accepted for iPhone/iOS17. Selected-detail cancellation/replacement, future reasoning UI/haptics, composer behavior and round-count behavior still require their own runtime acceptance.

## Maintenance rule

Update this document when the user supplies newer interaction evidence, explicitly changes a preferred interaction, or a real-device implementation proves an intentional compatibility/product deviation.
