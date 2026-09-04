# DEV-send-stream round 7 Runtime addendum

## b98 hard WebContent termination recovery — package-ready 2026-09-04

Exact identity:

- Candidate `DEV-send-stream-0.1.0-b98` / `0.1.0 (98)`, permanently reserved;
- product code `2edd55febe2005071722ddcb9989151b427165d8` — guarded product delta only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/RootViewController.swift`;
- exact package source `17c65a390f2724a55cd29d466e01eaab988dcbfe`;
- guarded staging `33886277311/101066715850` success including durable pre-write checkpoint, exact two-product-file scope, `git diff --check`, and Debug iphonesimulator compile;
- Push `33886537405/101067576599` success; PR `33886540813/101067587985` success;
- canonical Push Artifact `9942092070` / ZIP `sha256:f290b8a4d871016ce93a186b15c10e505a2a1d41b4adce4d19859d92fb65b3ae`;
- IPA `ChatGPTClient-0.1.0-b98-dev-send-stream.ipa` / `sha256:b1dc76dbe28e77ceac3468e8cfd3ca0ded41601bd02db6b228bd391a1d697b67`;
- independent unpacking: bundle `com.whitesharkssw.chatgptclient`, version/build `0.1.0 (98)`, Candidate b98, source `17c65a390f27`, Release, iOS14+, UIDeviceFamily `[1,2]`, Mach-O arm64.

Product boundary:

1. `webViewWebContentProcessDidTerminate` remains the only new recovery trigger. Silence, elapsed time, focus state, missing snapshots and ordinary navigation failures are not treated as disconnect evidence.
2. When `observingExternalResponse == true`, hard WebContent termination no longer calls `failCurrent`; external observation callbacks, current conversation identity and Repository live response remain intact.
3. If app state is active, the same executor performs exactly one existing full-page external-observation rebootstrap for that termination event. If inactive/background, no background network work is started; recovery is deferred to the existing foreground path.
4. Foreground recovery still runs b97's one authoritative `syncLatestMessages` reconcile plus one existing covered-Web page rebootstrap if the external response remains active.
5. Client-owned protected Send still treats WebContent termination as failure. No automatic resend/replay is authorized.
6. No timer, silence watchdog, retry loop, duplicate Send, regenerate, guessed `/resume`, challenge replay, Native background heartbeat or second response store.

b97 Human Runtime was explicitly **Not Executed** by user and remains permanently reserved. b98 supersedes only its test priority; b97's foreground authoritative Detail reconcile remains part of the b98 product behavior.

All later b98-named Artifacts caused only by docs/staging maintenance are **non-canonical for Human Runtime**. Canonical identity is only Push Artifact `9942092070` / IPA `sha256:b1dc76dbe28e77ceac3468e8cfd3ca0ded41601bd02db6b228bd391a1d697b67` from package source `17c65a390f2724a55cd29d466e01eaab988dcbfe`.

Evidence ladder: **b97 Runtime Not Executed / b98 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen Send No.**

**Next exact action:** install only canonical b98 IPA and collect one real hard WebContent-termination sample while a cross-platform external response is active. Verify `coveredExecutor.webProcess(state=terminated, mode=external_observation)` followed by `coveredExecutor.externalWebProcessRecovery(immediate_rebootstrap)` when foreground, or `deferred_to_foreground` followed by the existing foreground Detail reconcile + Web rebootstrap after return. The same Repository generation must survive and there must be no second Send. Do not allocate b99 before this Runtime gate.

## b98 hard WebContent termination recovery — checkpoint 2026-09-04

User explicitly chose not to run the b97 Human Runtime gate and asked to advance directly to b98. b97 remains a valid, permanently reserved package identity, but its Human Runtime result is **Not Executed**, not Positive or Negative.

Exact baseline before b98 product writes:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable.
- branch head before this checkpoint staging: `beba08deb0f0803f74417bd6026dd11ec8f4fa38`; base `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- parallel PR #35 / `DEV-official-sync-reload` remains draft research-only, head `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, with no product `ChatGPTClient/**` ownership or candidate-number conflict.
- b97 canonical product/package/Artifact remain `12fc1d1f5020d76d1892c25a0ced94323d5a0142` / `5e43c398b52a62de9f9a6e6546de7312ba5eb1df` / `9940228423`; never reuse or overwrite.
- `DEV-send-stream-0.1.0-b98` / Build98 is not yet allocated at this checkpoint and is the next unique candidate.

Evidence-backed defect and recovery boundary:

1. Current `CoveredWebSendExecutor.webViewWebContentProcessDidTerminate` is an explicit hard WebContent-death signal, but it currently calls `failCurrent("web_process_terminated")`; `failCurrent` clears `observingExternalResponse`/active events and Root then treats `.failed` as response failure and releases the executor.
2. For an **external/cross-platform observation only**, WebContent death is a transport interruption, not evidence that the server-side response failed. Existing Repository external live state must remain authoritative.
3. b94 Runtime already observed real covered-Web WebContent termination. b95 Runtime separately proved full-page existing-conversation rebootstrap can restart page-owned continuation. b96 Runtime proved one authoritative Detail request can materialize an already-finished final assistant; b97 preserves that foreground Detail reconcile.
4. For a **client-owned protected Send**, WebContent termination remains a failure. b98 must never automatically resend/replay a Send.

Intended minimal b98 product delta:

- allocate Build98 / Candidate `DEV-send-stream-0.1.0-b98`;
- only when `observingExternalResponse == true`, intercept `webViewWebContentProcessDidTerminate` before `failCurrent`;
- preserve external observation callbacks, current conversation identity and Repository live response;
- if the app is active, immediately issue exactly one existing full-page external-observation rebootstrap for that hard termination event;
- if the app is background/inactive, do not start background network work; defer to the existing foreground path, which already performs b97 authoritative Detail reconcile plus one external page rebootstrap;
- leave ordinary navigation failure semantics unchanged in b98; do not infer a disconnect from silence, elapsed time, focus state or missing snapshots;
- no timer/watchdog, retry loop, duplicate Send, resend/regenerate, guessed `/resume`, challenge replay, second response store or Native background heartbeat.

**Next exact action:** allocate `DEV-send-stream-0.1.0-b98`, apply only the two-file product delta above, run exact-scope checks + Debug Simulator compile, then bind formal b98 Push/PR package CI to the exact product head. Human Runtime should force/observe a real WebContent process termination while a cross-platform response is active and verify the same external live response survives and resumes, without a second Send.

## b97 foreground authoritative Detail reconcile — package-ready 2026-09-04

Exact identity:

- product code `12fc1d1f5020d76d1892c25a0ced94323d5a0142` — only `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/Conversation/NativeConversationContinuation.swift`, and `ChatGPTClient/RootViewController.swift` changed in the guarded product commit;
- Candidate `DEV-send-stream-0.1.0-b97` / `0.1.0 (97)`, permanently reserved;
- package source `5e43c398b52a62de9f9a6e6546de7312ba5eb1df`;
- staging `33881577700/101051252468` success including exact scope, `git diff --check`, and Debug iphonesimulator compile;
- Push `33881896437/101052287658` success; PR `33881905960/101052320038` success;
- canonical Push Artifact `9940228423` / ZIP `sha256:af05e9d0a522fb53c3e453bedcf9b49e44781158d7f7d8798ad1426b4c57b388`;
- IPA `ChatGPTClient-0.1.0-b97-dev-send-stream.ipa` / `sha256:49f8d9a8ef425409923bf904a3134265ddfa6d90597d72e04a1e976a5a8a90c7`;
- independent unpacking: bundle `com.whitesharkssw.chatgptclient`, version/build `0.1.0 (97)`, Candidate b97, source `5e43c398b52a`, iOS14+, UIDeviceFamily `[1,2]`, Mach-O arm64.

Product delta:

1. b96 10-second `DispatchWorkItem` Native continuation scheduling and account-reset cancellation hook are removed; authoritative Detail status remains diagnostic-only and existing Detail-to-live reconciliation is retained.
2. On foreground entry, a selected active external live response triggers exactly one existing authoritative `repository.syncLatestMessages(id:)` when no Detail operation is already running.
3. Existing covered-Web foreground page rebootstrap remains available in parallel for nonterminal live continuation.
4. If that one-shot Detail contains the final assistant, existing Repository `authoritative_assistant_materialized` reconciliation clears the stale external projection; Root then refreshes selected Detail presentation and releases an idle covered executor.
5. No background heartbeat, recurring polling, retry/watchdog/fallback, resend/regenerate, guessed `/resume`, challenge replay, or second response authority.

Pre-allocation PR workflow failures on heads before Build97 and the bot-pushed product-head `action_required` run are invalid/non-evidence because no formal b97 package job executed there. Any later docs/staging-maintenance PR Artifact is also non-canonical. Canonical Runtime identity is only Artifact `9940228423` / IPA `sha256:49f8d9a8ef425409923bf904a3134265ddfa6d90597d72e04a1e976a5a8a90c7`.

Evidence ladder: **b96 Runtime Negative for async-status automatic continuation/background-return convergence; manual authoritative Detail recovery Positive / b97 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen Send No.**

**Next exact action:** install only canonical b97 IPA; start a long external response, enter it while active, background/suspend ChatGPTClient until the other platform finishes, return to foreground without manual Sync/Reload, and export diagnostics after observing whether `foregroundExternalDetailReconcile.requested` performs one authoritative Detail request and automatically materializes the final assistant. Do not allocate b98 before this Runtime gate.

## b96 background-return Runtime — decisive rejection 2026-09-04

Latest Human Runtime source: `ChatGPTClient-Diagnostics-20260904-135118.json` from canonical `DEV-send-stream-0.1.0-b96`.

Exact observed target `sha256:0df178903e95`:

- Initial authoritative Conversation Detail returned HTTP200 with `visibleMessageCount=46` and `conversationAsyncStatus=missing`; `nativeContinuation.authoritativeDetail` recorded `asyncStatus=missing_or_unknown`.
- Covered official Web independently reported HTTP200 `IS_STREAMING` and advanced external reasoning/tool snapshots while foregrounded.
- The app entered background while the external response was still active. On foreground return, Root executed `foregroundExternalRebootstrap.requested` / covered page rebootstrap only; there was no automatic Native `detail.request`.
- After foreground return the selected authoritative Detail remained at 46 visible messages and the external live projection remained active/stale.
- User then manually invoked `同步最新消息` at 13:51:06Z. Its single authoritative Detail completed at 13:51:13Z with `visibleMessageCount=47`, still `conversationAsyncStatus=missing`, and zero trailing active timeline. Existing Repository reconciliation emitted `liveResponse.externalDetailReconciled` with reason `authoritative_assistant_materialized` and baseline `46 -> 47`, materializing the final assistant.

Runtime conclusions:

1. b96 automatic Native continuation is **Runtime Rejected as sufficient** for this real ordinary Detail shape because top-level `conversation_async_status` is absent. The 10-second `DispatchWorkItem` continuation never starts in this sample.
2. The server final answer itself is healthy/recoverable. The foreground defect is specifically the absence of one authoritative Detail reconciliation after background interruption.
3. One existing `syncLatestMessages` request is Runtime Positive as the recovery primitive. No resend, regenerate, guessed `/resume`, repeated polling, retry, watchdog or second response owner is required.
4. This result does **not** prove or promise completion while iOS keeps the app suspended in background. It justifies automatic convergence when the app returns to foreground. True-background completion/notification remains separate future work.

Evidence ladder for b96 is now: **Code written / Push+PR CI passed / Artifact produced / package verified / Human Runtime Negative for async-status-driven automatic continuation and background-return final convergence / manual authoritative Detail recovery Positive / Stable-Frozen Send No.** b96 remains permanently reserved.

### Historical b97 recovery plan — completed by package-ready section above

The exact interrupted-chain plan was: retire the b96 10-second Native scheduler, allocate b97, add one authoritative foreground Detail reconcile around existing covered-Web rebootstrap, run exact scope + Simulator + Push/PR CI, verify one canonical package, then update durable docs. That plan is now fully executed by the package-ready section above. Do not replay its staging steps or allocate b98 before b97 Human Runtime.

## b96 Native async-status continuation — historical package record

Current exact identity:

- Work: `DEV-send-stream`
- branch: `dev/send-stream-20260829`
- PR: #29 open / unmerged / mergeable
- base `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- exact b96 product code head: `9e50943de39dc304ab31904cbad8596d4ffddc14`
- exact b96 package source: `cd6268540e4f5a815829f26a713b10e8d1957239`
- Candidate / Build: `DEV-send-stream-0.1.0-b96` / `0.1.0 (96)`, permanently reserved
- prior b95 remains historical Runtime evidence only; do not reuse b95 or b96
- parallel PR #35 remains repository-isolated from the b96 product scope; same official bundle-ID research-package contamination warning is separate from this ChatGPTClient IPA

### Product behavior at b96 package time

b96 was the first Repository-owned Native cross-platform continuation candidate. It parsed top-level `conversation_async_status`, attempted a 10-second Detail scheduler only for exact `IS_STREAMING`, and retained existing Repository Detail-to-live reconciliation. The newer b96 Runtime section above supersedes that product hypothesis: ordinary authoritative Detail in the tested conversation omitted the field entirely, so the scheduler did not start and is removed in b97.

### Validation / Artifact

Earlier PR run `33856226503` on `9e50943...` was `action_required` with zero jobs; it remains invalid as CI evidence.

Canonical package-source correction `cd6268540e4f5a815829f26a713b10e8d1957239` produced real CI:

- Push run/job: `33877378585 / 101037475567` — **success**
- PR run/job: `33877383271 / 101037490825` — **success**
- toolchain: Xcode 16.4 / iphoneos18.5 / arm64
- canonical Push Artifact: `9938422716`
- Artifact ZIP digest and independently recomputed ZIP SHA-256: `5ea65cfb07c1c15dfc939646bbe7a2600825ba3ca1dab9ed100803037df3bd67`
- IPA: `ChatGPTClient-0.1.0-b96-dev-send-stream.ipa`
- IPA SHA-256: `a635903898324bdf0e59cf8712a2ebd5924def0da591d555fb25d2f62dabc361`
- sidecar SHA matches the independently recomputed IPA SHA
- independent unpacking confirms `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=96`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b96`, `DiagnosticsSourceCommit=cd6268540e4f`, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`, `iPhoneOS`, and Mach-O 64-bit arm64

Evidence ladder at package time: **Candidate allocated / Code written / exact Push build passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime was pending / Stable-Frozen Send No.** The newer Runtime section above supersedes that pending status.

## Official-App Probe stability conclusion / research pivot

Latest explicit Human Runtime: exact startup-safe Probe v0.8.1 package (`sha256:69d4257fa6a514724b54a5c19e17803349ba459fef37f76ce4cb4435d3efa724`) shows a white screen for roughly 10 seconds and then crashes. Earlier injected Probe packages also had intermittent mid-run crashes. Without a crash report, no individual private selector is the proven root cause; the durable result is that private response-callback swizzling is observably destabilizing enough that the v0.7/v0.8 callback/buffer ladder is retired.

The user also reports a separate useful Human Runtime fact: after an injected Probe crashes mid-run, reopening the official app and re-entering the same conversation shows the complete answer refreshed. This is **terminal re-entry recovery Runtime Positive**: completed server state can be recovered by fresh authoritative conversation entry without preserving the prior hooked callback chain or Web/process state. It does not alone prove the active polling start trigger.

Static inspection of the pristine official package supports the product pivot with exact strings/types: `conversation_async_status`, `KnownConversationAsyncStatus`, exact enum tokens `IS_STREAMING` / `COMPLETE`, `ConversationPollingManager.swift`, `poll(conversationID:...)`, `localPoll(conversationID:terminatingCondition:...)`, `Starting polling for conversation:`, `Conversation async status '...' is no longer streaming, stopping polling for conversation:`, `backend_streaming_completed`, `default_interval`, and `model_slug_intervals`. Probe v0.4-v0.7 Human Runtime independently showed authoritative `GET /backend-api/conversation/<id>` at roughly 9-12 second intervals.

Therefore no further injected official-App private callback package is required for this gate. The next evidence must come from ChatGPTClient Runtime itself.