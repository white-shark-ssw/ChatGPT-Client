# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: **merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope**. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

`DEV-multi-conversation-state` remains Active and not Stable/Frozen. b17 core multi-conversation Runtime is accepted; b18 historical-scroll Runtime is accepted; exact b19 real-device process-footprint Runtime is accepted for the observed 0→8 resident/repeated-switch matrix. Exact b20 is now the current Code + Static + CI + Artifact Candidate for the source-confirmed rapid-switch title defect; b20 Runtime is pending.

Current `main` head is `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`. Its latest advancement is merged planning PR #18 and does not overlap the current b20 product/config owner set. Synchronize before final merge.

## Active Work — DEV-multi-conversation-state

- **Branch / PR**: `dev/multi-conversation-state-20260827`; PR not created.
- **b16**: historical/rejected before Runtime; never reuse.
- **b17**: exact source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; Run `33045536770`; Artifact `9635486304`; core resident/coalescing/hidden-Sync/rapid-overlap Runtime accepted; historical-scroll defect reproduced.
- **b18**: exact source `f30c13b4ac2c40dcda829585682825ca906dceae`; Run `33054012226`; Artifact `9638821912`; historical-scroll/Sync/Reload-preservation/resident-regression Runtime accepted on iPhone/iOS17.
- **b19 measurement Runtime**: exact source `c6accf16c8cf80c719f1e569e356b2bbe664e91e`; Run `33063446367`; Artifact `9642715296`; iPhone/iOS17 run reached 8 residents with 53 valid task-VM samples. Observed physical footprint was approximately 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents. All observed HTTP statuses were 200, with no error/HTTP429. `processMemoryLimitRemainingBytes` was absent, so exact process-limit headroom remains Unverified.
- **Memory decision**: b19 provides no evidence for urgent normal-LRU eviction at 8 residents. Normal LRU capacity remains unfrozen rather than guessed from physical RAM or approximate text bytes. Existing memory-warning trimming remains the evidence-backed eviction behavior.
- **Current exact Candidate**: `DEV-multi-conversation-state-0.1.0-b20`, `0.1.0 (20)`.
- **b20 product/config source**: `754580fad96efa69f8a0ce7ea2bf542cacaf156e`; tree `715e13bf3a7e77d33daa62a7db80c2e087531011`.
- **b20 implementation**: one presentation behavior line in `RootViewController` updates the detail navigation title immediately from the selected target's existing `ConversationSummary.title` after `repository.selectConversation(id:)` and before `showConversation(id:)`; existing current Detail `apply(_:)` still confirms with `detail.title` when available. `ConversationFeature.swift`, Repository, Diagnostics, auth, scroll and residency behavior are unchanged.
- **b20 CI**: Run `33067148782`, Job `98499940471`, success.
- **b20 Artifact**: `9644208203`; ZIP `sha256:eca6ca2753692843bef794054d94fe319e9393f2d4d5ef4161e08ccb32539881`.
- **b20 IPA**: `ChatGPTClient-0.1.0-b20-dev-multi-conversation-state.ipa`; SHA `7632f10324e96a80e2eba6760511955a0b15a973ba351307de9aa4bed2cdf765`.
- **b20 package identity**: `0.1.0 (20)`, candidate b20, source `754580fad96e`, minimum iOS14.0, `[1,2]`, arm64.

### Validation labels

- **Code written**: Yes.
- **Static/source checks**: Passed.
- **CI passed**: Yes — b20 Run `33067148782`, Job `98499940471`.
- **Artifact produced**: Yes — b20 Artifact `9644208203`, identity accepted.
- **Runtime/manual/real-device**: b19 memory matrix accepted; **b20 rapid-switch title fix pending**.
- **Stable/Frozen**: **No**.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner and immediate selected-title presentation handoff.
- `ConversationRepository`: sole authoritative conversation data/read/recovery owner with account-scoped per-conversation residents/operations.
- `ConversationDetailViewController`: detail/messages/recovery presentation plus lightweight per-conversation historical scroll presentation metadata; Detail completion still owns final target detail title presentation.
- `DiagnosticsLogger`: accepted structured diagnostics owner with b19 task-VM process-memory enrichment.
- Default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole account/auth context owner.
- Historical anchor and future active-response `follow-tail` remain distinct; follow-tail must consume the future authoritative per-conversation Send/Stream response owner.

## Known issues / open acceptance

- b20 exact Runtime must verify rapid A→B→C selection changes navigation title immediately while earlier Details remain in flight, with no late A/B overwrite of C title/content.
- Normal LRU capacity remains unfrozen pending stronger headroom/pressure evidence; b19 shows no immediate pressure at 8 residents on tested iPhone/iOS17.
- Isolated same-target Reload replacement while an older Detail is actually in flight remains open; b15 remains accepted replacement-under-load baseline.
- Terminal failed resident navigation with no implicit retry remains open until a natural terminal failure is available.
- Supported account-context purge/late-callback isolation still requires a real supported account-switch/logout route.
- Missing-anchor-message discard remains Runtime-unexercised.
- Runtime below iOS17, iPad, non-personal workspace, Send/Stream and attachments remain Unknown / Unverified as applicable.
- No XCTest/UI-test target exists.

## Next exact action

Install exact b20 on iPhone/iOS17. Choose a slow-loading A, immediately select B before A finishes, then C before B finishes. Expected title transition is immediate A → B → C from list summaries; late A/B completion must not overwrite current C title/content. Spot-check resident return/historical scroll remains intact.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. CI/Artifact success is not Runtime proof.