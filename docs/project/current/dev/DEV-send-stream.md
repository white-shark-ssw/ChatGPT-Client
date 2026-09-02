# DEV-send-stream

## Status

**Active — exact b86 Runtime is Diagnostic Positive / continuation activation absent. b85 authoritative Detail block projection remains Runtime Positive, but the covered official page issued no matching `stream_status`, `/resume`, page-owned snapshot or SSE for at least 75 seconds after a clean manual re-arm while authoritative Detail proved active reasoning existed. In the same run the user-socket exact-target completion hint also did not fire (`targetMatch=false`), so the completed assistant message appeared only after a later explicit Sync. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b85 exact product/config source: `ec64dd170a6386612af8cb68b394045ce3c85313`
- b85 Runtime: **manual authoritative block projection Positive / automatic continuation Rejected**
- b86 exact diagnostics product source: `dc77a94be5b2f7eecd822480f759358ad6a0ad25`
- b86 clean package head: `f90caca0419f13254567485171fac7d970aa8c95`
- b86 Candidate / Build: `DEV-send-stream-0.1.0-b86` / `0.1.0 (86)`
- b86 Push: `33566939415 / 100052171917` — passed
- b86 PR: `33566968066 / 100052259409` — passed
- b86 Artifact: `9823485856`
- b86 ZIP: `sha256:cdccdcd034964b99e98e62c2e79a9bece96c190138c774e6f1590896d54fbacb`
- b86 IPA: `sha256:25d483ac31473b124e6ad555b79c488e78da91ec1761ee8a40076b6e978bee6f`
- b86 Runtime export: exact Candidate b86 / source `f90caca0419f` / iPhone / iOS17.0
- b39-b86 permanently reserved
- Stable/Frozen Send: No

## Send MVP contract

Client-owned Send keeps true same-response SSE. Cross-platform MVP may use real block/page snapshots, but one explicit Sync must be a stable acquisition boundary and later genuine blocks should continue without pressing Sync for every block when a real page-owned continuation attaches.

Do not satisfy this with fake typewriter, polling, timer, watchdog, speculative retry/fallback, duplicate Send/resend, a second response store, guessed Native resume/offset, WebSocket-body authority, or raw hidden-thought presentation.

## b86 decisive Runtime

Target privacy-safe conversation hash: `sha256:d597360f6d29`.

- `07:15:10` explicit Sync started.
- `07:15:20` authoritative Detail HTTP200 returned visible `34`, trailing timeline `6 = reasoning 1 + tools 5`.
- `responseGeneration=1` started from `external_authoritative_detail` and one live row rendered.
- `07:15:21` `manual_sync_rearm`; `07:15:22` covered page loaded.
- From that load until the next explicit Sync at `07:16:37` (~75 seconds), there were zero `externalStreamStatus*`, `externalResume*`, `externalStreamingObserved`, or page-owned/Repository snapshot events.
- User WebSocket emitted a structural message with `hasConversationKey=false`, `targetMatch=false`; current exact-target completion hint did not fire.
- `07:16:37` user pressed Sync again.
- `07:16:43` Detail returned visible `35`, trailing `0`; `externalDetailReconciled(reason=authoritative_assistant_materialized)` cleared the live row.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b86-no-continuation-no-final-auto-convergence-20260902.md`.

## Current conclusion

b86 resolves the prior fork: the covered page did **not** request `stream_status` at all during the clean observation window. The bottleneck is before resume/offset and before page-owned plural reads: **official page continuation activation itself**.

The lack of automatic final answer is separately explained by the current completion/update trigger also not firing: the user-socket structural frame did not match the target conversation. The b82 exact-target WebSocket hint is opportunistic, not reliable convergence.

Recorded visible Web Rule Lab evidence uses the same default persistent `WKWebsiteDataStore`. When the user visibly entered an externally active target conversation, official Web issued matching `stream_status` within roughly two seconds, then page-owned `/resume {conversation_id, offset}` and, after a 404, repeated page-owned `stream_status + /backend-api/conversations/{conversation}` reads.

Exact b86 covered programmatic `/c/<id>` load differs materially. This strengthens the working hypothesis that server capability is not the primary blocker; the likely differential is page activation/navigation/visibility/focus state, but the exact causal field/action remains Unverified.

## Next exact action

Before behavioral changes, diagnose the covered page activation state against the known-good visible Web entry path, limited to privacy-safe structure:

- `document.visibilityState` / `document.hidden`;
- `document.hasFocus()`;
- route/readiness shortly after `didFinish`;
- Native WebView window attachment / hidden / alpha / bounds intersection;
- whether a genuinely user-visible navigation/activation transition is what causes official Web to issue `stream_status`.

Do not call `stream_status` natively, guess `/resume` offset, add retry/polling, or make full Web UI a product dependency.

## Recorded later requirement

Entering/selecting a conversation should eventually perform exactly one authoritative latest-message Sync through `ConversationRepository`. This remains separate from continuation and does not keep an active external response current by itself.

## Frozen / preserved boundaries

- b80 tool/timeline -> reasoning-divider spacing: Frozen.
- external stopped-thinking semantics: Frozen.
- b80 final-materialization gate: preserve.
- b67 client-owned protected Send and b72 tested simultaneous ownership: preserve.
- `ConversationRepository` remains sole Native response/content authority.
- `AuthSessionStore` remains sole native auth/account authority.
- default persistent WebKit store remains sole persistent auth-secret authority.
- no raw hidden-thought presentation.

## Evidence ladder

- b83 covered-page manual acquisition: **Runtime Rejected**
- b84 active authoritative trailing timeline: **Runtime Positive**
- b85 explicit manual Detail block projection: **Runtime Positive**
- b85 repeated Sync same response generation: **Runtime Positive**
- b85 final reconcile when Detail is fetched: **Runtime Positive**
- b85 automatic continuation: **Runtime Rejected**
- b86 Code/Push+PR CI/Artifact/package: **Verified**
- b86 continuation-structure diagnostics: **Runtime Positive**
- b86 page-owned continuation activation: **Absent in exact run**
- b86 automatic final convergence: **Absent in exact run; final materialized only after manual Sync**
- b86 true cross-platform SSE: **Not acquired**
- Stable/Frozen Send: **No**

## Batch recovery point — b86 Runtime documentation

Known branch before the mistaken index write: `c5b4d0bd9ded4efd228532b5c850137a1920bea3`.

Completed:
1. Durable b86 Runtime evidence created.
2. Checkpoint updated with b86 Runtime conclusion.
3. A mistaken whole-file `BUILD_TEST_INDEX.md` replacement at commit `8436d4529aa2c5b476d59a5f083e3a99e0e6ff48` truncated historical rows; this is a documentation-only error.
4. A repair commit object `49905f8b4a686487f9651cef683dd2d1dbf39165` was created whose tree restores `docs/project/BUILD_TEST_INDEX.md` to exact prior blob `55673bc3f855bbe843c54d5095509037f0f69245` while preserving the b86 evidence/checkpoint commits.

Pending:
1. Move branch ref to repair commit `49905f8b4a686487f9651cef683dd2d1dbf39165` if it has not already been moved.
2. Verify full BUILD_TEST_INDEX history is restored.
3. Update only the b86 row using a non-destructive exact-line patch method.
4. Update PR #29 to b86 Runtime gate.

Must not touch during recovery: b86 product/config source, Artifact identity, b85 accepted Detail projection, client-owned SSE, Frozen presentation/final boundaries.

## Session round counter

This user turn is **round 19**.
