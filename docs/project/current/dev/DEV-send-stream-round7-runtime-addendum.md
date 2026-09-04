## b103 accepted-client hard-Web recovery Runtime Positive + b104 probe-removal allocation — 2026-09-05

Exact b103 Human Runtime evidence:

- Canonical Candidate `DEV-send-stream-0.1.0-b103` / Build103, source marker `e1cca160e9c4`; diagnostics `ChatGPTClient-Diagnostics-20260904-202930.json`, exact `sha256:99049f500c129571d33aa628720f7d23ce5cf6d183e887938cd7fa621a3bbc51`, 405144 bytes, iPhone / iOS17.0 / Release.
- The tested Native Send produced exactly one `coveredExecutor.requested`, one `submitResult`, one `sendObserved`, and one `sendResponse`. Send acceptance was explicit HTTP200 `text/event-stream` at `20:26:24Z`; there was no second protected Send anywhere in the export.
- The b103 probe fired at `20:28:23Z` while generation `1` remained active. In the same second Runtime recorded `webProcess terminated mode=client_send_or_idle`, `acceptedClientWebProcessRecovery state=handoff_requested policy=no_resend_same_generation`, executor release, and `acceptedClientRecovery.started trigger=web_process_terminated responseGeneration=1`.
- There was no `willResignActive`, `didEnterBackground`, `willEnterForeground`, or `didBecomeActive` event after the kill. Recovery therefore required no lifecycle nudge.
- The fresh observer returned HTTP200 `IS_STREAMING` at `20:28:26Z`, an external snapshot at `20:28:27Z` with the exact pre-kill continuity point `reasoningCharacters=884 / toolCount=21 / responseGeneration=1`, and `/resume` HTTP200 `text/event-stream` at `20:28:32Z`.
- Every post-kill event carrying a response generation used generation `1`. The same generation advanced to `reasoningCharacters=1768`, `toolCount=24`, `finalCharacters=7649`, then natural `terminal phase=completed` at `20:29:26Z`.
- Automatic authoritative reconcile immediately followed: one Detail HTTP200 changed authoritative visible messages `19 -> 21`; `liveResponse.reconciled responseGeneration=1` and `authoritativeReconcile.completed liveSnapshotCleared=true` occurred at `20:29:28Z`.
- Therefore b103 accepted-client hard-Web recovery is **Human Runtime Positive** for the tested foreground iPhone/iOS17 path: explicit accepted Send survives hard WebContent death, the same Repository generation automatically reattaches without resend or lifecycle nudge, live reasoning/tools/final continue, and terminal authoritative convergence clears the live projection.

b104 allocation / minimal next product action:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b104` / `0.1.0 (104)`. b104 is the first normal candidate after the deterministic b102/b103 kill experiment; Stable/Frozen remains No.
- Preserve the exact b103 accepted-client recovery logic in `RootViewController.swift` unchanged.
- Remove only the test instrumentation: delete `CoveredWebProcessKillProbe.swift`, remove its AppDelegate installer and Xcode file/build membership, then advance Build/Candidate 103 -> 104.
- Do not retain `_killWebContentProcessAndResetState`, the 120-second timer, swizzling or any probe-only behavior in b104. Do not add replacement timers, retries, polling, watchdogs, resend, challenge replay, guessed Native resume or a second response owner.
- Human Runtime for b104 should be an ordinary no-probe Send regression, not another forced-kill test. Hard-death recovery mechanism itself is already Runtime Positive on exact b103.

Resume/conflict guard before b104 product write:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 remains open/unmerged/mergeable at pre-stage head `964143043fa12e7902008bc6ef57a98e8c658393`; base `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, research-only, with no product/Candidate conflict.
- `BUILD_TEST_INDEX.md` contains no b104 before this allocation.

Batch recovery point:

- batch A in this staging run: record this b103 Runtime result + b104 allocation in checkpoint/index and push it before product changes;
- batch B: remove only the b103 kill probe, advance Build/Candidate to b104, run exact-scope audit + Simulator compile, then commit/push product;
- after batch B, formal packaging must bind `ios-foundation.yml` to the exact b104 product commit, then Push/PR CI + canonical Artifact/package verification must complete before Human Runtime;
- recovery must not alter b103 canonical product/package/Artifact, PR #35, accepted-client recovery logic, TD-029 one-Send ownership, or earlier reserved Candidate identities.

**Next exact action:** complete batch B only: remove the diagnostic kill probe and advance Build/Candidate to b104 without touching accepted-client recovery; exact-scope audit + Simulator compile before product commit.

## b103 accepted-client hard-Web recovery — package ready 2026-09-05

Exact package evidence:

- Candidate `DEV-send-stream-0.1.0-b103` / `0.1.0 (103)`, permanently reserved. Exact product `d514e9a5bde01bf3243d81016bf8cbda533fd5bf`; canonical package source `e1cca160e9c466ab98a2aeffc038e94f58335cab`. b103 is a Runtime recovery test candidate, not Stable/Frozen.
- Corrected guarded staging `33913972639 / 101156743875` passed b102 Runtime/checkpoint allocation, exact three-product-file scope audit and Debug Simulator compile, then committed product `d514e9a5bde01bf3243d81016bf8cbda533fd5bf`. Earlier staging `33913633892 / 101155651591` stopped before product write while matching the docs allocation marker and emitted no b103 product commit.
- Formal Push `33914210593 / 101157497020` and PR `33914214638 / 101157509705` both passed on exact package source `e1cca160e9c466ab98a2aeffc038e94f58335cab`.
- Canonical Push Artifact `9952548424`; downloaded Artifact ZIP independently recomputed `sha256:27fc23f1cb48d585ab3ffc0b181ec0dffafc42ccb3069fd72cbf5a0ba647f77a`, matching GitHub's Artifact digest.
- Canonical IPA `ChatGPTClient-0.1.0-b103-dev-send-stream.ipa`; independently recomputed `sha256:f41c81a89552027fb4c42152eb3864c1732494465230ffd4787c6bba56d746c3`, matching the emitted sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (103)`, Candidate b103, source marker `e1cca160e9c4`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, `iPhoneOS`, Mach-O 64-bit arm64. Binary strings include the exact b103 Candidate, `coveredExecutor.acceptedClientWebProcessRecovery`, `acceptedClientRecovery.started`, and `_killWebContentProcessAndResetState`.

Behavior / evidence boundary:

- b102 Human Runtime `sha256:6d2fde277427d3bbad6549946855c68b8df7e0433389b2d5c9e7d98212a3a6a6` proved the original client Send had exactly one protected Send and explicit HTTP200 SSE acceptance before deterministic WebContent death; server generation survived, and the same turn later resumed through existing covered observation/Detail with no second Send and reached terminal/final convergence.
- b103 therefore changes hard WebContent death only after exact client SSE acceptance: preserve the same prompt-owned Repository generation, emit `acceptedClientWebProcessInterrupted` instead of `.failed`, release the dead executor, and attach one fresh covered observer to the same generation immediately while active or on next foreground when inactive. It never resends/replays/regenerates the prompt.
- The one-shot 120-second kill remains Candidate-gated deterministic Human Runtime instrumentation only. It is not a production timeout/watchdog and must be removed/disabled before a later normal/Stable candidate.

Evidence ladder: **Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / b102 causal Runtime Positive / b103 recovery Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b103. Fresh-launch, open an existing conversation, start one deliberately >2-minute Native Send, keep the app foreground, and do not touch Sync/Reload/Stop or background the app. At ~120s expect `killProbe firing -> webProcess terminated -> acceptedClientWebProcessRecovery state=handoff_requested -> acceptedClientRecovery.started` with the same `responseGeneration`, followed by covered `IS_STREAMING`/snapshot/resume/live continuation and final terminal reconcile. There must be exactly one protected Send and no lifecycle nudge.

## b102 Human Runtime decisive + b103 accepted-client hard-Web recovery allocation — 2026-09-05

Exact b102 Human Runtime evidence:

- Canonical Candidate `DEV-send-stream-0.1.0-b102` / Build102, source marker `78bd3d2f3e45`; diagnostics `ChatGPTClient-Diagnostics-20260904-193801.json`, exact `sha256:6d2fde277427d3bbad6549946855c68b8df7e0433389b2d5c9e7d98212a3a6a6`, 460465 bytes, iPhone / iOS17.0 / Release.
- One Native protected Send started at `19:33:48Z`; exact counts are one `coveredExecutor.requested`, one `submitResult`, one `sendObserved`, one `sendResponse`. `sendResponse` was HTTP200 `text/event-stream`, so server acceptance is explicit before transport death.
- The deterministic probe fired at `19:35:54Z` while the response was still active: `coveredExecutor.webProcess state=terminated mode=client_send_or_idle`. Legacy behavior then marked the client-owned generation failed and released the executor.
- The server-side turn survived. After the user briefly backgrounded/foregrounded, existing b100 foreground discovery issued one authoritative Detail HTTP200, changed visible messages `17 -> 18`, observed `latestUserChanged=true` / `rearmDiscoveredRemoteTurn=true`, and created an external authoritative projection.
- A fresh covered observer then returned HTTP200 `IS_STREAMING`; `/resume` returned HTTP200 `text/event-stream`; reasoning/tool/final events continued to terminal with final 6079 chars, reasoning 2924 chars and 31 tools. Automatic terminal reconcile then changed authoritative visible messages `18 -> 19` and cleared the live projection.
- There was no second protected Send. Therefore hard WebContent death after explicit Send acceptance is now **Runtime proven to be transport loss, not server-turn failure** for this scenario. The remaining product defect is that current b102 requires a lifecycle nudge because it converts the client-owned generation to failed/released at the kill.

b103 allocation / minimal product direction:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b103` / `0.1.0 (103)`. b103 is a recovery test candidate, not Stable/Frozen.
- Only exact client Send HTTP200 `text/event-stream` acceptance may arm automatic hard-Web recovery. WebContent death before explicit acceptance remains failure and must never auto-resend/replay/regenerate.
- On accepted-client `webViewWebContentProcessDidTerminate`, preserve the existing Repository generation and prompt-owned live response; emit a transport-interruption event instead of `.failed`, release the dead executor, and when active create one fresh covered observer for the same conversation using the same Repository generation. No second Send occurs.
- If the app is inactive when the hard death callback arrives, do no background network work. The live client-owned snapshot remains active with no executor; on the next foreground lifecycle, one fresh covered observer is attached to that same generation.
- Reuse the already-proven external observation parsing path for `IS_STREAMING`, snapshot, `/resume`, reasoning/tool/final/terminal. `ConversationRepository` remains the sole response/content authority and the existing terminal authoritative Detail reconcile remains final authority.
- b103 may reuse the already-proven one-shot 120-second kill probe, Candidate-gated to exact b103, only to deterministically validate this new recovery path. It remains diagnostic instrumentation, not product timeout/watchdog policy, and must be removed/disabled before any later normal/Stable candidate.
- No timer beyond that explicit test probe, no polling, retry loop, heartbeat, duplicate Send, challenge replay, guessed resume, second response store or Native protected-Send implementation is authorized.

Resume/conflict guard before product write:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-allocation head `8081203d587d04e058d91e7985c45f36a361a99d`; base `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, with no `ChatGPTClient/**` product overlap or Candidate ownership conflict.
- `BUILD_TEST_INDEX.md` has no b103 identity before this allocation.

**Next exact action:** apply only Build/Candidate 103, exact b103 Candidate gate for the already-proven kill probe, and accepted-client hard-Web transport handoff in `RootViewController.swift`; run exact-scope audit + Simulator compile before formal packaging.

## b102 deterministic client-owned WebContent-death probe — package-ready 2026-09-05

Exact evidence:

- Candidate `DEV-send-stream-0.1.0-b102` / `0.1.0 (102)`, permanently reserved. This is a **diagnostic-only** candidate requested to make hard covered-Web death reproducible; it does not add client-owned response recovery.
- Exact product head `670310b4e8b15176f721291f4f96e46feadec46a`; canonical package source `78bd3d2f3e45c8e0061865d3133b92a274139110`. Relative to the verified pre-allocation head, product scope is exactly Xcode Build/Candidate + `AppDelegate.swift` installer + new `Protocol/CoveredWebProcessKillProbe.swift`; the package-source child changes only `ios-foundation.yml`.
- Probe behavior: only exact b102 installs a runtime interception of `WKWebView.evaluateJavaScript`; the first script containing the fixed `window.__coveredWebSendExecutor.submit(` marker arms one 120-second main-queue diagnostic action without logging prompt/script content. At fire it invokes `_killWebContentProcessAndResetState` only when that exact `WKWebView` responds to the selector. No Send/retry/resume API exists in the probe.
- Push `33910845721 / 101146639944` and PR `33910858535 / 101146674919` passed guard + unsigned TrollStore build. Canonical Push Artifact `9951331101`, ZIP `sha256:2da6bb66d0c5eba55d93463881e0ff5d0d55a9d7844f068d024e5cee31dff24a`. Same-source PR Artifact `9951329921` is CI corroboration only.
- Canonical IPA `ChatGPTClient-0.1.0-b102-dev-send-stream.ipa`, independently recomputed `sha256:53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`, matching sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (102)`, Candidate b102, source marker `78bd3d2f3e45`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64. Binary strings contain the exact b102 Candidate, `coveredExecutor.killProbe` and `_killWebContentProcessAndResetState`.

Evidence ladder: **Code written / exact diagnostic scope audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b102. Fresh-launch the app, choose an existing conversation, start exactly one deliberately >2-minute Native `测试发送…` response and keep the app foreground. Do not press Sync/Reload/Stop and do not send a second prompt. Expect `coveredExecutor.killProbe` `installed -> armed -> firing` at ~120s, followed by `coveredExecutor.webProcess state=terminated mode=client_send_or_idle` while the response is still active. Current product behavior is expected to mark that client-owned live response failed and release the executor; let the server-side generation finish, then export diagnostics. If the response finishes before `firing`, the run does not qualify and must be repeated with a longer response. Do not interpret this diagnostic timer as production timeout/retry policy.

## b102 deterministic client-owned WebContent-death diagnostic allocation — 2026-09-05

User explicitly pivots the next `DEV-send-stream` gate from waiting for another naturally occurring b101 `-1005` sample to a deterministic client-owned WebContent-process-death test. The 120-second termination is **diagnostic instrumentation only**, not production recovery policy.

Resume / conflict guard:

- Work `DEV-send-stream` remains selected; branch `dev/send-stream-20260829`; PR #29 is open / unmerged / mergeable.
- Verified pre-allocation branch head `18c1ff13c2ae3c3191414afc89e86ff73b5b78ac`; current target `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Canonical b101 remains permanently reserved: product `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`, package `da103452236e31e070eae68b9e7979a832662fc1`, Artifact `9948780963`, IPA `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`. Its exact `-1005` recovery branch remains Unexercised; b102 does not replace or rewrite that evidence.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft/open at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, research-only, with no `ChatGPTClient/**` product overlap or Candidate-number ownership conflict.
- Repository search found no existing `DEV-send-stream-0.1.0-b102`; `DEV-send-stream-0.1.0-b102` / `0.1.0 (102)` is now allocated and permanently reserved.

Evidence-backed diagnostic boundary:

1. Do **not** add client-owned recovery behavior yet. Current b98 rule intentionally still treats client-owned protected-Send WebContent death as failure; b102 exists to force that exact Runtime path before deciding the smallest recovery change.
2. Add one Candidate-gated Runtime probe that observes only the existing `CoveredWebSendExecutor` JavaScript submit invocation. The probe must not inspect/log prompt text; it only recognizes the fixed bridge call prefix.
3. On the first matching covered protected-Send submit for one `WKWebView`, schedule exactly one main-queue action 120 seconds later. This explicit timer exists only because the user requested a deterministic forced-death test; it is not a timeout, watchdog, keepalive, retry or production lifecycle signal.
4. At fire time, call the WebKit SPI selector `_killWebContentProcessAndResetState` on that exact `WKWebView` only when `responds(to:)` is true. Use Objective-C runtime dispatch so the app does not hard-link a private symbol. WebKit upstream exposes `_killWebContentProcess` / `_killWebContentProcessAndResetState` specifically as Web-process termination SPI/test surface.
5. Expected diagnostic chain if the answer is still active: `coveredExecutor.killProbe state=firing` -> `coveredExecutor.webProcess state=terminated mode=client_send_or_idle` -> existing client-owned `.failed(web_process_terminated)` / executor release. No prompt resend/regenerate, no duplicate protected Send, no Native guessed resume, no polling and no second response authority.
6. If the response naturally finishes before 120 seconds, a later forced idle Web kill does **not** qualify the client-owned active-response gate; repeat with a deliberately >2-minute response. Keep the app foreground for the deterministic first test so iOS suspension does not postpone the diagnostic timer.
7. b102 Runtime evidence decides the next product action. If server generation survives while Native marks the response failed, the next candidate may test no-resend conversion to page-owned observation / authoritative Detail reconciliation using only already-evidenced mechanisms. Do not implement that recovery in the same diagnostic candidate.

Intended b102 source scope:

- `ChatGPTClient.xcodeproj/project.pbxproj` — Build102 / Candidate b102 and compile membership for one diagnostic source;
- `ChatGPTClient/AppDelegate.swift` — install the probe once at launch; exact b102 Candidate guard remains inside the probe;
- `ChatGPTClient/Protocol/CoveredWebProcessKillProbe.swift` — one-shot submit-observer + 120-second WebContent termination instrumentation.

Batch recovery point:

- confirmed complete: task routing; AGENTS/START_HERE and required Send/background plans re-read; branch/PR/base/b101 identity verified; PR #35 conflict checked; b102 uniqueness checked; user explicitly authorized the 120-second forced-Web test; WebKit SPI existence verified from current upstream source/header;
- pending batch A: create the new diagnostic Swift file, wire AppDelegate + Xcode Build102 membership, verify exact three-product-file scope and Swift/Xcode compile;
- pending batch B: formal Push/PR CI and canonical b102 Artifact/IPA identity verification;
- pending batch C: update BUILD_TEST_INDEX / PROJECT_STATE / MODULE_STATUS / relevant rule/decision docs and PR #29 metadata, then hand exact IPA to Human Runtime;
- recovery must not touch PR #35, canonical b101 product/package/Artifact, earlier reserved Candidates, protected-Send/challenge rules, or `ConversationRepository` response ownership.

**Next exact action:** implement only the three-file b102 deterministic kill probe described above; compile before packaging. Human Runtime must launch b102 fresh, start exactly one deliberately >2-minute Native `测试发送…` response, keep the app foreground, do not press Sync/Reload/Stop, wait for the automatic 120-second WebContent kill, then let the server-side answer finish and export diagnostics.

## b101 Human Runtime — healthy long-suspension path; b100 rearm/reconcile gates Positive — 2026-09-05

Exact tested evidence:

- Candidate `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)`; source marker `da103452236e`; Release / iPhone / iOS17.0; diagnostics `ChatGPTClient-Diagnostics-20260904-185039.json`, `sha256:f7209546f3f2d1dd8ad08458b0dea8adbef522af100deb2f5de90cbe26180b9d`, 95964 bytes / 182 events.
- This sample contains zero exact `NSURLErrorDomain -1005`, zero `detail.transportRecovery` / `list.transportRecovery`, zero `authTransport.retired` / `authTransport.recoveryReady`, zero `coveredExecutor.webProcess`, and zero client-owned protected-Send evidence (`sendObserved`). Therefore the b101 bounded `-1005` recovery branch is **Unexercised / Unverified**, hard WebContent-process death is **Unexercised**, and this is **not** a client-owned accepted-Send death-recovery test.
- Dormant unfinished-turn discovery/rearm is Runtime Positive. App backgrounded `18:27:51Z -> 18:30:30Z` (~2m39s). Automatic `foregroundConversationDiscovery` issued one authoritative Detail, HTTP200 changed visible messages `13 -> 14`, and completed with `latestUserChanged=true` / `rearmDiscoveredRemoteTurn=true`. Covered observation then rearmed; a new user WebSocket opened, `externalStreamStatusResponse` returned HTTP200 `IS_STREAMING`, and Repository started `source=external_page_owned`; the next snapshot reached reasoning 112 chars / service messages 6 / tools 2.
- Known-active external foreground reconcile is Runtime Positive. While that external response was active, app backgrounded `18:30:44Z -> 18:32:40Z` (~1m56s). Foreground automatically emitted `foregroundExternalDetailReconcile.requested` plus Web page rebootstrap. Authoritative Detail HTTP200 changed `14 -> 15`, emitted `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)`, cleared the live projection and released the executor.
- WebSocket transport interruption was real but distinct from WebContent death: on both `18:30:30Z` and `18:32:40Z` the user socket emitted `error` + `close(1006)`. The first was followed by a new socket `created/open/message` and live continuation; the second coincided with Native authoritative final convergence. No `webViewWebContentProcessDidTerminate` callback occurred.
- Long dormant foreground discovery remained healthy after `18:32:48Z -> 18:50:23Z` (~17m35s): one automatic Detail returned HTTP200 and materialized `15 -> 17` (`addedVisibleMessageCount=2`, `latestUserChanged=true`, `rearmDiscoveredRemoteTurn=false`). This is normal-path long-suspension regression evidence only; because no `-1005` occurred, it does not accept the new b101 recovery branch.

Runtime classification:

- b101 bounded Native `-1005` recovery: **Unexercised / Unverified**;
- b100 unfinished remote-turn discovery + one covered rearm: **Runtime Positive**;
- b100 known-active external foreground Detail reconcile: **Runtime Positive**;
- b100 long dormant foreground discovery: **Runtime Positive again**, including ~17m35s in this sample;
- WebSocket `1006` interruption tolerance for the tested external flow: **Runtime Positive** via observer rearm / authoritative Detail convergence;
- b98 hard WebContent-process recovery: **Unexercised / Unverified**;
- client-owned accepted protected-Send recovery after Web/WebContent death: **Unexercised / future gate**;
- overall `DEV-send-stream`: **Runtime Partial / Stable-Frozen No**.

**Next exact action:** keep canonical b101 unchanged; no b102/product change is justified by this sample. Continue b101 only until an exact `-1005` sample exercises its bounded recovery branch, or explicitly pivot to the separately scoped client-owned accepted-Send transport-death gate. Never treat WebSocket code1006 as proof of `WKWebView` WebContent-process death and never auto-resend a protected Send.

## b101 Native read transport renewal — package-ready 2026-09-05

Exact evidence:

- Candidate `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)`, permanently reserved.
- Triggering Runtime evidence remains exact b100 diagnostics `ChatGPTClient-Diagnostics-20260904-174041.json`, `sha256:515c60b59d969ee1f33d76fec097d6163450058c5ef3fa9ccd551b2439f03818`: after ~12m37s background, foreground discovery fired but authoritative Detail, later Detail, two conversation-list GETs and manual Sync all failed `NSURLErrorDomain -1005` while covered WebSocket independently reopened; no hard WebContent-process termination signal occurred.
- Exact b101 product commit `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; exact product delta is only `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Product behavior: only idempotent Native conversation-list / Conversation Detail GETs gain bounded recovery. On the first exact `NSURLErrorNetworkConnectionLost (-1005)`, retire the matching cached `AuthTransientSession`, reacquire one fresh transient session from the existing default-WebKit-auth path, re-check account/operation freshness, then retry that same GET once. A second failure terminates normally. Protected Web Send, covered Web observation, b100 foreground discovery, Repository content authority and client-owned response ownership are unchanged.
- Initial staging workflow run `33903494492` had zero jobs due workflow parse failure and is invalid evidence; it emitted no product change. Corrected staging `33903822115 / 101123907440` passed exact two-product-file scope, `git diff --check` and Debug iphonesimulator compile, then committed product `54a9fa52...`.
- Exact canonical package source `da103452236e31e070eae68b9e7979a832662fc1` changes only `ios-foundation.yml` after the product commit. Formal Push `33904070096 / 101124706091` and same-source PR `33904076581 / 101124726725` both passed.
- Canonical Push Artifact `9948780963`, Artifact ZIP `sha256:df5e95d273c0a4f977b47ac7b64eb654daea99e3b797c3c54924b820fd165e64`. Same-source PR Artifact `9948785659` is CI corroboration only and is not the Human Runtime package authority.
- Canonical IPA `ChatGPTClient-0.1.0-b101-dev-send-stream.ipa`, independently recomputed `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`, matching the package sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (101)`, Candidate b101, source marker `da103452236e`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, iPhoneOS and Mach-O 64-bit arm64.

Evidence ladder: **Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

Batch recovery state:

- confirmed complete: b100 `-1005` Runtime evidence classified; b101 allocated; exact two-file product committed; corrected staging passed; canonical package source fixed; Push+PR package CI passed; canonical Artifact/IPA identity independently verified;
- this recorder batch owns only checkpoint + durable project docs. Product code, b101 package source/Artifact/IPA, PR #35 and prior candidates must not be changed by recovery;
- after this docs batch, only PR #29 metadata update and Human Runtime handoff remain.

**Next exact action:** use only canonical b101 IPA. Reproduce the long-suspension scenario that produced `-1005`; on foreground do not press Sync/Reload first. If the first authoritative Detail reports `-1005`, diagnostics must show exactly one `detail.transportRecovery` request, retirement of the current transient session, one fresh auth transport acquisition, one `transportAttempt=2`, then HTTP200/convergence or a normal terminal failure with no third attempt. Also verify conversation-list refresh remains functional after the same recovery. If the first GET is already healthy, the b101 recovery branch is Unexercised rather than accepted. Export diagnostics.

## b100 Human Runtime — Native transient transport failure / b101 allocation 2026-09-05

Exact tested evidence:

- Candidate `DEV-send-stream-0.1.0-b100` / `0.1.0 (100)`; Release / iPhone / iOS17.0; source marker `e88a50ad9c20`; diagnostics `ChatGPTClient-Diagnostics-20260904-174041.json`, `sha256:515c60b59d969ee1f33d76fec097d6163450058c5ef3fa9ccd551b2439f03818`, 77816 bytes / 146 events.
- Before the long background interval, authoritative Detail was healthy at HTTP200 / 10 visible messages. The app entered background at `17:26:58Z` and returned at `17:39:35Z` after about 12m37s.
- b100 foreground discovery itself fired correctly: `foregroundConversationDiscovery.requested` immediately started authoritative Detail generation 7. That GET failed after ~5s with exact `NSURLErrorDomain -1005` (`network connection lost`).
- This is **not evidence of hard WKWebView WebContent-process death**. The diagnostic contains zero `coveredExecutor.webProcess` and zero `coveredExecutor.externalWebProcessRecovery` events. On the same foreground return, covered Web created a user WebSocket at `17:39:35Z`, then opened and received a message at `17:39:36Z`.
- The failure persisted specifically across Native reads: foreground Detail generation 8 again failed `-1005`; two manual conversation-list GETs failed `-1005`; manual Sync Detail generation 9 also failed `-1005`. Meanwhile the covered Web user socket still emitted messages and later created/opened again at `17:40:13-14Z`.
- Current source explains the persistence. `ConversationRepository` caches one `AuthTransientSession` and `withTransientSession` reuses it indefinitely while account scope matches. The current transport is retired only for HTTP401/403; `normalizedTransportError` leaves `NSURLErrorNetworkConnectionLost` unchanged. Therefore a stale/broken ephemeral Native `URLSession` after suspension can be reused by Detail, list and manual Sync even while WebKit networking has independently recovered.

Runtime classification:

- b100 dormant foreground-discovery trigger: **still Runtime Positive as a lifecycle mechanism**;
- Native authoritative read transport after long suspension in this sample: **Runtime Negative** — repeated `NSURLErrorDomain -1005` across Detail/list/manual Sync with no successful Native HTTP recovery before export;
- b98 hard WebContent termination recovery: **still Unexercised / Unverified** because the hard termination callback did not occur;
- overall `DEV-send-stream`: **Runtime Partial / Stable-Frozen No**.

### b101 allocation / batch recovery point

- Work `DEV-send-stream` remains selected; branch `dev/send-stream-20260829`; PR #29 is open/unmerged/mergeable.
- Verified pre-allocation branch head `ff204bdd5874862e5b250f39bc0762bc1b94056f`; `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft/open at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`; it is research-only and has no `ChatGPTClient/**` product overlap.
- `BUILD_TEST_INDEX.md` has no b101 identity. `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)` is now permanently allocated/reserved.

Evidence-backed minimum b101 product boundary:

1. Change only the Native read transport owner. Protected Web Send, covered-Web observation/rebootstrap, Repository content/response authority and b100 foreground-discovery conditions remain unchanged.
2. On the **first exact** `NSURLErrorDomain / NSURLErrorNetworkConnectionLost (-1005)` from an idempotent Native Conversation Detail or conversation-list GET, retire only the matching cached `AuthTransientSession` with existing in-flight tasks allowed to finish, then obtain one fresh transient session through the existing `withTransientSession` / default-WebKit-auth path.
3. Retry that same read operation **at most once** with the fresh transport. The retry stays under the same Detail/list operation generation and must re-check account scope and operation freshness before issuing the replacement GET.
4. A second `-1005`, any other network error, auth failure, HTTP failure, supersession or scope change terminates normally. No timer, cadence, retry loop, reachability watcher, background heartbeat, Send replay, guessed resume or second state authority.
5. Add privacy-safe diagnostics proving transport retirement, one fresh-session acquisition/recovery attempt, and whether that bounded attempt succeeds or fails.

Intended product scope:

- `ChatGPTClient.xcodeproj/project.pbxproj` — Build101 / Candidate b101 only;
- `ChatGPTClient/Conversation/ConversationFeature.swift` — exact `-1005` stale-transient retirement plus one bounded read recovery for list/Detail only.

Batch state:

- confirmed complete: new b100 diagnostics analyzed; Web-process-death hypothesis rejected for this sample; exact Native `-1005` persistence tied to current `AuthTransientSession` reuse; branch/base/PR29 verified; PR35 product-overlap checked; b101 uniqueness checked and allocated by this checkpoint;
- pending: apply exact two-product-file b101 delta; run exact-scope + `git diff --check` + Debug iphonesimulator compile; bind formal Push/PR package CI to the exact product head; verify canonical Artifact/IPA identity; update durable project docs and PR #29 metadata;
- do not touch PR #35, protected-Send/challenge transport, Web process-recovery semantics, b100 canonical Artifact/IPA identity, or any earlier reserved candidate identity.

**Next exact action:** implement only the two-file b101 bounded Native-read transport renewal above and validate it before packaging.

## b100 Human Runtime — dormant foreground discovery Positive 2026-09-05

Exact tested evidence:

- Candidate `DEV-send-stream-0.1.0-b100` / `0.1.0 (100)`; Release / iPhone / iOS17.0; source marker `e88a50ad9c20`; diagnostics `ChatGPTClient-Diagnostics-20260904-171109.json`, `sha256:f0f3619ea61f30f9bcbaadbb577f3a99839a032dfcd95503e22b4a7bdb984696`, 72063 bytes / 127 events.
- The selected conversation was complete/idle at authoritative visible message count `8`. App entered background at `16:45:36Z` with no active external live response and returned at `17:05:07Z` after 1171s (~19m31s).
- On foreground, without any preceding `conversation.latestSync.requested`, b100 emitted `foregroundConversationDiscovery.requested` and exactly one automatic authoritative Detail operation (`operationGeneration=2`). HTTP200 Detail changed visible messages `8 -> 10`; `latestSync.end` recorded `addedVisibleMessageCount=2`.
- `foregroundConversationDiscovery.completed` reported `latestUserChanged=true`, `activeExternalAfterSync=false`, `liveResponseActive=false`, `rearmDiscoveredRemoteTurn=false`, `visibleMessageCount=10`. This is the expected completed-remote-turn branch: the assistant was already authoritative, so no covered observer rearm was required.
- A second background interval lasted 327s (~5m27s). Foreground again issued exactly one dormant discovery and converged `10 -> 10` with `latestUserChanged=false` / `rearmDiscoveredRemoteTurn=false`. A later explicit manual Sync at `17:10:59Z` also remained `10 -> 10`, so it was not required for convergence.
- The user WebSocket produced `error` + `close` code `1006` on the long foreground return, then a new socket was `created/open` within seconds. No `coveredExecutor.webProcess` / `externalWebProcessRecovery` event occurred. This proves dormant authoritative discovery works despite a stale/broken WebSocket, but does not exercise hard WKWebView WebContent-process termination recovery.
- One iOS memory warning occurred on the long foreground return; the protected resident was retained and the app continued normally with no crash/relaunch in this diagnostic. This is sample-local stability evidence only.
- This run contains zero `liveResponse.event` / `liveResponse.presentationApplied`, so b99 backlog-coalescing stress is still Unexercised here. It also does not exercise `rearmDiscoveredRemoteTurn=true` for an unfinished newly discovered remote turn, nor the exact-b100 known-active `foregroundExternalDetailReconcile` branch.

Runtime classification:

- b100 primary dormant cross-platform foreground discovery: **Runtime Positive**, including ~19m31s background and automatic authoritative materialization `8 -> 10` with no manual Sync/Reload;
- no-change foreground discovery: **Runtime Positive / one-shot no-op**;
- unfinished remote-turn rearm: **Unexercised / Unverified**;
- exact-b100 known-active external reconcile regression: **Unexercised in this sample**;
- b99 backlog coalescing: **Unexercised / Unverified in this sample**;
- b98 hard WebContent termination recovery: **Unexercised / Unverified**;
- overall `DEV-send-stream`: **Runtime Partial / Stable-Frozen No**.

**Next exact action:** no product change or b101 is justified by this sample. Keep canonical b100. If further qualification is desired, return foreground while a newly created remote turn is still unfinished and verify `rearmDiscoveredRemoteTurn=true` + one covered rearm; separately regression-check exact-b100 known-active `foregroundExternalDetailReconcile`. Do not add polling/timers/heartbeat/retries.

## b100 foreground dormant discovery — package-ready 2026-09-05

- Candidate `DEV-send-stream-0.1.0-b100` / `0.1.0 (100)`, permanently reserved.
- Product `70c7dc052865ef80ca7bdec083d7621c1a297eab`; exact delta: Xcode Build/Candidate + `ChatGPTClient/RootViewController.swift` only. Canonical package source `e88a50ad9c2098449b43fb0fce2c441a50cd20ac`.
- Initial staging `33894741044` was YAML parse failure with zero jobs/product writes and is invalid evidence. Corrected staging `33895020559/101095508915` passed exact scope, `git diff --check`, Simulator and product commit.
- Push `33895244146/101096229135` and PR `33895249810/101096247432` passed. Canonical Push Artifact `9945483725`, ZIP `sha256:babb23c845c4da971b488b4860c043fe8471adf830688920149df254cee70fd6`; IPA `sha256:5629deedca665b7a5cfa7e36b4996b7b1e4b7a160ca5cb35a465abfbd97fbc69`.
- Package inspection: `com.whitesharkssw.chatgptclient`, `0.1.0 (100)`, Candidate b100, source `e88a50ad9c20`, iOS14+, `[1,2]`, arm64.
- b99 Runtime `sha256:4a0d3925a4abf6ef24dc6743f9efb63a4dffcd049f3e41eb7a547f2b1d33d271`: known-active ~7m32s automatic Detail `5->6` Positive; later no-active-snapshot ~12m54s remote changes required manual Sync `6->8`, so dormant discovery Negative. b99 backlog coalescing Inconclusive in this sample; hard WebContent death Unverified.
- b100 adds exactly one foreground authoritative discovery without an active-snapshot precondition. It may rearm one existing covered observer only for an unfinished newly discovered remote turn. No polling/timer/retry/watchdog/background heartbeat/resend/second authority.

Evidence ladder: **b99 Runtime Partial / b100 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Human Runtime pending / Stable-Frozen No.**

**Next exact action:** test canonical b100. Keep a selected completed conversation idle, background app, create a new remote turn elsewhere, then foreground without Sync/Reload. Expect `foregroundConversationDiscovery.requested` + exactly one Detail; complete response should materialize, unfinished remote turn should set `rearmDiscoveredRemoteTurn=true` and rearm once. Regression-check known-active `foregroundExternalDetailReconcile` too.

## b99 Human Runtime — dormant foreground discovery gap / b100 allocation 2026-09-05

Exact tested b99 evidence:

- Candidate `DEV-send-stream-0.1.0-b99` / `0.1.0 (99)`, canonical package source `313c4c3bf2ac0dc729d4793198fe462ada5a14eb`, canonical IPA `sha256:68b7f99eac8fd1d3ab14c6085abd4a084f2b4759dc630f94044017c9a4aecf02`.
- Human Runtime diagnostics `ChatGPTClient-Diagnostics-20260904-161157.json`, `sha256:4a0d3925a4abf6ef24dc6743f9efb63a4dffcd049f3e41eb7a547f2b1d33d271`, 74674 bytes / 149 events / Release / iPhone / iOS17.0.
- First external response was acquired at `15:50:36Z`; app backgrounded at `15:50:38Z` and returned at `15:58:10Z` after 452s (~7m32s). Because an active external live snapshot still existed, b97-style foreground authoritative reconciliation ran automatically; Detail changed visible messages `5 -> 6`, emitted `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)`, cleared the live response and released the covered executor. This path is Runtime Positive.
- App backgrounded again at `15:58:25Z`, now with **no active live response and no covered executor**, and returned at `16:11:19Z` after 774s (~12m54s). No `foregroundExternalDetailReconcile` and no covered rebootstrap occurred because current `applicationWillEnterForeground` requires a pre-existing active external snapshot.
- Manual `同步最新消息` at `16:11:43Z` immediately found authoritative server change: visible messages `6 -> 8` (`addedVisibleMessageCount=2`). This proves the server state advanced while the client had no active receive owner, and the existing authoritative Detail request is sufficient to discover it once invoked.
- This sample contains zero `coveredExecutor.webProcess` / `externalWebProcessRecovery` events. b98 hard WebContent termination recovery remains Unexercised / Unverified.
- This sample contains only one `liveResponse.event` and one `liveResponse.presentationApplied`; therefore the b99 backlog-coalescing performance fix is not meaningfully exercised by this run. No freeze/crash was observed, but coalescing is not accepted from this sample.

Runtime classification:

- known-active external foreground final convergence: **Runtime Positive**, including ~7m32s background;
- b99 live-presentation backlog coalescing: **Unexercised / Inconclusive** in this sample;
- remote changes that begin/occur while the selected conversation has no active external snapshot/executor: **Runtime Negative for automatic foreground discovery**; manual one-shot Detail recovery Positive;
- b98 hard WebContent termination recovery: **Unexercised / Unverified**;
- overall b99: **Runtime Partial / Stable-Frozen No**.

Exact source explanation:

- `RootViewController.applicationWillEnterForeground` currently starts with `guard let conversationID = repository.selectedConversationID, let snapshot = repository.liveResponse(for: conversationID), snapshot.phase.isActive, snapshot.promptText.isEmpty else { return }`.
- Therefore a completed/released external response leaves no foreground discovery trigger for later cross-platform server changes.
- `ConversationDetailViewController` manual Sync already proves the normal authoritative `ConversationRepository.syncLatestMessages` request can recover those changes, and its existing Root callback can rearm covered observation when needed.

b100 allocation / batch recovery point:

- Work `DEV-send-stream` remains selected; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable.
- Verified pre-allocation branch head `6d8d99166d4e36c1b27ca84c842df3be84de21a1`; `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Product files remain exact b99 package product relative to `313c4c3...`; intervening branch commits are workflow/docs only.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft/open at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`; its seven changed paths remain research/workflow/checkpoint only, with zero `ChatGPTClient/**` or product Xcode overlap.
- `DEV-send-stream-0.1.0-b100` / `0.1.0 (100)` is the next unique product candidate and is now permanently allocated/reserved.

Evidence-backed b100 product boundary:

1. Keep client-owned active protected Send behavior unchanged: an active local response is not auto-Synced/replayed on foreground.
2. For a selected conversation with no client-owned active response, foreground entry may issue exactly one existing authoritative `ConversationRepository.syncLatestMessages` when no Detail operation is already in flight, even if no external live snapshot currently exists.
3. Preserve the existing b97 path and diagnostics when an external live snapshot already exists.
4. For the new no-snapshot discovery path, compare the authoritative latest-user identity before/after the one-shot Detail. If the server exposes a newly added latest user whose visible tail still ends in `.user`, or authoritative Detail itself recreates an active external live projection, reuse the existing covered observer with one force page reload so an in-progress remote response can continue. If the final assistant is already materialized, Detail alone is sufficient and no observer is required.
5. Do not poll. Do not add a timer, cadence, retry, watchdog, background heartbeat, guessed `/resume`, WebSocket-body authority, duplicate Send, challenge replay, response cache or second response owner.
6. Preserve b99 UIKit coalescing, b98 hard WebContent recovery, b97 authoritative reconcile, TD-029 protected Send ownership and Sync/Reload semantics.

Intended product scope:

- `ChatGPTClient.xcodeproj/project.pbxproj` — Build100 / Candidate b100 only;
- `ChatGPTClient/RootViewController.swift` — foreground one-shot authoritative discovery/rearm only.

Batch state:

- confirmed complete: b99 diagnostics analyzed; exact failure mechanism tied to source; branch/base/PR #29 verified; PR #35 overlap checked; b100 candidate uniqueness checked; this checkpoint written;
- pending: apply exact two-product-file delta; exact-scope + `git diff --check` + Debug iphonesimulator compile; bind formal b100 Push/PR package CI to exact product head; verify canonical Artifact/IPA identity; update durable project docs and PR #29 metadata;
- do not touch PR #35, protected-Send transport/challenge logic, Repository response authority, b99 canonical Artifact, or b98/b99 reserved candidate identities.

**Next exact action:** apply only the two-file b100 foreground-discovery delta above and validate it before packaging.

## b99 live-presentation coalescing — package-ready 2026-09-04

- Candidate `DEV-send-stream-0.1.0-b99` / `0.1.0 (99)`, permanently reserved.
- Exact product `ec05c284010cb0f2de066bd1cfc3968e07730779`; product commit changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Exact canonical package source `313c4c3bf2ac0dc729d4793198fe462ada5a14eb`.
- Initial staging workflow run `33890559324` parsed invalidly and created zero jobs/product changes; it is invalid evidence. Corrected guarded staging `33890678564/101081289220` passed baseline guard, exact two-product-file scope, `git diff --check`, and Debug iphonesimulator compile.
- Formal Push `33890809275/101081720750` and PR `33890812345/101081730258` both passed.
- Canonical Push Artifact `9943798885`; Artifact ZIP `sha256:303bad6e93b8dfdc48ecd77559ed42d6a03058e5d6db676dcd24c65c537df8b5`.
- Canonical IPA `ChatGPTClient-0.1.0-b99-dev-send-stream.ipa`, `sha256:68b7f99eac8fd1d3ab14c6085abd4a084f2b4759dc630f94044017c9a4aecf02`.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (99)`, Candidate b99, source `313c4c3bf2ac`, iOS14+, UIDeviceFamily `[1,2]`, `iphoneos`, Mach-O arm64.

b99 changes only the selected-conversation UIKit consumer: Repository still accepts/logs every live event, while `ConversationDetailViewController.liveResponseDidChange` schedules at most one pending main-queue presentation application and rebuilds from the latest Repository snapshot when that block runs. No timer/cadence, retry, watchdog, polling, Send replay, transport mutation or second response store is added. b98 WebContent recovery and b97 foreground Detail reconcile remain unchanged.

Evidence ladder: **b98 Runtime Partial / stability rejected; b99 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen Send No.**

**Next exact action:** use only canonical b99 IPA. Start one client-owned response, background for several minutes while it remains active, then foreground. Many `liveResponse.event` records may arrive, but `liveResponse.presentationApplied` must be materially coalesced and the app must remain responsive through terminal/final completion. Verify no second Send and no response-state loss. A separate real `webViewWebContentProcessDidTerminate` sample is still required before accepting b98 hard-process recovery.

# DEV-send-stream round 7 Runtime addendum

## b98 Human Runtime — foreground backlog freeze/crash 2026-09-04

Exact tested identity:

- Candidate `DEV-send-stream-0.1.0-b98` / `0.1.0 (98)`, permanently reserved;
- product `2edd55febe2005071722ddcb9989151b427165d8`;
- canonical package source `17c65a390f2724a55cd29d466e01eaab988dcbfe`;
- canonical Artifact `9942092070`;
- canonical IPA `sha256:b1dc76dbe28e77ceac3468e8cfd3ca0ded41601bd02db6b228bd391a1d697b67`;
- Human Runtime diagnostics `ChatGPTClient-Diagnostics-20260904-152557.json`, `sha256:e0a0bd2c42168d0c3f8a6dd681bbad1bb571d4061b0f2958131cae5f8e059105`, 269552 bytes / 548 events / Candidate b98 / source `17c65a390f27` / Release / iPhone / iOS17.0.

Observed Runtime facts:

1. The b98 hard WebContent-death branch was **not exercised**: the entire diagnostic contains zero `coveredExecutor.webProcess` events and therefore no `coveredExecutor.externalWebProcessRecovery` event. This sample cannot accept or reject that exact hard-termination recovery behavior.
2. The b97 foreground authoritative Detail reconcile carried inside b98 is **Runtime Positive** for the external/cross-platform response. After the app spent roughly 7m51s in background, foreground return automatically issued one authoritative Detail request; visible messages advanced `1 -> 2`, `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)` cleared the external live projection, and the executor was released without manual Sync/Reload.
3. A later client-owned protected Send was accepted once through the covered official Web path (`submitResult=submitted`, `sendResponse` HTTP200 `text/event-stream`) and was still active when the app backgrounded at `15:20:35Z`.
4. After roughly 5m04s background, foreground at `15:25:39Z` delivered a large buffered same-response event backlog. From `15:25:39Z` through `15:25:49Z`, 170 Repository `liveResponse.event` callbacks and 169 `liveResponse.presentationApplied` callbacks were recorded. The peak second was 39 live events plus 39 full live-presentation applications. The burst included 119 `final_delta`, 24 `reasoning_delta`, 18 tool transitions, and the final text reached 4750 characters.
5. Current source explains the UI pressure: every accepted Repository event calls `responseRuntime.onChange`, Root immediately calls `ConversationDetailViewController.liveResponseDidChange`, and that method synchronously rebuilds the full live projection/metrics, `tableView.reloadData()`, and `tableView.layoutIfNeeded()` for every event.
6. The user observed the app freeze and crash. The last pre-crash live event is at `15:25:49Z`; a fresh `launch.start` appears at `15:25:52Z`, followed by Candidate b98 ready at `15:25:55Z`. There is no graceful lifecycle shutdown record between them. This proves an abnormal process exit/relaunch in the tested window, but the exact OS termination class (watchdog, memory pressure, uncaught exception, other) remains **Unverified** without an iOS crash report.

Runtime classification:

- b98 hard WebContent termination recovery: **Unexercised / Unverified** in this sample;
- b97-style foreground authoritative final convergence inside b98: **Runtime Positive**;
- client-owned covered-Web response buffering/survival across ~5m background: **Runtime Positive transport signal**;
- foreground backlog presentation stability: **Runtime Negative — freeze/crash**;
- overall b98: **Runtime Partial / stability rejected; Stable-Frozen No**.

## b99 live-presentation main-queue coalescing — allocation / batch recovery point 2026-09-04

Exact resume guard before product writes:

- Work `DEV-send-stream`;
- branch `dev/send-stream-20260829`;
- PR #29 open / unmerged / mergeable;
- verified branch head before this checkpoint write `97bb33032a44edab4fbe65e2c4c7be75a1eac175`;
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- parallel PR #35 / `DEV-official-sync-reload` remains draft/open at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`; its seven changed paths are research/workflow/checkpoint only, with zero `ChatGPTClient/**` or product-Xcode overlap;
- b98 identity above remains permanently reserved and must not be reused;
- `DEV-send-stream-0.1.0-b99` / Build99 is the next unique product candidate and is allocated by this checkpoint.

Evidence-backed minimum product delta:

1. Keep every live response event flowing into the sole `ConversationRepository` owner exactly as today. Do not coalesce, drop, synthesize or reorder Repository state transitions.
2. Coalesce only the expensive selected-conversation UIKit presentation consumer in `ConversationDetailViewController` by scheduling at most one `DispatchQueue.main.async` live-presentation application for the current main-queue drain. Multiple live-state changes before that block executes collapse into one rebuild using the latest Repository snapshot.
3. The scheduled block must re-check displayed/selected conversation identity. If the live projection disappeared and authoritative Detail replaced it, preserve the existing `apply(detail)` path.
4. Normal sparse foreground streaming still presents on the next main turn. No timer, delay interval, retry, watchdog, polling, response cache or second response authority is introduced.
5. b98 WebContent termination logic, b97 foreground Detail reconcile, TD-029 protected Send ownership, one-Send invariant, Sync/Reload behavior and all transport parsing remain unchanged.

Intended product scope:

- `ChatGPTClient.xcodeproj/project.pbxproj` — Build99 / Candidate b99 only;
- `ChatGPTClient/Conversation/ConversationFeature.swift` — UI-only main-queue live-presentation coalescing only.

Batch recovery state:

- confirmed complete: b98 diagnostics analyzed; branch/base/PR #29 verified; PR #35 conflict check verified; b99 candidate uniqueness checked; this checkpoint written;
- pending: historical pre-package note; superseded by the b99 package-ready section at the top of this checkpoint.
- do not touch PR #35, official research package identities, b98 canonical package, protected-Send transport rules, or Repository response authority during recovery.

**Next exact action:** use the package-ready b99 Human Runtime gate at the top of this checkpoint.
