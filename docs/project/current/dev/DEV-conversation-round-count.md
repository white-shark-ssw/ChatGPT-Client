# DEV-conversation-round-count

## Status

**Merged — exact b38 Runtime accepted; post-merge durable state sync/checkpoint removal pending**

- **Work ID**: `DEV-conversation-round-count`
- **Exact accepted product/config source**: `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- **Accepted Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- **Runtime Artifact**: `9708425762`.
- **IPA SHA-256**: `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- **PR #27**: merged successfully.
- **Actual merge commit / current main immediately after merge**: `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- **Merged PR head**: `57b3efe576dbf187171439a68d6d2dfe2fba0ebc`.
- **Merge base parent**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- **Stable/Frozen**: tested Phase 8 scope is eligible for Stable now that Runtime + merge are both complete; Frozen remains No. Final durable docs must record this before checkpoint deletion.

## Runtime truth

- b36 exact Runtime identified severe long-message/table geometry stutter, including ordinary right-side scroll-indicator dragging.
- b37 bounded long-message display chunks + deterministic row geometry/prefix offsets + manual cell layout removed the reported stutter; user: **“这次确实不卡了”**.
- b38 preserved that geometry and restored genuine continuous full-distance round animation; user: **“没问题了”**.
- No new diagnostics export accompanied b38 acceptance; do not invent numerical b38 Runtime timings.

## Accepted durable architecture

- `ConversationRepository` remains sole conversation/list/read/recovery authority.
- `ConversationMessagePresentationProjection` remains ephemeral presentation-only virtualization/geometry; it is not a second conversation store.
- Full-message Copy remains authoritative-message based.
- `ConversationRoundProjection` remains the sole derived round semantics; each visible authoritative user message starts a round.
- Accepted quick navigation uses the deterministic O(1) target offset and one cancellable `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)` from current viewport to target.
- Short/long distances use one method; rapid taps retarget from current visual position; real drag immediately retakes viewport ownership.
- b26 stale-row cap, b29 refresh/top-blank correction, b31 semantic landing, b32 filtering/compact Copy and b33 physical-bottom direction remain accepted Phase 8 behavior.
- Rich Markdown/citation rendering remains future `DEV-message-rendering`.

## Finalization batch recovery point

- Batch A durable acceptance sync: COMPLETE on feature branch before merge.
- Batch B final merge guard: COMPLETE. Exact b38 product source→final PR head delta was docs-only; current-head synthetic merge was clean.
- Batch C merge: COMPLETE. PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Batch D post-merge completion: IN PROGRESS.

Batch D exact remaining actions:

1. Update `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md`, `TECHNICAL_DECISIONS.md`, and `BUILD_TEST_INDEX.md` on `main` to record actual merge `9110c9e...`, Phase 8 **Stable / merged**, Frozen No, exact b38 Runtime identity/evidence, and next planned Phase 9.
2. Verify `main` after those docs-only writes.
3. Delete only `docs/project/current/dev/DEV-conversation-round-count.md`.
4. Verify `docs/project/current/dev/` contains only README unless another genuinely new Active Work appeared.

Do not rebuild/reuse b24-b38 identities and do not modify accepted product source during Batch D.
