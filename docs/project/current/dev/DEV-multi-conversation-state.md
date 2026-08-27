# DEV-multi-conversation-state

## Status

**Ready for PR / closure — tested Plus/personal iPhone/iOS17 read-state scope accepted through exact b21; current main synchronized; remaining unexercised conditions explicitly scoped out rather than claimed Passed; Stable/Frozen remains No until merge/closure completes**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `4f38cdace0c94fed852534448f1362f1125270de`
- Synchronized merge commit: `7f2a9776cc419f8e8b30aebbf731e82b3bc24a92`
- Last / final Runtime Candidate for this Work: `DEV-multi-conversation-state-0.1.0-b21` / `0.1.0 (21)`
- Exact b21 product/config source: `6b50ead167bfde305d2ad58dd16fee6edaabf597`; tree `01168ce7be8d9cf4888ad1d0718238826730c30d`
- CI: Run `33070183417`; Job `98510113281`; success
- Artifact: `9645439329`; upload ZIP `sha256:b3e2da46ce9ac99fc7028b7f5186476b3264c4a8c0323a426ee275b62c0d7d14`
- IPA: `ChatGPTClient-0.1.0-b21-dev-multi-conversation-state.ipa`; SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`

## Accepted Runtime matrix

- b17: resident return; hidden valid completion; same-target coalescing; Sync A -> B -> A rejoin; rapid independent multi-conversation overlap without observed HTTP429 in supplied export.
- b18: independent per-conversation historical scroll anchors; first-time target isolation; visible Sync/Reload anchor preservation when anchored message remains; resident/coalescing regressions accepted.
- b19: 0 -> 8 resident process-footprint matrix with 53 valid task-VM samples; physical footprint approximately 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents; no observed error/HTTP429. Exact process-limit headroom was unavailable.
- b20: first unloaded Detail entry title lifecycle defect reproduced and source-confirmed; superseded.
- b21 title: first unloaded entry, re-entry and rapid unloaded A -> B -> C title switching accepted by direct user real-device result.
- b21 same-target Reload replacement-under-load: exact diagnostics contain two complete ordinary-load generation 1 -> Reload generation 2 replacement sequences. Older target task is cancelled; replacement owns the target and returns HTTP200. Strengthened sequence switches to an unrelated conversation while Reload remains active, returns to the Reload target and logs `detail.coalesced completionCount=2`; no duplicate Reload or stale overwrite occurs and unrelated conversation work remains independent.

## Closure scope decisions

The following conditions remain explicitly **Unknown / Unverified or conditional**, but no current evidence justifies keeping this Work Active merely to manufacture them:

- **Natural failed-resident navigation**: no natural terminal failure occurred in the accepted runs. Source contract keeps terminal failed resident from turning navigation into implicit retry; explicit Reload remains user-owned recovery. Do not induce artificial network failure or add retry/fallback merely to close a matrix cell. Reopen only if a real Runtime failure contradicts the contract.
- **Supported account-switch isolation**: no real supported account-switch/logout route exists in the current product flow. Account-scope purge/late-callback guards remain source-backed; Runtime proof is deferred until a supported route exists. Do not create fake account transition UI for this Work.
- **Normal LRU capacity**: b19 provides no evidence for urgent normal eviction at 8 residents. No arbitrary capacity will be added. Existing memory-warning trimming remains the evidence-backed policy. If future memory pressure/headroom evidence appears, handle it in the owning future Work.
- **Non-personal workspace isolation**: current accepted Runtime scope is Plus/personal. Additional workspace identity remains Unknown / Unverified and is not claimed supported.
- **Missing-anchor-message discard**: destructive branch change did not occur naturally. Source/CI behavior is discard anchor -> top; no defect evidence exists, so do not manufacture branch mutation solely for Runtime proof.
- **Active-response follow-tail**: explicitly separate Send/Stream Work. It must consume the future authoritative per-conversation response owner and is not part of this read-state closure.

These scope-outs are evidence boundaries, not claims of Runtime success.

## Main synchronization / conflict review

Real main advanced to `4f38cdace0c94fed852534448f1362f1125270de`. Relative to this Work's original merge base, main changed only six planning/rules files: `ATTACHMENT_TRANSFER_PLAN.md`, `CONVERSATION_LIST_CACHE_PLAN.md`, `CURRENT_WORK_RULES.md`, `DEVELOPMENT_PLAN.md`, `START_HERE.md`, `UI_INTERACTION_BASELINE.md`.

A real two-parent merge commit `7f2a9776cc419f8e8b30aebbf731e82b3bc24a92` now includes current main as its second parent and preserves those six main-owned files exactly. GitHub compare reports `behind_by=0` against current main. From exact b21 product source `6b50ead...` to synchronized head, GitHub reports only docs changes: no `ChatGPTClient/**`, Xcode project, workflow or packaging file changed. Therefore no product behavior/config changed during synchronization and no b22 / repeat real-device candidate is justified.

Current main planning also establishes `DEV-conversation-list-cache-core` as the next early infrastructure task after multi-conversation becomes Stable/merged. Preserve that priority; do not let this closure overwrite it.

## Evidence labels

- Code written: **Yes**.
- Static/source checks: **Passed**.
- CI passed: **Yes — b21 Run `33070183417`, Job `98510113281`**.
- Artifact produced / identity accepted: **Yes — b21 Artifact `9645439329`**.
- Runtime/manual/real-device: **Accepted for the tested multi-conversation core, historical scroll, 0→8 resident footprint matrix, title lifecycle and same-target Reload replacement-under-load/hidden-rejoin matrix on Plus/personal iPhone/iOS17**.
- Stable/Frozen: **Not yet — promote to Stable for this recorded scope only after PR merge; Frozen remains No**.

## Next exact action

Create the task PR from `dev/multi-conversation-state-20260827` to current `main`. Review the PR diff for owner conflicts and preservation of current main planning. Let PR CI validate the synchronized merge view if triggered. If no product/config conflict or new defect appears, merge the PR, update durable docs to the merged Stable tested scope, record final PR/merge evidence, remove only this checkpoint, and leave the conditional Unknown/Unverified boundaries documented.