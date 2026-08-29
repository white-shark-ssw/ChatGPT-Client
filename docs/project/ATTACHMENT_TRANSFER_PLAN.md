# Attachment Transfer / Download / Share Plan

_Last planned: 2026-08-29; refreshed with explicit attachment-entry responsiveness requirement._

## Purpose

This document defines the high-priority attachment path for the native ChatGPT client after the first proven text Send/Stream lifecycle.

The user has identified these as high-frequency daily operations:

- send images;
- send files/documents;
- receive files produced/sent by the assistant;
- tap an assistant file to download it and immediately invoke the iOS system share sheet;
- preserve one-tap copy actions for visible message/content surfaces.

Planned core Work ID remains `DEV-attachments`. A full persistent download manager is deliberately split into later `DEV-download-manager` work so it does not delay basic transfer usability.

## Priority decision

The old roadmap placed `DEV-attachments` after Markdown export/long-conversation tuning. That no longer matches current user priority.

New default route:

`DEV-multi-conversation-state -> DEV-conversation-round-count -> DEV-send-stream -> earliest daily-chat Candidate -> DEV-attachments`

`DEV-attachments` therefore becomes the first major capability immediately after accepted text Send/Stream. Conversation-list persistence/preview and other polish remain important, but they no longer outrank high-frequency file/image transfer.

## Evidence boundary

Current read/recovery evidence does **not** prove the present upload protocol, attachment node schema, assistant-file download URL/auth semantics, file-size limits, multi-file behavior or attachment lifecycle.

Before production implementation, the dedicated development Work must evidence current behavior from the actual service/runtime. Do not implement private upload/download endpoints or headers from history/memory alone.

Unknown / Unverified until then:

- upload endpoint(s) and request shape;
- whether upload is multipart, signed-URL, staged asset creation or another flow;
- exact attachment identity bound into Send requests;
- image/document differences;
- whether assistant-returned files use direct URLs, signed temporary URLs or authenticated download routes;
- server file-size/type/count limits;
- multi-attachment ordering/limits;
- background/resume semantics;
- if a future user-visible official-Web Send architecture is selected, the exact supported WebKit mechanism for handing a native-picker selection into the official-Web attachment input/send flow.

## Core scope — user sending images/files

### Picker entry

Use native iOS pickers compatible with the deployment target:

- photo/image selection through the appropriate Photos/PHPicker path available on iOS14+;
- generic files/documents through `UIDocumentPickerViewController` or the accepted system file picker path.

Do not invent a custom filesystem browser.

### Picker responsiveness contract

Attachment entry is a high-frequency interaction and has an explicit user acceptance requirement: tapping the composer `+` must not be followed by a long pause before the attachment action surface or picker appears.

- The `+` tap must produce immediate local visual response and begin presenting the native iOS attachment action surface / picker in the same user interaction.
- Picker presentation is a **local UI action**. It must not wait for WebView navigation, page warm-up, ChatGPT network requests, Sentinel/Turnstile work, upload negotiation or server acknowledgement.
- Do not insert a fake loading spinner merely to hide avoidable picker-entry latency.
- Privacy-safe diagnostics should record picker-entry source/type and tap-to-action-surface / tap-to-picker presentation duration, but never selected filenames or contents by default.
- Exact-device Runtime on the primary iPhone/iOS17 target is the acceptance authority. Functional file sending with clearly perceptible picker-entry lag is not sufficient.
- Test both a warm ordinary chat state and any future hybrid user-visible Web Send state; Web lifecycle state must not turn a local `+` tap into a network-gated action.
- If a future hybrid Web Send architecture is chosen, the exact file-selection handoff into official Web remains **Unknown / Unverified** until inspected and tested. Do not assume native code can programmatically populate or drive a Web file input, and do not use a hidden WebView/challenge workaround to force it.

### Composer presentation

Selected attachments belong to the owning conversation's composer/pending-send state.

- show compact image thumbnails or file cards before send;
- allow explicit removal before send;
- preserve unsent text/attachments when switching conversations only through the existing per-conversation draft owner once that owner exists;
- never leak A's selected attachments into B's composer;
- do not upload merely because the picker closed unless current protocol/product semantics require a staged upload and the user has clearly selected that attachment for the draft.

### Upload/send ownership

Once current protocol is evidenced:

1. create/prepare the attachment through the proven upload path;
2. bind the resulting authoritative attachment/asset identity to the exact pending message/conversation response owner;
3. send the user message exactly once through the established `DEV-send-stream` owner;
4. transition provisional local attachment presentation to server-backed identity when the service confirms it.

Do not create a parallel attachment repository or a second Send state machine.

### Upload UX

First usable version should provide:

- pending/selected state;
- upload-in-progress state when the protocol has a separate upload phase;
- visible failure state;
- explicit user retry by tapping/retrying after a failure where appropriate;
- explicit remove/cancel before final Send when still possible.

No automatic retry/watchdog/timer chain.

Exact byte progress is desirable when the underlying transfer exposes stable progress, but lack of byte-total evidence must not be papered over with fake percentages.

## Core scope — assistant files: tap -> download -> share

### Message presentation

When current protocol proves a user-visible downloadable assistant file/attachment, render a native compact file card instead of flattening it into ordinary text.

Display only evidenced metadata such as:

- safe filename;
- type/icon;
- size when supplied and trustworthy;
- download/progress/error state.

Do not expose hidden tool payloads/internal file handles merely because they exist in raw protocol nodes.

### Tap behavior

Primary first-version behavior:

`tap file card -> explicit download -> local temporary/cache file -> immediately present UIActivityViewController`

This lets the user immediately use system actions such as:

- Save to Files;
- AirDrop;
- share to another App;
- copy/open with another compatible App where iOS provides the action.

The first core version does not require a custom download-management screen.

### Download ownership

Use the currently evidenced authenticated transport:

- if the service provides an authenticated ChatGPT route, use the existing transient native auth owner rather than persisting copied credentials;
- if the service returns an evidenced signed/direct URL, use that exact semantics without adding unrelated ChatGPT headers;
- never log Authorization/Cookie values, signed query secrets, file contents or raw sensitive URLs.

Prefer `URLSessionDownloadTask`/file-backed transfer semantics for actual file bytes where appropriate, rather than holding large files fully in memory.

### Local file lifecycle

For the first version:

- download into an app-private temporary/cache location;
- sanitize filenames/path components before writing;
- keep the file valid for the duration of the share/open interaction;
- the user can persist it explicitly through the system share sheet / Save to Files;
- no promise of permanent in-app download history until `DEV-download-manager`.

Temporary cleanup must not race the active share sheet. Exact cleanup timing is implementation-level and should be deterministic rather than timer/watchdog based.

### Failure/cancellation

- show a visible transfer failure on that file card;
- a later user tap may explicitly try the download again;
- no silent automatic retry loop;
- leaving the conversation does not by itself have to destroy a valid transfer owner if the accepted attachment architecture later supports continued transfer, but this must follow real runtime evidence rather than speculation.

## One-tap copy contract

Copy is not an optional later polish feature.

### Basic message copy

The next conversation metadata/settings Work should establish a basic one-tap Copy action for visible user and assistant message text because this requires no new server protocol and touches the same message presentation surfaces.

Rules:

- copy the current user-visible textual message content;
- never include hidden reasoning/tool/system material;
- Copy does not alter message state or trigger network requests;
- use the system pasteboard;
- provide compact immediate feedback compatible with the official-style interaction baseline.

### Rich/scoped copy

When Markdown/code rendering is implemented:

- fenced code blocks get a dedicated one-tap code-copy control;
- code copy copies the code content rather than requiring long-press selection;
- other future user-visible rich content may expose a scoped Copy action when its semantics are clear;
- the base whole-message Copy action remains available unless a later evidenced official interaction intentionally replaces it.

## Security / privacy

- No attachment bytes or copied message contents in diagnostics.
- No auth secrets, signed download URLs or upload tokens in logs.
- Sanitize local filenames and reject path traversal components.
- Do not execute downloaded files inside the app merely because they are downloaded.
- Use system viewers/share actions for external file handling unless a later feature explicitly adds a safe native previewer.
- Respect current account/workspace scope; late upload/download callbacks from an old account must not attach content to the new account's conversation state.

## Diagnostics

Privacy-safe events may include:

- picker opened/type/count and picker-entry presentation duration;
- attachment selected/removed count;
- upload started/completed/failed with byte counts/duration/type category only;
- assistant file card detected count;
- download started/completed/failed/cancelled with byte counts/duration/type category only;
- share sheet presented/failed;
- copy action invoked by role/content-type count only.

Never log filenames when they may contain private content unless a later explicit redaction policy proves a safe representation; default to type/count/size/hash-safe metadata.

## Runtime acceptance matrix

At minimum on exact iPhone/iOS17 candidates:

1. Repeatedly tap composer `+` from an ordinary warm chat state; local action surface / picker begins presenting without clearly perceptible delay and without waiting on network activity.
2. If a hybrid user-visible Web Send architecture is selected, repeat `+` after Web enter/return and while the visible Web session is already resident; picker entry remains locally responsive and is not gated on page/challenge work.
3. Send one normal image with accompanying text.
4. Send one normal document/file with accompanying text.
5. Remove a selected attachment before Send; nothing uploads/sends unexpectedly.
6. Switch A -> B with unsent attachment draft when per-conversation draft ownership exists; no cross-conversation leakage.
7. Upload failure remains visible and does not duplicate the eventual message.
8. Assistant-returned downloadable file renders as a file card.
9. Tap assistant file -> download completes -> system share sheet appears.
10. Save to Files/AirDrop or another available share destination receives a valid file.
11. Download failure does not crash/blank the conversation and a later explicit tap can retry.
12. Large-enough file transfer uses file-backed transport without obvious whole-file memory spikes.
13. Account-context change rejects late attachment callbacks from the old scope.
14. Copy user message and assistant message with one action; clipboard text matches visible content and excludes hidden material.
15. When code-block rendering exists, code-copy returns the expected code content.

Additional file types/multi-attachment counts follow current server evidence rather than guessed capability.

## Download manager — lower priority

Planned later Work ID: `DEV-download-manager`.

Possible later scope only after core download/share is accepted:

- persistent download history;
- per-file progress list;
- retained local files / cleanup controls;
- reopen/share again without re-download when still available;
- optional background/resume behavior if current iOS/service semantics support it;
- storage usage and clear-cache management.

Do **not** block `DEV-attachments` on this manager.

## Relationship to other roadmap work

- `DEV-send-stream` must exist first because attachment sends need the authoritative conversation/message response owner.
- Basic whole-message Copy is pulled earlier into `DEV-conversation-round-count` because it is local UI behavior with no protocol dependency.
- `DEV-attachments` follows immediately after the first accepted text Send/Stream Candidate.
- `DEV-conversation-list-cache-preview` follows attachment core unless a later explicit user priority changes the route.
- Future message rendering adds code-block-specific Copy.
- Background completion/true-background work must not pretend ordinary attachment uploads/downloads are automatically background-resumable without evidence.

## Rejected routes

- Keep attachment sending near the end of the roadmap despite explicit high-frequency use.
- Build a full download manager before basic tap-download-share works.
- Guess private upload/download endpoints or headers.
- Make local attachment picker presentation wait on Web page/network/challenge/upload work.
- Hide picker-entry latency behind synthetic loading UI instead of fixing the local interaction path.
- Assume an unverified native-to-Web file-input handoff or use hidden browser/challenge work to force one.
- Download assistant files fully into memory when file-backed transfer is available.
- Persist copied auth secrets for downloads.
- Auto-retry uploads/downloads in loops.
- Copy hidden reasoning/tool/system content.
