# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: **merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope**. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

`DEV-multi-conversation-state` remains Active. b17 has accepted core multi-conversation Runtime evidence and reproduced the historical-scroll defect. Exact b18 has Code + static/source + CI + identity-valid Artifact + **real-device historical-scroll Runtime acceptance for the tested iPhone/iOS17 matrix**. Exact b19 is now the current **measurement-only** Candidate with Code + static/source + CI + identity-valid Artifact, but no Runtime memory result yet. No normal LRU capacity has been chosen or implemented. Work is not Stable/Frozen.

Current `main` head is `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`. Its latest advancement is merged planning PR #18 and changes only `CONVERSATION_LIST_CACHE_PLAN.md`, `DEVELOPMENT_PLAN.md`, `START_HERE.md`, and `UI_INTERACTION_BASELINE.md` relative to the prior main; it does not overlap b19 product/config/state owners. Synchronize before final merge.

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
- **b18**: exact source `f30c13b4ac2c40dcda829585682825ca906dceae`; tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`; Run `33054012226`; Artifact `9638821912`; historical-scroll/Sync/Reload-preservation/resident-regression Runtime accepted on iPhone/iOS17.
- **Current exact Candidate**: `DEV-multi-conversation-state-0.1.0-b19`, `0.1.0 (19)`, measurement-only.
- **Product/config source**: `c6accf16c8cf80c719f1e569e356b2bbe664e91e`; tree `9142ebe7c4cd0860428d8fe35ee341507f61d051`.
- **Implementation delta**: enriches existing `conversation / resident.*` diagnostics with current process task-VM memory sample fields. `ConversationFeature.swift` / `ConversationRepository` unchanged; no LRU/capacity behavior, timer, retry, fallback, watchdog, auth/protocol/parser or Send/Stream change.
- **CI**: Run `33063446367`, Job `98487641474`, success; exact b19 source.
- **Artifact**: `9642715296`; ZIP `sha256:7f33f13818b1ef77c83c84b7371fea2b930d4786709b72c9442fe33765b3bafc`.
- **IPA**: `ChatGPTClient-0.1.0-b19-dev-multi-conversation-state.ipa`; SHA `04861c63278d4a8fdf7c655f80b97f01cf8880d9f362d2f3edf1f55aec8ca8bc`.
- Independent package inspection: `0.1.0 (19)`, candidate `DEV-multi-conversation-state-0.1.0-b19`, source `c6accf16c8cf`, iOS14.0 minimum, device family `[1,2]`, Mach-O arm64.

### Validation labels

- **Code written**: Yes — exact b19 source published.
- **Static/source checks**: Passed.
- **CI passed**: Yes — Run `33063446367`, Job `98487641474`.
- **Artifact produced**: Yes — Artifact `9642715296`, identity accepted.
- **Runtime/manual/real-device**: **Pending for b19 process-memory measurement**. b18 remains the last runtime-tested product Candidate.
- **Stable/Frozen**: **No**.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation data/read/recovery owner with account-scoped per-conversation residents/operations.
- `ConversationDetailViewController`: detail/messages/recovery presentation plus lightweight per-conversation historical scroll presentation metadata.
- `DiagnosticsLogger`: accepted structured diagnostics owner; b19 adds measurement-only process-memory enrichment to resident events without changing resident ownership or policy.
- Default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole account/auth context owner.
- Historical anchor and future active-response `follow-tail` remain distinct. Follow-tail must consume the future authoritative per-conversation Send/Stream response owner.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — Completed / merged / Stable b15.
2. `DEV-multi-conversation-state` — Active; b18 historical scroll Runtime accepted; b19 memory-measurement Artifact ready for real-device evidence.
3. Continue durable post-recovery roadmap from current `DEVELOPMENT_PLAN.md` after this Work closes.
4. `DEV-send-stream` remains the point where real response ownership/follow-tail can become runtime-testable.

## Known issues / open acceptance

- Exact b19 real-device `processPhysFootprintBytes` / memory-limit-remaining evidence is still required before choosing normal resident/LRU capacity.
- Isolated same-target Reload replacement while an older Detail is actually in flight remains open as a multi-conversation regression spot-check; b15 remains accepted replacement-under-load baseline.
- Terminal failed resident navigation with no implicit retry remains open until a natural terminal failure is available.
- Supported account-context purge/late-callback isolation still requires a real supported account-switch/logout route.
- Missing-anchor-message discard is source/CI-defined but not runtime exercised in b18.
- Runtime below iOS17, iPad, non-personal workspace, Send/Stream and attachments remain Unknown / Unverified as applicable.
- No XCTest/UI-test target exists.

## Next exact action

Install exact b19 on iPhone/iOS17. Load several small and large conversations until multiple residents exist, repeatedly switch among them, then export diagnostics. Review real process footprint/headroom together with resident/active/protected counts and only then decide whether a bounded normal LRU is required and what capacity is defensible.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. CI/Artifact success is not Runtime proof.
