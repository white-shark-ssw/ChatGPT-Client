# DEV-send-stream b82 allocation — 2026-09-01

- Candidate: `DEV-send-stream-0.1.0-b82`
- Version / Build: `0.1.0 (82)`
- Formal branch before allocation docs: `68bb0688878c1135399bdc21ceacbfd7f150250e`
- b81 Runtime evidence commit at initial allocation: `e977a0ec40f827509a9175e6c4901accaa2d9cab`
- b82 allocation checkpoint commit: `b6c30083177d76b07adcf5bcce94bdd053120b51`
- Corrected b81 Runtime interpretation commit: `b736f25b30a696b1760d99a344b0e3e864e28c33`
- PR #29 was open / mergeable / unmerged at allocation.
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Exact search found no pre-existing `DEV-send-stream-0.1.0-b82` before allocation.
- Only one Active development checkpoint exists.
- b39-b82 are permanently reserved.

## Corrected evidence basis

Exact b81 device diagnostics show the covered `ws.chatgpt.com` socket created/open before the remote turns, then two privacy-safe JSON-array structural frames with exact current-conversation `targetMatch=true` at 16:22:20Z and 16:24:24Z while Native still had no external live response. The user confirms **two separate messages were sent remotely**, so the two frames are not duplicate notifications from one turn. Manual Sync at 16:24:59Z then returned authoritative Detail with visible messages 4 -> 8 and four added visible messages, consistent with two new user/assistant turns.

Therefore the original b82 “first frame only for the whole observation cycle” restriction is withdrawn.

## Authorized b82 scope

b82 may convert a target-matching WebSocket frame into a **bounded per-event acquisition hint** when all of the following hold:

1. the executor is observing the currently selected existing conversation;
2. no Repository live response for that conversation is already active;
3. no automatic acquisition Sync for that conversation is currently in flight;
4. the structural frame has exact current-conversation `targetMatch=true`.

For one accepted hint:

- start at most one `ConversationRepository.syncLatestMessages(id:)`;
- compare authoritative latest-user identity before/after the Sync;
- only if latest user changed and the conversation is still selected and no live response was naturally acquired meanwhile, perform one covered-page re-arm/reload;
- if latest user did not change, record `no_change` and stop without reload;
- if Sync fails, record failure and stop; manual Sync remains recovery.

A later distinct target-matching frame may trigger another bounded acquisition attempt once the previous automatic Sync is no longer in flight. This is necessary because b81 observed two target frames for two distinct remote Sends.

WebSocket content remains non-authoritative. No timer/poll/retry/watchdog/repeated automatic loop/account-wide notification/fake streaming/Frozen presentation changes are authorized.
