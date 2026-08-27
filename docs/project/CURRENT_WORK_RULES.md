# Current Work — Rules

## Status

**Active**

- **Task**: Define default conversation-entry scroll behavior to match official-style latest-message presentation without breaking per-conversation semantic scroll restoration.
- **User intent / acceptance criteria**: First entry into a conversation with no prior local reading position should show the latest message / bottom. Returning to a conversation that already has a saved reading position should restore that position instead of forcing bottom.
- **Baseline**: `main` after PR #20; active development task `DEV-multi-conversation-state` remains isolated on `dev/multi-conversation-state-20260827` and owns its own product code/checkpoint.
- **Evidence / reason**: Current b21 source `ConversationDetailViewController.restoreScrollAnchor(for:)` sends conversations with no saved anchor to `resetScrollPositionToTop()`, matching the user's observed current behavior.
- **Files in scope**: `docs/project/DEVELOPMENT_PLAN.md`, `docs/project/UI_INTERACTION_BASELINE.md`, this rules checkpoint.
- **Do-not-touch**: `ChatGPTClient/Conversation/ConversationFeature.swift`, active multi-conversation checkpoint, Candidate/build/CI/artifact state, multi-conversation-owned durable docs.
- **Completed**: Real source behavior confirmed; desired first-entry/latest-vs-return/restore semantics defined.
- **Validation state**: Rule planning active; no product code changed.
- **Pending**: Persist rule in non-overlapping durable docs, conflict-check, merge rules-only PR, reset rules checkpoint to Idle.
- **Next exact action**: Update `DEVELOPMENT_PLAN.md` and `UI_INTERACTION_BASELINE.md` with first-entry-bottom and saved-anchor restoration rules.
- **Rejected / do-not-repeat**: Do not make loading-state top offset into a saved reading anchor; do not animate through an entire long conversation on first display; do not force bottom on every return/Sync/Reload.
- **Open questions / risks**: Future Send/Stream follow-tail behavior must distinguish user-at-bottom from user-browsing-history; that integration remains owned by `DEV-send-stream`.
