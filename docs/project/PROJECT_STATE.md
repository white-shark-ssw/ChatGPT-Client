# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: **merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope**. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

`DEV-multi-conversation-state` remains Active. b17 has accepted core multi-conversation Runtime evidence and reproduced the historical-scroll defect. Exact b18 now has Code + static/source + CI + identity-valid Artifact + **real-device historical-scroll Runtime acceptance for the tested iPhone/iOS17 matrix**. The Work is still not Stable/Frozen because failure/account-switch/normal-LRU and one isolated replacement gate remain open.

Current `main` head is `2c33dacbefa613292eb89cbf606b0172a241e81e`. It advanced after b18 Artifact through docs-only message-timestamp planning (`DEVELOPMENT_PLAN.md`, `START_HERE.md`, `UI_INTERACTION_BASELINE.md` only); exact b18 product/runtime evidence remains tied to source `f30c13b4ac2c40dcda829585682825ca906dceae` and is not invalidated. Synchronize before final merge.

## Recovery completion

Final candidate: `DEV-conversation-recovery-0.1.0-b15`, version `0.1.0 (15)`.

- Product/config head `159e8ea4f7baf6cd890d1f9bbebeac41feefbf52`.
- CI Run `33004536664`; Artifact `9619988065`.
- IPA SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`.
- Validation: **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted**.

## Active Work — DEV-multi-conversation-state

- **Branch / PR**: `dev/multi-conversation-state-20260827`; PR not created.
- **b16**: historical/rejected before runtime; never reuse.
- **b17**: exact source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; Run `33045536770`; Artifact `9635486304`; core resident/coalescing/hidden-Sync/rapid-overlap Runtime accepted; P1 historical-scroll defect reproduced.
- **Current exact Candidate**: `DEV-multi-conversation-state-0.1.0-b18`, `0.1.0 (18)`.
- **Product/config source**: `f30c13b4ac2c40dcda829585682825ca906dceae`; tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- **Implementation**: lightweight per-conversation historical-reading anchor in `ConversationDetailViewController`, represented by message identity + relative visual offset. No global raw offset; no second conversation/response owner. Account reset clears anchors. Sync/Reload preserve only if the same anchor message remains.
- **Ownership boundary**: `ConversationRepository`, `AuthSessionStore`, protocol/network routes and current-node authority are unchanged. No fake Send/Stream state, retry, timer, fallback, watchdog or global rate limiter.
- **CI**: Run `33054012226`, Job `98456174184`, success; Xcode16.4; `arm64-apple-ios14.0`; exact b18 candidate/source.
- **Artifact**: `9638821912`; ZIP `sha256:36b59b8c4d3bdcadedd463a3554528452ff46478651671b50f4bd9f7fa2b5d2c`.
- **IPA**: `ChatGPTClient-0.1.0-b18-dev-multi-conversation-state.ipa`; SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.
- **Exact real-device identity**: iPhone / iOS17.0 / candidate b18 / build 18 / source `f30c13b4ac2c`.

### b18 real-device result

User executed the requested matrix and reported no issue. Diagnostic review records:

- 195 events, all level `info`;
- 21 `scrollAnchor.saved`, 19 `scrollAnchor.restored`;
- 17 `resident.hit`, 17 `resident.firstVisible`;
- all 17 recorded HTTP statuses are HTTP200;
- no error, no HTTP429, no `scrollAnchor.discarded` in this run.

Accepted for the observed/tested scope:

- A -> B -> A restores A's historical semantic/visual anchor.
- A and B preserve independent anchors over repeated switching.
- first-time third conversation does not inherit prior A/B offset.
- visible Sync preserves anchor when anchored message remains.
- B Sync survives B -> A -> B and re-coalesces to the same active target operation before hidden HTTP200 completion.
- Reload A preserves the same anchor after HTTP200 when anchored message remains.
- resident return still avoids navigation-only Detail refetch.

Runtime-unexercised conditional path: anchored message disappearance -> `scrollAnchor.discarded` -> top. No destructive branch mutation was manufactured solely to trigger it.

### Validation labels

- **Code written**: Yes.
- **Static/source checks**: Passed.
- **CI passed**: Yes.
- **Artifact produced**: Yes, identity accepted.
- **Runtime/manual/real-device**: **Passed for exact b18 historical-scroll/Sync/Reload-preservation/resident-regression matrix on iPhone/iOS17**.
- **Stable/Frozen**: **No**.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation data/read/recovery owner with account-scoped per-conversation residents/operations.
- `ConversationDetailViewController`: detail/messages/recovery presentation plus lightweight per-conversation historical scroll presentation metadata.
- Default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole account/auth context owner.
- Historical anchor and future active-response `follow-tail` are distinct. Follow-tail must consume the future authoritative per-conversation Send/Stream response owner; b18 does not implement fake response activity.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — Completed / merged / Stable b15.
2. `DEV-multi-conversation-state` — Active; b18 historical scroll Runtime accepted; remaining owner/memory acceptance below.
3. Continue durable post-recovery roadmap from current `DEVELOPMENT_PLAN.md`; current `main` also contains message-timestamp/display-preference planning.
4. `DEV-send-stream` remains the point where real response ownership/follow-tail can become runtime-testable.

## Known issues / open acceptance

- Isolated same-target Reload replacement while an older Detail is actually in flight remains open as a multi-conversation regression spot-check; b15 remains accepted replacement-under-load baseline.
- Terminal failed resident navigation with no implicit retry remains open until a natural terminal failure is available.
- Supported account-context purge/late-callback isolation still requires a real supported account-switch/logout route.
- Normal resident/LRU capacity remains Unknown until real **process/system memory** evidence; approximate visible-text bytes are not capacity evidence.
- Missing-anchor-message discard is source/CI-defined but not runtime exercised in b18.
- Runtime below iOS17, iPad, non-personal workspace, Send/Stream and attachments remain Unknown / Unverified as applicable.
- No XCTest/UI-test target exists.

## Next exact action

Collect real iPhone process/system memory evidence while several small and large conversations remain resident and are repeatedly switched. Do not choose normal LRU capacity from approximate visible-text bytes. Do not change product code solely to guess a capacity before that evidence exists.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. CI/Artifact success is not runtime proof.
