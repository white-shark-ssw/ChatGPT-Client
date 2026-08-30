# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Record the user's confirmed ChatGPT video-upload capability and refine the Composer/attachment development boundary.
- **User intent / acceptance criteria**: The native media picker must expose photo-library videos directly. Video sending is a required capability, not an optional experiment. The current official iOS app can upload video when the video is first saved to Files, and PC Web accepts video by drag/drop; our client should remove that iOS friction by selecting video directly from Photos.
- **Baseline**: `main@5bb77e0076a880dda70b5e4553d738effc91f1a4`; rules branch `rules/video-upload-capability-20260831`. Active development PR #29 remains `DEV-send-stream`; do not modify it.
- **Evidence / reason**: latest explicit user runtime/product evidence outranks the earlier plan wording that treated server-side video support as Unknown.
- **Files in scope**: this checkpoint and a non-overlapping durable video-capability addendum under `docs/project/`.
- **Do-not-touch**: active PR #29 files/checkpoint/product/Candidate/Artifact, including its current attachment plan copy.
- **Completed**: governance startup re-read; current main verified; requirement classified as confirmed product capability with native upload protocol still Unverified.
- **Validation state**: Rules/planning only; no product Code/CI/Artifact/Runtime changes.
- **Pending**: write durable addendum, merge rules PR, reset this checkpoint Idle.
- **Next exact action**: document that video upload/processing capability is user-confirmed while exact native upload endpoint/asset binding remains a `DEV-attachments` evidence task.
- **Rejected / do-not-repeat**: treating video server capability as unknown; filtering videos out of Photos; requiring users to save recordings to Files before selecting them.
- **Open questions / risks**: exact native upload protocol, accepted formats/size/count limits and Send attachment identity remain Unverified.

## Active task template

When a multi-step rules task starts, switch to `Active` early and maintain:

- **Task**
- **User intent / acceptance criteria**
- **Baseline**: rule files / branch / PR / commit
- **Evidence / reason**
- **Files in scope**
- **Do-not-touch**
- **Completed**
- **Validation state**: Rule drafted / documented / PR opened / merged
- **Pending**
- **Next exact action**
- **Rejected / do-not-repeat**
- **Open questions / risks**

## Proactive checkpoint rule

The conversation/context limit is unpredictable. Once the rules problem and usable direction are clear, establish an Active checkpoint. Refresh at meaningful rule decisions, permanent-rule edits, PR state changes, or direction changes.

## Completion

When complete, move durable rules to permanent files, reset only this file to `Idle`, and do not modify/delete/reset any Active development checkpoint merely to finish rules work.
