## DEV-send-stream b109 model-state Runtime result / b110 render probe — 2026-09-06

- Canonical b109 diagnostics `sha256:37669df4cddc25db7b0d3bb1ae96d54d722aee501fcf3e55888aff636d8edcdf` contain 16 chunk `willDisplay` samples. The target completed authoritative answer remains 2 messages / 6 rows / 0 live rows / one 5-chunk assistant message.
- Every sampled assistant chunk resolves all exposed UILabel text/attributed/highlight/tint colors to white with no highlight/selection state, while the user still observes blue/normal alternation. Exposed UILabel model state is therefore rejected as the differentiating color owner.
- b110 Build110 is reserved as a diagnostic-only after-display rendered-pixel aggregate probe for UILabel-only versus the same rectangle in the cell hierarchy. No color fix is claimed.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b109 package-qualified diagnostic Runtime gate — 2026-09-06

- Candidate `DEV-send-stream-0.1.0-b109` / product `11e7ec536b986c45811dc449cd2c4f6e442c28df` / package `8c6ea43677f2a0f39c08d6b9ca695c9c2e4a5267` is package-qualified after corrected staging `33984605217/101355720829`, Push `33984671709/101355898061` and PR `33984673860/101355903471` success.
- Canonical Artifact `9974791883` / ZIP `743e61fc4f20670d8a6cc5d5afd42f8942e40f2943abe1f9b23e4ca621b43956` / IPA `6c37dfb8496c533ce2d5e4878f22a5b265f7c55e87e9cbfbb9189155fa30096a` independently verifies Build109, Candidate b109, source `8c6ea43677f2`, Release, iOS14+, iPhone/iPad and arm64.
- b109 is diagnostic-only: per-chunk assistant `willDisplay` logs final UILabel/attributed/highlight/tint/selection state without message text/IDs and without changing rendering or Send/SSE/Repository/recovery behavior.
- Human Runtime diagnostic pending. b108 chunk-row color remains Runtime Negative; b107 accepted clean-EOF recovery remains Unexercised.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b108 Runtime Negative / b109 diagnostic gate — 2026-09-06

- Exact b108 diagnostics `sha256:c26f5ed8712ca63c8dae037e58330d5fa4b2f7cb47b8b0dafc078e920b4c813c` keep ordinary New Chat one-Send/terminal/authoritative reconcile Positive and keep b107 accepted clean-EOF recovery Unexercised because `stream_ended_without_done` did not occur.
- Exact video `sha256:6cecee7a5f249529c72c53ee08620740e9d8480b080d8914476f697ad0efdc73` proves the completed authoritative assistant answer alternates blue/normal across long-message presentation chunks even after `liveSnapshotCleared=true`; post-reconcile state is 6 authoritative rows / 0 live rows with one 1200-character-chunked assistant message.
- b108 color ownership correction is Runtime-insufficient. b109 Build109 is reserved as a diagnostic-only per-chunk UILabel final-state probe; no new color fix is claimed yet.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b108 package-qualified Human Runtime gate — 2026-09-06

- Candidate `DEV-send-stream-0.1.0-b108` / product `eb0de74460b0bd06a6d977bf915b5e06a5c946db` / package `d34ff4534ca76ee03e2c8a3eeddb29eca011319f` is package-qualified after staging `33981732350/101348043849`, Push `33981838027/101348321052` and PR `33981839719/101348326124` success.
- Canonical Artifact `9973988017` / ZIP `8e445a65346b9a32d8811645f2e21a2f1340942c9e7333beb4ddfc4c6a8a7c14` / IPA `a2639b5793316077c0f203bfd4dffdecd8cef74c361a4995bc8bfba05f657dbd` independently verifies Build108, Candidate b108, source `d34ff4534ca7`, Release, iOS14+, iPhone/iPad and arm64.
- Product scope is only Xcode Build/Candidate plus `ConversationMessageCell` assistant-body post-attributedText `messageLabel.textColor = .label`. Send/SSE/Repository/recovery and reasoning/user-link rendering are unchanged.
- b108 Human Runtime is Pending. Exact gate is normal assistant placeholder/final body color with reasoning SSE unchanged, plus ordinary New Chat Send regression. Inherited b107 accepted clean-EOF recovery remains Unexercised until exact `stream_ended_without_done` occurs.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.

## DEV-send-stream b107 Runtime Partial / b108 body-color gate — 2026-09-06

- Exact canonical b107 diagnostics `sha256:8e3e10b44e8e627f60e7a831d48f11c7fa9fff4bc4b0446b71588fbc38ade7da` / 411 events / Release / iPhone / iOS17.0 / source `4bd3501a3092` shows one New Chat protected HTTP200 SSE Send, authoritative SSE conversation-ID handoff, normal reasoning/final stream, `terminal` / generation `phase=completed`, then automatic HTTP200 authoritative Detail reconcile with `liveSnapshotCleared=true`.
- Zero `stream_ended_without_done` / accepted-client EOF recovery diagnostics occurred, so the b107 accepted clean-EOF same-generation branch remains Unexercised. The b107 manual-Sync stale-live target state also did not occur because the generation terminated normally.
- Exact screenshots `sha256:5b8d52c002a468ba6d5a79bacc1b922081c0fdc30d71880d0de0fadf9096a0b7` / `sha256:037b207c15012633a569087c2024abdd249a8646e3ad030d5726591135c20798` plus user observation reproduce the assistant body blue-text defect: placeholder/final body blue while reasoning SSE text is normal. Current source maps the split to `ConversationMessageCell.messageLabel` versus `reasoningTextView`; b106 pre-attributedText color/tint reset is Runtime-insufficient.
- b108 is allocated as `0.1.0 (108)` for one narrow `UILabel` body-color ownership correction only. Overall Send/Stream remains Runtime Partial / Stable-Frozen No.

## DEV-send-stream b105 authoritative new-chat first Send package ready — 2026-09-05

- b105 fills the missing new-conversation first-Send path without changing TD-029 ownership: official Web still owns protected Send/challenge; `ConversationRepository` remains sole Native response/content authority. Native creates no fake server conversation ID.
- Product `6ef4e874d7c2c5f144ab7e784f7a81755d1b2f59` is exact three-product-path scope. Corrected staging `33923512745/101186860450`, Push `33923732331/101187538891` and PR `33923735651/101187548902` passed. Canonical Artifact `9956018294`, ZIP `sha256:ba53bc8e50e1b89056565e3a557e196ef6b9c5db76e3b40dd28a0536e81d6921`, IPA `sha256:d162a7132ff830d3a2f6eb85a2b4a5b4ebc2d9f84531b01418912c99109e5095`; package independently verified Build105/Candidate b105/source `93ab92a9a4a7`/Release/iOS14+/arm64.
- First new-chat protected fetch is gated on a real official-page route conversation identity. Missing identity blocks the fetch with `new_conversation_identity_missing`; successful identity handoff re-keys the same executor and starts one Repository generation. Terminal Detail then performs one list refresh for sidebar convergence.
- Human Runtime pending. Stop remains unimplemented pending exact route/target/ack evidence; true background execution and b101 exact `-1005` branch remain separate evidence boundaries. Stable-Frozen No.

## DEV-send-stream b104 background-return Runtime Positive — 2026-09-05

- Exact b104 diagnostics `sha256:3789dc478c0bdf46c0f2ca2f572ebc618b4f53299e39fe68086e6dc936387216` closes the normal no-probe Send regression as Runtime Positive: one accepted HTTP200 SSE Send, no kill probe, no duplicate Send, same generation through terminal, then automatic authoritative Detail `21 -> 23` and live-state clear.
- The app entered background for ~96s. Most response events were not processed until the foreground timestamp, where 123 queued live events including 94 final deltas arrived immediately before terminal. This supports foreground backlog replay + authoritative convergence, not a claim of continuous WebKit execution while iOS was suspended.
- User-visible sequence “answer already visible, then loading” matches this architecture: queued live content is presented first; terminal immediately starts one authoritative Detail sync which confirms/replaces it with server-backed state about 2.25s later.
- No product/b105 change is justified from this successful sample. Stable-Frozen remains No because broader unresolved/unexercised gates remain separate.

## DEV-send-stream b104 normal no-probe recovery package ready — 2026-09-05

- b103 Human Runtime `sha256:99049f500c129571d33aa628720f7d23ce5cf6d183e887938cd7fa621a3bbc51` closes the accepted-client hard-Web foreground recovery gate as Runtime Positive: exactly one HTTP200 SSE accepted protected Send survived hard WebContent death, the same Repository generation automatically attached one fresh covered observer without a lifecycle nudge or resend, page-owned status/snapshot/resume continued, and terminal authoritative Detail converged `19 -> 21` and cleared live state.
- b104 removes only the deterministic b102/b103 test surface: no `CoveredWebProcessKillProbe`, no AppDelegate installer, no `_killWebContentProcessAndResetState`, no 120-second test timer. Accepted-client recovery in Root is unchanged. Product `4aebb546f3be6b71de0a67f466e6557a357dbfdc`; package `08fab73ab9a6fb83f6aa97702d2d4cd358b6ec43`.
- Staging `33917182143/101166941594`, Push `33917342654/101167460031`, PR `33917346052/101167471587` passed; Artifact `9953695815`; ZIP `sha256:2ef6278a72fd46e86cb279a97e0e84b2228b5c78eb390cdc7582229b84e3d82e`; IPA `sha256:9c35141e9877621d3a7e39245982cba6722acbb17a19f5ebabd8734d2b94df04`; package independently verified b104/source `08fab73ab9a6`/Release/iOS14+/arm64.
- Human Runtime for b104 is pending ordinary no-probe Send regression. No true-background/silent-stall/pre-acceptance recovery claim; Stable-Frozen No.

## DEV-send-stream b103 accepted-client hard-Web recovery package ready — 2026-09-05

- b102 Human Runtime `sha256:6d2fde277427d3bbad6549946855c68b8df7e0433389b2d5c9e7d98212a3a6a6` proves an explicitly accepted client-owned protected Send can survive hard WebContent death server-side and later finish through the existing covered observation + authoritative Detail chain without a second Send. The remaining defect was local: b102 marked the prompt-owned generation failed and required a lifecycle nudge to rediscover it.
- b103 preserves that same Repository generation after hard WebContent death **only after** HTTP200 `text/event-stream` Send acceptance. While active it immediately releases the dead executor and attaches one fresh covered observer; while inactive it defers the reattach until foreground. Pre-acceptance death remains failure. No prompt replay/regenerate, retry loop, polling, heartbeat, guessed resume or second response store is added.
- Exact product `d514e9a5bde01bf3243d81016bf8cbda533fd5bf`; package `e1cca160e9c466ab98a2aeffc038e94f58335cab`; corrected staging `33913972639/101156743875`; Push `33914210593/101157497020`; PR `33914214638/101157509705`; canonical Artifact `9952548424`; ZIP `sha256:27fc23f1cb48d585ab3ffc0b181ec0dffafc42ccb3069fd72cbf5a0ba647f77a`; IPA `sha256:f41c81a89552027fb4c42152eb3864c1732494465230ffd4787c6bba56d746c3`. Independent package inspection verifies b103/source `e1cca160e9c4`/Release/iOS14+/arm64.
- Human Runtime pending. The b103 120-second kill is still explicit test instrumentation only; no true background-execution claim. Stable-Frozen No.

## DEV-send-stream b102 deterministic hard-Web kill probe package ready — 2026-09-05

- User explicitly authorized a deterministic two-minute forced-Web test because natural `WKWebView` WebContent termination is difficult to reproduce. b102 is diagnostic instrumentation only; current client-owned WebContent-death failure semantics are intentionally unchanged until Runtime proves the server/Native outcome.
- Exact product `670310b4e8b15176f721291f4f96e46feadec46a`; package source `78bd3d2f3e45c8e0061865d3133b92a274139110`; Push `33910845721/101146639944`; PR `33910858535/101146674919`; canonical Artifact `9951331101`; ZIP `sha256:2da6bb66d0c5eba55d93463881e0ff5d0d55a9d7844f068d024e5cee31dff24a`; IPA `sha256:53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`.
- The first covered protected-Send submit in exact b102 arms one 120s action on that `WKWebView`; it calls WebKit `_killWebContentProcessAndResetState` only if available. It adds no resend/regenerate, no retry, no Native resume/status, no background keepalive and no second response/content authority.
- Human Runtime pending. b101 exact `-1005` transport renewal remains separately Unexercised; b102 does not supersede or claim it. Stable-Frozen No.

## DEV-send-stream b101 Human Runtime normal-path/regression update — 2026-09-05

- Exact b101 diagnostics `sha256:f7209546f3f2d1dd8ad08458b0dea8adbef522af100deb2f5de90cbe26180b9d` / 95964 bytes / 182 events / Release / iPhone / iOS17.0 / source `da103452236e` contains no `-1005` and no b101 transport-recovery diagnostic, so the bounded Native read recovery remains Unexercised rather than accepted.
- Previously-open b100 gates are now Runtime Positive: dormant unfinished remote turn auto-discovered `13 -> 14` with `rearmDiscoveredRemoteTurn=true`, then covered observation reacquired HTTP200 `IS_STREAMING` and a reasoning/tool snapshot; a later known-active foreground return auto-reconciled `14 -> 15` with `authoritative_assistant_materialized`.
- A later ~17m35s dormant interval auto-discovered authoritative `15 -> 17` via HTTP200 with no manual Sync/Reload. Two user-WebSocket `error/close(1006)` events occurred during earlier foreground returns, but no hard WebContent-process termination callback occurred.
- This sample has zero client-owned protected-Send evidence, so it does not qualify accepted-Send recovery after Web/WebContent death. No product/b102 change is justified; canonical b101 remains the Runtime candidate, overall Runtime Partial / Stable-Frozen No.

## DEV-send-stream b101 Native read transport recovery package ready — 2026-09-05

- Exact b100 Runtime `sha256:515c60b59d969ee1f33d76fec097d6163450058c5ef3fa9ccd551b2439f03818` adds a new failure classification: after ~12m37s suspension, b100 foreground discovery still triggered, but Native Detail/list/manual Sync repeatedly failed exact `NSURLErrorDomain -1005` while covered Web networking independently reopened. This rejects the hard-WebContent-death hypothesis for that sample and exposes stale cached `AuthTransientSession` reuse as the Native read recovery gap.
- b101 is the evidence-scoped correction: first exact `-1005` from conversation-list or Detail GET retires only the matching cached transient session, reacquires one fresh transient session through existing WebKit auth, and retries the same idempotent read at most once under the same operation generation/account scope. No timer, cadence, reachability watcher, retry loop, background heartbeat, Send replay or second authority is added.
- Product `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; package source `da103452236e31e070eae68b9e7979a832662fc1`; staging `33903822115/101123907440`; Push `33904070096/101124706091`; PR `33904076581/101124726725`; canonical Artifact `9948780963`; ZIP `sha256:df5e95d273c0a4f977b47ac7b64eb654daea99e3b797c3c54924b820fd165e64`; IPA `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`.
- Package identity independently verified as `com.whitesharkssw.chatgptclient`, `0.1.0 (101)`, Candidate b101, source `da103452236e`, Release/iOS14+/`[1,2]`/arm64. Human Runtime pending; Stable-Frozen No.

## DEV-send-stream b100 Human Runtime dormant-discovery Positive — 2026-09-05

- Exact b100 diagnostics `sha256:f0f3619ea61f30f9bcbaadbb577f3a99839a032dfcd95503e22b4a7bdb984696` / 72063 bytes / 127 events / Release / iPhone / iOS17.0 / source `e88a50ad9c20`.
- With the selected conversation idle at 8 visible messages, the app stayed backgrounded 1171s (~19m31s). Foreground automatically emitted `foregroundConversationDiscovery.requested`, issued exactly one authoritative Detail, and materialized `8 -> 10` (`addedVisibleMessageCount=2`, `latestUserChanged=true`) without manual Sync/Reload. Completed remote state required no covered rearm (`rearmDiscoveredRemoteTurn=false`).
- A second 327s (~5m27s) background return issued one automatic discovery and remained `10 -> 10`; a later manual Sync also remained `10 -> 10`, confirming the automatic path had already converged.
- The existing user WebSocket errored/closed with code 1006 on the long return and then reopened; no `webViewWebContentProcessDidTerminate` signal occurred. Dormant authoritative discovery is Runtime Positive even with a broken/stale user WebSocket, but hard WebContent recovery remains Unverified.
- No b101/product change is justified. Unfinished remote-turn rearm, exact-b100 known-active reconcile regression, b99 backlog coalescing stress and b98 hard WebContent termination recovery remain separate unverified gates. Stable-Frozen No.

## DEV-send-stream b100 foreground dormant-discovery override — 2026-09-05

- b99 Runtime: known-active external response auto-reconciled authoritative Detail `5->6` after ~7m32s background. After that response/executor was released, a later ~12m54s background interval had no automatic foreground discovery; manual Sync recovered `6->8`. b99 is Runtime Partial; its backlog-coalescing stress is Inconclusive in this sample; hard WebContent-death recovery remains Unverified.
- b100 changes only foreground discovery: selected conversation + no client-owned active response + no Detail operation => exactly one existing `ConversationRepository.syncLatestMessages`, even without a pre-existing external snapshot. Completed server state materializes directly; a newly discovered unfinished remote user turn may rearm the existing covered observer once.
- No polling/timer/retry/watchdog/background heartbeat/resend/guessed resume/second response authority.
- Exact product `70c7dc052865ef80ca7bdec083d7621c1a297eab`; package source `e88a50ad9c2098449b43fb0fce2c441a50cd20ac`; staging `33895020559/101095508915`, Push `33895244146/101096229135`, PR `33895249810/101096247432` passed; Artifact `9945483725`; IPA `sha256:5629deedca665b7a5cfa7e36b4996b7b1e4b7a160ca5cb35a465abfbd97fbc69`; Human Runtime pending; Stable-Frozen No.

## 2026-09-04 — b99 live-presentation coalescing package ready

- b98 Human Runtime exact diagnostics `sha256:e0a0bd2c42168d0c3f8a6dd681bbad1bb571d4061b0f2958131cae5f8e059105`: no hard WebContent termination event occurred, so that new b98 branch remains Unverified. The included foreground authoritative Detail reconcile is Runtime Positive, but a later client-owned response replayed 170 buffered live events after ~5m background and drove 169 synchronous full presentation applications; user observed freeze/crash and a fresh `launch.start` followed 3s after the last live event.
- b99 is the evidence-scoped stability correction: preserve every Repository event/state transition, but coalesce only the expensive selected Detail UIKit presentation onto one pending main-queue application using the latest Repository snapshot. No timer, retry, watchdog, polling, transport mutation, Send replay or second response authority.
- b99 exact product `ec05c284010cb0f2de066bd1cfc3968e07730779`; package source `313c4c3bf2ac0dc729d4793198fe462ada5a14eb`; staging `33890678564/101081289220`; Push `33890809275/101081720750`; PR `33890812345/101081730258`; Artifact `9943798885`; IPA `sha256:68b7f99eac8fd1d3ab14c6085abd4a084f2b4759dc630f94044017c9a4aecf02`; Human Runtime pending; Stable/Frozen No.

# Project State

## DEV-send-stream b107 package-ready Runtime gate — 2026-09-05

- b106 Runtime is Partial: SSE authoritative New Chat identity is Positive, while accepted-SSE clean EOF false-failure and stale-live double presentation are Negative; assistant blue text remains unresolved.
- b107 product `113fa19d7264b953949770d2e44cb500ded2da6b` and canonical package `4bd3501a3092dfe7aad7ea836ba0cb8e42b0d65f` preserve the b106 SSE-ID handoff and add only same-generation accepted EOF recovery plus authoritative manual-Sync stale-live cleanup.
- Staging `33960451799/101291316464`, Push `33960627676/101291785599`, PR `33960629168/101291789461` all passed. Canonical Artifact `9967821935` / ZIP `d2036ed0372b16c7690c9d3b324d680db6a522fd5ace26d27afa8733a95a9585` / IPA `7195d89cb9837efc3386c5dd7e030e7f11f10233689416e59c86d1ae4cf055cd` are independently package-verified.
- Evidence ladder: Code / guarded Simulator / Push CI / PR CI / Artifact / package identity verified; Human Runtime Pending; Stable-Frozen No.


## 2026-09-04 — b98 hard WebContent external-observation recovery package ready

- User explicitly skipped b97 Human Runtime; b97 is recorded as Runtime Not Executed and remains permanently reserved. b98 is the next unique Runtime candidate.
- `DEV-send-stream-0.1.0-b98` / `0.1.0 (98)` exact product `2edd55febe2005071722ddcb9989151b427165d8`, package source `17c65a390f2724a55cd29d466e01eaab988dcbfe`, PR #29 open/unmerged.
- b98 changes hard covered-Web process death for external/cross-platform observation from response failure into transport interruption: preserve the existing external Repository live response and callbacks; immediately full-page rebootstrap once if foreground, otherwise defer to the existing foreground recovery path. Client-owned protected Send still fails on WebContent death and is never resent automatically.
- Guarded staging `33886277311/101066715850` passed exact two-product-file scope + Simulator. Push `33886537405/101067576599` and PR `33886540813/101067587985` passed. Canonical Artifact `9942092070`; ZIP `sha256:f290b8a4d871016ce93a186b15c10e505a2a1d41b4adce4d19859d92fb65b3ae`; IPA `sha256:b1dc76dbe28e77ceac3468e8cfd3ca0ded41601bd02db6b228bd391a1d697b67`; independent package identity verified as b98/source `17c65a390f27`/Release/iOS14/arm64.
- Human Runtime Pending. This does not claim silent page-loop stall detection or true background execution; Stable/Frozen No.

## 2026-09-04 — b97 foreground authoritative Detail reconcile package ready

- b96 Human Runtime disproved its ordinary-Detail async-status trigger as sufficient: target Detail returned `conversation_async_status` missing both before and after completion. Background return performed covered-Web rebootstrap but no automatic Native Detail; a later manual one-shot `syncLatestMessages` changed visible messages `46->47` and immediately reconciled the final assistant.
- `DEV-send-stream-0.1.0-b97` / `0.1.0 (97)` is now permanently reserved. Exact product `12fc1d1f5020d76d1892c25a0ced94323d5a0142`; package source `5e43c398b52a62de9f9a6e6546de7312ba5eb1df`; PR #29 remains open/unmerged.
- b97 removes the b96 10-second Native `DispatchWorkItem` continuation scheduler. When the selected conversation already owns an active external live response and the app enters foreground, Root requests exactly one existing Repository `syncLatestMessages` if no Detail operation is in flight, while preserving the existing covered-Web foreground rebootstrap. If authoritative Detail already contains the final assistant, existing Repository reconciliation clears the external live projection and Root releases the idle executor.
- Guarded staging `33881577700/101051252468` passed exact four-product-file scope + Simulator. Push `33881896437/101052287658` and PR `33881905960/101052320038` passed. Canonical Artifact `9940228423`; Artifact ZIP `sha256:af05e9d0a522fb53c3e453bedcf9b49e44781158d7f7d8798ad1426b4c57b388`; IPA `sha256:49f8d9a8ef425409923bf904a3134265ddfa6d90597d72e04a1e976a5a8a90c7`; package identity independently verified as b97/source `5e43c398b52a`/iOS14/arm64.
- Human Runtime is Pending. This does not claim execution while iOS keeps the app suspended in background; the gate is automatic authoritative convergence when the app returns to foreground. Stable/Frozen No.

## 2026-09-04 — b96 Native async-status continuation package ready

- `DEV-send-stream-0.1.0-b96` / `0.1.0 (96)` is permanently reserved. Exact product head `9e50943de39dc304ab31904cbad8596d4ffddc14`; exact package source `cd6268540e4f5a815829f26a713b10e8d1957239`; PR #29 remains open/unmerged.
- Native `ConversationRepository` now parses authoritative Detail `conversation_async_status` only for exact evidenced `IS_STREAMING` / `COMPLETE`. Exact `IS_STREAMING` may schedule the existing Conversation Detail GET at the current 10s candidate approximation; non-streaming/missing/unknown stops or does not start. Protected Send remains TD-029 Web-owned and client-owned responses take precedence.
- Push CI `33877378585/101037475567` and PR CI `33877383271/101037490825` passed. Canonical Artifact `9938422716`; Artifact ZIP `sha256:5ea65cfb07c1c15dfc939646bbe7a2600825ba3ca1dab9ed100803037df3bd67`; IPA `sha256:a635903898324bdf0e59cf8712a2ebd5924def0da591d555fb25d2f62dabc361`; package identity independently verified as b96/source `cd6268540e4f`/iOS14/arm64.
- Human Runtime remains Pending. This is not Stable/Frozen proof.

## 2026-09-04 — Probe v0.6 exposes Swift-async dispatch-data callback surface / v0.7 gate

- Exact v0.6 Runtime `sha256:1cb6eb096c5748e7f781afbd761906bda39d55227a115a4e2dcea8c240de7a43`: 78,828 bytes / 207 events / zero parse errors / all v0.6.
- `probe.detail_task_callback_surface` Runtime-proves `__NSCFLocalSessionTask` exposes `connection:didReceiveData:completion:`, `_task_onqueue_didReceiveDispatchData:completionHandler:`, `_onqueue_didReceiveDispatchData:completion:`, plus `OS_dispatch_data` buffering ivars `_dataTaskData` / `_pendingResponseBytes` and completion block `_dataTaskCompletion`. Exact invocation order remains Unverified until the next observer.
- Same target Conversation Detail polling remains Runtime Positive after relaunch at ~10–12s intervals. Probe v0.7 is research-only and hooks only `_task_onqueue_didReceiveDispatchData:completionHandler:` to run the existing exact `conversation_async_status` scanner; no product network behavior changes. Product remains b95; b96 unallocated.

## 2026-09-04 — Probe v0.5 Runtime reconfirms Native Detail polling / v0.6 callback-surface gate

- Exact v0.5 JSONL `sha256:26e8646945831764bf6317c99213ff8a9621d09942e642a19b4f15aa24c892ba`: 47,648 bytes / 146 events / zero parse errors / all v0.5. Target `0df178903e95` again issued repeated `__NSCFLocalDataTask` authoritative Conversation Detail GETs at about 9.3s median after reacquisition.
- Zero `http.conversation_detail.async_status` events means the v0.5 public `URLSession:dataTask:didReceiveData:` hook did not cover the Swift-async Detail response path; it does **not** prove the field is absent. Native Detail polling remains Runtime Positive; exact async-status semantics remain Unverified.
- Probe v0.6 is research-only and records one bounded callback-surface snapshot from the first target Detail task (relevant selector/ivar names and type signatures only). It installs no guessed private callback hook and reads no content/auth. Dedicated research CI `33807128921 / 100820168958` passed; Artifact `9913354388`; dylib SHA `6c834d02d2e3a271be5b070a4e4d0027f8246237bc487cd2b24984f960a170cc`; repacked IPA SHA `d09160f1dce44ad7c1b8d9e4037ad4eaf2e29b68e73424eb2a81a78921a83681`; outer ZIP SHA `d63385fefd79c3d0c18c003a56025ce0dec517e81601ee1320675b433e2a945a`. Human Runtime pending. Product remains b95; b96 remains unallocated.

## 2026-09-04 — Probe v0.5 packaged / Detail async-status Human Runtime gate

- Cross-platform late-join remains primary. v0.4 Runtime observed same-target authoritative Conversation Detail GETs at ~9.7s median and user separately recalls official iOS updates arriving in blocks rather than SSE-like token flow.
- Probe v0.5 is research-only: it retains task-resume observation and adds privacy-safe observation of only the exact `conversation_async_status` enum from Conversation Detail response chunks via `URLSession:dataTask:didReceiveData:`. It logs no content/auth and initiates no network request.
- Exact source `b5b48ac67c09f39b0a40666ad9574cfa389b900b`; research CI `33803516248 / 100808374551` success; Artifact `9911983067`; digest `sha256:97d7b854ceda48afaff8efaac387e72af56812a256d5e96477cbfc9b6dd413ce`; dylib SHA `731ebdf5716cb321fa0f0047fadbc6ccc1a628e4fb4b17d162613e156e75b92e`; research IPA SHA `f53dfc8532738dbccfe80e24dc62fe1728abe0dcd57ce6a3cd015655378da86d`; official identity unchanged and exact diff vs pristine source is three intended files.
- Human Runtime must now prove Detail active/terminal state on the same target. Product remains exact b95; b96 remains unallocated; Stable/Frozen Send No.

## 2026-09-04 — Probe v0.4 Runtime observes Native Conversation Detail polling

- Exact v0.4 JSONL `sha256:cd2b1693a423a37504d96e410c97c04a7987e76283c6458b90ff2db17dc09bd5`: 58,776 bytes / 185 events / zero parse errors / clean-log start. v0.4 task-resume observer is Runtime Positive; no v0.2-style log storm.
- Target hash `0df178903e95` issued authoritative `GET /backend-api/conversation/<id>` tasks after foreground at `48.044 / 57.378 / 67.526 / 77.369 / 86.920s`, intervals ~`9.334 / 10.148 / 9.843 / 9.551s` (median ~`9.697s`). The user WebSocket concurrently failed with POSIX 53, so this HTTPS loop is independent of that socket.
- Official binary independently contains `TriggerAsyncStatusPollingConversationObserver`, `ConversationPollingManager`, polling start/stop diagnostics, `default_interval`, `conversation_async_status`, and `backend_streaming_completed`. Runtime + static evidence strongly support Native Conversation Detail polling as the cross-platform acquisition/recovery mechanism. Exact response-state trigger/stop semantics remain Unverified.
- Repeated `/f/conversation/prepare` is send/composer preparation (`MessageInputPrepareConversationViewModel`), not late-join polling. No target `stream_status`, `/resume`, or conversation WebSocket update was observed in this sample.
- Existing product `ConversationRepository` already owns authoritative Conversation Detail GET and content projection, but currently ignores top-level `async_status`. Product stays b95; b96 remains unallocated pending authoritative active/terminal state correlation. Stable/Frozen Send No.

## 2026-09-04 — official iOS Probe v0.4 package ready / task-resume late-join gate

Cross-platform late-join remains primary. Probe v0.2 is Inconclusive because a failed user-WebSocket receive produced 392,033 events / ~76 MB of instrumentation traffic. Exact official static evidence now proves native `ConversationPollingManager` / resume-fetch recovery / stream-status polling strings plus Swift async URLSession `data(for:)` / `bytes(for:)`. Probe v0.4 therefore observes each relevant NSURLSession task at `resume`, including Swift-async-created tasks, without logging content/auth.

Exact v0.4 source `db3f8a7d01f39f364f6166cf72245db426cadef1`; CI `33795191324 / 100781074234` success; Artifact `9908872470`; digest `sha256:29675f185f8b0919821e6fdb44a3cc4ff3673187c346dd00e1f45fc3f47a8ccc`; dylib SHA `cc6a2b29b19441f56f214b199e5e7512c1739b3ae8563bc7968c0eb26779ecf9`; research IPA SHA `b4c0e53ea07bea92787ef7186b5ad79e1aa5f7bb52ebd2c2272e7060261d3d6e`. Human Runtime v0.4 pending. b95 remains product Candidate; b96 unallocated; Stable/Frozen Send No.

## 2026-09-04 — official iOS Probe v0.3 research package ready

Cross-platform late-join remains the primary Send/Stream research gate. Probe v0.2 Runtime is Inconclusive because an official user-WebSocket error produced a very large repeated-receive log storm; the absence of target events in that polluted sample is not a protocol rejection. Probe v0.3 is research-only and package-verified: source `91abb9ca95d80ea4ab646fc33effd55083e0d3ee`, research CI `33793891708 / 100776808437` success, Artifact `9908389485`, dylib SHA `cd4294d523054109886a5026bc0c3dabcc6309d8dbcfafe3d27e2c3adec14f85`, research IPA SHA `3ec2645c338f25d99c9ccf94c38190994cccd8153a0846a5d76a5ca755288d61`. It deduplicates failed-socket receive logging and adds URL-form URLSession observation only. Human Runtime v0.3 is pending. b95 remains the product Candidate; b96 is unallocated; Stable/Frozen Send No.

## DEV-send-stream official-iOS Probe v0.1 Runtime / v0.2 observation override — 2026-09-04

- User-exported Probe v0.1 JSONL (`sha256:c74a66702bd670f81a393afea1c306d2a0cce415961c9fe11be15589eeb83093`) is valid Human Runtime research evidence: 29 events / zero parse errors.
- Official user WebSocket observation is Runtime Positive, including reconnect after `NSPOSIXErrorDomain/53`, but the captured socket subscribed only to `app_notifications`, `calpico-chatgpt`, and `push_auth_challenge`; no conversation/per-turn subscribe or target conversation-update/add-messages/async-status/catchup/live frame was captured.
- Therefore direct user-socket late-join is not supported by this sample. Overall late-join remains Inconclusive because Probe v0.1 excluded ordinary conversation HTTP/Detail/status/resume/SSE and delegate response lifecycle.
- Probe v0.2 is research-only and expands privacy-safe HTTP/SSE structural observation, redacts opaque URL path parts, records direct presence state, and adds a confirmed in-app `清空` log control. ChatGPTClient product and b95 identity remain unchanged; b96 remains unallocated.
- Next gate: build/package v0.2 against the exact supplied official package and collect one clean late-join JSONL starting from `probe.log_cleared`.

## DEV-send-stream cross-platform late-join priority override — 2026-09-04

- Latest explicit priority is to solve cross-platform automatic continuation interruption first. User reports official ChatGPT iOS can continue an answer initiated on another platform; treat that as current highest-priority Runtime evidence of an official late-join capability.
- Immediate gate is research-only observation of the official native realtime path, using the already-built privacy-safe injected Probe. Client-owned Web->Native handoff remains secondary until the cross-platform path is identified.
- Re-materialized official research IPA: `ChatGPT-Official-RealtimeProbe-TrollStore-20260904.ipa`, SHA `dd40dd092853f1e4dd4e52c560df0f1b24df18ebd47ca44015065442864ba555`; source official ZIP SHA `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`; Probe dylib SHA `0d20cf4761a982612fab995ed8766a887064005a561726c603edceea6072285e`. Research tooling only; no b96 allocated.
- Next evidence must reveal actual current-account registration/subscribe/topic/offset/conversation-update semantics before product implementation. `ConversationRepository` remains Native content authority.

## DEV-send-stream b95 Runtime / transport-handoff research override — 2026-09-04

- Exact b95 identity remains product `ac5e621aa69f5f27ef3167b4a951812be8b8e2c2`, package source `a10320e589acd551a8dc53f56aaf28a0a08f5b4a`, Artifact `9901461763`, IPA SHA `2fd213a1dd692202b496adabd393c4130080607384e3d6c0f84cd3f975a8840d`. Human Runtime is now Partial; Stable/Frozen Send No.
- Hard Reload recovery is Runtime Positive: while an external live projection was active/stuck, b95 released the executor, reset the live snapshot, performed one authoritative Reload, and materialized the completed assistant (`visible 32 -> 33`, zero trailing active timeline).
- Foreground full-page rebootstrap restarted page-owned continuation repeatedly in b95 and no WebContent termination was emitted in this run. Prior exact b94 termination still blocks treating repeated/heavy full-page Web as stable; cause remains Unverified.
- Automatic external terminal/final convergence remains insufficient: prior to Hard Reload the page stayed HTTP200 `IS_STREAMING` with static service `103` / tools `30` / final `0`; final materialized only via authoritative Reload in this sample.
- Secondary b95 defect: after Reload returned no active tail, Root still recreated a covered selection observer. Cleanup is warranted but is not the primary disconnect architecture.
- Strongest next research hypothesis comes from the user's proposal: use Web only for one protected Send/bootstrap, then perform a server-issued transport handoff to Native once a matching Native continuation channel is confirmed. This is not a direct transfer of a WKWebView `ReadableStream`; it requires independently usable server continuation identity/channel.
- Client-owned and cross-device cases must be proven separately. Historical self-send probes already expose `resume_conversation_token`; external comparison evidence suggests `stream_handoff`/`turn_exchange_id`/`topic_id` may support a realtime subscription for self-submitted turns. Cross-device active Sync does not yet prove access to equivalent handoff identity.
- No production b96 or ownership-rule change from guessed transport. Next gate is privacy-safe structural proof of a server-issued Native continuation channel; page polling/cadence reproduction remains rejected.

## DEV-send-stream b93 selection-focus package-ready override — 2026-09-03

- Exact b92 Runtime is Partial: covered external continuation works and client-owned protected Send/SSE natural terminal reconciliation works, but when an external live executor overlaps a second client-owned Send, the first stream can stop advancing and does not recover merely by reselection; explicit Sync later materialized the already-completed assistant.
- Exact b93 tests one evidence-backed variable only: when reselecting an already-active external response, reuse the existing covered executor and restore WKWebView first-responder/document focus without reload or Sync.
- b93 identity: allocation `b86c1a3ca94b215204b0cfb135fa0cd8b3603619`, product `556bd8886061f4126d11e4ac44f4e24ed580500c`, package source `2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0`, Push `33755063112/100647405265`, PR `33755067202/100647418537`, Artifact `9893141097`, IPA SHA `379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d`.
- b93 package inspection: `0.1.0 (93)`, Candidate `DEV-send-stream-0.1.0-b93`, source `2d2cde58a7fb`, iOS14+, `[1,2]`, iphoneos, arm64. Human Runtime pending; Stable/Frozen Send No.
- Preserved boundary: official page owns continuation transport, Repository owns Native content. No polling/retry/watchdog/timer, Native status/resume synthesis, guessed offset, duplicate Send, WebSocket-body authority, or second response store.

## DEV-send-stream b92 covered-form package-ready override — 2026-09-03

- b91 project-scoped route identity and official page-owned live continuation are Runtime Positive; Native progressive projection works without a second Sync. Natural terminal/final remains Unverified because b91 was force-quit while still streaming.
- b92 is one isolated presentation cleanup only: it removes the b90 `bringSubviewToFront(webView)` z-order mutation and retains the b91 scoped-route parser, page-owned continuation observation, protected Send ownership, and `ConversationRepository` response authority. Manual Sync records `manual_sync_covered` but does not promote the WebView.
- Candidate / Build: `DEV-send-stream-0.1.0-b92` / `0.1.0 (92)`, permanently reserved. Allocation checkpoint `296de318c20ccc32bfea1cb93246bd9d824d3403`; exact product `96ea3e3d8c5cabf67ff33331d40c9dcc6c9f0850`; exact product/config package source `54b5803a74a123431f0a2a8e662a1a2fe874b3ca`.
- Two earlier staging runs `33749925741` and `33750233706` failed in guard-only tooling before checkpoint/product application. Successful guarded staging `33750363774 / 100632281401` passed exact b91-state guard, exact two-product-file scope audit and Xcode Simulator compile.
- Formal Push CI `33750585725 / 100632980237` and PR CI `33750591494 / 100632998279` both passed on the b92 package identity.
- Canonical Push Artifact `9891430379`; Artifact digest `sha256:f3cb6291fabcb2cf48729750d23a4403607e8ac81dc4354749974e287412e970`; IPA `ChatGPTClient-0.1.0-b92-dev-send-stream.ipa`, independently recomputed SHA-256 `82d96d359767b72c623f367bf3cd2c5f3ae9d1d7411ad547c1ba3634341c3514`, matching sidecar.
- Independent package inspection confirms Release `0.1.0 (92)`, Candidate b92, source `54b5803a74a1`, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, `iphoneos`, Mach-O 64-bit arm64.
- Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**
- Human Runtime must use a project conversation, one explicit Sync only, keep Native UI visible, prove covered `manual_sync_covered` + `route=conversation` + page-owned live continuation without a second Sync, then allow natural completion and verify terminal/final convergence before exporting diagnostics.

## DEV-send-stream b91 project live-continuation Runtime Positive override — 2026-09-03

- Exact b91 Runtime on iPhone / iOS 17.0 matches Candidate `DEV-send-stream-0.1.0-b91`, Build 91, source marker `c5985f1e2e5d`.
- Project route identity is Runtime Positive: every recorded `coveredExecutor.pageActivation` remained `route=conversation`; the prior scoped-project degradation to `route=other` did not recur.
- After one explicit Sync established the active authoritative response, the official page itself issued matching `stream_status`; HTTP200 repeatedly returned `IS_STREAMING`, `externalStreamingObserved` fired, and the page-owned `/resume` offset 0 returned HTTP404 JSON before the already-existing page-owned read path continued via `stream_status` plus plural conversation snapshots.
- Web -> bridge -> `ConversationRepository` live progression is Runtime Positive without a second manual Sync: external snapshots advanced from service messages/tools `6 / 2` to `47 / 14`, while reasoning characters advanced `194 -> 909`; Native live presentation was repeatedly applied.
- The user-visible inability to return from the official Web page is explained by the intentionally retained b90 diagnostic `bringSubviewToFront(webView)`. It is a presentation artifact, not a continuation failure; source has no balancing send-to-back in that diagnostic path.
- The app was force-quit/relaunched while the response still reported `IS_STREAMING` and `finalCharacters=0`, so automatic terminal/final convergence remains Unverified in this run.
- Evidence ladder: **Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; project route identity Runtime Positive; page-owned live continuation Runtime Positive; Native progressive projection Runtime Positive; terminal/final Unverified; Stable-Frozen No.**
- Next exact product action: retain b91 route parser and continuation observation, remove only the b90 frontmost diagnostic so the executor remains covered, then validate live progression plus natural terminal/final completion. Do not add retry/polling/timer/watchdog/Native resume or status synthesis.

## DEV-send-stream b91 project-scoped route identity package-ready override — 2026-09-03

- User Runtime distinction is now material: ordinary non-project conversations do not show the same continuation failure, while the tested project conversation does and its visible official Web appears healthy.
- Source inspection proves the injected bridge parsed conversation identity only from `/c/{conversation}`. Official project canonicalization uses the already-evidenced `/g/{scope}/c/{conversation}` form; after that transition the old parser returned `null`, classified the valid project page as `route=other`, and disabled the bridge's target-equality gates for page-owned `stream_status`, `/resume`, plural conversation snapshots, WebSocket target matching and composer identity.
- Exact b91 changes only that shared identity parser so both ordinary `/c/{conversation}` and the evidenced project `/g/{scope}/c/{conversation}` are recognized. It preserves b90 frontmost diagnostics for causal isolation and adds no retry, polling, timer, watchdog, Native status/resume synthesis, duplicate Send or response-store authority.
- Candidate / Build: `DEV-send-stream-0.1.0-b91` / `0.1.0 (91)`, permanently reserved.
- Exact b91 product commit: `cdab4e091683dc179753ed114c9ab5993a6c2d24`; exact product/config package source: `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`.
- Guarded staging `33746622538 / 100620460993` passed ancestry guard, exact replacement, exact two-product-file scope audit and Xcode Simulator compile. Earlier run `33746541830 / 100620201072` failed at an over-strict base guard before product application and emitted no product commit.
- Formal Push CI `33746881658 / 100621278207` and PR CI `33746886896 / 100621297087` both passed on exact package source `c5985f1e...`.
- Canonical Push Artifact `9890000591`; Artifact digest `sha256:6062b02f9f1332744816d01a58e13c1a8c82017ee50828051f014ef79b943350`; IPA `ChatGPTClient-0.1.0-b91-dev-send-stream.ipa`, independently recomputed SHA-256 `abbd27370665fb97dd1ee5edd239c0a5fa1ea0694cbb329a81c32ee86867c140`, matching its sidecar.
- Independent package inspection confirms Release `0.1.0 (91)`, Candidate b91, source `c5985f1e2e5d`, MinimumOSVersion 14.0, iPhone/iPad family `[1,2]`, `iphoneos`, Mach-O arm64.
- Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime Unverified / Stable-Frozen No.**
- Human Runtime gate is project-specific: after project canonicalization the bridge must continue reporting `route=conversation` and then prove or disprove the existing official page-owned continuation path. Non-project conversations are regression coverage, not the primary target.

## DEV-send-stream b90 frontmost-presentation package-ready override — 2026-09-03

- Candidate / Build: `DEV-send-stream-0.1.0-b90` / `0.1.0 (90)`, permanently reserved.
- Exact b90 product commit: `5e9d735ddb2f7a2c46dbc43de2525980c86a1c1e`; exact product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`.
- b90 changes only one Runtime A/B variable relative to b89: after explicit manual-Sync rearm, the existing executor `WKWebView` is brought to the front of its current Root host before loading the same target. Existing interactivity, focus rearm, route, page-owned continuation observation, protected Send and `ConversationRepository` ownership remain unchanged.
- Corrected guarded staging `33727956426 / 100561161422` passed exact patch, exact two-product-file scope audit and Xcode Simulator compile, then committed/pushed product `5e9d735...`. An earlier staging run `33727587238 / 100560009446` also passed patch/scope/Simulator but failed before remote product commit only because the Actions token could not modify a workflow file; it emitted no b90 product identity.
- Push CI `33728071476 / 100561518990` and PR CI `33728075476 / 100561530874` both passed on package source `99f1aa15...`.
- Canonical Push Artifact `9882770072`; ZIP `sha256:363c6fdbade5d476eacdee064eec26ed3480c0e7ba1da3b5dcf6b8537af46f6e`; IPA `ChatGPTClient-0.1.0-b90-dev-send-stream.ipa`, SHA `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`.
- Independent package inspection confirms Release `0.1.0 (90)`, Candidate b90, source `99f1aa15ce49`, MinimumOSVersion 14.0, iPhone/iPad family and Mach-O arm64; sidecar SHA matches.
- Evidence ladder: **Code written / guarded scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**
- Human Runtime gate: after one explicit Sync on a deliberately long externally active response, b90 must prove `manual_sync_frontmost_ab` with `visibleSiblingCountAbove=0`, then determine whether the official page itself begins matching `stream_status` / `/resume` / snapshot continuation without another Sync.

## DEV-send-stream b89 decisive interactivity-negative Runtime override — 2026-09-03

- Exact b89 identity remains `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)`, product `f39bc9387575028d431b85409780a2f3670b3259`, package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676`, Artifact `9881665748`, IPA SHA `c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`.
- Exact iPhone/iOS17 Runtime is decisive: after manual Sync/rearm, covered Web had `isUserInteractionEnabled=true`, non-empty/intersecting key-window bounds, then `nativeFirstResponder=true` and `documentHasFocus=true`, but emitted zero matching page-owned `stream_status`, `/resume`, SSE or external snapshot continuation.
- The same external response advanced only when manually re-Synced: authoritative live timeline `5 -> 28`, tools `4 -> 25`, reasoning `1 -> 3`. Therefore interactivity is rejected as a sufficient condition for automatic continuation. Manual authoritative Detail block projection remains Runtime Positive.
- b89 also recorded `subviewIndex=0` / `visibleSiblingCountAbove=1`; the next isolated causal A/B is genuine frontmost presentation/occlusion, not a route/status/resume/polling workaround.

## DEV-send-stream b89 package-ready override — 2026-09-03

Exact b89 `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)` is now the Human Runtime candidate. Product commit `f39bc9387575028d431b85409780a2f3670b3259`; exact package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676`; guarded staging `33722656297 / 100544857329` passed; Push `33725042383 / 100552047445` and PR `33725044367 / 100552051932` passed. Canonical Push Artifact `9881665748`, ZIP `sha256:2e383a6328f801dd754d6858c3b9a8b71be5d5765a9a612d497b18c91b73988f`, IPA `sha256:c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`; package independently verified as Release 0.1.0 (89), Candidate b89, source `fe45aeadf7ae`, iOS14, arm64. b89 tests only covered-Web interactivity plus automatic user-activation diagnostics; real-device continuation causality is Pending and Stable/Frozen remains No.
## DEV-send-stream b82 Runtime override — 2026-09-02

Exact b82 `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`, product/config source `c7a274786dfd175e8f476fc15c4964840e112a1d`, Artifact `9811406038`, IPA SHA `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2` is Runtime **Partial**. Automatic final acquisition now works without manual Sync, but the observed current-conversation WebSocket trigger arrived only when authoritative Detail already changed 8 -> 10 (+2 visible messages) and the user reports the remote user message plus assistant answer appeared only after the answer had fully generated. No earlier WebSocket message, `externalStreamingObserved`, external snapshot or Repository external live response was captured. Therefore b82 is a completion/update acquisition path, not live request-start acquisition. b83 is not allocated. The next gate is an already-open visible official-Web comparison before choosing any new discovery mechanism.

## DEV-send-stream b79 candidate override — 2026-09-01

Exact b79 `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)` is now the latest test candidate. Formal exact product/config source is `a3d307b05d70e95568672bc29b0c939b7f3b8141`. The guarded staging path `33488975445 / 99795672696` passed exact scope, `git diff --check` and Xcode 16.4 Simulator build before the validated product blobs were transplanted. Formal Push `33489654106 / 99797864816` and PR `33489658656 / 99797878467` both passed. Canonical Push Artifact `9793240789` has ZIP `sha256:2016508002ae7ff43d803c90fcbb92ba01c45906c885be6f6e50a1e43e1e87fc` and IPA `sha256:39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`; independent unpacking confirms Release 0.1.0 (79), Candidate b79, source marker `a3d307b05d70`, MinimumOSVersion 14.0 and Mach-O arm64.

- b79 gives reasoning/tool transitions one neutral 12-point separator instead of inheriting the preceding item paragraph style.
- After explicit manual Sync, a changed latest user turn may force one same-conversation covered-page reload/re-arm when no live response is active; there is still no timer/poll/watchdog or automatic Sync implementation.
- An external page-owned terminal without a real final body no longer promotes reasoning into final; the local protected-Send compatibility fallback remains limited to local responses. Stopped external reasoning is presented as `已停止思考`.
- b78 remains the Runtime evidence predecessor: external reasoning/tool observation is only page-snapshot granular and external progressive final still has no authorized source. b79 does not fake final streaming.
- Runtime/manual/real-device b79: **Pending / Unverified**. Stable/Frozen Send: **No**. b39-b79 are permanently reserved.

## DEV-send-stream b78 candidate override — 2026-09-01

Exact b78 `DEV-send-stream-0.1.0-b78` / `0.1.0 (78)` is the current real-device candidate. Clean product commit `180065e0faf947292a9f21b56c4ea366a5c322fe` changes only `ChatGPTClient/Conversation/ConversationFeature.swift` and `ChatGPTClient.xcodeproj/project.pbxproj`; workflow-only child `031b1a1f2c1d01900c2ab79ff14b1f2fb6c7e809` is the exact product/config source. Final tooling validation `33482721335 / 99775722851` passed exact scope, `git diff --check`, and Xcode 16.4 Simulator build. Formal Push CI `33482983693 / 99776545604` and PR CI `33482987997 / 99776557269` passed. Canonical Push Artifact `9790836559` has ZIP `sha256:7b5900a960ef680cce34642ca6cef232f201a260b182d6b640266e81982b081f` and IPA `sha256:726e3c09bcac4eb8a40a8ecb79b8abb0f145d89e41481083bc51941a7978620e`; independent package inspection confirms Release 0.1.0 (78), Candidate b78, source marker `031b1a1f2c1d`, MinimumOSVersion 14.0, Mach-O arm64.

- b77 device Runtime is partial/rejected: inline tool rows still lacked correct deterministic/prominent presentation; Native user messages could show raw inline Markdown and truncate because rendering and measurement diverged; a route-level list HTTP403 invalidated-and-cancelled the shared transient session, cancelling the selected Detail, whose cancellation path failed to terminalize the current operation and caused permanent coalescing/`正在读取会话…`.
- b78 uses one attributed representation for user rendering and measurement, explicit character wrapping and inline-only Markdown on supported OS versions; it records privacy-safe latest-user character count for integrity evidence.
- b78 retires a 401/403-invalidated transient session with `finishTasksAndInvalidate()` so already-running Detail tasks are not cancelled; any current Detail cancellation is terminalized instead of leaving a zombie operation. No retry/timer/watchdog/polling/fallback was added.
- b78 tool rows are a distinct medium-weight/label-color presentation whose icon/text/separator paragraph geometry is owned by the tool paragraph style instead of mixed reasoning/tool spacing. Runtime visual acceptance remains required.
- b77's structure-only DOM evidence remains negative for an earlier progressive final-body source; b78 does not promote DOM text/WebSocket bodies or fake final streaming.
- Runtime/manual/real-device b78: **Pending / Unverified**. Stable/Frozen Send: **No**. b39-b78 are permanently reserved.

## DEV-send-stream b76 candidate override — 2026-09-01

Exact b76 `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` is the current test candidate. Exact product/config source `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71` passed guarded exact-scope assembly plus Xcode 16.4 Simulator build, formal Push CI `33440101178 / 99645927061` and PR CI `33440098527 / 99645917529`. Canonical Push Artifact `9775920927` has ZIP `sha256:52f94ed7dbfbe311e37656fcce9a60bb5f8cc9c6b2af29434f7020d47729e944` and IPA `sha256:b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd`. Independent package inspection confirms Release 0.1.0 (76), Candidate b76, source marker `0da5a7577f2c`, MinimumOSVersion 14.0, arm64, iPhone+iPad family.

- Current visible official Web can receive matching page-owned `/resume` HTTP404 JSON and then follow the active response through its own already-issued `stream_status` + plural `/backend-api/conversations/{conversation}` reads.
- The plural rolling `messages[]` window exposes the required service-message family during `IS_STREAMING` and the finished final message after `COMPLETE`; raw message count is not a cursor.
- b76 observes only those page-owned responses, validates target identity, derives entries after the latest user, and atomically projects them into the existing `ConversationRepository` live-response owner. It adds no Native polling/cadence, Native resume/offset request, WebSocket body authority or second state store. Actual page-owned `/resume` HTTP200 SSE support remains strictly validated and retained when it occurs.
- Typography candidate is tool 30 / reasoning 21 / final 21. Runtime visual acceptance is pending.
- Runtime/manual/real-device b76: **Pending / Unverified**. Stable/Frozen Send: **No**. b39-b76 are permanently reserved.

## DEV-send-stream b75 Runtime override — 2026-09-01

Exact b75 `DEV-send-stream-0.1.0-b75`, source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, IPA SHA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d` is package-verified and permanently reserved. iPhone/iOS17 Runtime is **partial/rejected**, not pending.

- Positive: b75 no longer promotes a page-owned matching resume request into a Native live response before HTTP200 SSE validation; repeated HTTP404 JSON resume responses therefore no longer flash the prior false `回答失败`.
- Rejected: while another platform's response was still active, the covered production page repeatedly issued matching `/backend-api/f/conversation/resume` but every observed response was HTTP404 JSON. Native correctly created no live response, so no `正在思考` / reasoning / tools / incremental final appeared. Successful Detail Sync/Reload only exposed server-backed visible messages later.
- Typography: exact 26 tool / 18.2 reasoning / 18.2 final values are implemented but the user's latest screenshot rejects the visual result as too tight/low. These numbers are not an accepted UI baseline.
- Geometry: supplied diagnostics prove `cooperative_main_queue` cache-miss scheduling and `resident_cache` reuse are executing. This export does not reproduce the former ~10s worst case, so the interactive-Back acceptance gate remains open.
- Next gate: use the existing Web Rule Lab on the same `.default()` WebKit session to determine current page-owned `stream_status -> resume` ordering/status and whether another page-owned transport follows the first resume 404. Do not guess Native resume/offset/polling or WebSocket body authority. b76 is not allocated yet.

_Last updated: 2026-09-01 through accepted b67 production transport Runtime, positive b72 tested cross-conversation simultaneous-generation Runtime, exact b73 real-device defect evidence, and exact b74 Code/scope/Simulator/Push+PR CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active at the b74 human Runtime gate. Stable/Frozen Send remains No._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / source identity

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Current actual `main` last verified this cycle is `d323b9eed2dda75b9986fc06e14014d3e9b365fb`; final target-main synchronization is still required before merge.

Latest exact product Candidate is **`DEV-send-stream-0.1.0-b74` / `0.1.0 (74)`**:

- exact product/config source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`;
- final clean-reassembly `33420128454 / 99580192017` passed exact four-file replay/content equality, scope/invariant audit, `git diff --check` and Xcode 16.4 iOS Simulator compile;
- Push `33420408779 / 99581104920` and PR `33420412792 / 99581117817` — success on exact source;
- canonical Push Artifact `9768668727`; ZIP `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`;
- IPA `sha256:07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`;
- independently unpacked package `0.1.0 (74)` / Candidate b74 / source `50dd61b8b31c` / Release / minimum iOS14 / arm64 / iPhone+iPad family.

b73 real-device evidence localized long resident re-entry delay to repeated historical geometry rebuild, retained the need for more main tool-row spacing, and exposed the missing external active-response lifecycle. A current Web Rule Lab capture proved official Web uses page-owned matching `POST /backend-api/f/conversation/resume` `{conversation_id, offset}` -> HTTP200 SSE after `stream_status` when entering an externally active conversation. b74 observes only that page-owned matching resume stream, never constructs the request/offset or polls, and feeds it into the existing Repository response runtime. b74 also reuses derived b38 geometry only for unchanged resident presentation identity and increases main tool rhythm. Evidence ladder: **Code / exact scope / Simulator compile / Push+PR CI / Artifact / package verified / Runtime pending / Stable-Frozen No.** b39-b74 are permanently reserved.

## b65 accepted probe predecessor

Exact b65 focused iPhone/iOS17 Runtime passed the verified-composer protected-Send / reasoning-final / exact-parent GitHub tool-detail scope: real Send -> HTTP200 SSE -> terminal, reasoning `14/295`, final `71/2827`, exact-parent matches `10/10`, tool presentation/completion `10/10`, and readable nested `工具输入` / `工具输出`. Remaining spacing/slash escaping was non-blocking.

## Exact b66 production Runtime — failed bridge, Send reached service

b66 was the first TD-029 production existing-conversation slice. Exact identity:

- Candidate `DEV-send-stream-0.1.0-b66`, source `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`, tree `31ef29457273a44dd202a63a96560563154e8823`;
- Push `33337771534 / 99327694040`, PR `33337774136 / 99327701256` — both success;
- Push Artifact `9739572172`;
- ZIP `sha256:6c6d8e165ed070e88a27abafc57973dc847937826e40c552bf9f0d29bb91bb45`;
- IPA `sha256:7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`.

Exact iPhone/iOS17 export `ChatGPTClient-Diagnostics-20260830-220515.json` matched build66/source. Two generations reproduced:

`composer_ready x2 -> submit_result=submitted x2 -> one send_observed -> send_transport_error`

No `coveredExecutor.sendResponse` occurred and Native response characters stayed zero. The user independently verified that the official ChatGPT app already contained the assistant reply, so the protected Send reached the service; Native lost the same-response transport before receiving the HTTP Response object. This is **not** an SSE parser/Web-rule failure.

Source correlation isolated a production Swift->JS duplicate-submit race: b66 kept `pendingSend` until later `send_observed`, while multiple ready callbacks could schedule asynchronous `evaluateJavaScript(submit(...))` calls before page-local `activeSend` became true. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b66-runtime.md`.

## b67 minimal correction

b67 changes only the executor operation gate:

1. `CoveredWebSendExecutor.isBusy` is owned by existing `activeEvents != nil`, spanning request through terminal/failure.
2. `pendingSend` is consumed immediately before issuing the one JS `submit(...)` evaluation.
3. Later duplicate composer-ready callbacks cannot schedule the same pending operation again.
4. Clearing `pendingSend` does not open a second Send window because `activeEvents` remains active.

Exact Root delta is only `+2/-1`; Xcode/workflow changes only allocate b67 identity. No selector, Web rule, protected route, SSE grammar, Repository ownership, Web Rule Lab, retry, resend, polling, timer, watchdog, fallback or compatibility shim changed.

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- Separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription route remains blocked by account-safety policy.
- **TD-029 remains the production Send decision.** Native history/composer/reasoning/tool/final UI is the product surface; one process-resident covered official Web surface may perform browser challenge + exactly one page-owned protected Send.
- Covered Web is transport/challenge execution only, never conversation/message/response/list/draft authority.
- `ConversationRepository` remains sole native conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole auth/account authority; `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority. b70 treats exact probe HTTP403 as temporary failure that preserves the last verified identity, while list/detail 401/403 discards stale copied transient transport and never auto-replays the failed operation.
- Full existing-conversation mobile-Web rendering remains rejected by TD-025/TD-028.
- No challenge solving/replay, no second credential store, no duplicate Send to obtain a stream, no automatic Sync/poll loop.
- Sync/Reload never resend/regenerate.

## Web Send maintenance capability

`docs/project/WEB_SEND_ADAPTER.md` remains the durable authority for current evidenced official composer/protected-Send/SSE/reasoning/tool rules and the Web Rule Lab maintenance loop. b66 evidence does **not** change that adapter contract: the failure was local production orchestration, not an official Web rule change.

The in-app Web Rule Lab is now implemented in the current production branch: visible `WKWebView`, `.default()` store, explicit user execution, temporary script/result only, copy/share allowed, no persisted body/log body, never production response owner.

## Current implementation boundary / shortest remaining Phase 9 sequence

Current source contains the Repository-owned existing-conversation production bridge and Web Rule Lab. b67 transport Runtime is accepted; exact b70 daily-chat parity/auth-lifecycle Runtime is the immediate gate.

After that gate, the shortest remaining sequence is:

1. accept/fix existing-conversation production Send/stream;
2. new-chat first Send and pending->authoritative handoff only if actual timing requires it;
3. exact server Stop evidence and one response-scoped Stop implementation;
4. A/B hidden-response ownership + follow-tail/history intent;
5. Sync/Reload active-response safety + b38 geometry/round/time/Copy regression;
6. final daily-chat Runtime matrix, target-main synchronization and Stable/merge decision.

Final Composer hierarchy/dynamic input/attachment staging belongs future serialized `DEV-composer-parity`; current Work keeps only the validation trigger. Background completion and attachments remain subsequent Works after accepted text Send/Stream ownership.

## Current exact Runtime gate

Install exact b74 Artifact `9768668727` / IPA SHA `07c999fd...285da` on the primary iPhone/iOS17 device. Confirm Candidate/source marker, then verify: repeated re-entry into the previously slow long resident materially removes the ~1.4s geometry rebuild stall without breaking geometry/quick navigation; meaningful main tool rows have larger vertical rhythm; an externally initiated still-active response is adopted when entering the conversation via the official page-owned matching `/resume` SSE without duplicate Send or synthetic user bubble; terminal history reconciles once; one normal local Native Send still follows the b67 protected-Send HTTP200 SSE route; b72 A/B simultaneous-generation ownership remains correct; hidden thoughts stay absent. Export diagnostics for the Runtime run.

## Remaining Unknown / Unverified

Exact b74 resident-geometry/tool-spacing/external-adoption Runtime, new-chat authoritative identity timing, exact server Stop mechanism, broader cross-conversation/service concurrency beyond the exact b72 A/B test, connector-detail schemas beyond the evidenced GitHub mapping, Native-constructed first/exclusive resume, 5/15-minute background behavior, WebContent termination recovery, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.

## 2026-09-03 — b92/b93 page-owned continuation loop interruption

Exact b92 single-executor Runtime proves that a background lifecycle transition can stop the official page-owned `stream_status`/snapshot loop even without another executor. Exact b93 proves successful first-responder/document-focus reacquisition does not necessarily restart a stopped loop. The next isolated candidate is foreground official-page rebootstrap without Native Detail Sync; selection rebootstrap remains separate. Stable/Frozen Send remains No.

## 2026-09-03 b94 Runtime update

`DEV-send-stream` remains Active / Stable-Frozen No. Exact b94 foreground official-page rebootstrap is Runtime Positive as a restart mechanism, but the same long-running project-conversation run later recorded covered WKWebView WebContent-process termination. The termination cause is Unverified. Late authoritative Sync remained HTTP200 yet server-owned trailing response and `IS_STREAMING` persisted without a final assistant. Next work is evidence-driven WebContent/rebootstrap reliability and user recovery design; no speculative polling/retry/timer workaround is approved.
