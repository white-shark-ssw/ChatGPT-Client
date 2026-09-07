# DEV-send-stream b84 active Detail trailing timeline — 2026-09-02

## Identity

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b84`
- Version / Build: `0.1.0 (84)`
- Exact product/config source: `626c3ad4d4d592618d794c4cb8854324f719f4a4`
- Clean CI/package head: `c7398eea6b20788f0e13a18f98e79d3c81ebfc21`
- Canonical Artifact: `9820763662`
- IPA SHA-256: `1a276fbfc46efeb75566989892d8811561563d6c43a664b1bb7b30799468be38`
- Runtime package metadata: Candidate b84 / source `c7398eea6b20` / iOS17.0
- Target diagnostic marker: `sha256:d597360f6d29`

## Exact Runtime chronology

The target is the same long/problematic conversation class that previously failed to acquire page-owned reasoning under b83.

- `21:25:56` initial authoritative Detail: visible 25, mapping 1293, trailing timeline 0.
- Manual Sync starts `21:28:12`.
- `21:28:16` authoritative Detail HTTP200: visible `25 -> 26` (new remote user row), mapping 1297, `trailingTimelineItemCount=1`, `trailingReasoningItemCount=1`, tools 0, thinking-preamble count 32.
- `manual_sync_rearm` then page loaded at `21:28:17`, but no `external_page_owned`, no `liveResponse.started`, no external snapshot and `livePresentationRowCount` remained 0.
- Second manual Sync starts `21:28:33`.
- `21:28:37` authoritative Detail HTTP200: visible still 26, mapping 1303, `trailingTimelineItemCount=4`, reasoning 1, tools 3.
- Re-arm/page load again completed, still without page-owned live acquisition.
- After relaunch, ordinary Detail at `21:28:49`: visible 26, mapping 1305, trailing timeline 5 = reasoning 1 + tools 4.
- Explicit Reload Detail at `21:28:56`: visible 26, mapping 1307, trailing timeline 6 = reasoning 1 + tools 5.

Across these active/pre-final samples, the authoritative Detail graph and approved trailing presentational timeline grew while no new visible assistant row existed and no page-owned live response was acquired.

## Decisive conclusion

b84's diagnostic hypothesis is **Runtime Positive**.

`ConversationRepository.parseCurrentBranch` already recognizes user-visible thinking preambles / approved reasoning recap / approved tool activity into `pendingTimeline`, while explicitly skipping raw `thoughts` and `inline_cot_expandable_content`. The exact Runtime above proves that this already-presentational `pendingTimeline` can be non-empty and grow during active cross-platform generation before a visible assistant message exists.

The current parser attaches `pendingTimeline` only when a later visible assistant message is appended. If the branch ends first, the ordinary `ConversationDetail.messages` projection drops the trailing timeline. b84 exported counts only, which is why the UI still had `livePresentationRowCount=0` despite Detail already holding presentational reasoning/tool structure.

Therefore the current manual-Sync instability is not solely a Web re-arm/acquisition problem. In this exact failing case, authoritative Detail itself already contains enough approved presentational structure for a Native block snapshot, but the Native projection discards it.

## Authorized next change

A minimal next Candidate may expose the actual already-approved trailing timeline from `parseCurrentBranch` to the existing `ConversationRepository` response runtime and present it through the existing live-response UI on explicit manual Sync. It must:

- reuse the existing per-conversation response owner; no second response store;
- keep raw `thoughts` / `inline_cot_expandable_content` non-presentational;
- preserve client-owned SSE unchanged;
- allow later page-owned snapshots to update the same external response generation when available;
- allow another explicit manual Sync to refresh an active external Detail-backed block when page continuation does not attach;
- reconcile/clear the external live snapshot once authoritative completed assistant content materializes;
- add no polling, timer, retry, watchdog, duplicate Send, automatic discovery or entry-sync behavior.

## Evidence classification

- b84 active-generation authoritative trailing presentational timeline: **Runtime Positive**
- b84 active timeline growth without visible assistant: **Runtime Positive (`1 -> 4 -> 5 -> 6`)**
- page-owned acquisition for this sample: **Negative**
- raw hidden thoughts presentational authorization: **No**
- minimal Native projection/response-owner correction: **Evidence-backed next action**
- Stable/Frozen Send: **No**
