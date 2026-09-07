# DEV-send-stream — official iOS realtime Probe in-app export UI — 2026-09-02

## Reason for this change

The target device is TrollStore-only and does not have a jailbreak or Filza. The first research Probe wrote `ChatGPTRealtimeProbe.jsonl` into the official ChatGPT app's Documents directory, which is valid technically but not directly usable by the user's actual device workflow.

This is a research-tooling accessibility change only. It does not modify ChatGPTClient product code and does not allocate b83.

## Change

The research Probe now includes `ProbeExportUI.m` and links UIKit.

When the injected Probe is loaded in the official ChatGPT process, it attaches a small `Probe` button to the active foreground window. Tapping the button:

- presents an explanatory alert if `ChatGPTRealtimeProbe.jsonl` does not yet exist;
- otherwise opens `UIActivityViewController` with the exact JSONL file URL so the user can Save to Files / AirDrop / share it without Filza or app document-sharing entitlement.

The button does not display or parse conversation bodies. It is only an export surface for the already privacy-bounded JSONL.

## Exact research identity

- Research branch: `dev/send-stream-20260829`
- Research source head: `a1d6ca0be8099a0e36c04ebecb649a31be5b48b9`
- Workflow: `Research Official iOS Realtime Probe`
- Run: `33553941529`
- Result: **success**
- Artifact ID: `9818535820`
- Artifact name: `ChatGPTRealtimeProbe-a1d6ca0be8099a0e36c04ebecb649a31be5b48b9`
- Artifact ZIP digest: `sha256:37068668207a813b66b661c20ee7e040f2abe7628523d237656f8cad632dd9b8`
- Exact dylib SHA-256 after Artifact download/reverification: `85782137ddce0fdab022805f2f822ed6ce5f50beefab4c446c97007bcf5d19c7`
- Exact dylib size: `134896` bytes

CI proved only that the UIKit-enabled research dylib builds, validates and is produced as an Artifact. It is not yet Runtime proof that the Probe loads in the official app or that its network hooks observe the target WebSocket path.

## Device-access decision

No Filza is required anymore.

If the device has an existing dylib-injection tool such as TrollFools, inject the exact dylib above as an additional dylib, keep the existing ChatGPTEnhancer injection, fully relaunch ChatGPT, and use the visible `Probe` button to export the JSONL.

If the device has only TrollStore itself and no dylib-injection entry, do **not** ask the user to jailbreak or install Filza. TrollStore is an installer/signing-bypass surface, not by itself a generic dylib injector. In that environment the next packaging action is to produce a research-only TrollStore-installable official-app test IPA from the user-supplied decrypted package with the Probe already wired into its existing research injection chain.

That packaging must preserve the user's existing ChatGPTEnhancer behavior and must not be described as product b83.

## Runtime gate after installation

1. Fully terminate and relaunch the research official ChatGPT build.
2. Confirm a small `Probe` button appears near the top-right safe area.
3. If no button appears, stop: classify Probe load/UI Runtime as failed and diagnose injection only.
4. If the button appears, run one deliberately long cross-platform turn in target conversation A without manually refreshing A.
5. After completion, tap `Probe` and share/save `ChatGPTRealtimeProbe.jsonl`.
6. Analyze whether target-matching `conversation-update`, `add-messages`, async-status or per-turn subscription events arrived before completion, plus exact registration/subscribe framing.

A visible `Probe` button proves only that the research dylib/UI constructor loaded. It does not by itself prove the WebSocket hook captured the official realtime protocol.

## Product boundary

- b83 remains unallocated.
- Official ChatGPT code/framework remains an evidence oracle, not a product dependency.
- `ConversationRepository` remains the sole Native response/content authority.
- No hidden polling, retry, watchdog, fake stream or second response store is authorized by this tooling change.
