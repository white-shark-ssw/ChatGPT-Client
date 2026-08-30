# Composer Video Upload Requirement

_Last updated: 2026-08-31 from explicit user runtime/product evidence._

This addendum supersedes any older project wording that treats ChatGPT video upload/processing support as Unknown.

## Confirmed product capability

The user has directly verified both of the following:

- the current ChatGPT iOS client can upload a video when the recording is first saved to Files and then selected as a file;
- ChatGPT Web on desktop accepts video by drag/drop.

Therefore **video upload is a required supported product capability for this client**, not an optional experiment.

## Required native UX

The native client must remove the current iOS friction:

- `+ -> 照片` opens the system media picker;
- the picker exposes **both images and videos** from Photos;
- do not require the user to first export/save a recording to Files;
- do not configure an image-only filter that hides videos;
- selected videos enter the same per-conversation Composer draft/attachment strip as selected images/files;
- staged video supports local preview/playback before Send;
- choosing/previewing a video does not automatically Send.

## Evidence boundary that remains open

The fact that the ChatGPT product accepts video is confirmed. What remains **Unknown / Unverified** for our native implementation is only the current private transfer binding:

- exact upload endpoint/request shape;
- staged/signed/multipart behavior;
- authoritative asset/file identity;
- how that identity is attached to the protected Send request;
- accepted formats, size/count limits and any processing/transcoding details;
- upload progress/cancel/resume semantics.

Those items belong to `DEV-attachments` and must be captured from current protocol/runtime evidence rather than guessed.

## Development ordering

Keep the planned split:

`DEV-send-stream -> DEV-composer-parity -> DEV-attachments`

- `DEV-composer-parity` owns direct Photos video selection, local staging, removal and preview.
- `DEV-attachments` owns the evidenced upload/asset/Send integration and must prove at least one real native video Send on the target iPhone/iOS17 device.

## Rejected routes

- Do not classify server-side video capability as unknown again unless newer real evidence contradicts the user's confirmed behavior.
- Do not hide videos from Photos merely because the current official iOS UI makes video selection inconvenient.
- Do not force a Photos video through a Save-to-Files workaround in our client.
- Do not infer the native upload protocol merely from desktop drag/drop or the current official Files workflow.
