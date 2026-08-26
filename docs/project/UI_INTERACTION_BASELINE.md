# UI / Interaction Baseline — Native iOS ChatGPT Client

_Last updated: 2026-08-27._

## Purpose

This document is the durable UI/interaction baseline for the native client. It is based on the user's current official ChatGPT iOS usage recordings plus explicit user requirements.

The default product rule is:

> **Use the official ChatGPT iOS interaction model as the baseline where it is acceptable; make targeted improvements only for explicit requirements or evidenced pain points.**

This is an interaction/behavior baseline, not a requirement for pixel-perfect copying. Use native UIKit/system behavior where practical and preserve iOS 14.0 compatibility unless a concrete requirement justifies a higher API.

## Evidence classification

- User-provided recordings are current visual interaction reference for the tested official App experience.
- Physical haptic feedback cannot be proven from a screen recording. The user explicitly reports a two-pulse haptic at the reasoning-to-final-answer transition; treat this as a user-confirmed interaction requirement to reproduce/tune on real device.
- `导出 Markdown` visible in recordings is **not an official ChatGPT App feature**; it came from the user's injected dylib. Markdown export is our enhancement.
- Floating overlays and unrelated system/other-app notifications are not part of the ChatGPT UI baseline.

## Global interaction principle

Do not invent a second UI language merely to be different from the official App. Prefer official-style patterns for sidebar/navigation, conversation top bar/overflow, composer, role presentation, message actions, menus/sheets, loading/error states and later advanced navigation.

## Main chat structure

The minimal chat screen uses:

- top-left sidebar/navigation entry;
- minimal top bar with current-context title/controls;
- top-right new-chat / overflow actions following the official pattern;
- vertically scrolling message region;
- bottom composer when send becomes supported.

Do not crowd the top bar with dedicated recovery/export buttons. Put ordinary manual recovery in the conversation overflow menu.

### Startup sidebar usability

On compact iPhone, the sidebar/navigation affordance must be available immediately once the native shell is configured. Opening the sidebar must not be the event that starts initial conversation-list loading; list loading should already be in progress after the accepted cold-start auth warm-up. A lazy primary-column view must not leave the user on an inert `新对话` screen with no usable way to reach the conversation list.

## Conversation header metadata

The conversation title remains primary top-bar text. The existing second-line conversation type (`聊天` or `工作`) is the metadata row.

The project adds optional conversation round count to the right:

- `聊天 · 23轮`
- `工作 · 23轮`

Rules:

- compact centered subtitle/metadata row;
- subdued secondary treatment;
- disabling `显示会话轮数` hides only `· N轮`;
- before authoritative detail exists, show type only rather than misleading `0轮`;
- switching/sync/reload/branch changes must follow authoritative conversation state without retaining the previous conversation's count.

Round count = user messages on the current active branch. Assistant/tool/system/reasoning/status nodes do not add rounds; regenerate alone does not add a round; branch changes recalculate rather than sum alternatives. The count is derived presentation data, not a mutable authority.

## Sidebar / conversation navigation

Use the official-style drawer/sidebar model rather than a custom tab-heavy system. Prioritize recent conversations, selected state, loading/pagination, and settings/account entry. Later destinations appear only when their feature work exists; do not add dead placeholders.

## Conversation messages

### User messages

Use a compact rounded bubble/background treatment similar to the official App.

### Assistant messages

Use wide readable document-style content without a large enclosing bubble. Later support Markdown/headings/lists/links/code/tables/visible attachments as evidence and roadmap require. Message actions should use compact official-style rows/context menus.

## Composer

Follow the official model: rounded composer, multiline growth, leading attachment/tool entry when supported, send affordance when valid, and stop control while an evidenced response is active. Do not preload unsupported future tools.

## Reasoning / thinking interaction

When current protocol supplies user-visible reasoning status/detail:

- active state uses subdued gray status plus an iOS14-compatible shimmer/flowing-light treatment;
- user-visible detail may expand/collapse;
- completed state becomes static, e.g. `思考了 Xs`, only when duration is actually available;
- never manufacture or expose hidden chain-of-thought.

### Reasoning-to-final haptic

Emit the user-required **two short haptic pulses** on the real lifecycle transition from reasoning to final answer. Trigger from response lifecycle, not cell redraw; do not vibrate per token or replay on re-render. Exact feel requires real-device tuning.

## Streaming presentation

Streaming belongs to the active assistant response, not a full-screen loading overlay. Incrementally update only the affected response surface, keep interaction responsive, bind stop/cancel to the exact response owner, and use manual recovery for stale/incomplete state rather than automatically resending.

## Manual recovery enhancements

These are explicit improvements over the default official interaction baseline.

### `同步最新消息`

Purpose: recover when server-side conversation state may be ahead of local thinking/streaming/incomplete state.

Interaction:

- available from current conversation overflow whenever an authoritative conversation identity exists;
- **must remain available during the ordinary initial detail-loading state** so the user can explicitly recover from a request that appears stuck;
- while a manual recovery action itself is active, duplicate recovery actions may be disabled until that action ends;
- fetch current server state through the authoritative conversation owner;
- never resend/regenerate or enter an automatic retry loop.

Feedback accepted from b12:

- centered `正在同步最新消息…` while the request is active;
- centered `已是最新` when unchanged or `已同步最新消息` when changed;
- success result stays visible about 2 seconds; the delay is presentation-only.

### `重载当前会话`

Purpose: recover when current conversation failed to load, timed out, remained blank/spinning or became unusable.

Interaction:

- terminal load-error state provides direct `重新加载`;
- overflow `重载当前会话` is also available **while ordinary initial detail loading is still in progress**, not only after successful load;
- starting manual reload supersedes the older ordinary selected-detail operation so a later stale completion cannot overwrite the newer result;
- reload rebuilds from current server detail through the authoritative owner;
- preserve unsent draft when practical;
- never resend existing messages.

Do not turn either action into automatic infinite retry/watchdog machinery.

## Markdown export enhancement

`导出 Markdown` is our enhancement, not official-App behavior. Place it naturally in overflow; export authoritative current user-visible branch data rather than mounted cells; use normal iOS share/file presentation; never expose hidden/internal reasoning/tool content.

## Loading / empty / error states

Use compact native official-style states.

- Initial/current conversation loading may show centered/system-style progress.
- Manual recovery remains reachable during ordinary detail loading as described above.
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
- Do not raise deployment target for decoration; requested reasoning shimmer is a deliberate exception implemented compatibly where possible.

## State ownership requirements

UI remains a consumer of authoritative state.

- Conversation title/text is not identity.
- Selected conversation has one production owner.
- Round count is derived from authoritative active branch.
- Stream/reasoning state belongs to owning conversation/response lifecycle.
- Haptics come from lifecycle transitions.
- Sync/reload operate through production conversation owner and do not create second stores/identities.
- A freshness/operation-generation guard may reject an obsolete older selected-detail result after a newer explicit recovery; that guard is not a second conversation-data authority.
- Export reads authoritative model rather than rendered UI.

## Validation expectations

Distinguish visual/code implementation, CI/build, artifact availability and real-device interaction. Sidebar/startup feel, recovery-during-load, reasoning UI/haptics, composer behavior and future round-count behavior require real-device/manual acceptance before being called stable.

## Maintenance rule

Update this document when the user supplies newer interaction evidence, explicitly changes a preferred interaction, or a real-device implementation proves an intentional compatibility/product deviation.