# DEV-send-stream

## Status

**Active — b43 valid hybrid Artifact produced; exact-device Runtime required**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Task**: deliver a usable ChatGPT-account Send path without circumventing browser anti-abuse protections. Native read/navigation remains the product shell; Send is explicitly allowed to use a **user-visible official ChatGPT Web surface**.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable predecessor b38 remains the merged native read/metadata/round-navigation baseline.
- **Working branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable. Actual b43 product/config source is `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`; later docs-only commits do not redefine that source.
- **Parallel/conflict guard**: resume guard verified unchanged main and no peer Active development checkpoint.
- **Candidate identity**: b39-b42 permanently reserved; valid hybrid Candidate is `DEV-send-stream-0.1.0-b43`, version/build `0.1.0 (43)`.

## Exact b42 decision evidence retained

Exact b42 source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, Artifact `9709824510`, exact iPhone/iOS17 default-primary-assistant Runtime established `proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, with non-empty PoW and Turnstile finalize submissions before successful Send.

Therefore pure native/transient-auth Send remains blocked. Do not implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, or a hidden WebView used only to harvest challenge output.

## User architecture decision — Option 2

The user explicitly chose **Native shell + user-visible official-Web Send** after b42 Path B.

Hard product requirements:

1. Web interaction must feel as close as practical to native iOS controls on iPhone 15 Pro Max / iOS 17.0; functional Send alone is insufficient.
2. Ordinary return/re-entry must avoid unnecessary page reconstruction/reload. Keep the visible official-Web controller/WebView resident where lifecycle and memory evidence permit.
3. Native UIKit remains the outer navigation/container owner.
4. No continuous DOM-observation/JS bridge chatter solely to mirror Web state into native UI.
5. Attachment entry is a hard UX gate: tapping `+` must not wait on Web/network/Sentinel/upload work before local selection UI begins presenting. Exact native-to-Web file handoff remains Unknown / Unverified until separately evidenced.

## b43 implementation

Net product change remains deliberately small and does not modify Stable `ConversationFeature.swift` or Root behavior:

- `AuthWebViewController.swift`
  - adds `AuthVerificationMode.hybridChat`;
  - adds one process-resident shared visible controller `AuthWebViewController.hybridChat` backed by default persistent `WKWebsiteDataStore`;
  - loads `https://chatgpt.com/` only when the user presents the surface;
  - first presentation loads once; later pop -> re-enter reuses the same controller/WebView without automatic reload;
  - no protocol-probe injection, prompt/answer scraping, token/proof capture or hybrid-mode account probe;
  - privacy-safe `webSend` diagnostics record presentation/reuse, destination/host, navigation duration/failure and explicit refresh only.
- `SettingsViewController.swift`
  - adds `混合发送` and `打开官方 ChatGPT（混合发送）`;
  - pushes the shared visible Web controller using native navigation.

Exact Option-2 implementation compare from `cdffa7a950ac128cc80ca0cf8de22dfe66a128fd` to product commit `8be4da4e6af3dad146bc43888ddeb3f4cd2037b8` changed only those two product files. An earlier Root prototype was reverted; Root and `ConversationFeature.swift` have no net product diff.

The milestone intentionally does **not** guess `/c/<conversation-id>` deep links, DOM automation, native message mirroring, or native-to-Web file-input injection.

## Rejected accidental old-identity emission

Before b43 metadata was published, old b42 workflow metadata automatically built newer hybrid code:

- push Run `33238065644` — success;
- Artifact `9710515489`;
- container `ChatGPTClient-DEV-send-stream-0.1.0-b42`;
- ZIP digest `sha256:d76747ea3c524f31e9a6e512119ab3a85172c5c7fc3492d4264a57f93bd86f7f`.

This Artifact is **identity-invalid and permanently rejected**. It does not redefine legitimate b42 Artifact `9709824510`, must not be installed, and is not Runtime evidence. PR Run `33238066937` is likewise invalid-identity CI evidence only.

## Exact valid b43 identity / validation ladder

- **Candidate**: `DEV-send-stream-0.1.0-b43`
- **Version/build**: `0.1.0 (43)`
- **Exact product/config source**: `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`
- **Atomic publication tree**: `126d165cf999b1e8d28e81329c4b04a3113a1cc7`
- **Push Run / Job**: `33241032864` / `99070294478` — success; build, inspect and upload all succeeded.
- **Artifact**: `9711364573`
- **Artifact ZIP digest**: `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`
- **IPA**: `ChatGPTClient-0.1.0-b43-dev-send-stream.ipa`
- **IPA SHA-256**: `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`
- **Independent package inspection**: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=43`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b43`, `DiagnosticsSourceCommit=f602d68ae95d`, Release, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`, Mach-O 64-bit arm64.
- **PR Run / Job**: `33241035013` / `99070299776` — success.
- **Evidence classification**: Code written; CI passed; Artifact produced; package identity independently verified. **Runtime/manual/real-device: pending. Stable/Frozen: No.**

## b43 exact-device Runtime gate

Test the exact b43 IPA on the primary iPhone/iOS17 runtime:

1. In Settings, open `打开官方 ChatGPT（混合发送）`; first native transition should appear promptly and official ChatGPT should become usable without an app-level stall.
2. Return with native Back, then enter the hybrid surface again. It must reuse the resident controller/WebView instead of avoidably reconstructing/reloading the page; diagnostics should show `residentReuse=true` on re-entry.
3. Exercise keyboard show/hide and normal typing. Input response must feel close to native and not exhibit material WebView-specific lag.
4. Send one ordinary text message through the visible official Web surface and observe streamed response scrolling.
5. Rapidly scroll a longer response/conversation and compare perceived smoothness with the accepted native reading surface.
6. Tap official Web `+` / attachment entry and judge time-to-action-surface/picker. Material perceptible delay means the hybrid UX is not accepted; do not mask it with a spinner.
7. Return to native read UI and verify ordinary conversation list/detail/round navigation still behaves normally.
8. Export diagnostics after the matrix if behavior is rejected or ambiguous. Diagnostics must contain no prompt/answer body, raw IDs, Cookie/Auth, challenge/proof/token values.

## State-owner boundary

- `ConversationRepository` remains sole native conversation/list/detail/recovery authority.
- `AuthSessionStore` remains auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `RootViewController` remains the native shell's compact navigation owner.
- The **visible** official-Web surface owns its own Web Send/challenge execution while the user is on that surface; it is not a second native conversation repository and does not become native message authority.
- Native Sync/Reload continue to never resend/regenerate.

## Batch recovery point — b43 handoff

Confirmed complete:

- Option 2 selected and UX constraints recorded.
- Hybrid product code written and net diff audited.
- Old-identity accidental Artifact `9710515489` rejected permanently.
- b43 Xcode/workflow identity atomically published at exact source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`.
- Push CI, PR CI, Artifact generation and independent package inspection all passed.

Pending:

- exact-device Runtime acceptance/rejection of first-entry latency, resident re-entry, keyboard/typing, visible Web Send/stream scroll, rapid scroll, `+` responsiveness and native-return regression.
- after Runtime, update durable evidence/status accordingly; do not merge PR #29 as accepted hybrid Send before user Runtime acceptance.

Recovery must not touch/reuse b39-b42 identities, rejected Artifact `9710515489`, Stable b38 geometry/round contracts, or any superseded unpublished preparation commit.

## Next exact action

Install and test exact `DEV-send-stream-0.1.0-b43` IPA on the primary iPhone/iOS17 device using the matrix above. User Runtime result is the next human-only gate; CI/Artifact success is not Runtime acceptance.
