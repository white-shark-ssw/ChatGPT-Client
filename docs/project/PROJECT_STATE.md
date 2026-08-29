# Project State

_Last updated: 2026-08-29 through b43 exact-device hybrid-feasibility Runtime and valid b44 integrated-send CI/Artifact._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the current Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen; Frozen remains No for current native conversation modules.

## Current Phase 9 — DEV-send-stream

### Security boundary retained from b42

Exact b42 (`e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`) proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output: PoW, Turnstile and `so` required; non-empty PoW + Turnstile were finalized before Send.

Therefore pure-native/transient-auth ChatGPT-account Send remains blocked. Prohibited routes remain: solver/bypass, fingerprint replay, captured proof/token replay, guessed fallback endpoint, hidden/shadow challenge WebView, DOM message scraping or challenge harvesting.

### Product architecture — TD-024

User explicitly selected **native shell/read/navigation + user-visible official ChatGPT Web Send**.

- Native list/detail stays primary.
- `ConversationRepository` remains sole native conversation/read/recovery authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Visible Web owns only its displayed official browser interaction; it is not a second native conversation repository.

### b43 Runtime — visible-Web feasibility largely accepted

Exact b43 source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

User tested the requested sequence on the primary iPhone/iOS17 device and reported **“基本上没什么问题”**:

- entry/re-entry, keyboard/typing, visible Web Send, stream scrolling, rapid scrolling and native return had no material problem reported;
- Web `+` -> picker was about **100–200 ms**, not rejected as excessive.

Limitation: Web photo selection filtered videos out of the Photos picker.

Verified platform boundary: public `WKUIDelegate.runOpenPanelWith...` customization is iOS 18.4+, not iOS17. Therefore b44 does not fake a video fix with private API or DOM/file-input injection. Native iOS17 video-selection/upload needs separately evidenced attachment transfer/handoff work. Current ChatGPT image-input documentation establishes static image input, not video processing support.

### Current exact b44 Candidate — integrated native-conversation Send trial

- **Candidate**: `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.
- **Exact product/config source**: `f1503cf7121512a84e5c55a3642181c17324d791`.
- **Push Run / Job**: `33245105815` / `99081114295` — success.
- **PR Run**: `33245107290` — success.
- **Artifact**: `9712583513`.
- **ZIP digest**: `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- **IPA**: `ChatGPTClient-0.1.0-b44-dev-send-stream.ipa`.
- **IPA SHA**: `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- **Independent package identity**: `0.1.0 (44)`, Candidate b44, source `f1503cf71215`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.
- **Evidence level**: Code / CI / Artifact / package identity passed. **Runtime pending; Stable/Frozen No.**

b44 product behavior:

- native detail now owns a bottom `发送消息…` affordance through Root-owned navigation;
- selected native conversation prepares the shared visible Web surface for trial route `https://chatgpt.com/c/<conversation-id>`;
- Web diagnostics report only route class / target-match / timings, never raw conversation ID/body/secrets;
- explicit `返回并同步` triggers exactly one existing `ConversationRepository.syncLatestMessages(id:)` and re-renders selected native detail on success;
- ordinary Back does not auto-Sync;
- standalone ordinary Settings hybrid-chat entry was removed; diagnostic Send probe remains;
- `ConversationFeature.swift` and Stable b38 deterministic long-message geometry are unchanged.

### b44 Runtime gate

Exact iPhone/iOS17 must establish:

1. native selected conversation -> `发送消息…` -> same Web conversation;
2. text Send and stream smoothness remains at least b43 quality;
3. explicit `返回并同步` reconciles exactly once into native detail;
4. ordinary Back does not Sync;
5. A/B native selection targets the correct A/B Web conversation;
6. resident same-target re-entry avoids unnecessary reload;
7. Web `+` remains acceptably responsive; **video filtering remains a known non-fixed iOS17 limitation**;
8. no regression to b38 native long-conversation/round-navigation behavior.

PR #29 remains open and must not be merged as accepted integrated Send before this Runtime gate passes.

## Candidate identity incident retained

Artifact `9710515489` was accidentally emitted with newer hybrid code under stale b42 identity. It is permanently rejected and must never be installed/promoted. Legitimate b42 remains Artifact `9709824510`.

## Authority / evidence rule

- UI text/title is never identity authority.
- Native Sync/Reload never resend/regenerate.
- CI/Artifact success is not Runtime proof.
- b39-b44 identities are permanently reserved once emitted; any corrected b44 product code must use b45+.
- iOS17 evidence does not prove lower iOS or iPad; non-personal workspace/account-switch and native attachment handoff remain Unknown/Unverified where not explicitly tested.
