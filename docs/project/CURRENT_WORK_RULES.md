# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Refine `DEV-composer-parity` attachment-picker and local-preview requirements from the user's latest explicit product decision.
- **User intent / acceptance criteria**: `文件` opens the system Files Picker directly with no official Add File intermediate sheet; selected files use the recorded rectangular card style with file type + filename and removable `×`; supported text-like local files are tappable for preview. `照片` must allow both images and videos and must not filter videos from the system media picker.
- **Baseline**: `main@91192f7a65d24b305dbb9adb3bafc176de41c4cd`; rules branch `rules/composer-picker-refinement-20260831`. Active development PR #29 remains `DEV-send-stream`, open/unmerged; do not modify it.
- **Evidence / reason**: latest explicit user requirement overrides the earlier official recording hierarchy for the file-entry path. Existing `COMPOSER_PARITY_PLAN.md` currently specifies an Add File intermediate sheet and image-only wording, so durable planning must be corrected.
- **Files in scope**: `docs/project/COMPOSER_PARITY_PLAN.md` and this Rules checkpoint only.
- **Do-not-touch**: PR #29 branch/checkpoint/product/Candidate/Artifact; `ATTACHMENT_TRANSFER_PLAN.md`, `DEVELOPMENT_PLAN.md`, `START_HERE.md` and other files changed by active PR #29.
- **Completed**: governance startup re-read; current main and PR #29 state verified; exact stale Composer-plan clauses identified.
- **Validation state**: Rules/planning only; no product Code/CI/Artifact/Runtime changes.
- **Pending**: update Composer plan, verify diff, merge rules PR if clean, reset checkpoint Idle.
- **Next exact action**: replace the Add File hierarchy with direct `UIDocumentPickerViewController`, add safe local text-file preview/card contract, and explicitly require PHPicker media selection to include both images and videos.
- **Rejected / do-not-repeat**: reintroducing the Add File intermediate sheet unless the user changes this requirement; image-only PHPicker filtering; treating local video selection as proof the ChatGPT service accepts video upload.
- **Open questions / risks**: exact server-side video upload/processing support remains Unknown/Unverified and belongs to `DEV-attachments`; local selection/preview must remain decoupled from server capability.

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

When complete, move durable rules to permanent rule files, reset only this file to `Idle`, and do not modify/delete/reset any Active development checkpoint merely to finish rules work.
