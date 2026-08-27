# START HERE

This is the repository's AI work entry point.

## Startup order

1. Read repository root `AGENTS.md`.
2. Read `CURRENT_WORK.md` and determine Rules vs Development/Feature from the user's current message.
3. Read `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `BUILD_TEST_INDEX.md`, `PROJECT_SPECIFIC_RULES.md`, and `DOCUMENTATION_POLICY.md`.
4. If `PROJECT_PROFILE.md` says `Initialization: Pending`, perform repository bootstrap according to `AGENTS.md` before substantive development.
5. For Rules work, use `CURRENT_WORK_RULES.md`.
6. For Development/Feature work, use `CURRENT_WORK_DEV.md` and exactly one selected checkpoint under `current/dev/`.
7. Before multi-conversation, production send/stream, background-completion or TrollStore true-background work, also read `CLIENT_ARCHITECTURE_GAP_REVIEW.md` plus the relevant `MULTI_CONVERSATION_STATE_PLAN.md` / `BACKGROUND_EXECUTION_PLAN.md`. These documents contain pre-send concurrency, async-freshness, account-scope and background active-response-set invariants that are not safe to rediscover ad hoc.
8. For any new post-recovery development task, read both the **Post-recovery development sequence** in `CLIENT_ARCHITECTURE_GAP_REVIEW.md` and the current phase ordering/scope in `DEVELOPMENT_PLAN.md` before choosing/creating the Work. Current branch/checkpoint evidence and the user's latest explicit requirement outrank either document if one is temporarily behind an Active parallel task. Cold-start login-state recovery belongs to `DEV-conversation-recovery`; do not create a separate `DEV-auth-resume` task.
9. Before `DEV-conversation-list-cache-core`, `DEV-conversation-list-preview`, or any later conversation-list persistence/preview work, also read `CONVERSATION_LIST_CACHE_PLAN.md`. The early cache core is an account-scoped durable snapshot behind `ConversationRepository`; it must support fast cold-start presentation and rapid-relaunch request suppression without per-row Detail prefetching or a second list authority. Preview is a later enhancement that reuses the same store.
10. Before `DEV-attachments`, assistant-file download/share, image/file upload/send, or `DEV-download-manager` work, also read `ATTACHMENT_TRANSFER_PLAN.md`. Core attachment transfer is high-priority after accepted text Send/Stream; tap-download-share must not be blocked by a full download manager, and private upload/download protocol details must be evidenced rather than guessed.

Do not ask the user to upload project documents that already exist in this repository.

## Source of truth

Current real source and current task branch evidence take priority over stale documentation. Runtime/user test evidence takes priority over CI-only assumptions.

If the repository changed since docs were last updated, verify real state and proactively correct docs in the same work cycle.

## History

Do not require old chat exports as a normal startup dependency. Only consult historical material when current source and current project docs cannot resolve a specific historical question.
