# DEV-send-stream b84 Detail projection diagnostics — 2026-09-02

## Purpose

b84 is a diagnostic-only Candidate created after exact b83 was Runtime Rejected. It does not attempt another Web re-arm fix and does not change user-visible reasoning behavior. Its original single question was whether an authoritative manual Detail Sync already ends with a non-empty, previously-authorized presentational reasoning/tool timeline that the current Native projection drops before a visible assistant message exists.

This document now also records the first exact b84 real-device sample where manual Sync successfully re-armed the covered official page and Native immediately acquired a real external reasoning snapshot.

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

## First b84 real-device Runtime sample — partial positive

Uploaded diagnostics identify exact b84 (`0.1.0 (84)`, Candidate `DEV-send-stream-0.1.0-b84`, source `c7398eea6b20`) on iOS17.0. Privacy-safe target conversation marker: `sha256:6f429823a988`.

The user reported that in this different conversation, pressing Sync made the reasoning block attach immediately. The log supports that observation.

Chronology:

1. `21:24:32` selection starts observing the existing conversation. Initial Detail at `21:24:33` is HTTP200, `visibleMessageCount=13`, `mappingCount=134`, `trailingTimelineItemCount=0`, `thinkingPreambleMessageCount=8`, `ignoredThoughtsMessageCount=12`.
2. After returning to the app, `21:25:00` latest Sync starts. The authoritative Sync result at `21:25:01` advances visible messages `13 -> 14` and mapping `134 -> 135`, but still reports `trailingTimelineItemCount=0`, `trailingReasoningItemCount=0`, `trailingToolItemCount=0`.
3. The successful Sync immediately emits `coveredExecutor.observing mode=manual_sync_rearm` at `21:25:01`; the covered page reaches `state=loaded` at `21:25:02`.
4. At `21:25:06`, only about four seconds after page load, Native starts `liveResponse` with `source=external_page_owned`, phase `thinking`. The same second records `externalStreamingObserved`, `externalDOMStructure assistantNodeCount=4 / textCharacters=1326`, and page-owned resume observation.
5. The page-owned resume response is HTTP404 JSON, so the already-established `page_owned_read_path` fallback is used; no Native-constructed resume/request is introduced.
6. At `21:25:07`, Native receives a changed external snapshot with `phase=reasoning`, `reasoningCharacters=258`, `serviceMessageCount=9`, `toolCount=3`. This is the first exact b84 Runtime proof that a manual Sync re-arm can successfully acquire live external reasoning in the covered production path.
7. At `21:25:13`, a later changed external snapshot reports `serviceMessageCount=11`; the live response then records `terminal / completed`, still with `finalCharacters=0`, and the covered snapshot reports `complete=true`.
8. The following authoritative reconcile at `21:25:14` still has `visibleMessageCount=14`, but now reports `trailingTimelineItemCount=6`, `trailingReasoningItemCount=2`, `trailingToolItemCount=4`, `thinkingPreambleMessageCount=10`, `ignoredThoughtsMessageCount=13`.

## What this sample proves

### Runtime confirmed

- Exact b84 manual Sync re-arm can successfully acquire a covered-page external live response.
- In this successful sample, `manual_sync_rearm -> page loaded -> external_page_owned -> non-empty reasoning snapshot` occurs within seconds.
- Page-owned `/resume` may still be HTTP404 while the existing page-owned read path supplies a genuine external reasoning/tool snapshot.
- A non-empty approved presentational trailing timeline can exist in authoritative Detail while the visible assistant row has still not been added (`visibleMessageCount` remained 14 at the `trailingTimelineItemCount=6` reconcile).

### Important timing qualification

The `trailingTimelineItemCount=6` authoritative Detail sample occurs **after** the live external response already emitted `terminal / completed` at `21:25:13`. Therefore this sample does **not** yet prove that `trailingTimelineItemCount > 0` is available during the still-active generation phase before terminal.

What it does prove is narrower and still useful: after page-owned completion but before the authoritative visible assistant row materializes, the current Detail parser can end with a non-empty already-presentational timeline that is not attached to a visible assistant message.

### Strong hypothesis, not yet a decision

The user's observation is that conversations which begin producing visible reasoning text quickly appear much easier to attach, while conversations with a long initial interval before visible reasoning repeatedly fail to acquire.

This successful sample is consistent with that hypothesis: shortly after the covered page loaded, it exposed enough live page/service structure for `external_page_owned` adoption and a real reasoning snapshot. The earlier b83 failure had repeated clean page loads but never entered `external_page_owned` during the long active interval.

Do **not** promote this correlation to a production rule yet. One same-build A/B comparison is still needed to distinguish first-presentational-content timing from other per-conversation/page-state differences.

## Current Runtime classification

b84 is **Runtime Partial Positive**, not Stable and not a product fix.

- Code written: **Yes**
- Exact product diff verified: **Yes**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced: **Yes**
- Package identity / SHA / architecture: **Verified**
- Covered-page manual Sync live reasoning acquisition: **Runtime Positive in this sample**
- Post-terminal/pre-visible-assistant non-empty trailing presentational timeline: **Runtime Positive**
- Active-generation non-empty trailing presentational timeline before terminal: **Still Unverified**
- Deterministic acquisition across conversations/response shapes: **Still Rejected/Unproven**
- Stable/Frozen Send: **No**

## Next exact action

Keep exact b84; do **not** allocate b85 yet.

Use the user's simultaneous test of the current conversation as the next A/B Runtime sample. For the same b84 build, determine whether manual Sync enters `external_page_owned` and whether a live reasoning snapshot appears while the answer is still generating. Export the diagnostics regardless of success or failure.

Decisive comparison:

- if the current conversation again fails despite clean `manual_sync_rearm` / page load while the successful conversation above acquires live reasoning within seconds, compare the timing/availability of user-visible page/service reasoning structure rather than adding another refresh/retry;
- if the current conversation also succeeds, b84 has two positive samples and the next investigation should focus on why prior long-running b83/b82 cases lacked page-owned presentational acquisition;
- if an active pre-terminal Detail sample ever shows `trailingTimelineItemCount > 0`, the original b84 projection hypothesis becomes directly Runtime confirmed for active generation and can justify a separate minimal Native projection design.

Do not expose raw skipped thoughts and do not add polling, timer, retry, duplicate Send/resend or a second response owner.
