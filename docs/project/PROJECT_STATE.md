# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope; PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.
- `DEV-multi-conversation-state-0.1.0-b21`: **merged Stable multi-conversation read-state baseline for tested Plus/personal iPhone/iOS17 scope**. PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`.

`DEV-multi-conversation-state` is complete for its recorded tested scope. Core residency/coalescing/hidden completion, historical scroll, observed 0→8 resident process-footprint behavior, title lifecycle, and same-target Reload replacement-under-load/hidden-rejoin behavior have accepted real-device evidence. Natural-failure/account-switch/non-personal/missing-anchor conditions remain explicit Unknown/Unverified boundaries; normal LRU is not implemented because current evidence does not justify one. Stable does not mean Frozen.

Current `main` includes PR #23 at `2057a6241839afabeaf9b81c9daea24d3a0978f6` before this closure-document update. PR #23 preserved the main planning priority for `DEV-conversation-list-cache-core`.

## Stable multi-conversation baseline — DEV-multi-conversation-state

- **Merged PR**: #23, merge commit `2057a6241839afabeaf9b81c9daea24d3a0978f6`.
- **Final Runtime Candidate**: `DEV-multi-conversation-state-0.1.0-b21`, `0.1.0 (21)`.
- **Exact tested product/config source**: `6b50ead167bfde305d2ad58dd16fee6edaabf597`; tree `01168ce7be8d9cf4888ad1d0718238826730c30d`.
- **Exact Candidate CI**: Run `33070183417`, Job `98510113281`, success.
- **Exact Runtime Artifact**: `9645439329`; ZIP `sha256:b3e2da46ce9ac99fc7028b7f5186476b3264c4a8c0323a426ee275b62c0d7d14`.
- **Runtime IPA**: `ChatGPTClient-0.1.0-b21-dev-multi-conversation-state.ipa`; SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`.
- **Package identity**: `0.1.0 (21)`, candidate b21, source `6b50ead167bf`, minimum iOS14.0, `[1,2]`, arm64.
- **PR merge-view validation**: PR Run `33093117645`, Job `98590935774`, success; checkout/tested merge `0520f118d4ada5eacfbac4ff444d9572e322efe1`; source metadata `0520f118d4ad`; PR validation Artifact `9655230149`, IPA SHA `933bb559a9356348227d8603ce9bd24139b6234d055fd3ea03de38d8857809cc`. This is merge-view CI evidence, not a replacement Runtime Candidate.

### Runtime evidence

- b17: resident return, hidden completion, same-target coalescing, Sync A→B→A rejoin and rapid independent overlap accepted; historical-scroll defect reproduced.
- b18: independent semantic historical scroll anchors, first-time target isolation, Sync/Reload anchor preservation when anchored message remains, resident/coalescing regressions accepted.
- b19: 8 residents, 53 valid task-VM samples, physical footprint ~16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents; all observed HTTP statuses 200 and no error/HTTP429. Exact process-limit headroom unavailable.
- b20: first unloaded Detail title lifecycle defect reproduced/source-confirmed; superseded.
- b21 title: first unloaded entry, re-entry and rapid A→B→C accepted by direct user real-device result.
- b21 Reload-under-load: two exact same-target replacement sequences accepted. Ordinary-load generation 1 is cancelled by Reload generation 2; replacement returns HTTP200. Strengthened case switches to an unrelated conversation while Reload is active, returns to target and logs `detail.coalesced completionCount=2`; no duplicate Reload/stale overwrite and unrelated conversation remains independent.

### Evidence boundaries retained after merge

- Natural terminal failed-resident navigation remains Runtime-unverified until a natural failure exists; do not manufacture failure/retry logic merely to fill a matrix cell.
- Supported account-context purge/late-callback Runtime proof remains deferred until a real supported switch/logout route exists; do not create fake account transition UI.
- Normal bounded LRU remains unfrozen; b19 gives no evidence for urgent normal eviction at 8 residents. Existing memory-warning trimming remains the evidence-backed policy.
- Non-personal workspace isolation remains Unknown / Unverified.
- Missing-anchor-message discard remains Runtime-unexercised with source/CI-defined behavior and no current defect evidence.
- Future Send/Stream follow-tail and attachments are separate Work and are not part of this Stable read-state claim.

### Validation labels

- **Code written**: Yes.
- **Static/source checks**: Passed.
- **CI passed**: Yes — exact b21 plus PR merge-view validation.
- **Artifact produced**: Yes — exact b21 identity accepted; PR merge-view Artifact recorded separately.
- **Runtime/manual/real-device**: Accepted for recorded multi-conversation read-state matrix on tested Plus/personal iPhone/iOS17.
- **Stable**: **Yes for the recorded tested scope after PR #23 merge**.
- **Frozen**: **No**.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner; selected target summary title is handed to Detail after ensuring first Detail view initialization has completed.
- `ConversationRepository`: sole authoritative conversation data/read/recovery owner with account-scoped per-conversation residents/operations.
- `ConversationDetailViewController`: detail/messages/recovery presentation plus lightweight per-conversation historical scroll metadata; loaded Detail remains final title presentation via `detail.title`.
- `DiagnosticsLogger`: accepted structured diagnostics owner with b19 task-VM process-memory enrichment.
- Default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole auth/account-context owner.
- Historical anchor and future active-response `follow-tail` remain distinct; follow-tail must consume future authoritative per-conversation Send/Stream response ownership.

## Roadmap handoff

The next serialized development priority is `DEV-conversation-list-cache-core`. Its durable scope is `CONVERSATION_LIST_CACHE_PLAN.md`: one account-scoped persistent list snapshot behind `ConversationRepository`, cache-first presentation after verified scope, and conservative rapid-relaunch request suppression without per-row Detail prefetching or a second list authority.

No new development checkpoint is activated merely by closing this Work; activate the next Work only when development begins.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen acceptance. CI/Artifact success is not Runtime proof.