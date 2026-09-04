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
