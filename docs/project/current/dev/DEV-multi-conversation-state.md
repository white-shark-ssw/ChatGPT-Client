# DEV-multi-conversation-state

## Status

**Active — b18 historical-scroll Runtime accepted; exact b19 measurement Runtime accepted for observed process-footprint matrix; user-reported rapid-switch title defect is source-confirmed and b20 is reserved for the minimal presentation fix; normal LRU remains unfrozen; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b19`
- Reserved Candidate: `DEV-multi-conversation-state-0.1.0-b20` / `0.1.0 (20)` — rapid-switch title presentation correction
- b19 exact product/config source: `c6accf16c8cf80c719f1e569e356b2bbe664e91e`; tree `9142ebe7c4cd0860428d8fe35ee341507f61d051`
- b19 CI: Run `33063446367`; Job `98487641474`; success
- b19 Artifact: `9642715296`; IPA SHA `04861c63278d4a8fdf7c655f80b97f01cf8880d9f362d2f3edf1f55aec8ca8bc`

## b19 real-device memory evidence

Exact exported metadata: `0.1.0 (19)`, candidate b19, source `c6accf16c8cf`, iPhone / iOS17.0.

Observed run:

- 165 events, all `info`; 21 recorded HTTP statuses, all HTTP200.
- 53 process-memory samples, all `processMemorySampleStatus=ok`.
- resident count progressed from 0 to 8, including several very large detail responses and repeated resident switching.
- `processPhysFootprintBytes`: approximately 16.3 MiB minimum, 78.1 MiB observed maximum, 48.5 MiB median.
- `processResidentSizeBytes`: approximately 129.8 MiB observed maximum.
- at 8 residents, repeated-switch samples were approximately 55–65 MiB physical footprint; final large hidden resident storage was about 64.9 MiB footprint / 115.8 MiB resident size.
- `residentTotalApproximateTextBytes` reached 8,974,051 bytes, but remains correlation-only and is not capacity evidence.
- footprint did not increase monotonically with resident count and fell substantially after large request/parse completion, consistent with source ownership that does not retain raw mapping payloads in residents.
- `processMemoryLimitRemainingBytes` was absent from all 53 Runtime samples. Current source only emits it when returned `TASK_VM_INFO` count includes `limit_bytes_remaining`; therefore exact iOS17 headroom remains Unverified.
- No HTTP429/error/regression was observed; same-target load coalescing remained active during repeated rapid taps.

### Memory decision

The exact b19 run does **not** provide evidence for an urgent normal-LRU eviction at 8 residents: observed footprint stayed low and stabilized after large loads. Do not manufacture an LRU capacity from physical RAM or approximate text bytes. Because process-limit remaining/headroom was not returned on this iOS17 run, normal LRU capacity remains unfrozen and Work remains Active. Existing memory-warning trimming remains the only evidence-backed eviction behavior for now.

## User-reported rapid-switch title defect

Runtime report: select A; before A Detail loads select B; before B loads select C. Navigation title continues showing A until the currently selected Detail finishes, then changes to the correct title.

Source confirmation:

- `RootViewController` updates `selectedConversationID` before calling `ConversationDetailViewController.showConversation(id:)`.
- `showConversation(id:)` changes loading rows/state but, when `existingDetail == nil`, does not change `title`.
- `title = detail.title` currently occurs only in `apply(_:)`, after the target Detail is available.
- existing selected-ID + `presentationGeneration` completion guards already reject stale hidden A/B presentation completion; network/Repository ownership is not the defect.

### b20 minimal fix contract

On target selection, update the detail navigation title immediately from the already-loaded `ConversationSummary.title` for that target (fallback to the existing neutral `新对话` title if a summary is unexpectedly absent). Loaded Detail may then synchronously/terminally confirm with `detail.title` through existing `apply(_:)`.

Do not change Repository, request cancellation/coalescing, account ownership, scroll anchors, Send/Stream, retry/timer/fallback behavior, or memory residency policy for this title correction.

## Evidence labels

- b18: Code + Static + CI + Artifact + tested Runtime accepted.
- b19 Code/Static/CI/Artifact: Passed.
- b19 Runtime/manual/real-device: **Accepted for observed process-footprint / 0→8 resident / repeated-switch matrix; process-limit headroom Unverified**.
- b20 Code/Static/CI/Artifact/Runtime: Pending.
- Stable/Frozen: **No**.

## Remaining gates

- b20 rapid A→B→C title correctness while A/B Detail requests remain in flight.
- normal LRU remains unfrozen pending stronger headroom/pressure evidence; b19 shows no immediate footprint pressure at 8 residents on tested iPhone/iOS17.
- isolated Reload replacement-under-load.
- natural failed-resident navigation.
- supported account-switch isolation when route exists.
- non-personal workspace isolation Unknown/Unverified.

## Next exact action

Implement b20 as the minimal detail-presentation title correction only, update candidate/build/package identity atomically, run static/CI/Artifact validation, then real-device test rapid A→B→C before prior Details finish. Do not reuse b19.