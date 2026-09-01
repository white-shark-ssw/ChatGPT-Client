# DEV-send-stream — official iOS realtime Probe TrollStore package — 2026-09-02

## Purpose

The target device has TrollStore but no jailbreak/Filza and may not have a separate dylib injector. To remove that tooling dependency, a research-only TrollStore-installable IPA was prepared from the exact user-supplied decrypted official ChatGPT package.

This is research tooling only. It is not a ChatGPTClient product Candidate and does not allocate b83.

## Source package identity

- User-supplied archive: `ChatGPT_Decrypted.zip`
- Source ZIP SHA-256: `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`
- App bundle ID: `com.openai.chat`
- Official app version/build observed in the supplied package: `1.2026.202 / 30140022279`
- Existing research enhancer entry: `Frameworks/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`
- Existing enhancer SHA-256: `aae66c63a7122d301be5025305b92ec63b8da020fdceef22df9bec7cc1acc7b3`
- `Assets.framework/Assets` already contains the load reference `@rpath/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`.

## Final chained Probe identity

The Probe was changed so the pre-existing enhancer is loaded before the Probe installs its own NSURLSession/WebSocket hooks. This preserves the existing enhancer behavior while allowing the Probe to wrap the final method implementations.

- Research source head: `5d2fd88a4a7916827811387b571091f4a894c64f`
- Research workflow run: `33554493790`
- Research job: `100011862928`
- Build/validate/upload: **success**
- Artifact ID: `9818748583`
- Artifact name: `ChatGPTRealtimeProbe-5d2fd88a4a7916827811387b571091f4a894c64f`
- Artifact ZIP digest: `sha256:b0e3f36eec3d9b51befac98e43b54370d754125c4a7f19fcde7f66596dea2a52`
- Exact chained Probe dylib SHA-256: `0d20cf4761a982612fab995ed8766a887064005a561726c603edceea6072285e`
- Exact chained Probe dylib size: `135088` bytes

## Packaging method

No new Mach-O load command was inserted.

The source package already loads the existing enhancer entry from `Assets.framework`. Packaging therefore uses the existing proven load path:

1. rename the exact original enhancer to `Frameworks/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.original.dylib` without changing its bytes;
2. place the exact chained Probe dylib at the original loaded path `Frameworks/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`;
3. Probe constructor priority loads the renamed original enhancer first via `dlopen`;
4. Probe then installs its research observation hooks and in-app export UI.

Expected runtime load chain:

`Assets.framework -> Probe entry -> renamed original ChatGPTEnhancer -> Probe NSURLSession/WebSocket hooks`

## Exact packaged IPA

- File: `ChatGPT-Official-RealtimeProbe-TrollStore.ipa`
- IPA SHA-256: `f23adc1e78dc3f76b66140f23548e331a3545c5b9772608122f493e738242e0f`
- Approximate size: 95 MB

Static package inspection confirms:

- loaded entry dylib SHA matches the final chained Probe SHA;
- renamed original enhancer SHA exactly matches the source package enhancer SHA;
- `Assets.framework` load reference remains unchanged;
- IPA contains the expected Probe marker strings and in-app `Probe` export UI;
- relative to the extracted user source package, content hash comparison reports exactly three intentional file changes:
  1. replaced `Frameworks/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`;
  2. added `Frameworks/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.original.dylib`;
  3. added `ChatGPTRealtimeProbe-Research.txt`.

No other extracted App file content changed.

## Evidence classification

- research Probe code written: Yes
- chained Probe CI compile/validate: Passed
- chained Probe Artifact produced: Yes
- TrollStore IPA assembled: Yes
- package static hash/difference validation: Passed
- TrollStore install: **Pending Human Runtime**
- Probe UI visible in official app: **Pending Human Runtime**
- original enhancer preserved at runtime: **Pending Human Runtime**
- WebSocket protocol captured: **Pending Human Runtime**
- b83 allocated: No
- Stable/Frozen Send: No

## Next Human Runtime gate

1. Install `ChatGPT-Official-RealtimeProbe-TrollStore.ipa` through TrollStore. This package uses the same bundle ID as the supplied official ChatGPT app, so it is intended as the research replacement/update for that app, not as a parallel product app.
2. Fully terminate ChatGPT and relaunch it.
3. Confirm a small blue `Probe` button appears near the top-right safe area.
4. If the button does not appear or the app does not launch, stop and report that exact result; do not perform the conversation test.
5. If the button appears, tapping it should open the normal iOS share sheet for `ChatGPTRealtimeProbe.jsonl` once the log exists. No Filza is required.
6. Keep target conversation A available, then from another platform send one deliberately long text turn to A. Do not manually refresh during generation.
7. After completion, tap `Probe`, export/share `ChatGPTRealtimeProbe.jsonl`, and provide that file for analysis.

The decisive protocol evidence remains whether a target-matching conversation event arrives before completion and what exact registration/subscribe framing is used by the current official app/account.

A successful install or visible Probe button is not by itself protocol Runtime proof.
