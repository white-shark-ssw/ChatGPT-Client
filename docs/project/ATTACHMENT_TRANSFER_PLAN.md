# Attachment Transfer / Download / Share Plan

_Last planned: 2026-08-29; refreshed through b43 exact-device Web attachment-entry Runtime and the iOS17 WebKit picker boundary._

## Purpose / priority

`DEV-attachments` remains the first major capability after accepted text Send/Stream because image/file sending and assistant-file download/share are high-frequency daily operations.

Core goals:

- send images;
- send files/documents;
- support media selection without avoidable local-picker delay;
- receive assistant files and tap -> download -> system share sheet;
- preserve one-tap Copy for visible content.

A full persistent download manager remains separate later `DEV-download-manager` work.

## New b43 Runtime evidence

On exact `DEV-send-stream-0.1.0-b43` / primary iPhone iOS17:

- user reported the requested hybrid interaction sequence was **“基本上没什么问题”**;
- Web `+` -> attachment selection latency was approximately **100–200 ms** and was not rejected as excessive;
- choosing the Web photo entry opened the system photo library but **video assets were filtered out**;
- user explicitly requires future media selection not to hide videos merely because an image-only picker path was chosen.

This establishes two separate facts:

1. picker-entry responsiveness around the observed 100–200 ms is currently acceptable for the tested visible-Web path;
2. the image-filtered media chooser is an explicit product limitation to address.

It does **not** establish that the ChatGPT service accepts or processes arbitrary video files.

## Verified iOS17 WebKit boundary

Do not assume the iOS17 app can simply intercept the webpage file chooser and replace it with a custom PHPicker.

Current public WebKit evidence shows:

- `WKUIDelegate webView(_:runOpenPanelWith:initiatedByFrame:completionHandler:)` is available on **iOS 18.4+**, not the project's primary iOS17 runtime;
- on iOS17 there is no supported public WKUIDelegate hook for replacing that Web upload panel with an app-owned media picker;
- therefore do not use private WebKit API, DOM/file-input injection, JavaScript automation or hidden browser behavior merely to expose videos.

Current official ChatGPT image-input documentation describes **static image** input; current generic file documentation does not prove video-processing support. Picker visibility and server acceptance must remain separate evidence gates.

### Consequence

For iOS17, a real video-capable attachment experience requires an **evidenced native attachment upload/handoff architecture** rather than a cosmetic Web chooser override. Exact upload protocol, asset identity and Send binding remain Unknown / Unverified until `DEV-attachments` measures them.

b44 integrated text-Send work intentionally does **not** claim this video limitation is fixed.

## Evidence boundary for native attachment transfer

Current read/recovery/visible-Web evidence still does not prove:

- upload endpoint(s) / request shape;
- multipart vs staged asset vs signed-upload behavior;
- exact attachment identity bound into Send;
- image/document/video differences;
- server file-size/type/count limits;
- multi-attachment ordering;
- background/resume semantics;
- assistant-file URL/auth/download semantics;
- whether video is accepted, rejected, transcoded or unsupported by the current ChatGPT product.

Do not implement these from memory/history alone.

## Core scope — user sending images/files

### Native picker entry

When the evidenced native transfer path exists, use system pickers compatible with the deployment target:

- Photos/PHPicker for media on iOS14+;
- `UIDocumentPickerViewController` for generic files/documents.

For the app-owned media picker, include both **images and videos** unless current server evidence requires a narrower supported-type UI. If the server later rejects video, show that as a capability/error boundary rather than silently hiding local video assets without explanation.

Do not invent a custom filesystem browser.

### Picker responsiveness contract

- `+` must produce immediate local feedback and begin presenting the local action surface/picker in the same interaction.
- Local picker presentation must not wait for page navigation, Sentinel/Turnstile, upload negotiation or server acknowledgement.
- Do not hide avoidable delay with a synthetic spinner.
- Privacy-safe diagnostics may record picker type and tap-to-presentation duration, never selected content or filenames by default.
- b43's observed Web picker-entry latency of ~100–200 ms is an accepted reference point, not a guaranteed universal threshold.
- Exact-device Runtime remains the authority.

### Composer / ownership

Selected attachments belong to the owning conversation's pending composer state:

- compact thumbnail/file card;
- explicit remove before send;
- no A -> B draft leakage;
- no upload merely because picker closed unless evidenced staged-upload semantics require it;
- authoritative attachment/asset identity must bind to the exact message/conversation Send owner;
- do not create a second attachment repository or second Send state machine.

### Upload UX

First usable native attachment version should expose:

- selected/pending;
- upload in progress when applicable;
- visible failure;
- explicit user retry where appropriate;
- remove/cancel before final Send where possible.

No automatic retry/watchdog/timer chain. Do not fake percentage progress when total/progress is not reliably available.

## Core scope — assistant files: tap -> download -> share

When current protocol proves a user-visible downloadable assistant file:

- render a compact native file card from evidenced metadata only;
- tap -> explicit file-backed download -> app-private temp/cache file -> `UIActivityViewController`;
- support Save to Files/AirDrop/other system share destinations;
- never flatten hidden tool payloads/internal handles into user file cards;
- use accepted transient auth or evidenced signed/direct URL semantics; never persist copied credentials;
- prefer `URLSessionDownloadTask`/file-backed transfer for actual files;
- sanitize filenames/path components;
- keep temp file valid for the active share interaction;
- explicit later tap may retry a failed download; no silent retry loop.

## Security / privacy

- No attachment bytes, copied message contents, raw filenames, auth secrets, signed URLs or upload tokens in diagnostics.
- Reject path traversal in local filenames.
- Do not execute downloaded files in-app merely because they were downloaded.
- Respect verified account/workspace scope; obsolete old-scope callbacks cannot attach content to the current account.

## Diagnostics

Safe attachment diagnostics may include:

- picker opened/type/count/presentation duration;
- selected/removed count;
- upload started/completed/failed with byte count/duration/type category;
- file-card detected count;
- download started/completed/failed/cancelled with byte counts/duration/category;
- share sheet presented/failed.

Default to type/count/size/hash-safe metadata, not private filenames/content.

## Runtime acceptance matrix

For exact iPhone/iOS17 attachment candidates, at minimum:

1. Repeated `+` from warm native chat -> local picker begins promptly without network gating.
2. App-owned media picker shows both photos and videos unless a documented supported-type policy intentionally narrows it.
3. Send one normal image with text.
4. Select one video and establish **actual current service behavior**; success is not assumed. If rejected, record exact user-visible capability/error behavior.
5. Send one normal document/file with text.
6. Remove selected attachment before Send; nothing unexpected uploads/sends.
7. A -> B draft switching does not leak attachments.
8. Upload failure remains visible and does not duplicate eventual message.
9. Assistant downloadable file renders as file card.
10. Tap file -> download -> system share sheet; saved/shared file remains valid.
11. File transfer remains file-backed without obvious whole-file memory spikes.
12. Old account-scope callbacks are rejected.
13. Whole-message Copy and future code-block Copy exclude hidden content.

Additional file types and counts follow service evidence, not guessed capability.

## Relationship to current hybrid Send

- b43 proves visible Web can be sufficiently smooth for the tested sequence and gives the ~100–200 ms attachment-entry observation.
- b44 changes normal Send entry to `native detail -> visible selected-conversation Web -> explicit return/sync`; it does not change the Web upload picker on iOS17.
- `DEV-attachments` must later decide, from fresh protocol/runtime evidence, how native-picked media/files are uploaded and bound into the permitted Send architecture.
- Do not use the visible Web surface as a hidden challenge/file-input bridge.

## Rejected routes

- Guess private upload/download endpoints or headers.
- Hide picker-entry delay behind fake loading UI.
- Claim iOS17 can publicly override WKWebView's file panel using the iOS18.4-only delegate.
- Use private WebKit API, DOM/file-input injection or hidden Web challenge automation to expose videos.
- Treat “video visible in picker” as proof ChatGPT supports processing that video.
- Build a full download manager before basic tap-download-share works.
- Persist copied auth secrets.
- Auto-retry uploads/downloads in loops.
- Copy hidden reasoning/tool/system content.
