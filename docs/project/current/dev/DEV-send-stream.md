# DEV-send-stream

## Status

**Active — exact scoped full navigation `/g/{scope}/c/{conversation}` is Runtime Positive for official page-owned continuation. Latest Web Rule Lab result closes the prior route ambiguity: after deliberately requesting the same already-visited project conversation through `/c/{conversation}`, official Web ended at the exact scoped canonical `/g/{scope}/c/{conversation}` route. This proves official Web can canonicalize an unscoped project route in at least a warm visible-Web state. It does not yet prove that a fresh/root production-like covered Web can do the same without prior project-route state. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Last verified PR head before this batch: `4ce3deec58fcfe03ce48bf86e96c0da7a26e3ae1`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 product / Artifact / IPA identity unchanged
- Stable/Frozen Send: No

## Runtime evidence

- `docs/project/runtime-evidence/DEV-send-stream-scoped-full-navigation-continuation-positive-20260903.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-project-canonical-anchor-20260903.md`

Current exact facts:

1. Control B: fresh full document navigation to exact official `/g/{scope}/c/{conversation}` with transient activation false starts page-owned `stream_status + plural_snapshot` continuation.
2. Official trusted project re-entry: sidebar anchor already contains `/g/{scope}/c/{conversation}` before navigation; page immediately issues project `stream_status` without a project Detail response supplying the scope.
3. Deliberate wrong-route probe in the same warm visible-Web session found exactly one visible exact scoped canonical anchor for the same conversation.
4. Final boolean route check now proves the post-navigation location itself is `EXACT_SCOPED_CANONICAL`: `currentIsExactScopedCanonical=true`, `currentIsExactUnscoped=false`, `currentIsProjectShape=true`, and the current conversation matches the saved target.
5. Therefore official Web can canonicalize `/c/{project-conversation}` back to `/g/{scope}/c/{conversation}` in this warm session.
6. This does **not** yet prove the fresh/root production-like covered Web has enough state to canonicalize the same way. b88 project failures remain evidence that current covered execution did not reach working continuation from its existing `/c/<conversationID>` path.
7. `gizmo_id` remains unverified as the route-source contract and must not be guessed.

## Next exact action

Run one final production-like Web Rule Lab control from a **fresh root document**: preserve the target project conversation ID/scope only in `sessionStorage`, full-navigate to `/`, then from that fresh root full-navigate directly to the unscoped `/c/{conversation}` while transient activation is false. Observe only whether official Web (a) canonicalizes to exact `/g/{scope}/c/{conversation}` and (b) starts page-owned continuation (`stream_status` / official snapshots) while the remote response is still active.

Decision:

- if fresh-root `/c/{conversation}` canonicalizes and continuation starts, current b88 failure is not explained by scoped-route identity alone; re-open covered-Web state differential before product code;
- if fresh-root `/c/{conversation}` does not canonicalize or canonicalizes without continuation while exact scoped Control B remains Positive, b89 may target deterministic official canonical-route acquisition/reload rather than guessed `gizmo_id`.

Do not allocate b89 before this production-like control. No guessed project endpoint, router internals, polling, timers, retries or Native continuation synthesis.

## Batch recovery state

New canonicalization-result docs batch started from verified PR head `4ce3deec58fcfe03ce48bf86e96c0da7a26e3ae1`.

- confirmed complete: this checkpoint recovery write;
- pending: extend `DEV-send-stream-official-project-canonical-anchor-20260903.md` with exact canonicalization result;
- pending: synchronize PR #29 title/body to the fresh-root final gate;
- pending: re-verify PR/head and close this checkpoint batch identity.

Do not touch product source, version/build, Candidate, Artifact or IPA in recovery.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 51**.
