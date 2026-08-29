# DEV-send-stream

## Status

**Active — exact b43 hybrid Artifact ready; waiting for real-device Runtime**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Task**: deliver a usable ChatGPT-account Send path without circumventing browser anti-abuse protections. Native read/navigation remains the product shell; ChatGPT-account Send is explicitly allowed to use a **user-visible official ChatGPT Web surface** under TD-024.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable predecessor b38 remains the merged native read/metadata/round-navigation baseline.
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable and retitled `DEV-send-stream: hybrid visible-Web Send b43 Runtime gate`.
- **Parallel/conflict guard**: resume guard on 2026-08-29 found no peer Active development checkpoint; `main` remained exactly `34811877896ca88c6656be6676f5466a19931ce6` through the b43 handoff.

## Security / architecture boundary retained

Exact b42 `DEV-send-stream-0.1.0-b42`, product source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`, exact iPhone/iOS17 default-primary-assistant Runtime established:

- `proofOfWorkRequired=true`;
- `turnstileRequired=true`;
- `soRequired=true`;
- Sentinel finalize submitted non-empty PoW and non-empty Turnstile before successful Send.

Therefore pure-native/transient-WebKit-auth ChatGPT-account Send remains blocked. Do not implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, hidden challenge-harvesting WebViews or native replay of browser challenge output.

The user explicitly selected **Option 2 / TD-024**: native shell/read/navigation + **user-visible official ChatGPT Web Send**. This is a deliberate hybrid architecture and is not pure-native Send.

## Hard UX requirements

1. Web interaction must feel as close as practical to native iOS controls on the primary iPhone 15 Pro Max / iOS 17.0; functional Send alone is insufficient.
2. Ordinary Back -> re-entry must avoid unnecessary page reconstruction/reload; keep the visible official-Web controller/WebView resident where lifecycle/memory permit.
3. Native UIKit remains the outer navigation/container owner.
4. No continuous DOM observation/JS bridge chatter solely to mirror Web state into native UI.
5. Attachment `+` must not wait on Web navigation, network, Sentinel/Turnstile or upload preparation before local selection UI begins presenting. Exact native-picker -> official-Web file handoff remains Unknown / Unverified.

## b43 product implementation

The first hybrid Candidate is intentionally narrow:

- `AuthWebViewController.swift`
  - adds `AuthVerificationMode.hybridChat`;
  - adds one process-resident shared visible controller `AuthWebViewController.hybridChat` using default persistent `WKWebsiteDataStore`;
  - loads official `https://chatgpt.com/` on first visible presentation only;
  - ordinary pop -> re-entry reuses the same controller/WebView without automatic reload;
  - no protocol-probe injection, prompt/answer/reasoning scraping, token/proof capture or hybrid account probe;
  - privacy-safe `webSend` diagnostics cover presentation/reuse, destination/host, navigation duration/failure and explicit refresh only.
- `SettingsViewController.swift`
  - adds `混合发送` and `打开官方 ChatGPT（混合发送）`;
  - pushes the shared visible Web controller using native navigation.

Exact Option-2 implementation compare `cdffa7a950ac128cc80ca0cf8de22dfe66a128fd` -> `8be4da4e6af3dad146bc43888ddeb3f4cd2037b8` changed only those two product files. An early Root prototype was reverted; b43 has no net product change to `RootViewController.swift` or `ConversationFeature.swift`.

No `/c/<conversation-id>` deep-link guess, DOM automation, native message mirroring, challenge harvesting or native-to-Web file-input injection is part of b43.

## Rejected identity incident

Before b43 metadata was atomically published, product commit `8be4da4e6af3dad146bc43888ddeb3f4cd2037b8` automatically built under stale b42 metadata:

- push Run `33238065644`;
- Artifact `9710515489`;
- container `ChatGPTClient-DEV-send-stream-0.1.0-b42`;
- ZIP `sha256:d76747ea3c524f31e9a6e512119ab3a85172c5c7fc3492d4264a57f93bd86f7f`.

This Artifact is **identity-invalid and permanently rejected**. Never install or cite it as Runtime. It does not redefine legitimate b42 Artifact `9709824510`. PR Run `33238066937` is likewise invalid-identity CI evidence only.

## Exact valid b43 identity / evidence

- **Candidate**: `DEV-send-stream-0.1.0-b43`
- **Version/build**: `0.1.0 (43)`
- **Exact product/config source**: `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`
- **Atomic publication tree**: `126d165cf999b1e8d28e81329c4b04a3113a1cc7`
- **Push Run / Job**: `33241032864` / `99070294478` — success
- **PR Run / Job**: `33241035013` / `99070299776` — success
- **Artifact**: `9711364573`
- **Artifact ZIP digest**: `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`
- **IPA**: `ChatGPTClient-0.1.0-b43-dev-send-stream.ipa`
- **IPA SHA-256**: `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`
- **Independent package inspection**: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=43`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b43`, `DiagnosticsSourceCommit=f602d68ae95d`, Release, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`, Mach-O 64-bit arm64.
- **Evidence classification**: Code written / CI passed / Artifact produced / package identity verified. **Runtime/manual/real-device pending. Stable/Frozen No.**

## State-owner boundary

- `ConversationRepository` remains sole native conversation/list/detail/recovery authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `RootViewController` remains the native shell's compact navigation owner.
- The **visible** official-Web surface owns only its own official Web session/Send interaction while presented; it is not a second native conversation repository or native response authority.
- Native Sync/Reload continue to never resend/regenerate.
- Stable b38 bounded-chunk/deterministic-geometry/round-navigation contracts remain untouched by b43 product code.

## Exact-device Runtime matrix — next human gate

Install exact b43 on the primary iPhone/iOS17 device and test:

1. Settings -> `打开官方 ChatGPT（混合发送）`; first native transition should appear promptly and official ChatGPT should become usable without an app-level stall.
2. Use native Back, then enter again. Re-entry must reuse the resident controller/WebView instead of avoidably reconstructing/reloading the page; diagnostics should show `residentReuse=true`.
3. Exercise keyboard show/hide and normal typing; judge whether input response is close enough to native.
4. Send one ordinary text message through the **visible official Web surface** and observe streamed-response scrolling.
5. Rapidly scroll a longer response/conversation and compare perceived smoothness with the accepted native reading surface.
6. Tap official Web `+` / attachment entry; material perceptible delay before the local action surface/picker means the hybrid UX is not accepted.
7. Return to native list/detail and exercise ordinary reading/round navigation; confirm no regression.
8. If any behavior is rejected or ambiguous, export diagnostics and supply the exact JSON. Diagnostics must contain no prompt/answer body, raw IDs, Cookie/Auth or challenge/proof/token values.

## Durable docs / PR synchronized before this checkpoint write

The docs-only chain after exact b43 product source synchronized:

- `MODULE_STATUS.md`
- `PROJECT_STATE.md`
- `TECHNICAL_DECISIONS.md` with TD-024
- `PROJECT_SPECIFIC_RULES.md`
- `DEVELOPMENT_PLAN.md`
- `PROJECT_PROFILE.md`
- `BUILD_TEST_INDEX.md`
- selected checkpoint

PR #29 body/title now records Option 2, exact valid b43 identity, rejected `9710515489`, and the Runtime gate.

Verified compare from exact b43 product source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c` to docs head `e3600cb2d8dedbaaa1e7e0c5010c1e8fae4c97ee` contained **only eight `docs/project/` files**, with no Swift/Xcode/workflow/script drift. This checkpoint write is docs-only and may advance branch/PR head without redefining b43 product source.

## Batch closure / recovery point

Completed:

- architecture Option 2 selected;
- minimal hybrid product implementation written;
- old-identity accidental Artifact rejected;
- valid b43 identity atomically published at exact source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`;
- push CI + PR CI succeeded;
- valid Artifact produced and independently package-identity verified;
- durable docs and PR synchronized;
- product-source -> docs-head drift audit passed as docs-only.

Pending only for this Candidate:

- exact-device Runtime acceptance/rejection of the matrix above.

Recovery must not reuse b39-b43 Candidate identities, must never promote rejected Artifact `9710515489`, must not redefine legitimate b42/b43 product sources, and must not merge PR #29 as accepted hybrid Send before user Runtime acceptance.

## Next exact action

User installs/tests exact `DEV-send-stream-0.1.0-b43` IPA on the primary iPhone/iOS17 device. If the user reports any defect or supplies diagnostics, re-run branch/PR/base/conflict identity guard first, interpret the exact b43 Runtime evidence, and allocate **b44 or later** for any corrected product code. If the user accepts the full matrix, record Runtime acceptance before deciding PR merge/next phase.
