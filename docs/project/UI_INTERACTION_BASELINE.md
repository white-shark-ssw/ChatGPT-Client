# UI / Interaction Baseline — Native iOS ChatGPT Client

_Last updated: 2026-08-27._

## Purpose

This document is the durable UI/interaction baseline for the native client. It is based on the user's current official ChatGPT iOS usage recordings plus explicit user requirements.

The default product rule is:

> **Use the official ChatGPT iOS interaction model as the baseline where it is acceptable; make targeted improvements only for explicit requirements or evidenced pain points.**

This is an interaction/behavior baseline, not a pixel-perfect requirement. Use native UIKit/system behavior where practical and preserve iOS14 compatibility unless a concrete requirement justifies higher APIs.

## Evidence classification

- User-provided recordings are current visual interaction reference for the tested official App experience and current-client acceptance feedback.
- Physical haptics cannot be proven from screen recording; the user explicitly reports a two-pulse reasoning-to-final haptic and it requires real-device tuning.
- `导出 Markdown` visible in recordings is **not an official ChatGPT App feature**; it came from the user's injected dylib. Markdown export is our enhancement.
- Floating overlays and unrelated system/other-app notifications are not part of the ChatGPT UI baseline.

## Global interaction principle

Do not invent a second UI language merely to be different from the official App. Prefer official-style patterns for sidebar/navigation, top bar/overflow, composer, role presentation, message actions, menus/sheets, loading/error states and later advanced navigation.

## Main chat structure

The minimal chat screen uses:

- top-left/native list-detail navigation as appropriate for current state;
- minimal top bar with current-context title/controls;
- top-right new-chat / overflow actions when supported;
- vertically scrolling message region;
- bottom composer when send becomes supported.

Do not crowd the top bar with dedicated recovery/export buttons. Put ordinary manual recovery in the conversation overflow menu.

### Compact iPhone startup and list/detail navigation

Current read-only product state has no useful new-chat composer yet. Therefore, when there is **no selected conversation at launch**, the compact iPhone product root must be the **conversation list**, not a blank secondary `新对话 / 从侧边栏选择一个会话` placeholder.

Rules:

- accepted WebKit warm-up may happen first, but once the product shell appears it should open on the conversation list immediately, even if list rows are still loading;
- the list request must begin automatically after accepted auth warm-up; revealing a sidebar/list must not be what starts it;
- selecting a conversation presents the detail;
- normal native Back / UISplitViewController compact navigation returns from detail to the conversation list;
- there must be **one navigation owner/affordance for the same action**. Do not layer a custom sidebar button on top of UISplitViewController's own compact navigation and produce duplicate icons;
- repeated taps on a custom `show(.primary)` control are not an acceptable substitute for reliable native compact navigation.

b13 real-device evidence established this rule: initial list loading itself started immediately, but the user remained on the secondary placeholder and duplicate sidebar controls made list access unreliable. b14 implements the native single-owner direction; runtime acceptance is pending.

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
- switching/sync/reload/branch changes follow authoritative conversation state without retaining previous count.

Round count = user messages on current active branch. Assistant/tool/system/reasoning/status nodes do not add rounds; regenerate alone does not add a round; branch changes recalculate rather than sum alternatives. Count is derived presentation data, not mutable authority.

## Sidebar / conversation navigation

Use official-style drawer/list-detail navigation rather than a custom tab-heavy system. Prioritize recent conversations, selected state, loading/pagination and settings/account entry. Later destinations appear only when implemented; do not add dead placeholders.

## Conversation messages

### User messages

Use a compact rounded bubble/background treatment similar to the official App.

### Assistant messages

Use wide readable document-style content without a large enclosing bubble. Later support Markdown/headings/lists/links/code/tables/visible attachments as evidence and roadmap require. Message actions use compact official-style rows/context menus.

## Composer

Follow the official model: rounded composer, multiline growth, leading attachment/tool entry when supported, send affordance when valid, stop control while an evidenced response is active. Do not preload unsupported future tools.

## Reasoning / thinking interaction

When current protocol supplies user-visible reasoning status/detail:

- active state uses subdued gray status plus an iOS14-compatible shimmer/flowing-light treatment;
- user-visible detail may expand/collapse;
- completed state becomes static, e.g. `思考了 Xs`, only when duration is actually available;
- never manufacture or expose hidden chain-of-thought.

### Reasoning-to-final haptic

Emit the user-required **two short haptic pulses** on the real lifecycle transition from reasoning to final answer. Trigger from response lifecycle, not cell redraw; do not vibrate per token or replay on re-render. Exact feel requires real-device tuning.

## Streaming presentation

Streaming belongs to the active assistant response, not a full-screen loading overlay. Incrementally update only affected response surface, keep interaction responsive, bind stop/cancel to exact response owner, and use manual recovery for stale/incomplete state rather than automatically resending.

## Manual recovery enhancements

### `同步最新消息`

Purpose: recover when server-side conversation state may be ahead of local thinking/streaming/incomplete state.

Interaction:

- available from current conversation overflow whenever authoritative conversation identity exists;
- **remain available during ordinary initial detail loading** so the user can explicitly recover from a request that appears stuck;
- while one manual recovery itself is active, duplicate recovery actions may be disabled until it ends;
- fetch server state through authoritative conversation owner;
- never resend/regenerate or enter automatic retry loop.

Feedback accepted from b12:

- centered `正在同步最新消息…` while request active;
- centered `已是最新` when unchanged or `已同步最新消息` when changed;
- success stays visible about 2 seconds; delay is presentation-only.

### `重载当前会话`

Purpose: recover when current conversation failed to load, timed out, remained blank/spinning or became unusable.

Interaction:

- terminal load-error state provides direct `重新加载`;
- overflow `重载当前会话` is also available **while ordinary initial detail loading is in progress**;
- starting a newer manual recovery makes older selected-detail completion obsolete so it cannot overwrite the newer result;
- runtime evidence from b13 additionally shows the client should not intentionally leave the replaced selected-detail network request active while issuing the replacement: overlapping replacements hit HTTP429. This request-lifecycle correction is pending and is separate from b14's shell fix;
- reload rebuilds from current server detail through authoritative owner;
- preserve unsent draft when practical;
- never resend existing messages.

Do not turn either action into automatic retry/watchdog machinery.

## Markdown export enhancement

`导出 Markdown` is our enhancement, not official-App behavior. Place naturally in overflow; export authoritative current user-visible branch rather than mounted cells; use normal iOS share/file presentation; never expose hidden/internal reasoning/tool content.

## Loading / empty / error states

Use compact native official-style states.

- Conversation list may be visibly empty/loading while initial server data is fetched; that is preferable to hiding the list behind an unusable blank detail placeholder.
- Initial/current conversation loading may show centered/system-style progress.
- Manual recovery remains reachable during ordinary detail loading as described above.
- Terminal failure stops indefinite spinning and presents concise failure state with direct reload.
- Empty/new-chat state remains simple once new-chat is actually usable.
- Preserve original error evidence instead of hiding failures behind silent retries.

## Menus and sheets

Prefer native UIKit/system menus/sheets/context menus compatible with deployment target. Conversation overflow reserves natural positions for recovery/future actions; destructive actions use standard destructive presentation.

## Visual direction

- Native iOS feel.
- System font/SF Symbols where available.
- Light/Dark support following system/application appearance policy.
- Moderate density similar to official App.
- Do not raise deployment target for decoration; requested reasoning shimmer is a deliberate compatible exception where possible.

## State ownership requirements

UI remains a consumer of authoritative state.

- Conversation title/text is not identity.
- Selected conversation has one production owner.
- Round count derives from authoritative active branch.
- Stream/reasoning state belongs to owning conversation/response lifecycle.
- Haptics come from lifecycle transitions.
- Sync/reload operate through production conversation owner and do not create second stores/identities.
- Freshness/operation-generation may reject an obsolete older selected-detail result after newer explicit recovery; it is not a second conversation-data authority.
- UISplitViewController/native navigation owns compact list/detail presentation; do not create a duplicate custom navigation authority.
- Export reads authoritative model rather than rendered UI.

## Validation expectations

Distinguish visual/code implementation, CI/build, artifact availability and real-device interaction. Compact startup/list-detail navigation, recovery-during-load/request replacement, reasoning UI/haptics, composer and future round-count behavior require real-device/manual acceptance before being called stable.

## Maintenance rule

Update this document when the user supplies newer interaction evidence, changes a preferred interaction, or real-device implementation proves an intentional compatibility/product deviation.