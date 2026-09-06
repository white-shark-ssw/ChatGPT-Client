## b113 Human Runtime Positive — native message presentation 2026-09-06

Exact Human Runtime evidence:

- Diagnostics `sha256:334a2f88d284e04936f0226c3cb6bdbad0710f1af5ead9c8168301fc5581af55` and screenshot `sha256:be52e664e6f62b49e4432e98379ff7d2280f09693c8f6a66827665c51acbb184` are from the exact canonical package identity: Release `0.1.0 (113)`, Candidate `DEV-message-rendering-0.1.0-b113`, source marker `75ccad152086`, bundle `com.whitesharkssw.chatgptclient`, iPhone, iOS17.0.
- All 78 exported events are `info`. The export contains 18 `assistantChunkColor.willDisplay` and 18 `assistantChunkRender.afterDisplay` samples covering chunk indexes `0...4` / rows `1...5` of the five-chunk authoritative assistant answer.
- Every captured direct-attributed, UILabel CALayer, UILabel hierarchy and hierarchy-crop blue-dominant fraction is `0.000`. Assistant reuse provenance is only `none` or `assistant`, never `user`; all 18 prior-link reuse counts are `0`; current assistant body link-run counts are also `0`. The b112 role-isolated reuse fix therefore remains intact under repeated b113 scrolling/reuse.
- Screenshot directly verifies the user-color acceptance case: `https://github.com/white-shark-ssw/ChatGPT-Client.git` is blue while the immediately following Chinese prose is normal `.label`, so the previous over-broad bare-URL range is not reproduced.
- Screenshot also shows native/readable assistant presentation: emphasis is visually bold, `ChatGPT-Client` inline code uses a code treatment, `2 分钟筛选结果` is rendered as a heading, the pipe-table delimiter control row is no longer exposed, table content remains readable, and the raw private-use `filecite` token is replaced with a readable `[文件引用 L2-L2]` label. No guessed citation click-through is claimed.
- The export contains one `message.copy` for `user` and one for `assistant`. Diagnostics prove the full-message Copy actions were invoked but do not expose clipboard payload bytes. The user explicitly reports this b113 result has no problem, so the tested interaction scenario is accepted without inventing telemetry that was not captured.

Classification:

- b113 is **Human Runtime Positive for the tested native message-presentation scope**: link-only blue user text, readable assistant rich-text/citation presentation, long-message reuse/geometry behavior in the supplied scenario, and preservation of the b112 assistant-color invariant.
- This result does not make `DEV-send-stream` Stable/Frozen and does not exercise the separate b107 accepted clean-EOF recovery gate.
- Citation destination navigation remains intentionally out of scope until authoritative annotation/resource objects are retained. Do not infer clickable source resolution from this result.
- No b114 product candidate is justified by this evidence.

Integration boundary:

- `DEV-message-rendering` remains **Active — Human Runtime Positive / stacked integration pending / Stable-Frozen No** because PR #36 is stacked onto the separate Active `DEV-send-stream` branch. This task session must not merge PR #36 and silently advance another task's branch/checkpoint from b112 to b113.
- Product/package/Artifact identities remain unchanged. PR #36 is now explicitly marked Human Runtime Positive; the next action is stacked integration coordination by the owning `DEV-send-stream` path.

**Evidence ladder:** Code written / exact scope + static diff check + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / **Human Runtime Positive for tested b113 presentation scope** / Stable-Frozen No.

# DEV-message-rendering

## Runtime evidence settlement recovery point — 2026-09-06

- **Exact pre-settlement branch head**: `67a10de87228da7ad07da3337684d68cc43a965f`; stacked PR #36 remains open/mergeable against unchanged `dev/send-stream-20260829` head `50432b8743f3391a8174a3b7aae745298082d433`; `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- **Canonical identity revalidated**: `DEV-message-rendering-0.1.0-b113` / Build113 / package source `75ccad15208610c2b0420033846f9bb15bbdb494` / Artifact `9976713893` / IPA `sha256:2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`.
- **New Human Runtime evidence**: diagnostics file `sha256:334a2f88d284e04936f0226c3cb6bdbad0710f1af5ead9c8168301fc5581af55`; screenshot `sha256:be52e664e6f62b49e4432e98379ff7d2280f09693c8f6a66827665c51acbb184`; user explicitly reports the result has no problem and authorizes continued progress.
- **Evidence summary before durable settlement**: Diagnostics metadata is Release / Build113 / Candidate b113 / source `75ccad152086` / iPhone / iOS17.0. All 78 events are `info`. Eighteen `assistantChunkColor.willDisplay` and 18 `assistantChunkRender.afterDisplay` samples cover chunk indexes `0...4`; every direct-attributed, UILabel-layer, UILabel-hierarchy and hierarchy-crop blue-dominant fraction captured is `0.000`; `reusedFromRole` is only `none` or `assistant`, never `user`; all prior-link reuse counts are `0`. User and assistant Copy actions are both present. Screenshot directly shows the GitHub URL blue with immediately following Chinese text normal, readable heading/emphasis/inline-code/table presentation, readable `[文件引用 ...]` replacement, and no assistant blue/normal regression in the visible answer.
- **Batch D — completed**: b113 Human Runtime Positive is durably recorded in the Build/Test Index, project state/module/profile, technical decisions, project-specific rules, and this checkpoint with the exact screenshot/diagnostics evidence boundary preserved. Recorder run `33992001595` succeeded and committed durable Runtime truth at `24237d2fd98f1198ebe89583fb1a11a3ffde08a0`.
- **Batch E — completed**: PR #36 title/body now classify b113 Human Runtime Positive and set stacked integration coordination as the next action. PR remains open/mergeable; it was intentionally not merged into the separate Active `DEV-send-stream` branch.
- **Do not touch during settlement**: product code, Build/Candidate identity, Artifact identity, PR #29 body/branch, `DEV-send-stream` checkpoints, Send/SSE/Repository authority, or b112 role-isolated reuse.

## Status

**Active — Human Runtime Positive / stacked integration pending**

- **Work ID**: `DEV-message-rendering`
- **Routing aliases / keywords**: `消息渲染 / Markdown / 富文本 / filecite / 引用 / 链接颜色 / 用户链接`
- **Task**: Implement native user/assistant message presentation for link-only blue user text plus Markdown/code/table/file-citation display.
- **User intent / acceptance criteria**: User message ordinary text must use normal label color while only actual links are blue, including a bare URL immediately followed by Chinese text. Assistant body must stop exposing raw Markdown control syntax for headings/emphasis/lists/code/tables and must consume raw `filecite` control tokens into readable native presentation. Preserve the b112 assistant color fix. Citation target navigation is not to be guessed without authoritative annotation/resource evidence.
- **Baseline**: Stacked on `DEV-send-stream` Runtime-positive b112 branch head `50432b8743f3391a8174a3b7aae745298082d433`. Canonical b112 product/package/Artifact remain `3957b806f32f0995ceb9cf8f9487aba939f3b306` / `b5e3164721e01ceb1fe320ebd290bda79a921fc2` / `9975978222`; b112 Human Runtime diagnostics `sha256:36fd01529ee522fd0646f7bdf6e6f409dca3f55a4b17ff21c88e4e19d16e23b2` prove role-isolated assistant reuse color consistency on iPhone/iOS17 light appearance.
- **Working branch / PR / head commit**: `dev/message-rendering-20260906`; stacked PR #36 -> `dev/send-stream-20260829`; current docs/runtime-settlement head follows `24237d2fd98f1198ebe89583fb1a11a3ffde08a0`; exact product remains `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`; exact package source remains `75ccad15208610c2b0420033846f9bb15bbdb494`. Later docs/tooling commits do not replace this canonical package identity.
- **Candidate identity**: `DEV-message-rendering-0.1.0-b113` / `0.1.0 (113)` permanently reserved; canonical Artifact `9976713893`; ZIP SHA-256 `51d5bcd5e804c2877faafa67f4bb263d6d849b83a24c4c28982c6880aecc7ebf`; IPA SHA-256 `2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`.
- **Evidence**: Canonical b113 diagnostics `sha256:334a2f88d284e04936f0226c3cb6bdbad0710f1af5ead9c8168301fc5581af55` + screenshot `sha256:be52e664e6f62b49e4432e98379ff7d2280f09693c8f6a66827665c51acbb184` are Human Runtime Positive for the tested presentation scope. User URL color boundary, rich assistant rendering, readable non-interactive citation label, repeated long-message reuse, and b112 assistant-color regression safety all pass in the supplied scenario; user explicitly reports no problem.
- **Files / modules in scope**: Exact product scope is `ChatGPTClient/Conversation/ConversationFeature.swift` + `ChatGPTClient.xcodeproj/project.pbxproj`; task checkpoint and durable presentation docs as evidence changes.
- **State owner / shared dependencies**: `ConversationRepository` remains authoritative content owner. This task owns presentation transformation only. It depends on unmerged b112 message-cell role-isolated reuse and b38 bounded long-message presentation geometry.
- **Frozen / do-not-touch**: Do not change protected Send/SSE/Web executor/recovery authority; do not merge user/assistant reuse pools; do not expose hidden reasoning/tool/system content; do not invent citation URLs/file navigation from opaque `turnNfileM` tokens; do not add third-party rendering dependency without explicit evidence/need.
- **Parallel conflicts checked against**: `DEV-send-stream` / PR #29 touches the same `ConversationFeature.swift` and is therefore an explicit stacked dependency, not an independent parallel task. PR #35 is research-only and does not touch product `ChatGPTClient/**` or product build identity. `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. b113 is uniquely reserved to this task.
- **Completed**: Governance/preflight; isolated stacked branch/checkpoint; b113 durable allocation; product implementation; exact staging run `33991155027 / 101373512529` passed baseline guard, exact two-product-path scope, `git diff --check`, Debug Simulator compile, and committed product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`; Push+PR package CI passed; canonical Artifact/package independently verified; Human Runtime Positive durably recorded; PR #36 Runtime status updated.
- **Validation state**: **Code written / exact scope + static diff check + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime Positive for tested b113 presentation scope / Stable-Frozen No.**
- **Pending**: stacked integration coordination only. No b114 product candidate is justified by current evidence.
- **Next exact action**: continue from the owning `DEV-send-stream` task if integration is desired: re-run that task's resume/conflict guard, then decide/record how PR #36 is integrated without silently invalidating its b112 checkpoint/candidate state. Do not merge PR #36 from this task checkpoint.
- **Rejected / do-not-repeat**: Do not treat b112 color fix as unresolved; do not use Foundation's over-broad bare-URL Markdown range for user color; do not add UILabel `.link` attributes merely to make text blue; do not simply hide all citation evidence; do not implement guessed click-through citation resolution; do not parse raw Markdown separately after 1200-character chunking; do not fully reparse active growing assistant Markdown on every token.
- **Open questions / risks**: Current authoritative model retains only visible text and does not retain server citation annotation/resource objects, so b113 can present `filecite` cleanly but cannot claim authoritative source opening. Stacked integration remains intentionally separate because the base branch belongs to another Active task.

## Batch recovery point — b113 staging/package

- **Exact allocation commit**: `f90caf1f6836b4bba572dc1f4026ebe2f1538d3d` records b113 in `BUILD_TEST_INDEX.md` before product changes.
- **Batch A — completed**: `DEV-message-rendering-0.1.0-b113` / Build113 is durably recorded as this task's unique reserved candidate.
- **Batch B — completed**: exact product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`; staging `33991155027/101373512529` passed exact product scope, `git diff --check`, Debug Simulator compile; only Xcode identity + `ConversationFeature.swift` product paths changed.
- **Batch C — completed**: package source `75ccad15208610c2b0420033846f9bb15bbdb494`; stacked PR #36; Push `33991287459/101373866191` and PR `33991302325/101373908835` passed; canonical Artifact `9976713893`; ZIP/IPA identities independently verified. Human Runtime has now passed and is durably recorded above.
- **Recovery rule**: never replay completed batches. Preserve b112 product/package/Artifact/runtime identities unchanged; preserve PR #29 and PR #35; do not touch Send/SSE/Repository authority or b112 role-isolated reuse identifiers. If interrupted, re-read this checkpoint plus actual branch/PR state and continue only from the explicit stacked-integration boundary above.
