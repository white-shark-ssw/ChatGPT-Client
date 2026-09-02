# DEV-send-stream

## Status

**Active — exact scoped full navigation `/g/{scope}/c/{conversation}` is Runtime Positive for official page-owned continuation. Latest Web Rule Lab evidence now also proves that after deliberately navigating toward the same project conversation through the unscoped `/c/{conversation}` form, the rendered official page exposes exactly one visible anchor for that same conversation using the exact scoped canonical `/g/{scope}/c/{conversation}` href. `gizmo_id` is not Runtime-confirmed. One final ambiguity remains before b89: the probe classified the resulting current route as `other`, so verify whether the official page already canonicalized the location itself back to the scoped route or whether the page stayed on another route while only exposing the canonical anchor. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Last verified PR head before this checkpoint write: `b13806e6ef50179acecc29e6a61facfbe246f302`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 product / Artifact / IPA identity unchanged
- Stable/Frozen Send: No

## Runtime evidence

- `docs/project/runtime-evidence/DEV-send-stream-scoped-full-navigation-continuation-positive-20260903.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-project-canonical-anchor-20260903.md`

Current exact facts:

1. Control B: fresh full document navigation to exact official `/g/{scope}/c/{conversation}` with transient activation false starts page-owned `stream_status + plural_snapshot` continuation.
2. Official trusted project re-entry: sidebar anchor already contains `/g/{scope}/c/{conversation}` before navigation; page immediately issues project `stream_status` without a project Detail response supplying the scope.
3. Deliberate wrong-route probe: after asking the same visible official Web session to navigate to `/c/{conversation}`, DOM inspection found:
   - `sameConversationLinkCount=1`;
   - `scopedConversationLinkCount=1`;
   - `exactCanonicalLinkCount=1`;
   - `exactCanonicalVisibleCount=1`;
   - `sameProjectScopeLinkCount=1`.
4. The same probe returned `currentRoute=other`, because its classifier only labeled an exact `/c/{id}` path and did not classify the actual post-navigation route. Therefore do not yet claim whether the page remained unscoped or automatically canonicalized to `/g/{scope}/c/{conversation}`.

## Next exact action

Run one privacy-safe boolean route check using the saved scope/conversation from the wrong-route probe. Return only whether current `location.pathname` is the exact unscoped target, the exact scoped canonical target, or another route. Do not reload, do not start another PC response, and do not expose raw IDs.

Decision after that check:

- if current location already equals exact scoped canonical route, investigate what current visible-Web state enabled automatic canonicalization and do not add redundant second navigation;
- if current location remains unscoped/other while the exact scoped anchor is present, canonical-anchor resolution becomes a directly evidenced b89 mechanism candidate; then verify the same canonical anchor is deterministically available in the covered production-like page state without manual sidebar expansion before product code.

Do not allocate b89 before this route ambiguity is closed. No guessed `gizmo_id`, router internals, project endpoints, polling, timers, retries or Native continuation protocol synthesis.

## Batch recovery state

This checkpoint write starts the new wrong-route-canonical evidence batch. Pending after this point: extend the existing canonical-anchor Runtime evidence with the exact wrong-route DOM counts; then verify PR/head identity. Do not touch product/version/Candidate/Artifact/IPA and do not replay earlier Control B or canonical-anchor writes.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 50**.
