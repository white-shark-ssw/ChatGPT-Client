# Official iOS Realtime Probe

Current research revision: **Probe v0.2**.

Research-only observer for the user-supplied TrollStore ChatGPT package. It is not linked into ChatGPTClient and is not a product Candidate.

## What it observes

Only privacy-safe structure:

- privacy-safe conversation/realtime HTTP path shape, method/status/MIME/JSON key names, including Detail/stream-status/resume/SSE candidates;
- likely realtime registration HTTP method/path/status and JSON key names;
- WebSocket host/path plus query presence/count, never query values;
- outbound command/frame key names, command type, symbolic topic, offset value class;
- inbound frame/payload key names, event/update type, message count, and a 12-hex SHA-256 prefix for conversation identity;
- transport errors by domain/code.

It does not log Cookie/Authorization headers, signed WebSocket query values, prompt/answer/reasoning/tool text, request/response bodies, or raw conversation IDs.

## Build

Run on macOS/Xcode:

```sh
bash scripts/research/official_ios_realtime_probe/build_probe.sh
```

The output is `ChatGPTRealtimeProbe.dylib` plus SHA-256 sidecar.

## Install for research

Inject the built dylib into the supplied official ChatGPT TrollStore app with the same TrollFools-style mechanism already used by that package. Keep the existing `ChatGPTEnhancer` injection; this probe is an additional observer.

After injection, fully terminate and relaunch ChatGPT. The probe writes `ChatGPTRealtimeProbe.jsonl` into the app Documents directory and mirrors only event names to unified logs. The in-app `清空` control deletes prior JSONL content and writes a fresh `probe.log_cleared` marker before the next test.

## Decisive test

1. Launch the injected official app and open/keep conversation A available.
2. Confirm `probe.loaded` and WebSocket setup events exist in `ChatGPTRealtimeProbe.jsonl`.
3. From another platform, send one deliberately long text turn to A.
4. Let the response complete without manually refreshing A on the official iOS app.
5. Export/copy only `ChatGPTRealtimeProbe.jsonl` for analysis.

The decisive question is whether a target conversation event (`conversation-update`, `add-messages`, async status, or a per-turn subscription) arrives before assistant completion.

## Evidence boundary

A positive early WebSocket event authorizes only a realtime trigger design. WebSocket message bodies do not become ChatGPTClient content authority until separately proven complete and lifecycle-safe. `ConversationRepository` remains the product response owner.
