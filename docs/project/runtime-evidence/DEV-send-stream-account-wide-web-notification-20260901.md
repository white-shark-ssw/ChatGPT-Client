# DEV-send-stream account-wide Web notification evidence — 2026-09-01

## User Runtime observation

On the official ChatGPT PC Web client, the user can remain on conversation A. Even when conversation B has not been opened in that browser session, when B produces a new answer the Web UI shows a notification bubble at the upper-right.

## Evidence classification

This is **user Runtime evidence** that the official Web runtime receives an account-wide new-answer/completion signal that is not inherently tied to the currently open conversation page and does not require the target conversation B to have been opened first.

This materially strengthens the earlier official-iOS observation that any account conversation completion can trigger a two-stage haptic even while another screen/conversation is visible.

What is now supported:

- an account-wide completion/new-answer signal exists in the official Web runtime;
- the signal can reach a page currently displaying a different conversation;
- the target conversation does not need to have been opened in that browser session for the Web UI to notify;
- therefore an event-driven account-wide notification/automatic-Sync design is technically plausible for this client if the same signal can be observed safely.

What remains **Unknown / Unverified**:

- exact transport (WebSocket, fetch/long-poll, service worker, browser push, another channel, etc.);
- exact event schema/fields;
- whether the event directly carries a conversation identifier or requires a bounded authoritative list/detail refresh;
- whether the signal remains available under the app's covered `WKWebsiteDataStore.default()` browser runtime;
- foreground/background delivery semantics on iOS.

## Architecture consequence

Do not implement a timer/poll/watchdog to imitate the official behavior. The next protocol-evidence step should be a privacy-safe Web Rule Lab capture while official Web remains on conversation A and another platform causes conversation B to complete.

The probe should identify the **account-level event source** without recording message bodies, auth secrets or raw identifiers. If a reliable event is proven, one deduplicated accepted event can fan out to:

1. one completion haptic/notification;
2. one bounded authoritative conversation-list/detail Sync;
3. current-detail refresh only when the affected conversation is selected;
4. no duplicate Send and no second conversation-state owner.

## Candidate boundary

This evidence does **not** expand b80. b80 remains limited to the already-proven tool/divider spacing correction and external COMPLETE/final-materialization race correction. Account-wide completion notification/automatic Sync requires its own protocol evidence before product implementation.
