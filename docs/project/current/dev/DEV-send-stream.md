# DEV-send-stream

## Status

**Active — b82 Runtime remains Partial. Passive official Web is Runtime Rejected. Official iOS static evidence proves a separate topic-based realtime layer. A research-only Foundation WebSocket observer has been written and CI-built, now with in-app JSONL export and a TrollStore-only prepackaged official-app research IPA. Exact registration/topic/current-account behavior is still Runtime Pending; therefore b83 remains unallocated. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main` verified this round: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b82 product/config source: `c7a274786dfd175e8f476fc15c4964840e112a1d`
- Candidate: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- Canonical b82 Artifact: `9811406038`
- b82 IPA SHA-256: `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2`
- b39-b82 permanently reserved
- b83: **not allocated**
- Stable/Frozen Send: No

## Current accepted Runtime evidence

### b82

b82 automatically acquires a completed remote turn without manual Sync, but the first exact-conversation user-socket `targetMatch=true` frame arrived only when authoritative Detail already advanced `8 -> 10`. No earlier socket frame, external snapshot or Repository live response was observed during generation. Therefore that socket event is accepted only as a completion/update hint for the tested flow, not a request-start/live-stream signal.

### Visible official Web

The user tested official ChatGPT Web already open on the same conversation before a remote long turn. It did not automatically show the remote user row, live response, or even the completed turn without explicit refresh/navigation. Passive page visibility/focus is therefore rejected as the missing acquisition mechanism.

## Official iOS native realtime static evidence

The user-supplied official package (`com.openai.chat` 1.2026.202 / build 30140022279) statically proves a separate native realtime layer including `WebSocketRegisterResponse.websocketURL`, `WebSocketTopic(topicId, offset)`, `SubscribePayload(topicId, lastOffset, recovered, catchups)`, `connect` / `subscribe` / `presence`, catchup/live semantics, `WebSocketConversationEventsService`, `conversation-update`, `add-messages`, async-status/task/title/stop updates, and a bounded `ConversationPollingManager`.

This is static evidence only. Exact current registration URL/topic/auth/offset framing remains Runtime Pending.

## Research realtime Probe — latest exact identity

Research source/tooling:

- `scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m`
- `scripts/research/official_ios_realtime_probe/ProbeExportUI.m`
- `scripts/research/official_ios_realtime_probe/ProbeEnhancerChain.m`
- `scripts/research/official_ios_realtime_probe/build_probe.sh`
- `.github/workflows/research-official-ios-realtime-probe.yml`

Final chained Probe:

- source head: `5d2fd88a4a7916827811387b571091f4a894c64f`
- workflow run: `33554493790` — **success**
- job: `100011862928`
- Build research dylib: success
- Validate research artifact: success
- Upload research probe: success
- Artifact ID: `9818748583`
- Artifact: `ChatGPTRealtimeProbe-5d2fd88a4a7916827811387b571091f4a894c64f`
- Artifact ZIP digest: `sha256:b0e3f36eec3d9b51befac98e43b54370d754125c4a7f19fcde7f66596dea2a52`
- exact Probe dylib SHA-256: `0d20cf4761a982612fab995ed8766a887064005a561726c603edceea6072285e`
- exact Probe dylib size: `135088` bytes

The Probe links system Foundation/UIKit/ObjC/System only. It does not link official `ChatGPT.framework` as a product dependency.

### Privacy boundary

The Probe records only privacy-safe structure: likely realtime request path/method/status/key names; WebSocket host/path without signed query values; command/topic/offset shape; inbound event/update key names/counts and hashed conversation identity. It does not intentionally log Cookie/Authorization/token/challenge values, raw conversation IDs, prompt/answer/reasoning/tool bodies or signed WebSocket query values.

### In-app export

The target phone has TrollStore but no jailbreak/Filza. The Probe includes a small blue `Probe` button on the active ChatGPT window. Tapping it opens the standard iOS share sheet for `ChatGPTRealtimeProbe.jsonl`; no Filza or Files-document-sharing entitlement is required.

A visible Probe button proves only dylib/UI Runtime loading, not WebSocket protocol capture.

## TrollStore-only prepackaged official-app research IPA

Because TrollStore itself is not a generic dylib injector, a research IPA was assembled from the exact user-supplied decrypted package using its already-existing Enhancer load path.

Source package:

- `ChatGPT_Decrypted.zip`
- source ZIP SHA-256: `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`
- original Enhancer SHA-256: `aae66c63a7122d301be5025305b92ec63b8da020fdceef22df9bec7cc1acc7b3`

Packaging chain:

`Assets.framework -> Probe entry -> renamed original ChatGPTEnhancer -> Probe NSURLSession/WebSocket hooks`

No new Mach-O load command was inserted. The existing `@rpath/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib` reference remains unchanged. The original enhancer bytes are preserved under `ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.original.dylib`, loaded before Probe hook installation.

Exact research IPA:

- `ChatGPT-Official-RealtimeProbe-TrollStore.ipa`
- SHA-256: `f23adc1e78dc3f76b66140f23548e331a3545c5b9772608122f493e738242e0f`
- approx size: 95 MB

Static extracted-tree comparison versus the user source package found exactly three intentional file-content changes:

1. replaced the existing Enhancer load-entry file with the final Probe;
2. added the byte-identical renamed original Enhancer;
3. added `ChatGPTRealtimeProbe-Research.txt`.

No other extracted App file content changed.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-official-ios-runtime-hook-plan-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-build-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-export-ui-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-official-ios-realtime-probe-trollstore-package-20260902.md`

## Evidence ladder

- official native realtime architecture: Static Positive
- research Probe code written: Yes
- chained Probe CI: Passed
- chained Probe Artifact produced: Yes
- TrollStore research IPA assembled: Yes
- package static hash/difference validation: Passed
- TrollStore install: **Pending Human Runtime**
- Probe UI load: **Pending Human Runtime**
- original Enhancer preserved at runtime: **Pending Human Runtime**
- official WebSocket registration/topic/event capture: **Pending Human Runtime**
- b83: not allocated
- Stable/Frozen Send: No

## Product decision / frozen boundaries

The official package is an evidence oracle, not a ChatGPTClient dependency. Do not embed/link/call/redistribute official private framework code as product implementation. After exact Runtime evidence, reimplement only the minimum verified wire behavior in our own Swift/Foundation code.

Preserve:

- b80 tool/timeline -> reasoning-divider spacing Frozen;
- external stopped-thinking semantics Frozen;
- b80 final-materialization gate;
- b67 client-owned protected Send and b72 tested simultaneous ownership;
- `ConversationRepository` as sole Native response/content authority;
- `AuthSessionStore` as sole native auth/account authority.

Do not add duplicate Send/resend, fake streaming, speculative retry/watchdog/fallback, hidden fixed polling or a second response store.

## Session round counter

The user explicitly reset the conversation round count. This user turn is **round 7**. Continue displaying the current round count at the end of each user-facing response.

## Next exact action — Human Runtime Gate

**Do not allocate b83 yet.**

1. Install exact research IPA `ChatGPT-Official-RealtimeProbe-TrollStore.ipa` SHA-256 `f23adc1e78dc3f76b66140f23548e331a3545c5b9772608122f493e738242e0f` through TrollStore.
2. Fully terminate and relaunch ChatGPT.
3. Confirm a small blue `Probe` button appears near the top-right safe area.
4. If the app fails to launch or no Probe button appears, stop and report that exact result; diagnose packaging/load only.
5. If Probe appears, tap once. Once the JSONL exists, the system share sheet should open; this confirms the user can retrieve the log without Filza.
6. Keep target conversation A available, send one deliberately long turn to A from another platform, and do not manually refresh during generation.
7. After completion, tap `Probe`, export/share `ChatGPTRealtimeProbe.jsonl`, and provide that file for analysis.

The decisive protocol evidence remains whether a target-matching `conversation-update`, `add-messages`, async-status or per-turn subscription event arrives before completion, plus exact registration/subscribe framing.
