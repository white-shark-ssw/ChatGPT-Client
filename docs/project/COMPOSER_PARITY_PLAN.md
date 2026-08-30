# Official Composer Parity Plan

_Last planned: 2026-08-31 from the user-supplied official ChatGPT iOS screen recording._

## Purpose

Define the future native Composer interaction baseline required to match the official ChatGPT iOS app as closely as practical in **interaction logic, state transitions, placement, attachment staging and preview behavior**.

This plan is intentionally separate from current `DEV-send-stream` transport/protocol evidence and from later attachment upload/download transport.

Target future Work ID:

`DEV-composer-parity`

User-facing name:

**官方输入框 / Composer 1:1 对标**

## Development ordering

Current `DEV-send-stream` PR #29 is an Active evidence branch. Its exact b65 Candidate is already Code/CI/Artifact/package verified and waiting on focused Runtime evidence. Do **not** broaden that Candidate/Runtime gate with unrelated Composer polish.

Default serialized order after the current Send/Stream acceptance boundary is:

`DEV-send-stream -> DEV-composer-parity -> DEV-attachments -> DEV-message-rendering -> DEV-conversation-list-preview`

Reason for the dedicated stage:

- Send/Stream owns protected Send, response lifecycle, reasoning/final/tool semantics, Stop and eventual accepted response ownership.
- Composer parity owns the native input surface, draft/picker presentation, local attachment staging/preview and mode/effort controls.
- `DEV-attachments` then binds already-selected native attachments to the **evidenced current upload/asset/message protocol** and implements assistant-file download/share.

This avoids destabilizing an active transport/evidence task while also ensuring native attachment transfer is built on the final official-style Composer instead of a temporary input box.

The active Send/Stream branch currently changes shared roadmap files. Until that Work closes/synchronizes, this document records the intended insertion point without editing its checkpoint, branch, Candidate, `DEVELOPMENT_PLAN.md`, `START_HERE.md` or attachment plan.

## Recording evidence

User-supplied official-app recording:

- duration: **55.1 seconds**;
- video: **510×1108**;
- frame rate: **30 fps**;
- total frames: **1653**.

Review method for this planning pass:

- all frames were scanned for frame-to-frame visual change;
- every major transition peak was identified;
- interaction-heavy ranges were then re-reviewed at approximately 0.15–0.30 second intervals;
- the observations below are visual/product evidence only; they do not prove private upload or Send protocol fields.

## Observed official Composer state machine

### 1. Empty / collapsed state

At the start of the recording the Composer is a compact rounded bar pinned to the bottom safe-area region.

Observed layout:

- leading `+` attachment/tool entry;
- one-line `询问 ChatGPT` placeholder;
- compact trailing voice/microphone/action controls;
- empty state uses the official blue voice-style action rather than a text-send arrow;
- the rest of the conversation/new-chat surface remains visually dominant.

The native client should not begin with a permanently tall text editor when the draft is empty and unfocused.

### 2. Focus transition

Around the first tap on the text field (~1.8s), the system keyboard animates in and the Composer moves with it rather than being covered.

Requirements:

- keyboard and Composer movement use one coordinated layout transition;
- the existing draft/attachments remain in the same Composer owner;
- the field becomes first responder without replacing the Composer hierarchy;
- focus itself does not create/send a server conversation.

### 3. Text entered / send-action transition

After the first non-empty text appears (~3.8s), the trailing primary action changes to the blue **Send arrow**.

The action state is derived from current sendability, not from an unrelated timer:

- empty/non-sendable -> official empty/voice action;
- valid text and/or later valid staged attachment -> Send action;
- active authoritative response -> future Stop action according to `DEV-send-stream` lifecycle evidence.

Do not maintain a second global `isStreaming` or independent button state owner.

### 4. Multiline auto-growth

As text wraps (~4s onward), the rounded Composer grows upward while its bottom control row remains visually anchored.

Observed rules:

- growth is continuous with text content;
- the conversation viewport yields space to the Composer/keyboard;
- leading `+` and trailing actions remain aligned to the Composer's bottom action row;
- growth stops at a bounded inline maximum rather than consuming the full screen indefinitely;
- long draft content remains editable at that capped size.

Exact point/line caps are implementation measurements to reproduce from side-by-side Runtime on the target device. Do not hard-code values solely from the 510×1108 recording scale.

### 5. Inline max-height -> full-screen editor

Once the inline editor is tall, an expansion affordance appears at the upper trailing edge of the draft area. Around ~13.4s the recording shows a native animated transition into a large rounded-top editor surface occupying most of the screen.

Full-screen editor contract:

- same draft identity; no copy into a second durable draft;
- text/cursor/selection state survives the transition;
- Send remains available at the lower trailing region;
- transition has visible spatial continuity rather than an instant replacement;
- collapse returns to the same inline Composer state and restores the editing context;
- no message/network action occurs merely because the editor is expanded/collapsed.

The full-screen editor is a presentation mode over the same draft owner.

### 6. Native text editing semantics

The recording exercises native text selection/context actions around ~19–20s.

Requirements:

- standard iOS selection handles and edit menu remain available;
- Select All / Cut / Copy / Paste behavior must not be blocked by custom gestures;
- clearing the last text returns the Composer to the proper empty/sendability state;
- full-message Copy elsewhere remains independent from Composer text editing.

### 7. Keyboard dismissed with a non-empty long draft

Around ~30–31s the keyboard is dismissed while the long draft remains. The Composer stays content-sized/tall at the bottom instead of collapsing the existing multiline draft into a one-line bar.

Therefore Composer height is a function of draft content + presentation mode, not keyboard visibility alone.

### 8. `+` action menu

Around ~31.8s the leading `+` opens an anchored rounded/material menu without discarding the current draft.

The recorded menu contains the current official entries visible in that session, including:

- 相机;
- 照片;
- 文件;
- 插件;
- 深入思考 (shown selected in the recording).

Product rule:

- reproduce the official menu ordering/grouping for capabilities the client actually supports;
- capability items are not decorative placeholders: unsupported service capabilities stay absent/disabled according to current evidence rather than pretending to work;
- menu open/close does not mutate draft text/attachments.

`深入思考` in this recording is visual evidence for an official reasoning-related mode entry. It is **not** sufficient evidence for the exact later composer-side reasoning-effort level set or request mapping.

## Official file-selection interaction

### 9. File entry is not just a raw system picker

After selecting `文件` (~33s), the official app first presents an **Add File** sheet containing:

- `上传文件` action;
- recent/local file cards/items;
- native sheet dismissal affordance.

Selecting `上传文件` then enters the system document picker. Returning with a selected file inserts a local file card into the Composer.

1:1 target:

`+ -> 文件 -> official-style Add File sheet -> 上传文件 / recent items -> system document picker -> local Composer file card`

The first native implementation does not need to invent cloud/recent sources that are not available to the app, but it should preserve the same hierarchy rather than jumping straight from `+` to a filesystem browser if the official interaction can be reproduced with supported sources.

### File card

Observed Composer file-card behavior:

- card sits above the draft text;
- bounded filename/type presentation;
- compact remove `×` affordance;
- remains part of the same pending draft;
- file selection does not automatically Send the message.

The card is local staged presentation until `DEV-attachments` supplies authoritative upload/asset identity.

## Official photo-selection interaction

### 10. Single photo

Selecting `照片` opens the native photo picker. Choosing one photo and finishing returns to the Composer with a thumbnail above the text, adjacent to other staged attachments when present.

Requirements:

- local picker opens promptly;
- picker cancel does not mutate the draft;
- selected image is represented by a compact thumbnail with remove `×`;
- adding media does not automatically Send.

### 11. Multiple photos

The recording reopens Photos and selects multiple images (~42–46s). On return:

- multiple thumbnails appear in one horizontal staged-attachment strip;
- existing file card remains in the same strip/draft;
- each image is independently removable;
- the attachment row can exceed the visible Composer width without forcing the whole Composer wider.

Use a horizontal scroll/container strategy. Do not wrap dozens of thumbnails into an unbounded vertical wall above the text.

### 12. Attachment preview

Around ~49–54s, tapping an image thumbnail opens a full-screen image preview and closing it returns to the same Composer/draft.

Preview contract:

- tap staged image -> full-screen preview with native black/background presentation appropriate to media;
- dismissal restores Composer text, attachment ordering, keyboard/focus state where possible;
- preview is presentation only; it does not duplicate attachment identity or upload;
- opening/closing preview never Sends.

A future document preview may use the appropriate system preview only when file type/local availability supports it; do not invent execution/rendering for unsafe files.

## Draft and state ownership

The future Composer must have one coherent per-conversation/new-chat draft owner.

Conceptually:

`verified account scope + authoritative conversation identity OR one pending-new-chat presentation target -> ComposerDraft`

Draft presentation may include:

- text;
- text selection/cursor presentation;
- staged local attachments;
- inline/full-screen presentation mode;
- current send configuration selections that are not yet server authority.

Rules:

- A's draft never appears in B;
- new-chat draft is not a fake server conversation;
- selecting/previewing/removing an attachment changes only that draft;
- moving inline <-> full-screen does not create a second draft;
- `ConversationRepository` / accepted response owner remains server-conversation/response authority;
- attachment upload ownership later attaches to the exact draft/Send operation instead of creating a parallel Send state machine.

Exact cross-process draft persistence remains a separate explicit product decision; do not silently persist sensitive drafts merely because display preferences are persisted.

## Reasoning-effort controls — explicit user requirement

The user has separately supplied official-app references requiring the native client to preserve the official **reasoning-effort selector near the Composer Send area**, including the corresponding reasoning-effort behavior in **Work mode**.

This recording itself does not show enough evidence to freeze the exact current level labels/order/defaults for those selectors, so this plan freezes the **interaction/product requirement** while leaving exact values and request mapping evidence-driven.

### Ordinary Chat mode

- Place the reasoning-effort selector in the same Composer action region and relative position as the current official App reference, adjacent to the Send-side controls rather than burying it in Settings.
- Only show the control when the selected model/mode actually supports it according to current service/UI evidence.
- Opening the selector should use the same compact menu/sheet pattern and labels/order as the current official App.
- Changing effort changes the pending Send configuration, not historical messages.
- Do not invent unsupported effort levels or translate old labels from memory.

### Work mode

- `聊天` and `工作` are separate Composer contexts when current service evidence establishes Work-mode semantics.
- Work mode may expose a different reasoning-effort set/default/placement. Do **not** blindly reuse Chat-mode option availability merely because both are called reasoning effort.
- Switching mode must re-resolve the supported effort choices from the current authoritative capability/protocol evidence.
- Exact retention behavior when switching Chat <-> Work (retain separate last selections vs reset to official default) must match the official App/current service evidence rather than being guessed.

### Protocol ownership

The UI selector is not enough to prove Send semantics.

Before production mapping, capture current evidence for:

- the exact option labels/identities presented by the official App/Web for ordinary Chat;
- the exact Work-mode option labels/identities;
- selected model/mode capability gating;
- the exact protected-Send field/key/value representation corresponding to each effort choice;
- server-returned confirmation/metadata, if any;
- default behavior when the selector is untouched.

No selector value may be mapped to a guessed private field/value. The current `DEV-send-stream` transport/lifecycle owner remains the only place that can authorize the final Send request integration.

Do not make `AppPreferences` the authority for server-side model/reasoning state. At most, a future explicit UX decision may remember a presentation preference; the actual outgoing Send configuration must remain tied to the current conversation/new-chat send context and current supported capability.

## Proposed implementation sequence for `DEV-composer-parity`

### Step 1 — official reference measurement

- Re-run side-by-side review on the target iPhone/iOS17 device.
- Measure compact composer margins, corner radius, minimum/maximum inline height, attachment card size, row spacing, expansion transition and full-screen editor geometry.
- Capture the current Chat-mode and Work-mode reasoning-effort controls before freezing exact labels/options.
- Treat current official behavior as evidence; do not reproduce stale screenshots if the App changed.

### Step 2 — one Composer presentation owner

Implement one native Composer hierarchy/state machine that supports:

- empty/collapsed;
- focused empty;
- one-line/multiline text;
- bounded inline maximum;
- full-screen editor presentation;
- keyboard show/hide;
- current sendability/action state.

No alternate temporary composer for new chat vs existing chat unless actual ownership requires a pending target. Share presentation components while keeping each conversation's draft isolated.

### Step 3 — official text editing transitions

- dynamic multiline growth;
- bounded inline height;
- internal text scrolling when capped;
- expansion/collapse transition;
- cursor/selection preservation;
- native edit menu;
- keyboard-safe layout;
- empty <-> send-arrow action transition.

### Step 4 — local attachment staging UI

Implement the **local interaction layer only**:

- `+` menu;
- Camera / Photos / Files entries that are currently supported;
- official-style Add File sheet + system document picker;
- native photo/media picker;
- one/multiple staged attachment strip;
- remove;
- horizontal scrolling;
- staged image full-screen preview;
- per-conversation draft isolation.

This step does not guess/upload private attachment protocol.

### Step 5 — reasoning-effort / mode controls

Once exact UI/protocol evidence exists:

- reproduce the Composer-side Chat selector;
- reproduce Work-mode selector behavior;
- gate choices by current model/mode capability;
- pass the selected current Send configuration into the already-accepted Send owner exactly once.

### Step 6 — Send/Stop integration

Integrate with the accepted `DEV-send-stream` lifecycle:

- empty/voice state when not sendable;
- Send arrow when sendable;
- one Send action -> one exact owned Send;
- active response -> official Stop affordance from authoritative lifecycle;
- failed/terminal response returns action state deterministically;
- no timer/debounce/watchdog/retry merely to make the button feel responsive.

### Step 7 — handoff to `DEV-attachments`

`DEV-attachments` consumes the staged local attachment draft UI and adds only the evidenced transfer/server pieces:

- upload/create asset;
- bind authoritative asset identity to the exact outgoing message;
- progress/failure where real transport supports it;
- assistant file cards;
- tap -> file-backed download -> system share sheet.

Do not rebuild a second attachment strip/picker UX inside `DEV-attachments`.

## Runtime acceptance matrix

Exact target-device Candidate should verify at minimum:

1. Empty new chat shows official compact collapsed Composer.
2. Tap field -> keyboard/Composer animate together with no jump/overlap.
3. First typed character changes the trailing action to the official Send state.
4. Multi-line typing grows smoothly to the measured inline cap.
5. Long text at the cap remains editable/scrollable without layout thrash.
6. Expand -> full-screen editor uses visible official-like transition; collapse restores exact draft/cursor context.
7. Native Select All/Cut/Copy/Paste remains usable.
8. Clearing text restores empty action correctly.
9. Dismiss keyboard with a long draft -> draft remains correctly sized; no accidental one-line collapse.
10. `+` menu opens/closes without losing draft state.
11. File -> Add File sheet -> system document picker -> local file card.
12. Cancel document picker -> no draft mutation.
13. One photo -> thumbnail inserted without sending.
14. Multiple photos -> horizontal strip; each attachment independently removable.
15. Existing file + multiple photos coexist in stable ordering.
16. Tap image -> full-screen preview -> close -> same draft/ordering/focus state.
17. A -> B -> A preserves each conversation's independent text/attachments/presentation state during the live process.
18. New-chat pending draft never becomes a fake persisted server conversation before Send.
19. Ordinary Chat reasoning-effort selector matches current official labels/order/placement and affects the exact evidenced Send configuration.
20. Work-mode effort selector matches current official mode-specific behavior; Chat/Work choices do not leak incorrectly.
21. One tap on Send creates exactly one owned Send; no duplicate request from UI transitions.
22. Active response exposes Stop from the authoritative response lifecycle.
23. Dynamic Type / VoiceOver / light-dark basic sanity without breaking the official geometry intent.
24. No prompt/draft/attachment content or private selector/request values leak into diagnostics.

## Explicit non-goals / rejected routes

- Do not modify current exact b65 product/Candidate merely to prototype Composer parity.
- Do not merge Composer UI into the active b65 formatting Runtime gate.
- Do not guess attachment upload/download endpoints from the recording.
- Do not implement hidden Web file-input injection or private WebKit picker override.
- Do not hard-code unverified reasoning-effort levels/request values.
- Do not create one global draft shared by conversations.
- Do not store full sensitive draft text in `AppPreferences`.
- Do not create a second response/Send state owner inside the Composer.
- Do not fake animations with timer-stepped frame changes.
- Do not auto-upload or auto-Send because picker selection completed.

## Durable product decision

The official ChatGPT iOS Composer interaction shown in the user recording is now the required baseline for the native client. The future implementation should aim for **1:1 behavioral parity first**, then tune geometry/animation on exact device by side-by-side comparison. Deviations require an explicit user requirement, platform limitation or stronger current-service evidence.
