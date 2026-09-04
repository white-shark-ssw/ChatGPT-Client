# DEV-send-stream round 7 Runtime addendum

## Probe crash pattern / official-App callback research retired — 2026-09-04

Latest explicit Human Runtime: exact startup-safe Probe v0.8.1 package (`sha256:69d4257fa6a514724b54a5c19e17803349ba459fef37f76ce4cb4435d3efa724`) no longer dies at the earliest launch boundary, but shows a white screen for roughly 10 seconds and then crashes. Therefore v0.8.1 is also **Runtime Negative as a usable official-App research package**. Do not ask the user to repeat protocol reproduction with v0.8.1.

The user additionally reports that earlier injected Probe packages also had an intermittent mid-run crash problem, including the last otherwise usable Probe package. Exact per-version crash attribution is not reconstructed from a crash report, so do not claim one selector as the proven cause. The durable conclusion is narrower: private response-callback swizzling in the injected official process is now observably destabilizing enough that continuing the v0.7/v0.8 callback/buffer hook ladder is not an acceptable research method.

A separate Runtime observation is strongly useful for product architecture: after such a mid-run crash, reopening the official app and re-entering the conversation showed the **complete assistant answer already refreshed**. This proves that terminal recovery does not require preserving the previously hooked callback chain or the pre-crash Web/process state; a fresh authoritative conversation re-entry can materialize the completed server state. It does not by itself prove the exact active polling start trigger.

Re-analysis of the exact pristine official package (`ChatGPT_Decrypted.zip` `sha256:bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`) identifies the relevant static evidence inside `Payload/ChatGPT.app/Frameworks/ChatGPT.framework/ChatGPT` (`sha256:80e19700e42f7181bd2e307f1dd007a12b3e77feaec6d2a4326f1419e490bc9f`):

- `conversation_async_status`
- `KnownConversationAsyncStatus` adjacent to exact enum tokens `IS_STREAMING` and `COMPLETE`
- `ConversationPollingManager.swift`, `poll(conversationID:...)`, `localPoll(conversationID:terminatingCondition:...)`
- `Starting polling for conversation:`
- `Conversation async status '...' is no longer streaming, stopping polling for conversation:`
- `backend_streaming_completed`
- polling-state metrics `ios.conversation_polling.is_streaming_message`, `chat_has_active_async_tasks`, `is_waiting_for_server_streaming`
- configuration keys `default_interval` and `model_slug_intervals`

This static contract aligns with repeated Human Runtime from Probe v0.4-v0.7 showing authoritative `GET /backend-api/conversation/<id>` at about 9-12 second intervals. The product already owns that exact Detail GET in `ConversationRepository` and already parses `mapping/current_node`, but currently ignores top-level `conversation_async_status`.

**Research direction change:** stop adding private response callback hooks to the official app. The next implementation gate moves into ChatGPTClient itself: keep `ConversationRepository` as the sole Native content/response owner, parse only the exact evidenced top-level `conversation_async_status` values, and permit Native continuation refresh only after an authoritative Detail response itself reports `IS_STREAMING`; stop when the authoritative Detail reports `COMPLETE` / no longer streaming. Do not globally poll idle conversations and do not create a second response store. The exact refresh interval must remain tied to the repeated official Runtime evidence/config contract rather than an unrelated fast timer.

Evidence ladder: **official Native Detail polling Runtime Positive / terminal re-entry recovery Runtime Positive / private injected callback research method Runtime Negative for stability / exact async-status enum + polling stop contract Static Positive / ChatGPTClient product still exact b95 / b96 not yet allocated at this checkpoint / Stable-Frozen Send No.**

**Next exact action:** run product-change conflict/candidate guard, then implement the smallest Repository-owned async-status continuation slice in ChatGPTClient and validate it as one coherent product Candidate instead of producing another injected official-App Probe.

## Probe v0.8 launch-crash Runtime / v0.8.1 startup-safe batch package — 2026-09-04

Exact user Human Runtime result for the first Probe v0.8 batch package is **launch crash immediately after entering the app**. Therefore the exact v0.8 IPA `sha256:d9072fad0e8bb020e8b9681d7d4e29e3bba473bb357af5197b5c90d259422970` is Runtime Negative as a usable research package and produces no protocol/response evidence. Do not ask the user to retry that exact IPA.

Source differential identifies a strong, not yet crash-log-proven, startup-risk cause in `ProbeBatchHooks.m`: `constructor(200)` executed the batch far earlier than the previously stable v0.7 constructor, performed Foundation/NSURLSessionTask class work at that ultra-early stage, globally scanned task classes, and installed a second independent `resume` swizzle chain. Because no device crash report was captured, classify that exact causal attribution as **Inferred**, not proven.

The replacement batch preserves the one-human-run diagnostic goal but removes those startup risks. `ProbeBatchHooksSafe.m` uses normal constructor priority, does not install any second `resume` hook, and targets only the exact Runtime-evidenced `__NSCFLocalDataTask` class. It installs the same four v0.6-evidenced private selectors only when their exact type encodings match. Each private callback now checks `conversation_detail` first; non-target tasks are forwarded immediately before any dispatch-data scan. The old `ProbeBatchHooks.m` remains in source as evidence but is no longer compiled.

Exact startup-safe research source/package identity:

- source head: `1fd92f19ad090ad86b55a3cec371864e18c86f58`
- dedicated research run/job: `33851524572 / 100955187606` — success
- regular PR CI on the same head: `33851528476` — success
- canonical research Artifact: `9928515526`
- Artifact digest / downloaded ZIP SHA-256: `3b3cf2d30c8701dc6c3601aede78d5a03d190140d13c65e66211b7f8289d93ca`
- Probe dylib SHA-256: `6328c5b5897059890a7094caba7c8df96f2a6162b260d8fb7f1b6543a565bd2e`
- pristine official source ZIP SHA-256: `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`
- repacked startup-safe research IPA SHA-256: `69d4257fa6a514724b54a5c19e17803349ba459fef37f76ce4cb4435d3efa724`
- outer delivery ZIP SHA-256: `dad9c4d1dac1a6e9cbe29d8535709f19d8dc0d014cb32c1c77d0bdf8f13b74e3`
- official identity preserved: `com.openai.chat / 1.2026.202 / 30140022279`
- exact content diff versus pristine source remains zero removed / two added (original enhancer backup + research marker) / one modified (enhancer load entry replaced by the startup-safe Probe).

Evidence ladder: **v0.8 first batch Human Runtime launch-crash / v0.8 diagnostic evidence invalid / startup-risk cause inferred from source differential / startup-safe replacement code written / dedicated research CI passed / regular PR CI passed / Artifact produced / package identity independently verified / corrected package Human Runtime pending / ChatGPTClient product remains exact b95 / b96 unallocated / Stable-Frozen Send No.**

**Next exact action:** use only the corrected startup-safe v0.8.1 batch package. First gate is simply that official ChatGPT launches and stays alive. If it launches, continue the same single comprehensive cross-platform active-to-terminal run and export both logs once. If it still launch-crashes, stop immediately; do not ask the user for another protocol reproduction and do not add more response surfaces. Product b96 remains unallocated.