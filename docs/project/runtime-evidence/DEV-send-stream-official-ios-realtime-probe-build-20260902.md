# DEV-send-stream — official iOS realtime research probe build — 2026-09-02

## Scope

Research/tooling evidence only. This does not allocate b83 and does not modify ChatGPTClient product behavior.

## Source identity

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- Research source/workflow head: `501839a8aad91373c2a90397c08cf84251553f41`
- Probe source: `scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m`
- Build script: `scripts/research/official_ios_realtime_probe/build_probe.sh`
- Workflow: `.github/workflows/research-official-ios-realtime-probe.yml`

## CI / Artifact

- Workflow: `Research Official iOS Realtime Probe`
- Run: `33552727671`
- Job: `100005909674`
- Conclusion: **success**
- Build research dylib: success
- Validate research artifact: success
- Upload research probe: success
- Artifact ID: `9818074442`
- Artifact name: `ChatGPTRealtimeProbe-501839a8aad91373c2a90397c08cf84251553f41`
- Artifact ZIP digest reported by GitHub: `sha256:220c19a6074ca2678b3a70c30fe60bfda257be3df3cb1a607d995665d06ec056`
- Probe dylib SHA-256: `7b449f91bc903fa56216d142f2373c0f0c94065271ba7a7160aae0a0f5c4b6ff`
- Probe dylib size: `112352` bytes

Local re-verification after downloading the canonical workflow Artifact reproduced the exact dylib SHA-256 above.

## Mach-O boundary

`ChatGPTRealtimeProbe.dylib` has install name:

- `@rpath/ChatGPTRealtimeProbe.dylib`

Its linked dependencies are system-only:

- Foundation;
- libobjc;
- libSystem;
- CoreFoundation.

It does **not** link `ChatGPT.framework`, CydiaSubstrate, or the existing ChatGPTEnhancer dylib.

The probe is therefore an independent research observer rather than a product dependency on official private code.

## Observation behavior

The probe installs Objective-C runtime hooks around Foundation URLSession/WebSocket paths and writes bounded JSONL structural events to `ChatGPTRealtimeProbe.jsonl` in the official app Documents directory.

It is designed to record only:

- likely realtime registration request method/path and response status/key names;
- WebSocket host/path plus query presence/count, never query values;
- outbound command/frame key names, command type, safe symbolic topic and offset value class;
- inbound frame/payload key names, event/update type, message count and a short SHA-256 conversation identity hash;
- transport error domain/code.

It does not intentionally record:

- Cookie / Authorization headers;
- signed WebSocket query values;
- access/session/challenge values;
- request/response bodies as text;
- prompt/answer/reasoning/tool text;
- raw conversation IDs.

A post-build string spot-check of the dylib found no `Cookie`, `Authorization`, `prompt`, `reasoning`, `answer`, or `tool` logging strings.

## Installation boundary

The research Artifact is intended to be injected as an **additional** dylib into the supplied TrollStore/decrypted official ChatGPT app with TrollFools-style injection. Do not replace or remove the existing ChatGPTEnhancer solely for this test.

This avoids repackaging official code in ChatGPTClient and keeps the probe isolated from the product Candidate chain.

## Decisive Runtime gate

1. Inject the exact dylib SHA above into the supplied official ChatGPT app.
2. Fully terminate and relaunch official ChatGPT.
3. Verify `probe.loaded` and WebSocket setup events appear in `ChatGPTRealtimeProbe.jsonl`.
4. Keep target conversation A available.
5. From another platform, send one deliberately long text turn to A.
6. Do not manually refresh the target conversation during the generation interval.
7. After completion, export only `ChatGPTRealtimeProbe.jsonl`.
8. Determine whether a target conversation `conversation-update`, `add-messages`, async-status, or per-turn subscribe event arrived before completion.

A positive early event may authorize a minimal b83 **trigger/acquisition** implementation. It does not by itself authorize WebSocket message bodies as Native content authority.

## Evidence classification

- Probe source written: **Yes**.
- iOS SDK compile: **CI Positive**.
- Mach-O/signature validation: **CI Positive**.
- Research Artifact produced: **Yes**.
- Official-app injection: **Not yet Runtime tested**.
- Official-app hook execution: **Not yet Runtime tested**.
- Exact registration/topic/current-account protocol: **Pending**.
- b83: **not allocated**.
- Stable/Frozen Send as a whole: **No**.
