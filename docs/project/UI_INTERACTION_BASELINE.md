# UI / Interaction Baseline — Native iOS ChatGPT Client

_Last updated: 2026-08-26._

## Purpose

This document is the durable UI/interaction baseline for the native client. It is based on the user's current official ChatGPT iOS usage recordings plus explicit user requirements.

The default product rule is:

> **Use the official ChatGPT iOS interaction model as the baseline where it is acceptable; make targeted improvements only for explicit requirements or evidenced pain points.**

This is an interaction/behavior baseline, not a requirement for pixel-perfect copying. Use native UIKit/system behavior where practical and preserve iOS 14.0 compatibility unless a concrete requirement justifies a higher API.

## Evidence classification

- User-provided recordings are current visual interaction reference for the tested official App experience.
- Physical haptic feedback cannot be proven from a screen recording. The user explicitly reports a two-pulse haptic at the reasoning-to-final-answer transition; treat this as a user-confirmed interaction requirement to reproduce/tune on real device.
- **Important correction**: the `导出 Markdown` menu item visible in the recordings is **not an official ChatGPT App feature**. It came from the user's separately injected dylib. In this project Markdown export is our enhancement and must not be cited as official-App behavior.
- The floating `--%` overlay and unrelated system/other-app notifications visible in recordings are not part of the ChatGPT UI baseline.

## Global interaction principle

Do not invent a second UI language merely to be different from the official App.

Prefer official-style patterns for:

- sidebar / conversation navigation;
- new-chat entry;
- conversation top bar and overflow menu;
- composer shape and send/stop state transition;
- user-message vs assistant-message layout;
- assistant message action row;
- model/tool/attachment menus and system sheets;
- project/navigation grouping when those capabilities are eventually implemented;
- loading, sheet, context-menu and destructive-action conventions.

Our additions should appear inside those established surfaces whenever possible.

## Main chat structure

The minimal chat screen uses:

- top-left sidebar/navigation entry;
- minimal top bar with current-context title/controls as supported by the current product state;
- top-right new-chat / overflow actions following the official pattern;
- vertically scrolling message region;
- bottom composer with attachment entry, expanding text input and send/stop affordance.

Do not crowd the top bar with dedicated recovery/export buttons. Put normal manual actions in the conversation overflow menu and expose contextual recovery directly in error/stale states where useful.

## Sidebar / conversation navigation

Use the official-style drawer/sidebar model rather than a custom tab-heavy navigation system.

First usable scope should prioritize:

- recent conversation list;
- selected-conversation state;
- new chat entry when send/new-chat becomes supported;
- loading / pagination as evidenced by protocol;
- settings/account entry when already supported by current shell.

Later capabilities such as Projects, Images/Library, scheduled/remote/plugin areas should appear only when their feature work is implemented and current protocol/UI evidence exists. Do not show dead placeholder destinations merely to mimic the full official sidebar.

## Conversation messages

### User messages

Use a compact rounded bubble/background treatment similar to the official App rather than making both roles symmetric full-width chat bubbles.

### Assistant messages

Use wide readable document-style content without a large enclosing bubble.

Support native rendering components as evidence and roadmap require, including:

- Markdown text;
- headings/lists/links;
- code blocks with appropriate code treatment/actions;
- tables with suitable horizontal handling;
- visible attachments/media nodes when later supported.

Message-level actions should follow the official-style compact row/context menu rather than introducing persistent oversized controls.

## Composer

Follow the official interaction model:

- rounded native composer;
- text field grows vertically for multiline input within sensible bounds;
- attachment/tool entry on the leading side when supported;
- send affordance appears when send is available/valid;
- while a response is actively generating, the send affordance becomes a stop control when current protocol supports stop/cancel.

Do not preload the composer with many future tool buttons before those capabilities exist.

## Reasoning / thinking interaction

This is a required core interaction for `DEV-send-stream` when current protocol evidence supplies user-visible reasoning status/detail.

### Active reasoning state

- Show a subdued gray reasoning/status label.
- Reproduce the official-style shimmer/flowing-light visual treatment while reasoning is actively progressing, within reasonable UIKit/iOS 14-compatible implementation constraints.
- The reasoning/status line is tappable when user-visible detail is available.

### Expanded reasoning detail

- Tapping the reasoning/status line expands/collapses the user-visible reasoning summary/detail/tool-status that the service explicitly returns for display.
- Expanded content may update incrementally while current protocol supplies new user-visible detail.
- Never manufacture, infer or expose hidden chain-of-thought. Only render explicit user-visible server content.

### Completed reasoning state

- When reasoning completes, collapse the active shimmer state to a static subdued summary such as `思考了 Xs` when the duration is actually available/evidenced.
- The completed reasoning summary remains tappable so the user can reopen/close available user-visible reasoning detail.
- Final answer content begins below this reasoning summary following the official visual flow.

### Reasoning-to-final haptic

The user explicitly reports that the official App gives **two short haptic feedback pulses** when reasoning completes and the formal answer takes over/starts refreshing. Preserve this interaction.

Implementation constraints:

- Trigger from the response lifecycle transition, not from cell rendering/reuse/reload.
- Do not vibrate for every streamed token.
- Do not replay the two-pulse transition merely because an already-completed response was reloaded/re-rendered.
- Exact feedback generator/intensity/spacing is not frozen from the recording. Tune on real device against the user's observed official behavior and record the accepted result.

## Streaming presentation

Streaming belongs to the active assistant response, not to a full-screen loading overlay.

- Incrementally update the affected assistant message/reasoning surface.
- Keep scrolling/input interaction responsive.
- Do not broad-reload the entire message list for every stream update.
- Stop/cancel state belongs to the active response lifecycle and its owning conversation.
- If a stream is stale/incomplete, expose the manual recovery action described below rather than automatically resending the user's message.

## Manual recovery enhancements

These are explicit improvements over the default official interaction baseline.

### `同步最新消息`

Purpose: recover when server-side generation is already more complete than the local client state, for example when a completion notification has arrived but the client still shows reasoning/streaming or incomplete content.

Interaction:

- available from the current conversation overflow menu;
- may also appear contextually near a clearly stale/incomplete response when that state can be identified without speculative timers;
- fetch current server conversation state and reconcile through the authoritative conversation owner;
- never resend the user's prompt or silently regenerate.

If the sync shows that reasoning/final answer is already complete, replace stale local thinking/streaming UI with the current server-backed completed state.

### `重载当前会话`

Purpose: recover when the current conversation itself failed to load, timed out, remained blank/spinning or became unusable.

Interaction:

- load-error state should provide a direct `重新加载` action;
- current conversation overflow menu may also expose `重载当前会话` for a loaded-but-broken/stale case;
- reload rebuilds that conversation from current server detail through the authoritative owner;
- preserve an unsent composer draft when practical;
- do not resend existing messages.

Do not turn either action into an automatic infinite retry/watchdog chain.

## Markdown export enhancement

`导出 Markdown` is our feature, historically proven useful to the user through a separately injected dylib, not an official-App capability.

Interaction guideline:

- place it naturally in the current conversation overflow menu;
- export from the authoritative conversation model/current user-visible branch, not from mounted cells;
- use normal iOS share/file presentation after generating the `.md` file;
- do not expose hidden/internal reasoning/tool content that is not user-visible.

## Loading / empty / error states

Use compact native official-style states rather than custom full-screen complexity.

- Initial/current conversation loading may show a centered/system-style progress indicator.
- On a terminal load failure/timeout, stop indefinite visual spinning and show a concise failure state with direct `重新加载`.
- Empty/new-chat states should remain visually simple and composer-focused.
- Preserve original error evidence in diagnostics rather than hiding repeated failures behind silent automatic retries.

## Menus and sheets

Prefer native UIKit/system menu/sheet/context-menu conventions compatible with the deployment target.

Conversation overflow should reserve natural positions for current and future actions. Exact ordering may be refined during implementation against the current official App and actual enabled capabilities, but avoid creating a separate settings page for actions that naturally belong in the conversation menu.

Destructive actions such as delete should use standard destructive presentation.

## Visual direction

- Native iOS feel.
- System font/SF Symbols where available under deployment constraints.
- Light/Dark support following system/application appearance policy.
- Moderate information density similar to the official App.
- Avoid decorative effects that require raising deployment target without a product need.
- Shimmer reasoning state is a specifically requested exception and should be implemented with an iOS 14-compatible approach if possible.

## State ownership requirements

UI must remain a consumer of authoritative state.

- Conversation title/text is not conversation identity.
- Selected conversation has one production owner.
- Stream/reasoning state belongs to the owning conversation/response lifecycle.
- Haptics are emitted from state transition events, not arbitrary redraws.
- Sync/reload operate through the production conversation owner; they must not establish second stores/identities.
- Export reads authoritative conversation data rather than currently rendered UI.

## Validation expectations

For UI behavior, distinguish:

- visual/code implementation;
- CI/build success;
- artifact availability;
- real-device interaction result.

The official-style reasoning transition, shimmer/detail interaction, double haptic, sidebar feel, composer behavior and recovery flows require real-device/manual acceptance before being described as matched/stable.

## Maintenance rule

Update this document when the user supplies newer official-App interaction evidence, explicitly changes a preferred interaction, or a real-device implementation proves that an iOS-compatibility constraint requires an intentional deviation.
