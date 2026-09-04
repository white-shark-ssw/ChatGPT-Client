# DEV-send-stream round 7 Runtime addendum

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
