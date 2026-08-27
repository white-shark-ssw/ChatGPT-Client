# DEV-multi-conversation-state

## Status

**Active — b18 historical-scroll Runtime accepted; b19 process-footprint Runtime accepted for observed 0→8 resident matrix; b20 Runtime exposed a first-detail-view-load title lifecycle defect; exact b21 now has Code + Static + CI + identity-valid Artifact + accepted real-device title Runtime; normal LRU remains unfrozen; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b21`
- Current exact Candidate: `DEV-multi-conversation-state-0.1.0-b21` / `0.1.0 (21)` — first Detail view-load title lifecycle correction
- b21 exact product/config source: `6b50ead167bfde305d2ad58dd16fee6edaabf597`; tree `01168ce7be8d9cf4888ad1d0718238826730c30d`
- b21 CI: Run `33070183417`; Job `98510113281`; success
- b21 Artifact: `9645439329`; upload ZIP `sha256:b3e2da46ce9ac99fc7028b7f5186476b3264c4a8c0323a426ee275b62c0d7d14`
- b21 IPA: `ChatGPTClient-0.1.0-b21-dev-multi-conversation-state.ipa`; SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`

## b19 real-device memory evidence

Exact b19 iPhone/iOS17 run reached 8 residents with 53 valid process-memory samples. Observed physical footprint was approximately 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents; observed HTTP statuses were all 200 and no HTTP429/error appeared. `processMemoryLimitRemainingBytes` was absent, so exact process-limit headroom remains Unverified.

### Memory decision

The b19 run provides no evidence for urgent normal-LRU eviction at 8 residents. Do not manufacture an LRU capacity from physical RAM or approximate text bytes. Normal LRU remains unfrozen; existing memory-warning trimming remains the evidence-backed eviction behavior.

## b20 title work and exact Runtime result

### Intended b20 correction

After `repository.selectConversation(id:)`, `RootViewController` immediately sets `detailViewController.title` from the already-loaded target `ConversationSummary.title`, falling back to neutral `新对话` only if the summary is unexpectedly absent; existing Detail `apply(_:)` later confirms with `detail.title`.

### Real-device evidence

Uploaded diagnostics metadata identifies exact `0.1.0 (20)`, candidate `DEV-multi-conversation-state-0.1.0-b20`, source `754580fad96e`, iPhone / iOS17.0.

Observed user-visible defect: on the first entry into the current conversation, the navigation title shows `新对话` while `正在读取会话…` is visible. Returning to the list and entering the same conversation again shows the correct title.

Exact sequence in the supplied run:

- `11:48:37Z`: first selection of `sha256:2e383eb82736`, list position 1; `resident.miss`; Detail generation 1 starts.
- `11:48:46Z`: same target Detail HTTP200 completes after about 9565.84 ms and is stored hidden because selection had moved elsewhere.
- `11:48:48Z`: same target selected again; `resident.hit`; `resident.firstVisible` about 28.70 ms.

### Source-confirmed root cause

b20 summary lookup is not the failure. `RootViewController` sets the summary title before calling `showConversation(id:)`. On first use, `ConversationDetailViewController`'s view has not loaded. The missing-detail/loading path in `showConversation(id:)` calls `resetScrollPositionToTop()`, which accesses `view` and triggers `viewDidLoad()`. `viewDidLoad()` executes `title = "新对话"`, overwriting the just-installed target summary title. When Detail later applies, `title = detail.title` corrects it. On second entry the view is already loaded, so this one-time lifecycle overwrite does not recur.

The initial cold-start auth probe HTTP403 in the same export is not causal: a later list generation successfully verified the same Plus/personal account and returned HTTP200 28/29 before the title reproduction. Do not add automatic auth retry/fallback based on this title defect.

## b21 exact change / evidence

Minimal implementation keeps b20's summary-title handoff and changes only first-view lifecycle ordering in `RootViewController`:

`repository.selectConversation(id:) -> detailViewController.loadViewIfNeeded() -> assign target ConversationSummary.title -> showConversation(id:)`.

This makes the existing first `viewDidLoad()` initialization happen before the real selected summary title is assigned, so it cannot overwrite that title afterward. Loaded/resident targets still pass through existing `apply(_:)`, where current Detail `detail.title` remains the final title presentation.

- Root product behavior delta from b20 is exactly one line: `detailViewController.loadViewIfNeeded()`.
- Product/config diff is exactly four files: `RootViewController.swift`, Xcode project, workflow, build script.
- `ConversationFeature.swift`, Repository, Diagnostics, auth, scroll anchors, protocol and memory residency behavior are unchanged.
- Static Swift parse passed before publication.
- Run `33070183417` exact head SHA is `6b50ead167bfde305d2ad58dd16fee6edaabf597`; all build/inspect/upload steps succeeded.
- Artifact `9645439329` exact name is `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b21`.
- Independent package inspection matches GitHub digest and sidecar: `0.1.0 (21)`, candidate b21, source `6b50ead167bf`, minimum iOS `14.0`, `UIDeviceFamily=[1,2]`, Mach-O arm64; IPA SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`.

### b21 real-device acceptance

After installing exact b21 and running the requested title checks, the user reported **“没问题了”**. Treat this as accepted direct real-device evidence for the requested b21 title matrix on the tested iPhone/iOS17 environment:

- first entry into an unloaded conversation no longer presents the b20 `新对话` lifecycle overwrite while loading;
- returning/re-entering remains correct;
- requested rapid unloaded A -> B -> C selection/title check produced no reported issue, including no reported late A/B overwrite of the current target.

No new diagnostics export accompanied this acceptance, so do not claim additional HTTP/timing evidence beyond the user's direct Runtime result.

No Repository/list-detail protocol/account ownership/request cancellation/coalescing/scroll/Send-Stream/retry/timer/watchdog/fallback/LRU behavior was added or changed.

## Evidence labels

- b18: Code + Static + CI + Artifact + tested Runtime accepted.
- b19: Code + Static + CI + Artifact + observed process-footprint Runtime accepted; process-limit headroom Unverified.
- b20 Code/Static/CI/Artifact: **Passed**.
- b20 Runtime/manual/real-device: **Partial/failing — first Detail view load overwrites selected summary title with `新对话`; second resident-backed entry is correct**.
- b21 Code: **Yes**.
- b21 Static/source: **Passed**.
- b21 CI: **Passed — Run `33070183417`, Job `98510113281`**.
- b21 Artifact: **Produced / identity independently accepted — Artifact `9645439329`**.
- b21 Runtime/manual/real-device: **Accepted for the requested first-unloaded-entry / re-entry / rapid A→B→C title matrix on tested iPhone/iOS17; no issue reported**.
- Stable/Frozen: **No**.

## Remaining gates

- isolated same-target Reload replacement-under-load in the multi-conversation implementation;
- natural failed-resident navigation with no implicit retry;
- supported account-switch isolation when a real route exists;
- normal LRU remains unfrozen pending stronger headroom/pressure evidence if a bounded capacity becomes necessary;
- non-personal workspace isolation Unknown/Unverified;
- missing-anchor-message discard remains Runtime-unexercised;
- future Send/Stream follow-tail remains separate Work evidence.

## Next exact action

Use exact b21 for the next evidence-only regression gate: start an unloaded/slow conversation Detail and, while that same target's ordinary Detail request is still in flight, explicitly choose `重载当前会话`. Expected: the newer Reload owns that target, the older same-target Detail is cancelled/superseded per the accepted repository contract, the replacement completes without stale overwrite, and unrelated conversations remain independent. This is a Runtime spot-check of existing code, not a reason to create b22 unless the test exposes a defect. Do not invent retry/fallback/LRU behavior.