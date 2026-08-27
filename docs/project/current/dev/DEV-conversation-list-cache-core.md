# DEV-conversation-list-cache-core

## Status

**Active — b23 real-device cache-core Runtime accepted for tested Plus/personal iPhone/iOS17 scope; ready for PR/merge preparation**

- **Work ID**: `DEV-conversation-list-cache-core`
- **Routing aliases / keywords**: `持久化会话列表缓存核心 / 会话列表缓存核心 / 列表缓存 / conversation list cache core`
- **Task**: Add the first account-scoped persistent conversation-list snapshot and rapid-relaunch automatic-refresh suppression behind the existing authoritative `ConversationRepository`.
- **Baseline / synchronization**: branch was created from `main@76d88794e9bc0dff9860ace3ad496e319355ee08` and synchronized with current `main@846dad81e382e6b7a862f082ef5bc5d4ce617493` via two-parent merge `27a107b9f993302743e6cfb45800ed12c9499643`. Main was rechecked before b23 allocation and remains `846dad81e382e6b7a862f082ef5bc5d4ce617493` at this Runtime checkpoint.
- **Working branch / PR**: `dev/conversation-list-cache-core-20260828`; PR not created. Branch head immediately before this Runtime-doc update: `6bf0156fa87ded90014195e1e20c69da5982cc95`.
- **Exact accepted Runtime Candidate**: `DEV-conversation-list-cache-core-0.1.0-b23` / `0.1.0 (23)`; exact product/config source `d2af0fc157f6e2d037636c55f963c18071a332d5`; corrected product source `7bb6d116d785614dccf0e2a2b412d2823ad583e1`.
- **Exact b23 CI / Artifact**: Run `33101116431`, Job `98618762016`, success; Artifact `9658508764`; outer ZIP `sha256:fa57e557a484f98b06753ce3f09fe4cdd89d390ea00a8778e052a518a560776b`; IPA `ChatGPTClient-0.1.0-b23-dev-conversation-list-cache-core.ipa`; IPA SHA `8f6911616fff1e93885191fcaec0f31a1e3c9488b7f4522fdbdb7dc5518be516`. Package inspection: `0.1.0 (23)`, arm64, minimum iOS14.0, device families `[1,2]`, Candidate/source metadata match `d2af0fc157f6`.
- **Historical b22**: `DEV-conversation-list-cache-core-0.1.0-b22` remains permanently reserved and Runtime-partial/failing. It proved disk snapshot write/read, 60-second `recent_skip`, stale one-refresh and manual-bypass mechanics, but visible cache publication happened only after ~4.4–5.0s account verification, offline auth failure bypassed cache, and manual refresh lacked explicit terminal UI feedback. Corrected code must never reuse b22.

## b23 implementation / ownership

- Product correction is confined to `ChatGPTClient/Conversation/ConversationFeature.swift`; candidate identity also changes Xcode build settings, workflow and `scripts/build_ipa.sh`.
- `ConversationRepository` remains sole authoritative in-memory list/conversation owner and main-thread mutation domain.
- `AuthSessionStore` is unchanged and remains sole verified auth/account authority; default persistent WebKit storage remains sole persistent auth-secret authority.
- `ConversationListCacheStore` persists schema-1 list snapshots plus `last-verified-scope.txt` containing only the existing 64-hex SHA-256 cache namespace. No raw user/account IDs, cookies, tokens, bearer values, Detail mappings or message bodies are persisted.
- Automatic cold start may provisionally publish the last successfully verified scope's cached **list titles** before current network account verification completes. This provisional cache is not account/transport authority.
- A different subsequently verified scope rejects/clears the provisional presentation; confirmed auth unavailability rejects it; temporary transport failure may retain it without retry.
- Provisional/offline rows are list-only and cannot start Detail until current scope is actually verified. Tapping them reports `当前仅显示缓存，联网验证账户后可打开会话`.
- Manual refresh bypasses freshness suppression and provides visible navigation prompt feedback: `正在刷新会话列表…`, success `已刷新 · N 条`, failure with retained rows `刷新失败 · 当前显示缓存`.
- No retry/timer/watchdog/polling, alternate endpoint, second repository/list owner or auth-secret persistence was added.

## b23 Runtime evidence — user supplied exact iPhone/iOS17 diagnostics + screenshot

- Export metadata identifies build `23`, Candidate `DEV-conversation-list-cache-core-0.1.0-b23`, source `d2af0fc157f6`, iPhone, iOS17.0, Plus/personal scope.
- First successful b23 online launch establishes/migrates cache bookkeeping. The stale 28-entry snapshot (`ageSeconds=2463.43`) is loaded, one normal list request returns 28 with server `totalCount=29`, reconciliation records `insertedCount=1`, `preservedOffPageCount=1`, `resultCount=29`, and the 29-entry snapshot is written successfully.
- Rapid relaunch at `18:15:26Z`: `listCache.provisional.completed` hits 29 entries in `4.09 ms` at age `18.32s` **before** account verification finishes (~4521 ms). After matching verification, the already-published cache remains (`published=false` on the second scoped load), decision is `recent_skip`, and `networkRequest=skipped`.
- Another rapid relaunch at `18:15:37Z` with network unavailable: provisional 29-entry cache loads in `4.30 ms`; auth fails naturally with `NSURLErrorDomain -1005`; repository chooses `offline_cache`; `listLoad` completes `status=ok`, source `cache`, 29 items in `31.58 ms`. No login/account-verification overlay replaces the list.
- Offline manual refresh at `18:15:41Z` fails naturally at auth with `-1005`; the screenshot confirms the list remains visible and the centered navigation prompt above the `ChatGPT` title shows `刷新失败 · 当前显示缓存`.
- Online manual refresh at `18:16:08Z` uses `manual_bypass`, emits exactly one `list.request`, receives HTTP200, preserves the off-page item (`pageCount=28`, `preservedOffPageCount=1`, `resultCount=29`) and writes cache successfully. A second manual refresh at `18:16:21Z` again emits exactly one request and preserves the same 29-row result.
- Direct user result: `好像没问题了`; no new functional defect reported in this b23 matrix.

## Acceptance / evidence boundaries

Accepted on exact b23 for tested Plus/personal iPhone/iOS17 scope:
- immediate provisional cached list before slow account verification;
- recent rapid-relaunch automatic list-request suppression;
- stale cache one-refresh path;
- offline cold-start cache preservation without login overlay or automatic retry;
- manual refresh bypass request mechanics;
- visible offline refresh-failure feedback with retained rows;
- first-page-28 safety preserving one genuinely off-page cached item;
- small snapshot I/O (observed ~1–20 ms scoped reads/writes; provisional reads ~4 ms).

Still **Unknown / Unverified** unless naturally exercised later:
- supported real account-switch / verified-scope-mismatch Runtime transition;
- provisional cached-row tap/Detail-block guard Runtime (source/CI-defined, no supplied tap sequence);
- corrupt/schema-incompatible snapshot Runtime rejection;
- iPad, iOS below 17, non-personal workspace identity.

These conditional boundaries do not contradict the accepted tested b23 scope and do not justify manufacturing fake account transitions or corrupting user data solely to fill a matrix cell.

## Validation state

- **Code written**: Yes.
- **Static/source review**: Passed.
- **CI passed**: Yes — exact b23 Run `33101116431` / Job `98618762016`.
- **Artifact produced**: Yes — exact identity-valid b23 Artifact `9658508764`.
- **Runtime/manual/real-device**: **Accepted for the recorded b23 cache-core matrix on Plus/personal iPhone/iOS17**.
- **Stable**: **Not yet merged; do not mark merged Stable before PR/merge evidence**.
- **Frozen**: No.

## Next exact action

Update durable cache/project/build evidence to b23 Runtime truth, then prepare PR/merge from `dev/conversation-list-cache-core-20260828` against current `main`, re-check target advancement and run PR merge-view CI as required. Do not change product code without new defect evidence.