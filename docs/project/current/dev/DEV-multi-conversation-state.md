# DEV-multi-conversation-state

## Status

**Active — b18 historical-scroll Runtime accepted; b19 process-footprint Runtime accepted for observed 0→8 resident matrix; exact b20 title Candidate has Code + Static + CI + Artifact but real-device Runtime exposed a first-detail-view-load title lifecycle defect; b21 is reserved for the minimal lifecycle correction; normal LRU remains unfrozen; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`
- Branch head before b21 product edit: `0e0749b7d8386d7a5b66b0ff1dc4dfb16a19b935` (docs-only after exact b20 product source)
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b20`
- Reserved Candidate: `DEV-multi-conversation-state-0.1.0-b21` / `0.1.0 (21)` — first Detail view-load title lifecycle correction
- b20 exact product/config source: `754580fad96efa69f8a0ce7ea2bf542cacaf156e`; tree `715e13bf3a7e77d33daa62a7db80c2e087531011`
- b20 CI: Run `33067148782`; Job `98499940471`; success
- b20 Artifact: `9644208203`; upload ZIP `sha256:eca6ca2753692843bef794054d94fe319e9393f2d4d5ef4161e08ccb32539881`
- b20 IPA: `ChatGPTClient-0.1.0-b20-dev-multi-conversation-state.ipa`; SHA `7632f10324e96a80e2eba6760511955a0b15a973ba351307de9aa4bed2cdf765`

## b19 real-device memory evidence

Exact b19 iPhone/iOS17 run reached 8 residents with 53 valid process-memory samples. Observed physical footprint was approximately 16.3–78.1 MiB and generally 55–65 MiB during repeated switching at 8 residents; observed HTTP statuses were all 200 and no HTTP429/error appeared. `processMemoryLimitRemainingBytes` was absent, so exact process-limit headroom remains Unverified.

### Memory decision

The b19 run provides no evidence for urgent normal-LRU eviction at 8 residents. Do not manufacture an LRU capacity from physical RAM or approximate text bytes. Normal LRU remains unfrozen; existing memory-warning trimming remains the evidence-backed eviction behavior.

## b20 title work and exact Runtime result

### Intended b20 correction

After `repository.selectConversation(id:)`, `RootViewController` immediately sets `detailViewController.title` from the already-loaded target `ConversationSummary.title`, falling back to neutral `新对话` only if the summary is unexpectedly absent; existing Detail `apply(_:)` later confirms with `detail.title`.

### New real-device evidence

Uploaded diagnostics metadata identifies exact `0.1.0 (20)`, candidate `DEV-multi-conversation-state-0.1.0-b20`, source `754580fad96e`, iPhone / iOS17.0.

Observed user-visible defect: on the first entry into the current conversation, the navigation title shows `新对话` while `正在读取会话…` is visible. Returning to the list and entering the same conversation again shows the correct title.

Exact sequence in the supplied run:

- `11:48:37Z`: first selection of `sha256:2e383eb82736`, list position 1; `resident.miss`; Detail generation 1 starts.
- `11:48:46Z`: same target Detail HTTP200 completes after about 9565.84 ms and is stored hidden because selection had moved elsewhere.
- `11:48:48Z`: same target selected again; `resident.hit`; `resident.firstVisible` about 28.70 ms.

This matches the report that first entry shows the neutral title but second resident-backed entry is correct.

### Source-confirmed root cause

b20 summary lookup is not the failure. `RootViewController` sets the summary title before calling `showConversation(id:)`. On first use, `ConversationDetailViewController`'s view has not loaded. The missing-detail/loading path in `showConversation(id:)` calls `resetScrollPositionToTop()`, which accesses `view` and triggers `viewDidLoad()`. `viewDidLoad()` currently executes unconditional `title = "新对话"`, overwriting the just-installed target summary title. When Detail later applies, `title = detail.title` corrects it. On second entry the view is already loaded, so this one-time lifecycle overwrite does not recur.

The initial cold-start auth probe HTTP403 in the same export is not causal: a later list generation successfully verified the same Plus/personal account and returned HTTP200 28/29 before the title reproduction. Do not add automatic auth retry/fallback based on this title defect.

## b21 minimal fix contract

Change only the Detail presentation lifecycle invariant so first `viewDidLoad()` does not overwrite a title that the Root already installed for the selected list summary. Preserve neutral `新对话` only when no title has been assigned yet. Keep b20's immediate selection-title handoff unchanged.

Do not change Repository, list/detail protocol, account/auth ownership, request cancellation/coalescing, scroll anchors, Send/Stream, retry/timer/watchdog/fallback behavior, or memory residency/LRU policy.

## Evidence labels

- b18: Code + Static + CI + Artifact + tested Runtime accepted.
- b19: Code + Static + CI + Artifact + observed process-footprint Runtime accepted; process-limit headroom Unverified.
- b20 Code/Static/CI/Artifact: **Passed**.
- b20 Runtime/manual/real-device: **Partial/failing — first Detail view load overwrites the selected summary title with `新对话`; second resident-backed entry is correct**.
- b21 Code/Static/CI/Artifact/Runtime: **Pending**.
- Stable/Frozen: **No**.

## Remaining gates

- b21 first entry into an unloaded conversation must show its list-summary title immediately while loading; returning/re-entering must remain correct.
- b21 rapid A→B→C while all targets are initially unloaded must show each selected list-summary title immediately; late A/B completion must not overwrite current C title/content.
- normal LRU remains unfrozen pending stronger headroom/pressure evidence.
- isolated Reload replacement-under-load.
- natural failed-resident navigation.
- supported account-switch isolation when route exists.
- non-personal workspace isolation Unknown/Unverified.

## Next exact action

Implement b21 as the smallest Detail view lifecycle correction: preserve an already-assigned title during first `viewDidLoad()` and use neutral `新对话` only when title is still unset. Update version/build/candidate/package identity atomically, run static/CI/Artifact validation, then real-device test first-entry loading title plus rapid A→B→C. Never reuse b20.