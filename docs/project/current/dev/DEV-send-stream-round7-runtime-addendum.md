# DEV-send-stream round 7 Runtime addendum

## b96 background-return Runtime — decisive rejection / b97 recovery point 2026-09-04

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

### b97 intended minimal delta

Candidate `DEV-send-stream-0.1.0-b97` is not yet emitted and must be allocated before packaging. The evidence-backed product delta is:

- retire the b96 10-second Native `DispatchWorkItem` polling/scheduling path; retain only harmless authoritative Detail status observation and existing Repository Detail-to-live reconciliation;
- on `UIApplication.willEnterForegroundNotification`, when the selected conversation already owns an active external live response (`phase.isActive && promptText.isEmpty`), issue exactly one existing `repository.syncLatestMessages(id:)` if no Detail operation is already in flight;
- keep the existing covered Web foreground rebootstrap as the live transport recovery when the authoritative Detail still does not contain a final assistant;
- if the one-shot authoritative Detail already materializes the final assistant, existing Repository reconciliation removes the external live projection and Root releases the now-idle external executor;
- no background heartbeat, no recurring foreground polling, no retry/fallback, no second Send, no Native status/resume synthesis.

### Batch recovery point

Known baseline before b97 writes:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable.
- base `main` `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- feature head before this checkpoint write `3455486f56099d7b45c659e1974903f4c1bf6a87`.
- b96 canonical product/package/Artifact remain `9e50943de39dc304ab31904cbad8596d4ffddc14` / `cd6268540e4f5a815829f26a713b10e8d1957239` / `9938422716`; never reuse or overwrite.
- Xcode currently still says Build96 / Candidate b96; `BUILD_TEST_INDEX.md` has no b97 row. Parallel PR #35 remains research-only and does not touch `ChatGPTClient/**` or product Candidate numbering.

Planned coherent write batches:

A. **Confirmed by this commit:** record exact b96 Runtime rejection and b97 recovery direction in this checkpoint.
B. Allocate b97 in Xcode build/Candidate identity only after rechecking current head.
C. Product code: retire b96 timer scheduling; remove its account-reset cancellation call; add one-shot foreground Detail reconciliation around the existing Root foreground Web rebootstrap.
D. Point `.github/workflows/ios-foundation.yml` at exact b97 product head/Candidate and run formal Push+PR CI/package.
E. Verify Artifact/IPA identity, then update `BUILD_TEST_INDEX.md`, `PROJECT_STATE.md`, `PROJECT_PROFILE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, this checkpoint and PR #29 with b96 Runtime rejection + b97 exact evidence.

Recovery must not touch PR #35, b96 canonical Artifact identity, or allocate b98. If interrupted, re-read actual branch head and perform only the missing batch.

**Next exact action:** allocate `DEV-send-stream-0.1.0-b97` in Debug/Release Xcode settings, then apply only the three evidence-backed product edits above.

## b96 Native async-status continuation — package-ready 2026-09-04

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

### Product behavior

b96 is the first Repository-owned Native cross-platform continuation candidate:

1. authoritative `GET /backend-api/conversation/{id}` Detail parses exact top-level `conversation_async_status` tokens `IS_STREAMING` / `COMPLETE`; missing or unknown values are non-authoritative and do not start continuation;
2. exact `IS_STREAMING` may create/continue one external live response in the existing `ConversationRepository` authority and schedule the next existing Detail GET;
3. current interval is a 10-second **candidate approximation** backed by repeated official iOS Human Runtime Detail intervals (~9-12s) plus static official `default_interval` / `model_slug_intervals` evidence; it is not claimed as the exact compiled official default;
4. the first authoritative Detail that is not exact `IS_STREAMING` stops scheduling; exact `COMPLETE` is the evidenced expected terminal token;
5. account-scope reset cancels all Native continuations; a client-owned response with nonempty prompt remains authoritative and stops external Native continuation;
6. terminal authoritative Detail is stored first, then removal of the external live projection notifies the selected Detail VC, which applies the newly stored server Detail when current-node/messages changed;
7. no idle/global polling, guessed `/resume`, guessed offset, retry/watchdog/fallback, duplicate Send, WebSocket-body authority, challenge replay, or second response store;
8. protected Send remains TD-029 covered official-Web owned.

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

The user also reports a separate useful Runtime fact: after an injected Probe crashes mid-run, reopening the official app and re-entering the same conversation shows the complete answer refreshed. This is **terminal re-entry recovery Runtime Positive**: completed server state can be recovered by fresh authoritative conversation entry without preserving the prior hooked callback chain or Web/process state. It does not alone prove the active polling start trigger.

Static inspection of the pristine official package supports the product pivot with exact strings/types: `conversation_async_status`, `KnownConversationAsyncStatus`, exact enum tokens `IS_STREAMING` / `COMPLETE`, `ConversationPollingManager.swift`, `poll(conversationID:...)`, `localPoll(conversationID:terminatingCondition:...)`, `Starting polling for conversation:`, `Conversation async status '...' is no longer streaming, stopping polling for conversation:`, `backend_streaming_completed`, `default_interval`, and `model_slug_intervals`. Probe v0.4-v0.7 Human Runtime independently showed authoritative `GET /backend-api/conversation/<id>` at roughly 9-12 second intervals.

Therefore no further injected official-App private callback package is required for this gate. The next evidence must come from ChatGPTClient Runtime itself.