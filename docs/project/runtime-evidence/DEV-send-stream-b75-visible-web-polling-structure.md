# DEV-send-stream b75 Visible-Web Polling Structure

_Date: 2026-09-01_

## Purpose

Record the second privacy-safe Web Rule Lab capture after the current visible official page reproduced `stream_status -> /resume 404 -> repeated page-owned status/conversation reads` for an externally active response.

This evidence does not authorize Native polling, Native-constructed resume/offset, WebSocket body parsing, duplicate Send, retry/timer/watchdog behavior, or a second conversation/response authority.

## Capture

The user installed a read-only structure probe before entering a conversation whose response was still being generated on another platform. The probe cloned only page-owned `stream_status` and plural `/backend-api/conversations/{conversation}` JSON responses and recorded bounded structural summaries. It did not export message text, raw IDs, auth/challenge values or Web storage.

## Observed lifecycle

- First plural conversation snapshot: HTTP200 JSON, `messages.__count = 113`, `async_status = 3`, `current_node` present, no `mapping` object.
- `GET /backend-api/conversation/{conversation}/stream_status` returned HTTP200 JSON with exactly one root key `status` and value `IS_STREAMING`.
- The page then issued its own matching `{conversation_id, offset}` `/backend-api/f/conversation/resume`; response was HTTP404 JSON.
- After that 404, the page continued its own repeated status/conversation reads.
- Subsequent plural conversation snapshots changed while the response was still active:
  - `messages.__count 113 -> 116`;
  - then `116 -> 120`;
  - then `120 -> 125`;
  - `update_time` advanced with those snapshots.
- While generation continued, repeated `stream_status` responses remained `IS_STREAMING`.
- Several later page-owned snapshots were unchanged at `messages.__count = 125` while status still reported `IS_STREAMING`.
- `stream_status` then changed to `COMPLETE`.
- The next plural conversation snapshot remained `messages.__count = 125`; `async_status` was no longer present in the bounded safe-field summary.
- User-level WebSocket frames were present alongside the cycle: one 373-character JSON array with 4 elements, repeated 54-character JSON arrays with 1 element, and one 180-character JSON array with 1 element. Their contents were intentionally not captured, so they remain structural/notification evidence only.

## Current conclusions

1. Current visible official Web does not require a successful `/resume` SSE to keep following this externally active response.
2. `stream_status` is a lifecycle/status signal in this capture: the entire exported shape is `{status}`, and it transitions `IS_STREAMING -> COMPLETE`.
3. The plural `/backend-api/conversations/{conversation}` response is not the existing singular Detail `mapping + current_node` schema. It uses a top-level `messages` array plus `current_node`, pagination fields and conversation metadata.
4. That plural response changes incrementally during active generation: message count and update time advance before terminal `COMPLETE`. Therefore it is more than a terminal-only final reconciliation surface.
5. This capture still does not reveal the per-entry structure of `messages[]`, so it does not yet prove which new entries are user-visible reasoning/tool/final nodes or whether their bodies are incrementally updated in place.
6. The next product decision must not guess that schema. One final narrow structure-only probe is required for bounded `messages[]` entries.

## Source correlation

Current `ConversationRepository` parses the accepted singular Detail `mapping + current_node` schema and already contains the evidenced filtering/reasoning/tool projection rules. The plural page-owned response is a different schema. If a final probe proves its `messages[]` entries contain the same service message objects or a safely transformable subset, the smallest acceptable b76 direction is to observe only page-owned fetch responses already issued by official Web and feed an evidenced transformation through the existing Repository response authority. Native must not reproduce the page's six-second polling cadence.

## Candidate boundary

- Exact tested product remains b75 source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`.
- b39-b75 remain permanently reserved.
- b76 remains unallocated.
- No product/config code changed for this capture.
- Stable/Frozen Send remains No.

## Next exact evidence gate

Capture only a bounded structural summary of the plural response's `messages[]` entries during a fresh externally active response: per-entry root keys; role/status/recipient/content-type; text/parts character counts; metadata key names and safe reasoning/tool enums/booleans; whether repeated snapshots append new entries or mutate the last entries while `stream_status` remains `IS_STREAMING`. Never export bodies or raw IDs.
