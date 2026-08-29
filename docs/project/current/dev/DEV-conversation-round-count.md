# DEV-conversation-round-count

## Status

**Active — exact b38 Runtime accepted; durable acceptance sync complete; final merge guard/merge/post-merge cleanup pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27.
- **Exact accepted product/config source**: `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- **Accepted Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- **Runtime Artifact**: `9708425762`.
- **IPA SHA-256**: `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable/Frozen before merge: No/No. Stable promotion waits only for final merge/state sync; Frozen remains No.

## Runtime truth — accepted 2026-08-29

User tested exact b38 and replied **“没问题了”** after exact b37 had already been accepted with **“这次确实不卡了”**.

Accepted recorded iPhone/iOS17 behavior:

- b37 deterministic message geometry / bounded long-message presentation removes the severe long-conversation and right-side scroll-indicator stutter reproduced in b36.
- b38 restores genuine continuous full-distance previous/next animation without reintroducing the reported stutter.
- Quick navigation remains semantically targeted at authoritative user-message round starts and consumes O(1) deterministic target offsets.
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
- `ConversationMessageCell` uses deterministic manual frame layout for bounded display chunks; Copy still reads the complete authoritative visible message.
- b38 round navigation uses one `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)` from current viewport to deterministic target; short/long distance use one method.
- b26 authoritative-total stale-row cap (`30 -> 29`, repeated `29/29`), b29 right-top refresh/top-blank correction, b31 semantic user-row landing, b32 filtering/compact Copy and b33 physical-bottom direction remain part of the accepted Phase 8 scope.
- Rich Markdown/citation rendering remains future `DEV-message-rendering`.

## Exact b38 evidence

- Exact product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact push Run / Job `33230823568` / `99043233637` — success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: `0.1.0 (38)`, Candidate b38, source `0d1801137e4e`, MinimumOSVersion 14.0, arm64.
- Product-head merge-view Run / Job `33230825189` / `99043238346` succeeded on synthetic merge `fd1ed7508f04e9045b99239cad88dca8f6e01450` against then-current `main@a6e3b2bc...`; later docs-only commits require a fresh current-head merge check.
- Runtime/manual/real-device: **Accepted** on recorded iPhone/iOS17 scope.

## Finalization batch recovery point

### Known identity

- Exact tested product source remains `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67` regardless of later docs-only commits.
- Main last verified before Batch B: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- `docs/project/current/dev/` contained only this Active Work plus README; no parallel development conflict at last check.
- Exact b24-b38 identities are reserved and must never be rebuilt/reused.

### Batch status

- **Batch A — durable acceptance sync: COMPLETE.** Updated `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md`, `TECHNICAL_DECISIONS.md`, and `BUILD_TEST_INDEX.md` to b38 Runtime-accepted truth. Product code/config untouched.
- **Batch B — final merge guard: PENDING.** Re-read real branch head, main, PR #27 and active checkpoints; compare exact product source→current branch and verify only docs changed; obtain fresh current-head/current-main synthetic merge/mergeability evidence.
- **Batch C — merge: PENDING.** Merge PR #27 only if Batch B is clean, using exact expected current head SHA.
- **Batch D — post-merge completion: PENDING.** On main, record actual merge SHA/current main and Stable/Frozen state, then remove only this checkpoint.

Recovery next exact action: perform Batch B only. Do not replay Batch A and do not touch product source/Candidate identity.

## Evidence boundary

- Code written: Yes.
- Static/source audit: Passed.
- Exact push CI: Passed.
- Identity-valid Artifact: Produced and independently verified.
- Runtime/manual/real-device: **Accepted**.
- Stable: Pending final merge/state sync.
- Frozen: No.
