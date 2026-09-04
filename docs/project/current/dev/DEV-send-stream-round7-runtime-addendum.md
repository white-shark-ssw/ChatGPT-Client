# DEV-send-stream round 7 Runtime addendum

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

Evidence ladder: **Candidate allocated / Code written / exact Push build passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen Send No.**

Batch recovery point: product and package work are complete through canonical package source `cd626854...`. The only remaining deterministic repository writes before handoff are durable evidence indexing (`BUILD_TEST_INDEX.md`, current project state/profile/module status) and PR #29 metadata. These are docs-only and must not change the canonical b96 product/package identity. After that, the next gate is Human Runtime on the exact IPA above.

**Next exact action:** record b96 package evidence in durable project docs and PR #29, then hand exact canonical IPA to the user for one cross-platform active-to-terminal real-device run.

## Official-App Probe stability conclusion / research pivot

Latest explicit Human Runtime: exact startup-safe Probe v0.8.1 package (`sha256:69d4257fa6a514724b54a5c19e17803349ba459fef37f76ce4cb4435d3efa724`) shows a white screen for roughly 10 seconds and then crashes. Earlier injected Probe packages also had intermittent mid-run crashes. Without a crash report, no individual private selector is the proven root cause; the durable result is that private response-callback swizzling is observably destabilizing enough that the v0.7/v0.8 callback/buffer ladder is retired.

The user also reports a separate useful Runtime fact: after an injected Probe crashes mid-run, reopening the official app and re-entering the same conversation shows the complete answer refreshed. This is **terminal re-entry recovery Runtime Positive**: completed server state can be recovered by fresh authoritative conversation entry without preserving the prior hooked callback chain or Web/process state. It does not alone prove the active polling start trigger.

Static inspection of the pristine official package supports the product pivot with exact strings/types: `conversation_async_status`, `KnownConversationAsyncStatus`, exact enum tokens `IS_STREAMING` / `COMPLETE`, `ConversationPollingManager.swift`, `poll(conversationID:...)`, `localPoll(conversationID:terminatingCondition:...)`, `Starting polling for conversation:`, `Conversation async status '...' is no longer streaming, stopping polling for conversation:`, `backend_streaming_completed`, `default_interval`, and `model_slug_intervals`. Probe v0.4-v0.7 Human Runtime independently showed authoritative `GET /backend-api/conversation/<id>` at roughly 9-12 second intervals.

Therefore no further injected official-App private callback package is required for this gate. The next evidence must come from ChatGPTClient b96 Runtime itself.