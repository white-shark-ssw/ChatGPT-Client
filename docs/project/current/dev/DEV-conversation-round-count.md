# DEV-conversation-round-count

## Status

**Active — exact b38 Runtime accepted; durable sync + final merge guard complete; merge/post-merge cleanup pending**

- **Work ID**: `DEV-conversation-round-count`
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27.
- **Exact accepted product/config source**: `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- **Accepted Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- **Runtime Artifact**: `9708425762`.
- **IPA SHA-256**: `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable/Frozen before merge: No/No. Stable promotion waits only for merge/state sync; Frozen remains No.

## Runtime truth — accepted 2026-08-29

User tested exact b38 and replied **“没问题了”** after exact b37 had already been accepted with **“这次确实不卡了”**.

Accepted recorded iPhone/iOS17 behavior:

- b37 bounded long-message presentation + deterministic geometry removes the severe long-conversation and right-side scroll-indicator stutter reproduced in b36.
- b38 restores genuine continuous full-distance previous/next animation without reintroducing the reported stutter.
- Semantic target remains the authoritative user-message round start; target offset comes from O(1) deterministic presentation geometry.
- Rapid taps retarget through one transient semantic cursor + one cancellable animator; real drag immediately retakes viewport ownership.
- No hard final correction snap is required by the accepted path.

No new diagnostics export accompanied b38 acceptance; do not invent numerical b38 Runtime timings.

## Accepted durable architecture / behavior

- `ConversationRepository` remains sole conversation/list/read/recovery authority.
- `AuthSessionStore` remains sole verified auth/account authority; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `ConversationListCacheStore` remains storage-only.
- `AppPreferences` remains sole persisted settings owner.
- `ConversationRoundProjection` remains derived semantic round data; every visible authoritative user message starts one round.
- `ConversationMessagePresentationProjection` is ephemeral presentation-only virtualization: bounded plain-text chunks, deterministic row metrics/prefix offsets and message→first-row mapping derive from authoritative messages.
- `ConversationMessageCell` uses deterministic manual frame layout for bounded display chunks; Copy reads the complete authoritative visible message.
- b38 round navigation uses one `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)` from current viewport to deterministic target; short/long distances use one method.
- b26 stale-row cap, b29 top-refresh correction, b31 semantic landing, b32 filtering/compact Copy and b33 physical-bottom direction remain part of the accepted Phase 8 scope.
- Rich Markdown/citation rendering remains future `DEV-message-rendering`.

## Exact b38 evidence

- Product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Push Run / Job `33230823568` / `99043233637` — success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: `0.1.0 (38)`, Candidate b38, source `0d1801137e4e`, iOS14 minimum, arm64.
- Runtime/manual/real-device: **Accepted** on recorded iPhone/iOS17 scope.

## Finalization batch recovery point

### Batch A — durable acceptance sync: COMPLETE

Updated `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md`, `TECHNICAL_DECISIONS.md`, and `BUILD_TEST_INDEX.md` to b38 Runtime-accepted truth. Product code/config untouched.

### Batch B — final merge guard: COMPLETE

Verified immediately before merge:

- Real development head before this checkpoint write: `61a2d35407e0efb7e96b069759bec0c501deea1a`.
- Main unchanged: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- PR #27: open, not merged, `mergeable=true`, head `61a2d354...`, base `main@a6e3b2bc...`.
- Exact product source `0d180113...` -> current head compare: 12 commits ahead, **only eight `docs/project/` files changed** (`PROJECT_PROFILE`, `PROJECT_STATE`, `MODULE_STATUS`, `PROJECT_SPECIFIC_RULES`, `DEVELOPMENT_PLAN`, `TECHNICAL_DECISIONS`, `BUILD_TEST_INDEX`, this checkpoint). No product/config/source drift after tested b38.
- `docs/project/current/dev/` still contains only this Active checkpoint plus README; no parallel Work conflict.
- Fresh current-head/current-main GitHub synthetic merge: `8d9e0f107b2a058625e5cc7fa2c8673b4a3b7413`, message explicitly `Merge 61a2d35407e0efb7e96b069759bec0c501deea1a into a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Since post-Runtime changes are docs-only, exact b38 product CI/Artifact/Runtime evidence remains applicable; no product rebuild is required by this merge guard.

### Batch C — merge: PENDING

Merge PR #27 only with exact expected current PR head after this checkpoint commit is accounted for. Because this checkpoint write itself advances the branch by docs only, re-read PR head immediately before merge and use that exact SHA in `expected_head_sha`.

### Batch D — post-merge completion: PENDING

On merged `main`, record actual merge SHA/current main and Stable/Frozen state in durable docs, then remove only this checkpoint.

Recovery next exact action: re-read PR #27 once after this docs-only checkpoint commit, confirm mergeable/base unchanged and merge with exact expected head. Do not replay Batch A/B and do not touch/rebuild b38 product identity.

## Evidence boundary

- Code written: Yes.
- Static/source audit: Passed.
- Exact push CI: Passed.
- Identity-valid Artifact: Produced and independently verified.
- Runtime/manual/real-device: **Accepted**.
- Stable: Pending final merge/state sync.
- Frozen: No.
