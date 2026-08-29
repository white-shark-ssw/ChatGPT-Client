# DEV-send-stream

## Status

**Active — b48 exact-device Runtime completed. Native composer -> official Web protected Send succeeded for two sequential turns, but b48 Native assistant streaming failed because the filter used the wrong patch field names. b49 is allocated for the smallest source-backed `o/p/v` parser correction. Long-term TD-024/TD-025 hidden/shadow-Web boundary remains unchanged; this remains an isolated diagnostic experiment.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / Native composer / Web Send engine / filtered SSE / hidden Web diagnostic`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b48 product/config source**: `6ccba03cefaa32a1186f1f468c3e696ed9457699`; permanently reserved after Artifact emission.
- **b48 Runtime Artifact**: `9718885751`; IPA SHA `c1f2f6a4e750af8abc7438e289f709cdf23c564f06ce2118b1c9b74f2d8ed850`.
- **Allocated next Candidate**: `DEV-send-stream-0.1.0-b49`, version/build `0.1.0 (49)`.
- **Stable/Frozen Send**: No.

## Current resume / identity guard

Current-session guard revalidated before b49 allocation:

- latest branch `AGENTS.md` then `docs/project/START_HERE.md` reread;
- user message clearly continues the b48 `DEV-send-stream` Runtime experiment;
- branch before b48 Runtime evidence write was `0ae6eb672988be79b8a1128e0cb2073142d58b53`;
- PR #29 open / mergeable / not merged and pointed to the same branch;
- current `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- `docs/project/current/dev/` contains no other Active development checkpoint;
- compare `6ccba03... -> 0ae6eb6...` showed only `docs/project/**` changes, so b48 product source did not drift;
- repository search found no prior `DEV-send-stream-0.1.0-b49` allocation.

The b48 Runtime evidence file was then added in docs-only commit `3977245890aafd9fbb5ef7e5c92692cdb2901a4b`.

## b48 exact Runtime result

User supplied screenshot + diagnostics for exact b48 / Release / iPhone / iOS17.0 / source `6ccba03cefaa`.

### Positive facts

1. Native composer became ready using the real Web `#prompt-textarea` state.
2. Attempt 1 Native submit -> `submitted` -> official protected Send observed -> HTTP200 `text/event-stream`, `filtered=true`.
3. First stream reached terminal after 268 SSE frames.
4. Web composer returned ready after terminal.
5. Attempt 2 Native submit -> `submitted` -> a second official protected Send -> again HTTP200 SSE `filtered=true`.
6. User later opened the newly created authoritative conversation through the ordinary Native list/detail path and confirmed both assistant answers existed server-side.

### Negative facts

First-turn terminal metrics:

- `removedTextPatchCount=0`
- `removedTextCharacters=0`
- `nativeDeltaCount=0`
- `nativeCharacters=0`
- `webAssistantTextCharacters=5864`
- `webMessageNodes=2`
- `webElementCount=951`
- `terminal=true`

Therefore b48 did **not** remove assistant text before Web React and did **not** deliver Native incremental text. The screenshot correctly showed the Native surface with both user prompts but empty `ChatGPT:` bodies.

Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b48-runtime.md`.

## Deterministic b48 defect

Exact b48 source `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift` filters for verbose fields:

- `node.op`
- `node.path`
- `node.value`

Exact current protocol evidence already present in the repository from b40 uses compact fields:

- operation `o`
- path `p`
- value `v`
- batch envelope `o == "patch"` with compact patch entries in `v`.

This is direct current-source evidence, not a guessed protocol change. It fully explains why b48 captured 268 frames but matched zero text patches.

## b49 exact scope

Make only the smallest correction needed to re-run the same diagnostic gate:

- `NativeWebSendEngineProbe.swift`: change assistant text-patch recognition from `op/path/value` to evidenced `o/p/v`; recursive handling must continue to catch compact entries inside `o:"patch"` / `v:[...]` batches.
- retain the existing b48 Native composer bridge, official Web form/Send ownership, default persistent WebKit store, full-size hidden-under-Native layout, no-clone stream transform, structural diagnostics and privacy boundary;
- update Settings label, Xcode Build/Candidate identity and workflow/artifact identity to b49;
- do not change `ConversationRepository`, `AuthSessionStore`, `RootViewController`, `ConversationFeature`, build scripts, attachments, existing-chat history virtualization or durable TD-024/TD-025 policy;
- no retry/timer/watchdog/fallback;
- do not add speculative alternate patch shapes beyond the already-evidenced current compact form.

## b49 Runtime gate

On exact iPhone/iOS17:

1. Native composer still submits first and second turn without touching Web composer.
2. Each official Send is HTTP200 SSE.
3. First long response produces `removedTextPatchCount > 0`, `removedTextCharacters > 0`, `nativeDeltaCount > 0`, `nativeCharacters > 0`.
4. Assistant text visibly appears incrementally in Native output.
5. `webAssistantTextCharacters` stays near zero/small relative to the Native response rather than thousands of characters.
6. Web composer becomes ready after terminal and second sequential Native Send succeeds.

Passing b49 still does not prove existing long-conversation viability. Existing-conversation response/history virtualization is a later separate experiment only after this corrected gate passes.

## Non-atomic GitHub write-chain recovery point

### Batch A — b48 Runtime evidence + b49 allocation

- b48 Runtime evidence file created: complete.
- checkpoint rolled to b49: this write.

### Batch B — non-CI b49 assembly

Create a temporary assembly branch from the post-checkpoint head. Expected product/config changes only:

- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`
- `ChatGPTClient/SettingsViewController.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `.github/workflows/ios-foundation.yml`

### Batch C — audit / publish

- compare assembly against real development head;
- require exactly those four expected paths;
- Light Guard real branch head immediately before publish;
- non-force fast-forward complete b49 chain onto `dev/send-stream-20260829`.

### Batch D — CI / Artifact

- accept only complete b49 exact source CI;
- require Push + PR CI when emitted;
- inspect Push Artifact package identity and hashes independently;
- once Artifact emits, b49 becomes permanently reserved.

### Batch E — durable docs / PR

Update Build/Test Index, Project State/module/profile as warranted, checkpoint and PR with b48 Runtime + exact b49 evidence. Do not change TD-024/TD-025 before a later explicit Runtime-backed architecture decision.

## Next exact action

Create the non-CI b49 assembly branch, make only the compact `o/p/v` patch correction plus Candidate identity files, audit the exact four-file diff, fast-forward it to the real branch, then autonomously continue through CI/package verification to the exact-device b49 Runtime gate. Do not wait for an extra `继续` reply.