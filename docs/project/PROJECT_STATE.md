# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: **merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope**. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

`DEV-multi-conversation-state` remains Active and not Stable/Frozen. b17 core multi-conversation Runtime is accepted; b18 historical-scroll Runtime is accepted; b19 real-device process-footprint Runtime is accepted for the observed 0→8 resident/repeated-switch matrix. b20 real-device Runtime exposed a first-Detail-view-load title lifecycle defect. Exact b21 now has Code + Static + CI + identity-valid Artifact + accepted direct real-device title Runtime for the requested first-entry/re-entry/rapid A→B→C matrix.

Current `main` head is `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`. It includes merged planning PR #18 and does not overlap b21 product/config owners. Synchronize before final merge.

## Active Work — DEV-multi-conversation-state

- **Branch / PR**: `dev/multi-conversation-state-20260827`; PR not created.
- **b16**: historical/rejected before Runtime; never reuse.
- **b17**: exact source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; core resident/coalescing/hidden-Sync/rapid-overlap Runtime accepted; historical-scroll defect reproduced.
- **b18**: exact source `f30c13b4ac2c40dcda829585682825ca906dceae`; historical-scroll/Sync/Reload-preservation/resident-regression Runtime accepted on iPhone/iOS17.
- **b19 measurement Runtime**: exact source `c6accf16c8cf80c719f1e569e356b2bbe664e91e`; iPhone/iOS17 run reached 8 residents with 53 valid task-VM samples. Physical footprint was approximately 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents. Observed HTTP statuses were all 200 with no error/HTTP429. `processMemoryLimitRemainingBytes` was absent, so exact process-limit headroom remains Unverified.
- **Memory decision**: b19 provides no evidence for urgent normal-LRU eviction at 8 residents. Normal LRU capacity remains unfrozen rather than guessed from physical RAM or approximate text bytes; memory-warning trimming remains the evidence-backed eviction behavior.
- **b20 Runtime defect**: exact `0.1.0 (20)` / source `754580fad96e` real-device export shows first selection of an unloaded target at `11:48:37Z`, Detail HTTP200 after ~9565.84 ms, then second selection at `11:48:48Z` as a resident hit. User observed `新对话` only on first loading entry. Source confirms Root assigned summary title before first Detail view load, then `viewDidLoad()` overwrote it with neutral `新对话`; second entry did not rerun that lifecycle initialization. The same export's earlier auth HTTP403 is not causal because later account verification/list HTTP200 completed before the title reproduction.
- **Current exact Candidate**: `DEV-multi-conversation-state-0.1.0-b21`, `0.1.0 (21)`.
- **b21 product/config source**: `6b50ead167bfde305d2ad58dd16fee6edaabf597`; tree `01168ce7be8d9cf4888ad1d0718238826730c30d`.
- **b21 implementation**: Root calls `detailViewController.loadViewIfNeeded()` after selection and before assigning the target `ConversationSummary.title`. This only fixes lifecycle ordering; b20's summary-title handoff and existing Detail `apply(_:)` final title remain intact. `ConversationFeature.swift`, Repository, Diagnostics, auth, protocol, scroll and residency behavior are unchanged.
- **b21 CI**: Run `33070183417`, Job `98510113281`, success.
- **b21 Artifact**: `9645439329`; ZIP `sha256:b3e2da46ce9ac99fc7028b7f5186476b3264c4a8c0323a426ee275b62c0d7d14`.
- **b21 IPA**: `ChatGPTClient-0.1.0-b21-dev-multi-conversation-state.ipa`; SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`.
- **b21 package identity**: `0.1.0 (21)`, candidate b21, source `6b50ead167bf`, minimum iOS14.0, `[1,2]`, arm64.
- **b21 Runtime**: after the requested exact b21 first-unloaded-entry/re-entry/rapid A→B→C title checks, the user reported `没问题了`. This accepts the b21 title lifecycle correction on the tested iPhone/iOS17 environment. No additional diagnostics export accompanied this acceptance, so no extra HTTP/timing claims are made.

### Validation labels

- **Code written**: Yes — b21 exact source published.
- **Static/source checks**: Passed.
- **CI passed**: Yes — b21 Run `33070183417`, Job `98510113281`.
- **Artifact produced**: Yes — b21 Artifact `9645439329`, identity independently accepted.
- **Runtime/manual/real-device**: b19 memory matrix accepted; b20 title lifecycle defect reproduced; **b21 title lifecycle correction accepted for the requested real-device matrix**.
- **Stable/Frozen**: **No**.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner; selected target summary title is handed to Detail after ensuring first Detail view initialization has completed.
- `ConversationRepository`: sole authoritative conversation data/read/recovery owner with account-scoped per-conversation residents/operations.
- `ConversationDetailViewController`: detail/messages/recovery presentation plus lightweight per-conversation historical scroll metadata; loaded Detail remains final title presentation via `detail.title`.
- `DiagnosticsLogger`: accepted structured diagnostics owner with b19 task-VM process-memory enrichment.
- Default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole account/auth context owner.
- Historical anchor and future active-response `follow-tail` remain distinct; follow-tail must consume the future authoritative per-conversation Send/Stream response owner.

## Known issues / open acceptance

- Isolated same-target Reload replacement while an older Detail is actually in flight remains open; b15 remains accepted replacement-under-load baseline, but the multi-conversation implementation still needs its own spot-check.
- Terminal failed resident navigation with no implicit retry remains open until a natural terminal failure is available.
- Supported account-context purge/late-callback isolation still requires a real supported account-switch/logout route.
- Normal LRU capacity remains unfrozen pending stronger headroom/pressure evidence if a bounded capacity becomes necessary; b19 shows no immediate pressure at 8 residents on tested iPhone/iOS17.
- Missing-anchor-message discard remains Runtime-unexercised.
- Runtime below iOS17, iPad, non-personal workspace, Send/Stream and attachments remain Unknown / Unverified as applicable.
- No XCTest/UI-test target exists.

## Next exact action

Use exact b21 for the isolated same-target Reload replacement-under-load Runtime spot-check: select an unloaded/slow conversation and trigger `重载当前会话` while that target's ordinary Detail request is still in flight. Expected: the older same-target request is cancelled/superseded, the Reload result becomes authoritative without stale overwrite, and unrelated conversations remain independent. This is evidence collection on existing b21 code; do not create b22 unless a defect is actually reproduced.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. CI/Artifact success is not Runtime proof.