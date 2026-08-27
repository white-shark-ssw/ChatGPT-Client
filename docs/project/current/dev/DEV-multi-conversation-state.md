# DEV-multi-conversation-state

## Status

**Active — b18 historical-scroll Runtime accepted; exact b19 process-footprint Runtime accepted for observed 0→8 resident matrix; b20 rapid-switch title correction has Code + Static + CI + identity-valid Artifact and awaits exact real-device Runtime; normal LRU remains unfrozen; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b19`
- Current exact Candidate: `DEV-multi-conversation-state-0.1.0-b20` / `0.1.0 (20)` — rapid-switch title presentation correction
- b20 exact product/config source: `754580fad96efa69f8a0ce7ea2bf542cacaf156e`; tree `715e13bf3a7e77d33daa62a7db80c2e087531011`
- b20 CI: Run `33067148782`; Job `98499940471`; success
- b20 Artifact: `9644208203`; upload ZIP `sha256:eca6ca2753692843bef794054d94fe319e9393f2d4d5ef4161e08ccb32539881`
- b20 IPA: `ChatGPTClient-0.1.0-b20-dev-multi-conversation-state.ipa`; SHA `7632f10324e96a80e2eba6760511955a0b15a973ba351307de9aa4bed2cdf765`

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
- `processMemoryLimitRemainingBytes` was absent from all 53 Runtime samples; exact iOS17 process-limit headroom remains Unverified.
- No HTTP429/error/regression was observed; same-target load coalescing remained active during repeated rapid taps.

### Memory decision

The exact b19 run does **not** provide evidence for urgent normal-LRU eviction at 8 residents: observed footprint stayed low and stabilized after large loads. Do not manufacture an LRU capacity from physical RAM or approximate text bytes. Because process-limit remaining/headroom was not returned on this iOS17 run, normal LRU capacity remains unfrozen. Existing memory-warning trimming remains the only evidence-backed eviction behavior for now.

## User-reported rapid-switch title defect

Runtime report: select A; before A Detail loads select B; before B loads select C. Navigation title continues showing A until the currently selected Detail finishes, then changes to the correct title.

Source-confirmed cause:

- `RootViewController` updates `selectedConversationID` before calling `ConversationDetailViewController.showConversation(id:)`.
- `showConversation(id:)` changes loading rows/state but, when `existingDetail == nil`, does not change `title`.
- `title = detail.title` occurs only in `apply(_:)`, after target Detail becomes available.
- selected-ID + `presentationGeneration` completion guards already reject stale hidden A/B presentation completion; Repository/network ownership is not the defect.

## b20 exact change / evidence

Minimal product change: after `repository.selectConversation(id:)`, `RootViewController` immediately sets `detailViewController.title` from the existing target `ConversationSummary.title`, falling back to neutral `新对话` only if that summary is unexpectedly absent; existing `apply(_:)` still confirms with `detail.title` when current Detail completes.

- Product diff is exactly four files: `RootViewController.swift`, Xcode project, workflow, build script.
- Root behavior change is one line; `ConversationFeature.swift`, Repository, Diagnostics, auth, scroll anchors and memory residency behavior are unchanged.
- Static parse passed before publication.
- Run `33067148782` exact head SHA is `754580fad96efa69f8a0ce7ea2bf542cacaf156e`; all build/inspect/upload steps succeeded.
- Artifact `9644208203` exact name `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b20`.
- Independent package inspection matches sidecar and embedded identity: `0.1.0 (20)`, b20, source `754580fad96e`, minimum iOS `14.0`, `UIDeviceFamily=[1,2]`, Mach-O arm64.

No Repository/request cancellation/coalescing/account ownership/scroll/Send-Stream/retry/timer/fallback/LRU behavior was added or changed.

## Evidence labels

- b18: Code + Static + CI + Artifact + tested Runtime accepted.
- b19 Code + Static + CI + Artifact + **observed process-footprint Runtime accepted**; process-limit headroom Unverified.
- b20 Code: **Yes**.
- b20 Static/source: **Passed**.
- b20 CI: **Passed — Run `33067148782`, Job `98499940471`**.
- b20 Artifact: **Produced / identity independently accepted — Artifact `9644208203`**.
- b20 Runtime/manual/real-device: **Pending**.
- Stable/Frozen: **No**.

## Remaining gates

- b20 rapid A→B→C title correctness while A/B Detail requests remain in flight; late A/B completion must not overwrite C title/content.
- normal LRU remains unfrozen pending stronger headroom/pressure evidence; b19 shows no immediate footprint pressure at 8 residents on tested iPhone/iOS17.
- isolated Reload replacement-under-load.
- natural failed-resident navigation.
- supported account-switch isolation when route exists.
- non-personal workspace isolation Unknown/Unverified.

## Next exact action

Install exact b20 on iPhone/iOS17. Choose a slow-loading A, immediately select B before A Detail completes, then immediately C before B completes. Expected: navigation title changes immediately A → B → C from list summaries; C completion may confirm/update C title, and late A/B completion must not overwrite C title/content. Also spot-check resident return / historical scroll remains intact. Runtime acceptance remains pending until this exact Candidate is tested.