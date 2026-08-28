# UI / Interaction Baseline — Native iOS ChatGPT Client

_Last updated: 2026-08-28._

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

b25 real-device comparison against the official ChatGPT iOS App establishes the required compact detail-header hierarchy:

- **conversation title is the primary first line**;
- conversation type / round count is a subdued compact second line;
- for the currently supported ordinary-chat detail path, round count On presents `聊天 · 23轮` and round count Off presents `聊天`;
- the metadata row must not sit above the title and must not create prompt-style extra navigation-bar height;
- detail conversation metadata must therefore not use `navigationItem.prompt` as its presentation owner.

Round count is derived presentation data from authoritative active-branch user messages, never a second mutable authority.

`工作 · N轮` remains the intended Work/Project presentation **only when an authoritative current Work/Project type source is evidenced**. Do not infer `工作` from conversation title or other presentation text merely to imitate the official label.

## Sidebar / conversation navigation

Use the official-style drawer/sidebar/list model rather than a custom tab-heavy system. Prioritize recent conversations, selected state, loading/pagination, settings/account entry and native compact navigation ownership.

### Persistent cold-start list and message preview

The planned `DEV-conversation-list-cache-preview` enhancement adds a dense one-line preview under the conversation title and a persistent account-scoped list snapshot.

Recommended row treatment on compact iPhone:

- title remains the primary line, normally one line with tail truncation for dense scanning;
- preview is one subdued `.secondaryLabel` line below the title with tail truncation;
- Dynamic Type may increase row height; do not force a fixed height that clips accessibility text;
- preview is derived display metadata only and never changes conversation identity or tap behavior.

Cold-start presentation follows cache-first / stale-while-refresh semantics **after current account/workspace verification**:

1. show the matching account-scoped cached list immediately when available;
2. start one normal list refresh;
3. merge changed/new rows without blanking the already-visible cache;
4. if refresh fails, keep the cache visible and present failure non-destructively.

Never flash another account's cached titles/previews before the current account scope is verified.

Message preview sourcing must not create a request storm:

- if current runtime evidence proves the existing list response itself includes a usable user-visible preview field, use it from that same list request;
- otherwise use only locally known current visible user/assistant messages obtained through normal Detail/Sync/Reload and later Send/Stream activity;
- do **not** automatically issue one Conversation Detail request per list row merely to populate previews;
- hidden/system/tool/reasoning content is never a preview source;
- persist only a bounded clipped preview, not the full message body/raw Detail payload.

If another client updates a conversation and the current list response provides only a newer `update_time` without preview content, the cached subtitle may represent the **last locally known preview** until that conversation is normally opened/synced/reloaded. Do not silently solve this with hidden Detail prefetching.

A future `显示会话消息预览` preference uses the centralized settings owner. Toggling it only changes list presentation; it does not trigger network requests or erase the cached snapshot.

### List refresh presentation

A pull-to-refresh gesture is presentation for an actual manual list refresh, not an independent loading authority.

- The active pull/refresh region must have a visible native/system indication; do not expose a blank spacer above the first row with no indication of why it exists.
- Use dynamic system styling so the refresh affordance remains readable in Light/Dark appearance without hard-coded per-theme colors.
- If a list load is already active and a new `UIRefreshControl` trigger is rejected as redundant, end that newly-started refresh-control presentation immediately.
- Do not leave an invisible refresh-control area pushing the first row down until an older load later finishes.
- When refresh presentation ends, if the table remains stranded above `-adjustedContentInset.top` and the user is no longer dragging/decelerating, normalize it back to the real top. If the user's gesture is still active, defer that normalization until drag/deceleration ends instead of fighting the gesture.
- Rejecting a redundant refresh must not create a duplicate list request, retry, debounce timer or watchdog.
- Presentation diagnostics may record refresh state, `contentOffset`/adjusted inset and a reason, but must not include conversation titles/IDs merely to diagnose this UI issue.
- Successful/failed manual refresh continues to use the existing retained-list feedback contract.

## Conversation messages

### User messages
Use a compact rounded bubble/background treatment similar to the official App.

When `显示消息时间` is enabled, show subdued timestamp metadata **above** each visible user bubble, aligned to the user-message side. The timestamp is not part of the message body and must not change message identity or copying/export semantics.

### Assistant messages
Use wide readable document-style content without a large enclosing bubble. Later support Markdown/headings/lists/links/code/tables/visible attachments as evidence and roadmap require.

When `显示消息时间` is enabled, show subdued timestamp metadata **above** each visible assistant response, aligned to the assistant/document side. Reasoning/status rows are not independent assistant messages merely because they are visible UI; timestamp ownership follows the actual visible assistant message model supplied by the service/response owner.

### Message timestamp source and formatting

- Historical/server-backed messages use the authoritative message `createTime` / service `create_time` already present in the conversation model; do not refetch Detail solely for timestamps.
- Use the device's current locale and time zone.
- Same-day messages may use time-only; older messages include enough date context to avoid ambiguity. Exact localized formatting/spacing is implementation-level and should be tuned on real device without raising the deployment target.
- If a historical message has no authoritative timestamp, omit the metadata rather than fabricate a current time.
- Future optimistic Send presentation may temporarily show a provisional local timestamp only if the authoritative response/message owner needs it; once server-backed time exists, the display must hand off to that authoritative value rather than keep a second durable timestamp authority.

## Message actions / Copy

Copy is a required daily-use interaction and must remain easy in the native client.

### Basic message Copy

- Visible assistant textual replies expose a compact official-style Copy action in the response action area.
- The assistant Copy visual should use a small `doc.on.doc`-style system symbol, clear/no emphasized button background and a subdued dynamic system tint such as `.secondaryLabel`; it must follow Light/Dark appearance automatically rather than use a large bright-blue custom treatment.
- Keep the assistant action row compact; hiding Copy for a user-message cell must collapse that action slot rather than reserve assistant-action height.
- Visible user messages expose Copy through the native message/context action surface without requiring manual text selection.
- Copy reads the authoritative **user-visible** message text; hidden reasoning/tool/system content is never included merely because it exists in the protocol graph.
- Copy uses the system pasteboard, does not mutate message state and does not trigger any network request.
- Provide compact immediate feedback such as `已复制`; exact presentation is implementation-level.

b25 real-device evidence accepts assistant Copy function for the tested case. b27 changes the requested visual treatment only; its compact Light/Dark appearance remains Runtime-pending until tested. User-message/context Copy and future scoped code Copy remain subject to their applicable Runtime checks.

### Scoped Copy

When Markdown/code rendering exists:

- each fenced code block gets a dedicated one-tap Copy control;
- code Copy copies the block's code content, not surrounding prose/cell decorations;
- whole-message Copy remains available unless a later explicit interaction decision changes it.

## Conversation entry / reading-position behavior

The official-style default is **latest-message first**, while the multi-conversation presentation owner preserves an already-established reading position.

### First entry with no local reading anchor

- When a loaded conversation becomes visible and this process has no valid saved semantic reading anchor for that conversation, present the **latest message / bottom of the current visible branch** by default.
- Do not present the first historical message merely because `UITableView` begins at offset zero.
- The loading/empty placeholder position is not a reading position and must not be captured as an anchor.
- For a long conversation, initial latest-message placement should appear at the final position without visibly animating through hundreds/thousands of historical rows.
- This applies equally when Detail finished while the conversation was hidden and the conversation is later shown for the first time without an established reading anchor.

### Return to an already-read conversation

- Once a real semantic reading anchor has been captured for A, switching A -> B -> A restores A's anchor rather than forcing A to the bottom.
- B maintains its own independent reading anchor; selecting/jumping/scrolling B never mutates A's saved position.
- Sync/Reload/current-branch replacement should preserve an established anchor through the same presentation owner when it is still resolvable; they are not treated as fresh first-entry events.
- If authoritative replacement makes an old anchor impossible to resolve, discard the obsolete anchor explicitly. Do not silently treat a raw top offset as a new authoritative reading position.

### Future streamed content

When Send/Stream exists, latest-message follow behavior extends these semantics:

- if the user is already at/near the latest edge, new streamed content may keep following the active answer naturally;
- if the user deliberately scrolls upward to inspect history, streaming must not continuously steal the viewport back to the bottom;
- switching to another conversation never cancels the hidden conversation's response merely because its viewport is no longer visible;
- exact near-bottom threshold/follow-tail state is owned by `DEV-send-stream` and requires real-device tuning.

## Quick previous / next answer navigation

This is a user-required long-conversation enhancement and is optional through settings.

### Semantic target

- `上一轮回答` / `下一轮回答` navigate by derived **round answer anchors**, not raw pixel percentages.
- A round begins at an authoritative visible user message. Its historical answer anchor is the first visible assistant reply after that user message and before the next visible user message.
- Multiple tool/reasoning/system nodes do not independently become “rounds”. A missing historical assistant reply does not get a fabricated anchor.
- The same derived round projection supports header round count and answer navigation, avoiding parallel mutable indexes.

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

Tapping must produce visible spatial continuity and semantic one-answer progression:

- resolve the adjacent answer anchor in the chosen direction from the current visible round context;
- scroll the existing `UITableView` to the assistant-answer row start using native animated row scrolling;
- do **not** instantly teleport to a final raw offset;
- do **not** fake a long jump with timer-stepped offsets;
- a user touch/drag may naturally interrupt the animation and takes priority.

b25 diagnostics proved that recomputing every tap only from the still-moving visible rows can repeatedly request the same answer (`targetRow=61`, later `105`, `143`) during rapid taps. The corrected interaction contract is:

- while native programmatic scrolling is still in flight, consecutive button taps advance from the **last requested derived answer target**, not from a stale intermediate visible viewport;
- this programmatic target cursor is transient presentation state only and points into the existing derived answer-row projection; it is not a second semantic round/answer authority;
- a real user drag clears that cursor and re-establishes navigation context from the actual user-controlled viewport;
- target positioning uses native `.top` row semantics so the assistant answer start, not an estimated raw pixel offset for a self-sizing row, is the navigation destination.

b26 real-device diagnostics show that this transient target cursor materially improved semantic progression, including rapid `214 -> 221 -> 227` targets, but the user still observed occasional start delay and mid-animation hitch. Therefore b27 adds the following interaction-performance rule without changing semantic ownership:

- do not recompute/reset the answer-jump control on every programmatic `scrollViewDidScroll` frame;
- update direction/control presentation at semantic events such as tap target change, real drag-direction change/end, deceleration end and programmatic animation end;
- avoid resetting the same symbol/accessibility state when the effective direction did not change;
- keep native row animation and user interruption; do not replace this with debounce/timers/watchdogs or speculative height-cache machinery.

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

## Assistant files — download and share

The high-priority attachment interaction is specified in `ATTACHMENT_TRANSFER_PLAN.md` and follows accepted text Send/Stream ownership.

### File card

When current protocol proves a user-visible downloadable assistant file, render a native compact file card inside the owning assistant response rather than flattening it into ordinary text.

Display only currently evidenced metadata such as:

- safe filename;
- type/icon;
- size when supplied/trustworthy;
- download/progress/error state.

The attachment identity belongs to the authoritative message/attachment model, not to a URL stored only in the cell.

### Tap -> download -> system share

Required first-version interaction:

`tap file card -> explicit download -> app-private local temporary/cache file -> immediately present UIActivityViewController`

This intentionally exposes native system actions such as Save to Files, AirDrop and compatible third-party share/open targets.

- Do not substitute an expiring/authenticated remote URL for a completed reliable local download.
- A visible failure remains on the owning file card and a later user action may retry; no automatic retry loop.
- If a valid local downloaded copy already exists for the same attachment identity, a later tap may reuse it and open the share sheet without needless redownload.
- A full download-management screen is not required for this interaction.

## Composer

Follow the official model: rounded composer, multiline growth, leading attachment/tool entry when supported, send affordance when valid, and stop control while an evidenced response is active. Do not preload unsupported future tools.

### High-frequency image/file send

After text Send/Stream is accepted, native attachment sending becomes the next high-priority capability:

- leading `+` opens official-style attachment choices;
- **照片/图片** uses the iOS14-compatible native Photos/PHPicker path;
- **文件** uses `UIDocumentPickerViewController` / accepted system document picker path;
- selected attachments display compact thumbnails/file cards in the owning composer before Send;
- user can explicitly remove an attachment before Send;
- pending attachment state belongs to the owning conversation draft so A's selected file never appears in B;
- upload progress/failure is shown only to the fidelity actually supported by the evidenced transfer;
- upload endpoint/headers/asset identity/type/size limits must be captured from current protocol before production implementation.

Do not silently upload/retry/resend merely because picker selection or transfer failed. Do not recompress/transcode images unless current service requirements justify it.

## Download manager — later

Basic assistant-file tap-download-share must ship before a custom download manager.

A later optional `DEV-download-manager` may add:

- active/recent download list;
- retained local-file history;
- re-open/re-share/delete;
- storage usage/cleanup controls;
- pause/resume/background behavior only if current iOS/service evidence supports it.

The manager must not block core attachment usability.

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

For the conversation list specifically, a valid matching persistent cache is useful content rather than an error placeholder. A failed refresh may keep those cached rows visible while the refresh failure is surfaced separately; this is not an automatic network fallback/retry loop.

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
- Persistent list cache is a scope-bound durable snapshot consumed through `ConversationRepository`, not a second list/conversation authority.
- Cached preview is bounded derived presentation metadata and may be last-locally-known when server preview content is unavailable; it never triggers automatic Detail fan-out.
- Round count is derived from authoritative active branch.
- Message timestamp display is derived from the authoritative message timestamp where available; the display toggle is preference state, not message state.
- Copy reads authoritative user-visible message/block content and never hidden reasoning/tool/system payloads.
- First-entry latest-message placement and returned-conversation semantic restoration are two states of the same per-conversation presentation owner; raw loading/top offsets are not a second reading-position authority.
- Answer-jump anchors are a lightweight derived presentation index over the authoritative visible active branch; they are rebuilt after authoritative message projection changes.
- A rapid-tap programmatic answer-target cursor is transient UI state pointing into that projection; it is cleared by real user drag and cannot become a second semantic answer/scroll authority.
- Per-conversation semantic scroll state remains owned by the existing conversation presentation owner; quick navigation cannot introduce a competing saved-offset store.
- Stream/reasoning state belongs to owning conversation/response lifecycle.
- Pending outgoing attachments belong to the owning conversation composer/draft state.
- Incoming download state belongs to the owning attachment identity and must not migrate across conversations/accounts.
- Sync/reload operate through production conversation owner and do not create second stores/identities.
- A freshness/operation-generation guard may reject obsolete selected-detail results; request-task cancellation/replacement remains lifecycle ownership at the same authoritative repository.
- Export reads authoritative model rather than rendered UI.

## Validation expectations

Distinguish visual/code implementation, CI/build, artifact availability and real-device interaction. b14 compact startup/list-detail navigation is real-device accepted for iPhone/iOS17. b25 real-device testing accepted assistant Copy function, historical message-time display for the tested case and persisted conversation-display Preferences, while rejecting the prompt-style header, rapid answer-jump behavior and redundant refresh-control presentation; b25 diagnostics also exposed a `30/29` list reconciliation invariant failure. b26 real-device testing then accepted the compact title-first header, sequential answer-target progression and the authoritative-total `29/29` list bound for the tested sequence, while still reporting answer-jump smoothness hitch and a blank top refresh region and explicitly requesting timestamp-above/compact-Copy presentation changes. b27 contains the scoped corrections described above and is **Code + source diff audit + exact CI + identity-valid Artifact + PR merge-view CI only; Runtime pending**.

For conversation entry/scroll behavior, real-device validation should include: first entry into a long unloaded conversation lands at the latest message without visible top-to-bottom traversal; first display of a hidden-completed Detail with no saved anchor also lands at latest; A -> B -> A restores A's previously established semantic reading position; loading placeholders never overwrite that anchor behavior.

For the current header validation, compare against the supplied official-app reference: title first, `聊天 · N轮` second, normal compact navigation-bar height, and round-count Off leaving `聊天` without altering title hierarchy. `工作` is not accepted until authoritative type evidence exists.

For b27 answer navigation, real-device validation must include a long conversation, rapid repeated taps while animation is still moving, upward/downward real-drag direction changes, manual interruption, first/last boundaries, target answer start alignment, A/B independent scroll anchors, Sync/Reload anchor rebuild, keyboard/composer coexistence when available, and confirmation that jumps visibly animate without the prior start/mid-animation hitch. If hitch remains after removing the evidenced per-frame updater, measure before adding any row-height cache or other optimization.

For list cache/preview, real-device validation should include warm-cache cold start, one-request refresh/reconciliation, network-failure cache retention, no automatic Detail fan-out, account-scope isolation, first-page-28 merge behavior, and relaunch persistence of a preview derived from an already-opened conversation. For the b27 regression specifically, top pull/manual refresh must show a visible refresh affordance, redundant pull during an existing load must not start a duplicate request, completion must not leave a persistent blank top region, and with authoritative `totalCount=29` reconciled `resultCount` must remain at or below 29. If the blank region reproduces, capture the privacy-safe `conversationList.refreshPresentation` / `conversationList.refreshTopNormalized` diagnostics.

For b27 timestamps/Copy, verify timestamps appear above both user and assistant messages, assistant Copy remains functional and visually compact, and the symbol/tint remains appropriate in both Light and Dark appearance. Clipboard output must still match user-visible content and exclude hidden material/UI decorations.

For attachment receive/download/share, validate a real assistant file card, one user-triggered download, valid local file, immediate system share sheet, explicit failure/no auto retry, conversation/account isolation and safe local-file reuse.

For attachment send, validate real image + document selection/upload/send, pending removal, A/B draft isolation and no duplicate send on failure.

## Maintenance rule

Update this document when the user supplies newer interaction evidence, explicitly changes a preferred interaction, or a real-device implementation proves an intentional compatibility/product deviation.
