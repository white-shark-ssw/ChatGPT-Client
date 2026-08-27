# DEV-multi-conversation-state

## Status

**Active — exact b18 historical scroll restoration is real-device accepted for the tested iPhone/iOS17 matrix; b17 core multi-conversation evidence remains accepted; Work is not Stable/Frozen because failure/account-switch/normal-LRU and one isolated replacement gate remain open**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 Send/Stream 所需的多会话 freshness、异步所有权与轻量 per-conversation presentation 基线。
- **Stable product baseline**: `DEV-conversation-recovery-0.1.0-b15`, version `0.1.0 (15)`.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; PR `Not created`.
- **Current target branch**: `main@2c33dacbefa613292eb89cbf606b0172a241e81e`; this advanced after b18 Artifact through a docs-only message-timestamp planning merge. It changed only `DEVELOPMENT_PLAN.md`, `START_HERE.md`, and `UI_INTERACTION_BASELINE.md`, so it does not invalidate exact b18 product/runtime evidence. Synchronize before final merge.
- **Current exact Candidate**: `DEV-multi-conversation-state-0.1.0-b18`, version `0.1.0 (18)`.
- **Exact b18 product/config source**: `f30c13b4ac2c40dcda829585682825ca906dceae`; tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- **Artifact**: `9638821912`; IPA `ChatGPTClient-0.1.0-b18-dev-multi-conversation-state.ipa`; IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`.

## Candidate history

### b16 — historical / rejected before runtime

- Exact source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; CI Run `33009246356` succeeded.
- Artifact `9621830284` embedded wrong recovery candidate/slug and is permanently rejected/superseded before runtime.
- Source review also found stale-scope, waiter, hidden-Sync, list-freshness, task-handle and owner-domain gaps.
- Never reuse b16.

### b17 — identity-valid / core runtime accepted

- Exact product/config source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; tree `3451585f83c7bac69368709fe6273b90a0294d29`.
- CI Run `33045536770`, job `98428537619`, success; Artifact `9635486304` identity accepted.
- iPhone/iOS17 runtime accepted resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin and rapid different-conversation overlap up to three active operations with no HTTP429 in that export.
- User reproduced P1 historical scroll defect: A near ~10% -> B scroll -> A returned shifted.

### b18 — historical semantic scroll correction / runtime accepted for tested matrix

#### Code / ownership boundary

- `ConversationRepository`, auth owner, protocol/network routes and current-node ownership are unchanged.
- `ConversationDetailViewController` owns lightweight per-conversation historical scroll presentation metadata only.
- Anchor representation is message identity + relative visual offset; no global raw `contentOffset` is copied between conversations.
- `displayedConversationID` captures the actually displayed outgoing conversation even after repository selection changes.
- No-anchor target starts from normal top; account-scope reset clears anchors.
- Visible Sync/Reload preserves the anchor only when the same anchored message remains in the refreshed current branch.
- Missing anchor message discards to top instead of guessing another message.
- Diagnostics: privacy-safe `scrollAnchor.saved`, `scrollAnchor.restored`, `scrollAnchor.discarded`; no raw message IDs/bodies/titles/secrets.
- No fake `isStreaming`, response owner, timer, retry, fallback, watchdog, global rate limiter or speculative follow-tail state.

#### Static / CI / Artifact

- `ConversationFeature.swift` blob `daf60d76b1295a9662a119b28766511039a52e8e`.
- Exact product diff contains only workflow, Xcode project, `ConversationFeature.swift`, and `scripts/build_ipa.sh`.
- Run `33054012226`, Job `98456174184`: success on Xcode16.4; exact checkout `f30c13b4ac2c40dcda829585682825ca906dceae`; `arm64-apple-ios14.0`; `BUILD SUCCEEDED`.
- Artifact `9638821912`; ZIP `sha256:36b59b8c4d3bdcadedd463a3554528452ff46478651671b50f4bd9f7fa2b5d2c`.
- IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`; independent sidecar/package identity matches embedded `0.1.0 (18)`, b18, source `f30c13b4ac2c`, iOS14.0 minimum, `[1,2]`, arm64.

## Exact b18 real-device evidence — 2026-08-27

User installed exact b18 on iPhone/iOS17, executed the requested scroll/regression matrix and reported **no problem found**. Supplied diagnostics metadata independently identifies:

- candidate `DEV-multi-conversation-state-0.1.0-b18`;
- build `18` / app `0.1.0`;
- source `f30c13b4ac2c`;
- device class `iPhone` / iOS `17.0`.

Diagnostic review:

- 195 exported events, all level `info`.
- 17 events carrying HTTP status are all HTTP200.
- no error event, no HTTP429, no `scrollAnchor.discarded` in this run.
- `scrollAnchor.saved`: 21 events; `scrollAnchor.restored`: 19 events.
- `resident.hit`: 17; `resident.firstVisible`: 17; no navigation-only refetch observed for already-resident return.
- Three conversations were loaded/resident during the run.

### b18 acceptance matrix result

1. **Historical A -> B -> A restoration: PASSED.** Multiple returns restore the exact saved row/relative offset for A; examples include row `6` / `79.00`, row `7` / `2.33`, then later row `7` / `2.67`.
2. **Independent A/B anchors over repeated switching: PASSED.** B independently restores row `1` / `124.33`, row `7` / `54.00`, row `21` / `152.67` and later row `22` / `4.67`, while A restores its own distinct anchors.
3. **First-time/no-anchor C starts normally: PASSED for observed/user-tested behavior.** C first appears as `resident.miss` and starts its own Detail load with no prior `scrollAnchor.restored`; it only receives its first saved anchor when later leaving C. User reported no inherited-position problem.
4. **Visible Sync preserves historical anchor when message remains: PASSED.** A Sync HTTP200 retains `row 7 / 2.33` across saved->restored. A later B Sync survives B->A->B, return restores B `row 21 / 174.67`, `detail.coalesced completionCount=2` confirms rejoin, and Sync completes HTTP200 while hidden.
5. **Reload preserves historical anchor when message remains: PASSED.** Before Reload A saves `row 7 / 2.33`; Reload generation 3 completes HTTP200 and restores the same `row 7 / 2.33`.
6. **b17 core regression spot-check: PASSED for observed paths.** Resident returns remain `resident.hit` without navigation-only Detail requests; active same-target Sync return coalesces instead of duplicating the operation; hidden Sync completion is stored target-specifically.
7. **Missing-anchor-message discard path: UNVERIFIED at runtime.** No natural branch change removed an anchored message, so no `scrollAnchor.discarded` occurred. Source/CI contract remains accepted but this run does not claim device proof of that conditional path.

## User-confirmed future Send/Stream scroll semantics

- Per-conversation presentation distinguishes **historical-reading anchor** from future **follow-tail** intent.
- If A is at/near bottom and has an authoritative active response, hidden growth/completion must make return-to-A land at A's current latest bottom.
- Intentional upward scrolling while A generates exits follow-tail and later restores historical reading position.
- B scrolling never mutates A presentation state and hidden A growth never mutates B.
- b18 intentionally does not invent response lifecycle state; follow-tail becomes runtime-testable only after the real per-conversation Send/Stream response owner exists.

## Evidence labels

### b18
- **Code written**: Yes — exact source published.
- **Static/source checks**: Passed.
- **CI passed**: Yes — Run `33054012226`, Job `98456174184`.
- **Artifact produced**: Yes — Artifact `9638821912`, identity independently accepted.
- **Runtime/manual/real-device**: **Passed for the tested historical-scroll / Sync / Reload-preservation / resident-regression matrix on exact iPhone/iOS17 b18**.
- **Stable/Frozen**: **No**.

## Remaining Work before Stable

- Isolated target-only Reload replacement while older same-target Detail is actually in flight remains open as a multi-conversation regression spot-check; b15 remains accepted replacement-under-load baseline.
- Terminal failed resident A -> B -> A with no implicit retry remains open until a natural terminal failure is available; do not manufacture unsafe failure conditions.
- Supported account-switch/logout purge and late-callback rejection remain runtime-open until a real supported route exists.
- Normal resident capacity/LRU remains Unknown until real **process/system memory** evidence exists; approximate visible-text bytes cannot select capacity.
- Non-personal workspace isolation remains Unknown / Unverified.
- Missing-anchor-message discard remains runtime-unexercised but source/CI-defined; do not manufacture a destructive branch mutation solely to test it.

## Next exact action

**Do not change product code yet. Collect real iPhone process/system memory evidence while several small and large conversations remain resident and are switched repeatedly. Use that evidence to decide whether a bounded normal LRU policy is needed now and, if so, what capacity is defensible. Do not choose capacity from `residentApproximateTextBytes`.**

Before final PR/merge, synchronize the branch with current `main@2c33dacbefa613292eb89cbf606b0172a241e81e` and re-run only validation materially affected by the synchronized source. Exact b18 runtime evidence remains tied to product source `f30c13b4ac2c40dcda829585682825ca906dceae`.
