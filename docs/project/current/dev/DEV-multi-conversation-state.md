# DEV-multi-conversation-state

## Status

**Active — b18 historical-scroll Runtime accepted; b19 process-footprint Runtime accepted for observed 0→8 resident matrix; b21 title Runtime accepted; b21 same-target Reload replacement-under-load Runtime accepted from exact diagnostics; normal LRU remains unfrozen; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `2d0853ebd418a33d5bdd46f342d4b4a9536c4657`
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b21`
- Current exact Candidate: `DEV-multi-conversation-state-0.1.0-b21` / `0.1.0 (21)`
- b21 exact product/config source: `6b50ead167bfde305d2ad58dd16fee6edaabf597`; tree `01168ce7be8d9cf4888ad1d0718238826730c30d`
- b21 CI: Run `33070183417`; Job `98510113281`; success
- b21 Artifact: `9645439329`; upload ZIP `sha256:b3e2da46ce9ac99fc7028b7f5186476b3264c4a8c0323a426ee275b62c0d7d14`
- b21 IPA: `ChatGPTClient-0.1.0-b21-dev-multi-conversation-state.ipa`; SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`

## Accepted runtime matrix

### b17 / b18 multi-conversation and scroll

- resident return / hidden completion / same-target coalescing / rapid independent A-B-C overlap accepted.
- Sync A -> B -> A rejoin accepted with no duplicate target request on return.
- b18 per-conversation historical scroll anchors accepted for A/B independent positions, first-time C, Sync preservation, Reload preservation and resident-return regression.
- Future active-response follow-tail remains a separate Send/Stream integration contract and is not implemented by this Work.

### b19 process-memory evidence

Exact b19 iPhone/iOS17 run reached 8 residents with 53 valid process-memory samples. Observed physical footprint was approximately 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents; observed HTTP statuses were all 200 and no HTTP429/error appeared. `processMemoryLimitRemainingBytes` was absent, so exact process-limit headroom remains Unverified.

Decision: the observed run provides no evidence for urgent normal-LRU eviction at 8 residents. Do not manufacture an LRU capacity from physical RAM or approximate text bytes. Existing memory-warning trimming remains the evidence-backed eviction behavior; normal LRU remains unfrozen.

### b20 / b21 title lifecycle

b20 Runtime exposed a first-detail-view-load lifecycle defect: the selected list-summary title was installed before `showConversation`, then first `viewDidLoad()` overwrote it with neutral `新对话`. b21 changed only lifecycle ordering in `RootViewController`:

`repository.selectConversation(id:) -> detailViewController.loadViewIfNeeded() -> assign target ConversationSummary.title -> showConversation(id:)`.

The user then accepted exact b21 on iPhone/iOS17 for first unloaded entry, re-entry and rapid unloaded A -> B -> C title switching, with no reported stale A/B overwrite of the current target.

### b21 same-target Reload replacement-under-load — Runtime accepted

Uploaded diagnostics metadata identifies exact `0.1.0 (21)`, candidate `DEV-multi-conversation-state-0.1.0-b21`, source `6b50ead167bf`, iPhone / iOS17.0.

The run contains two complete same-target replacement sequences and one hidden/rejoin strengthening sequence:

1. Target `sha256:2e383eb82736`, list position 2:
   - generation 1 `load` started and issued Detail request at `14:05:30Z`.
   - user requested `重载当前会话` at `14:05:33Z` while generation 1 was still in flight.
   - `detail.cancel.requested` records cancelled generation 1 / replacement generation 2 / `taskPresent=true`.
   - generation 1 logged `detail.cancelled` and `detailLoad.end status=cancelled` after ~2830.60 ms.
   - generation 2 `reload` returned HTTP200, 9,366,700 bytes, mapping 1977, 830 visible messages, then `resident.stored visibility=foreground` and `conversationReload.end status=ok` after ~10.4 s.

2. Target `sha256:d7a1643df0df`, list position 26:
   - generation 1 `load` started at `14:07:01Z`.
   - Reload requested at `14:07:04Z` while generation 1 remained in flight.
   - generation 1 was explicitly cancelled and generation 2 `reload` became the replacement owner.
   - while generation 2 remained active, selection moved to another conversation `sha256:a9852360091a`; that unrelated conversation loaded independently and stored foreground.
   - returning to the Reload target at `14:07:22Z` logged `detail.coalesced`, generation 2 / kind reload / `completionCount=2`; no duplicate Reload was started.
   - the same generation 2 response returned HTTP200 with 19,327,096 bytes, mapping 3633, 1470 visible messages; `resident.stored` completed and `conversationReload.end status=ok` after ~21.25 s.
   - subsequent navigation back to the unrelated resident and then back to the Reload target produced normal `resident.hit` / historical-scroll restoration, with no stale overwrite reported.

This directly accepts the multi-conversation same-target replacement invariant: newer Reload owns the target; older in-flight load is cancelled/superseded; returning to the target while Reload is still active coalesces onto the same operation; unrelated conversation work remains independent. No b22 is justified by this test.

## Evidence labels

- Code written: **Yes**.
- Static/source checks: **Passed**.
- CI passed: **Yes — b21 Run `33070183417`, Job `98510113281`**.
- Artifact produced / identity accepted: **Yes — Artifact `9645439329`**.
- Runtime/manual/real-device: **Accepted for tested multi-conversation core, historical scroll, b19 0→8 resident process-footprint matrix, b21 title matrix, and b21 same-target Reload replacement-under-load including hidden/rejoin coalescing**.
- Stable/Frozen: **No**.

## Base / parallel status

Real `main` advanced from the older recorded base to `2d0853ebd418a33d5bdd46f342d4b4a9536c4657`. Compared with the prior recorded `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`, the advancement only changes `ATTACHMENT_TRANSFER_PLAN.md`, `DEVELOPMENT_PLAN.md`, `START_HERE.md` and `UI_INTERACTION_BASELINE.md`; it does not modify b21 product source / Repository / Root / candidate config. Open PR count was 0 at this gate, and no second Active DEV checkpoint exists on this branch.

## Remaining conditional / closure gates

- natural failed-resident navigation with no implicit retry: Runtime-unverified until a natural terminal failure occurs; do not manufacture retry/failure logic merely to exercise it.
- supported account-switch isolation: Runtime-unverified until a real supported account-switch/logout route exists.
- normal LRU capacity: remains unfrozen; current 8-resident evidence does not justify adding one.
- non-personal workspace isolation: Unknown / Unverified.
- missing-anchor-message discard: Runtime-unexercised; no current evidence of a defect.
- future Send/Stream follow-tail: separate Work evidence and must consume the future authoritative per-conversation response owner.

## Next exact action

No product defect was exposed by the Reload-under-load gate, so do not create b22. Review the remaining conditional gates for explicit scope-out versus actual availability. If none is currently exercisable without inventing unsupported product behavior, synchronize the development branch with current `main@2d0853ebd418a33d5bdd46f342d4b4a9536c4657`, perform conflict/owner review, create the task PR, run validation for any materially synchronized product/config changes, and proceed toward Work closure without claiming untested conditions as Runtime-passed.