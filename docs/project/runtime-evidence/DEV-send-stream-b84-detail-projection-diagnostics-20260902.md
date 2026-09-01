# DEV-send-stream b84 Detail projection diagnostics — 2026-09-02

## Purpose

b84 is a diagnostic-only Candidate created after exact b83 was Runtime Rejected. It does not attempt another Web re-arm fix and does not change user-visible reasoning behavior. Its single question is whether an authoritative manual Detail Sync already ends with a non-empty, previously-authorized presentational reasoning/tool timeline that the current Native projection drops before a visible assistant message exists.

## Identity

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29
- Candidate: `DEV-send-stream-0.1.0-b84`
- Version / Build: `0.1.0 (84)`
- Exact product/config source: `626c3ad4d4d592618d794c4cb8854324f719f4a4`
- Clean CI/package head: `c7398eea6b20788f0e13a18f98e79d3c81ebfc21`
- Push run/job: `33559649854 / 100028790782` — success
- PR run/job: `33559655688 / 100028812048` — success
- Canonical Artifact: `9820763662`
- Artifact ZIP digest: `sha256:65ff52ddc7b6c4ad1e85e0c084a4f55799da06baad602dff3693edd12a814e9f`
- IPA: `ChatGPTClient-0.1.0-b84-dev-send-stream.ipa`
- IPA SHA-256: `1a276fbfc46efeb75566989892d8811561563d6c43a664b1bb7b30799468be38`
- Package source short SHA: `c7398eea6b20`
- Minimum iOS: 14.0
- Architecture: arm64

## Product diff

Exact product source `626c3ad4...` changes only:

1. `ChatGPTClient/Conversation/ConversationFeature.swift`
   - adds integer-only structural fields to `detail.response`;
   - counts the trailing already-presentational pending timeline after `parseCurrentBranch` finishes;
   - counts thinking-preamble messages;
   - separately counts raw `thoughts` and `inline_cot_expandable_content` messages that remain skipped.
2. `ChatGPTClient.xcodeproj/project.pbxproj`
   - build `83 -> 84`;
   - Candidate `DEV-send-stream-0.1.0-b83 -> DEV-send-stream-0.1.0-b84`.

No client-owned SSE, covered-page acquisition behavior, automatic discovery, entry-one-shot Sync, retry/timer/polling, UI rendering or response ownership changed.

## New structural fields

Each authoritative `detail.response` can now include:

- `trailingTimelineItemCount`
- `trailingReasoningItemCount`
- `trailingToolItemCount`
- `thinkingPreambleMessageCount`
- `ignoredThoughtsMessageCount`
- `ignoredInlineCotMessageCount`

These are integer counts only.

## Privacy / presentation boundary

b84 does **not** log or export prompt text, reasoning text, final-answer text, tool body text, authentication/session/challenge material, signed query values, or raw hidden chain-of-thought.

`thoughts` and `inline_cot_expandable_content` remain explicitly non-presentational. Their counts are diagnostic structure only and do not authorize displaying their contents.

## CI / package validation

Push and PR builds both completed successfully with Xcode 16.4. The canonical Push build reports:

- `BUILD SUCCEEDED`
- Candidate `DEV-send-stream-0.1.0-b84`
- source `c7398eea6b20`
- emitted IPA `ChatGPTClient-0.1.0-b84-dev-send-stream.ipa`
- IPA SHA-256 `1a276fbfc46efeb75566989892d8811561563d6c43a664b1bb7b30799468be38`

Downloaded Artifact inspection independently matched the sidecar and verified actual package metadata `0.1.0 (84)`, Candidate `DEV-send-stream-0.1.0-b84`, `DiagnosticsSourceCommit=c7398eea6b20`, minimum iOS 14.0 and an arm64 Mach-O executable.

## Runtime gate

Runtime is **Pending**.

On a deliberately long cross-platform turn, while the remote response is still generating:

1. press manual Sync two or three times at separated points during the active response;
2. do not rely on the covered page visually showing reasoning — b84 is diagnostic-only;
3. export the app diagnostics while the turn is still active if possible;
4. provide the diagnostic JSON.

Decisive interpretation:

- `trailingTimelineItemCount > 0` during active generation means authoritative Detail already contains an approved presentational trailing timeline that current projection drops before a visible assistant row; this authorizes investigating a minimal Native projection fix.
- `trailingTimelineItemCount == 0` across active Detail samples means this hypothesis is rejected; reassess the data source instead of exposing raw skipped thoughts or adding speculative polling.

## Evidence ladder

- b84 Code written: **Yes**
- Exact product diff verified: **Yes**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced: **Yes**
- Package identity / SHA / architecture: **Verified**
- Runtime/manual/real-device: **Pending**
- Stable/Frozen Send: **No**
