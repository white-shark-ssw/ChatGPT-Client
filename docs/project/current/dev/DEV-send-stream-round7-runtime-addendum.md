# DEV-send-stream round 7 Runtime addendum

## b96 Native async-status continuation — recovered live state 2026-09-04

Resume identity guard after the interrupted/long-running write chain:

- Work: `DEV-send-stream`
- branch: `dev/send-stream-20260829`
- PR: #29 open / unmerged / mergeable
- base `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- recovered branch head: `9e50943de39dc304ab31904cbad8596d4ffddc14`
- prior accepted product remains b95 only for Runtime evidence: product `ac5e621aa69f5f27ef3167b4a951812be8b8e2c2`, package source `a10320e589acd551a8dc53f56aaf28a0a08f5b4a`, Artifact `9901461763`, IPA `sha256:2fd213a1dd692202b496adabd393c4130080607384e3d6c0f84cd3f975a8840d`
- `DEV-send-stream-0.1.0-b96` / `0.1.0 (96)` is now **allocated and permanently reserved**. Do not reuse b96.
- parallel PR #35 remains repository-isolated from the b96 product scope and has no exact changed-file overlap with `ChatGPTClient/**`, `ChatGPTClient.xcodeproj/**`, or this checkpoint; same official bundle-ID research-package contamination rule remains separate.

### Recovered write-chain facts

The interrupted chain did in fact advance beyond the older checkpoint wording:

1. `06e905977c51aaa46d7cb98509dda9813617853c` recorded the Probe crash pattern and pivot away from private official-App response callback hooks.
2. `c181def786868bed7b912ffcfb98bb17646f5cb3` allocated b96.
3. `a8ab29fd17ac5baed61e8994bcf26f74da45ccdb` wrote the first b96 product slice: parse top-level `conversation_async_status`, exact known tokens `IS_STREAMING` / `COMPLETE`, and Repository-owned Native continuation using the already-existing authoritative Conversation Detail GET.
4. `9e50943de39dc304ab31904cbad8596d4ffddc14` added the terminal-detail presentation reconcile so that when authoritative Detail removes the external live projection, the selected Native detail can immediately apply the newly stored terminal server Detail.
5. Xcode Debug/Release now both identify Build 96 / Candidate `DEV-send-stream-0.1.0-b96`.
6. `.github/workflows/ios-foundation.yml` is switched to the b96 package workflow, but its current product-source comment still names `a8ab29f...` and must be corrected to the latest product head before the canonical package run.

### b96 behavioral boundary

- `ConversationRepository` remains the sole Native conversation/content/response-lifecycle authority.
- Protected Send remains TD-029 covered official-Web owned.
- Native continuation starts only after an authoritative Detail itself reports exact `IS_STREAMING`.
- The refresh loop issues only the already-existing `GET /backend-api/conversation/{id}` path and projects through the same Repository resident/live-response state.
- The current b96 interval is a 10-second **candidate approximation** backed by repeated official iOS Human Runtime Detail intervals (~9-12s) plus static official `default_interval` / `model_slug_intervals` evidence. It is not claimed to be the exact compiled official default.
- Any authoritative Detail that is not exact `IS_STREAMING` stops scheduling; exact `COMPLETE` is the evidenced expected terminal token.
- account-scope reset cancels all Native continuations; a client-owned response remains authoritative and stops external Native continuation.
- no idle/global polling, guessed `/resume`, guessed offset, retry/watchdog/fallback, duplicate Send, WebSocket-body authority, challenge replay, or second response store.

### Current validation state

A PR workflow run exists for recovered head `9e50943...`: run `33856226503`, but GitHub concluded `action_required` with **zero jobs executed**. Therefore this is not CI evidence and emitted no Artifact.

Evidence ladder: **b96 Candidate allocated / product code written / terminal UI reconcile written / static-local compile not yet proven on exact recovered head / CI not run (action_required, zero jobs) / Artifact not produced / Human Runtime pending / Stable-Frozen Send No.**

Batch recovery point now: product batches are confirmed written through `9e50943...`; remaining deterministic work is (A) correct the b96 workflow product-source marker to the current product head and trigger a real Push CI from a direct repository write, (B) verify CI + Artifact/package identity, (C) update `BUILD_TEST_INDEX.md`, durable project state and PR #29, then (D) hand exact b96 IPA to the user for one real-device cross-platform active-to-terminal run. Recovery must not replay the old staging workflows or touch PR #35.

**Next exact action:** update only `.github/workflows/ios-foundation.yml` product-source marker from `a8ab29f...` to `9e50943...`; this is a real identity correction and should provide a direct push event for the canonical b96 CI/package path.

## Official-App Probe stability conclusion / research pivot

Latest explicit Human Runtime: exact startup-safe Probe v0.8.1 package (`sha256:69d4257fa6a514724b54a5c19e17803349ba459fef37f76ce4cb4435d3efa724`) shows a white screen for roughly 10 seconds and then crashes. Earlier injected Probe packages also had intermittent mid-run crashes. Without a crash report, no individual private selector is the proven root cause; the durable result is that private response-callback swizzling is observably destabilizing enough that the v0.7/v0.8 callback/buffer ladder is retired.

The user also reports a separate useful Runtime fact: after an injected Probe crashes mid-run, reopening the official app and re-entering the same conversation shows the complete answer refreshed. This is **terminal re-entry recovery Runtime Positive**: completed server state can be recovered by fresh authoritative conversation entry without preserving the prior hooked callback chain or Web/process state. It does not alone prove the active polling start trigger.

Static inspection of the pristine official package supports the product pivot with exact strings/types: `conversation_async_status`, `KnownConversationAsyncStatus`, exact enum tokens `IS_STREAMING` / `COMPLETE`, `ConversationPollingManager.swift`, `poll(conversationID:...)`, `localPoll(conversationID:terminatingCondition:...)`, `Starting polling for conversation:`, `Conversation async status '...' is no longer streaming, stopping polling for conversation:`, `backend_streaming_completed`, `default_interval`, and `model_slug_intervals`. Probe v0.4-v0.7 Human Runtime independently showed authoritative `GET /backend-api/conversation/<id>` at roughly 9-12 second intervals.

Therefore no further injected official-App private callback package is required for this gate. The next evidence must come from ChatGPTClient b96 Runtime itself.