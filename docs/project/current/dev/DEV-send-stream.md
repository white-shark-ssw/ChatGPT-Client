# DEV-send-stream

## Status

**Active — Option 2 hybrid user-visible Web Send selected**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Task**: deliver a usable ChatGPT-account Send path without circumventing browser anti-abuse protections. Native read/navigation remains the product shell; Send is explicitly allowed to use a **user-visible official ChatGPT Web surface**.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable predecessor b38 remains the merged native read/metadata/round-navigation baseline.
- **Working branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable. Resume guard verified no peer Active development checkpoint and unchanged base main.
- **Candidate identity**: b39-b42 are permanently reserved. `DEV-send-stream-0.1.0-b43` is allocated for the first hybrid visible-Web feasibility/smoothness Candidate.

## Exact b42 decision evidence retained

Exact `DEV-send-stream-0.1.0-b42`, source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, Artifact `9709824510`, exact iPhone/iOS17 default `primary_assistant` new-chat Runtime established `proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, with non-empty PoW and Turnstile finalize submissions before successful Send.

Therefore pure native/transient-auth Send remains blocked. This Work must not implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, or a hidden WebView used only to harvest challenge output.

## User architecture decision — Option 2

The user explicitly chose the **Native shell + user-visible official-Web Send** direction after b42 Path B.

Hard product requirements:

1. Web interaction must feel as close as practical to native iOS controls on iPhone 15 Pro Max / iOS 17.0; functional Send alone is insufficient.
2. Ordinary return/re-entry must avoid unnecessary page reconstruction/reload. Keep the visible official-Web controller/WebView resident where lifecycle and memory evidence permit.
3. Native UIKit remains the outer navigation/container owner.
4. No continuous DOM-observation/JS bridge chatter solely to mirror Web state into native UI.
5. Attachment entry is a hard UX gate: tapping `+` must not wait on Web/network/Sentinel/upload work before local selection UI begins presenting. Exact native-to-Web file handoff remains Unknown / Unverified until separately evidenced.

## Hybrid implementation currently written

Net product diff after Batch B audit is intentionally small and avoids Stable `ConversationFeature.swift` / Root behavior:

- `AuthWebViewController.swift`
  - adds `AuthVerificationMode.hybridChat`;
  - adds one process-resident shared visible controller `AuthWebViewController.hybridChat` backed by the existing default persistent `WKWebsiteDataStore`;
  - loads the evidenced official root `https://chatgpt.com/` only from `viewWillAppear` when the user actually presents the surface;
  - first presentation loads once; later pop -> re-enter reuses the same controller/WebView without an automatic reload;
  - does not inject protocol-probe scripts, scrape prompt/answer text, capture tokens/proofs, or run auth account probes in hybrid mode;
  - adds privacy-safe `webSend` diagnostics for presentation/reuse, destination/host, navigation duration/failure and explicit user refresh.
- `SettingsViewController.swift`
  - adds a visible `混合发送` section and `打开官方 ChatGPT（混合发送）` entry;
  - pushes the shared visible Web controller with native navigation.

Exact net compare from the Option-2 checkpoint commit `cdffa7a950ac128cc80ca0cf8de22dfe66a128fd` to product head `8be4da4e6af3dad146bc43888ddeb3f4cd2037b8` changed only those two files. An earlier Root prototype was immediately reverted; Root and `ConversationFeature.swift` have no net product diff.

This first milestone intentionally does **not** guess `/c/<conversation-id>` deep links, DOM automation, native message mirroring, or native-to-Web file-input injection. Those remain separately Unverified.

## Accidental old-identity emission discovered

The existing workflow was still configured as b42 and triggers on every `ChatGPTClient/**` push. Therefore product commit `8be4da4e6af3dad146bc43888ddeb3f4cd2037b8` automatically produced:

- push Run `33238065644` — success;
- Artifact `9710515489`;
- Artifact container name `ChatGPTClient-DEV-send-stream-0.1.0-b42`;
- Artifact digest `sha256:d76747ea3c524f31e9a6e512119ab3a85172c5c7fc3492d4264a57f93bd86f7f`.

This Artifact is **identity-invalid and permanently rejected** because it contains product code newer than the exact accepted b42 source while still carrying b42 package/Candidate metadata. It does not redefine or supersede the legitimate exact b42 Artifact `9709824510`, and it must never be installed or cited as a Runtime Candidate.

The corresponding PR-triggered run `33238066937` also succeeded at the same wrong b42 metadata boundary and is CI-only invalid identity evidence, not a Runtime Candidate.

## First valid hybrid Candidate — b43

`DEV-send-stream-0.1.0-b43` is allocated.

The final b43 identity publication commit is `aac437ae616156dfe3657caeecc8e1e90ad86434`, built atomically on branch head `e72cc226b79d09e351819619efb2a2b4c7a4d89a` with tree `f834c3570376be12341c72c6a8c22ff9f6a72e27`:

- Xcode metadata blob `f26636045934e94873b05fa21664a9a1e90735a8`: `CURRENT_PROJECT_VERSION=43`, `DIAGNOSTICS_CANDIDATE=DEV-send-stream-0.1.0-b43` for Debug/Release;
- workflow blob `ddf5ee61aae265b41cc06a34924be18cbaf7f647`: workflow `iOS Hybrid Web Send`, Artifact container b43.

Earlier unpublished preparation commits based on older checkpoint parents are superseded tooling state only; none may be force-pushed or cited as Candidate source.

### b43 exact-device Runtime focus

- first entry: native transition appears promptly and official page becomes usable without app-level UI stall;
- resident re-entry: pop -> re-enter must log `residentReuse=true` and must not perform avoidable full-page reconstruction/reload;
- keyboard show/hide, typing, Send, streamed response scrolling and rapid scrolling feel acceptably close to native;
- official Web `+` / attachment entry is exercised for responsiveness observation; material lag means hybrid UX is not accepted;
- native Back/return is smooth and native read UI remains intact;
- diagnostics contain no prompt/body/raw IDs/Cookie/Auth/challenge/proof/token values.

## State-owner boundary

- `ConversationRepository` remains sole native conversation/list/detail/recovery authority.
- `AuthSessionStore` remains auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `RootViewController` remains single native compact navigation owner for the native shell.
- The user-visible official-Web surface owns its own browser-side Web Send/challenge execution while visible; it is not a second native conversation repository and does not become native message authority.
- Native Sync/Reload continue to never resend/regenerate.

## Non-atomic batch recovery point — hybrid implementation

Known state before actual ref move:

- base `main@34811877896ca88c6656be6676f5466a19931ce6`;
- PR #29 open + mergeable;
- exact legitimate b42 source/Artifact remain `e8946e48a0b5ad86b402faf5eabba627e3393adf` / `9709824510`;
- accidental Artifact `9710515489` is permanently rejected as identity-invalid;
- no peer Active dev task;
- exact final b43 atomic publication commit is `aac437ae616156dfe3657caeecc8e1e90ad86434`.

Batches:

- **Batch A complete**: Option 2 selection + hard UX requirements recorded.
- **Batch B complete**: minimal user-visible resident/reusable Web surface + Settings entry written; exact net diff audited to two files.
- **Batch C final ref move pending**: move branch exactly once to `aac437ae616156dfe3657caeecc8e1e90ad86434`, then verify resulting b43 push/PR CI and package identity.
- **Batch D pending**: verify exact valid b43 Artifact/IPA identity and hand IPA to user for real-device hybrid smoothness/attachment-entry test.
- **Batch E pending**: record actual CI/Artifact/Runtime evidence and update durable docs/PR body.

Recovery rules:

- never reuse/rewrite b39-b42 identities/Artifacts;
- accidental Artifact `9710515489` remains rejected and must not be promoted;
- do not redefine exact legitimate b42 product source;
- do not weaken Stable b38 geometry/round/navigation contracts;
- do not force branch to any superseded unpublished preparation commit;
- do not merge PR #29 as production Send acceptance before exact hybrid Runtime evidence supports the claimed scope;
- do not implement unverified deep-link/file-input/DOM automation merely to accelerate the milestone.

## Next exact action

Move `dev/send-stream-20260829` to `aac437ae616156dfe3657caeecc8e1e90ad86434`, verify b43 push/PR CI and Artifact identity, then continue autonomously to the real-device gate.
