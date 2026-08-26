# DEV-conversation-recovery

## Status

**Ready to merge — b15 Runtime/manual accepted on target iPhone/iOS17**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open pending final merge.
- **Base checked**: main `3a138ab6378fb72b9b36dedd3df55dc29e2ba814`; branch `behind_by=0`; PR mergeable before final docs update.
- **No competing Active development checkpoint/candidate** at the final conflict scan.

## Accepted runtime progression

- **b10**: core `同步最新消息` / full `重载当前会话` accepted; no resend/duplicate.
- **b12**: centered sync toast accepted; public `WKWebsiteDataStore.default()` warm-up accepted for persisted cold-start auth hydration.
- **b13**: immediate list start and stale-generation rejection worked; compact navigation failed and concurrent replacement detail requests produced HTTP429.
- **b14**: compact startup/navigation accepted; cold start lands on conversation list, duplicate sidebar icons removed, native list/detail navigation usable.
- **b15**: selected-detail cancellation/replacement accepted; old in-flight detail task is cancelled before one replacement request and the b13 overlap-driven HTTP429 did not reproduce.

## Final b15 identity

- Candidate `DEV-conversation-recovery-0.1.0-b15`
- Version / Build `0.1.0 (15)`
- Product/config head `159e8ea4f7baf6cd890d1f9bbebeac41feefbf52`
- CI run `33004536664` success
- Synthetic merge `fb0c6d75362e111758b62a98f89696b7f1cb6c92`
- Exact tested product/config tree `7a988bcad27d023eac77683985c5d7d92b22c176`
- Artifact `9619988065`, `ChatGPTClient-DEV-conversation-recovery-0.1.0-b15`
- IPA `ChatGPTClient-0.1.0-b15-dev-conversation-recovery.ipa`
- IPA SHA-256 `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`
- Artifact ZIP digest `sha256:cf4e8bce5a80bdd86bd9b8457b86c7a41de65d762c6ee158422760538faa50a7`
- Embedded source `fb0c6d75362e`, min iOS14.0, arm64.

## b15 real-device evidence

Exact b15 diagnostics on iPhone/iOS17 prove two independent manual replacement cases:

1. Conversation list position 6: ordinary generation 1 was active; manual reload requested replacement generation 2. `detail.cancel.requested` recorded cancelled=1/replacement=2, generation 1 ended `status=cancelled` after 2451.99 ms, generation 2 returned HTTP200 with 168 visible messages after 3861.52 ms, and `conversationReload.end` was `status=ok`.
2. Conversation list position 5: ordinary generation 3 was active; manual latest-sync requested generation 4. `detail.cancel.requested` recorded cancelled=3/replacement=4, generation 3 ended `status=cancelled` after 2352.66 ms, generation 4 returned HTTP200 with 591 visible messages after 5367.98 ms, and `latestSync.end` was `status=ok`.
3. No HTTP429 appears in these accepted replacement sequences.
4. User explicitly reported exact b15 had no issues.

## Accepted architecture / invariants

- `ConversationRepository` remains the single production conversation read/recovery owner.
- `AuthTransientSession.dataTask` only exposes the already-created transient `URLSessionDataTask`; auth/cookie/header/endpoint semantics are unchanged.
- Manual sync/reload may replace the current selected-detail request by cancelling the old task after the new generation takes ownership.
- Operation-generation rejection remains for late callbacks.
- No retry, timer, watchdog, fallback, resend/regenerate, hidden WebView or second state authority.
- b14 compact native navigation and b12 centered sync feedback remain accepted.

## Validation state

`DEV-conversation-recovery-0.1.0-b15` = **Code written + static/source review + CI passed + Artifact produced + Runtime/manual/real-device tested and accepted for the defined recovery scope**.

The Work is ready for final merge. After merge, move these conclusions to durable project docs, record the merge SHA, remove this checkpoint, and leave future `DEV-multi-conversation-state` as the next serialized development Work.
