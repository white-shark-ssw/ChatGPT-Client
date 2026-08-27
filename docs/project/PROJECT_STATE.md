# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: **merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope**. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

`DEV-multi-conversation-state` remains Active. b17 has accepted core real-device multi-conversation evidence but reproduced the P1 per-conversation scroll-anchor defect. b18 is now the exact identity-valid correction Candidate with Code + static/source review + CI + Artifact evidence; b18 Runtime/manual/real-device validation is pending. The merged Stable baseline remains b15 until this Work completes and merges.

## Recovery completion

Final candidate: `DEV-conversation-recovery-0.1.0-b15`, version `0.1.0 (15)`.

- Product/config head `159e8ea4f7baf6cd890d1f9bbebeac41feefbf52`.
- Tested synthetic merge `fb0c6d75362e111758b62a98f89696b7f1cb6c92`; tree `7a988bcad27d023eac77683985c5d7d92b22c176`.
- CI Run `33004536664`; Artifact `9619988065`.
- IPA `ChatGPTClient-0.1.0-b15-dev-conversation-recovery.ipa`; SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`; ZIP `sha256:cf4e8bce5a80bdd86bd9b8457b86c7a41de65d762c6ee158422760538faa50a7`.
- Validation: **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted**.

## Active Work — DEV-multi-conversation-state

- **Work / branch**: `DEV-multi-conversation-state` on `dev/multi-conversation-state-20260827`; PR not created.
- **Baseline/conflict gate**: `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; no open PR; no second Active DEV checkpoint at b18 publication.
- **b16**: historical/rejected before runtime; never reuse.
- **b17**: exact source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; tree `3451585f83c7bac69368709fe6273b90a0294d29`; Run `33045536770`; Artifact `9635486304`; core real-device resident/coalescing/hidden-Sync/rapid-overlap sequences accepted; P1 scroll defect reproduced.
- **Current exact Candidate**: `DEV-multi-conversation-state-0.1.0-b18`, version `0.1.0 (18)`.
- **Exact b18 product/config source**: `f30c13b4ac2c40dcda829585682825ca906dceae`; tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- **Atomic publication**: built off parent `49be4de3b2918ae72b22e3de7a386136d92c2523`; exact diff contains only workflow, Xcode project, `ConversationFeature.swift`, and `scripts/build_ipa.sh`; branch ref moved once.
- **b18 implementation**: per-conversation lightweight historical-reading presentation anchor in `ConversationDetailViewController`, represented by message identity + relative visual offset. The actually displayed conversation is tracked separately from repository selection so outgoing A can be captured before rows become B. No global raw offset copying. Missing/new target starts at top. Account reset clears anchors. Sync/Reload preserve the anchor only when the same anchored message remains in the refreshed current branch.
- **Ownership boundary**: `ConversationRepository`, auth owner, network/protocol paths and current-node data ownership are unchanged. No fake Send/Stream response owner, `isStreaming`, timer, retry, fallback, watchdog, or speculative follow-tail state was introduced.
- **Diagnostics**: privacy-safe `scrollAnchor.saved`, `scrollAnchor.restored`, and `scrollAnchor.discarded`; no raw message IDs/bodies/titles/secrets.
- **CI**: Run `33054012226`, Job `98456174184`, success; exact checkout `f30c13b4ac2c40dcda829585682825ca906dceae`; Xcode16.4; Release compile target `arm64-apple-ios14.0`; exact b18 candidate/source inputs; `BUILD SUCCEEDED`.
- **Artifact**: `9638821912`, name `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b18`; ZIP digest `sha256:36b59b8c4d3bdcadedd463a3554528452ff46478651671b50f4bd9f7fa2b5d2c`.
- **IPA**: `ChatGPTClient-0.1.0-b18-dev-multi-conversation-state.ipa`; SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`; independent hash matches sidecar.
- **Embedded identity**: `0.1.0 (18)`, candidate b18, source `f30c13b4ac2c`, min iOS14.0, device families `[1,2]`, Mach-O arm64.
- **Validation**: `Code written = Yes`; `Static/source = Passed`; `CI = Passed`; `Artifact = Produced and identity accepted`; `Runtime/manual/real-device = Pending`; `Stable/Frozen = No`.

## Current architecture

### Accepted Stable baseline

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: authoritative conversation data/read/recovery owner.
- `ConversationSidebarViewController`: list presentation/initial list request.
- `ConversationDetailViewController`: detail/messages, recovery presentation, and Active-branch lightweight scroll presentation metadata.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole account/auth context owner.

### Active multi-conversation direction

- One `ConversationRepository` owns account-scoped per-conversation resident and async-operation state; foreground selection is presentation only.
- Current resident scope key is `userID + accountID + conversationID`; non-personal workspace identity remains Unknown / Unverified.
- `current_node` is retained as minimum directly evidenced branch-tip metadata; raw mapping payload is discarded.
- UIKit presentation metadata is not conversation-data authority.
- b18 historical scroll state is per conversation and lightweight. Future active-response `follow-tail` eligibility must consume a real per-conversation Send/Stream response owner and is not implemented in b18.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — Completed / merged / Stable b15.
2. `DEV-multi-conversation-state` — Active; b18 exact runtime Candidate now ready for device validation of semantic scroll restoration.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

## Known issues / open acceptance

- b18 needs exact iPhone/iOS17 runtime proof for A≈10% -> B scroll -> A restoring the same semantic/visual point, independent A/B anchors, first-time target top behavior, and Sync/Reload anchor preservation when the anchored message remains.
- Account-context purge/late-callback isolation still requires a real supported account-switch/logout route before Runtime acceptance.
- Normal-operation resident/LRU bound remains Unknown until real process/system memory evidence; approximate visible-text bytes are not memory-capacity evidence.
- Runtime below iOS17, iPad, non-personal workspace, send/streaming and attachments remain Unknown / Unverified as applicable.
- No XCTest/UI-test target exists.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. CI/Artifact success is not runtime proof.
